# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f057 import monotonic


def test_monotonic_increasing_returns_true():
    """Covers line 3 (condition) and line 4 (return True) via sorted-ascending branch."""
    assert monotonic([1, 2, 3, 4]) is True


def test_monotonic_decreasing_returns_true():
    """Covers line 3 (condition, second operand) and line 4 (return True) via sorted-descending branch."""
    assert monotonic([4, 3, 2, 1]) is True


def test_monotonic_equal_elements_returns_true():
    """A constant list is both ascending and descending; covers line 4."""
    assert monotonic([7, 7, 7]) is True


def test_non_monotonic_returns_false():
    """Covers line 3 (condition, both operands false) and line 5 (return False)."""
    assert monotonic([1, 3, 2]) is False


def test_empty_list_is_monotonic():
    """Edge case: empty list is trivially monotonic; covers line 4."""
    assert monotonic([]) is True


def test_single_element_list_is_monotonic():
    """Edge case: single-element list is trivially monotonic; covers line 4."""
    assert monotonic([42]) is True


def test_two_element_list_non_monotonic():
    """A two-element list is always monotonic; ensures line 5 is not hit here but line 3 is."""
    assert monotonic([2, 1]) is True


def test_input_list_is_not_mutated():
    """Postcondition: the function must not mutate its argument."""
    original = [3, 1, 2]
    snapshot = list(original)
    monotonic(original)
    assert original == snapshot
