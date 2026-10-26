# file: project/blib2to3/pgen2/literals.py:25-44
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}

import re

import pytest

from blib2to3.pgen2.literals import escape


def _make_escape_match(text: str):
    """Build a Match object whose group(0) is the full escape sequence and
    group(1) is the tail (everything after the leading backslash)."""
    m = re.match(r"\\(.+)", text)
    assert m is not None
    return m


def test_escape_simple_escape():
    # Covers lines 26-30: simple_escapes hit branch.
    m = _make_escape_match("\\n")
    assert escape(m) == "\n"


def test_escape_valid_hex():
    # Covers lines 31-32, 36, 44: hex branch, successful int conversion.
    m = _make_escape_match("\\x41")
    assert escape(m) == "A"


def test_escape_hex_too_short():
    # Covers lines 33-34: hex escape with fewer than 2 hex digits.
    m = _make_escape_match("\\x1")
    with pytest.raises(ValueError, match=r"invalid hex string escape \('\\x1'\)"):
        escape(m)


def test_escape_hex_invalid_digits():
    # Covers lines 37-38: int(hexes, 16) raises ValueError.
    m = _make_escape_match("\\xzz")
    with pytest.raises(ValueError, match=r"invalid hex string escape \('\\xzz'\)"):
        escape(m)


def test_escape_valid_octal():
    # Covers lines 40-41, 44: octal branch, successful int conversion.
    m = _make_escape_match("\\101")
    assert escape(m) == "A"


def test_escape_octal_invalid():
    # Covers lines 42-43: int(tail, 8) raises ValueError.
    m = _make_escape_match("\\9")
    with pytest.raises(ValueError, match=r"invalid octal string escape \('\\9'\)"):
        escape(m)


def test_escape_unknown_letter_falls_into_octal_error():
    # Covers the else branch (line 39) plus the octal ValueError path:
    # tail is neither a simple escape nor starts with 'x'.
    m = _make_escape_match("\\z")
    with pytest.raises(ValueError, match=r"invalid octal string escape \('\\z'\)"):
        escape(m)
