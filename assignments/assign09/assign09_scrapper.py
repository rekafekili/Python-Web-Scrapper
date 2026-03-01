from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

jobWebsites = ["berlinstartupjobs.com", "weworkremotely.com", "web3.career"]


# Playwright -> Soup
def getPageSoup(pageUrl: str) -> BeautifulSoup:
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(pageUrl)
    pageContent = page.content()
    p.stop()
    return BeautifulSoup(pageContent, "html.parser")


# berlinstartupjobs.com - Soup -> List
def parseBerlinJobs(soup: BeautifulSoup) -> list:
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


# berlinstartupjobs.com - Playwright -> List
def scrapeBerlinJobs(keyword: str) -> list:
    bs = getPageSoup(f"https://berlinstartupjobs.com/skill-areas/{keyword}")
    print("BeautifulSoup Success: Berlin")
    return parseBerlinJobs(bs)


# weworkremotely.com - Soup -> List
def parseWeWorkJobs(soup: BeautifulSoup) -> list:
    jobList = soup.find_all("li", class_="new-listing-container")
    res = []

    for item in jobList:
        title = item.find("h3", class_="new-listing__header__title").string
        company = item.find("p", class_="new-listing__company-name").get_text().strip()
        description = (
            item.find("p", class_="new-listing__company-headquarters")
            .get_text()
            .strip()
        )
        link = item.find("a", class_="listing-link--unlocked")
        if link:
            link = link["href"]
        else:
            link = ""
        res.append(
            {
                "title": title,
                "company": company,
                "description": description,
                "link": link,
            }
        )

    return res


# weworkremotely.com - Playwright -> List
def scrapeWeWorkJobs(keyword: str) -> list:
    bs = getPageSoup(f"https://weworkremotely.com/remote-jobs/search?term={keyword}")
    print("BeautifulSoup Success: WeWork")
    return parseWeWorkJobs(bs)


# web3.career - Soup -> List
def parseWeb3CareerJobs(soup: BeautifulSoup) -> list:
    jobList = soup.find_all("tr", class_="table_row")
    res = []

    for item in jobList:
        try:
            title = item.find("h2", class_="my-primary").string
            print(title)
            company = item.find("h3").string
            description = item.find("p", class_="text-salary").get_text().strip()
            link = item.find("a")["href"]
            res.append(
                {
                    "title": title,
                    "company": company,
                    "description": description,
                    "link": link,
                }
            )
        except:
            pass
    return res


# web3.career - Playwright -> List
def scrapeW3cCareerJobs(keyword: str) -> list:
    bs = getPageSoup(f"https://web3.career/{keyword}-jobs")
    print("BeautifulSoup Success: W3C")
    return parseWeb3CareerJobs(bs)
