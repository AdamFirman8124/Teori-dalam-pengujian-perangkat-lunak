# file: script_124.py:1-36
# asked: {"lines": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36], "branches": [[25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 31], [31, 32], [31, 36]]}
# gained: {"lines": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36], "branches": [[25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 31], [31, 32], [31, 36]]}

import pytest
from script_124 import valid_date


def test_valid_date_empty_string():
    """Test that empty string returns False"""
    assert valid_date('') == False


def test_valid_date_invalid_format_slash():
    """Test that date with slashes instead of dashes returns False"""
    assert valid_date('06/04/2020') == False


def test_valid_date_invalid_format_missing_parts():
    """Test that date with missing parts returns False"""
    assert valid_date('06-04') == False


def test_valid_date_invalid_format_too_many_parts():
    """Test that date with too many parts returns False"""
    assert valid_date('06-04-2020-01') == False


def test_valid_date_invalid_month_zero():
    """Test that month 0 returns False"""
    assert valid_date('00-15-2020') == False


def test_valid_date_invalid_month_thirteen():
    """Test that month 13 returns False"""
    assert valid_date('13-15-2020') == False


def test_valid_date_invalid_day_31_month_zero():
    """Test day 0 in 31-day month returns False"""
    assert valid_date('01-00-2020') == False


def test_valid_date_invalid_day_31_month_32():
    """Test day 32 in 31-day month returns False"""
    assert valid_date('01-32-2020') == False


def test_valid_date_valid_31_day_month():
    """Test valid date in 31-day month returns True"""
    assert valid_date('01-15-2020') == True


def test_valid_date_invalid_day_30_month_zero():
    """Test day 0 in 30-day month returns False"""
    assert valid_date('04-00-2020') == False


def test_valid_date_invalid_day_30_month_31():
    """Test day 31 in 30-day month returns False"""
    assert valid_date('04-31-2020') == False


def test_valid_date_valid_30_day_month():
    """Test valid date in 30-day month returns True"""
    assert valid_date('06-04-2020') == True


def test_valid_date_invalid_day_february_zero():
    """Test day 0 in February returns False"""
    assert valid_date('02-00-2020') == False


def test_valid_date_invalid_day_february_30():
    """Test day 30 in February returns False"""
    assert valid_date('02-30-2020') == False


def test_valid_date_valid_february():
    """Test valid date in February returns True"""
    assert valid_date('02-15-2020') == True


def test_valid_date_valid_with_whitespace():
    """Test that valid date with surrounding whitespace returns True"""
    assert valid_date('  03-11-2000  ') == True


def test_valid_date_non_numeric_month():
    """Test that non-numeric month returns False"""
    assert valid_date('ab-15-2020') == False


def test_valid_date_non_numeric_day():
    """Test that non-numeric day returns False"""
    assert valid_date('03-ab-2020') == False


def test_valid_date_non_numeric_year():
    """Test that non-numeric year returns False"""
    assert valid_date('03-15-abcd') == False
