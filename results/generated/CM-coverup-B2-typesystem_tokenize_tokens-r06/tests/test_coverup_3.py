# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

import pytest

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_get_position_empty_content_index_minus_one():
    token = Token(value="x", start_index=0, end_index=0, content="")
    position = token._get_position(-1)
    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == -1


def test_get_position_default_empty_content():
    token = Token(value="x", start_index=0, end_index=0)
    position = token._get_position(0)
    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_single_line():
    token = Token(value="hel", start_index=0, end_index=3, content="hello")
    position = token._get_position(2)
    assert position.line_no == 1
    assert position.column_no == 3
    assert position.char_index == 2


def test_get_position_single_character_line():
    token = Token(value="h", start_index=0, end_index=1, content="hello")
    position = token._get_position(0)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_multiline_middle_line():
    token = Token(value="cde", start_index=3, end_index=6, content="ab\ncde\nf")
    position = token._get_position(5)
    assert position.line_no == 2
    assert position.column_no == 3
    assert position.char_index == 5


def test_get_position_multiline_last_line():
    token = Token(value="f", start_index=7, end_index=8, content="ab\ncde\nf")
    position = token._get_position(7)
    assert position.line_no == 3
    assert position.column_no == 1
    assert position.char_index == 7


def test_get_position_only_newline_empty_last_line():
    token = Token(value="\n", start_index=0, end_index=1, content="\n")
    position = token._get_position(0)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_trailing_blank_line():
    token = Token(value="\n", start_index=2, end_index=3, content="a\n\n")
    position = token._get_position(2)
    assert position.line_no == 2
    assert position.column_no == 1
    assert position.char_index == 2


def test_get_position_at_newline_character():
    token = Token(value="\n", start_index=2, end_index=3, content="ab\ncde")
    position = token._get_position(2)
    assert position.line_no == 1
    assert position.column_no == 2
    assert position.char_index == 2
