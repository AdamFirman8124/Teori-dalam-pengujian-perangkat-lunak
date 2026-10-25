# file: project/typesystem/tokenize/tokens.py:63-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_repr_returns_class_name_and_string():
    token = Token(value="hello", start_index=0, end_index=4, content="hello")
    assert token.string == "hello"
    result = repr(token)
    assert result == "Token('hello')"
    assert result == "%s(%s)" % (Token.__name__, repr("hello"))


def test_token_repr_with_subclass_uses_subclass_name():
    class MyToken(Token):
        pass

    token = MyToken(value=123, start_index=1, end_index=3, content="x123y")
    assert token.string == "123"
    result = repr(token)
    assert result == "MyToken('123')"
