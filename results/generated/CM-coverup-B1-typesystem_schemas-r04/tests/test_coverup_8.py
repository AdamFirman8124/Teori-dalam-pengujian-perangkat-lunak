# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_getitem():
    definitions = SchemaDefinitions({"a": 1})
    assert definitions["a"] == 1


def test_schema_definitions_iter_and_len():
    definitions = SchemaDefinitions({"a": 1, "b": 2})
    assert len(definitions) == 2
    assert sorted(iter(definitions)) == ["a", "b"]


def test_schema_definitions_setitem():
    definitions = SchemaDefinitions()
    definitions["a"] = 1
    assert definitions["a"] == 1
    assert len(definitions) == 1


def test_schema_definitions_setitem_duplicate_key():
    definitions = SchemaDefinitions()
    definitions["a"] = 1
    with pytest.raises(AssertionError) as exc_info:
        definitions["a"] = 2
    assert "has already been set" in str(exc_info.value)
    # The original value must be untouched.
    assert definitions["a"] == 1


def test_schema_definitions_delitem():
    definitions = SchemaDefinitions({"a": 1, "b": 2})
    del definitions["a"]
    assert "a" not in definitions
    assert len(definitions) == 1
    with pytest.raises(KeyError):
        definitions["a"]


def test_schema_definitions_mutable_mapping_protocol():
    definitions = SchemaDefinitions()
    definitions["a"] = 1
    # MutableMapping mixin methods exercise __getitem__/__iter__/__len__.
    assert "a" in definitions
    assert definitions.get("a") == 1
    assert definitions.get("missing") is None
    assert list(definitions.keys()) == ["a"]
    assert list(definitions.values()) == [1]
    assert list(definitions.items()) == [("a", 1)]
    assert definitions.pop("a") == 1
    assert len(definitions) == 0
    definitions["b"] = 2
    definitions.clear()
    assert len(definitions) == 0
