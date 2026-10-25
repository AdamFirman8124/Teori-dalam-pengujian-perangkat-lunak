# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest

from typesystem.schemas import Schema


@pytest.mark.parametrize("strict", [False, True])
def test_schema_validate_builds_validator_validates_and_constructs_schema(strict):
    calls = []
    input_value = object()
    validated_value = object()

    class Validator:
        def validate(self, value, *, strict=False):
            calls.append(("validate", value, strict))
            return validated_value

    validator = Validator()

    class ExampleSchema(Schema):
        @classmethod
        def make_validator(cls, *, strict=False):
            calls.append(("make_validator", strict))
            return validator

        def __init__(self, value):
            calls.append(("construct", value))
            self.value = value

    result = ExampleSchema.validate(input_value, strict=strict)

    assert isinstance(result, ExampleSchema)
    assert result.value is validated_value
    assert calls == [
        ("make_validator", strict),
        ("validate", input_value, strict),
        ("construct", validated_value),
    ]
