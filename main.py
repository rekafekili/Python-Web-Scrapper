import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/remote-full-time-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

jobTags = soup.find("section", class_="jobs").find_all("li")[:-1]

for jobTag in jobTags:
    title = jobTag.find("h3").string.strip()
    region = jobTag.find("p", class_="new-listing__company-headquarters").get_text(
        strip=True
    )
    company = jobTag.find("p", class_="new-listing__company-name").get_text(strip=True)
    print(title)
    print(region)
    print(company)
    print("================")
