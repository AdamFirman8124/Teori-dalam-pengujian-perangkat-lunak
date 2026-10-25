

# Generated at 2026-10-24 05:33:28.411751
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"name": "example"}'
    scanner = Mock(name="scanner")

    with patch(
        f"{_TokenizingDecoder.__module__}._make_scanner",
        return_value=scanner,
    ) as make_scanner:
        decoder = _TokenizingDecoder(content=content, strict=False)

    make_scanner.assert_called_once_with(decoder, content)
    assert decoder.scan_once is scanner
    assert decoder.strict is False

# Generated at 2026-10-24 05:33:51.263580
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Ada", "values": [1, true, null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    fields = {key.value: value for key, value in token.value.items()}

    name = fields["name"]
    assert isinstance(name, ScalarToken)
    assert name.value == "Ada"
    assert (name.start, name.end) == (9, 13)

    values = fields["values"]
    assert isinstance(values, ListToken)
    assert (values.start, values.end) == (26, 40)
    assert [item.value for item in values.value] == [1, True, None]


def test_tokenize_json_rejects_empty_content():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t ")

    error = exc_info.value
    assert error.text == "No content."
    assert error.code == "no_content"
    assert error.position == Position(column_no=1, line_no=1, char_index=0)


def test_tokenize_json_reports_malformed_json_position():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.position.line_no == 1
    assert error.position.column_no == 10
    assert error.position.char_index == 9

# Generated at 2026-10-24 05:34:01.706719
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"name": "example"}'
    scanner = Mock()
    object_hook = Mock()

    with (
        patch.object(JSONDecoder, "__init__", return_value=None) as decoder_init,
        patch(__name__ + "._make_scanner", return_value=scanner) as make_scanner,
    ):
        decoder = _TokenizingDecoder(
            content=content,
            object_hook=object_hook,
            strict=False,
        )

    decoder_init.assert_called_once_with(
        object_hook=object_hook,
        strict=False,
    )
    make_scanner.assert_called_once_with(decoder, content)
    assert decoder.scan_once is scanner

# Generated at 2026-10-24 05:34:11.842189
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"name": "Alice", "age": 30}'

    decoder = _TokenizingDecoder(content=content)

    assert isinstance(decoder, JSONDecoder)
    assert callable(decoder.scan_once)

    token, end = decoder.scan_once(content, 0)

    assert isinstance(token, DictToken)
    assert end == len(content)

# Generated at 2026-10-24 05:34:29.149124
# Unit test for function validate_json

# Generated at 2026-10-24 05:34:31.652807
# Unit test for function validate_json

# Generated at 2026-10-24 05:34:34.069311
# Unit test for function validate_json

# Generated at 2026-10-24 05:34:36.905039
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:34:39.322590
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:34:40.677383
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 05:35:08.983665
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "name": "Alice",
        "age": 30,
        "active": true,
        "scores": [10, 20.5, null],
        "details": {"verified": false}
    }
    """

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)

# Generated at 2026-10-24 05:35:34.487729
# Unit test for function tokenize_json
def test_tokenize_json():
    content = b"""
    {
        "name": "Alice",
        "age": 30,
        "height": 1.65,
        "active": true,
        "tags": ["admin", null]
    }
    """

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "Alice",
        "age": 30,
        "height": 1.65,
        "active": True,
        "tags": ["admin", None],
    }

    with pytest.raises(ParseError):
        module_0.tokenize_json("")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": "Alice",}')

# Generated at 2026-10-24 05:35:36.904636
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:35:39.322445
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:35:47.997282
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"name": "Alice", "active": true, "age": 30}')

# Generated at 2026-10-24 05:36:06.840933
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Ada", "active": true, "scores": [1, 2.5, null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "Ada",
        "active": True,
        "scores": [1, 2.5, None],
    }
    assert token.start == 0
    assert token.end == len(content) - 1

    # Bytes input is also supported.
    bytes_token = module_0.tokenize_json(b'{"value": 42}')
    assert isinstance(bytes_token, DictToken)
    assert bytes_token.value == {"value": 42}

    # Empty content produces a specific parsing error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        column_no=1,
        line_no=1,
        char_index=0,
    )

    # Malformed JSON produces a positioned parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position == Position(
        column_no=10,
        line_no=1,
        char_index=9,
    )

# Generated at 2026-10-24 05:36:34.897509
# Unit test for function tokenize_json
def test_tokenize_json():
    import pytest

    content = '{"name":"Alice","items":[1,null,true],"meta":{"ok":false}}'
    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["items"], ListToken)
    assert [item.value for item in values["items"].value] == [1, None, True]
    assert all(isinstance(item, ScalarToken) for item in values["items"].value)

    assert isinstance(values["meta"], DictToken)
    meta = {key.value: value for key, value in values["meta"].value.items()}
    assert isinstance(meta["ok"], ScalarToken)
    assert meta["ok"].value is False

    # Bytes input is supported.
    bytes_token = module_0.tokenize_json(b'{"value":42}')
    assert isinstance(bytes_token, DictToken)
    bytes_values = {key.value: value for key, value in bytes_token.value.items()}
    assert bytes_values["value"].value == 42

    # Empty content produces a specific parse error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    assert exc_info.value.code == "no_content"
    assert exc_info.value.text == "No content."
    assert exc_info.value.position == Position(
        column_no=1, line_no=1, char_index=0
    )

    # Malformed JSON reports the decoder's position.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"value":}')

    assert exc_info.value.code == "parse_error"
    assert exc_info.value.text == "Expecting value."
    assert exc_info.value.position == Position(
        column_no=10, line_no=1, char_index=9
    )

# Generated at 2026-10-24 05:36:56.785288
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Alice","age":30,"active":true,'
        '"nothing":null,"tags":["admin",2]}'
    )

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

    assert isinstance(values["nothing"], ScalarToken)
    assert values["nothing"].value is None

    assert isinstance(values["tags"], ListToken)
    assert [item.value for item in values["tags"].value] == ["admin", 2]

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    error = exc_info.value
    assert error.text == "No content."
    assert error.code == "no_content"
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name":}')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 05:37:24.533158
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:37:26.201325
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 05:37:39.923879
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "age": 30, "active": true, "tags": ["admin", null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)

    items = list(token.value.items())
    assert len(items) == 4

    name_key, name_value = items[0]
    assert isinstance(name_key, ScalarToken)
    assert name_key.value == "name"
    assert isinstance(name_value, ScalarToken)
    assert name_value.value == "Alice"

    age_key, age_value = items[1]
    assert age_key.value == "age"
    assert age_value.value == 30

    active_key, active_value = items[2]
    assert active_key.value == "active"
    assert active_value.value is True

    tags_key, tags_value = items[3]
    assert tags_key.value == "tags"
    assert isinstance(tags_value, ListToken)
    assert [item.value for item in tags_value.value] == ["admin", None]

# Generated at 2026-10-24 05:37:42.342956
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:37:50.877554
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('"hello"')

# Generated at 2026-10-24 05:38:14.368096
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "active": true, "scores": [1, 2]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start_index == 0
    assert token.end_index == len(content) - 1
    assert token.content == content

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["scores"], ListToken)
    assert [item.value for item in values["scores"].value] == [1, 2]

    # Bytes input is supported.
    bytes_token = module_0.tokenize_json(b'"hello"')
    assert isinstance(bytes_token, ScalarToken)
    assert bytes_token.value == "hello"

    # Empty and malformed input raise parsing errors.
    with pytest.raises(ParseError):
        module_0.tokenize_json(" \n\t ")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')

# Generated at 2026-10-24 05:38:37.984691
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name":"Alice","items":[1,true,null],"details":{"active":false}}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    def unwrap(current: Token) -> typing.Any:
        if isinstance(current, ScalarToken):
            return current.value
        if isinstance(current, ListToken):
            return [unwrap(item) for item in current.value]
        if isinstance(current, DictToken):
            return {
                unwrap(key): unwrap(value)
                for key, value in current.value.items()
            }
        raise AssertionError(f"Unexpected token type: {type(current)!r}")

    assert unwrap(token) == {
        "name": "Alice",
        "items": [1, True, None],
        "details": {"active": False},
    }

    items_token = next(
        value for key, value in token.value.items() if key.value == "items"
    )
    assert isinstance(items_token, ListToken)
    assert content[items_token.start : items_token.end + 1] == "[1,true,null]"

# Generated at 2026-10-24 05:38:40.399527
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:38:42.815182
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:38:52.627134
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"name": "Alice", "age": 30}')

# Generated at 2026-10-24 05:39:17.305467
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Alice","age":30,"active":true,'
        '"scores":[1,2.5],"note":null}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "Alice",
        "age": 30,
        "active": True,
        "scores": [1, 2.5],
        "note": None,
    }

    # Bytes input should produce the same parsed value.
    bytes_token = module_0.tokenize_json(content.encode("utf-8"))
    assert isinstance(bytes_token, DictToken)
    assert bytes_token.value == token.value

    # Empty or whitespace-only content has a specific error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    assert exc_info.value.code == "no_content"
    assert exc_info.value.text == "No content."
    assert exc_info.value.position == Position(
        column_no=1,
        line_no=1,
        char_index=0,
    )

    # Invalid JSON should be converted from JSONDecodeError to ParseError.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 05:39:34.509849
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Alice","age":30,"active":true,'
        '"score":1.5,"tags":["admin",null]}'
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
        "score": 1.5,
        "tags": ["admin", None],
    }

    # Bytes input should also be accepted.
    bytes_token = module_0.tokenize_json(b'{"value":42}')
    assert unwrap(bytes_token) == {"value": 42}

    # Empty and malformed JSON should produce ParseError.
    with pytest.raises(ParseError):
        module_0.tokenize_json("   ")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name":}')

# Generated at 2026-10-24 05:39:37.071941
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:39:39.486835
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:39:41.903987
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:39:44.319055
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:39:45.670066
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 05:40:08.200186
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "active": true, "items": [1, null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["items"], ListToken)
    assert [item.value for item in values["items"].value] == [1, None]

    # Bytes input is supported.
    bytes_token = module_0.tokenize_json(b'{"value": 42}')
    assert isinstance(bytes_token, DictToken)
    bytes_values = {key.value: value for key, value in bytes_token.value.items()}
    assert bytes_values["value"].value == 42

    # Empty input produces a positionally marked error.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.text == "No content."
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    # Malformed JSON reports the parser position.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"a":}')

    error = exc_info.value
    assert error.code == "parse_error"
    assert error.text == "Expecting value."
    assert error.position.line_no == 1
    assert error.position.column_no == 6
    assert error.position.char_index == 5

# Generated at 2026-10-24 05:40:19.670752
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "active": true, "scores": [10, 20], "extra": null}'
    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    assert isinstance(values["scores"], ListToken)
    assert [item.value for item in values["scores"].value] == [10, 20]

    assert isinstance(values["extra"], ScalarToken)
    assert values["extra"].value is None

    # Bytes input is accepted.
    bytes_token = module_0.tokenize_json(b'"hello"')
    assert isinstance(bytes_token, ScalarToken)
    assert bytes_token.value == "hello"

    # Empty and malformed content produce positional parse errors.
    with pytest.raises(ParseError):
        module_0.tokenize_json("   ")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')

# Generated at 2026-10-24 05:40:22.089030
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:24.503343
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:26.918584
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:29.411349
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:31.827536
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:34.243824
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:36.658409
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:39.073059
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:41.485664
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:43.901278
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:46.316135
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:48.731480
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:51.146776
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:53.565142
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:55.975501
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:58.556489
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:40:59.857863
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 05:41:20.902462
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "active": true, "scores": [1, null]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.content == content
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Alice"

    assert isinstance(values["active"], ScalarToken)
    assert values["active"].value is True

    scores = values["scores"]
    assert isinstance(scores, ListToken)
    assert [item.value for item in scores.value] == [1, None]

    # Every token's source range is inclusive.
    assert (
        content[token.start_index : token.end_index + 1]
        == content
    )

    # Bytes input is supported.
    byte_token = module_0.tokenize_json(b'"hello"')
    assert isinstance(byte_token, ScalarToken)
    assert byte_token.value == "hello"

    # Empty input produces a positionally marked ParseError.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json(" \n\t")

    error = exc_info.value
    assert error.code == "no_content"
    assert error.position.line_no == 1
    assert error.position.column_no == 1
    assert error.position.char_index == 0

    # Malformed JSON also produces a ParseError.
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_json('{"name": }')

    assert exc_info.value.code == "parse_error"

# Generated at 2026-10-24 05:41:39.642692
# Unit test for function tokenize_json
def test_tokenize_json():
    content = (
        '{"name":"Ada","age":37,"score":-2.5e2,'
        '"active":true,"missing":null,'
        '"items":[1,2.5,{"ok":false}]}'
    )

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)

    values = {key.value: value for key, value in token.value.items()}

    assert isinstance(values["name"], ScalarToken)
    assert values["name"].value == "Ada"

    assert isinstance(values["age"], ScalarToken)
    assert values["age"].value == 37

    assert isinstance(values["score"], ScalarToken)
    assert values["score"].value == -250.0

    assert values["active"].value is True
    assert values["missing"].value is None

    items = values["items"]
    assert isinstance(items, ListToken)
    assert [item.value for item in items.value[:2]] == [1, 2.5]

    nested = items.value[2]
    assert isinstance(nested, DictToken)
    nested_values = {key.value: value for key, value in nested.value.items()}
    assert nested_values["ok"].value is False

    # The root token covers the complete JSON document.
    assert token.start.char_index == 0
    assert token.end.char_index == len(content) - 1

    # Bytes input is supported.
    bytes_token = module_0.tokenize_json(b'["value"]')
    assert isinstance(bytes_token, ListToken)
    assert bytes_token.value[0].value == "value"

    # Empty and malformed JSON produce ParseError.
    with pytest.raises(ParseError):
        module_0.tokenize_json("   \n\t")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')

# Generated at 2026-10-24 05:41:42.058399
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:41:44.596898
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:41:47.115932
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:41:49.529861
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:41:51.944569
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:41:54.360867
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:41:56.774872
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:41:59.190474
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:42:00.573330
# Unit test for function tokenize_json
def test_tokenize_json():token = module_0.tokenize_json('{"a": 1, "b": [true, null, "x"]}')

# Generated at 2026-10-24 05:42:29.511000
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Ada", "items": [1, true, null]}'

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
    assert name_key.start == 1
    assert name_key.end == 6

    assert isinstance(name_value, ScalarToken)
    assert name_value.value == "Ada"
    assert name_value.start == 9

# Generated at 2026-10-24 05:42:46.634811
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alice", "items": [1, null, true]}'

    token = module_0.tokenize_json(content)

    assert isinstance(token, DictToken)

    fields = {key.value: value for key, value in token.value.items()}

    assert isinstance(fields["name"], ScalarToken)
    assert fields["name"].value == "Alice"

    assert isinstance(fields["items"], ListToken)
    assert [item.value for item in fields["items"].value] == [1, None, True]

    # Bytes input should also be supported.
    bytes_token = module_0.tokenize_json(b'{"value": 42}')
    bytes_fields = {key.value: value for key, value in bytes_token.value.items()}
    assert bytes_fields["value"].value == 42

    # Empty and malformed JSON should produce ParseError.
    with pytest.raises(ParseError):
        module_0.tokenize_json(" \n\t")

    with pytest.raises(ParseError):
        module_0.tokenize_json('{"name": }')

# Generated at 2026-10-24 05:42:49.051409
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:42:52.048960
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:42:54.471681
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:42:56.878556
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:42:59.292801
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:01.709455
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:04.125444
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:06.538540
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:08.956780
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:11.369981
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:13.783162
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:16.200186
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:18.617586
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:21.044065
# Unit test for function tokenize_json

# Generated at 2026-10-24 05:43:23.456670
# Unit test for function tokenize_json