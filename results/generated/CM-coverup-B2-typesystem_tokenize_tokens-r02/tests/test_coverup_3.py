# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token
from typesystem.base import Position


def _make_token(content: str) -> Token:
    token = object.__new__(Token)
    token._content = content
    return token


def test_get_position_empty_content():
    token = _make_token("")
    pos = token._get_position(0)
    assert isinstance(pos, Position)
    assert pos.line_no == 1
    assert pos.column_no == 1
    assert pos.char_index == 0


def test_get_position_single_line():
    token = _make_token("hello")
    pos = token._get_position(4)
    assert pos.line_no == 1
    assert pos.column_no == 5
    assert pos.char_index == 4


def test_get_position_multiline():
    token = _make_token("ab\ncd\nefgh")
    pos = token._get_position(9)
    assert pos.line_no == 3
    assert pos.column_no == 4
    assert pos.char_index == 9


def test_get_position_index_at_line_start():
    token = _make_token("ab\ncd")
    pos = token._get_position(3)
    assert pos.line_no == 2
    assert pos.column_no == 1
    assert pos.char_index == 3


def test_get_position_index_beyond_content():
    token = _make_token("abc")
    pos = token._get_position(100)
    assert pos.line_no == 1
    assert pos.column_no == 3
    assert pos.char_index == 100
