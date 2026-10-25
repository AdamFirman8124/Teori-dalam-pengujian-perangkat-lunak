# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

from typesystem.tokenize.tokens import Token


def test_get_position_for_empty_content():
    token = Token(None, 0, 0, content="")

    position = token._get_position(0)

    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_on_first_line():
    token = Token(None, 0, 2, content="abc")

    position = token._get_position(1)

    assert position.line_no == 1
    assert position.column_no == 2
    assert position.char_index == 1


def test_get_position_on_nonempty_later_line():
    token = Token(None, 0, 3, content="a\nbc")

    position = token._get_position(3)

    assert position.line_no == 2
    assert position.column_no == 2
    assert position.char_index == 3


def test_get_position_on_empty_later_line():
    token = Token(None, 0, 2, content="a\n\n")

    position = token._get_position(2)

    assert position.line_no == 2
    assert position.column_no == 1
    assert position.char_index == 2
