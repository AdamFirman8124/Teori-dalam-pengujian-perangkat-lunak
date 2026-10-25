

# Generated at 2026-10-24 00:55:12.036531
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Alice","age":30,"active":true,'
        '"tags":["admin",null],"details":{"score":4.5}}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["age"], ScalarToken)
    assert values["age"].value == 30

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["tags"], ListToken)
    assert [item.value for item in values["tags"].value] == ["admin", None]

    assert isinstance(values["details"], DictToken)
    details = {
        key.value: value.value for key, value in values["details"].value.items()
    }
    assert details == {"score": 4.5}


def test_tokenize_json_accepts_bytes():
    token = module_0.tokenize_json(b'{"value": 123}')

    assert isinstance(token, DictToken)
    values = {key.value: value.value for key, value in token.value.items()}
    assert values == {"value": 123}


@pytest.mark.parametrize("content", ["", " \n\t "])
def test_tokenize_json_rejects_empty_content(content):
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(content)

    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.char_index == 0


def test_tokenize_json_rejects_malformed_json():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.char_index == 9

# Generated at 2026-10-24 00:55:43.051926
# Unit test for function tokenize_json
def test_tokenize_json():
    def unwrap(token: Token) -> typing.Any:
        if isinstance(token, DictToken):
            return {
                unwrap(key): unwrap(value)
                for key, value in token.value.items()
            }
        if isinstance(token, ListToken):
            return [unwrap(value) for value in token.value]
        return token.value

    content = (
        b'{"name": "Alice", "age": 30, "active": true, '
        b'"tags": ["admin", null]}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert unwrap(token) == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "tags": ["admin", None],
    }

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("   ")

    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1,
        line_no=1,
        char_index=0,
    )

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 00:56:09.103238
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30, "active": true}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "Alice",
        "age": 30,
        "active": True,
    }
    assert token.start == 0
    assert token.end == len(content) - 1


def test_tokenize_json_scalar():
    content = '"hello"'

    token = module_0.tokenize_json(content)

    assert isinstance(token, ScalarToken)
    assert token.value == "hello"
    assert token.start == 0
    assert token.end == len(content) - 1


def test_tokenize_json_bytes():
    token = module_0.tokenize_json(b"[1, 2, null]")

    assert isinstance(token, ListToken)
    assert token.value == [1, 2, None]


def test_tokenize_json_empty_content():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.position == Position(column_no=1, line_no=1, char_index=0)


def test_tokenize_json_invalid_content():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.position.line_no == 1

# Generated at 2026-10-24 00:56:19.608716
# Unit test for constructor of class _TokenizingDecoder

# Generated at 2026-10-24 00:56:46.846529
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():content = "{}"

# Generated at 2026-10-24 00:58:27.568337
# Unit test for function validate_json

# Generated at 2026-10-24 00:58:34.878925
# Unit test for function validate_json
def test_validate_json():from typesystem.fields import String


# Generated at 2026-10-24 00:59:01.005253
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "name": "Alice",
        "age": 30,
        "active": true,
        "tags": ["python", null]
    }
    """

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["age"], ScalarToken)
    assert values["age"].value == 30

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["tags"], ListToken)
    assert [item.value for item in values["tags"].value] == ["python", None]


def test_tokenize_json_accepts_bytes():
    token = module_0.tokenize_json(b'{"value": 123}')

    assert isinstance(token, DictToken)
    values = {key.value: value for key, value in token.value.items()}
    assert values["value"].value == 123


def test_tokenize_json_rejects_empty_content():
    import pytest

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t ")

    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1,
        line_no=1,
        char_index=0,
    )


def test_tokenize_json_reports_invalid_json_position():
    import pytest

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.position.line_no == 1
    assert error.position.column_no == 10
    assert error.position.char_index == 9

# Generated at 2026-10-24 00:59:34.271872
# Unit test for function tokenize_json
def test_tokenize_json():
    def unwrap(token: Token) -> typing.Any:
        if isinstance(token, DictToken):
            return {
                unwrap(key): unwrap(value)
                for key, value in token.value.items()
            }
        if isinstance(token, ListToken):
            return [unwrap(item) for item in token.value]
        return token.value

    # Valid nested JSON.
    content = '{"name":"Ada","age":37,"active":true,"items":[1,null,"x"]}'
    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert unwrap(token) == {
        "name": "Ada",
        "age": 37,
        "active": True,
        "items": [1, None, "x"],
    }
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    # Bytes are accepted.
    bytes_token = module_0.tokenize_json(b'["hello", 2.5]')
    assert isinstance(bytes_token, ListToken)
    assert unwrap(bytes_token) == ["hello", 2.5]

    # Top-level scalar values are tokenized.
    scalar_token = module_0.tokenize_json("true")
    assert isinstance(scalar_token, ScalarToken)
    assert scalar_token.value is True
    assert scalar_token.start == 0
    assert scalar_token.end == 3

    # Empty content produces the explicit no-content error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t ")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.text == "No content."
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    # Malformed JSON produces a positioned parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.position.line_no == 1
    assert error.position.char_index == 9

# Generated at 2026-10-24 00:59:59.781316
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

# Generated at 2026-10-24 01:00:33.560653
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

# Generated at 2026-10-24 01:01:11.821245
# Unit test for function tokenize_json
def test_tokenize_json():import pytest


def _unwrap_token(token: Token) -> typing.Any:
    """Convert a token tree into ordinary Python values."""
    if isinstance(token, DictToken):
        return {
            key.value: _unwrap_token(value)
            for key, value in token.value.items()
        }

    if isinstance(token, ListToken):
        return [_unwrap_token(item) for item in token.value]

    return token.value


def test_tokenize_json() -> None:
    content = (
        '{"name":"Alice","age":30,"active":true,'
        '"items":[1,null],"metadata":{"score":1.5}}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    assert _unwrap_token(token) == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "items": [1, None],
        "metadata": {"score": 1.5},
    }

    fields = {key.value: value for key, value in token.value.items()}

    assert isinstance(fields["name"], ScalarToken)
    assert isinstance(fields["items"], ListToken)
    assert isinstance(fields["metadata"], DictToken)

    # Verify that scalar positions include the complete JSON representation.
    name_token = fields["name"]
    assert content[name_token.start : name_token.end + 1] == '"Alice"'

    age_token = fields["age"]
    assert content[age_token.start : age_token.end + 1] == "30"


def test_tokenize_json_accepts_bytes() -> None:
    token = module_0.tokenize_json(b'{"value":42}')

    assert isinstance(token, DictToken)
    assert _unwrap_token(token) == {"value": 42}
    assert token.content == '{"value":42}'


def test_tokenize_json_rejects_empty_content() -> None:
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t ")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.text == "No content."
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0


def test_tokenize_json_reports_invalid_json_position() -> None:
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"value": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.text == "Expecting value."
    assert error.position.line_no == 1
    assert error.position.column_no == 11
    assert error.position.char_index == 10

# Generated at 2026-10-24 01:01:44.998093
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    pairs = list(token.value.items())
    assert len(pairs) == 2

    name_key, name_value = pairs[0]
    assert isinstance(name_key, ScalarToken)
    assert name_key.value == "name"
    assert (name_key.start, name_key.end) == (1, 6)

    assert isinstance(name_value, ScalarToken)
    assert name_value.value == "Alice"
    assert (name_value.start, name_value.end) == (9, 15)

    age_key, age_value = pairs[1]
    assert isinstance(age_key, ScalarToken)
    assert age_key.value == "age"
    assert (age_key.start, age_key.end) == (18, 22)

    assert isinstance(age_value, ScalarToken)
    assert age_value.value == 30
    assert (age_value.start, age_value.end) == (25, 26)

    # Bytes input is also supported.
    bytes_token = module_0.tokenize_json(b'["value", true, null]')
    assert isinstance(bytes_token, ListToken)
    assert [item.value for item in bytes_token.value] == ["value", True, None]

    # Empty and malformed JSON should produce positional parse errors.
    with pytest.raises(ParseError):
        module_0.tokenize_json(" \n\t")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')

# Generated at 2026-10-24 01:02:01.831456
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

# Generated at 2026-10-24 01:02:37.876003
# Unit test for function tokenize_json
def test_tokenize_json():import pytest


def _plain_value(token: Token) -> typing.Any:
    """Recursively remove token metadata and return ordinary Python values."""
    if isinstance(token, DictToken):
        return {
            _plain_value(key): _plain_value(value)
            for key, value in token.value.items()
        }
    if isinstance(token, ListToken):
        return [_plain_value(item) for item in token.value]
    return token.value


def test_tokenize_json() -> None:
    content = (
        '{"name":"Alice","age":30,"scores":[1,2.5],'
        '"active":true,"note":null}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content
    assert _plain_value(token) == {
        "name": "Alice",
        "age": 30,
        "scores": [1, 2.5],
        "active": True,
        "note": None,
    }

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert content[values["name"].start : values["name"].end + 1] == '"Alice"'

    assert isinstance(values["scores"], ListToken)
    assert [type(item) for item in values["scores"].value] == [
        ScalarToken,
        ScalarToken,
    ]

    # Bytes input is also supported.
    assert _plain_value(module_0.tokenize_json(b'{"value":42}')) == {"value": 42}

    # Empty and malformed JSON should produce positional parse errors.
    with pytest.raises(ParseError):
        module_0.tokenize_json("   ")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name":}')

# Generated at 2026-10-24 01:03:06.150370
# Unit test for function tokenize_json
def test_tokenize_json():
    import pytest

    content = '{"name": "Alice", "age": 30, "active": true}'
    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        ScalarToken("name", 1, 6, content): ScalarToken("Alice", 9, 15, content),
        ScalarToken("age", 18, 22, content): ScalarToken(30, 25, 26, content),
        ScalarToken("active", 29, 36, content): ScalarToken(True, 39, 42, content),
    }

    # The root token spans the entire JSON object.
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    # Bytes input is supported.
    bytes_token = module_0.tokenize_json(b'"hello"')
    assert isinstance(bytes_token, ScalarToken)
    assert bytes_token.value == "hello"

    # Empty content produces a specific parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1,
        line_no=1,
        char_index=0,
    )

    # Malformed JSON reports the location of the parsing failure.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 10
    assert exc_info.value.position.char_index == 9

# Generated at 2026-10-24 01:03:34.195816
# Unit test for function tokenize_json
def test_tokenize_json():
    # Scalar value
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Array with different JSON scalar types
    token = module_0.tokenize_json(b'[1, 2.5, "three", true, false, null]')
    assert isinstance(token, ListToken)
    assert [item.value for item in token.value] == [
        1,
        2.5,
        "three",
        True,
        False,
        None,
    ]
    assert all(isinstance(item, ScalarToken) for item in token.value)

    # Nested object
    token = module_0.tokenize_json('{"items": [1, 2]}')
    assert isinstance(token, DictToken)

    key_token, value_token = next(iter(token.value.items()))
    assert isinstance(key_token, ScalarToken)
    assert key_token.value == "items"
    assert isinstance(value_token, ListToken)
    assert [item.value for item in value_token.value] == [1, 2]

    # Empty input
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("   ")

    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1
    assert exc_info.value.position.char_index == 0

    # Malformed JSON
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 01:04:05.132482
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name": "Alice", "age": 30, "active": true, '
        '"scores": [10, 20], "metadata": null}'
    )
    expected = {
        "name": "Alice",
        "age": 30,
        "active": True,
        "scores": [10, 20],
        "metadata": None,
    }

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == expected
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    # Bytes input is also supported.
    bytes_token = module_0.tokenize_json(content.encode("utf-8"))
    assert isinstance(bytes_token, DictToken)
    assert bytes_token.value == expected

    # Empty and malformed input should produce positional parse errors.
    with pytest.raises(ParseError):
        module_0.tokenize_json("   ")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": "Alice"')

# Generated at 2026-10-24 01:04:21.711434
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

# Generated at 2026-10-24 01:04:54.785087
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name":"Alice","age":30}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert set(values) == {"name", "age"}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"
    assert values["name"].start == 8
    assert values["name"].end == 14

    assert isinstance(values["age"], ScalarToken)
    assert values["age"].value == 30
    assert values["age"].start == 22
    assert values["age"].end == 23

    # Bytes input is also supported.
    bytes_token = module_0.tokenize_json(b'["value", true, null]')
    assert isinstance(bytes_token, ListToken)
    assert [item.value for item in bytes_token.value] == ["value", True, None]

    # Empty input produces a positional ParseError.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t ")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    # Invalid JSON produces a parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"