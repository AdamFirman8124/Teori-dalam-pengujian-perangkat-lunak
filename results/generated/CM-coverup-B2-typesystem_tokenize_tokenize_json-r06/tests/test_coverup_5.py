# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import pytest

from typesystem.base import ValidationError
from typesystem.fields import String
from typesystem.tokenize.tokenize_json import validate_json


@pytest.mark.parametrize("content", ['"hello"', b'"hello"'])
def test_validate_json_returns_validated_value(content):
    result = validate_json(content, String())

    assert result == "hello"


def test_validate_json_raises_validation_error_for_invalid_value():
    with pytest.raises(ValidationError) as exc_info:
        validate_json("123", String())

    assert exc_info.value.messages()
