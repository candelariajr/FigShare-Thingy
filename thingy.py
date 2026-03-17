import json
import reques ts
from requests.exceptions import HTTPError, RequestException

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

apikey = config["api-key"]
BASE_URL = "https://api.figshare.com/v2"


def figshare_get(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"token {apikey}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except HTTPError:
        print("HTTP error:", response.status_code)
        print(response.text)
        raise
    except RequestException as e:
        print("Request failed:", e)
        raise


articles = figshare_get("account/articles")
print(articles)
