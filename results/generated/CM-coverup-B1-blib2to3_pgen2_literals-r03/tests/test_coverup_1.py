# file: project/blib2to3/pgen2/literals.py:25-44
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}

import pytest
from unittest.mock import Mock

from blib2to3.pgen2.literals import escape, evalString, simple_escapes


def make_match(all_, tail):
    """Build a fake Match whose group(0, 1) returns (all_, tail)."""
    m = Mock()
    m.group.return_value = (all_, tail)
    return m


@pytest.mark.parametrize("tail,expected", sorted(simple_escapes.items()))
def test_escape_simple_escapes(tail, expected):
    m = make_match("\\" + tail, tail)
    result = escape(m)
    assert result == expected
    assert isinstance(result, str)
    m.group.assert_called_once_with(0, 1)


@pytest.mark.parametrize(
    "tail,expected",
    [("x41", "A"), ("x00", "\x00"), ("xff", "\xff"), ("x4a", "J")],
)
def test_escape_hex_valid(tail, expected):
    assert escape(make_match("\\" + tail, tail)) == expected


@pytest.mark.parametrize("tail", ["x", "x4"])
def test_escape_hex_too_short(tail):
    with pytest.raises(ValueError) as excinfo:
        escape(make_match("\\" + tail, tail))
    assert str(excinfo.value) == "invalid hex string escape ('\\%s')" % tail
    assert excinfo.value.__cause__ is None


@pytest.mark.parametrize("tail", ["xzz", "x4z", "xgg"])
def test_escape_hex_invalid_digits(tail):
    with pytest.raises(ValueError) as excinfo:
        escape(make_match("\\" + tail, tail))
    assert str(excinfo.value) == "invalid hex string escape ('\\%s')" % tail
    assert excinfo.value.__cause__ is None
    assert excinfo.value.__suppress_context__ is True


@pytest.mark.parametrize(
    "tail,expected",
    [("0", "\x00"), ("7", "\x07"), ("101", "A"), ("377", "\xff")],
)
def test_escape_octal_valid(tail, expected):
    assert escape(make_match("\\" + tail, tail)) == expected


@pytest.mark.parametrize("tail", ["8", "9", "18", "78"])
def test_escape_octal_invalid_digits(tail):
    with pytest.raises(ValueError) as excinfo:
        escape(make_match("\\" + tail, tail))
    assert str(excinfo.value) == "invalid octal string escape ('\\%s')" % tail
    assert excinfo.value.__cause__ is None
    assert excinfo.value.__suppress_context__ is True


def test_escape_asserts_leading_backslash():
    with pytest.raises(AssertionError):
        escape(make_match("n", "n"))


def test_evalstring_uses_escape_for_simple_hex_and_octal():
    assert evalString("'\\n'") == "\n"
    assert evalString('"\\t"') == "\t"
    assert evalString("'\\x41'") == "A"
    assert evalString("'\\101'") == "A"


def test_evalstring_invalid_hex_escape():
    with pytest.raises(ValueError) as excinfo:
        evalString("'\\xzz'")
    assert str(excinfo.value) == "invalid hex string escape ('\\xzz')"
    assert excinfo.value.__cause__ is None
