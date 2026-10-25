# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_mapping_operations():
    value = object()
    definitions = SchemaDefinitions({"example": value})

    assert definitions["example"] is value
    assert list(iter(definitions)) == ["example"]
    assert len(definitions) == 1


def test_schema_definitions_set_and_delete():
    definitions = SchemaDefinitions()
    value = object()

    definitions["example"] = value

    assert definitions["example"] is value
    assert len(definitions) == 1

    del definitions["example"]

    assert len(definitions) == 0
    assert list(definitions) == []


def test_schema_definitions_rejects_redefinition():
    original = object()
    replacement = object()
    definitions = SchemaDefinitions({"example": original})

    with pytest.raises(AssertionError) as exc_info:
        definitions["example"] = replacement

    assert exc_info.value.args == (
        "Definition for {key!r} has already been set.",
    )
    assert definitions["example"] is original
    assert len(definitions) == 1
