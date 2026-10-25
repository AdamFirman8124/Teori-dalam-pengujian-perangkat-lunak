# file: project/typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_start_position_single_line():
    token = Token(value="abc", start_index=2, end_index=4, content="abcdef")
    position = token.start
    assert position.line_no == 1
    assert position.column_no == 3
    assert position.char_index == 2


def test_token_start_position_multiline():
    token = Token(value="abc", start_index=5, end_index=7, content="ab\ncdef")
    position = token.start
    assert position.line_no == 2
    assert position.column_no == 3
    assert position.char_index == 5


def test_token_start_position_index_zero():
    token = Token(value="abc", start_index=0, end_index=1, content="abc")
    position = token.start
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0
