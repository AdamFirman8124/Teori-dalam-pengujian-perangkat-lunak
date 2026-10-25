# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


def test_valid_date_31_day_month_valid():
    # Exercises lines 3-6 (parse), line 9 condition False branch, line 18 (return True).
    # NOTE: due to operator precedence in the source (line 9: "A and day < 1 or day > 31"),
    # any day > 29 is rejected by the later checks, so the max valid day is 29.
    assert valid_date("01-29-2020") is True


def test_valid_date_strips_whitespace():
    # Exercises line 4 (strip) plus the success path
    assert valid_date("  06-15-2021  ") is True


def test_valid_date_month_out_of_range_low():
    # Exercises lines 7-8 (month < 1)
    assert valid_date("0-15-2020") is False


def test_valid_date_month_out_of_range_high():
    # Exercises lines 7-8 (month > 12)
    assert valid_date("13-15-2020") is False


def test_valid_date_31_day_month_day_too_large():
    # Exercises lines 9-10 (day > 31 for a 31-day month)
    assert valid_date("1-32-2020") is False


def test_valid_date_30_day_month_day_31_rejected():
    # Due to operator precedence, day=31 in a 30-day month hits line 9-10 return False
    assert valid_date("4-31-2020") is False


def test_valid_date_30_day_month_valid():
    # Exercises line 11 condition False branch (max valid day is 29, see note above)
    assert valid_date("4-29-2020") is True


def test_valid_date_30_day_month_day_too_large():
    # Exercises lines 11-12 (day > 30)
    assert valid_date("6-31-2020") is False


def test_valid_date_february_day_29_valid():
    # Exercises line 13 condition False branch
    assert valid_date("2-29-2020") is True


def test_valid_date_february_day_too_large():
    # Exercises lines 13-14 (day > 29)
    assert valid_date("2-30-2020") is False


def test_valid_date_day_zero_rejected():
    # Exercises the day < 1 branch of line 13
    assert valid_date("2-0-2020") is False


def test_valid_date_exception_bad_format():
    # Exercises lines 15-16 (except -> return False): split produces wrong arity
    assert valid_date("1-2020") is False


def test_valid_date_exception_non_numeric():
    # Exercises lines 15-16 via int() raising ValueError
    assert valid_date("aa-bb-cccc") is False


def test_valid_date_exception_non_string():
    # Exercises lines 15-16 via .strip() raising AttributeError
    assert valid_date(None) is False
