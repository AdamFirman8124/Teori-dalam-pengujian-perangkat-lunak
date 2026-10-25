

# Generated at 2026-10-24 19:13:02.656935
# Unit test for function validate_json
def test_validate_json():
    import typing

    import typesystem

    class Book(typesystem.Schema):
        title = typesystem.String(max_length=100)
        author = typesystem.String()
        num_pages = typesystem.Integer(default=0)

    # 1. Valid JSON string parses and validates cleanly.
    content = '{"title": "Frankenstein", "author": "Mary Shelley", "num_pages": 280}'
    value, error_messages = module_0.validate_json(content, validator=Book)
    assert error_messages == []
    assert value.title == "Frankenstein"
    assert value.author == "Mary Shelley"
    assert value.num_pages == 280

    # 2. Bytes input is decoded (utf-8) and validated.
    value, error_messages = module_0.validate_json(
        '{"title": "Ozymandias", "author": "Percy Shelley"}'.encode("utf-8"),
        validator=Book,
    )
    assert error_messages == []
    assert value.title == "Ozymandias"
    assert value.author == "Percy Shelley"
    assert value.num_pages == 0  # default applied

    # 3. Empty / whitespace-only content raises a ParseError with clear code.
    for empty in ("", "   \n\t "):
        try:
            module_0.validate_json(empty, validator=Book)
        except ParseError as exc:
            assert exc.code == "no_content"
            assert exc.text == "No content."
            assert exc.position.line_no == 1
            assert exc.position.column_no == 1
            assert exc.position.char_index == 0
        else:
            raise AssertionError("Expected ParseError for empty content.")

    # 4. Malformed JSON raises a ParseError with positional information.
    try:
        module_0.validate_json('{"title": "Dracula", "author": }', validator=Book)
    except ParseError as exc:
        assert exc.code == "parse_error"
        assert "Expecting value" in exc.text
        assert exc.position.line_no == 1
        assert exc.position.column_no > 1
        assert exc.position.char_index > 0
    else:
        raise AssertionError("Expected ParseError for malformed JSON.")

    # 5. Multi-line JSON: error position points at the correct line.
    multiline = '{\n  "title": "Dracula",\n  "author": \n}\n'
    try:
        module_0.validate_json(multiline, validator=Book)
    except ParseError as exc:
        assert exc.code == "parse_error"
        assert exc.position.line_no == 4
        assert exc.position.column_no == 1
    else:
        raise AssertionError("Expected ParseError for malformed multi-line JSON.")

    # 6. Validation failure: wrong type is reported as ValidationError,
    #    not ParseError (JSON itself was valid).
    try:
        module_0.validate_json('{"title": "Dracula", "author": "Stoker"}', validator=Book)
    except ValidationError as exc:
        messages = exc.messages()
        assert len(messages) == 1
        assert messages[0].code == "required"
        assert messages[0].index == ["num_pages"]
    else:
        raise AssertionError("Expected ValidationError for missing required field.")

    # 7. Validation failure with position info: bad type on a known field.
    try:
        module_0.validate_json(
            '{"title": "Dracula", "author": "Stoker", "num_pages": "many"}',
            validator=Book,
        )
    except ValidationError as exc:
        messages = exc.messages()
        assert len(messages) == 1
        assert messages[0].code == "parse_error"
        assert messages[0].text == "Must be a number."
        assert messages[0].start_position.char_index == 47
    else:
        raise AssertionError("Expected ValidationError for invalid field type.")

    # 8. Validation failure using a bare Field validator.
    value, error_messages = module_0.validate_json('{"a": 1}', validator=Book)
    assert value == {"a": 1}
    assert len(error_messages) == 2
    codes = {message.code for message in error_messages}
    assert codes == {"required"}
    indexes = {message.index for message in error_messages}
    assert indexes == {["title"], ["author"]}

    # 9. Scalar content against an object schema fails validation, not parsing.
    try:
        module_0.validate_json('"just a string"', validator=Book)
    except ValidationError as exc:
        messages = exc.messages()
        assert len(messages) == 1
        assert messages[0].code == "invalid"
    else:
        raise AssertionError("Expected ValidationError for non-object JSON.")

# Generated at 2026-10-24 19:13:05.342784
# Unit test for function validate_json
def test_validate_json():
    import typing

    import typesystem

    class Book(typesystem.Schema):
        title = typesystem.String(max_length=100)
        author = typesystem.String()
        num_pages = typesystem.Integer(default=0)

    # 1. Valid JSON string parses and validates cleanly.
    content = '{"title": "Frankenstein", "author": "Mary Shelley", "num_pages": 280}'
    value, error_messages = module_0.validate_json(content, validator=Book)
    assert error_messages == []
    assert value.title == "Frankenstein"
    assert value.author == "Mary Shelley"
    assert value.num_pages == 280

    # 2. Bytes input is decoded (utf-8) and validated.
    value, error_messages = module_0.validate_json(
        '{"title": "Ozymandias", "author": "Percy Shelley"}'.encode("utf-8"),
        validator=Book,
    )
    assert error_messages == []
    assert value.title == "Ozymandias"
    assert value.author == "Percy Shelley"
    assert value.num_pages == 0  # default applied

    # 3. Empty / whitespace-only content raises a ParseError with clear code.
    for empty in ("", "   \n\t "):
        try:
            module_0.validate_json(empty, validator=Book)
        except ParseError as exc:
            assert exc.code == "no_content"
            assert exc.text == "No content."
            assert exc.position.line_no == 1
            assert exc.position.column_no == 1
            assert exc.position.char_index == 0
        else:
            raise AssertionError("Expected ParseError for empty content.")

    # 4. Malformed JSON raises a ParseError with positional information.
    try:
        module_0.validate_json('{"title": "Dracula", "author": }', validator=Book)
    except ParseError as exc:
        assert exc.code == "parse_error"
        assert "Expecting value" in exc.text
        assert exc.position.line_no == 1
        assert exc.position.column_no > 1
        assert exc.position.char_index > 0
    else:
        raise AssertionError("Expected ParseError for malformed JSON.")

    # 5. Multi-line JSON: error position points at the correct line.
    multiline = '{\n  "title": "Dracula",\n  "author": \n}\n'
    try:
        module_0.validate_json(multiline, validator=Book)
    except ParseError as exc:
        assert exc.code == "parse_error"
        assert exc.position.line_no == 4
        assert exc.position.column_no == 1
    else:
        raise AssertionError("Expected ParseError for malformed multi-line JSON.")

    # 6. Validation failure: wrong type is reported as ValidationError,
    #    not ParseError (JSON itself was valid).
    try:
        module_0.validate_json('{"title": "Dracula", "author": "Stoker"}', validator=Book)
    except ValidationError as exc:
        messages = exc.messages()
        assert len(messages) == 1
        assert messages[0].code == "required"
        assert messages[0].index == ["num_pages"]
    else:
        raise AssertionError("Expected ValidationError for missing required field.")

    # 7. Validation failure with position info: bad type on a known field.
    try:
        module_0.validate_json(
            '{"title": "Dracula", "author": "Stoker", "num_pages": "many"}',
            validator=Book,
        )
    except ValidationError as exc:
        messages = exc.messages()
        assert len(messages) == 1
        assert messages[0].code == "parse_error"
        assert messages[0].text == "Must be a number."
        assert messages[0].start_position.char_index == 47
    else:
        raise AssertionError("Expected ValidationError for invalid field type.")

    # 8. Validation failure using a bare Field validator.
    value, error_messages = module_0.validate_json('{"a": 1}', validator=Book)
    assert value == {"a": 1}
    assert len(error_messages) == 2
    codes = {message.code for message in error_messages}
    assert codes == {"required"}
    indexes = {message.index for message in error_messages}
    assert indexes == {["title"], ["author"]}

    # 9. Scalar content against an object schema fails validation, not parsing.
    try:
        module_0.validate_json('"just a string"', validator=Book)
    except ValidationError as exc:
        messages = exc.messages()
        assert len(messages) == 1
        assert messages[0].code == "invalid"
    else:
        raise AssertionError("Expected ValidationError for non-object JSON.")

# Generated at 2026-10-24 19:13:07.883304
# Unit test for function validate_json

# Generated at 2026-10-24 19:13:10.300541
# Unit test for function validate_json

# Generated at 2026-10-24 19:13:12.717494
# Unit test for function validate_json

# Generated at 2026-10-24 19:13:15.138686
# Unit test for function validate_json

# Generated at 2026-10-24 19:13:17.555071
# Unit test for function validate_json

# Generated at 2026-10-24 19:13:19.972168
# Unit test for function validate_json

# Generated at 2026-10-24 19:13:26.054858
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    import pytest

    # Missing required 'content' kwarg raises KeyError.
    with pytest.raises(KeyError):
        _TokenizingDecoder()

    # Constructor accepts 'content', sets up scan_once, and passes
    # through standard JSONDecoder kwargs.
    decoder = _TokenizingDecoder(content='{"key": "value"}')
    assert isinstance(decoder, JSONDecoder)
    assert callable(decoder.scan_once)

    # The scan_once callable produced by the constructor tokenizes
    # JSON, returning a (Token, end_position) tuple.
    token, end = decoder.scan_once('{"key": "value"}', 0)
    assert isinstance(token, DictToken)
    assert end == len('{"key": "value"}')
    assert token._value["key"]._value == "value"

    # Extra JSONDecoder kwargs are forwarded to the parent class.
    decoder = _TokenizingDecoder(content="[1, 2]", object_pairs_hook=dict)
    assert isinstance(decoder, JSONDecoder)
    token, end = decoder.scan_once("[1, 2]", 0)
    assert isinstance(token, ListToken)
    assert end == len("[1, 2]")

# Generated at 2026-10-24 19:13:28.726700
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:31.438160
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:34.106128
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:37.015752
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:39.683806
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:42.338582
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:44.993711
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:47.664968
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:50.324929
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:53.108260
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:55.768921
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:13:58.188981
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:00.606213
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:03.025826
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:05.577172
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:08.002660
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:10.420590
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:12.840844
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:15.424192
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:17.838983
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:20.263944
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:22.681046
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:25.101511
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:27.519195
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:29.935063
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:32.375497
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:34.783434
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:37.203839
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:39.620688
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:42.039810
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:44.455662
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:47.168791
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:49.874905
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:52.537528
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:55.179669
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:14:57.913977
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:00.728464
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:03.563934
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:05.980184
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:08.396065
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:10.813469
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:13.230686
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:15.649960
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:18.065416
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:20.481690
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:22.899039
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:25.313524
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:27.911223
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:30.575223
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:33.342997
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:36.029183
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:38.687146
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:41.457304
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:44.193723
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:46.962512
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:49.649212
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:52.323763
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:55.047303
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:15:57.585602
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:00.002128
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:02.422770
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:05.011311
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:07.429560
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:09.978423
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:12.390615
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:14.801941
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:17.219615
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:19.637397
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:22.055452
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:24.499703
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:26.946407
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:29.389257
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:31.805919
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:34.224262
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:36.636032
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:39.056878
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:41.475997
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:43.896779
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:46.312534
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:48.728218
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:51.147110
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:53.565081
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:55.981939
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:16:58.400857
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:00.815984
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:03.232985
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:05.649003
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:08.065715
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:10.483277
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:12.898267
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:17.590037
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:20.005778
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:22.423440
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:24.840661
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:27.493215
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:30.199883
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:32.946627
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:35.595227
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:38.236713
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:40.887932
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:43.562044
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:46.190293
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:48.606459
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:51.022078
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:53.593318
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:56.010595
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:17:58.429357
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:00.844229
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:03.263968
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:05.680733
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:08.098286
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:10.516184
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:12.935615
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:15.348301
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:17.762721
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:20.179055
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:22.597886
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:25.016772
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:27.433277
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:29.851060
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:42.222976
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:44.640046
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:47.060282
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:49.477934
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:51.894066
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:54.312265
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:56.730143
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:18:59.146477
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:01.578113
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:03.994411
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:06.424167
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:08.859760
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:11.290054
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:13.708608
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:16.125597
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:18.853177
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:21.506198
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:24.454158
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:27.131591
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:29.785939
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:32.507699
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:35.185346
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:37.833015
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:40.469803
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:43.012595
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:45.429031
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:47.847391
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:50.260771
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:52.677580
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:19:55.094524
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:03.514928
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:05.933662
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:08.351323
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:10.765685
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:13.186131
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:15.603882
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:18.021004
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:20.438511
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:22.858604
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:25.274663
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:27.691048
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:30.395022
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:33.043154
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:35.699082
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:38.358095
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:41.012830
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:43.716817
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:46.369997
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:48.788955
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:51.205999
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:53.624486
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:56.040125
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:20:58.456976
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:00.983950
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:03.398353
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:05.816843
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:08.233623
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:10.652442
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:13.069843
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:15.486333
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:28.099126
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:30.803044
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:33.443581
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:36.141837
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:38.795490
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:41.536218
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:44.185913
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:46.874827
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:49.667371
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:54.461551
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:56.879924
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:21:59.294845
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:01.715094
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:04.131542
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:06.548115
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:08.967730
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:11.384121
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:13.951873
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:16.368831
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:18.787093
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:21.203567
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:23.622313
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:26.040515
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:28.455798
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:30.878518
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:33.292311
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:35.709899
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:38.124842
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:40.542008
# Unit test for function tokenize_json

# Generated at 2026-10-24 19:22:42.963153
# Unit test for function tokenize_json