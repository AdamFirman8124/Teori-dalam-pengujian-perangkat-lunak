

# Generated at 2022-06-13 17:50:05.007771
# Unit test for function evalString
def test_evalString():
    assert evalString('"\\0"') == "\0"
    assert evalString("'\\0'") == "\0"
    assert evalString("'\\''") == "'"
    assert evalString('"\\""') == '"'
    assert evalString("'\\a'") == "\a"
    assert evalString("'\\b'") == "\b"
    assert evalString("'\\f'") == "\f"
    assert evalString("'\\n'") == "\n"
    assert evalString("'\\r'") == "\r"
    assert evalString("'\\t'") == "\t"
    assert evalString("'\\v'") == "\v"
    assert evalString("'\\x61'") == "a"
    assert evalString("'\\4'") == chr(4)

# Generated at 2022-06-13 17:50:06.690273
# Unit test for function test
def test_test():
    with pytest.raises(AssertionError):
        test()

# Generated at 2022-06-13 17:50:18.118236
# Unit test for function escape
def test_escape():
    # Test escaping of characters already escaped
    assert escape(re.match(r'\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\\xef')) == '\xef'
    assert escape(re.match(r'\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\\167')) == '\x87'
    assert escape(re.match(r'\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\\07')) == '\x07'

# Generated at 2022-06-13 17:50:29.441707
# Unit test for function evalString
def test_evalString():
    assert evalString(r'"\r\n\t"') == "\r\n\t"
    assert evalString(r"'\r\n\t'") == "\r\n\t"
    assert evalString(r'"\x00\n\t"') == "\x00\n\t"
    assert evalString(r"'\x00\n\t'") == "\x00\n\t"
    assert evalString(r'"\xFF\n\t"') == "\xFF\n\t"
    assert evalString(r"'\xFF\n\t'") == "\xFF\n\t"
    assert evalString(r'"\377\n\t"') == "\377\n\t"
    assert evalString(r"'\377\n\t'") == "\377\n\t"

# Generated at 2022-06-13 17:50:35.127693
# Unit test for function evalString
def test_evalString():
    assert evalString("'0'") == '0'
    assert evalString("'1'") == '1'
    # Test for strings which require escaping
    assert evalString("'\\\\'") == '\\'
    assert evalString("'\\x42'") == 'B'
    assert evalString("'\\n'") == '\n'
    assert evalString("'\\r'") == '\r'
    assert evalString("'\\''") == "'"
    assert evalString("'\\\"'") == '"'
    assert evalString("'\\t'") == '\t'
    assert evalString("'\\a'") == '\a'
    assert evalString("'\\f'") == '\f'

# Generated at 2022-06-13 17:50:44.039130
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x", "\\x")) == r"\x"

# Generated at 2022-06-13 17:50:55.111624
# Unit test for function escape
def test_escape():
    # Can we handle valid escapes correctly
    for c in simple_escapes.keys():
        # Note: Can use re.escape instead of '\\' + character
        assert escape(re.search(re.escape(c), '\\' + c)) == c

    # Can we handle octal escapes correctly
    assert escape(re.search(r'\o', '\\012')) == '\n'
    assert escape(re.search(r'\o', '\\777')) == '\xFF'
    assert escape(re.search(r'\o', '\\400')) == '\x00'
    assert escape(re.search(r'\o', '\\1')) == '\x01'

    # Can we handle hex escapes correctly

# Generated at 2022-06-13 17:51:00.072890
# Unit test for function escape
def test_escape():
    tests = {'\\x61': 'a', '\\x41': 'A', '\\123': 'S', '\\a': '\a', '\\xG1': 'Invalid'}
    for test in tests.keys():
        assert escape(re.match(r'\\([abfnrtv]|x.{0,2}|[0-7]{1,3})', test)) == tests[test]


# Generated at 2022-06-13 17:51:06.762531
# Unit test for function escape
def test_escape():
    from tests.test_literals import assert_eval_equal

    assert_eval_equal("'\\xab'", "b''")
    assert_eval_equal("'\\141\\142'", "b''")
    assert_eval_equal("'\\xab\\n'", b"\xab\n")
    assert_eval_equal("'\\141\\142\\n'", b"\xab\n")
    assert_eval_equal("'\\741\\142'", b"\xab")
    assert_eval_equal("'\\141\\742'", b"\xab")
    assert_eval_equal('"\\xab\\n"', '"\xab\\n"')
    assert_eval_equal('"\\141\\142\\n"', '"ab\\n"')
    assert_eval_

# Generated at 2022-06-13 17:51:07.468758
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:51:24.217602
# Unit test for function escape
def test_escape():
    assert escape("\\a") == "\\a"
    assert escape("\\xaa") == "\\xaa"
    assert escape("\\255") == "\\255"
    with pytest.raises(ValueError):
        escape("\\x")
    with pytest.raises(ValueError):
        escape("\\xaz")
    with pytest.raises(ValueError):
        escape("\\256")
    with pytest.raises(ValueError):
        escape("\\1000")


# Generated at 2022-06-13 17:51:31.474291
# Unit test for function escape
def test_escape():
    from unittest import TestCase

    class TestEscape(TestCase):
        def test_escape(self):
            self.assertEqual(escape(r"\\x04"), r"\\x04")
            self.assertRaises(ValueError, escape, r"\x04")
            self.assertEqual(escape(r"\056"), r".")
            self.assertRaises(ValueError, escape, r"\56")
            self.assertRaises(ValueError, escape, r"\56\x\04")

# Generated at 2022-06-13 17:51:32.504010
# Unit test for function test
def test_test():
    lines = test().splitlines()
    assert len(lines) == 0, lines

# Generated at 2022-06-13 17:51:40.189841
# Unit test for function escape
def test_escape():
    tests = (
        ("\\a", "\a"),
        ("\\b", "\b"),
        ("\\f", "\f"),
        ("\\n", "\n"),
        ("\\r", "\r"),
        ("\\t", "\t"),
        ("\\v", "\v"),
        ("\\\\", "\\"),
        ("\\'", "'"),
        ('\\"', '"'),
        ("\\x00", "\x00"),
        ("\\x41", "A"),
        ("\\777", "\x1f"),
        ("\\400", "\x00"),
        ("\\255", "\x00"),
    )
    for test, expected in tests:
        assert escape(re.match("(.*)", test)) == expected


if __name__ == "__main__":
    test_escape()

# Generated at 2022-06-13 17:51:49.890774
# Unit test for function escape
def test_escape():
    # Test hex escape
    assert escape(re.match(r"\\x.{0,2}", r"\xf0")) == chr(0xf0)
    assert escape(re.match(r"\\x.{0,2}", r"\x0a")) == chr(0x0a)
    assert escape(re.match(r"\\x.{0,2}", r"\x00")) == chr(0x00)
    # Test octal escape
    assert escape(re.match(r"\\[0-7]{1,3}", r"\000")) == chr(0)
    assert escape(re.match(r"\\[0-7]{1,3}", r"\377")) == chr(255)

# Generated at 2022-06-13 17:51:59.217598
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv'\"\\]|\d{1,3}|x(?:.*)?)", r"\a")) == "\a"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|\d{1,3}|x(?:.*)?)", r"\b")) == "\b"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|\d{1,3}|x(?:.*)?)", r"\f")) == "\f"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|\d{1,3}|x(?:.*)?)", r"\n")) == "\n"

# Generated at 2022-06-13 17:52:03.497660
# Unit test for function escape
def test_escape():
    try:
        escape(None)
    except TypeError:
        pass
    else:
        print("FAILED: expected to raise TypeError")

    assert escape(re.match(r"\\x", "\\x")) == '\\'
    assert escape(re.match(r"\\", "\\x")) == 'x'

# Generated at 2022-06-13 17:52:04.256592
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:11.186088
# Unit test for function escape
def test_escape():
    import ast
    import string
    from string import hexdigits, octdigits
    from random import choice

    # Test simple escapes
    for char, value in simple_escapes.items():
        assert ast.literal_eval(r'\%s' % char) == value
    assert ast.literal_eval(r'\0') == '\x00'

    # Test hex escapes
    for i in range(1, 16):
        assert ast.literal_eval(r'\x%x' % i) == chr(i)
    for i in range(16, 256):
        # chr() may return something different on some platforms
        assert len(ast.literal_eval(r'\x%x' % i)) == 1

    # Test octal escapes

# Generated at 2022-06-13 17:52:14.374884
# Unit test for function escape
def test_escape():
    assert len(escape.__annotations__) == 2
    assert escape.__annotations__['m'] == Match[Text]
    assert escape.__annotations__['return'] == Text


# Generated at 2022-06-13 17:52:35.032023
# Unit test for function test
def test_test():
    test

# Generated at 2022-06-13 17:52:35.624312
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:47.331140
# Unit test for function escape
def test_escape():
    import sys
    import os

    def _fake_m(s):
        return (s, s)

    if sys.platform == "win32":
        newline = "\n"
        nulldevice = "NUL"
    else:
        newline = "\n"
        nulldevice = "/dev/null"

    assert escape(_fake_m("\a")) == "\a"
    assert escape(_fake_m("\b")) == "\b"
    assert escape(_fake_m("\f")) == "\f"
    assert escape(_fake_m("\n")) == "\n"
    if os.linesep != "\n":
        # We assume this is tested in test_tokenize.py.
        assert escape(_fake_m("\r")) == "\r"
    assert escape(_fake_m("\t")) == "\t"


# Generated at 2022-06-13 17:52:53.017213
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\x41', '\\x41')) == 'A'
    assert escape(re.match('\\x4G', '\\x4G')) == '4G'

    #  couldn't get the specific ValueError to be raised
    #  ValueError: invalid hex string escape ('\\x4G')
    #  assert escape(re.match('\\x4G', '\\x4G')) == '4G'

# Generated at 2022-06-13 17:52:55.170488
# Unit test for function escape
def test_escape():
    assert "\\x" == escape(re.match(r"\\x", "\\x")).strip()



# Generated at 2022-06-13 17:53:04.941741
# Unit test for function escape
def test_escape():
    # Answers are based on Python 2.5.5
    assert escape('\\a') == chr(7)
    assert escape('\\b') == chr(8)
    assert escape('\\f') == chr(12)
    assert escape('\\n') == chr(10)
    assert escape('\\r') == chr(13)
    assert escape('\\t') == chr(9)
    assert escape('\\v') == chr(11)
    assert escape('\\"') == '"'
    assert escape("\\\'") == "'"
    assert escape('\\\\') == '\\'
    assert escape('\\x61') == 'a'
    assert escape('\\11') == chr(9)
    assert escape('\\011') == chr(9)
    assert escape('\\x05f') == '_'


# Generated at 2022-06-13 17:53:05.554809
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:13.492929
# Unit test for function escape
def test_escape():
    assert escape('\\a') == '\x07'
    assert escape('\\b') == '\x08'
    assert escape('\\f') == '\x0c'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\x0b'
    assert escape('\\"') == "\""
    assert escape('\\\'') == "'"
    assert escape('\\\\') == "\\"
    assert escape('\\x1a') == '\x1a'
    assert escape('\\07') == '\x07'
    assert escape('\\012') == '\n'
    assert escape('\\37') == '\x1f'

# Generated at 2022-06-13 17:53:15.321670
# Unit test for function escape
def test_escape():
    assert evalString('"\\n"') == "\n"



# Generated at 2022-06-13 17:53:25.449058
# Unit test for function escape
def test_escape():
    nonr = r'\n \x1234 \12 \35 \xAA x'
    assert escape(re.match(r'\\(x.{0,2}|[0-7]{1,3})', r'\12')) == '\n'
    assert escape(re.match(r'\\(x.{0,2}|[0-7]{1,3})', r'\35')) == '\n'
    assert escape(re.match(r'\\(x.{0,2}|[0-7]{1,3})', r'\x1234')) == '\x1234'
    assert escape(re.match(r'\\(x.{0,2}|[0-7]{1,3})', r'\xAA')) == '\xaa'

# Generated at 2022-06-13 17:53:58.862794
# Unit test for function escape
def test_escape():
    assert escape(re.search(r'\\[abfnrtv]', 'x')) is None
    assert escape(re.search(r'\\([abfnrtv])', '\a'))[1] == 'a'
    assert escape(re.search(r'\\([abfnrtv])', '\b'))[1] == 'b'
    assert escape(re.search(r'\\([abfnrtv])', '\f'))[1] == 'f'
    assert escape(re.search(r'\\([abfnrtv])', '\n'))[1] == 'n'
    assert escape(re.search(r'\\([abfnrtv])', '\r'))[1] == 'r'

# Generated at 2022-06-13 17:54:09.948200
# Unit test for function escape
def test_escape():
    m = re.search(r"\\x([0-9a-fA-F]{2})", "\\x1234")
    assert m
    assert escape(m) == '\x12'

    m = re.search(r"\\x([0-9a-fA-F]{2})", "\\x99")
    assert m
    assert escape(m) == '\x99'
    
    m = re.search(r"\\x([0-9a-fA-F]{2})", "\\xZZ")
    assert m
    try:
        escape(m)
        assert False
    except ValueError:
        pass

    m = re.search(r"\\x([0-9a-fA-F]{2})", "\\xZ")
    assert m

# Generated at 2022-06-13 17:54:16.948604
# Unit test for function escape
def test_escape():
    testcases = [
        ("\\'", "'"),
        ('\\"', '"'),
        ("\\n", "\n"),
        ("\\123", "\123"),
        ("\\x61", "a"),
        ("\\x6a", "j"),
        ("\\xab", "\xab"),
        ("\\uFFFf", "\uFFFf"),
        ("\\uABCd", "\uABCd"),
        ("\\U0000ABCD", "\U0000ABCD"),
        ("\\U0001ABCD", "\U0001ABCD"),
        ("\\U0004ABCD", "\U0004ABCD"),
    ]


# Generated at 2022-06-13 17:54:18.192675
# Unit test for function test
def test_test():
    try:
        test()
    except:
        raise Exception("Failure")

# Generated at 2022-06-13 17:54:18.877242
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:54:28.043559
# Unit test for function escape
def test_escape():
    test_escape_quotes = [("\\'", "'"), ('\\"', '"'), ("\\\\", "\\")]
    test_escape_others = [("\\a", "\a"), ("\\b", "\b"), ("\\f", "\f"), ("\\n", "\n"), ("\\r", "\r"), ("\\t", "\t"), ("\\v", "\v")]

    def test_escape_results(tests):
        for (input, output) in tests:
            assert escape(re.match(r'\\(.*)', input)) == output

    test_escape_results(test_escape_quotes)
    test_escape_results(test_escape_others)

# Generated at 2022-06-13 17:54:30.805963
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\.{2}', '\\10')) == chr(8)
    assert escape(re.match(r'\\.{2}', '\\10')) != '\\10'

# Generated at 2022-06-13 17:54:37.091064
# Unit test for function escape
def test_escape():
    assert escape(re.search(r'\\x1f', "\\x1f")) == "\x1f"
    assert escape(re.search(r'\\1f', "\\1f")) == "\x1f"
    assert escape(re.search(r'\\xf', "\\xf")) == "\x0f"
    assert escape(re.search(r'\\f', "\\f")) == "\x0c"



# Generated at 2022-06-13 17:54:42.236671
# Unit test for function escape
def test_escape():
    assert escape("\\x01") == chr(1)
    assert escape("\\x7f") == chr(127)
    assert escape("\\377") == chr(255)
    assert escape("\\x00") == chr(0)
    assert escape("\\en") == chr(10)
    assert escape("\\t") == chr(9)
    assert escape("\\r") == chr(13)
    assert escape("\\v") == chr(11)
    assert escape("\\a") == chr(7)
    assert escape("\\b") == chr(8)
    assert escape("\\f") == chr(12)
    assert escape("\\'") == chr(39)
    assert escape('\\"') == chr(34)
    assert escape("\\\\") == chr(92)


# Generated at 2022-06-13 17:54:52.321123
# Unit test for function escape
def test_escape():
    assert escape("\\'") == "'"
    assert escape("\\x01") == '\x01'
    assert escape("\\x20") == ' '
    assert escape("\\x7f") == '\x7f'
    assert escape("\\x80") == '\x80'
    assert escape("\\xff") == '\xff'
    assert escape("\\x00") == '\x00'
    assert escape("\\0") == '\0'
    assert escape("\\10") == '\0'
    assert escape("\\11") == '\t'
    assert escape("\\34") == '4'
    assert escape("\\177") == '\177'
    assert escape("\\200") == '\0'


# Generated at 2022-06-13 17:55:43.849816
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:46.538800
# Unit test for function test
def test_test():
    # normal cases
    assert test() == None
    # boundaries
    # exceptions
    # But it can not be tested. It make output.

# Generated at 2022-06-13 17:55:48.544865
# Unit test for function test
def test_test():
    assert chr(39) == "'"
    assert chr(39) == evalString(repr(chr(39)))
    #
    test()

# Generated at 2022-06-13 17:55:55.427807
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", "\\b")) == "\b"
    for i in (0, 128, 256, 512):
        c = chr(i)
        x = hex(i)[2:]
        if len(x) % 2:
            x = "0" + x
        assert escape(re.match(r"\\(.)", "\\x" + x)) == c
        o = oct(i)[1:]
        assert escape(re.match(r"\\(.)", "\\" + o)) == c

# Generated at 2022-06-13 17:56:02.731794
# Unit test for function escape
def test_escape():
    import ast
    import random

    for s in simple_escapes:
        c = simple_escapes[s]
        assert c == escape(ast.Str(s='\\' + s))

    # Test all possible octal escapes, including \\0
    for i in range(512):
        s = '\\%03o' % i
        assert chr(i % 256) == escape(ast.Str(s=s))

    # Test all possible hex escapes
    for i in range(65536):
        s = '\\x%04x' % i
        assert chr(i) == escape(ast.Str(s=s))

    # Test a couple thousand random escapes

# Generated at 2022-06-13 17:56:04.710534
# Unit test for function test
def test_test():
    try:
        test()
    except AssertionError as e:
        print(e)

# Generated at 2022-06-13 17:56:14.474052
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\t")) == "\t"
    assert escape(re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", '\\"')) == '"'
    assert escape(re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\xab")) == "\xab"
    assert escape(re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\141")) == "a"

# Generated at 2022-06-13 17:56:23.861925
# Unit test for function test

# Generated at 2022-06-13 17:56:24.991196
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:25.336244
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:57:28.263589
# Unit test for function test
def test_test():
    try:
        assert test()
    except Exception:
        raise AssertionError("test() didn't work")
    assert True

# Generated at 2022-06-13 17:57:37.690111
# Unit test for function escape
def test_escape():
    tests = [
        (r"\a", "\x07"),
        (r"\b", "\x08"),
        (r"\f", "\x0c"),
        (r"\n", "\n"),
        (r"\r", "\r"),
        (r"\t", "\t"),
        (r"\v", "\x0b"),
        (r"\'", "'"),
        (r'\"', '"'),
        (r"\\", "\\"),
        (r"\xFF", "\xff"),
        (r"\053", "3"),
        (r"\0", "\0"),
    ]

    for t in tests:
        m = re.search(r"\\(.+)", t[0])
        assert m is not None
        assert escape(m) == t[1]

# Generated at 2022-06-13 17:57:39.068459
# Unit test for function escape
def test_escape():
    escape('\\a') == '\a'
    escape('\\b') == '\b'

# Generated at 2022-06-13 17:57:49.330171
# Unit test for function escape
def test_escape():
    # Test non-hex string escape
    m = re.search(r'\\([abfnrtv]|\\|[\'\"])', "\\x")
    assert escape(m) == "x"

    # Test hex string escape
    m = re.search(r'\\x.{0,2}', "\\x41")
    assert escape(m) == "A"

    # Test octal string escape
    m = re.search(r'\\[0-7]{1,3}', "\\101")
    assert escape(m) == "A"

# Generated at 2022-06-13 17:57:52.330841
# Unit test for function test
def test_test():
    try:
        test()
    except Exception as e:
        raise ValueError from e

# Generated at 2022-06-13 17:57:53.059578
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:57:57.298994
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(')", "\\'")) == "\'"
    assert escape(re.match(r"\\(\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\'\"")) == "\'"

# Generated at 2022-06-13 17:58:07.637783
# Unit test for function escape
def test_escape():
    class MSubMock():
        def __init__(self, all, tail):
            self.all = all
            self.tail = tail

        def group(self, n):
            if n == 0:
                return self.all
            elif n == 1:
                return self.tail

    # Test simple_escapes
    for key, value in simple_escapes.items():
        m = MSubMock("\\" + key, key)
        assert escape(m) == value

    # Test x escapes
    m = MSubMock("\\xff", "x")
    assert escape(m) == "\xff"
    m = MSubMock("\\xfe", "xfe")
    assert escape(m) == "\xfe"
    m = MSubMock("\\x1", "x1")
    assert escape

# Generated at 2022-06-13 17:58:08.568281
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:18.816906
# Unit test for function escape
def test_escape():
    assert evalString('"test"') == 'test'
    assert evalString('"test1"') == 'test1'
    assert evalString("'test'") == 'test'
    assert evalString("'test1'") == 'test1'
    assert evalString("'\\x00'") == "\x00"
    assert evalString("'\\x12'") == "\x12"
    assert evalString("'\\xFF'") == "\xFF"
    assert evalString("'\\000'") == "\0"
    assert evalString("'\\077'") == "\077"
    assert evalString("'\\000'") == "\0"
    assert evalString("'\\0'") == "\0"
    assert evalString("'\\n'") == "\n"