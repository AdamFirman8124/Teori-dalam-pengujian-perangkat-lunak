# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f122 import add_elements


def test_add_elements_includes_only_values_with_at_most_two_characters():
    arr = [1, -2, 99, 100, -100]
    original = arr.copy()

    assert add_elements(arr, len(arr)) == 98
    assert arr == original


def test_add_elements_only_considers_first_k_elements():
    arr = [10, 20, 30]

    assert add_elements(arr, 2) == 30
