from requests import get

# For Loops
websites = (
    "google.com",
    "https://airbnb.com",
    "twitter.com",
    "https://facebook.com",
    "https://tiktok.com",
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        # print(f"{website} is OK")
        results[website] = True
    else:
        # print(f"{website} is not OK")
        results[website] = False

print(results)
