import json
import os
from bs4 import BeautifulSoup

with open('/Users/w/Documents/GATech-FinServInnovLab-SummerTask/filings_index.json', 'r') as file:
    data = json.load(file)

# Process each company and year
for company, years in data.items():
    for year, filepath in years.items():
        # Construct the full path to the file
        full_path = os.path.join('/Users/w/Documents/GATech-FinServInnovLab-SummerTask/', filepath)
        
        # Read and parse the HTML file
        with open(full_path, 'r', encoding='utf-8') as html_file:
            lines = html_file.readlines()
        
        # Look for <DESCRIPTION>GRAPHIC and remove lines until 'end'
        clean_lines = []
        skip = False
        for line in lines:
            if '<DESCRIPTION>GRAPHIC' in line or 'Financial_Report.xlsx' in line:
                skip = True
            if skip:
                if line.strip() == 'end':
                    skip = False
            else:
                if line.strip():  # This condition excludes lines that contain no text
                    clean_lines.append(line)

        # Parse with BeautifulSoup
        soup = BeautifulSoup(''.join(clean_lines), 'html.parser')
        text = soup.get_text()

        # Write the cleaned text back to the same HTML file
        with open(full_path, 'w', encoding='utf-8') as html_file:
            html_file.write(text)

        print(f'Processed {company}, {year}')
