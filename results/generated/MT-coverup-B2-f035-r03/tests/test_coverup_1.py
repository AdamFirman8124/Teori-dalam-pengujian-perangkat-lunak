# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import f035


def test_max_element_returns_largest_value():
    assert f035.max_element([3, 1, 7, 2]) == 7


def test_max_element_handles_single_element():
    assert f035.max_element([5]) == 5
