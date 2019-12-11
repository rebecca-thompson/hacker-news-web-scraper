import requests
import constants

def fetch_posts(num_of_posts):
    print(get_raw_web_content())


def get_raw_web_content(page_number=1):
    try:
        return requests.get("%s?p=%s" % (constants.SOURCE_URL, page_number)).text
    except:
        return constants.ERROR_MESSAGE

