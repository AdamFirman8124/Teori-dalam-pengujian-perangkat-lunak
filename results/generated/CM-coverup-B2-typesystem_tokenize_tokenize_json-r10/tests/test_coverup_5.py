# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import pytest
import typesystem.tokenize.tokenize_json as tokenize_json_module
from typesystem.base import ValidationError
from typesystem.tokenize.tokenize_json import validate_json


def test_validate_json_delegates_to_tokenize_and_validate(monkeypatch):
    sentinel_token = object()
    sentinel_validator = object()
    seen = {}

    def fake_tokenize_json(content):
        seen["content"] = content
        return sentinel_token

    def fake_validate_with_positions(token, validator):
        seen["token"] = token
        seen["validator"] = validator
        assert token is sentinel_token
        assert validator is sentinel_validator
        return "validated-value"

    monkeypatch.setattr(tokenize_json_module, "tokenize_json", fake_tokenize_json)
    monkeypatch.setattr(tokenize_json_module, "validate_with_positions", fake_validate_with_positions)

    result = validate_json('{"a": 1}', sentinel_validator)

    assert result == "validated-value"
    assert seen["content"] == '{"a": 1}'
    assert seen["token"] is sentinel_token
    assert seen["validator"] is sentinel_validator


def test_validate_json_str_content_success():
    class StubValidator:
        def validate(self, value):
            assert value == {"a": 1}
            return value

    value = validate_json('{"a": 1}', StubValidator())

    assert value == {"a": 1}


def test_validate_json_bytes_content_success():
    class StubSchemaValidator:
        @classmethod
        def validate(cls, value):
            return value

    value = validate_json(b'[1, 2, 3]', StubSchemaValidator)

    assert value == [1, 2, 3]


def test_validate_json_validation_error_carries_positions():
    def failing_validate(value):
        assert value == {"a": 1}
        raise ValidationError(text="Invalid value.", code="invalid")

    class FailingValidator:
        def validate(self, value):
            return failing_validate(value)

    with pytest.raises(ValidationError) as exc_info:
        validate_json('{"a": 1}', FailingValidator())

    messages = exc_info.value.messages()
    assert len(messages) == 1
    assert messages[0].text == "Invalid value."
    assert messages[0].code == "invalid"
    assert hasattr(messages[0], "start_position")
    assert hasattr(messages[0], "end_position")
    assert messages[0].start_position is not None
    assert messages[0].end_position is not None
