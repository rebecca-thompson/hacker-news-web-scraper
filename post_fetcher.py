from bs4 import BeautifulSoup
import pprint
import requests
import constants
import sys
import re
import math
from decimal import *

def fetch_posts(num_of_posts):
    num_of_pages = math.ceil((Decimal(num_of_posts)/Decimal(constants.POSTS_PER_PAGE)))
    posts = []

    for page in range(1,num_of_pages+1):
        content = get_raw_web_content(page)
        parse_raw_web_content(content, posts)

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(posts[0:num_of_posts])


def get_raw_web_content(page_number=1):
    try:
        return requests.get("%s?p=%s" % (constants.SOURCE_URL, page_number)).text
    except:
        print(constants.ERROR_MESSAGE)
        sys.exit(1)


def parse_raw_web_content(raw_content, posts):
    page = BeautifulSoup(raw_content, "html.parser")
    post_elements = get_post_html_elements(page)
    convert_html_elements_to_posts(post_elements, posts)


def get_post_html_elements(page):
    table = page.find("table", class_="itemlist")
    rows = table.find_all("tr")
    elements = [rows[x:x+3] for x in range(0, len(rows), 3)]
    return elements[0:-1]


def convert_html_elements_to_posts(elements, posts):
    for element in elements:
        item = {}
        item["title"] = get_html_element_text_by_class(element[0], "a", "storylink")
        item["uri"] = get_uri(element[0], "storylink")
        item["author"] = get_html_element_text_by_class(element[1], "a", "hnuser")
        item["points"] = strip_non_numeric_characters(get_html_element_text_by_class(element[1], "span", "score"))
        item["comments"] = get_comments(element[1])
        item["rank"] = strip_non_numeric_characters(get_html_element_text_by_class(element[0], "span", "rank"))
        posts.append(item)


def get_html_element_text_by_class(element, tag, class_name):
    tag_element = element.find(tag, class_=class_name)
    if tag_element is not None:
        return tag_element.text
    else:
        return ""


def get_uri(element, class_name):
    a_element = element.find("a", class_=class_name)
    if a_element is not None:
        return a_element["href"]
    else:
        return ""

def get_comments(element):
    a_element = element.find("td", class_="subtext").find_all("a")[-1]
    if a_element is not None:
        return strip_non_numeric_characters(a_element.text)
    else:
        return ""


def strip_non_numeric_characters(input):
    return re.sub("[^0-9]", "", input)


