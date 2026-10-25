# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import pytest

from typesystem.base import ValidationError
from typesystem.fields import Integer
from typesystem.tokenize.tokenize_json import validate_json


def test_validate_json_returns_validated_value():
    value = validate_json("123", validator=Integer())

    assert value == 123


def test_validate_json_raises_positionally_marked_validation_error():
    with pytest.raises(ValidationError) as exc_info:
        validate_json('"not an integer"', validator=Integer())

    messages = exc_info.value.messages()

    assert messages
    assert all(message.code for message in messages)
    assert all(message.start_position is not None for message in messages)
    assert all(message.end_position is not None for message in messages)
