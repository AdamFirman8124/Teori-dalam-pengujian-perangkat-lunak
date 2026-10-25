# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import pytest

from typesystem import String
from typesystem.schemas import Schema


class Person(Schema):
    name = String()
    age = String()


@pytest.fixture(autouse=True)
def clean_schema_state():
    yield
    # Person is defined at module level but holds no global mutable state;
    # nothing to reset. Fixture kept to make cleanup intent explicit.


def test_eq_returns_false_for_non_schema_instance():
    person = Person()
    person.name = "alice"
    person.age = "30"

    assert (person == "not a schema") is False
    assert (person == 42) is False
    assert (person != "not a schema") is True


def test_eq_returns_false_for_other_schema_class():
    class Animal(Schema):
        name = String()

    animal = Animal()
    animal.name = "alice"
    person = Person()
    person.name = "alice"
    person.age = "30"

    # Different class, even with matching attribute values -> False
    assert (person == animal) is False
    assert (animal == person) is False


def test_eq_returns_false_when_field_values_differ():
    person_a = Person()
    person_a.name = "alice"
    person_a.age = "30"

    person_b = Person()
    person_b.name = "alice"
    person_b.age = "31"

    assert (person_a == person_b) is False
    assert (person_a != person_b) is True


def test_eq_returns_true_when_all_fields_match():
    person_a = Person()
    person_a.name = "alice"
    person_a.age = "30"

    person_b = Person()
    person_b.name = "alice"
    person_b.age = "30"

    assert (person_a == person_b) is True
    assert (person_a != person_b) is False


def test_eq_with_empty_fields():
    class Empty(Schema):
        pass

    assert (Empty() == Empty()) is True
    assert (Empty() == "nope") is False
