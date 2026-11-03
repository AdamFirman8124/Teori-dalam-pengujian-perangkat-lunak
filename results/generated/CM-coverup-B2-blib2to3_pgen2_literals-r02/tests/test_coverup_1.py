# file: project/blib2to3/pgen2/literals.py:25-44
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}

"""Tests for blib2to3.pgen2.literals.escape (lines 26-44)."""

import pytest

from blib2to3.pgen2 import literals


class FakeMatch:
    """Minimal re.Match stand-in supporting the group(0, 1) call pattern."""

    def __init__(self, whole, tail):
        self._whole = whole
        self._tail = tail

    def group(self, *indices):
        values = {0: self._whole, 1: self._tail}
        return tuple(values[index] for index in indices)


@pytest.mark.parametrize("tail, expected", sorted(literals.simple_escapes.items()))
def test_escape_simple_escapes(tail, expected):
    # Lines 26-30: group unpacking, assert, dict hit, early return.
    result = literals.escape(FakeMatch("\\" + tail, tail))
    assert result == expected


@pytest.mark.parametrize(
    "whole, tail, expected",
    [
        ("\\x41", "x41", "A"),  # valid hex escape -> lines 31-32, 35-36, 44
        ("\\101", "101", "A"),  # valid octal escape -> lines 39-41, 44
    ],
)
def test_escape_numeric_escapes(whole, tail, expected):
    assert literals.escape(FakeMatch(whole, tail)) == expected


@pytest.mark.parametrize(
    "whole, tail, expected_message, suppressed",
    [
        # fewer than two hex digits -> lines 33-34 (raised directly)
        ("\\x", "x", "invalid hex string escape ('\\x')", False),
        # non-hex digits after 'x' -> lines 37-38 (re-raised "from None")
        ("\\xzz", "xzz", "invalid hex string escape ('\\xzz')", True),
        # tail that is not valid octal -> lines 42-43 (re-raised "from None")
        ("\\9", "9", "invalid octal string escape ('\\9')", True),
    ],
)
def test_escape_invalid_escapes(whole, tail, expected_message, suppressed):
    with pytest.raises(ValueError) as excinfo:
        literals.escape(FakeMatch(whole, tail))
    assert str(excinfo.value) == expected_message
    assert excinfo.value.__suppress_context__ is suppressed


def test_escape_asserts_on_malformed_match():
    # Line 27: the whole-match group must start with a backslash.
    with pytest.raises(AssertionError):
        literals.escape(FakeMatch("n", "n"))


@pytest.mark.parametrize(
    "literal, expected",
    [
        (r"'\n'", "\n"),   # simple escape through the real regex
        (r"'\x41'", "A"),  # valid hex through the real regex
        (r"'\101'", "A"),  # valid octal through the real regex
    ],
)
def test_evalstring_delegates_to_escape(literal, expected):
    assert literals.evalString(literal) == expected


@pytest.mark.parametrize(
    "literal, expected_message",
    [
        (r"'\x'", "invalid hex string escape ('\\x')"),
        (r"'\xzz'", "invalid hex string escape ('\\xzz')"),
    ],
)
def test_evalstring_invalid_hex(literal, expected_message):
    with pytest.raises(ValueError) as excinfo:
        literals.evalString(literal)
    assert str(excinfo.value) == expected_message
