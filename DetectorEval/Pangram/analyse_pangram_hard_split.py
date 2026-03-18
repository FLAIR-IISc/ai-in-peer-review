import json
import numpy as np
import re

results_file = "[DESTINATION_JSON_FILE]"


with open(results_file, 'r') as f:
	results = json.load(f)

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
# print(len(pure_reviews))
excnt = 0
avg_ratio = 0

level_4_cnt = 0

markdown_buffer = ""

for key, val in results.items():

	# remove easy subset examples
	if ("gpt_4o_latest" in key or "meta-llama-Llama-3.3-70B-Instruct" in key):
		continue


	haireview = open(key, "r").read()

	hreviewpath = re.sub(r'level4.*:::', 'reviews/', key)

	hreview = open(hreviewpath, "r").read()

	len_haireview = len(haireview.split())
	len_hreview = len(hreview.split())

	# length filtering
	if not (0 <= len_haireview / len_hreview < 1.25):
		continue


	true_labe = '/reviews/'

	for i in range(1,5):
		if f'level{i}' in key:
			true_labe = f'level{i}'

	predicted_label = val["prediction_short"]

	anal_dict[true_labe].append(predicted_label)

	if true_labe == 'level4' and predicted_label == 'AI':
		level_4_cnt += 1
		markdown_buffer += f"## ({level_4_cnt}) {key}\n"
		hreviewpath = re.sub(r'level4.*:::', 'reviews/', key)
		hreview = open(hreviewpath, "r").read()
		haireview = open(key, "r").read()

		markdown_buffer += f"### Human review:\n\n{hreview}\n\n"
		markdown_buffer += f"### Polished review:\n\n{haireview}\n\n"

	excnt += 1


print(f"Total examples processed: {excnt}")

consol_dict = {}

for key, val in anal_dict.items():
	freqs = count_freq(val)
	print(f"{key}: {freqs}")
	consol_dict[key] = freqs

print(consol_dict)

import numpy as np

cm = np.zeros((5,3))

for level_idx, level in enumerate(['level1', 'level2', 'level3', 'level4', '/reviews/']):
	for idx, pred in enumerate(['AI', 'Mixed', 'Human']):
		if pred in consol_dict[level]:
			cm[level_idx, idx] = consol_dict[level][pred] * 100

print(print(np.array2string(cm.T, separator=', ')))

with open("level4_pangram_fps.md", "w") as f:
	f.write(markdown_buffer)
