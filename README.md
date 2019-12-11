# Hacker News Web Scraper
A command-line tool that scraps the Hacker News website and returns information about the top stories in JSON format

## To Build Locally

1. Install Docker - https://docs.docker.com/v17.09/engine/installation/
2. In the project root, run `docker build -t hacker-news .`

## To Run Tests

1. In the project root, run `./run-tests.sh`
Note: To run tests locally you will need to have Python3 installed and run `pip install -r requirements.txt` in the project root

## To Run in Docker
`docker run hacker-news --posts 12`