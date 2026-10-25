# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import importlib

import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


tokenize_yaml_module = importlib.import_module("typesystem.tokenize.tokenize_yaml")


def test_tokenize_yaml_constructs_all_token_types():
    content = (
        "name: hello\n"
        "items:\n"
        "  - 12\n"
        "  - 3.5\n"
        "  - true\n"
        "  - null\n"
    )

    token = tokenize_yaml_module.tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "hello",
        "items": [12, 3.5, True, None],
    }

    name_key = token.lookup_key(["name"])
    name = token.lookup(["name"])
    items = token.lookup(["items"])
    integer = token.lookup(["items", 0])
    floating_point = token.lookup(["items", 1])
    boolean = token.lookup(["items", 2])
    null = token.lookup(["items", 3])

    assert isinstance(name_key, ScalarToken)
    assert name_key.value == "name"
    assert name_key.string == "name"

    assert isinstance(name, ScalarToken)
    assert name.value == "hello"
    assert name.string == "hello"
    assert name.start == Position(line_no=1, column_no=7, char_index=6)
    assert name.end == Position(line_no=1, column_no=11, char_index=10)

    assert isinstance(items, ListToken)
    assert items.value == [12, 3.5, True, None]

    assert isinstance(integer, ScalarToken)
    assert integer.value == 12
    assert integer.string == "12"

    assert isinstance(floating_point, ScalarToken)
    assert floating_point.value == 3.5
    assert floating_point.string == "3.5"

    assert isinstance(boolean, ScalarToken)
    assert boolean.value is True
    assert boolean.string == "true"

    assert isinstance(null, ScalarToken)
    assert null.value is None
    assert null.string == "null"


def test_tokenize_yaml_accepts_bytes_and_ignores_invalid_utf8():
    token = tokenize_yaml_module.tokenize_yaml(b"value: \xff42\n")

    assert isinstance(token, DictToken)
    assert token.value == {"value": 42}

    value = token.lookup(["value"])
    assert isinstance(value, ScalarToken)
    assert value.value == 42
    assert value.string == "42"


@pytest.mark.parametrize("content", ["", " \n\t ", b" \n\t "])
def test_tokenize_yaml_rejects_empty_content(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml_module.tokenize_yaml(content)

    message = exc_info.value.messages()[0]
    expected_position = Position(line_no=1, column_no=1, char_index=0)

    assert message.text == "No content."
    assert message.code == "no_content"
    assert message.start_position == expected_position
    assert message.end_position == expected_position


@pytest.mark.parametrize(
    ("content", "expected_index"),
    [
        ("key: @invalid", 5),
        ("[1, 2", 5),
    ],
)
def test_tokenize_yaml_converts_yaml_syntax_errors(content, expected_index):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml_module.tokenize_yaml(content)

    message = exc_info.value.messages()[0]
    expected_position = Position(
        line_no=1,
        column_no=expected_index + 1,
        char_index=expected_index,
    )

    assert message.code == "parse_error"
    assert message.text.endswith(".")
    assert message.start_position == expected_position
    assert message.end_position == expected_position


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        tokenize_yaml_module.tokenize_yaml("value: 1")
