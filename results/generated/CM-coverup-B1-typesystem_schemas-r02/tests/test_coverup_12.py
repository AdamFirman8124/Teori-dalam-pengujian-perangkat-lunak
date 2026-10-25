# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

from typesystem.schemas import Schema


def test_schema_validate_uses_validator_and_constructs_schema():
    calls = []
    original = object()
    validated = object()

    class Validator:
        def validate(self, value, *, strict=False):
            calls.append(("validate", value, strict))
            return validated

    validator = Validator()

    class TestSchema(Schema):
        @classmethod
        def make_validator(cls, *, strict=False):
            calls.append(("make_validator", cls, strict))
            return validator

        def __init__(self, value):
            self.received_value = value

    result = TestSchema.validate(original, strict=True)

    assert isinstance(result, TestSchema)
    assert result.received_value is validated
    assert calls == [
        ("make_validator", TestSchema, True),
        ("validate", original, True),
    ]


def test_schema_validate_uses_default_non_strict_mode():
    calls = []

    class Validator:
        def validate(self, value, *, strict=False):
            calls.append(("validate", value, strict))
            return {"validated": value}

    class TestSchema(Schema):
        @classmethod
        def make_validator(cls, *, strict=False):
            calls.append(("make_validator", cls, strict))
            return Validator()

        def __init__(self, value):
            self.received_value = value

    result = TestSchema.validate("input")

    assert isinstance(result, TestSchema)
    assert result.received_value == {"validated": "input"}
    assert calls == [
        ("make_validator", TestSchema, False),
        ("validate", "input", False),
    ]
