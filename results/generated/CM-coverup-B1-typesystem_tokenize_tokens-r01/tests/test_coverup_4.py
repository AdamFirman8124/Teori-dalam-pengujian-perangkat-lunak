# file: project/typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [10, 11, 12, 13], "branches": []}
# gained: {"lines": [10, 11, 12, 13], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_initialization_sets_all_attributes():
    value = {"name": "example"}
    token = Token(value=value, start_index=2, end_index=9, content="example")

    assert token._value is value
    assert token._start_index == 2
    assert token._end_index == 9
    assert token._content == "example"


def test_token_initialization_uses_default_content():
    token = Token(value=None, start_index=0, end_index=0)

    assert token._value is None
    assert token._start_index == 0
    assert token._end_index == 0
    assert token._content == ""
