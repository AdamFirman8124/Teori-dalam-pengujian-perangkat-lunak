# file: project/typesystem/schemas.py:133-140
# asked: {"lines": [135, 136, 137, 138, 139], "branches": []}
# gained: {"lines": [135, 136, 137, 138, 139], "branches": []}

import pytest

from typesystem.fields import Field, Integer, String
from typesystem.schemas import Schema


def test_make_validator_required_and_no_additional_properties():
    class Example(Schema):
        name = String()
        age = Integer(default=0)

    validator = Example.make_validator(strict=True)

    assert isinstance(validator, Field)
    assert validator.required == ["name"]
    assert validator.additional_properties is False
    assert set(validator.properties) == {"name", "age"}

    value, error = validator.validate_or_error({"name": "Ada"})
    assert error is None
    assert value == {"name": "Ada", "age": 0}

    value, error = validator.validate_or_error({"name": "Ada", "extra": 1})
    assert value is None
    assert error is not None


def test_make_validator_non_strict_allows_additional_properties():
    class Example(Schema):
        name = String()

    validator = Example.make_validator()

    assert validator.required == ["name"]
    assert validator.additional_properties is None

    value, error = validator.validate_or_error({"name": "Ada", "extra": 1})
    assert error is None
    assert value == {"name": "Ada"}


def test_make_validator_all_fields_have_defaults():
    class Example(Schema):
        name = String(default="anon")
        age = Integer(default=0)

    validator = Example.make_validator(strict=True)

    assert validator.required == []
    assert validator.additional_properties is False

    value, error = validator.validate_or_error({})
    assert error is None
    assert value == {"name": "anon", "age": 0}


def test_make_validator_does_not_mutate_schema_fields():
    class Example(Schema):
        name = String()

    original_fields = dict(Example.fields)
    validator = Example.make_validator(strict=True)

    assert Example.fields == original_fields
    assert validator.properties is not Example.fields
    assert validator.properties == original_fields
    assert validator.required == ["name"]
