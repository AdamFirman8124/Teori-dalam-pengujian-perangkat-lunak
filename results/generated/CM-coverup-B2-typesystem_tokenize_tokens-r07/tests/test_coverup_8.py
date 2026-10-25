# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

import pytest

from typesystem.tokenize.tokens import ListToken, ScalarToken


def test_list_token_get_value():
    inner_tokens = [
        ScalarToken(value=1, start_index=0, end_index=1, content="1"),
        ScalarToken(value="a", start_index=1, end_index=2, content="a"),
    ]
    token = ListToken(value=inner_tokens, start_index=0, end_index=2, content="[1a]")

    result = token._get_value()

    # Line 103: list comprehension over child tokens calling _get_value()
    assert result == [1, "a"]
    assert isinstance(result, list)
    assert len(result) == len(inner_tokens)


def test_list_token_get_child_token():
    inner_tokens = [
        ScalarToken(value=1, start_index=0, end_index=1, content="1"),
        ScalarToken(value="a", start_index=1, end_index=2, content="a"),
    ]
    token = ListToken(value=inner_tokens, start_index=0, end_index=2, content="[1a]")

    child = token._get_child_token(1)

    # Line 106: indexing into self._value
    assert child is inner_tokens[1]
    assert child._get_value() == "a"

    first = token._get_child_token(0)
    assert first is inner_tokens[0]
    assert first._get_value() == 1
