import sys
import json
import os
# #filter out level 1 and 4 from subset file and store to another file and then pass it to humanizer and store the result.

# sys.stdout = open("loggings.txt","w")
path_file = "./llm_rev_500_only14.txt"

with open(path_file, "r") as file:
    subset_path_mod = file.readlines()
    
    
# subset_path_mod =[path.strip() for path in subset_path if "level1" in path or "level4" in path] #only include level1 and level4

# with open("llm_rev_500_only14.txt","w") as file:
#     file.write("\n".join(subset_path_mod))
    
start_idx = 1062
end_idx = 2000
#max=2000(0 to 1999)
subset_path_ = subset_path_mod[start_idx:end_idx]
#Write subset path to a file for safekeeping



################
import requests
import time

submit_url = "https://humanize.undetectable.ai/submit"
query_url = "https://humanize.undetectable.ai/document"
api_key = ""
headers = {
"apikey": api_key,
"Content-Type": "application/json"
}

#################
count = start_idx
#Read content of each path and send to humanizer,get response and store it under Responses/
for each_review_file in subset_path_:
    with open(each_review_file,"r") as file:
        org_review = file.read() #review text
    print("\n\nProcessing : ",each_review_file)
    # print("Original Review : ",org_review)
    output_path = each_review_file.replace("/home/naveeja/Project/Human_or_AI/Data_Preprocessing/cleandata/","./Responses/")
    
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir,exist_ok=True)
    
    ###########

    data = {
    "content": org_review,
    "readability": "University",
    "purpose": "Article",
    "strength": "Quality",
    "model": "v2"
    }
    def submit_resp():
        submit_response = requests.post(submit_url, json=data, headers=headers)
        # Print the response
        if submit_response.status_code == 200:
            response_json = submit_response.json()
            document_id = response_json.get("id")  # Extracts the document ID
            print("Document submitted successfully. Document ID:", document_id)
            # Wait for 15 seconds before fetching the result
            print("Waiting for 12 seconds to allow processing...")
            time.sleep(12)
            query_data = {"id": document_id}
            query_response = requests.post(query_url, json=query_data, headers=headers)
            if query_response.status_code == 200:
                response_json = query_response.json()
                # print("Processed Document:", response_json)
                humanized_review = response_json["output"]
                if humanized_review:
                    with open(output_path,"w") as file:
                        file.write(humanized_review)
                    # print("humanized_review : ",humanized_review)
                    print("Written : ",output_path)
                    return "Success"
                else:
                    print("\nReturned NONE once:",each_review_file)
                    #try fetching again after sometime
                    time.sleep(15)
                    query_response = requests.post(query_url, json=query_data, headers=headers)
                    response_json = query_response.json()
                    humanized_review = response_json["output"]
                    if humanized_review:
                        with open(output_path,"w") as file:
                            file.write(humanized_review)
                    # print("humanized_review : ",humanized_review)
                        print("Written : ",output_path)
                        return "Success"    
                    else:
                        print("\nReturned NONE twice:",each_review_file)
                        return "None"
            else:
                print("Error retrieving document:", query_response.status_code, query_response.text)
                return "502"
                
        else:
            print("Error submitting document:", submit_response.status_code, submit_response.text)
            return "SubmissionFailed"
    
    status = submit_resp()
    if status=="Success":
        print("Index done :",count)
        count += 1
        continue
    elif status == "None" or  status == "502" or  status == "SubmissionFailed":
        #try submitting again 
        print("STATUS@ :", status)
        time.sleep(15)
        status = submit_resp()
        if status !="Success":
            print("Failed again at :",each_review_file)
            print("STATUS@ :", status)
            break
        print("Index done :",count)
        count += 1
    

    
print("ALL DONE!!!")
    ######