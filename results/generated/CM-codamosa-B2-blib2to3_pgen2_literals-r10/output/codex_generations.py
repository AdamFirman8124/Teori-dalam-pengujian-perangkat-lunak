

# Generated at 2026-11-01 21:41:44.590333
# Unit test for function evalString
def test_evalString():
    # Basic strings
    assert module_0.evalString("'hello'") == 'hello'
    assert module_0.evalString('"hello"') == 'hello'

    # Empty strings
    assert module_0.evalString("''") == ''
    assert module_0.evalString('""') == ''

    # Triple-quoted strings
    assert module_0.evalString("'''hello'''") == 'hello'
    assert module_0.evalString('"""hello"""') == 'hello'
    assert module_0.evalString("''''''") == ''
    assert module_0.evalString('""""""') == ''

    # Escaped quotes
    assert module_0.evalString("'it\\'s'") == "it's"
    assert module_0.evalString('"say \\"hi\\""') == 'say "hi"'
    assert module_0.evalString("'\"both\"'") == '"both"'
    assert module_0.evalString('"\'quotes\'"') == "'quotes'"

    # Simple character escapes
    assert module_0.evalString("'a\\nb'") == 'a\nb'
    assert module_0.evalString("'a\\tb'") == 'a\tb'
    assert module_0.evalString("'a\\rb'") == 'a\rb'
    assert module_0.evalString("'a\\ab'") == 'a\ab'
    assert module_0.evalString("'a\\bb'") == 'a\bb'
    assert module_0.evalString("'a\\fb'") == 'a\fb'
    assert module_0.evalString("'a\\vb'") == 'a\vb'

    # Backslash escape
    assert module_0.evalString("'a\\\\b'") == 'a\\b'

    # Hex escapes
    assert module_0.evalString("'\\x41'") == 'A'
    assert module_0.evalString("'\\x7e'") == '~'
    assert module_0.evalString("'\\x00'") == '\x00'

    # Octal escapes
    assert module_0.evalString("'\\101'") == 'A'
    assert module_0.evalString("'\\7'") == '\a'
    assert module_0.evalString("'\\0'") == '\x00'

    # Mixed escapes
    assert module_0.evalString("'tab\\there\\nnewline'") == 'tab\there\nnewline'

    # Consecutive backslash escapes
    assert module_0.evalString("'\\\\\\\\'") == '\\\\'

    # Literal newline inside triple-quoted string
    assert module_0.evalString("'''a\nb'''") == 'a\nb'

    # Round-trip over all Latin-1 characters (mirrors module self-test)
    for i in range(256):
        c = chr(i)
        assert module_0.evalString(repr(c)) == c

    # Truncated hex escape raises ValueError
    try:
        module_0.evalString("'\\x'")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for truncated hex escape")

    # Malformed hex escape raises ValueError
    try:
        module_0.evalString("'\\xzz'")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for malformed hex escape")

# Generated at 2026-11-01 21:42:15.005758
# Unit test for function test
def test_test():
    # Mirror the round-trip check performed by module_0.test(): every character
    # must survive repr() followed by evalString().
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, (i, c, s, e)

    # Running module_0.test() itself should produce no mismatch reports on stdout.
    import io
    from unittest.mock import patch

    buf = io.StringIO()
    with patch("sys.stdout", buf):
        module_0.test()
    assert buf.getvalue() == "", buf.getvalue()

    # Additional sanity checks for evalString on multi-character literals.
    assert evalString('"hello"') == "hello"
    assert evalString("'it\\'s'") == "it's"
    assert evalString('"\\"quoted\\""') == '"quoted"'
    assert evalString('"""triple\nquoted"""') == "triple\nquoted"
    assert evalString("'''tab\\there'''") == "tab\there"
    assert evalString('"oct\\101bc"') == "oAbc"
    assert evalString('"hex\\x41ex"') == "hAex"

# Generated at 2026-11-01 21:42:57.604272
# Unit test for function escape
def test_escape():
    import re

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    def make_match(literal):
        m = pattern.match(literal)
        assert m is not None, "pattern failed to match %r" % literal
        return m

    def expect_value_error(literal):
        try:
            module_0.escape(make_match(literal))
        except ValueError:
            return True
        return False

    # Simple single-character escapes
    simple_cases = {
        "a": "\a",
        "b": "\b",
        "f": "\f",
        "n": "\n",
        "r": "\r",
        "t": "\t",
        "v": "\v",
        "'": "'",
        '"': '"',
        "\\": "\\",
    }
    for letter, expected in simple_cases.items():
        result = module_0.escape(make_match("\\" + letter))
        assert result == expected, (
            "module_0.escape(%r) returned %r, expected %r" % ("\\" + letter, result, expected)
        )

    # Hexadecimal escapes
    assert module_0.escape(make_match("\\x41")) == "A"
    assert module_0.escape(make_match("\\x61")) == "a"
    assert module_0.escape(make_match("\\x30")) == "0"
    assert module_0.escape(make_match("\\x00")) == "\x00"
    assert module_0.escape(make_match("\\xff")) == "\xff"
    assert module_0.escape(make_match("\\x7e")) == "~"

    # Single-digit hex (regex permits 0..2 hex digits; < 2 raises later,
    # but a 2-digit form must decode correctly)
    assert module_0.escape(make_match("\\x09")) == "\t"

    # Octal escapes
    assert module_0.escape(make_match("\\0")) == "\x00"
    assert module_0.escape(make_match("\\7")) == "\x07"
    assert module_0.escape(make_match("\\12")) == "\n"          # 0o12 == 10
    assert module_0.escape(make_match("\\101")) == "A"          # 0o101 == 65
    assert module_0.escape(make_match("\\777")) == chr(0o777)   # 0o777 == 511
    assert module_0.escape(make_match("\\176")) == "~"          # 0o176 == 126

    # Only the matched portion is consumed; group(0) includes the backslash
    m = pattern.match("\\nrest-of-text")
    assert m is not None
    assert module_0.escape(m) == "\n"

    # Invalid hex escapes raise ValueError
    assert expect_value_error("\\x"), "truncated \\x escape should raise"
    assert expect_value_error("\\xy"), "non-hex digit after \\x should raise"
    assert expect_value_error("\\xzz"), "non-hex digits after \\x should raise"
    assert expect_value_error("\\xg1"), "invalid hex digit should raise"

    # Valid-but-short hex like \\xA handled: len(hexes) < 2 -> error
    assert expect_value_error("\\xa"), "single hex digit should raise"

    # Sanity: results are str instances
    assert isinstance(module_0.escape(make_match("\\n")), str)
    assert isinstance(module_0.escape(make_match("\\x41")), str)
    assert isinstance(module_0.escape(make_match("\\101")), str)

# Generated at 2026-11-01 21:43:22.074890
# Unit test for function test
def test_test():
    # Verify that every possible single character round-trips through
    # repr() followed by evalString(), mirroring the logic in module_0.test()
    # but asserting correctness instead of printing mismatches.
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, (
            "evalString round-trip failed for index %d: "
            "char=%r, repr=%r, result=%r" % (i, c, s, e)
        )

# Generated at 2026-11-01 21:43:38.459098
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() should print nothing when all repr/evalString round-trips succeed
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", repr(buf.getvalue())

    # Verify evalString behavior on concrete inputs
    assert evalString("'a\\nb'") == "a\nb"
    assert evalString('"a\\tb"') == "a\tb"
    assert evalString("'\\x41'") == "A"
    assert evalString('"\\101\\102"') == "AB"
    assert evalString("'''\\r\\v\\f\\a\\b'''") == "\r\v\f\a\b"
    assert evalString("'\\\\\\'\\\"'") == "\\'\""
    assert evalString("'plain'") == "plain"
    assert evalString('""') == ""

# Generated at 2026-11-01 21:44:35.397243
# Unit test for function evalString
def test_evalString():
    # Plain strings
    assert module_0.evalString("'hello'") == "hello"
    assert module_0.evalString('"hello"') == "hello"
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""

    # Triple-quoted strings
    assert module_0.evalString("'''hello'''") == "hello"
    assert module_0.evalString('"""hello"""') == "hello"
    assert module_0.evalString("'''\nfoo\nbar'''") == "\nfoo\nbar"
    assert module_0.evalString('''"it's a \'test\'"''') == "it's a 'test'"

    # Embedded opposite quotes
    assert module_0.evalString("'she said \"hi\"'") == 'she said "hi"'
    assert module_0.evalString('"it\'s here"') == "it's here"

    # Simple escapes
    assert module_0.evalString("'a\\tb'") == "a\tb"
    assert module_0.evalString("'a\\nb'") == "a\nb"
    assert module_0.evalString("'a\\\\b'") == "a\\b"
    assert module_0.evalString("'\\a\\b\\f\\n\\r\\t\\v'") == "\a\b\f\n\r\t\v"
    assert module_0.evalString("'\\''") == "'"
    assert module_0.evalString('"\\""') == '"'

    # Hex escapes
    assert module_0.evalString("'\\x41\\x42\\x43'") == "ABC"
    assert module_0.evalString("'\\xff'") == "\xff"
    assert module_0.evalString("'\\x00'") == "\x00"

    # Octal escapes
    assert module_0.evalString("'\\101\\102\\103'") == "ABC"
    assert module_0.evalString("'\\0'") == "\0"
    assert module_0.evalString("'\\7'") == "\a"
    assert module_0.evalString("'\\377'") == "\xff"
    assert module_0.evalString("'\\777'") == chr(511)

    # Mixed content
    assert module_0.evalString("'A\\tB\\nC'") == "A\tB\nC"

# Generated at 2026-11-01 21:45:01.917895
# Unit test for function escape
def test_escape():
    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    def m(s):
        match = pattern.match(s)
        assert match is not None, s
        return match

    # Simple escapes are looked up in simple_escapes.
    simple = {
        "a": "\a", "b": "\b", "f": "\f", "n": "\n",
        "r": "\r", "t": "\t", "v": "\v",
        "'": "'", '"': '"', "\\": "\\",
    }
    for tail, expected in simple.items():
        assert module_0.escape(m("\\" + tail)) == expected

    # Hex escapes.
    assert module_0.escape(m("\\x41")) == "A"
    assert module_0.escape(m("\\x7a")) == "z"
    assert module_0.escape(m("\\x00")) == "\x00"
    assert module_0.escape(m("\\xFF")) == "\xff"

    # Octal escapes.
    assert module_0.escape(m("\\0")) == "\x00"
    assert module_0.escape(m("\\7")) == "\x07"
    assert module_0.escape(m("\\101")) == "A"
    assert module_0.escape(m("\\777")) == chr(0o777)

    def expect_value_error(s, msg):
        try:
            module_0.escape(m(s))
        except ValueError as e:
            assert msg in str(e), str(e)
        else:
            raise AssertionError("expected ValueError for %r" % s)

    # Invalid hex escapes: too short or non-hex digits.
    expect_value_error("\\x", "invalid hex string escape")
    expect_value_error("\\x4", "invalid hex string escape")
    expect_value_error("\\xzz", "invalid hex string escape")

    # Minimal stand-in for re.Match supporting group(0, 1).
    class FakeMatch:
        def __init__(self, full, tail):
            self._groups = (full, tail)

        def group(self, *indices):
            if len(indices) == 1:
                return self._groups[indices[0]]
            return tuple(self._groups[i] for i in indices)

    # group(0) must start with a backslash (assertion check).
    try:
        module_0.escape(FakeMatch("n", "n"))
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for non-backslash match")

    # Invalid octal module_0.escape(unreachable via the real regex, exercised directly).
    try:
        module_0.escape(FakeMatch("\\8", "8"))
    except ValueError as e:
        assert "invalid octal string escape" in str(e)
    else:
        raise AssertionError("expected ValueError for octal \\8")

# Generated at 2026-11-01 21:46:04.116413
# Unit test for function escape

# Generated at 2026-11-01 21:46:41.451392
# Unit test for function escape
def test_escape():pattern = r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})"

# Generated at 2026-11-01 21:47:20.570279
# Unit test for function escape
def test_escape():
    pattern = r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})"


# Generated at 2026-11-01 21:48:15.761164
# Unit test for function escape

# Generated at 2026-11-01 21:48:40.445019
# Unit test for function escape
def test_escape():pattern = r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})"

# Generated at 2026-11-01 21:49:10.758337
# Unit test for function escape
def test_escape():import re

import pytest

_ESCAPE_RE = r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})"


def _match(text):
    """Build a real match object using the same regex used by evalString."""
    return re.match(_ESCAPE_RE, text)


class _FakeMatch:
    """Minimal stand-in for a Match object with fixed groups."""

    def __init__(self, *groups):
        self._groups = groups

    def group(self, *indices):
        return tuple(self._groups[i] for i in indices)


def test_escape_simple_escapes():
    for key, expected in simple_escapes.items():
        assert module_0.escape(_match("\\" + key)) == expected


def test_escape_hex_two_digits():
    assert module_0.escape(_match("\\x41")) == "A"
    assert module_0.escape(_match("\\x61")) == "a"
    assert module_0.escape(_match("\\x30")) == "0"
    assert module_0.escape(_match("\\x00")) == "\x00"
    assert module_0.escape(_match("\\xFF")) == "\xff"
    assert module_0.escape(_match("\\x7e")) == "~"


def test_escape_octal_escapes():
    assert module_0.escape(_match("\\0")) == "\x00"
    assert module_0.escape(_match("\\7")) == chr(7)
    assert module_0.escape(_match("\\10")) == chr(8)
    assert module_0.escape(_match("\\12")) == "\n"
    assert module_0.escape(_match("\\101")) == "A"
    assert module_0.escape(_match("\\377")) == "\xff"
    assert module_0.escape(_match("\\777")) == chr(0o777)


def test_escape_hex_too_short_raises():
    with pytest.raises(ValueError, match="invalid hex string escape"):
        module_0.escape(_match("\\x"))
    with pytest.raises(ValueError, match="invalid hex string escape"):
        module_0.escape(_match("\\x4"))


def test_escape_hex_invalid_digits_raises():
    with pytest.raises(ValueError, match="invalid hex string escape"):
        module_0.escape(_match("\\xz9"))


def test_escape_octal_invalid_digits_raises():
    # The real regex only matches [0-7], so fake a match with bad octal digits.
    with pytest.raises(ValueError, match="invalid octal string escape"):
        module_0.escape(_FakeMatch("\\9", "9"))
    with pytest.raises(ValueError, match="invalid octal string escape"):
        module_0.escape(_FakeMatch("\\9x", "9x"))


def test_escape_requires_backslash_prefix():
    with pytest.raises(AssertionError):
        module_0.escape(_FakeMatch("n", "n"))


def test_escape_all_octal_byte_values():
    for i in range(256):
        assert module_0.escape(_match("\\%o" % i)) == chr(i)

# Generated at 2026-11-01 21:49:34.366112
# Unit test for function evalString
def test_evalString():
    import pytest

    # Simple strings with no escapes
    assert module_0.evalString("'hello'") == "hello"
    assert module_0.evalString('"hello"') == "hello"
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""

    # Triple-quoted strings
    assert module_0.evalString("'''hello'''") == "hello"
    assert module_0.evalString('"""hello"""') == "hello"
    assert module_0.evalString("''''''") == ""

    # Simple escape sequences
    assert module_0.evalString(r"'\n'") == "\n"
    assert module_0.evalString(r"'\t'") == "\t"
    assert module_0.evalString(r"'\r'") == "\r"
    assert module_0.evalString(r"'\\'") == "\\"
    assert module_0.evalString(r"'\a\b\f\v'") == "\a\b\f\v"
    assert module_0.evalString(r"'\''") == "'"
    assert module_0.evalString(r"'\"'") == '"'
    assert module_0.evalString(r"'a\nb'") == "a\nb"

    # Hex escapes
    assert module_0.evalString(r"'\x41'") == "A"
    assert module_0.evalString(r"'\x4a'") == "j"
    assert module_0.evalString(r"'\x00'") == "\x00"
    assert module_0.evalString(r"'\xff'") == "\xff"

    # Octal escapes
    assert module_0.evalString(r"'\101'") == "A"
    assert module_0.evalString(r"'\0'") == "\x00"
    assert module_0.evalString(r"'\377'") == "\xff"

    # Mixed escapes
    assert module_0.evalString(r"'a\nb\x41\101'") == "a\nbAA"

    # Round-trip: every character 0-255 should survive repr + evalString
    for i in range(256):
        c = chr(i)
        assert module_0.evalString(repr(c)) == c, "failed for char %d" % i

    # Invalid hex escapes raise ValueError
    with pytest.raises(ValueError):
        module_0.evalString(r"'\x'")
    with pytest.raises(ValueError):
        module_0.evalString(r"'\x4'")
    with pytest.raises(ValueError):
        module_0.evalString(r"'\xzz'")

    # Bad quoting raises AssertionError
    with pytest.raises(AssertionError):
        module_0.evalString("hello")          # no quotes
    with pytest.raises(AssertionError):
        module_0.evalString("'hello\"")       # mismatched quotes
    with pytest.raises(AssertionError):
        module_0.evalString("'")              # too short

# Generated at 2026-11-01 21:49:44.085536
# Unit test for function test
def test_test():
    # Run the module's self-test with stdout captured; it only prints
    # when evalString fails to round-trip a character via repr().
    buf = io.StringIO()
    with redirect_stdout(buf):
        module_0.test()
    output = buf.getvalue()
    assert output == "", "evalString/repr round-trip failures reported:\n%s" % output

# Generated at 2026-11-01 21:50:42.809352
# Unit test for function escape

# Generated at 2026-11-01 21:51:02.162698
# Unit test for function escape
def test_escape():import re

    # Simple escapes