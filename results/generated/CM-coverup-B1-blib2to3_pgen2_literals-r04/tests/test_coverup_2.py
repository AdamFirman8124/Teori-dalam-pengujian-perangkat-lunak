# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

import pytest

from blib2to3.pgen2.literals import evalString


def test_single_quoted_plain():
    assert evalString("'abc'") == "abc"


def test_double_quoted_plain():
    assert evalString('"abc"') == "abc"


def test_triple_single_quoted():
    assert evalString("'''abc'''") == "abc"


def test_triple_double_quoted():
    assert evalString('"""abc"""') == "abc"


def test_simple_escapes():
    assert evalString(r"'" "\a\b\f\n\r\t\v" r"'") == "\a\b\f\n\r\t\v"


def test_escaped_quote_and_backslash():
    assert evalString(r"'a\'b\\c\"d'") == "a'b\\c\"d"


def test_hex_escape_two_digits():
    assert evalString(r"'\x41'") == "A"


def test_hex_escape_one_digit_raises():
    with pytest.raises(ValueError, match="invalid hex string escape"):
        evalString(r"'\x4'")


def test_hex_escape_zero_digits_raises():
    with pytest.raises(ValueError, match="invalid hex string escape"):
        evalString(r"'\x'")


def test_octal_escape():
    assert evalString(r"'\101\102'") == "AB"


def test_octal_escape_short():
    assert evalString(r"'\7'") == "\x07"


def test_mixed_escapes():
    assert evalString(r"'" r"A\t\\x41\n\x42\101" r"'") == "A\t\\x41\nBA"


def test_empty_string():
    assert evalString("''") == ""


def test_empty_triple_quoted_string():
    assert evalString("''''''") == ""


def test_missing_quotes_raises():
    with pytest.raises(AssertionError):
        evalString("abc")


def test_mismatched_quotes_raises():
    with pytest.raises(AssertionError):
        evalString("'abc\"")


def test_triple_quoted_missing_closing_raises():
    with pytest.raises(AssertionError):
        evalString("'''abc'")


def test_too_short_triple_quoted_raises():
    with pytest.raises(AssertionError):
        evalString("'''")


def test_single_char_raises():
    with pytest.raises(AssertionError):
        evalString("'")
