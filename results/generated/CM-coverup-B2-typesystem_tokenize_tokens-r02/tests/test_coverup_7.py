# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

import pytest

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_hash():
    token = ScalarToken(value="abc", start_index=0, end_index=3, content="abc")
    other = ScalarToken(value="abc", start_index=0, end_index=3, content="abc")

    # Covers line 76: __hash__ delegates to hash of the underlying value.
    assert hash(token) == hash("abc")

    # Equal tokens (same value and indices) must hash identically.
    assert token == other
    assert hash(token) == hash(other)

    # The token must be usable in hash-based containers.
    mapping = {token: "present"}
    assert mapping[other] == "present"


def test_scalar_token_get_value():
    token = ScalarToken(value=123, start_index=0, end_index=3, content="123")

    # Covers line 79: _get_value returns the wrapped value.
    assert token._get_value() == 123

    # The value is also exposed consistently through the public property.
    assert token.value == 123


def test_scalar_token_hash_and_get_value_with_none():
    token = ScalarToken(value=None, start_index=5, end_index=9, content="null")

    assert token._get_value() is None
    assert hash(token) == hash(None)
