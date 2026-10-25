# file: project/typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_token_end_returns_end_position():
    token = Token(value="value", start_index=0, end_index=6, content="abc\ndef")

    assert token.end == Position(line_no=2, column_no=3, char_index=6)
