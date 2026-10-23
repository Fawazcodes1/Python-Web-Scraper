"""
FREE STARTER PYTHON SCRAPER
Extracts quotes and authors from a public test website.

Need anti-bot bypass, proxy rotation, lead extraction, and Excel exports?
Get the Full Python Automation Toolkit Pro on Selar:
https://selar.co/your-custom-link-here
"""

import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")
        
        for quote, author in zip(quotes, authors):
            print(f"Quote: {quote.text} | Author: {author.text}")

if __name__ == "__main__":
    print("Starting free scraper sample...")
    scrape_quotes()
