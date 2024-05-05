# from sec_edgar_downloader import Downloader
# import os

# def fetch_filings():
#     # init downloader
#     dl = Downloader("YourCompanyName", "your-email@company.com")
    
#     # specify companies and tickers
#     companies = {
#         "JPM": "JPMorgan Chase & Co.",
#         "MSFT": "Microsoft Corp",
#         "AAPL": "Apple Inc."
#     }

#     for ticker, _ in companies.items():
#         # download filings
#         dl.get("10-K", ticker, after="1995-01-01", before="2024-01-01")

# fetch_filings()

########################################################################################################################################################

import requests
import tokens

def get_summary(text):
    API_URL = "https://api-inference.huggingface.co/models/human-centered-summarization/financial-summarization-pegasus"
    headers = {"Authorization": "Bearer " + tokens.TOKEN_1}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({"inputs": text})
    return output


import requests

def get_sentiment(text):
    API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
    headers = {"Authorization": "Bearer " + tokens.TOKEN_1}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({"inputs": text})
    return output



import os
import parse_10K

def find_file_paths(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            ## 0: all, 1: business description, 2: risk, 3: management discussion and analysis.
            ## overall_sum = get_summary(parse_10K.parse_10k_filing(filepath, 0))
            biz_des_sum = get_summary(parse_10K.parse_10k_filing(filepath, 1))
            # risk_sum = get_summary(parse_10K.parse_10k_filing(filepath, 2))
            # mgmt_sum = get_summary(parse_10K.parse_10k_filing(filepath, 3))

            text = biz_des_sum[0]['summary_text']
            print(text)
            #biz_sentiment = get_sentiment(biz_des_sum)
            #print(biz_sentiment)
            # risk_sentiment = get_sentiment(risk_sum)
            # mgm_sentiment = get_sentiment(mgmt_sum)

            exit()

# Example usage
root_directory = './sec-edgar-filings'  # Replace with the actual root directory path
find_file_paths(root_directory)
