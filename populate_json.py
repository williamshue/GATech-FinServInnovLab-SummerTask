import os
import parse_10K
import numpy
import json
import time
import inf_api_caller 

'''
    Description: this file populates a json with with all the data from the downloaded sec filings
    Input: the function takes the path to the directory containing the sec filings
    Output: a file named data.json containing the processed data from the sec filings'''
def popjson(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir): ## loop over all files in the directoy and sub dirs.
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            ticker = filepath.split('/')[2]

            year_str = filepath.split('-')[4] ## store the year for organizing in json
            year = int(year_str)
            if year >= 99:
                year_str = "19" + year_str
            else: 
                year_str = "20" + year_str
            year = year_str

            ## parse_10k_filing is a parser I got from github, it proved very difficult for me to write my own parser quickly
            ## inf_api_caller leverages hugging faces inference api to get a summary of the text, this was the LLM used: 
            ## https://api-inference.huggingface.co/models/human-centered-summarization/financial-summarization-pegasus
            ## 0: all, 1: business description, 2: risk, 3: management discussion and analysis. (params used for the parse_10k_filing call)
            try:
                print(filepath)
                biz_sum = inf_api_caller.get_summary(parse_10K.parse_10k_filing(filepath, 1))
            except:
                biz_sum = [{'summary_text': 'no data'}]

            try:
                risk_sum = inf_api_caller.get_summary(parse_10K.parse_10k_filing(filepath, 2))
            except:
                risk_sum = [{'summary_text': 'no data'}]

            try:
                mgmt_sum = inf_api_caller.get_summary(parse_10K.parse_10k_filing(filepath, 3))
            except:
                mgmt_sum = [{'summary_text': 'no data'}]
            print("here")

            time.sleep(2) ## needed to add sleep to wait for th API 

            ## 0 -> Negative; 1 -> Neutral; 2 -> Positive ## these were the numbers associated with the sentiment of the labels
            print(biz_sum)
            try: 
                biz_sentiment = inf_api_caller.get_sentiment(biz_sum[0]['summary_text'])
            except:
                time.sleep(2)
                biz_sentiment = inf_api_caller.get_sentiment(biz_sum[0]['summary_text'])
            try: 
                risk_sentiment = inf_api_caller.get_sentiment(risk_sum[0]['summary_text'])
            except:
                time.sleep(2)
                risk_sentiment = inf_api_caller.get_sentiment(risk_sum[0]['summary_text'])
            try: 
                mgmt_sentiment = inf_api_caller.get_sentiment(mgmt_sum[0]['summary_text'])    
            except:
                time.sleep(2)
                mgmt_sentiment = inf_api_caller.get_sentiment(mgmt_sum[0]['summary_text'])    
            
            try:
                with open('data.json', 'r') as file: ## load an existing file or make a new one if it doesn't exist already
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = {}

            ## update the summaries in the json file
            if ticker in existing_data:
                existing_data[ticker]['Details'][str(year)] = {
                    'Business Summary': {
                        'Summary Text': biz_sum[0]['summary_text'],
                        'Positive Sentiment': next(item['score'] for item in biz_sentiment[0] if item['label'] == 'LABEL_2'),
                        'Neutral Sentiment': next(item['score'] for item in biz_sentiment[0] if item['label'] == 'LABEL_1'),
                        'Negative Sentiment': next(item['score'] for item in biz_sentiment[0] if item['label'] == 'LABEL_0')
                    },
                    'Risk Summary': {
                        'Summary Text': risk_sum[0]['summary_text'],
                        'Positive Sentiment': next(item['score'] for item in risk_sentiment[0] if item['label'] == 'LABEL_2'),
                        'Neutral Sentiment': next(item['score'] for item in risk_sentiment[0] if item['label'] == 'LABEL_1'),
                        'Negative Sentiment': next(item['score'] for item in risk_sentiment[0] if item['label'] == 'LABEL_0')
                    },
                    'Management Summary': {
                        'Summary Text': mgmt_sum[0]['summary_text'],
                        'Positive Sentiment': next(item['score'] for item in mgmt_sentiment[0] if item['label'] == 'LABEL_2'),
                        'Neutral Sentiment': next(item['score'] for item in mgmt_sentiment[0] if item['label'] == 'LABEL_1'),
                        'Negative Sentiment': next(item['score'] for item in mgmt_sentiment[0] if item['label'] == 'LABEL_0')
                    }
                }
            else:
                existing_data[ticker] = { ## handle in the case where the company already has a submission
                    'Year': year,
                    'Details': {
                        str(year): {
                            'Business Summary': {
                                'Summary Text': biz_sum[0]['summary_text'],
                                'Positive Sentiment': next(item['score'] for item in biz_sentiment[0] if item['label'] == 'LABEL_2'),
                                'Neutral Sentiment': next(item['score'] for item in biz_sentiment[0] if item['label'] == 'LABEL_1'),
                                'Negative Sentiment': next(item['score'] for item in biz_sentiment[0] if item['label'] == 'LABEL_0')
                            },
                            'Risk Summary': {
                                'Summary Text': risk_sum[0]['summary_text'],
                                'Positive Sentiment': next(item['score'] for item in risk_sentiment[0] if item['label'] == 'LABEL_2'),
                                'Neutral Sentiment': next(item['score'] for item in risk_sentiment[0] if item['label'] == 'LABEL_1'),
                                'Negative Sentiment': next(item['score'] for item in risk_sentiment[0] if item['label'] == 'LABEL_0')
                            },
                            'Management Summary': {
                                'Summary Text': mgmt_sum[0]['summary_text'],
                                'Positive Sentiment': next(item['score'] for item in mgmt_sentiment[0] if item['label'] == 'LABEL_2'),
                                'Neutral Sentiment': next(item['score'] for item in mgmt_sentiment[0] if item['label'] == 'LABEL_1'),
                                'Negative Sentiment': next(item['score'] for item in mgmt_sentiment[0] if item['label'] == 'LABEL_0')
                            }
                        }
                    }
                }

            with open('data.json', 'w') as file:
                json.dump(existing_data, file, indent=4)   ## finally write to the file
            
            os.remove(filepath) ## easier to know what's been processed when I hit usage cap ## delete original filings to avoid repeats
