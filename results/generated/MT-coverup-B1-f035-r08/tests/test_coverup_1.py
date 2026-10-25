# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f035 import max_element


def test_max_element_updates_maximum():
    assert max_element([1, 3, 2, 5, 4]) == 5


def test_max_element_keeps_initial_maximum():
    assert max_element([5, 4, 3, 2, 1]) == 5
