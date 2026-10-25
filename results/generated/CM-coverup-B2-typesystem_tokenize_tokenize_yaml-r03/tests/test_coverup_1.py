# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import importlib

import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


tokenize_yaml_module = importlib.import_module("typesystem.tokenize.tokenize_yaml")


def test_tokenize_yaml_builds_all_token_types_from_bytes():
    content = (
        b"name: hello\n"
        b"items:\n"
        b"  - 7\n"
        b"  - 2.5\n"
        b"  - true\n"
        b"  - null\n"
    )

    token = tokenize_yaml_module.tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "hello",
        "items": [7, 2.5, True, None],
    }
    assert token.start == Position(line_no=1, column_no=1, char_index=0)

    name_token = token.lookup(["name"])
    items_token = token.lookup(["items"])

    assert isinstance(name_token, ScalarToken)
    assert name_token.value == "hello"
    assert isinstance(items_token, ListToken)

    expected_values = [7, 2.5, True, None]
    for index, expected_value in enumerate(expected_values):
        item_token = token.lookup(["items", index])
        assert isinstance(item_token, ScalarToken)
        assert item_token.value == expected_value


@pytest.mark.parametrize("content", ["", " \n\t "])
def test_tokenize_yaml_rejects_empty_string_content(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml_module.tokenize_yaml(content)

    message = exc_info.value.messages()[0]
    expected_position = Position(line_no=1, column_no=1, char_index=0)

    assert message.text == "No content."
    assert message.code == "no_content"
    assert message.start_position == expected_position
    assert message.end_position == expected_position


@pytest.mark.parametrize(
    "content",
    [
        'key: "\\q"\n',
        "key: [1, 2\n",
    ],
)
def test_tokenize_yaml_converts_yaml_syntax_errors_to_parse_errors(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml_module.tokenize_yaml(content)

    message = exc_info.value.messages()[0]
    position = message.start_position

    assert message.code == "parse_error"
    assert message.text
    assert message.text.endswith(".")
    assert position is not None
    assert message.end_position == position
    assert 0 <= position.char_index <= len(content)
    assert position.line_no == content.count("\n", 0, position.char_index) + 1
    assert position.column_no == (
        position.char_index - content.rfind("\n", 0, position.char_index)
    )


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        tokenize_yaml_module.tokenize_yaml("key: value")
