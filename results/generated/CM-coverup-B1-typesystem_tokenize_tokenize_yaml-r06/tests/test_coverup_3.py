# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import importlib

import pytest


def test_validate_yaml_tokenizes_and_validates(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    token = object()
    validator = object()
    expected = object()
    calls = {}

    def fake_tokenize_yaml(content):
        calls["content"] = content
        return token

    def fake_validate_with_positions(*, token, validator):
        calls["token"] = token
        calls["validator"] = validator
        return expected

    monkeypatch.setattr(module, "tokenize_yaml", fake_tokenize_yaml)
    monkeypatch.setattr(
        module, "validate_with_positions", fake_validate_with_positions
    )

    result = module.validate_yaml("name: example", validator)

    assert result is expected
    assert calls == {
        "content": "name: example",
        "token": token,
        "validator": validator,
    }


def test_validate_yaml_requires_pyyaml(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    monkeypatch.setattr(module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        module.validate_yaml("name: example", object())
