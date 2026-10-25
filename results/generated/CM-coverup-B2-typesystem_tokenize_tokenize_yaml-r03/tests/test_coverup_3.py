# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import importlib

import pytest


def test_validate_yaml_delegates_tokenization_and_validation(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    content = b"name: foo"
    validator = object()
    token = object()
    expected = ({"name": "foo"}, None)
    calls = {}

    def fake_tokenize_yaml(received_content):
        calls["content"] = received_content
        return token

    def fake_validate_with_positions(*, token, validator):
        calls["token"] = token
        calls["validator"] = validator
        return expected

    monkeypatch.setattr(module, "tokenize_yaml", fake_tokenize_yaml)
    monkeypatch.setattr(
        module, "validate_with_positions", fake_validate_with_positions
    )

    result = module.validate_yaml(content, validator)

    assert result is expected
    assert calls == {
        "content": content,
        "token": token,
        "validator": validator,
    }


def test_validate_yaml_requires_pyyaml(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")

    def unexpected_tokenize_call(content):
        pytest.fail("tokenize_yaml must not be called when PyYAML is unavailable")

    monkeypatch.setattr(module, "yaml", None)
    monkeypatch.setattr(module, "tokenize_yaml", unexpected_tokenize_call)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        module.validate_yaml("name: foo", object())
