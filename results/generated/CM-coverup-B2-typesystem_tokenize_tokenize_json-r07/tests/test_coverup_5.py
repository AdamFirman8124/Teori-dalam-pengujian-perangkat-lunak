# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

from unittest.mock import MagicMock

from typesystem.tokenize.tokenize_json import validate_json


def test_validate_json_str_content_success():
    validator = MagicMock()
    validator.validate.return_value = {"validated": True}
    result = validate_json('{"a": 1}', validator)
    assert result == {"validated": True}
    validator.validate.assert_called_once_with({"a": 1})


def test_validate_json_bytes_content_success():
    validator = MagicMock()
    validator.validate.return_value = [1, 2, 3]
    result = validate_json(b'[1, 2, 3]', validator)
    assert result == [1, 2, 3]
    validator.validate.assert_called_once_with([1, 2, 3])


def test_validate_json_delegates_to_tokenize_and_validate_with_positions():
    validator = MagicMock()
    sentinel = object()
    validator.validate.return_value = sentinel
    result = validate_json('{"x": null}', validator)
    assert result is sentinel
    validator.validate.assert_called_once_with({"x": None})
