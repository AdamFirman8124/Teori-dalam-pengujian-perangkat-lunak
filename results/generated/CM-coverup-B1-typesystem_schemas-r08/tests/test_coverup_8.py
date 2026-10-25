# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest
from typesystem.schemas import SchemaDefinitions


def test_getitem_returns_set_value():
    d = SchemaDefinitions()
    d._definitions["a"] = 1
    assert d["a"] == 1
    assert d.__getitem__("a") == 1


def test_getitem_missing_key_raises_keyerror():
    d = SchemaDefinitions()
    with pytest.raises(KeyError):
        _ = d["missing"]


def test_iter_yields_keys():
    d = SchemaDefinitions([("a", 1), ("b", 2)])
    assert set(iter(d)) == {"a", "b"}
    assert list(d.__iter__()) == ["a", "b"]
    assert list(d.keys()) == ["a", "b"]


def test_len_returns_count():
    d = SchemaDefinitions()
    assert len(d) == 0
    assert d.__len__() == 0
    d._definitions["x"] = 10
    assert len(d) == 1
    d._definitions["y"] = 20
    assert len(d) == 2


def test_setitem_sets_new_key():
    d = SchemaDefinitions()
    d["new"] = 123
    assert d._definitions["new"] == 123
    assert d["new"] == 123
    assert len(d) == 1


def test_setitem_duplicate_key_raises_assertion_error():
    d = SchemaDefinitions()
    d["dup"] = 1
    assert d["dup"] == 1
    with pytest.raises(AssertionError) as exc_info:
        d["dup"] = 2
    assert str(exc_info.value) == r"Definition for {key!r} has already been set."
    # postcondition: original value unchanged
    assert d["dup"] == 1
    assert len(d) == 1


def test_delitem_removes_key():
    d = SchemaDefinitions({"a": 1, "b": 2})
    assert len(d) == 2
    del d["a"]
    assert "a" not in d._definitions
    assert "a" not in d
    assert len(d) == 1
    assert d["b"] == 2


def test_delitem_missing_key_raises_keyerror():
    d = SchemaDefinitions({"a": 1})
    with pytest.raises(KeyError):
        del d["nope"]
    # postcondition: existing data unchanged
    assert d["a"] == 1
    assert len(d) == 1
