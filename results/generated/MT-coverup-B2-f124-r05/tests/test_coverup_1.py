# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


def test_valid_dates_return_true():
    # Exercises lines 3-6 (try, strip, split, int conversion) and line 18 (return True)
    assert valid_date("03-11-1948") is True
    assert valid_date(" 06-04-2020 ") is True  # leading/trailing whitespace exercises strip()
    assert valid_date("02-29-2020") is True    # Feb 29 passes (day <= 29)


def test_month_out_of_range_returns_false():
    # Exercises lines 7-8, both disjuncts of the condition
    assert valid_date("00-15-2023") is False   # month < 1
    assert valid_date("13-15-2023") is False   # month > 12


def test_31_day_months_bad_day_returns_false():
    # Exercises lines 9-10, both disjuncts of the condition
    assert valid_date("01-00-2023") is False   # month in 31-day list and day < 1
    assert valid_date("04-32-2023") is False   # day > 31 (month not in 31-day list)


def test_30_day_months_bad_day_returns_false():
    # Exercises lines 11-12, both disjuncts of the condition
    assert valid_date("04-00-2023") is False   # month in 30-day list and day < 1
    assert valid_date("02-31-2023") is False   # day > 30 (month not in 30-day list)


def test_february_bad_day_returns_false():
    # Exercises lines 13-14, both disjuncts of the condition
    assert valid_date("02-00-2023") is False   # month == 2 and day < 1
    assert valid_date("02-30-2023") is False   # day > 29 (but not > 30, so line 11 passes)


def test_malformed_input_returns_false():
    # Exercises lines 15-16 (except -> return False)
    assert valid_date("01-ab-2023") is False        # int() raises ValueError
    assert valid_date("01-15") is False             # too few '-'-separated parts
    assert valid_date("01-15-2023-extra") is False  # too many parts


def test_non_string_input_returns_false():
    # .strip() raises AttributeError, caught by the bare except
    assert valid_date(None) is False
    assert valid_date(123) is False
