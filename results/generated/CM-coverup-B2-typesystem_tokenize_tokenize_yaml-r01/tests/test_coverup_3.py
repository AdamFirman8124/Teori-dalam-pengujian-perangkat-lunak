# file: project/typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest

from typesystem import fields, schemas
from typesystem.base import ParseError, ValidationError
from typesystem.tokenize.tokenize_yaml import validate_yaml


class Example(schemas.Schema):
    text = fields.String()


def test_validate_yaml_success():
    value = validate_yaml("text: hello", validator=Example)
    assert isinstance(value, Example)
    assert value["text"] == "hello"
    assert dict(value) == {"text": "hello"}


def test_validate_yaml_bytes_content():
    value = validate_yaml(b"text: hello", validator=Example)
    assert isinstance(value, Example)
    assert value["text"] == "hello"


def test_validate_yaml_field_validator():
    value = validate_yaml("hello", validator=fields.String())
    assert value == "hello"


def test_validate_yaml_parse_error():
    with pytest.raises(ParseError) as exc_info:
        validate_yaml("text: hello\n  bad_indent: [", validator=Example)
    message = exc_info.value.messages()[0]
    assert message.code == "parse_error"
    assert message.start_position is not None


def test_validate_yaml_validation_error():
    with pytest.raises(ValidationError) as exc_info:
        validate_yaml("text: 123", validator=Example)
    message = exc_info.value.messages()[0]
    assert message.text == "Must be a string."
    assert message.start_position.line_no == 1
    assert message.start_position.column_no == 7


def test_validate_yaml_missing_pyyaml(monkeypatch):
    import typesystem.tokenize.tokenize_yaml as tokenize_yaml_module

    monkeypatch.setattr(tokenize_yaml_module, "yaml", None)
    with pytest.raises(AssertionError) as exc_info:
        tokenize_yaml_module.validate_yaml("text: hello", validator=Example)
    assert "'pyyaml' must be installed." in str(exc_info.value)
