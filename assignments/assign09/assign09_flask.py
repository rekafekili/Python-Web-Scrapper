# Flask를 사용해 잡 스크래퍼의 프론트엔드를 구축합니다.
# 유저는 python, javascript, java 등과 같은 용어를 검색할 수 있어야 합니다.
# 스크래퍼는 berlinstartupjobs.com, weworkremotely.com 및 web3.career의 결과를 표시해야 합니다.

from flask import Flask, render_template, request, redirect
from .assign09_scrapper import scrapeBerlinJobs, scrapeWeWorkJobs, scrapeW3cCareerJobs

app = Flask("MultipleJobScrapper")

search_history = []
berlin_job_db: dict[str:list] = {}
wework_job_db: dict[str:list] = {}
w3c_job_db: dict[str:list] = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search/")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")

    berlin_jobs = []
    wework_jobs = []
    w3c_jobs = []

    if keyword in search_history:
        berlin_jobs = berlin_jobs[keyword]
        wework_jobs = wework_job_db[keyword]
        w3c_jobs = w3c_job_db[keyword]
    else:
        search_history.append(keyword)
        berlin_jobs = scrapeBerlinJobs(keyword)
        wework_jobs = scrapeWeWorkJobs(keyword)
        w3c_jobs = scrapeW3cCareerJobs(keyword)
        berlin_job_db[keyword] = berlin_jobs
        wework_job_db[keyword] = wework_jobs
        w3c_job_db[keyword] = w3c_jobs

    return render_template(
        "search.html",
        keyword=keyword,
        berlinJobs=berlin_jobs,
        weworkJobs=wework_jobs,
        w3cJobs=w3c_jobs,
    )
