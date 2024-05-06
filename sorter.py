import json

'''This is a short script which simply takes the path to my data.json file and sorts the entries by year.
   The sec_edgar_downloader did not dowload the files in sequence, this caused the json entries to be out of order,
   it made things much simpler for me to just run this scrip to order the json entries to plot them in sequence.'''
file_path = '/Users/w/Documents/GATech-FinServInnovLab-SummerTask/data.json' ## path to json file

with open(file_path, 'r') as file: ## open the file an read in the data
    data = json.load(file)

for company in data:
    sorted_data = dict(sorted(data[company].items())) ## sort companies by year and store below
    data[company] = sorted_data

with open(file_path, 'w') as file: ## overwrite original file with sorted data
    json.dump(data, file, indent=4)

print("JSON file has been sorted by year and updated.")
