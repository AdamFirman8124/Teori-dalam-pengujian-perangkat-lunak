# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import pytest
from json.decoder import JSONDecoder

from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def _scanner(content):
    context = JSONDecoder()
    context.memo["sentinel"] = object()
    return context, _make_scanner(context, content)


@pytest.mark.parametrize(
    ("content", "expected", "expected_type"),
    [
        ('"hello"', "hello", str),
        ("null", None, type(None)),
        ("true", True, bool),
        ("false", False, bool),
        ("-42", -42, int),
        ("1.5", 1.5, float),
        ("1e2", 100.0, float),
        ("1.5e-2", 0.015, float),
    ],
)
def test_make_scanner_scalar_branches(content, expected, expected_type):
    context, scan_once = _scanner(content)

    token, end = scan_once(content, 0)

    assert isinstance(token, ScalarToken)
    assert token.value == expected
    assert type(token.value) is expected_type
    assert token.string == content
    assert end == len(content)
    assert context.memo == {}


def test_make_scanner_object_branch():
    content = '{"name": "Ada", "active": true, "score": 3}'
    context, scan_once = _scanner(content)

    token, end = scan_once(content, 0)

    assert isinstance(token, DictToken)
    assert token.value == {"name": "Ada", "active": True, "score": 3}
    assert token.string == content
    assert end == len(content)
    assert context.memo == {}


def test_make_scanner_array_branch():
    content = '[1, "two", null, false, 3.5]'
    context, scan_once = _scanner(content)

    token, end = scan_once(content, 0)

    assert isinstance(token, ListToken)
    assert token.value == [1, "two", None, False, 3.5]
    assert token.string == content
    assert end == len(content)
    assert context.memo == {}


@pytest.mark.parametrize("content", ["x", "nope", "truth", "failure"])
def test_make_scanner_rejects_invalid_tokens_and_clears_memo(content):
    context, scan_once = _scanner(content)

    with pytest.raises(StopIteration) as exc_info:
        scan_once(content, 0)

    assert exc_info.value.value == 0
    assert context.memo == {}


def test_make_scanner_rejects_index_past_end_and_clears_memo():
    content = ""
    context, scan_once = _scanner(content)

    with pytest.raises(StopIteration) as exc_info:
        scan_once(content, 0)

    assert exc_info.value.value == 0
    assert context.memo == {}
