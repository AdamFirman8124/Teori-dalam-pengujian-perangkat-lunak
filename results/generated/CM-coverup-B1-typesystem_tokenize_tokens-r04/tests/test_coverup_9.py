# file: project/typesystem/tokenize/tokens.py:24-26
# asked: {"lines": [26], "branches": []}
# gained: {"lines": [26], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_string_returns_slice():
    token = Token("value", 2, 5, content="abcdefgh")
    assert token.string == "cdef"


def test_token_string_single_character():
    token = Token("value", 3, 3, content="abcdefgh")
    assert token.string == "d"


def test_token_string_default_empty_content():
    token = Token("value", 0, 0)
    assert token.string == ""


def test_token_string_end_index_past_content_end():
    token = Token("value", 4, 100, content="abcdefgh")
    assert token.string == "efgh"


def test_token_string_start_index_past_content_end():
    token = Token("value", 50, 60, content="abcdefgh")
    assert token.string == ""
