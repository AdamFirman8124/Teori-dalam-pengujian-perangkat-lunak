# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import re

import pytest

import pysnooper.utils as utils_module


def test_get_shortish_repr_normalize_strips_address():
    class WithAddress:
        def __repr__(self):
            return "<WithAddress at 0x1234ABCD>"

    obj = WithAddress()
    raw = repr(obj)
    assert "at 0x" in raw

    result = utils_module.get_shortish_repr(obj, normalize=True)

    assert result == "<WithAddress>"
    assert "at 0x" not in result
    assert "0x1234ABCD" not in result
    # postcondition: equals regex substitution applied by normalize_repr
    assert result == utils_module.DEFAULT_REPR_RE.sub("", raw)


def test_get_shortish_repr_normalize_leaves_plain_repr():
    class Plain:
        def __repr__(self):
            return "<Plain>"

    result = utils_module.get_shortish_repr(Plain(), normalize=True)
    assert result == "<Plain>"


def test_get_shortish_repr_normalize_true_on_default_object_repr():
    obj = object()
    raw = repr(obj)
    assert "at 0x" in raw
    result = utils_module.get_shortish_repr(obj, normalize=True)
    assert "at 0x" not in result
    assert result == utils_module.DEFAULT_REPR_RE.sub("", raw)
    assert result == "<object object>"


def test_get_shortish_repr_normalize_false_preserves_address():
    class WithAddress:
        def __repr__(self):
            return "<WithAddress at 0x1234ABCD>"

    result = utils_module.get_shortish_repr(WithAddress(), normalize=False)
    assert result == "<WithAddress at 0x1234ABCD>"
    assert "at 0x" in result


def test_normalize_repr_direct_if_exposed():
    func = getattr(utils_module, "normalize_repr", None)
    if func is None:
        pytest.skip("normalize_repr not exposed at module level")
    assert func("<object object at 0x7f8b8c0d5e00>") == "<object object>"
    assert func("<object object>") == "<object object>"
    assert func("hello") == "hello"
    assert func("") == ""
    # regex requires at least 4 hex digits
    assert func("foo at 0x12") == "foo at 0x12"
    assert func("<A at 0xABCDEF> and <B at 0x123456>") == "<A> and <B>"
