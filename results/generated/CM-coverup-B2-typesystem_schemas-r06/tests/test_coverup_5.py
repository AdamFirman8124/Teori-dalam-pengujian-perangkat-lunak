# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import typesystem


def test_schema_eq_false_for_unrelated_type():
    class Person(typesystem.Schema):
        name = typesystem.String()

    person = Person(name="alice")
    assert (person == "alice") is False
    assert (person == 123) is False
    assert (person == {"name": "alice"}) is False
    assert (person == None) is False  # noqa: E711
    assert (person != "alice") is True


def test_schema_eq_false_for_different_schema_class():
    class Person(typesystem.Schema):
        name = typesystem.String()

    class Other(typesystem.Schema):
        name = typesystem.String()

    person = Person(name="alice")
    other = Other(name="alice")
    assert (person == other) is False
    assert (other == person) is False


def test_schema_eq_false_for_differing_field_value():
    class Person(typesystem.Schema):
        name = typesystem.String()

    first = Person(name="alice")
    second = Person(name="bob")
    assert (first == second) is False
    assert (second == first) is False
    assert (first != second) is True


def test_schema_eq_true_for_equal_field_values():
    class Person(typesystem.Schema):
        name = typesystem.String()

    first = Person(name="alice")
    second = Person(name="alice")
    assert (first == second) is True
    assert (second == first) is True
    assert (first != second) is False
    assert (first == first) is True


def test_schema_eq_true_for_empty_schema():
    class Empty(typesystem.Schema):
        pass

    first = Empty()
    second = Empty()
    assert (first == second) is True
    assert (first == "not-a-schema") is False
