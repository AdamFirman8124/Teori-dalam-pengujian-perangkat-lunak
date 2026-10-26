# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_eval_string_single_quotes():
    assert evalString("'abc'") == "abc"


def test_eval_string_double_quotes():
    assert evalString('"abc"') == "abc"


def test_eval_string_triple_single_quotes():
    assert evalString("'''abc'''") == "abc"


def test_eval_string_triple_double_quotes():
    assert evalString('"""abc"""') == "abc"


def test_eval_string_escapes():
    assert evalString(r"'\a\b\f\n\r\t\v'") == "\a\b\f\n\r\t\v"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r"'\'\"'") == "'\""
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"


def test_eval_string_empty():
    assert evalString("''") == ""
    assert evalString('""') == ""


def test_eval_string_rejects_non_string():
    with pytest.raises(AssertionError):
        evalString("abc")


def test_eval_string_rejects_unterminated():
    with pytest.raises(AssertionError):
        evalString("'abc")


def test_eval_string_rejects_too_short():
    with pytest.raises(AssertionError):
        evalString("'''")


def test_eval_string_mismatched_quotes():
    with pytest.raises(AssertionError):
        evalString("'abc\"")
