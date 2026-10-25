# file: project/typesystem/tokenize/tokenize_json.py:165-180
# asked: {"lines": [166, 167, 169, 171, 172, 174, 175, 176, 177, 179, 180], "branches": [[166, 167], [166, 169], [169, 171], [169, 174]]}
# gained: {"lines": [166, 167, 169, 171, 172, 174, 175, 176, 177, 179, 180], "branches": [[166, 167], [166, 169], [169, 171], [169, 174]]}

import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokenize_json import tokenize_json
from typesystem.tokenize.tokens import Token


def test_tokenize_json_from_bytes():
    token = tokenize_json(b'{"key": "value"}')
    assert isinstance(token, Token)
    assert token.value == {"key": "value"}


def test_tokenize_json_empty_content():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("   \n\t ")
    error = exc_info.value
    (message,) = error.messages()
    assert message.text == "No content."
    assert message.code == "no_content"
    assert message.start_position == Position(line_no=1, column_no=1, char_index=0)


def test_tokenize_json_invalid_json():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json('{"key": "value"')
    error = exc_info.value
    (message,) = error.messages()
    assert message.code == "parse_error"
    assert message.text.endswith(".")
    assert message.start_position.line_no == 1
    assert message.start_position.column_no == 16
    assert message.start_position.char_index == 15


def test_tokenize_json_invalid_json_multiline():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json('{\n  "key": "value"\n')
    error = exc_info.value
    (message,) = error.messages()
    assert message.code == "parse_error"
    assert message.text.endswith(".")
    assert message.start_position.line_no == 3
    assert message.start_position.column_no == 1
    assert message.start_position.char_index == 19
