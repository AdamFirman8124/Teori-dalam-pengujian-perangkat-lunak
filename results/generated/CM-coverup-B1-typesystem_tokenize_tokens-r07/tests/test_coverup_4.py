# file: project/typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [10, 11, 12, 13], "branches": []}
# gained: {"lines": [10, 11, 12, 13], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_init_stores_all_fields():
    token = Token("abc", 1, 4, "abc")

    assert token._value == "abc"
    assert token._start_index == 1
    assert token._end_index == 4
    assert token._content == "abc"


def test_token_init_default_content_is_empty_string():
    token = Token(42, 0, 2)

    assert token._value == 42
    assert token._start_index == 0
    assert token._end_index == 2
    assert token._content == ""


def test_token_init_accepts_arbitrary_value_and_negative_indices():
    value = {"nested": [1, 2, 3]}
    token = Token(value, -5, -1, "text")

    assert token._value is value
    assert token._start_index == -5
    assert token._end_index == -1
    assert token._content == "text"


def test_token_instances_do_not_share_state():
    first = Token("a", 0, 1)
    second = Token("b", 1, 2, "b")

    assert first._value == "a"
    assert first._start_index == 0
    assert first._end_index == 1
    assert first._content == ""

    assert second._value == "b"
    assert second._start_index == 1
    assert second._end_index == 2
    assert second._content == "b"
