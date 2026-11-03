

# Generated at 2026-11-03 06:16:58.478211
# Unit test for function tokenize_json

# Generated at 2026-11-03 06:18:25.755749
# Unit test for function tokenize_json
def test_tokenize_json():# Dict content: tokenizes into a DictToken with correct value and span.
    content = '{"name": "tom", "values": [1, 2.5, true, false, null]}'
    token = module_0.tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {"name": "tom", "values": [1, 2.5, True, False, None]}
    assert token.start_index == 0
    assert token.end_index == len(content) - 1
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1

    # Lists tokenize into ListToken.
    list_token = module_0.tokenize_json('  [1, "two"]  ')
    assert isinstance(list_token, ListToken)
    assert list_token.value == [1, "two"]
    assert list_token.start_index == 2
    assert list_token.end_index == 11

    # Scalar strings tokenize into ScalarToken; bytes input is decoded.
    scalar = module_0.tokenize_json(b'"hello"')
    assert isinstance(scalar, ScalarToken)
    assert scalar.value == "hello"
    assert scalar.start_index == 0
    assert scalar.end_index == 6

    # Numbers: integer and float.
    num = module_0.tokenize_json("42")
    assert isinstance(num, ScalarToken)
    assert num.value == 42

    flt = module_0.tokenize_json("-3.5e2")
    assert isinstance(flt, ScalarToken)
    assert flt.value == -350.0

    # Bare literals.
    assert module_0.tokenize_json("true").value is True
    assert module_0.tokenize_json("false").value is False
    assert module_0.tokenize_json("null").value is None

# Generated at 2026-11-03 06:19:16.510030
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"key": "value"}'

    # Constructor accepts content kwarg and initializes scan_once
    decoder = _TokenizingDecoder(content=content)
    assert decoder.scan_once is not None

    # The decoder should still behave like a JSONDecoder otherwise
    assert decoder.strict is True

    # scan_once should tokenize the content into a DictToken
    token, end = decoder.scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}
    assert end == len(content)

    # decode should return a tokenized structure
    decoded = decoder.decode(content)
    assert isinstance(decoded, DictToken)
    assert decoded.value == {"key": "value"}

    # scan_once should also handle scalar values
    token, end = decoder.scan_once('"abc"', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == "abc"
    assert end == 5

    # Constructor works with additional JSONDecoder kwargs
    decoder = _TokenizingDecoder(strict=False, content=content)
    assert decoder.scan_once is not None
    assert decoder.strict is False

    # Missing 'content' kwarg should raise KeyError
    try:
        _TokenizingDecoder()
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError when 'content' is not provided")

# Generated at 2026-11-03 06:20:32.692865
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"name": "tom", "value": 42}'

    # Constructor should accept the 'content' keyword argument
    decoder = _TokenizingDecoder(content=content)

    # 'scan_once' should be set and callable
    assert callable(decoder.scan_once)

    # Scanning the content should produce a DictToken covering the whole content
    token, end = decoder.scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert end == len(content)
    assert token.value == {"name": "tom", "value": 42}

    # The scanner should also handle scalar content
    scalar_content = '"abc"'
    decoder_scalar = _TokenizingDecoder(content=scalar_content)
    scalar_token, scalar_end = decoder_scalar.scan_once(scalar_content, 0)
    assert isinstance(scalar_token, ScalarToken)
    assert scalar_token.value == "abc"
    assert scalar_end == len(scalar_content)

    # Extra keyword arguments should be forwarded to JSONDecoder
    decoder_with_kwargs = _TokenizingDecoder(content=content, parse_float=float)
    assert decoder_with_kwargs.parse_float is float

    # Constructing without the required 'content' argument should raise KeyError
    try:
        _TokenizingDecoder()
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError when 'content' is not provided")

# Generated at 2026-11-03 06:22:21.135923
# Unit test for function validate_json