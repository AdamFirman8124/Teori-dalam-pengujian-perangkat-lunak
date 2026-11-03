# file: project/blib2to3/pgen2/literals.py:47-55
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55], "branches": [[50, 51], [50, 52]]}

"""Tests for blib2to3.pgen2.literals.evalString (previously uncovered lines 48-55).

evalString is a pure function: it only reads its argument and the module-level
constant `simple_escapes`, and never mutates any state.  Therefore no
monkeypatching or teardown is required to avoid state pollution between tests.
"""

import pytest

from blib2to3.pgen2.literals import evalString


# ---------------------------------------------------------------------------
# Line 48 (both sides of the `or`), line 49, line 50 (False branch),
# lines 52-54, and line 55 (regex with no matches).
# ---------------------------------------------------------------------------

def test_single_quoted_plain_string():
    assert evalString("'hello'") == "hello"


def test_double_quoted_plain_string():
    # Exercises the second operand of the `or` on line 48.
    assert evalString(r'"hello"') == "hello"


def test_single_quoted_string_containing_double_quote():
    # Line 55 regex finds nothing to substitute.
    assert evalString("'\"'") == '"'


# ---------------------------------------------------------------------------
# Lines 50-51: triple-quote detection (True branch).
# ---------------------------------------------------------------------------

def test_triple_single_quoted_string():
    assert evalString("'''hello'''") == "hello"


def test_triple_double_quoted_string():
    assert evalString('"""hello"""') == "hello"


def test_empty_triple_double_quoted_string():
    # Boundary case for the line-53 assertion: len(s) == 2 * len(q).
    assert evalString('""""""') == ""


def test_empty_single_quoted_string():
    assert evalString("''") == ""


def test_triple_double_quoted_string_with_escape():
    assert evalString(r'"""a\nb"""') == "a\nb"


# ---------------------------------------------------------------------------
# Assertion-failure branches of lines 48, 52 and 53.
# ---------------------------------------------------------------------------

def test_missing_quotes_raises_assertion_error():
    # Line 48: neither quote character at the start; message is repr(s[:1]).
    with pytest.raises(AssertionError, match="'h'"):
        evalString("hello")


def test_unterminated_string_raises_assertion_error():
    # Line 52: string does not end with its opening quote.
    with pytest.raises(AssertionError, match="'o'"):
        evalString("'hello")


def test_too_short_triple_quoted_string_raises_assertion_error():
    # Line 53: "'''" is detected as triple-quoted but len(s) == 3 < 6.
    with pytest.raises(AssertionError):
        evalString("'''")


# ---------------------------------------------------------------------------
# Line 55: escape-sequence substitution (each match invokes `escape`).
# ---------------------------------------------------------------------------

def test_simple_escapes():
    assert evalString("'\\a\\b\\f\\n\\r\\t\\v'") == "\a\b\f\n\r\t\v"


def test_quote_and_backslash_escapes():
    assert evalString("'\\'x\\\"y\\\\z'") == "'x\"y\\z"


def test_lone_escaped_quote():
    assert evalString("'\\''") == "'"


def test_hex_escape():
    assert evalString(r'"\x41"') == "A"


def test_hex_escape_consumes_at_most_two_digits():
    # `x.{0,2}` is greedy but bounded; the trailing digit stays literal.
    assert evalString(r'"\x411"') == "A1"


def test_octal_escapes():
    assert evalString(r'"\101\1"') == "A\x01"


def test_mixed_escapes():
    assert evalString(r'"\x41\n\102\t"') == "A\nB\t"


def test_short_hex_escape_raises_value_error():
    with pytest.raises(ValueError, match="invalid hex string escape"):
        evalString(r'"\x4"')


def test_non_hex_digits_raise_value_error():
    with pytest.raises(ValueError, match="invalid hex string escape"):
        evalString(r'"\xzz"')
