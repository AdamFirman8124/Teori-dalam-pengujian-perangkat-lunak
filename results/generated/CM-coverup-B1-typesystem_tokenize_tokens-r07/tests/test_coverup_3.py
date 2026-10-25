# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_get_position_with_empty_content():
    position = Token(None, 0, 0, "")._get_position(0)

    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_with_empty_line():
    position = Token(None, 0, 0, "\n")._get_position(0)

    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_with_multiple_lines():
    position = Token(None, 0, 4, "a\nxyz")._get_position(4)

    assert isinstance(position, Position)
    assert position.line_no == 2
    assert position.column_no == 3
    assert position.char_index == 4
