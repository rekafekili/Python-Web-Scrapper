# Dynamic Scraping -> Playwright

# 1. pip install playwright
# 2. playwright install -> install browsers
from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://google.com")

page.screenshot(path="screenshot.png")
