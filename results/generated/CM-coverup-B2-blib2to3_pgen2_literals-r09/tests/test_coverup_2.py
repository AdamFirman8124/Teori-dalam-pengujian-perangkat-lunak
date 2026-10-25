# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_eval_string_with_single_quotes_and_escapes():
    assert evalString("'line\\nnext\\tend'") == "line\nnext\tend"


def test_eval_string_with_double_quotes():
    assert evalString('"plain text"') == "plain text"


def test_eval_string_with_triple_quotes():
    assert evalString("'''first\\nsecond'''") == "first\nsecond"


def test_eval_string_rejects_invalid_opening_quote():
    with pytest.raises(AssertionError):
        evalString("not quoted")


def test_eval_string_rejects_mismatched_closing_quote():
    with pytest.raises(AssertionError):
        evalString("'mismatched\"")


def test_eval_string_rejects_single_triple_quote_delimiter():
    with pytest.raises(AssertionError):
        evalString("'''")
