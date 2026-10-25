# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import importlib

import pytest

from typesystem import fields


@pytest.fixture
def yaml_module():
    return importlib.import_module("typesystem.tokenize.tokenize_yaml")


def test_validate_yaml_tokenizes_and_validates(monkeypatch, yaml_module):
    token = object()
    validator = fields.String()
    calls = []

    def fake_tokenize_yaml(content):
        calls.append(("tokenize_yaml", content))
        return token

    def fake_validate_with_positions(*, token, validator):
        calls.append(("validate_with_positions", token, validator))
        return "validated"

    monkeypatch.setattr(yaml_module, "tokenize_yaml", fake_tokenize_yaml)
    monkeypatch.setattr(
        yaml_module,
        "validate_with_positions",
        fake_validate_with_positions,
    )

    result = yaml_module.validate_yaml("name: alice", validator)

    assert result == "validated"
    assert calls == [
        ("tokenize_yaml", "name: alice"),
        ("validate_with_positions", token, validator),
    ]


def test_validate_yaml_requires_pyyaml(monkeypatch, yaml_module):
    def unexpected_tokenize_call(content):
        pytest.fail("tokenize_yaml must not be called when PyYAML is unavailable")

    monkeypatch.setattr(yaml_module, "yaml", None)
    monkeypatch.setattr(
        yaml_module,
        "tokenize_yaml",
        unexpected_tokenize_call,
    )

    with pytest.raises(
        AssertionError,
        match=r"^'pyyaml' must be installed\.$",
    ):
        yaml_module.validate_yaml("name: alice", fields.String())
