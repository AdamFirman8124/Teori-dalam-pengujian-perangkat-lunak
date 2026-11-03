# file: project/typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

import pytest

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


@pytest.mark.parametrize(
    "content, index, expected_line_no, expected_column_no",
    [
        # Empty slice -> splitlines() yields no lines: both max() calls
        # fall back to 1 (covers the "not lines" branch).
        ("", 0, 1, 1),
        # Single line, slice covers the whole content.
        ("abc", 2, 1, 3),
        # Slice stops in the middle of the first line.
        ("ab\ncd", 1, 1, 2),
        # Slice spans several lines: position is taken from the last line.
        ("ab\ncd", 4, 2, 2),
        # Content ending with a newline: the last split line is empty, so
        # the inner max(len(lines[-1]), 1) falls back to 1.
        ("ab\n\n", 3, 2, 1),
    ],
)
def test_get_position(content, index, expected_line_no, expected_column_no):
    token = Token(value="x", start_index=0, end_index=1, content=content)
    position = token._get_position(index)

    assert isinstance(position, Position)
    assert position.line_no == expected_line_no
    assert position.column_no == expected_column_no
    assert position.char_index == index


def test_get_position_slice_is_inclusive_of_index():
    # content[: index + 1] must include the character at `index`.
    token = Token(value="x", start_index=0, end_index=1, content="abcdef")
    position = token._get_position(3)

    assert position.line_no == 1
    assert position.column_no == 4  # "abcd" -> 4 characters on the line
    assert position.char_index == 3


def test_start_and_end_properties_delegate_to_get_position():
    token = Token(value="x", start_index=0, end_index=5, content="ab\ncd")

    start = token.start
    assert isinstance(start, Position)
    assert start.line_no == 1
    assert start.column_no == 1
    assert start.char_index == 0

    end = token.end
    assert isinstance(end, Position)
    assert end.line_no == 2
    assert end.column_no == 2
    assert end.char_index == 5
