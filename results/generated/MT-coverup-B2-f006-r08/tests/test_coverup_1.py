# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

import pytest

from f006 import parse_nested_parens


def test_parse_nested_parens_multiple_groups():
    """Covers lines 6-18: inner function, '(' branch (depth/max_depth update),
    else branch (')' decrements), return of max_depth, and the list comprehension."""
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]


def test_parse_nested_parens_single_group():
    """Covers a single group with both '(' and ')' characters."""
    assert parse_nested_parens('((()))') == [3]


def test_parse_nested_parens_filters_empty_groups():
    """Extra spaces produce empty strings after split(), exercising the
    falsy branch of the `if x` filter in the comprehension."""
    result = parse_nested_parens('  ((()))  ()  ')
    assert result == [3, 1]


def test_parse_nested_parens_empty_string():
    """An empty input string yields an empty result list (comprehension
    filter rejects the single empty split element)."""
    assert parse_nested_parens('') == []


def test_parse_nested_parens_balanced_returns_to_zero():
    """Depths must return to zero for balanced groups; max depth is tracked
    via max(depth, max_depth) on line 12."""
    assert parse_nested_parens('() ()() ((())())') == [1, 1, 3]
