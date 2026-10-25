# file: project/typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import json

import pytest

from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def _context_and_scanner(content):
    context = json.JSONDecoder(strict=True)
    if not hasattr(context, "memo"):
        context.memo = {}
    scanner = _make_scanner(context, content)
    return context, scanner


def test_scan_string_token():
    content = '"hello"'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"
    assert end == len(content)
    assert end - 1 == 6


def test_scan_object_token():
    content = '{"a": 1}'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1}
    assert end == len(content)


def test_scan_empty_object_token():
    content = '{}'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, DictToken)
    assert token.value == {}
    assert end == 2


def test_scan_array_token():
    content = '[1, 2]'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ListToken)
    assert token.value == [1, 2]
    assert end == len(content)


def test_scan_null_token():
    content = 'null'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value is None
    assert end == 4


def test_scan_true_token():
    content = 'true'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value is True
    assert end == 4


def test_scan_false_token():
    content = 'false'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value is False
    assert end == 5


def test_scan_integer_token():
    content = '42'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 42
    assert isinstance(token.value, int)
    assert end == 2


def test_scan_float_frac_token():
    content = '3.14'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == pytest.approx(3.14)
    assert isinstance(token.value, float)
    assert end == 4


def test_scan_float_exp_token():
    content = '1e10'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == pytest.approx(1e10)
    assert isinstance(token.value, float)
    assert end == 4


def test_scan_float_frac_and_exp_token():
    content = '1.5e2'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == pytest.approx(150.0)
    assert end == 5


def test_scan_negative_int_token():
    content = '-7'
    _, scanner = _context_and_scanner(content)
    token, end = scanner(content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == -7
    assert end == 2


def test_scan_index_error_raises_stop_iteration():
    content = ''
    _, scanner = _context_and_scanner(content)
    with pytest.raises(StopIteration) as excinfo:
        scanner(content, 0)
    assert excinfo.value.value == 0


def test_scan_index_past_end_raises_stop_iteration():
    content = 'null'
    _, scanner = _context_and_scanner(content)
    with pytest.raises(StopIteration) as excinfo:
        scanner(content, 10)
    assert excinfo.value.value == 10


def test_scan_invalid_char_raises_stop_iteration():
    content = '@'
    _, scanner = _context_and_scanner(content)
    with pytest.raises(StopIteration) as excinfo:
        scanner(content, 0)
    assert excinfo.value.value == 0


def test_scan_n_prefix_mismatch_raises():
    content = 'nul'
    _, scanner = _context_and_scanner(content)
    with pytest.raises(StopIteration):
        scanner(content, 0)


def test_scan_t_prefix_mismatch_raises():
    content = 'tru'
    _, scanner = _context_and_scanner(content)
    with pytest.raises(StopIteration):
        scanner(content, 0)


def test_scan_f_prefix_mismatch_raises():
    content = 'fals'
    _, scanner = _context_and_scanner(content)
    with pytest.raises(StopIteration):
        scanner(content, 0)


def test_memo_cleared_after_success():
    content = '{"a": 1}'
    context, scanner = _context_and_scanner(content)
    context.memo["pollution"] = "x"
    token, end = scanner(content, 0)
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1}
    assert context.memo == {}


def test_memo_cleared_after_failure():
    content = '@'
    context, scanner = _context_and_scanner(content)
    context.memo["pollution"] = "x"
    with pytest.raises(StopIteration):
        scanner(content, 0)
    assert context.memo == {}


def test_memo_cleared_after_string_scan():
    content = '"hi"'
    context, scanner = _context_and_scanner(content)
    context.memo["k"] = "v"
    token, end = scanner(content, 0)
    assert token.value == "hi"
    assert context.memo == {}
