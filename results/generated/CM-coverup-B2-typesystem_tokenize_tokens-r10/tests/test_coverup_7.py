# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

import pytest

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_get_value_returns_stored_value():
    """Line 79: ScalarToken._get_value must return the wrapped value."""
    token = ScalarToken("hello", start_index=0, end_index=5)
    assert token._get_value() == "hello"
    # The public .value property delegates to _get_value(), so it must agree.
    assert token.value == "hello"


def test_scalar_token_get_value_with_non_string_value():
    """_get_value works for arbitrary scalar payloads, not just strings."""
    token = ScalarToken(123, start_index=10, end_index=13)
    assert token._get_value() == 123
    assert token.value == 123


def test_scalar_token_hash_matches_underlying_value_hash():
    """Line 76: ScalarToken.__hash__ must delegate to hash(self._value)."""
    token = ScalarToken(42, start_index=3, end_index=5)
    assert hash(token) == hash(42)


def test_scalar_token_hash_consistent_and_usable_in_collections():
    """Hashing must be consistent across equal tokens and usable in sets/dicts."""
    token_a = ScalarToken("abc", start_index=0, end_index=3)
    token_b = ScalarToken("abc", start_index=0, end_index=3)
    token_c = ScalarToken("xyz", start_index=4, end_index=7)

    # Same value/indexes -> same hash every time.
    assert hash(token_a) == hash(token_a)
    assert hash(token_a) == hash(token_b)

    # Usable as dictionary keys / set members thanks to __hash__ + __eq__.
    mapping = {token_a: "first"}
    assert mapping[token_b] == "first"
    assert token_c not in mapping
    assert len({token_a, token_b, token_c}) == 2
