FROM python:3

ADD cli.py /

ENTRYPOINT ["python", "./cli.py"]
