# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

from typesystem.tokenize.tokens import Token


def test_get_position_with_empty_content():
    token = Token(None, 0, 0, content="")

    position = token._get_position(0)

    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_with_nonempty_line():
    token = Token(None, 0, 2, content="abc")

    position = token._get_position(2)

    assert position.line_no == 1
    assert position.column_no == 3
    assert position.char_index == 2


def test_get_position_with_empty_line():
    token = Token(None, 0, 0, content="\n")

    position = token._get_position(0)

    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_after_multiple_lines():
    token = Token(None, 0, 5, content="ab\nxyz")

    position = token._get_position(5)

    assert position.line_no == 2
    assert position.column_no == 3
    assert position.char_index == 5
