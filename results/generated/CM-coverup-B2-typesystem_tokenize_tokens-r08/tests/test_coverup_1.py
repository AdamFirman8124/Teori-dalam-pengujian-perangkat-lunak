# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

import pytest

from typesystem.tokenize.tokens import DictToken, ScalarToken


def test_dict_token_init_populates_child_maps():
    key_a = ScalarToken("a", 0, 1)
    key_b = ScalarToken("b", 2, 3)
    value_1 = ScalarToken(1, 4, 5)
    value_2 = ScalarToken(2, 6, 7)
    value = {key_a: value_1, key_b: value_2}

    token = DictToken(value, 0, 7, content='{"a": 1, "b": 2}')

    assert token._value is value
    assert token._child_keys == {"a": key_a, "b": key_b}
    assert token._child_keys["a"] is key_a
    assert token._child_keys["b"] is key_b
    assert token._child_tokens == {"a": value_1, "b": value_2}
    assert token._child_tokens["a"] is value_1
    assert token._child_tokens["b"] is value_2


def test_dict_token_get_value():
    key_a = ScalarToken("a", 0, 1)
    key_b = ScalarToken("b", 2, 3)
    value_1 = ScalarToken(1, 4, 5)
    value_2 = ScalarToken(2, 6, 7)

    token = DictToken({key_a: value_1, key_b: value_2}, 0, 7)

    result = token._get_value()

    assert result == {"a": 1, "b": 2}
    assert type(result) is dict


def test_dict_token_get_child_token():
    key_a = ScalarToken("a", 0, 1)
    value_1 = ScalarToken(1, 4, 5)

    token = DictToken({key_a: value_1}, 0, 5)

    assert token._get_child_token("a") is value_1
    with pytest.raises(KeyError):
        token._get_child_token("missing")


def test_dict_token_get_key_token():
    key_a = ScalarToken("a", 0, 1)
    value_1 = ScalarToken(1, 4, 5)

    token = DictToken({key_a: value_1}, 0, 5)

    assert token._get_key_token("a") is key_a
    with pytest.raises(KeyError):
        token._get_key_token("missing")


def test_dict_token_empty_dict():
    token = DictToken({}, 0, 2, content="{}")

    assert token._child_keys == {}
    assert token._child_tokens == {}
    assert token._get_value() == {}
    with pytest.raises(KeyError):
        token._get_child_token("a")
    with pytest.raises(KeyError):
        token._get_key_token("a")


def test_dict_token_nested_dict_value():
    inner_key = ScalarToken("x", 0, 1)
    inner_value = ScalarToken(10, 2, 4)
    inner = DictToken({inner_key: inner_value}, 0, 4)
    outer_key = ScalarToken("inner", 5, 10)

    token = DictToken({outer_key: inner}, 0, 10)

    assert token._get_value() == {"inner": {"x": 10}}
    assert token._get_child_token("inner") is inner
    assert token._get_key_token("inner") is outer_key
    assert token._get_child_token("inner")._get_value() == {"x": 10}
