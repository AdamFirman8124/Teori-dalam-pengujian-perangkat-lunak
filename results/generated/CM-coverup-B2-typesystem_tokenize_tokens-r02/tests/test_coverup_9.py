# file: project/typesystem/tokenize/tokens.py:24-26
# asked: {"lines": [26], "branches": []}
# gained: {"lines": [26], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_string_returns_full_content_slice():
    # Accessing .string executes line 26:
    #     return self._content[self._start_index : self._end_index + 1]
    token = Token(value={"a": 1}, start_index=0, end_index=4, content="hello")
    assert token.string == "hello"


def test_token_string_returns_partial_slice():
    # Verifies both indices are used correctly (inclusive end via + 1).
    token = Token(value=None, start_index=1, end_index=3, content="hello")
    assert token.string == "ell"


def test_token_string_with_default_empty_content():
    # Covers the default content='' branch of __init__ combined with line 26.
    token = Token(value=None, start_index=0, end_index=0)
    assert token.string == ""
