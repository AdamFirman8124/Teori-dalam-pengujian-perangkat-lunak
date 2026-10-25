# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f047 import median


def test_median_odd_length_unsorted():
    data = [3, 1, 2]
    original = list(data)
    assert median(data) == 2
    assert data == original


def test_median_even_length_unsorted():
    data = [4, 1, 3, 2]
    original = list(data)
    result = median(data)
    assert result == 2.5
    assert isinstance(result, float)
    assert data == original


def test_median_single_element():
    assert median([42]) == 42


def test_median_two_elements():
    result = median([10, 0])
    assert result == 5.0
    assert isinstance(result, float)
