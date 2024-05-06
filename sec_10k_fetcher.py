from sec_edgar_downloader import Downloader
import os

'''Description: This function uses the sec_edgar_downloader to dowload the companies sec 10k filings for the years specified
   Input: no input -- the filings and years are specified within the function
   Output: the files are downloaded to a directory in the same directory where this file is run''' 
def fetch_filings():
    ## init downloader
    dl = Downloader("YourCompanyName", "your-email@company.com")
    
    ## specify companies and tickers
    companies = {
        "AMZN": "Amazon.com Inc",
        "MSFT": "Microsoft Corp",
        "AAPL": "Apple Inc."
    }

    for ticker, _ in companies.items():
        ## download filings
        dl.get("10-K", ticker, after="1995-01-01", before="2024-01-01")
