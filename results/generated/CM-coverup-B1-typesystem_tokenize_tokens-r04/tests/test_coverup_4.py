# file: project/typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [10, 11, 12, 13], "branches": []}
# gained: {"lines": [10, 11, 12, 13], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_init_sets_all_attributes():
    token = Token(value="abc", start_index=0, end_index=3, content="abc")

    assert token._value == "abc"
    assert token._start_index == 0
    assert token._end_index == 3
    assert token._content == "abc"


def test_token_init_default_content_is_empty_string():
    token = Token(value=123, start_index=5, end_index=8)

    assert token._value == 123
    assert token._start_index == 5
    assert token._end_index == 8
    assert token._content == ""
