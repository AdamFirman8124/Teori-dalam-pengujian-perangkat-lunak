# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


# NOTE: valid_date is a pure function (no I/O, no global state, no side
# effects), so no monkeypatching or fixture-based cleanup is required; each
# test is self-contained and leaves no state behind.


@pytest.mark.parametrize(
    "date",
    [
        "01-01-2020",        # January, mid-range day
        "12-29-2021",        # 31-day month, highest day actually accepted
        "04-29-2020",        # 30-day month, highest day actually accepted
        "02-29-2020",        # February, boundary day (year not validated)
        "  06-15-1999  ",    # exercises the .strip() call on line 4
        "1-1-2020",          # single-digit month/day still parse via int()
    ],
)
def test_valid_date_accepts_valid_dates(date):
    """Dates accepted by the implementation must reach line 18 and return True."""
    assert valid_date(date) is True


@pytest.mark.parametrize(
    "date",
    [
        "00-10-2020",        # month < 1  -> line 8
        "13-10-2020",        # month > 12 -> line 8
    ],
)
def test_valid_date_rejects_out_of_range_month(date):
    assert valid_date(date) is False


@pytest.mark.parametrize(
    "date",
    [
        "01-00-2020",        # 31-day month with day < 1 -> line 10
        "01-32-2020",        # day > 31                  -> line 10
        "12-33-2020",        # day > 31 for another 31-day month
    ],
)
def test_valid_date_rejects_bad_day_for_31_day_month(date):
    assert valid_date(date) is False


@pytest.mark.parametrize(
    "date",
    [
        "04-00-2020",        # 30-day month with day < 1 -> line 12
        "04-31-2020",        # day > 30                  -> line 12
        "06-31-2020",
        "09-31-2020",
        "11-31-2020",
    ],
)
def test_valid_date_rejects_bad_day_for_30_day_month(date):
    assert valid_date(date) is False


@pytest.mark.parametrize(
    "date",
    [
        "02-00-2020",        # February with day < 1 -> line 14
        "02-30-2020",        # day > 29              -> line 14
    ],
)
def test_valid_date_rejects_bad_day_for_february(date):
    assert valid_date(date) is False


@pytest.mark.parametrize(
    "date",
    [
        # Because of operator precedence in the implementation, the
        # `or day > 30` / `or day > 29` arms apply to *every* month, so
        # days 30 and 31 are rejected regardless of the month.
        "01-30-2020",        # rejected by line 13's `day > 29`
        "12-30-2021",        # rejected by line 13's `day > 29`
        "01-31-2020",        # rejected by line 11's `day > 30`
        "12-31-2021",        # rejected by line 11's `day > 30`
    ],
)
def test_valid_date_rejects_day_30_and_31_for_all_months(date):
    """Documents the implementation's actual (precedence-driven) behavior."""
    assert valid_date(date) is False


@pytest.mark.parametrize(
    "date",
    [
        "",                  # split('-') on empty string -> ValueError
        "01-01",             # not enough parts -> ValueError on unpacking
        "01-01-2020-extra",  # too many parts   -> ValueError on unpacking
        "aa-bb-cccc",        # non-numeric month/day/year -> ValueError
        "01-01-20x0",        # non-numeric year -> ValueError
        None,                # None.strip() -> AttributeError
        12345,               # int has no .strip() -> AttributeError
    ],
)
def test_valid_date_rejects_malformed_input_via_except_branch(date):
    """Malformed input must be caught by the bare except (lines 15-16)."""
    assert valid_date(date) is False


def test_valid_date_does_not_validate_year():
    """The year is parsed but never range-checked, so odd years pass."""
    assert valid_date("02-29-1900") is True
    assert valid_date("01-01-99999") is True
    assert valid_date("01-01-0") is True
