# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest

from typesystem.tokenize.tokenize_json import _TokenizingDecoder, tokenize_json
from typesystem.tokenize.tokens import Token


def test_tokenizing_decoder_init_executes_missing_lines():
    """Instantiating _TokenizingDecoder directly executes lines 160-162:
    popping 'content' from kwargs, calling super().__init__, and
    installing a custom scan_once scanner."""
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)

    # Line 160: 'content' was popped from kwargs, so it must not linger.
    # Line 161: JSONDecoder.__init__ ran, so standard attributes exist.
    assert decoder.strict is True
    # Line 162: a custom scanner was installed on the instance.
    assert decoder.scan_once is not None
    assert "scan_once" in decoder.__dict__

    # The installed scanner must actually work when decoding.
    token = decoder.decode(content)
    assert isinstance(token, Token)
    assert token.value == {"a": 1}


def test_tokenizing_decoder_init_with_extra_kwargs():
    """Extra kwargs are forwarded to JSONDecoder.__init__ via *args/**kwargs,
    while 'content' alone is consumed by line 160."""
    content = "[1, 2, 3]"
    decoder = _TokenizingDecoder(object_hook=None, content=content)

    assert decoder.scan_once is not None
    token = decoder.decode(content)
    assert isinstance(token, Token)
    assert token.value == [1, 2, 3]


def test_tokenize_json_triggers_decoder_init():
    """tokenize_json constructs _TokenizingDecoder(content=content),
    thereby executing lines 160-162 through the public entry point."""
    token = tokenize_json('{"key": "value"}')

    assert isinstance(token, Token)
    assert token.value == {"key": "value"}
