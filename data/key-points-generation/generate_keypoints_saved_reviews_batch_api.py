from __future__ import annotations
import argparse
import os
from pathlib import Path
import re
from datetime import datetime
import json

parser = argparse.ArgumentParser(description="Generate key points for saved review text files.")
parser.add_argument("--root", type=str, required=True, help="Root directory containing review .txt files")
parser.add_argument("--model_name", default="gpt-5-mini", help="OpenAI model name")
parser.add_argument("--overwrite", action="store_true", help="Regenerate even if _keypoints file exists")
parser.add_argument("--batch_file_path", type=str, required=True, help="Path to save the batch API request file")

args = parser.parse_args()


PROMPT_TEMPLATE = (
    "You are given a review written by a reviewer of an AI conference. You need to give the key points discussed in the review as a one or two liner for each point. Write only the key points.\nReview: {review}"
)

def find_review_files(root):
    return [str(p) for p in Path(root).rglob("*.txt") if not p.name.endswith("_keypoints.txt") and re.search(rf".*/(train|test|dev)/(.*)/(level[1-4]|reviews|references)/.*", str(p)) is not None]


def needs_processing(review_path, overwrite):

    # first make sure the .txt file in question is a review and not something else like subset summary or subset pathfiles
    if "NOPDF" not in str(review_path):
        return False
    if "prompt.txt" in str(review_path):
        return False
    review_filepath_pattern = rf".*/(train|test|dev)/(.*)/(level[1-4]|reviews|references)/.*"
    match = re.search(review_filepath_pattern, str(review_path))

    if match is None:
        return False

    target = review_path.replace('.txt', '_keypoints.txt')
    
    if os.path.exists(target) and os.path.getsize(target) > 0 and not overwrite:
        return False
    else:
        return True


def make_prompt(review_text):
    return PROMPT_TEMPLATE.format(review=review_text.strip())

def process_single(review_path, model_name, overwrite):
    '''
    returns the batch entry
    '''
    
    if not needs_processing(review_path, overwrite):
        return None
    
    with open(review_path, 'r') as fin:
        text = fin.read().strip()

    if not text:
        print(f"[SKIP] Empty review: {review_path}")
        return None
    
    target_path = review_path.replace('.txt', '_keypoints.txt')
    prompt = make_prompt(text)

    batch_file_entry = {
        "custom_id": f"{target_path}::{datetime.now().strftime('%Y%m%d%H%M%S')}", 
        "method": "POST", 
        "url": "/v1/chat/completions", 
        "body": {
            "model": model_name, 
            "messages": [
                {"role": "user", "content": prompt},
            ],
        }
    }

    return batch_file_entry

review_files = find_review_files(args.root)

print(f"Discovered {len(review_files)} candidate review files under {args.root}")

batch_entries = []

for rf in review_files:
    entry = process_single(rf, args.model_name, args.overwrite)
    if entry is not None:
        batch_entries.append(entry)

with open(args.batch_file_path, 'w') as fout:
    for entry in batch_entries:
        fout.write(json.dumps(entry) + '\n')

print(f"Batch file created at {args.batch_file_path} with {len(batch_entries)} entries.")