# file: project/typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [10, 11, 12, 13], "branches": []}
# gained: {"lines": [10, 11, 12, 13], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_initializes_all_attributes():
    value = object()

    token = Token(value, start_index=3, end_index=7, content="test")

    assert token._value is value
    assert token._start_index == 3
    assert token._end_index == 7
    assert token._content == "test"
