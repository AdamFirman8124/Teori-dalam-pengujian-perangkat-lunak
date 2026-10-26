# file: project/typesystem/schemas.py:175-182
# asked: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}
# gained: {"lines": [176, 177, 178, 179, 180, 182], "branches": []}

import pytest
from typesystem.fields import Field
from typesystem.schemas import Schema


def test_getitem_returns_serialized_value():
    class Person(Schema):
        name = Field()

    instance = Person({"name": "alice"})
    assert instance.fields["name"] is not None
    assert getattr(instance, "name") == "alice"
    assert instance["name"] == "alice"
    assert instance["name"] == instance.fields["name"].serialize(getattr(instance, "name"))


def test_getitem_unknown_key_raises_keyerror():
    class Person(Schema):
        name = Field()

    instance = Person({"name": "alice"})
    with pytest.raises(KeyError) as exc_info:
        instance["does_not_exist"]
    assert exc_info.value.args[0] == "does_not_exist"
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__suppress_context__ is True


def test_getitem_missing_attribute_raises_keyerror():
    class Person(Schema):
        name = Field()

    # Dict-style init without the key leaves the attribute unset,
    # so getattr(self, key) raises AttributeError internally.
    instance = Person({})
    assert "name" in instance.fields
    assert not hasattr(instance, "name")
    with pytest.raises(KeyError) as exc_info:
        instance["name"]
    assert exc_info.value.args[0] == "name"
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__suppress_context__ is True


def test_getitem_delegates_to_field_serialize(monkeypatch):
    class Upper(Field):
        def serialize(self, obj):
            return f"serialized:{obj}"

    class Item(Schema):
        title = Upper()

    instance = Item({"title": "hello"})
    assert getattr(instance, "title") == "hello"
    # Default behaviour uses the field's serialize.
    assert instance["title"] == "serialized:hello"

    # Spy via monkeypatch to prove __getitem__ calls field.serialize(value).
    field = instance.fields["title"]
    calls = []

    def fake_serialize(value):
        calls.append(value)
        return "mocked"

    monkeypatch.setattr(field, "serialize", fake_serialize)
    assert instance["title"] == "mocked"
    assert calls == ["hello"]
    # Explicitly undo to verify cleanup restores original behaviour.
    monkeypatch.undo()
    assert calls == ["hello"]
    assert field.serialize("hello") == "serialized:hello"
    assert instance["title"] == "serialized:hello"
