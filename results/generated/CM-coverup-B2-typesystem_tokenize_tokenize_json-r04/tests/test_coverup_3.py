# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import importlib

from json.decoder import JSONDecoder


def test_tokenizing_decoder_initializes_scanner_with_content(monkeypatch):
    tokenize_json_module = importlib.import_module(
        "typesystem.tokenize.tokenize_json"
    )
    content = '{"answer": 42}'
    scanner = object()
    calls = []

    def fake_make_scanner(context, supplied_content):
        calls.append((context, supplied_content))
        return scanner

    monkeypatch.setattr(tokenize_json_module, "_make_scanner", fake_make_scanner)

    decoder = tokenize_json_module._TokenizingDecoder(
        content=content,
        strict=False,
    )

    assert isinstance(decoder, JSONDecoder)
    assert decoder.strict is False
    assert calls == [(decoder, content)]
    assert decoder.scan_once is scanner
