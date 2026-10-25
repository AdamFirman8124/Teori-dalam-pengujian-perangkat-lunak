# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_get_position_empty_content():
    token = Token(None, 0, 0, content="")
    pos = token._get_position(0)
    assert isinstance(pos, Position)
    assert pos.line_no == 1
    assert pos.column_no == 1
    assert pos.char_index == 0
    assert pos == Position(1, 1, 0)


def test_get_position_empty_slice_via_negative_index():
    token = Token("hello", 0, 5, content="hello")
    pos = token._get_position(-1)
    # content = "hello"[:0] == "" -> lines == []
    assert pos == Position(1, 1, -1)
    assert pos.line_no == 1
    assert pos.column_no == 1


def test_get_position_single_line():
    token = Token("hello", 0, 5, content="hello")
    pos = token._get_position(1)
    # content = "he" -> lines == ["he"]
    assert pos == Position(1, 2, 1)
    pos2 = token._get_position(4)
    assert pos2 == Position(1, 5, 4)


def test_get_position_single_char_column_floor():
    token = Token("hello", 0, 5, content="hello")
    pos = token._get_position(0)
    # content = "h" -> lines == ["h"], max(len("h"), 1) == 1
    assert pos == Position(1, 1, 0)


def test_get_position_multiline():
    token = Token(None, 0, 5, content="ab\ncd")
    pos = token._get_position(4)
    # content = "ab\ncd" -> lines == ["ab", "cd"]
    assert pos == Position(2, 2, 4)
    assert pos.line_no == 2
    assert pos.column_no == 2
    assert pos.char_index == 4


def test_get_position_empty_last_line():
    token = Token(None, 0, 1, content="\n")
    pos = token._get_position(0)
    # content = "\n" -> lines == [""] -> max(len(""), 1) == 1
    assert pos == Position(1, 1, 0)
    assert pos.line_no == 1
    assert pos.column_no == 1


def test_get_position_multiline_empty_last_line():
    token = Token(None, 0, 3, content="a\n\n")
    pos = token._get_position(2)
    # content = "a\n\n" -> lines == ["a", ""] -> line 2, empty last line floors to 1
    assert pos.line_no == 2
    assert pos.column_no == 1
    assert pos == Position(2, 1, 2)
