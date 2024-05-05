import sec_10k_fetcher
import populate_json

#sec_10k_fetcher.fetch_filings()

root_directory = './sec-edgar-filings'  # Replace with the actual root directory path
populate_json.popjson(root_directory)