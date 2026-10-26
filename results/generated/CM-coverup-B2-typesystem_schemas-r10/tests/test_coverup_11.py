# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest

from typesystem import Integer, String
from typesystem.base import ValidationError
from typesystem.schemas import Schema


def test_validate_non_strict():
    class ExampleSchema(Schema):
        name = String()
        age = Integer()

    value = {"name": "alice", "age": "30"}
    result = ExampleSchema.validate(value)

    assert isinstance(result, ExampleSchema)
    assert result["name"] == "alice"
    assert result["age"] == 30


def test_validate_strict():
    class ExampleSchema(Schema):
        name = String()
        age = Integer()

    value = {"name": "bob", "age": 42}
    result = ExampleSchema.validate(value, strict=True)

    assert isinstance(result, ExampleSchema)
    assert result["name"] == "bob"
    assert result["age"] == 42


def test_validate_strict_rejects_extra_keys():
    class ExampleSchema(Schema):
        name = String()

    with pytest.raises(ValidationError):
        ExampleSchema.validate({"name": "carol", "extra": 1}, strict=True)


def test_validate_missing_required_field_raises():
    class ExampleSchema(Schema):
        name = String()

    with pytest.raises(ValidationError):
        ExampleSchema.validate({})
