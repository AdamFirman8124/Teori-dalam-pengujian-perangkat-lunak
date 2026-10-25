# file: project/typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_token_start_returns_position_for_start_index():
    token = Token(value="value", start_index=6, end_index=10, content="abc\ndefghij")

    assert token.start == Position(line_no=2, column_no=3, char_index=6)
