from assignments.wanted_scrapper import WantedScrapper

keywordInput = input("Enter a keyword: ")
scrapper = WantedScrapper(keywordInput)
scrapper.start()
