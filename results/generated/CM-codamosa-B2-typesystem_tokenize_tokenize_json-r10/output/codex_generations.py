

# Generated at 2026-11-03 05:37:38.031019
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"key": "value", "numbers": [1, 2.5, true, false, null]}'

    # Constructor accepts the required 'content' keyword argument
    decoder = _TokenizingDecoder(content=content)

    # It should still be a valid JSONDecoder instance
    assert isinstance(decoder, JSONDecoder)

    # A tokenizing scanner should have been installed
    assert callable(decoder.scan_once)

    # Decoding should produce a DictToken wrapping the raw content
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.value == {
        "key": "value",
        "numbers": [1, 2.5, True, False, None],
    }
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.string == content

    # A bare scalar document should be wrapped in a ScalarToken
    scalar = decoder.decode('"hello world"')
    assert isinstance(scalar, ScalarToken)
    assert scalar.value == "hello world"

    # Extra keyword arguments are forwarded to JSONDecoder
    decoder = _TokenizingDecoder(content=content, strict=False)
    assert decoder.strict is False

    # The 'content' keyword argument is required
    try:
        _TokenizingDecoder()
    except KeyError:
        pass
    else:
        raise AssertionError("KeyError not raised when 'content' is missing")

# Generated at 2026-11-03 05:39:53.606622
# Unit test for function tokenize_json
def test_tokenize_json():
    import pytest

    from typesystem.base import ParseError, Position
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

    # A simple JSON object tokenizes into a DictToken.
    token = module_0.tokenize_json('{"a": 1}')
    assert isinstance(token, DictToken)
    assert token.value == {"a": ScalarToken(1, 6, 6, '{"a": 1}')}
    assert token.start == 0
    assert token.end == 7

    # A simple JSON array tokenizes into a ListToken.
    token = module_0.tokenize_json('[1, 2, 3]')
    assert isinstance(token, ListToken)
    assert token.value == [
        ScalarToken(1, 1, 1, '[1, 2, 3]'),
        ScalarToken(2, 4, 4, '[1, 2, 3]'),
        ScalarToken(3, 7, 7, '[1, 2, 3]'),
    ]

    # A simple JSON string tokenizes into a ScalarToken.
    token = module_0.tokenize_json('"abc"')
    assert isinstance(token, ScalarToken)
    assert token.value == "abc"
    assert token.start == 0
    assert token.end == 4

    # Numbers, booleans and null tokenize into ScalarTokens.
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("1.5").value == 1.5
    assert module_0.tokenize_json("true").value is True
    assert module_0.tokenize_json("false").value is False
    assert module_0.tokenize_json("null").value is None

    # Nested structures tokenize correctly.
    token = module_0.tokenize_json('{"a": [1, 2], "b": {"c": true}}')
    assert isinstance(token, DictToken)
    assert isinstance(token.value["a"], ListToken)
    assert isinstance(token.value["b"], DictToken)
    assert token.value["b"].value["c"].value is True

    # Bytes input is decoded before tokenizing.
    token = module_0.tokenize_json(b'{"a": 1}')
    assert isinstance(token, DictToken)
    assert token.value["a"].value == 1

    # Keys are tokenized as ScalarTokens too.
    token = module_0.tokenize_json('{"key": "value"}')
    assert isinstance(token.value["key"], ScalarToken)
    assert token.value["key"].value == "key"
    assert token.value["value"].value == "value"

    # Empty content raises a parse error with a clear message.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("")
    assert exc_info.value.text == "No content."
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1, line_no=1, char_index=0
    )

    # Whitespace-only content also raises a parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("   \n  ")
    assert exc_info.value.code == "no_content"

    # Invalid JSON raises a parse error with position information.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"a": }')
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 7
    assert exc_info.value.position.char_index == 6

    # Invalid JSON in a multiline document reports the correct line.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no == 3

    # Bytes input with invalid JSON also raises a parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(b"{invalid}")
    assert exc_info.value.code == "parse_error"

# Generated at 2026-11-03 05:41:40.623529
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"key": "value"}'

    # Constructor accepts content keyword and builds a scanner.
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)

    # Default JSONDecoder attributes are still initialized.
    assert decoder.strict is True

    # Decoding with the tokenizing scanner yields a DictToken.
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}

    # Constructor forwards extra args/kwargs to JSONDecoder.
    decoder = _TokenizingDecoder(
        object_hook=None, parse_float=float, parse_int=int, content=content
    )
    assert callable(decoder.scan_once)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}

    # Non-strict mode is honored.
    decoder = _TokenizingDecoder(strict=False, content=content)
    assert decoder.strict is False

    # Scanner works for scalar content as well.
    decoder = _TokenizingDecoder(content="123")
    token = decoder.decode("123")
    assert isinstance(token, ScalarToken)
    assert token.value == 123

    # Missing content keyword raises KeyError.
    try:
        _TokenizingDecoder()  # type: ignore
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError when 'content' is not provided")

# Generated at 2026-11-03 05:43:45.539409
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"key": "value"}'
    decoder = _TokenizingDecoder(content=content)

    # Should be a valid JSONDecoder subclass with a custom scan_once
    assert isinstance(decoder, JSONDecoder)
    assert callable(decoder.scan_once)

    # scan_once should tokenize the content into a DictToken
    token, end = decoder.scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert end == len(content)
    assert token.value["key"].value == "value"

    # scan_once should tokenize scalar values as well
    scalar_content = "123"
    scalar_decoder = _TokenizingDecoder(content=scalar_content)
    token, end = scalar_decoder.scan_once(scalar_content, 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 123
    assert end == len(scalar_content)

    # Should accept additional JSONDecoder arguments
    decoder = _TokenizingDecoder(content=content, strict=False)
    assert isinstance(decoder, JSONDecoder)
    assert decoder.strict is False

    # Memo should be shared via the decoder and cleared after each scan
    decoder = _TokenizingDecoder(content=content)
    decoder.scan_once(content, 0)
    assert decoder.memo == {}