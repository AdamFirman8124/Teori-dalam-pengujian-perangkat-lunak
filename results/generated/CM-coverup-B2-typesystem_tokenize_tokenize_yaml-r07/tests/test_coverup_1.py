# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

import pytest

from typesystem.base import Position
from typesystem.tokenize.tokenize_yaml import _get_position


@pytest.mark.parametrize(
    "content,index,expected_line_no,expected_column_no",
    [
        ("", 0, 1, 1),
        ("hello", 0, 1, 1),
        ("hello", 5, 1, 6),
        ("hello", 2, 1, 3),
        ("ab\ncd", 2, 1, 3),
        ("ab\ncd", 3, 2, 1),
        ("a\nb", 2, 2, 1),
        ("ab\ncd\nef", 6, 3, 1),
        ("ab\ncd\nef", 7, 3, 2),
        ("ab\ncd\nef", 8, 3, 3),
        ("\n", 0, 1, 1),
        ("\n", 1, 2, 1),
        ("line1\nline2\n", 12, 3, 1),
    ],
)
def test_get_position(content, index, expected_line_no, expected_column_no):
    result = _get_position(content, index)

    assert isinstance(result, Position)
    assert result.line_no == expected_line_no
    assert result.column_no == expected_column_no
    assert result.char_index == index
    assert result == Position(
        line_no=expected_line_no,
        column_no=expected_column_no,
        char_index=index,
    )


def test_get_position_start_of_content():
    result = _get_position("hello\nworld", 0)

    assert result.line_no == 1
    assert result.column_no == 1
    assert result.char_index == 0


def test_get_position_end_of_content():
    content = "hello\nworld"
    result = _get_position(content, len(content))

    assert result.line_no == 2
    assert result.column_no == 6
    assert result.char_index == len(content)
