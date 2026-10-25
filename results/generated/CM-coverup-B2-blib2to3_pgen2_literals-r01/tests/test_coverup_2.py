# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2 import literals


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("'plain'", "plain"),
        ('"double"', "double"),
        ("'''multi\nline'''", "multi\nline"),
        ('"""multi\nline"""', "multi\nline"),
    ],
)
def test_eval_string_removes_single_and_triple_quotes(source, expected):
    assert literals.evalString(source) == expected


def test_eval_string_decodes_supported_escapes():
    source = r"""'line\nhex:\x41 octal:\101 slash:\\ quote:\' double:\"'"""
    expected = "line\nhex:A octal:A slash:\\ quote:' double:" + '"'

    assert literals.evalString(source) == expected


@pytest.mark.parametrize("source", ["", "unquoted"])
def test_eval_string_rejects_unquoted_text(source):
    with pytest.raises(AssertionError):
        literals.evalString(source)


@pytest.mark.parametrize("source", ["'unterminated", '"unterminated'])
def test_eval_string_rejects_missing_closing_quote(source):
    with pytest.raises(AssertionError):
        literals.evalString(source)


@pytest.mark.parametrize("source", ["'", '"', "'''", '"""'])
def test_eval_string_rejects_literals_too_short_for_their_quotes(source):
    with pytest.raises(AssertionError):
        literals.evalString(source)
