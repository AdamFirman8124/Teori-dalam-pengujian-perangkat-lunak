# file: project/typesystem/tokenize/tokenize_json.py:20-95
# asked: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}
# gained: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}

import pytest
from json.decoder import JSONDecodeError

from typesystem.tokenize.tokenize_json import (
    _TokenizingDecoder,
    _TokenizingJSONObject,
    tokenize_json,
)


def _parse_object(content, start=1):
    """Call _TokenizingJSONObject directly with a real scanner."""
    decoder = _TokenizingDecoder(content=content)
    return _TokenizingJSONObject((content, start), True, decoder.scan_once, {}, content)


def test_empty_object():
    result, end = _parse_object("{}")
    assert result == {}
    assert end == 2


def test_empty_object_with_whitespace():
    result, end = _parse_object("{  }")
    assert result == {}
    assert end == 4


def test_object_with_leading_whitespace():
    result, end = _parse_object('{ "a": 1}')
    assert end == 9
    (key, value), = result.items()
    assert key.value == "a"
    assert value.value == 1


def test_invalid_property_name():
    with pytest.raises(JSONDecodeError) as exc_info:
        _parse_object("{1: 2}")
    assert exc_info.value.msg == "Expecting property name enclosed in double quotes"
    assert exc_info.value.pos == 1


def test_whitespace_before_colon():
    result, end = _parse_object('{"a" : 1}')
    assert end == 9
    assert list(result.values())[0].value == 1


def test_missing_colon_delimiter():
    with pytest.raises(JSONDecodeError) as exc_info:
        _parse_object('{"a" 1}')
    assert exc_info.value.msg == "Expecting ':' delimiter"


def test_whitespace_after_colon():
    result, end = _parse_object('{"a":  1}')
    assert end == 9
    assert list(result.values())[0].value == 1


def test_missing_value():
    with pytest.raises(JSONDecodeError) as exc_info:
        _parse_object('{"a":')
    assert exc_info.value.msg == "Expecting value"


def test_whitespace_before_closing_brace():
    result, end = _parse_object('{"a": 1 }')
    assert end == 9
    assert list(result.values())[0].value == 1


def test_missing_comma_delimiter():
    with pytest.raises(JSONDecodeError) as exc_info:
        _parse_object('{"a": 1 "b": 2}')
    assert exc_info.value.msg == "Expecting ',' delimiter"


def test_unterminated_object():
    with pytest.raises(JSONDecodeError) as exc_info:
        _parse_object('{"a": 1')
    assert exc_info.value.msg == "Expecting ',' delimiter"


def test_trailing_whitespace_without_closing_brace():
    with pytest.raises(JSONDecodeError) as exc_info:
        _parse_object('{"a": 1 ')
    assert exc_info.value.msg == "Expecting ',' delimiter"


def test_multiple_pairs_with_whitespace():
    content = '{"a": 1, "b": 2}'
    result, end = _parse_object(content)
    assert end == len(content)
    assert [key.value for key in result] == ["a", "b"]
    assert [value.value for value in result.values()] == [1, 2]


def test_invalid_property_name_after_comma():
    with pytest.raises(JSONDecodeError) as exc_info:
        _parse_object('{"a": 1, 2: 3}')
    assert exc_info.value.msg == "Expecting property name enclosed in double quotes"


def test_duplicate_keys():
    content = '{"a": 1, "a": 2}'
    result, end = _parse_object(content)
    assert end == len(content)
    assert {key.value for key in result} == {"a"}


def test_tokenize_json_uses_tokenizing_object():
    token = tokenize_json('{"a": 1}')
    assert token.string == '{"a": 1}'
