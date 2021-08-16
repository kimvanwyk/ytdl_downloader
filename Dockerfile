FROM registry.gitlab.com/kimvanwyk/python3-poetry:latest
COPY ./ytdl_downloader/*.py /app/
COPY pyproject.toml /app/

VOLUME /out

ENTRYPOINT ["python", "main.py", "--out_dir", "/out"]
