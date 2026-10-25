# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


@pytest.mark.parametrize(
    "value",
    [
        " 1-29-2024 ",
        "4-29-2024",
        "2-29-2024",
    ],
)
def test_valid_date_accepts_parseable_dates_that_pass_all_checks(value):
    assert valid_date(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "0-15-2024",
        "13-15-2024",
    ],
)
def test_valid_date_rejects_out_of_range_months(value):
    assert valid_date(value) is False


@pytest.mark.parametrize(
    "value",
    [
        "1-0-2024",
        "1-32-2024",
    ],
)
def test_valid_date_rejects_invalid_days_at_31_day_month_check(value):
    assert valid_date(value) is False


@pytest.mark.parametrize(
    "value",
    [
        "4-0-2024",
        "4-31-2024",
    ],
)
def test_valid_date_rejects_invalid_days_at_30_day_month_check(value):
    assert valid_date(value) is False


@pytest.mark.parametrize(
    "value",
    [
        "2-0-2024",
        "2-30-2024",
    ],
)
def test_valid_date_rejects_invalid_days_at_february_check(value):
    assert valid_date(value) is False


@pytest.mark.parametrize(
    "value",
    [
        None,
        "not-a-date",
        "1-1-not-a-year",
        "1-1-2024-extra",
    ],
)
def test_valid_date_rejects_values_that_cannot_be_parsed(value):
    assert valid_date(value) is False
