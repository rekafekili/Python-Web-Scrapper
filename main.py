from flask import Flask, render_template, request
from assignments.wanted_scrapper import WantedScrapper

app = Flask("JobScrapper")


# @ : decorator
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    ws = WantedScrapper(keyword)
    pageContent = ws.getPageContent()
    jobDb = ws.scrapeContent(pageContent)
    return render_template("search.html", keyword=keyword, jobDb=jobDb)


app.run()
