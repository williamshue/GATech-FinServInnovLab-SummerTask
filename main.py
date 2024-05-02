import sec_10k_fetcher
import file_org

## sec_10k_fetcher.py
sec_10k_fetcher.fetch_filings()

## file_org.py
file_org.generate_filing_index('sec-edgar-filings')
file_path = 'filings_index.json'
file_org.sort_filing_index(file_path)

