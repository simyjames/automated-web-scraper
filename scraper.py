import requests
from bs4 import BeautifulSoup
import csv

def scrape_website():
    # Define the target URL
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the website")
        return

    # Parse the website content
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    # Extract quotes and authors
    data = []
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        data.append({"quote": text, "author": author})

    # Save data to a CSV file
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["quote", "author"])
        writer.writeheader()
        writer.writerows(data)

    print("Quotes successfully saved to quotes.csv")

if __name__ == "__main__":
    scrape_website()
