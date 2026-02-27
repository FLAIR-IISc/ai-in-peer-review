import json

input_file = "/home/rounak/ai-involvement-in-peer-reviews/detector_scores_caliberation/combined-hard-split-main-paper.json"
detector = "binoculars_cxt"
field = "prob"

with open(input_file, "r") as f:
	data = json.load(f)

threshold = 0.8125
print(f"Using threshold: {threshold}")

results_dict = {
	"level1": [],
	"level2": [],
	"level3": [],
	"level4": [],
	"/reviews/": []
}

for key, val in data.items():
	# if '/reviews/' not in key:
	# 	continue

	if '/test/' not in key:
		continue

	# if 'neurips' in key:
	# 	continue

	score = val[detector][field]

	true_label = '/reviews/'

	if val['category'] != 'human':
		true_label = val['category']

	pred_label = 1 if score < threshold else 0

	results_dict[true_label].append(pred_label)

for label, preds in results_dict.items():
	print(f"{label}: {sum(preds)*100/len(preds)}% of {len(preds)}")

for label, preds in results_dict.items():
	print(f"${sum(preds)*100/len(preds):.1f}$", end=" & ")

print()
