# file: project/typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

from unittest.mock import Mock

from typesystem.schemas import Schema


def test_schema_validate_uses_non_strict_validator_by_default(monkeypatch):
    class TestSchema(Schema):
        __test__ = False

        def __init__(self, value):
            self.value = value

    raw_value = {"name": "raw"}
    validated_value = {"name": "validated"}
    validator = Mock()
    validator.validate.return_value = validated_value
    make_validator = Mock(return_value=validator)
    monkeypatch.setattr(TestSchema, "make_validator", make_validator)

    result = TestSchema.validate(raw_value)

    make_validator.assert_called_once_with(strict=False)
    validator.validate.assert_called_once_with(raw_value, strict=False)
    assert isinstance(result, TestSchema)
    assert result.value is validated_value


def test_schema_validate_uses_strict_validator_when_requested(monkeypatch):
    class TestSchema(Schema):
        __test__ = False

        def __init__(self, value):
            self.value = value

    raw_value = {"name": "raw"}
    validated_value = {"name": "validated"}
    validator = Mock()
    validator.validate.return_value = validated_value
    make_validator = Mock(return_value=validator)
    monkeypatch.setattr(TestSchema, "make_validator", make_validator)

    result = TestSchema.validate(raw_value, strict=True)

    make_validator.assert_called_once_with(strict=True)
    validator.validate.assert_called_once_with(raw_value, strict=True)
    assert isinstance(result, TestSchema)
    assert result.value is validated_value
