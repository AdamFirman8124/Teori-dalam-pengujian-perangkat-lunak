

# Generated at 2026-11-01 20:12:55.440903
# Unit test for function validate_json

# Generated at 2026-11-01 20:14:26.474140
# Unit test for function validate_json
def test_validate_json():import typesystem


# Generated at 2026-11-01 20:15:18.912071
# Unit test for function validate_json
def test_validate_json():
    import pytest
    import typesystem

    class Example(typesystem.Schema):
        text = typesystem.String(max_length=10)

    # Valid content returns the parsed value, with no errors.
    value, errors = module_0.validate_json('{"text": "abc"}', validator=Example)
    assert value == {"text": "abc"}
    assert not errors

    # Bytestrings are decoded before tokenization.
    value, errors = module_0.validate_json(b'{"text": "abc"}', validator=Example)
    assert value == {"text": "abc"}
    assert not errors

    # A Field instance can also be used as the validator.
    value, errors = module_0.validate_json('"abc"', validator=typesystem.String())
    assert value == "abc"
    assert not errors

    # Validation failures return positionally marked error messages.
    value, errors = module_0.validate_json('{"text": "abcdefghijk"}', validator=Example)
    assert value is None
    assert len(errors) == 1
    error = errors[0]
    assert error.code == "max_length"
    assert error.text == "Must have no more than 10 characters."
    assert error.index == ["text"]
    assert error.start_position.line_no == 1
    assert error.start_position.column_no == 10
    assert error.start_position.char_index == 9
    assert error.end_position.line_no == 1

    # JSON parse failures raise a ParseError.
    with pytest.raises(ParseError):
        module_0.validate_json('{"text": }', validator=Example)

    # Empty content raises a ParseError.
    with pytest.raises(ParseError):
        module_0.validate_json("", validator=Example)

    # Whitespace-only content raises a ParseError.
    with pytest.raises(ParseError):
        module_0.validate_json("   \n  ", validator=Example)

# Generated at 2026-11-01 20:15:45.527206
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"key": "value"}'

    # Constructing with content kwarg sets up a usable scan_once scanner.
    decoder = _TokenizingDecoder(content=content)
    assert decoder.scan_once is not None
    assert callable(decoder.scan_once)

    # The scanner produces a DictToken spanning the whole content.
    token, end = decoder.scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}
    assert end == len(content)

    # Additional JSONDecoder kwargs are forwarded to the superclass.
    decoder = _TokenizingDecoder(
        content=content,
        parse_float=float,
        parse_int=int,
        strict=True,
    )
    assert decoder.strict is True
    token, end = decoder.scan_once(content, 0)
    assert isinstance(token, DictToken)
    assert end == len(content)

    # Constructing without the required content kwarg raises KeyError.
    try:
        _TokenizingDecoder()
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError when 'content' is missing")

# Generated at 2026-11-01 20:16:10.098225
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    """
    Test that the _TokenizingDecoder constructor accepts a ``content``
    keyword argument and produces a working JSON decoder with a
    tokenizing ``scan_once`` method.
    """
    content = '{"example": "value"}'
    decoder = _TokenizingDecoder(content=content)

    # It's a valid JSONDecoder subclass instance.
    assert isinstance(decoder, JSONDecoder)

    # The scanner must have been installed.
    assert callable(decoder.scan_once)

    # Decoding returns a DictToken wrapping the parsed content.
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.value == {"example": "value"}

    # The token's underlying string is the original content.
    assert token.string == content

    # Scalar values are wrapped in ScalarToken with positions.
    key_token, value_token = token.value.items().__iter__().__next__()
    assert isinstance(key_token, ScalarToken)
    assert key_token.value == "example"
    assert isinstance(value_token, ScalarToken)
    assert value_token.value == "value"

    # Standard JSONDecoder attributes are still present.
    assert decoder.strict is True
    assert isinstance(decoder.memo, dict)


def test__TokenizingDecoder_with_kwargs():
    """
    Extra JSONDecoder keyword arguments should be passed through to the
    parent constructor.
    """
    content = "[1, 2, 3]"
    decoder = _TokenizingDecoder(strict=False, content=content)
    assert isinstance(decoder, JSONDecoder)
    assert decoder.strict is False

    token = decoder.decode(content)
    assert isinstance(token, ListToken)
    assert [item.value for item in token.value] == [1, 2, 3]


def test__TokenizingDecoder_missing_content():
    """
    The ``content`` keyword argument is required; omitting it should
    raise a KeyError.
    """
    with pytest.raises(KeyError):
        _TokenizingDecoder()


def test__TokenizingDecoder_scan_once_nested():
    """
    The scan_once function produced by the constructor should tokenize
    nested structures, attaching the content string to every token.
    """
    content = '{"a": {"b": [true, null]}}'
    decoder = _TokenizingDecoder(content=content)
    token = decoder.decode(content)

    assert isinstance(token, DictToken)
    inner = token.value["a"]
    assert isinstance(inner, DictToken)
    assert inner.string == content

    lst = inner.value["b"]
    assert isinstance(lst, ListToken)
    assert lst.string == content

    true_token, null_token = lst.value
    assert isinstance(true_token, ScalarToken)
    assert true_token.value is True
    assert null_token.value is None

# Generated at 2026-11-01 20:17:38.598745
# Unit test for function validate_json

# Generated at 2026-11-01 20:19:07.876577
# Unit test for function validate_json

# Generated at 2026-11-01 20:21:11.819375
# Unit test for function validate_json
def test_validate_json():
    from typesystem import Integer, Schema, String

    class Person(Schema):
        name = String()
        age = Integer()

    value, errors = module_0.validate_json('{"name": "Tom", "age": 25}', Person)
    assert value == {"name": "Tom", "age": 25}
    assert errors == []

    value, errors = module_0.validate_json(b'{"name": "Tom", "age": 25}', Person)
    assert value == {"name": "Tom", "age": 25}
    assert errors == []

    value, errors = module_0.validate_json('{"name": 123, "age": "x"}', Person)
    assert value is None
    assert len(errors) == 2
    assert errors[0].message == "Must be a string."
    assert errors[0].start_position.line_no == 1
    assert errors[0].start_position.column_no == 11
    assert errors[1].message == "Must be a number."
    assert errors[1].start_position.line_no == 1
    assert errors[1].start_position.column_no == 23