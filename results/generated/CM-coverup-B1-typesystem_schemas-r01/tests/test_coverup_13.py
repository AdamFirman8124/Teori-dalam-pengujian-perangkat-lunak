# file: project/typesystem/schemas.py:160-164
# asked: {"lines": [164], "branches": []}
# gained: {"lines": [164], "branches": []}

import pytest

from typesystem import Schema, fields


def test_is_sparse_true_when_fields_have_no_instance_attributes():
    class Person(Schema):
        name = fields.String()
        age = fields.Integer()

    person = Person()

    assert person.is_sparse is True
    assert isinstance(person.is_sparse, bool)


def test_is_sparse_false_when_all_fields_are_shadowed_by_properties():
    class Base(Schema):
        name = fields.String()

    class Shadowed(Base):
        @property
        def name(self):
            return "shadow"

    instance = Shadowed()

    assert instance.is_sparse is False
    assert instance.name == "shadow"


def test_is_sparse_false_for_schema_without_fields():
    class Empty(Schema):
        pass

    assert Empty().is_sparse is False


def test_is_sparse_true_when_only_some_fields_are_shadowed():
    class Base(Schema):
        name = fields.String()
        age = fields.Integer()

    class Partial(Base):
        @property
        def name(self):
            return "shadow"

    instance = Partial()

    assert instance.is_sparse is True


def test_is_sparse_false_after_instance_attribute_is_set(monkeypatch):
    class Person(Schema):
        name = fields.String()

    person = Person()
    assert person.is_sparse is True

    monkeypatch.setattr(person, "name", "Ada", raising=False)

    assert person.is_sparse is False
    assert person.name == "Ada"
