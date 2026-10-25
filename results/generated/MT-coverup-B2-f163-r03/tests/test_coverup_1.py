# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

from f163 import generate_integers


def test_full_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_reversed_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_clamped_low():
    assert generate_integers(0, 5) == [2, 4]


def test_clamped_high():
    assert generate_integers(5, 20) == [6, 8]


def test_both_above_upper_bound_empty():
    assert generate_integers(10, 14) == []


def test_both_below_lower_bound_empty():
    assert generate_integers(0, 1) == []


def test_single_even():
    assert generate_integers(2, 2) == [2]


def test_single_odd_filtered_out():
    assert generate_integers(3, 3) == []


def test_odd_range_filters_to_single_even():
    assert generate_integers(3, 5) == [4]
