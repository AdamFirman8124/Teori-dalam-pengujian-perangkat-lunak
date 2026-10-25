# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import re

import pytest

from pysnooper import utils
from pysnooper.utils import DEFAULT_REPR_RE, normalize_repr


def test_normalize_repr_removes_memory_address():
    item_repr = "<Foo object at 0x7f8b2c3d4e50>"
    result = normalize_repr(item_repr)
    assert result == "<Foo object>"
    assert ' at 0x' not in result


def test_normalize_repr_no_memory_address():
    item_repr = "<Foo object>"
    result = normalize_repr(item_repr)
    assert result == "<Foo object>"


def test_normalize_repr_multiple_addresses():
    item_repr = "<A at 0xdeadbeef> and <B at 0xCAFEBABE>"
    result = normalize_repr(item_repr)
    assert result == "<A> and <B>"


def test_normalize_repr_short_hex_not_removed():
    # The regex requires at least 4 hex digits, so 3 digits stay untouched
    item_repr = "<Foo at 0xabc>"
    result = normalize_repr(item_repr)
    assert result == "<Foo at 0xabc>"


def test_normalize_repr_empty_string():
    assert normalize_repr("") == ""


def test_normalize_repr_uses_default_regex(monkeypatch):
    # Verify line 64 uses the module-level DEFAULT_REPR_RE
    sentinel = re.compile('XX_SENTINEL_XX')
    monkeypatch.setattr(utils, 'DEFAULT_REPR_RE', sentinel)
    result = normalize_repr("XX_SENTINEL_XX at 0x1234")
    assert result == " at 0x1234"
    monkeypatch.undo()
    assert utils.DEFAULT_REPR_RE is DEFAULT_REPR_RE
