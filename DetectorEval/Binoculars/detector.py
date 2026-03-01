from typing import Union

import os
import numpy as np
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

from utils import assert_tokenizer_consistency
from metrics import perplexity, entropy

torch.set_grad_enabled(False)

huggingface_config = {
    # Only required for private models from Huggingface (e.g. LLaMA models)
    "TOKEN": os.environ.get("HF_TOKEN", None)
}

# selected using Falcon-7B and Falcon-7B-Instruct at bfloat16
BINOCULARS_ACCURACY_THRESHOLD = 0.9015310749276843  # optimized for f1-score
BINOCULARS_FPR_THRESHOLD = 0.8536432310785527  # optimized for low-fpr [chosen at 0.01%]

# predefined models
model_fullnames = { 
                    'llama3-8b': 'meta-llama/Meta-Llama-3.1-8B',
                    'llama3-8b-instruct': 'meta-llama/Meta-Llama-3.1-8B-Instruct',
                    'falcon-7b': 'tiiuae/falcon-7b',
                    'falcon-7b-instruct': 'tiiuae/falcon-7b-instruct',
                    }

DEVICE_1 = "cuda:0" if torch.cuda.is_available() else "cpu"
DEVICE_2 = "cuda:1" if torch.cuda.device_count() > 1 else DEVICE_1


class Binoculars(object):
    def __init__(self,
                 observer_name: str = "falcon-7b",
                 performer_name: str = "falcon-7b-instruct",
                 use_bfloat16: bool = True,
                 max_token_observed: int = 512,
                 mode: str = "low-fpr",
                 ) -> None:
        
        observer_name_or_path = model_fullnames.get(observer_name, observer_name)
        performer_name_or_path = model_fullnames.get(performer_name, performer_name)
        assert_tokenizer_consistency(observer_name_or_path, performer_name_or_path)
        self.change_mode(mode)
        
        self.observer_model = AutoModelForCausalLM.from_pretrained(observer_name_or_path,
                                                                   device_map={"": DEVICE_1},
                                                                   trust_remote_code=True,
                                                                   torch_dtype=torch.bfloat16 if use_bfloat16
                                                                   else torch.float32,
                                                                   token=huggingface_config["TOKEN"]
                                                                   )
        self.performer_model = AutoModelForCausalLM.from_pretrained(performer_name_or_path,
                                                                    device_map={"": DEVICE_2},
                                                                    trust_remote_code=True,
                                                                    torch_dtype=torch.bfloat16 if use_bfloat16
                                                                    else torch.float32,
                                                                    token=huggingface_config["TOKEN"]
                                                                    )
        self.observer_model.eval()
        self.performer_model.eval()

        self.tokenizer = AutoTokenizer.from_pretrained(observer_name_or_path)
        if not self.tokenizer.pad_token:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.max_token_observed = max_token_observed

    def change_mode(self, mode: str) -> None:
        if mode == "low-fpr":
            self.threshold = BINOCULARS_FPR_THRESHOLD
        elif mode == "accuracy":
            self.threshold = BINOCULARS_ACCURACY_THRESHOLD
        else:
            raise ValueError(f"Invalid mode: {mode}")

    def _tokenize(self, batch: list[str]) -> transformers.BatchEncoding:
        batch_size = len(batch)
        encodings = self.tokenizer(
            batch,
            return_tensors="pt",
            padding="longest" if batch_size > 1 else False,
            truncation=True,
            max_length=self.max_token_observed,
            return_token_type_ids=False).to(self.observer_model.device)
        return encodings
    
    # This function is used to tokenize the context and review separately
    def _tokenize_with_context(self, context: str, review: str):
        # Tokenise context
        context_ids = self.tokenizer(
            context,
            return_tensors="pt",
            truncation=True,
            max_length=self.max_token_observed // 2,
            add_special_tokens=False
        )
        # Tokenise review
        review_ids = self.tokenizer(
            review,
            return_tensors="pt",
            truncation=True,
            max_length=self.max_token_observed // 2,
            add_special_tokens=False
        )
        # Concatenate context and review
        input_ids = torch.cat(
            [context_ids.input_ids, review_ids.input_ids], dim=1
        )
        # Attention Mask - 1 for all tokens
        attention_mask = torch.ones_like(input_ids)
        # Loss Mask: 0 for context, 1 for review
        loss_mask = torch.cat(
            [
                torch.zeros_like(context_ids.input_ids),
                torch.ones_like(review_ids.input_ids)
            ],
            dim=1
        )
        return transformers.BatchEncoding({
            "input_ids": input_ids.to(self.observer_model.device),
            "attention_mask": attention_mask.to(self.observer_model.device),
            "loss_mask": loss_mask.to(self.observer_model.device),
        })


    @torch.inference_mode()
    def _get_logits(self, encodings: transformers.BatchEncoding):
        input_ids_1 = encodings["input_ids"].to(DEVICE_1)
        attention_mask_1 = encodings["attention_mask"].to(DEVICE_1)
        input_ids_2 = encodings["input_ids"].to(DEVICE_2)
        attention_mask_2 = encodings["attention_mask"].to(DEVICE_2)
        observer_logits = self.observer_model(input_ids=input_ids_1, attention_mask=attention_mask_1).logits
        performer_logits = self.performer_model(input_ids=input_ids_2, attention_mask=attention_mask_2).logits
        if DEVICE_1 != "cpu":
            torch.cuda.synchronize()
        return observer_logits, performer_logits


    def compute_score(self, input_text: Union[list[str], str]) -> Union[float, list[float]]:
        batch = [input_text] if isinstance(input_text, str) else input_text
        encodings = self._tokenize(batch)
        observer_logits, performer_logits = self._get_logits(encodings)
        ppl = perplexity(encodings, performer_logits)
        x_ppl = entropy(observer_logits.to(DEVICE_1), performer_logits.to(DEVICE_1),
                        encodings.to(DEVICE_1), self.tokenizer.pad_token_id)
        binoculars_scores = ppl / x_ppl
        binoculars_scores = binoculars_scores.tolist()
        return binoculars_scores[0] if isinstance(input_text, str) else binoculars_scores
    
    def compute_score_with_context(self, review_text, context_text):
        encodings = self._tokenize_with_context(context_text, review_text)
        observer_logits, performer_logits = self._get_logits(encodings)
        ppl = perplexity(encodings, performer_logits,
            loss_mask=encodings["loss_mask"])
        x_ppl = entropy(observer_logits.to(DEVICE_1), performer_logits.to(DEVICE_1),
            encodings.to(DEVICE_1), self.tokenizer.pad_token_id,
            loss_mask=encodings["loss_mask"])
        binoculars_scores = ppl / x_ppl
        binoculars_scores = binoculars_scores.tolist()
        return binoculars_scores[0]

    def predict(self, input_text: Union[list[str], str]) -> Union[list[str], str]:
        binoculars_scores = np.array(self.compute_score(input_text))
        pred = np.where(binoculars_scores < self.threshold,
                        "Most likely AI-generated",
                        "Most likely human-generated"
                        ).tolist()
        return pred
    
    def predict_with_context(self, review_text, context_text):
        binoculars_scores = self.compute_score_with_context(review_text, context_text)
        pred = np.where(binoculars_scores < self.threshold,
                        "Most likely AI-generated",
                        "Most likely human-generated"
                        ).tolist()
        return pred