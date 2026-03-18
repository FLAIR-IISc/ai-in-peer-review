import json
import re
import os
from openai import AzureOpenAI, OpenAI
import time
import yaml
#old
# def clean_text(text):
    
#     numbers = re.findall(r'(\d+)\n', text)
#     cleaned_text = text
#     for number in numbers:
#         cleaned_text = cleaned_text.replace(f'{number}\n', '')
#     # print(cleaned_text, numbers)
#     return cleaned_text

#new
def clean_text(text):
    cleaned_text = re.sub(r'\n(\d+\n)+', '', text)
    return cleaned_text

#old
# def get_paper(paper_address, paper_number):
#     final_address = f'{paper_address}/parsed_pdfs/{paper_number}.pdf.json'
#     with open(final_address, "r", encoding='utf-8') as file:
#         data = json.load(file)
#     data_dict = {}
#     sections = data.get('metadata', {}).get('sections', [])
#     final_string = ""
#     for section in sections:
#         heading = section.get('heading')
#         text = section.get('text')
#         text = clean_text(text)
#         data_dict[heading] = text
#         if(heading!= None and text!= None):
#             final_string += "##"+heading + "\n\n" + text
#     return final_string

#new
def get_paper(paper_address, paper_number):
    final_address = f'{paper_address}/parsed_pdfs/{paper_number}.pdf.json'
    with open(final_address, "r", encoding='utf-8') as file:
        data = json.load(file)
    data_dict = {}
    final_string = ""
    abstract_text = data.get('metadata', {}).get('abstractText',"")
    if len(abstract_text)>0:
        final_string += "Abstract" + "\n" + abstract_text +"\n"
    sections = data.get('metadata', {}).get('sections', [])
    if sections: #sections = null exists in data
        for section in sections:
            heading = section.get('heading')
            text = section.get('text')
            text = clean_text(text)
            data_dict[heading] = text
            if(heading!= None and text!= None and heading != "Acknowledgements"):
                final_string += heading + "\n" + text + "\n"

    return final_string

def preprocess_iclr(json_data):

    seen_combinations = set()
    unique_reviews = []
    seen_reviewer = []

    for review in json_data.get("reviews", []):
        other_key = review.get("OTHER_KEYS")
        title = review.get("TITLE")
        comments = review.get("comments")
        if comments and other_key:
            unique_identifier = (other_key, title)
            if 'AnonReviewer' in other_key and  unique_identifier not in seen_combinations:
                seen_combinations.add(unique_identifier)    
                if other_key in seen_reviewer:
                    for rev in unique_reviews:
                        if rev.get("OTHER_KEYS") == other_key:
                            rev["comments"] = rev.get("comments")+ "\n" +comments
                else:
                    seen_reviewer.append(other_key)               
                    unique_reviews.append(review) 

    json_data["reviews"] = unique_reviews
    # print(unique_reviews)
    return json_data


def summarize(comments, level, llm_name, temperature):
    if(level =="3"):
        prompt_template = "summarization_3_prompt"
    if(level =="4"):
        prompt_template = "summarization_4_prompt"
    
    prompt_path = "AI_generation/prompts.yaml"
    with open(prompt_path) as f:
        prompts = yaml.safe_load(f)
    prompt_template = prompts.get(prompt_template, None)

    summarization_prompt = make_prompt(prompt_template=prompt_template, paper_contents= "", human_input=comments)

    summarized_comments = llm_call(summarization_prompt, llm_name, temperature=temperature)
    summarized_comments = extract_answer(summarized_comments)
    return summarized_comments

#modified
def get_human_review_all(paper_address, paper_number):
    final_address = f'{paper_address}/reviews/{paper_number}.json'
    with open(final_address, "r", encoding='utf-8') as file:
        data = json.load(file)
    if "iclr" in final_address:
        data = preprocess_iclr(data)
    # Extracting the comments section from the reviews
    all_reviews = []
    for review in data.get("reviews", []):
        if review:
            comments = review.get("comments", "")
            if comments:
                all_reviews.append(comments)
                
    return all_reviews
    # reviews = data.get('reviews', [])
    # comments_string = ""

    # comments = reviews[0].get('comments', "")
    # if comments:
    #     comments_string += comments + "\n\n"  
    #     if(level=="3" or level =="4"):
    #         comments_string = summarize(comments_string, level, llm_name, temperature)

    # return comments_string


def make_prompt(prompt_template, paper_contents, human_input):
    formatted_prompt = prompt_template.format(
            PaperInPromptFormat=paper_contents,
            HumanInput = human_input
        )
    return formatted_prompt

# complete this
def llm_call(prompt, llm_name, temperature=0.3):
    
    # api_key = os.environ.get("OPENAI_API_KEY")
    # api_endpoint = os.environ.get("OPENAI_ENDPOINT")
    # api_version = os.environ.get("OPENAI_VERSION")

    # client = AzureOpenAI(api_key=api_key, azure_endpoint=api_endpoint, api_version=api_version)
    
    # while True:
    #     try:
    #         messages = [{"role": "user", "content": prompt}]
    #         response = client.chat.completions.create(model = llm_name, temperature= temperature, messages=messages)
    #         # print(response)
    #         return response.choices[0].message.content
    #     except Exception as e:
    #         pass
    #         print(f"Got error {e}. Sleeping for 5 seconds...")
    #         time.sleep(5)    
      
    # populate this
    client = OpenAI(
    api_key = "",
    organization='',
    project='',
    )
    messages = [{"role": "user", "content": prompt}]
    complete = False
    while(not complete):
        try:
            result = client.chat.completions.create(
                model=llm_name,
                messages=messages,
                temperature=temperature
            )
            complete = True
        except Exception as e: 
            print(e)
    final_answer = result.choices[0].message.content
    return final_answer

def extract_answer(answer_string):
    # start_tag = "<Answer>"
    # end_tag = "</Answer>"

    # Check if both <Answer> and </Answer> are present
    # pattern = r"<Answer>(.*?)<\/Answer>"
    # match = re.search(pattern, answer_string, re.DOTALL)
    
    # if match:
    #     return match.group(1).strip()
    
    # # Check if only <Answer> is present
    # if start_tag in answer_string and end_tag not in answer_string:
    #     return answer_string.split(start_tag, 1)[-1].strip()
    
    # # If no tags are present, return as is
    return answer_string.strip()

# changed this added level
# old
# def write_review(paper_address, paper_number, Review, level):
#     # Check if the directory 'reviews_llm' exists, and if not, create it
#     reviews_llm_dir = os.path.join(paper_address, 'reviews_llm')
#     if not os.path.exists(reviews_llm_dir):
#         os.makedirs(reviews_llm_dir)
    
#     # Define the final address for the JSON file
#     final_address = os.path.join(reviews_llm_dir, f'{paper_number}.json')
    
#     # Check if the file already exists
#     if os.path.exists(final_address):
#         # Read the existing data from the file
#         with open(final_address, 'r', encoding='utf-8') as json_file:
#             data = json.load(json_file)
#     else:
#         # If the file does not exist, create the structure
#         data = {"reviews": []}
    
#     # Append the new review to the 'reviews' list
#     new_review = {
#         # "level": level,
#         "comments": Review,
#         "GPTZero":";;",
#     }
#     data["reviews"].append(new_review)
    
#     # Write the updated data back to the file
#     with open(final_address, 'w', encoding='utf-8') as json_file:
#         json.dump(data, json_file, ensure_ascii=False, indent=4)

#     return final_address


#modified
def write_review(reviews_llm_dir, paper_number, Review):    #reviews_llm_dir = ""../data/nips_2013-2017/2017/test/reviews_llama_3_1_70b/level1"
    final_address = os.path.join(reviews_llm_dir, f'{paper_number}.json')
    # Check if the file already exists
    if os.path.exists(final_address):
        # Read the existing data from the file
        with open(final_address, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    else:
        # If the file does not exist, create the structure
        data = {"reviews": []}
    
    # Append the new review to the 'reviews' list
    new_review = {
        "comments": Review,
    }
    data["reviews"].append(new_review)
    
    # Write the updated data back to the file
    with open(final_address, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)





