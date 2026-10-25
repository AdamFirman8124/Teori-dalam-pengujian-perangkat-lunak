# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import importlib

import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokenize_yaml import tokenize_yaml
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def test_tokenize_yaml_constructs_all_supported_token_types():
    content = (
        "text: hello\n"
        "integer: 12\n"
        "float: 1.5\n"
        "boolean: true\n"
        "nothing: null\n"
        "items:\n"
        "  - world\n"
        "  - 7\n"
    )

    token = tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "text": "hello",
        "integer": 12,
        "float": 1.5,
        "boolean": True,
        "nothing": None,
        "items": ["world", 7],
    }

    assert isinstance(token.lookup(["text"]), ScalarToken)
    assert token.lookup(["text"]).value == "hello"
    assert token.lookup(["text"]).string == "hello"

    assert isinstance(token.lookup(["integer"]), ScalarToken)
    assert token.lookup(["integer"]).value == 12

    assert isinstance(token.lookup(["float"]), ScalarToken)
    assert token.lookup(["float"]).value == 1.5

    assert isinstance(token.lookup(["boolean"]), ScalarToken)
    assert token.lookup(["boolean"]).value is True

    assert isinstance(token.lookup(["nothing"]), ScalarToken)
    assert token.lookup(["nothing"]).value is None

    assert isinstance(token.lookup(["items"]), ListToken)
    assert token.lookup(["items"]).value == ["world", 7]
    assert isinstance(token.lookup(["items", 0]), ScalarToken)
    assert token.lookup(["items", 0]).value == "world"


def test_tokenize_yaml_decodes_bytes_and_ignores_invalid_utf8():
    token = tokenize_yaml(b"\xff42")

    assert isinstance(token, ScalarToken)
    assert token.value == 42
    assert token.string == "42"
    assert token.start == Position(line_no=1, column_no=1, char_index=0)
    assert token.end == Position(line_no=1, column_no=2, char_index=1)


@pytest.mark.parametrize("content", ["", " \n\t", b"", b" \n\t"])
def test_tokenize_yaml_rejects_empty_content(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(content)

    messages = exc_info.value.messages()
    expected_position = Position(line_no=1, column_no=1, char_index=0)

    assert len(messages) == 1
    assert messages[0].text == "No content."
    assert messages[0].code == "no_content"
    assert messages[0].start_position == expected_position
    assert messages[0].end_position == expected_position


def test_tokenize_yaml_converts_yaml_parser_error_to_parse_error():
    content = "[1, 2"

    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(content)

    messages = exc_info.value.messages()
    expected_position = Position(line_no=1, column_no=6, char_index=5)

    assert len(messages) == 1
    assert messages[0].code == "parse_error"
    assert messages[0].text.endswith(".")
    assert messages[0].start_position == expected_position
    assert messages[0].end_position == expected_position


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    module = importlib.import_module(tokenize_yaml.__module__)
    monkeypatch.setattr(module, "yaml", None)

    with pytest.raises(AssertionError, match="pyyaml.*must be installed"):
        tokenize_yaml("value")
