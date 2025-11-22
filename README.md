📚 Books Web Scraper – README.md

Project Title

Books to Scrape – Web Scraper Using Python


---

📌 Project Overview

This project is a web scraping application built using Python and BeautifulSoup / Requests / Scrapy (choose your library).
The scraper collects book details from the website Books to Scrape (an open practice site for web scraping).

📍 Target Website: Books to Scrape
🔗 Website URL: https://books.toscrape.com/


---

🎯 Project Goal

The main goal of this project is to extract book information automatically, including:

Book Title

Price

Rating

Availability

Product Page Link

Category (optional)


The scraped data can be stored in CSV / JSON / Database for further analysis.


---

🛠️ Tech Stack Used

Technology	Purpose

Python	Main programming language
BeautifulSoup	HTML parsing
Requests	Downloading web page content
Pandas	Exporting data into CSV
Scrapy (if used)	Framework for large-scale scraping



---

📑 Features

✔ Scrapes book details from all pages
✔ Saves extracted data in CSV file
✔ Handles pagination automatically
✔ Clean and structured data output
✔ Easy to modify and extend


---

📂 Folder Structure

Books-Web-Scraper/
│── scraper.py
│── requirements.txt
│── README.md
│── output/
│     ├── books.csv


---

🚀 How to Run

# Clone this repository
git clone https://github.com/yourusername/books-web-scraper.git

# Navigate to project
cd books-web-scraper

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python scraper.py


---

📦 Output Example

Title, Price, Rating, Availability, Link
A Light in the Attic, £51.77, 3 Stars, In stock, https://books.toscrape.com/...



---

📜 License

This project is for educational and personal use only.
The target website is publicly available for web scraping practice.


---

🙌 Author

Achal Ghate