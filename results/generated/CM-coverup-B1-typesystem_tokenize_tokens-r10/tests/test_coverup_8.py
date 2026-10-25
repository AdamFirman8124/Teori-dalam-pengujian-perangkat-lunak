# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

import pytest

from typesystem.tokenize.tokens import ListToken, ScalarToken


def test_list_token_get_value_returns_child_values():
    children = [
        ScalarToken("alpha", 1, 6, '["alpha", 42]'),
        ScalarToken(42, 8, 10, '["alpha", 42]'),
    ]
    token = ListToken(children, 0, 11, '["alpha", 42]')

    assert token._get_value() == ["alpha", 42]


def test_list_token_get_child_token_returns_indexed_token():
    children = [
        ScalarToken("alpha", 1, 6, '["alpha", 42]'),
        ScalarToken(42, 8, 10, '["alpha", 42]'),
    ]
    token = ListToken(children, 0, 11, '["alpha", 42]')

    assert token._get_child_token(0) is children[0]
    assert token._get_child_token(1) is children[1]

    with pytest.raises(IndexError):
        token._get_child_token(2)
