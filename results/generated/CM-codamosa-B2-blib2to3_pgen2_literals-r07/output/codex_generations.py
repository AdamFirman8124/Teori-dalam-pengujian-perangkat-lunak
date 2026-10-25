

# Generated at 2026-10-24 05:54:14.490175
# Unit test for function evalString

# Generated at 2026-10-24 05:54:33.181364
# Unit test for function evalString
def test_evalString():
    # plain quoting, both quote styles
    assert module_0.evalString("'abc'") == "abc"
    assert module_0.evalString('"abc"') == "abc"
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""

    # triple-qu

# Generated at 2026-10-24 05:54:45.325055
# Unit test for function escape

# Generated at 2026-10-24 05:54:46.794935
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 05:55:13.641854
# Unit test for function evalString

# Generated at 2026-10-24 05:55:14.951242
# Unit test for function evalString
def test_evalString():
    # plain quoting, both quote styles
    assert module_0.evalString("'abc'") == "abc"
    assert module_0.evalString('"abc"') == "abc"
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""

    # triple-qu

# Generated at 2026-10-24 05:55:31.546463
# Unit test for function test
def test_test():
    import io
    import sys

    # module_0.test() prints only when a round-trip mismatch is found;
    # a clean run must produce no output at all.
    buf = io.StringIO()
    orig_stdout = sys.stdout
    sys.stdout = buf
    try:
        module_0.test()
    finally:
        sys.stdout = orig_stdout
    assert buf.getvalue() == "", "module_0.test() reported mismatches: %r" % buf.getvalue()

    # Direct checks on the underlying round-trip behavior.
    assert evalString("'\\n'") == "\n"
    assert evalString("'\\t'") == "\t"
    assert evalString("'\\x41'") == "A"
    assert evalString("'\\101'") == "A"
    assert evalString('"a\\tb"') == "a\tb"
    assert evalString(repr(chr(0))) == chr(0)
    assert evalString(repr(chr(255))) == chr(255)
    assert evalString(repr("quote's")) == "quote's"
    assert evalString(repr('say "hi"')) == 'say "hi"'

    # Invalid escapes must raise ValueError.
    for bad in ("'\\x'", "'\\xg1'", "'\\8'", "'\\9'"):
        try:
            evalString(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % bad)

# Generated at 2026-10-24 05:55:44.141214
# Unit test for function escape
def test_escape():import pytest


def test_escape() -> None:
    def match_escape(value: Text) -> Match[Text]:
        match = re.fullmatch(r"\\(.*)", value)
        assert match is not None
        return match

    for tail, expected in simple_escapes.items():
        assert module_0.escape(match_escape("\\" + tail)) == expected

    assert module_0.escape(match_escape(r"\x41")) == "A"
    assert module_0.escape(match_escape(r"\xFF")) == "\xff"
    assert module_0.escape(match_escape(r"\0")) == "\0"
    assert module_0.escape(match_escape(r"\101")) == "A"
    assert module_0.escape(match_escape(r"\377")) == "\xff"

    for invalid in (r"\x", r"\x1", r"\xGG", r"\8", r"\q"):
        with pytest.raises(ValueError):
            module_0.escape(match_escape(invalid))

# Generated at 2026-10-24 05:55:56.327742
# Unit test for function escape

# Generated at 2026-10-24 05:55:57.761703
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 05:56:08.204906
# Unit test for function escape
def test_escape():import pytest


def test_escape() -> None:
    def evaluate(value: Text) -> Text:
        match = re.fullmatch(r"\\(.*)", value, flags=re.DOTALL)
        assert match is not None
        return module_0.escape(match)

    for escaped, expected in simple_escapes.items():
        assert evaluate("\\" + escaped) == expected

    assert evaluate(r"\x00") == "\x00"
    assert evaluate(r"\x41") == "A"
    assert evaluate(r"\xFF") == "\xff"

    assert evaluate(r"\0") == "\0"
    assert evaluate(r"\12") == "\n"
    assert evaluate(r"\141") == "a"

    for invalid in (r"\x", r"\xG1", r"\8", r"\invalid"):
        with pytest.raises(ValueError):
            evaluate(invalid)

# Generated at 2026-10-24 05:56:20.375953
# Unit test for function escape
def test_escape():import pytest


def test_escape() -> None:
    def decode(value: Text) -> Text:
        match = re.fullmatch(r"\\(.*)", value)
        assert match is not None
        return module_0.escape(match)

    for tail, expected in simple_escapes.items():
        assert decode("\\" + tail) == expected

    assert decode(r"\x41") == "A"
    assert decode(r"\xFF") == "\xff"
    assert decode(r"\101") == "A"
    assert decode(r"\0") == "\0"
    assert decode(r"\777") == chr(0o777)

    with pytest.raises(ValueError, match="invalid hex string escape"):
        decode(r"\x")

    with pytest.raises(ValueError, match="invalid hex string escape"):
        decode(r"\xG1")

    with pytest.raises(ValueError, match="invalid octal string escape"):
        decode(r"\8")

# Generated at 2026-10-24 05:56:32.474791
# Unit test for function escape

# Generated at 2026-10-24 05:56:33.913275
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 05:56:41.818044
# Unit test for function test

# Generated at 2026-10-24 05:56:43.224650
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 05:56:59.303408
# Unit test for function escape

# Generated at 2026-10-24 05:57:00.734795
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 05:57:18.450730
# Unit test for function evalString
def test_evalString():import pytest


def test_evalString() -> None:
    # Ordinary quoted strings.
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""
    assert module_0.evalString("'hello'") == "hello"
    assert module_0.evalString('"hello world"') == "hello world"

    # Triple-quoted strings.
    assert module_0.evalString("'''hello'''") == "hello"
    assert module_0.evalString('"""line 1\nline 2"""') == "line 1\nline 2"

    # Simple escape sequences.
    assert module_0.evalString(r"'\a\b\f\n\r\t\v'") == "\a\b\f\n\r\t\v"
    assert module_0.evalString(r"'can\'t'") == "can't"
    assert module_0.evalString(r'"say \"hello\""') == 'say "hello"'
    assert module_0.evalString(r"'\\'") == "\\"

    # Hexadecimal and octal escapes.
    assert module_0.evalString(r"'\x00'") == "\x00"
    assert module_0.evalString(r"'\x41'") == "A"
    assert module_0.evalString(r"'\101'") == "A"
    assert module_0.evalString(r"'\7'") == "\x07"
    assert module_0.evalString(r"'\12'") == "\n"
    assert module_0.evalString(r"'\777'") == chr(0o777)

    # Multiple and adjacent escapes.
    assert module_0.evalString(r"'\x48\145llo\n'") == "Hello\n"

    # Unknown escapes are preserved.
    assert module_0.evalString(r"'\q'") == r"\q"

    # Verify every character representation handled by the original test.
    for i in range(256):
        character = chr(i)
        assert module_0.evalString(repr(character)) == character

    # Invalid hexadecimal escapes.
    with pytest.raises(ValueError, match="invalid hex string escape"):
        module_0.evalString(r"'\x'")

    with pytest.raises(ValueError, match="invalid hex string escape"):
        module_0.evalString(r"'\x4'")

    with pytest.raises(ValueError, match="invalid hex string escape"):
        module_0.evalString(r"'\xGG'")

    # Invalid or mismatched delimiters.
    with pytest.raises(AssertionError):
        module_0.evalString("unquoted")

    with pytest.raises(AssertionError):
        module_0.evalString("'unterminated")

# Generated at 2026-10-24 05:57:34.119686
# Unit test for function evalString
def test_evalString():import pytest


def test_evalString() -> None:
    # Every character represented by repr() should round-trip correctly.
    for i in range(256):
        character = chr(i)
        assert module_0.evalString(repr(character)) == character

    # Supported quoting and escape forms.
    assert module_0.evalString("'plain text'") == "plain text"
    assert module_0.evalString('"plain text"') == "plain text"
    assert module_0.evalString(r"'don\'t'") == "don't"
    assert module_0.evalString(r'"say \"hello\""') == 'say "hello"'
    assert module_0.evalString(r"'\\'") == "\\"
    assert module_0.evalString(r"'\141\142\143'") == "abc"
    assert module_0.evalString(r"'\x41\x42\x43'") == "ABC"
    assert module_0.evalString('"""line 1\\nline 2"""') == "line 1\nline 2"
    assert module_0.evalString("'''line 1\\tline 2'''") == "line 1\tline 2"

    # Unknown escapes are preserved.
    assert module_0.evalString(r"'\q'") == r"\q"

    # Hex escapes require exactly two valid hexadecimal digits.
    for literal in (r"'\x'", r"'\x1'", r"'\xGG'", r"'\xG1'"):
        with pytest.raises(ValueError, match="invalid hex string escape"):
            module_0.evalString(literal)

# Generated at 2026-10-24 05:58:01.051718
# Unit test for function evalString
def test_evalString():import pytest


def test_evalString() -> None:
    cases = [
        ("''", ""),
        ('""', ""),
        ("'plain text'", "plain text"),
        ('"plain text"', "plain text"),
        ("'''line 1\nline 2'''", "line 1\nline 2"),
        ('"""line 1\nline 2"""', "line 1\nline 2"),
        (r"'it\'s'", "it's"),
        (r'"say \"hello\""', 'say "hello"'),
        (r"'\a\b\f\n\r\t\v\\'", "\a\b\f\n\r\t\v\\"),
        (r"'\x41\101'", "AA"),
        (r"'\0\12\377'", "\0\n\xff"),
        (r"'\q\8'", r"\q\8"),  # Unsupported escapes are preserved.
        ("'Unicode: cafÃ© â'", "Unicode: cafÃ© â"),
    ]

    for literal, expected in cases:
        assert module_0.evalString(literal) == expected

    # repr() should round-trip every byte-valued character.
    for i in range(256):
        character = chr(i)
        assert module_0.evalString(repr(character)) == character

    for invalid_hex in (r"'\x'", r"'\x1'", r"'\xGG'"):
        with pytest.raises(ValueError, match="invalid hex string escape"):
            module_0.evalString(invalid_hex)

    for malformed in ("unquoted", "'unterminated", "'''"):
        with pytest.raises(AssertionError):
            module_0.evalString(malformed)

# Generated at 2026-10-24 05:58:08.832039
# Unit test for function test

# Generated at 2026-10-24 05:58:10.268091
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 05:58:21.542941
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    output = io.StringIO()
    with redirect_stdout(output):
        module_0.test()

    assert output.getvalue() == ""

# Generated at 2026-10-24 05:58:33.277439
# Unit test for function escape

# Generated at 2026-10-24 05:58:34.747614
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 05:58:41.396468
# Unit test for function test

# Generated at 2026-10-24 05:58:42.829211
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 05:59:05.869896
# Unit test for function escape

# Generated at 2026-10-24 05:59:07.301573
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 05:59:20.922143
# Unit test for function test

# Generated at 2026-10-24 05:59:22.354964
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 05:59:31.881007
# Unit test for function test

# Generated at 2026-10-24 05:59:33.297184
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 05:59:40.993728
# Unit test for function test

# Generated at 2026-10-24 05:59:42.427028
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 05:59:49.902593
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    output = io.StringIO()
    with redirect_stdout(output):
        module_0.test()

    assert output.getvalue() == ""

# Generated at 2026-10-24 05:59:59.732272
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout

    output = io.StringIO()
    with redirect_stdout(output):
        module_0.test()

    assert output.getvalue() == ""

# Generated at 2026-10-24 06:00:10.177408
# Unit test for function escape

# Generated at 2026-10-24 06:00:12.712513
# Unit test for function escape

# Generated at 2026-10-24 06:00:15.128662
# Unit test for function escape

# Generated at 2026-10-24 06:00:17.544798
# Unit test for function escape

# Generated at 2026-10-24 06:00:20.698120
# Unit test for function escape

# Generated at 2026-10-24 06:00:31.360272
# Unit test for function escape
def test_escape():simple = re.match(r"\\(.*)", r"\n")

# Generated at 2026-10-24 06:00:44.083713
# Unit test for function escape

# Generated at 2026-10-24 06:00:45.546027
# Unit test for function escape
def test_escape():import re

# Generated at 2026-10-24 06:00:52.672757
# Unit test for function test

# Generated at 2026-10-24 06:00:54.105744
# Unit test for function test
def test_test():import io

# Generated at 2026-10-24 06:00:56.718214
# Unit test for function escape

# Generated at 2026-10-24 06:00:59.133279
# Unit test for function escape

# Generated at 2026-10-24 06:01:01.701410
# Unit test for function escape

# Generated at 2026-10-24 06:01:04.206493
# Unit test for function escape

# Generated at 2026-10-24 06:01:06.621383
# Unit test for function escape

# Generated at 2026-10-24 06:01:09.036661
# Unit test for function escape

# Generated at 2026-10-24 06:01:11.450083
# Unit test for function escape

# Generated at 2026-10-24 06:01:13.865007
# Unit test for function escape

# Generated at 2026-10-24 06:01:16.280640
# Unit test for function escape

# Generated at 2026-10-24 06:01:18.694657
# Unit test for function test

# Generated at 2026-10-24 06:01:21.111194
# Unit test for function test

# Generated at 2026-10-24 06:01:23.525481
# Unit test for function test

# Generated at 2026-10-24 06:01:25.938627
# Unit test for function escape

# Generated at 2026-10-24 06:01:28.352989
# Unit test for function escape

# Generated at 2026-10-24 06:01:30.766868
# Unit test for function escape

# Generated at 2026-10-24 06:01:33.181949
# Unit test for function test

# Generated at 2026-10-24 06:01:35.596492
# Unit test for function test

# Generated at 2026-10-24 06:01:38.012255
# Unit test for function test

# Generated at 2026-10-24 06:01:40.424981
# Unit test for function test

# Generated at 2026-10-24 06:01:42.838125
# Unit test for function test

# Generated at 2026-10-24 06:01:45.256719
# Unit test for function test

# Generated at 2026-10-24 06:01:47.668203
# Unit test for function test

# Generated at 2026-10-24 06:01:50.082751
# Unit test for function test

# Generated at 2026-10-24 06:01:52.500000
# Unit test for function test

# Generated at 2026-10-24 06:01:54.912232
# Unit test for function escape

# Generated at 2026-10-24 06:01:57.326107
# Unit test for function escape

# Generated at 2026-10-24 06:01:59.742361
# Unit test for function escape

# Generated at 2026-10-24 06:02:02.158477
# Unit test for function test

# Generated at 2026-10-24 06:02:04.571603
# Unit test for function test

# Generated at 2026-10-24 06:02:06.983576
# Unit test for function test

# Generated at 2026-10-24 06:02:09.397766
# Unit test for function test

# Generated at 2026-10-24 06:02:11.811982
# Unit test for function test

# Generated at 2026-10-24 06:02:14.225149
# Unit test for function test

# Generated at 2026-10-24 06:02:16.642880
# Unit test for function test

# Generated at 2026-10-24 06:02:19.055247
# Unit test for function test

# Generated at 2026-10-24 06:02:21.471547
# Unit test for function test

# Generated at 2026-10-24 06:02:23.884393
# Unit test for function escape

# Generated at 2026-10-24 06:02:30.989783
# Unit test for function escape
def test_escape():match = re.match(r"\\(x.{0,2})", r"\x41")

# Generated at 2026-10-24 06:02:51.457947
# Unit test for function evalString

# Generated at 2026-10-24 06:02:52.784529
# Unit test for function evalString
def test_evalString():
    # plain quoting, both quote styles
    assert module_0.evalString("'abc'") == "abc"
    assert module_0.evalString('"abc"') == "abc"
    assert module_0.evalString("''") == ""
    assert module_0.evalString('""') == ""

    # triple-qu

# Generated at 2026-10-24 06:03:04.704023
# Unit test for function escape

# Generated at 2026-10-24 06:03:07.123585
# Unit test for function escape

# Generated at 2026-10-24 06:03:09.537500
# Unit test for function escape

# Generated at 2026-10-24 06:03:11.954075
# Unit test for function escape

# Generated at 2026-10-24 06:03:14.368908
# Unit test for function escape

# Generated at 2026-10-24 06:03:16.785637
# Unit test for function escape

# Generated at 2026-10-24 06:03:19.197288
# Unit test for function escape

# Generated at 2026-10-24 06:03:21.613235
# Unit test for function escape

# Generated at 2026-10-24 06:03:24.027591
# Unit test for function escape

# Generated at 2026-10-24 06:03:26.922337
# Unit test for function test

# Generated at 2026-10-24 06:03:29.335926
# Unit test for function test

# Generated at 2026-10-24 06:03:31.750859
# Unit test for function test

# Generated at 2026-10-24 06:03:34.164170
# Unit test for function escape

# Generated at 2026-10-24 06:03:36.577910
# Unit test for function escape

# Generated at 2026-10-24 06:03:38.991288
# Unit test for function escape

# Generated at 2026-10-24 06:03:41.409199
# Unit test for function escape

# Generated at 2026-10-24 06:03:43.823121
# Unit test for function escape

# Generated at 2026-10-24 06:03:46.234613
# Unit test for function escape

# Generated at 2026-10-24 06:03:48.655569
# Unit test for function escape

# Generated at 2026-10-24 06:03:51.076723
# Unit test for function escape

# Generated at 2026-10-24 06:03:53.493577
# Unit test for function escape