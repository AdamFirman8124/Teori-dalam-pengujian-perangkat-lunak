# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


def test_valid_date_full_month_31_days():
    # Lines 3-6 parse; line 9/11/13 conditions all False; line 18 returns True
    assert valid_date("01-29-2020") is True


def test_valid_date_strips_whitespace():
    # Line 4 (strip) plus the success path
    assert valid_date("  06-15-2021  ") is True


def test_valid_date_month_out_of_range_low():
    # Lines 7-8 (month < 1)
    assert valid_date("0-15-2020") is False


def test_valid_date_month_out_of_range_high():
    # Lines 7-8 (month > 12)
    assert valid_date("13-15-2020") is False


def test_valid_date_31_day_month_day_too_large():
    # Lines 9-10 (day > 31)
    assert valid_date("1-32-2020") is False


def test_valid_date_31_day_month_day_zero():
    # Lines 9-10 via the `day < 1` half of the condition
    assert valid_date("1-0-2020") is False


def test_valid_date_30_day_month_day_zero():
    # Lines 11-12 via the `day < 1` half of the condition
    assert valid_date("4-0-2020") is False


def test_valid_date_30_day_month_valid():
    # Line 11 condition False branch
    assert valid_date("4-29-2020") is True


def test_valid_date_30_day_month_day_too_large():
    # Lines 11-12 (day > 30)
    assert valid_date("6-31-2020") is False


def test_valid_date_february_day_29_valid():
    # Line 13 condition False branch
    assert valid_date("2-29-2020") is True


def test_valid_date_february_day_too_large():
    # Lines 13-14 (day > 29)
    assert valid_date("2-30-2020") is False


def test_valid_date_february_day_zero():
    # Lines 13-14 via the `day < 1` half of the condition
    assert valid_date("2-0-2020") is False


def test_valid_date_day_30_rejected_by_precedence():
    # Documents actual behavior: `or day > 29` fires for any month, so day 30 fails
    assert valid_date("1-30-2020") is False


def test_valid_date_exception_bad_format():
    # Lines 15-16 (except -> return False): split produces wrong arity
    assert valid_date("1-2020") is False


def test_valid_date_exception_non_numeric():
    # Lines 15-16 via int() raising ValueError
    assert valid_date("aa-bb-cccc") is False


def test_valid_date_exception_non_string():
    # Lines 15-16 via .strip() raising AttributeError
    assert valid_date(None) is False
