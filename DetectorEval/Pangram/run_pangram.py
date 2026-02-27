import json
import os
from pathlib import Path
from pangram import Pangram

pangram_client = Pangram(api_key=os.getenv("PANGRAM_API_KEY"))

def call_pangram(text):
    return pangram_client.predict(text)  

def load_existing_results(result_file):
    """Load existing Pangram results from JSON file."""
    if os.path.exists(result_file.replace("/home/naveeja/Project/Human_or_AI", "/home/rounak/ai-involvement-in-peer-reviews")):
        with open(result_file.replace("/home/naveeja/Project/Human_or_AI", "/home/rounak/ai-involvement-in-peer-reviews"), 'r') as f:
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
        with open(file_path.replace("/home/naveeja/Project/Human_or_AI", "/home/rounak/ai-involvement-in-peer-reviews"), 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def main():
    # File pathsd
    paths_file = "[PATHFILE]"
    result_file = "[DESTINATION_JSON_FILE]"
    
    print("Loading existing results...")
    existing_results = load_existing_results(result_file)
    print(f"Found {len(existing_results)} existing results")
    
    print("Reading file paths...")
    file_paths = read_file_paths(paths_file)
    print(f"Found {len(file_paths)} files to process")
    
    # Find files that haven't been processed yet
    files_to_process = []
    for file_path in file_paths:
        if file_path not in existing_results:
            files_to_process.append(file_path)
    
    print(f"Files to process: {len(files_to_process)}")
    
    if not files_to_process:
        print("All files have already been processed!")
        return
    
    # Process remaining files
    new_results = existing_results.copy()
    processed_count = 0
    
    for i, file_path in enumerate(files_to_process):
        print(f"Processing file {i+1}/{len(files_to_process)}: {os.path.basename(file_path)}")
        
        # Read text content
        text = read_text_file(file_path)
        if text is None:
            print(f"Skipping {file_path} due to read error")
            continue
        
        # Call Pangram
        try:
            pangram_score = call_pangram(text)
            new_results[file_path] = pangram_score
            processed_count += 1
            
            # Save intermediate results every 5 files
            if processed_count % 10 == 0:
                save_results(new_results, result_file)
                print(f"Saved intermediate results ({processed_count} files processed)")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue

        
    
    # Save final results
    print("Saving final results...")
    save_results(new_results, result_file)
    print(f"Processing complete! Processed {processed_count} new files.")
    print(f"Total results: {len(new_results)}")

if __name__ == "__main__":
    main()