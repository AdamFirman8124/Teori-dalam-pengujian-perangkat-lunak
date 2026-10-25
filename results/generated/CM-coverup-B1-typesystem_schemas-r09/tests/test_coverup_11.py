# file: project/typesystem/schemas.py:150-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

from typesystem.base import ValidationError, ValidationResult
from typesystem.schemas import Schema


def test_validate_or_error_success(monkeypatch):
    class S(Schema):
        pass

    sentinel = S.__new__(S)

    @classmethod
    def fake_validate(cls, value, *, strict=False):
        assert value == {"a": 1}
        assert strict is False
        return sentinel

    monkeypatch.setattr(S, "validate", fake_validate)
    result = S.validate_or_error({"a": 1})
    assert isinstance(result, ValidationResult)
    assert result.value is sentinel
    assert result.error is None
    v, e = result
    assert v is sentinel
    assert e is None


def test_validate_or_error_failure(monkeypatch):
    class S(Schema):
        pass

    err = ValidationError.__new__(ValidationError)

    @classmethod
    def fake_validate(cls, value, *, strict=False):
        assert value == "bad"
        assert strict is False
        raise err

    monkeypatch.setattr(S, "validate", fake_validate)
    result = S.validate_or_error("bad")
    assert isinstance(result, ValidationResult)
    assert result.value is None
    assert result.error is err
    v, e = result
    assert v is None
    assert e is err


def test_validate_or_error_strict_forwarding(monkeypatch):
    class S(Schema):
        pass

    seen = {}

    @classmethod
    def fake_validate(cls, value, *, strict=False):
        seen["value"] = value
        seen["strict"] = strict
        return "ok-value"

    monkeypatch.setattr(S, "validate", fake_validate)
    result = S.validate_or_error("x", strict=True)
    assert seen == {"value": "x", "strict": True}
    assert isinstance(result, ValidationResult)
    assert result.value == "ok-value"
    assert result.error is None
