# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_eval_string_with_single_quotes_and_escapes():
    value = evalString(r"'line\nhex\x21octal\141'")
    assert value == "line\nhex!octala"


def test_eval_string_with_double_quotes():
    value = evalString(r'"say \"hello\""')
    assert value == 'say "hello"'


def test_eval_string_with_triple_quotes():
    value = evalString("'''multiline text'''")
    assert value == "multiline text"


def test_eval_string_rejects_invalid_opening_quote():
    with pytest.raises(AssertionError):
        evalString("not quoted")


def test_eval_string_rejects_missing_closing_quote():
    with pytest.raises(AssertionError):
        evalString("'not closed")


def test_eval_string_rejects_too_short_quoted_string():
    with pytest.raises(AssertionError):
        evalString("'")
