# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_getitem():
    definitions = SchemaDefinitions({"a": 1, "b": 2}, c=3)

    assert definitions["a"] == 1
    assert definitions["b"] == 2
    assert definitions["c"] == 3

    with pytest.raises(KeyError):
        definitions["missing"]


def test_schema_definitions_iter():
    definitions = SchemaDefinitions({"a": 1, "b": 2}, c=3)

    assert list(iter(definitions)) == ["a", "b", "c"]
    assert list(definitions) == ["a", "b", "c"]
    assert set(definitions) == {"a", "b", "c"}


def test_schema_definitions_len():
    empty = SchemaDefinitions()
    assert len(empty) == 0

    definitions = SchemaDefinitions({"a": 1, "b": 2}, c=3)
    assert len(definitions) == 3


def test_schema_definitions_setitem_new_key():
    definitions = SchemaDefinitions()

    definitions["a"] = 1
    assert definitions["a"] == 1
    assert len(definitions) == 1

    definitions["b"] = 2
    assert definitions["b"] == 2
    assert len(definitions) == 2
    assert list(definitions) == ["a", "b"]


def test_schema_definitions_setitem_duplicate_key_raises():
    definitions = SchemaDefinitions({"a": 1})

    with pytest.raises(AssertionError) as exc_info:
        definitions["a"] = 99

    assert "has already been set" in str(exc_info.value)
    # Failed assignment must not overwrite the existing definition.
    assert definitions["a"] == 1
    assert len(definitions) == 1


def test_schema_definitions_delitem():
    definitions = SchemaDefinitions({"a": 1, "b": 2})

    del definitions["a"]
    assert len(definitions) == 1
    assert list(definitions) == ["b"]
    with pytest.raises(KeyError):
        definitions["a"]

    del definitions["b"]
    assert len(definitions) == 0
    assert list(definitions) == []

    with pytest.raises(KeyError):
        del definitions["b"]
