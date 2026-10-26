# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import pytest

from typesystem.fields import Array, Object, String
from typesystem.schemas import Reference, Schema, SchemaDefinitions, SchemaMetaclass


def test_field_attributes_are_popped_and_collected():
    class Example(metaclass=SchemaMetaclass):
        name = String()

    # Lines 63-64: the Field attribute is removed from attrs and collected.
    assert not hasattr(Example, "name")
    assert "name" in Example.fields
    assert isinstance(Example.fields["name"], String)


def test_inherited_fields_from_base_schemas():
    class Base(metaclass=SchemaMetaclass):
        name = String()

    class Child(Base):
        age = String()

    class Override(Child):
        name = String(default="x")

    # Lines 70-71 (true branch): inherited field added when not shadowed.
    assert "name" in Child.fields
    assert "age" in Child.fields
    assert Child.fields["name"] is Base.fields["name"]

    # Line 70 (false branch): shadowed field is not overwritten.
    assert Override.fields["name"] is not Base.fields["name"]
    assert Override.fields["name"].default == "x"


def test_definitions_are_propagated_and_class_registered():
    definitions = SchemaDefinitions()

    class Person(metaclass=SchemaMetaclass, definitions=definitions):
        name = String()
        friend = Reference("Person")

    # Lines 75-76: set_definitions applied to Reference fields.
    assert Person.fields["friend"].definitions is definitions
    # Non-reference fields are untouched but must not raise.
    assert isinstance(Person.fields["name"], String)

    # Line 88: the new type is registered under its name.
    assert definitions["Person"] is Person


def test_definitions_propagated_through_nested_fields():
    definitions = SchemaDefinitions()

    class Nested(metaclass=SchemaMetaclass, definitions=definitions):
        tags = Array(Reference("Nested"))
        profile = Object(properties={"avatar": Reference("Nested")})

    # Lines 75-76 via recursion into Array and Object children.
    assert Nested.fields["tags"].items.definitions is definitions
    assert Nested.fields["profile"].properties["avatar"].definitions is definitions
    assert definitions["Nested"] is Nested


def test_schema_subclassing_with_definitions_kwarg():
    definitions = SchemaDefinitions()

    class Base(Schema):
        name = String()

    class Child(Base, definitions=definitions):
        age = String()

    # Inherited fields plus own field, with registration on definitions.
    assert set(Child.fields) == {"name", "age"}
    assert definitions["Child"] is Child
