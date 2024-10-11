# Real Estate Web Scraper

This project is a web scraping and content parsing application designed specifically for real estate purposes. It enables users to scrape real estate websites, clean the content, and extract relevant information such as property details, listing dates, and pricing. Built using Python, Streamlit, Selenium, and a language model, this tool is tailored to help real estate professionals, investors, and researchers efficiently gather data from listing websites.

## Features

- **Website Scraping**: Uses Selenium to load a web page and BeautifulSoup to extract the body content.
- **Content Cleaning**: Removes unnecessary HTML elements such as `<script>` and `<style>` tags for a cleaner view of the page content.
- **Content Parsing**: Allows users to specify what information they want to extract from the content.
- **Modular Design**: The project is split into separate modules (scrape.py for scraping and cleaning, parse.py for parsing with language models).

## How It Works

1. **Enter a URL**: Input the link to the real estate website you want to scrape. For example, use the URL of your local board of realtors.
2. **Sort Listings**: Make sure the listings on the site are sorted from newest to oldest before scraping.
3. **Scrape the Site**: Click the "Scrape Site" button to load and scrape the web page.
4. **View the DOM Content**: The extracted content can be viewed in an expandable section on the page.
5. **Parse the Content**: Provide a description of what you want to parse from the content (e.g., details about property listings). Click "Parse Content" to extract the desired information.

### Prerequisites

- Python 3.x
- Streamlit
- Selenium
- BeautifulSoup
- ChromeDriver (make sure the path to chromedriver is correct in scrape.py)
- Ollama language model installed locally



