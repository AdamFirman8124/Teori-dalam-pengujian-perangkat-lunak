# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

"""Tests for f022.filter_integers.

Line 6 (the list-comprehension return) only executes when the function is
actually called, so these tests invoke it with inputs that exercise both
branches of the ``isinstance(x, int)`` filter.

The function under test is pure (no I/O, no globals, no side effects), so no
monkeypatching or teardown is required; each test is fully self-contained and
leaves no state behind.
"""

from f022 import filter_integers


def test_filter_integers_mixed_types_executes_line_6():
    """Mixed input: exercises both the keep and skip branches of the filter."""
    values = [1, "hello", 2.5, 3, None, [4], 5]
    result = filter_integers(values)
    assert result == [1, 3, 5]
    # Postcondition: every returned element is an int.
    assert all(isinstance(x, int) for x in result)
    # Postcondition: input list is not mutated.
    assert values == [1, "hello", 2.5, 3, None, [4], 5]


def test_filter_integers_empty_list():
    """Empty input still executes line 6 and yields an empty list."""
    assert filter_integers([]) == []


def test_filter_integers_no_integers():
    """All elements filtered out: exercises only the skip branch."""
    assert filter_integers(["a", 1.5, None, 3.14, {"k": 1}]) == []


def test_filter_integers_all_integers():
    """All elements kept: exercises only the keep branch."""
    assert filter_integers([0, -1, 42, 7]) == [0, -1, 42, 7]


def test_filter_integers_zero_and_negatives():
    """Zero and negative integers are valid ints and must be kept."""
    result = filter_integers([-3, 0, "x", -7.5, 9])
    assert result == [-3, 0, 9]


def test_filter_integers_bools_are_ints():
    """Documents Python semantics: bool is a subclass of int, so kept."""
    result = filter_integers([True, False, "no", 2])
    assert result == [True, False, 2]
    assert all(isinstance(x, int) for x in result)
