import requests
import tokens

'''
    Description: summarizes text using an LLM to get insight into a lenghty filing.
    Input: text to be summarized.
    Output: a (hopefully good) summary of the text'''
def get_summary(text):
    API_URL = "https://api-inference.huggingface.co/models/human-centered-summarization/financial-summarization-pegasus" ## setup the api and all
    headers = {"Authorization": "Bearer " + tokens.TOKEN_1}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json() ## load the text to be summarized

    output = query({"inputs": text}) ## execute the query
    return output ## return the summary


import requests

def get_sentiment(text):
    API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
    headers = {"Authorization": "Bearer " + tokens.TOKEN_1}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({"inputs": text})
    return output