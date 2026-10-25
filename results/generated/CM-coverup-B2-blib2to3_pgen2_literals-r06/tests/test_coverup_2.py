# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_eval_string_single_quotes():
    assert evalString("'hello'") == "hello"


def test_eval_string_double_quotes():
    assert evalString('"hello"') == "hello"


def test_eval_string_triple_single_quotes():
    assert evalString("'''hello'''") == "hello"


def test_eval_string_triple_double_quotes():
    assert evalString('"""hello"""') == "hello"


def test_eval_string_escapes():
    assert evalString(r"'" + r"\a\b\f\n\r\t\v\\\'\"" + "'") == "\a\b\f\n\r\t\v\\'\""


def test_eval_string_hex_escape():
    assert evalString(r"'\x41'") == "A"


def test_eval_string_octal_escape():
    assert evalString(r"'\101'") == "A"


def test_eval_string_empty_string():
    assert evalString("''") == ""


def test_eval_string_wrong_quote_raises():
    with pytest.raises(AssertionError):
        evalString("'hello\"")


def test_eval_string_too_short_raises():
    with pytest.raises(AssertionError):
        evalString("'")
