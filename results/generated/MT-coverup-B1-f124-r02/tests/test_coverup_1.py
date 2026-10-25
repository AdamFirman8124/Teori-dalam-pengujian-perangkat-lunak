# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

import pytest

from f124 import valid_date


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (" 1-1-2024 ", True),
        ("4-29-2024", True),
        ("2-29-2024", True),
        ("4-30-2024", False),
        ("0-1-2024", False),
        ("13-1-2024", False),
        ("1-0-2024", False),
        ("1-32-2024", False),
        ("4-0-2024", False),
        ("4-31-2024", False),
        ("2-0-2024", False),
        ("2-30-2024", False),
    ],
)
def test_valid_date_boundaries(value, expected):
    assert valid_date(value) is expected


@pytest.mark.parametrize(
    "value",
    [
        None,
        "not-a-date",
        "1-1",
        "one-1-2024",
    ],
)
def test_valid_date_rejects_malformed_values(value):
    assert valid_date(value) is False
