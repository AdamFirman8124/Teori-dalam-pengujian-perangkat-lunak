# file: project/typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_token_start_single_line():
    token = Token(value="abc", start_index=0, end_index=3, content="abc")
    position = token.start

    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_token_start_mid_line_column():
    token = Token(value="world", start_index=6, end_index=11, content="hello world")
    position = token.start

    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 7
    assert position.char_index == 6


def test_token_start_multiline():
    content = "hello\nworld"
    token = Token(value="world", start_index=7, end_index=11, content=content)
    position = token.start

    assert isinstance(position, Position)
    assert position.line_no == 2
    assert position.column_no == 2
    assert position.char_index == 7


def test_token_start_empty_content():
    token = Token(value=None, start_index=0, end_index=0, content="")
    position = token.start

    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_token_start_uses_start_index_not_end_index():
    content = "hello\nworld"
    token = Token(value="hello", start_index=0, end_index=11, content=content)
    position = token.start

    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0
