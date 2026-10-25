# file: project/typesystem/tokenize/tokens.py:24-26
# asked: {"lines": [26], "branches": []}
# gained: {"lines": [26], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_string_property():
    token = Token.__new__(Token)
    token._content = "hello world"
    token._start_index = 0
    token._end_index = 4

    assert token.string == "hello"

    token._start_index = 6
    token._end_index = 10
    assert token.string == "world"

    token._start_index = 5
    token._end_index = 5
    assert token.string == " "
