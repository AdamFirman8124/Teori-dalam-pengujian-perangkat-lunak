# file: project/typesystem/schemas.py:150-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

from typesystem.base import ValidationError
from typesystem.schemas import Schema


def test_schema_validate_or_error_returns_validated_value(monkeypatch):
    input_value = object()
    validated_value = object()
    calls = []

    def validate(cls, value, *, strict=False):
        calls.append((cls, value, strict))
        return validated_value

    monkeypatch.setattr(Schema, "validate", classmethod(validate))

    result = Schema.validate_or_error(input_value, strict=True)

    assert calls == [(Schema, input_value, True)]
    assert result.value is validated_value
    assert result.error is None


def test_schema_validate_or_error_returns_validation_error(monkeypatch):
    input_value = object()
    expected_error = ValidationError(text="Invalid value.", code="invalid")
    calls = []

    def validate(cls, value, *, strict=False):
        calls.append((cls, value, strict))
        raise expected_error

    monkeypatch.setattr(Schema, "validate", classmethod(validate))

    result = Schema.validate_or_error(input_value, strict=False)

    assert calls == [(Schema, input_value, False)]
    assert result.value is None
    assert result.error is expected_error
