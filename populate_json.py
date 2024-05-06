import os
import parse_10K
import numpy
import json
import time
import inf_api_caller 

def popjson(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            ticker = filepath.split('/')[2]

            year_str = filepath.split('-')[4]
            year = int(year_str)
            if year >= 99:
                year_str = "19" + year_str
            else: 
                year_str = "20" + year_str
            year = year_str

            # ## 0: all, 1: business description, 2: risk, 3: management discussion and analysis.
            # ## overall_sum = get_summary(parse_10K.parse_10k_filing(filepath, 0))
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

            time.sleep(2)

            ## 0 -> Negative; 1 -> Neutral; 2 -> Positive
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
            
        

            # Load existing JSON data if available
            try:
                with open('data.json', 'r') as file:
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = {}

            # Check if ticker already exists
            if ticker in existing_data:
                # Add a new entry for the current year
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
                # Create a new entry for the ticker
                existing_data[ticker] = {
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

            # Save the updated dictionary to a JSON file
            with open('data.json', 'w') as file:
                json.dump(existing_data, file, indent=4)  # Using `indent` for a prettier output
            
            os.remove(filepath) ## easier to know what's been processed when I hit usage cap
