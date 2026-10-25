# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import typesystem.schemas as schemas
from typesystem.fields import Field, String


def test_schema_metaclass_collects_declared_and_inherited_fields(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    inherited = String()
    inherited_override = String()

    class Parent(schemas.Schema):
        parent_field = inherited
        overridden = inherited_override

    class NonFieldBase:
        fields = {"ignored": object()}

    child_field = String()
    child_override = String()

    class Child(Parent, NonFieldBase):
        own_field = child_field
        overridden = child_override

    assert "parent_field" not in Parent.__dict__
    assert "overridden" not in Parent.__dict__
    assert "own_field" not in Child.__dict__
    assert "overridden" not in Child.__dict__

    assert Child.fields == {
        "parent_field": inherited,
        "own_field": child_field,
        "overridden": child_override,
    }
    assert Child.fields["overridden"] is child_override
    assert inherited_override not in Child.fields.values()
    assert "ignored" not in Child.fields


def test_schema_metaclass_sets_definitions_and_registers_schema(monkeypatch):
    monkeypatch.setattr(Field, "_creation_counter", 0)

    definitions = schemas.SchemaDefinitions()
    calls = []
    original_set_definitions = schemas.set_definitions

    def recording_set_definitions(field, supplied_definitions):
        calls.append((field, supplied_definitions))
        original_set_definitions(field, supplied_definitions)

    monkeypatch.setattr(
        schemas, "set_definitions", recording_set_definitions
    )

    first = String()
    second = String()
    attrs = {
        "__module__": __name__,
        "first": first,
        "second": second,
    }

    registered_schema = schemas.SchemaMetaclass.__new__(
        schemas.SchemaMetaclass,
        "RegisteredSchema",
        (schemas.Schema,),
        attrs,
        definitions=definitions,
    )

    assert registered_schema.fields == {
        "first": first,
        "second": second,
    }
    assert calls == [
        (first, definitions),
        (second, definitions),
    ]
    assert definitions["RegisteredSchema"] is registered_schema
    assert "first" not in registered_schema.__dict__
    assert "second" not in registered_schema.__dict__
