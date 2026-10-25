# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import pytest

from typesystem.base import ParseError
from typesystem.tokenize.tokenize_yaml import tokenize_yaml
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def test_tokenize_yaml_str_mapping():
    token = tokenize_yaml('{"a": 1}')
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1}
    assert token._start_index == 0
    assert token._end_index == len('{"a": 1}') - 1
    assert token._content == '{"a": 1}'


def test_tokenize_yaml_bytes_mapping():
    content = '{"a": 1}'.encode("utf-8")
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1}
    assert token._start_index == 0
    assert token._end_index == len('{"a": 1}') - 1
    assert token._content == '{"a": 1}'


def test_tokenize_yaml_sequence():
    token = tokenize_yaml("[1, 2, 3]")
    assert isinstance(token, ListToken)
    assert token.value == [1, 2, 3]
    assert token._start_index == 0
    assert token._end_index == len("[1, 2, 3]") - 1
    assert token._content == "[1, 2, 3]"


def test_tokenize_yaml_scalar_string():
    token = tokenize_yaml('"abc"')
    assert isinstance(token, ScalarToken)
    assert token.value == "abc"
    assert token._start_index == 0
    assert token._end_index == len('"abc"') - 1
    assert token._content == '"abc"'


def test_tokenize_yaml_int():
    token = tokenize_yaml("123")
    assert isinstance(token, ScalarToken)
    assert token.value == 123
    assert token._start_index == 0
    assert token._end_index == len("123") - 1
    assert token._content == "123"


def test_tokenize_yaml_float():
    token = tokenize_yaml("1.5")
    assert isinstance(token, ScalarToken)
    assert token.value == 1.5
    assert token._start_index == 0
    assert token._end_index == len("1.5") - 1
    assert token._content == "1.5"


def test_tokenize_yaml_bool():
    token = tokenize_yaml("true")
    assert isinstance(token, ScalarToken)
    assert token.value is True
    assert token._start_index == 0
    assert token._end_index == len("true") - 1
    assert token._content == "true"


def test_tokenize_yaml_null():
    token = tokenize_yaml("null")
    assert isinstance(token, ScalarToken)
    assert token.value is None
    assert token._start_index == 0
    assert token._end_index == len("null") - 1
    assert token._content == "null"


def test_tokenize_yaml_empty_string():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("")
    messages = exc_info.value.messages()
    assert len(messages) == 1
    assert messages[0].text == "No content."
    assert messages[0].code == "no_content"
    position = messages[0].start_position
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_tokenize_yaml_whitespace_only_string():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("   \n  ")
    messages = exc_info.value.messages()
    assert len(messages) == 1
    assert messages[0].text == "No content."
    assert messages[0].code == "no_content"
    position = messages[0].start_position
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0


def test_tokenize_yaml_parse_error():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("{invalid")
    messages = exc_info.value.messages()
    assert len(messages) == 1
    assert messages[0].code == "parse_error"
    assert messages[0].text.endswith(".")
    assert len(messages[0].text) > 1
    position = messages[0].start_position
    assert position is not None
    assert position.line_no >= 1
    assert position.column_no >= 1
    assert position.char_index >= 0


def test_tokenize_yaml_nested_structures():
    content = '{"a": [1, 2], "b": {"c": true}}'
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"a": [1, 2], "b": {"c": True}}
    key_token = token._child_keys["a"]
    assert isinstance(key_token, ScalarToken)
    assert key_token.value == "a"
    assert key_token._content == content
    child_token = token._child_tokens["a"]
    assert isinstance(child_token, ListToken)
    assert child_token.value == [1, 2]
    assert child_token._content == content
