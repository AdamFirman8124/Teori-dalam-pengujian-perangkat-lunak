# file: project/typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

from typesystem.tokenize.tokenize_json import _TokenizingDecoder, tokenize_json


def test_tokenizing_decoder_init_executes_lines_160_162():
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)
    # postconditions for lines 160-162:
    # 160: content popped from kwargs, 161: super().__init__ ran,
    # 162: scan_once installed via _make_scanner
    assert callable(decoder.scan_once)
    assert callable(decoder.decode)
    token = decoder.decode(content)
    assert token is not None
    assert token.value == {"a": 1}
    assert token.lookup(["a"]).value == 1


def test_tokenizing_decoder_init_with_passthrough_args_kwargs():
    content = '[1, 2, 3]'
    # exercise *args/**kwargs passthrough to JSONDecoder (line 161)
    decoder = _TokenizingDecoder(content=content, strict=False, parse_float=float)
    assert decoder.strict is False
    assert decoder.parse_float is float
    assert callable(decoder.scan_once)
    token = decoder.decode(content)
    assert token is not None
    assert token.value == [1, 2, 3]
    assert token.lookup([0]).value == 1


def test_tokenize_json_end_to_end_covers_decoder_init():
    # tokenize_json instantiates _TokenizingDecoder(content=content)
    token = tokenize_json('{"x": true}')
    assert token is not None
    assert token.value == {"x": True}
    assert token.lookup(["x"]).value is True
