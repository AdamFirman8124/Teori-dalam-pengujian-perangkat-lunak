# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f035 import max_element


def test_max_element_returns_largest_value():
    values = [2, 5, 3]
    original_values = values.copy()

    result = max_element(values)

    assert result == 5
    assert values == original_values


def test_max_element_returns_first_value_when_all_others_are_smaller():
    values = [7, 4, 1]
    original_values = values.copy()

    result = max_element(values)

    assert result == 7
    assert values == original_values
