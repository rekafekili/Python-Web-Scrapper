from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


class WantedScrapper:
    def __init__(self, keyword: str):
        self.keyword = keyword

    def sleep(self) -> None:
        time.sleep(5)

    def getPageContent(self) -> str:
        p = sync_playwright().start()
        # headless=True로 진행하면 웹사이트에서 봇으로 판단하고 차단 당할 확률이 큼.
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = f"https://www.wanted.co.kr/search?query={self.keyword}&search_method=popular&tab=position"
        page.goto(url)
        self.sleep()
        content = page.content()
        p.stop()
        print("The Page Explored:", url)
        return content

    def scrapeContent(self, content: str) -> list[dict]:
        soup = BeautifulSoup(content, "html.parser")
        jobs_db: list[dict] = []

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
                "link": link,
            }
            jobs_db.append(job)

        print("Scrapped Jobs:", len(jobs_db))
        return jobs_db

    def exportToCSV(self, jobs: list[dict]) -> None:
        file = open(f"./artifacts/{self.keyword}_jobs_downloaded.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(jobs[0].keys())

        for job in jobs:
            writer.writerow(job.values())
        file.close()
        print("Export Success!")

    def start(self):
        page = self.getPageContent()
        jobs = self.scrapeContent(page)
        if len(jobs) > 0:
            self.exportToCSV(jobs)
        else:
            print("Result is not exist.")
