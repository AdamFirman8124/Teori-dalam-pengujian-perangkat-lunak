# file: project/typesystem/tokenize/tokens.py:63-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_repr_includes_class_name_and_string():
    token = Token(value=None, start_index=1, end_index=3, content="abcdef")

    assert token.string == "bcd"
    assert repr(token) == "Token('bcd')"
