# file: project/blib2to3/pgen2/literals.py:25-44
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}

import re

import pytest

from blib2to3.pgen2.literals import escape


def _match(pattern, text):
    m = re.match(pattern, text)
    assert m is not None
    return m


def test_escape_simple_escape():
    # Covers lines 26-30: simple escape lookup hit.
    m = _match(r"\\(.)", "\\n")
    assert escape(m) == "\n"


def test_escape_valid_hex():
    # Covers lines 31-36 and 44: valid hex escape.
    m = _match(r"\\(x[0-9a-fA-F]+)", "\\x41")
    assert escape(m) == "A"


def test_escape_hex_too_short():
    # Covers lines 31-34: hex escape with fewer than 2 digits.
    m = _match(r"\\(x[0-9a-fA-F]*)", "\\x1")
    with pytest.raises(ValueError, match=r"invalid hex string escape \('\\x1'\)"):
        escape(m)


def test_escape_hex_invalid_digits():
    # Covers lines 35-38: hex escape with non-hex characters.
    m = _match(r"\\(x.*)", "\\xzz")
    with pytest.raises(ValueError, match=r"invalid hex string escape \('\\xzz'\)"):
        escape(m)


def test_escape_valid_octal():
    # Covers lines 40-41 and 44: valid octal escape.
    m = _match(r"\\([0-7]+)", "\\101")
    assert escape(m) == "A"


def test_escape_octal_invalid():
    # Covers lines 42-43: invalid octal escape.
    m = _match(r"\\(.+)", "\\9")
    with pytest.raises(ValueError, match=r"invalid octal string escape \('\\9'\)"):
        escape(m)
