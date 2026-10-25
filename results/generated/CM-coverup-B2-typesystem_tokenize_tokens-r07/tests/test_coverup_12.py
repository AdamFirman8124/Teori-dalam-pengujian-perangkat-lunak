# file: project/typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_token_end_returns_expected_position():
    content = "abc\ndefg\nh"
    token = Token(value="defg", start_index=4, end_index=8, content=content)

    end = token.end

    assert isinstance(end, Position)
    assert end.char_index == 8
    assert end.line_no == 2
    assert end.column_no == 4
