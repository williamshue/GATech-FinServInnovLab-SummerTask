import requests
import tokens

# API_URL = "https://api-inference.huggingface.co/models/human-centered-summarization/financial-summarization-pegasus"
# headers = {"Authorization": "Bearer " + tokens.TOKEN_1}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

# # Load the text file content
# # with open('/Users/w/Documents/GATech-FinServInnovLab-SummerTask/sec-edgar-filings/AAPL/10-K/0001047469-97-006960/full-submission.txt', 'r', encoding='utf-8') as file:
# #     file_content = file.read()

# # Call the API with the loaded text
# output = query({"inputs": "the potential effects of technological changes and other risks and uncertainties detailed under “Certain Factors Affecting Results of Operations” in Part II, Item 7,Competition and Regulation in Part I, Item 1 and throughout this report.    Accordingly, you are cautioned not to place undue reliance on forward-looking statements, which speak only as of the date on which they are made. Morgan Stanley undertakes no obligation to update publicly or reviseany forward-looking statements to reflect the impact of circumstances or events that arise after the dates they are made, whether as a result of new information, future events or otherwise. You should, however, consult further disclosures MStanley may make in future filings of its Annual Report on Form 10-K, Quarterly Reports on Form 10-Q and Current Reports on Form 8-K, and any amendments thereto"
#                 })

# print(output)

import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# headers = {"Authorization": "Bearer " + tokens.TOKEN_1}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Process the file in chunks of 1000 lines
def process_file(file_path):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            lines = ''.join([file.readline() for _ in range(1000)])
            if not lines:
                break
            results.append(query({"inputs": lines}))
    return results

output = process_file('/Users/w/Documents/GATech-FinServInnovLab-SummerTask/sec-edgar-filings/AAPL/10-K/0001047469-97-006960/full-submission.txt')
print(output)

## other models to use: 
## ProsusAI/finbert
## human-centered-summarization/financial-summarization-pegasus
## nickmuchi/distilroberta-finetuned-financial-text-classification