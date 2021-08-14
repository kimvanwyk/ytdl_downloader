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
        return list(self.urls.keys())

    def mark_url_downloaded(self, url):
        if url in self.urls:
            requests.put(f"{self.domain}/urls/downloaded", json={"id": self.urls[url]})


if __name__ == "__main__":
    api = API()
    urls = api.get_urls()
    print(urls)
    api.mark_url_downloaded(urls[0])
    urls = api.get_urls()
    print(urls)
