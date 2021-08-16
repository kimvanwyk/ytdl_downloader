import attr
from dotenv import load_dotenv
import requests
from rich import print

import os

load_dotenv()


@attr.s
class API:
    debug = attr.ib(default=False)
    domain = attr.ib(default=os.getenv("API_DOMAIN"))

    def get_urls(self):
        res = requests.get(f"{self.domain}/urls/pending")

        self.urls = {v: k for (k, v) in res.json().items()}
        urls = list(self.urls.keys())
        if self.debug:
            print("API: URLs to download:")
            print(urls)
        return urls

    def mark_url_downloaded(self, url):
        if url in self.urls:
            if self.debug:
                print(f"Marking {url} as downloaded")
            requests.put(f"{self.domain}/urls/downloaded", json={"id": self.urls[url]})


if __name__ == "__main__":
    api = API(debug=True)
    urls = api.get_urls()
    api.mark_url_downloaded(urls[0])
    urls = api.get_urls()
