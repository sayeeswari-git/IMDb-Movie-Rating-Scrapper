🎬 IMDb Movie Rating Scraper

A Python automation project that uses Selenium to scrape IMDb’s Top 250 Movies, including:

✔ Movie Title
✔ Release Year
✔ IMDb Rating

The extracted data is saved into a CSV file for easy analysis.

🛠️ Technologies Used
Tool	Purpose
Python	Main programming language
Selenium	Browser automation
WebDriver Manager	Auto ChromeDriver installation
Pandas	Data structure + CSV export
📌 Features

Scrapes IMDb live data

Saves data into CSV format

Dynamic content handling with Selenium

Can run in headless mode

🚀 How to Run

Install required libraries:

pip install -r requirements.txt


Run the script:

python imdb_scraper.py


Output will be generated as:

imdb_top_250.csv

📄 Output Sample
Title	Year	Rating
The Shawshank Redemption	1994	9.2
The Godfather	1972	9.1
✨ Future Enhancements

Scrape cast, genre, runtime

Export to Excel

Visualization dashboard

Flask/React UI frontend
