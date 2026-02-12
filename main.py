import requests
from bs4 import BeautifulSoup

baseUrl = "https://weworkremotely.com"
url = "https://weworkremotely.com/remote-full-time-jobs"

all_jobs = []


def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobTags = soup.find("section", class_="jobs").find_all("li")[:-1]
    for jobTag in jobTags:
        title = jobTag.find("h3").string.strip()
        print(f"scraping {title}")
        region = None
        regionTag = jobTag.find("p", class_="new-listing__company-headquarters")
        if regionTag:
            region = jobTag.find(
                "p", class_="new-listing__company-headquarters"
            ).get_text(strip=True)
        company = jobTag.find("p", class_="new-listing__company-name").get_text(
            strip=True
        )
        link = jobTag.find("a", class_="listing-link--unlocked")["href"]
        all_jobs.append(
            {
                "title": title,
                "region": region,
                "company": company,
                "link": f"{baseUrl}{link}",
            }
        )
    print("Scrape Complete!")


def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))


total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for pageIndex in range(total_pages):
    pageUrl = f"{url}?page={pageIndex + 1}"
    print("request page", pageUrl)
    scrape_page(pageUrl)

print(len(all_jobs))
