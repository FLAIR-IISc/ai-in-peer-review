import os
import random
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, classification_report
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    get_linear_schedule_with_warmup,
)
from torch.optim import AdamW
from tqdm import tqdm
import warnings
import time
import copy
import re
from collections import Counter
warnings.filterwarnings('ignore')
import argparse

parser = argparse.ArgumentParser(description="Train a BERT-based classifier on review segments.")
parser.add_argument("--leave_model", type=str, default=None)
parser.add_argument("--source_csv", type=str, required=True, help="Path to the CSV file containing the data.")

args = parser.parse_args()



MODEL_NAME = "roberta-base"  
MAX_LENGTH = 512         
BATCH_SIZE = 96
EPOCHS = 3
LR = 2e-5
WEIGHT_DECAY = 0.01
RANDOM_SEED = 42
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
BINARY = False
OUTPUT_DIR = f"./roberta_base_classifier_{'binary' if BINARY else 'multi'}_{args.leave_model if args.leave_model else 'easy-all-ex'}_data"
PRIORITY = ["HUMAN", "AI"] # majority voting priority order, so if there are equal number of ai and human segments, choose HUMAN

def majority_vote(preds):
    counts = Counter(preds)
    max_count = max(counts.values())
    tied = [k for k, v in counts.items() if v == max_count]
    for p in PRIORITY:
        if p in tied:
            return p

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

set_seed(RANDOM_SEED)


def prepare_label_mapping(df):
    unique = sorted(["level1", "level2", "level3", "level4", "reviews"] if not BINARY else ["AI", "HUMAN"])
    label2id = {lbl: i for i, lbl in enumerate(unique)}
    id2label = {i: lbl for lbl, i in label2id.items()}
    return label2id, id2label, 5 if not BINARY else 2

class BertDataset(Dataset):
    def __init__(self, source_ids, texts, labels, tokenizer, max_length):
        self.source_ids = source_ids
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = str(self.texts[idx])
        label = int(self.labels[idx])

        encoding = self.tokenizer(
            text,
            truncation=True,
            max_length=self.max_length,
            return_attention_mask=True,
            padding=False,   # padding done by collator
        )

        return {
            "source_id": self.source_ids[idx],
            "input_ids": encoding["input_ids"],
            "attention_mask": encoding["attention_mask"],
            "labels": label,  # Keep as int, tensor conversion in collate
        }
    
def filter_examples(df, select_dict, unselect_dict):
    """
    Filter out examples whose 'id' contains the remove_keyword
    """
    filtered_df = copy.deepcopy(df)
    for col, keep_kw in select_dict.items():
        pattern = "|".join(map(re.escape, keep_kw))
        filtered_df = filtered_df[filtered_df[col].str.contains(pattern)]
    for col, remove_kw in unselect_dict.items():
        pattern = "|".join(map(re.escape, remove_kw))
        filtered_df = filtered_df[~filtered_df[col].str.contains(pattern)]
    return filtered_df

def build_components(df):

    if BINARY:
        df['label'] = df['label'].apply(lambda x: 'AI' if x in ['level1', 'level2', 'level3'] else 'HUMAN')

    label2id, id2label, num_labels = prepare_label_mapping(df)

    df = df.copy()
    df["label_id"] = df["label"].map(label2id)

    train_df = df[df['split'] == 'train']
    val_df = df[df['split'] == 'test']

    if args.leave_model is not None:
        select_dict = {
            "path": [args.leave_model, "/reviews/"]
        }
        unselect_dict = {
            "path": [args.leave_model]
        }

        train_df = filter_examples(train_df, {}, unselect_dict)
        val_df = filter_examples(val_df, select_dict, {})


    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    train_dataset = BertDataset(
        train_df["path"].tolist(),
        train_df["text"].tolist(),
        train_df["label_id"].tolist(),
        tokenizer,
        MAX_LENGTH,
    )

    val_dataset = BertDataset(
        val_df["path"].tolist(),
        val_df["text"].tolist(),
        val_df["label_id"].tolist(),
        tokenizer,
        MAX_LENGTH,
    )

    def bert_collate_fn(batch):
        """Custom collate function for BERT-style models"""
        global_attention_masks = []
        max_length = max(len(item['input_ids']) for item in batch)
        
        # Pre-allocate tensors for efficiency
        batch_size = len(batch)
        input_ids_batch = torch.full((batch_size, max_length), tokenizer.pad_token_id, dtype=torch.long)
        attention_mask_batch = torch.zeros((batch_size, max_length), dtype=torch.long)
        labels_batch = torch.zeros(batch_size, dtype=torch.long)
        
        for idx, item in enumerate(batch):
            seq_len = len(item['input_ids'])
            input_ids_batch[idx, :seq_len] = torch.tensor(item['input_ids'], dtype=torch.long)
            attention_mask_batch[idx, :seq_len] = torch.tensor(item['attention_mask'], dtype=torch.long)
            labels_batch[idx] = item['labels']
        
        return {
            'source_ids': [item['source_id'] for item in batch],
            'input_ids': input_ids_batch,
            'attention_mask': attention_mask_batch,
            'labels': labels_batch
        }
        

    train_loader = DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True, collate_fn=bert_collate_fn, num_workers=4, pin_memory=True
    )
    val_loader = DataLoader(
        val_dataset, batch_size=BATCH_SIZE*4, shuffle=False, collate_fn=bert_collate_fn, num_workers=4, pin_memory=True
    )

    try:
        model = AutoModelForSequenceClassification.from_pretrained(
            OUTPUT_DIR,
            num_labels=num_labels,
            id2label=id2label,
            label2id=label2id,
        )
        print(f"Loaded model from {OUTPUT_DIR}")
        training_required = False
    except Exception as e:
        print(e)
        print(f"Could not load model from {OUTPUT_DIR}, initializing new model.")
        training_required = True

        model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_NAME,
            num_labels=num_labels,
            id2label=id2label,
            label2id=label2id,
        )

    return model, tokenizer, train_loader, val_loader, label2id, id2label, training_required

def evaluate(model, dataloader):
    model.eval()
    preds, labels = [], []
    source_ids = []
    total_loss = 0.0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="Evaluating", leave=False):
            source_ids.extend(batch["source_ids"])
            batch = {k: v.to(DEVICE) for k, v in batch.items() if k != 'source_ids'}
            outputs = model(**batch)
            total_loss += outputs.loss.item()

            logits = outputs.logits
            pred = torch.argmax(logits, dim=-1)
            preds.extend(pred.cpu().tolist())
            labels.extend(batch["labels"].cpu().tolist())

    return total_loss / len(dataloader), preds, labels, source_ids


def train(model, train_loader, val_loader):
    model.to(DEVICE)

    optimizer = AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    total_steps = len(train_loader) * EPOCHS
    scheduler = get_linear_schedule_with_warmup(
        optimizer, int(0.1 * total_steps), total_steps
    )

    best_f1 = -1

    for epoch in range(1, EPOCHS + 1):
        model.train()
        running_loss = 0.0
        
        # Timing variables
        data_load_time = 0.0
        forward_time = 0.0
        backward_time = 0.0
        
        # Progress bar for training
        progress_bar = tqdm(train_loader, desc=f"Epoch {epoch}/{EPOCHS} [Training]", leave=True)
        
        for batch_idx, batch in enumerate(progress_bar):
            # Time data loading
            t_start = time.time()
            batch = {k: v.to(DEVICE)  for k, v in batch.items() if k != 'source_ids'}
            data_load_time += time.time() - t_start
            
            # Time forward pass
            t_start = time.time()
            outputs = model(**batch)
            loss = outputs.loss
            forward_time += time.time() - t_start

            # Time backward pass
            t_start = time.time()
            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            backward_time += time.time() - t_start

            running_loss += loss.item()
            
            # Update progress bar with current loss
            avg_loss = running_loss / (batch_idx + 1)
            progress_bar.set_postfix({'loss': f'{avg_loss:.4f}'})

        train_loss = running_loss / len(train_loader)
        print(f"Epoch {epoch}/{EPOCHS} | Train Loss: {train_loss:.4f}")
        print(f"  ├─ Data loading: {data_load_time:.2f}s ({data_load_time*100/(data_load_time+forward_time+backward_time):.1f}%)")
        print(f"  ├─ Forward pass: {forward_time:.2f}s ({forward_time*100/(data_load_time+forward_time+backward_time):.1f}%)")
        print(f"  └─ Backward pass: {backward_time:.2f}s ({backward_time*100/(data_load_time+forward_time+backward_time):.1f}%)")

        val_loss, preds, labels, _ = evaluate(model, val_loader)
        acc = accuracy_score(labels, preds)
        f1 = f1_score(labels, preds, average="weighted")

        print(f"Epoch {epoch}/{EPOCHS} | Val Loss: {val_loss:.4f} | Acc: {acc:.4f} | F1: {f1:.4f}")

        if f1 > best_f1:
            best_f1 = f1
            model.save_pretrained(OUTPUT_DIR)
            print(f"Saved best model to {OUTPUT_DIR} (F1={best_f1:.4f})")
        print()

def run_training(df):
    model, tokenizer, train_loader, val_loader, label2id, id2label, training_required = build_components(df)
    print(f"Training {MODEL_NAME} (num_labels = {len(label2id)})")
    if training_required:
        train(model, train_loader, val_loader)
    else:
        model.to(DEVICE)

    print(f"\nFinal Evaluation: LEAVE MODEL {args.leave_model if args.leave_model else 'NONE'}")
    val_loss, preds, labels, source_ids = evaluate(model, val_loader)

    print("Loss:", val_loss)
    print("Accuracy:", accuracy_score(labels, preds))
    print("Weighted F1:", f1_score(labels, preds, average="weighted"))
    print("\nClassification Report:")
    print(classification_report(labels, preds, target_names=list(label2id.keys())))

    preds = [id2label[p] for p in preds]
    labels = [id2label[l] for l in labels]

    rev2info = dict()

    for id, label, pred in zip(source_ids, labels, preds):
        rev = id.split('_fragment_')[0] if '_fragment_' in id else id
        if rev not in rev2info:
            rev2info[rev] = dict()
            rev2info[rev]["predictions"] = []
        rev2info[rev]["true_label"] = label

        binary_pred = 'AI' if pred in ['level1', 'level2', 'level3'] else 'HUMAN' if not BINARY else pred

        rev2info[rev]["predictions"].append(binary_pred)

    # do a majority vote over the predictions for each review
    for rev in rev2info.keys():
        rev2info[rev]["final_prediction"] = majority_vote(rev2info[rev]["predictions"])

    y_test_temp = []
    test_preds_temp = []

    for rev in rev2info.keys():
        y_test_temp.append(rev2info[rev]["true_label"])
        test_preds_temp.append(rev2info[rev]["final_prediction"])

    labels = y_test_temp
    preds = test_preds_temp

    results_dict = {label: [] for label in label2id.keys()}

    for pred, true in zip(preds, labels):
        if pred == 'AI':
            results_dict[true].append(1)
        else:
            results_dict[true].append(0)
        
    for level in results_dict.keys():
        if len(results_dict[level]) > 0:
            print(f"{level}: {np.mean(results_dict[level])}")

    return model, tokenizer

df = pd.read_csv(args.source_csv)

run_training(df)

