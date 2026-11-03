# file: project/typesystem/tokenize/tokens.py:63-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_repr_contains_class_name_and_quoted_string():
    """
    Covers Token.__repr__ (line 64): the returned string must be built from
    the class name and repr() of the token's `string` property.
    """
    # content="hello", indices 0..4 => string == "hello"
    token = Token("some_value", 0, 4, content="hello")

    result = repr(token)

    assert result == "Token('hello')"
    assert token.__class__.__name__ in result
    assert repr(token.string) in result


def test_token_repr_uses_actual_subclass_name():
    """
    Ensures __repr__ uses self.__class__.__name__ rather than a hard-coded
    class name, by checking a subclass instance.
    """
    class SpecialToken(Token):
        pass

    token = SpecialToken(123, 1, 3, content="abcdef")

    result = repr(token)

    assert result == "SpecialToken('bcd')"
    assert result.startswith(SpecialToken.__name__ + "(")


def test_token_repr_with_empty_string_content():
    """
    Edge case: empty slice yields an empty string, whose repr is "''".
    """
    token = Token(None, 0, -1, content="anything")

    result = repr(token)

    assert result == "Token('')"
