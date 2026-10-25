# file: project/typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token
from typesystem.base import Position


def test_token_start_property_returns_position():
    token = Token(value="x", start_index=4, end_index=6, content="ab\ncde")
    position = token.start
    assert isinstance(position, Position)
    # content[:5] == "ab\ncd" -> 2 lines, last line "cd" has length 2
    assert position.line_no == 2
    assert position.column_no == 2
    assert position.char_index == 4


def test_token_start_property_single_line_content():
    token = Token(value="x", start_index=0, end_index=1, content="abc")
    position = token.start
    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0
