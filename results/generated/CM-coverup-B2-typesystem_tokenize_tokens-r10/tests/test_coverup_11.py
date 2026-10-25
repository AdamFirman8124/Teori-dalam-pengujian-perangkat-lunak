# file: project/typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_start_property_returns_position():
    token = Token(value="x", start_index=4, end_index=6, content="hello\nworld")

    position = token.start

    assert position.line_no == 1
    assert position.column_no == 5
    assert position.char_index == 4


def test_token_start_property_after_newline():
    token = Token(value="x", start_index=7, end_index=9, content="hello\nworld")

    position = token.start

    assert position.line_no == 2
    assert position.column_no == 2
    assert position.char_index == 7


def test_token_start_property_with_empty_content():
    token = Token(value="x", start_index=0, end_index=0, content="")

    position = token.start

    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0
