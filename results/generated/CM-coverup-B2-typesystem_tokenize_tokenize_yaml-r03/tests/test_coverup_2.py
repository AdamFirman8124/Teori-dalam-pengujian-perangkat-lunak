# file: project/typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [18, 19, 20, 21], "branches": []}
# gained: {"lines": [18, 19, 20, 21], "branches": []}

from typesystem.tokenize.tokenize_yaml import _get_position


def test_get_position_on_first_line():
    position = _get_position("abc", 1)

    assert position.line_no == 1
    assert position.column_no == 2
    assert position.char_index == 1


def test_get_position_on_subsequent_line():
    content = "first\nsecond\nthird"
    position = _get_position(content, 8)

    assert position.line_no == 2
    assert position.column_no == 3
    assert position.char_index == 8
