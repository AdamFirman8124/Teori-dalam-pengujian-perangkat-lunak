# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

import pytest

from typesystem.base import Position
from typesystem.tokenize.tokenize_yaml import _get_position


@pytest.mark.parametrize(
    ("content", "index", "expected"),
    [
        ("hello", 0, (1, 1, 0)),
        ("first\nsecond\nthird", 15, (3, 3, 15)),
    ],
)
def test_get_position(content, index, expected):
    position = _get_position(content, index)

    assert isinstance(position, Position)
    assert (position.line_no, position.column_no, position.char_index) == expected
