# file: project/typesystem/tokenize/tokenize_json.py:20-95
# asked: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}
# gained: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}

import pytest
from typesystem.base import ParseError
from typesystem.tokenize.tokenize_json import tokenize_json


def _assert_parse_error(content, fragment):
    with pytest.raises(ParseError) as exc_info:
        tokenize_json(content)
    err = exc_info.value
    text = getattr(err, "text", str(err))
    assert fragment in text
    return err


def test_empty_objects():
    t1 = tokenize_json("{}")
    assert t1 is not None
    assert type(t1).__name__ == "DictToken"

    t2 = tokenize_json("{ }")
    assert t2 is not None
    assert type(t2).__name__ == "DictToken"

    t3 = tokenize_json("{\n\t }")
    assert t3 is not None
    assert type(t3).__name__ == "DictToken"

    t4 = tokenize_json(b"{}")
    assert t4 is not None


def test_simple_object_fast_path_colon():
    t = tokenize_json('{"a":1}')
    assert t is not None
    assert type(t).__name__ == "DictToken"

    t2 = tokenize_json('{"a":1,"b":2}')
    assert t2 is not None

    t3 = tokenize_json('{"a":1, "b":2, "c":3}')
    assert t3 is not None


def test_colon_with_whitespace():
    t1 = tokenize_json('{"a" : 1}')
    assert t1 is not None

    t2 = tokenize_json('{"a"  :  1}')
    assert t2 is not None

    t3 = tokenize_json('{"a"\n :\n 1}')
    assert t3 is not None


def test_missing_colon_raises():
    _assert_parse_error('{"a" 1}', "Expecting ':' delimiter")
    _assert_parse_error('{"a" }', "Expecting ':' delimiter")
    _assert_parse_error('{"a" ,}', "Expecting ':' delimiter")


def test_value_whitespace_fast_paths():
    t1 = tokenize_json('{"a": 1}')
    assert t1 is not None

    t2 = tokenize_json('{"a":   1}')
    assert t2 is not None

    t3 = tokenize_json('{"a": \t\n 1}')
    assert t3 is not None

    t4 = tokenize_json('{"a":\n  1 }')
    assert t4 is not None


def test_missing_value_raises():
    _assert_parse_error('{"a":', "Expecting value")
    _assert_parse_error('{"a": ', "Expecting value")
    _assert_parse_error('{"a": }', "Expecting value")
    _assert_parse_error('{"a": x}', "Expecting value")
    _assert_parse_error('{"a":1, "b":}', "Expecting value")


def test_value_trailing_whitespace_and_truncation():
    t = tokenize_json('{"a":1 }')
    assert t is not None

    t2 = tokenize_json('{"a":1  }')
    assert t2 is not None

    t3 = tokenize_json('{"a" : 1 , "b" : 2 }')
    assert t3 is not None

    _assert_parse_error('{"a":1', "Expecting ',' delimiter")
    _assert_parse_error('{"a":1 ', "Expecting ',' delimiter")
    _assert_parse_error('{"a":1  ', "Expecting ',' delimiter")


def test_comma_and_delimiter_errors():
    _assert_parse_error('{"a":1;}', "Expecting ',' delimiter")
    _assert_parse_error('{"a":1 2}', "Expecting ',' delimiter")
    _assert_parse_error('{"a":1 "b":2}', "Expecting ',' delimiter")


def test_property_name_errors():
    _assert_parse_error('{x}', "Expecting property name")
    _assert_parse_error('{ x}', "Expecting property name")
    _assert_parse_error('{  x}', "Expecting property name")
    _assert_parse_error('{"a":1,}', "Expecting property name")
    _assert_parse_error('{"a":1, 123}', "Expecting property name")
    _assert_parse_error('{"a":1, b}', "Expecting property name")
    _assert_parse_error('{"a":1, "b":2, }', "Expecting property name")
