import os
from utils import *
import sys
import time

outputpath_model = "gpt_4o_latest"
llm_name = "chatgpt-4o-latest"

from ftfy import fix_text
def remove_markdown(text):
    text = re.sub(r"#+\s*", "", text) # Remove headings (###, ##, #)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)  # Remove **bold**
    text = re.sub(r"\*(.*?)\*", r"\1", text)  # Remove *italic*
    text = re.sub(r"_(.*?)_", r"\1", text)  # Remove _italic_
    text = re.sub(r"\n{2,}", "\n", text)  # Reduce multiple newlines to 1
    text = text.strip() 
    return text

def generate_level1(data_dir,guideline_in_prompt,output_format,prompt_template):
    # folders = os.listdir(data_dir) #dev,test,train folders
    folders = ['dev','test','train']
    for folder in folders:
        folderpath = os.path.join(data_dir,folder) #../data/nips_2013-2017/2017/test
        parsed_pdfs = os.path.join(folderpath,"parsed_pdfs")
        
        output_path = os.path.join(folderpath,outputpath_model)
        os.makedirs(output_path, exist_ok=True)
        
        file_output_path = os.path.join(output_path,"level1")
        os.makedirs(file_output_path, exist_ok=True)
        
        for each_paper in os.listdir(parsed_pdfs):
            paper_name = each_paper.split('.')[0]
            PaperString = get_paper(folderpath,paper_name)
            complete_prompt = prompt_template.format(guidelines= guideline_in_prompt,
                                                     PaperInPromptFormat=PaperString)
                                                    #  OutputFormat=output_format)
            print('#'*50)
            print(complete_prompt)
            answer = llm_call(complete_prompt,llm_name)
            print("$"*50)
            print(answer)
            print("$"*50)
            write_review(file_output_path, paper_name, answer) 

def generate_level2(data_dir,guideline_in_prompt,output_format,prompt_template):
    # folders = os.listdir(data_dir) #dev,test,train folders
    folders = ['dev','test','train']
    for folder in folders:
        folderpath = os.path.join(data_dir,folder) #../data/nips_2013-2017/2017/test
        parsed_pdfs = os.path.join(folderpath,"parsed_pdfs")
        output_path = os.path.join(folderpath,outputpath_model)
        os.makedirs(output_path, exist_ok=True)
        file_output_path = os.path.join(output_path,"level2")
        os.makedirs(file_output_path, exist_ok=True)
        
        for each_paper in os.listdir(parsed_pdfs): 
            paper_name = each_paper.split('.')[0]
            PaperString = get_paper(folderpath,paper_name)
            complete_prompt = prompt_template.format(guidelines= guideline_in_prompt,
                                                     PaperInPromptFormat=PaperString)
                                                    #  OutputFormat=output_format)
            print('#'*50)
            print(complete_prompt)
            answer = llm_call(complete_prompt,llm_name)
            print("$"*50)
            print(answer)
            print("$"*50)
            write_review(file_output_path, paper_name, answer) 

def generate_level3(data_dir,guideline_in_prompt,output_format,summarize_prompt,generatn_prompt):
    # folders = os.listdir(data_dir) #dev,test,train folders  
    folders = ['dev','test','train']  
    for folder in folders:
        folderpath = os.path.join(data_dir,folder) #../data/nips_2013-2017/2017/test
        human_reviews = os.path.join(folderpath,"reviews")
        output_path = os.path.join(folderpath,outputpath_model)
        os.makedirs(output_path, exist_ok=True)
        
        file_output_path = os.path.join(output_path,"level3")
        os.makedirs(file_output_path, exist_ok=True)
        
        for each_paper in os.listdir(human_reviews): 
            paper_name = each_paper.split('.')[0]
            # print(f"paper_name : {paper_name}")
            human_reviews = get_human_review_all(folderpath,paper_name)
            PaperString = get_paper(folderpath,paper_name)
            for each_review in human_reviews:
                complete_prompt = summarize_prompt.format(humanreview = each_review)
                                                        #   OutputFormat=output_format)
                
                
                print(f"Level 3 summarization :\n{complete_prompt}")
                print('#'*50)
                each_summarized = llm_call(complete_prompt,llm_name)
                clean_summarized = remove_markdown(each_summarized)
                clean_summarized = fix_text(clean_summarized)
                complete_prompt = generatn_prompt.format(summarized_humanreview = clean_summarized,
                                                                guidelines=guideline_in_prompt,
                                                                PaperInPromptFormat=PaperString)
                                                                # OutputFormat=output_format)
                print(f"Level 3 generation :\n{complete_prompt}")
                print('#'*50)
                answer = llm_call(complete_prompt,llm_name)
                print("$"*50)
                print(answer)
                print("$"*50)
                write_review(file_output_path, paper_name, answer)

def generate_level4(data_dir,output_format,prompt_template):
    # folders = os.listdir(data_dir) #dev,test,train folders
    folders = ['dev','test','train']
    for folder in folders:
        folderpath = os.path.join(data_dir,folder) #../data/nips_2013-2017/2017/test
        human_reviews = os.path.join(folderpath,"reviews")
        output_path = os.path.join(folderpath,outputpath_model)
        os.makedirs(output_path, exist_ok=True)
        
        file_output_path = os.path.join(output_path,"level4")
        os.makedirs(file_output_path, exist_ok=True)
        
        for each_paper in os.listdir(human_reviews): 
            paper_name = each_paper.split('.')[0]
            # print(f"paper_name : {paper_name}")
            human_reviews = get_human_review_all(folderpath,paper_name)
            
            for each_review in human_reviews:
                complete_prompt = prompt_template.format(humanreview = each_review)
                                                        #  OutputFormat=output_format)
                print('#'*50)
                print(complete_prompt)
                answer = llm_call(complete_prompt,llm_name)
                print("$"*50)
                print(answer)
                print("$"*50)
                write_review(file_output_path, paper_name, answer) 

def generate_llm_review(data_dir,level,conference):
    prompt_path = "./prompts.yaml"
    guidelines_path = "./guidelines.yaml"

    with open(prompt_path) as f:
        promptsyaml = yaml.safe_load(f)
        
    with open(guidelines_path) as f:
        guidelinesyaml = yaml.safe_load(f)
        
    guideline_in_prompt = guidelinesyaml.get(conference,None)
    if not guideline_in_prompt:
        print("Guidelines not loaded properly")
    output_format = promptsyaml.get("output_format",None)

    # folders = os.listdir(data_dir) #dev,test,train folders
    if level == '1':
        prompt_template_name = f"level_{level}_prompt"
        prompt_template = promptsyaml.get(prompt_template_name, None)
        generate_level1(data_dir,guideline_in_prompt,output_format,prompt_template)
        
    elif level == '2':
        prompt_template_name = f"level_{level}_prompt"
        prompt_template = promptsyaml.get(prompt_template_name, None)
        generate_level2(data_dir,guideline_in_prompt,output_format,prompt_template)
        
    elif level == '3':
        summarize_prompt = promptsyaml.get("level_3_summarizationprompt", None)
        generatn_prompt = promptsyaml.get("level_3_generation", None)
        generate_level3(data_dir,guideline_in_prompt,output_format,summarize_prompt,generatn_prompt)
        
    elif level == '4':
        prompt_template_name = f"level_{level}_prompt"
        prompt_template = promptsyaml.get(prompt_template_name, None)
        generate_level4(data_dir,output_format,prompt_template)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py '../data/nips_2013-2017/2017/' '1' 'nips'")
        print("where \n directory to process : '../data/nips_2013-2017/2017/ \n Level: '1' \n Guidelines:'nips'(check guidelines.yaml)")
        sys.exit(1)
    start_time = time.time()
    data_dir = sys.argv[1]
    level = sys.argv[2]
    conference = sys.argv[3]
    print("Processing directory :",data_dir)
    print("Level :",level)
    print("Using guidelines from :",conference)
    loggingfile = f"loggings{level}.txt"
    sys.stdout = open(loggingfile, "w")
    # tokenizer, model = load_model()
    # print("Successfully loaded model!")
    
    # data_dir = [ "../data/acl_2017/",
    #                  "../data/conll_2016/",
    #                   "../data/iclr_2017/",
    #                    "../data/nips_2013-2017/2013/",
    #                     "../data/nips_2013-2017/2014/",
    #                      "../data/nips_2013-2017/2015/",
    #                       "../data/nips_2013-2017/2016/",
    #                        "../data/nips_2013-2017/2017/"]

    # data_dir = ["../data/nips_2013-2017/2017/"]
    
    generate_llm_review(data_dir,level,conference)
    print(f"\n{data_dir} level {level} took {(time.time()-start_time)/60} min")