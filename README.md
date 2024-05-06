# SEC 10K Filings Insight Analysis Dashboard

### Summary

This project was developed by William Shue, the dashboard can be used at: [https://williamshue.net/SEC_10K_Filings_Insight_Analysis_Dashboard/](https://williamshue.net/SEC_10K_Filings_Insight_Analysis_Dashboard/).

*note*: I would have loved nothing more than to use Chat GPT3.5/4 or Anthorpic's Claude Opus to generate textual insights; unfortunately I was unable to obtain free credits for those services. Most hugging face models have very small context winodws, which is why I used [human-centered-summarization/financial-summarization-pegasus](https://huggingface.co/human-centered-summarization/financial-summarization-pegasus) as the LLM to summarize the filings, and [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) to generate sentiment scores.

*note*: Retrospectively I would have also desgined the dashboard to allow for the user to select the tickers and modified the backend to allow this.

## The Tech Stack 
I used the following tech stack to develop the web application. I selected the tools becuase I was familiar with them, they allowed efficent deployment of a lightweight web app which allowed for easily visualizing/interacting with the insights obtained leveraging the LLMs accessed via Hugging Face's Inference API.

### Backend:
**Python Scripts** which fetch data using the SEC EDGAR Downloader, clearn and orgainze the data, and make calls to Hugging Face via the inference API in order to get insights on the data; then storing everything in an orgainzed fashion in the data store.

### Datastore:
**The data.json file** which is modified and updated via the python scripts to allow for processing/visualizing data.

### Front End: 
**The index.html** document with contains vanilla **Java Script for allowing the webpage to be interactive** and **CSS for styling the webpage**.

## How The Application Works

1. main.py calls the 

![Alt Text](flow.png)




