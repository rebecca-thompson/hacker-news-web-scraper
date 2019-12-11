from bs4 import BeautifulSoup
import pprint
import requests
import constants
import sys
import re
import math
from decimal import *

posts = []

def fetch_posts(num_of_posts):
    num_of_pages = get_num_of_pages(num_of_posts)
    get_list_of_posts(num_of_pages)

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(posts[0:num_of_posts])


def get_num_of_pages(num_of_posts):
    return math.ceil((Decimal(num_of_posts)/Decimal(constants.POSTS_PER_PAGE)))


def get_list_of_posts(num_of_pages):
    for page in range(1,num_of_pages+1):
        content = get_raw_web_content(page)
        parse_raw_web_content(content)


def get_raw_web_content(page_number=1):
    try:
        return requests.get("%s?p=%s" % (constants.SOURCE_URL, page_number)).text
    except:
        print(constants.ERROR_MESSAGE)
        sys.exit(1)


def parse_raw_web_content(raw_content):
    page = BeautifulSoup(raw_content, "html.parser")
    post_elements = get_post_html_elements(page)
    convert_html_elements_to_posts(post_elements)


# The html <table> has three <tr> html elements per post and an extra <tr> at the end
# This function splits the <tr> elements into groups of three and then ignores the last grouping
def get_post_html_elements(page):
    table = page.find("table", class_="itemlist")
    rows = table.find_all("tr")
    elements = [rows[x:x+3] for x in range(0, len(rows), 3)]
    return elements[0:-1]

def convert_html_elements_to_posts(elements):
    for element in elements:
        item = {}
        item["title"] = get_title(element[0])
        item["uri"] = get_uri(element[0])
        item["author"] = get_author(element[1])
        item["points"] = get_points(element[1])
        item["comments"] = get_comments(element[1])
        item["rank"] = get_rank(element[0])
        posts.append(item)


def get_title(element):
    return get_html_element_text_by_class(element, "a", "storylink")


def get_uri(element):
    a_element = element.find("a", class_="storylink")
    if a_element is not None:
        return a_element["href"]
    else:
        return ""


def get_author(element):
    return get_html_element_text_by_class(element, "a", "hnuser")


def get_points(element):
    points = strip_non_numeric_characters(get_html_element_text_by_class(element, "span", "score"))
    if points is not None and points != "" and int(points) >= 0:
            return int(points)
    else:
        return None


# The comment <a> element does not have a CSS class so it is retrieved by its index
def get_comments(element):
    comments = strip_non_numeric_characters(element.find("td", class_="subtext").find_all("a")[-1].text)
    if comments is not None and comments != "" and int(comments) >= 0:
        return int(comments)
    else:
        return None


def get_rank(element):
    rank = strip_non_numeric_characters(get_html_element_text_by_class(element, "span", "rank"))
    if rank is not None and rank != "" and int(rank) >= 0:
        if int(rank) >= 0:
            return int(rank)
    else:
        return None


def get_html_element_text_by_class(element, tag, class_name):
    tag_element = element.find(tag, class_=class_name)
    if tag_element is not None:
        return tag_element.text
    else:
        return ""


def strip_non_numeric_characters(input):
    return re.sub("[^0-9]", "", input)


