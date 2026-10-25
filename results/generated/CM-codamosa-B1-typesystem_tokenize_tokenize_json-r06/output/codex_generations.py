

# Generated at 2026-10-24 06:08:02.768242
# Unit test for function validate_json
def test_validate_json():from unittest.mock import Mock


def test_validate_json(monkeypatch):
    content = '{"name": "Alice"}'
    validator = Mock(spec=Field)
    token = Mock(spec=Token)
    expected_result = {"name": "Alice"}

    mock_tokenize_json = Mock(return_value=token)
    mock_validate_with_positions = Mock(return_value=expected_result)

    monkeypatch.setitem(
        validate_json.__globals__, "tokenize_json", mock_tokenize_json
    )
    monkeypatch.setitem(
        validate_json.__globals__,
        "validate_with_positions",
        mock_validate_with_positions,
    )

    result = module_0.validate_json(content, validator)

    assert result == expected_result
    mock_tokenize_json.assert_called_once_with(content)
    mock_validate_with_positions.assert_called_once_with(
        token=token,
        validator=validator,
    )

# Generated at 2026-10-24 06:08:22.841843
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name": "Alice", "age": 30, "active": true, '
        '"scores": [10, 20, null]}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["age"], ScalarToken)
    assert values["age"].value == 30

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    scores = values["scores"]
    assert isinstance(scores, ListToken)
    assert [item.value for item in scores.value] == [10, 20, None]
    assert all(isinstance(item, ScalarToken) for item in scores.value)

    # Bytes input is supported.
    bytes_token = module_0.tokenize_json(b'{"value": 1}')
    assert isinstance(bytes_token, DictToken)

    # Empty and malformed input produce positional parse errors.
    with pytest.raises(ParseError) as empty_error:
        module_0.tokenize_json(" \n\t")
    assert empty_error.value.code == "no_content"
    assert empty_error.value.position == Position(
        column_no=1,
        line_no=1,
        char_index=0,
    )

    with pytest.raises(ParseError) as parse_error:
        module_0.tokenize_json('{"name": }')
    assert parse_error.value.code == "parse_error"

# Generated at 2026-10-24 06:08:41.053982
# Unit test for function validate_json
def test_validate_json():
    import sys
    from unittest.mock import Mock, patch

    content = '{"name": "Alice"}'
    validator = Mock(spec=Field)
    token = Mock(spec=Token)
    expected_result = object()

    module = sys.modules[validate_json.__module__]

    with (
        patch.object(module, "tokenize_json", return_value=token) as mock_tokenize,
        patch.object(
            module,
            "validate_with_positions",
            return_value=expected_result,
        ) as mock_validate,
    ):
        result = module_0.validate_json(content, validator)

    assert result is expected_result
    mock_tokenize.assert_called_once_with(content)
    mock_validate.assert_called_once_with(token=token, validator=validator)

# Generated at 2026-10-24 06:08:57.642802
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"message": "hello"}'
    scanner = Mock()

    with patch(
        f"{_TokenizingDecoder.__module__}._make_scanner",
        return_value=scanner,
    ) as make_scanner:
        decoder = _TokenizingDecoder(content=content, strict=False)

    assert isinstance(decoder, JSONDecoder)
    assert decoder.strict is False
    assert decoder.scan_once is scanner
    make_scanner.assert_called_once_with(decoder, content)

# Generated at 2026-10-24 06:09:00.159693
# Unit test for function validate_json

# Generated at 2026-10-24 06:09:02.574653
# Unit test for function validate_json

# Generated at 2026-10-24 06:09:04.991885
# Unit test for function validate_json

# Generated at 2026-10-24 06:09:09.364089
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:09:11.779408
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:09:21.502850
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json("42")

# Generated at 2026-10-24 06:09:49.570751
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name":"Alice","items":[1,true,null]}'
    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    members = {key.value: value for key, value in token.value.items()}

    name = members["name"]
    assert isinstance(name, ScalarToken)
    assert name.value == "Alice"
    assert content[name.start : name.end + 1] == '"Alice"'

    items = members["items"]
    assert isinstance(items, ListToken)
    assert [item.value for item in items.value] == [1, True, None]
    assert content[items.start : items.end + 1] == "[1,true,null]"

    # Bytes input is accepted.
    scalar = module_0.tokenize_json(b'"hello"')
    assert isinstance(scalar, ScalarToken)
    assert scalar.value == "hello"
    assert scalar.start == 0
    assert scalar.end == 6

    # Empty input produces a positionally marked ParseError.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.text == "No content."
    assert error.position.char_index == 0
    assert error.position.line_no == 1
    assert error.position.column_no == 1

    # Invalid JSON reports the location at which a value was expected.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{\n  "x":\n}')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.text == "Expecting value."
    assert error.position.char_index == 9
    assert error.position.line_no == 3
    assert error.position.column_no == 1

# Generated at 2026-10-24 06:09:52.081629
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:09:54.499892
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:09:56.915658
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:09:59.331600
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:01.913483
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:04.334581
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:06.749198
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:09.165140
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:11.580578
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:13.994193
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:16.411945
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:18.822669
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:21.238904
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:10:22.736627
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 06:10:41.480620
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30, "active": true, "items": [1, null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["age"], ScalarToken)
    assert values["age"].value == 30

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["items"], ListToken)
    assert [item.value for item in values["items"].value] == [1, None]

    # Bytes input is supported.
    bytes_token = module_0.tokenize_json(b'{"value": 42}')
    assert isinstance(bytes_token, DictToken)
    [(key, value)] = bytes_token.value.items()
    assert key.value == "value"
    assert value.value == 42

    # Empty content produces a positionally marked ParseError.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    error = exc_info.value
    assert error.text == "No content."
    assert error.code == "no_content"
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    # Invalid JSON also produces a ParseError at the decoder's position.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.position.line_no == 1
    assert error.position.char_index == 9

# Generated at 2026-10-24 06:11:00.183919
# Unit test for function tokenize_json
def test_tokenize_json():
    import pytest

    def unwrap(token: Token) -> typing.Any:
        if isinstance(token, DictToken):
            return {
                unwrap(key): unwrap(value)
                for key, value in token.value.items()
            }
        if isinstance(token, ListToken):
            return [unwrap(item) for item in token.value]
        return token.value

    content = (
        '{"name": "Alice", "age": 30, "active": true, '
        '"scores": [10, 9.5], "metadata": null}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start_index == 0
    assert token.end_index == len(content) - 1
    assert unwrap(token) == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "scores": [10, 9.5],
        "metadata": None,
    }

    # Bytes input is supported.
    assert unwrap(module_0.tokenize_json(b'{"valid": true}')) == {"valid": True}

    # Empty and malformed input produce positional parse errors.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1, line_no=1, char_index=0
    )

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')
    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 06:11:02.754778
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:05.169550
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:07.584535
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:09.996964
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:12.418591
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:14.831241
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:17.245576
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:19.663033
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:22.225138
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:24.641068
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:27.056024
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:11:37.395639
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json("123")

# Generated at 2026-10-24 06:11:57.356216
# Unit test for function tokenize_json
def test_tokenize_json():import pytest


def _unwrap_token(token: Token) -> typing.Any:
    if isinstance(token, DictToken):
        return {
            _unwrap_token(key): _unwrap_token(value)
            for key, value in token.value.items()
        }
    if isinstance(token, ListToken):
        return [_unwrap_token(item) for item in token.value]
    if isinstance(token, ScalarToken):
        return token.value
    raise AssertionError(f"Unexpected token type: {type(token)!r}")


def test_tokenize_json() -> None:
    content = """
    {
        "name": "Alice",
        "age": 30,
        "active": true,
        "score": 9.5,
        "tags": ["admin", null]
    }
    """

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert _unwrap_token(token) == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "score": 9.5,
        "tags": ["admin", None],
    }

    # Bytes input is also supported.
    bytes_token = module_0.tokenize_json(b'{"value": 42}')
    assert _unwrap_token(bytes_token) == {"value": 42}

    # Empty and malformed input should produce ParseError.
    with pytest.raises(ParseError):
        module_0.tokenize_json("   ")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')

# Generated at 2026-10-24 06:12:19.823397
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Ada","scores":[1,2.5],"active":true,"metadata":null}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Ada"

    assert isinstance(values["scores"], ListToken)
    assert [item.value for item in values["scores"].value] == [1, 2.5]

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["metadata"], ScalarToken)
    assert values["metadata"].value is None

    # Bytes are accepted.
    bytes_token = module_0.tokenize_json(b"42")
    assert isinstance(bytes_token, ScalarToken)
    assert bytes_token.value == 42

    # Empty input produces a positionally marked error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    # Malformed JSON produces a parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name":}')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 06:12:22.241469
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:12:24.659238
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:12:27.218208
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:12:29.634365
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:12:32.054871
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:12:33.457862
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 06:13:04.624677
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:06.072618
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 06:13:17.066808
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30, "active": true, "items": [1, null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["age"], ScalarToken)
    assert values["age"].value == 30

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["items"], ListToken)
    assert [item.value for item in values["items"].value] == [1, None]

# Generated at 2026-10-24 06:13:19.578825
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:22.125828
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:24.542509
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:26.955893
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:29.370884
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:31.786252
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:34.204381
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:36.617645
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:39.033062
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:41.448166
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:43.860794
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:46.276267
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:48.693474
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:13:51.112250
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:14:00.031330
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"name": "Alice", "active": true}')

# Generated at 2026-10-24 06:14:17.773799
# Unit test for function tokenize_json
def test_tokenize_json():
    def to_python(token: Token) -> typing.Any:
        if isinstance(token, DictToken):
            return {
                to_python(key): to_python(value)
                for key, value in token.value.items()
            }
        if isinstance(token, ListToken):
            return [to_python(item) for item in token.value]
        assert isinstance(token, ScalarToken)
        return token.value

    content = """
    {
        "name": "Alice",
        "age": 30,
        "active": true,
        "score": 9.5,
        "tags": ["admin", null]
    }
    """

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert to_python(token) == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "score": 9.5,
        "tags": ["admin", None],
    }

    # Bytes are also accepted.
    bytes_token = module_0.tokenize_json(b'["value", 42]')
    assert isinstance(bytes_token, ListToken)
    assert to_python(bytes_token) == ["value", 42]

    # Empty and malformed input produce ParseError.
    with pytest.raises(ParseError):
        module_0.tokenize_json("   ")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')

# Generated at 2026-10-24 06:14:37.924005
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:14:40.450382
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:14:42.864949
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:14:45.279176
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:14:47.695154
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:14:50.109567
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:14:52.527787
# Unit test for function tokenize_json

# Generated at 2026-10-24 06:15:01.778770
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"name": "Alice", "age": 30}')

# Generated at 2026-10-24 06:15:19.850192
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Alice","age":30,"active":true,'
        '"scores":[10,9.5,null],"details":{"city":"London"}}'
    )

    token = module_0.tokenize_json(content)

    def unwrap(item):
        if isinstance(item, ScalarToken):
            return item.value
        if isinstance(item, ListToken):
            return [unwrap(value) for value in item.value]
        if isinstance(item, DictToken):
            return {
                unwrap(key): unwrap(value)
                for key, value in item.value.items()
            }
        raise AssertionError(f"Unexpected token type: {type(item)!r}")

    assert isinstance(token, DictToken)
    assert unwrap(token) == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "scores": [10, 9.5, None],
        "details": {"city": "London"},
    }

    # Bytes input is supported.
    bytes_token = module_0.tokenize_json(b'"hello"')
    assert isinstance(bytes_token, ScalarToken)
    assert bytes_token.value == "hello"

    # Empty and malformed JSON produce positional parse errors.
    with pytest.raises(ParseError):
        module_0.tokenize_json("   ")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name":}')

# Generated at 2026-10-24 06:15:31.404281
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30}'
    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    values = {key.value: value.value for key, value in token.value.items()}
    assert values == {"name": "Alice", "age": 30}


def test_tokenize_json_empty_content():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t ")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0


def test_tokenize_json_invalid_content():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.position.line_no == 1


def test_tokenize_json_accepts_bytes():
    token = module_0.tokenize_json(b'"hello"')

    assert isinstance(token, ScalarToken)
    assert token.value == "hello"
    assert token.start == 0
    assert token.end == 6
    assert token.content == "hello"

# Generated at 2026-10-24 06:15:41.718613
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30, "active": true, "tags": ["admin", null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "tags": ["admin", None],
    }
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

# Generated at 2026-10-24 06:16:01.572290
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Ada", "active": true, "scores": [1, 2.5, null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1

    items = list(token.value.items())
    assert len(items) == 3

    name_key, name_value = items[0]
    assert isinstance(name_key, ScalarToken)
    assert name_key.value == "name"
    assert name_key.start == 1
    assert name_key.end == 6
    assert name_value.value == "Ada"

    active_key, active_value = items[1]
    assert active_key.value == "active"
    assert active_value.value is True

    scores_key, scores_value = items[2]
    assert scores_key.value == "scores"
    assert isinstance(scores_value, ListToken)
    assert [item.value for item in scores_value.value] == [1, 2.5, None]


def test_tokenize_json_rejects_empty_content():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0


def test_tokenize_json_reports_invalid_json_position():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.position.line_no == 1
    assert error.position.column_no == 10
    assert error.position.char_index == 9


def test_tokenize_json_accepts_bytes():
    token = module_0.tokenize_json(b'["value", 42]')

    assert isinstance(token, ListToken)
    assert [item.value for item in token.value] == ["value", 42]

# Generated at 2026-10-24 06:16:18.803367
# Unit test for function tokenize_json
def test_tokenize_json():
    expected = {
        "name": "Alice",
        "age": 30,
        "active": True,
        "tags": ["admin", "user"],
        "metadata": None,
    }

    content = (
        '{"name":"Alice","age":30,"active":true,'
        '"tags":["admin","user"],"metadata":null}'
    )

    # Valid string input.
    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == expected

    # Valid bytes input.
    bytes_token = module_0.tokenize_json(content.encode("utf-8"))

    assert isinstance(bytes_token, DictToken)
    assert bytes_token.value == expected

    # Empty input produces a specific parsing failure.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("   \n\t")

    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1,
        line_no=1,
        char_index=0,
    )

    # Malformed JSON produces a general parsing failure.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 06:16:59.846739
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30, "active": true, "tags": ["admin", null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "tags": ["admin", None],
    }
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

# Generated at 2026-10-24 06:17:11.087463
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30, "active": true, "tags": ["admin", null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    assert token.value["name"].value == "Alice"
    assert token.value["age"].value == 30
    assert token.value["active"].value is True

    tags = token.value["tags"]
    assert isinstance(tags, ListToken)
    assert [item.value for item in tags.value] == ["admin", None]

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("")

    assert exc_info.value.code == "no_content"

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 06:17:26.992238
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Ada","scores":[10,20],"active":true,"note":null}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Ada"

    assert isinstance(values["scores"], ListToken)
    assert [item.value for item in values["scores"].value] == [10, 20]

    assert values["active"].value is True
    assert values["note"].value is None

    # Token positions should identify the corresponding source text.
    name_token = values["name"]
    assert content[name_token.start : name_token.end + 1] == '"Ada"'

    # Bytes input is supported.
    number_token = module_0.tokenize_json(b"42")
    assert isinstance(number_token, ScalarToken)
    assert number_token.value == 42

    # Empty and malformed JSON produce ParseError.
    with pytest.raises(ParseError) as empty_error:
        module_0.tokenize_json("   ")
    assert empty_error.value.code == "no_content"
    assert empty_error.value.position.char_index == 0

    with pytest.raises(ParseError) as malformed_error:
        module_0.tokenize_json('{"name": }')
    assert malformed_error.value.code == "parse_error"

# Generated at 2026-10-24 06:17:38.519197
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30, "active": true, "tags": ["admin", null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["age"], ScalarToken)
    assert values["age"].value == 30

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["tags"], ListToken)
    assert [item.value for item in values["tags"].value] == ["admin", None]

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json("")

    assert exc_info.value.code == "no_content"

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 06:18:01.494532
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name": "Alice", "active": true, '
        '"scores": [10, 20], "details": {"age": 30}}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["scores"], ListToken)
    assert [item.value for item in values["scores"].value] == [10, 20]

    assert isinstance(values["details"], DictToken)
    details = {
        key.value: value for key, value in values["details"].value.items()
    }
    assert details["age"].value == 30


def test_tokenize_json_accepts_bytes():
    token = module_0.tokenize_json(b"42")

    assert isinstance(token, ScalarToken)
    assert token.value == 42


def test_tokenize_json_rejects_empty_content():
    with pytest.raises(ParseError):
        module_0.tokenize_json(" \n\t ")


def test_tokenize_json_rejects_invalid_json():
    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')