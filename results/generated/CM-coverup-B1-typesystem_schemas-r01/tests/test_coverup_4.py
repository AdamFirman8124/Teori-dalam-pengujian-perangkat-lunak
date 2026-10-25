# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import pytest

from typesystem import Schema
from typesystem.fields import String
from typesystem.schemas import Reference, SchemaDefinitions, SchemaMetaclass


def test_field_attrs_are_popped_and_collected():
    class Article(Schema):
        title = String()
        body = String()

    # Fields must be collected into `fields` (lines 62-64)...
    assert set(Article.fields.keys()) == {"title", "body"}

    # ...and popped from `attrs`, so they are not left as class attributes.
    assert "title" not in Article.__dict__
    assert "body" not in Article.__dict__

    # Postcondition: instances still validate via the collected fields.
    article = Article(title="t", body="b")
    assert article.title == "t"
    assert article.body == "b"


def test_fields_are_inherited_from_base_schemas():
    class Base(Schema):
        name = String()

    class Child(Base):
        email = String()

    # Lines 69-71: base fields merged into the subclass fields.
    assert set(Child.fields.keys()) == {"name", "email"}

    # Overridden field: parent's version must be skipped (`key not in fields` is False).
    class Override(Base):
        name = String(default="overridden")

    assert "name" in Override.fields
    assert Override.fields["name"].default == "overridden"


def test_definitions_are_set_on_reference_fields_and_class_is_registered():
    definitions = SchemaDefinitions()

    class Pet(Schema, definitions=definitions):
        name = String()

    class Owner(Schema, definitions=definitions):
        name = String()
        pet = Reference(to="Pet")

    # Lines 74-76: `set_definitions` applied to every field, including the Reference.
    assert Owner.fields["pet"].definitions is definitions
    # Lines 87-88: the new type is registered under its name.
    assert definitions["Pet"] is Pet
    assert definitions["Owner"] is Owner

    # Postcondition: the reference can now be resolved and validation works.
    owner = Owner.validate({"name": "n", "pet": {"name": "rex"}})
    assert owner.pet.name == "rex"


def test_definitions_registration_with_inherited_fields():
    definitions = SchemaDefinitions()

    class Base(Schema, definitions=definitions):
        id = String()

    class Derived(Base, definitions=definitions):
        extra = String()

    # Inherited fields (lines 69-71) plus definitions propagation (lines 74-76, 87-88).
    assert set(Derived.fields.keys()) == {"id", "extra"}
    assert definitions["Base"] is Base
    assert definitions["Derived"] is Derived
    instance = Derived.validate({"id": "1", "extra": "e"})
    assert instance.id == "1"
    assert instance.extra == "e"
