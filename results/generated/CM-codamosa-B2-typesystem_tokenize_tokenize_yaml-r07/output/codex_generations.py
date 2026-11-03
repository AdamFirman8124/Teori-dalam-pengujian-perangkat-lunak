

# Generated at 2026-11-01 21:08:03.955384
# Unit test for function tokenize_yaml
def test_tokenize_yaml():import pytest

pytestmark = pytest.mark.skipif(yaml is None, reason="pyyaml is not installed")


def test_tokenize_yaml_dict():
    content = "name: John\nage: 22"
    token = module_0.tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"name": "John", "age": 22}
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content


def test_tokenize_yaml_inline_dict():
    token = module_0.tokenize_yaml("{a: 123}")
    assert isinstance(token, DictToken)
    assert token.value == {"a": 123}


def test_tokenize_yaml_nested():
    content = "root:\n  child:\n    leaf: true"
    token = module_0.tokenize_yaml(content)
    assert token.value == {"root": {"child": {"leaf": True}}}


def test_tokenize_yaml_list():
    content = "- 1\n- 2\n- 3"
    token = module_0.tokenize_yaml(content)
    assert isinstance(token, ListToken)
    assert token.value == [1, 2, 3]


def test_tokenize_yaml_scalars():
    assert module_0.tokenize_yaml("123").value == 123
    assert module_0.tokenize_yaml("1.25").value == 1.25
    assert module_0.tokenize_yaml("true").value is True
    assert module_0.tokenize_yaml("false").value is False
    assert module_0.tokenize_yaml("null").value is None
    assert module_0.tokenize_yaml("~").value is None
    assert module_0.tokenize_yaml("'hello world'").value == "hello world"


def test_tokenize_yaml_bytes_input():
    token = module_0.tokenize_yaml(b"a: 1\nb: two")
    assert token.value == {"a": 1, "b": "two"}
    assert token.content == "a: 1\nb: two"


def test_tokenize_yaml_empty_string_raises_no_content():
    for content in ("", "   ", "\n"):
        with pytest.raises(ParseError) as exc_info:
            module_0.tokenize_yaml(content)
        assert exc_info.value.code == "no_content"
        assert exc_info.value.text == "No content."
        assert exc_info.value.position == Position(
            line_no=1, column_no=1, char_index=0
        )


def test_tokenize_yaml_parse_error():
    content = "{unclosed"
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml(content)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.text.endswith(".")
    assert isinstance(exc_info.value.position, Position)


def test_tokenize_yaml_parse_error_position():
    content = "valid: 1\ninvalid: yaml: oops"
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml(content)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no == 2


def test_tokenize_yaml_child_token_positions():
    content = "outer: hello"
    token = module_0.tokenize_yaml(content)
    children = list(dict(token.get_value())) if hasattr(token, "get_value") else []
    # Verify scalar values retain their source positions via lookup.
    scalar = token.lookup(0, "outer")
    assert isinstance(scalar, ScalarToken)
    assert scalar.value == "hello"
    assert scalar.char_index == content.index("hello")

# Generated at 2026-11-01 21:09:42.219387
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest

    validator = Schema(properties={"a": Field(type="integer")})

    value, error = module_0.validate_yaml("a: 123", validator=validator)
    assert value == {"a": 123}
    assert error is None

    value, error = module_0.validate_yaml(b"a: 123", validator=validator)
    assert value == {"a": 123}
    assert error is None

    value, error = module_0.validate_yaml("a: abc", validator=validator)
    assert value is None
    assert error is not None
    assert error.messages()[0].text == "Must be a valid number."
    assert error.messages()[0].start_position.line_no == 1
    assert error.messages()[0].start_position.column_no == 4
    assert error.messages()[0].end_position.line_no == 1
    assert error.messages()[0].end_position.column_no == 6

    with pytest.raises(ParseError):
        module_0.validate_yaml("", validator=validator)

    with pytest.raises(ParseError):
        module_0.validate_yaml("a:\n-b\n", validator=validator)

    with pytest.raises(ParseError):
        module_0.validate_yaml("a: b\nc: d\n: e\n", validator=validator)

# Generated at 2026-11-01 21:10:38.566555
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import pytest

    # Test basic mapping tokenization
    token = module_0.tokenize_yaml("{key: value}")
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}
    assert token.start_index == 0
    assert token.end_index == len("{key: value}") - 1

    # Test scalar token inside mapping
    value_token = token.lookup([0])
    assert isinstance(value_token, ScalarToken)
    assert value_token.value == "value"

    # Test key token
    key_token = token.lookup_key([0])
    assert isinstance(key_token, ScalarToken)
    assert key_token.value == "key"

    # Test nested mappings
    content = "person:\n  name: Tom\n  age: 25"
    token = module_0.tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"person": {"name": "Tom", "age": 25}}

    # Test sequences
    content = "- 1\n- 2\n- 3"
    token = module_0.tokenize_yaml(content)
    assert isinstance(token, ListToken)
    assert token.value == [1, 2, 3]
    assert isinstance(token.lookup([0]), ScalarToken)
    assert token.lookup([0]).value == 1

    # Test nested list inside dict
    content = "items:\n  - a\n  - b"
    token = module_0.tokenize_yaml(content)
    assert token.value == {"items": ["a", "b"]}
    assert isinstance(token.lookup(["items"]), ListToken)

    # Test integer scalar
    token = module_0.tokenize_yaml("123")
    assert isinstance(token, ScalarToken)
    assert token.value == 123
    assert isinstance(token.value, int)

    # Test float scalar
    token = module_0.tokenize_yaml("3.14")
    assert isinstance(token, ScalarToken)
    assert token.value == 3.14
    assert isinstance(token.value, float)

    # Test boolean scalar
    token = module_0.tokenize_yaml("true")
    assert isinstance(token, ScalarToken)
    assert token.value is True

    token = module_0.tokenize_yaml("false")
    assert isinstance(token, ScalarToken)
    assert token.value is False

    # Test null scalar
    token = module_0.tokenize_yaml("null")
    assert isinstance(token, ScalarToken)
    assert token.value is None

    # Test string scalar
    token = module_0.tokenize_yaml("hello")
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"

    # Test quoted string scalar
    token = module_0.tokenize_yaml('"quoted string"')
    assert isinstance(token, ScalarToken)
    assert token.value == "quoted string"

    # Test tokens carry content reference
    content = "key: value"
    token = module_0.tokenize_yaml(content)
    assert token._content == content

    # Test bytes content
    token = module_0.tokenize_yaml(b"{key: value}")
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}

    # Test empty content raises ParseError
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("")
    assert exc_info.value.text == "No content."
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        line_no=1, column_no=1, char_index=0
    )

    # Test whitespace-only content raises ParseError
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("   \n  ")
    assert exc_info.value.text == "No content."
    assert exc_info.value.code == "no_content"

    # Test invalid YAML raises ParseError
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("key: [unclosed")
    assert exc_info.value.code == "parse_error"
    assert isinstance(exc_info.value.position, Position)

    # Test invalid YAML with correct error position
    content = "key1: value1\nkey2: -invalid-\nkey3: value3"
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml(content)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no == 2
    assert exc_info.value.position.column_no == 7

# Generated at 2026-11-01 21:12:41.725666
# Unit test for function tokenize_yaml

# Generated at 2026-11-01 21:14:34.981635
# Unit test for function tokenize_yaml

# Generated at 2026-11-01 21:16:18.414168
# Unit test for function tokenize_yaml

# Generated at 2026-11-01 21:17:51.180677
# Unit test for function validate_yaml