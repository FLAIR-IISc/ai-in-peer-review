import os
import json
from detector import Binoculars
import argparse


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
            conference = parts[1].removeprefix("humanized_data")
            i = 2
            if conference.startswith("nips"):
                conference += "/" + parts[i]
                i += 1
            set_name = parts[i]
            paper_number = parts[-1].strip(".txt").split("_")[0]
        context_path = f"data/rawdata/{conference}/{set_name}/parsed_pdfs/{paper_number}.pdf.json"

        with open(context_path, "r") as f:
            context_data = json.load(f)
        sections = context_data.get("metadata", {}).get("sections", [])
        for section in sections:
            if "heading" in section and section["heading"] and "introduction" in section["heading"].lower():
                intro_text = section.get("text", "")
            elif "heading" in section and section["heading"] and "conclusion" in section["heading"].lower():
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
    bino = Binoculars()
    
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
                    score = bino.compute_score(text)
                else:
                    score = bino.compute_score_with_context(text, context_text)
            else:
                score = bino.compute_score(text)
            new_results[file_path] = score
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
    parser.add_argument("--context", action="store_true")
    args = parser.parse_args()
            
    main(args)
