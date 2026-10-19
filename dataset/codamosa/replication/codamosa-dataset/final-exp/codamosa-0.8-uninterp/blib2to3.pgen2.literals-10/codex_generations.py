

# Generated at 2022-06-13 17:49:56.716107
# Unit test for function escape
def test_escape():

    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = escape(s[0:2])
        if e != c:
            print(i, c, e)

# Generated at 2022-06-13 17:50:05.361333
# Unit test for function escape

# Generated at 2022-06-13 17:50:07.007136
# Unit test for function test
def test_test():
    try:
        test()
    except ValueError:
        return

# Generated at 2022-06-13 17:50:18.351696
# Unit test for function escape
def test_escape():
    # Test against exact values expected
    assert escape(re.search('\\\\', '\\\\')) == '\\'
    assert escape(re.search('\\\\a', '\\\\a')) == '\a'
    assert escape(re.search('\\\\b', '\\\\b')) == '\b'
    assert escape(re.search('\\\\f', '\\\\f')) == '\f'
    assert escape(re.search('\\\\n', '\\\\n')) == '\n'
    assert escape(re.search('\\\\r', '\\\\r')) == '\r'
    assert escape(re.search('\\\\t', '\\\\t')) == '\t'
    assert escape(re.search('\\\\v', '\\\\v')) == '\v'
    assert escape(re.search('\\\\"', '\\\\"')) == '"'

# Generated at 2022-06-13 17:50:29.514478
# Unit test for function escape
def test_escape():
    s = "\\x0000"
    assert re.sub(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", escape, s) == "\x00"
    s = "\\x0A"
    assert re.sub(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", escape, s) == "\n"
    s = "\\x1A"
    assert re.sub(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", escape, s) == "\x1a"
    s = "\\0000"

# Generated at 2022-06-13 17:50:31.647674
# Unit test for function escape
def test_escape():
    # assert escape('\x20') == ' '
    # assert escape('\u0100') == 'Ā'
    assert escape('\u0020') == ' '
    assert escape('\u0100') == 'Ā'

# Generated at 2022-06-13 17:50:41.674256
# Unit test for function escape

# Generated at 2022-06-13 17:50:48.903801
# Unit test for function escape
def test_escape():
    assert escape(("\\a", "a", 1)) == "\a"
    assert escape(("\\b", "b", 1)) == "\b"
    assert escape(("\\f", "f", 1)) == "\f"
    assert escape(("\\n", "n", 1)) == "\n"
    assert escape(("\\r", "r", 1)) == "\r"
    assert escape(("\\t", "t", 1)) == "\t"
    assert escape(("\\v", "v", 1)) == "\v"
    assert escape(("\\'", "'", 1)) == "'"
    assert escape(('\\"', '"', 1)) == '"'
    assert escape(("\\\\", "\\", 1)) == "\\"
    assert escape(("\\x41", "x41", 1)) == "A"
    assert escape

# Generated at 2022-06-13 17:50:49.808584
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:50:52.355790
# Unit test for function escape
def test_escape():
    for c in range(256):
        s = repr(chr(c))
        assert escape(re.match(r"\\(.*)", s)) == s[1:]

# Generated at 2022-06-13 17:51:20.686936
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x[0-9a-f]{2}", "\\x81")) == "\u0081"
    assert escape(re.match(r"\\[0-7]{3}", "\\377")) == "\xff"
    assert escape(re.match(r"\\[0-7]{3}", "\\400")) == "\u0100"
    assert escape(re.match(r"\\x[0-9a-f]{2}", "\\xff")) == "\xff"
    assert escape(re.match(r"\\x[0-9a-f]{2}", "\\x00")) == "\u0000"

# Generated at 2022-06-13 17:51:32.557609
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"
    assert escape(re.match(r"\\v", "\\v")) == "\v"
    assert escape(re.match(r"\\'", "\\'")) == "'"
    assert escape(re.match(r'\\"', '\\"')) == '"'
    assert escape

# Generated at 2022-06-13 17:51:33.520442
# Unit test for function test
def test_test():
    test()
    assert True

# Generated at 2022-06-13 17:51:42.925138
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\'", r"\'")) == "'"
    assert escape(re.match(r'\\"', r'\"')) == '"'
    assert escape(re.match(r'\\\\', r'\\')) == '\\'
    assert escape(re.match(r"\\a", r"\a")) == "\a"
    assert escape(re.match(r"\\b", r"\b")) == "\b"
    assert escape(re.match(r"\\f", r"\f")) == "\f"
    assert escape(re.match(r"\\n", r"\n")) == "\n"
    assert escape(re.match(r"\\r", r"\r")) == "\r"

# Generated at 2022-06-13 17:51:43.807888
# Unit test for function test
def test_test():
    rval = test()
    assert rval is None

# Generated at 2022-06-13 17:51:51.892382
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x[0-9a-fA-F]{2}|[0-7]{1,3})",
                           "\\a")) == "\a"

    assert escape(re.match(r"\\([abfnrtv'\"\\]|x[0-9a-fA-F]{2}|[0-7]{1,3})",
                           "\\b")) == "\b"

    assert escape(re.match(r"\\([abfnrtv'\"\\]|x[0-9a-fA-F]{2}|[0-7]{1,3})",
                           "\\f")) == "\f"


# Generated at 2022-06-13 17:51:57.556986
# Unit test for function escape
def test_escape():
    result = escape('x1')
    assert result == '\x01', result
    result = escape('x12')
    assert result == '\x12', result
    result = escape('x123')
    assert result == '\\x123', result
    result = escape('011')
    assert result == '\t', result
    result = escape('071')
    assert result == '\\071', result
    result = escape('\\071')
    assert result == '\\071', result

# Generated at 2022-06-13 17:52:05.473158
# Unit test for function escape
def test_escape():
    """Check that escape() handles all the possible inputs"""

    assert escape(re.match(r"\\'", "\\'")) == "'"
    assert escape(re.match(r'\\"', '\\"')) == '"'

    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"

# Generated at 2022-06-13 17:52:14.666368
# Unit test for function escape
def test_escape():
    test_list = [
        r"\a",
        r"\b",
        r"\f",
        r"\n",
        r"\r",
        r"\t",
        r"\v",
        r"\'",
        r"\"",
        r"\\",
        r"\x00",
        r"\001",
        r"\002",
        r"\003",
        r"\004",
        r"\005",
        r"\006",
        r"\a",
        r"\b",
        r"\f",
        r"\n",
        r"\r",
        r"\t",
        r"\v",
        r"\'",
        r"\"",
        r"\\"
    ]


# Generated at 2022-06-13 17:52:19.570649
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([a-z]+)", "\\abc" )) == "\abc"
    assert escape(re.match(r"\\([a-z]+)", "\\def" )) == "\def"
    assert escape(re.match(r"\\([a-z]+)", "\\g"   )) == "g"
    assert escape(re.match(r"\\([a-z]+)", "\\h"   )) == "h"
    assert escape(re.match(r"\\([a-z]+)", "\\i"   )) == "i"


# Generated at 2022-06-13 17:52:40.805765
# Unit test for function escape
def test_escape():
    assert(escape(re.match(r"\\x00", "\\x00")) == chr(0))
    assert(escape(re.match(r"\\x41", "\\x41")) == chr(65))
    assert(escape(re.match(r"\\00", "\\00")) == chr(0))
    assert(escape(re.match(r"\\01", "\\01")) == chr(1))
    assert(escape(re.match(r"\\15", "\\15")) == chr(13))
    assert(escape(re.match(r"\\77", "\\77")) == chr(63))

# Generated at 2022-06-13 17:52:52.210130
# Unit test for function escape
def test_escape():
    import unittest

    class TestEscape(unittest.TestCase):
        def _test_escaped_char(self, c: str, val: str):
            m = re.match(r"\\(" + c + ")", "\\" + c)
            self.assertEqual(escape(m), val)

        def test_simple_escapes(self):
            self._test_escaped_char("'", "'")
            self._test_escaped_char('"', '"')
            self._test_escaped_char("\\", "\\")
            self._test_escaped_char("a", "\x07")
            self._test_escaped_char("b", "\x08")
            self._test_escaped_char("f", "\x0c")

# Generated at 2022-06-13 17:53:01.982867
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(')", r"\'")).endswith("'")
    assert escape(re.match(r"\\(\"|\\)", r"\"")).endswith('"')
    assert escape(re.match(r"\\(\\)", r"\\")).endswith("\\")
    assert escape(re.match(r"\\([abfnrtv])", r"\t")).endswith("\t")
    assert escape(re.match(r"\\((x.{0,2}|[0-7]{1,3})", r"\x12")).endswith("\x12")

# Generated at 2022-06-13 17:53:03.279592
# Unit test for function escape
def test_escape():
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 17:53:12.146342
# Unit test for function escape

# Generated at 2022-06-13 17:53:23.537539
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x5f", "\\x5f")) == "_"
    assert escape(re.match(r"\\x5f", "\\x5f")) == "_"
    assert escape(re.match(r"\\xf", "\\xf")) == "\x0f"
    assert escape(re.match(r"\\x5", "\\x5")) == "\\x5"
    assert escape(re.match(r"\\x", "\\x")) == "\\x"
    assert escape(re.match(r"\\|x", "\\|x")) == "\\|x"
    assert escape(re.match(r"\\|x", "\\|x")) == "\\|x"
    assert escape(re.match(r"\\377", "\\377")) == "\xff"

# Generated at 2022-06-13 17:53:31.533047
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\[abfnrtv]', r'\a')) == "\a"
    assert escape(re.match(r'\\[abfnrtv]', r'\b')) == "\b"
    assert escape(re.match(r'\\[abfnrtv]', r'\f')) == "\f"
    assert escape(re.match(r'\\[abfnrtv]', r'\n')) == "\n"
    assert escape(re.match(r'\\[abfnrtv]', r'\r')) == "\r"
    assert escape(re.match(r'\\[abfnrtv]', r'\t')) == "\t"

# Generated at 2022-06-13 17:53:39.493258
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfrnrt'\"\\]|x.{0,2}|[0-7]{1,3})", r"\a")) == "\a"
    assert escape(re.match(r"\\([abfrnrt'\"\\]|x.{0,2}|[0-7]{1,3})", r"\x61")) == "a"
    assert escape(re.match(r"\\([abfrnrt'\"\\]|x.{0,2}|[0-7]{1,3})", r"\111")) == "I"

# Generated at 2022-06-13 17:53:41.613105
# Unit test for function test
def test_test():
    if(test()):
        print('testing successfull')
    else:
        print('testing fail')

test_test()

# Generated at 2022-06-13 17:53:42.306830
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:54:12.691473
# Unit test for function escape
def test_escape():
    assert escape(re.search(r'\\a', r'\\a')) == '\a'
    assert escape(re.search(r'\\b', r'\\b')) == '\b'
    assert escape(re.search(r'\\f', r'\\f')) == '\f'
    assert escape(re.search(r'\\n', r'\\n')) == '\n'
    assert escape(re.search(r'\\r', r'\\r')) == '\r'
    assert escape(re.search(r'\\t', r'\\t')) == '\t'
    assert escape(re.search(r'\\v', r'\\v')) == '\v'
    assert escape(re.search(r"\\'", r"\\'")) == "'"

# Generated at 2022-06-13 17:54:21.036027
# Unit test for function escape
def test_escape():
    assert escape("\\a") == chr(7)
    assert escape("\\b") == chr(8)
    assert escape("\\f") == chr(12)
    assert escape("\\n") == chr(10)
    assert escape("\\r") == chr(13)
    assert escape("\\t") == chr(9)
    assert escape("\\v") == chr(11)
    assert escape("\\'") == chr(39)
    assert escape('\\"') == chr(34)
    assert escape("\\\\") == chr(92)
    assert escape("\\xAA") == chr(170)
    assert escape("\\143") == chr(99)

# Generated at 2022-06-13 17:54:30.469419
# Unit test for function escape
def test_escape():
    escaped = """
    \\a \\b \\f \\n \\r \\t \\v
    \\\' \\" \\\\
    \\x00 \\x0f \\xff
    \\000 \\00f \\200 \\377
    """
    correct = (
        "\a \b \f \n \r \t \v "
        "' \" \\"
        "\\x00 \\x0f \\xff "
        "\\000 \\00f \\200 \\377 "
    )

    escaped2 = re.sub(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", escape, escaped)
    assert escaped2 == correct

# Generated at 2022-06-13 17:54:40.668102
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\a", r"\a")) == "\a"
    assert escape(re.match(r"\\b", r"\b")) == "\b"
    assert escape(re.match(r"\\f", r"\f")) == "\f"
    assert escape(re.match(r"\\n", r"\n")) == "\n"
    assert escape(re.match(r"\\r", r"\r")) == "\r"
    assert escape(re.match(r"\\t", r"\t")) == "\t"
    assert escape(re.match(r"\\v", r"\v")) == "\v"
    assert escape(re.match(r'\\"', r'"')) == '"'
    assert escape(re.match(r"\\'", r"'"))

# Generated at 2022-06-13 17:54:42.235167
# Unit test for function test
def test_test():
    """Test function provided for unit testing"""
    test()

# Generated at 2022-06-13 17:54:44.170177
# Unit test for function test
def test_test():
    s = '"\'"'
    assert evalString(s) == s[1:-1]

# Generated at 2022-06-13 17:54:44.890194
# Unit test for function test
def test_test():
    assert 1 == 1

# Generated at 2022-06-13 17:54:45.590018
# Unit test for function test
def test_test():
    pass

# Generated at 2022-06-13 17:54:54.781651
# Unit test for function escape

# Generated at 2022-06-13 17:54:55.858613
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:23.377102
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:26.827048
# Unit test for function test
def test_test():
    test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:

# Generated at 2022-06-13 17:55:31.166836
# Unit test for function test
def test_test():
    import unittest
    class Test_test(unittest.TestCase):
        def test_test(self):
            test()
    unittest.main()

# Generated at 2022-06-13 17:55:32.799626
# Unit test for function test
def test_test():
    # This is a doctest to run all the examples.

    '''
    >>> test()
    '''
    pass

# Generated at 2022-06-13 17:55:40.329929
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\'", "\\'")).__eq__("'")
    assert escape(re.match("\\'", "\\'")).__eq__("'")
    assert escape(re.match('\\"', '\\"')).__eq__('"')
    assert escape(re.match("\\\\", "\\\\")).__eq__("\\")
    assert escape(re.match("\\a", "\\a")).__eq__("\a")
    assert escape(re.match("\\b", "\\b")).__eq__("\b")
    assert escape(re.match("\\f", "\\f")).__eq__("\f")
    assert escape(re.match("\\n", "\\n")).__eq__("\n")

# Generated at 2022-06-13 17:55:50.096050
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\x0a", "\\x0a")) == "\x0a"
    assert escape(re.match("\\0a", "\\0a")) == "\n"
    assert escape(re.match("\\a", "\\a")) == "\x07"
    assert escape(re.match("\\b", "\\b")) == "\x08"
    assert escape(re.match("\\f", "\\f")) == "\x0c"
    assert escape(re.match("\\n", "\\n")) == "\n"
    assert escape(re.match("\\r", "\\r")) == "\r"
    assert escape(re.match("\\t", "\\t")) == "\t"
    assert escape(re.match("\\v", "\\v")) == "\x0b"

# Generated at 2022-06-13 17:55:59.349399
# Unit test for function escape
def test_escape():
    from unittest.mock import patch

    with patch("sys.stdout", new=None):
        s = "\\a\\b\\f\\n\\r\\t\\v\\'\\\"\\\\"
        assert escape(re.search(r"^\\.","\\a")).endswith(s[1])
        assert escape(re.search(r"^\\.","\\b")).endswith(s[3])
        assert escape(re.search(r"^\\.","\\f")).endswith(s[5])
        assert escape(re.search(r"^\\.","\\n")).endswith(s[7])
        assert escape(re.search(r"^\\.","\\r")).endswith(s[9])
        assert escape(re.search(r"^\\.","\\t")).endsw

# Generated at 2022-06-13 17:55:59.845905
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:04.582123
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

    assert escape("\\x61") == "a"
    assert escape("\\171") == "q"
    assert escape("\\x7a") == "z"

    assert escape("\\072") == ":"
    assert escape("\\077") == "?"

    assert escape("\\012") == "\n"


# Generated at 2022-06-13 17:56:11.823619
# Unit test for function escape
def test_escape():
    assert escape('\\n') == '\n'
    assert escape('\\x1a') == '\x1a'
    assert escape('\\xaa') == '\xaa'
    assert escape('\\377') == '\xFF'
    assert escape('\\444') == '\xCC'

    try:
        escape('\\xaa')
        raise AssertionError('Unexpected success with \\xaa')
    except ValueError:
        assert True


# Generated at 2022-06-13 17:57:06.004582
# Unit test for function test
def test_test():

    from pytest import raises

    with raises(ValueError):
        test()

# Generated at 2022-06-13 17:57:19.137963
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\", r"\"")) == "\\"
    assert escape(re.match(r"\\", r"\\")) == "\\"
    assert escape(re.match(r"\\[abfnrtv]", r"\a")) == "\a"
    assert escape(re.match(r"\\[abfnrtv]", r"\b")) == "\b"
    assert escape(re.match(r"\\[abfnrtv]", r"\f")) == "\f"
    assert escape(re.match(r"\\[abfnrtv]", r"\n")) == "\n"
    assert escape(re.match(r"\\[abfnrtv]", r"\r")) == "\r"

# Generated at 2022-06-13 17:57:28.830298
# Unit test for function escape
def test_escape():
    cases = [
        # (input, expected output)
        ("\\'", "'"),
        ("\\a", "\a"),
        ("\\x5e", "^"),
        ("\\056", "."),
    ]
    for case, expected in cases:
        actual = escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", case))
        assert actual == expected, (actual, expected)

# Generated at 2022-06-13 17:57:35.735999
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x0A", "\\x0A")) == "\n"
    assert escape(re.match(r"\\x0A", "\\x0A")) == "\n"
    assert escape(re.match(r"\\x0A", "\\x0A")) == "\n"

# Generated at 2022-06-13 17:57:42.924903
# Unit test for function escape
def test_escape():

    tests = [
        (r"\a", "\a"),
        (r"\b", "\b"),
        (r"\t", "\t"),
        (r"\n", "\n"),
        (r"\v", "\v"),
        (r"\f", "\f"),
        (r"\r", "\r"),
        (r"\\", "\\"),
        (r"\'", "\'"),
        (r'\"', '"'),
        (r"\013", "\013"),
        (r"\00", "\000"),
        (r"\x41", "A"),
        ("\\", "\\"),
    ]

# Generated at 2022-06-13 17:57:51.776006
# Unit test for function test
def test_test():
    test()
    expected = [
        123,
        '{',
        ("'{'", '"'),
        ('"{}"', '{'),
        124,
        '|',
        ("'|'", '"'),
        ('"|"', '|'),
        125,
        '}',
        ("'}'", '"'),
        ('"}"', '}'),
        126,
        '~',
        ("'~'", '"'),
        ('"~"', '~'),
    ]
    assert expected == test()

# Generated at 2022-06-13 17:58:01.785669
# Unit test for function escape
def test_escape():
    # test simple escapes
    for i, esc in simple_escapes.items():
        escaped = "\\%s" % i
        assert escape(re.match(r"\\[a-z]", escaped)) == esc
    # test octal escapes
    for i in range(256):
        escaped = "\\%o" % i
        assert escape(re.match(r"\\[0-7]{1,3}", escaped)) == chr(i)
    # test hexadecimal escapes
    assert escape(re.match(r"\\x[a-z]{2}", "\\xab")) == "ª"
    assert escape(re.match(r"\\x[A-Z]{2}", "\\xAB")) == "ª"
    # test error cases
    # bad hexadecimal escape


# Generated at 2022-06-13 17:58:07.424530
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\", "\\")) == "\\"
    assert escape(re.match(r"\\", "\\x42")) == "B"
    assert escape(re.match(r"\\", "\\09")) == "\t"

# Generated at 2022-06-13 17:58:11.719387
# Unit test for function test
def test_test():
  result1 = evalString("'\\x61'")
  assert result1 == 'a', "result1: %s" % result1
  result2 = evalString("b'\\x61'")
  assert result2 == b'a', "result2: %s" % result2
  result3 = evalString('b"\\x61"')
  assert result3 == b'a', "result3: %s" % result3

# Generated at 2022-06-13 17:58:20.691732
# Unit test for function escape
def test_escape():
    from pytest import raises
    from sys import hexversion

    assert escape(re.match(r'\\a', r'\a')) == "\a"
    assert escape(re.match(r'\\b', r'\b')) == "\b"
    assert escape(re.match(r'\\f', r'\f')) == "\f"
    assert escape(re.match(r'\\n', r'\n')) == "\n"
    assert escape(re.match(r'\\r', r'\r')) == "\r"
    assert escape(re.match(r'\\t', r'\t')) == "\t"
    assert escape(re.match(r'\\v', r'\v')) == "\v"