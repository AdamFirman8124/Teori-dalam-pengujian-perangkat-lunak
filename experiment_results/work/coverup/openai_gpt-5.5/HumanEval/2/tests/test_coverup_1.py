# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest

from script_2 import truncate_number


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (3.5, 0.5),
        (7.0, 0.0),
        (0.25, 0.25),
        (12.875, 0.875),
    ],
)
def test_truncate_number_returns_decimal_part(number, expected):
    assert truncate_number(number) == pytest.approx(expected)


def test_truncate_number_returns_value_less_than_one():
    result = truncate_number(123.456)

    assert result == pytest.approx(0.456)
    assert 0 <= result < 1
