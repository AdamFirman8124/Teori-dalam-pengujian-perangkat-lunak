# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_hash_uses_value():
    token = ScalarToken("example", 0, 7)

    assert hash(token) == hash("example")


def test_scalar_token_value_returns_stored_value():
    value = object()
    token = ScalarToken(value, 0, 0)

    assert token.value is value
