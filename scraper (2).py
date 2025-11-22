import requests
from bs4 import BeautifulSoup
import csv
import os
import time
from urllib.parse import urljoin # Import urljoin

BASE_URL = "http://books.toscrape.com/"

def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WebScraper/1.0; +https://example.com/bot)"
    }
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")

def parse_book(article):
    title = article.h3.a["title"].strip()
    price = article.find("p", class_="price_color").text.strip()
    availability = article.find("p", class_="instock availability").text.strip()
    rating = article.p.get("class", [])
    rating = [r for r in rating if r != 'star-rating']
    rating = rating[0] if rating else ''
    return {
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating
    }

def scrape_site(pages=2):
    results = []
    next_url = BASE_URL
    page_count = 0
    while next_url and page_count < pages:
        print(f"Fetching page: {next_url}")
        soup = get_soup(next_url)
        articles = soup.find_all("article", class_="product_pod")
        for a in articles:
            results.append(parse_book(a))
        # find next
        next_li = soup.select_one("li.next > a")
        if next_li:
            href = next_li['href']
            # Use urljoin to correctly build the next page URL
            next_url = urljoin(next_url, href)
        else:
            next_url = None
        page_count += 1
        time.sleep(1)  # polite delay
    os.makedirs("data", exist_ok=True)
    out_path = os.path.join("data", "books.csv")
    with open(out_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["title","price","availability","rating"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    print(f"Saved {len(results)} records to {out_path}")
    return out_path

if __name__ == "__main__":
    scrape_site(pages=5)