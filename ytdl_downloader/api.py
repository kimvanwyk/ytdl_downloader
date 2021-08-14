from dotenv import load_dotenv
import requests

import os

load_dotenv()


class API:
    def __init__(self):
        self.domain = os.getenv("API_DOMAIN")

    def get_urls(self):
        res = requests.get(f"{self.domain}/urls/pending")

        self.urls = {v: k for (k, v) in res.json().items()}
        return self.urls.keys()


if __name__ == "__main__":
    api = API()
    urls = api.get_urls()
    print(urls)
