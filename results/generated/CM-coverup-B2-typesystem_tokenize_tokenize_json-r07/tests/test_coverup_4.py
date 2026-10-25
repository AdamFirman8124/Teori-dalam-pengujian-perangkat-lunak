# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest
from json.decoder import JSONDecoder

import typesystem.tokenize.tokenize_json as tokenize_json_module
from typesystem.tokenize.tokenize_json import _TokenizingDecoder, tokenize_json
from typesystem.tokenize.tokens import DictToken, ScalarToken


def test_tokenizing_decoder_init_pops_content_and_builds_scanner():
    # Lines 160-162: content popped, super().__init__ called, scan_once replaced.
    decoder = _TokenizingDecoder(content='{"a": 1}')

    assert isinstance(decoder, JSONDecoder)
    assert callable(decoder.scan_once)

    token, end = decoder.scan_once('{"a": 1}', 0)
    assert isinstance(token, DictToken)
    assert end == len('{"a": 1}')
    assert token.value == {"a": 1}

    child = token._get_child_token("a")
    assert isinstance(child, ScalarToken)
    assert child.value == 1


def test_tokenizing_decoder_forwards_remaining_kwargs_to_jsondecoder():
    # Line 161: kwargs other than "content" reach JSONDecoder.__init__.
    decoder = _TokenizingDecoder(content="{}", strict=False)

    assert decoder.strict is False
    assert callable(decoder.scan_once)


def test_tokenizing_decoder_requires_content_kwarg():
    # Line 160: kwargs.pop("content") raises KeyError when absent.
    with pytest.raises(KeyError):
        _TokenizingDecoder()


def test_tokenizing_decoder_passes_self_and_content_to_make_scanner(monkeypatch):
    # Line 162: _make_scanner is called with (self, content) and its result stored.
    calls = []

    def fake_make_scanner(context, content):
        calls.append((context, content))
        return lambda string, idx: ("sentinel", idx)

    monkeypatch.setattr(tokenize_json_module, "_make_scanner", fake_make_scanner)

    decoder = _TokenizingDecoder(content="abc")

    assert len(calls) == 1
    context, content = calls[0]
    assert context is decoder
    assert content == "abc"
    assert decoder.scan_once("abc", 0) == ("sentinel", 0)


def test_tokenize_json_uses_tokenizing_decoder():
    token = tokenize_json('{"a": [1, 2]}')

    assert isinstance(token, DictToken)
    assert token.value == {"a": [1, 2]}
