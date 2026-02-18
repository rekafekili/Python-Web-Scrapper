from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


def sleep7():
    time.sleep(7)


p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto(
    "https://www.wanted.co.kr/search?query=flutter&search_method=popular&tab=position"
)

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")
jobs_db = []

jobs = soup.find_all("div", class_="JobCard_container__zQcZs")

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title___kfvj")
    company_name = job.find(
        "span",
        class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu wds-nkj4w6",
    )
    location = job.find(
        "span",
        class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l wds-nkj4w6",
    )
    reward = job.find("span", class_="JobCard_reward__oCSIQ")
    job = {
        "title": title.string,
        "company_name": company_name.string,
        "location": location.string,
        "reward": reward.string,
    }
    jobs_db.append(job)

print(f"Jobs DB length:", len(jobs_db))
print(jobs_db)
