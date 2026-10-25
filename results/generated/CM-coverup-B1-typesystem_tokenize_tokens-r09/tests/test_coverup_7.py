# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_hash_matches_value_hash():
    token = ScalarToken(value="hello", start_index=0, end_index=5)

    assert hash(token) == hash("hello")
    assert hash(token) == hash(token._value)


def test_scalar_token_hash_is_consistent_for_equal_values():
    token1 = ScalarToken(value="hello", start_index=0, end_index=5)
    token2 = ScalarToken(value="hello", start_index=0, end_index=5)

    assert hash(token1) == hash(token2)
    assert len({token1, token2}) >= 1
    assert token1 in {token1, token2}


def test_scalar_token_get_value_returns_value():
    token = ScalarToken(value="hello", start_index=0, end_index=5)

    assert token._get_value() == "hello"
    assert token._get_value() == token._value


def test_scalar_token_get_value_and_hash_for_various_values():
    for value in ("", "a", "123", "true", "null"):
        token = ScalarToken(value=value, start_index=0, end_index=len(value))

        assert token._get_value() == value
        assert hash(token) == hash(value)
