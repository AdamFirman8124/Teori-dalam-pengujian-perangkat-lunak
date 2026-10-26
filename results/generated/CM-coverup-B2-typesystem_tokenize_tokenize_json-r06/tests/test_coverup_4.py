# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

from typesystem.tokenize.tokenize_json import _TokenizingDecoder
from typesystem.tokenize.tokens import DictToken


def test_tokenizing_decoder_initializes_scanner_and_decodes_content():
    content = '{"answer": 42}'
    decoder = _TokenizingDecoder(content=content)

    token = decoder.decode(content)

    assert callable(decoder.scan_once)
    assert isinstance(token, DictToken)
    assert token.value == {"answer": 42}
    assert token.string == content
