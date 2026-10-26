# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import pytest

from json.decoder import JSONDecoder

from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def _make_scanner_with_context(content):
    # Each test builds its own decoder context, so no state leaks between tests.
    context = JSONDecoder()
    return context, _make_scanner(context, content)


def test_scan_string():
    context, scan_once = _make_scanner_with_context('"abc"')
    token, end = scan_once('"abc"', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == "abc"
    assert token.start.char_index == 0
    assert token.end.char_index == 4
    assert end == 5
    assert context.memo == {}


def test_scan_object():
    content = '{"a": 1}'
    context, scan_once = _make_scanner_with_context(content)
    token, end = scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1
    assert end == len(content)
    assert context.memo == {}


def test_scan_object_with_whitespace_and_null_value():
    content = '{ "a" : 1 , "b" : null }'
    context, scan_once = _make_scanner_with_context(content)
    token, end = scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1
    assert end == len(content)
    assert context.memo == {}


def test_scan_array():
    content = '[1, 2]'
    context, scan_once = _make_scanner_with_context(content)
    token, end = scan_once(content, 0)
    assert isinstance(token, ListToken)
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1
    assert end == len(content)
    assert context.memo == {}


@pytest.mark.parametrize(
    "content,expected_value",
    [("null", None), ("true", True), ("false", False)],
)
def test_scan_literals(content, expected_value):
    context, scan_once = _make_scanner_with_context(content)
    token, end = scan_once(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value is expected_value
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1
    assert end == len(content)
    assert context.memo == {}


def test_scan_integer():
    content = "42"
    context, scan_once = _make_scanner_with_context(content)
    token, end = scan_once(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 42
    assert isinstance(token.value, int) and not isinstance(token.value, bool)
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1
    assert end == len(content)
    assert context.memo == {}


def test_scan_float():
    content = "1.5"
    context, scan_once = _make_scanner_with_context(content)
    token, end = scan_once(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 1.5
    assert isinstance(token.value, float)
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1
    assert end == len(content)
    assert context.memo == {}


def test_scan_number_with_exponent_uses_parse_float():
    content = "1e2"
    context, scan_once = _make_scanner_with_context(content)
    token, end = scan_once(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 100.0
    assert isinstance(token.value, float)
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1
    assert end == len(content)
    assert context.memo == {}


def test_scan_empty_input_raises_stop_iteration():
    # Covers the IndexError branch: string[idx] on an empty string.
    context, scan_once = _make_scanner_with_context("")
    with pytest.raises(StopIteration) as excinfo:
        scan_once("", 0)
    assert excinfo.value.value == 0
    # The finally clause must still have cleared the memo.
    assert context.memo == {}


def test_scan_unrecognized_character_raises_stop_iteration():
    # Covers the final else branch raising StopIteration(idx).
    context, scan_once = _make_scanner_with_context("x")
    with pytest.raises(StopIteration) as excinfo:
        scan_once("x", 0)
    assert excinfo.value.value == 0
    assert context.memo == {}


def test_memo_cleared_even_when_scan_fails():
    # Covers the try/finally in scan_once: memo.clear() runs on the error path too.
    context, scan_once = _make_scanner_with_context("zzz")
    context.memo["sentinel"] = "sentinel"
    with pytest.raises(StopIteration):
        scan_once("zzz", 0)
    assert context.memo == {}
