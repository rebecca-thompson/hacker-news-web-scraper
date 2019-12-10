import pytest
from cli import check_value_within_range

def test_only_accepts_between_zero_and_one_hundred():
    assert check_value_within_range('20') == 20
