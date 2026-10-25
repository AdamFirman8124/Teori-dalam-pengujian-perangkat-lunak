# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


def test_valid_date_returns_true():
    assert valid_date("03-15-2021") is True


def test_valid_date_31_day_month():
    # NOTE: due to operator precedence in the source
    # (`... and day < 1 or day > 31`), any day > 29 returns False,
    # so the highest day that passes for a 31-day month is 29.
    assert valid_date("01-29-2021") is True


def test_valid_date_30_day_month():
    assert valid_date("04-29-2021") is True


def test_valid_date_feb_29():
    assert valid_date("02-29-2021") is True


def test_day_30_always_returns_false():
    # The bare `day > 29` in the February check rejects day 30
    # for every month, not just February.
    assert valid_date("01-30-2021") is False


def test_day_31_always_returns_false():
    # The bare `day > 30` in the 30-day-month check rejects day 31
    # for every month, including 31-day months like January.
    assert valid_date("01-31-2021") is False


def test_feb_30_returns_false():
    # The bare `day > 29` in the February check rejects Feb 30.
    assert valid_date("02-30-2021") is False


def test_invalid_month_returns_false():
    assert valid_date("13-01-2021") is False
    assert valid_date("00-10-2021") is False


def test_day_below_one_returns_false():
    assert valid_date("01-00-2021") is False
    assert valid_date("04-00-2021") is False
    assert valid_date("02-00-2021") is False


def test_malformed_input_returns_false():
    assert valid_date("not-a-date") is False


def test_unsplittable_input_returns_false():
    assert valid_date("2021") is False


def test_non_string_input_returns_false():
    assert valid_date(None) is False
    assert valid_date(12345) is False


def test_whitespace_is_stripped():
    assert valid_date("  03-15-2021  ") is True
