# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f047 import median


def test_median_with_odd_number_of_unsorted_values():
    values = [9, 1, 5]

    assert median(values) == 5
    assert values == [9, 1, 5]


def test_median_with_even_number_of_unsorted_values():
    values = [8, 2, 6, 4]

    assert median(values) == 5.0
    assert values == [8, 2, 6, 4]
