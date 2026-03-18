import json
import copy

input_file = ""

with open(input_file, "r") as f:
	data = json.load(f)

uniform_results = {}

for conf in data.keys():
	for itm in data[conf]:
		
		if itm["category"] != "human":
			id = f"{conf}/{itm['set']}/{itm['paper_number']}/{itm['category']}/{itm['model']}/{itm['key'].split('_')[-1]}"
		else:
			id = f"{conf}/{itm['set']}/{itm['paper_number']}/reviews/{itm['key'].split('_')[-1]}"

		uniform_results[id] = copy.deepcopy(itm)

output_file = input_file.replace(".json", "_uniform.json")
with open(output_file, "w") as f:
	json.dump(uniform_results, f, indent=4)