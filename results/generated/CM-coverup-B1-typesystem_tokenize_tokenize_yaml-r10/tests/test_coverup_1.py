# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

import pytest

from typesystem.base import Position
from typesystem.tokenize.tokenize_yaml import _get_position


@pytest.mark.parametrize(
    ("content", "index", "expected"),
    [
        ("", 0, (1, 1, 0)),
        ("first line", 5, (1, 6, 5)),
        ("first\nsecond", 7, (2, 2, 7)),
        ("first\nsecond\nthird", 14, (3, 2, 14)),
    ],
)
def test_get_position_returns_expected_position(content, index, expected):
    position = _get_position(content, index)

    assert isinstance(position, Position)
    assert (position.line_no, position.column_no, position.char_index) == expected


def test_get_position_at_newline_character():
    content = "first\nsecond"
    index = content.index("\n")

    position = _get_position(content, index)

    assert position.line_no == 1
    assert position.column_no == 6
    assert position.char_index == index
