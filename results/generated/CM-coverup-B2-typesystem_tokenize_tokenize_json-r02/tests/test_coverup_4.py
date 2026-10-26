# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import json

import pytest

import typesystem.tokenize.tokenize_json as tokenize_json_module
from typesystem.tokenize.tokenize_json import _TokenizingDecoder, tokenize_json
from typesystem.tokenize.tokens import ScalarToken


def test_tokenizing_decoder_pops_content_and_sets_scan_once(monkeypatch):
    calls = []
    sentinel = object()

    def fake_make_scanner(decoder, content):
        calls.append((decoder, content))
        return sentinel

    monkeypatch.setattr(tokenize_json_module, "_make_scanner", fake_make_scanner)

    decoder = _TokenizingDecoder(content='{"a": 1}')

    assert decoder.scan_once is sentinel
    assert len(calls) == 1
    assert calls[0][0] is decoder
    assert calls[0][1] == '{"a": 1}'


def test_tokenizing_decoder_passes_remaining_kwargs_to_jsondecoder(monkeypatch):
    calls = []

    def fake_make_scanner(decoder, content):
        calls.append((decoder, content))
        return lambda *args, **kwargs: (None, 0)

    monkeypatch.setattr(tokenize_json_module, "_make_scanner", fake_make_scanner)

    decoder = _TokenizingDecoder(content="1", strict=False)

    assert decoder.strict is False
    assert len(calls) == 1
    assert calls[0][1] == "1"


def test_tokenizing_decoder_requires_content_kwarg():
    with pytest.raises(KeyError):
        _TokenizingDecoder()


def test_tokenize_json_uses_tokenizing_decoder():
    token = tokenize_json('{"a": [1, 2], "b": null}')

    assert isinstance(token, ScalarToken) or token.value == {"a": [1, 2], "b": None}
    assert token.value == {"a": [1, 2], "b": None}


def test_tokenize_json_accepts_bytes_content():
    token = tokenize_json(b'{"a": 1}')

    assert token.value == {"a": 1}


def test_tokenize_json_raises_parse_error_for_invalid_json():
    from typesystem.base import ParseError

    with pytest.raises(ParseError):
        tokenize_json("{invalid")
