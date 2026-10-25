# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

import pytest

from f163 import generate_integers


def test_generate_integers_normal_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_generate_integers_reversed_arguments():
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_generate_integers_clamps_lower_bound():
    assert generate_integers(0, 5) == [2, 4]


def test_generate_integers_clamps_upper_bound():
    assert generate_integers(5, 20) == [6, 8]


def test_generate_integers_clamps_both_bounds():
    assert generate_integers(-10, 100) == [2, 4, 6, 8]


def test_generate_integers_odd_bounds_filter_evens():
    assert generate_integers(3, 7) == [4, 6]


def test_generate_integers_single_even():
    assert generate_integers(4, 4) == [4]


def test_generate_integers_single_odd_empty():
    assert generate_integers(3, 3) == []


def test_generate_integers_below_range_empty():
    assert generate_integers(0, 1) == []


def test_generate_integers_above_range_empty():
    assert generate_integers(9, 10) == []


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 2, [2]),
        (7, 8, [8]),
        (1, 9, [2, 4, 6, 8]),
        (6, 3, [4, 6]),
    ],
)
def test_generate_integers_parametrized(a, b, expected):
    result = generate_integers(a, b)
    assert result == expected
    assert all(isinstance(i, int) and i % 2 == 0 and 2 <= i <= 8 for i in result)
