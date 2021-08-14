from api import API
from ytdl_downloader import Downloader


def download(debug=False):
    api = API(debug)
    dl = Downloader(api.get_urls(), debug=debug)
    successful_urls = dl.download()
    if debug:
        print(f"Successful URLS: {successful_urls}")
    for url in successful_urls:
        api.mark_url_downloaded(url)


download(True)
