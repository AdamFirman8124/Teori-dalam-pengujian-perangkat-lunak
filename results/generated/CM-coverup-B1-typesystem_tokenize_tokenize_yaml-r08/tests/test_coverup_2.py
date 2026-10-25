# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest
import typesystem.tokenize.tokenize_yaml as tokenize_yaml_module
from typesystem.tokenize.tokenize_yaml import validate_yaml
from typesystem.fields import String
from typesystem.schemas import Schema
from typesystem.base import ParseError, ValidationError


def test_validate_yaml_field_str_success():
    value = validate_yaml("hello", validator=String())
    assert value == "hello"


def test_validate_yaml_field_bytes_success():
    value = validate_yaml(b"hello", validator=String())
    assert value == "hello"


def test_validate_yaml_schema_success():
    class User(Schema):
        name = String()

    value = validate_yaml("name: Alice", validator=User)
    assert isinstance(value, User)
    assert value.name == "Alice"


def test_validate_yaml_validation_error_has_positions():
    with pytest.raises(ValidationError) as exc_info:
        validate_yaml("hello", validator=String(max_length=2))
    messages = exc_info.value.messages()
    assert len(messages) == 1
    msg = messages[0]
    assert msg.code == "max_length"
    assert msg.start_position is not None
    assert msg.end_position is not None


def test_validate_yaml_assert_without_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)
    with pytest.raises(AssertionError, match="'pyyaml' must be installed"):
        validate_yaml("hello", validator=String())


def test_validate_yaml_propagates_parse_error():
    with pytest.raises(ParseError):
        validate_yaml("   ", validator=String())
