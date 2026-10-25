# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (3.75, 0.75),
        (5.0, 0.0),
        (-1.25, 0.75),
    ],
)
def test_truncate_number_returns_fractional_part(number, expected):
    assert truncate_number(number) == pytest.approx(expected)
