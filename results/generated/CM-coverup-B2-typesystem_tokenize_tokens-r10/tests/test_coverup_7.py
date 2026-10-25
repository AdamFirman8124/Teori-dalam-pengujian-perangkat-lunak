# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_value_and_hash():
    value = "example"
    token = ScalarToken(value, 0, len(value), value)

    assert token.value == value
    assert hash(token) == hash(value)
