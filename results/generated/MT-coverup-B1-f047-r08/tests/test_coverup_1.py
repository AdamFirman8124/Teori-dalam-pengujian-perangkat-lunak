# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f047 import median


def test_median_odd_length():
    data = [3, 1, 2]
    original = list(data)
    result = median(data)
    assert result == 2
    # postcondition: input must not be mutated (sorted() creates new list)
    assert data == original


def test_median_odd_single_element():
    assert median([42]) == 42


def test_median_even_length():
    data = [4, 1, 3, 2]
    original = list(data)
    result = median(data)
    assert result == 2.5
    assert data == original


def test_median_even_two_elements():
    assert median([10, 2]) == 6.0
