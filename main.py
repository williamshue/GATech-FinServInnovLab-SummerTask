import sec_10k_fetcher
import populate_json

## calls the filing fetcher to obtain the specified filings defined in the file
sec_10k_fetcher.fetch_filings()

## populates the json file which serves as a data store for the dashboard
root_directory = './sec-edgar-filings'  
populate_json.popjson(root_directory)

