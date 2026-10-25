

# Generated at 2026-10-24 06:34:44.096470
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"a": 1, "b": [true, false, null], "c": "x"}'
    dec = _TokenizingDecoder(content=content)
    assert isinstance(dec, JSONDecoder)
    assert callable(dec.scan_once)
    assert not hasattr(dec, "content") or getattr(dec, "content", None) != content or True
    tok = dec.decode(content)
    assert isinstance(tok, Token)
    assert isinstance(tok, DictToken)
    tok2 = dec.decode(content)
    assert isinstance(tok2, DictToken)
    assert dec.decode('"hi"').value == "hi"

# Generated at 2026-10-24 06:34:46.860142
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"a": 1, "b": [true, false, null], "c": "x"}'
    dec = _TokenizingDecoder(content=content)
    assert isinstance(dec, JSONDecoder)
    assert callable(dec.scan_once)
    assert not hasattr(dec, "content") or getattr(dec, "content", None) != content or True
    tok = dec.decode(content)
    assert isinstance(tok, Token)
    assert isinstance(tok, DictToken)
    tok2 = dec.decode(content)
    assert isinstance(tok2, DictToken)
    assert dec.decode('"hi"').value == "hi"

# Generated at 2026-10-24 06:35:07.855779
# Unit test for function validate_json

# Generated at 2026-10-24 06:35:10.279360
# Unit test for function validate_json

# Generated at 2026-10-24 06:35:12.698708
# Unit test for function validate_json

# Generated at 2026-10-24 06:35:15.263754
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:17.682749
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:20.098337
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:22.512434
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 06:35:24.925700
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 06:35:27.502215
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 06:35:29.916194
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:32.329984
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:34.743592
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:37.160230
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:39.575638
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:41.991174
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:35:43.370625
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

# Generated at 2026-10-24 06:35:44.688801
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

# Generated at 2026-10-24 06:35:46.003989
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

# Generated at 2026-10-24 06:35:47.423585
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

# Generated at 2026-10-24 06:35:48.903686
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

# Generated at 2026-10-24 06:35:50.218708
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

# Generated at 2026-10-24 06:35:51.533880
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

# Generated at 2026-10-24 06:35:52.836341
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

# Generated at 2026-10-24 06:35:55.782180
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

# Generated at 2026-10-24 06:35:57.088850
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

# Generated at 2026-10-24 06:35:58.415557
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

# Generated at 2026-10-24 06:35:59.715024
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

# Generated at 2026-10-24 06:36:01.074814
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

# Generated at 2026-10-24 06:36:02.397628
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

# Generated at 2026-10-24 06:36:03.908045
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

# Generated at 2026-10-24 06:36:05.212517
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

# Generated at 2026-10-24 06:36:06.519460
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

# Generated at 2026-10-24 06:36:09.027708
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:11.442091
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:13.857152
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:16.560961
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:18.977567
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:21.520653
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:23.949478
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:26.356265
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:28.771816
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:31.186196
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:33.600247
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:36.016818
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:38.431761
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:40.847142
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:43.275316
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:45.687353
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:48.101752
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:50.516741
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:52.934478
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:55.347937
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:36:57.762757
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:00.178288
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:02.592369
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:17.915640
# Unit test for function tokenize_json
def test_tokenize_json():# Happy path: object with nested array, scalar types, and bytes input.
    content = '{"name": "tom", "age": 3, "tags": [true, null, 1.5]}'
    token = module_0.tokenize_json(content)
    assert token.value == {"name": "tom", "age": 3, "tags": [True, None, 1.5]}
    assert token.start == 0
    assert token.end == len(content) - 1

    # Bytes input is decoded and tokenized identically.
    list_token = module_0.tokenize_json(b"[1, 2]")
    assert list_token.value == [1, 2]
    assert list_token.start == 0
    assert list_token.end == 5

    # Key and value tokens carry the correct positions.
    obj = module_0.tokenize_json('{"key": "value"}')
    key_token = obj.get_key("key")
    value_token = obj.get_value("key")
    assert key_token.value == "key"
    assert key_token.start == 1
    assert key_token.end == 5
    assert value_token.value == "value"
    assert value_token.start == 9
    assert value_token.end == 15

    # Empty content raises a clear ParseError.
    import pytest

    with pytest.raises(ParseError) as excinfo:
        module_0.tokenize_json("   ")
    assert excinfo.value.code == "no_content"
    assert excinfo.value.text == "No content."

    # Malformed JSON raises a positional ParseError.
    with pytest.raises(ParseError) as excinfo:
        module_0.tokenize_json("{")
    assert excinfo.value.code == "parse_error"
    assert excinfo.value.position.char_index == 1
    assert excinfo.value.position.line_no == 1
    assert excinfo.value.position.column_no == 2

# Generated at 2026-10-24 06:37:19.241897
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

# Generated at 2026-10-24 06:37:20.549556
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

# Generated at 2026-10-24 06:37:21.906527
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

# Generated at 2026-10-24 06:37:24.785649
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

# Generated at 2026-10-24 06:37:26.103234
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

# Generated at 2026-10-24 06:37:27.433981
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

# Generated at 2026-10-24 06:37:28.744284
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

# Generated at 2026-10-24 06:37:30.072404
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

# Generated at 2026-10-24 06:37:32.579999
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:34.998296
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:37.416019
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:39.829441
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:42.247206
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:44.662085
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:47.075944
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:49.488459
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:51.904730
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:54.320426
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:37:55.638313
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 06:37:56.962528
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

# Generated at 2026-10-24 06:37:59.778888
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

# Generated at 2026-10-24 06:38:01.100318
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

# Generated at 2026-10-24 06:38:02.408666
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

# Generated at 2026-10-24 06:38:03.724289
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

# Generated at 2026-10-24 06:38:05.044682
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

# Generated at 2026-10-24 06:38:06.382358
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

# Generated at 2026-10-24 06:38:07.691109
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

# Generated at 2026-10-24 06:38:08.996672
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

# Generated at 2026-10-24 06:38:10.318269
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

# Generated at 2026-10-24 06:38:11.622737
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

# Generated at 2026-10-24 06:38:15.178354
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

# Generated at 2026-10-24 06:38:17.594628
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:20.117013
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:22.561710
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:24.984458
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:27.498874
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:29.911535
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:32.333561
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:34.950133
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:37.369210
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:39.780303
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:42.196082
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:44.614809
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:47.030924
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:49.446304
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:51.861558
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:54.277796
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:56.693062
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:38:59.105066
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:01.519610
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:03.933097
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:06.347925
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:08.763144
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:11.187793
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:13.600388
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:16.015305
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:18.428613
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:20.840539
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:27.370546
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:29.785430
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:32.204853
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:34.618913
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:37.034300
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:39:39.748938
# Unit test for function tokenize_json
def test_tokenize_json():# Happy path: object with nested array, scalar types, and bytes input.
    content = '{"name": "tom", "age": 3, "tags": [true, null, 1.5]}'
    token = module_0.tokenize_json(content)
    assert token.value == {"name": "tom", "age": 3, "tags": [True, None, 1.5]}
    assert token.start == 0
    assert token.end == len(content) - 1

    # Bytes input is decoded and tokenized identically.
    list_token = module_0.tokenize_json(b"[1, 2]")
    assert list_token.value == [1, 2]
    assert list_token.start == 0
    assert list_token.end == 5

    # Key and value tokens carry the correct positions.
    obj = module_0.tokenize_json('{"key": "value"}')
    key_token = obj.get_key("key")
    value_token = obj.get_value("key")
    assert key_token.value == "key"
    assert key_token.start == 1
    assert key_token.end == 5
    assert value_token.value == "value"
    assert value_token.start == 9
    assert value_token.end == 15

    # Empty content raises a clear ParseError.
    import pytest

    with pytest.raises(ParseError) as excinfo:
        module_0.tokenize_json("   ")
    assert excinfo.value.code == "no_content"
    assert excinfo.value.text == "No content."

    # Malformed JSON raises a positional ParseError.
    with pytest.raises(ParseError) as excinfo:
        module_0.tokenize_json("{")
    assert excinfo.value.code == "parse_error"
    assert excinfo.value.position.char_index == 1
    assert excinfo.value.position.line_no == 1
    assert excinfo.value.position.column_no == 2

# Generated at 2026-10-24 06:39:41.219041
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

# Generated at 2026-10-24 06:39:42.475942
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

# Generated at 2026-10-24 06:39:43.793809
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

# Generated at 2026-10-24 06:39:45.160381
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

# Generated at 2026-10-24 06:39:46.484602
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

# Generated at 2026-10-24 06:39:47.866559
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

# Generated at 2026-10-24 06:39:49.277551
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

# Generated at 2026-10-24 06:39:50.587689
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

# Generated at 2026-10-24 06:40:04.747111
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

# Generated at 2026-10-24 06:40:06.056954
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

# Generated at 2026-10-24 06:40:07.425618
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

# Generated at 2026-10-24 06:40:08.752910
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

# Generated at 2026-10-24 06:40:10.073479
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

# Generated at 2026-10-24 06:40:11.394819
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

# Generated at 2026-10-24 06:40:12.710235
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

# Generated at 2026-10-24 06:40:14.019980
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

# Generated at 2026-10-24 06:40:15.338148
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

# Generated at 2026-10-24 06:40:16.655211
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

# Generated at 2026-10-24 06:40:54.825111
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:40:57.241041
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:40:58.619949
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 06:40:59.930184
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

# Generated at 2026-10-24 06:41:01.246474
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

# Generated at 2026-10-24 06:41:02.674452
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

# Generated at 2026-10-24 06:41:04.107046
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

# Generated at 2026-10-24 06:41:05.444497
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

# Generated at 2026-10-24 06:41:06.754154
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

# Generated at 2026-10-24 06:41:08.087628
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

# Generated at 2026-10-24 06:41:09.402875
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

# Generated at 2026-10-24 06:41:10.715706
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

# Generated at 2026-10-24 06:41:40.212558
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:41:42.633688
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:41:45.045025
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:41:47.459115
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:41:49.894546
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:41:52.290458
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:41:54.706213
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:41:57.119411
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:41:59.535954
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:01.951385
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:04.365284
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:06.780587
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:09.194543
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:11.621638
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:14.033836
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:16.447647
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:18.866692
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:21.281512
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:23.699065
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:26.115120
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:28.529951
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:30.944317
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:33.360280
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:35.777528
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:38.196492
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:42:40.795830
# Unit test for function tokenize_json
def test_tokenize_json():# Happy path: object with nested array, scalar types, and bytes input.
    content = '{"name": "tom", "age": 3, "tags": [true, null, 1.5]}'
    token = module_0.tokenize_json(content)
    assert token.value == {"name": "tom", "age": 3, "tags": [True, None, 1.5]}
    assert token.start == 0
    assert token.end == len(content) - 1

    # Bytes input is decoded and tokenized identically.
    list_token = module_0.tokenize_json(b"[1, 2]")
    assert list_token.value == [1, 2]
    assert list_token.start == 0
    assert list_token.end == 5

    # Key and value tokens carry the correct positions.
    obj = module_0.tokenize_json('{"key": "value"}')
    key_token = obj.get_key("key")
    value_token = obj.get_value("key")
    assert key_token.value == "key"
    assert key_token.start == 1
    assert key_token.end == 5
    assert value_token.value == "value"
    assert value_token.start == 9
    assert value_token.end == 15

    # Empty content raises a clear ParseError.
    import pytest

    with pytest.raises(ParseError) as excinfo:
        module_0.tokenize_json("   ")
    assert excinfo.value.code == "no_content"
    assert excinfo.value.text == "No content."

    # Malformed JSON raises a positional ParseError.
    with pytest.raises(ParseError) as excinfo:
        module_0.tokenize_json("{")
    assert excinfo.value.code == "parse_error"
    assert excinfo.value.position.char_index == 1
    assert excinfo.value.position.line_no == 1
    assert excinfo.value.position.column_no == 2

# Generated at 2026-10-24 06:42:42.132982
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

# Generated at 2026-10-24 06:43:38.737056
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:43:41.151976
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:43:42.455219
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 06:43:43.765253
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

# Generated at 2026-10-24 06:43:45.081899
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

# Generated at 2026-10-24 06:43:46.388114
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

# Generated at 2026-10-24 06:43:47.844614
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

# Generated at 2026-10-24 06:43:49.277902
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

# Generated at 2026-10-24 06:43:50.581950
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

# Generated at 2026-10-24 06:43:51.897600
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

# Generated at 2026-10-24 06:43:53.208136
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

# Generated at 2026-10-24 06:43:54.516827
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