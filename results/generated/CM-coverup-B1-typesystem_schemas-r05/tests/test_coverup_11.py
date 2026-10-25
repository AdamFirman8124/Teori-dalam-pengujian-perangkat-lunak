# file: project/typesystem/schemas.py:150-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

from typesystem.base import ValidationError
from typesystem.schemas import Schema


def test_validate_or_error_returns_validated_value_and_forwards_strict():
    supplied_value = object()
    validated_value = object()
    calls = []

    class SuccessfulSchema(Schema):
        @classmethod
        def validate(cls, value, *, strict=False):
            calls.append((value, strict))
            return validated_value

    result = SuccessfulSchema.validate_or_error(supplied_value, strict=True)

    assert result.value is validated_value
    assert result.error is None
    assert calls == [(supplied_value, True)]


def test_validate_or_error_returns_caught_validation_error():
    supplied_value = object()
    expected_error = ValidationError(text="Invalid value.", code="invalid")
    calls = []

    class FailingSchema(Schema):
        @classmethod
        def validate(cls, value, *, strict=False):
            calls.append((value, strict))
            raise expected_error

    result = FailingSchema.validate_or_error(supplied_value, strict=True)

    assert result.value is None
    assert result.error is expected_error
    assert calls == [(supplied_value, True)]
