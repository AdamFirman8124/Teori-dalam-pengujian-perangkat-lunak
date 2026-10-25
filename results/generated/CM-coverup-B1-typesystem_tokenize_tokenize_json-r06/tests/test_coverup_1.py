# file: project/typesystem/tokenize/tokenize_json.py:20-95
# asked: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}
# gained: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}

import pytest
from json.decoder import JSONDecodeError

from typesystem.tokenize.tokenize_json import (
    _TokenizingDecoder,
    _TokenizingJSONObject,
)
from typesystem.tokenize.tokens import DictToken, ScalarToken


def _make_scan_once(content):
    # Each call builds a fresh decoder/scanner, so no state leaks between tests.
    decoder = _TokenizingDecoder(content=content)
    return decoder.scan_once


def _as_plain_dict(result):
    return {key.value: value.value for key, value in result.items()}


def test_simple_object_covers_main_loop_and_return():
    content = '{"a": 1}'
    scan_once = _make_scan_once(content)
    result, end = _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert end == len(content)
    assert len(result) == 1
    assert _as_plain_dict(result) == {"a": 1}
    key, value = next(iter(result.items()))
    assert isinstance(key, ScalarToken)
    assert key.value == "a"
    assert isinstance(value, ScalarToken)
    assert value.value == 1


def test_empty_object_returns_immediately():
    content = "{}"
    scan_once = _make_scan_once(content)
    result, end = _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert result == {}
    assert end == 2


def test_whitespace_before_first_key_and_around_delimiters():
    # s_and_end points just past the opening "{" (index 1), i.e. index 2.
    content = ' { "a" : 1 } '
    scan_once = _make_scan_once(content)
    result, end = _TokenizingJSONObject((content, 2), True, scan_once, {}, content)

    assert end == len(content) - 1
    assert _as_plain_dict(result) == {"a": 1}


def test_multiple_whitespace_chars_after_colon():
    content = '{"a":  1}'
    scan_once = _make_scan_once(content)
    result, end = _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert end == len(content)
    assert _as_plain_dict(result) == {"a": 1}


def test_nested_object_as_value():
    content = '{"a": {"b": 1}}'
    scan_once = _make_scan_once(content)
    result, end = _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert end == len(content)
    assert len(result) == 1
    key, value = next(iter(result.items()))
    assert key.value == "a"
    assert isinstance(value, DictToken)


def test_duplicate_keys_use_memo():
    # ScalarToken instances do not compare equal by value, so duplicate keys
    # end up as two distinct dict entries; both pairs are still appended.
    content = '{"a": 1, "a": 2}'
    scan_once = _make_scan_once(content)
    memo = {}
    result, end = _TokenizingJSONObject((content, 1), True, scan_once, memo, content)

    assert end == len(content)
    assert len(result) == 2
    assert sorted(value.value for value in result.values()) == [1, 2]
    assert all(key.value == "a" for key in result)
    # The memo was populated with the repeated key string.
    assert memo == {"a": "a"}


def test_key_not_enclosed_in_double_quotes_raises():
    content = "{a: 1}"
    scan_once = _make_scan_once(content)

    with pytest.raises(JSONDecodeError) as excinfo:
        _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert "property name enclosed in double quotes" in excinfo.value.msg
    assert excinfo.value.pos == 1


def test_missing_colon_raises():
    content = '{"a" 1}'
    scan_once = _make_scan_once(content)

    with pytest.raises(JSONDecodeError) as excinfo:
        _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert "Expecting ':' delimiter" in excinfo.value.msg
    assert excinfo.value.pos == 5


def test_missing_value_raises_expecting_value():
    content = '{"a":'
    scan_once = _make_scan_once(content)

    with pytest.raises(JSONDecodeError) as excinfo:
        _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert "Expecting value" in excinfo.value.msg
    assert excinfo.value.pos == 5


def test_missing_closing_brace_raises_expecting_comma():
    content = '{"a": 1'
    scan_once = _make_scan_once(content)

    with pytest.raises(JSONDecodeError) as excinfo:
        _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert "Expecting ',' delimiter" in excinfo.value.msg
    assert excinfo.value.pos == 7


def test_unquoted_key_after_comma_raises():
    content = '{"a": 1, 2: 3}'
    scan_once = _make_scan_once(content)

    with pytest.raises(JSONDecodeError) as excinfo:
        _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert "property name enclosed in double quotes" in excinfo.value.msg
    assert excinfo.value.pos == 9


def test_multiple_keys_cover_comma_continuation_path():
    content = '{"a": 1, "b": "x"}'
    scan_once = _make_scan_once(content)
    result, end = _TokenizingJSONObject((content, 1), True, scan_once, {}, content)

    assert end == len(content)
    assert _as_plain_dict(result) == {"a": 1, "b": "x"}
