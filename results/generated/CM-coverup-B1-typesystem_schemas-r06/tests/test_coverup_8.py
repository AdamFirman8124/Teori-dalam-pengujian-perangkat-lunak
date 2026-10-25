# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_mapping_operations():
    definitions = SchemaDefinitions({"existing": 1})

    assert definitions["existing"] == 1
    assert list(iter(definitions)) == ["existing"]
    assert len(definitions) == 1

    definitions["added"] = 2
    assert definitions["added"] == 2
    assert len(definitions) == 2

    del definitions["added"]
    assert len(definitions) == 1
    assert "added" not in definitions


def test_schema_definitions_rejects_duplicate_keys():
    definitions = SchemaDefinitions({"duplicate": "original"})

    with pytest.raises(
        AssertionError,
        match=r"^Definition for \{key!r\} has already been set\.$",
    ):
        definitions["duplicate"] = "replacement"

    assert definitions["duplicate"] == "original"
    assert len(definitions) == 1
