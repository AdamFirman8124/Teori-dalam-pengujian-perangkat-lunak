# file: project/typesystem/schemas.py:133-140
# asked: {"lines": [135, 136, 137, 138, 139], "branches": []}
# gained: {"lines": [135, 136, 137, 138, 139], "branches": []}

import pytest

from typesystem.fields import Integer, Object, String
from typesystem.schemas import Schema


class ExampleSchema(Schema):
    name = String()
    age = Integer(default=0)


def test_make_validator_non_strict():
    validator = ExampleSchema.make_validator()

    assert isinstance(validator, Object)
    assert validator.properties == ExampleSchema.fields
    # 'age' has a default, so only 'name' is required.
    assert validator.required == ["name"]
    # strict=False -> additional_properties is None
    assert validator.additional_properties is None


def test_make_validator_strict():
    validator = ExampleSchema.make_validator(strict=True)

    assert isinstance(validator, Object)
    assert validator.properties == ExampleSchema.fields
    assert validator.required == ["name"]
    # strict=True -> additional_properties is False
    assert validator.additional_properties is False


def test_make_validator_all_fields_required_when_no_defaults():
    class NoDefaultsSchema(Schema):
        first = String()
        second = String()

    validator = NoDefaultsSchema.make_validator()

    assert isinstance(validator, Object)
    assert sorted(validator.required) == ["first", "second"]
    assert validator.additional_properties is None


def test_make_validator_no_fields_required_when_all_have_defaults():
    class AllDefaultsSchema(Schema):
        first = String(default="a")
        second = String(default="b")

    validator = AllDefaultsSchema.make_validator()

    assert isinstance(validator, Object)
    assert validator.required == []
    assert validator.additional_properties is None
