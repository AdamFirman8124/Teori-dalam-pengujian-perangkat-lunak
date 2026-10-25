# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


@pytest.mark.parametrize(
    ("x", "y", "z"),
    [
        (1, 2, 3),  # x + y == z
        (1, 3, 2),  # x + z == y
        (3, 1, 2),  # y + z == x
    ],
)
def test_any_int_returns_true_when_two_values_sum_to_third(x, y, z):
    assert any_int(x, y, z) is True


@pytest.mark.parametrize(
    ("x", "y", "z"),
    [
        (1, 1, 3),
        ("1", 2, 3),
        (1, "2", 3),
        (1, 2, "3"),
    ],
)
def test_any_int_returns_false_for_no_sum_or_non_integer(x, y, z):
    assert any_int(x, y, z) is False
