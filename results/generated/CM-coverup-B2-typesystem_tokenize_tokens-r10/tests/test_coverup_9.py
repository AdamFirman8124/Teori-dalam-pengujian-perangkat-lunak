# file: project/typesystem/tokenize/tokens.py:24-26
# asked: {"lines": [26], "branches": []}
# gained: {"lines": [26], "branches": []}

def test_token_string_returns_sliced_content():
    from typesystem.tokenize.tokens import Token
    token = Token("ell", 1, 3, "hello")
    assert token.string == "ell"
    assert token.string == "hello"[1:3 + 1]


def test_token_string_single_character():
    from typesystem.tokenize.tokens import Token
    token = Token("h", 0, 0, "hello")
    assert token.string == "h"


def test_token_string_full_content():
    from typesystem.tokenize.tokens import Token
    token = Token("hello", 0, 4, "hello")
    assert token.string == "hello"
