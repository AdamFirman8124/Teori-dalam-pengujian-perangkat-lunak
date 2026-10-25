# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest

from typesystem.schemas import Schema


@pytest.mark.parametrize("strict", [False, True])
def test_schema_validate_uses_validator_and_returns_schema(monkeypatch, strict):
    calls = []

    class ExampleSchema(Schema):
        def __init__(self, value):
            self.received_value = value

    class Validator:
        def validate(self, value, *, strict=False):
            calls.append(("validate", value, strict))
            return {"validated": value}

    validator = Validator()

    def make_validator(cls, *, strict=False):
        calls.append(("make_validator", cls, strict))
        return validator

    monkeypatch.setattr(
        ExampleSchema, "make_validator", classmethod(make_validator)
    )

    result = ExampleSchema.validate("input", strict=strict)

    assert isinstance(result, ExampleSchema)
    assert result.received_value == {"validated": "input"}
    assert calls == [
        ("make_validator", ExampleSchema, strict),
        ("validate", "input", strict),
    ]
