# file: project/typesystem/schemas.py:133-140
# asked: {"lines": [135, 136, 137, 138, 139], "branches": []}
# gained: {"lines": [135, 136, 137, 138, 139], "branches": []}

import typing
from typesystem.fields import Field, Object, String
from typesystem.schemas import Schema


def test_make_validator_non_strict():
    class MySchema(Schema):
        req = String()
        opt = String(default="hello")

    validator = MySchema.make_validator()

    assert isinstance(validator, Object)
    assert validator.properties == MySchema.fields
    assert validator.required == ["req"]
    assert validator.additional_properties is None
    assert "req" in validator.required
    assert "opt" not in validator.required


def test_make_validator_strict():
    class MySchemaStrict(Schema):
        req = String()
        opt = String(default="hello")

    validator = MySchemaStrict.make_validator(strict=True)

    assert isinstance(validator, Object)
    assert validator.properties == MySchemaStrict.fields
    assert validator.required == ["req"]
    assert validator.additional_properties is False
    value, error = validator.validate_or_error({"req": "a", "opt": "b"})
    assert error is None
    assert value == {"req": "a", "opt": "b"}
    _, error2 = validator.validate_or_error({"req": "a", "extra": "nope"})
    assert error2 is not None


def test_make_validator_explicit_non_strict_kwarg():
    class AnotherSchema(Schema):
        a = String()
        b = String()

    validator = AnotherSchema.make_validator(strict=False)

    assert isinstance(validator, Object)
    assert set(validator.required) == {"a", "b"}
    assert validator.additional_properties is None
    assert validator.properties == AnotherSchema.fields
