# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

from typesystem.fields import String
from typesystem.schemas import Schema, SchemaDefinitions, SchemaMetaclass


def test_direct_field_popped_into_fields():
    class Example(metaclass=SchemaMetaclass):
        name = String()

    assert "name" in Example.fields
    assert isinstance(Example.fields["name"], String)
    assert not hasattr(Example, "name")


def test_inherited_fields_merged_and_shadowed():
    class Base(metaclass=SchemaMetaclass):
        name = String()

    class Child(Base):
        age = String()

    assert set(Child.fields) == {"name", "age"}
    assert Child.fields["name"] is Base.fields["name"]

    class Override(Child):
        name = String(default="x")

    assert set(Override.fields) == {"name", "age"}
    assert Override.fields["name"] is not Base.fields["name"]
    assert Override.fields["name"] is not Child.fields["name"]
    assert Override.fields["age"] is Child.fields["age"]


def test_definitions_propagated_and_registered():
    definitions = SchemaDefinitions()

    class Person(metaclass=SchemaMetaclass, definitions=definitions):
        name = String()

    assert "name" in Person.fields
    assert definitions["Person"] is Person
    assert len(definitions) == 1


def test_schema_subclassing_with_definitions():
    definitions = SchemaDefinitions()

    class Base2(Schema):
        name = String()

    class Child2(Base2, definitions=definitions):
        age = String()

    assert set(Child2.fields) == {"name", "age"}
    assert Child2.fields["name"] is Base2.fields["name"]
    assert definitions["Child2"] is Child2
    assert "Base2" not in definitions
