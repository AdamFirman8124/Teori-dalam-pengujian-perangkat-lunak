# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

from f124 import valid_date


def test_valid_date_success_31_day_month():
    assert valid_date("01-15-2020") is True


def test_valid_date_strips_whitespace():
    assert valid_date("  06-15-2021  ") is True


def test_valid_date_month_out_of_range_low():
    assert valid_date("0-15-2020") is False


def test_valid_date_month_out_of_range_high():
    assert valid_date("13-15-2020") is False


def test_valid_date_31_day_month_day_zero():
    # (month in 31-day list and day < 1) -> True
    assert valid_date("1-0-2020") is False


def test_valid_date_day_gt_31():
    # day > 31 -> True
    assert valid_date("1-32-2020") is False


def test_valid_date_day_31_rejected():
    # day=31 passes first check but fails day > 30 check
    assert valid_date("01-31-2020") is False


def test_valid_date_30_day_month_day_zero():
    # (month in 30-day list and day < 1) -> True
    assert valid_date("4-0-2020") is False


def test_valid_date_30_day_month_day_30_rejected():
    # day=30 passes first two checks but fails day > 29 check
    assert valid_date("4-30-2020") is False


def test_valid_date_day_30_rejected():
    assert valid_date("1-30-2020") is False


def test_valid_date_february_29_valid():
    assert valid_date("2-29-2020") is True


def test_valid_date_february_30_invalid():
    assert valid_date("2-30-2020") is False


def test_valid_date_february_day_zero():
    # (month == 2 and day < 1) -> True
    assert valid_date("2-0-2020") is False


def test_valid_date_exception_bad_format():
    assert valid_date("1-2020") is False


def test_valid_date_exception_non_numeric():
    assert valid_date("aa-bb-cccc") is False


def test_valid_date_exception_non_string():
    assert valid_date(None) is False
