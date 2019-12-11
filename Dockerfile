FROM python:3

ADD cli.py /
ADD post_fetcher.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./cli.py"]
