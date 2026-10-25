# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import pytest

from typesystem import Array, Object, Reference, String
from typesystem.schemas import Schema, SchemaDefinitions


def test_schema_metaclass_pops_field_attrs_and_inherits_base_fields():
    class Base(Schema, metaclass=type(Schema)):
        pass

    class Parent(Base):
        name = String()

    class Child(Parent):
        title = String()

    # Lines 63-64: Field attributes are popped from attrs and collected into fields.
    assert "name" not in Child.__dict__
    assert "title" not in Child.__dict__
    assert list(Child.fields.keys()) == ["name", "title"]
    assert isinstance(Child.fields["name"], String)
    assert isinstance(Child.fields["title"], String)

    # Lines 70-71: Fields from base classes are inherited when not overridden.
    assert Child.fields["name"] is Parent.fields["name"]


def test_schema_metaclass_with_definitions():
    definitions = SchemaDefinitions()

    class WithDefinitions(Schema, definitions=definitions):
        name = String()
        tags = Array(items=Reference(to="Other"))
        nested = Object(properties={"inner": Reference(to="Other")})
        ref = Reference(to="Other")

    # Lines 75-76: set_definitions is applied to every field, including
    # References nested inside Array items and Object properties.
    assert WithDefinitions.fields["ref"].definitions is definitions
    assert WithDefinitions.fields["tags"].items.definitions is definitions
    assert WithDefinitions.fields["nested"].properties["inner"].definitions is definitions

    # Line 88: The new class is registered in the definitions mapping.
    assert definitions["WithDefinitions"] is WithDefinitions


def test_schema_metaclass_definitions_isolated_per_class():
    definitions = SchemaDefinitions()

    class Registered(Schema, definitions=definitions):
        name = String()

    # Line 88: registration uses the class name as the key.
    assert list(definitions.keys()) == ["Registered"]
    assert definitions["Registered"] is Registered

    # Cleanup: remove the registered entry to avoid state pollution.
    del definitions["Registered"]
    assert len(definitions) == 0
