

# Generated at 2026-11-02 10:52:47.762079
# Unit test for function evalString
def test_evalString():
    # Plain strings with matching quote styles
    assert module_0.evalString("'hello'") == "hello"
    assert module_0.evalString('"hello"') == "hello"
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""

    # Triple-quoted strings
    assert module_0.evalString("'''triple'''") == "triple"
    assert module_0.evalString('"""triple"""') == "triple"

    # Simple escape sequences
    assert module_0.evalString(r"'\a'") == "\a"
    assert module_0.evalString(r"'\b'") == "\b"
    assert module_0.evalString(r"'\f'") == "\f"
    assert module_0.evalString(r"'\n'") == "\n"
    assert module_0.evalString(r"'\r'") == "\r"
    assert module_0.evalString(r"'\t'") == "\t"
    assert module_0.evalString(r"'\v'") == "\v"
    assert module_0.evalString(r"'\''") == "'"
    assert module_0.evalString("'\\\"'") == '"'
    assert module_0.evalString(r"'\\'") == "\\"

    # Mixed literals and escapes
    assert module_0.evalString(r"'line1\nline2\tend'") == "line1\nline2\tend"

    # Hex escapes
    assert module_0.evalString(r"'\x41'") == "A"
    assert module_0.evalString(r"'\x4a'") == "J"
    assert module_0.evalString(r"'\x00'") == "\x00"

    # Octal escapes (1-3 digits)
    assert module_0.evalString(r"'\101'") == "A"
    assert module_0.evalString(r"'\10'") == "\x08"
    assert module_0.evalString(r"'\0'") == "\x00"
    assert module_0.evalString(r"'\7'") == "\x07"
    assert module_0.evalString(r"'\777'") == chr(511)

    # Round-trip: every character should survive repr() -> module_0.evalString()
    for i in range(256):
        c = chr(i)
        assert module_0.evalString(repr(c)) == c, "failed for chr(%d)" % i

    # Invalid hex escape raises ValueError
    try:
        module_0.evalString(r"'\xzz'")
        raise AssertionError("expected ValueError for invalid hex escape")
    except ValueError:
        pass

    # Invalid octal escape raises ValueError
    try:
        module_0.evalString(r"'\8'")
        raise AssertionError("expected ValueError for invalid octal escape")
    except ValueError:
        pass

    try:
        module_0.evalString(r"'\9'")
        raise AssertionError("expected ValueError for invalid octal escape")
    except ValueError:
        pass

    # Malformed input raises AssertionError
    for bad in ["hello", "'hello\"", '"hello\'', "'hello", "'"]:
        try:
            module_0.evalString(bad)
            raise AssertionError("expected AssertionError for %r" % bad)
        except AssertionError:
            pass

# Generated at 2026-11-02 10:54:31.435766
# Unit test for function escape
def test_escape():
    class FakeMatch:
        def __init__(self, all, tail):
            self._all = all
            self._tail = tail

        def group(self, *args):
            if args == (0, 1):
                return (self._all, self._tail)
            raise AssertionError("unexpected group call: %r" % (args,))

    def make(tail):
        return FakeMatch("\\" + tail, tail)

    # Simple escapes resolve via simple_escapes
    assert module_0.escape(make("n")) == "\n"
    assert module_0.escape(make("t")) == "\t"
    assert module_0.escape(make("r")) == "\r"
    assert module_0.escape(make("a")) == "\a"
    assert module_0.escape(make("b")) == "\b"
    assert module_0.escape(make("f")) == "\f"
    assert module_0.escape(make("v")) == "\v"
    assert module_0.escape(make("'")) == "'"
    assert module_0.escape(make('"')) == '"'
    assert module_0.escape(make("\\")) == "\\"

    # Hex escapes
    assert module_0.escape(make("x41")) == "A"
    assert module_0.escape(make("x4a")) == "J"
    assert module_0.escape(make("x00")) == "\x00"
    assert module_0.escape(make("xff")) == "\xff"
    assert module_0.escape(make("x7f")) == "\x7f"

    # Octal escapes
    assert module_0.escape(make("101")) == "A"
    assert module_0.escape(make("0")) == "\x00"
    assert module_0.escape(make("7")) == "\x07"
    assert module_0.escape(make("10")) == "\x08"
    assert module_0.escape(make("777")) == "\u01ff"  # 0o777 == 511

    # Invalid hex escapes raise ValueError
    for bad in ("x", "x4", "xg", "x1g", "xzz"):
        try:
            module_0.escape(make(bad))
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for '\\%s'" % bad)

    # Invalid octal escapes raise ValueError
    for bad in ("8", "9", "18"):
        try:
            module_0.escape(make(bad))
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for '\\%s'" % bad)

    # Works with real match objects from the pattern used by evalString
    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\101")) == "A"
    assert module_0.escape(pattern.match("\\\\")) == "\\"
    assert module_0.escape(pattern.match('\\"')) == '"'

    print("test_escape passed")


if __name__ == "__main__":
    test_escape()

# Generated at 2026-11-02 10:55:44.264996
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    # module_0.test() checks that evalString(repr(c)) == c for all 256 chars.
    # When everything round-trips correctly, nothing should be printed.
    buf = io.StringIO()
    with redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() printed mismatches: %r" % buf.getvalue()

    # Additionally verify the round-trip property directly
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, "round-trip failed for %r: %r -> %r" % (i, s, e)
# nonce:06d7c995

# Generated at 2026-11-02 10:58:16.666168
# Unit test for function escape
def test_escape():
    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    def run(raw):
        m = pattern.match(raw)
        assert m is not None
        return module_0.escape(m)

    # Simple escapes resolved via simple_escapes
    assert run("\\a") == "\a"
    assert run("\\b") == "\b"
    assert run("\\f") == "\f"
    assert run("\\n") == "\n"
    assert run("\\r") == "\r"
    assert run("\\t") == "\t"
    assert run("\\v") == "\v"
    assert run("\\'") == "'"
    assert run('\\"') == '"'
    assert run("\\\\") == "\\"

    # Hex escapes (exactly two hex digits)
    assert run("\\x41") == "A"
    assert run("\\x7a") == "z"
    assert run("\\x00") == "\x00"
    assert run("\\xff") == "\xff"

    # Octal escapes (one to three octal digits)
    assert run("\\0") == "\x00"
    assert run("\\7") == "\x07"
    assert run("\\101") == "A"
    assert run("\\176") == "~"
    assert run("\\777") == chr(0o777)

    # Invalid hex escapes raise ValueError
    for raw in ("\\x1", "\\xg1", "\\xzz"):
        try:
            run(raw)
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % raw)

    # Invalid octal escape raises ValueError (bypass the pattern with a stub)
    class FakeMatch:
        def __init__(self, groups):
            self._groups = groups

        def group(self, *indices):
            return tuple(self._groups[i] for i in indices)

    try:
        module_0.escape(FakeMatch(("\\9", "9")))
    except ValueError as e:
        assert "invalid octal string escape" in str(e)
    else:
        raise AssertionError("expected ValueError for octal \\9")

    # Round-trip: every character's repr must eval back to itself
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c
# nonce:710a442d

# Generated at 2026-11-02 11:01:02.772348
# Unit test for function escape
def test_escape():
    import re
    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    def esc(s):
        m = pattern.match(s)
        assert m is not None, s
        assert m.group(0) == s, s
        return module_0.escape(m)

    # Simple escapes map directly through simple_escapes.
    for tail, expected in simple_escapes.items():
        assert esc("\\" + tail) == expected

    assert esc("\\n") == "\n"
    assert esc("\\t") == "\t"
    assert esc("\\\\") == "\\"
    assert esc("\\'") == "'"
    assert esc('\\"') == '"'

    # Hex escapes.
    assert esc("\\x41") == "A"
    assert esc("\\xff") == "\xff"
    assert esc("\\xFF") == "\xff"
    assert esc("\\x4") == "\x04"
    assert esc("\\x0a") == "\n"
    assert esc("\\x00") == "\x00"

    # Octal escapes.
    assert esc("\\0") == "\x00"
    assert esc("\\7") == "\x07"
    assert esc("\\77") == "\x3f"
    assert esc("\\777") == "\u01ff"
    assert esc("\\101") == "A"
    assert esc("\\400") == "\u0100"

    # Invalid escapes raise ValueError.
    for bad in ("\\x", "\\xg", "\\xzz", "\\x4g", "\\8", "\\9"):
        try:
            esc(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # Error messages mention the escape kind.
    try:
        esc("\\xg")
    except ValueError as e:
        assert "invalid hex string escape" in str(e)
    else:
        raise AssertionError("expected ValueError for '\\xg'")

    try:
        esc("\\8")
    except ValueError as e:
        assert "invalid octal string escape" in str(e)
    else:
        raise AssertionError("expected ValueError for '\\8'")