# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest

from typesystem.schemas import Schema


@pytest.mark.parametrize("strict", [False, True])
def test_validate_uses_validator_and_constructs_schema(monkeypatch, strict):
    calls = []
    normalized = {"normalized": "value"}

    class TestSchema(Schema):
        def __init__(self, value):
            self.received = value

    class StubValidator:
        def validate(self, value, *, strict=False):
            calls.append(("validate", value, strict))
            return normalized

    validator = StubValidator()

    def make_validator(cls, *, strict=False):
        calls.append(("make_validator", strict))
        return validator

    monkeypatch.setattr(TestSchema, "make_validator", classmethod(make_validator))

    result = TestSchema.validate("input", strict=strict)

    assert isinstance(result, TestSchema)
    assert result.received is normalized
    assert calls == [
        ("make_validator", strict),
        ("validate", "input", strict),
    ]
