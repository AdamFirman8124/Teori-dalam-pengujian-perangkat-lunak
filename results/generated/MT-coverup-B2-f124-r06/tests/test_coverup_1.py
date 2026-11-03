# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


def test_valid_date_returns_true_for_valid_dates():
    """Happy path: lines 3-7, 9, 11, 13 taken on their False branches, line 18 reached."""
    assert valid_date('03-11-2000') is True
    # surrounding whitespace is stripped before parsing (line 4)
    assert valid_date('  03-11-2000\t') is True
    # valid day in a 31-day month
    assert valid_date('01-15-2000') is True
    # valid day in a 30-day month
    assert valid_date('04-15-2000') is True
    # February 29 is accepted
    assert valid_date('02-29-2000') is True


def test_valid_date_returns_false_for_out_of_range_month():
    """Line 8: month < 1 and month > 12 branches."""
    assert valid_date('00-10-2000') is False   # month < 1
    assert valid_date('13-10-2000') is False   # month > 12


def test_valid_date_returns_false_for_bad_day_in_31_day_month():
    """Line 10: both operands of '(month in [... ] and day < 1) or (day > 31)'."""
    assert valid_date('01-00-2000') is False   # day < 1 with month in 31-day list
    assert valid_date('01-32-2000') is False   # day > 31 with month in 31-day list
    assert valid_date('04-32-2000') is False   # day > 31 fires even for other months


def test_valid_date_returns_false_for_bad_day_in_30_day_month():
    """Line 12: both operands of '(month in [... ] and day < 1) or (day > 30)'."""
    assert valid_date('04-00-2000') is False   # day < 1 with month in 30-day list
    assert valid_date('04-31-2000') is False   # day > 30 with month in 30-day list
    assert valid_date('02-31-2000') is False   # day > 30 fires even for other months


def test_valid_date_returns_false_for_bad_day_in_february():
    """Line 14: both operands of '(month == 2 and day < 1) or (day > 29)'."""
    assert valid_date('02-00-2000') is False   # day < 1 in February
    assert valid_date('02-30-2000') is False   # day > 29 in February
    assert valid_date('01-30-2000') is False   # day > 29 fires even for other months


def test_valid_date_returns_false_on_malformed_input():
    """Lines 15-16: the except handler via split/unpack and int() failures."""
    assert valid_date('03-11') is False           # too few '-'-separated parts
    assert valid_date('03-11-2000-01') is False   # too many '-'-separated parts
    assert valid_date('aa-bb-cccc') is False      # non-numeric components


def test_valid_date_returns_false_for_non_string_input():
    """Lines 15-16: the except handler via attribute errors on date.strip()."""
    assert valid_date(None) is False
    assert valid_date(123) is False
