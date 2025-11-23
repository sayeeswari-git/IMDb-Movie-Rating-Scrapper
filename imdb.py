from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Uncomment for headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# IMDb Top 250 Movies URL
url = "https://www.imdb.com/chart/top/"
driver.get(url)
time.sleep(3)

# Extract Movie Elements
movies = driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item__tc")

movie_titles = []
movie_years = []
movie_ratings = []

for movie in movies:
    try:
        title = movie.find_element(By.CSS_SELECTOR, "h3").text
        year = movie.find_element(By.CSS_SELECTOR, ".cli-title-metadata span:first-child").text
        rating = movie.find_element(By.CSS_SELECTOR, ".ipc-rating-star--imdb > span:nth-child(2)").text

        movie_titles.append(title)
        movie_years.append(year)
        movie_ratings.append(rating)

    except:
        continue

# Save to DataFrame
df = pd.DataFrame({
    "Title": movie_titles,
    "Year": movie_years,
    "IMDb Rating": movie_ratings
})

# Export as CSV
df.to_csv("imdb_top_250.csv", index=False)
print("Scraping Completed! CSV saved as imdb_top_250.csv")

driver.quit()