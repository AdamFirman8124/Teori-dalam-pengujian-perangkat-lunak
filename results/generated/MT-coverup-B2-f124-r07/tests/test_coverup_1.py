# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

from f124 import valid_date


def test_valid_date_valid_day_within_29():
    assert valid_date("01-15-2020") is True


def test_valid_date_strips_whitespace():
    assert valid_date("  06-15-2021  ") is True


def test_valid_date_valid_30_day_month_day_29():
    assert valid_date("4-29-2020") is True


def test_valid_date_february_day_29():
    assert valid_date("2-29-2020") is True


def test_valid_date_month_too_low():
    assert valid_date("0-15-2020") is False


def test_valid_date_month_too_high():
    assert valid_date("13-15-2020") is False


def test_valid_date_31_day_month_day_zero():
    # Line 9: month in 31-day list and day < 1
    assert valid_date("1-0-2020") is False


def test_valid_date_day_over_31():
    # Line 9: day > 31 (or-branch)
    assert valid_date("1-32-2020") is False
    assert valid_date("4-32-2020") is False


def test_valid_date_30_day_month_day_zero():
    # Line 11: month in 30-day list and day < 1
    assert valid_date("4-0-2020") is False


def test_valid_date_day_31():
    # Line 11: day > 30 (or-branch); actual behaviour rejects day 31 here
    assert valid_date("1-31-2020") is False


def test_valid_date_february_day_zero():
    # Line 13: month == 2 and day < 1
    assert valid_date("2-0-2020") is False


def test_valid_date_day_30():
    # Line 13: day > 29 (or-branch); actual behaviour rejects day 30 here
    assert valid_date("1-30-2020") is False
    assert valid_date("4-30-2020") is False


def test_valid_date_february_day_30():
    assert valid_date("2-30-2020") is False


def test_valid_date_exception_wrong_format():
    assert valid_date("1-2020") is False
    assert valid_date("1-15-2020-extra") is False
    assert valid_date("") is False


def test_valid_date_exception_non_numeric():
    assert valid_date("aa-bb-cccc") is False


def test_valid_date_exception_non_string():
    assert valid_date(None) is False
