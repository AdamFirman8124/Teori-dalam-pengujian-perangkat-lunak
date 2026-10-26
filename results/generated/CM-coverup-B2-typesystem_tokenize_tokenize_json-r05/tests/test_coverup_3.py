# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest
from json.decoder import JSONDecoder

from typesystem.tokenize.tokenize_json import _TokenizingDecoder, tokenize_json
from typesystem.tokenize.tokens import Token


def test_tokenizing_decoder_init_pops_content_and_sets_scan_once():
    decoder = _TokenizingDecoder(content='{"a": 1}')

    assert isinstance(decoder, JSONDecoder)
    assert callable(decoder.scan_once)


def test_tokenizing_decoder_init_forwards_kwargs_to_super():
    def object_hook(obj):
        return obj

    decoder = _TokenizingDecoder(object_hook=object_hook, content='{"a": 1}')

    assert decoder.object_hook is object_hook
    assert callable(decoder.scan_once)


def test_tokenizing_decoder_scan_once_returns_token():
    decoder = _TokenizingDecoder(content='true')

    token, end = decoder.scan_once('true', 0)

    assert isinstance(token, Token)
    assert token.value is True
    assert end == 4


def test_tokenizing_decoder_decode_returns_token():
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)

    result = decoder.decode(content)

    assert isinstance(result, Token)


def test_tokenize_json_executes_tokenizing_decoder_init():
    result = tokenize_json('{"a": 1}')

    assert isinstance(result, Token)


def test_tokenize_json_bytes_executes_tokenizing_decoder_init():
    result = tokenize_json(b'[1, 2, 3]')

    assert isinstance(result, Token)
