# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

import pytest
from typesystem.tokenize.tokens import ListToken, Token


def test_list_token_get_value_delegates_to_children():
    class StubToken(Token):
        def _get_value(self):
            return self._value

    child1 = StubToken("a", 0, 1, content="a")
    child2 = StubToken(2, 1, 2, content="b")
    token = ListToken([child1, child2], 0, 2, content="ab")
    result = token._get_value()
    assert result == ["a", 2]
    # a new list is built each time, not the internal list itself
    assert result is not token._value
    assert token._value == [child1, child2]


def test_list_token_get_value_empty_list():
    token = ListToken([], 0, 0, content="")
    result = token._get_value()
    assert result == []
    assert isinstance(result, list)


def test_list_token_get_child_token_by_index():
    class StubToken(Token):
        def _get_value(self):
            return self._value

    child1 = StubToken("x", 0, 1, content="x")
    child2 = StubToken("y", 1, 2, content="y")
    token = ListToken([child1, child2], 0, 2, content="xy")
    assert token._get_child_token(0) is child1
    assert token._get_child_token(1) is child2
    assert token._get_child_token(-1) is child2
