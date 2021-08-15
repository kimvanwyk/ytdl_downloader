FROM registry.gitlab.com/kimvanwyk/python3-poetry:latest
COPY ./ytdl_downloader/*.py /app/
COPY pyproject.toml /app/

ENTRYPOINT ["python", "main.py"]
