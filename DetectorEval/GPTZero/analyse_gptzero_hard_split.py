import json
import numpy as np

results_file = "[DESTINATION_JSON_FILE]"
	
with open(results_file, 'r') as f:
	results = json.load(f)

print(len(results))

def count_freq(predictions):
	freq_dict = {}
	for pred in predictions:
		if pred in freq_dict:
			freq_dict[pred] += 1
		else:
			freq_dict[pred] = 1

	for key in freq_dict:
		freq_dict[key] = freq_dict[key] / len(predictions)

	return freq_dict

anal_dict = {
	"level1": [],
	"level2": [],
	"level3": [],
	"level4": [],
	"/reviews/": []
}

excnt = 0

for key, val in results.items():

	true_labe = '/reviews/'

	for i in range(1,5):
		if f'level{i}' in key:
			true_labe = f'level{i}'

	cur_preds = val['documents'][0]['class_probabilities']

	cat_preds = [cur_preds['ai'], cur_preds['mixed'], cur_preds['human']]

	predicted_label = int(np.argmax(cat_preds))

	anal_dict[true_labe].append(predicted_label)
	excnt += 1

print(f"Total examples processed: {excnt}")

consol_dict = {}

for key, val in anal_dict.items():
	freqs = count_freq(val)
	print(f"{key}: {freqs}")
	consol_dict[key] = freqs

import numpy as np

cm = np.zeros((5,3))

for level_idx, level in enumerate(['level1', 'level2', 'level3', 'level4', '/reviews/']):
	for idx, pred in enumerate([0, 1, 2]):
		if pred in consol_dict[level]:
			cm[level_idx, idx] = consol_dict[level][pred] * 100

print(print(np.array2string(cm.T, separator=', ')))