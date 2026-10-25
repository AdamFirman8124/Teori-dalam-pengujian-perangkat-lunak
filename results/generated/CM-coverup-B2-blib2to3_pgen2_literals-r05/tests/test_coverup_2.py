# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_eval_string_single_quoted():
    assert evalString("'hello'") == "hello"


def test_eval_string_double_quoted():
    assert evalString('"hello"') == "hello"


def test_eval_string_triple_single_quoted():
    assert evalString("'''hello'''") == "hello"


def test_eval_string_triple_double_quoted():
    assert evalString('"""hello"""') == "hello"


def test_eval_string_escapes():
    assert evalString(r"'a\tb\nc\\d\'e\"f'") == "a\tb\nc\\d'e\"f"


def test_eval_string_hex_escape():
    assert evalString(r"'\x41\x04'") == "A\x04"


def test_eval_string_invalid_hex_escape():
    with pytest.raises(ValueError):
        evalString(r"'\x4'")


def test_eval_string_octal_escape():
    assert evalString(r"'\101\7'") == "A\x07"


def test_eval_string_bad_quote():
    with pytest.raises(AssertionError):
        evalString("hello")


def test_eval_string_unterminated():
    with pytest.raises(AssertionError):
        evalString("'hello")


def test_eval_string_too_short_triple():
    with pytest.raises(AssertionError):
        evalString("'''")
