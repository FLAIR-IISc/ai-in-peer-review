import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import hashlib

import argparse

parser = argparse.ArgumentParser(description="Extract features from JSON file.")
parser.add_argument("--results_file", type=str, required=True, help="Path to the input JSON file.")
parser.add_argument("--threshold", type=float, required=True, help="Similarity threshold for exact match.")
parser.add_argument("--score_aggregation_mode", type=str, choices=["max", "avg"], default="max", help="Pooling mode for scores across multiple reference generations from same model.")
parser.add_argument("--output_dir", type=str, required=True, help="Directory to save the output features.")
parser.add_argument("--monochrome", action="store_true", help="when this flag is disabled, candidate reviews from different generating models, gpt_4o_latest, meta-llama-Llama-3.3B-Instruct, human are plotted in different colors.")
parser.add_argument("--vertical", action="store_true", help="when this flag is enabled, the subplots are arranged vertically.")

args = parser.parse_args()

plt.rcParams['font.family'] = 'Lato'
plt.rcParams['font.size'] = 12

with open(args.results_file, "r") as fin:
    results_data = json.load(fin)
      
review2features = dict()
x_axes = set()

for key, val in results_data.items():
     

    ref_gen_model_wise_scores = dict()
    for ref_id in sorted(val.keys()):
        ref_gen_model = ref_id.split("@")[1]
        if ref_gen_model not in ref_gen_model_wise_scores:
            ref_gen_model_wise_scores[ref_gen_model] = []
        if not isinstance(val[ref_id], float):
            ref_gen_model_wise_scores[ref_gen_model].append(val[ref_id][str(args.threshold)])
        else:
            ref_gen_model_wise_scores[ref_gen_model].append(val[ref_id])

    for ref_gen_model in sorted(ref_gen_model_wise_scores.keys()):
        if args.score_aggregation_mode == "max":
            aggregated_score = max(ref_gen_model_wise_scores[ref_gen_model])
        else:  # avg
            aggregated_score = sum(ref_gen_model_wise_scores[ref_gen_model]) / len(ref_gen_model_wise_scores[ref_gen_model])

        if key not in review2features:
            review2features[key] = dict()
        review2features[key][ref_gen_model] = aggregated_score
            
for key in review2features.keys():
    aggregate_score = 0
    for ref_model in review2features[key].keys():
        x_axes.add(ref_model)
        if args.score_aggregation_mode == "max":
                aggregate_score = max(aggregate_score, review2features[key][ref_model])
        elif args.score_aggregation_mode == "avg":
                aggregate_score += review2features[key][ref_model]

    review2features[key][f"aggregate={args.score_aggregation_mode}"] = aggregate_score if args.score_aggregation_mode == "max" else aggregate_score / len(review2features[key].keys())
    x_axes.add(f"aggregate={args.score_aggregation_mode}")

args.output_dir = os.path.join(args.output_dir, f"threshold={args.threshold}_aggregation={args.score_aggregation_mode}/")
os.makedirs(args.output_dir, exist_ok=True)

PALETTE = [
    "blue", "orange", "green", "red",
    "purple", "teal", "brown", "pink"
]

def model_to_color(name):
    h = int(hashlib.md5(name.encode()).hexdigest(), 16)
    return PALETTE[h % len(PALETTE)]

model_list = ["gemini-2.5-pro", "gemma-3-27b-it", "gpt_4o_latest", "gpt-5", "meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4", "meta-llama-Llama-3.3-70B-Instruct", "Qwen3-30B-A3B-Thinking-2507-FP8", "human"]

level_names = ["AI w/ Basic Prompts (AI-BP)", "AI w/ Elaborate Prompts (AI-EP)", "AI w/ Human Input (AI-HI)", "Human-written AI-Polished (H-AI)", "Human (H)"]

if not args.monochrome:
    author2color = {m: model_to_color(m) for m in model_list}

    for ref_author in x_axes:

        print(ref_author)

        level_wise = [{}, {}, {}, {}, {}]

        for key, val in review2features.items():

            author = "human"
            for x in model_list:
                if x in key:
                    author = x


            z_score = val[ref_author]

            for i in range(1, 5):
                if f"level{i}" in key:
                    if author not in level_wise[i-1].keys():
                        level_wise[i-1][author] = []
                    level_wise[i-1][author].append(z_score)
            
            if "/reviews/" in key:
                if author not in level_wise[4].keys():
                    level_wise[4][author] = []
                level_wise[4][author].append(z_score)

        level_wise_dict = dict()
        for i in range(1,6):
            print(f"LEVEL {i} examples: {sum([len(level_wise[i-1][author]) for author in level_wise[i-1].keys()])}")
            level_wise_dict[f"LEVEL {i}"] = level_wise[i-1]

        num_levels = 5
        if args.vertical:
            fig, axes = plt.subplots(nrows=num_levels, ncols=1, figsize=(4, 3 * num_levels))
        else:
            fig, axes = plt.subplots(nrows=1, ncols=num_levels, figsize=(4 * num_levels, 3))
        bins = 50

        for i in range(1, num_levels + 1):
            level_name = f"LEVEL {i}"
            ax = axes[i - 1]
            # extract the first element of each tuple (similarity_gpt); guard against empty or malformed entries

            for author in level_wise_dict[level_name].keys():
                data = level_wise_dict[level_name][author]
                if data:
                    ax.hist(data, bins=bins, color=author2color[author], alpha=0.5, range=(-0.01, 1.01), label=author)

            ax.set_title(level_names[i-1])
            # ax.set_ylim(0,1)
            ax.set_ylabel('Count', fontsize=14)
            ax.set_xlabel(f"{args.score_aggregation_mode} similarity with {ref_author} references" if "aggregate" not in ref_author else f"{args.score_aggregation_mode} similarity", fontsize=14)
            # ax.legend()

        # Add a global title for all subplots
        fig.suptitle(f"Threshold: {args.threshold}", fontsize=16)

        plt.tight_layout()
        print(f"saving figure to {os.path.join(args.output_dir, f'distri-level-plot-{ref_author}-sim.pdf')}")
        plt.savefig(os.path.join(args.output_dir, f"distri-level-plot-{ref_author}-sim.pdf"), dpi=600)

else:
    for ref_author in x_axes:

        level_wise = [[], [], [], [], []]

        for key, val in review2features.items():

            # val[ref_author] are my scores

            z_score = val[ref_author]

            for i in range(1, 5):
                if f"level{i}" in key:
                    level_wise[i-1].append(z_score)
            
            if "/reviews/" in key:
                level_wise[4].append(z_score)

        level_wise_dict = dict()
        for i in range(1,6):
            print(f"LEVEL {i} examples: {len(level_wise[i-1])}")
            level_wise_dict[f"LEVEL {i}"] = level_wise[i-1]

        num_levels = 5
        if args.vertical:
            fig, axes = plt.subplots(nrows=num_levels, ncols=1, figsize=(4, 2.5 * num_levels))
        else:       
            fig, axes = plt.subplots(nrows=1, ncols=num_levels, figsize=(4 * num_levels, 3))
        bins = 50

        for i in range(1, num_levels + 1):
            level_name = f"LEVEL {i}"
            ax = axes[i - 1]
            # extract the first element of each tuple (similarity_gpt); guard against empty or malformed entries

            data = level_wise_dict[level_name]
            if data:
                ax.hist(data, bins=bins, alpha=0.7, range = (-0.01,1.01))
            ax.set_title(level_names[i-1])
            ax.set_xlim(0.5,1)
            ax.set_ylabel('Count', fontsize=14)
            if not args.vertical:
                ax.set_xlabel(f"{args.score_aggregation_mode} similarity with {ref_author} references" if "aggregate" not in ref_author else f"{args.score_aggregation_mode} similarity", fontsize=14)
            elif i==num_levels:
                ax.set_xlabel(f"{args.score_aggregation_mode} similarity with {ref_author} references" if "aggregate" not in ref_author else f"\n{args.score_aggregation_mode} similarity", fontsize=18)

        # Add a global title for all subplots
        fig.suptitle(f"Cosine Similarity\n", fontsize=18)

        plt.tight_layout()
        print(f"saving figure to {os.path.join(args.output_dir, f'distri-level-plot-{ref_author}-sim-monochrome.pdf')}")
        plt.savefig(os.path.join(args.output_dir, f"distri-level-plot-{ref_author}-sim-monochrome.pdf"), dpi=600)
 