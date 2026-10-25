# file: project/typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_start_property_returns_position():
    token = Token(value="x", start_index=4, end_index=6, content="hello\nworld")

    position = token.start

    assert position.line_no == 1
    assert position.column_no == 5
    assert position.char_index == 4
