# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

from f163 import generate_integers


def test_generate_integers_clamps_bounds_and_filters_even_numbers():
    assert generate_integers(0, 10) == [2, 4, 6, 8]
    assert generate_integers(7, 3) == [4, 6]
    assert generate_integers(9, 10) == []
