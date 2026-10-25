# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import importlib
from unittest.mock import Mock

import pytest


tokenize_yaml_module = importlib.import_module(
    "typesystem.tokenize.tokenize_yaml"
)


def test_validate_yaml_tokenizes_and_validates(monkeypatch):
    token = object()
    validator = object()
    expected = object()
    tokenize = Mock(return_value=token)
    validate = Mock(return_value=expected)

    monkeypatch.setattr(tokenize_yaml_module, "tokenize_yaml", tokenize)
    monkeypatch.setattr(
        tokenize_yaml_module, "validate_with_positions", validate
    )

    result = tokenize_yaml_module.validate_yaml("name: example", validator)

    assert result is expected
    tokenize.assert_called_once_with("name: example")
    validate.assert_called_once_with(token=token, validator=validator)


def test_validate_yaml_requires_pyyaml(monkeypatch):
    tokenize = Mock()
    validate = Mock()

    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)
    monkeypatch.setattr(tokenize_yaml_module, "tokenize_yaml", tokenize)
    monkeypatch.setattr(
        tokenize_yaml_module, "validate_with_positions", validate
    )

    with pytest.raises(
        AssertionError, match="'pyyaml' must be installed"
    ):
        tokenize_yaml_module.validate_yaml("name: example", object())

    tokenize.assert_not_called()
    validate.assert_not_called()
