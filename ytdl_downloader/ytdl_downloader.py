import attr
from rich import print
import yt_dlp


@attr.s
class Downloader:
    urls = attr.ib()
    debug = attr.ib(default=False)
    outdir = attr.ib(default=".")

    def __attrs_post_init__(self):
        self.current_url = None
        self.successful_urls = []

    def __hook(self, d):
        if d.get("status") == "finished":
            self.successful_urls.append(self.current_url)
            if self.debug:
                print(f'{self.current_url} downloaded to "{d["filename"]}"')

    def download(self):
        with yt_dlp.YoutubeDL(
            {
                "ignoreerrors": True,
                "continuedl": True,
                "outtmpl": f"{self.outdir}/%(title)s.%(ext)s",
                "progress_hooks": [self.__hook],
            }
        ) as ytdl:
            for url in self.urls:
                if self.debug:
                    print(f"Downloading {url}")
                self.current_url = url
                ytdl.download([self.current_url])
        return list(set(self.successful_urls))
