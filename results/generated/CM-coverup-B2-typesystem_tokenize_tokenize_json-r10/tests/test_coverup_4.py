# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

from typesystem.tokenize.tokenize_json import _TokenizingDecoder


def test_tokenizing_decoder_init_sets_custom_scanner():
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)
    token, end = decoder.scan_once(content, 0)
    assert end == len(content)
    assert token is not None


def test_tokenizing_decoder_init_forwards_kwargs():
    content = '[1, 2, 3]'
    decoder = _TokenizingDecoder(content=content, strict=False)
    assert decoder.strict is False
    assert callable(decoder.scan_once)
    token, end = decoder.scan_once(content, 0)
    assert end == len(content)
    assert token is not None


def test_tokenizing_decoder_init_scan_once_uses_content():
    content = '"hello"'
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)
    token, end = decoder.scan_once(content, 0)
    assert end == len(content)
    # ScalarToken should wrap the string value
    assert token.value == "hello"
