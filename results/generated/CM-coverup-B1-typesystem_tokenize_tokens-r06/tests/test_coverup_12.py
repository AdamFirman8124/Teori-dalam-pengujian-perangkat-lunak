# file: project/typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_token_end_single_line():
    token = Token(value="hello", start_index=0, end_index=4, content="hello")
    result = token.end
    assert isinstance(result, Position)
    assert result == Position(line_no=1, column_no=5, char_index=4)
    assert result.line_no == 1
    assert result.column_no == 5
    assert result.char_index == 4


def test_token_end_uses_end_index_not_start_index():
    token = Token(value="hello", start_index=0, end_index=4, content="hello world")
    end = token.end
    start = token.start
    assert end.char_index == 4
    assert start.char_index == 0
    assert end != start
    assert end == Position(line_no=1, column_no=5, char_index=4)


def test_token_end_multiline():
    content = "hello\nworld"
    token = Token(value="world", start_index=6, end_index=10, content=content)
    result = token.end
    assert result == Position(line_no=2, column_no=5, char_index=10)


def test_token_end_empty_content():
    token = Token(value="", start_index=0, end_index=0, content="")
    result = token.end
    assert result == Position(line_no=1, column_no=1, char_index=0)
