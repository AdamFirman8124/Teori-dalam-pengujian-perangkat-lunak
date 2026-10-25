# file: project/typesystem/schemas.py:175-182
# asked: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}
# gained: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}

import pytest

from typesystem.fields import Field
from typesystem.schemas import Schema


def test_schema_getitem_serializes_field_value():
    calls = []

    class RecordingField(Field):
        def serialize(self, obj):
            calls.append(obj)
            return f"serialized:{obj}"

    class ExampleSchema(Schema):
        value = RecordingField()

    instance = ExampleSchema({"value": "original"})

    assert instance["value"] == "serialized:original"
    assert calls == ["original"]


def test_schema_getitem_raises_key_error_for_unknown_field():
    class ExampleSchema(Schema):
        value = Field()

    instance = ExampleSchema({"value": "original"})

    with pytest.raises(KeyError) as exc_info:
        instance["unknown"]

    assert exc_info.value.args == ("unknown",)
    assert exc_info.value.__suppress_context__ is True


def test_schema_getitem_raises_key_error_when_field_attribute_is_missing():
    class ExampleSchema(Schema):
        value = Field()

    instance = ExampleSchema({})

    assert "value" in instance.fields
    assert not hasattr(instance, "value")

    with pytest.raises(KeyError) as exc_info:
        instance["value"]

    assert exc_info.value.args == ("value",)
    assert exc_info.value.__suppress_context__ is True
