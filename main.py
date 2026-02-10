import requests

# import cloudscraper
from bs4 import BeautifulSoup

# scraper = cloudscraper.create_scraper()
url = "https://weworkremotely.com/remote-full-time-jobs"

# response = scraper.get(url)
response = requests.get(url)

# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", class_="jobs").find_all("li")

print(jobs)
