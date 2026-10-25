# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_mapping_operations():
    definitions = SchemaDefinitions({"first": 1})

    assert definitions["first"] == 1
    assert list(definitions) == ["first"]
    assert len(definitions) == 1

    definitions["second"] = 2
    assert definitions["second"] == 2
    assert len(definitions) == 2

    del definitions["first"]
    assert list(definitions) == ["second"]
    assert len(definitions) == 1
    with pytest.raises(KeyError):
        definitions["first"]


def test_schema_definitions_rejects_duplicate_key():
    definitions = SchemaDefinitions(existing="original")

    with pytest.raises(AssertionError) as exc_info:
        definitions["existing"] = "replacement"

    assert str(exc_info.value) == "Definition for {key!r} has already been set."
    assert definitions["existing"] == "original"
    assert len(definitions) == 1
