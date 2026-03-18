'''
as if its creation on 26-10-2025, this script is no different than the similarly named script in the reference generation folder
'''

import json
import os
import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--batch_responses_path", type=str, required=True, help="Path to batch responses file")

args = parser.parse_args()

files_written = 0

with open(args.batch_responses_path, "r") as fin:
	for line in fin:
		batch_response = json.loads(line)
		destination_file = batch_response["custom_id"].split("::")[0]
		reference_review = batch_response["response"]["body"]["choices"][0]["message"]["content"]

		if os.path.exists(destination_file) and os.path.getsize(destination_file) > 0:
			raise FileExistsError("File already exists and is not empty:", destination_file)

		with open(destination_file, "w") as fout:
			fout.write(reference_review)

		files_written += 1

		# print(destination_file)

print(f"Total files written: {files_written}")