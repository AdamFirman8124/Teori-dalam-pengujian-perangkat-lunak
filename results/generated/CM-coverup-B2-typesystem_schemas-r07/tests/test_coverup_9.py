# file: project/typesystem/schemas.py:175-182
# asked: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}
# gained: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}

import pytest

from typesystem import Schema, fields


class PersonSchema(Schema):
    name = fields.String()
    age = fields.Integer()


class UpperField(fields.Field):
    def serialize(self, obj):
        return obj.upper() if isinstance(obj, str) else obj


class UpperSchema(Schema):
    name = UpperField()


def make_instance(schema_cls, **attrs):
    """Build a Schema instance without relying on __init__ validation."""
    instance = object.__new__(schema_cls)
    for key, value in attrs.items():
        setattr(instance, key, value)
    return instance


def test_getitem_returns_value_for_known_field(monkeypatch):
    instance = make_instance(PersonSchema)
    monkeypatch.setattr(instance, "name", "alice", raising=False)
    monkeypatch.setattr(instance, "age", 30, raising=False)

    assert instance["name"] == "alice"
    assert instance["age"] == 30
    # Postcondition: lookup does not mutate the instance.
    assert instance.name == "alice"
    assert instance.age == 30


def test_getitem_uses_field_serialize(monkeypatch):
    instance = make_instance(UpperSchema)
    monkeypatch.setattr(instance, "name", "alice", raising=False)

    assert instance["name"] == "ALICE"
    # Postcondition: the stored attribute is untouched by serialization.
    assert instance.name == "alice"


def test_getitem_unknown_field_raises_keyerror():
    instance = make_instance(PersonSchema)

    with pytest.raises(KeyError) as exc_info:
        instance["missing"]

    assert exc_info.value.args == ("missing",)
    # `raise ... from None` must suppress the original KeyError context.
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__suppress_context__ is True


def test_getitem_missing_attribute_raises_keyerror():
    instance = make_instance(PersonSchema)

    with pytest.raises(KeyError) as exc_info:
        instance["name"]

    assert exc_info.value.args == ("name",)
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__suppress_context__ is True
    # Postcondition: no attribute was created as a side effect.
    assert not hasattr(instance, "name")
