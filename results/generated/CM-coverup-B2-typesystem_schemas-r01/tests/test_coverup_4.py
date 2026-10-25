# file: project/typesystem/schemas.py:51-89
# asked: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [63, 64, 70, 71, 75, 76, 88], "branches": [[62, 63], [69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import pytest
from typesystem import Schema
from typesystem.fields import String
from typesystem.schemas import Reference, SchemaDefinitions


def test_direct_fields_are_collected_and_popped():
    class Article(Schema):
        title = String()
        body = String()

    assert set(Article.fields.keys()) == {"title", "body"}
    assert "title" not in Article.__dict__
    assert "body" not in Article.__dict__

    article = Article(title="t", body="b")
    assert article.title == "t"
    assert article.body == "b"


def test_fields_are_inherited_from_base():
    class Base(Schema):
        name = String()

    class Child(Base):
        email = String()

    assert set(Child.fields.keys()) == {"name", "email"}
    assert set(Base.fields.keys()) == {"name"}

    child = Child(name="a", email="a@example.com")
    assert child.name == "a"
    assert child.email == "a@example.com"


def test_child_field_overrides_base_field():
    class Base2(Schema):
        name = String()

    class Override(Base2):
        name = String(default="overridden")

    assert set(Override.fields.keys()) == {"name"}
    assert Override.fields["name"].default == "overridden"
    assert Override().name == "overridden"


def test_definitions_propagated_and_registered():
    definitions = SchemaDefinitions()

    class Pet(Schema, definitions=definitions):
        name = String()

    class Owner(Schema, definitions=definitions):
        name = String()
        pet = Reference(to="Pet")

    assert definitions["Pet"] is Pet
    assert definitions["Owner"] is Owner
    assert Owner.fields["pet"].definitions is definitions

    owner = Owner.validate({"name": "n", "pet": {"name": "rex"}})
    assert owner.pet.name == "rex"


def test_definitions_with_inherited_fields():
    definitions = SchemaDefinitions()

    class Base3(Schema, definitions=definitions):
        id = String()

    class Derived(Base3, definitions=definitions):
        extra = String()

    assert set(Derived.fields.keys()) == {"id", "extra"}
    assert definitions["Base3"] is Base3
    assert definitions["Derived"] is Derived

    instance = Derived.validate({"id": "1", "extra": "e"})
    assert instance.id == "1"
    assert instance.extra == "e"
