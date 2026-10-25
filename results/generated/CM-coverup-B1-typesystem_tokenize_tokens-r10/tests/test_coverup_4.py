# file: project/typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [10, 11, 12, 13], "branches": []}
# gained: {"lines": [10, 11, 12, 13], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_init_with_explicit_content():
    token = Token(value="hello", start_index=0, end_index=5, content="hello world")
    assert token._value == "hello"
    assert token._start_index == 0
    assert token._end_index == 5
    assert token._content == "hello world"


def test_token_init_with_default_content():
    token = Token(value=123, start_index=2, end_index=5)
    assert token._value == 123
    assert token._start_index == 2
    assert token._end_index == 5
    assert token._content == ""
