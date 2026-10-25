# file: project/typesystem/tokenize/tokens.py:24-26
# asked: {"lines": [26], "branches": []}
# gained: {"lines": [26], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_string_returns_inclusive_content_slice():
    token = Token(value=None, start_index=1, end_index=3, content="abcde")

    assert token.string == "bcd"
