

# Generated at 2022-06-13 17:49:52.293940
# Unit test for function test
def test_test():
    test()
    #No exception should be raised

# Generated at 2022-06-13 17:50:01.211201
# Unit test for function evalString
def test_evalString():
    assert evalString("'abc'") == 'abc'
    assert evalString('"abc"') == 'abc'
    assert evalString("'abc'") == 'abc'
    assert evalString("'a\\\\bc'") == 'a\\bc'
    assert evalString("'a\\'bc'") == "a'bc"
    assert evalString('"a\\"bc"') == 'a"bc'
    assert evalString("'a\\\nbc'") == "abc"
    assert evalString("'\\'") == "'"


# TODO: Would be nice to have a string-literal parser, to not just
# depend on re. Find a grammar somewhere.
#
# TODO: If the RE is too slow, try pre-compiling it.

# Generated at 2022-06-13 17:50:03.534502
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", "\\x34")) == "4"
    assert escape(re.match(r"\\(.)", "\\r")) == "\r"



# Generated at 2022-06-13 17:50:15.968900
# Unit test for function evalString
def test_evalString():
        # Simple single quoted strings
        assert evalString("''") == ""
        assert evalString("'a'") == "a"
        assert evalString("'\\''") == "'"
        assert evalString("'\\a'") == "\a"
        assert evalString("'\\b'") == "\b"
        assert evalString("'\\f'") == "\f"
        assert evalString("'\\n'") == "\n"
        assert evalString("'\\r'") == "\r"
        assert evalString("'\\t'") == "\t"
        assert evalString("'\\v'") == "\v"
        assert evalString("'\\x61'") == "a"

        # Simple double quoted strings
        assert evalString('""') == ""
        assert evalString('"a"') == "a"
        assert eval

# Generated at 2022-06-13 17:50:19.658622
# Unit test for function evalString
def test_evalString():
    assert evalString('"\\\\"') == "\\"
    assert evalString(r"\'\"\'") == '"\''
    assert evalString(r"\xAd") == chr(0xad)
    assert evalString(r"\342\200\235") == chr(0x2035)
    assert evalString('"\n\n"') == "\n\n"
    assert evalString('"\x41\x42"') == "AB"
    assert evalString(r"'\n\n'") == "\n\n"
    assert evalString(r"'\x41\x42'") == "AB"

# Generated at 2022-06-13 17:50:25.688096
# Unit test for function evalString
def test_evalString():
    assert evalString("''") == ""
    assert evalString('""') == ""
    assert evalString("'1'") == "1"
    assert evalString('"1"') == "1"
    assert evalString("'0x1'") == "0x1"
    assert evalString('"0x1"') == "0x1"
    assert evalString("'0xa'") == "0xa"
    assert evalString('"0xa"') == "0xa"
    assert evalString("'\\n'") == "\n"
    assert evalString('"\\n"') == "\n"
    assert evalString("'\\t'") == "\t"
    assert evalString('"\\t"') == "\t"
    assert evalString("'\\\\'") == "\\"
    assert evalString('"\\\\"')

# Generated at 2022-06-13 17:50:33.989804
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x12")) == chr(0x12)
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\5")) == chr(5)
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\v")) == chr(11)

# Generated at 2022-06-13 17:50:42.922905
# Unit test for function escape
def test_escape():
    m = re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\a")
    assert m.group(1) == "a"
    assert escape(m) == "\x07"

    m = re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x01")
    assert m.group(1) == "x01"
    assert escape(m) == "\x01"

    m = re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x41")

# Generated at 2022-06-13 17:50:54.217728
# Unit test for function escape
def test_escape():
    class T:
        def __init__(self, exp, val):
            self.exp = exp
            self.val = val


# Generated at 2022-06-13 17:51:02.942580
# Unit test for function escape
def test_escape():
    assert escape("\\a") == "\a"
    assert escape("\\b") == "\b"
    assert escape("\\f") == "\f"
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("\\'") == "'"
    assert escape('\\"') == '"'
    assert escape("\\\\") == "\\"

    assert escape("\\x0a") == "\n"
    assert escape("\\010") == "\b"
    assert escape("\\101") == "A"
    assert escape("\\x41") == "A"

    assert escape("\\x0a") == "\n"
    assert escape("\\x01") == "\x01"
    assert escape

# Generated at 2022-06-13 17:51:27.095566
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:51:27.705494
# Unit test for function escape
def test_escape():
    pass

# Generated at 2022-06-13 17:51:36.190124
# Unit test for function evalString
def test_evalString():
    # The output from function evalString should be the same as the input,
    # but without the enclosing quotes and with any escaped characters
    # (like \\n for newline) converted to the actual character.

    # See also test_backquote which is intended to be a more exhaustive test,
    # but which currently doesn't test the full range of escape characters
    # or the effects of surrounding white space.

    # Single character tests
    assert evalString("'a'") == "a"
    assert evalString('"a"') == "a"
    assert evalString("'\\x61'") == "a"

    # Multiple character tests
    assert evalString("'ab'") == "ab"
    assert evalString('"ab"') == "ab"
    assert evalString("'\\x61\\x62'") == "ab"

    # New

# Generated at 2022-06-13 17:51:43.831058
# Unit test for function escape
def test_escape():
    # easy cases
    assert escape(re.match("\\a", r"\a")) == "\a"
    assert escape(re.match("\\'", r"\'")) == "'"
    assert escape(re.match("\\x41", r"\x41")) == "A"
    # hex escapes are case-insensitive
    assert escape(re.match("\\x41", r"\x41")) == "A"
    assert escape(re.match("\\x41", r"\x41")) == "A"
    # invalid hex escapes are rejected with ValueError
    try:
        escape(re.match("\\x1", r"\x1"))
    except ValueError as e:
        pass
    else:
        assert False, "ValueError not raised"

# Generated at 2022-06-13 17:51:54.804412
# Unit test for function escape
def test_escape():
    def check_escape(esc, expected):
        assert escape(re.search(r"\\(%s)"%esc, "test")) == expected

    check_escape("a", "\a")
    check_escape("b", "\b")
    check_escape("f", "\f")
    check_escape("n", "\n")
    check_escape("r", "\r")
    check_escape("t", "\t")
    check_escape("v", "\v")
    check_escape("'", "'")
    check_escape('"', '"')
    check_escape('\\', "\\")
    check_escape("x00", "\x00")
    check_escape("x7F", "\x7F")
    check_escape("xFF", "\xFF")
    check_escape("x0000", "\x00")
   

# Generated at 2022-06-13 17:52:05.720449
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", "\\a")) == '\a'
    assert escape(re.match(r"\\(.)", "\\b")) == '\x08'
    assert escape(re.match(r"\\(.)", "\\f")) == '\x0c'
    assert escape(re.match(r"\\(.)", "\\n")) == '\n'
    assert escape(re.match(r"\\(.)", "\\r")) == '\r'
    assert escape(re.match(r"\\(.)", "\\t")) == '\t'
    assert escape(re.match(r"\\(.)", "\\v")) == '\x0b'
    assert escape(re.match(r"\\(.)", r"\\'")) == "'"
    assert escape

# Generated at 2022-06-13 17:52:09.039566
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\x41', '\\x41')) == "A"
    assert escape(re.match(r"\\x41", "\x41")) == "A"

# Unit tests for function evalString

# Generated at 2022-06-13 17:52:13.774605
# Unit test for function escape
def test_escape():
    """Testcase for function escape"""
    assert escape(re.search(r'\n', '\n')) == '\n'
    assert escape(re.search(r'x08', 'x08')) == '\x08'
    assert escape(re.search(r'/', '/')) == '/'
    assert escape(re.search(r'\n', '\n')) == '\n'

# Generated at 2022-06-13 17:52:23.789881
# Unit test for function evalString
def test_evalString():
    assert evalString('"abc"') == "abc"

# Generated at 2022-06-13 17:52:33.424532
# Unit test for function evalString
def test_evalString():
    assert evalString('""') == ""
    assert evalString('"ab"') == 'ab'
    assert evalString('"\\n"') == '\n'
    assert evalString('"\\xff"') == '\xff'
    assert evalString('"\\u1234"') == '\u1234'
    assert evalString('"\\U00010111"') == '\U00010111'
    assert evalString('"\\000"') == '\000'
    assert evalString('"\\00"') == '\00'
    assert evalString('"\\0"') == '\0'
    assert evalString('"\\11"') == '\11'
    assert evalString('"\\011"') == '\011'
    assert evalString('"\\111"') == '\111'

# Generated at 2022-06-13 17:52:46.088728
# Unit test for function test
def test_test():
    import unittest
    class TestTest(unittest.TestCase):
        def test_it(self):
            def testit_helper():
                test()
            self.assertRaises(AssertionError, testit_helper)
    unittest.main()

# Generated at 2022-06-13 17:52:55.337631
# Unit test for function evalString
def test_evalString():
    assert evalString("'\\x01'") == "\x01"
    assert evalString("'\\01'") == "\x01"
    assert evalString("'\\001'") == "\001"
    assert evalString("'\\\n'") == "\x01"
    assert evalString("'\\\r\n'") == "\x01"
    assert evalString("'\\\r\n\r'") == "\x01"
    assert evalString("'\\\r\r\r'") == "\r\r\r"
    assert evalString("'\\\n'") == "\n"
    assert evalString("'\\\n\n'") == "\n\n"
    assert evalString("'\n'") == "\n"
    assert evalString("'\\xabcd'") == "\xab"
   

# Generated at 2022-06-13 17:53:02.043766
# Unit test for function escape
def test_escape():
    # test lowercase hex formatting
    assert escape(re.match('\\x40', '\\x40')) == '@'

    # test uppercase hex formating
    assert escape(re.match('\\x40', '\\x40')) == '@'

    # test octal formatting
    assert escape(re.match('\\040', '\\040')) == ' '

    # test single character formatting
    assert escape(re.match('\\a', '\\a')) == '\x07'

    # test string character formatting
    assert escape(re.match('\\"', '\\"')) == '"'

    # test group character formatting
    assert escape(re.match("\\'", "\\'")) == "'"

    # test backslash character formatting

# Generated at 2022-06-13 17:53:11.075402
# Unit test for function escape
def test_escape():
    from unittest import TestCase

    class TestEvalString(TestCase):
        def test_escape(self):
            for key in simple_escapes:
                self.assertEqual(simple_escapes[key], evalString(repr(simple_escapes[key])))
            try:
                escape(re.match(r'\s', '\\s'))
            except ValueError:
                pass
            else:
                self.fail()
            self.assertEqual('\x01', escape(re.match(r'\\x01', '\\x01')))
            self.assertEqual('\x01', escape(re.match(r'\\x01', '\\x011')))
            self.assertEqual('\x01', escape(re.match(r'\\x01', '\\x01a')))

# Generated at 2022-06-13 17:53:17.146341
# Unit test for function escape
def test_escape():
    assert escape("\\n") == "\n"
    assert escape("\\n") != "\\n"
    assert escape("\\x44") == "D"
    assert escape("\\x44") != "x44"
    assert escape("\\0") == "\0"
    assert escape("\\0") != "\\0"


# Generated at 2022-06-13 17:53:27.480434
# Unit test for function escape
def test_escape():
    assert escape(re.search('\\a', '\a')) == '\a'
    assert escape(re.search('\\b', '\b')) == '\b'
    assert escape(re.search('\\f', '\f')) == '\f'
    assert escape(re.search('\\n', '\n')) == '\n'
    assert escape(re.search('\\r', '\r')) == '\r'
    assert escape(re.search('\\t', '\t')) == '\t'
    assert escape(re.search('\\v', '\v')) == '\v'
    assert escape(re.search('\\\\', '\\')) == '\\'
    assert escape(re.search('\\\'', "'")) == "'"

# Generated at 2022-06-13 17:53:32.088212
# Unit test for function escape
def test_escape():
    def test_esc(s):
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", s)
        assert m is not None, repr(s)
        return escape(m)

    assert test_esc("\\'") == "'"
    assert test_esc("\\x0a") == "\n"
    assert test_esc("\\07") == "\a"

# Generated at 2022-06-13 17:53:32.389945
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:39.573394
# Unit test for function escape
def test_escape():
    # Test the different escape sequences
    assert escape("\\n") == "\n"
    assert escape("\\a") == "\a"
    assert escape("\\b") == "\b"
    assert escape("\\f") == "\f"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("\\'") == "'"
    assert escape('\\"') == '"'
    assert escape("\\\\") == "\\"

    # Test invalid escape characters
    try:
        escape("\\z")
    except ValueError:
        pass
    else:
        assert False

    # Test octal escape sequences
    assert escape(r"\0") == "\x00"
    assert escape(r"\07") == "\x07"
   

# Generated at 2022-06-13 17:53:48.296290
# Unit test for function escape
def test_escape():
    cases = {
        "\\\\": "\\",
        '\\"': '"',
        "\\'": "'",
        '\\a': "\a",
        '\\b': "\b",
        '\\f': "\f",
        '\\n': "\n",
        '\\r': "\r",
        '\\t': "\t",
        '\\v': "\v",
        "\\x7F": "\x7f",
        "\\160": "\x80",
    }
    for s, c in cases.items():
        assert escape(re.match(r"\\.*", s)) == c

            # Unit test for function evalString



# Generated at 2022-06-13 17:54:08.811750
# Unit test for function test
def test_test():
    import bdb
    import pdb
    import pickle
    import sys

    try:
        import trace
    except ImportError:
        pass

    try:
        import linecache
    except ImportError:
        pass

    try:
        import idlelib.pydoc
    except ImportError:
        pass

    class MyTest(object):
        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return "MyTest(%r)" % self.x

    class MyBadTest(object):
        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return "MyBadTest(%r" % self.x  # note missing trailing ')'


# Generated at 2022-06-13 17:54:16.270678
# Unit test for function escape
def test_escape():
    m = re.match(r"\\(.)", "\\a")
    assert m
    assert escape(m) == '\a'

    m = re.match(r"\\(.)", '\\b')
    assert m
    assert escape(m) == '\b'

    m = re.match(r"\\(.)", '\\f')
    assert m
    assert escape(m) == '\f'

    m = re.match(r"\\(.)", '\\n')
    assert m
    assert escape(m) == '\n'

    m = re.match(r"\\(.)", '\\r')
    assert m
    assert escape(m) == '\r'

    m = re.match(r"\\(.)", '\\t')
    assert m

# Generated at 2022-06-13 17:54:19.204573
# Unit test for function escape
def test_escape():
    assert escape("\\n") == "\n"
    assert escape("\\x41") == "A"
    assert escape("\\x4") == "4"
    assert escape("\\420") == "("
    assert escape("\\0420") == "("

# Generated at 2022-06-13 17:54:23.108122
# Unit test for function evalString
def test_evalString():

    string = '"a\\\\\'"'

    assert evalString(string) == 'a\\\'', "Failed to eval a string"

    string = '"\\\\\'"'

    assert evalString(string) == '\\\'', "Failed to eval a string"

# Generated at 2022-06-13 17:54:33.194495
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\a', '\\a')) == escape(re.match('\\a', '\\a'))
    assert escape(re.match('\\x', '\\x')) == escape(re.match('\\x', '\\x'))
    assert escape(re.match('\\b', '\\b')) == escape(re.match('\\b', '\\b'))
    assert escape(re.match('\\x', '\\x')) == escape(re.match('\\x', '\\x'))
    assert escape(re.match('\\f', '\\f')) == escape(re.match('\\f', '\\f'))
    assert escape(re.match('\\x', '\\x')) == escape(re.match('\\x', '\\x'))

# Generated at 2022-06-13 17:54:43.471934
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\a', r'\a')) == '\a'
    assert escape(re.match('\\b', r'\b')) == '\b'
    assert escape(re.match('\\f', r'\f')) == '\f'
    assert escape(re.match('\\n', r'\n')) == '\n'
    assert escape(re.match('\\r', r'\r')) == '\r'
    assert escape(re.match('\\t', r'\t')) == '\t'
    assert escape(re.match('\\v', r'\v')) == '\v'
    assert escape(re.match('\\\'', r"\'")) == '\''

# Generated at 2022-06-13 17:54:44.503090
# Unit test for function test
def test_test():
    test()



# Generated at 2022-06-13 17:54:50.331567
# Unit test for function escape
def test_escape():
    '''
    >>> escape(re.match('\\\\', '\\'))
    '\\\\'
    >>> escape(re.match('\\\\xAF', '\\xAF'))
    '\xaf'
    >>> escape(re.match('\\\\AF', '\\AF'))
    Traceback (most recent call last):
      ...
    ValueError: invalid octal string escape ('\\AF')
    '''
    pass


# Generated at 2022-06-13 17:54:57.430476
# Unit test for function escape
def test_escape():
    testcases = [
        ("\\x1A", "\\x1A"),
        ("\\x1Aa", "\x1A"),
        ("\\x1Aaa", "\x1A"),
        ("\\x1Aaaa", "\x1A"),
        ("\\x1Aaag", "\\x1A"),
        ("\\x1Aag", "\\x1A"),
        ("\\x1AAg", "\\x1A"),
        ("\\xAAg", "\\xAA"),
    ]
    for tcase in testcases:
        actual = escape(tcase[0])
        expected = tcase[1]
        assert actual == expected, f"For testcase {tcase[0]}, got {actual} instead of {expected}"

# Generated at 2022-06-13 17:55:08.396612
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\a", "\\a")) == "\a"
    assert escape(re.match("\\b", "\\b")) == "\b"
    assert escape(re.match("\\f", "\\f")) == "\f"
    assert escape(re.match("\\n", "\\n")) == "\n"
    assert escape(re.match("\\r", "\\r")) == "\r"
    assert escape(re.match("\\t", "\\t")) == "\t"
    assert escape(re.match("\\v", "\\v")) == "\v"
    assert escape(re.match("\\'", "\\'")) == "'"
    assert escape(re.match('\\"', '\\"')) == '"'
    assert escape(re.match("\\\\", "\\\\")) == "\\"
    assert escape

# Generated at 2022-06-13 17:55:46.511822
# Unit test for function escape
def test_escape():
    m = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\n")
    assert escape(m) == "n"


# Generated at 2022-06-13 17:56:00.601790
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\.', r"\'")) == "'"
    assert escape(re.match(r'\\.', r'\"')) == '"'
    assert escape(re.match(r'\\.', r"\\")) == "\\"
    assert escape(re.match(r'\\.', r"\a")) == "\a"
    assert escape(re.match(r'\\.', r"\b")) == "\b"
    assert escape(re.match(r'\\.', r"\f")) == "\f"
    assert escape(re.match(r'\\.', r"\n")) == "\n"
    assert escape(re.match(r'\\.', r"\r")) == "\r"
    assert escape(re.match(r'\\.', r"\t"))

# Generated at 2022-06-13 17:56:12.701733
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", r"\a")) == "\a"
    assert escape(re.match(r"\\(.)", r"\b")) == "\b"
    assert escape(re.match(r"\\(.)", r"\f")) == "\f"
    assert escape(re.match(r"\\(.)", r"\n")) == "\n"
    assert escape(re.match(r"\\(.)", r"\r")) == "\r"
    assert escape(re.match(r"\\(.)", r"\t")) == "\t"
    assert escape(re.match(r"\\(.)", r"\v")) == "\v"
    assert escape(re.match(r"\\(.)", r"\'")) == "'"

# Generated at 2022-06-13 17:56:13.045575
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:22.250351
# Unit test for function escape
def test_escape():
    r = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\'")
    assert r is not None
    e = escape(r)
    assert e == "'"
    r = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\\"")
    assert r is not None
    e = escape(r)
    assert e == "\""
    r = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\b")
    assert r is not None

# Generated at 2022-06-13 17:56:23.102135
# Unit test for function escape
def test_escape():
    assert escape("\\x26") == "&"

# Generated at 2022-06-13 17:56:28.734574
# Unit test for function test
def test_test():
    import subprocess
    import sys
    import tempfile
    with tempfile.TemporaryFile("w+") as stdout:
        with open(sys.argv[0]) as fp:
            code = fp.read()
        print(code, file=stdout)
        stdout.flush()
        stdout.seek(0)
        proc = subprocess.Popen([sys.executable, "-m", "doctest", "-v"], stdin=stdout)
        out, err = proc.communicate()
        if proc.returncode:
            raise AssertionError(err)

# Generated at 2022-06-13 17:56:34.543072
# Unit test for function evalString
def test_evalString():
    test_string = "\"test\""
    test_string2 = "'''test'''"
    test_string3 = '"\"test\""'

    s = evalString(test_string)
    assert s == "test"
    s = evalString(test_string2)
    assert s == "test"
    s = evalString(test_string3)
    assert s == '"test"'

# Generated at 2022-06-13 17:56:43.639852
# Unit test for function escape
def test_escape():
    # Test simple escapes
    assert escape(re.match(r"\\(a)", r"\a")) == "\a"
    assert escape(re.match(r"\\(b)", r"\b")) == "\b"
    assert escape(re.match(r"\\(f)", r"\f")) == "\f"
    assert escape(re.match(r"\\(n)", r"\n")) == "\n"
    assert escape(re.match(r"\\(r)", r"\r")) == "\r"
    assert escape(re.match(r"\\(t)", r"\t")) == "\t"
    assert escape(re.match(r"\\(v)", r"\v")) == "\v"
    assert escape(re.match(r"\\(')", r"\'")) == "'"
    assert escape

# Generated at 2022-06-13 17:56:46.115327
# Unit test for function escape
def test_escape():
    assert escape("\\x0A") == "\n"
    assert escape("\\b") == "\b"
    assert escape("\\t") == "\t"

# Generated at 2022-06-13 17:57:17.899029
# Unit test for function escape
def test_escape():
    from .depythonify import depythonify

    escape_testcases = [('\\a', '\a'),
                        ('\\e', 'e'),
                        ('\\xFF', '\xff'),
                        ('\\377', '\377'),
                        ('\\xFEF', 'xFEF'),
                        ('\\1234', '\1234'),
                        ('\\01234', '\01234')]

    for inp, exp in escape_testcases:
        res = depythonify.escape(re.match(r"\\(.)", inp))
        assert res == exp

# Generated at 2022-06-13 17:57:19.369742
# Unit test for function test
def test_test():
    val = test()
    assert val is None

# Example of unit test for escape

# Generated at 2022-06-13 17:57:34.424722
# Unit test for function escape
def test_escape():
    from test.support import run_unittest
    from unittest import TestCase

    class EscapeTestCase(TestCase):
        def test_escape(self):
            data = [
                # (Input, Output)
                ("\\x7F", "\\x7F"),
                ("\\x7f", "\u007f"),
                ("\\x00", "\x00"),
                ("\\n", "\n"),
                ("\\r", "\r"),
                ("\\v", "\u000b"),
                ("\\b", "\b"),
                ("\\a", "\a"),
                ("\\t", "\t"),
                ("\\f", "\f"),
                ('\\"', '"'),
                ("\\'", "'"),
                ("\\\\", "\\"),
            ]
            for d in data:
                input = d[0]


# Generated at 2022-06-13 17:57:42.299289
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(a)", '\\a')) == '\a'
    assert escape(re.match(r"\\(b)", '\\b')) == '\b'
    assert escape(re.match(r"\\(f)", '\\f')) == '\f'
    assert escape(re.match(r"\\(n)", '\\n')) == '\n'
    assert escape(re.match(r"\\(r)", '\\r')) == '\r'
    assert escape(re.match(r"\\(t)", '\\t')) == '\t'
    assert escape(re.match(r"\\(v)", '\\v')) == '\v'
    assert escape(re.match(r"\\(x00)", '\\x00')) == chr

# Generated at 2022-06-13 17:57:50.670722
# Unit test for function escape

# Generated at 2022-06-13 17:57:54.311678
# Unit test for function test
def test_test():
    # test.test()
    assert len("") == 0
    assert len("") == 0
    assert len("") == 0
    assert len("") == 0
    assert len("") == 0

# Generated at 2022-06-13 17:58:02.949420
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\x(\d+)", "\\x00")) == "\x00"
    assert escape(re.search(r"\\x(\d+)", "\\xFF")) == "\xFF"
    assert escape(re.search(r"\\x(\d+)", "\\xE7")) == "\xE7"
    assert escape(re.search(r"\\x(\d+)", "\\xE7")) == "\xE7"
    assert escape(re.search(r"\\x(\d+)", "\\xE7")) == "\xE7"
    assert escape(re.search(r"\\x(\d+)", "\\x0F")) == "\x0F"
    assert escape(re.search(r"\\x(\d+)", "\\x00")) == "\x00"

# Generated at 2022-06-13 17:58:08.398480
# Unit test for function test
def test_test():
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        test()
        assert sys.stdout.getvalue() == ""
    finally:
        sys.stdout = old_stdout



# Generated at 2022-06-13 17:58:08.875615
# Unit test for function test
def test_test():
    assert test() == None

# Generated at 2022-06-13 17:58:18.137038
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\x', "\\x")) == ""
    assert escape(re.match(r'\\x','\\x23')) == "#"
    assert escape(re.match(r'\\x','\\x1A')) == "\x1A"
    assert escape(re.match(r'\\x','\\xAA')) == "\xAA"
    assert escape(re.match(r'\\3','\\3')) == "3"
    assert escape(re.match(r'\\0','\\03')) == "\x03"
    with pytest.raises(ValueError):
        escape(re.match(r'\\x','\\x3'))
        escape(re.match(r'\\x','\\xA'))

# Generated at 2022-06-13 17:59:24.086312
# Unit test for function escape
def test_escape():
    # Test escape() function behaves as expected
    assert escape(re.match('\\"', r'\"')) == '"'
    assert escape(re.match('\\a', r'\a')) == '\a'
    assert escape(re.match('\\b', r'\b')) == '\b'
    assert escape(re.match('\\f', r'\f')) == '\f'
    assert escape(re.match('\\n', r'\n')) == '\n'
    assert escape(re.match('\\r', r'\r')) == '\r'
    assert escape(re.match('\\t', r'\t')) == '\t'
    assert escape(re.match('\\v', r'\v')) == '\v'

# Generated at 2022-06-13 17:59:26.160370
# Unit test for function test
def test_test():
    try:
        test()
    except:
        assert False, 'test_test failed'
    assert True



# Generated at 2022-06-13 17:59:26.703928
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:59:33.940433
# Unit test for function escape
def test_escape():
    global escape

    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\v'
    assert escape('\\\'') == '\''
    assert escape('\\\"') == '"'
    assert escape('\\\\') == '\\'
    assert escape('\\x41') == 'A'
    assert escape('\\x42') == 'B'
    assert escape('\\x43') == 'C'
    assert escape('\\x44') == 'D'
    assert escape('\\x45') == 'E'