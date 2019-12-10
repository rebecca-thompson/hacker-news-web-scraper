import pytest
from argparse import ArgumentTypeError
from cli import check_value_within_range

def test_only_accepts_between_one_and_one_hundred():
    assert check_value_within_range('20') == 20

    with pytest.raises(ArgumentTypeError):
        check_value_within_range('-1')

    with pytest.raises(ArgumentTypeError):
        check_value_within_range('101')
