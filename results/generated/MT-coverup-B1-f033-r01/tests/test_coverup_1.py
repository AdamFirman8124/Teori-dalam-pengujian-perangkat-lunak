# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f033 import sort_third


def test_sort_third_sorts_every_third_element_without_mutating_input():
    original = [9, 8, 7, 6, 5, 4, 3]

    result = sort_third(original)

    assert result == [3, 8, 7, 6, 5, 4, 9]
    assert original == [9, 8, 7, 6, 5, 4, 3]
    assert result is not original
