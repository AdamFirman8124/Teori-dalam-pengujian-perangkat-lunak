# file: project/typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}

import types
import pytest
import yaml
import typesystem.tokenize.tokenize_yaml as yaml_mod
from typesystem.base import ParseError
from typesystem.tokenize.tokenize_yaml import tokenize_yaml
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def _msg(exc_info):
    return exc_info.value.messages()[0]


def test_assert_requires_pyyaml(monkeypatch):
    monkeypatch.setattr(yaml_mod, "yaml", None)
    with pytest.raises(AssertionError):
        tokenize_yaml("a: 1")


def test_empty_string_raises_no_content():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("")
    msg = _msg(exc_info)
    assert msg.code == "no_content"
    assert msg.text == "No content."
    assert msg.start_position.line_no == 1
    assert msg.start_position.column_no == 1
    assert msg.start_position.char_index == 0
    assert msg.end_position.line_no == 1


def test_whitespace_only_raises_no_content():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("   \n  \t  \n")
    msg = _msg(exc_info)
    assert msg.code == "no_content"
    assert msg.text == "No content."


def test_empty_bytes_raises_no_content():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(b"")
    assert _msg(exc_info).code == "no_content"
    with pytest.raises(ParseError) as exc_info2:
        tokenize_yaml(b"   \n  ")
    assert _msg(exc_info2).code == "no_content"


def test_bytes_input_is_decoded():
    token = tokenize_yaml(b"a: 1")
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1}


def test_bytes_with_invalid_utf8_ignored():
    token = tokenize_yaml(b"\xff\xfea: 1")
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1}


def test_mapping_token():
    content = "a: 1\nb: 2"
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1, "b": 2}
    assert token.start.char_index >= 0
    assert token.end.char_index >= token.start.char_index


def test_sequence_token():
    content = "- 1\n- 2\n- 3"
    token = tokenize_yaml(content)
    assert isinstance(token, ListToken)
    assert token.value == [1, 2, 3]
    assert token.start.char_index >= 0
    assert token.end.char_index >= token.start.char_index


def test_plain_scalar_str_token():
    token = tokenize_yaml("hello")
    assert isinstance(token, ScalarToken)
    assert token.value == "hello"
    assert isinstance(token.value, str)


def test_int_token():
    token = tokenize_yaml("42")
    assert isinstance(token, ScalarToken)
    assert token.value == 42
    assert isinstance(token.value, int)


def test_float_token():
    token = tokenize_yaml("3.14")
    assert isinstance(token, ScalarToken)
    assert token.value == 3.14
    assert isinstance(token.value, float)


def test_bool_tokens():
    t_true = tokenize_yaml("true")
    assert isinstance(t_true, ScalarToken)
    assert t_true.value is True
    t_false = tokenize_yaml("false")
    assert isinstance(t_false, ScalarToken)
    assert t_false.value is False


def test_null_tokens():
    t_null = tokenize_yaml("null")
    assert isinstance(t_null, ScalarToken)
    assert t_null.value is None
    t_tilde = tokenize_yaml("~")
    assert isinstance(t_tilde, ScalarToken)
    assert t_tilde.value is None


def test_nested_mixed_covers_all_constructors():
    content = (
        "str_key: hello\n"
        "int_key: 123\n"
        "float_key: 1.5\n"
        "bool_key: true\n"
        "null_key: null\n"
        "list_key:\n"
        "  - 1\n"
        "  - hello\n"
        "  - 2.5\n"
        "  - false\n"
        "  - null\n"
    )
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {
        "str_key": "hello",
        "int_key": 123,
        "float_key": 1.5,
        "bool_key": True,
        "null_key": None,
        "list_key": [1, "hello", 2.5, False, None],
    }


def test_scanner_error_real_parse_error():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("\t- tab not allowed")
    msg = _msg(exc_info)
    assert msg.code == "parse_error"
    assert msg.text.endswith(".")
    assert msg.start_position.char_index >= 0


def test_parser_error_real_parse_error():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("[1, 2")
    msg = _msg(exc_info)
    assert msg.code == "parse_error"
    assert msg.text.endswith(".")
    assert msg.start_position.char_index >= 0


def test_mocked_scanner_error_branch(monkeypatch):
    def _raise_scanner(*args, **kwargs):
        raise yaml.scanner.ScannerError(
            None, None, "mock scanner problem", types.SimpleNamespace(index=1)
        )

    monkeypatch.setattr(yaml, "load", _raise_scanner)
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("a: 1")
    msg = _msg(exc_info)
    assert msg.code == "parse_error"
    assert msg.text == "mock scanner problem."
    assert msg.start_position.char_index == 1


def test_mocked_parser_error_branch(monkeypatch):
    def _raise_parser(*args, **kwargs):
        raise yaml.parser.ParserError(
            None, None, "mock parser problem", types.SimpleNamespace(index=2)
        )

    monkeypatch.setattr(yaml, "load", _raise_parser)
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("a: 1")
    msg = _msg(exc_info)
    assert msg.code == "parse_error"
    assert msg.text == "mock parser problem."
    assert msg.start_position.char_index == 2
