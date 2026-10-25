# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_getitem():
    definitions = SchemaDefinitions({"key": "value"})
    assert definitions["key"] == "value"


def test_schema_definitions_iter():
    definitions = SchemaDefinitions({"a": 1, "b": 2})
    assert sorted(iter(definitions)) == ["a", "b"]


def test_schema_definitions_len():
    definitions = SchemaDefinitions({"a": 1, "b": 2})
    assert len(definitions) == 2


def test_schema_definitions_setitem():
    definitions = SchemaDefinitions()
    definitions["key"] = "value"
    assert definitions["key"] == "value"
    assert len(definitions) == 1


def test_schema_definitions_setitem_duplicate_raises():
    definitions = SchemaDefinitions({"key": "value"})
    with pytest.raises(AssertionError):
        definitions["key"] = "other"
    # The original value must be untouched after the failed set.
    assert definitions["key"] == "value"


def test_schema_definitions_delitem():
    definitions = SchemaDefinitions({"key": "value"})
    del definitions["key"]
    assert len(definitions) == 0
    assert "key" not in definitions
    with pytest.raises(KeyError):
        definitions["key"]


def test_schema_definitions_mutable_mapping_protocol():
    definitions = SchemaDefinitions()
    definitions["a"] = 1
    definitions["b"] = 2
    assert dict(definitions) == {"a": 1, "b": 2}
    definitions.pop("a")
    assert list(definitions) == ["b"]
    definitions.clear()
    assert len(definitions) == 0
