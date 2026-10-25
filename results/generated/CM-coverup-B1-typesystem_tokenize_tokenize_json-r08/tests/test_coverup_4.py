# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import pytest
import typesystem.tokenize.tokenize_json as validate_json_module
from typesystem.base import ParseError, ValidationError
from typesystem.fields import Integer, String
from typesystem.schemas import Schema
from typesystem.tokenize.tokenize_json import validate_json


def test_validate_json_field_with_str_content():
    validator = String()
    result = validate_json('"hello"', validator)
    assert result == "hello"


def test_validate_json_field_with_bytes_content():
    validator = String()
    result = validate_json(b'"hello"', validator)
    assert result == "hello"


def test_validate_json_integer_field():
    validator = Integer()
    result = validate_json("123", validator)
    assert result == 123


def test_validate_json_schema_success():
    class User(Schema):
        name = String()
        age = Integer()

    result = validate_json('{"name": "Tom", "age": 21}', User)
    if isinstance(result, dict):
        assert result == {"name": "Tom", "age": 21}
    else:
        assert result.name == "Tom"
        assert result.age == 21


def test_validate_json_validation_error_has_positions():
    validator = Integer()
    with pytest.raises(ValidationError) as exc_info:
        validate_json('"not-an-int"', validator)
    messages = exc_info.value.messages()
    assert len(messages) == 1
    msg = messages[0]
    assert msg.text
    assert msg.start_position is not None
    assert msg.end_position is not None
    assert msg.start_position.char_index >= 0
    assert msg.end_position.char_index >= msg.start_position.char_index


def test_validate_json_wiring_with_monkeypatch(monkeypatch):
    calls = {}
    fake_token = object()
    sentinel = object()

    def fake_tokenize(content):
        calls["content"] = content
        return fake_token

    def fake_validate(*, token, validator):
        calls["token"] = token
        calls["validator"] = validator
        return sentinel

    monkeypatch.setattr(validate_json_module, "tokenize_json", fake_tokenize)
    monkeypatch.setattr(validate_json_module, "validate_with_positions", fake_validate)

    validator = String()
    result = validate_json_module.validate_json('{"a": 1}', validator)

    assert result is sentinel
    assert calls["content"] == '{"a": 1}'
    assert calls["token"] is fake_token
    assert calls["validator"] is validator
