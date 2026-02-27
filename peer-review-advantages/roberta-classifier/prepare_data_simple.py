import json
import os
import argparse
import re
import pandas as pd
from tqdm import tqdm
from nltk.tokenize import word_tokenize, TreebankWordDetokenizer

parser = argparse.ArgumentParser()
parser.add_argument('--path_file', required=True, help='path to file containing list of paths to reviews')
parser.add_argument('--fragment', type=int, default=None, help='if specified, break reviews into fragments of that many words for feature extraction')
parser.add_argument('--overlap', type=int, default=0, help='if fragmenting, number of overlapping words between fragments, only applicable if fragment is not None')
parser.add_argument('--fragmentation_level', type=str, default='char', choices=['word', 'char'], help='level at which to fragment text')
parser.add_argument('--output_file', type=str, required=True, help='path to output csv file')
args = parser.parse_args()

detok = TreebankWordDetokenizer()


def extract_paper_fp_from_review_fp(review_filepath):
    ## extract the paper contents 
    # pattern = r".*cleandata/(.*)/(train|test|dev)/.*(level[1-4]|reviews)/(.*)_([1-9]*).txt"
    pattern = "SO THAT IT IS NEVER MATCHED" 
    match = re.search(pattern, review_filepath)
    
    if match is not None:
        conference = match.group(1)
        split = match.group(2)
        level = match.group(3)
        paper_number = match.group(4)
        reviewer_number = match.group(5)

        # return conference, split, level, paper_number, reviewer_number
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

def fragment_text(text, fragment_size, overlap_size=0):
    
    if args.fragmentation_level == 'word':
        words = word_tokenize(text)
        fragments = []
        start = 0
        while start < len(words):
            end = min(start + fragment_size, len(words))
            # fragment = ' '.join(words[start:end])
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
            # fragment = ' '.join(words[start:end])
            fragment = text[start:end]
            
            fragments.append(fragment)
            if end == len(text):
                break
            start = end - overlap_size
        return fragments
    else:
        raise ValueError("Invalid fragmentation level specified.")

data_dict = {}

def get_label(review_id):
    label = "reviews"
    for i in range(1,5):
        if f"level{i}" in review_id:
            label = f"level{i}"

    return label

def get_split(review_id):
    for split in ['train', 'test', 'dev']:
        if f"/{split}/" in review_id:
            ans = split
            break
            
    return ans


with open(args.path_file, 'r') as fin:
    for line in tqdm(fin):
        review_filepath = line.strip()
        
        try:
            review_text = open(review_filepath.replace('/home/naveeja/Project/Human_or_AI/Data_Preprocessing/cleandata', '/home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata'), 'r').read().strip()
        except:
            review_text = open(review_filepath, 'r').read().strip()


        if args.fragment is not None:
            review_texts_buffer = fragment_text(review_text, args.fragment, args.overlap)
            review_ids_buffer = [review_filepath + f"_fragment_{i}" for i in range(len(review_texts_buffer))]
        else:
            review_texts_buffer = [review_text]
            review_ids_buffer = [review_filepath]
        
        label = get_label(review_filepath)
        split = get_split(review_filepath)
        for review_id, review_text in zip(review_ids_buffer, review_texts_buffer):
            data_dict[review_id] = {
                'text': review_text,
                'label': label,
                'split': split
            }


# make a pandas dataframe from linguistic_features_dict
df = pd.DataFrame.from_dict(data_dict, orient='index')

df.to_csv(args.output_file, index_label='path')