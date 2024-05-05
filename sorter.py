import json

# Path to your JSON file
file_path = '/Users/w/Documents/GATech-FinServInnovLab-SummerTask/data.json'

# Load the data from the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Sort the entries for each company by year
for company in data:
    sorted_data = dict(sorted(data[company].items()))
    data[company] = sorted_data

# Save the sorted data back to the JSON file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("The JSON file has been sorted by year and updated.")
