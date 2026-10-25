# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import importlib

import pytest


tokenize_yaml_module = importlib.import_module("typesystem.tokenize.tokenize_yaml")


def test_validate_yaml_tokenizes_and_validates_with_positions(monkeypatch):
    token = object()
    validator = object()
    calls = {}

    def fake_tokenize_yaml(content):
        calls["content"] = content
        return token

    def fake_validate_with_positions(**kwargs):
        calls["validation_kwargs"] = kwargs
        return "validated-value"

    monkeypatch.setattr(tokenize_yaml_module, "tokenize_yaml", fake_tokenize_yaml)
    monkeypatch.setattr(
        tokenize_yaml_module,
        "validate_with_positions",
        fake_validate_with_positions,
    )

    result = tokenize_yaml_module.validate_yaml("name: example", validator)

    assert result == "validated-value"
    assert calls == {
        "content": "name: example",
        "validation_kwargs": {"token": token, "validator": validator},
    }


def test_validate_yaml_requires_pyyaml(monkeypatch):
    def fail_if_called(*args, **kwargs):
        pytest.fail("Validation must stop before tokenization when PyYAML is unavailable")

    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)
    monkeypatch.setattr(tokenize_yaml_module, "tokenize_yaml", fail_if_called)
    monkeypatch.setattr(
        tokenize_yaml_module,
        "validate_with_positions",
        fail_if_called,
    )

    with pytest.raises(AssertionError, match="'pyyaml' must be installed\\."):
        tokenize_yaml_module.validate_yaml("name: example", object())
