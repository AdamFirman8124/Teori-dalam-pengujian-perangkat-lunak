# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import importlib
from unittest.mock import Mock


def test_validate_json_tokenizes_content_and_validates_token(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_json")
    content = '{"name": "example"}'
    validator = object()
    token = object()
    expected = object()

    tokenize_json = Mock(return_value=token)
    validate_with_positions = Mock(return_value=expected)
    monkeypatch.setattr(module, "tokenize_json", tokenize_json)
    monkeypatch.setattr(
        module, "validate_with_positions", validate_with_positions
    )

    result = module.validate_json(content, validator)

    assert result is expected
    tokenize_json.assert_called_once_with(content)
    validate_with_positions.assert_called_once_with(
        token=token, validator=validator
    )
