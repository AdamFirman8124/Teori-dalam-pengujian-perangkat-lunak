# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (3.5, 0.5),
        (7.0, 0.0),
        (0.25, 0.25),
        (12.75, 0.75),
    ],
)
def test_truncate_number_returns_fractional_part(number, expected):
    from script_2 import truncate_number

    result = truncate_number(number)

    assert result == pytest.approx(expected)
    assert isinstance(result, float)
    assert 0.0 <= result < 1.0
