# Hacker News Web Scraper
A command-line tool that scraps the Hacker News website and returns information about the top posts

## How it works

This tool scraps Hacker News (https://news.ycombinator.com/news) and parses the information about the top posts 
into the following object structure:

 {  'author': 'a-name',
    'comments': '0',
    'points': '0',
    'rank': '0',
    'title': 'a-title',
    'uri': 'a-url'
  }

It was built and tested in Python 3.7. To run it locally, ensure you have Python 3.x and `pip` installed on your machine.
To install dependencies run `pip install -r requirements.txt` in the project root. 

It uses the Beautiful Soup and requests libraries to fetch and parse the html. These are two well-known libraries
for web scraping and Python is often considered one of the best languages for this type of task.

Hacker News also has its own API (https://github.com/HackerNews/API), but for the purposes of this project it was decided 
to use web scraping instead as it is quicker than making multiple calls to the API and there are certain fields not
exposed by the API that are available in the web view (such as number of comments).

## To Build and Run

If you have Python 3 installed in your machine and have installed the dependencies, you can run this tool from the project
root by running `python cli.py --posts 20`. If you do not specify a number of posts to return, the tool defaults to 10.

You can also build and run this in Docker:

1. Install Docker - https://docs.docker.com/v17.09/engine/installation/
2. In the project root, run `docker build -t hacker-news .`
3. Run `docker run hacker-news --posts 3`

## To Run Tests

In the project root, run `./run-tests.sh`