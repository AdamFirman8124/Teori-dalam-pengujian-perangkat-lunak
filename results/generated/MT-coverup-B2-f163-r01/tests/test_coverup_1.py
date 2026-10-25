# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

from f163 import generate_integers


def test_generate_integers_normal_order():
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_generate_integers_reversed_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_generate_integers_clamps_lower_bound():
    assert generate_integers(0, 5) == [2, 4]
    assert generate_integers(-10, 3) == [2]


def test_generate_integers_clamps_upper_bound():
    assert generate_integers(5, 20) == [6, 8]
    assert generate_integers(20, 5) == [6, 8]


def test_generate_integers_filters_odd_numbers():
    assert generate_integers(3, 7) == [4, 6]
    assert generate_integers(3, 3) == []


def test_generate_integers_single_even():
    assert generate_integers(4, 4) == [4]


def test_generate_integers_empty_when_range_below_bounds():
    assert generate_integers(0, 1) == []
    assert generate_integers(-5, -1) == []


def test_generate_integers_empty_when_range_above_bounds():
    assert generate_integers(9, 10) == []
    assert generate_integers(10, 9) == []
