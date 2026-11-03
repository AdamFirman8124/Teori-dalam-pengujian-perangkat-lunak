

# Generated at 2026-11-01 23:33:11.068758
# Unit test for function validate_json

# Generated at 2026-11-01 23:35:14.969382
# Unit test for function validate_json

# Generated at 2026-11-01 23:36:48.565978
# Unit test for function validate_json

# Generated at 2026-11-01 23:37:55.031892
# Unit test for function validate_json
def test_validate_json():
    from typesystem.fields import Integer, String

    # Successful validation with a simple field.
    value, error = module_0.validate_json('{"a": 1}', Field())
    assert value == {"a": 1}
    assert error is None

    # Successful validation with a schema.
    class Book(Schema):
        title = String()
        num_pages = Integer()

    value, error = module_0.validate_json(
        '{"title": "Frankenstein", "num_pages": 280}', Book
    )
    assert value == {"title": "Frankenstein", "num_pages": 280}
    assert error is None

    # Validation failure returns positionally marked error messages.
    value, error = module_0.validate_json('{"title": 123, "num_pages": "x"}', Book)
    assert value is None
    assert error is not None
    assert len(error.messages()) == 2

    # Parse error on malformed JSON.
    try:
        module_0.validate_json('{"a": }', Field())
    except ParseError as exc:
        assert exc.code == "parse_error"
        assert exc.position.line_no == 1
        assert exc.position.column_no == 7
    else:
        raise AssertionError("ParseError not raised")

    # Parse error on empty content.
    try:
        module_0.validate_json("", Field())
    except ParseError as exc:
        assert exc.code == "no_content"
    else:
        raise AssertionError("ParseError not raised")

    # Bytes input is decoded as UTF-8.
    value, error = module_0.validate_json(b'{"a": 2}', Field())
    assert value == {"a": 2}
    assert error is None

# Generated at 2026-11-01 23:38:29.736117
# Unit test for function validate_json
def test_validate_json():import pytest

from typesystem import String, Integer, Array, Schema
from typesystem.base import Message, ParseError, Position, ValidationError
from typesystem.tokenize.tokenize_json import validate_json


class Book(Schema):
    title = String()
    author = String()


def test_validate_json_valid():
    content = '{"title": "Frankenstein", "author": "Mary Shelley"}'
    value, error = module_0.validate_json(content, validator=Book)
    assert error is None
    assert value == {"title": "Frankenstein", "author": "Mary Shelley"}


def test_validate_json_bytes():
    content = b'{"title": "Frankenstein", "author": "Mary Shelley"}'
    value, error = module_0.validate_json(content, validator=Book)
    assert error is None
    assert value == {"title": "Frankenstein", "author": "Mary Shelley"}


def test_validate_json_validation_error():
    content = '{"title": 123, "author": "Mary Shelley"}'
    value, error = module_0.validate_json(content, validator=Book)
    assert value is None
    assert isinstance(error, Message)
    assert error.code == "type_error"
    assert error.index == ["title"]
    assert error.start_position.char_index == 11
    assert error.start_position.line_no == 1
    assert error.start_position.column_no == 12


def test_validate_json_missing_property():
    content = '{"title": "Frankenstein"}'
    value, error = module_0.validate_json(content, validator=Book)
    assert value is None
    assert isinstance(error, Message)
    assert error.code == "required"
    assert error.index == []


def test_validate_json_parse_error():
    content = '{"title": "Frankenstein"'
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_json(content, validator=Book)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position == Position(
        column_no=24, line_no=1, char_index=23
    )


def test_validate_json_empty_string():
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_json("", validator=Book)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1, line_no=1, char_index=0
    )


def test_validate_json_whitespace_only():
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_json("  \n\t ", validator=Book)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1, line_no=1, char_index=0
    )


def test_validate_json_multiple_lines():
    content = '{\n  "title": "Frankenstein",\n  "author": 123\n}'
    value, error = module_0.validate_json(content, validator=Book)
    assert value is None
    assert isinstance(error, Message)
    assert error.index == ["author"]
    assert error.start_position.line_no == 3
    assert error.start_position.column_no == 13

# Generated at 2026-11-01 23:39:15.957819
# Unit test for function tokenize_json
def test_tokenize_json():
    # A simple string tokenizes into a ScalarToken.
    token = module_0.tokenize_json('"abc"')
    assert isinstance(token, ScalarToken)
    assert token.value == "abc"
    assert token.start == 0
    assert token.end == 4

    # Bytes input is decoded to utf-8.
    token = module_0.tokenize_json(b'"abc"')
    assert isinstance(token, ScalarToken)
    assert token.value == "abc"

    # Numbers tokenize into ScalarTokens.
    token = module_0.tokenize_json("123")
    assert isinstance(token, ScalarToken)
    assert token.value == 123
    assert token.start == 0
    assert token.end == 2

    token = module_0.tokenize_json("1.5")
    assert isinstance(token, ScalarToken)
    assert token.value == 1.5

    # Booleans and null tokenize into ScalarTokens.
    assert module_0.tokenize_json("true").value is True
    assert module_0.tokenize_json("false").value is False
    assert module_0.tokenize_json("null").value is None

    # Dicts tokenize into DictTokens containing ScalarTokens.
    token = module_0.tokenize_json('{"a": 1}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == 7
    assert token.value["a"].value == 1
    assert token.value["a"].start == 6
    assert token.value["a"].end == 6
    key = list(token.value.keys())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "a"

    # Nested structures tokenize recursively.
    token = module_0.tokenize_json('{"a": [1, "b", {"c": true}]}')
    assert isinstance(token, DictToken)
    assert isinstance(token.value["a"], ListToken)
    items = token.value["a"].value
    assert [item.value for item in items] == [1, "b", {"c": True}]
    assert isinstance(items[2], DictToken)

    # Whitespace is skipped and positions reflect the original content.
    token = module_0.tokenize_json('  {"a" : 1}  ')
    assert isinstance(token, DictToken)
    assert token.start == 2
    assert token.end == 11

    # Empty content raises a "no_content" parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("")
    assert exc_info.value.code == "no_content"
    assert exc_info.value.text == "No content."
    assert exc_info.value.position == Position(
        column_no=1, line_no=1, char_index=0
    )

    # Whitespace-only content also raises "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("   \n\t ")
    assert exc_info.value.code == "no_content"

    # Invalid JSON raises a "parse_error" with position information.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("{")
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 2

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"a" 1}')
    assert exc_info.value.code == "parse_error"

    # A multi-line document reports the correct line number on error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{\n  "a": 1,\n}')
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no == 3

    # Non-utf8 bytes decode with errors ignored, yielding no content.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(b"\xff\xfe")
    assert exc_info.value.code == "no_content"

# Generated at 2026-11-01 23:40:32.417185
# Unit test for function validate_json

# Generated at 2026-11-01 23:42:11.438593
# Unit test for function validate_json