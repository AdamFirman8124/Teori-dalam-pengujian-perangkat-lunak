# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import importlib

import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


tokenize_yaml_module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
tokenize_yaml = tokenize_yaml_module.tokenize_yaml


def test_tokenize_yaml_rejects_missing_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        tokenize_yaml("value")


def test_tokenize_yaml_rejects_empty_content():
    with pytest.raises(ParseError) as caught:
        tokenize_yaml(" \n\t ")

    message = caught.value.messages()[0]
    expected_position = Position(column_no=1, line_no=1, char_index=0)

    assert message.text == "No content."
    assert message.code == "no_content"
    assert message.start_position == expected_position
    assert message.end_position == expected_position


def test_tokenize_yaml_constructs_all_token_types_from_bytes():
    content = (
        b"text: hello\n"
        b"integer: 42\n"
        b"floating: 3.5\n"
        b"boolean: true\n"
        b"nothing: null\n"
        b"items:\n"
        b"  - world\n"
        b"  - 7\n"
        b"\xff"
    )

    token = tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "text": "hello",
        "integer": 42,
        "floating": 3.5,
        "boolean": True,
        "nothing": None,
        "items": ["world", 7],
    }

    text = token.lookup(["text"])
    integer = token.lookup(["integer"])
    floating = token.lookup(["floating"])
    boolean = token.lookup(["boolean"])
    nothing = token.lookup(["nothing"])
    items = token.lookup(["items"])

    assert isinstance(text, ScalarToken)
    assert isinstance(integer, ScalarToken)
    assert isinstance(floating, ScalarToken)
    assert isinstance(boolean, ScalarToken)
    assert isinstance(nothing, ScalarToken)
    assert isinstance(items, ListToken)
    assert isinstance(items.lookup([0]), ScalarToken)
    assert isinstance(items.lookup([1]), ScalarToken)

    assert text.string == "hello"
    assert integer.string == "42"
    assert floating.string == "3.5"
    assert boolean.string == "true"
    assert nothing.string == "null"
    assert items.lookup([0]).string == "world"
    assert items.lookup([1]).string == "7"

    assert text.start == Position(line_no=1, column_no=7, char_index=6)
    assert text.end == Position(line_no=1, column_no=11, char_index=10)
    assert items.lookup([0]).value == "world"
    assert items.lookup([1]).value == 7


@pytest.mark.parametrize(
    "content",
    [
        'key: "unterminated',
        "key: [1, 2",
    ],
)
def test_tokenize_yaml_converts_yaml_syntax_errors(content):
    with pytest.raises(ParseError) as caught:
        tokenize_yaml(content)

    message = caught.value.messages()[0]

    assert message.code == "parse_error"
    assert message.text.endswith(".")
    assert message.start_position is not None
    assert message.end_position == message.start_position
    assert message.start_position.char_index >= 0
    assert message.start_position.line_no >= 1
    assert message.start_position.column_no >= 1
