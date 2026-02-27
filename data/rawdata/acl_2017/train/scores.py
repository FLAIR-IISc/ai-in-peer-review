import json

def get_gptzero_scores(file_path):
    # Open the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Initialize lists to store the scores
    score_part1 = []
    score_part2 = []
    score_part3 = []
    
    # Iterate over each review and split the "GPTZero" string
    for review in data.get("reviews", []):
        gptzero_scores = review.get("GPTZero", "").split(";")
        
        # Append each part of the score to the respective list
        if len(gptzero_scores) == 3:
            score_part1.append(int(gptzero_scores[0]))
            score_part2.append(int(gptzero_scores[1]))
            score_part3.append(int(gptzero_scores[2]))
    
    return score_part1, score_part2, score_part3

# Example usage
# paper_numbers = [12, 16, 18, 19, 21, 26, 31, 56, 66]
# ai_scores_1 = []
# ai_scores_3 = []
# ai_scores_4 = []
# ai_scores_5 = []
# for paper_number in paper_numbers:
#     file_path = f"reviews_llm/{str(paper_number)}.json"
#     score_part1, score_part2, score_part3 = get_gptzero_scores(file_path)

#     ai_scores_1.append(score_part1[0])
#     ai_scores_3.append(score_part1[1])
#     ai_scores_4.append(score_part1[2])
#     ai_scores_5.append(score_part1[3])

# print("ai_score_1 = ", ai_scores_1)
# print("ai_score_3 = ", ai_scores_3)
# print("ai_score_4 = ", ai_scores_4)
# print("ai_score_5 = ", ai_scores_5)

