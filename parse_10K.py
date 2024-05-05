## modified to handle local files from https://github.com/rsljr/edgarParser/blob/master/parse_10K.py 

import re
import unicodedata
from bs4 import BeautifulSoup as bs

def parse_10k_filing(filepath, section):
    
    if section not in [0, 1, 2, 3]:
        print("Not a valid section")
        sys.exit()
    
    def get_text(filepath):
        with open(filepath, 'r') as file:
            html = bs(file, "lxml")
        text = html.get_text()
        text = unicodedata.normalize("NFKD", text).encode('ascii', 'ignore').decode('utf8')
        text = text.split("\n")
        text = " ".join(text)
        return(text)
    
    def extract_text(text, item_start, item_end):
        starts = [i.start() for i in item_start.finditer(text)]
        ends = [i.start() for i in item_end.finditer(text)]
        positions = []
        for s in starts:
            control = 0
            for e in ends:
                if control == 0:
                    if s < e:
                        control = 1
                        positions.append([s,e])
        item_length = 0
        item_position = []
        for p in positions:
            if (p[1]-p[0]) > item_length:
                item_length = p[1]-p[0]
                item_position = p

        item_text = text[item_position[0]:item_position[1]]

        return(item_text)

    text = get_text(filepath)
        
    if section == 1 or section == 0:
        item1_start = re.compile("item\\s*[1][\\.\\;\\:\\-\\_]*\\s*\\b", re.IGNORECASE)
        item1_end = re.compile("item\\s*1a[\\.\\;\\:\\-\\_]\\s*Risk|item\\s*2[\\.\\,\\;\\:\\-\\_]\\s*Prop", re.IGNORECASE)
        businessText = extract_text(text, item1_start, item1_end)
        
    if section == 2 or section == 0:
        item1a_start = re.compile("(?<!,\\s)item\\s*1a[\\.\\;\\:\\-\\_]\\s*Risk", re.IGNORECASE)
        item1a_end = re.compile("item\\s*2[\\.\\;\\:\\-\\_]\\s*Prop|item\\s*[1][\\.\\;\\:\\-\\_]*\\s*\\b", re.IGNORECASE)
        riskText = extract_text(text, item1a_start, item1a_end)
        
    if section == 3 or section == 0:
        item7_start = re.compile("item\\s*[7][\\.\\;\\:\\-\\_]*\\s*\\bM", re.IGNORECASE)
        item7_end = re.compile("item\\s*7a[\\.\\;\\:\\-\\_]\\sQuanti|item\\s*8[\\.\\,\\;\\:\\-\\_]\\s*", re.IGNORECASE)
        mdaText = extract_text(text, item7_start, item7_end)
    
    if section == 0:
        data = [businessText, riskText, mdaText]
    elif section == 1:
        data = [businessText]
    elif section == 2:
        data = [riskText]
    elif section == 3:
        data = [mdaText]
    return(data)

# Example usage
result = parse_10k_filing('/Users/w/Documents/GATech-FinServInnovLab-SummerTask/sec-edgar-filings/META/10-K/0001326801-23-000013/full-submission.txt', 1)
print(result)
