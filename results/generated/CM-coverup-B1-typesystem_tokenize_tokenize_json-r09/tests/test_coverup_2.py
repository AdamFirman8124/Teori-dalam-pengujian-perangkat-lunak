# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import pytest
from typesystem.tokenize.tokenize_json import _TokenizingDecoder, _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def _make(text):
    decoder = _TokenizingDecoder(content=text)
    scanner = _make_scanner(decoder, text)
    return decoder, scanner


def test_scan_string():
    text = '"hello"'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"
    assert end == len(text)
    assert token.start.char_index == 0
    assert token.end.char_index == end - 1
    assert token._content == text
    assert decoder.memo == {}


def test_scan_object():
    text = '{"a": 1}'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, DictToken)
    assert end == len(text)
    assert token.start.char_index == 0
    assert token.end.char_index == end - 1
    assert token._content == text
    raw = token.value
    assert "a" in raw
    inner = raw["a"]
    assert inner == 1 or getattr(inner, "value", None) == 1
    assert decoder.memo == {}


def test_scan_array():
    text = '[1, 2]'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, ListToken)
    assert end == len(text)
    assert token.start.char_index == 0
    assert token.end.char_index == end - 1
    assert token._content == text
    raw = list(token.value)
    assert len(raw) == 2
    assert (raw[0] == 1 or getattr(raw[0], "value", None) == 1)
    assert (raw[1] == 2 or getattr(raw[1], "value", None) == 2)
    assert decoder.memo == {}


def test_scan_null():
    text = 'null'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value is None
    assert end == 4
    assert token.start.char_index == 0
    assert token.end.char_index == 3
    assert decoder.memo == {}


def test_scan_true():
    text = 'true'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value is True
    assert end == 4
    assert token.start.char_index == 0
    assert token.end.char_index == 3
    assert decoder.memo == {}


def test_scan_false():
    text = 'false'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value is False
    assert end == 5
    assert token.start.char_index == 0
    assert token.end.char_index == 4
    assert decoder.memo == {}


def test_scan_integer_uses_parse_int(monkeypatch):
    text = '42'
    decoder = _TokenizingDecoder(content=text)
    seen = {}
    orig = decoder.parse_int
    def fake_parse_int(v):
        seen["v"] = v
        return orig(v)
    monkeypatch.setattr(decoder, "parse_int", fake_parse_int)
    scanner = _make_scanner(decoder, text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 42
    assert end == 2
    assert seen == {"v": "42"}
    assert decoder.memo == {}


def test_scan_negative_integer():
    text = '-7'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == -7
    assert end == len(text)
    assert decoder.memo == {}


def test_scan_float_frac_uses_parse_float(monkeypatch):
    text = '3.14'
    decoder = _TokenizingDecoder(content=text)
    seen = {}
    orig = decoder.parse_float
    def fake_parse_float(v):
        seen["v"] = v
        return orig(v)
    monkeypatch.setattr(decoder, "parse_float", fake_parse_float)
    scanner = _make_scanner(decoder, text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == pytest.approx(3.14)
    assert end == len(text)
    assert seen == {"v": "3.14"}
    assert decoder.memo == {}


def test_scan_float_exp_only():
    text = '1e10'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == pytest.approx(1e10)
    assert end == len(text)
    assert decoder.memo == {}


def test_scan_float_frac_and_exp():
    text = '1.5E-3'
    decoder, scanner = _make(text)
    token, end = scanner(text, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == pytest.approx(0.0015)
    assert end == len(text)
    assert decoder.memo == {}


def test_scan_empty_raises_stop_iteration():
    text = ''
    decoder, scanner = _make(text)
    with pytest.raises(StopIteration):
        scanner(text, 0)
    assert decoder.memo == {}


def test_scan_index_out_of_range_raises_stop_iteration():
    text = 'true'
    decoder, scanner = _make(text)
    with pytest.raises(StopIteration):
        scanner(text, 100)
    assert decoder.memo == {}


def test_scan_invalid_char_raises_stop_iteration():
    text = '!'
    decoder, scanner = _make(text)
    with pytest.raises(StopIteration):
        scanner(text, 0)
    assert decoder.memo == {}


def test_scan_truncated_null_raises():
    text = 'nul'
    decoder, scanner = _make(text)
    with pytest.raises(StopIteration):
        scanner(text, 0)
    assert decoder.memo == {}


def test_scan_truncated_true_raises():
    text = 'tru'
    decoder, scanner = _make(text)
    with pytest.raises(StopIteration):
        scanner(text, 0)
    assert decoder.memo == {}


def test_scan_truncated_false_raises():
    text = 'fals'
    decoder, scanner = _make(text)
    with pytest.raises(StopIteration):
        scanner(text, 0)
    assert decoder.memo == {}


def test_scan_single_n_t_f_letters_raise():
    for text in ["n", "t", "f", "x"]:
        decoder, scanner = _make(text)
        with pytest.raises(StopIteration):
            scanner(text, 0)
        assert decoder.memo == {}


def test_memo_cleared_on_success():
    text = '"abc"'
    decoder, scanner = _make(text)
    decoder.memo["pollution"] = "value"
    token, end = scanner(text, 0)
    assert token.value == "abc"
    assert decoder.memo == {}


def test_memo_cleared_on_failure():
    text = '!'
    decoder, scanner = _make(text)
    decoder.memo["pollution"] = "value"
    with pytest.raises(StopIteration):
        scanner(text, 0)
    assert decoder.memo == {}


def test_scan_with_offset():
    text = '  true'
    decoder, scanner = _make(text)
    token, end = scanner(text, 2)
    assert isinstance(token, ScalarToken)
    assert token.value is True
    assert end == 6
    assert token.start.char_index == 2
    assert token.end.char_index == 5
    assert decoder.memo == {}
