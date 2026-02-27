import json
import os
import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--batch_responses_path", type=str, required=True, help="Path to batch responses file")

args = parser.parse_args()

skipped = 0

with open(args.batch_responses_path, "r") as fin:
	for line in fin:
		batch_response = json.loads(line)
		timestamp = batch_response["custom_id"].split("::")[-1]
		destination_file = batch_response["custom_id"].replace(f"::{timestamp}", "")
		# print(destination_file)
		# exit(1)

		try:
			reference_review = batch_response["response"]["body"]["choices"][0]["message"]["content"]
		except KeyError:
			skipped += 1
			continue

		os.makedirs(os.path.dirname(destination_file), exist_ok=True)

		if os.path.exists(destination_file) and os.path.getsize(destination_file) > 0:
			# raise FileExistsError("File already exists and is not empty:", destination_file)
			continue

		with open(destination_file, "w") as fout:
			fout.write(reference_review)

		# print(destination_file)

print("Skipped:", skipped)