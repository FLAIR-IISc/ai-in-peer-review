import json

input_file = "/home/rounak/ai-involvement-in-peer-reviews/detector_scores_caliberation/old_data_uniform.json"
detector = "binoculars_cxt"
field = "prob"


with open(input_file, "r") as f:
	data = json.load(f)

human_scores = []

for key, val in data.items():
	if '/reviews/' not in key:
		continue

	if '/dev/' not in key:
		continue

	if "neurips_2013" not in key and "neurips_2014" not in key and "neurips_2015" not in key:
		continue

	score = val[detector][field]

	human_scores.append((score, key))

print(len(human_scores))
print(sorted(human_scores)[:5])

threshold = min(human_scores)[0]

print(threshold)
