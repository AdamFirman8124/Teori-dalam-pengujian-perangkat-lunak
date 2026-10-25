# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_unique_digits_empty_input():
    x = []
    result = unique_digits(x)
    assert result == []
    assert x == []


def test_unique_digits_all_odd_digits_sorted():
    x = [135, 31, 9, 111, 5]
    original = list(x)
    result = unique_digits(x)
    assert result == [5, 9, 31, 111, 135]
    assert result == sorted(result)
    assert all(int(c) % 2 == 1 for value in result for c in str(value))
    assert x == original


def test_unique_digits_no_odd_digit_elements():
    x = [20, 42, 8, 246]
    original = list(x)
    result = unique_digits(x)
    assert result == []
    assert x == original


def test_unique_digits_mixed_elements_and_digit_positions():
    x = [135, 12, 21, 31, 9, 20, 111, 2, 7]
    original = list(x)
    result = unique_digits(x)
    assert result == [7, 9, 31, 111, 135]
    assert result == sorted(result)
    assert all(int(c) % 2 == 1 for value in result for c in str(value))
    assert x == original


def test_unique_digits_single_digit_odd_and_even():
    x = [5, 4, 3, 2, 1, 0]
    original = list(x)
    result = unique_digits(x)
    assert result == [1, 3, 5]
    assert x == original
