# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

import typing

import pytest

from typesystem.tokenize.tokens import ListToken, Token


class _LeafToken(Token):
    """Minimal concrete token whose _get_value returns the raw value."""

    def _get_value(self) -> typing.Any:
        return self._value


def test_list_token_get_value_recurses_into_children():
    children = [
        _LeafToken(1, start_index=0, end_index=1),
        _LeafToken("two", start_index=2, end_index=5),
    ]
    token = ListToken(children, start_index=0, end_index=5)

    value = token._get_value()

    # Line 103: list comprehension over child tokens.
    assert value == [1, "two"]
    # The result must be a fresh list, not the internal _value list.
    assert value is not token._value


def test_list_token_get_value_empty_list():
    token = ListToken([], start_index=0, end_index=0)

    assert token._get_value() == []


def test_list_token_get_child_token_returns_element():
    child = _LeafToken(42, start_index=1, end_index=3)
    token = ListToken([child], start_index=0, end_index=3)

    result = token._get_child_token(0)

    # Line 106: direct indexing into the internal value list.
    assert result is child
    assert isinstance(result, Token)
    assert result._get_value() == 42


def test_list_token_get_child_token_negative_index():
    first = _LeafToken("a", start_index=0, end_index=1)
    second = _LeafToken("b", start_index=2, end_index=3)
    token = ListToken([first, second], start_index=0, end_index=3)

    assert token._get_child_token(-1) is second
    assert token._get_child_token(-2) is first


def test_list_token_get_child_token_out_of_range_raises():
    token = ListToken([], start_index=0, end_index=0)

    with pytest.raises(IndexError):
        token._get_child_token(0)
