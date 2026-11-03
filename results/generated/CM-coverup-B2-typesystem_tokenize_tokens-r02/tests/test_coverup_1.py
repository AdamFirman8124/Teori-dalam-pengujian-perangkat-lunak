# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

import pytest

from typesystem.tokenize.tokens import DictToken, ScalarToken


def test_dict_token_init_builds_child_maps():
    """Lines 84-86: __init__ stores the value and builds the lookup maps."""
    key_a = ScalarToken("a", 0, 3, '"a"')
    key_b = ScalarToken("b", 10, 13, '"b"')
    val_one = ScalarToken(1, 5, 6, "1")
    val_two = ScalarToken(2, 15, 16, "2")
    value = {key_a: val_one, key_b: val_two}

    token = DictToken(value, 0, 16, '{"a": 1, "b": 2}')

    assert token._value is value
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == '{"a": 1, "b": 2}'
    # _child_keys maps each key token's raw value to the key token itself.
    assert token._child_keys["a"] is key_a
    assert token._child_keys["b"] is key_b
    # _child_tokens maps each key token's raw value to the value token.
    assert token._child_tokens["a"] is val_one
    assert token._child_tokens["b"] is val_two


def test_dict_token_init_with_keyword_args():
    """Exercise the **kwargs branch of DictToken.__init__ (line 84)."""
    key = ScalarToken("k", 0, 3, '"k"')
    val = ScalarToken("v", 5, 8, '"v"')

    token = DictToken(
        value={key: val}, start_index=0, end_index=8, content='{"k": "v"}'
    )

    assert token._value == {key: val}
    assert token._child_keys["k"] is key
    assert token._child_tokens["k"] is val


def test_dict_token_get_value_resolves_child_tokens():
    """Lines 89-91: _get_value resolves every child token to its raw value."""
    key_a = ScalarToken("a", 0, 3, '"a"')
    key_b = ScalarToken("b", 10, 13, '"b"')
    val_one = ScalarToken(1, 5, 6, "1")
    val_two = ScalarToken(2, 15, 16, "2")
    token = DictToken({key_a: val_one, key_b: val_two}, 0, 16, '{"a": 1, "b": 2}')

    assert token._get_value() == {"a": 1, "b": 2}


def test_dict_token_get_value_with_nested_dict_token():
    """Lines 89-91 with a DictToken as a value (recursive resolution)."""
    inner_key = ScalarToken("x", 0, 3, '"x"')
    inner_val = ScalarToken(True, 5, 9, "true")
    inner = DictToken({inner_key: inner_val}, 0, 9, '{"x": true}')

    outer_key = ScalarToken("nested", 0, 8, '"nested"')
    outer = DictToken({outer_key: inner}, 0, 9, '{"nested": {"x": true}}')

    assert outer._get_value() == {"nested": {"x": True}}


def test_dict_token_get_child_token_and_key_token():
    """Lines 95 and 98: lookups return the exact stored tokens."""
    key_a = ScalarToken("a", 0, 3, '"a"')
    key_b = ScalarToken("b", 10, 13, '"b"')
    val_one = ScalarToken(1, 5, 6, "1")
    val_two = ScalarToken(2, 15, 16, "2")
    token = DictToken({key_a: val_one, key_b: val_two}, 0, 16, '{"a": 1, "b": 2}')

    # Line 95: _get_child_token returns the value token for a given key.
    assert token._get_child_token("a") is val_one
    assert token._get_child_token("b") is val_two

    # Line 98: _get_key_token returns the key token for a given key.
    assert token._get_key_token("a") is key_a
    assert token._get_key_token("b") is key_b

    # Missing keys propagate KeyError from the dict subscript.
    with pytest.raises(KeyError):
        token._get_child_token("missing")
    with pytest.raises(KeyError):
        token._get_key_token("missing")
