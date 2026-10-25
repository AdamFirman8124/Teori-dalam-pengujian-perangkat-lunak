# file: project/typesystem/schemas.py:150-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

from typesystem.base import ValidationError, ValidationResult
from typesystem.schemas import Schema


def test_validate_or_error_returns_validated_value(monkeypatch):
    input_value = object()
    validated_value = object()
    calls = []

    def fake_validate(cls, value, *, strict=False):
        calls.append((cls, value, strict))
        return validated_value

    monkeypatch.setattr(Schema, "validate", classmethod(fake_validate))

    result = Schema.validate_or_error(input_value, strict=True)

    assert isinstance(result, ValidationResult)
    assert result.value is validated_value
    assert result.error is None
    assert calls == [(Schema, input_value, True)]


def test_validate_or_error_returns_validation_error(monkeypatch):
    input_value = object()
    error = ValidationError.__new__(ValidationError)
    Exception.__init__(error, "expected validation failure")
    calls = []

    def fake_validate(cls, value, *, strict=False):
        calls.append((cls, value, strict))
        raise error

    monkeypatch.setattr(Schema, "validate", classmethod(fake_validate))

    result = Schema.validate_or_error(input_value, strict=False)

    assert isinstance(result, ValidationResult)
    assert result.value is None
    assert result.error is error
    assert calls == [(Schema, input_value, False)]
