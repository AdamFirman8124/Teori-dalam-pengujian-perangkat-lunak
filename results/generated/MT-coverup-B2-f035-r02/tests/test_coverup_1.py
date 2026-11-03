# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

"""Tests for f035.max_element covering lines 3-7 and all branches."""

from f035 import max_element


def test_max_element_max_in_middle_covers_true_branch():
    # m starts as 1 (line 3); loop hits 5 which is > m, so line 6 executes,
    # then 3 is compared (False branch) before returning (line 7).
    assert max_element([1, 5, 3]) == 5


def test_max_element_max_at_start_covers_false_branch():
    # First element is already the maximum: every comparison takes the
    # False branch of 'e > m', and the initial value is returned.
    assert max_element([9, 4, 7, 2]) == 9


def test_max_element_single_element():
    # Loop body executes exactly once with a False comparison.
    assert max_element([42]) == 42


def test_max_element_all_negative():
    # Ensures comparison logic works without assuming positive values.
    assert max_element([-10, -3, -7]) == -3


def test_max_element_with_duplicates():
    # Equal elements must not replace the current maximum (False branch),
    # while the larger duplicate path still updates m (True branch).
    assert max_element([2, 8, 8, 1, 8]) == 8
