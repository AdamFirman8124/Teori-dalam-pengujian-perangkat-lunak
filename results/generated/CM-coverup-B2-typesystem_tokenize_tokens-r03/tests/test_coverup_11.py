# file: project/typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_start_property_returns_position():
    token = Token(value="x", start_index=4, end_index=6, content="hello\nworld")

    position = token.start

    # content[:start_index + 1] == "hello" -> single line, column = len("hello")
    assert position.line_no == 1
    assert position.column_no == 5
    assert position.char_index == 4


def test_token_start_property_multiline_position():
    token = Token(value="x", start_index=8, end_index=9, content="hello\nworld")

    position = token.start

    # content[:9] == "hello\nwor" -> second line, column = len("wor")
    assert position.line_no == 2
    assert position.column_no == 3
    assert position.char_index == 8
