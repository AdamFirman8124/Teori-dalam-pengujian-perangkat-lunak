# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_hash_uses_scalar_value():
    token = ScalarToken("value", 0, 5, "value")

    assert hash(token) == hash("value")


def test_scalar_token_get_value_returns_scalar_value():
    token = ScalarToken("value", 0, 5, "value")

    assert token._get_value() == "value"
    assert token.value == "value"
