# from assignments.wanted_scrapper import WantedScrapper

# keywordInput = input("Enter a keyword: ")
# scrapper = WantedScrapper(keywordInput)
# scrapper.start()

from flask import Flask

app = Flask("JobScrapper")


# @ : decorator
@app.route("/")
def home():
    return "hey there!"


app.run()
