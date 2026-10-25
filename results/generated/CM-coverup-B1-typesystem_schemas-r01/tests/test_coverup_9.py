# file: project/typesystem/schemas.py:175-182
# asked: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}
# gained: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}

import pytest

from typesystem import String
from typesystem.schemas import Schema


class ExampleSchema(Schema):
    name = String()


def test_getitem_returns_serialized_value():
    schema = ExampleSchema(name="example")
    assert schema["name"] == "example"


def test_getitem_missing_key_raises_keyerror():
    schema = ExampleSchema(name="example")
    with pytest.raises(KeyError) as exc_info:
        schema["missing"]
    assert exc_info.value.args[0] == "missing"


def test_getitem_field_present_but_attribute_missing_raises_keyerror():
    schema = ExampleSchema(name="example")
    # Simulate an instance where the field exists in self.fields
    # but the corresponding attribute is missing, exercising the
    # AttributeError branch of the except clause.
    object.__delattr__(schema, "name")
    with pytest.raises(KeyError) as exc_info:
        schema["name"]
    assert exc_info.value.args[0] == "name"
