# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import pytest

from typesystem.base import ParseError, ValidationError
from typesystem.fields import Integer, String
from typesystem.schemas import Schema
from typesystem.tokenize import tokenize_json as tokenize_json_module
from typesystem.tokenize.tokenize_json import validate_json


class Album(Schema):
    name = String()
    year = Integer()


def test_validate_json_with_schema_returns_validated_schema():
    value = validate_json('{"name": "Discovery", "year": 2001}', Album)

    assert isinstance(value, Album)
    assert value["name"] == "Discovery"
    assert value["year"] == 2001
    assert dict(value) == {"name": "Discovery", "year": 2001}


def test_validate_json_with_field_instance():
    value = validate_json("123", Integer())

    assert value == 123


def test_validate_json_accepts_bytes_content():
    value = validate_json(b'{"name": "Discovery", "year": 2001}', Album)

    assert isinstance(value, Album)
    assert value["name"] == "Discovery"
    assert value["year"] == 2001


def test_validate_json_raises_positional_validation_error():
    with pytest.raises(ValidationError) as exc_info:
        validate_json('{"name": "Discovery", "year": "not-a-year"}', Album)

    messages = exc_info.value.messages()
    assert len(messages) == 1
    assert messages[0].index[-1] == "year"
    assert messages[0].start_position is not None
    assert messages[0].end_position is not None


def test_validate_json_raises_parse_error_for_invalid_json():
    with pytest.raises(ParseError) as exc_info:
        validate_json('{"name": ', Album)

    messages = exc_info.value.messages()
    assert len(messages) == 1
    assert messages[0].code == "parse_error"


def test_validate_json_raises_parse_error_for_empty_content():
    with pytest.raises(ParseError) as exc_info:
        validate_json("   ", Album)

    messages = exc_info.value.messages()
    assert len(messages) == 1
    assert messages[0].code == "no_content"


def test_validate_json_delegates_token_to_validate_with_positions(monkeypatch):
    calls = []
    sentinel_token = object()
    sentinel_result = object()

    def fake_tokenize_json(content):
        calls.append(("tokenize_json", content))
        return sentinel_token

    def fake_validate_with_positions(token, validator):
        calls.append(("validate_with_positions", token, validator))
        return sentinel_result

    monkeypatch.setattr(tokenize_json_module, "tokenize_json", fake_tokenize_json)
    monkeypatch.setattr(
        tokenize_json_module, "validate_with_positions", fake_validate_with_positions
    )

    result = validate_json('{"name": "Discovery", "year": 2001}', Album)

    assert result is sentinel_result
    assert calls == [
        ("tokenize_json", '{"name": "Discovery", "year": 2001}'),
        ("validate_with_positions", sentinel_token, Album),
    ]
