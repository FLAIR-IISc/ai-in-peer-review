import transformers
import numpy as np
import tqdm
import argparse
import os
import tempfile
import sys
import json
import re
import functools
import yaml
import torch
from openai import OpenAI
from datetime import datetime
import time

def parse_args():
    parser = argparse.ArgumentParser(description='Generate reference peer reviews')
    
    parser.add_argument('--pathfile', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--keypoints_source', type=str, default=None, help='Path to the keypoints source file for level3 reviews, if None, set to output_dir')
    parser.add_argument('--model_name', type=str, required=True, help='Model name to use for generation')
    parser.add_argument('--base_url', type=str, required=False, default=None, help='Base URL for the model API')
    parser.add_argument('--create_batch_file', action='store_true', help='whether to create batch file for generation instead of individual chat completion calls')
    parser.add_argument('--batch_file_path', type=str, default=None, help='Path to save the batch file if create_batch_file is set')
    parser.add_argument('--global_openai_metadata', type=str, default=None, help='Path to global openai metadata dump file')
    parser.add_argument('--add_dev', action='store_true', help='Whether to generate references for the dev set as well')
    parser.add_argument('--verbose', action='store_true', help='Whether to print verbose logs')
    parser.add_argument('--dry-run', action='store_true', help='If set, do not actually make API calls or write output files')
    parser.add_argument('--prompt_templates_file', type=str, default="hard-subset-prompts.yaml", help='Path to the prompt templates YAML file')
    
    return parser.parse_args()

args = parse_args()

api_key = os.getenv("OPENAI_API_KEY")

if not args.create_batch_file:
    client_args = {
        "api_key": api_key,
    }
    if args.base_url is not None:
        client_args["base_url"] = args.base_url
    client = OpenAI(**client_args)

# if args.create_batch_file is True, clear the destination batch file if it exists
if args.create_batch_file:
    if os.path.exists(args.batch_file_path):
        os.remove(args.batch_file_path)

pathfile = args.pathfile

if args.keypoints_source is None:
    args.keypoints_source = args.output_dir

# load review guidelines
with open("conference-guidelines.yaml","r") as fin:
    review_guidelines = yaml.load(fin, Loader=yaml.SafeLoader)

# load prompt variations
with open(args.prompt_templates_file,"r") as fin:
    review_generation_prompts = yaml.load(fin, Loader=yaml.SafeLoader)

def get_openai_response(model_name, base_url, api_key, prompt):
    if args.dry_run:
        return ""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content

def remove_linenumbers(text):
    return re.sub(r'^\s*\d+\s*\n?', '', text, flags=re.MULTILINE)

def format_paper_contents(paper_contents):
    buffer = ""

    if "metadata" in paper_contents.keys() and "title" in paper_contents["metadata"].keys() and paper_contents["metadata"]["title"] is not None:
        title = remove_linenumbers(paper_contents["metadata"]["title"].strip())
        buffer += f"{title}\n\n"
    
    if "abstractText" in paper_contents["metadata"].keys() and paper_contents["metadata"]["abstractText"] is not None:
        abstract = remove_linenumbers(paper_contents["metadata"]["abstractText"].strip())
        buffer += f"ABSTRACT\n{abstract}\n\n"

    if "sections" in paper_contents["metadata"].keys() and paper_contents["metadata"]["sections"] is not None:
        for section in paper_contents["metadata"]["sections"]:
            if section["heading"] is None:
                continue
            section_heading = section["heading"]
            section_text = remove_linenumbers(section["text"])

            buffer += f"{section_heading}\n{section_text}\n\n"

    if "references" in paper_contents["metadata"].keys() and paper_contents["metadata"]["references"] is not None:
        buffer += "References:\n"
        for reference in paper_contents["metadata"]["references"]:
            for ref_field in reference.keys():
                if reference[ref_field] is None:
                    continue

                if isinstance(reference[ref_field], str):
                    ref_text = remove_linenumbers(reference[ref_field])
                    buffer += f"{ref_text}, "
                elif isinstance(reference[ref_field], list):
                    for itm in reference[ref_field]:
                        buffer += f"{remove_linenumbers(itm)}, "

            buffer += "\n\n"

    return buffer.strip()

def extract_paper_contents_from_filepath(paper_filepath):
    with open(paper_filepath, "r") as fin:
        file_content = json.load(fin)

    return format_paper_contents(file_content)

def extract_paper_fp_from_review_fp(review_filepath):
    ## extract the paper contents 
    pattern = r".*cleandata/(.*)/(train|test|dev)/.*(level[1-4]|reviews)/(.*)_([1-9]*).txt"
    match = re.search(pattern, review_filepath)
    conference = match.group(1)
    split = match.group(2)
    level = match.group(3)
    paper_number = match.group(4)
    reviewer_number = match.group(5)

    return (
        f"rawdata/{conference}/{split}/parsed_pdfs/{paper_number}.pdf.json", 
        conference, 
        split, 
        level, 
        paper_number, 
        reviewer_number
    )

def shorthand(model_name):
    mapping = {
        "/home/danishp/rounaksaha/.cache/huggingface/hub/models--Qwen--Qwen3-30B-A3B-Thinking-2507-FP8/snapshots/60d80c83c53c3b611c642dbb8c942b3f90c5948a": "Qwen3-30B-A3B-Thinking-2507-FP8",
        "/home/danishp/rounaksaha/.cache/huggingface/hub/models--google--gemma-3-27b-it/snapshots/005ad3404e59d6023443cb575daa05336842228a": "gemma-3-27b-it", 
        "/home/danishp/rounaksaha/.cache/huggingface/hub/models--hugging-quants--Meta-Llama-3.1-70B-Instruct-AWQ-INT4/snapshots/2123003760781134cfc31124aa6560a45b491fdf": "meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4",
    }
    return mapping.get(model_name, model_name)

with open(pathfile,"r") as file:
    all_paths = file.readlines()
all_paths = [path.strip() for path in all_paths]


papers = dict()

for each_review_path in tqdm.tqdm(all_paths): #each line in case of new reviews

    paper_filepath, conference, split, level, paper_number, reviewer_number = extract_paper_fp_from_review_fp(each_review_path)

    if split == "dev" and not args.add_dev:
        continue
    
    unique_id = f"{conference}***{split}***{paper_number}"

    if unique_id not in papers.keys():
        paper_text = extract_paper_contents_from_filepath(paper_filepath)

        '''really ugly code to extract just the conference name follows'''
        conference_wo_yr = conference
        remove_list = ['_2016', '_2017', '_2013', '-2017','/2013','/2014','/2015','/2016','/2017']
        for _ in remove_list:
            conference_wo_yr = conference_wo_yr.replace(_,'')
        '''ugl(ier) code ends here'''

        papers[unique_id] = {
            "paper_content": paper_text,
            "conference_wo_yr": conference_wo_yr,
            "conference": conference,
            "split": split,
            "paper_number": paper_number,
            "human_reviews": dict()
        }

    if level == "reviews":
        resolved_filepath = each_review_path
        with open(resolved_filepath,"r") as file:
            review_text = file.read()
        papers[unique_id]["human_reviews"][reviewer_number] = review_text

    
reviews_generated = 0
batch_entries = 0

included_destination = set()

total_human_reviews = sum([len(papers[pid]["human_reviews"].keys()) for pid in papers.keys()])
print("Total human reviews to process: ", total_human_reviews)

print(len(papers.keys()), "papers to process")

for instance in tqdm.tqdm(papers.values()):
#   if instance["split"] != "test":
#     continue
  for prompt_key in review_generation_prompts.keys():

    '''
    LET'S DECIDE ON THIS CONVENTION THAT ALL PROMPT KEYS WILL BE NAMED AS:
    [level1|level2|level3|level4]@<prompt_id>
    '''

    level = prompt_key.split("@")[0]  # e.g., level1, level2, etc.

    for reviewer_number, human_review in instance["human_reviews"].items():

        prompt_template = review_generation_prompts[prompt_key]

        prompt_filled = prompt_template.replace("{PAPER_CONTENT}", instance['paper_content'])
        prompt_filled = prompt_filled.replace("{CONFERENCE}", (instance['conference']).upper())
        prompt_filled = prompt_filled.replace("{GUIDELINES}", review_guidelines[instance['conference_wo_yr']])
            
        if (level == "level1") or (level == "level2"):
            out_file = os.path.join(
                args.output_dir, 
                f"{instance['conference']}/{instance['split']}/{instance['paper_number']}/{level}/{shorthand(args.model_name)}/{prompt_key}:::1.txt"
            )
        elif level == "level3":
            # fetch the keypoints
            keypoints_source = os.path.join(
                args.keypoints_source, 
                f"{instance['conference']}/{instance['split']}/{instance['paper_number']}/reviews/{reviewer_number}_keypoints.txt"
            )
            summarized_human_review = open(keypoints_source, "r").read().strip()
            prompt_filled = prompt_filled.replace("{SUMMARIZED_HUMAN_REVIEW}", summarized_human_review)
            out_file = os.path.join(
                args.output_dir, 
                f"{instance['conference']}/{instance['split']}/{instance['paper_number']}/{level}/{shorthand(args.model_name)}/{prompt_key}:::{reviewer_number}.txt"
            )
        else:
            prompt_filled = prompt_filled.replace("{HUMAN_REVIEW}", human_review)
            out_file = os.path.join(
                args.output_dir, 
                f"{instance['conference']}/{instance['split']}/{instance['paper_number']}/{level}/{shorthand(args.model_name)}/{prompt_key}:::{reviewer_number}.txt"
            )


        os.makedirs(os.path.dirname(out_file), exist_ok=True)

        if (os.path.exists(out_file) and os.path.getsize(out_file) > 0):
            if args.verbose:
                print(f"File {out_file} already exists and is not empty. Skipping.")
            continue
        elif (out_file in included_destination):
            continue
        elif not args.create_batch_file:
            if args.verbose:
                print(f"making api call with {len(prompt_filled.split())} input words")

            start_time = time.time()

            model_response = get_openai_response(
                model_name=args.model_name,  # or the name you used to serve
                base_url=args.base_url,
                api_key=api_key,
                prompt=prompt_filled
            )

            end_time = time.time()
            if args.verbose:
                print("Time taken for generation: ", end_time - start_time)

            reviews_generated += 1

            if not args.dry_run:
                with open(out_file,"w") as fout:
                    fout.write(model_response)

            included_destination.add(out_file)

            generation_metadata = {
                "model_name": args.model_name,
                "prompt_template": prompt_template,
                "file_written_to": out_file,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            with open(args.global_openai_metadata, "a") as metaout:
                metaout.write(json.dumps(generation_metadata) + "\n")

            with open(out_file.replace(".txt","_prompt.txt"),"w") as fout:
                fout.write(prompt_filled)
            # print("prompt printed at ", out_file.replace(".txt","_prompt.txt"))

        else:
            batch_file_entry = {
                "custom_id": f"{out_file}::{datetime.now().strftime('%Y%m%d%H%M%S')}", 
                "method": "POST", 
                "url": "/v1/chat/completions", 
                "body": {
                    "model": args.model_name, 
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt_filled},
                    ],
                }
            }


            with open(args.batch_file_path, "a") as batchout:
                batchout.write(json.dumps(batch_file_entry) + "\n")

            batch_entries += 1
            included_destination.add(out_file)


if not args.create_batch_file:
    print(reviews_generated, "reviews generated, phew!")
else:
    print(f"Batch file created at {args.batch_file_path} with {batch_entries} entries.")

