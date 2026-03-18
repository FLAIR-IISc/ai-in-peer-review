'''
as of its creation this script is no different than a similar script in reference generation folder
'''

from openai import OpenAI
import json
import os
import argparse
import tqdm
import time

'''
MAKE SURE TO MODIFY THE DESCRIPTION IN METADATA, for instance the reference generation job of the 3743 subset was submitted with an older description, although this does not affect the generation, you never know if you would need to look at the metadata later!
'''

parser = argparse.ArgumentParser()
parser.add_argument("--batch_file_path", type=str, required=True, help="path to batch file")

args = parser.parse_args()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

batch_input_file = client.files.create(
    file=open(args.batch_file_path, "rb"),
    purpose="batch"
)

print("BATCH INPUT FILE: ", batch_input_file)

batch_input_file_id = batch_input_file.id
batch__ = client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
        "description": "hard-subset gpt-5-mini keypoint generation 26.10.25",
    }
)

print("BATCH: ", batch__)

print("Batch ID:", batch__.id)

'''
3743 subset gpt-5-mini keypoint generation 26.10.25:
BATCH INPUT FILE:  FileObject(id='file-5diPjgw6dF2MwBAJvJ9WBn', bytes=31585549, created_at=1761501233, filename='openai_keypoints_batch.jsonl', object='file', purpose='batch', status='processed', expires_at=1764093233, status_details=None)
BATCH:  Batch(id='batch_68fe6035f77c8190aec4c0bb748c674e', completion_window='24h', created_at=1761501237, endpoint='/v1/chat/completions', input_file_id='file-5diPjgw6dF2MwBAJvJ9WBn', object='batch', status='validating', cancelled_at=None, cancelling_at=None, completed_at=None, error_file_id=None, errors=None, expired_at=None, expires_at=1761587637, failed_at=None, finalizing_at=None, in_progress_at=None, metadata={'description': 'hard-subset gpt-5-mini keypoint generation 26.10.25'}, model=None, output_file_id=None, request_counts=BatchRequestCounts(completed=0, failed=0, total=0), usage=BatchUsage(input_tokens=0, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=0, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=0))
Batch ID: batch_68fe6035f77c8190aec4c0bb748c674e
l4-nopdf-keypoints batch id: batch_6992a81c0b3c81908d5ea58f61acd8c6
'''
