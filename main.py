from flask import Flask, render_template, request, redirect, send_file
from assignments.wanted_scrapper import WantedScrapper

app = Flask("JobScrapper")

db = {}


# @ : decorator
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")

    if keyword in db:
        jobs = db[keyword]
    else:
        ws = WantedScrapper(keyword)
        pageContent = ws.getPageContent()
        jobs = ws.scrapeContent(pageContent)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobDb=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")

    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")

    ws = WantedScrapper(keyword)
    ws.exportToCSV(db[keyword])
    return send_file(f"./artifacts/{keyword}_jobs_downloaded.csv", as_attachment=True)


app.run()
