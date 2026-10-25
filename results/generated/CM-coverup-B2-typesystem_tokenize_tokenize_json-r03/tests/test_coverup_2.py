# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import importlib
from unittest.mock import Mock


def test_validate_json_tokenizes_content_and_validates_token(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_json")
    content = b'{"name": "example"}'
    validator = object()
    token = object()
    expected = object()

    tokenize = Mock(return_value=token)
    validate = Mock(return_value=expected)
    monkeypatch.setattr(module, "tokenize_json", tokenize)
    monkeypatch.setattr(module, "validate_with_positions", validate)

    result = module.validate_json(content, validator)

    assert result is expected
    tokenize.assert_called_once_with(content)
    validate.assert_called_once_with(token=token, validator=validator)
