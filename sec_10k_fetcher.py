from sec_edgar_downloader import Downloader

dl = Downloader("PlaceholderCompanyName", "placeholder@placeholder.com")

## Berkshire Hathaway Inc Class A, Ticker: BRK.A
dl.get("10-K", "BRK-A", after="1995-01-01", before="2024-01-01")
## Assignment states "through 2023", 
## so I'll ask for everyting after Jan. 1st 1995
## and everything before Jan. 1st 2024

## Goldman Sachs Group Inc, Ticker: GS
dl.get("10-K", "GS", after="1995-01-01", before="2024-01-01")

## Morgan Stanley, Ticker: MS
dl.get("10-K", "MS", after="1995-01-01", before="2024-01-01")
