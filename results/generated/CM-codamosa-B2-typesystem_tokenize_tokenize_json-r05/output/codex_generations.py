

# Generated at 2026-11-02 18:15:59.199569
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"key": "value"}'

    # Constructing with content succeeds and sets up scan_once.
    decoder = _TokenizingDecoder(content=content)
    assert isinstance(decoder, JSONDecoder)
    assert callable(decoder.scan_once)

    # The decoder can tokenize its content via the custom scanner.
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}

    # Additional kwargs are forwarded to JSONDecoder.
    decoder = _TokenizingDecoder(content=content, strict=False)
    assert decoder.strict is False

    # content is a required keyword argument.
    try:
        _TokenizingDecoder()  # type: ignore
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError when 'content' is missing")

# Generated at 2026-11-02 18:16:17.492686
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"name": "tom", "values": [1, 2.5, true, null]}'
    decoder = _TokenizingDecoder(content=content)

    # The decoder should be a valid JSONDecoder with a scanner attached.
    assert isinstance(decoder, JSONDecoder)
    assert callable(decoder.scan_once)

    # The scanner should tokenize the content it was constructed with.
    token, end = decoder.scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert token.value["name"].value == "tom"
    assert isinstance(token.value["values"], ListToken)
    assert token.value["values"].value[0].value == 1
    assert token.value["values"].value[1].value == 2.5
    assert token.value["values"].value[2].value is True
    assert token.value["values"].value[3].value is None
    assert end == len(content)

    # Extra keyword arguments are forwarded to JSONDecoder.
    decoder2 = _TokenizingDecoder(parse_float=float, content="{}")
    assert decoder2.parse_float is float

    # The "content" keyword argument is required.
    try:
        _TokenizingDecoder()
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError when 'content' is not provided")

# Generated at 2026-11-02 18:16:22.115763
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    from json.decoder import JSONDecoder

    content = '{"key": "value"}'
    decoder = _TokenizingDecoder(content=content)

    # It should be a valid JSONDecoder subclass
    assert isinstance(decoder, JSONDecoder)

    # It should have a scan_once scanner callable built from the content
    assert callable(decoder.scan_once)

    # The content kwarg must be supplied, otherwise KeyError is raised
    try:
        _TokenizingDecoder()  # type: ignore
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError when 'content' is missing")

    # Default JSONDecoder arguments should still be accepted
    decoder_with_args = _TokenizingDecoder(
        object_hook=None, content=content, strict=True
    )
    assert callable(decoder_with_args.scan_once)

    # scan_once should tokenize a value within the content correctly
    token, end = decoder.scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1

# Generated at 2026-11-02 18:16:35.156306
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"key": "value"}'

    # Constructor accepts `content` keyword and installs a scan_once scanner.
    decoder = _TokenizingDecoder(content=content)
    assert decoder.scan_once is not None

    # Decoding with the tokenizer returns a DictToken rooted at the object.
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    # Extra JSONDecoder arguments are forwarded to the superclass.
    decoder = _TokenizingDecoder(parse_int=int, strict=True, content=content)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}

    # The scanner produces ScalarTokens for primitives.
    content = '{"count": 1, "name": "abc", "active": true, "empty": null}'
    decoder = _TokenizingDecoder(content=content)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.value == {"count": 1, "name": "abc", "active": True, "empty": None}
    assert all(isinstance(key, ScalarToken) for key in token._value)
    assert all(isinstance(val, ScalarToken) for val in token._value.values())

# Generated at 2026-11-02 18:17:13.868275
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"a": 1, "b": [true, null], "c": {"d": 1.5}}'

    # Constructor requires the "content" keyword argument and accepts
    # standard JSONDecoder arguments as well.
    decoder = _TokenizingDecoder(content=content)
    other = _TokenizingDecoder(content=content, strict=True)

    assert isinstance(decoder, JSONDecoder)
    assert callable(decoder.scan_once)
    assert callable(other.scan_once)

    # Decoding returns a positional token tree rather than plain python types.
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1

    (key_a, value_a), (key_b, value_b), (key_c, value_c) = token._value.items()

    assert isinstance(key_a, ScalarToken) and key_a._value == "a"
    assert isinstance(value_a, ScalarToken) and value_a._value == 1

    assert isinstance(key_b, ScalarToken) and key_b._value == "b"
    assert isinstance(value_b, ListToken)
    first, second = value_b._value
    assert isinstance(first, ScalarToken) and first._value is True
    assert isinstance(second, ScalarToken) and second._value is None

    assert isinstance(key_c, ScalarToken) and key_c._value == "c"
    assert isinstance(value_c, DictToken)
    ((inner_key, inner_value),) = value_c._value.items()
    assert isinstance(inner_key, ScalarToken) and inner_key._value == "d"
    assert isinstance(inner_value, ScalarToken) and inner_value._value == 1.5

    # scan_once can be invoked directly.
    scalar, end = decoder.scan_once("123", 0)
    assert isinstance(scalar, ScalarToken)
    assert scalar._value == 123
    assert scalar.start == 0
    assert scalar.end == 2
    assert end == 3

    # Invalid JSON raises JSONDecodeError.
    try:
        decoder.decode("{invalid")
    except JSONDecodeError:
        pass
    else:
        raise AssertionError("Expected JSONDecodeError")

# Generated at 2026-11-02 18:18:34.486614
# Unit test for function tokenize_json

# Generated at 2026-11-02 18:20:26.806684
# Unit test for function tokenize_json
def test_tokenize_json():content = '{"a": 1, "b": [true, null, 1.5], "c": "x"}'

# Generated at 2026-11-02 18:22:16.071701
# Unit test for function tokenize_json

# Generated at 2026-11-02 18:24:23.139366
# Unit test for function tokenize_json