# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest

import typesystem.tokenize.tokenize_yaml as tokenize_yaml_module
from typesystem.base import ValidationError
from typesystem.fields import Integer, String
from typesystem.schemas import Schema
from typesystem.tokenize.tokenize_yaml import validate_yaml


def test_validate_yaml_with_field_valid():
    value = validate_yaml("hello", String())

    assert value == "hello"


def test_validate_yaml_with_field_bytes_content():
    value = validate_yaml(b"123", Integer())

    assert value == 123


def test_validate_yaml_with_schema_valid():
    class Person(Schema):
        name = String()
        age = Integer()

    value = validate_yaml("name: tom\nage: 20\n", Person)

    if hasattr(value, "name"):
        assert value.name == "tom"
        assert value.age == 20
    else:
        assert value["name"] == "tom"
        assert value["age"] == 20


def test_validate_yaml_with_field_invalid():
    with pytest.raises(ValidationError) as exc_info:
        validate_yaml("abc", Integer())

    messages = exc_info.value.messages()
    assert messages
    assert all(getattr(message, "text", None) for message in messages)


def test_validate_yaml_with_schema_invalid():
    class Person(Schema):
        name = String()
        age = Integer()

    with pytest.raises(ValidationError) as exc_info:
        validate_yaml("name: tom\nage: abc\n", Person)

    messages = exc_info.value.messages()
    assert messages
    assert all(getattr(message, "text", None) for message in messages)


def test_validate_yaml_requires_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)

    with pytest.raises(AssertionError, match=r"pyyaml.*must be installed"):
        validate_yaml("123", Integer())
