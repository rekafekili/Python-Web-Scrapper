from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def extractJobDb(soup: BeautifulSoup):
    jobList = soup.find_all("div", class_="bjs-jlid__wrapper")
    res = []

    for item in jobList:
        title = item.find("h4", class_="bjs-jlid__h").find("a").string
        company = item.find("a", class_="bjs-jlid__b").string
        description = item.find("div", class_="bjs-jlid__description").string
        link = item.find("h4", class_="bjs-jlid__h").find("a")["href"]
        res.append(
            {
                "title": title,
                "company": company,
                "description": description,
                "link": link,
            }
        )

    return res


p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://berlinstartupjobs.com/engineering/")
pageContent = page.content()

job_db = []
keywords = ["python", "typescript", "javascript"]

# https://berlinstartupjobs.com/engineering/ 스크래핑
while True:
    bs = BeautifulSoup(pageContent, "html.parser")
    job_db.append(extractJobDb(bs))

    next_btn = bs.find("a", class_="next page-numbers")

    if next_btn != None:
        next_link = next_btn["href"]
        page.goto(next_link)
        pageContent = page.content()
    else:
        break

# https://berlinstartupjobs.com/skill-areas/[keyword]/ 스크래핑
skills_job_db = []
for keyword in keywords:
    page.goto(f"https://berlinstartupjobs.com/skill-areas/{keyword}/")
    pageContent = page.content()
    bs = BeautifulSoup(pageContent, "html.parser")
    skills_job_db.append(extractJobDb(bs))

print(job_db)
print(skills_job_db)
p.stop()
