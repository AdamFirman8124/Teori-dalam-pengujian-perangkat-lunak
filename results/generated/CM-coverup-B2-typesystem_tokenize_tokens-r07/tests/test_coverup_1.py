# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

import typing
import pytest
from typesystem.tokenize.tokens import DictToken, ScalarToken, Token


def test_dict_token_init_and_get_value():
    key1 = ScalarToken("a", 0, 1, content="a")
    key2 = ScalarToken("b", 2, 3, content="b")
    val1 = ScalarToken("x", 5, 6, content="x")
    val2 = ScalarToken("y", 7, 8, content="y")
    mapping = {key1: val1, key2: val2}
    token = DictToken(mapping, 0, 8, content="content")

    # postconditions for __init__ lines 84-86
    assert isinstance(token, DictToken)
    assert isinstance(token, Token)
    assert token._child_keys == {"a": key1, "b": key2}
    assert token._child_tokens == {"a": val1, "b": val2}
    assert token._child_keys["a"] is key1
    assert token._child_keys["b"] is key2
    assert token._child_tokens["a"] is val1
    assert token._child_tokens["b"] is val2

    # exercises _get_value lines 89-91 via both direct and property access
    assert token._get_value() == {"a": "x", "b": "y"}
    assert token.value == {"a": "x", "b": "y"}


def test_dict_token_get_child_token():
    key1 = ScalarToken("name", 0, 4)
    val1 = ScalarToken("example", 10, 17)
    key2 = ScalarToken("age", 5, 8)
    val2 = ScalarToken(30, 18, 20)
    token = DictToken({key1: val1, key2: val2}, 0, 20)

    # exercises _get_child_token line 95
    assert token._get_child_token("name") is val1
    assert token._get_child_token("age") is val2
    assert token._get_child_token("name")._get_value() == "example"
    assert token._get_child_token("age")._get_value() == 30


def test_dict_token_get_key_token():
    key1 = ScalarToken("k1", 0, 2)
    key2 = ScalarToken("k2", 3, 5)
    val1 = ScalarToken("v1", 6, 8)
    val2 = ScalarToken("v2", 9, 11)
    token = DictToken({key1: val1, key2: val2}, 0, 11)

    # exercises _get_key_token line 98
    assert token._get_key_token("k1") is key1
    assert token._get_key_token("k2") is key2
    assert token._get_key_token("k1")._get_value() == "k1"
    assert token._get_key_token("k2")._get_value() == "k2"
