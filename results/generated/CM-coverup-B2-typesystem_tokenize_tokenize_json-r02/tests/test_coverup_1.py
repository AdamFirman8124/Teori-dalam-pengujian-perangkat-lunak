# file: project/typesystem/tokenize/tokenize_json.py:20-95
# asked: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}
# gained: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}

import pytest
from json.decoder import JSONDecodeError
from typesystem.tokenize.tokenize_json import _TokenizingJSONObject
from typesystem.tokenize.tokens import ScalarToken


def _make_single_char_scanner(content, store):
    def _scan(s, idx):
        tok = ScalarToken(s[idx], idx, idx + 1, content)
        store.append(tok)
        return tok, idx + 1
    return _scan


def _raising_scan(s, idx):
    raise StopIteration(idx)


def test_empty_object_no_whitespace():
    s = "{}"
    memo = {}
    result, end = _TokenizingJSONObject((s, 1), True, _raising_scan, memo, s)
    assert result == {}
    assert end == 2


def test_empty_object_with_whitespace():
    s = "{ }"
    memo = {}
    result, end = _TokenizingJSONObject((s, 1), True, _raising_scan, memo, s)
    assert result == {}
    assert end == 3


def test_invalid_property_name_no_whitespace():
    s = "{x}"
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, _raising_scan, {}, s)
    assert "Expecting property name enclosed in double quotes" in str(exc.value)


def test_invalid_property_name_after_whitespace():
    s = "{   x}"
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, _raising_scan, {}, s)
    assert "Expecting property name enclosed in double quotes" in str(exc.value)


def test_single_pair_fast_colon_no_whitespace():
    s = '{"a":1}'
    store = []
    fake = _make_single_char_scanner(s, store)
    result, end = _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert end == len(s) == 7
    assert len(result) == 1
    assert list(result.values())[0] is store[0]
    assert all(isinstance(k, ScalarToken) for k in result)


def test_single_pair_whitespace_before_colon_single_space_after():
    s = '{"a" : 1}'
    store = []
    fake = _make_single_char_scanner(s, store)
    result, end = _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert end == len(s) == 9
    assert len(result) == 1
    assert list(result.values())[0] is store[0]


def test_single_pair_double_space_after_colon():
    s = '{"a":  1}'
    store = []
    fake = _make_single_char_scanner(s, store)
    result, end = _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert end == len(s) == 9
    assert len(result) == 1
    assert list(result.values())[0] is store[0]


def test_missing_colon_raises():
    s = '{"a" 1}'
    store = []
    fake = _make_single_char_scanner(s, store)
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert "Expecting ':' delimiter" in str(exc.value)


def test_colon_at_end_indexerror_then_expecting_value():
    s = '{"a":'
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, _raising_scan, {}, s)
    assert "Expecting value" in str(exc.value)


def test_expecting_value_raises():
    s = '{"a":}'
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, _raising_scan, {}, s)
    assert "Expecting value" in str(exc.value)


def test_multi_pair_with_comma_and_whitespace():
    s = '{"a":1, "b":2}'
    store = []
    fake = _make_single_char_scanner(s, store)
    result, end = _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert end == len(s) == 14
    assert len(result) == 2
    assert len(store) == 2
    assert set(result.values()) == set(store)


def test_expecting_comma_delimiter_raises():
    s = '{"a":1;}'
    store = []
    fake = _make_single_char_scanner(s, store)
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert "Expecting ',' delimiter" in str(exc.value)


def test_truncated_object_indexerror_after_value_raises():
    s = '{"a":1'
    store = []
    fake = _make_single_char_scanner(s, store)
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert "Expecting ',' delimiter" in str(exc.value)


def test_missing_property_name_after_comma_raises():
    s = '{"a":1,}'
    store = []
    fake = _make_single_char_scanner(s, store)
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert "Expecting property name enclosed in double quotes" in str(exc.value)


def test_whitespace_after_value_before_close():
    s = '{"a":1 }'
    store = []
    fake = _make_single_char_scanner(s, store)
    result, end = _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert end == len(s) == 8
    assert len(result) == 1
    assert list(result.values())[0] is store[0]


def test_whitespace_after_value_before_comma():
    s = '{"a":1 , "b":2}'
    store = []
    fake = _make_single_char_scanner(s, store)
    result, end = _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert end == len(s) == 15
    assert len(result) == 2
    assert len(store) == 2


def test_whitespace_after_value_at_end_raises():
    s = '{"a":1 '
    store = []
    fake = _make_single_char_scanner(s, store)
    with pytest.raises(JSONDecodeError) as exc:
        _TokenizingJSONObject((s, 1), True, fake, {}, s)
    assert "Expecting ',' delimiter" in str(exc.value)
