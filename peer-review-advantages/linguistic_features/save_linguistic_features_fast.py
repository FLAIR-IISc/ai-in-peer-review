#!/usr/bin/env python

import os

# --- Limit BLAS / NumPy threading so process-level parallelism scales better ---
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

from FeatureExtractor import StyloAIFeatureExtractor
import json
import argparse
import re
from joblib import Parallel, delayed, cpu_count
from tqdm import tqdm
from nltk.tokenize import word_tokenize, TreebankWordDetokenizer

# ---------------------------------------------------------------------------
# Global, per-process extractor (lazy init)
# ---------------------------------------------------------------------------

_extractor = None


def get_extractor():
    """Lazily initialize the heavy StyloAIFeatureExtractor once per process."""
    global _extractor
    if _extractor is None:
        _extractor = StyloAIFeatureExtractor()
    return _extractor


# Reasonable default; you can tweak if you want, but no new CLI args needed.
BATCH_SIZE = 64


def chunked(seq, size):
    """Yield successive chunks of size `size` from list-like `seq`."""
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


# ---------------------------------------------------------------------------
# Argument parsing (same interface as before)
# ---------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('--path_file', required=True, help='path to file containing list of paths to reviews')
parser.add_argument('--source_dir', required=True, help='source directory containing reviews')
parser.add_argument('--output_dir', required=True, help='directory to save linguistic features')
parser.add_argument('--suffix', required=True, help='string suffix to append to filename wo which linguistic features are saved')
parser.add_argument('--with_context', action='store_true', help='whether to compute context overlap features')
parser.add_argument('--fragment', type=int, default=None,
                    help='if specified, break reviews into fragments of that many words for feature extraction')
parser.add_argument('--overlap', type=int, default=0,
                    help='if fragmenting, number of overlapping words between fragments, only applicable if fragment is not None')
parser.add_argument('--num_workers', type=int, default=16, help='number of parallel workers to use')
parser.add_argument('--fragmentation_level', type=str, default='char',
                    choices=['word', 'char'], help='level at which to fragment text')
parser.add_argument('--rewrite', action='store_true',
                    help='even if destination file exists, recalculate for all examples and overwrite')

args = parser.parse_args()

out_filepath = os.path.join(
    args.output_dir,
    args.source_dir.split('/')[-1],
    f"linguistic_features_{args.suffix}.json"
)

detok = TreebankWordDetokenizer()

if os.path.exists(out_filepath) and not args.rewrite:
    linguistic_features_dict = json.load(open(out_filepath, 'r'))
else:
    linguistic_features_dict = {}


# ---------------------------------------------------------------------------
# Helpers copied from original script
# ---------------------------------------------------------------------------

def extract_paper_fp_from_review_fp(review_filepath):
    """Extract metadata from review filepath and construct paper path & identifiers."""
    # pattern = r".*cleandata/(.*)/(train|test|dev)/.*(level[1-4]|reviews)/(.*)_([1-9]*).txt"
    pattern = "SO THAT IT IS NEVER MATCHED"  
    match = re.search(pattern, review_filepath)

    if match is not None:
        conference = match.group(1)
        split = match.group(2)
        level = match.group(3)
        paper_number = match.group(4)
        reviewer_number = match.group(5)

        generating_model = "OLD PARSER FUNCTION: GENRATING MODEL NOT PARSED"
        prompt = f"{level}@NAV" if level != "reviews" else "DIVINE BENEVOLENCE"

    else:
        pattern = r".*hard-subset/(.*)/(train|test|dev)/(.*)/(level[1-4]|reviews)/(.*).txt"
        match = re.search(pattern, review_filepath)

        conference = match.group(1)
        split = match.group(2)
        paper_number = match.group(3)
        level = match.group(4)

        if '/' in match.group(5):
            generating_model = match.group(5).split('/')[0]
            fileid = match.group(5).split('/')[1]
        else:
            generating_model = "human_review"
            fileid = match.group(5)

        if ":::" in fileid:
            reviewer_number = fileid.split(":::")[-1]
            prompt = fileid.split(":::")[0]
        else:
            reviewer_number = fileid
            if level != "reviews":
                prompt = f"{level}@NAV"
            else:
                prompt = "DIVINE BENEVOLENCE"

    return conference, split, level, paper_number, reviewer_number, generating_model, prompt


def remove_linenumbers(text):
    return re.sub(r'^\s*\d+\s*\n?', '', text, flags=re.MULTILINE)


def format_paper_contents(paper_contents):
    buffer = ""

    if "metadata" in paper_contents.keys() and "title" in paper_contents["metadata"].keys() and \
            paper_contents["metadata"]["title"] is not None:
        title = remove_linenumbers(paper_contents["metadata"]["title"].strip())
        buffer += f"{title}\n\n"

    if "abstractText" in paper_contents["metadata"].keys() and paper_contents["metadata"]["abstractText"] is not None:
        abstract = remove_linenumbers(paper_contents["metadata"]["abstractText"].strip())
        buffer += f"ABSTRACT\n{abstract}\n\n"

    if "sections" in paper_contents["metadata"].keys() and paper_contents["metadata"]["sections"] is not None:
        for section in paper_contents["metadata"]["sections"]:
            if section["heading"] is None:
                continue
            section_heading = section["heading"]
            section_text = remove_linenumbers(section["text"])

            buffer += f"{section_heading}\n{section_text}\n\n"

    if "references" in paper_contents["metadata"].keys() and paper_contents["metadata"]["references"] is not None:
        buffer += "References:\n"
        for reference in paper_contents["metadata"]["references"]:
            for ref_field in reference.keys():
                if reference[ref_field] is None:
                    continue

                if isinstance(reference[ref_field], str):
                    ref_text = remove_linenumbers(reference[ref_field])
                    buffer += f"{ref_text}, "
                elif isinstance(reference[ref_field], list):
                    for itm in reference[ref_field]:
                        buffer += f"{remove_linenumbers(itm)}, "

            buffer += "\n\n"

    return buffer.strip()


def extract_paper_contents_from_filepath(paper_filepath):
    with open(paper_filepath, "r") as fin:
        file_content = json.load(fin)

    return format_paper_contents(file_content)


def fragment_text(text, fragment_size, overlap_size=0):
    if args.fragmentation_level == 'word':
        words = word_tokenize(text)
        fragments = []
        start = 0
        while start < len(words):
            end = min(start + fragment_size, len(words))
            fragment = detok.detokenize(words[start:end])
            fragments.append(fragment)
            if end == len(words):
                break
            start = end - overlap_size
        return fragments
    elif args.fragmentation_level == 'char':
        fragments = []
        start = 0
        while start < len(text):
            end = min(start + fragment_size, len(text))
            fragment = text[start:end]
            fragments.append(fragment)
            if end == len(text):
                break
            start = end - overlap_size
        return fragments
    else:
        raise ValueError("Invalid fragmentation level specified.")


# ---------------------------------------------------------------------------
# Batch worker for joblib
# ---------------------------------------------------------------------------

def process_batch(batch, paper_dict):
    """
    Process a batch of (path, review_text, paper_fp) triples.

    Returns: list of (path, feature_dict)
    """
    extractor = get_extractor()
    results = []
    for path, review_text, paper_fp in batch:
        context_text = paper_dict.get(paper_fp)
        feats = extractor.extract_all_features(review_text, context_text)
        results.append((path, feats))
    return results


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

if args.source_dir.endswith('/'):
    args.source_dir = args.source_dir[:-1]

paths = []
review_texts = []
paper_dict = dict()
paper_texts = []  # actually stores paper filepaths (keys into paper_dict)

with open(args.path_file, 'r') as fin:
    for line in tqdm(fin):
        review_filepath = line.strip()

        if review_filepath in linguistic_features_dict.keys():
            continue

        try:
            # print(review_filepath.replace('/home/naveeja/Project/Human_or_AI/Data_Preprocessing/cleandata/', args.source_dir))
            current_review_text = open(
                review_filepath.replace('/home/naveeja/Project/Human_or_AI/Data_Preprocessing/cleandata', args.source_dir),
                'r'
            ).read().strip()
        except Exception:
            conference, split, level, paper_number, reviewer_number, generating_model, prompt = \
                extract_paper_fp_from_review_fp(review_filepath)
            review_fp = os.path.join(
                args.source_dir,
                f"{conference}/{split}/{paper_number}/{level}/{generating_model if level != 'reviews' else ''}/{prompt}:::{reviewer_number}.txt"
            )

            review_texts_buffer = []

            try:
                current_review_text = open(
                    review_filepath.replace('/home/rounak/Downloads/hard-subset', args.source_dir),
                    'r'
                ).read().strip()
            except Exception:
                current_review_text = open(review_fp, 'r').read().strip()

        if args.fragment is not None:
            review_texts_buffer = fragment_text(current_review_text, args.fragment, args.overlap)
            paths.extend([review_filepath + f"_fragment_{i}" for i in range(len(review_texts_buffer))])
        else:
            review_texts_buffer = [current_review_text]
            paths.append(review_filepath)

        review_texts.extend(review_texts_buffer)

        if args.with_context:
            paper_fp = f"/home/rounak/ai-involvement-in-peer-reviews/data/{conference}/{split}/parsed_pdfs/{paper_number}.pdf.json"
            paper_dict[paper_fp] = extract_paper_contents_from_filepath(paper_fp)
        else:
            try:
                paper_fp = f"/home/rounak/ai-involvement-in-peer-reviews/data/{conference}/{split}/parsed_pdfs/{paper_number}.pdf.json"
            except:
                paper_fp = review_filepath
            
            
            paper_dict[paper_fp] = None

        paper_texts.extend([paper_fp] * len(review_texts_buffer))

print(cpu_count())
print(len(paths), len(review_texts), len(paper_texts))


# Build items and batches
items = list(zip(paths, review_texts, paper_texts))
batches = list(chunked(items, BATCH_SIZE))

# Parallel feature extraction with batched jobs and lazy per-process extractor
results_batches = Parallel(n_jobs=min(cpu_count(), args.num_workers))(
    delayed(process_batch)(batch, paper_dict) for batch in tqdm(batches, desc="Extracting features")
)

# Flatten and fill linguistic_features_dict
for batch in results_batches:
    for path, result_dict in batch:
        linguistic_features_dict[path] = result_dict

os.makedirs(os.path.dirname(out_filepath), exist_ok=True)
with open(out_filepath, 'w') as fout:
    json.dump(linguistic_features_dict, fout, indent=4)
