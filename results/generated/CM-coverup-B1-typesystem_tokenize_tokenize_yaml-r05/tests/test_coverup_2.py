# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest

import typesystem
from typesystem.base import ParseError, ValidationError
from typesystem.tokenize.tokenize_yaml import validate_yaml


class Example(typesystem.Schema):
    name = typesystem.String(max_length=10)
    age = typesystem.Integer()


def test_validate_yaml_valid_string():
    content = "name: foo\nage: 42\n"
    value = validate_yaml(content, Example)
    assert isinstance(value, Example)
    assert value.name == "foo"
    assert value.age == 42
    assert dict(value) == {"name": "foo", "age": 42}


def test_validate_yaml_valid_bytes():
    content = b"name: foo\nage: 42\n"
    value = validate_yaml(content, Example)
    assert isinstance(value, Example)
    assert value.name == "foo"
    assert value.age == 42


def test_validate_yaml_with_field_validator():
    value = validate_yaml("123", typesystem.Integer())
    assert value == 123


def test_validate_yaml_parse_error():
    with pytest.raises(ParseError) as exc_info:
        validate_yaml("{invalid", Example)
    exc = exc_info.value
    text = getattr(exc, "text", str(exc))
    assert text
    if hasattr(exc, "code"):
        assert exc.code == "parse_error"
    if hasattr(exc, "position"):
        assert exc.position is not None


def test_validate_yaml_no_content_error():
    with pytest.raises(ParseError) as exc_info:
        validate_yaml("", Example)
    exc = exc_info.value
    text = getattr(exc, "text", str(exc))
    assert text
    if hasattr(exc, "code"):
        assert exc.code == "no_content"


def test_validate_yaml_validation_error_positions():
    content = "name: a-very-long-name-exceeding-limit\nage: 42\n"
    with pytest.raises(ValidationError) as exc_info:
        validate_yaml(content, Example)
    messages = exc_info.value.messages()
    assert len(messages) == 1
    message = messages[0]
    assert message.index is not None
    assert message.start_position is not None
    assert message.end_position is not None
