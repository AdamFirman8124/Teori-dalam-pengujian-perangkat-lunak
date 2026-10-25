# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_mapping_operations():
    definitions = SchemaDefinitions({"existing": 1})

    assert definitions["existing"] == 1
    assert list(definitions) == ["existing"]
    assert len(definitions) == 1

    definitions["new"] = 2

    assert definitions["new"] == 2
    assert len(definitions) == 2

    del definitions["existing"]

    assert list(definitions) == ["new"]
    assert len(definitions) == 1
    with pytest.raises(KeyError):
        definitions["existing"]


def test_schema_definitions_rejects_duplicate_keys():
    definitions = SchemaDefinitions(existing=1)

    with pytest.raises(AssertionError) as exc_info:
        definitions["existing"] = 2

    assert str(exc_info.value) == "Definition for {key!r} has already been set."
    assert definitions["existing"] == 1
    assert len(definitions) == 1


def test_schema_definitions_delete_missing_key_raises_key_error():
    definitions = SchemaDefinitions()

    with pytest.raises(KeyError):
        del definitions["missing"]

    assert len(definitions) == 0
