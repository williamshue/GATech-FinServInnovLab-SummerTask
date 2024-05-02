from sec_edgar_downloader import Downloader

def fetch_filings():

    dl = Downloader("PlaceholderCompanyName", "placeholder@placeholder.com")

    ## Goldman Sachs Group Inc, Ticker: GS
    dl.get("10-K", "GS", after="1995-01-01", before="2024-01-01")

    ## Morgan Stanley, Ticker: MS
    dl.get("10-K", "MS", after="1995-01-01", before="2024-01-01")

    dl.get("10-K", "AAPL", after="1995-01-01", before="2024-01-01")


fetch_filings()