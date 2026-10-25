# file: project/typesystem/schemas.py:133-140
# asked: {"lines": [135, 136, 137, 138, 139], "branches": []}
# gained: {"lines": [135, 136, 137, 138, 139], "branches": []}

import pytest

from typesystem import Boolean, Integer, String
from typesystem.schemas import Schema


class PersonSchema(Schema):
    name = String()
    age = Integer(default=0)


def test_make_validator_non_strict():
    validator = PersonSchema.make_validator()

    # Line 135: only fields without a default are required.
    assert validator.required == ["name"]
    # Lines 136-139: properties mirror the schema fields.
    assert set(validator.properties.keys()) == {"name", "age"}
    # strict=False -> additional_properties is None.
    assert validator.additional_properties is None

    # Postcondition: validator accepts a valid payload.
    value, error = validator.validate_or_error({"name": "Alice"})
    assert error is None
    assert value == {"name": "Alice", "age": 0}

    # Postcondition: missing required field is reported.
    value, error = validator.validate_or_error({})
    assert error is not None
    assert any(message.code == "required" for message in error.messages())


def test_make_validator_strict():
    validator = PersonSchema.make_validator(strict=True)

    assert validator.required == ["name"]
    assert set(validator.properties.keys()) == {"name", "age"}
    # strict=True -> additional_properties is False.
    assert validator.additional_properties is False

    # Postcondition: unknown keys are rejected in strict mode.
    value, error = validator.validate_or_error(
        {"name": "Alice", "age": 1, "extra": "nope"}, strict=True
    )
    assert error is not None
    assert any(message.code == "invalid_property" for message in error.messages())


def test_make_validator_all_fields_have_defaults():
    class AllDefaultsSchema(Schema):
        flag = Boolean(default=False)

    validator = AllDefaultsSchema.make_validator()

    # Line 135: list comprehension yields no required keys.
    assert validator.required == []
    assert set(validator.properties.keys()) == {"flag"}

    # Postcondition: empty input validates because all fields have defaults.
    value, error = validator.validate_or_error({})
    assert error is None
    assert value == {"flag": False}
