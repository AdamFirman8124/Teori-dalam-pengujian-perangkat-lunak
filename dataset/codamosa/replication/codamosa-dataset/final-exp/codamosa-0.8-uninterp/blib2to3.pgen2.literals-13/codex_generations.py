

# Generated at 2022-06-13 17:50:03.860745
# Unit test for function escape
def test_escape():
    import unittest


# Generated at 2022-06-13 17:50:05.091898
# Unit test for function escape
def test_escape():
    assert escape('\a') == '\a'

# Generated at 2022-06-13 17:50:05.968938
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:50:17.425135
# Unit test for function escape
def test_escape():
    hex_str = [
        ("\\x41", "\x41"),
        ("\\x41A", "\x41A"),
        ("\\x41AB", "\x41AB"),
        ("\\x41ABC", "\x41ABC"),
        ("\\x41ABCD", "\x41ABCD"),
        ("\\x41ABCDE", "\x41ABCDE"),
        ("\\x41ABCDEF", "\x41ABCDEF"),
    ]
    for s, res in hex_str:
        assert escape(re.match(r"\\x\S{0,6}", s)) == res

# Generated at 2022-06-13 17:50:29.037432
# Unit test for function evalString
def test_evalString():
    assert evalString('"\\x7f"') == "\x7f"
    assert evalString("'''\\x7F'''") == "\x7F"
    assert evalString("'\\a\\b\\c\\d\\e\\f'") == "\a\b\c\d\e\f"
    assert evalString("'\\g\\h\\i\\j\\k\\l'") == "\\g\\h\\i\\j\\k\\l"
    assert evalString("'\\m\\n\\o\\p\\q\\r'") == "\\m\n\\o\\p\\q\r"
    assert evalString("'\\s\\t\\u\\v\\w\\x'") == "\\s\t\\u\\v\\w\\x"

# Generated at 2022-06-13 17:50:30.043561
# Unit test for function evalString
def test_evalString():
    assert evalString("'hello world'") == 'hello world'
    assert evalString('"hello world"') == 'hello world'


# Generated at 2022-06-13 17:50:41.401834
# Unit test for function escape
def test_escape():
    from lib2to3 import pytree
    from lib2to3.pgen2 import token
    from lib2to3.pygram import python_symbols as syms
    from lib2to3.pygram import python_grammar
    from lib2to3.fixer_util import String, touch_import
    from lib2to3.fixer_util import Newline, Comma

    parser = python_grammar.parser()
    result = parser.parse("""'\\xac\\U000000ac'""")
    print(result)
    assert len(result) == 2
    # string+token_eof
    assert result[0].type == syms.single_quoted
    assert len(result[0].children) == 1
    # string
    assert result[0].children[0].type == token.STRING
   

# Generated at 2022-06-13 17:50:42.886645
# Unit test for function escape
def test_escape():
    if escape(None) is not None:
        raise Exception("Failed")


# Generated at 2022-06-13 17:50:54.216854
# Unit test for function evalString
def test_evalString():
    assert evalString("'abc'") == "abc"
    assert evalString("u'abc'") == "abc"
    assert evalString("b'abc'") == "abc"
    assert evalString("ur'abc'") == "abc"
    assert evalString('"abc"') == "abc"
    assert evalString('u"abc"') == "abc"
    assert evalString('b"abc"') == "abc"
    assert evalString('ur"abc"') == "abc"

    assert evalString("'''abc'''") == "abc"
    assert evalString("u'''abc'''") == "abc"
    assert evalString("b'''abc'''") == "abc"
    assert evalString("ur'''abc'''") == "abc"
    assert evalString('"""abc"""') == "abc"


# Generated at 2022-06-13 17:51:00.150469
# Unit test for function evalString
def test_evalString():
    assert evalString("'123'") == "123"
    assert evalString("'456\\n'") == "456\n"
    assert evalString("'789\\t'") == "789\t"
    assert evalString("'101\\n112\\t'") == "101\n112\t"
    assert evalString("'123\\141'") == "123a"
    assert evalString("'123\\51'") == "123\t"
    assert evalString("'123\\x41'") == "123A"

# Generated at 2022-06-13 17:51:20.602291
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([\"\'\\abfnrtv])", "\\a")) == "\a"
    assert escape(re.match(r"\\([\"\'\\abfnrtv])", "\\b")) == "\b"
    assert escape(re.match(r"\\([\"\'\\abfnrtv])", "\\f")) == "\f"
    assert escape(re.match(r"\\([\"\'\\abfnrtv])", "\\n")) == "\n"
    assert escape(re.match(r"\\([\"\'\\abfnrtv])", "\\r")) == "\r"
    assert escape(re.match(r"\\([\"\'\\abfnrtv])", "\\t")) == "\t"

# Generated at 2022-06-13 17:51:32.555359
# Unit test for function escape
def test_escape():

    # Check simple escapes.
    assert escape(re.match(r'\a', r'\a')) == '\a'
    assert escape(re.match(r'\b', r'\b')) == '\b'
    assert escape(re.match(r'\f', r'\f')) == '\f'
    assert escape(re.match(r'\n', r'\n')) == '\n'
    assert escape(re.match(r'\r', r'\r')) == '\r'
    assert escape(re.match(r'\t', r'\t')) == '\t'
    assert escape(re.match(r'\v', r'\v')) == '\v'
    assert escape(re.match(r'\'', r'\''))

# Generated at 2022-06-13 17:51:40.633113
# Unit test for function escape
def test_escape():
    assert escape(chr(0)) == "\x00"
    assert escape(chr(0x9)) == "\x09"
    assert escape(chr(0xA)) == "\x0A"
    assert escape(chr(0xB)) == "\x0B"
    assert escape(chr(0xC)) == "\x0C"
    assert escape(chr(0xD)) == "\x0D"
    assert escape(chr(0x20)) == chr(0x20)
    assert escape(chr(0x21)) == chr(0x21)
    assert escape(chr(0x22)) == chr(0x22)
    assert escape(chr(0x23)) == chr(0x23)

# Generated at 2022-06-13 17:51:42.244885
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:51:50.731312
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x5f", r"\x5f")) == "_"
    assert escape(re.match(r"\\x5g", r"\x5g")) == "g"
    assert escape(re.match(r"\\U0023", r"\U0023")) == "#"
    assert escape(re.match(r"\\U002g", r"\U002g")) == "g"
    # assert escape(re.match(r"\\U0", r"\U0")) is None
    # assert escape(re.match(r"\\U02", r"\U02")) is None
    # assert escape(re.match(r"\\U02g", r"\U02g")) is None
    # assert escape(re.match(r"\\U02ggg", r"

# Generated at 2022-06-13 17:51:51.951008
# Unit test for function escape
def test_escape():
    pass

# Generated at 2022-06-13 17:51:53.302056
# Unit test for function test
def test_test():
    with pytest.raises(SystemExit):
        test()

# Generated at 2022-06-13 17:52:03.659853
# Unit test for function escape
def test_escape():
    cases = [
        (r'\x3d', '='),
        (r'\17', '\x0f'),
        (r'\a', '\x07'),
        (r'\n', '\n'),
        (r'\r', '\r'),
        (r'\r\n', '\r\n'),
        (r'\x0a', '\n'),
        (r'\\r\\n', '\\r\\n'),
        (r'\z', 'z'),
        (r'\05', '\x05'),
        (r'\\', '\\'),
        (r'\\a', 'a'),
    ]

    for case, expected_result in cases:
        assert escape(case) == expected_result

# Generated at 2022-06-13 17:52:07.246040
# Unit test for function escape
def test_escape():
    # tests gets passed to function evalString and then to escape
    # see: https://github.com/python/mypy/issues/2287
    result = evalString("'b\\x00\''")
    assert result == "\b\x00'"
    result = evalString("'b\\000\''")
    assert result == "\b\x00'"

# Generated at 2022-06-13 17:52:15.885252
# Unit test for function escape

# Generated at 2022-06-13 17:52:25.727393
# Unit test for function escape
def test_escape():
    assert escape("\a" == "a")
    assert escape("\b" == "b")
    assert escape("\f" == "f")
    assert escape("\n" == "n")
    assert escape("\r" == "r")
    assert escape("\t" == "t")
    assert escape("\v" == "v")
    assert escape("'" == "'")
    assert escape('"' == '"')
    assert escape("\\" == "\\")

# Generated at 2022-06-13 17:52:26.232196
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:26.758320
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:27.894303
# Unit test for function test
def test_test():  # noqa: WPS432
    test()  # noqa: WPS421

# Generated at 2022-06-13 17:52:28.459482
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:37.385136
# Unit test for function escape
def test_escape():
    test_pairs = [
        (r"\a", "\a"),
        (r"\b", "\b"),
        (r"\f", "\f"),
        (r"\n", "\n"),
        (r"\r", "\r"),
        (r"\t", "\t"),
        (r"\v", "\v"),
        (r"'", "'"),
        (r'"', '"'),
        (r"\\", "\\"),
        (r"\x03", "\x03"),
        (r"\x3", "x3"),
        (r"\x00", "\x00"),
        (r"\00", "\00"),
        (r"\000", "\000"),
    ]
    for test_pair in test_pairs:
        input_, output = test_pair
       

# Generated at 2022-06-13 17:52:49.265156
# Unit test for function escape
def test_escape():
    # Test simple escapes
    for (test, expect) in simple_escapes.items():
        assert escape(re.match(r"\\" + test, r"\\" + test)) == expect

    # Test hex escapes
    assert escape(re.match(r"\\x41", r"\\x41")) == "A"
    assert escape(re.match(r"\\x4D", r"\\x4D")) == "M"
    assert escape(re.match(r"\\x4e", r"\\x4e")) == "N"
    assert escape(re.match(r"\\x6D", r"\\x6D")) == "m"

    # Test large hex escapes

# Generated at 2022-06-13 17:52:53.686623
# Unit test for function test
def test_test():
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        test()
        assert sys.stdout.getvalue() == ""
    finally:
        sys.stdout = old_stdout


# Generated at 2022-06-13 17:52:54.524889
# Unit test for function test
def test_test():
    assert test() == None

# Generated at 2022-06-13 17:52:55.603422
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:05.814423
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\v', '\\v')) == '\v'


# Generated at 2022-06-13 17:53:08.507662
# Unit test for function escape
def test_escape():
    esc = '\\'
    res = escape(esc)
    assert res == '\\', res

    esc = '\\xab'
    res = escape(esc)
    assert res == '\xab', res
    return

# Generated at 2022-06-13 17:53:20.449010
# Unit test for function escape
def test_escape():
    def ck(m, e):
        assert escape(re.match(r'\\%s' % m, r'\%s' % m)) == e
    ck('x00', '\x00')
    ck('x7f', '\x7f')
    ck('xFF', '\xFF')
    ck('x00', '\x00')
    ck('x10', '\x10')
    ck('100', 'd')
    ck('77', '?')
    ck('0', '\0')
    ck('077', '?')
    ck('07', '\a')
    ck('a', '\n')
    ck('b', '\x08')
    ck('f', '\x0C')

# Generated at 2022-06-13 17:53:35.169961
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\a")) == "\a"
    assert escape(re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\b")) == "\b"
    assert escape(re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\f")) == "\f"
    assert escape(re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\n")) == "\n"

# Generated at 2022-06-13 17:53:40.546092
# Unit test for function escape
def test_escape():
    # Test all the ways that escape() can be called
    # These tests correspond to the five ways that escape()
    # can be called as documented in the docstring for escape()
    assert escape("\\'") == "'"
    assert escape("\\b") == "\b"
    assert escape("\\n") == "\n"
    assert escape("\\x5d") == "]"
    assert escape("\\77") == "?"
    # There aren't really any exceptions to be caught for escape()
    # but for the sake of ensuring we have 100% test coverage,
    # here is a fake test to see if we have an exception in escape()
    # that isn't being caught.  If there is an uncaught exception,
    # the following call to escape() will cause the function to
    # return an error message instead of an actual value.

# Generated at 2022-06-13 17:53:51.883904
# Unit test for function escape
def test_escape():
    actual = escape(re.match("a", "\\a"))
    assert actual == "\a"

    actual = escape(re.match("b", "\\b"))
    assert actual == "\b"

    actual = escape(re.match("f", "\\f"))
    assert actual == "\f"

    actual = escape(re.match("n", "\\n"))
    assert actual == "\n"

    actual = escape(re.match("r", "\\r"))
    assert actual == "\r"

    actual = escape(re.match("t", "\\t"))
    assert actual == "\t"

    actual = escape(re.match("v", "\\v"))
    assert actual == "\v"

    actual = escape(re.match("'", "\\'"))
    assert actual == "'"


# Generated at 2022-06-13 17:54:01.579937
# Unit test for function escape
def test_escape():
    m = type("Match", (object,), {})
    m.group = lambda x, y: ("\\" + y, y)
    assert escape(m) == "\\"
    m.group = lambda x, y: ("\\'", y)
    assert escape(m) == "'"
    m.group = lambda x, y: ('\\"', y)
    assert escape(m) == '"'
    m.group = lambda x, y: ('\\a', y)
    assert escape(m) == "\a"
    m.group = lambda x, y: ('\\b', y)
    assert escape(m) == "\b"
    m.group = lambda x, y: ('\\f', y)
    assert escape(m) == "\f"

# Generated at 2022-06-13 17:54:07.075572
# Unit test for function test
def test_test():
    sys.stdout = open("evalString.tmp", "w")
    test()
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    got = open("evalString.tmp", "r").read()

# Generated at 2022-06-13 17:54:15.151838
# Unit test for function escape
def test_escape():
    # Test for valid sequences
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x..|[0-7]{1,3})", r"\'\'")) == "'"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x..|[0-7]{1,3})", r"\"\"")) == '"'
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x..|[0-7]{1,3})", r"\\")) == "\\"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x..|[0-7]{1,3})", r"\a")) == "\a"

# Generated at 2022-06-13 17:54:16.612393
# Unit test for function test
def test_test():
    test()



# Generated at 2022-06-13 17:54:41.888582
# Unit test for function escape
def test_escape():  # type: ignore
    # Various escape matches
    assert escape(re.match(r"\\x[0-9A-Fa-f]{2}", r"\x4f")) == "O"
    assert escape(re.match(r"\\[0-9]{3}", r"\040")) == " "
    assert escape(re.match(r"\\(?P<thing>.", r"\a")) == "\a"
    assert escape(re.match(r"\\(?P<thing>.", r'\"')) == '"'
    assert escape(re.match(r"\\(?P<thing>.", r"\\")) == "\\"
    # Non-matches
    assert escape(re.match(r"[xyz]", "x")) == "x"

# Generated at 2022-06-13 17:54:52.055857
# Unit test for function escape
def test_escape():
    import unittest
    from warnings import catch_warnings
    from test.support import captured_stdout, captured_stderr

    class EscapeTests(unittest.TestCase):
        def test_single_char_escapes(self):
            # test single-character escapes
            s = "abfnrtv'" + '"'
            e = str(s)
            self.assertEqual(escape(re.match(r"\\", "\\")), "\\")
            self.assertEqual(escape(re.match(r"\\", "\\a")), "\a")
            for i in range(len(s)):
                self.assertEqual(escape(re.match(r"\\.", "\\" + s[i])), s[i])


# Generated at 2022-06-13 17:54:59.101567
# Unit test for function escape
def test_escape():
    """
    Test escape function
    """

    assert escape(re.match(r"\\a", r"\a")) == "\a"
    assert escape(re.match(r"\\b", r"\b")) == "\b"
    assert escape(re.match(r"\\f", r"\f")) == "\f"
    assert escape(re.match(r"\\n", r"\n")) == "\n"
    assert escape(re.match(r"\\r", r"\r")) == "\r"
    assert escape(re.match(r"\\t", r"\t")) == "\t"
    assert escape(re.match(r"\\v", r"\v")) == "\v"
    assert escape(re.match(r"\\'", r"\'")) == "\'"

# Generated at 2022-06-13 17:55:01.486726
# Unit test for function escape
def test_escape():
    assert escape(re.search(r'\\f', '\f')) == '\f'

# Generated at 2022-06-13 17:55:16.957448
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

# Generated at 2022-06-13 17:55:17.679178
# Unit test for function test
def test_test():
    test()



# Generated at 2022-06-13 17:55:18.194211
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:19.766977
# Unit test for function escape
def test_escape():
    assert escape('\\"') == '"'
    assert escape('\\a') == '\a'

# Generated at 2022-06-13 17:55:20.866828
# Unit test for function test
def test_test():
    test() # doctest: +ELLIPSIS


# Generated at 2022-06-13 17:55:35.686500
# Unit test for function escape
def test_escape():
    simple_escape_examples = [
        ("\\a", "\a"),
        ("\\f", "\f"),
        ("\\b", "\b"),
        ("\\n", "\n"),
        ("\\r", "\r"),
        ("\\t", "\t"),
        ("\\v", "\v"),
        ("\\'", "'"),
        ('\\"', '"'),
        ("\\\\", "\\"),
    ]
    for (s, c) in simple_escape_examples:
        m = re.match(r"\\(.)$", s)
        assert escape(m) == c


# Generated at 2022-06-13 17:56:09.491735
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:18.153874
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\n")) == "\n"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\x23")) == "#"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\x2")) == r"\x2"

# Generated at 2022-06-13 17:56:19.347795
# Unit test for function test
def test_test():
    # Just run test()
    test()

# Generated at 2022-06-13 17:56:25.175410
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})",
                           "\\x61")) == 'a'
    # test the invalid octal string escape
    with pytest.raises(ValueError):
        escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})",
                        "\\8"))



# Generated at 2022-06-13 17:56:28.318333
# Unit test for function escape
def test_escape():
    text = r"\x23 \234 \0 \12 \a"
    assert escape(('\\x23', 'x23')) == r"\x23"
    assert escape(('\\234', '234')) == r"\234"
    assert escape(('\\0', '0')) == "\0"
    assert escape(('\\12', '12')) == "\12"
    assert escape(('\\a', 'a')) == "\a"



# Generated at 2022-06-13 17:56:30.094078
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:34.715217
# Unit test for function escape
def test_escape():
    # We don't want the escape function to make a match object but rather
    # return the string that should replace the match.  We'll cheat a
    # little.
    m = re.match('foo', 'foo')

    assert escape(m) == 'foo'

    # TODO:
    # Test each escape sequence
    # Test for valid string escapes
    # Test for invalid character escapes

# Generated at 2022-06-13 17:56:35.275791
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:44.194329
# Unit test for function escape
def test_escape():
    # Unit tests for the escape() function
    assert escape(re.match(r'\\a', '\a')) == '\a'
    assert escape(re.match(r'\\b', '\b')) == '\b'
    assert escape(re.match(r'\\f', '\f')) == '\f'
    assert escape(re.match(r'\\n', '\n')) == '\n'
    assert escape(re.match(r'\\r', '\r')) == '\r'
    assert escape(re.match(r'\\t', '\t')) == '\t'
    assert escape(re.match(r'\\v', '\v')) == '\v'
    assert escape(re.match(r"\\'", "'")) == "'"

# Generated at 2022-06-13 17:56:49.015044
# Unit test for function test
def test_test():
    import StringIO

    buf = StringIO.StringIO()
    save_stdout = sys.stdout
    sys.stdout = buf
    try:
        test()
    finally:
        sys.stdout = save_stdout

    assert buf.getvalue() == ""


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 17:58:03.473800
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"^\\(.)", r'\x7F')) == chr(0x7F)
    assert escape(re.match(r"^\\(.)", r'\x1F')) == chr(0x1F)
    assert escape(re.match(r"^\\(.)", r'\x0F')) == chr(0x0F)
    assert escape(re.match(r"^\\(.)", r'\x00')) == chr(0)
    assert escape(re.match(r"^\\(.)", r'\0')) == chr(0)
    assert escape(re.match(r"^\\(.)", r'\127')) == chr(0o127)

# Generated at 2022-06-13 17:58:05.935940
# Unit test for function test
def test_test():
    test()
    import pytest
    with pytest.raises(AssertionError):
        test()
    with pytest.raises(AssertionError):
        test()

# Generated at 2022-06-13 17:58:08.068869
# Unit test for function escape
def test_escape():
    test_cases = [
        ("\\'", "'"),
        ("\\u1234", "\u1234"),
        ("\\U00012345", "\U00012345"),
        ("\\x32", "2"),
        (r"\\", "\\"),
    ]

    for test_case in test_cases:
        assert escape(test_case[0]) == test_case[1]

# Generated at 2022-06-13 17:58:17.285600
# Unit test for function escape
def test_escape():
    test_string = "a\\b'c\\\nd\\xe4\\055\\n\\077\\100\\o100"

    r"""
    test_string_exp = "a\bc'd\xe4-\n?\x80\o100"
    test_string_exp = evalString(test_string)
    """
    test_string_exp = "a\bc'dä-\n?Ø\o100"
    assert escape(re.match(r"\\(.)", test_string)) == "a"
    assert escape(re.match(r"\\(.)", test_string)) == "a"
    assert escape(re.match(r"\\(.)", test_string)) == "b"
    assert escape(re.match(r"\\(.)", test_string)) == "'"

# Generated at 2022-06-13 17:58:28.049917
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

# Generated at 2022-06-13 17:58:28.847962
# Unit test for function test
def test_test():
    pass


# Generated at 2022-06-13 17:58:39.423093
# Unit test for function escape
def test_escape():
    assert escape('\\a')
    assert escape('\\x') == 'x'
    assert escape('\\0')
    assert escape('\\1')
    assert escape('\\2')
    assert escape('\\3')
    assert escape('\\4')
    assert escape('\\5')
    assert escape('\\6')
    assert escape('\\7')
    assert escape('\\8') == '8'
    assert escape('\\9') == '9'
    assert escape('\\b')
    assert escape('\\n')
    assert escape('\\r')
    assert escape('\\t')
    assert escape('\\v')
    assert escape('\\f')
    assert escape('\\\'')
    assert escape('\\"')
    assert escape('\\\\')
    assert escape('\\x1')
    assert escape('\\x12')
   

# Generated at 2022-06-13 17:58:47.090707
# Unit test for function escape
def test_escape():
    # Test simple escape
    assert escape({'0': 'a', 'group': {'0': 'a'}, 'groups': ('a',),
                   'string': '\\a'}) == "\a"
    assert escape({'0': 'a', 'group': {'0': 'a'}, 'groups': ('a',),
                   'string': '\\a'}) == "\a"

    # Test octal escape
    assert escape({'0': '000', 'group': {'0': '000'}, 'groups': ('000',),
                   'string': '\\000'}) == "\x00"
    assert escape({'0': '010', 'group': {'0': '010'}, 'groups': ('010',),
                   'string': '\\010'}) == "\x08"

# Generated at 2022-06-13 17:58:53.020757
# Unit test for function escape
def test_escape():
    assert escape("\\b") == "\b"
    assert escape("\\x61") == "a"
    assert escape("\\x61\\x62") == "ab"
    assert escape("\\x61\\x62\\x63") == "abc"
    assert escape("\\x61\\x62\\x63\\x64") == "abcd"
    assert escape("\\x61\\x62\\x63\\x64\\x65") == "abcde"
    assert escape("\\x61\\x62\\x63\\x64\\x65\\x66") == "abcdef"
    assert escape("\\x61\\x62\\x63\\x64\\x65\\x66\\x67") == "abcdefg"

# Generated at 2022-06-13 17:58:57.072613
# Unit test for function escape
def test_escape():
    for i in range(256):
        c = chr(i)
        if c not in simple_escapes:
            assert escape(re.search(r"\\x{:02x}".format(i), c)) == c
            assert escape(re.search(r"\\{:03o}".format(i), c)) == c
    assert escape(re.search(r"\\x", 'x')) == 'x'
    assert escape(re.search(r"\\0", '0')) == '0'

