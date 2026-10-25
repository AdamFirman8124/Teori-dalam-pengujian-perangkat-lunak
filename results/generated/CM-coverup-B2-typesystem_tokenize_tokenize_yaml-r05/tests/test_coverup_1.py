# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

import pytest

from typesystem.base import Position
from typesystem.tokenize.tokenize_yaml import _get_position


def test_get_position_at_start_of_content():
    position = _get_position("first line", 0)

    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_after_newline():
    content = "first\nsecond line"
    index = content.index("second")

    position = _get_position(content, index)

    assert isinstance(position, Position)
    assert position.line_no == 2
    assert position.column_no == 1
    assert position.char_index == index


@pytest.mark.parametrize(
    ("content", "index", "expected_line", "expected_column"),
    [
        ("one\ntwo\nthree", 4, 2, 1),
        ("one\ntwo\nthree", 6, 2, 3),
        ("one\ntwo\nthree", 8, 3, 1),
    ],
)
def test_get_position_tracks_line_and_column(
    content, index, expected_line, expected_column
):
    position = _get_position(content, index)

    assert position.line_no == expected_line
    assert position.column_no == expected_column
    assert position.char_index == index
