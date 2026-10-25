# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f136 import largest_smallest_integers


def test_largest_smallest_integers_with_negative_and_positive_values():
    values = [-7, -2, 0, 3, 9]
    original_values = values.copy()

    result = largest_smallest_integers(values)

    assert result == (-2, 3)
    assert values == original_values


def test_largest_smallest_integers_with_only_negative_values():
    values = [-8, -4, -1]
    original_values = values.copy()

    result = largest_smallest_integers(values)

    assert result == (-1, None)
    assert values == original_values


def test_largest_smallest_integers_with_only_positive_values():
    values = [2, 5, 11]
    original_values = values.copy()

    result = largest_smallest_integers(values)

    assert result == (None, 2)
    assert values == original_values


def test_largest_smallest_integers_with_no_negative_or_positive_values():
    values = [0, 0]
    original_values = values.copy()

    result = largest_smallest_integers(values)

    assert result == (None, None)
    assert values == original_values
