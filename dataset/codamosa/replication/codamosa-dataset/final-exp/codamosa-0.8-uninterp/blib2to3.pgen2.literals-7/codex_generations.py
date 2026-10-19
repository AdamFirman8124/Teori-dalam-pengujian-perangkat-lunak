

# Generated at 2022-06-13 17:49:59.751657
# Unit test for function escape
def test_escape():
    for key, value in simple_escapes.items():
        m = re.match(r"\\(a|b|f|n|r|t|v|'|\"|\\)", "\\" + key)
        assert escape(m) == value

# Generated at 2022-06-13 17:50:07.485433
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\a", "\\a")) == "\a"
    assert escape(re.match(r"\b", "\\b")) == "\b"
    assert escape(re.match(r"\f", "\\f")) == "\f"
    assert escape(re.match(r"\n", "\\n")) == "\n"
    assert escape(re.match(r"\r", "\\r")) == "\r"
    assert escape(re.match(r"\t", "\\t")) == "\t"
    assert escape(re.match(r"\v", "\\v")) == "\v"
    assert escape(re.match(r"\'", "\\'")) == "'"
    assert escape(re.match(r'\"', '\\"')) == '"'

# Generated at 2022-06-13 17:50:15.600527
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\x08", "\\x08")) == "\x08"
    assert escape(re.search(r"\\[\\'\"]", "\\'")) == "'"

    # raise exception for invalid escape sequence
    try:
        escape(re.search(r"\\[\\'\"]", "\\x"))
    except ValueError:
        pass
    try:
        escape(re.search(r"\\[\\'\"]", "\\08"))
    except ValueError:
        pass

# Generated at 2022-06-13 17:50:19.351081
# Unit test for function escape
def test_escape():
    m = '\\xab'
    assert escape(m) == '\xab'
    m = '\\n'
    assert escape(m) == '\n'
    m = '\\t'
    assert escape(m) == '\t'
    m = '\\x'
    try:
        escape(m)
    except ValueError:
        pass
    else:
        assert False



# Generated at 2022-06-13 17:50:29.619611
# Unit test for function escape
def test_escape():
    import re
    assert re.sub(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", escape, "\\a") == "\a"
    assert re.sub(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", escape, "\\\t") == "\t"
    assert re.sub(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", escape, "\\x1f") == "\x1f"

# Generated at 2022-06-13 17:50:41.143312
# Unit test for function escape
def test_escape():
    import ast
    import doctest
    import textwrap
    import unittest
    import warnings

    class EscapeTestCase(unittest.TestCase):
        def runTest(self):
            # Check that a SyntaxError is raised when
            # <string> is invalid.
            warnings.filterwarnings("error", module="literal_eval")

# Generated at 2022-06-13 17:50:41.676490
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:50:47.468786
# Unit test for function evalString
def test_evalString():
    tests = [
        ["'abc'", "abc"],
        ["'abc\\xFF'", "abc\xff"],
        ["'abc\\377'", "abc\xff"],
        ["u'abc'", "abc"],
        ["u'abc\\xFF'", "abc\xff"],
        ["u'abc\\377'", "abc\xff"],
        ["'abc\\n'", "abc\n"],
        ["r'abc\\n'", "abc\\n"],
    ]
    for test_tuple in tests:
        assert evalString(test_tuple[0]) == test_tuple[1]

# Generated at 2022-06-13 17:50:57.680506
# Unit test for function escape
def test_escape():
    assert evalString("'\\x41'") == "A"
    assert evalString("'\\141'") == "a"
    assert evalString("'\\''") == "'"

# Generated at 2022-06-13 17:51:05.948313
# Unit test for function escape
def test_escape():
    m = re.match(r'\\([abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\b')
    assert escape(m) == "\b"
    m = re.match(r'\\([abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\x311')
    assert escape(m) == "\x311"
    m = re.match(r'\\([abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\07')
    assert escape(m) == "\x07"



# Generated at 2022-06-13 17:51:24.922143
# Unit test for function escape
def test_escape():
    import sys
    import unittest

    class EscapeTests(unittest.TestCase):
        # simple_escapes
        def test_escape_a(self):
            result = repr(escape(re.match("\\a", "\\a")))
            self.assertEqual(result, "'\\x07'")
        def test_escape_b(self):
            result = repr(escape(re.match("\\b", "\\b")))
            self.assertEqual(result, "'\\x08'")
        def test_escape_f(self):
            result = repr(escape(re.match("\\f", "\\f")))
            self.assertEqual(result, "'\\x0c'")

# Generated at 2022-06-13 17:51:28.844374
# Unit test for function escape
def test_escape():
    for i in range(0o100, 0o400):
        assert escape(re.match(r"\\" + oct(i)[2:], '\\' + oct(i)[2:])) == chr(i)



# Generated at 2022-06-13 17:51:36.672065
# Unit test for function escape
def test_escape():
    # \x -> x
    esc = escape(re.match(r'\\x', '\\x'))
    assert esc == 'x', "Expected 'x', got '%s'" % esc

    # \x4 -> x4
    esc = escape(re.match(r'\\x4', '\\x4'))
    assert esc == 'x4', "Expected 'x4', got '%s'" % esc

    # \x4a -> x4a
    esc = escape(re.match(r'\\x4a', '\\x4a'))
    assert esc == 'x4a', "Expected 'x4a', got '%s'" % esc

    # \\x4 -> \x4

# Generated at 2022-06-13 17:51:43.923250
# Unit test for function evalString

# Generated at 2022-06-13 17:51:45.127347
# Unit test for function test
def test_test():
    result = evalString("'\n'")
    assert result == '\n'

# Generated at 2022-06-13 17:51:47.049813
# Unit test for function evalString
def test_evalString():
    assert evalString('"\x61"') == 'a'
    assert evalString('"\u0061"') == 'a'

# Generated at 2022-06-13 17:51:50.969921
# Unit test for function evalString
def test_evalString():
    for s, r in [
        (r'"\r\n"', r"\r\n"),
        (r"r'\r\n'", r"\r\n"),
        (r"u'\u20ac'", "€"),
        (r'u"\u20ac"', "€"),
    ]:
        assert evalString(s) == r

# Generated at 2022-06-13 17:51:54.920566
# Unit test for function test
def test_test():
    import sys
    from io import StringIO

    save_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        test()
    finally:
        sys.stdout = save_stdout
    assert sys.stdout.getvalue() == ""

# Generated at 2022-06-13 17:52:05.720445
# Unit test for function evalString
def test_evalString():
    from ast_compat import parse
    with open(__file__, 'r') as file:
        txt = file.read()
    module = parse(txt, __file__)
    body = module.body
    func_def = body[len(body) - 2]
    func_body = func_def.body
    assert func_body[0].value.s == "assert s.startswith('\'') or s.startswith('\"'), repr(s[:1])"
    assert func_body[1].value.s == "q = s[0]"
    assert func_body[2].value.s == "if s[:3] == q * 3:"
    assert func_body[3].value.s == "q = q * 3"

# Generated at 2022-06-13 17:52:14.892269
# Unit test for function evalString
def test_evalString():

    # Assert: Empty string evaluated becomes empty string
    assert evalString('') == ''

    # Assert: Empty quotes evaluates to empty string
    assert evalString('""') == ''

    # Assert: Empty single quotes evaluates to empty string
    assert evalString("''") == ''

    # Assert: 'e' evaluates to 'e'
    assert evalString("'e'") == 'e'

    # Assert: '\n' evaluates to '\n'
    assert evalString("'\n'") == '\n'

    # Assert: '\\n' evaluates to '\\n'
    assert evalString("'\\\\n'") == '\\n'

    # Assert: '\t' evaluates to '\t'
    assert evalString("'\t'") == '\t'

    # Assert: '\\t

# Generated at 2022-06-13 17:52:41.127369
# Unit test for function escape
def test_escape():
    assert escape("\\'") == "'"
    assert escape("\\\\") == "\\"
    assert escape("\\\"") == "\""
    assert escape("\\a") == "\a"
    assert escape("\\b") == "\b"
    assert escape("\\f") == "\f"
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("\\x12") == "\x12"
    assert escape("\\02") == "\x02"
    assert escape("\\012") == "\n"
    assert escape("\\12") == "\x0a"
    assert escape("\\1234") == "\x34"
    assert escape("\\123") == "\x1a"


# Generated at 2022-06-13 17:52:52.492295
# Unit test for function evalString
def test_evalString():
    from . import test_support
    from .test_support import check_re_sub

    for i in range(256):
        s = chr(i)
        assert evalString('"' + s + '"') == s
    for i in range(256):
        s = chr(i)
        assert evalString("'" + s + "'") == s
    for i in range(256):
        s = chr(i)
        assert evalString("u'" + s + "'") == s
    for i in range(256):
        s = chr(i)
        assert evalString("ur'" + s + "'") == s
    assert evalString("u'abc'") == "abc"
    assert evalString("ur'abc'") == "abc"
    assert evalString("u'\\xf1'") == "\xf1"

# Generated at 2022-06-13 17:53:03.664824
# Unit test for function escape
def test_escape():
    m = re.search('(\\\w)', '\\x')
    assert escape(m) == 'x'
    m = re.search('(\\\w)', '\\a')
    assert escape(m) == '\a'
    m = re.search('(\\\w)', '\\r')
    assert escape(m) == '\r'
    m = re.search('(\\\w)', '\\t')
    assert escape(m) == '\t'
    m = re.search('(\\\w)', '\\f')
    assert escape(m) == '\f'
    m = re.search('(\\\w)', '\\b')
    assert escape(m) == '\b'
    m = re.search('(\\\w)', '\\v')

# Generated at 2022-06-13 17:53:12.449400
# Unit test for function evalString
def test_evalString():
    def check(s, result):
        assert evalString(s) == result
    # Test simple cases
    check('"a"', 'a')
    check('"ab"', 'ab')
    check('"abc"', 'abc')
    check('""', '')
    # Test escaping
    check('"\\a\\b\\f\\n\\r\\t\\v"', "\a\b\f\n\r\t\v")
    check('"\\"\\\'\\\\"', '"\'\\')
    # Test octal escaping
    check('"\\0"', "\0")
    check('"\\01"', "\01")
    check('"\\012"', "\012")
    check('"\\0123"', "\0123")
    # Test hex escaping

# Generated at 2022-06-13 17:53:21.593178
# Unit test for function evalString
def test_evalString():
    # Test a string with no escape characters
    assert evalString('"This string has no escapes"') == "This string has no escapes"
    # Test a string containing all types of escape characters

# Generated at 2022-06-13 17:53:26.341350
# Unit test for function evalString
def test_evalString():
    assert evalString("'a\\nb'") == "a\nb"
    assert evalString("'a\\x61\\nb'") == "aab\nb"
    assert evalString("'a\\161\\nb'") == "aab\nb"
    assert evalString("'a\\061\\nb'") == "aab\nb"

# Generated at 2022-06-13 17:53:35.742223
# Unit test for function escape
def test_escape():
    examples =({'\a':
                r"\a",
                '\b':
                r"\b",
                '\f':
                r"\f",
                '\n':
                r"\n",
                '\r':
                r"\r",
                '\t':
                r"\t",
                '\v':
                r"\v",
                '\'':
                r"\'",
                '\"':
                r'\"',
                '\\':
                r"\\",
                r"\x9c":
                r"\x9c"
                })
    for k, v in examples.items():
        m = re.match(r"\\(.+)", v)
        assert escape(m) == k


# Generated at 2022-06-13 17:53:46.200603
# Unit test for function escape
def test_escape():
    import re

    escaped_chars = {
        r"\a": "ab",
        r"\b": "cd",
        r"\f": "ef",
        r"\n": "gh",
        r"\r": "ij",
        r"\t": "kl",
        r"\v": "mn",
        r"\'": "op",
        r'\"': "qr",
        r"\\": "st",
        r"\x20": "uv",
        r"\x2b": "wx",
        r"\077": "yz",
        r"\x": "ab",
        r"\x2": "cd",
        r"\77": "ef",
    }


# Generated at 2022-06-13 17:53:46.919879
# Unit test for function evalString
def test_evalString():
    assert evalString('"a"') == "a"

# Generated at 2022-06-13 17:53:50.288123
# Unit test for function evalString
def test_evalString():
    assert evalString('"\x71\x75\x6f\x74\x65\x20\x74\x65\x73\x74"') == 'quote test'

# Generated at 2022-06-13 17:55:48.276313
# Unit test for function escape

# Generated at 2022-06-13 17:55:57.841965
# Unit test for function escape
def test_escape():
    # Replace escaped chars
    assert escape(re.match(r"\\v", r"\v")) == "\v"
    assert escape(re.match(r"\\a", r"\a")) == "\a"
    assert escape(re.match(r"\\b", r"\b")) == "\b"
    assert escape(re.match(r"\\f", r"\f")) == "\f"
    assert escape(re.match(r"\\n", r"\n")) == "\n"
    assert escape(re.match(r"\\t", r"\t")) == "\t"
    assert escape(re.match(r"\\\\", r"\\")) == "\\"
    assert escape(re.match(r"\\\"", r"\"")) == '"'

# Generated at 2022-06-13 17:55:58.855117
# Unit test for function test
def test_test():
    """Pass"""

# Generated at 2022-06-13 17:56:03.623177
# Unit test for function escape
def test_escape():
    # 'escape' does not modify its argument if it's not a string
    assert escape(1) == 1
    assert escape(1.0) == 1.0
    assert escape(True) == True
    assert escape(None) == None
    # If there is no match, nothing gets returned
    assert escape(re.match('b', 'a')) == None
    # Otherwise, the matched group gets returned
    assert escape(re.match('b', 'b')) == 'b'
    assert escape(re.match('b', 'ab')) == 'b'
    assert escape(re.match('b', 'ba')) == 'b'
    # The first group is the entire match, so it's the same as above
    assert escape(re.search('b', 'b')) == 'b'
    # If there is a second group,

# Generated at 2022-06-13 17:56:09.273067
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x[0-9a-fA-F]", "\\xFF")) == 'ÿ'
    assert escape(re.match(r"\\[1-7]", "\\123")) == '{'
    assert escape(re.match(r"\\[1-7]", "\\99")) == 'c'


# Generated at 2022-06-13 17:56:18.019250
# Unit test for function escape
def test_escape():
    import unittest
    from io import StringIO

    class TestEscape(unittest.TestCase):
        simple_escapes = {
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

        def test_basic(self):
            for key in self.simple_escapes:
                self.assertEqual(escape("\\" + key), self.simple_escapes[key])
                self.assertEqual(escape("\\" + key + "foo"), self.simple_escapes[key])


# Generated at 2022-06-13 17:56:25.439158
# Unit test for function escape
def test_escape():
    test_values = {
        "\\a": "\a",
        "\\b": "\b",
        "\\f": "\f",
        "\\n": "\n",
        "\\r": "\r",
        "\\t": "\t",
        "\\v": "\v",
        "\\'": "'",
        '\\"': '"',
        "\\\\": "\\",
        "\\x07": "\x07",
        "\\037": "\037",
        "\\x1F": "\x1F",
    }
    for k, v in test_values.items():
        assert escape(re.match(r"\\(.+)", k)) == v

# Generated at 2022-06-13 17:56:30.443006
# Unit test for function escape
def test_escape():
    # invalid escape sequence
    def invalid_escape_seq():
        escape("\\?")

    assert_raises(ValueError, invalid_escape_seq)

    # invalid hex string escape
    def invalid_hex_str_escape():
        escape("\\x0")

    assert_raises(ValueError, invalid_hex_str_escape)
    assert_raises(ValueError, invalid_hex_str_escape)

    # invalid octal string escape
    def invalid_oct_str_escape():
        escape("\\81")

    assert_raises(ValueError, invalid_oct_str_escape)
    assert_raises(ValueError, invalid_oct_str_escape)

    # valid escape sequence
    assert escape("\\a") == "\a"
    assert escape("\\b") == "\b"
    assert escape("\\f")

# Generated at 2022-06-13 17:56:39.968970
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\([abfnrtv\'"]|\\|[0-7]{1,3})', r'\a')) == "\a"
    assert escape(re.match(r'\\([abfnrtv\'"]|\\|[0-7]{1,3})', r'\b')) == "\b"
    assert escape(re.match(r'\\([abfnrtv\'"]|\\|[0-7]{1,3})', r'\f')) == "\f"
    assert escape(re.match(r'\\([abfnrtv\'"]|\\|[0-7]{1,3})', r'\n')) == "\n"

# Generated at 2022-06-13 17:56:51.296719
# Unit test for function escape
def test_escape():
    """Test escape function with parameter"""
    # Test simple escape string
    result = escape(re.search(r"\\[']", "\\'"))
    assert result == "'"

    result = escape(re.search(r"\\['\"]", "\\\""))
    assert result == "\""

    result = escape(re.search(r"\\['\"]", "\\\\"))
    assert result == "\\"
    # Test hex escape character
    result = escape(re.search(r"\\[x]", "\\x"))
    assert result == "\\x"
    result = escape(re.search(r"\\[x]", "\\x0"))
    assert result == "\\x0"
    result = escape(re.search(r"\\[x]", "\\x00"))
    assert result == "\x00"

# Generated at 2022-06-13 17:58:20.861357
# Unit test for function test
def test_test():
    # Test that function test raises no errors
    test()

# Generated at 2022-06-13 17:58:30.917354
# Unit test for function escape
def test_escape():
    import lib2to3.pytree
    import lib2to3.pgen2.token
    import lib2to3.pgen2.parse

# Generated at 2022-06-13 17:58:31.891690
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:35.365814
# Unit test for function escape
def test_escape():
    # Test invalid escape
    try:
        escape(r'\x')
    except ValueError as e:
        assert str(e) == "invalid hex string escape ('\\x')"
    else:
        assert False, 'Expected ValueError'

# Generated at 2022-06-13 17:58:35.894463
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:40.125536
# Unit test for function escape
def test_escape():
    import asteval
    string = '\\a\\b\\f\\n\\r\\t\\v\\"\\\'\\\\'
    result = asteval.escape(string)
    answer = '\a\b\f\n\r\t\v"\'"\\'
    assert result == answer, 'Expected: %s, got %s' % (answer, result)

# Generated at 2022-06-13 17:58:41.039864
# Unit test for function test
def test_test():
    assert test() is None


# Generated at 2022-06-13 17:58:44.983516
# Unit test for function escape
def test_escape():
    expected = '\x10'
    assert escape(re.match('\\x10', '\\x10')) == expected
    assert escape(re.match('\\\\', '\\\\')) == '\\'
    # 'a' is special case, not in simple_escapes
    assert escape(re.match('\\a', '\\a')) == '\x07'

# Generated at 2022-06-13 17:58:45.450730
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:46.164073
# Unit test for function test
def test_test():
    assert(test() == None)