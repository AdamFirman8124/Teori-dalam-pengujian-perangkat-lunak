# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


@pytest.mark.parametrize(
    ("literal", "expected"),
    [
        ("'plain text'", "plain text"),
        ('"plain text"', "plain text"),
        ("''", ""),
        ('""', ""),
        ("'''triple-quoted'''", "triple-quoted"),
        ('"""triple-quoted"""', "triple-quoted"),
    ],
)
def test_eval_string_valid_literals(literal, expected):
    assert evalString(literal) == expected


def test_eval_string_decodes_escapes():
    body = "\\a\\b\\f\\n\\r\\t\\v\\\\\\x41\\101\\'\\\""
    literal = "'" + body + "'"

    assert evalString(literal) == "\a\b\f\n\r\t\v\\AA'\""


@pytest.mark.parametrize("literal", ["", "unquoted", "`invalid`"])
def test_eval_string_rejects_missing_opening_quote(literal):
    with pytest.raises(AssertionError):
        evalString(literal)


@pytest.mark.parametrize(
    "literal",
    [
        "'unterminated",
        '"unterminated',
        "'mismatched\"",
        '"mismatched\'',
    ],
)
def test_eval_string_rejects_missing_matching_closing_quote(literal):
    with pytest.raises(AssertionError):
        evalString(literal)


@pytest.mark.parametrize("literal", ["'''", '"""'])
def test_eval_string_rejects_incomplete_triple_quoted_literal(literal):
    with pytest.raises(AssertionError):
        evalString(literal)
