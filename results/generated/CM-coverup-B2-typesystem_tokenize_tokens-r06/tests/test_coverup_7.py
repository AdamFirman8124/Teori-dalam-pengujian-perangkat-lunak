# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_hash_and_value() -> None:
    value = "scalar value"
    token = ScalarToken(value, 0, len(value), value)

    assert hash(token) == hash(value)
    assert token.value == value
