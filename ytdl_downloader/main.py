from api import API
from dotenv import load_dotenv
import schedule

from ytdl_downloader import Downloader

import os
import time

load_dotenv()


def download(debug=False):
    api = API(debug)
    dl = Downloader(api.get_urls(), debug=debug)
    successful_urls = dl.download()
    if debug:
        print(f"Successful URLS: {successful_urls}")
    for url in successful_urls:
        api.mark_url_downloaded(url)


if __name__ == "__main__":
    from pyproject_details import PyProjectToml
    import argparse

    toml = PyProjectToml()
    parser = argparse.ArgumentParser(prog=toml.name, description=toml.description)
    parser.add_argument("--quiet", action="store_false", help="Suppress program output")
    parser.add_argument("--version", action="version", version=toml.version)
    args = parser.parse_args()

    schedule.every(int(os.getenv("WAIT_MINUTES", 60))).minutes.do(
        download, debug=args.quiet
    )
    while True:
        schedule.run_pending()
        time.sleep(1)
