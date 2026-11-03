# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_get_position_with_empty_content():
    """Covers the 'no lines' branch: line_no=1, column_no=1."""
    token = Token(value=None, start_index=0, end_index=0, content="")
    position = token._get_position(0)
    assert position == Position(line_no=1, column_no=1, char_index=0)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_single_line():
    """Covers a single line: column_no is the length of the last line."""
    token = Token(value=None, start_index=0, end_index=4, content="hello")
    position = token._get_position(4)
    assert position == Position(line_no=1, column_no=5, char_index=4)
    assert position.line_no == 1
    assert position.column_no == 5
    assert position.char_index == 4


def test_get_position_multiple_lines():
    """Covers the multi-line branch: line_no counts lines, column_no is
    the length of the last line."""
    token = Token(value=None, start_index=0, end_index=6, content="abc\ndef")
    position = token._get_position(6)
    assert position == Position(line_no=2, column_no=3, char_index=6)
    assert position.line_no == 2
    assert position.column_no == 3
    assert position.char_index == 6


def test_get_position_empty_last_line():
    """Covers the max(len(lines[-1]), 1) fallback when the last line is
    empty (content ends with a blank line)."""
    token = Token(value=None, start_index=0, end_index=2, content="a\n\n")
    position = token._get_position(2)
    assert position == Position(line_no=2, column_no=1, char_index=2)
    assert position.line_no == 2
    assert position.column_no == 1
    assert position.char_index == 2


def test_get_position_index_beyond_content():
    """Slicing beyond the content length is safe and clamps to the content."""
    token = Token(value=None, start_index=0, end_index=3, content="abc")
    position = token._get_position(10)
    assert position == Position(line_no=1, column_no=3, char_index=10)
    assert position.line_no == 1
    assert position.column_no == 3
    assert position.char_index == 10
