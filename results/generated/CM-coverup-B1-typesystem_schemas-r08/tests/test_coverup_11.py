# file: project/typesystem/schemas.py:150-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

import typesystem
from typesystem.base import ValidationError, ValidationResult


def test_validate_or_error_success():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    result = Person.validate_or_error({"name": "Alice", "age": 30})

    assert isinstance(result, ValidationResult)
    assert result.error is None
    assert isinstance(result.value, Person)
    assert result.value["name"] == "Alice"
    assert result.value["age"] == 30


def test_validate_or_error_failure():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    result = Person.validate_or_error({"name": "Alice", "age": "not-an-int"})

    assert isinstance(result, ValidationResult)
    assert result.value is None
    assert isinstance(result.error, ValidationError)
    assert result.error is not None


def test_validate_or_error_failure_non_dict():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    result = Person.validate_or_error(12345, strict=False)

    assert isinstance(result, ValidationResult)
    assert result.value is None
    assert isinstance(result.error, ValidationError)


def test_validate_or_error_forwards_strict_flag(monkeypatch):
    class Item(typesystem.Schema):
        title = typesystem.String()

    seen = {}
    orig_validate = Item.validate

    def spy(cls, value, *, strict=False):
        seen["value"] = value
        seen["strict"] = strict
        return orig_validate(value, strict=strict)

    monkeypatch.setattr(Item, "validate", classmethod(spy))

    result = Item.validate_or_error({"title": "hello"}, strict=True)

    assert seen["value"] == {"title": "hello"}
    assert seen["strict"] is True
    assert isinstance(result, ValidationResult)
    assert result.error is None
    assert isinstance(result.value, Item)
    assert result.value["title"] == "hello"


def test_validate_or_error_forwards_strict_flag_on_error(monkeypatch):
    class Item(typesystem.Schema):
        title = typesystem.String()

    seen = {}
    orig_validate = Item.validate

    def spy(cls, value, *, strict=False):
        seen["strict"] = strict
        return orig_validate(value, strict=strict)

    monkeypatch.setattr(Item, "validate", classmethod(spy))

    result = Item.validate_or_error({"title": 12345}, strict=True)

    assert seen["strict"] is True
    assert isinstance(result, ValidationResult)
    assert result.value is None
    assert isinstance(result.error, ValidationError)
