# file: project/typesystem/tokenize/tokens.py:63-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_repr_uses_class_name_and_string():
    token = Token("value", 0, 2, "abc")
    assert token.string == "abc"
    assert repr(token) == "Token('abc')"


def test_token_repr_with_subclass_and_empty_content():
    class MyToken(Token):
        pass

    token = MyToken(None, 0, 0, "")
    assert token.string == ""
    assert repr(token) == "MyToken('')"


def test_token_repr_with_quotes_in_string():
    token = Token(1, 1, 3, "x'ab")
    assert token.string == "'ab"
    assert repr(token) == "Token(\"'ab\")"
