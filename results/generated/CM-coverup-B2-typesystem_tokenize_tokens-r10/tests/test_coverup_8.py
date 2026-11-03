# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

"""Tests targeting previously uncovered lines in typesystem/tokenize/tokens.py:

    - line 103: ListToken._get_value
                (return [token._get_value() for token in self._value])
    - line 106: ListToken._get_child_token
                (return self._value[key])

These tests only construct local Token objects and never mutate module or
global state, so no monkeypatching/teardown is required to avoid pollution.
"""

import pytest

from typesystem.tokenize.tokens import ListToken, ScalarToken, Token


def _make_children(*values):
    """Build a list of ScalarToken children with distinct index ranges."""
    children = []
    start = 0
    for value in values:
        children.append(
            ScalarToken(value=value, start_index=start, end_index=start + 1)
        )
        start += 2
    return children


def test_list_token_get_value_maps_child_tokens():
    children = _make_children(1, 2, 3)
    token = ListToken(value=children, start_index=0, end_index=5)

    result = token._get_value()

    # Postcondition: one entry per child, each produced by calling the
    # child token's own _get_value() implementation.
    assert isinstance(result, list)
    assert len(result) == len(children)
    assert result == [child._get_value() for child in children]
    assert result == [1, 2, 3]


def test_list_token_get_value_with_no_children():
    # Exercises the comprehension with zero iterations (empty-list branch).
    token = ListToken(value=[], start_index=0, end_index=0)

    assert token._get_value() == []


def test_list_token_get_child_token_returns_child_at_index():
    children = _make_children("a", "b", "c")
    token = ListToken(value=children, start_index=0, end_index=5)

    # Postcondition: the exact child token stored at the requested index is
    # returned (identity check, not merely equality).
    assert token._get_child_token(0) is children[0]
    assert token._get_child_token(1) is children[1]
    assert token._get_child_token(2) is children[2]
    assert isinstance(token._get_child_token(0), Token)

    # Negative indices behave like plain list indexing.
    assert token._get_child_token(-1) is children[2]
    assert token._get_child_token(-3) is children[0]


def test_list_token_get_child_token_out_of_range_raises():
    children = _make_children("a", "b")
    token = ListToken(value=children, start_index=0, end_index=3)

    with pytest.raises(IndexError):
        token._get_child_token(len(children))
