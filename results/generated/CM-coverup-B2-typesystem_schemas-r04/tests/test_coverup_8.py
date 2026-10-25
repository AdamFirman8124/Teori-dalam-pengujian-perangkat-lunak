# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_mapping_operations():
    definitions = SchemaDefinitions({"alpha": 1})

    assert definitions["alpha"] == 1
    assert list(definitions) == ["alpha"]
    assert len(definitions) == 1

    definitions["beta"] = 2
    assert definitions["beta"] == 2
    assert len(definitions) == 2

    del definitions["alpha"]
    assert list(definitions) == ["beta"]
    assert len(definitions) == 1

    with pytest.raises(KeyError):
        definitions["alpha"]


def test_schema_definitions_rejects_duplicate_keys():
    definitions = SchemaDefinitions(existing="original")

    with pytest.raises(AssertionError):
        definitions["existing"] = "replacement"

    assert definitions["existing"] == "original"
    assert len(definitions) == 1


def test_schema_definitions_delete_missing_key_raises_key_error():
    definitions = SchemaDefinitions()

    with pytest.raises(KeyError):
        del definitions["missing"]

    assert len(definitions) == 0
