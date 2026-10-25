# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import importlib

import pytest


def test_validate_yaml_tokenizes_and_validates_with_positions(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    token = object()
    validator = object()
    expected = object()
    calls = []

    def fake_tokenize_yaml(content):
        calls.append(("tokenize_yaml", content))
        return token

    def fake_validate_with_positions(*, token, validator):
        calls.append(("validate_with_positions", token, validator))
        return expected

    monkeypatch.setattr(module, "yaml", object())
    monkeypatch.setattr(module, "tokenize_yaml", fake_tokenize_yaml)
    monkeypatch.setattr(
        module, "validate_with_positions", fake_validate_with_positions
    )

    result = module.validate_yaml("name: example", validator)

    assert result is expected
    assert calls == [
        ("tokenize_yaml", "name: example"),
        ("validate_with_positions", token, validator),
    ]


def test_validate_yaml_requires_pyyaml(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_yaml")
    tokenize_called = False

    def fake_tokenize_yaml(content):
        nonlocal tokenize_called
        tokenize_called = True
        pytest.fail("tokenize_yaml must not be called when PyYAML is unavailable")

    monkeypatch.setattr(module, "yaml", None)
    monkeypatch.setattr(module, "tokenize_yaml", fake_tokenize_yaml)

    with pytest.raises(
        AssertionError, match=r"^'pyyaml' must be installed\.$"
    ):
        module.validate_yaml("name: example", object())

    assert tokenize_called is False
