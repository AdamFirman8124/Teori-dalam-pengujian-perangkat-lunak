# file: project/typesystem/schemas.py:150-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

from typesystem.base import ValidationError
from typesystem.schemas import Schema


def test_schema_validate_or_error_returns_validated_value():
    payload = object()
    validated_value = object()
    calls = []

    class TestSchema(Schema):
        @classmethod
        def validate(cls, value, *, strict=False):
            calls.append((value, strict))
            return validated_value

    result = TestSchema.validate_or_error(payload, strict=True)

    assert calls == [(payload, True)]
    assert result.value is validated_value
    assert result.error is None


def test_schema_validate_or_error_returns_validation_error():
    payload = object()
    expected_error = ValidationError(text="Invalid value.", code="invalid")
    calls = []

    class TestSchema(Schema):
        @classmethod
        def validate(cls, value, *, strict=False):
            calls.append((value, strict))
            raise expected_error

    result = TestSchema.validate_or_error(payload, strict=False)

    assert calls == [(payload, False)]
    assert result.value is None
    assert result.error is expected_error
