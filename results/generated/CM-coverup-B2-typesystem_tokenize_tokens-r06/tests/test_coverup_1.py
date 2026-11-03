# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

import pytest

from typesystem.tokenize.tokens import DictToken, ScalarToken


def test_dict_token_init_builds_child_maps():
    # Exercises lines 84-86: super().__init__ plus the two dict comprehensions
    key_a = ScalarToken("a", 1, 4, '"a"')
    key_b = ScalarToken("b", 8, 11, '"b"')
    val_a = ScalarToken(1, 6, 7, "1")
    val_b = ScalarToken(2, 13, 14, "2")
    token = DictToken({key_a: val_a, key_b: val_b}, 0, 15, '{"a": 1, "b": 2}')

    # _child_keys / _child_tokens are keyed by the *unwrapped* key values
    assert token._child_keys == {"a": key_a, "b": key_b}
    assert token._child_tokens == {"a": val_a, "b": val_b}
    # Identity checks to make sure the exact token objects were stored
    assert token._get_key_token("a") is key_a
    assert token._get_key_token("b") is key_b
    assert token._get_child_token("a") is val_a
    assert token._get_child_token("b") is val_b


def test_dict_token_get_value_unwraps_child_tokens():
    # Exercises lines 89-91: _get_value dict comprehension
    key = ScalarToken("key", 1, 6, '"key"')
    value = ScalarToken(42, 8, 10, "42")
    token = DictToken({key: value}, 0, 11, '{"key": 42}')

    result = token._get_value()
    assert result == {"key": 42}
    assert type(result) is dict
    # The returned mapping must contain plain Python values, not tokens
    assert all(not isinstance(v, ScalarToken) for v in result.values())
    assert all(not isinstance(k, ScalarToken) for k in result.keys())
    # The public .value property delegates to _get_value()
    assert token.value == {"key": 42}


def test_dict_token_get_value_nested():
    # _get_value must recurse into nested DictToken values
    inner_key = ScalarToken("x", 10, 13, '"x"')
    inner_val = ScalarToken(True, 15, 19, "true")
    inner = DictToken({inner_key: inner_val}, 9, 20, '{"x": true}')
    outer_key = ScalarToken("outer", 1, 8, '"outer"')
    token = DictToken({outer_key: inner}, 0, 21, '{"outer": {"x": true}}')

    assert token.value == {"outer": {"x": True}}


def test_dict_token_get_child_token():
    # Exercises line 95
    key = ScalarToken("key", 1, 6, '"key"')
    value = ScalarToken(42, 8, 10, "42")
    token = DictToken({key: value}, 0, 11, '{"key": 42}')

    assert token._get_child_token("key") is value
    # Token.lookup() is built on top of _get_child_token()
    assert token.lookup(["key"]) is value


def test_dict_token_get_key_token():
    # Exercises line 98
    key = ScalarToken("key", 1, 6, '"key"')
    value = ScalarToken(42, 8, 10, "42")
    token = DictToken({key: value}, 0, 11, '{"key": 42}')

    assert token._get_key_token("key") is key
    # Token.lookup_key() is built on top of _get_key_token()
    assert token.lookup_key(["key"]) is key


def test_dict_token_missing_key_raises_keyerror():
    key = ScalarToken("key", 1, 6, '"key"')
    value = ScalarToken(42, 8, 10, "42")
    token = DictToken({key: value}, 0, 11, '{"key": 42}')

    with pytest.raises(KeyError):
        token._get_child_token("missing")
    with pytest.raises(KeyError):
        token._get_key_token("missing")
