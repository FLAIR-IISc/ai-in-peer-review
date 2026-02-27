import os
import json
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--source_dir", type=str, help="Source subset")
parser.add_argument("--target_dir", type=str, help="Target subset")
parser.add_argument("--keypoints", action="store_true", help="Whether to share keypoints")
parser.add_argument("--reference_reviews", action="store_true", help="Whether to share reference reviews")
parser.add_argument("--dry-run", action="store_true", help="If set, do not actually copy files, just print what would be done")

args = parser.parse_args()

if args.source_dir.endswith("/"):
    args.source_dir = args.source_dir[:-1]
if args.target_dir.endswith("/"):
    args.target_dir = args.target_dir[:-1]

def parse_paper_details(filepath, root_dir):
    pattern = rf".*{root_dir}/(.*)/(train|test|dev)/(.*)/(level[1-4]|reviews|references)/.*"
    match = re.search(pattern, filepath)
    if match is None:
        return None, None, None
    conference = match.group(1)
    split = match.group(2)
    paper_number = match.group(3)

    return conference, split, paper_number


# walk through all  text files in the source_dir not ending with with _keypoints.txt or _reference_review.txt and store them in a set
source_files = set()
for root, dirs, files in os.walk(args.source_dir):
    for filename in files:
        if filename.endswith(".txt") and not (filename.endswith("_keypoints.txt") or filename.endswith("_reference_review.txt")):
            conference, split, paper_number = parse_paper_details(os.path.join(root, filename), args.source_dir)
            if conference is not None:
                source_files.add(f"{conference}::{split}::{paper_number}")
            
target_files = set()
for root, dirs, files in os.walk(args.target_dir):
    for filename in files:
        if filename.endswith(".txt") and not (filename.endswith("_keypoints.txt") or filename.endswith("_reference_review.txt")):
            conference, split, paper_number = parse_paper_details(os.path.join(root, filename), args.target_dir)
            target_files.add(f"{conference}::{split}::{paper_number}")
            
common_files = source_files.intersection(target_files)

print(f"Found {len(common_files)} common papers")

# make a list of files ending with _keypoints.txt or _reference_review.txt in the source_dir that have os.path.join(args.source_dir, common_file) as a prefix in their filename
files_to_copy = []
for root, dirs, files in os.walk(args.source_dir):
    for filename in files:
        if filename.endswith("_keypoints.txt") or filename.endswith("_reference_review.txt"):
            conference, split, paper_number = parse_paper_details(os.path.join(root, filename), args.source_dir)
            if f"{conference}::{split}::{paper_number}" in common_files:

                # does the same file exist in the target_dir?
                destination_filepath = os.path.join(root, filename).replace(args.source_dir, args.target_dir)
                if os.path.exists(destination_filepath) and os.path.getsize(destination_filepath) > 0:
                    continue
                
                if (args.keypoints and filename.endswith("_keypoints.txt")) or (args.reference_reviews and filename.endswith("_reference_review.txt")):
                    # if we are here, we need to copy this file to the destination filepath
                    files_to_copy.append((
                        os.path.join(root, filename),
                        destination_filepath
                    ))

if args.dry_run:
    print(f"Dry run mode. {len(files_to_copy)} files would be copied:")
    for idx, (src, dst) in enumerate(files_to_copy):
        print(f"({idx+1})\t{src} -> {dst}")
else:
    print(f"{len(files_to_copy)} files would be copied:")
    for idx, (src, dst) in enumerate(files_to_copy):
        print(f"({idx+1})\t{src} -> {dst}")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(src, "r") as fin:
            content = fin.read()
        with open(dst, "w") as fout:
            fout.write(content)
    print(f"Copied {len(files_to_copy)} files.")