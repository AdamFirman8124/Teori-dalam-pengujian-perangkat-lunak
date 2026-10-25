# file: project/typesystem/tokenize/tokens.py:63-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_repr_includes_class_name_and_string() -> None:
    token = Token(value=None, start_index=0, end_index=2, content="abc")

    assert repr(token) == "Token('abc')"
