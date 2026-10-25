# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import importlib

import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokenize_yaml import tokenize_yaml
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def test_tokenize_yaml_builds_all_token_types():
    content = (
        "title: hello\n"
        "values:\n"
        "  - 12\n"
        "  - 1.5\n"
        "  - true\n"
        "  - null\n"
    )

    token = tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "title": "hello",
        "values": [12, 1.5, True, None],
    }
    assert token.string == content
    assert token.start == Position(line_no=1, column_no=1, char_index=0)

    title_key = token.lookup_key(["title"])
    title = token.lookup(["title"])
    values = token.lookup(["values"])

    assert isinstance(title_key, ScalarToken)
    assert title_key.value == "title"
    assert title_key.string == "title"

    assert isinstance(title, ScalarToken)
    assert title.value == "hello"
    assert title.string == "hello"

    assert isinstance(values, ListToken)
    assert values.value == [12, 1.5, True, None]

    expected = [
        (12, "12"),
        (1.5, "1.5"),
        (True, "true"),
        (None, "null"),
    ]
    for index, (expected_value, expected_string) in enumerate(expected):
        child = values.lookup([index])
        assert isinstance(child, ScalarToken)
        assert child.value == expected_value
        assert type(child.value) is type(expected_value)
        assert child.string == expected_string


def test_tokenize_yaml_decodes_bytes_and_ignores_invalid_utf8():
    token = tokenize_yaml(b"ab\xffcd")

    assert isinstance(token, ScalarToken)
    assert token.value == "abcd"
    assert token.string == "abcd"
    assert token.start == Position(line_no=1, column_no=1, char_index=0)
    assert token.end == Position(line_no=1, column_no=4, char_index=3)


@pytest.mark.parametrize("content", ["", " \n\t", b"", b" \n\t"])
def test_tokenize_yaml_rejects_empty_content(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(content)

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
def test_tokenize_yaml_converts_yaml_syntax_errors(content):
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(content)

    message = exc_info.value.messages()[0]

    assert message.code == "parse_error"
    assert message.text.endswith(".")
    assert message.start_position is not None
    assert message.end_position == message.start_position
    assert message.start_position.char_index >= 0
    assert message.start_position.line_no >= 1
    assert message.start_position.column_no >= 1


def test_tokenize_yaml_requires_pyyaml(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    monkeypatch.setattr(module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        module.tokenize_yaml("value")
