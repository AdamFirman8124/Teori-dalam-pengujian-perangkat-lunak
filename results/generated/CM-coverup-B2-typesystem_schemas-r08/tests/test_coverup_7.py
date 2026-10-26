# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

import pytest

from typesystem.fields import Integer, String
from typesystem.schemas import Schema


def test_repr_non_sparse_all_fields_present():
    class Person(Schema):
        name = String()
        age = Integer()

    person = Person(name="Alice", age=30)

    result = repr(person)

    assert result == "Person(name='Alice', age=30)"
    assert not person.is_sparse
    assert not result.endswith(" [sparse]")


def test_repr_sparse_some_fields_missing():
    class Person(Schema):
        name = String()
        age = Integer()

    person = Person(name="Bob")

    result = repr(person)

    assert result == "Person(name='Bob') [sparse]"
    assert person.is_sparse
    assert "age" not in result


def test_repr_sparse_no_fields_present():
    class Person(Schema):
        name = String()
        age = Integer()

    person = Person()

    result = repr(person)

    assert result == "Person() [sparse]"
    assert person.is_sparse


def test_repr_empty_schema():
    class Empty(Schema):
        pass

    empty = Empty()

    result = repr(empty)

    assert result == "Empty()"
    assert not empty.is_sparse


def test_repr_includes_default_value_and_is_not_sparse():
    class Settings(Schema):
        name = String(default="unknown")
        count = Integer(default=7)

    settings = Settings()

    result = repr(settings)

    assert result == "Settings(name='unknown', count=7)"
    assert not settings.is_sparse
