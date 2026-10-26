# file: project/typesystem/tokenize/tokenize_json.py:20-95
# asked: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}
# gained: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}

import pytest
from json.decoder import JSONDecodeError
from typesystem.tokenize.tokenize_json import _TokenizingJSONObject


def _int_scan(s, idx):
    return int(s[idx]), idx + 1


def _stop_scan(s, idx):
    raise StopIteration(idx)


def _never_scan(s, idx):
    raise AssertionError("scan_once should not be called")


def test_empty_object_no_ws():
    s = "{}"
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _never_scan, memo, s)
    assert d == {}
    assert end == 2
    assert memo == {}


def test_empty_object_with_ws():
    s = "{ }"
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _never_scan, memo, s)
    assert d == {}
    assert end == 3
    assert memo == {}


def test_empty_object_multi_ws():
    s = "{  \n\t }"
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _never_scan, memo, s)
    assert d == {}
    assert end == len(s)
    assert memo == {}


def test_invalid_prop_no_ws():
    s = "{x}"
    with pytest.raises(JSONDecodeError):
        _TokenizingJSONObject((s, 1), True, _never_scan, {}, s)


def test_invalid_prop_with_ws():
    s = "{ x}"
    with pytest.raises(JSONDecodeError):
        _TokenizingJSONObject((s, 1), True, _never_scan, {}, s)


def test_single_pair_no_ws():
    s = '{"a":1}'
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _int_scan, memo, s)
    assert len(d) == 1
    assert list(d.values())[0] == 1
    assert end == len(s)
    assert "a" in memo


def test_leading_ws_before_key():
    s = '{ "a":1}'
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _int_scan, memo, s)
    assert len(d) == 1
    assert list(d.values())[0] == 1
    assert end == len(s)
    assert "a" in memo


def test_colon_with_ws():
    s = '{"a" :1}'
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _int_scan, memo, s)
    assert len(d) == 1
    assert list(d.values())[0] == 1
    assert end == len(s)


def test_colon_missing_raises():
    s = '{"a" 1}'
    with pytest.raises(JSONDecodeError, match="Expecting ':' delimiter"):
        _TokenizingJSONObject((s, 1), True, _never_scan, {}, s)


def test_single_space_after_colon():
    s = '{"a": 1}'
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _int_scan, memo, s)
    assert len(d) == 1
    assert list(d.values())[0] == 1
    assert end == len(s)


def test_multi_space_after_colon():
    s = '{"a":  1}'
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _int_scan, memo, s)
    assert len(d) == 1
    assert list(d.values())[0] == 1
    assert end == len(s)


def test_truncated_after_colon():
    s = '{"a":'
    with pytest.raises(JSONDecodeError, match="Expecting value"):
        _TokenizingJSONObject((s, 1), True, _stop_scan, {}, s)


def test_space_then_truncated_after_colon():
    s = '{"a": '
    with pytest.raises(JSONDecodeError, match="Expecting value"):
        _TokenizingJSONObject((s, 1), True, _stop_scan, {}, s)


def test_stop_iteration_maps_to_expecting_value():
    s = '{"a":1}'
    with pytest.raises(JSONDecodeError, match="Expecting value"):
        _TokenizingJSONObject((s, 1), True, _stop_scan, {}, s)


def test_after_value_with_ws():
    s = '{"a":1 }'
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _int_scan, memo, s)
    assert len(d) == 1
    assert list(d.values())[0] == 1
    assert end == len(s)


def test_after_value_truncated_raises_comma():
    s = '{"a":1'
    with pytest.raises(JSONDecodeError, match="Expecting ',' delimiter"):
        _TokenizingJSONObject((s, 1), True, _int_scan, {}, s)


def test_invalid_comma_delimiter():
    s = '{"a":1;}'
    with pytest.raises(JSONDecodeError, match="Expecting ',' delimiter"):
        _TokenizingJSONObject((s, 1), True, _int_scan, {}, s)


def test_two_pairs():
    s = '{"a":1,"b":2}'
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _int_scan, memo, s)
    assert len(d) == 2
    assert sorted(d.values()) == [1, 2]
    assert end == len(s)
    assert "a" in memo
    assert "b" in memo


def test_two_pairs_ws_after_comma():
    s = '{"a":1, "b":2}'
    memo = {}
    d, end = _TokenizingJSONObject((s, 1), True, _int_scan, memo, s)
    assert len(d) == 2
    assert sorted(d.values()) == [1, 2]
    assert end == len(s)


def test_invalid_key_after_comma_brace():
    s = '{"a":1,}'
    with pytest.raises(JSONDecodeError, match="Expecting property name"):
        _TokenizingJSONObject((s, 1), True, _int_scan, {}, s)


def test_invalid_key_after_comma_digit():
    s = '{"a":1,2}'
    with pytest.raises(JSONDecodeError, match="Expecting property name"):
        _TokenizingJSONObject((s, 1), True, _int_scan, {}, s)
