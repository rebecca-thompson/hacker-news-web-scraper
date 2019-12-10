FROM python:3

ADD src/hacker_news /

ENTRYPOINT ["python", "./cli.py"]
