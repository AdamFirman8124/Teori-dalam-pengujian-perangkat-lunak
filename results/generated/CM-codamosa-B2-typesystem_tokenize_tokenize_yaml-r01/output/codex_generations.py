

# Generated at 2026-10-25 12:31:44.377072
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:31:49.604794
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:31:52.654227
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:31:55.844930
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:31:58.503317
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:32:23.389048
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:32:26.350952
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:07.207810
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:10.381264
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:13.615190
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:33:18.164521
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:33:20.007434
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 12:33:39.575339
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:42.653368
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:45.352982
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:47.770579
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:33:50.189978
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:33:52.602514
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:33:55.329770
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:33:57.749058
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:00.470234
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:02.883155
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:05.295729
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:07.708581
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:10.121833
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:12.543181
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:14.957511
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:17.369201
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:36.821315
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: alice\nage: 30\n")

# Generated at 2026-10-25 12:34:43.073566
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 12:34:46.344130
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:49.726284
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:52.139120
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:34:54.553118
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:57.162486
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:34:59.577579
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:02.146888
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:04.562330
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:06.976587
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:09.392377
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:11.806165
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:14.233672
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:16.644876
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:19.055016
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:21.467084
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:35:23.881182
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:26.296791
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:28.709141
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:31.123947
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:33.538526
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:35:54.895021
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = "name: foo\nvalue: 42\n"
    token = module_0.tokenize_yaml(content)

    assert isinstance(token, DictToken)
    assert token.start_index == 0
    assert token.end_index == len(content) - 1

    key = list(token.keys())[0]
    assert isinstance(key, ScalarToken)
    assert key.value == "name"
    assert key.start_index == 0
    assert key.end_index == len("name") - 1

    value = token[key]
    assert isinstance(value, ScalarToken)
    assert value.value == "foo"

    second_key = list(token.keys())[1]
    second_value = token[second_key]
    assert second_value.value == 42
    assert isinstance(second_value.value, int)

    list_content = "items:\n  - 1\n  - 2\n"
    list_token = module_0.tokenize_yaml(list_content)
    assert isinstance(list_token, DictToken)
    items = list_token[list_key := list(list_token.keys())[0]]
    assert isinstance(items, ListToken)
    assert [item.value for item in items] == [1, 2]

# Generated at 2026-10-25 12:36:12.747377
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:15.162973
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:17.761764
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:20.176886
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:22.589345
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:25.002234
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:27.433491
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:29.845328
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:32.253339
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:34.663997
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:37.079254
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:39.493142
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:41.906230
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:44.320877
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:46.736350
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:49.151204
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:51.567805
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:53.982236
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:36:56.395695
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:36:58.809283
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:01.601312
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:04.683312
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:37:07.652802
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: alice\nage: 30\n")

# Generated at 2026-10-25 12:37:26.001950
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:30.999098
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 12:37:36.823114
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:39.506228
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:42.166897
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:44.582081
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:46.995745
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:49.410337
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:52.304655
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:54.719640
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:57.132963
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:37:59.547116
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:38:01.962182
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:38:04.691124
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:38:07.865250
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:38:09.402045
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 12:38:16.265409
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 12:38:19.164325
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:38:39.200965
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 12:38:41.847034
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:38:44.263000
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:38:46.673313
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:38:49.377010
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:38:51.799667
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:38:54.211325
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:38:56.625562
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:38:59.038867
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:01.451306
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:03.865424
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:06.276721
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:08.690586
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:11.102881
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:13.517440
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:16.418365
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: alice\nage: 30\n")

# Generated at 2026-10-25 12:39:20.321053
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:21.777387
# Unit test for function validate_yaml
def test_validate_yaml():from typesystem import String, Integer


# Generated at 2026-10-25 12:39:24.884828
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:29.786516
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:39:32.860489
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: alice\nage: 30\n")

# Generated at 2026-10-25 12:39:35.626636
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:38.039875
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:40.455099
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:43.089985
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:45.503132
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:48.342500
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:50.756562
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:53.170897
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:55.582985
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:39:57.996726
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:00.412246
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:02.824468
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:05.238254
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:07.652252
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:10.066535
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:12.478840
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:14.889923
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:17.303140
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:24.265401
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    from typesystem.base import ParseError, ValidationError
    from typesystem.fields import Integer, String

    if yaml is None:
        pytest.skip("pyyaml is not installed.")

    class Person(Schema):
        name = String()
        age = Integer()

    # 1. Valid YAML string validates and returns the parsed value.
    value = module_0.validate_yaml("name: Alice\nage: 30\n", Person)
    assert value == {"name": "Alice", "age": 30}

    # 2. Bytes input is decoded and validated the same way.
    value = module_0.validate_yaml(b"name: Bob\nage: 25\n", Person)
    assert value == {"name": "Bob", "age": 25}

    # 3. Missing required field raises ValidationError with position info.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("age: 30\n", Person)
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.start_position is not None
    assert message.start_position.line_no == 1

    # 4. Wrong scalar type raises ValidationError pointing at the value.
    with pytest.raises(ValidationError) as exc_info:
        module_0.validate_yaml("name: Alice\nage: not_a_number\n", Person)
    message = exc_info.value.messages[0]
    assert message.code in ("parse", "invalid")
    assert message.start_position.line_no == 2

    # 5. Malformed YAML raises ParseError with a nonzero position.
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("name: [unclosed\n", Person)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no >= 1

    # 6. Empty content raises ParseError with code "no_content".
    with pytest.raises(ParseError) as exc_info:
        module_0.validate_yaml("   \n", Person)
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1

# Generated at 2026-10-25 12:40:29.408264
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:40:32.666723
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: alice\nage: 30\n")

# Generated at 2026-10-25 12:40:39.214156
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:40:42.083982
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:40:47.714475
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: alice\nage: 30\n")

# Generated at 2026-10-25 12:40:50.480299
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:52.896913
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:55.639249
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:40:58.055253
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:00.469227
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:02.883742
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:05.295675
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:08.019721
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:10.433501
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:12.845562
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:15.260184
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:17.675182
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:20.088183
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:22.502738
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:24.918235
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:27.332195
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:29.751343
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:32.164053
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:34.579494
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:36.993939
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:39.404973
# Unit test for function validate_yaml

# Generated at 2026-10-25 12:41:42.316957
# Unit test for function tokenize_yaml

# Generated at 2026-10-25 12:41:45.245293
# Unit test for function tokenize_yaml
def test_tokenize_yaml():token = module_0.tokenize_yaml("name: alice\nage: 30\n")