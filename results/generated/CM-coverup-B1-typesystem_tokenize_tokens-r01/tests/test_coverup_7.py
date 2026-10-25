# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_hash_uses_value():
    token = ScalarToken("value", 0, 5)

    assert hash(token) == hash("value")


def test_scalar_token_get_value_returns_value():
    value = object()
    token = ScalarToken(value, 0, 0)

    assert token.value is value
    assert token._get_value() is value
