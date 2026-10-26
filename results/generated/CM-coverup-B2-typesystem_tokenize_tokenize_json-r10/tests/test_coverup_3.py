# file: project/typesystem/tokenize/tokenize_json.py:165-180
# asked: {"lines": [166, 167, 169, 171, 172, 174, 175, 176, 177, 179, 180], "branches": [[166, 167], [166, 169], [169, 171], [169, 174]]}
# gained: {"lines": [166, 167, 169, 171, 172, 174, 175, 176, 177, 179, 180], "branches": [[166, 167], [166, 169], [169, 171], [169, 174]]}

import pytest
from typesystem.base import ParseError
from typesystem.tokenize.tokenize_json import tokenize_json


def test_tokenize_json_valid_str():
    token = tokenize_json('{"a": 1}')
    assert token.value == {"a": 1}


def test_tokenize_json_valid_bytes():
    token = tokenize_json(b'{"a": 1}')
    assert token.value == {"a": 1}


def test_tokenize_json_bytes_with_invalid_utf8_ignored():
    token = tokenize_json(b'\xff{"a": 1}')
    assert token.value == {"a": 1}


def test_tokenize_json_empty_str():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("")
    assert isinstance(exc_info.value, ParseError)


def test_tokenize_json_whitespace_str():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("   \n\t  ")
    assert isinstance(exc_info.value, ParseError)


def test_tokenize_json_empty_bytes():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json(b"")
    assert isinstance(exc_info.value, ParseError)


def test_tokenize_json_parse_error_str():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("{invalid}")
    assert isinstance(exc_info.value, ParseError)


def test_tokenize_json_parse_error_bytes():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json(b"{invalid}")
    assert isinstance(exc_info.value, ParseError)
