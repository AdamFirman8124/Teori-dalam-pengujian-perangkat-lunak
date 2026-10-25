# file: project/typesystem/schemas.py:175-182
# asked: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}
# gained: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}

import pytest
from typesystem.fields import Field
from typesystem.schemas import Schema


class _EchoField(Field):
    def serialize(self, obj):
        return f"serialized:{obj}"


def test_getitem_returns_serialized_value():
    class Person(Schema):
        name = _EchoField()

    obj = Person({"name": "hello"})
    assert obj.fields["name"] is Person.fields["name"]
    assert getattr(obj, "name") == "hello"
    result = obj["name"]
    assert result == "serialized:hello"


def test_getitem_unknown_key_raises_keyerror():
    class Person(Schema):
        name = _EchoField()

    obj = Person({"name": "hello"})
    with pytest.raises(KeyError) as exc_info:
        obj["missing"]
    assert exc_info.value.args[0] == "missing"
    assert exc_info.value.__suppress_context__ is True
    assert exc_info.value.__cause__ is None


def test_getitem_missing_attribute_raises_keyerror():
    class Person(Schema):
        name = _EchoField()

    obj = Person({})
    assert "name" in Person.fields
    assert "name" in obj.fields
    with pytest.raises(AttributeError):
        getattr(obj, "name")
    with pytest.raises(KeyError) as exc_info:
        obj["name"]
    assert exc_info.value.args[0] == "name"
    assert exc_info.value.__suppress_context__ is True
    assert exc_info.value.__cause__ is None
