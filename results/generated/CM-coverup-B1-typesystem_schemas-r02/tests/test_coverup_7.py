# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

from typesystem import String, Integer
from typesystem.schemas import Schema


def test_repr_with_all_fields_set():
    class Person(Schema):
        name = String()
        age = Integer()

    person = Person(name="Tom", age=25)
    result = repr(person)

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

    person = Person(name="Tom")
    # Simulate a field declared in `fields` but with no attribute on the
    # instance, so the `hasattr(self, key)` filter drops it.
    object.__delattr__(person, "age") if hasattr(person, "age") else None

    result = repr(person)

    assert "age=" not in result
    assert result == "Person(name='Tom') [sparse]"


def test_repr_empty_schema():
    class Empty(Schema):
        pass

    result = repr(Empty())

    assert result == "Empty()"
