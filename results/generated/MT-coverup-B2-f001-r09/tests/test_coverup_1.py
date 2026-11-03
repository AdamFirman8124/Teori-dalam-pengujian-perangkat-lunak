# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import pytest

from f001 import separate_paren_groups


def test_simple_group_covers_open_close_and_emit():
    """'(' branch, ')' branch, inner if True (depth back to 0), append+clear, return."""
    result = separate_paren_groups("()")
    assert isinstance(result, list)
    assert result == ["()"]


def test_nested_group_covers_depth_not_zero_branch():
    """Inner ')' leaves current_depth == 1, so the 'if current_depth == 0' check is False there."""
    result = separate_paren_groups("(())")
    assert result == ["(())"]


def test_multiple_groups_with_non_paren_characters():
    """Spaces exercise neither the '(' nor the ')' branch (both conditions False)."""
    result = separate_paren_groups("() (()) ()")
    assert result == ["()", "(())", "()"]


def test_empty_string_skips_loop_and_returns_empty_list():
    """Loop body never executes; function still returns an empty list."""
    result = separate_paren_groups("")
    assert result == []


def test_unbalanced_open_never_emits():
    """Depth never returns to 0, so nothing is appended even though '(' chars are consumed."""
    result = separate_paren_groups("((")
    assert result == []


def test_leading_close_paren_makes_depth_negative():
    """')' first drives depth to -1, so the depth == 0 check is False on that iteration."""
    result = separate_paren_groups(")(")
    assert result == []
