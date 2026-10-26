# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_eval_string_single_quoted_with_escapes():
    source = "'line\\n\\x41\\101\\\\\\''"

    assert evalString(source) == "line\nAA\\'"


def test_eval_string_double_quoted():
    assert evalString('"say \\"hello\\""') == 'say "hello"'


def test_eval_string_triple_quoted():
    source = "'''first line\nsecond line'''"

    assert evalString(source) == "first line\nsecond line"


def test_eval_string_rejects_missing_opening_quote():
    with pytest.raises(AssertionError):
        evalString("not quoted")


def test_eval_string_rejects_missing_closing_quote():
    with pytest.raises(AssertionError):
        evalString("'unterminated")


def test_eval_string_rejects_triple_quote_without_content_or_closing_quote():
    with pytest.raises(AssertionError):
        evalString("'''")
