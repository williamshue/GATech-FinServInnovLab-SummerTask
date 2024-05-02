import os
import json

def generate_filing_index(directory):
    result = {}
    for ticker in os.listdir(directory):
        ticker_path = os.path.join(directory, ticker, '10-K')
        if os.path.isdir(ticker_path):
            result[ticker] = {}
            for filing in os.listdir(ticker_path):
                year = int(filing.split('-')[1])

                if 95 <= year <= 99:
                    year = int('19' + str(year))
                elif 0 <= year <= 23:
                    year = int('20' + str(year).zfill(2))
                
                full_path = os.path.join(ticker_path, filing, 'full-submission.txt')
                result[ticker][year] = full_path

    with open('filings_index.json', 'w') as f:
        json.dump(result, f, indent=4)

def sort_filing_index(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    sorted_data = {key: dict(sorted(values.items())) for key, values in data.items()}

    with open(file_path, 'w') as file:
        json.dump(sorted_data, file, indent=4)


