# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import importlib

import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


tokenize_yaml_module = importlib.import_module("typesystem.tokenize.tokenize_yaml")


def test_tokenize_yaml_constructs_all_token_types_from_bytes():
    content = (
        b"\xfftext: hello\n"
        b"integer: 12\n"
        b"floating: 1.5\n"
        b"boolean: true\n"
        b"nothing: null\n"
        b"items:\n"
        b"  - world\n"
    )

    token = tokenize_yaml_module.tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "text": "hello",
        "integer": 12,
        "floating": 1.5,
        "boolean": True,
        "nothing": None,
        "items": ["world"],
    }

    expected_scalars = {
        "text": "hello",
        "integer": 12,
        "floating": 1.5,
        "boolean": True,
        "nothing": None,
    }
    for key, expected_value in expected_scalars.items():
        key_token = token.lookup_key([key])
        value_token = token.lookup([key])

        assert isinstance(key_token, ScalarToken)
        assert key_token.value == key
        assert isinstance(value_token, ScalarToken)
        assert value_token.value == expected_value

    items_token = token.lookup(["items"])
    item_token = token.lookup(["items", 0])

    assert isinstance(items_token, ListToken)
    assert items_token.value == ["world"]
    assert isinstance(item_token, ScalarToken)
    assert item_token.value == "world"

    decoded_content = content.decode("utf-8", "ignore")
    assert token.string == decoded_content
    assert token.start == Position(line_no=1, column_no=1, char_index=0)


@pytest.mark.parametrize("content", ["", " \n\t "])
def test_tokenize_yaml_rejects_empty_content(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml_module.tokenize_yaml(content)

    messages = exc_info.value.messages()
    assert len(messages) == 1

    message = messages[0]
    expected_position = Position(line_no=1, column_no=1, char_index=0)

    assert message.text == "No content."
    assert message.code == "no_content"
    assert message.start_position == expected_position
    assert message.end_position == expected_position


@pytest.mark.parametrize(
    "content",
    [
        "\tinvalid",
        "items:\n  [one, two\n",
    ],
)
def test_tokenize_yaml_converts_yaml_syntax_errors_to_parse_errors(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml_module.tokenize_yaml(content)

    messages = exc_info.value.messages()
    assert len(messages) == 1

    message = messages[0]
    assert message.code == "parse_error"
    assert message.text.endswith(".")
    assert message.start_position is not None
    assert message.end_position == message.start_position
    assert message.start_position.line_no >= 1
    assert message.start_position.column_no >= 1
    assert 0 <= message.start_position.char_index <= len(content)


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        tokenize_yaml_module.tokenize_yaml("value")
