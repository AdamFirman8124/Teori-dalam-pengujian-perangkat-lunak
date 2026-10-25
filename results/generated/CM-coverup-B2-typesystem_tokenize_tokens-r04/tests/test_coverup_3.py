# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

import pytest

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def make_token(content: str) -> Token:
    """Build a Token without relying on its __init__ signature."""
    token = object.__new__(Token)
    token._content = content
    return token


def test_position_empty_content_uses_defaults():
    token = make_token("")
    pos = token._get_position(-1)

    assert isinstance(pos, Position)
    assert pos.line_no == 1
    assert pos.column_no == 1
    assert pos.char_index == -1


def test_position_empty_content_index_zero():
    token = make_token("")
    pos = token._get_position(0)

    assert (pos.line_no, pos.column_no, pos.char_index) == (1, 1, 0)


def test_position_single_line():
    token = make_token("abc")
    pos = token._get_position(1)

    assert (pos.line_no, pos.column_no, pos.char_index) == (1, 2, 1)


def test_position_multiline():
    token = make_token("abc\ndef")
    pos = token._get_position(5)

    assert (pos.line_no, pos.column_no, pos.char_index) == (2, 2, 5)


def test_position_trailing_newline():
    token = make_token("abc\n")
    pos = token._get_position(3)

    assert (pos.line_no, pos.column_no, pos.char_index) == (1, 3, 3)


def test_position_blank_last_line_clamps_column_to_one():
    token = make_token("a\n\n")
    pos = token._get_position(2)

    assert (pos.line_no, pos.column_no, pos.char_index) == (2, 1, 2)
