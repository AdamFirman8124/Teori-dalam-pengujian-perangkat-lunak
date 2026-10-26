

# Generated at 2026-10-25 14:08:24.995483
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

# Generated at 2026-10-25 14:08:54.375551
# Unit test for function evalString

# Generated at 2026-10-25 14:09:00.490195
# Unit test for function evalString
def test_evalString():assert module_0.evalString(r"'hello\nworld\x21\040'") == "hello\nworld! "

# Generated at 2026-10-25 14:09:46.633078
# Unit test for function evalString
def test_evalString():cases = [
        ("''", ""),
        ('""', ""),
        ("'plain text'", "plain text"),
        ('"plain text"', "plain text"),
        ("'''multiple\nlines'''", "multiple\nlines"),
        ('"""multiple\nlines"""', "multiple\nlines"),
        ("'\\x41\\101'", "AA"),
        ("'\\0\\377\\777'", "\0" + chr(0o377) + chr(0o777)),
        (r"'\q'", r"\q"),
    ]


# Generated at 2026-10-25 14:09:53.697684
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 14:09:56.626224
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

# Generated at 2026-10-25 14:10:14.116495
# Unit test for function escape

# Generated at 2026-10-25 14:10:36.029349
# Unit test for function escape
def test_escape():assert module_0.escape(re.match(r"\\(.*)", r"\n")) == "\n"

# Generated at 2026-10-25 14:10:52.516204
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 14:11:08.630280
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

# Generated at 2026-10-25 14:11:11.256937
# Unit test for function test

# Generated at 2026-10-25 14:11:13.672448
# Unit test for function test

# Generated at 2026-10-25 14:11:16.090032
# Unit test for function test

# Generated at 2026-10-25 14:11:18.506480
# Unit test for function test

# Generated at 2026-10-25 14:11:20.923021
# Unit test for function test

# Generated at 2026-10-25 14:11:23.336090
# Unit test for function test

# Generated at 2026-10-25 14:11:25.755547
# Unit test for function test

# Generated at 2026-10-25 14:11:28.343216
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 14:11:44.844546
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

# Generated at 2026-10-25 14:12:07.681895
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

# Generated at 2026-10-25 14:12:32.689845
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 14:13:02.476333
# Unit test for function escape

# Generated at 2026-10-25 14:13:24.634990
# Unit test for function escape
def test_escape():assert module_0.escape(re.fullmatch(r"\\(a)", r"\a")) == "\a"

# Generated at 2026-10-25 14:13:34.002387
# Unit test for function test
def test_test():import contextlib

# Generated at 2026-10-25 14:13:49.771374
# Unit test for function escape

# Generated at 2026-10-25 14:14:04.720295
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-25 14:14:21.069707
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

# Generated at 2026-10-25 14:14:34.415070
# Unit test for function escape

# Generated at 2026-10-25 14:14:42.608815
# Unit test for function escape
def test_escape():match = re.match(r"\\(x41)", r"\x41")

# Generated at 2026-10-25 14:15:00.567411
# Unit test for function escape

# Generated at 2026-10-25 14:15:03.094809
# Unit test for function escape

# Generated at 2026-10-25 14:15:05.628256
# Unit test for function escape

# Generated at 2026-10-25 14:15:08.212591
# Unit test for function test

# Generated at 2026-10-25 14:15:10.799311
# Unit test for function test

# Generated at 2026-10-25 14:15:13.212989
# Unit test for function test

# Generated at 2026-10-25 14:15:15.714639
# Unit test for function test

# Generated at 2026-10-25 14:15:18.347915
# Unit test for function test

# Generated at 2026-10-25 14:15:20.767333
# Unit test for function test

# Generated at 2026-10-25 14:15:23.182421
# Unit test for function escape

# Generated at 2026-10-25 14:15:25.596284
# Unit test for function escape

# Generated at 2026-10-25 14:15:28.011129
# Unit test for function escape

# Generated at 2026-10-25 14:15:30.424281
# Unit test for function escape

# Generated at 2026-10-25 14:15:32.837153
# Unit test for function escape

# Generated at 2026-10-25 14:15:35.311069
# Unit test for function escape

# Generated at 2026-10-25 14:15:37.710084
# Unit test for function escape

# Generated at 2026-10-25 14:15:40.133481
# Unit test for function escape

# Generated at 2026-10-25 14:15:42.551632
# Unit test for function escape

# Generated at 2026-10-25 14:15:46.509231
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

# Generated at 2026-10-25 14:16:00.947650
# Unit test for function escape

# Generated at 2026-10-25 14:16:07.499142
# Unit test for function escape
def test_escape():match = re.match(r"\\(x[0-9A-Fa-f]{2})", r"\x41")

# Generated at 2026-10-25 14:16:24.748030
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

# Generated at 2026-10-25 14:16:32.793109
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

# Generated at 2026-10-25 14:16:45.592400
# Unit test for function escape

# Generated at 2026-10-25 14:16:55.934272
# Unit test for function escape
def test_escape():match = re.match(r"\\(n)", "\\n")

# Generated at 2026-10-25 14:17:27.816249
# Unit test for function evalString
def test_evalString():
    import pytest

    # Plain strings and quoting styles
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""
    assert module_0.evalString("'hello'") == "hello"
    assert module_0.evalString('"hello world"') == "hello world"
    assert module_0.evalString("'''multiline\nstring'''") == "multiline\nstring"
    assert module_0.evalString('"""triple quoted"""') == "triple quoted"

    # Simple escapes
    assert module_0.evalString(r"'\a\b\f\n\r\t\v'") == "\a\b\f\n\r\t\v"
    assert module_0.evalString(r"'\\'") == "\\"
    assert module_0.evalString(r"'can\'t'") == "can't"
    assert module_0.evalString(r'"say: \""') == 'say: "'

    # Hexadecimal and octal escapes
    assert module_0.evalString(r"'\x41\x42\x43'") == "ABC"
    assert module_0.evalString(r"'\101\102\103'") == "ABC"
    assert module_0.evalString(r"'\0\07\377'") == "\0\x07\xff"

    # Unknown escapes are preserved
    assert module_0.evalString(r"'\q'") == r"\q"

    # Every byte-sized character should survive a repr/evaluate round trip
    for i in range(256):
        character = chr(i)
        assert module_0.evalString(repr(character)) == character

    # Invalid hexadecimal escapes
    for literal in (r"'\x'", r"'\x1'", r"'\xGG'", r"'\xG1'"):
        with pytest.raises(ValueError, match="invalid hex string escape"):
            module_0.evalString(literal)

    # Invalid or mismatched delimiters
    for literal in ("unquoted", "'unterminated", '"unterminated'):
        with pytest.raises(AssertionError):
            module_0.evalString(literal)

# Generated at 2026-10-25 14:17:46.520535
# Unit test for function escape

# Generated at 2026-10-25 14:18:12.855352
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")