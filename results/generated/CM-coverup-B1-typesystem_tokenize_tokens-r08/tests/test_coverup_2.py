# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest

from typesystem.tokenize.tokens import Token


class _ChildToken(Token):
    """Concrete Token that returns a fixed child for any key."""

    def __init__(self, child):
        super().__init__(value="child-holder", start_index=0, end_index=0)
        self._child = child

    def _get_child_token(self, key):
        return self._child


def test_lookup_traverses_children():
    leaf = Token(value="leaf", start_index=0, end_index=4)
    middle = _ChildToken(child=leaf)
    root = _ChildToken(child=middle)

    result = root.lookup(index=[0, 1])

    assert result is leaf
    assert result._value == "leaf"


def test_lookup_empty_index_returns_self():
    token = Token(value="root", start_index=0, end_index=4)

    result = token.lookup(index=[])

    assert result is token
