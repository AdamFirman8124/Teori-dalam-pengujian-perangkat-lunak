# file: project/typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [10, 11, 12, 13], "branches": []}
# gained: {"lines": [10, 11, 12, 13], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_stores_all_constructor_arguments():
    token = Token("hello", 3, 8, "hello")

    assert token._value == "hello"
    assert token._start_index == 3
    assert token._end_index == 8
    assert token._content == "hello"


def test_token_content_defaults_to_empty_string():
    token = Token(42, 0, 2)

    assert token._value == 42
    assert token._start_index == 0
    assert token._end_index == 2
    assert token._content == ""


@pytest.mark.parametrize(
    "value,start_index,end_index,content",
    [
        (None, 0, 0, ""),
        ("", 5, 5, "raw"),
        ({"a": 1}, 10, 20, "{\"a\": 1}"),
        ([1, 2, 3], 1, 4, "[1, 2, 3]"),
        (3.5, 7, 9, "3.5"),
    ],
)
def test_token_attributes_match_inputs(value, start_index, end_index, content):
    token = Token(value, start_index, end_index, content)

    assert token._value is value or token._value == value
    assert token._start_index == start_index
    assert token._end_index == end_index
    assert token._content == content


def test_token_instances_are_independent():
    first = Token("a", 0, 1, "a")
    second = Token("b", 1, 2, "b")

    assert first._value == "a"
    assert second._value == "b"
    assert first._start_index == 0
    assert second._start_index == 1
    assert first._content == "a"
    assert second._content == "b"
