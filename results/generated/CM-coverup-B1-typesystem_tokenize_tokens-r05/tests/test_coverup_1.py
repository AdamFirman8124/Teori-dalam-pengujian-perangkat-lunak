# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

import pytest

from typesystem.tokenize.tokens import DictToken, ScalarToken


def _make_dict_token():
    key_a = ScalarToken("a", 1, 4)
    key_b = ScalarToken("b", 6, 9)
    value_1 = ScalarToken(1, 5, 6)
    value_2 = ScalarToken(2, 10, 11)
    token = DictToken({key_a: value_1, key_b: value_2}, 0, 12, content='{"a": 1, "b": 2}')
    return token, key_a, key_b, value_1, value_2


def test_dict_token_init_populates_child_maps():
    token, key_a, key_b, value_1, value_2 = _make_dict_token()

    assert token._child_keys == {"a": key_a, "b": key_b}
    assert token._child_keys["a"] is key_a
    assert token._child_keys["b"] is key_b
    assert token._child_tokens == {"a": value_1, "b": value_2}
    assert token._child_tokens["a"] is value_1
    assert token._child_tokens["b"] is value_2


def test_dict_token_init_empty_dict():
    token = DictToken({}, 0, 2, content="{}")

    assert token._child_keys == {}
    assert token._child_tokens == {}
    assert token._get_value() == {}


def test_dict_token_get_value():
    token, _, _, _, _ = _make_dict_token()

    assert token._get_value() == {"a": 1, "b": 2}


def test_dict_token_get_value_nested_dict():
    inner_key = ScalarToken("x", 6, 9)
    inner_value = ScalarToken(42, 10, 12)
    inner = DictToken({inner_key: inner_value}, 5, 13)
    outer_key = ScalarToken("nested", 1, 9)
    outer = DictToken({outer_key: inner}, 0, 14)

    assert outer._get_value() == {"nested": {"x": 42}}
    assert outer._get_child_token("nested") is inner
    assert outer._get_key_token("nested") is outer_key


def test_dict_token_get_child_token():
    token, _, _, value_1, value_2 = _make_dict_token()

    assert token._get_child_token("a") is value_1
    assert token._get_child_token("b") is value_2
    with pytest.raises(KeyError):
        token._get_child_token("missing")


def test_dict_token_get_key_token():
    token, key_a, key_b, _, _ = _make_dict_token()

    assert token._get_key_token("a") is key_a
    assert token._get_key_token("b") is key_b
    with pytest.raises(KeyError):
        token._get_key_token("missing")
