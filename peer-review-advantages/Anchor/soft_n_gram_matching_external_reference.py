import os
import json
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import argparse
from pathlib import Path
from datetime import datetime

from tqdm import tqdm

def log_command():
    import sys, os
    cmd = f"CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES', '<not set>')} " \
          + " ".join(["python"] + sys.argv)
    print(">>> Command executed:\n", cmd, "\n")
    return cmd

parser = argparse.ArgumentParser()
parser.add_argument("--embedding_model", type=str, default="linq-embed-mistral")
parser.add_argument("--cache_dir", type=str, default="/data/assets/hub")
parser.add_argument("--similarity_threshold", type=str, help="float or comma separated list of floats")
parser.add_argument("--min_n", type=int, default=3)
parser.add_argument("--max_n", type=int, default=10)
parser.add_argument("--batch_size", type=int, required=True)
parser.add_argument("--all_files_path", type=str, required=True)
parser.add_argument("--dataset_subset_path", type=str, required=True)
parser.add_argument("--verbose", action='store_true', default=False)
parser.add_argument("--out_suffix", type=str, required=True)
parser.add_argument("--dry_run", action='store_true', default=False)
args = parser.parse_args()


if ',' in args.similarity_threshold:
    similarity_threshold = [float(x) for x in args.similarity_threshold.split(',')]
else:
    similarity_threshold = float(args.similarity_threshold)

def extract_paper_fp_from_review_fp(review_filepath):
    ## extract the paper contents 
    if '_fragment_' in review_filepath:
        review_filepath = review_filepath.split('_fragment_')[0]
        
    # pattern = r".*cleandata/(.*)/(train|test|dev)/.*(level[1-4]|reviews)/(.*)_([1-9]*).txt"
    pattern = "SO THAT NOTHING MATCHES THIS"
    match = re.search(pattern, review_filepath)
    
    if match is not None:
        conference = match.group(1)
        split = match.group(2)
        level = match.group(3)
        paper_number = match.group(4)
        reviewer_number = match.group(5)

        # return conference, split, level, paper_number, reviewer_number
        generating_model = "OLD PARSER FUNCTION: GENRATING MODEL NOT PARSED"
        prompt = f"{level}@NAV" if level != "reviews" else "DIVINE BENEVOLENCE"

    else:
        pattern = r".*hard-subset/(.*)/(train|test|dev)/(.*)/(level[1-4]|reviews)/(.*).txt"
        match = re.search(pattern, review_filepath)

        conference = match.group(1)
        split = match.group(2)
        paper_number = match.group(3)
        level = match.group(4)

        if '/' in match.group(5):
            generating_model = match.group(5).split('/')[0]
            fileid = match.group(5).split('/')[1]
        else:
            generating_model = "human_review"
            fileid = match.group(5)

        if ":::" in fileid:
            reviewer_number = fileid.split(":::")[-1]
            prompt = fileid.split(":::")[0]
        else:
            reviewer_number = fileid
            if level != "reviews":
                prompt = f"{level}@NAV"
            else:
                prompt = "DIVINE BENEVOLENCE"

    return conference, split, level, paper_number, reviewer_number

def get_ref_filenames(conference, split, paper_number, ref_ai=True):
    def check(s):
        if any(substring in s for substring in ['gemini', 'BALANCED', 'CONSERVATIVE', 'INNOVATIVE', 'NITPICKY', 'P4']):
            return False
        return True
    if ref_ai:
        reference_dirpath = Path(os.path.join(args.dataset_subset_path, f"{conference}/{split}/{paper_number}/references/"))
        return sorted(list([str(x) for x in reference_dirpath.rglob("*_reference_review.txt") if check(str(x))]))
    else:
        # this is probably never going to be used in the program, just there for legacy reasons
        ref_list = []
        for i in range(20):
            filepath = f"/home/naveeja/Project/Human_or_AI/Data_Preprocessing/cleandata/{conference}/{split}/reviews/{paper_number}_{i+1}.txt"
            ref_list.append(filepath)
        return ref_list

def get_review_filepath_new(old_filepath):
    '''
    Note that old filepaths are applicable only for reviews in the dataset, not reference reviews because they are always inside the dataset_subset_path
    '''
    conference, split, level, paper_number, reviewer_number = extract_paper_fp_from_review_fp(old_filepath)
    if "gpt_4o_latest" in old_filepath:
        author = "gpt_4o_latest"
    elif "meta-llama-Llama-3.3-70B-Instruct" in old_filepath:
        author = "meta-llama-Llama-3.3-70B-Instruct"
    elif "/reviews/" in old_filepath:
        author = "reviews"

    new_filepath = os.path.join(args.dataset_subset_path, f"{conference}/{split}/{paper_number}/{level}/{author if author !='reviews' else ''}/{reviewer_number}.txt")

    return new_filepath


embedding_model = args.embedding_model
out_dir = f"results/soft-n-gram-similarity/{args.dataset_subset_path.split('/')[-1]}/{embedding_model}/"
os.makedirs(out_dir, exist_ok=True)
cache_dir = args.cache_dir
output_filepath = f"results/soft-n-gram-similarity/{args.dataset_subset_path.split('/')[-1]}/{embedding_model}/result_anchor_features_{args.out_suffix}_{args.min_n}_{args.max_n}.json"
all_files_path = args.all_files_path

print(output_filepath)

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
log_command()

if embedding_model == "text-embedding-3-small" or embedding_model == "text-embedding-3-large":
    if not args.dry_run:
        openai_key = os.getenv("OPENAI_API_KEY")
        client = OpenAI(api_key=openai_key)

elif embedding_model == "specter2":
    
    from transformers import AutoTokenizer
    from adapters import AutoAdapterModel
    import torch

    tokenizer = AutoTokenizer.from_pretrained('allenai/specter2_base', cache_dir=cache_dir)
    model = AutoAdapterModel.from_pretrained('allenai/specter2_base', cache_dir=cache_dir)
    model.load_adapter("allenai/specter2", source="hf", load_as="specter2", set_active=True)
    model = model.to("cuda:0")
    max_length = 512

elif embedding_model == "linq-embed-mistral":
    import torch
    import torch.nn.functional as F
    from torch import Tensor
    from transformers import AutoTokenizer, AutoModel, BitsAndBytesConfig

    def last_token_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
        left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
        if left_padding:
            return last_hidden_states[:, -1]
        else:
            sequence_lengths = attention_mask.sum(dim=1) - 1
            batch_size = last_hidden_states.shape[0]
            return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]
        
    bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,                # enable 4-bit quantization
            bnb_4bit_use_double_quant=True,   # nested quantization for memory saving
            bnb_4bit_quant_type="nf4",        # NormalFloat4 (best quality)
            bnb_4bit_compute_dtype="bfloat16" # computation dtype (fp16 also works if bf16 not available)
        )
        
    tokenizer = AutoTokenizer.from_pretrained(
        'Linq-AI-Research/Linq-Embed-Mistral', 
        cache_dir=cache_dir
    )
    model = AutoModel.from_pretrained(
        'Linq-AI-Research/Linq-Embed-Mistral', 
        quantization_config=bnb_config,
        cache_dir=cache_dir).to("cuda:0")
    max_length = 4096

else:
    raise ValueError("Embedding model not implemented")

def embed_text_single_pass(texts):

    review_contents = texts
    if embedding_model == "text-embedding-3-small" or embedding_model == "text-embedding-3-large":
        # print("burning credits")
        response = client.embeddings.create(
            model=embedding_model,
            input=review_contents
        )

        review_embeddings = [item.embedding for item in response.data]
    elif embedding_model == "specter2":
        text_batch = review_contents
        inputs = tokenizer(
            text_batch, 
            padding=True, 
            truncation=True,
            return_tensors="pt", 
            return_token_type_ids=False, 
            max_length=512
        ).to("cuda:0")
        output = model(**inputs)
        embeddings = output.last_hidden_state[:, 0, :]
        review_embeddings = embeddings.detach().cpu().numpy().tolist()
    elif embedding_model == "linq-embed-mistral":
        input_texts = review_contents
        batch_dict = tokenizer(input_texts, max_length=max_length, padding=True, truncation=True, return_tensors="pt").to("cuda:0")
        if args.verbose:
            print(batch_dict['input_ids'].shape)
        outputs = model(**batch_dict)
        embeddings = last_token_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

        # Normalize embeddings
        embeddings = F.normalize(embeddings, p=2, dim=1)
        review_embeddings = embeddings.detach().cpu().numpy().tolist()
        
    return review_embeddings

def embed_texts(texts, batch_size=16):
    if args.dry_run:
        return [[0.1]*2 for _ in texts]  # assuming embedding size of 20 for dry run
    multi_pass_embeddings = []
    i = 0
    while i < len(texts):
        cur_batch_size = batch_size

        if embedding_model == "linq-embed-mistral" or embedding_model == "specter2":
            token_limit = 7000 if embedding_model == "linq-embed-mistral" else 16000
            while True:
                batch_texts = texts[i:i+cur_batch_size]
                tokenized_batch_input_ids = tokenizer(batch_texts, max_length=max_length, padding=True, truncation=True, return_tensors="pt")['input_ids']

                batch_shape = tokenized_batch_input_ids.shape
                if batch_shape[0] * batch_shape[1] > token_limit:
                    cur_batch_size = int(cur_batch_size * 0.95)
                    # print(f"Reducing batch size to {cur_batch_size}")
                else:
                    # print(f"Operating at batch size {cur_batch_size}")
                    batch_texts = texts[i:i+cur_batch_size]
                    break
        else:
            batch_texts = texts[i:i+cur_batch_size]

        batch_embeddings = embed_text_single_pass(batch_texts)
        multi_pass_embeddings.extend(batch_embeddings)

        if i % (5 * batch_size) == 0:
            if embedding_model == "linq-embed-mistral" or embedding_model == "specter2":
                # print("Emptying CUDA cache...")
                torch.cuda.empty_cache()

        i += cur_batch_size

    assert len(multi_pass_embeddings) == len(texts)

    return multi_pass_embeddings

def get_overlapping_phrases(text_filepath: str, min_n: int, max_n: int) -> list[str]:
    """Generates all overlapping phrases of specified lengths from a text."""
    text = open(text_filepath, "r").read().strip()
    words = text.split()
    phrases = []
    # Ensure min_n and max_n are within the bounds of the text length
    min_n = min(min_n, len(words))
    max_n = min(max_n, len(words))
    
    for n in range(min_n, max_n + 1):
        # for i in range(len(words) - n + 1):
        #     phrases.append(" ".join(words[i:i+n]))
        start_idx = 0
        while start_idx + n <= len(words):
            phrases.append(" ".join(words[start_idx:start_idx + n]))
            start_idx += (n // 4)  # 25% overlap
    return phrases
    
def compute_soft_n_gram_matching_from_similarity_matrix(
    similarity_matrix,
    similarity_threshold # let this threshold be a float or a list of floats, if a single float return the similarity score, if a list of floats return a dict of similarity where key is the threshold and value is the similarity score
):
    if isinstance(similarity_threshold, list):
        scores = dict()
        for threshold in similarity_threshold:
            matched_phrase_count = 0
            for i in range(similarity_matrix.shape[0]):
                if np.any(similarity_matrix[i, :] > threshold): # Check if any similarity value in the row is above the threshold
                    matched_phrase_count += 1

            total_edited_phrases = similarity_matrix.shape[0]
            score = matched_phrase_count / total_edited_phrases if total_edited_phrases > 0 else 0.0
            scores[threshold] = score
        return scores
    
    elif isinstance(similarity_threshold, float):
        matched_phrase_count = 0
        for i in range(similarity_matrix.shape[0]):
            if np.any(similarity_matrix[i, :] > similarity_threshold): # Check if any similarity value in the row is above the threshold
                matched_phrase_count += 1
                

        total_edited_phrases = similarity_matrix.shape[0]
        score = matched_phrase_count / total_edited_phrases if total_edited_phrases > 0 else 0.0

        return score
    
    else:
        raise ValueError("similarity_threshold must be a float or a list of floats")
    
def get_ref_metadata_from_new_filepath(ref_review_filepath):
    '''
    Expects new filepath, ofc because all reference reviews are inside dataset_subset_path
    '''
    generating_model = ref_review_filepath.split('/')[-2]
    generation_id = ref_review_filepath.split('/')[-1].replace('_reference_review.txt', '')
    return generating_model, generation_id

with open(all_files_path, "r") as fin:
    all_review_filepaths = [line.strip() for line in fin.readlines()]
    

anchor_features = dict()

'''
Exploiting the fact that reviews of the same paper are contiguous in all_review_filepaths, bucket same paper reviews, we can speed up computations by doing some preprocessing over each bucket
'''
head = -1
tail = 0
papers_set = dict()
curr_paper_hash = ''

def construct_paper_hash(review_filepath):
    '''
    always expects old review filepath
    '''
    conference, split, level, paper_number, reviewer_number = extract_paper_fp_from_review_fp(review_filepath)
    paper_hash = f"{conference}::{split}::{paper_number}"
    return paper_hash

while tail < len(all_review_filepaths):
    while head + 1 < len(all_review_filepaths) and (curr_paper_hash == '' or construct_paper_hash(all_review_filepaths[head + 1]) == curr_paper_hash):
        head += 1
        curr_paper_hash = construct_paper_hash(all_review_filepaths[head])

    # reviews from tail to head inclusive belong to the same paper
    if '::dev::' not in curr_paper_hash:
        # currently ignoring the papers in dev split
        papers_set[curr_paper_hash] = all_review_filepaths[tail:head+1]

    # reset the window
    tail = head + 1
    head = tail - 1
    curr_paper_hash = ''

print(f"Found {len(papers_set)} unique papers")

total_words = 0

for idx, (key, val) in enumerate(tqdm(papers_set.items())):

    current_review_filepaths_old = val

    # current_review_filepaths_new = [get_review_filepath_new(x) for x in current_review_filepaths_old]
    current_review_filepaths_new = current_review_filepaths_old # assuming all files are already in new filepath format

    conference, split, paper_number = key.split("::")[0], key.split("::")[1], key.split("::")[2]
        
    ai_reference_filepaths_new = get_ref_filenames(conference, split, paper_number, ref_ai=True)

    all_review_phrases = []
    review_phrase_boundaries = dict()
    for review_filepath_old in current_review_filepaths_old:
        this_review_phrases = get_overlapping_phrases(review_filepath_old, args.min_n, args.max_n) # terrible variable naming
        num_phrases = len(this_review_phrases)
        review_phrase_boundaries[review_filepath_old] = (len(all_review_phrases), len(all_review_phrases) + num_phrases)
        all_review_phrases.extend(this_review_phrases)

    # if args.verbose:
    #     print("review phrase boundaries", review_phrase_boundaries)

    all_reference_phrases = []
    reference_phrase_boundaries = dict()
    for ref_filepath_new in ai_reference_filepaths_new:
        this_ref_phrases = get_overlapping_phrases(ref_filepath_new, args.min_n, args.max_n)
        num_phrases = len(this_ref_phrases)
        reference_phrase_boundaries[ref_filepath_new] = (len(all_reference_phrases), len(all_reference_phrases) + num_phrases)
        all_reference_phrases.extend(this_ref_phrases)

    # if args.verbose:
    #     print("reference phrase boundaries", reference_phrase_boundaries)

    # with every phrase collected together, we can compute embeddings in one go, letting the utility function handle optimum batching

    if args.verbose:
        print(len(all_review_phrases), len(all_reference_phrases))


    all_review_phrase_embeddings = embed_texts(all_review_phrases, batch_size=args.batch_size)
    all_reference_phrase_embeddings = embed_texts(all_reference_phrases, batch_size=args.batch_size)

    total_words += sum(len(phrase.split()) for phrase in all_review_phrases) + sum(len(phrase.split()) for phrase in all_reference_phrases)

    if args.verbose:
        print(len(all_review_phrase_embeddings), len(all_reference_phrase_embeddings))

    if not args.dry_run:
        similarity_matrix = cosine_similarity(all_review_phrase_embeddings, all_reference_phrase_embeddings)
    else:
        similarity_matrix = np.random.rand(len(all_review_phrase_embeddings), len(all_reference_phrase_embeddings))

    # now you can just slice the similarity matrix by boundaries to get individual review-reference similarity matrices

    for review_filepath_old, (start, end) in review_phrase_boundaries.items():
        anchor_features[review_filepath_old] = dict()
        for ref_filepath_new, (ref_start, ref_end) in reference_phrase_boundaries.items():
            similarity_slice = similarity_matrix[start:end, ref_start:ref_end]

            if not args.dry_run:
                score = compute_soft_n_gram_matching_from_similarity_matrix(
                    similarity_slice,
                    similarity_threshold
                )
            else:
                score = 0
            ref_generating_model, ref_generation_id = get_ref_metadata_from_new_filepath(ref_filepath_new)
            anchor_features[review_filepath_old][f"{ref_generation_id}@{ref_generating_model}"] = score
    
    if idx % 5 == 0: # dump results every 5 papers
        with open(output_filepath, "w") as fout:
            json.dump(anchor_features, fout, indent=4)


with open(output_filepath, "w") as fout:
    json.dump(anchor_features, fout, indent=4)

print(f"Total words processed: {total_words}")