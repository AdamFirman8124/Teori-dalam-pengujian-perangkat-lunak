# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f122 import add_elements


def test_add_elements_includes_only_one_and_two_digit_values():
    assert add_elements([1, 23, 100, -4, 999], 4) == 20


def test_add_elements_with_empty_slice():
    assert add_elements([1, 2, 3], 0) == 0
