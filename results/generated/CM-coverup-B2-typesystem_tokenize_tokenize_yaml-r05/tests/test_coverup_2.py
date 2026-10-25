# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest

import typesystem.tokenize.tokenize_yaml as tokenize_yaml_module
from typesystem import fields
from typesystem.base import ValidationError
from typesystem.schemas import Schema
from typesystem.tokenize.tokenize_yaml import validate_yaml


def test_validate_yaml_with_valid_field():
    value = validate_yaml("123", validator=fields.Integer())

    assert value == 123


def test_validate_yaml_with_valid_field_from_bytes():
    value = validate_yaml(b"123", validator=fields.Integer())

    assert value == 123


def test_validate_yaml_with_valid_schema():
    class Example(Schema):
        a = fields.Integer()
        b = fields.String()

    value = validate_yaml("a: 1\nb: 'example'\n", validator=Example)

    if isinstance(value, dict):
        assert value == {"a": 1, "b": "example"}
    else:
        assert value.a == 1
        assert value.b == "example"


def test_validate_yaml_with_invalid_value_raises_positional_error():
    class Example(Schema):
        a = fields.Integer()
        b = fields.String()

    with pytest.raises(ValidationError) as exc_info:
        validate_yaml("a: 'not-an-integer'\n", validator=Example)

    assert len(exc_info.value.messages()) >= 1


def test_validate_yaml_delegates_to_tokenize_and_validate(monkeypatch):
    calls = {}
    sentinel_token = object()
    sentinel_validator = object()
    expected = {"a": 1}

    def fake_tokenize_yaml(content):
        calls["content"] = content
        return sentinel_token

    def fake_validate_with_positions(*, token, validator):
        calls["token"] = token
        calls["validator"] = validator
        return expected

    monkeypatch.setattr(
        tokenize_yaml_module, "tokenize_yaml", fake_tokenize_yaml
    )
    monkeypatch.setattr(
        tokenize_yaml_module,
        "validate_with_positions",
        fake_validate_with_positions,
    )

    result = validate_yaml("a: 1\n", validator=sentinel_validator)

    assert result is expected
    assert calls == {
        "content": "a: 1\n",
        "token": sentinel_token,
        "validator": sentinel_validator,
    }


def test_validate_yaml_without_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)

    with pytest.raises(AssertionError, match="'pyyaml' must be installed\\."):
        validate_yaml("a: 1\n", validator=fields.Integer())
