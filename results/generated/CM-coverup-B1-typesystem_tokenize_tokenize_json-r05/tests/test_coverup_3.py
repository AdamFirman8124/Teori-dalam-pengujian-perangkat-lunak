# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest

from typesystem.tokenize.tokenize_json import (
    _TokenizingDecoder,
    tokenize_json,
)
from typesystem.tokenize.tokens import Token


def test_tokenizing_decoder_init_sets_scan_once():
    content = '{"key": [1, 2, 3]}'
    decoder = _TokenizingDecoder(content=content)

    assert decoder.scan_once is not None
    assert callable(decoder.scan_once)
    token = decoder.decode(content)
    assert isinstance(token, Token)
    assert token.value == {"key": [1, 2, 3]}


def test_tokenizing_decoder_pops_content_kwarg():
    # If 'content' were forwarded to JSONDecoder.__init__ it would raise TypeError.
    decoder = _TokenizingDecoder(content="[1, 2]", object_hook=lambda obj: obj)

    token = decoder.decode("[1, 2]")
    assert isinstance(token, Token)
    assert token.value == [1, 2]


def test_tokenizing_decoder_scan_once_is_per_instance():
    first = _TokenizingDecoder(content="1")
    second = _TokenizingDecoder(content="2")

    assert first.scan_once is not second.scan_once
    assert first.decode("1").value == 1
    assert second.decode("2").value == 2


def test_tokenizing_decoder_requires_content():
    with pytest.raises(KeyError):
        _TokenizingDecoder()


def test_tokenize_json_constructs_tokenizing_decoder(monkeypatch):
    created = []
    original_init = _TokenizingDecoder.__init__

    def spy_init(self, *args, **kwargs):
        created.append(kwargs.get("content"))
        original_init(self, *args, **kwargs)

    monkeypatch.setattr(_TokenizingDecoder, "__init__", spy_init)

    token = tokenize_json('{"a": 1}')

    assert created == ['{"a": 1}']
    assert isinstance(token, Token)
    assert token.value == {"a": 1}
