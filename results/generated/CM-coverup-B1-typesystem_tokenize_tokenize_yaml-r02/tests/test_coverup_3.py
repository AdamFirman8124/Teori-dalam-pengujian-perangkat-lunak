# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import importlib

import pytest
from typesystem.fields import String


tokenize_yaml_module = importlib.import_module(
    "typesystem.tokenize.tokenize_yaml"
)


def test_validate_yaml_parses_and_validates_content():
    result = tokenize_yaml_module.validate_yaml("hello", String())

    assert result == "hello"


def test_validate_yaml_requires_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        tokenize_yaml_module.validate_yaml("hello", String())
