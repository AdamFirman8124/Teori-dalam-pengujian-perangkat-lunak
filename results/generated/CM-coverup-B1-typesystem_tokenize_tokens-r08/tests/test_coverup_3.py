# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_get_position_empty_content():
    token = Token(None, 0, 0, content="")
    pos = token._get_position(0)
    assert isinstance(pos, Position)
    assert pos == Position(1, 1, 0)
    assert (pos.line_no, pos.column_no, pos.char_index) == (1, 1, 0)


def test_get_position_single_line():
    token = Token(None, 0, 2, content="hello")
    pos = token._get_position(1)
    assert pos == Position(1, 2, 1)
    assert (pos.line_no, pos.column_no, pos.char_index) == (1, 2, 1)


def test_get_position_multi_line():
    token = Token(None, 0, 5, content="ab\ncd")
    pos = token._get_position(4)
    assert pos == Position(2, 2, 4)
    assert (pos.line_no, pos.column_no, pos.char_index) == (2, 2, 4)


def test_get_position_empty_last_line():
    token = Token(None, 0, 1, content="\n")
    pos = token._get_position(0)
    assert pos == Position(1, 1, 0)
    assert (pos.line_no, pos.column_no, pos.char_index) == (1, 1, 0)
