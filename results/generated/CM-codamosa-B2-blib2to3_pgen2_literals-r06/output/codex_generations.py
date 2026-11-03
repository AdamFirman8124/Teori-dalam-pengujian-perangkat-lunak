

# Generated at 2026-11-02 19:36:42.141770
# Unit test for function escape
def test_escape():
    import pytest

    pattern = re.compile(r"\\(x.{0,2}|[0-7]{1,3}|.)")

    # Simple escapes map to their control characters / literals
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # Hex escapes
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x61")) == "a"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"
    # At most two hex digits are consumed
    assert module_0.escape(pattern.match("\\x41a")) == "A"

    # Octal escapes
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\101")) == "A"
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # Invalid hex escapes
    with pytest.raises(ValueError):
        module_0.escape(pattern.match("\\x"))      # fewer than two hex digits
    with pytest.raises(ValueError):
        module_0.escape(pattern.match("\\x4"))     # fewer than two hex digits
    with pytest.raises(ValueError):
        module_0.escape(pattern.match("\\xzz"))    # non-hex digits

    # Invalid octal escapes (digit outside 0-7, or non-octal tail)
    broad = re.compile(r"\\(.{1,3})")
    with pytest.raises(ValueError):
        module_0.escape(broad.match("\\8"))
    with pytest.raises(ValueError):
        module_0.escape(broad.match("\\q"))

# Generated at 2026-11-02 19:38:10.270694
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    # module_0.test() prints only when a round-trip mismatch is found;
    # for all 256 characters there should be no output and no exception.
    buf = io.StringIO()
    with redirect_stdout(buf):
        result = module_0.test()
    assert result is None
    assert buf.getvalue() == "", "unexpected mismatch output: %r" % buf.getvalue()

# Generated at 2026-11-02 19:39:39.619990
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    # module_0.test() prints a line only when evalString(repr(c)) != c for some
    # character in range(256). A correct implementation prints nothing.
    buf = io.StringIO()
    with redirect_stdout(buf):
        module_0.test()

    output = buf.getvalue()
    assert output == "", (
        "module_0.test() reported mismatching round-trips:\n%s" % output
    )


def test_test_returns_none():
    # module_0.test() should complete without raising and return None
    result = module_0.test()
    assert result is None


def test_test_covers_all_256_chars():
    # Independently verify the invariant that module_0.test() checks:
    # evalString(repr(c)) == c for every character in range(256)
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, "mismatch for index %d: repr=%r got=%r" % (i, s, e)


def test_test_specific_escapes():
    # Spot-check the escape handling exercised by module_0.test()
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\\'") == "\\"
    assert evalString('"""a\nb"""') == "a\nb"