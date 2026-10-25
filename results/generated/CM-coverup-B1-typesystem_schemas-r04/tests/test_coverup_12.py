# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest
import typesystem


def test_validate_returns_schema_instance():
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    result = Person.validate({"name": "Ada", "age": 36})

    assert isinstance(result, Person)
    assert result["name"] == "Ada"
    assert result["age"] == 36
    assert dict(result) == {"name": "Ada", "age": 36}


def test_validate_strict_true_returns_schema_instance():
    class Person(typesystem.Schema):
        name = typesystem.String()

    result = Person.validate({"name": "Ada"}, strict=True)

    assert isinstance(result, Person)
    assert result["name"] == "Ada"


def test_validate_strict_true_rejects_additional_properties():
    class Person(typesystem.Schema):
        name = typesystem.String()

    with pytest.raises(typesystem.ValidationError):
        Person.validate({"name": "Ada", "extra": 1}, strict=True)


def test_validate_non_strict_allows_additional_properties():
    class Person(typesystem.Schema):
        name = typesystem.String()

    # In non-strict mode, additional properties are allowed by the validator
    # (no ValidationError), but the resulting Schema instance only stores
    # the declared fields.
    result = Person.validate({"name": "Ada", "extra": 1})

    assert isinstance(result, Person)
    assert result["name"] == "Ada"
    assert "extra" not in result


def test_validate_forwards_strict_to_make_validator(monkeypatch):
    class Person(typesystem.Schema):
        name = typesystem.String()

    seen = []
    original = Person.make_validator.__func__

    def spy(cls, *, strict=False):
        seen.append(strict)
        return original(cls, strict=strict)

    monkeypatch.setattr(Person, "make_validator", classmethod(spy))

    result = Person.validate({"name": "Ada"}, strict=True)

    assert seen == [True]
    assert isinstance(result, Person)
    assert result["name"] == "Ada"
