"""Generate key points for each review in saved_keypoints.

For every .txt file under the root directory (default: /home/rounak/saved_keypoints)
that does NOT already have a companion *_keypoints.txt file, this script will:

1. Read the review text.
2. Send it to the specified OpenAI model (default: gpt-5-mini) with the user-provided prompt format.
3. Save the returned key points into a new file with the same name plus the suffix '_keypoints.txt'.

Safety & Resumability:
 - Existing *_keypoints.txt files are never overwritten unless --overwrite is passed.
 - If the base review file is empty or whitespace, it is skipped.
 - Network/API errors are retried with exponential backoff.

Environment Variables:
  OPENAI_API_KEY      (required)
  OPENAI_ORG          (optional)
  OPENAI_PROJECT      (optional)
  OPENAI_BASE_URL     (optional, if using a proxy or different endpoint)

Example usage:
  python generate_keypoints_saved_reviews.py \
      --root /home/rounak/saved_keypoints \
      --model gpt-5-mini \
      --max-workers 4

Dry run (no API calls, just shows which files would be processed):
  python generate_keypoints_saved_reviews.py --dry-run

"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import os
import sys
import time
import traceback
from pathlib import Path
from typing import List, Optional
import re

try:
    from openai import OpenAI
except ImportError:  # Provide a helpful message if dependency missing.
    OpenAI = None  # type: ignore

PROMPT_TEMPLATE = (
    "You are given a review written by a reviewer of an AI conference. You need to give the key points "
    "discussed in the review as a one or two liner for each point. Write only the key points.\nReview: {review}"
)


def build_client():
    if OpenAI is None:
        raise RuntimeError("openai Python package not installed. Install with: pip install openai")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable is required.")

    client_args = {"api_key": api_key}
    org = os.environ.get("OPENAI_ORG")
    if org:
        client_args["organization"] = org
    project = os.environ.get("OPENAI_PROJECT")
    if project:
        client_args["project"] = project
    base_url = os.environ.get("OPENAI_BASE_URL")
    if base_url:
        client_args["base_url"] = base_url
    return OpenAI(**client_args)


def find_review_files(root: Path) -> List[Path]:
    return [p for p in root.rglob("*.txt") if not (p.name.endswith("_keypoints.txt") or p.name.endswith("_prompt.txt")) and re.search(rf".*/(train|test|dev)/(.*)/(level[1-4]|reviews|references)/.*", str(p)) is not None]


def needs_processing(review_path: Path, overwrite: bool) -> bool:

    # if '/test/' not in str(review_path) and '/dev/' not in str(review_path):
    #     return False

    # if '/train/' not in str(review_path):
    #     return False
    
    if '/references/' in str(review_path):
        return False
    
    if 'ttbt' in str(review_path):
        return False
    
    if 'temp-0.3' in str(review_path):
        return False

    # first make sure the .txt file is a review in question and not something else like subset summary or subset pathfiles
    review_filepath_pattern = rf".*/(train|test|dev)/(.*)/(level[1-4]|reviews|references)/.*"
    match = re.search(review_filepath_pattern, str(review_path))

    if match is None:
        return False

    target = review_path.with_name(review_path.stem + "_keypoints.txt")
    if not target.exists():
        return True
    return overwrite


def make_prompt(review_text: str) -> str:
    return PROMPT_TEMPLATE.format(review=review_text.strip())


def call_model(client, model: str, prompt: str, temperature: float, max_retries: int, retry_backoff: float) -> str:
    # Using chat.completions for compatibility with repository patterns.
    attempt = 0
    while True:
        attempt += 1
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                # temperature=temperature,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:  # broad to ensure retries on transient issues
            if attempt > max_retries:
                raise
            sleep_for = retry_backoff * (2 ** (attempt - 1))
            print(f"[WARN] Model call failed (attempt {attempt}/{max_retries}): {e}. Retrying in {sleep_for:.1f}s", file=sys.stderr)
            time.sleep(sleep_for)


def process_single(
    review_path: Path,
    model: str,
    temperature: float,
    dry_run: bool,
    overwrite: bool,
    max_retries: int,
    retry_backoff: float,
    client=None,
) -> Optional[Path]:
    try:
        if not needs_processing(review_path, overwrite):
            return None
        text = review_path.read_text(encoding="utf-8", errors="replace").strip()
        if not text:
            print(f"[SKIP] Empty review: {review_path}")
            return None
        target_path = review_path.with_name(review_path.stem + "_keypoints.txt")
        
        prompt = make_prompt(text)
        # # Basic truncation safeguard if extremely long (avoid excessive tokens)
        # if len(prompt) > 30000:  # characters, rough heuristic
        #     print("[WARNING] Prompt too long, truncating to 30,000 chars", file=sys.stderr)
        #     prompt = prompt[:30000] + "\n[TRUNCATED]"
        if dry_run:
            print(f"[DRY] Would process: {review_path} -> {target_path}")
            
            batch_file_entry = {
                "custom_id": f"{str(target_path)}::{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}", 
                "method": "POST", 
                "url": "/v1/chat/completions", 
                "body": {
                    "model": model, 
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt},
                    ],
                }
            }

            return batch_file_entry
        
        answer = call_model(client, model, prompt, temperature, max_retries, retry_backoff)
        target_path.write_text(answer + "\n", encoding="utf-8")
        print(f"[OK] {review_path} -> {target_path}")
        return target_path, batch_file_entry
    except Exception as e:
        print(f"[ERROR] Failed processing {review_path}: {e}", file=sys.stderr)
        traceback.print_exc()
        return None


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate key points for saved review text files.")
    parser.add_argument("--root", type=Path, default=Path("/home/rounak/saved_keypoints"), help="Root directory containing review .txt files")
    parser.add_argument("--model", default="gpt-5-mini", help="OpenAI model name")
    parser.add_argument("--temperature", type=float, default=0.2, help="Sampling temperature")
    parser.add_argument("--max-workers", type=int, default=4, help="Parallel workers for processing")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate even if _keypoints file exists")
    parser.add_argument("--dry-run", action="store_true", help="List actions without making API calls or writing output")
    parser.add_argument("--max-retries", type=int, default=5, help="Maximum retries per API call")
    parser.add_argument("--retry-backoff", type=float, default=2.0, help="Initial backoff (exponential)")
    parser.add_argument("--batch-file-out", type=Path, default=None, help="If set in dry-run mode, output batch request file instead of printing to console")
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    root: Path = args.root
    if not root.exists():
        print(f"Root directory does not exist: {root}", file=sys.stderr)
        return 1

    review_files = find_review_files(root)
    if not review_files:
        print("No review .txt files found.")
        return 0

    print(f"Discovered {len(review_files)} candidate review files under {root}")
    client = None if args.dry_run else build_client()

    # Process in parallel
    processed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = [
            executor.submit(
                process_single,
                rf,
                args.model,
                args.temperature,
                args.dry_run,
                args.overwrite,
                args.max_retries,
                args.retry_backoff,
                client,
            )
            for rf in review_files
        ]
        for fut in concurrent.futures.as_completed(futures):
            if fut.result() is not None:
                processed += 1

                if args.dry_run and args.batch_file_out is not None:
                    batch_file_entry = fut.result()
                    with open(args.batch_file_out, "a") as batchout:
                        batchout.write(json.dumps(batch_file_entry) + "\n")

    print(f"Finished. Generated key points for {processed} reviews.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv[1:]))
