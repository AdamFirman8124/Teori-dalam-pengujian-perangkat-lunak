# file: project/typesystem/schemas.py:150-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

import typesystem
from typesystem.base import ValidationError


def test_validate_or_error_success():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    result = Person.validate_or_error({"name": "Alice", "age": 30})

    assert result.error is None
    assert isinstance(result.value, Person)
    assert result.value["name"] == "Alice"
    assert result.value["age"] == 30
    assert result.value == Person(name="Alice", age=30)


def test_validate_or_error_failure():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    result = Person.validate_or_error({"name": "Alice"}, strict=True)

    assert result.value is None
    assert isinstance(result.error, ValidationError)
    assert len(list(result.error.messages())) > 0
