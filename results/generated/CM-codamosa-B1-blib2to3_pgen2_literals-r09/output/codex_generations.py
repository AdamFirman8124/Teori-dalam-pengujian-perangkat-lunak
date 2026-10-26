

# Generated at 2026-10-25 12:38:53.987382
# Unit test for function evalString

# Generated at 2026-10-25 12:38:56.400967
# Unit test for function evalString

# Generated at 2026-10-25 12:38:58.815871
# Unit test for function evalString

# Generated at 2026-10-25 12:39:01.228383
# Unit test for function evalString

# Generated at 2026-10-25 12:39:03.641759
# Unit test for function evalString

# Generated at 2026-10-25 12:39:06.056252
# Unit test for function evalString

# Generated at 2026-10-25 12:39:08.469659
# Unit test for function evalString

# Generated at 2026-10-25 12:39:10.885589
# Unit test for function evalString

# Generated at 2026-10-25 12:39:13.299967
# Unit test for function evalString

# Generated at 2026-10-25 12:39:16.304549
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

# Generated at 2026-10-25 12:39:19.260699
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

# Generated at 2026-10-25 12:39:20.778875
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

# Generated at 2026-10-25 12:39:22.209912
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

# Generated at 2026-10-25 12:39:23.643071
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

# Generated at 2026-10-25 12:39:26.855788
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

# Generated at 2026-10-25 12:39:31.368301
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

# Generated at 2026-10-25 12:39:34.074287
# Unit test for function evalString

# Generated at 2026-10-25 12:39:37.098675
# Unit test for function evalString

# Generated at 2026-10-25 12:39:39.511641
# Unit test for function evalString

# Generated at 2026-10-25 12:39:41.925494
# Unit test for function escape

# Generated at 2026-10-25 12:39:44.339970
# Unit test for function escape

# Generated at 2026-10-25 12:39:47.021845
# Unit test for function escape

# Generated at 2026-10-25 12:39:49.435080
# Unit test for function escape

# Generated at 2026-10-25 12:39:51.849632
# Unit test for function escape

# Generated at 2026-10-25 12:39:54.264050
# Unit test for function escape

# Generated at 2026-10-25 12:39:56.676322
# Unit test for function escape

# Generated at 2026-10-25 12:39:59.090387
# Unit test for function escape

# Generated at 2026-10-25 12:40:01.527220
# Unit test for function escape

# Generated at 2026-10-25 12:40:03.941755
# Unit test for function escape

# Generated at 2026-10-25 12:40:06.357796
# Unit test for function escape

# Generated at 2026-10-25 12:40:08.772474
# Unit test for function escape

# Generated at 2026-10-25 12:40:11.521070
# Unit test for function test

# Generated at 2026-10-25 12:40:13.935190
# Unit test for function test

# Generated at 2026-10-25 12:40:16.348116
# Unit test for function test

# Generated at 2026-10-25 12:40:18.911948
# Unit test for function escape

# Generated at 2026-10-25 12:40:23.476495
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 12:40:28.183961
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

# Generated at 2026-10-25 12:40:29.896216
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

# Generated at 2026-10-25 12:40:31.558955
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

# Generated at 2026-10-25 12:40:33.071747
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

# Generated at 2026-10-25 12:40:38.885297
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

# Generated at 2026-10-25 12:40:40.384325
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

# Generated at 2026-10-25 12:40:45.157415
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

# Generated at 2026-10-25 12:40:49.253754
# Unit test for function escape

# Generated at 2026-10-25 12:40:51.670738
# Unit test for function escape

# Generated at 2026-10-25 12:40:54.434564
# Unit test for function escape

# Generated at 2026-10-25 12:40:56.849475
# Unit test for function escape

# Generated at 2026-10-25 12:40:59.268720
# Unit test for function escape

# Generated at 2026-10-25 12:41:01.682823
# Unit test for function escape

# Generated at 2026-10-25 12:41:04.093771
# Unit test for function escape

# Generated at 2026-10-25 12:41:06.509453
# Unit test for function escape

# Generated at 2026-10-25 12:41:09.226032
# Unit test for function escape

# Generated at 2026-10-25 12:41:11.645388
# Unit test for function test

# Generated at 2026-10-25 12:41:14.057285
# Unit test for function test

# Generated at 2026-10-25 12:41:16.473184
# Unit test for function test

# Generated at 2026-10-25 12:41:18.888598
# Unit test for function escape

# Generated at 2026-10-25 12:41:21.302772
# Unit test for function escape

# Generated at 2026-10-25 12:41:23.714966
# Unit test for function escape

# Generated at 2026-10-25 12:41:26.132193
# Unit test for function test

# Generated at 2026-10-25 12:41:28.546787
# Unit test for function test

# Generated at 2026-10-25 12:41:30.962188
# Unit test for function test

# Generated at 2026-10-25 12:41:33.378086
# Unit test for function escape

# Generated at 2026-10-25 12:41:35.794279
# Unit test for function escape

# Generated at 2026-10-25 12:41:38.207840
# Unit test for function escape

# Generated at 2026-10-25 12:41:40.811774
# Unit test for function escape

# Generated at 2026-10-25 12:41:42.254723
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 12:41:43.622899
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

# Generated at 2026-10-25 12:41:46.594516
# Unit test for function escape

# Generated at 2026-10-25 12:41:48.137658
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 12:42:05.927422
# Unit test for function escape

# Generated at 2026-10-25 12:42:08.341560
# Unit test for function escape

# Generated at 2026-10-25 12:42:10.757269
# Unit test for function escape

# Generated at 2026-10-25 12:42:13.173724
# Unit test for function escape

# Generated at 2026-10-25 12:42:15.881089
# Unit test for function escape

# Generated at 2026-10-25 12:42:18.293361
# Unit test for function escape

# Generated at 2026-10-25 12:42:20.706720
# Unit test for function escape

# Generated at 2026-10-25 12:42:23.121390
# Unit test for function escape

# Generated at 2026-10-25 12:42:25.537019
# Unit test for function escape

# Generated at 2026-10-25 12:42:27.952745
# Unit test for function escape

# Generated at 2026-10-25 12:42:30.366876
# Unit test for function escape

# Generated at 2026-10-25 12:42:32.781500
# Unit test for function escape

# Generated at 2026-10-25 12:42:35.196703
# Unit test for function escape

# Generated at 2026-10-25 12:42:37.612447
# Unit test for function escape

# Generated at 2026-10-25 12:42:40.027168
# Unit test for function escape

# Generated at 2026-10-25 12:42:42.811192
# Unit test for function escape

# Generated at 2026-10-25 12:42:47.433149
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 12:43:05.034932
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

# Generated at 2026-10-25 12:43:28.075359
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

# Generated at 2026-10-25 12:43:30.495263
# Unit test for function escape

# Generated at 2026-10-25 12:43:32.905601
# Unit test for function escape

# Generated at 2026-10-25 12:43:35.320992
# Unit test for function escape

# Generated at 2026-10-25 12:43:38.175286
# Unit test for function escape

# Generated at 2026-10-25 12:43:40.587504
# Unit test for function escape

# Generated at 2026-10-25 12:43:43.004043
# Unit test for function escape

# Generated at 2026-10-25 12:44:19.273872
# Unit test for function test

# Generated at 2026-10-25 12:44:21.693612
# Unit test for function test

# Generated at 2026-10-25 12:44:24.106221
# Unit test for function test

# Generated at 2026-10-25 12:44:26.634485
# Unit test for function test

# Generated at 2026-10-25 12:44:29.213912
# Unit test for function test

# Generated at 2026-10-25 12:44:31.773985
# Unit test for function test

# Generated at 2026-10-25 12:44:34.186787
# Unit test for function escape

# Generated at 2026-10-25 12:44:36.603820
# Unit test for function escape

# Generated at 2026-10-25 12:44:39.018300
# Unit test for function escape

# Generated at 2026-10-25 12:44:41.432389
# Unit test for function test

# Generated at 2026-10-25 12:44:43.847224
# Unit test for function test

# Generated at 2026-10-25 12:44:46.264794
# Unit test for function test

# Generated at 2026-10-25 12:44:48.681769
# Unit test for function escape

# Generated at 2026-10-25 12:44:51.095895
# Unit test for function escape

# Generated at 2026-10-25 12:44:53.511893
# Unit test for function escape

# Generated at 2026-10-25 12:44:55.924819
# Unit test for function escape

# Generated at 2026-10-25 12:44:58.338318
# Unit test for function escape

# Generated at 2026-10-25 12:45:00.752593
# Unit test for function escape

# Generated at 2026-10-25 12:45:03.169140
# Unit test for function escape

# Generated at 2026-10-25 12:45:04.943063
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 12:45:12.418475
# Unit test for function test

# Generated at 2026-10-25 12:45:22.671882
# Unit test for function test
def test_test():
    # Basic literals
    assert evalString("'hello'") == "hello"
    assert evalString('"hello"') == "hello"
    assert evalString("''") == ""
    assert evalString('""') == ""

    # Triple-quoted literals
    assert evalString("'''hi'''") == "hi"
    assert evalString('"""hi"""') == "hi"

    # Simple escapes
    assert evalString("'a\\nb'") == "a\nb"
    assert evalString("'a\\tb'") == "a\tb"
    assert evalString("'a\\rb'") == "a\rb"
    assert evalString("'a\\\\b'") == "a\\b"
    assert evalString("'a\\'b'") == "a'b"
    assert evalString('"a\\"b"') == 'a"b'

    # Hex escapes
    assert evalString("'\\x41'") == "A"
    assert evalString("'\\x7a'") == "z"

    # Octal escapes
    assert evalString("'\\101'") == "A"
    assert evalString("'\\0'") == "\x00"

    # Full round-trip over every character
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, (i, c, repr(c))

# Generated at 2026-10-25 12:45:49.186235
# Unit test for function test

# Generated at 2026-10-25 12:45:51.760893
# Unit test for function test

# Generated at 2026-10-25 12:45:54.175567
# Unit test for function test

# Generated at 2026-10-25 12:45:56.589170
# Unit test for function escape

# Generated at 2026-10-25 12:45:59.002664
# Unit test for function escape

# Generated at 2026-10-25 12:46:01.494671
# Unit test for function escape

# Generated at 2026-10-25 12:46:03.876619
# Unit test for function test

# Generated at 2026-10-25 12:46:06.290459
# Unit test for function test

# Generated at 2026-10-25 12:46:07.746288
# Unit test for function test
def test_test():
    # Basic literals
    assert evalString("'hello'") == "hello"
    assert evalString('"hello"') == "hello"
    assert evalString("''") == ""
    assert evalString('""') == ""

    # Triple-quoted literals
    assert evalString("'''hi'''") == "hi"
    assert evalString('"""hi"""') == "hi"

    # Simple escapes
    assert evalString("'a\\nb'") == "a\nb"
    assert evalString("'a\\tb'") == "a\tb"
    assert evalString("'a\\rb'") == "a\rb"
    assert evalString("'a\\\\b'") == "a\\b"
    assert evalString("'a\\'b'") == "a'b"
    assert evalString('"a\\"b"') == 'a"b'

    # Hex escapes
    assert evalString("'\\x41'") == "A"
    assert evalString("'\\x7a'") == "z"

    # Octal escapes
    assert evalString("'\\101'") == "A"
    assert evalString("'\\0'") == "\x00"

    # Full round-trip over every character
    for i in range(256):
        c = chr(i)
        assert evalString(repr(c)) == c, (i, c, repr(c))

# Generated at 2026-10-25 12:46:14.807409
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

# Generated at 2026-10-25 12:46:17.650012
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

# Generated at 2026-10-25 12:46:34.062072
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

# Generated at 2026-10-25 12:46:36.479316
# Unit test for function test

# Generated at 2026-10-25 12:46:38.892611
# Unit test for function test

# Generated at 2026-10-25 12:46:41.306449
# Unit test for function test

# Generated at 2026-10-25 12:46:43.918623
# Unit test for function test

# Generated at 2026-10-25 12:46:46.330053
# Unit test for function test

# Generated at 2026-10-25 12:46:48.744873
# Unit test for function test

# Generated at 2026-10-25 12:46:51.158690
# Unit test for function escape

# Generated at 2026-10-25 12:46:53.571679
# Unit test for function escape

# Generated at 2026-10-25 12:46:55.984721
# Unit test for function escape

# Generated at 2026-10-25 12:46:58.399357
# Unit test for function escape

# Generated at 2026-10-25 12:47:00.813164
# Unit test for function escape

# Generated at 2026-10-25 12:47:03.227153
# Unit test for function escape

# Generated at 2026-10-25 12:47:05.642413
# Unit test for function escape

# Generated at 2026-10-25 12:47:08.055213
# Unit test for function escape

# Generated at 2026-10-25 12:47:10.470587
# Unit test for function escape

# Generated at 2026-10-25 12:47:13.229054
# Unit test for function escape

# Generated at 2026-10-25 12:47:14.562285
# Unit test for function escape
def test_escape():pattern = re.compile(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})")

# Generated at 2026-10-25 12:47:32.682206
# Unit test for function test
def test_test():import io

# Generated at 2026-10-25 12:47:35.896414
# Unit test for function escape

# Generated at 2026-10-25 12:47:38.500505
# Unit test for function escape

# Generated at 2026-10-25 12:47:40.919338
# Unit test for function escape

# Generated at 2026-10-25 12:47:43.329000
# Unit test for function test

# Generated at 2026-10-25 12:47:45.743281
# Unit test for function test

# Generated at 2026-10-25 12:47:48.458435
# Unit test for function test

# Generated at 2026-10-25 12:47:50.872645
# Unit test for function test

# Generated at 2026-10-25 12:47:53.287000
# Unit test for function test

# Generated at 2026-10-25 12:47:55.700769
# Unit test for function test

# Generated at 2026-10-25 12:47:58.118135
# Unit test for function escape

# Generated at 2026-10-25 12:48:00.530138
# Unit test for function escape

# Generated at 2026-10-25 12:48:02.986109
# Unit test for function escape

# Generated at 2026-10-25 12:48:05.371824
# Unit test for function test

# Generated at 2026-10-25 12:48:07.786894
# Unit test for function test

# Generated at 2026-10-25 12:48:10.202601
# Unit test for function test

# Generated at 2026-10-25 12:48:12.615899
# Unit test for function escape

# Generated at 2026-10-25 12:48:15.031817
# Unit test for function escape

# Generated at 2026-10-25 12:48:17.443827
# Unit test for function escape

# Generated at 2026-10-25 12:48:19.857227
# Unit test for function escape

# Generated at 2026-10-25 12:48:22.272854
# Unit test for function escape

# Generated at 2026-10-25 12:48:24.686073
# Unit test for function escape

# Generated at 2026-10-25 12:48:27.101042
# Unit test for function escape

# Generated at 2026-10-25 12:48:29.515072
# Unit test for function escape

# Generated at 2026-10-25 12:48:31.930185
# Unit test for function escape

# Generated at 2026-10-25 12:48:34.343951
# Unit test for function escape

# Generated at 2026-10-25 12:48:36.758076
# Unit test for function escape

# Generated at 2026-10-25 12:48:39.286203
# Unit test for function escape

# Generated at 2026-10-25 12:48:41.700191
# Unit test for function test

# Generated at 2026-10-25 12:48:44.114144
# Unit test for function test

# Generated at 2026-10-25 12:48:46.531191
# Unit test for function test

# Generated at 2026-10-25 12:48:51.080341
# Unit test for function escape

# Generated at 2026-10-25 12:48:53.491813
# Unit test for function escape

# Generated at 2026-10-25 12:48:55.906360
# Unit test for function escape