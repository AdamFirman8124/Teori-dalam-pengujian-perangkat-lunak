# file: project/typesystem/schemas.py:95-131
# asked: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 110], [124, 125], [127, 0], [127, 128]]}
# gained: {"lines": [96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131], "branches": [[96, 97], [96, 110], [100, 101], [100, 105], [101, 102], [101, 108], [102, 101], [102, 103], [105, 106], [105, 108], [106, 105], [106, 107], [110, 111], [110, 127], [111, 112], [111, 124], [114, 115], [114, 123], [124, 125], [127, 0], [127, 128]]}

import pytest

import typesystem


def test_schema_init_with_positional_dict():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    person = Person({"name": "Tom", "age": 42})
    assert person.name == "Tom"
    assert person.age == 42

    # Keys missing from the dict are simply not set.
    partial = Person({"name": "Jane"})
    assert partial.name == "Jane"


def test_schema_init_with_positional_object():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    class Record:
        name = "Tom"
        age = 42

    person = Person(Record())
    assert person.name == "Tom"
    assert person.age == 42

    class PartialRecord:
        name = "Jane"

    partial = Person(PartialRecord())
    assert partial.name == "Jane"


def test_schema_init_with_keyword_arguments():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer(default=0)

    person = Person(name="Tom", age=42)
    assert person.name == "Tom"
    assert person.age == 42

    # Defaults are applied for omitted keyword arguments.
    defaulted = Person(name="Jane")
    assert defaulted.name == "Jane"
    assert defaulted.age == 0


def test_schema_init_with_invalid_keyword_argument():
    class Person(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(TypeError) as exc_info:
        Person(name=123)

    message = str(exc_info.value)
    assert message.startswith("Invalid argument 'name' for Person().")
    assert "Must be a string." in message


def test_schema_init_with_unexpected_keyword_argument():
    class Person(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(TypeError) as exc_info:
        Person(name="Tom", unknown="value")

    assert str(exc_info.value) == (
        "'unknown' is an invalid keyword argument for Person()."
    )


def test_schema_init_with_multiple_positional_arguments():
    class Person(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(AssertionError):
        Person({"name": "Tom"}, {"name": "Jane"})


def test_schema_init_with_positional_and_keyword_arguments():
    class Person(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(AssertionError):
        Person({"name": "Tom"}, name="Jane")
