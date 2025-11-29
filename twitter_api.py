# ===============================
# FILE: twitter_api.py
# ===============================
import requests
from config import BEARER_TOKEN, QUERY, MAX_TWEETS

# Mengambil tweet dari API Twitter
def ambil_tweet():
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {"query": QUERY, "max_results": MAX_TWEETS}

    try:
        res = requests.get(url, headers=headers, params=params, timeout=10)

        if res.status_code != 200:
            raise Exception("TOKEN / RATE LIMIT")

        api_data = res.json()
        tweets = [t["text"] for t in api_data["data"]]

        return list(set(tweets)), "API TWITTER"

    except:
        return None, "ERROR"