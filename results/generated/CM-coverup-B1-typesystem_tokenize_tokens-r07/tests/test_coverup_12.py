# file: project/typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_end_returns_position_for_end_index():
    token = Token(value=None, start_index=0, end_index=3, content="ab\ncd")

    position = token.end

    assert position.line_no == 2
    assert position.column_no == 1
    assert position.char_index == 3
