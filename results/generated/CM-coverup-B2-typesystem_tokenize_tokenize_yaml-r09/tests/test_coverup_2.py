# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokenize_yaml import _get_position


def test_get_position_for_single_and_multiline_content():
    content = "first\nsecond\nthird"

    assert _get_position(content, 0) == Position(
        line_no=1, column_no=1, char_index=0
    )
    assert _get_position(content, 6) == Position(
        line_no=2, column_no=1, char_index=6
    )
    assert _get_position(content, 15) == Position(
        line_no=3, column_no=3, char_index=15
    )
    assert _get_position(content, len(content)) == Position(
        line_no=3, column_no=6, char_index=len(content)
    )
