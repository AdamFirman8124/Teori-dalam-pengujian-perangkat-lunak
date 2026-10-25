# file: project/typesystem/tokenize/tokens.py:63-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_repr_uses_class_name_and_string():
    token = Token(value=None, start_index=0, end_index=4, content="hello world")

    assert token.string == "hello"
    assert repr(token) == "Token('hello')"


def test_token_repr_uses_subclass_name():
    class SubToken(Token):
        pass

    token = SubToken(value=1, start_index=2, end_index=3, content="abcdef")

    assert token.string == "cd"
    assert repr(token) == "SubToken('cd')"


def test_token_repr_with_empty_string():
    token = Token(value=None, start_index=0, end_index=-1, content="")

    assert token.string == ""
    assert repr(token) == "Token('')"


def test_token_repr_quotes_are_escaped():
    token = Token(value=None, start_index=0, end_index=2, content="a'b")

    assert token.string == "a'b"
    assert repr(token) == 'Token("a\'b")'
