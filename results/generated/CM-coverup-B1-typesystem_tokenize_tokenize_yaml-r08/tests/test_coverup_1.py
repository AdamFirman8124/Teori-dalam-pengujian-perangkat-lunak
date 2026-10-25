# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

import pytest

from typesystem.base import Position
from typesystem.tokenize.tokenize_yaml import _get_position


def test_get_position_single_line_start():
    content = "abc"
    position = _get_position(content, 0)

    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_single_line_middle():
    content = "abc"
    position = _get_position(content, 2)

    assert position.line_no == 1
    assert position.column_no == 3
    assert position.char_index == 2


def test_get_position_single_line_end():
    content = "abc"
    position = _get_position(content, len(content))

    assert position.line_no == 1
    assert position.column_no == 4
    assert position.char_index == 3


def test_get_position_multiline_second_line():
    content = "a\nb"
    position = _get_position(content, 2)

    assert position.line_no == 2
    assert position.column_no == 1
    assert position.char_index == 2


def test_get_position_multiline_third_line():
    content = "line one\nline two\nline three"
    index = content.index("three")
    position = _get_position(content, index)

    assert position.line_no == 3
    assert position.column_no == 6
    assert position.char_index == index


def test_get_position_on_newline_character():
    content = "ab\ncd"
    position = _get_position(content, 2)

    # The newline itself belongs to the first line, at column 3.
    assert position.line_no == 1
    assert position.column_no == 3
    assert position.char_index == 2


def test_get_position_empty_content():
    position = _get_position("", 0)

    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


@pytest.mark.parametrize(
    "content,index,expected",
    [
        ("abc", 0, Position(line_no=1, column_no=1, char_index=0)),
        ("abc", 3, Position(line_no=1, column_no=4, char_index=3)),
        ("a\nb", 2, Position(line_no=2, column_no=1, char_index=2)),
        ("a\nb\nc", 4, Position(line_no=3, column_no=1, char_index=4)),
        ("\n", 1, Position(line_no=2, column_no=1, char_index=1)),
    ],
)
def test_get_position_matches_expected_position(content, index, expected):
    position = _get_position(content, index)

    assert position == expected
    assert position.line_no == expected.line_no
    assert position.column_no == expected.column_no
    assert position.char_index == expected.char_index


def test_get_position_returns_new_instance_each_call():
    content = "a\nb"
    first = _get_position(content, 2)
    second = _get_position(content, 2)

    assert first is not second
    assert first == second
    assert first.line_no == second.line_no == 2
    assert first.column_no == second.column_no == 1
    assert first.char_index == second.char_index == 2
