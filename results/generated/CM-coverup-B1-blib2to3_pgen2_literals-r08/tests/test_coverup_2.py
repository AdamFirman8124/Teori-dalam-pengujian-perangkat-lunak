# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_eval_string_single_quotes():
    assert evalString("'hello'") == "hello"


def test_eval_string_double_quotes():
    assert evalString('"hello"') == "hello"


def test_eval_string_empty_single_quotes():
    assert evalString("''") == ""


def test_eval_string_empty_double_quotes():
    assert evalString('""') == ""


def test_eval_string_triple_single_quotes():
    assert evalString("'''hello'''") == "hello"


def test_eval_string_triple_double_quotes():
    assert evalString('"""hello"""') == "hello"


def test_eval_string_empty_triple_single_quotes():
    assert evalString("''''''") == ""


def test_eval_string_empty_triple_double_quotes():
    assert evalString('""""""') == ""


def test_eval_string_simple_escapes():
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r'"\r"') == "\r"
    assert evalString(r"'\<newline>'".replace("<newline>", "\n")) is not None


def test_eval_string_quote_escapes():
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\"'") == '"'
    assert evalString(r'"\'"') == "'"
    assert evalString(r'"\""') == '"'


def test_eval_string_hex_and_octal_escapes():
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\n\x41\101'") == "\nAA"


def test_eval_string_triple_quote_with_escapes():
    assert evalString(r"'''a\nb'''") == "a\nb"
    assert evalString(r'"""a\nb"""') == "a\nb"


def test_eval_string_invalid_start_raises():
    with pytest.raises(AssertionError):
        evalString("hello")
    with pytest.raises(AssertionError):
        evalString("")
    with pytest.raises(AssertionError):
        evalString("x'hi'")


def test_eval_string_mismatched_end_raises():
    with pytest.raises(AssertionError):
        evalString("'hello\"")
    with pytest.raises(AssertionError):
        evalString("\"hello'")
    with pytest.raises(AssertionError):
        evalString("'''hello\"\"\"")


def test_eval_string_too_short_single_raises():
    with pytest.raises(AssertionError):
        evalString("'")
    with pytest.raises(AssertionError):
        evalString('"')


def test_eval_string_too_short_triple_raises():
    with pytest.raises(AssertionError):
        evalString("'''")
    with pytest.raises(AssertionError):
        evalString('"""')
    with pytest.raises(AssertionError):
        evalString("'''''")
