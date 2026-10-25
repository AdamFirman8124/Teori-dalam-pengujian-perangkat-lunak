# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f047 import median


def test_median_with_odd_number_of_items():
    values = [9, 1, 5]
    original = values.copy()

    assert median(values) == 5
    assert values == original


def test_median_with_even_number_of_items():
    values = [10, 2, 8, 4]
    original = values.copy()

    assert median(values) == 6.0
    assert values == original
