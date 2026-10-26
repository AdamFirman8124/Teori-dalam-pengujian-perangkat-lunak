# file: project/typesystem/schemas.py:9-29
# asked: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}
# gained: {"lines": [14, 17, 20, 23, 25, 29], "branches": []}

import pytest

from typesystem.schemas import SchemaDefinitions


def test_schema_definitions_mapping_protocol():
    definitions = SchemaDefinitions()

    # __len__ on a fresh instance
    assert len(definitions) == 0

    # __setitem__ (line 23, 25, 26)
    definitions["int"] = int
    definitions["str"] = str

    # __len__ after insertion
    assert len(definitions) == 2

    # __getitem__ (line 14)
    assert definitions["int"] is int
    assert definitions["str"] is str

    # __iter__ (line 17)
    assert list(iter(definitions)) == ["int", "str"]
    assert set(definitions) == {"int", "str"}

    # __delitem__ (line 29)
    del definitions["int"]
    assert len(definitions) == 1
    assert "int" not in definitions
    assert list(definitions) == ["str"]

    # __getitem__ raises KeyError for missing keys
    with pytest.raises(KeyError):
        definitions["int"]


def test_schema_definitions_setitem_duplicate_raises():
    definitions = SchemaDefinitions()
    definitions["field"] = int

    # __setitem__ assertion branch (line 25) for duplicate keys
    with pytest.raises(AssertionError) as excinfo:
        definitions["field"] = str

    # The message is a plain raw string, not formatted
    assert r"Definition for {key!r} has already been set." in str(excinfo.value)

    # Original value must be untouched after the failed set
    assert definitions["field"] is int
    assert len(definitions) == 1


def test_schema_definitions_init_with_args_and_kwargs():
    # __init__ delegates to dict(*args, **kwargs)
    definitions = SchemaDefinitions([("a", 1)], b=2)
    assert len(definitions) == 2
    assert definitions["a"] == 1
    assert definitions["b"] == 2
    assert set(definitions) == {"a", "b"}
