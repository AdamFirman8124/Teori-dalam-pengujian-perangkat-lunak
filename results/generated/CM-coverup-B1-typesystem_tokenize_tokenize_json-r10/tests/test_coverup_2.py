# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import pytest
from json.decoder import JSONDecoder

from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def _scanner_for(content, **decoder_kwargs):
    ctx = JSONDecoder(**decoder_kwargs)
    scanner = _make_scanner(ctx, content)
    return scanner, ctx


def test_scan_string():
    content = '"hello"'
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value == "hello"
    assert end == len(content)
    assert ctx.memo == {}


def test_scan_string_with_offset():
    content = '"a" "b"'
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 4)
    assert isinstance(tok, ScalarToken)
    assert tok.value == "b"
    assert end == len(content)
    assert ctx.memo == {}


def test_scan_object():
    content = '{"a": 1}'
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, DictToken)
    assert isinstance(tok.value, dict)
    assert end == len(content)
    assert ctx.memo == {}


def test_scan_array():
    content = '[1, 2, 3]'
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ListToken)
    assert isinstance(tok.value, list)
    assert len(tok.value) == 3
    assert end == len(content)
    assert ctx.memo == {}


def test_scan_null():
    content = "null"
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value is None
    assert end == 4
    assert ctx.memo == {}


def test_scan_true():
    content = "true"
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value is True
    assert end == 4
    assert ctx.memo == {}


def test_scan_false():
    content = "false"
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value is False
    assert end == 5
    assert ctx.memo == {}


def test_scan_integer(monkeypatch):
    ctx = JSONDecoder()
    monkeypatch.setattr(ctx, "parse_int", lambda x: 999)
    content = "123"
    scanner = _make_scanner(ctx, content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value == 999
    assert end == 3
    assert ctx.memo == {}


def test_scan_integer_default():
    content = "-123"
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value == -123
    assert end == len(content)


def test_scan_float_frac_only():
    content = "12.5"
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value == pytest.approx(12.5)
    assert end == len(content)


def test_scan_float_exp_only(monkeypatch):
    ctx = JSONDecoder()
    seen = {}
    orig = ctx.parse_float

    def spy(x):
        seen["arg"] = x
        return orig(x)

    monkeypatch.setattr(ctx, "parse_float", spy)
    content = "1e10"
    scanner = _make_scanner(ctx, content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value == pytest.approx(1e10)
    assert seen["arg"] == "1e10"
    assert end == len(content)


def test_scan_float_frac_and_exp():
    content = "-1.5E-2"
    scanner, ctx = _scanner_for(content)
    tok, end = scanner(content, 0)
    assert isinstance(tok, ScalarToken)
    assert tok.value == pytest.approx(-1.5e-2)
    assert end == len(content)


def test_scan_index_error_empty():
    content = ""
    scanner, ctx = _scanner_for(content)
    ctx.memo["pollution"] = "x"
    with pytest.raises(StopIteration) as exc:
        scanner(content, 0)
    assert exc.value.value == 0
    assert ctx.memo == {}


def test_scan_index_error_out_of_range():
    content = "true"
    scanner, ctx = _scanner_for(content)
    with pytest.raises(StopIteration) as exc:
        scanner(content, 10)
    assert exc.value.value == 10
    assert ctx.memo == {}


def test_scan_invalid_char():
    content = "!"
    scanner, ctx = _scanner_for(content)
    ctx.memo["k"] = "v"
    with pytest.raises(StopIteration) as exc:
        scanner(content, 0)
    assert exc.value.value == 0
    assert ctx.memo == {}


def test_scan_n_prefix_mismatch():
    content = "nul"
    scanner, ctx = _scanner_for(content)
    with pytest.raises(StopIteration):
        scanner(content, 0)
    assert ctx.memo == {}


def test_scan_t_prefix_mismatch():
    content = "tru"
    scanner, ctx = _scanner_for(content)
    with pytest.raises(StopIteration):
        scanner(content, 0)
    assert ctx.memo == {}


def test_scan_f_prefix_mismatch():
    content = "fals"
    scanner, ctx = _scanner_for(content)
    with pytest.raises(StopIteration):
        scanner(content, 0)
    assert ctx.memo == {}


def test_scan_memo_cleared_on_success():
    content = '"hi"'
    scanner, ctx = _scanner_for(content)
    ctx.memo["a"] = "b"
    tok, end = scanner(content, 0)
    assert tok.value == "hi"
    assert ctx.memo == {}


def test_scan_memo_cleared_on_failure():
    content = "@"
    scanner, ctx = _scanner_for(content)
    ctx.memo["a"] = "b"
    with pytest.raises(StopIteration):
        scanner(content, 0)
    assert ctx.memo == {}
