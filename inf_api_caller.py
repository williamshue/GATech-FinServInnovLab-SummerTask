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