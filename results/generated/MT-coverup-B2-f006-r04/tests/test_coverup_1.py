# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

from f006 import parse_nested_parens


def test_multiple_groups_covers_all_branches():
    """Exercises the loop, the '(' branch (lines 10-12), the else branch
    (line 14), both returns (lines 16 and 18) and the truthy side of the
    `if x` filter."""
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]


def test_max_depth_is_kept_after_depth_decreases():
    """max_depth must record the deepest point reached, not the final depth:
    for '((()))' the depth ends at 0 but the maximum was 3."""
    assert parse_nested_parens('((()))') == [3]
    assert parse_nested_parens('()') == [1]
    assert parse_nested_parens('(()())') == [2]


def test_empty_groups_are_filtered_out():
    """Consecutive separators produce empty strings after split(' ');
    covers the falsy branch of the `if x` filter on line 18."""
    assert parse_nested_parens('()  ()') == [1, 1]
    assert parse_nested_parens(' () ') == [1]


def test_empty_string_yields_empty_list():
    """''.split(' ') == [''] and the filter drops it, so parse_paren_group
    is never invoked and an empty list is returned."""
    assert parse_nested_parens('') == []
