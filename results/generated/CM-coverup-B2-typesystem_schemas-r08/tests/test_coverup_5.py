# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

from typesystem.fields import Field
from typesystem.schemas import Schema


def test_schema_eq_equal_values_returns_true():
    class Person(Schema):
        name = Field()
        age = Field()

    a = Person({"name": "Alice", "age": 30})
    b = Person({"name": "Alice", "age": 30})
    result = (a == b)
    assert result is True
    assert (a != b) is False
    assert (b == a) is True


def test_schema_eq_first_field_differs_returns_false():
    class Person(Schema):
        name = Field()
        age = Field()

    a = Person({"name": "Alice", "age": 30})
    b = Person({"name": "Bob", "age": 30})
    result = (a == b)
    assert result is False
    assert (a != b) is True
    assert (b == a) is False


def test_schema_eq_second_field_differs_returns_false():
    class Person(Schema):
        name = Field()
        age = Field()

    a = Person({"name": "Alice", "age": 30})
    b = Person({"name": "Alice", "age": 31})
    result = (a == b)
    assert result is False
    assert (a != b) is True
    assert (b == a) is False


def test_schema_eq_different_type_returns_false():
    class Person(Schema):
        name = Field()
        age = Field()

    a = Person({"name": "Alice", "age": 30})
    assert (a == "Alice") is False
    assert (a == 123) is False
    assert (a == None) is False  # noqa: E711
    assert (a == {"name": "Alice", "age": 30}) is False
    assert (a == object()) is False
    assert (a != "Alice") is True

    class Other(Schema):
        name = Field()
        age = Field()

    c = Other({"name": "Alice", "age": 30})
    assert (a == c) is False
    assert (c == a) is False
    assert (a != c) is True


def test_schema_eq_empty_schema_returns_true():
    class Empty(Schema):
        pass

    a = Empty()
    b = Empty()
    assert (a == b) is True
    assert (a != b) is False
