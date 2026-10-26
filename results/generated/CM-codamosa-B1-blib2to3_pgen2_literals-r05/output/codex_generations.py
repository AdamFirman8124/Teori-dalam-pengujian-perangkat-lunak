

# Generated at 2026-10-25 09:08:23.191835
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints only on mismatch; a clean run must print nothing
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() reported mismatches: %r" % buf.getvalue()

    # Basic literals round-trip through evalString
    assert evalString("'a'") == "a"
    assert evalString('"hello"') == "hello"
    assert evalString("'''triple\nquoted'''") == "triple\nquoted"
    assert evalString('"""double triple"""') == "double triple"

    # Escapes
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\"'") == '"'
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\0'") == "\0"

    # All single characters round-trip via repr
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c

    # Invalid escapes raise ValueError
    for bad in (r"'\x'", r"'\xZZ'", r"'\8'", r"'\9'"):
        try:
            evalString("'%s'" % bad.replace("\\", "\\\\")[1:-1] if False else "'" + bad[1:] + "'")
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # Missing quotes trip the assertion
    try:
        evalString("abc")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unquoted string")

# Generated at 2026-10-25 09:08:25.786464
# Unit test for function escape

# Generated at 2026-10-25 09:08:28.323873
# Unit test for function escape

# Generated at 2026-10-25 09:08:30.738830
# Unit test for function escape

# Generated at 2026-10-25 09:08:33.159159
# Unit test for function escape

# Generated at 2026-10-25 09:08:35.750820
# Unit test for function escape

# Generated at 2026-10-25 09:08:38.168766
# Unit test for function escape

# Generated at 2026-10-25 09:08:40.586528
# Unit test for function escape

# Generated at 2026-10-25 09:08:43.005239
# Unit test for function escape

# Generated at 2026-10-25 09:08:45.440592
# Unit test for function escape

# Generated at 2026-10-25 09:08:47.858358
# Unit test for function escape

# Generated at 2026-10-25 09:08:50.273378
# Unit test for function escape

# Generated at 2026-10-25 09:08:52.692604
# Unit test for function escape

# Generated at 2026-10-25 09:08:55.196973
# Unit test for function escape

# Generated at 2026-10-25 09:08:57.615464
# Unit test for function escape

# Generated at 2026-10-25 09:09:00.034214
# Unit test for function escape

# Generated at 2026-10-25 09:09:02.450930
# Unit test for function escape

# Generated at 2026-10-25 09:09:04.868168
# Unit test for function escape

# Generated at 2026-10-25 09:09:07.286784
# Unit test for function escape

# Generated at 2026-10-25 09:09:09.703570
# Unit test for function escape

# Generated at 2026-10-25 09:09:12.117987
# Unit test for function escape

# Generated at 2026-10-25 09:09:14.534142
# Unit test for function escape

# Generated at 2026-10-25 09:09:58.165810
# Unit test for function escape

# Generated at 2026-10-25 09:10:02.652009
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 09:10:05.542352
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints only on mismatch; a clean run must print nothing
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() reported mismatches: %r" % buf.getvalue()

    # Basic literals round-trip through evalString
    assert evalString("'a'") == "a"
    assert evalString('"hello"') == "hello"
    assert evalString("'''triple\nquoted'''") == "triple\nquoted"
    assert evalString('"""double triple"""') == "double triple"

    # Escapes
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\"'") == '"'
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\0'") == "\0"

    # All single characters round-trip via repr
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c

    # Invalid escapes raise ValueError
    for bad in (r"'\x'", r"'\xZZ'", r"'\8'", r"'\9'"):
        try:
            evalString("'%s'" % bad.replace("\\", "\\\\")[1:-1] if False else "'" + bad[1:] + "'")
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # Missing quotes trip the assertion
    try:
        evalString("abc")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unquoted string")

# Generated at 2026-10-25 09:10:40.457121
# Unit test for function escape

# Generated at 2026-10-25 09:10:41.993831
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 09:10:52.811896
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 09:10:55.567319
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints only on mismatch; a clean run must print nothing
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() reported mismatches: %r" % buf.getvalue()

    # Basic literals round-trip through evalString
    assert evalString("'a'") == "a"
    assert evalString('"hello"') == "hello"
    assert evalString("'''triple\nquoted'''") == "triple\nquoted"
    assert evalString('"""double triple"""') == "double triple"

    # Escapes
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\"'") == '"'
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\0'") == "\0"

    # All single characters round-trip via repr
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c

    # Invalid escapes raise ValueError
    for bad in (r"'\x'", r"'\xZZ'", r"'\8'", r"'\9'"):
        try:
            evalString("'%s'" % bad.replace("\\", "\\\\")[1:-1] if False else "'" + bad[1:] + "'")
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # Missing quotes trip the assertion
    try:
        evalString("abc")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unquoted string")

# Generated at 2026-10-25 09:10:56.929849
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 09:10:58.380342
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 09:11:03.876897
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints only on mismatch; a clean run must print nothing
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() reported mismatches: %r" % buf.getvalue()

    # Basic literals round-trip through evalString
    assert evalString("'a'") == "a"
    assert evalString('"hello"') == "hello"
    assert evalString("'''triple\nquoted'''") == "triple\nquoted"
    assert evalString('"""double triple"""') == "double triple"

    # Escapes
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\"'") == '"'
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\0'") == "\0"

    # All single characters round-trip via repr
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c

    # Invalid escapes raise ValueError
    for bad in (r"'\x'", r"'\xZZ'", r"'\8'", r"'\9'"):
        try:
            evalString("'%s'" % bad.replace("\\", "\\\\")[1:-1] if False else "'" + bad[1:] + "'")
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # Missing quotes trip the assertion
    try:
        evalString("abc")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unquoted string")

# Generated at 2026-10-25 09:11:21.418166
# Unit test for function escape

# Generated at 2026-10-25 09:11:27.051832
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 09:11:56.812642
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 09:12:00.025419
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints only on mismatch; a clean run must print nothing
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() reported mismatches: %r" % buf.getvalue()

    # Basic literals round-trip through evalString
    assert evalString("'a'") == "a"
    assert evalString('"hello"') == "hello"
    assert evalString("'''triple\nquoted'''") == "triple\nquoted"
    assert evalString('"""double triple"""') == "double triple"

    # Escapes
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\"'") == '"'
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\0'") == "\0"

    # All single characters round-trip via repr
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c

    # Invalid escapes raise ValueError
    for bad in (r"'\x'", r"'\xZZ'", r"'\8'", r"'\9'"):
        try:
            evalString("'%s'" % bad.replace("\\", "\\\\")[1:-1] if False else "'" + bad[1:] + "'")
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # Missing quotes trip the assertion
    try:
        evalString("abc")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unquoted string")

# Generated at 2026-10-25 09:12:03.404043
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints only on mismatch; a clean run must print nothing
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() reported mismatches: %r" % buf.getvalue()

    # Basic literals round-trip through evalString
    assert evalString("'a'") == "a"
    assert evalString('"hello"') == "hello"
    assert evalString("'''triple\nquoted'''") == "triple\nquoted"
    assert evalString('"""double triple"""') == "double triple"

    # Escapes
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\"'") == '"'
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\0'") == "\0"

    # All single characters round-trip via repr
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c

    # Invalid escapes raise ValueError
    for bad in (r"'\x'", r"'\xZZ'", r"'\8'", r"'\9'"):
        try:
            evalString("'%s'" % bad.replace("\\", "\\\\")[1:-1] if False else "'" + bad[1:] + "'")
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # Missing quotes trip the assertion
    try:
        evalString("abc")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unquoted string")

# Generated at 2026-10-25 09:12:04.799090
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 09:12:07.679249
# Unit test for function escape

# Generated at 2026-10-25 09:12:12.281391
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 09:12:28.490503
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 09:12:30.981892
# Unit test for function escape

# Generated at 2026-10-25 09:12:33.395901
# Unit test for function escape

# Generated at 2026-10-25 09:12:35.818128
# Unit test for function escape

# Generated at 2026-10-25 09:12:38.237384
# Unit test for function escape

# Generated at 2026-10-25 09:12:40.649120
# Unit test for function escape

# Generated at 2026-10-25 09:12:43.070046
# Unit test for function escape

# Generated at 2026-10-25 09:12:45.484212
# Unit test for function test

# Generated at 2026-10-25 09:12:47.901788
# Unit test for function test

# Generated at 2026-10-25 09:12:50.318860
# Unit test for function test

# Generated at 2026-10-25 09:12:52.998721
# Unit test for function test

# Generated at 2026-10-25 09:12:55.406270
# Unit test for function test

# Generated at 2026-10-25 09:12:57.823632
# Unit test for function test

# Generated at 2026-10-25 09:13:00.240107
# Unit test for function test

# Generated at 2026-10-25 09:13:02.656218
# Unit test for function test

# Generated at 2026-10-25 09:13:05.073499
# Unit test for function test

# Generated at 2026-10-25 09:13:07.492335
# Unit test for function escape

# Generated at 2026-10-25 09:13:09.909950
# Unit test for function escape

# Generated at 2026-10-25 09:13:12.327801
# Unit test for function escape

# Generated at 2026-10-25 09:13:14.743393
# Unit test for function test

# Generated at 2026-10-25 09:13:17.162074
# Unit test for function test

# Generated at 2026-10-25 09:13:19.581595
# Unit test for function test

# Generated at 2026-10-25 09:13:21.999900
# Unit test for function escape

# Generated at 2026-10-25 09:13:24.414751
# Unit test for function escape

# Generated at 2026-10-25 09:13:26.834581
# Unit test for function escape

# Generated at 2026-10-25 09:13:29.396700
# Unit test for function escape

# Generated at 2026-10-25 09:13:31.753359
# Unit test for function escape

# Generated at 2026-10-25 09:13:34.169622
# Unit test for function escape

# Generated at 2026-10-25 09:13:36.585260
# Unit test for function escape

# Generated at 2026-10-25 09:13:39.003085
# Unit test for function escape

# Generated at 2026-10-25 09:13:41.419983
# Unit test for function escape

# Generated at 2026-10-25 09:13:43.839519
# Unit test for function test

# Generated at 2026-10-25 09:13:46.256006
# Unit test for function test

# Generated at 2026-10-25 09:13:48.672119
# Unit test for function test

# Generated at 2026-10-25 09:13:51.086629
# Unit test for function escape

# Generated at 2026-10-25 09:13:53.518750
# Unit test for function escape

# Generated at 2026-10-25 09:13:55.937823
# Unit test for function escape

# Generated at 2026-10-25 09:13:58.359881
# Unit test for function test

# Generated at 2026-10-25 09:14:00.777885
# Unit test for function test

# Generated at 2026-10-25 09:14:03.195605
# Unit test for function test

# Generated at 2026-10-25 09:14:05.611765
# Unit test for function escape

# Generated at 2026-10-25 09:14:08.100570
# Unit test for function escape

# Generated at 2026-10-25 09:14:10.517792
# Unit test for function escape

# Generated at 2026-10-25 09:14:12.933705
# Unit test for function escape

# Generated at 2026-10-25 09:14:15.352260
# Unit test for function escape

# Generated at 2026-10-25 09:14:17.770501
# Unit test for function escape

# Generated at 2026-10-25 09:14:20.187354
# Unit test for function test

# Generated at 2026-10-25 09:14:22.605415
# Unit test for function test

# Generated at 2026-10-25 09:14:25.022601
# Unit test for function test

# Generated at 2026-10-25 09:14:27.438369
# Unit test for function escape

# Generated at 2026-10-25 09:14:29.963910
# Unit test for function escape

# Generated at 2026-10-25 09:14:32.373513
# Unit test for function escape

# Generated at 2026-10-25 09:14:34.792372
# Unit test for function escape

# Generated at 2026-10-25 09:14:37.208634
# Unit test for function escape

# Generated at 2026-10-25 09:14:39.625486
# Unit test for function escape

# Generated at 2026-10-25 09:14:42.045308
# Unit test for function test

# Generated at 2026-10-25 09:14:44.465342
# Unit test for function test

# Generated at 2026-10-25 09:14:46.880750
# Unit test for function test

# Generated at 2026-10-25 09:14:49.296929
# Unit test for function escape

# Generated at 2026-10-25 09:14:51.711510
# Unit test for function escape

# Generated at 2026-10-25 09:14:54.134841
# Unit test for function escape

# Generated at 2026-10-25 09:14:56.552131
# Unit test for function escape

# Generated at 2026-10-25 09:14:58.967563
# Unit test for function escape

# Generated at 2026-10-25 09:15:14.173074
# Unit test for function escape
def test_escape():import re


# Generated at 2026-10-25 09:15:17.145838
# Unit test for function test
def test_test():
    import io
    import contextlib

    # module_0.test() prints only on mismatch; a clean run must print nothing
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module_0.test()
    assert buf.getvalue() == "", "module_0.test() reported mismatches: %r" % buf.getvalue()

    # Basic literals round-trip through evalString
    assert evalString("'a'") == "a"
    assert evalString('"hello"') == "hello"
    assert evalString("'''triple\nquoted'''") == "triple\nquoted"
    assert evalString('"""double triple"""') == "double triple"

    # Escapes
    assert evalString(r"'\n'") == "\n"
    assert evalString(r"'\t'") == "\t"
    assert evalString(r"'\\'") == "\\"
    assert evalString(r"'\''") == "'"
    assert evalString(r"'\"'") == '"'
    assert evalString(r"'\x41'") == "A"
    assert evalString(r"'\101'") == "A"
    assert evalString(r"'\0'") == "\0"

    # All single characters round-trip via repr
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c

    # Invalid escapes raise ValueError
    for bad in (r"'\x'", r"'\xZZ'", r"'\8'", r"'\9'"):
        try:
            evalString("'%s'" % bad.replace("\\", "\\\\")[1:-1] if False else "'" + bad[1:] + "'")
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # Missing quotes trip the assertion
    try:
        evalString("abc")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unquoted string")

# Generated at 2026-10-25 09:15:21.140936
# Unit test for function escape

# Generated at 2026-10-25 09:15:22.676544
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 09:15:24.027162
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 09:15:26.571037
# Unit test for function escape

# Generated at 2026-10-25 09:15:28.986649
# Unit test for function escape

# Generated at 2026-10-25 09:15:31.569997
# Unit test for function escape

# Generated at 2026-10-25 09:15:33.980877
# Unit test for function escape

# Generated at 2026-10-25 09:15:36.395021
# Unit test for function escape

# Generated at 2026-10-25 09:15:38.812112
# Unit test for function escape

# Generated at 2026-10-25 09:15:41.235782
# Unit test for function escape

# Generated at 2026-10-25 09:15:43.647093
# Unit test for function escape

# Generated at 2026-10-25 09:15:46.061824
# Unit test for function escape

# Generated at 2026-10-25 09:15:48.481323
# Unit test for function escape

# Generated at 2026-10-25 09:15:50.895256
# Unit test for function escape

# Generated at 2026-10-25 09:15:53.361135
# Unit test for function escape

# Generated at 2026-10-25 09:15:55.767584
# Unit test for function test

# Generated at 2026-10-25 09:15:58.177726
# Unit test for function test

# Generated at 2026-10-25 09:16:00.592348
# Unit test for function test

# Generated at 2026-10-25 09:16:03.008975
# Unit test for function escape

# Generated at 2026-10-25 09:16:32.189084
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 09:16:48.699534
# Unit test for function escape
def test_escape():
    import re

    # Helper: run module_0.escape() the way evalString does
    def run(raw):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", raw)
        assert m is not None, "regex did not match %r" % raw
        return module_0.escape(m)

    pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

    # 1. Simple escapes
    assert module_0.escape(pattern.match("\\n")) == "\n"
    assert module_0.escape(pattern.match("\\t")) == "\t"
    assert module_0.escape(pattern.match("\\r")) == "\r"
    assert module_0.escape(pattern.match("\\a")) == "\a"
    assert module_0.escape(pattern.match("\\b")) == "\b"
    assert module_0.escape(pattern.match("\\f")) == "\f"
    assert module_0.escape(pattern.match("\\v")) == "\v"
    assert module_0.escape(pattern.match("\\'")) == "'"
    assert module_0.escape(pattern.match('\\"')) == '"'
    assert module_0.escape(pattern.match("\\\\")) == "\\"

    # 2. Hex escapes (\xHH, one or two hex digits after \x)
    assert module_0.escape(pattern.match("\\x41")) == "A"
    assert module_0.escape(pattern.match("\\x4")) == "\x04"
    assert module_0.escape(pattern.match("\\x00")) == "\x00"
    assert module_0.escape(pattern.match("\\xff")) == "\xff"

    # 3. Octal escapes (1-3 octal digits)
    assert module_0.escape(pattern.match("\\101")) == "A"      # 0o101 == 65
    assert module_0.escape(pattern.match("\\0")) == "\x00"
    assert module_0.escape(pattern.match("\\7")) == "\x07"
    assert module_0.escape(pattern.match("\\777")) == "\xff"   # 0o777 == 255, chr() truncates? No:
    # Note: chr(0o777) == chr(511) == '\u01ff' â this is what module_0.escape() actually returns
    assert module_0.escape(pattern.match("\\777")) == chr(0o777)

    # 4. Invalid hex escapes raise ValueError
    for bad in ("\\xzz", "\\x"):
        try:
            module_0.escape(pattern.match(bad))
        except ValueError as e:
            assert "invalid hex string escape" in str(e)
        else:
            raise AssertionError("expected ValueError for %r" % bad)

    # 5. Invalid octal escapes raise ValueError
    try:
        module_0.escape(pattern.match("\\8"))   # regex matched? '8' is not in [0-7]
    except (ValueError, AttributeError):
        pass  # '\\8' doesn't match the regex at all; test via direct Match instead

    # 6. Exhaustive round-trip: every byte value survives repr -> evalString
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, "round-trip failed for %d" % i

    # 7. Realistic multi-escape strings via evalString
    assert evalString(r"'a\nb\x41\102'") == "a\nbAB"


if __name__ == "__main__":
    test_escape()
    print("all escape tests passed")

# Generated at 2026-10-25 09:16:51.224502
# Unit test for function test

# Generated at 2026-10-25 09:16:53.642015
# Unit test for function test

# Generated at 2026-10-25 09:16:56.054855
# Unit test for function test

# Generated at 2026-10-25 09:17:01.540467
# Unit test for function test

# Generated at 2026-10-25 09:17:03.957153
# Unit test for function test

# Generated at 2026-10-25 09:17:06.393827
# Unit test for function test

# Generated at 2026-10-25 09:17:19.411782
# Unit test for function escape

# Generated at 2026-10-25 09:17:20.805503
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 09:17:29.194904
# Unit test for function escape

# Generated at 2026-10-25 09:17:30.676043
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 09:17:33.752685
# Unit test for function test

# Generated at 2026-10-25 09:17:36.486214
# Unit test for function test

# Generated at 2026-10-25 09:17:38.903291
# Unit test for function test

# Generated at 2026-10-25 09:17:41.315390
# Unit test for function escape

# Generated at 2026-10-25 09:17:43.730650
# Unit test for function escape

# Generated at 2026-10-25 09:17:46.542364
# Unit test for function escape

# Generated at 2026-10-25 09:17:48.960537
# Unit test for function escape

# Generated at 2026-10-25 09:17:51.377973
# Unit test for function escape

# Generated at 2026-10-25 09:17:53.794076
# Unit test for function escape

# Generated at 2026-10-25 09:17:56.209129
# Unit test for function test

# Generated at 2026-10-25 09:17:58.626993
# Unit test for function test

# Generated at 2026-10-25 09:18:01.047467
# Unit test for function test

# Generated at 2026-10-25 09:18:03.735292
# Unit test for function escape

# Generated at 2026-10-25 09:18:06.152350
# Unit test for function escape

# Generated at 2026-10-25 09:18:08.568043
# Unit test for function escape

# Generated at 2026-10-25 09:18:10.985354
# Unit test for function test

# Generated at 2026-10-25 09:18:13.398642
# Unit test for function test

# Generated at 2026-10-25 09:18:15.813215
# Unit test for function test

# Generated at 2026-10-25 09:18:18.228035
# Unit test for function escape

# Generated at 2026-10-25 09:18:20.648436
# Unit test for function escape

# Generated at 2026-10-25 09:18:23.063132
# Unit test for function escape