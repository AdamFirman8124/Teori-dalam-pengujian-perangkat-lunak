# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest

from typesystem.schemas import Schema


@pytest.mark.parametrize("strict", [False, True])
def test_schema_validate_uses_validator_and_returns_schema_instance(strict):
    calls = []
    original_value = object()
    validated_value = object()

    class Validator:
        def validate(self, value, *, strict=False):
            calls.append(("validate", value, strict))
            return validated_value

    class ExampleSchema(Schema):
        @classmethod
        def make_validator(cls, *, strict=False):
            calls.append(("make_validator", cls, strict))
            return Validator()

        def __init__(self, value):
            self.received_value = value

    result = ExampleSchema.validate(original_value, strict=strict)

    assert calls == [
        ("make_validator", ExampleSchema, strict),
        ("validate", original_value, strict),
    ]
    assert isinstance(result, ExampleSchema)
    assert result.received_value is validated_value
