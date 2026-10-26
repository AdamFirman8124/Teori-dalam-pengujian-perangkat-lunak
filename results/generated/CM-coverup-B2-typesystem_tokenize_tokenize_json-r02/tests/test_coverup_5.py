# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import pytest

from typesystem.base import ValidationError
from typesystem.fields import Integer, String
from typesystem.tokenize.tokenize_json import validate_json


def test_validate_json_returns_validated_json_value():
    result = validate_json('"hello"', String())

    assert result == "hello"


def test_validate_json_accepts_bytes_content():
    result = validate_json(b"42", Integer())

    assert result == 42


def test_validate_json_raises_positioned_validation_error():
    with pytest.raises(ValidationError) as exc_info:
        validate_json('"not an integer"', Integer())

    error = exc_info.value
    assert error.messages()
    assert error.messages()[0].code == "type"
