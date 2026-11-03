# file: project/blib2to3/pgen2/literals.py:25-44
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}

import re
from unittest.mock import Mock

import pytest

from blib2to3.pgen2.literals import escape, simple_escapes


def _match(escape_text):
    """Build a Match object shaped like the one eval_escapes' regex feeds to escape().

    ``escape_text`` must include the leading backslash, e.g. ``"\\x41"``.
    The error paths of ``escape`` (short/invalid hex, invalid octal) are
    unreachable through eval_escapes' regex, hence the direct construction.
    """
    m = re.match(r"\\(.+)", escape_text)
    assert m is not None, "test bug: pattern must match"
    return m


def test_escape_returns_simple_escapes():
    # Lines 26-30: tail is a key of simple_escapes -> mapped value returned.
    for tail, expected in simple_escapes.items():
        assert escape(_match("\\" + tail)) == expected


@pytest.mark.parametrize(
    "escape_text, expected",
    [
        ("\\x41", "A"),
        ("\\x00", "\x00"),
        ("\\xff", "\xff"),
    ],
)
def test_escape_valid_hex(escape_text, expected):
    # Lines 31-32, 35-36 and 44: 'x' branch with a successful int(..., 16).
    assert escape(_match(escape_text)) == expected


@pytest.mark.parametrize(
    "escape_text, expected",
    [
        ("\\101", "A"),
        ("\\0", "\x00"),
        ("\\7", "\x07"),
    ],
)
def test_escape_valid_octal(escape_text, expected):
    # Lines 39-41 (else branch of the hex check) and 44: successful int(..., 8).
    assert escape(_match(escape_text)) == expected


def test_escape_hex_too_short_raises():
    # Lines 33-34: fewer than two hex digits after the 'x'.
    with pytest.raises(ValueError) as excinfo:
        escape(_match("\\x4"))
    assert str(excinfo.value) == "invalid hex string escape ('\\x4')"


def test_escape_hex_invalid_digits_raises():
    # Lines 37-38: int(hexes, 16) raises ValueError and is re-raised.
    with pytest.raises(ValueError) as excinfo:
        escape(_match("\\xzz"))
    assert str(excinfo.value) == "invalid hex string escape ('\\xzz')"


def test_escape_octal_invalid_raises():
    # Lines 42-43: int(tail, 8) raises ValueError and is re-raised.
    with pytest.raises(ValueError) as excinfo:
        escape(_match("\\9"))
    assert str(excinfo.value) == "invalid octal string escape ('\\9')"


def test_escape_asserts_backslash_prefix():
    # Line 27: the assert requires group(0) to start with a backslash.
    bogus = Mock()
    bogus.group.return_value = ("n", "n")  # group(0) lacks the leading backslash
    with pytest.raises(AssertionError):
        escape(bogus)
