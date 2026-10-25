# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

import pytest

from typesystem.tokenize.tokenize_yaml import _get_position


@pytest.mark.parametrize(
    ("content", "index", "line_no", "column_no"),
    [
        ("hello", 0, 1, 1),
        ("hello", 3, 1, 4),
        ("first\nsecond", 6, 2, 1),
        ("first\nsecond\nthird", 14, 3, 2),
    ],
)
def test_get_position_returns_expected_position(
    content, index, line_no, column_no
):
    position = _get_position(content, index)

    assert position.line_no == line_no
    assert position.column_no == column_no
    assert position.char_index == index


def test_get_position_at_newline_uses_preceding_line():
    content = "first\nsecond"

    position = _get_position(content, 5)

    assert position.line_no == 1
    assert position.column_no == 6
    assert position.char_index == 5
