# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


def test_valid_date_returns_true_for_valid_dates():
    # Success path: lines 3-14 pass through, line 18 executes.
    # NOTE: due to operator precedence in the source, any day > 29 returns False,
    # so valid inputs must have day <= 29.
    assert valid_date("03-15-2021") is True
    assert valid_date("12-29-1999") is True
    assert valid_date("02-29-2020") is True
    assert valid_date("04-29-2021") is True


def test_valid_date_strips_whitespace():
    # Covers line 4 (.strip()) on the success path.
    assert valid_date("  03-15-2021  ") is True
    assert valid_date("\t02-29-2020\n") is True


def test_valid_date_month_out_of_range():
    # Covers the True branch of line 7 (month < 1 or month > 12) -> line 8.
    assert valid_date("00-10-2020") is False
    assert valid_date("13-10-2020") is False


def test_valid_date_31_day_month_branches():
    # Covers line 9 -> line 10 (day < 1 for a 31-day month).
    assert valid_date("01-00-2020") is False
    # Covers line 9's unguarded 'or day > 31'.
    assert valid_date("01-32-2020") is False


def test_valid_date_30_day_month_branches():
    # Covers line 11 -> line 12 (day < 1 for a 30-day month).
    assert valid_date("04-00-2020") is False
    # Covers line 11's unguarded 'or day > 30' (month 1 is not in the list).
    assert valid_date("01-31-2020") is False


def test_valid_date_february_branches():
    # Covers line 13 -> line 14 (day < 1 for February).
    assert valid_date("02-00-2020") is False
    # Covers line 13's unguarded 'or day > 29' (month 1 is not February).
    assert valid_date("01-30-2020") is False


def test_valid_date_exception_paths():
    # Covers the except branch (line 15) -> line 16.
    assert valid_date("") is False                   # not enough values to unpack
    assert valid_date("01-15") is False              # not enough values to unpack
    assert valid_date("01-15-2020-extra") is False   # too many values to unpack
    assert valid_date("ab-cd-efgh") is False         # int() raises ValueError
    assert valid_date(None) is False                 # None.strip() raises AttributeError
