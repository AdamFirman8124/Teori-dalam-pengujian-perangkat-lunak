# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f057 import monotonic


def test_monotonic_increasing_returns_true():
    """Covers line 3 (condition true via sorted(l)) and line 4."""
    assert monotonic([1, 2, 3]) is True


def test_monotonic_decreasing_returns_true():
    """Covers line 3 (condition true via sorted(l, reverse=True)) and line 4."""
    assert monotonic([3, 2, 1]) is True


def test_monotonic_non_monotonic_returns_false():
    """Covers line 3 (condition false) and line 5."""
    assert monotonic([1, 3, 2]) is False


def test_monotonic_empty_list():
    """Edge case: empty list is trivially monotonic (line 4)."""
    assert monotonic([]) is True


def test_monotonic_single_element():
    """Edge case: single element is trivially monotonic (line 4)."""
    assert monotonic([42]) is True


def test_monotonic_equal_elements():
    """Edge case: all-equal list is both non-decreasing and non-increasing (line 4)."""
    assert monotonic([7, 7, 7]) is True


def test_monotonic_non_strict_increasing():
    """Duplicates still count as monotonic increasing (line 4)."""
    assert monotonic([1, 1, 2, 3]) is True


def test_monotonic_non_strict_decreasing():
    """Duplicates still count as monotonic decreasing (line 4)."""
    assert monotonic([3, 3, 2, 1]) is True


def test_monotonic_unsorted_with_duplicates_returns_false():
    """Non-monotonic list with duplicates hits line 5."""
    assert monotonic([1, 2, 2, 1]) is False


def test_monotonic_does_not_mutate_input():
    """Postcondition: the input list is not modified by the function."""
    data = [3, 1, 2]
    monotonic(data)
    assert data == [3, 1, 2]
