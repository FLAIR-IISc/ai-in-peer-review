import time
import math
from datetime import timedelta, datetime
from openai import OpenAI
from google import genai
import os
import json

import argparse

parser = argparse.ArgumentParser(description="Monitor an OpenAI Batch until completion.")
parser.add_argument("--batch_id", type=str, help="ID of the OpenAI Batch to monitor.")
parser.add_argument("--batch_file_path", type=str, help="Path to the batch file used to create the batch.") # required only for logging
parser.add_argument("--poll_interval", type=int, default=60, help="Seconds between polls (default 60).")
parser.add_argument("--timeout_hours", type=int, default=24, help="Give up after this many hours (default 24).")
parser.add_argument("--verbose", action="store_true", help="If set, print progress lines.")
parser.add_argument("--save_output_path", type=str, required=True, help="Path to save the output file.")
parser.add_argument("--base_url", type=str, default=None, help="Base URL for OpenAI API")
parser.add_argument("--global_openai_metadata", type=str, required=True, help="Path to global openai metadata dump file")

args = parser.parse_args()

def human_delta(seconds):
    if seconds is None:
        return "unknown"
    return str(timedelta(seconds=int(max(0, seconds))))

def monitor_batch(client, batch_id, poll_interval=60, timeout_hours=24, verbose=True):
    """
    Monitor an OpenAI Batch until it reaches a terminal state.
    Prints progress, an ETA estimate (based on recent completion rate), and
    when finished, prints usage and tries to download the output file.

    Args:
        client: OpenAI client instance (from openai import OpenAI; client = OpenAI()).
        batch_id: str, id of the batch to monitor.
        poll_interval: seconds between polls (default 60).
        timeout_hours: give up after this many hours (default 24).
        verbose: if True, print progress lines.

    Returns:
        final_batch: the final batch object returned by client.batches.retrieve
        output_path: path to saved output file (or None)
    """
    start_time = time.time()
    timeout_seconds = timeout_hours * 3600
    history = []  # list of (timestamp, completed_count)
    last_print = 0

    metadata = {}

    while True:
        batch = client.batches.retrieve(batch_id)
        status = getattr(batch, "status", None)
        rc = getattr(batch, "request_counts", None)
        completed = getattr(rc, "completed", None) if rc is not None else None
        total = getattr(rc, "total", None) if rc is not None else None
        failed = getattr(rc, "failed", None) if rc is not None else None

        now = time.time()
        history.append((now, completed if completed is not None else 0))

        # Keep only last N history points to compute rate
        if len(history) > 6:
            history = history[-6:]

        # Compute rate (requests/sec) using first and last in history
        if len(history) >= 2:
            dt = history[-1][0] - history[0][0]
            dcompleted = history[-1][1] - history[0][1]
            rate = (dcompleted / dt) if dt > 0 else 0.0
        else:
            rate = None

        remaining = None
        eta_seconds = None
        if (total is not None) and (completed is not None):
            remaining = total - completed
            if rate and rate > 0:
                eta_seconds = remaining / rate
            else:
                eta_seconds = None

        # Print concise progress line (no spam)
        if verbose and (now - last_print >= max(10, poll_interval/2)):
            pct = (completed / total * 100) if (completed is not None and total) else None
            pct_str = f"{pct:.2f}%" if pct is not None else "?"
            eta_str = human_delta(eta_seconds)
            elapsed = human_delta(now - start_time)
            print(f"[{datetime.fromtimestamp(now).isoformat()}] status={status} | completed={completed}/{total} ({pct_str}) | failed={failed} | elapsed={elapsed} | ETA={eta_str}")
            last_print = now

        # Terminal statuses
        if status in ("completed", "failed", "cancelled", "expired"):
            if verbose:
                print(f"Batch reached terminal status: {status}")
            break

        # Timeout guard
        if now - start_time > timeout_seconds:
            print(f"Timeout reached ({timeout_hours} hours). Stopping monitor.")
            break

        time.sleep(poll_interval)

    # Re-fetch final batch to show final metadata
    final_batch = client.batches.retrieve(batch_id)
    if verbose:
        print("Final batch object:")
        print(final_batch)

    metadata["final_batch"] = final_batch.model_dump()

    # Show usage if present
    usage = getattr(final_batch, "usage", None)
    if usage:
        if verbose:
            print("Aggregated usage (total_tokens / input_tokens / output_tokens):")
            try:
                print(f"  total_tokens: {usage.total_tokens}")
                print(f"  input_tokens: {usage.input_tokens}")
                print(f"  output_tokens: {usage.output_tokens}")
            except Exception:
                # Some SDK shapes differ; just print the object
                print(usage)
    else:
        if verbose:
            print("Usage not present (the batch might not have finalized accounting).")

    # If there is an output_file_id, try to download it
    output_file_id = getattr(final_batch, "output_file_id", None)

    if output_file_id and args.base_url is None:
        output_meta = client.files.content(output_file_id)
        filename = args.save_output_path
        
        with open(filename, "w") as fout:
            fout.write(output_meta.text)
            
        if verbose:
            print(f"Responses saved at {filename}")
    
    elif output_file_id and args.base_url is not None:
        genai_client = genai.Client()
        file_content = genai_client.files.download(file=output_file_id).decode('utf-8')

        with open(args.save_output_path, "w") as fout:
            for line in file_content.splitlines():
                fout.write(line + "\n")

        if verbose:
            print(f"Responses saved at {args.save_output_path}")

    else:
        if verbose:
            print("No output_file_id present in the batch (yet).")

    return final_batch, args.save_output_path, metadata

if args.base_url is None:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)
else:
    base_url = args.base_url
    openai_api_key = os.getenv("GEMINI_API_KEY")
    client = OpenAI(base_url=base_url, api_key=openai_api_key)

final_batch, output_path, metadata = monitor_batch(
    client, 
    batch_id=args.batch_id, 
    poll_interval=args.poll_interval,
    verbose=args.verbose
)

batch_file_path_dirname = os.path.dirname(args.batch_file_path)
batch_responses_dirname = os.path.dirname(args.save_output_path)
openai_metadata_dirname = os.path.dirname(args.global_openai_metadata)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
save_batch_file_copy = args.batch_file_path.replace(batch_file_path_dirname, openai_metadata_dirname).replace(".jsonl", f"_{timestamp}.jsonl")
save_batch_responses_copy = args.save_output_path.replace(batch_responses_dirname, openai_metadata_dirname).replace(".jsonl", f"_{timestamp}.jsonl")

metadata["batch_file_path"] = save_batch_file_copy
metadata["batch_responses_path"] = save_batch_responses_copy

# copy batch file to openai metadata dir using system cp
os.system(f"cp {args.batch_file_path} {save_batch_file_copy}")
# copy batch responses to openai metadata dir using system cp
os.system(f"cp {args.save_output_path} {save_batch_responses_copy}")

# save metadata to global_openai_metadata path
with open(args.global_openai_metadata, "a") as fout:
    fout.write(json.dumps(metadata) + "\n")

print("Metadata saved to", args.global_openai_metadata)