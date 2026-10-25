# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import json

import pytest

from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        ('"hello"', "hello"),
        ("null", None),
        ("true", True),
        ("false", False),
    ],
)
def test_make_scanner_parses_scalar_literals(content, expected):
    context = json.JSONDecoder()
    context.memo["sentinel"] = object()
    scan_once = _make_scanner(context, content)

    token, end = scan_once(content, 0)

    assert isinstance(token, ScalarToken)
    assert token.value == expected
    assert token.string == content
    assert end == len(content)
    assert context.memo == {}


def test_make_scanner_parses_object():
    content = '{"answer": 42, "valid": true}'
    context = json.JSONDecoder()
    scan_once = _make_scanner(context, content)

    token, end = scan_once(content, 0)

    assert isinstance(token, DictToken)
    assert token.value == {"answer": 42, "valid": True}
    assert token.string == content
    assert end == len(content)
    assert context.memo == {}


def test_make_scanner_parses_array():
    content = '[1, "two", null, false]'
    context = json.JSONDecoder()
    context.memo["sentinel"] = object()
    scan_once = _make_scanner(context, content)

    token, end = scan_once(content, 0)

    assert isinstance(token, ListToken)
    assert token.value == [1, "two", None, False]
    assert token.string == content
    assert end == len(content)
    assert context.memo == {}


def test_make_scanner_uses_parse_int():
    content = "123"
    parsed_values = []
    context = json.JSONDecoder()

    def parse_int(value):
        parsed_values.append(value)
        return ("integer", value)

    context.parse_int = parse_int
    scan_once = _make_scanner(context, content)

    token, end = scan_once(content, 0)

    assert isinstance(token, ScalarToken)
    assert token.value == ("integer", "123")
    assert token.string == content
    assert end == len(content)
    assert parsed_values == ["123"]
    assert context.memo == {}


@pytest.mark.parametrize(
    ("content", "expected_argument"),
    [
        ("1.25", "1.25"),
        ("1e2", "1e2"),
        ("1.25e2", "1.25e2"),
    ],
)
def test_make_scanner_uses_parse_float(content, expected_argument):
    parsed_values = []
    context = json.JSONDecoder()

    def parse_float(value):
        parsed_values.append(value)
        return ("float", value)

    context.parse_float = parse_float
    scan_once = _make_scanner(context, content)

    token, end = scan_once(content, 0)

    assert isinstance(token, ScalarToken)
    assert token.value == ("float", expected_argument)
    assert token.string == content
    assert end == len(content)
    assert parsed_values == [expected_argument]
    assert context.memo == {}


@pytest.mark.parametrize("content", ["nope", "truth", "falsy", "x"])
def test_make_scanner_rejects_invalid_values_and_clears_memo(content):
    context = json.JSONDecoder()
    context.memo["sentinel"] = object()
    scan_once = _make_scanner(context, content)

    with pytest.raises(StopIteration) as exc_info:
        scan_once(content, 0)

    assert exc_info.value.value == 0
    assert context.memo == {}


def test_make_scanner_rejects_index_at_end_and_clears_memo():
    content = "null"
    context = json.JSONDecoder()
    context.memo["sentinel"] = object()
    scan_once = _make_scanner(context, content)

    with pytest.raises(StopIteration) as exc_info:
        scan_once(content, len(content))

    assert exc_info.value.value == len(content)
    assert context.memo == {}
