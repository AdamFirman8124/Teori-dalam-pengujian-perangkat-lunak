# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

import pytest

from typesystem import String, Integer
from typesystem.schemas import Schema


def test_repr_with_all_fields_set():
    class Person(Schema):
        name = String()
        age = Integer()

    person = Person(name="Tom", age=25)
    result = repr(person)

    assert person.is_sparse is False
    assert result == "Person(name='Tom', age=25)"
    assert "[sparse]" not in result


def test_repr_is_sparse_when_field_missing():
    class Person(Schema):
        name = String()
        age = Integer()

    person = Person(name="Tom")
    result = repr(person)

    assert person.is_sparse is True
    assert result == "Person(name='Tom') [sparse]"


def test_repr_excludes_fields_without_attribute():
    class Person(Schema):
        name = String()
        age = Integer()

    person = Person(name="Tom", age=25)
    assert hasattr(person, "age")

    # Drop the attribute so `hasattr(self, key)` filters it out of the repr.
    delattr(person, "age")
    assert not hasattr(person, "age")

    result = repr(person)

    assert "age=" not in result
    assert result == "Person(name='Tom') [sparse]"


def test_repr_empty_schema():
    class Empty(Schema):
        pass

    instance = Empty()
    result = repr(instance)

    assert instance.is_sparse is False
    assert result == "Empty()"
