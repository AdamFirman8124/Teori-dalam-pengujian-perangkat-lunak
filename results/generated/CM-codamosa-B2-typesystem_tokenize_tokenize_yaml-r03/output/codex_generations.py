

# Generated at 2026-11-02 16:35:03.230862
# Unit test for function tokenize_yaml
def test_tokenize_yaml():import pytest

from typesystem.base import ParseError, Position
from typesystem.tokenize.tokenize_yaml import tokenize_yaml


def test_tokenize_yaml_mapping():
    token = module_0.tokenize_yaml("key: value")
    assert token.start_index == 0
    assert token.end_index == 9
    assert token.value == {"key": "value"}


def test_tokenize_yaml_nested_mapping():
    content = "nested:\n  key: value\n"
    token = module_0.tokenize_yaml(content)
    assert token.value == {"nested": {"key": "value"}}
    nested_token = token.value["nested"]
    assert nested_token.start_index == content.index("key")
    assert nested_token.end_index == content.index("value") + len("value") - 1


def test_tokenize_yaml_sequence():
    token = module_0.tokenize_yaml("- 1\n- 2\n- 3\n")
    assert token.value == [1, 2, 3]
    assert token.start_index == 0
    assert token.end_index == 11


def test_tokenize_yaml_scalar_int():
    token = module_0.tokenize_yaml("123")
    assert token.value == 123
    assert token.start_index == 0
    assert token.end_index == 2


def test_tokenize_yaml_scalar_float():
    token = module_0.tokenize_yaml("1.5")
    assert token.value == 1.5
    assert token.start_index == 0
    assert token.end_index == 2


def test_tokenize_yaml_scalar_bool():
    token = module_0.tokenize_yaml("true")
    assert token.value is True
    assert token.start_index == 0
    assert token.end_index == 3


def test_tokenize_yaml_scalar_null():
    token = module_0.tokenize_yaml("null")
    assert token.value is None
    assert token.start_index == 0
    assert token.end_index == 3


def test_tokenize_yaml_scalar_string():
    token = module_0.tokenize_yaml("abc")
    assert token.value == "abc"
    assert token.start_index == 0
    assert token.end_index == 2


def test_tokenize_yaml_bytes_content():
    token = module_0.tokenize_yaml(b"key: value")
    assert token.value == {"key": "value"}


def test_tokenize_yaml_empty_string():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("")
    assert exc_info.value.text == "No content."
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position == Position(
        line_no=1, column_no=1, char_index=0
    )


def test_tokenize_yaml_whitespace_only():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("   \n  ")
    assert exc_info.value.code == "no_content"


def test_tokenize_yaml_parse_error():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("key: value\n  invalid: indent")
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.text.endswith(".")
    assert exc_info.value.position.line_no == 2
    assert exc_info.value.position.char_index == 13

# Generated at 2026-11-02 16:36:15.869543
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = module_0.tokenize_yaml("a: 1")
    assert token.start_index == 0
    assert token.end_index == 4
    assert token.value == {"a": 1}
    assert token.get_value() == {"a": 1}


def test_tokenize_yaml_nested():
    content = """
    a:
      b: [1, 2, 3]
    """
    token = module_0.tokenize_yaml(content)
    assert token.value == {"a": {"b": [1, 2, 3]}}
    dict_token = token.lookup(["a"])
    assert dict_token.get_value() == {"b": [1, 2, 3]}
    list_token = dict_token.lookup(["b"])
    assert list_token.get_value() == [1, 2, 3]
    scalar_token = list_token.lookup([0])
    assert scalar_token.get_value() == 1


def test_tokenize_yaml_scalar_types():
    content = "int: 1\nfloat: 1.5\nbool: true\nnull: null\nstring: abc"
    token = module_0.tokenize_yaml(content)
    assert token.get_value() == {
        "int": 1,
        "float": 1.5,
        "bool": True,
        "null": None,
        "string": "abc",
    }
    assert isinstance(token.lookup(["int"]).get_value(), int)
    assert isinstance(token.lookup(["float"]).get_value(), float)
    assert isinstance(token.lookup(["bool"]).get_value(), bool)
    assert token.lookup(["null"]).get_value() is None
    assert isinstance(token.lookup(["string"]).get_value(), str)


def test_tokenize_yaml_bytes():
    token = module_0.tokenize_yaml(b"a: 1")
    assert token.get_value() == {"a": 1}


def test_tokenize_yaml_empty_content():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("")
    assert exc_info.value.text == "No content."
    assert exc_info.value.code == "no_content"
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1


def test_tokenize_yaml_whitespace_only():
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml("   \n  ")
    assert exc_info.value.code == "no_content"


def test_tokenize_yaml_parse_error():
    content = "a: 1\n b: 2"
    with pytest.raises(ParseError) as exc_info:
        module_0.tokenize_yaml(content)
    assert exc_info.value.code == "parse_error"
    assert exc_info.value.position.line_no == 2
    assert exc_info.value.position.char_index == 5

# Generated at 2026-11-02 16:40:01.674917
# Unit test for function validate_yaml

# Generated at 2026-11-02 16:43:02.559075
# Unit test for function validate_yaml