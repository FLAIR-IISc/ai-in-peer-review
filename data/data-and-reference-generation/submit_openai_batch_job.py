from openai import OpenAI, base_url, RateLimitError, APIError
from google import genai
from google.genai import types
import json
import os
import argparse
import tqdm
import time
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--batch_file_path", type=str, required=True, help="path to batch file")
parser.add_argument("--base_url", type=str, default=None, help="Base URL for OpenAI API")
parser.add_argument("--description", type=str, default="reference generation job", help="Description for the batch job metadata")
parser.add_argument("--max_retries", type=int, default=3, help="Maximum number of retries for rate limit handling")
parser.add_argument("--retry_delay", type=int, default=120, help="Delay between retries in seconds")
parser.add_argument("--verbose", action="store_true", help="if not set, prints ONLY the batch id")

args = parser.parse_args()

if args.base_url is None:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)
    batch_input_file = client.files.create(
        file=open(args.batch_file_path, "rb"),
        purpose="batch"
    )

    if args.verbose:
        print("BATCH INPUT FILE: ", batch_input_file)

    batch_input_file_id = batch_input_file.id
else:
    base_url = args.base_url
    openai_api_key = os.getenv("GEMINI_API_KEY")
    client = OpenAI(base_url=base_url, api_key=openai_api_key)

    gemini_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    uploaded_file = gemini_client.files.upload(
        file=args.batch_file_path, 
        config=types.UploadFileConfig(
            display_name='this-ones-legit', 
            mime_type='application/json'
        )
    )
    batch_input_file_id = uploaded_file.name

    if args.verbose:
        print("BATCH INPUT FILE: ", uploaded_file)
        print("BATCH INPUT FILE ID: ", batch_input_file_id)


max_retries = args.max_retries
retry_delay = args.retry_delay  # seconds

for attempt in range(1, max_retries + 1):
    try:
        batch__ = client.batches.create(
            input_file_id=batch_input_file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={
                "description": args.description,
            }
        )
        break

    except RateLimitError as e:
        if attempt < max_retries:
            print(f"Rate limit hit (attempt {attempt}/{max_retries}). Retrying in {retry_delay//60} minutes...")
            time.sleep(retry_delay)
        else:
            print(f"Rate limit error persisted after {max_retries} attempts. Exiting.")
            sys.exit(1)

    except APIError as e:
        # Explicitly check if it's 429 (rate limit) — covers APIError variant of RateLimitError
        if getattr(e, "status_code", None) == 429 and attempt < max_retries:
            print(f"API 429 rate limit (attempt {attempt}/{max_retries}). Retrying in {retry_delay//60} minutes...")
            time.sleep(retry_delay)
        else:
            print(f"API error: {e}. Exiting.")
            sys.exit(1)

    except Exception as e:
        print(f"Unexpected error ({type(e).__name__}): {e}")
        sys.exit(1)

# print("BATCH: ", batch__)

if args.verbose:
    print("Batch ID:", batch__.id)
else:
    print(batch__.id)

