# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import importlib

import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokenize_yaml import tokenize_yaml
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


@pytest.mark.parametrize("content", [" \n\t", b" \n\t"])
def test_tokenize_yaml_rejects_empty_content(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(content)

    message = exc_info.value.messages()[0]
    expected_position = Position(line_no=1, column_no=1, char_index=0)
    assert message.text == "No content."
    assert message.code == "no_content"
    assert message.start_position == expected_position
    assert message.end_position == expected_position


def test_tokenize_yaml_constructs_all_supported_token_types():
    content = (
        "text: hello\n"
        "integer: 42\n"
        "float: 3.5\n"
        "boolean: true\n"
        "nothing: null\n"
        "sequence:\n"
        "  - item\n"
        "  - 7\n"
    )

    token = tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "text": "hello",
        "integer": 42,
        "float": 3.5,
        "boolean": True,
        "nothing": None,
        "sequence": ["item", 7],
    }

    key = token.lookup_key(["text"])
    assert isinstance(key, ScalarToken)
    assert key.value == "text"

    text = token.lookup(["text"])
    assert isinstance(text, ScalarToken)
    assert text.value == "hello"

    integer = token.lookup(["integer"])
    assert isinstance(integer, ScalarToken)
    assert integer.value == 42
    assert type(integer.value) is int

    floating_point = token.lookup(["float"])
    assert isinstance(floating_point, ScalarToken)
    assert floating_point.value == 3.5
    assert type(floating_point.value) is float

    boolean = token.lookup(["boolean"])
    assert isinstance(boolean, ScalarToken)
    assert boolean.value is True

    null = token.lookup(["nothing"])
    assert isinstance(null, ScalarToken)
    assert null.value is None

    sequence = token.lookup(["sequence"])
    assert isinstance(sequence, ListToken)
    assert sequence.value == ["item", 7]

    first_item = sequence.lookup([0])
    assert isinstance(first_item, ScalarToken)
    assert first_item.value == "item"

    second_item = sequence.lookup([1])
    assert isinstance(second_item, ScalarToken)
    assert second_item.value == 7


def test_tokenize_yaml_decodes_bytes_while_ignoring_invalid_utf8():
    token = tokenize_yaml(b"\xff123")

    assert isinstance(token, ScalarToken)
    assert token.value == 123
    assert token.string == "123"


@pytest.mark.parametrize("content", ["key: @", "[1, 2"])
def test_tokenize_yaml_converts_yaml_syntax_errors_to_parse_errors(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(content)

    message = exc_info.value.messages()[0]
    assert message.code == "parse_error"
    assert message.text.endswith(".")
    assert message.start_position is not None
    assert message.end_position == message.start_position
    assert 0 <= message.start_position.char_index <= len(content)
    assert message.start_position.line_no >= 1
    assert message.start_position.column_no >= 1


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    monkeypatch.setattr(module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        module.tokenize_yaml("value")
