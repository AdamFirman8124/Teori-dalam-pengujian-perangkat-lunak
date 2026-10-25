# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

from typesystem.tokenize.tokenize_yaml import _get_position


def test_get_position_at_start_of_content():
    position = _get_position("first line", 0)

    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_get_position_after_multiple_newlines():
    content = "first\nsecond\nthird"
    index = content.index("c")

    position = _get_position(content, index)

    assert position.line_no == 2
    assert position.column_no == 3
    assert position.char_index == index
