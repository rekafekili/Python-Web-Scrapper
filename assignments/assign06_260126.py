# BLUEPRINT | DONT EDIT

import requests

movie_ids = [238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
baseUrl = "https://nomad-movies.nomadcoders.workers.dev/movies/"

print("Movie List")
for i in movie_ids:
    endUrl = f"{baseUrl}{i}"
    response = requests.get(endUrl)
    data = response.json()
    print(
        f"Title: {data["title"]}\nOverview: {data["overview"]}\nVoteAvg: {data["vote_average"]}"
    )
    print("========================================================================")

# /YOUR CODE
