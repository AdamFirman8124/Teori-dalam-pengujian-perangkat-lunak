# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

from f163 import generate_integers


def test_generate_integers_clamps_bounds_and_filters_odds():
    assert generate_integers(0, 10) == [2, 4, 6, 8]


def test_generate_integers_accepts_reversed_bounds():
    assert generate_integers(7, 3) == [4, 6]


def test_generate_integers_returns_empty_list_for_out_of_range_bounds():
    assert generate_integers(9, 12) == []
