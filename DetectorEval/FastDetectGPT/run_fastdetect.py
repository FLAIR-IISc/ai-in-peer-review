# Copyright (c) Guangsheng Bao.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# Modified 2026.
import torch
import os
import argparse
import json
from model import load_tokenizer, load_model
from fast_detect_gpt import get_sampling_discrepancy_analytic
from scipy.stats import norm

# Considering balanced classification that p(D0) equals to p(D1), we have
#   p(D1|x) = p(x|D1) / (p(x|D1) + p(x|D0))
def compute_prob_norm(x, mu0, sigma0, mu1, sigma1):
    pdf_value0 = norm.pdf(x, loc=mu0, scale=sigma0)
    pdf_value1 = norm.pdf(x, loc=mu1, scale=sigma1)
    prob = pdf_value1 / (pdf_value0 + pdf_value1)
    return prob

class FastDetectGPT:
    def __init__(self, args):
        self.args = args
        self.criterion_fn = get_sampling_discrepancy_analytic
        self.scoring_tokenizer = load_tokenizer(args.scoring_model_name, args.cache_dir)
        self.scoring_model = load_model(args.scoring_model_name, args.device, args.cache_dir)
        self.max_len = self.scoring_model.config.max_position_embeddings
        self.scoring_model.eval()
        if args.sampling_model_name != args.scoring_model_name:
            self.sampling_tokenizer = load_tokenizer(args.sampling_model_name, args.cache_dir)
            self.sampling_model = load_model(args.sampling_model_name, args.device, args.cache_dir)
            self.max_len = min(self.max_len, self.sampling_model.config.max_position_embeddings)
            self.sampling_model.eval()
        # To obtain probability values that are easy for users to understand, we assume normal distributions
        # of the criteria and statistic the parameters on a group of dev samples. The normal distributions are defined
        # by mu0 and sigma0 for human texts and by mu1 and sigma1 for AI texts. We set sigma1 = 2 * sigma0 to
        # make sure of a wider coverage of potential AI texts.
        # Note: the probability could be high on both left side and right side of Normal(mu0, sigma0).
        #   gpt-j-6B_gpt-neo-2.7B: mu0: 0.2713, sigma0: 0.9366, mu1: 2.2334, sigma1: 1.8731, acc:0.8122
        #   gpt-neo-2.7B_gpt-neo-2.7B: mu0: -0.2489, sigma0: 0.9968, mu1: 1.8983, sigma1: 1.9935, acc:0.8222
        #   falcon-7b_falcon-7b-instruct: mu0: -0.0707, sigma0: 0.9520, mu1: 2.9306, sigma1: 1.9039, acc:0.8938
        distrib_params = {
            'gpt-j-6B_gpt-neo-2.7B': {'mu0': 0.2713, 'sigma0': 0.9366, 'mu1': 2.2334, 'sigma1': 1.8731},
            'gpt-neo-2.7B_gpt-neo-2.7B': {'mu0': -0.2489, 'sigma0': 0.9968, 'mu1': 1.8983, 'sigma1': 1.9935},
            'falcon-7b_falcon-7b-instruct': {'mu0': -0.0707, 'sigma0': 0.9520, 'mu1': 2.9306, 'sigma1': 1.9039},
            'llama3-8b_llama3-8b-instruct': {'mu0': 0.1603, 'sigma0': 1.0791, 'mu1': 2.4686, 'sigma1': 2.1582},
        }
        key = f'{args.sampling_model_name}_{args.scoring_model_name}'
        self.classifier = distrib_params[key]


    # compute conditional probability curvature
    def compute_crit(self, text):
        tokenized = self.scoring_tokenizer(text, truncation=True, return_tensors="pt", padding=False, return_token_type_ids=False).to(self.args.device)
        labels = tokenized.input_ids[:, 1:]
        with torch.no_grad():
            logits_score = self.scoring_model(**tokenized).logits[:, :-1]
            if self.args.sampling_model_name == self.args.scoring_model_name:
                logits_ref = logits_score
            else:
                tokenized = self.sampling_tokenizer(text, truncation=True, return_tensors="pt", padding=False, return_token_type_ids=False).to(self.args.device)
                assert torch.all(tokenized.input_ids[:, 1:] == labels), "Tokenizer is mismatch."
                logits_ref = self.sampling_model(**tokenized).logits[:, :-1]
            res = self.criterion_fn(logits_ref, logits_score, labels)
            crit = res['discrepancy']
            log_likelihood = res['log_likelihood']
        return crit, labels.size(1), log_likelihood
    
    
    # compute conditional probability curvature with added context
    def compute_crit_cxt(self, review, abstract):
        rev_tok = self.scoring_tokenizer(review, truncation=True, return_tensors="pt", add_special_tokens=False).to(self.args.device)
        review_len = rev_tok.input_ids.size(1)
        remaining_len = self.max_len - review_len
        if remaining_len <= 0:
            return self.compute_crit(review)
        abs_tok = self.scoring_tokenizer(abstract, truncation=True, max_length=remaining_len, return_tensors="pt", add_special_tokens=False).to(self.args.device)
        abstract_len = abs_tok.input_ids.size(1)
        input_ids = torch.cat([abs_tok.input_ids, rev_tok.input_ids], dim=1)
        attention_mask = torch.ones_like(input_ids)
        with torch.no_grad():
            outputs = self.scoring_model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            # Separate out logits of review text for further expectation and variance computations
            logits_score = logits[:, abstract_len:-1, :]
            labels = rev_tok.input_ids[:, 1:]
            if logits_score.size(1) != labels.size(1):
                print(f"Warning: logits_score shape {logits_score.shape} doesn't match labels shape {labels.shape}")
                return self.compute_crit(review)
            if self.args.sampling_model_name == self.args.scoring_model_name:
                logits_ref = logits_score
            else:
                rev_tok_ref = self.sampling_tokenizer(review, truncation=True, return_tensors="pt", add_special_tokens=False).to(self.args.device)
                assert torch.all(rev_tok_ref.input_ids[:, 1:] == labels), "Tokenizer mismatch."
                review_len_ref = rev_tok_ref.input_ids.size(1)
                remaining_len_ref = self.max_len - review_len_ref
                if remaining_len_ref <= 0:
                    return self.compute_crit(review)
                abs_tok_ref = self.sampling_tokenizer(abstract, truncation=True, max_length=remaining_len_ref, return_tensors="pt", add_special_tokens=False).to(self.args.device)
                abstract_len_ref = abs_tok_ref.input_ids.size(1)
                input_ids_ref = torch.cat([abs_tok_ref.input_ids, rev_tok_ref.input_ids], dim=1)
                attention_mask_ref = torch.ones_like(input_ids_ref)
                outputs_ref = self.sampling_model(input_ids=input_ids_ref, attention_mask=attention_mask_ref)
                logits_ref = outputs_ref.logits[:, abstract_len_ref:-1, :]
                labels_ref = rev_tok_ref.input_ids[:, 1:]
                if logits_ref.size(1) != labels_ref.size(1):
                    print(f"Warning: logits_ref shape {logits_ref.shape} doesn't match labels_ref shape {labels_ref.shape}")
                    return self.compute_crit(review)
            res = self.criterion_fn(logits_ref, logits_score, labels)
            crit = res['discrepancy']
            log_likelihood = res['log_likelihood']
        return crit, labels.size(1), log_likelihood


    # compute probability
    def compute_prob(self, review, context=None, only_log_likelihood=False):
        if context is not None and context.strip() and len(context.strip()) > 0:
            crit, ntoken, log_likelihood = self.compute_crit_cxt(review, context)
        else:
            crit, ntoken, log_likelihood = self.compute_crit(review)
        mu0 = self.classifier['mu0']
        sigma0 = self.classifier['sigma0']
        mu1 = self.classifier['mu1']
        sigma1 = self.classifier['sigma1']
        if only_log_likelihood:
            return log_likelihood
        prob = compute_prob_norm(crit, mu0, sigma0, mu1, sigma1)
        return prob, crit, ntoken, log_likelihood
    

def load_existing_results(result_file):
    """Load existing gptzero results from JSON file."""
    if os.path.exists(result_file):
        with open(result_file, 'r') as f:
            return json.load(f)
    return {}

def save_results(results, result_file):
    """Save results to JSON file."""
    os.makedirs(os.path.dirname(result_file), exist_ok=True)
    with open(result_file, 'w') as f:
        json.dump(results, f, indent=4)

def read_file_paths(paths_file):
    """Read file paths from the paths file."""
    with open(paths_file, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def read_text_file(file_path):
    """Read text content from a file."""
    try:
        with open(f'data/{file_path}', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def get_context_from_path(file_path):
    """Extract context from a file path."""
    try:
        parts = file_path.split("/")
        if parts[1] == "hard-subset":
            conference = parts[2]
            i = 3
            if conference.startswith("nips"):
                conference += "/" + parts[i]
                i += 1
            set_name = parts[i]
            i += 1
            paper_number = parts[i]
        else:
            conference = parts[1].lstrip("humanized_data")
            i = 2
            if conference.startswith("nips"):
                conference += "/" + parts[i]
                i += 1
            set_name = parts[i]
            paper_number = parts[-1].strip(".txt").split("_")[0]
        context_path = f"rawdata/{conference}/{set_name}/parsed_pdfs/{paper_number}.pdf.json"

        with open(context_path, "r") as f:
            context_data = json.load(f)
        sections = context_data.get("metadata", {}).get("sections", [])
        for section in sections:
            if "introduction" in section.get("heading", "").lower():
                intro_text = section.get("text", "")
            elif "conclusion" in section.get("heading", "").lower():
                conclusion_text = section.get("text", "")
        context_text = intro_text + " " + conclusion_text
        return context_text
        
    except Exception as e:
        print(f"Error extracting context for {file_path}: {e}")
        return None


def main(args):
    paths_file = "[PATHFILE]"
    result_file = "[DESTINATION_JSON_FILE]"
    
    print("Loading existing results...")
    existing_results = load_existing_results(result_file)
    print(f"Found {len(existing_results)} existing results")
    
    print("Reading file paths...")
    file_paths = read_file_paths(paths_file)
    print(f"Found {len(file_paths)} files to process")
    
    files_to_process = []
    for file_path in file_paths:
        if file_path not in existing_results:
            files_to_process.append(file_path)
    
    print(f"Files to process: {len(files_to_process)}")
    
    if not files_to_process:
        print("All files have already been processed!")
        return
    
    new_results = existing_results.copy()
    processed_count = 0
            
    detector = FastDetectGPT(args)
    
    for i, file_path in enumerate(files_to_process):
        print(f"Processing file {i+1}/{len(files_to_process)}: {os.path.basename(file_path)}")
        
        text = read_text_file(file_path)
        if text is None:
            print(f"Skipping {file_path} due to read error")
            continue
        
        try:
            if args.context:
                context_text = get_context_from_path(file_path)
                context_text = context_text.strip() if context_text else None
                if context_text is None or len(context_text) == 0:
                    print(f"Context not found for {file_path}, using only text")
                    prob, crit, ntokens, log_likelihood = detector.compute_prob(
                        review=text, context=None, only_log_likelihood=args.only_log_likelihood)
                else:
                    prob, crit, ntokens, log_likelihood = detector.compute_prob(
                        review=text, context=context_text, only_log_likelihood=args.only_log_likelihood)
            else:
                prob, crit, ntokens, log_likelihood = detector.compute_prob(
                    review=text, context=None, only_log_likelihood=args.only_log_likelihood)
            new_results[file_path] = {
                "prob": prob,
                "crit": crit,
                "ntokens": ntokens,
                "log_likelihood": log_likelihood
            }
            processed_count += 1
            # Save intermediate results every 100 files
            if processed_count % 100 == 0:
                save_results(new_results, result_file)
                print(f"Saved intermediate results ({processed_count} files processed)")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue

    print("Saving final results...")
    save_results(new_results, result_file)
    print(f"Processing complete! Processed {processed_count} new files.")
    print(f"Total results: {len(new_results)}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sampling_model_name", type=str, default="falcon-7b") # Set to "falcon-7b" or "llama3-8B"
    parser.add_argument("--scoring_model_name", type=str, default="falcon-7b-instruct") # Set to "falcon-7b-instruct" or "llama3-8b-instruct"
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--cache_dir", type=str, default="../cache")
    parser.add_argument("--only_log_likelihood", action="store_true")
    parser.add_argument("--context", action="store_true")
    args = parser.parse_args()
    main(args)