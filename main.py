from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


def sleep7():
    time.sleep(7)


p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

sleep7()

page.click("button.Aside_searchButton__Ib5Dn")

sleep7()

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

sleep7()

page.keyboard.down("Enter")

sleep7()

page.click("a#search_tab_position")

for i in range(4):
    sleep7()
    page.keyboard.down("End")

sleep7()

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")
