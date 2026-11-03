# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

"""Tests for f001.separate_paren_groups.

These tests exercise every line and branch of the function:
  - initialization (lines 6-8)
  - the for-loop over characters (line 10)
  - the '(' branch (lines 11-13)
  - the ')' branch (lines 14-16)
  - the depth == 0 flush branch (lines 18-19)
  - the depth != 0 (no flush) branch (line 18, false side)
  - characters that are neither '(' nor ')' (e.g. spaces)
  - the final return (line 22), including the empty-input case

The function under test is pure (no module state, no I/O), so no
monkeypatching or fixture-based cleanup is required; each test is fully
self-contained and cannot pollute global state.
"""

from typing import List

import pytest

from f001 import separate_paren_groups


def test_mixed_groups_covers_all_branches() -> None:
    """Spaces (non-paren chars), '(' branch, ')' branch and the depth==0 flush."""
    result: List[str] = separate_paren_groups("( ) (( )) (( )( ))")
    assert result == ["()", "(())", "(()())"]


def test_unclosed_group_covers_depth_not_zero_branch() -> None:
    """A ')' that does not bring depth back to 0 must not flush a group."""
    result: List[str] = separate_paren_groups("(()")
    assert result == []


def test_deeply_nested_group() -> None:
    """Nested parens accumulate; only the outermost close flushes a group."""
    result: List[str] = separate_paren_groups("((()))")
    assert result == ["((()))"]


def test_single_pair() -> None:
    """Minimal input exercising one open, one close, one flush."""
    result: List[str] = separate_paren_groups("()")
    assert result == ["()"]


def test_empty_input_returns_empty_list() -> None:
    """Loop body never runs; the function still returns an empty list."""
    result: List[str] = separate_paren_groups("")
    assert result == []
    assert isinstance(result, list)


def test_only_separators_yields_no_groups() -> None:
    """Only non-paren characters: neither branch taken, empty result."""
    result: List[str] = separate_paren_groups("   \t ")
    assert result == []


def test_result_is_fresh_list_not_shared_state() -> None:
    """Two calls must not share internal state (guards against pollution)."""
    first: List[str] = separate_paren_groups("()")
    second: List[str] = separate_paren_groups("(())")
    assert first == ["()"]
    assert second == ["(())"]
    assert first is not second


@pytest.mark.parametrize(
    "paren_string,expected",
    [
        ("()", ["()"]),
        ("()()", ["()", "()"]),
        ("(())", ["(())"]),
        ("(()())", ["(()())"]),
        ("(()", []),
        ("())", ["()"]),
        ("", []),
    ],
)
def test_parametrized_grouping(paren_string: str, expected: List[str]) -> None:
    """Table-driven coverage of open/close/flush and unbalanced branches."""
    assert separate_paren_groups(paren_string) == expected
