# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_get_position_for_empty_content_slice():
    token = Token(value=None, start_index=0, end_index=0, content="abc")

    position = token._get_position(-1)

    assert position == Position(1, 1, -1)


def test_get_position_for_single_line_content():
    token = Token(value=None, start_index=0, end_index=1, content="ab")

    position = token._get_position(1)

    assert position == Position(1, 2, 1)


def test_get_position_for_multiple_lines():
    token = Token(value=None, start_index=0, end_index=3, content="ab\nc")

    position = token._get_position(3)

    assert position == Position(2, 1, 3)


def test_get_position_when_last_split_line_is_empty():
    token = Token(value=None, start_index=0, end_index=0, content="\n")

    position = token._get_position(0)

    assert position == Position(1, 1, 0)
