# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import pytest
from typesystem.base import ValidationError
from typesystem.fields import Integer, String
from typesystem.schemas import Schema
from typesystem.tokenize.tokenize_json import validate_json


def test_validate_json_with_field_str_content():
    validator = String()
    result = validate_json('"hello"', validator)
    assert result == "hello"


def test_validate_json_with_field_bytes_content():
    validator = String()
    result = validate_json(b'"hello"', validator)
    assert result == "hello"


def test_validate_json_with_schema_class():
    class User(Schema):
        name = String()
        age = Integer()

    result = validate_json('{"name": "tom", "age": 3}', User)
    if isinstance(result, dict):
        assert result == {"name": "tom", "age": 3}
    else:
        assert result.name == "tom"
        assert result.age == 3


def test_validate_json_validation_error_includes_positions():
    validator = Integer()
    with pytest.raises(ValidationError) as exc_info:
        validate_json('"not-an-int"', validator)
    messages = exc_info.value.messages()
    assert len(messages) == 1
    message = messages[0]
    assert message.text is not None
    assert message.start_position is not None
    assert message.end_position is not None
