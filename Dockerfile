FROM python:3

ADD cli.py /
ADD post_fetcher.py /
ADD constants.py /

RUN pip install requests
RUN pip install bs4
RUN pip install pprint

ENTRYPOINT ["python", "./cli.py"]
