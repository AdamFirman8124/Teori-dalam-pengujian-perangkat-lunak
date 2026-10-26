

# Generated at 2026-10-25 14:19:12.932005
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    # 1. Constructor accepts content and returns a usable decoder
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)

    # 2. Missing required "content" kwarg raises KeyError
    with pytest.raises(KeyError):
        _TokenizingDecoder()

    # 3. Forwards extra JSONDecoder kwargs (e.g. parse_float, strict)
    decoder = _TokenizingDecoder(
        content="[1.5]",
        strict=True,
        parse_float=float,
        parse_int=int,
    )
    token = decoder.decode("[1.5]")
    assert isinstance(token, ListToken)

    # 4. Decoding produces positional tokens bound to the content string
    decoder = _TokenizingDecoder(content=content)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    key, value = list(token.value.items())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "a"
    assert value.value == 1
    assert value.start == 6

    # 5. scan_once is re-usable across the same decoder instance
    scan_once = decoder.scan_once
    result, end = scan_once(content, 0)
    assert isinstance(result, DictToken)
    assert end == len(content)

    # 6. Invalid JSON still raises JSONDecodeError (with positions)
    from json.decoder import JSONDecodeError

    decoder = _TokenizingDecoder(content="{invalid}")
    with pytest.raises(JSONDecodeError):
        decoder.decode("{invalid}")

# Generated at 2026-10-25 14:19:16.690390
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    # 1. Constructor accepts content and returns a usable decoder
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)

    # 2. Missing required "content" kwarg raises KeyError
    with pytest.raises(KeyError):
        _TokenizingDecoder()

    # 3. Forwards extra JSONDecoder kwargs (e.g. parse_float, strict)
    decoder = _TokenizingDecoder(
        content="[1.5]",
        strict=True,
        parse_float=float,
        parse_int=int,
    )
    token = decoder.decode("[1.5]")
    assert isinstance(token, ListToken)

    # 4. Decoding produces positional tokens bound to the content string
    decoder = _TokenizingDecoder(content=content)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    key, value = list(token.value.items())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "a"
    assert value.value == 1
    assert value.start == 6

    # 5. scan_once is re-usable across the same decoder instance
    scan_once = decoder.scan_once
    result, end = scan_once(content, 0)
    assert isinstance(result, DictToken)
    assert end == len(content)

    # 6. Invalid JSON still raises JSONDecodeError (with positions)
    from json.decoder import JSONDecodeError

    decoder = _TokenizingDecoder(content="{invalid}")
    with pytest.raises(JSONDecodeError):
        decoder.decode("{invalid}")

# Generated at 2026-10-25 14:19:18.019169
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    # 1. Constructor accepts content and returns a usable decoder
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)

    # 2. Missing required "content" kwarg raises KeyError
    with pytest.raises(KeyError):
        _TokenizingDecoder()

    # 3. Forwards extra JSONDecoder kwargs (e.g. parse_float, strict)
    decoder = _TokenizingDecoder(
        content="[1.5]",
        strict=True,
        parse_float=float,
        parse_int=int,
    )
    token = decoder.decode("[1.5]")
    assert isinstance(token, ListToken)

    # 4. Decoding produces positional tokens bound to the content string
    decoder = _TokenizingDecoder(content=content)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    key, value = list(token.value.items())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "a"
    assert value.value == 1
    assert value.start == 6

    # 5. scan_once is re-usable across the same decoder instance
    scan_once = decoder.scan_once
    result, end = scan_once(content, 0)
    assert isinstance(result, DictToken)
    assert end == len(content)

    # 6. Invalid JSON still raises JSONDecodeError (with positions)
    from json.decoder import JSONDecodeError

    decoder = _TokenizingDecoder(content="{invalid}")
    with pytest.raises(JSONDecodeError):
        decoder.decode("{invalid}")

# Generated at 2026-10-25 14:19:20.217644
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    # 1. Constructor accepts content and returns a usable decoder
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)

    # 2. Missing required "content" kwarg raises KeyError
    with pytest.raises(KeyError):
        _TokenizingDecoder()

    # 3. Forwards extra JSONDecoder kwargs (e.g. parse_float, strict)
    decoder = _TokenizingDecoder(
        content="[1.5]",
        strict=True,
        parse_float=float,
        parse_int=int,
    )
    token = decoder.decode("[1.5]")
    assert isinstance(token, ListToken)

    # 4. Decoding produces positional tokens bound to the content string
    decoder = _TokenizingDecoder(content=content)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    key, value = list(token.value.items())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "a"
    assert value.value == 1
    assert value.start == 6

    # 5. scan_once is re-usable across the same decoder instance
    scan_once = decoder.scan_once
    result, end = scan_once(content, 0)
    assert isinstance(result, DictToken)
    assert end == len(content)

    # 6. Invalid JSON still raises JSONDecodeError (with positions)
    from json.decoder import JSONDecodeError

    decoder = _TokenizingDecoder(content="{invalid}")
    with pytest.raises(JSONDecodeError):
        decoder.decode("{invalid}")

# Generated at 2026-10-25 14:19:21.650287
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    # 1. Constructor accepts content and returns a usable decoder
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)
    assert callable(decoder.scan_once)

    # 2. Missing required "content" kwarg raises KeyError
    with pytest.raises(KeyError):
        _TokenizingDecoder()

    # 3. Forwards extra JSONDecoder kwargs (e.g. parse_float, strict)
    decoder = _TokenizingDecoder(
        content="[1.5]",
        strict=True,
        parse_float=float,
        parse_int=int,
    )
    token = decoder.decode("[1.5]")
    assert isinstance(token, ListToken)

    # 4. Decoding produces positional tokens bound to the content string
    decoder = _TokenizingDecoder(content=content)
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(content) - 1
    key, value = list(token.value.items())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "a"
    assert value.value == 1
    assert value.start == 6

    # 5. scan_once is re-usable across the same decoder instance
    scan_once = decoder.scan_once
    result, end = scan_once(content, 0)
    assert isinstance(result, DictToken)
    assert end == len(content)

    # 6. Invalid JSON still raises JSONDecodeError (with positions)
    from json.decoder import JSONDecodeError

    decoder = _TokenizingDecoder(content="{invalid}")
    with pytest.raises(JSONDecodeError):
        decoder.decode("{invalid}")

# Generated at 2026-10-25 14:19:49.402046
# Unit test for function tokenize_json
def test_tokenize_json():content = (
        '{"name":"Ada\\nLovelace","active":true,'
        '"scores":[1,2.5,null],"meta":{"count":3}}'
    )

# Generated at 2026-10-25 14:20:18.074570
# Unit test for function validate_json
def test_validate_json():from unittest.mock import Mock


def test_validate_json(monkeypatch):
    content = '{"name": "Alice"}'
    token = object()
    validator = Mock(spec=Field)
    expected_result = {"name": "Alice"}

    tokenize_mock = Mock(return_value=token)
    validate_mock = Mock(return_value=expected_result)

    monkeypatch.setitem(
        validate_json.__globals__, "tokenize_json", tokenize_mock
    )
    monkeypatch.setitem(
        validate_json.__globals__, "validate_with_positions", validate_mock
    )

    result = module_0.validate_json(content, validator)

    assert result == expected_result
    tokenize_mock.assert_called_once_with(content)
    validate_mock.assert_called_once_with(
        token=token,
        validator=validator,
    )

# Generated at 2026-10-25 14:20:51.168957
# Unit test for function validate_json

# Generated at 2026-10-25 14:21:07.635808
# Unit test for function validate_json
def test_validate_json():from typesystem.fields import Integer

# Generated at 2026-10-25 14:21:41.889173
# Unit test for function validate_json
def test_validate_json():
    content = b'{"name": "Alice"}'
    tokenize_mock = Mock(return_value=sentinel.token)
    validate_mock = Mock(return_value=sentinel.result)

    with patch.dict(
        validate_json.__globals__,
        {
            "tokenize_json": tokenize_mock,
            "validate_with_positions": validate_mock,
        },
    ):
        result = module_0.validate_json(content, sentinel.validator)

    assert result is sentinel.result
    tokenize_mock.assert_called_once_with(content)
    validate_mock.assert_called_once_with(
        token=sentinel.token,
        validator=sentinel.validator,
    )

# Generated at 2026-10-25 14:21:58.436351
# Unit test for function tokenize_json
def test_tokenize_json():
    # Object â DictToken
    token = module_0.tokenize_json('{"a": 1}')
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1}
    assert token.start == 0
    assert token.end == len('{"a": 1}') - 1

    # Array â ListToken
    token = module_0.tokenize_json('[1, "two", null, true]')
    assert isinstance(token, ListToken)
    assert token.value == [1, "two", None, True]

    # Scalar string â ScalarToken
    token = module_0.tokenize_json('"hello"')
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Nested structure
    token = module_0.tokenize_json('{"list": [1, {"x": false}]}')
    assert token.value == {"list": [1, {"x": False}]}

    # Empty object / empty array
    assert isinstance(module_0.tokenize_json("{}"), DictToken)
    assert isinstance(module_0.tokenize_json("[]"), ListToken)

    # Leading/trailing whitespace is allowed
    token = module_0.tokenize_json('  {"a": 1}  \n')
    assert token.value == {"a": 1}

    # Bytes input is decoded as UTF-8
    token = module_0.tokenize_json(b'{"key": "\xc3\xa9"}')  # Ã©
    assert token.value == {"key": "Ã©"}

    # Empty string â ParseError with code "no_content"
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("")
    assert exc.value.code == "no_content"
    assert exc.value.text == "No content."
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 1

    # Whitespace-only string â same "no_content" error
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json("   \n\t ")
    assert exc.value.code == "no_content"

    # Invalid JSON â ParseError with code "parse_error" and position info
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{"a": }')
    assert exc.value.code == "parse_error"
    assert exc.value.position.line_no == 1
    assert exc.value.position.column_no == 7
    assert exc.value.position.char_index == 6

    # Multiline error position: line/column tracked correctly
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_json('{\n  "a": 1,\n  "b": ?\n}')
    assert exc.value.code == "parse_error"
    assert exc.value.position.line_no == 3
    assert exc.value.position.column_no == 8

    # Error message ends with a period
    assert exc.value.text.endswith(".")

# Generated at 2026-10-25 14:22:23.505104
# Unit test for function validate_json
def test_validate_json():
    import sys
    from unittest.mock import patch, sentinel

    module = sys.modules[validate_json.__module__]
    content = '{"name": "Alice"}'
    validator = sentinel.validator
    token = sentinel.token
    expected_result = sentinel.validation_result

    with patch.object(module, "tokenize_json", return_value=token) as mock_tokenize:
        with patch.object(
            module,
            "validate_with_positions",
            return_value=expected_result,
        ) as mock_validate:
            result = module_0.validate_json(content, validator)

    assert result is expected_result
    mock_tokenize.assert_called_once_with(content)
    mock_validate.assert_called_once_with(token=token, validator=validator)

# Generated at 2026-10-25 14:22:59.866999
# Unit test for function validate_json

# Generated at 2026-10-25 14:23:13.281267
# Unit test for function validate_json
def test_validate_json():result = module_0.validate_json(
        '{"name": "Alice", "active": true, "scores": [10, 20]}',
        Field(),
    )

# Generated at 2026-10-25 14:23:41.033918
# Unit test for function validate_json
def test_validate_json():
    content = '{"name": "Alice"}'
    validator = Mock(spec=Field)
    token = Mock(spec=Token)
    expected_result = ({"name": "Alice"}, [])

    with patch(
        "typesystem.tokenize.json.tokenize_json",
        return_value=token,
    ) as mock_tokenize, patch(
        "typesystem.tokenize.json.validate_with_positions",
        return_value=expected_result,
    ) as mock_validate:
        result = module_0.validate_json(content, validator)

    assert result == expected_result
    mock_tokenize.assert_called_once_with(content)
    mock_validate.assert_called_once_with(token=token, validator=validator)

# Generated at 2026-10-25 14:24:18.306274
# Unit test for function validate_json

# Generated at 2026-10-25 14:24:47.898796
# Unit test for function validate_json
def test_validate_json():validator = Field()

# Generated at 2026-10-25 14:24:53.345138
# Unit test for function validate_json

# Generated at 2026-10-25 14:24:58.790846
# Unit test for function validate_json

# Generated at 2026-10-25 14:25:01.207007
# Unit test for function validate_json

# Generated at 2026-10-25 14:25:03.624970
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:06.131532
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:11.608890
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:14.023912
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:16.438360
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:18.853117
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:21.268354
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:23.683417
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:26.097047
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:28.510923
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:30.925302
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:33.339826
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:35.755205
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:38.170255
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:40.583511
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:43.002694
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:45.419898
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:47.832739
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:50.248171
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:52.662687
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:55.077819
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:57.491635
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:25:59.906743
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:02.320948
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:04.740360
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:07.153220
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:09.569423
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:11.984088
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:14.399533
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:16.814254
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:20.506396
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:22.925445
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:25.342943
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:27.756252
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:30.170540
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:32.586642
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:35.001251
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:37.415890
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:39.831159
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:42.250193
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:44.666445
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:47.082685
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:49.495573
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:51.910291
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:54.324813
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:56.740876
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:26:59.155176
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:01.571130
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:03.991068
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:06.405385
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:08.819036
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:11.233974
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:16.678939
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:19.096892
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:21.510429
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:23.925034
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:26.339376
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:28.756566
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:31.174229
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:33.587832
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:36.002382
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:38.420243
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:40.836732
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:43.256361
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:45.674399
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:48.087021
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:50.502472
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:52.918212
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:55.334688
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:27:57.751450
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:00.165277
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:02.580749
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:05.000593
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:07.419505
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:09.835260
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:12.253075
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:14.677449
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:17.092231
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:19.506945
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:21.918983
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:24.333973
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:26.749290
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:29.163392
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:31.580604
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:33.994997
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:36.410113
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:38.825237
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:41.244106
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:43.660889
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:46.075995
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:49.798196
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:52.212886
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:54.627860
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:57.043866
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:28:59.456992
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:29:01.874842
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:29:04.291237
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:29:06.705412
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:29:09.119081
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:29:11.535781
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:29:13.949374
# Unit test for function tokenize_json

# Generated at 2026-10-25 14:29:19.391948
# Unit test for function tokenize_json