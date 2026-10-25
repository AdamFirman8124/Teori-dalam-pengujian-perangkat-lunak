# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import importlib
from unittest.mock import Mock

import pytest


def test_validate_yaml_tokenizes_and_validates_with_positions(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    content = "answer: 42"
    validator = object()
    token = object()
    expected = object()
    tokenize = Mock(return_value=token)
    validate = Mock(return_value=expected)

    monkeypatch.setattr(module, "yaml", object())
    monkeypatch.setattr(module, "tokenize_yaml", tokenize)
    monkeypatch.setattr(module, "validate_with_positions", validate)

    result = module.validate_yaml(content, validator)

    assert result is expected
    tokenize.assert_called_once_with(content)
    validate.assert_called_once_with(token=token, validator=validator)


def test_validate_yaml_requires_pyyaml(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    tokenize = Mock()
    validate = Mock()

    monkeypatch.setattr(module, "yaml", None)
    monkeypatch.setattr(module, "tokenize_yaml", tokenize)
    monkeypatch.setattr(module, "validate_with_positions", validate)

    with pytest.raises(AssertionError) as exc_info:
        module.validate_yaml("answer: 42", object())

    assert str(exc_info.value) == "'pyyaml' must be installed."
    tokenize.assert_not_called()
    validate.assert_not_called()
