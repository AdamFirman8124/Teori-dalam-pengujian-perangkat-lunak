# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f138 import is_equal_to_sum_even


@pytest.mark.parametrize(
    "n, expected",
    [
        (8, True),
        (10, True),
        (100, True),
        (6, False),
        (2, False),
        (0, False),
        (-8, False),
        (7, False),
        (9, False),
        (1, False),
        (-7, False),
    ],
)
def test_is_equal_to_sum_even(n, expected):
    assert is_equal_to_sum_even(n) is expected


def test_is_equal_to_sum_even_even_and_at_least_eight():
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(12) is True


def test_is_equal_to_sum_even_even_but_less_than_eight():
    assert is_equal_to_sum_even(6) is False
    assert is_equal_to_sum_even(0) is False


def test_is_equal_to_sum_even_odd():
    assert is_equal_to_sum_even(9) is False
    assert is_equal_to_sum_even(7) is False
