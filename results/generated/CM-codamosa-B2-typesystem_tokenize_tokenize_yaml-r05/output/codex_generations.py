

# Generated at 2026-10-24 06:50:23.203346
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:50:25.617315
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:50:28.133318
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:50:30.551231
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:50:32.966760
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:50:35.381067
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:50:55.722376
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:51:29.159104
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:51:32.049893
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:25.361540
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:27.916030
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:30.331114
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:32.874930
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:35.288214
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:37.703831
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:40.120254
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:42.539137
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:45.406365
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:52:59.887878
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import pytest

    # Basic mapping with all scalar types
    token = module_0.tokenize_yaml("name: app\nversion: 2\nratio: 1.5\nenabled: true\nmissing: null\n")
    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "app",
        "version": 2,
        "ratio": 1.5,
        "enabled": True,
        "missing": None,
    }
    # Nested sequence
    token = module_0.tokenize_yaml("items:\n  - a\n  - b\n")
    assert isinstance(token["items"], ListToken)
    assert token["items"].value == ["a", "b"]

    # Tokens carry positions into the source string
    token = module_0.tokenize_yaml("name: app\n")
    assert token.start == 0
    value = token.value["name"]
    assert token.get_value_token_for_key("name").value == "app"

    # Empty content raises ParseError
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("   \n")
    assert exc.value.code == "no_content"
    assert exc.value.position.line_no == 1

    # Invalid YAML raises ParseError with a position
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("foo: [unclosed\n")
    assert exc.value.code == "parse_error"
    assert exc.value.position.line_no == 1

    # Bytes input works
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}

# Generated at 2026-10-24 06:53:01.197614
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import pytest

    # Basic mapping with all scalar types
    token = module_0.tokenize_yaml("name: app\nversion: 2\nratio: 1.5\nenabled: true\nmissing: null\n")
    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "app",
        "version": 2,
        "ratio": 1.5,
        "enabled": True,
        "missing": None,
    }
    # Nested sequence
    token = module_0.tokenize_yaml("items:\n  - a\n  - b\n")
    assert isinstance(token["items"], ListToken)
    assert token["items"].value == ["a", "b"]

    # Tokens carry positions into the source string
    token = module_0.tokenize_yaml("name: app\n")
    assert token.start == 0
    value = token.value["name"]
    assert token.get_value_token_for_key("name").value == "app"

    # Empty content raises ParseError
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("   \n")
    assert exc.value.code == "no_content"
    assert exc.value.position.line_no == 1

    # Invalid YAML raises ParseError with a position
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("foo: [unclosed\n")
    assert exc.value.code == "parse_error"
    assert exc.value.position.line_no == 1

    # Bytes input works
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}

# Generated at 2026-10-24 06:53:19.043902
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:21.756457
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:24.426674
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:26.835775
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:29.358536
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:31.863808
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:34.276222
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:36.691531
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:39.248272
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:53:41.664354
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:53:44.079315
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:53:46.496295
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:53:47.861377
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import pytest

    # Basic mapping with all scalar types
    token = module_0.tokenize_yaml("name: app\nversion: 2\nratio: 1.5\nenabled: true\nmissing: null\n")
    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "app",
        "version": 2,
        "ratio": 1.5,
        "enabled": True,
        "missing": None,
    }
    # Nested sequence
    token = module_0.tokenize_yaml("items:\n  - a\n  - b\n")
    assert isinstance(token["items"], ListToken)
    assert token["items"].value == ["a", "b"]

    # Tokens carry positions into the source string
    token = module_0.tokenize_yaml("name: app\n")
    assert token.start == 0
    value = token.value["name"]
    assert token.get_value_token_for_key("name").value == "app"

    # Empty content raises ParseError
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("   \n")
    assert exc.value.code == "no_content"
    assert exc.value.position.line_no == 1

    # Invalid YAML raises ParseError with a position
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("foo: [unclosed\n")
    assert exc.value.code == "parse_error"
    assert exc.value.position.line_no == 1

    # Bytes input works
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}

# Generated at 2026-10-24 06:53:49.457510
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import pytest

    # Basic mapping with all scalar types
    token = module_0.tokenize_yaml("name: app\nversion: 2\nratio: 1.5\nenabled: true\nmissing: null\n")
    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "app",
        "version": 2,
        "ratio": 1.5,
        "enabled": True,
        "missing": None,
    }
    # Nested sequence
    token = module_0.tokenize_yaml("items:\n  - a\n  - b\n")
    assert isinstance(token["items"], ListToken)
    assert token["items"].value == ["a", "b"]

    # Tokens carry positions into the source string
    token = module_0.tokenize_yaml("name: app\n")
    assert token.start == 0
    value = token.value["name"]
    assert token.get_value_token_for_key("name").value == "app"

    # Empty content raises ParseError
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("   \n")
    assert exc.value.code == "no_content"
    assert exc.value.position.line_no == 1

    # Invalid YAML raises ParseError with a position
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("foo: [unclosed\n")
    assert exc.value.code == "parse_error"
    assert exc.value.position.line_no == 1

    # Bytes input works
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}

# Generated at 2026-10-24 06:53:50.785363
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import pytest

    # Basic mapping with all scalar types
    token = module_0.tokenize_yaml("name: app\nversion: 2\nratio: 1.5\nenabled: true\nmissing: null\n")
    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "app",
        "version": 2,
        "ratio": 1.5,
        "enabled": True,
        "missing": None,
    }
    # Nested sequence
    token = module_0.tokenize_yaml("items:\n  - a\n  - b\n")
    assert isinstance(token["items"], ListToken)
    assert token["items"].value == ["a", "b"]

    # Tokens carry positions into the source string
    token = module_0.tokenize_yaml("name: app\n")
    assert token.start == 0
    value = token.value["name"]
    assert token.get_value_token_for_key("name").value == "app"

    # Empty content raises ParseError
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("   \n")
    assert exc.value.code == "no_content"
    assert exc.value.position.line_no == 1

    # Invalid YAML raises ParseError with a position
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("foo: [unclosed\n")
    assert exc.value.code == "parse_error"
    assert exc.value.position.line_no == 1

    # Bytes input works
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}

# Generated at 2026-10-24 06:54:08.731628
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:11.398803
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:14.089156
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:32.223615
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:34.736239
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:37.153496
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:39.655986
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:42.077360
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:44.625077
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:47.040172
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:49.568993
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:52.380460
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:54:53.699832
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import pytest

    # Basic mapping with all scalar types
    token = module_0.tokenize_yaml("name: app\nversion: 2\nratio: 1.5\nenabled: true\nmissing: null\n")
    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "app",
        "version": 2,
        "ratio": 1.5,
        "enabled": True,
        "missing": None,
    }
    # Nested sequence
    token = module_0.tokenize_yaml("items:\n  - a\n  - b\n")
    assert isinstance(token["items"], ListToken)
    assert token["items"].value == ["a", "b"]

    # Tokens carry positions into the source string
    token = module_0.tokenize_yaml("name: app\n")
    assert token.start == 0
    value = token.value["name"]
    assert token.get_value_token_for_key("name").value == "app"

    # Empty content raises ParseError
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("   \n")
    assert exc.value.code == "no_content"
    assert exc.value.position.line_no == 1

    # Invalid YAML raises ParseError with a position
    with pytest.raises(ParseError) as exc:
        module_0.tokenize_yaml("foo: [unclosed\n")
    assert exc.value.code == "parse_error"
    assert exc.value.position.line_no == 1

    # Bytes input works
    token = module_0.tokenize_yaml(b"key: value\n")
    assert token.value == {"key": "value"}

# Generated at 2026-10-24 06:55:11.572394
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:14.266971
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:16.982593
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:34.699367
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:37.342135
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:39.756799
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:42.168972
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:44.583957
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:46.998580
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:49.411195
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:51.980526
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:55:54.676677
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:12.603832
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:15.310288
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:17.981657
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:20.399768
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:22.816833
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:25.235304
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:27.829801
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:30.240098
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:32.655265
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:35.070249
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:37.488414
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:39.901705
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:42.315801
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:44.730462
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:47.148401
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:49.562584
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:51.977551
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:54.391297
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:56:56.811325
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:56:59.226112
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:58:37.296545
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 06:58:50.717086
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:58:55.017095
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:58:57.606061
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:59:00.021319
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:59:02.436359
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:59:04.965523
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:59:23.332090
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:59:26.133799
# Unit test for function validate_yaml

# Generated at 2026-10-24 06:59:38.132407
# Unit test for function validate_yaml

# Generated at 2026-10-24 07:00:08.639179
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 07:00:20.362648
# Unit test for function tokenize_yaml

# Generated at 2026-10-24 07:00:36.085917
# Unit test for function tokenize_yaml