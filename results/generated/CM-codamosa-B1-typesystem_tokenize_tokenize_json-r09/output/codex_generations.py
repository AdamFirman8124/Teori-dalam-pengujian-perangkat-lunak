

# Generated at 2026-10-24 01:49:35.628061
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:49:38.596374
# Unit test for function validate_json

# Generated at 2026-10-24 01:49:49.859982
# Unit test for function validate_json
def test_validate_json():from typesystem.fields import String


# Generated at 2026-10-24 01:50:00.041780
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"name": "Alice"}'
    scanner = Mock()

    with patch(f"{__name__}._make_scanner", return_value=scanner) as make_scanner:
        decoder = _TokenizingDecoder(content=content, strict=False)

    assert isinstance(decoder, JSONDecoder)
    assert decoder.strict is False
    assert decoder.scan_once is scanner
    make_scanner.assert_called_once_with(decoder, content)

# Generated at 2026-10-24 01:50:16.588389
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:50:19.556346
# Unit test for function validate_json

# Generated at 2026-10-24 01:50:29.800844
# Unit test for function validate_json
def test_validate_json():from typesystem.fields import Integer


# Generated at 2026-10-24 01:50:47.317545
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:51:04.144055
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:51:20.693782
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:51:58.794570
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Ada","scores":[1,2.5],"active":true,"optional":null}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Ada"
    assert values["name"].start.char_index == content.index('"Ada"')
    assert values["name"].end.char_index == content.index('"Ada"') + len('"Ada"') - 1

    assert isinstance(values["scores"], ListToken)
    assert [item.value for item in values["scores"].value] == [1, 2.5]

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["optional"], ScalarToken)
    assert values["optional"].value is None


def test_tokenize_json_accepts_bytes():
    token = module_0.tokenize_json(b'{"value":42}')
    assert isinstance(token, DictToken)

    values = {key.value: value.value for key, value in token.value.items()}
    assert values == {"value": 42}


def test_tokenize_json_rejects_empty_content():
    with pytest.raises(ParseError):
        module_0.tokenize_json(" \n\t ")


def test_tokenize_json_rejects_invalid_json():
    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name":}')

# Generated at 2026-10-24 01:52:15.371650
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 01:52:31.858301
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 01:52:48.549649
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:53:05.037118
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:53:21.613344
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 01:53:38.213110
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 01:53:55.020859
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:54:11.519383
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:54:28.084044
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 01:54:44.773483
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 01:55:01.272697
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:55:17.850221
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:55:34.338455
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:55:50.823756
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:56:07.321068
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:56:23.796096
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:56:40.692343
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:56:57.189562
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:57:13.766335
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 01:57:30.253603
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:57:46.946971
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:58:03.608862
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:58:20.286914
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:58:36.812788
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar

# Generated at 2026-10-24 01:58:53.608817
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:59:10.106407
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object with keys and values of each scalar type
    token = module_0.tokenize_json('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len('{"a": 1, "b": "x", "c": true, "d": null, "e": 1.5}') - 1

    # Keys and values are ScalarTokens with correct positions
    assert isinstance(token.value["a"], ScalarToken)
    assert token.value["a"].value == 1
    assert token.value["b"].value == "x"
    assert token.value["c"].value is True
    assert token.value["d"].value is None
    assert token.value["e"].value == 1.5

    # Nested list and dict
    token = module_0.tokenize_json('{"list": [1, 2], "dict": {"k": "v"}}')
    assert isinstance(token.value["list"], ListToken)
    assert isinstance(token.value["dict"], DictToken)
    assert token.value["list"].value[1].value == 2

    # Empty object and empty list
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Whitespace and leading/trailing whitespace
    token = module_0.tokenize_json('  \n {"a" : 1 }  \n ')
    assert token.value["a"].value == 1

    # Bytes input is decoded
    token = module_0.tokenize_json('{"a": 1}'.encode("utf-8"))
    assert token.value["a"].value == 1

    # String escapes
    token = module_0.tokenize_json('{"a": "line\\nbreak", "b": "\\u0041"}')
    assert token.value["a"].value == "line\nbreak"
    assert token.value["b"].value == "A"


def test_tokenize_json_empty_input():
    for empty in ("", "   ", "\n\t"):
        with pytest.raises(ParseError) as exc:
            module_0.tokenize_json(empty)
        assert exc.value.code == "no_content"
        assert exc.value.text == "No content."


def test_tokenize_json_parse_errors():
    # Not JSON at all
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("invalid")
    assert exc.value.code == "parse_error"

    # Truncated JSON
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": ')
    assert exc.value.code == "parse_error"

    # Position information is included
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": 1,}')
    assert exc.value.position is not None
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 9

    # Multi-line string reports correct line number
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  invalid\n}')
    assert exc.value.position.line_no == 3


def test_tokenize_json_bytes_with_invalid_utf8():
    # Invalid bytes are decoded with "ignore", so they're dropped
    token = module_0.tokenize_json(b'{"a": \xff1}')
    assert token.value["a"].value == 1

# Generated at 2026-10-24 01:59:27.502200
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar: string
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Scalar: int, float, exponent
    assert module_0.tokenize_json("123").value == 123
    assert module_0.tokenize_json("-42").value == -42
    assert module_0.tokenize_json("3.14").value == 3.14
    assert module_0.tokenize_json("1e3").value == 1000.0
    assert isinstance(module_0.tokenize_json("123"), ScalarToken)

    # Scalar