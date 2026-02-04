# For Loops
websites = (
    "google.com",
    "https://airbnb.com",
    "twitter.com",
    "https://facebook.com",
    "https://tiktok.com",
)

for website in websites:
    if not website.startswith("https://"):
        # print("Have to fix", website)
        website = f"https://{website}"
    print(website)
