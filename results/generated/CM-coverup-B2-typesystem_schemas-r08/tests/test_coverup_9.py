# file: project/typesystem/schemas.py:175-182
# asked: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}
# gained: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}

import pytest

from typesystem import String
from typesystem.schemas import Schema


class ExampleSchema(Schema):
    name = String()


def test_getitem_returns_serialized_value():
    schema = ExampleSchema(name="hello")
    # Covers lines 176-178 and 182: key present in fields and as attribute.
    assert schema["name"] == "hello"


def test_getitem_raises_keyerror_for_unknown_key():
    schema = ExampleSchema(name="hello")
    # Covers lines 179-180: KeyError raised from fields lookup.
    with pytest.raises(KeyError) as exc_info:
        schema["missing"]
    assert exc_info.value.args[0] == "missing"


def test_getitem_raises_keyerror_when_attribute_missing():
    schema = ExampleSchema(name="hello")
    # Remove the instance attribute so getattr fails while the field exists.
    del schema.name
    # Covers lines 179-180 via the AttributeError branch.
    with pytest.raises(KeyError) as exc_info:
        schema["name"]
    assert exc_info.value.args[0] == "name"
