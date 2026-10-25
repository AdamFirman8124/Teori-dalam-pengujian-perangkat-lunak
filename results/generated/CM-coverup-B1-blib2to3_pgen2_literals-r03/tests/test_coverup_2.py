# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_eval_string_single_quoted():
    assert evalString("'abc'") == "abc"
    assert evalString("''") == ""


def test_eval_string_double_quoted():
    assert evalString('"abc"') == "abc"
    assert evalString('""') == ""


def test_eval_string_triple_quoted():
    assert evalString("'''abc'''") == "abc"
    assert evalString('"""abc"""') == "abc"
    assert evalString("'''a'b'''") == "a'b"
    assert evalString('"""a"b"""') == 'a"b'


def test_eval_string_simple_escapes():
    assert evalString(r"'a\nb\tc\\d\'e\"f'") == "a\nb\tc\\d'e\"f"
    assert evalString(r"'\a\b\f\n\r\t\v'") == "\a\b\f\n\r\t\v"


def test_eval_string_hex_and_octal_escapes():
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\0'") == "\0"


def test_eval_string_invalid_hex_escape():
    with pytest.raises(ValueError):
        evalString(r"'\x4'")
    with pytest.raises(ValueError):
        evalString(r"'\xZZ'")


def test_eval_string_requires_quotes():
    with pytest.raises(AssertionError):
        evalString("abc")


def test_eval_string_requires_matching_quote():
    with pytest.raises(AssertionError):
        evalString("'abc\"")
    with pytest.raises(AssertionError):
        evalString("'''abc'")


def test_eval_string_requires_minimum_length():
    with pytest.raises(AssertionError):
        evalString("'")
    with pytest.raises(AssertionError):
        evalString('"')
