# file: project/typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_token_end_property_multiline_content():
    """Covers line 38: `end` delegates to `_get_position(self._end_index)`.

    With content "ab\ncd" and end_index=4, the sliced content is "ab\ncd",
    which splits into 2 lines, so the end position is line 2, column 2.
    """
    token = Token(value="x", start_index=0, end_index=4, content="ab\ncd")
    position = token.end
    assert isinstance(position, Position)
    assert position.line_no == 2
    assert position.column_no == 2
    assert position.char_index == 4
    # char_index equals the end index (not the start index), proving that
    # `end` used `self._end_index`.
    assert position == Position(line_no=2, column_no=2, char_index=4)


def test_token_end_property_empty_content():
    """Covers the `not lines` branch of `_get_position` via the `end` property."""
    token = Token(value="x", start_index=0, end_index=0, content="")
    position = token.end
    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_token_end_property_index_beyond_content():
    """`end` must still work when end_index exceeds the content length."""
    token = Token(value="x", start_index=0, end_index=10, content="abc")
    position = token.end
    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 3
    assert position.char_index == 10


def test_token_end_property_default_content():
    """`end` works with the default (empty) content argument."""
    token = Token(value="x", start_index=0, end_index=2)
    position = token.end
    assert isinstance(position, Position)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 2
