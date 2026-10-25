# file: project/typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

from typesystem.tokenize.tokens import ScalarToken


def test_scalar_token_value_and_hash():
    value = ("example", 42)
    token = ScalarToken(value, start_index=0, end_index=1)

    assert token.value is value
    assert hash(token) == hash(value)
