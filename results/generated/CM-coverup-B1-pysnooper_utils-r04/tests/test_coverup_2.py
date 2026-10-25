# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

import pytest

from pysnooper.utils import get_shortish_repr


class _BadRepr:
    def __repr__(self):
        raise ValueError("boom")


class _NewlineRepr:
    def __repr__(self):
        return "line1\r\nline2\nline3"


def test_get_shortish_repr_uses_custom_repr_by_type():
    result = get_shortish_repr(42, custom_repr=((int, lambda item: "INT"),))
    assert result == "INT"


def test_get_shortish_repr_uses_custom_repr_by_callable_condition():
    result = get_shortish_repr(
        "hello", custom_repr=((lambda item: isinstance(item, str), lambda item: "STR"),)
    )
    assert result == "STR"


def test_get_shortish_repr_falls_back_to_builtin_repr():
    result = get_shortish_repr(42)
    assert result == "42"


def test_get_shortish_repr_returns_repr_failed_on_exception():
    result = get_shortish_repr(_BadRepr())
    assert result == "REPR FAILED"


def test_get_shortish_repr_strips_carriage_returns_and_newlines():
    result = get_shortish_repr(_NewlineRepr())
    assert result == "line1line2line3"
    assert "\r" not in result
    assert "\n" not in result


def test_get_shortish_repr_normalize_removes_memory_address():
    obj = object()
    raw = repr(obj)
    assert "0x" in raw  # sanity check that normalization has something to do

    result = get_shortish_repr(obj, normalize=True)
    assert "0x" not in result
    assert result == "<object object>"


def test_get_shortish_repr_without_normalize_keeps_memory_address():
    obj = object()
    result = get_shortish_repr(obj, normalize=False)
    assert result == repr(obj)
    assert "0x" in result


def test_get_shortish_repr_truncates_to_max_length():
    # repr of the string includes quotes: 'abcdefghijklmnopqrstuvwxyz'
    result = get_shortish_repr("abcdefghijklmnopqrstuvwxyz", max_length=10)
    assert len(result) == 10
    assert "..." in result
    assert result == "'ab...xyz'"


def test_get_shortish_repr_does_not_truncate_short_string():
    result = get_shortish_repr("abc", max_length=10)
    assert result == "'abc'"


def test_get_shortish_repr_max_length_none_keeps_full_string():
    long_string = "x" * 100
    result = get_shortish_repr(long_string, max_length=None)
    assert result == repr(long_string)


def test_get_shortish_repr_max_length_zero_skips_truncation():
    long_string = "x" * 100
    result = get_shortish_repr(long_string, max_length=0)
    assert result == repr(long_string)


def test_get_shortish_repr_normalize_and_truncate_together():
    obj = object()
    result = get_shortish_repr(obj, max_length=10, normalize=True)
    # normalized repr is "<object object>"; truncate(10) -> "<ob" + "..." + "ect>"
    assert len(result) == 10
    assert "0x" not in result
    assert result == "<ob...ect>"
