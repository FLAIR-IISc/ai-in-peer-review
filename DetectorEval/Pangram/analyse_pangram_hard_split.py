import json
import numpy as np

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

excnt = 0

for key, val in results.items():

	true_labe = '/reviews/'

	for i in range(1,5):
		if f'level{i}' in key:
			true_labe = f'level{i}'

	predicted_label = val["prediction_short"]

	anal_dict[true_labe].append(predicted_label)

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

'''
level1: {'AI Detected': 0.1927710843373494, 'Fully AI Generated': 0.4457831325301205, 'AI Assisted': 0.28313253012048195, 'Fully Human Written': 0.06626506024096386, 'Mostly Human, AI Assisted': 0.006024096385542169, 'Mostly Human Written': 0.006024096385542169}
level2: {}
level3: {}
level4: {'Fully Human Written': 0.6303030303030303, 'AI Assisted': 0.296969696969697, 'AI Detected': 0.006060606060606061, 'Fully AI Generated': 0.03636363636363636, 'Mostly Human, AI Assisted': 0.01818181818181818, 'Mostly Human, AI Detected': 0.006060606060606061, 'Human Written': 0.006060606060606061}
/reviews/: {}
'''

'''
With updated Level 4:
level1: {'AI': 0.9725343320848939, 'Mixed': 0.02746566791510612}
level2: {'AI': 0.9939024390243902, 'Mixed': 0.006097560975609756}
level3: {'AI': 0.9330296127562643, 'Mixed': 0.05284738041002278, 'Human': 0.014123006833712985}
level4: {'Human': 0.4962894248608534, 'Mixed': 0.35528756957328383, 'AI': 0.14842300556586271}
/reviews/: {'Human': 1.0}
{'level1': {'AI': 0.9725343320848939, 'Mixed': 0.02746566791510612}, 'level2': {'AI': 0.9939024390243902, 'Mixed': 0.006097560975609756}, 'level3': {'AI': 0.9330296127562643, 'Mixed': 0.05284738041002278, 'Human': 0.014123006833712985}, 'level4': {'Human': 0.4962894248608534, 'Mixed': 0.35528756957328383, 'AI': 0.14842300556586271}, '/reviews/': {'Human': 1.0}}
[[ 97.25343321,  99.3902439 ,  93.30296128,  14.84230056,   0.        ],
 [  2.74656679,   0.6097561 ,   5.28473804,  35.52875696,   0.        ],
 [  0.        ,   0.        ,   1.41230068,  49.62894249, 100.        ]]

On Level 4 with only with pdf reviews:
level4: {'AI': 0.7968828557063852, 'Human': 0.10306686777275012, 'Mixed': 0.10005027652086476}

L4 NAV: {'Human': 0.7413793103448276, 'Mixed': 0.23419540229885058, 'AI': 0.02442528735632184}
L4 P1NOPDF: {'AI': 0.07802874743326489, 'Human': 0.6940451745379876, 'Mixed': 0.22792607802874743}
L4 P2NOPDF: {'Mixed': 0.5316973415132924, 'Human': 0.3067484662576687, 'AI': 0.16155419222903886}
L4 P3NOPDF: {'AI': 0.384297520661157, 'Mixed': 0.4793388429752066, 'Human': 0.13636363636363635}
'''