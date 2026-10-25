# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import json

import pytest

from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


@pytest.mark.parametrize(
    ("source", "expected_type", "expected_value"),
    [
        ('"hello"', ScalarToken, "hello"),
        ('{"key": 1}', DictToken, {"key": 1}),
        ('[1, "two", true, null]', ListToken, [1, "two", True, None]),
        ("null", ScalarToken, None),
        ("true", ScalarToken, True),
        ("false", ScalarToken, False),
        ("-42", ScalarToken, -42),
        ("1.25", ScalarToken, 1.25),
        ("2e3", ScalarToken, 2000.0),
        ("3.5e-2", ScalarToken, 0.035),
    ],
)
def test_make_scanner_tokenizes_each_json_value_type(
    source, expected_type, expected_value
):
    decoder = json.JSONDecoder()
    scanner = _make_scanner(decoder, source)

    token, end = scanner(source, 0)

    assert isinstance(token, expected_type)
    assert token.value == expected_value
    assert token.string == source
    assert end == len(source)
    assert decoder.memo == {}


def test_make_scanner_uses_configured_number_parsers():
    integer_calls = []
    float_calls = []

    def parse_int(value):
        integer_calls.append(value)
        return ("integer", value)

    def parse_float(value):
        float_calls.append(value)
        return ("float", value)

    decoder = json.JSONDecoder(parse_int=parse_int, parse_float=parse_float)

    integer_source = "-17"
    integer_token, integer_end = _make_scanner(
        decoder, integer_source
    )(integer_source, 0)

    fraction_source = "1.25"
    fraction_token, fraction_end = _make_scanner(
        decoder, fraction_source
    )(fraction_source, 0)

    exponent_source = "2e3"
    exponent_token, exponent_end = _make_scanner(
        decoder, exponent_source
    )(exponent_source, 0)

    combined_source = "3.5e-2"
    combined_token, combined_end = _make_scanner(
        decoder, combined_source
    )(combined_source, 0)

    assert integer_calls == ["-17"]
    assert float_calls == ["1.25", "2e3", "3.5e-2"]
    assert integer_token.value == ("integer", "-17")
    assert fraction_token.value == ("float", "1.25")
    assert exponent_token.value == ("float", "2e3")
    assert combined_token.value == ("float", "3.5e-2")
    assert integer_end == len(integer_source)
    assert fraction_end == len(fraction_source)
    assert exponent_end == len(exponent_source)
    assert combined_end == len(combined_source)
    assert decoder.memo == {}


@pytest.mark.parametrize("source", ["", "x", "nul", "tru", "fals"])
def test_make_scanner_raises_stop_iteration_for_missing_or_invalid_value(source):
    decoder = json.JSONDecoder()
    decoder.memo["stale"] = object()
    scanner = _make_scanner(decoder, source)

    with pytest.raises(StopIteration) as exc_info:
        scanner(source, 0)

    assert exc_info.value.value == 0
    assert decoder.memo == {}


def test_make_scanner_clears_memo_after_successful_scan():
    source = '"value"'
    decoder = json.JSONDecoder()
    decoder.memo["stale"] = "entry"
    scanner = _make_scanner(decoder, source)

    token, end = scanner(source, 0)

    assert token.value == "value"
    assert end == len(source)
    assert decoder.memo == {}
