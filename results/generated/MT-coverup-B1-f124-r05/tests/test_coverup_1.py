# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


@pytest.mark.parametrize(
    "date",
    [
        "1-29-2024",
        "4-29-2024",
        "2-29-2024",
        " 12-1-2024 ",
    ],
)
def test_valid_date_returns_true_for_accepted_dates(date):
    assert valid_date(date) is True


@pytest.mark.parametrize(
    "date",
    [
        "0-1-2024",
        "13-1-2024",
        "1-0-2024",
        "1-32-2024",
        "4-0-2024",
        "4-31-2024",
        "2-0-2024",
        "2-30-2024",
    ],
)
def test_valid_date_rejects_out_of_range_values(date):
    assert valid_date(date) is False


@pytest.mark.parametrize(
    "date",
    [
        None,
        "",
        "1-1",
        "1-1-2024-extra",
        "January-1-2024",
    ],
)
def test_valid_date_rejects_malformed_values(date):
    assert valid_date(date) is False
