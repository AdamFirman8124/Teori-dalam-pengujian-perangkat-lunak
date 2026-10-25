# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


def test_valid_date_returns_true():
    assert valid_date("03-15-2021") is True


def test_valid_date_30_day_month():
    # Due to operator precedence (`and` binds tighter than `or`), the
    # `day > 29` check applies to every month, so day 30 is rejected
    # even for 30-day months. Day 29 is the maximum accepted day.
    assert valid_date("04-29-2021") is True


def test_valid_date_feb_29():
    assert valid_date("02-29-2021") is True


def test_day_30_and_31_are_rejected_for_all_months():
    assert valid_date("01-31-2021") is False
    assert valid_date("04-30-2021") is False
    assert valid_date("12-31-2021") is False


def test_invalid_month_returns_false():
    assert valid_date("13-01-2021") is False
    assert valid_date("00-10-2021") is False


def test_day_above_31_returns_false():
    assert valid_date("01-32-2021") is False


def test_day_above_30_returns_false():
    assert valid_date("04-31-2021") is False


def test_day_above_29_returns_false():
    assert valid_date("02-30-2021") is False


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
