from sec_edgar_downloader import Downloader
import os

def fetch_filings():
    # init downloader
    dl = Downloader("YourCompanyName", "your-email@company.com")
    
    # specify companies and tickers
    companies = {
        "JPM": "JPMorgan Chase & Co.",
        "MSFT": "Microsoft Corp",
        "AAPL": "Apple Inc."
    }

    for ticker, _ in companies.items():
        # download filings
        dl.get("10-K", ticker, after="1995-01-01", before="2024-01-01")
