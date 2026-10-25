

# Generated at 2026-10-24 20:49:01.939203
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

# Generated at 2026-10-24 20:49:04.588586
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

# Generated at 2026-10-24 20:49:07.360768
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

# Generated at 2026-10-24 20:49:10.097570
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

# Generated at 2026-10-24 20:49:12.846601
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

# Generated at 2026-10-24 20:49:15.524278
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:18.178408
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:20.850459
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:23.510588
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:26.160250
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:28.805367
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:31.496226
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:34.183251
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:36.937419
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:39.459715
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:41.976073
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:44.395010
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:46.810782
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:49.230036
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:51.646203
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:54.063528
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:56.480535
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:49:59.045342
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:01.464696
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:03.884215
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:06.298846
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:08.715389
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:11.131169
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:13.549823
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:15.966357
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:18.386399
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:20.804462
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:23.219177
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:25.639224
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:28.057505
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:30.471908
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:32.888044
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:35.302694
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:37.718398
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:40.136095
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:42.553239
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:44.971736
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:47.390173
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:49.809747
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:52.225996
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:54.645444
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:50:57.368402
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:00.081793
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:02.752158
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:05.176746
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:07.592307
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:10.011316
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:12.600680
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:15.340665
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:18.108522
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:20.823193
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:23.538606
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:26.188906
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:28.839436
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:31.526598
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:34.237072
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:36.950981
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:39.721809
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:42.471227
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:45.149951
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:49.688087
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:52.110941
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:54.531744
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:56.947337
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:51:59.366911
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:01.785219
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:04.207952
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:06.626392
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:09.046811
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:11.463736
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:13.880557
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:16.296439
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:18.713962
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:21.131454
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:23.547996
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:26.306592
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:29.016027
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:31.662713
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:34.352356
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:37.163440
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:39.927768
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:42.613491
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:45.281656
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:47.936310
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:50.676981
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:53.372781
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:56.032256
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:52:58.552161
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:00.968497
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:03.503402
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:07.866704
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:10.397942
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:12.818401
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:15.237863
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:17.649989
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:20.069441
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:22.488524
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:24.903945
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:27.323666
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:29.737964
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:32.161203
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:34.575943
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:36.989956
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:39.613754
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:42.494525
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:45.161175
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:47.816268
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:50.556164
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:53.316447
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:55.973807
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:53:58.634069
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:01.334276
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:04.067974
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:06.812372
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:09.470114
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:12.196639
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:14.836648
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:17.476289
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:20.068181
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:22.488024
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:46.673295
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:49.340493
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:52.032431
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:54.780939
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:54:57.550596
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:00.260264
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:02.822486
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:05.344621
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:07.760054
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:10.276128
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:12.693934
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:15.213997
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:17.632049
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:20.048138
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:22.463588
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:24.883752
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:27.301041
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:29.717783
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:32.295374
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:34.961594
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:37.618869
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:40.282209
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:42.837926
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:45.255578
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:48.075806
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:50.733149
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:53.389304
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:56.048570
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:55:58.716999
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:01.402448
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:15.863443
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:18.277762
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:20.695904
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:23.112781
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:25.532864
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:27.949328
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:30.368324
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:32.787837
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:35.202151
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:37.619828
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:40.035699
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:42.452893
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:44.870054
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:47.286153
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:49.703152
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:52.121118
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:54.534050
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:56.953091
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:56:59.401744
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:01.789741
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:04.445189
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:07.114764
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:09.853350
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:12.517556
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:15.164166
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:17.871140
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:20.407864
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:22.826280
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:25.245156
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:57:27.664325
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:10.865083
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:13.554341
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:16.215978
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:18.981030
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:21.499997
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:23.918096
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:26.440761
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:28.859686
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:31.278711
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:33.696082
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:36.112931
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:38.530766
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:40.949971
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:43.480745
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:46.136406
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:48.791909
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:51.470852
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:54.203462
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:56.978826
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:58:59.633707
# Unit test for function tokenize_json

# Generated at 2026-10-24 20:59:02.306128
# Unit test for function tokenize_json