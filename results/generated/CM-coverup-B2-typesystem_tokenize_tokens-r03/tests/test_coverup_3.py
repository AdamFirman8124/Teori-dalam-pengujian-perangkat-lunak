# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

from typesystem.tokenize.tokens import Token


def test_get_position_for_empty_content() -> None:
    token = Token(value=None, start_index=0, end_index=0, content="")

    position = token._get_position(0)

    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_for_multiline_content() -> None:
    token = Token(value=None, start_index=0, end_index=4, content="ab\ncd")

    position = token._get_position(4)

    assert position.line_no == 2
    assert position.column_no == 2
    assert position.char_index == 4


def test_get_position_at_newline_uses_first_column() -> None:
    token = Token(value=None, start_index=0, end_index=1, content="\n")

    position = token._get_position(0)

    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0
