# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

import pytest

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_hash_returns_hash_of_value():
    token = ScalarToken("hello", 0, 5)
    assert hash(token) == hash("hello")


def test_scalar_token_hash_matches_value_for_various_types():
    for value in (42, 3.5, "abc", (1, 2), True, None):
        token = ScalarToken(value, 0, 1)
        assert hash(token) == hash(value)


def test_scalar_token_hash_is_stable_across_calls():
    token = ScalarToken("stable", 2, 8)
    assert hash(token) == hash(token)


def test_scalar_token_hash_equal_for_equal_values():
    first = ScalarToken("same", 0, 4)
    second = ScalarToken("same", 10, 14)
    assert hash(first) == hash(second)


def test_scalar_token_usable_as_dict_key_and_in_set():
    token = ScalarToken("key", 0, 3)
    mapping = {token: "stored"}
    assert mapping[token] == "stored"
    assert token in {token}


def test_scalar_token_get_value_returns_original_value():
    value = {"nested": [1, 2, 3]}
    token = ScalarToken(value, 0, 10)
    assert token._get_value() is value


def test_scalar_token_get_value_returns_scalar_values():
    for value in (0, "", None, False, 1.25):
        token = ScalarToken(value, 0, 1)
        assert token._get_value() == value


def test_scalar_token_get_value_does_not_mutate_token_state():
    token = ScalarToken("value", 3, 8, content="value")
    assert token._get_value() == "value"
    assert token._get_value() == "value"
    assert token._start_index == 3
    assert token._end_index == 8
    assert token._content == "value"
