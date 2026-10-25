# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import json

import pytest

from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


@pytest.mark.parametrize(
    ("source", "index", "expected_value", "expected_end", "expected_string"),
    [
        ('"hello"', 0, "hello", 7, '"hello"'),
        ("xxnull", 2, None, 6, "null"),
        ("xxtrue", 2, True, 6, "true"),
        ("xxfalse", 2, False, 7, "false"),
    ],
)
def test_make_scanner_tokenizes_scalar_values(
    source, index, expected_value, expected_end, expected_string
):
    context = json.JSONDecoder()
    scanner = _make_scanner(context, source)

    token, end = scanner(source, index)

    assert isinstance(token, ScalarToken)
    assert token.value == expected_value
    assert token.string == expected_string
    assert token._start_index == index
    assert token._end_index == expected_end - 1
    assert end == expected_end
    assert context.memo == {}


@pytest.mark.parametrize(
    ("source", "expected_type", "expected_value"),
    [
        ('{"a": 1, "nested": {"enabled": true}}', DictToken, {
            "a": 1,
            "nested": {"enabled": True},
        }),
        ('[1, "x", null, false, {"a": 2}]', ListToken, [
            1,
            "x",
            None,
            False,
            {"a": 2},
        ]),
        ("{}", DictToken, {}),
        ("[]", ListToken, []),
    ],
)
def test_make_scanner_tokenizes_objects_and_arrays(
    source, expected_type, expected_value
):
    context = json.JSONDecoder()
    context.memo["stale"] = "value"
    scanner = _make_scanner(context, source)

    token, end = scanner(source, 0)

    assert isinstance(token, expected_type)
    assert token.value == expected_value
    assert token.string == source
    assert token._start_index == 0
    assert token._end_index == len(source) - 1
    assert end == len(source)
    assert context.memo == {}


@pytest.mark.parametrize(
    ("source", "expected_value", "expected_call"),
    [
        ("123", ("integer", "123"), ("int", "123")),
        ("1.5", ("floating", "1.5"), ("float", "1.5")),
        ("1e2", ("floating", "1e2"), ("float", "1e2")),
        ("1.5e2", ("floating", "1.5e2"), ("float", "1.5e2")),
    ],
)
def test_make_scanner_uses_number_conversion_hooks(
    source, expected_value, expected_call
):
    calls = []

    def parse_int(value):
        calls.append(("int", value))
        return ("integer", value)

    def parse_float(value):
        calls.append(("float", value))
        return ("floating", value)

    context = json.JSONDecoder(parse_int=parse_int, parse_float=parse_float)
    scanner = _make_scanner(context, source)

    token, end = scanner(source, 0)

    assert isinstance(token, ScalarToken)
    assert token.value == expected_value
    assert token.string == source
    assert end == len(source)
    assert calls == [expected_call]
    assert context.memo == {}


def test_make_scanner_raises_stop_iteration_at_end_and_clears_memo():
    context = json.JSONDecoder()
    context.memo["stale"] = "value"
    scanner = _make_scanner(context, "")

    with pytest.raises(StopIteration) as exc_info:
        scanner("", 0)

    assert exc_info.value.value == 0
    assert context.memo == {}


@pytest.mark.parametrize("source", ["?", "nope", "truth", "failure"])
def test_make_scanner_rejects_unrecognized_or_incomplete_values_and_clears_memo(
    source,
):
    context = json.JSONDecoder()
    context.memo["stale"] = "value"
    scanner = _make_scanner(context, source)

    with pytest.raises(StopIteration) as exc_info:
        scanner(source, 0)

    assert exc_info.value.value == 0
    assert context.memo == {}
