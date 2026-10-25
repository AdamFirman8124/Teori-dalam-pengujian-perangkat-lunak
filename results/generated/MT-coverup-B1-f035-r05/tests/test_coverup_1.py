# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f035 import max_element


def test_max_element_increasing_executes_true_branch():
    data = [1, 2, 3, 10, 4]
    original = list(data)
    assert max_element(data) == 10
    assert data == original


def test_max_element_decreasing_executes_false_branch():
    data = [9, 5, 3, 1]
    original = list(data)
    assert max_element(data) == 9
    assert data == original


def test_max_element_single_element():
    assert max_element([42]) == 42


def test_max_element_duplicates_and_negatives():
    assert max_element([2, 2, 2]) == 2
    assert max_element([-5, -1, -3]) == -1
    assert max_element([0, -7, 0]) == 0
