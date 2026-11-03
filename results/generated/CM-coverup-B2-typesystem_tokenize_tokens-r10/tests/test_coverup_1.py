# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

import pytest

from typesystem.tokenize.tokens import DictToken, ScalarToken


def test_dict_token_init_builds_child_maps():
    """Lines 84-86: __init__ stores child key/value token maps."""
    key_a = ScalarToken("a", 0, 3, '"a"')
    key_b = ScalarToken("b", 6, 9, '"b"')
    value_one = ScalarToken(1, 4, 5, "1")
    value_two = ScalarToken(2, 10, 11, "2")

    raw = {key_a: value_one, key_b: value_two}
    token = DictToken(raw, 0, 12, '{"a": 1, "b": 2}')

    # Line 84: super().__init__ was called with the positional args.
    assert token._value is raw
    assert token._start_index == 0
    assert token._end_index == 12
    assert token._content == '{"a": 1, "b": 2}'

    # Line 85: _child_keys maps each key token's value to the key token.
    assert token._child_keys == {"a": key_a, "b": key_b}
    # Line 86: _child_tokens maps each key token's value to the value token.
    assert token._child_tokens == {"a": value_one, "b": value_two}


def test_dict_token_init_with_non_string_scalar_keys():
    """Lines 84-86 also work for non-string scalar keys (e.g. ints)."""
    key_int = ScalarToken(7, 0, 1, "7")
    value_str = ScalarToken("x", 3, 6, "'x'")

    token = DictToken({key_int: value_str}, 0, 7)

    assert token._child_keys == {7: key_int}
    assert token._child_tokens == {7: value_str}


def test_dict_token_get_value_returns_plain_nested_dict():
    """Lines 89-91: _get_value recursively unwraps tokens to plain data."""
    inner_key = ScalarToken("inner", 0, 7)
    inner_value = ScalarToken(True, 9, 13)
    inner = DictToken({inner_key: inner_value}, 0, 14)

    outer_key = ScalarToken("outer", 20, 27)
    outer_list_value = ScalarToken([1, 2], 29, 34)
    outer = DictToken(
        {outer_key: outer_list_value, inner_key: inner},
        20,
        40,
    )

    result = outer._get_value()

    assert result == {"outer": [1, 2], "inner": {"inner": True}}
    # The result must be plain data, not token instances.
    assert type(result["outer"]) is list
    assert type(result["inner"]) is dict
    assert type(result["inner"]["inner"]) is bool


def test_dict_token_get_value_empty_dict():
    """Lines 89-91: empty dict yields empty plain dict."""
    token = DictToken({}, 0, 2, "{}")
    assert token._get_value() == {}


def test_dict_token_get_child_token():
    """Line 95: _get_child_token looks up by key value."""
    key = ScalarToken("alpha", 0, 7)
    value = ScalarToken(42, 9, 11)
    token = DictToken({key: value}, 0, 12)

    child = token._get_child_token("alpha")

    assert child is value


def test_dict_token_get_child_token_missing_key_raises():
    """Line 95: unknown key raises KeyError."""
    token = DictToken({}, 0, 2)
    with pytest.raises(KeyError):
        token._get_child_token("missing")


def test_dict_token_get_key_token():
    """Line 98: _get_key_token looks up by key value."""
    key = ScalarToken("beta", 0, 6)
    value = ScalarToken("gamma", 8, 15)
    token = DictToken({key: value}, 0, 16)

    key_token = token._get_key_token("beta")

    assert key_token is key


def test_dict_token_get_key_token_missing_key_raises():
    """Line 98: unknown key raises KeyError."""
    token = DictToken({}, 0, 2)
    with pytest.raises(KeyError):
        token._get_key_token("missing")
