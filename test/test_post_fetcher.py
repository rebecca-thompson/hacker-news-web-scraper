import pytest
from bs4 import BeautifulSoup
from post_fetcher import get_num_of_pages, parse_raw_web_content, ParsingError


def test_get_num_of_pages():
    assert get_num_of_pages('1') == 1
    assert get_num_of_pages('31') == 2
    assert get_num_of_pages('70') == 3
    assert get_num_of_pages('100') == 4
