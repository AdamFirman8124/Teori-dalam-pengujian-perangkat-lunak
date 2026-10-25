# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest
import typesystem.tokenize.tokenize_yaml as tokenize_yaml_module
from typesystem.tokenize.tokenize_yaml import validate_yaml
from typesystem.fields import Integer, String
from typesystem.schemas import Schema
from typesystem.base import ValidationError


class PersonSchema(Schema):
    name = String(max_length=100)
    age = Integer()


def test_validate_yaml_scalar_string():
    value = validate_yaml("hello", String())
    assert value == "hello"


def test_validate_yaml_bytes_content():
    value = validate_yaml(b"hello", String())
    assert value == "hello"


def test_validate_yaml_mapping_with_schema():
    result = validate_yaml("name: Alice\nage: 30\n", PersonSchema)
    if isinstance(result, dict):
        assert result["name"] == "Alice"
        assert result["age"] == 30
    else:
        assert result.name == "Alice"
        assert result.age == 30


def test_validate_yaml_validation_error_has_positions():
    with pytest.raises(ValidationError) as exc_info:
        validate_yaml("not-an-int", Integer())
    messages = exc_info.value.messages()
    assert len(messages) >= 1
    msg = messages[0]
    assert msg.text
    assert msg.start_position is not None
    assert msg.end_position is not None
    assert msg.start_position.char_index >= 0


def test_validate_yaml_requires_pyyaml(monkeypatch):
    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)
    with pytest.raises(AssertionError, match="pyyaml"):
        validate_yaml("hello", String())
