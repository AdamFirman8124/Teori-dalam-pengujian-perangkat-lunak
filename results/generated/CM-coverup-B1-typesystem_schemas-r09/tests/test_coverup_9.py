# file: project/typesystem/schemas.py:175-182
# asked: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}
# gained: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}

from types import SimpleNamespace

import pytest

from typesystem.schemas import Schema


def test_schema_getitem_serializes_attribute_value():
    class Field:
        def __init__(self):
            self.received = None

        def serialize(self, value):
            self.received = value
            return f"serialized:{value}"

    field = Field()
    instance = SimpleNamespace(fields={"name": field}, name="Alice")

    assert Schema.__getitem__(instance, "name") == "serialized:Alice"
    assert field.received == "Alice"


def test_schema_getitem_raises_key_error_for_unknown_field():
    instance = SimpleNamespace(fields={})

    with pytest.raises(KeyError) as exc_info:
        Schema.__getitem__(instance, "missing")

    assert exc_info.value.args == ("missing",)
    assert exc_info.value.__suppress_context__ is True


def test_schema_getitem_raises_key_error_for_missing_attribute():
    class Field:
        def serialize(self, value):
            pytest.fail("serialize() must not be called for a missing attribute")

    instance = SimpleNamespace(fields={"missing": Field()})

    with pytest.raises(KeyError) as exc_info:
        Schema.__getitem__(instance, "missing")

    assert exc_info.value.args == ("missing",)
    assert exc_info.value.__suppress_context__ is True
