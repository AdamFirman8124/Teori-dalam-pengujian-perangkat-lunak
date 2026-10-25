# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import json

import pytest

from typesystem.base import ParseError
from typesystem.tokenize.tokenize_json import (
    _make_scanner,
    _TokenizingDecoder,
    tokenize_json,
)
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


@pytest.mark.parametrize(
    "text, expected_type, expected_value",
    [
        ('"hi"', ScalarToken, "hi"),
        ("null", ScalarToken, None),
        ("true", ScalarToken, True),
        ("false", ScalarToken, False),
        ("42", ScalarToken, 42),
        ("-1.5", ScalarToken, -1.5),
        ("1e3", ScalarToken, 1000.0),
        ("[1, 2]", ListToken, [1, 2]),
        ('{"a": 1}', DictToken, {"a": 1}),
    ],
)
def test_scan_once_returns_expected_token(text, expected_type, expected_value):
    decoder = _TokenizingDecoder(content=text)
    token, end = decoder.scan_once(text, 0)

    assert isinstance(token, expected_type)
    assert token.value == expected_value
    assert end == len(text)
    assert decoder.memo == {}


def test_scan_once_raises_stop_iteration_at_end_of_string():
    decoder = _TokenizingDecoder(content="")
    with pytest.raises(StopIteration):
        decoder.scan_once("", 0)
    assert decoder.memo == {}


def test_scan_once_raises_stop_iteration_for_unrecognized_token():
    decoder = _TokenizingDecoder(content="x")
    with pytest.raises(StopIteration):
        decoder.scan_once("x", 0)
    assert decoder.memo == {}


def test_scan_once_clears_memo_on_success_and_error():
    class TrackingDict(dict):
        def __init__(self):
            super().__init__()
            self.clear_calls = 0

        def clear(self):
            self.clear_calls += 1
            super().clear()

    decoder = json.JSONDecoder()
    decoder.memo = TrackingDict()
    scan_once = _make_scanner(decoder, '{"a": 1}')

    token, end = scan_once('{"a": 1}', 0)
    assert token.value == {"a": 1}
    assert end == len('{"a": 1}')
    assert decoder.memo.clear_calls == 1
    assert decoder.memo == {}

    with pytest.raises(StopIteration):
        scan_once("x", 0)
    assert decoder.memo.clear_calls == 2
    assert decoder.memo == {}


def test_tokenize_json_covers_all_scanner_branches():
    content = (
        '{"string": "value", "object": {"nested": 1}, '
        '"array": [1, 2.5, 3e2], "null": null, "true": true, "false": false}'
    )
    token = tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "string": "value",
        "object": {"nested": 1},
        "array": [1, 2.5, 300.0],
        "null": None,
        "true": True,
        "false": False,
    }


def test_tokenize_json_truncated_object_raises_parse_error():
    with pytest.raises(ParseError):
        tokenize_json('{"a": ')


def test_tokenize_json_invalid_value_raises_parse_error():
    with pytest.raises(ParseError):
        tokenize_json('{"a": x}')
