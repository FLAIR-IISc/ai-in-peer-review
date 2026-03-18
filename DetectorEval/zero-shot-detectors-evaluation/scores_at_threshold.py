import json
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", type=str, required=True)
parser.add_argument("--detector", type=str, required=True)
parser.add_argument("--field", type=str, required=True)
parser.add_argument("--sign", type=int, default=1)
parser.add_argument("--threshold", type=float, required=True)
parser.add_argument("--length_filtering", action="store_true")

args = parser.parse_args()

input_file = args.input_file
detector = args.detector
field = args.field
threshold = args.threshold
length_filtering = args.length_filtering

examples_evaluated = 0

with open(input_file, "r") as f:
	data = json.load(f)


print(f"Using threshold: {threshold}")

results_dict = {
	"level1": [],
	"level2": [],
	"level3": [],
	"level4": [],
	"/reviews/": []
}

length_filtered_examples = {}

for key, val in data.items():

	if '/test/' not in key:
		continue


	review_filepath = key

	for i in range(13,18):
		if f"neurips_20{i}/" in review_filepath:
			review_filepath = review_filepath.replace(f"neurips_20{i}/", f"nips_2013-2017/20{i}/")
			break

	try:
		open(review_filepath, "r").close()
	except:
		review_filepath = "/home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/" + review_filepath

	haireview = open(review_filepath, "r").read()

	hreviewpath = re.sub(r'level4.*:::', 'reviews/', review_filepath)

	hreview = open(hreviewpath, "r").read()

	len_haireview = len(haireview.split())
	len_hreview = len(hreview.split())

	if length_filtering and not (0 <= len_haireview / len_hreview < 1.25):
		continue

	score = val[detector][field]

	true_label = '/reviews/'


	for level in ["level1", "level2", "level3", "level4"]:
		if f"/{level}/" in key:
			true_label = level
			break

	pred_label = 1 if (args.sign)*score > (args.sign)*threshold else 0

	results_dict[true_label].append(pred_label)
	examples_evaluated += 1
	length_filtered_examples[key] = val

print("Examples evaluated:", examples_evaluated)

for label, preds in results_dict.items():
	if len(preds) == 0:
		continue
	print(f"{label}: {sum(preds)*100/len(preds)}% of {len(preds)}")

for label, preds in results_dict.items():
	if len(preds) == 0:
		continue
	print(f"${sum(preds)*100/len(preds):.1f}$", end=" & ")

print()


