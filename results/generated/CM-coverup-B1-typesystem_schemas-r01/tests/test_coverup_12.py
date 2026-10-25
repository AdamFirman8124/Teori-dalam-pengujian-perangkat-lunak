# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest

from typesystem import String, Integer
from typesystem.base import ValidationError
from typesystem.schemas import Schema


def test_validate_executes_validator_and_returns_schema_instance():
    class ExampleSchema(Schema):
        name = String()
        age = Integer()

    value = {"name": "alice", "age": 30}
    result = ExampleSchema.validate(value)

    assert isinstance(result, ExampleSchema)
    assert result["name"] == "alice"
    assert result["age"] == 30
    assert dict(result) == {"name": "alice", "age": 30}


def test_validate_strict_mode_rejects_coercion():
    class StrictSchema(Schema):
        count = Integer()

    with pytest.raises(ValidationError):
        StrictSchema.validate({"count": "42"}, strict=True)

    result = StrictSchema.validate({"count": "42"}, strict=False)
    assert isinstance(result, StrictSchema)
    assert result["count"] == 42


def test_validate_missing_required_field_raises():
    class RequiredSchema(Schema):
        name = String()

    with pytest.raises(ValidationError):
        RequiredSchema.validate({})

    class DefaultSchema(Schema):
        name = String(default="bob")

    result = DefaultSchema.validate({})
    assert isinstance(result, DefaultSchema)
    assert result["name"] == "bob"
