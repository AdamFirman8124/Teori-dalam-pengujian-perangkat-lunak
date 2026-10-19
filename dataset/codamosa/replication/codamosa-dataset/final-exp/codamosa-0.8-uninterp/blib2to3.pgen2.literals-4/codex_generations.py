

# Generated at 2022-06-13 17:50:03.925747
# Unit test for function escape
def test_escape():
    from typing import Pattern, Any, Iterable

    from hypothesis import given, assume, example, settings

    from .regex_strategies import regex_strings, regexs
    from . import verify_hypothesis_regex_strategies_match_examples

    @settings(max_examples=200)
    @given(regex_strings())
    def test_escape_example(regex: Text) -> None:
        assume(regex.startswith("\\"))
        # cannot have "inside a set" in regex
        # if not regex.startswith("\\[") and not regex.startswith("\\{"): # type: Any

# Generated at 2022-06-13 17:50:16.021994
# Unit test for function evalString
def test_evalString():

    # Simple tests
    assert evalString(r'"a"') == "a"
    assert evalString(r"u'a'") == "a"
    assert evalString(r"'a'") == "a"
    assert evalString(r'"\r"') == "\r"
    assert evalString(r"'\r'") == "\r"

    # Test various escape sequences

# Generated at 2022-06-13 17:50:20.319671
# Unit test for function escape

# Generated at 2022-06-13 17:50:29.595289
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x", "\\x")) == "x"
    assert escape(re.match(r"\\x", "\\x")) == "x"
    assert escape(re.match(r"\\0", "\\0")) == "\x00"
    assert escape(re.match(r"\\0", "\\07")) == "\x07"
    assert escape(re.match(r"\\0", "\\01")) == "\x01"
    assert escape(re.match(r"\\0", "\\012")) == "\x0a"
    assert escape(re.match(r"\\0", "\\012")) == "\x0a"
    assert escape(re.match(r"\\07", "\\077")) == "\x3f"

# Generated at 2022-06-13 17:50:41.104202
# Unit test for function escape
def test_escape():
    m = re.match("\\A\\x06", '\x06')
    assert escape(m) == "\\x06"

    m = re.match("\\A\\x06\\x07", '\x06')    
    e = escape(m)
    assert e == "\\x06"

    m = re.match("\\A\\06", '\x06')
    assert escape(m) == "\\06"

    m = re.match("\\A\\06\\07", '\x06')    
    e = escape(m)
    assert e == "\\06"

    m = re.match("\\A\\06\\07", '\x06\x07')    
    e = escape(m)
    assert e == "\\06\\07"


# Generated at 2022-06-13 17:50:42.408545
# Unit test for function test
def test_test():
    """Just make sure test() doesn't blow up"""
    test()

# Generated at 2022-06-13 17:50:53.833751
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\x\d\d", "\\x1a")) == '\x1a'
    assert escape(re.search(r"\\x\d\d", "\\x1a")) != '\x1b'
    assert escape(re.search(r"\\x\d\d", "\\x1a")) != '\\x1a'
    assert escape(re.search(r"\\x\d\d", "\\x1a")) != '1a'
    assert escape(re.search(r"\\x\d\d", "\\x1a")) != '\u001a'

    assert escape(re.search(r"\\\d\d\d", "\\033")) == '\x1b'

# Generated at 2022-06-13 17:51:02.657277
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\'")) == "'"
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", '\\"')) == '"'
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\\\")) == "\\"

# Generated at 2022-06-13 17:51:08.457250
# Unit test for function escape
def test_escape():
    from hypothesis import given
    from hypothesis import strategies as st

    @given(st.text(min_size=1).filter(lambda s: s.startswith("\\")))
    def test_simples(s):
        res = escape(re.match("\\(.*)", s))
        assert res == simple_escapes.get(s[1:], "")

    @given(st.text(min_size=1).filter(lambda s: s.startswith("\\x")))
    def test_hex(s):
        match = re.match("\\(x.*)", s)
        assert match
        x = s[2:]
        try:
            int(x, 16)
        except ValueError:
            with pytest.raises(ValueError):
                escape(match)

# Generated at 2022-06-13 17:51:20.602238
# Unit test for function escape
def test_escape():

    def test_escape_simple(m):
        all, tail = m.group(0, 1)
        assert all.startswith("\\")
        assert all == "\\" + tail
        esc = simple_escapes.get(tail)
        assert esc == escape(m)

    test_escape_simple(re.match(r"\\(.)", "\\a"))
    test_escape_simple(re.match(r"\\(.)", "\\b"))
    test_escape_simple(re.match(r"\\(.)", "\\f"))
    test_escape_simple(re.match(r"\\(.)", "\\n"))
    test_escape_simple(re.match(r"\\(.)", "\\r"))
    test_escape_simple(re.match(r"\\(.)", "\\t"))

# Generated at 2022-06-13 17:51:36.360246
# Unit test for function escape
def test_escape():
    for i in range(256):
        c = chr(i)
        s = r"\%03o" % i
        e = escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", s))
        if e != c:
            print(i, c, s, e)



# Generated at 2022-06-13 17:51:38.407448
# Unit test for function escape
def test_escape():
    m = re.match(r"", r"")
    m.group = lambda a, b=None: ["\\n", "n"]
    assert escape(m) == "\n"

# Generated at 2022-06-13 17:51:48.525113
# Unit test for function escape
def test_escape():
    tests = {
        '\\a':"\a",
        '\\b':"\b",
        '\\f':"\f",
        '\\n':"\n",
        '\\r':"\r",
        '\\t':"\t",
        '\\v':"\v",
        '\\\'':"'",
        '\\"':'"',
        '\\\\':"\\",
        '\\x61':"a",
        '\\x7a':"z",
        '\\102':"B",
        '\\172':"z",
        '\\13':"\r",
        '\\012':"\n",
        '\\377':"\xff",
    }

# Generated at 2022-06-13 17:51:58.485439
# Unit test for function escape

# Generated at 2022-06-13 17:52:02.792753
# Unit test for function escape
def test_escape():
    assert escape("\\") == "\\"
    assert escape("\\n") == "\n"
    assert escape("\\x0a") == "\n"
    assert escape("\\07") == "\a"
    assert escape("\\007") == "\x07"
    assert escape("\\077") == "?"
    assert escape("\\377") == "?"

# Generated at 2022-06-13 17:52:10.635417
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\'", r"\'")) is "'"
    assert escape(re.match('\\"', r'\"')) is '"'
    assert escape(re.match("\\\\", r"\\")) is "\\"
    assert escape(re.match("\\x61", r"\x61")) is "a"
    assert escape(re.match("\\x61", r"\x6")) is ValueError
    assert escape(re.match("\\x61", r"\x611")) is ValueError
    assert escape(re.match("\\x61", r"\x61t")) is ValueError

# Generated at 2022-06-13 17:52:18.299371
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})$", r"\t")) == '\t'
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})$", r"\n")) == '\n'
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})$", r"\v")) == '\x0b'

# Generated at 2022-06-13 17:52:20.535861
# Unit test for function escape
def test_escape():
    m = re.match(r"\\(.')", "'\\''")
    assert escape(m) == "'"


# Generated at 2022-06-13 17:52:29.685267
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\0")) == "\0"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\00")) == "\0"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\000")) == "\0"

# Generated at 2022-06-13 17:52:38.325914
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", "\\a")) == "\a"
    assert escape(re.match(r"\\(.)", "\\b")) == "\b"
    assert escape(re.match(r"\\(.)", "\\f")) == "\f"
    assert escape(re.match(r"\\(.)", "\\n")) == "\n"
    assert escape(re.match(r"\\(.)", "\\r")) == "\r"
    assert escape(re.match(r"\\(.)", "\\t")) == "\t"
    assert escape(re.match(r"\\(.)", "\\v")) == "\v"
    assert escape(re.match(r"\\(.)", "\\'")) == "\'"

# Generated at 2022-06-13 17:53:03.259320
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\a', r'\a')) == '\a'
    assert escape(re.match('\\b', r'\b')) == '\b'
    assert escape(re.match('\\f', r'\f')) == '\f'
    assert escape(re.match('\\n', r'\n')) == '\n'
    assert escape(re.match('\\r', r'\r')) == '\r'
    assert escape(re.match('\\t', r'\t')) == '\t'
    assert escape(re.match('\\v', r'\v')) == '\v'
    assert escape(re.match("\\'", r"\'")) == "'"

# Generated at 2022-06-13 17:53:05.292135
# Unit test for function evalString
def test_evalString():
    print(evalString('"abc"x'))
    print(evalString('"abc"'))

# Generated at 2022-06-13 17:53:08.988347
# Unit test for function escape
def test_escape():
    def test(input, expected_output):
        assert escape(re.match(r"\\"+input, "")) == expected_output

    test("x1F", '\x1f')
    test("x99", '\x99')
    test("x63", '\x63')


# Generated at 2022-06-13 17:53:13.940992
# Unit test for function escape
def test_escape():
    assert escape(r"\t") == "\t"
    assert escape(r"\n") == "\n"
    assert escape(r"\x41") == "\x41"
    assert escape(r"\x4F") == "\x4F"
    assert escape(r"\x41A") == "\x41" + "A"
    assert escape(r"\077") == "\x3F"
    assert escape(r"\777") == "\x3F"
    assert escape(r"\7777") == "\x3F"

# Generated at 2022-06-13 17:53:24.507956
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r'\a')) == "\a"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r'\b')) == "\b"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r'\f')) == "\f"

# Generated at 2022-06-13 17:53:25.069315
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:28.712486
# Unit test for function escape
def test_escape():
    assert escape("\\n") == "\n"
    assert escape("\\x00") == "\0"
    assert escape("\\xFF") == "\xFF"
    assert escape("\\377") == "\377"
    assert escape("\\500") == "\500"
    assert escape("\\21") == "\21"
    assert escape("\\9") == "\9"

# Generated at 2022-06-13 17:53:35.021283
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\a")) == "\a"
    assert escape(re.search(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\b")) == "\b"
    assert escape(re.search(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\f")) == "\f"

# Generated at 2022-06-13 17:53:45.802882
# Unit test for function evalString
def test_evalString():
    assert evalString("'\\x61'") == 'a'
    assert evalString("'\\x00'") == '\x00'
    assert evalString("'\\n'") == '\n'
    assert evalString("'bob'") == 'bob'
    assert evalString("'bob \\'\\\\\\' bobby'") == 'bob \'\\\' bobby'
    assert evalString("'bob \\' bobby'") == 'bob \' bobby'
    assert evalString("'\\x61 \\' bobby'") == 'a \' bobby'
    assert evalString("'\\'") == '\''
    assert evalString("'\\\\'") == '\\'
    assert evalString("'\\\\\\\\'") == '\\\\'
    assert evalString("'\\\\\\''") == '\\\''

# Generated at 2022-06-13 17:53:59.369154
# Unit test for function escape
def test_escape():
    from pythonparser import utils
    assert utils.escape(r"\a") == "\a"
    assert utils.escape(r"\b") == "\b"
    assert utils.escape(r"\f") == "\f"
    assert utils.escape(r"\v") == "\v"
    assert utils.escape(r"\t") == "\t"
    assert utils.escape(r"\r") == "\r"
    assert utils.escape(r"\n") == "\n"
    assert utils.escape(r"\'") == "'"
    assert utils.escape(r'"') == '"'
    assert utils.escape(r"\xFF") == chr(0xFF)
    assert utils.escape(r"\377") == chr(0xFF)


# Generated at 2022-06-13 17:54:34.784349
# Unit test for function escape
def test_escape():
    assert escape("\a") == "\a"
    assert escape("\b") == "\b"
    assert escape("\f") == "\f"
    assert escape("\n") == "\n"
    assert escape("\r") == "\r"
    assert escape("\t") == "\t"
    assert escape("\v") == "\v"
    assert escape("\'") == "\'"
    assert escape('\"') == '\"'
    assert escape("\\") == "\\"

    assert escape("\x20") == " "
    assert escape("\x7F") == chr(0x7F)
    assert escape("\x80") == chr(0x80)
    assert escape("\xFF") == chr(0xFF)

    assert escape("\000") == chr(0)

# Generated at 2022-06-13 17:54:44.265834
# Unit test for function escape
def test_escape():
    # pylint: disable=unused-variable
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\x7f")) == "\x7f"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\3")) == "\x03"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\'foo'")) == "\'foo\'"

# Generated at 2022-06-13 17:54:53.995881
# Unit test for function escape
def test_escape():
    m_groups = ("\\x23", "x23")
    m = re.match("(\\x23)", "x23")
    m.groups = m_groups
    assert escape(m) == "#"

    m_groups = ("\\v", "v")
    m = re.match("(\\v)", "v")
    m.groups = m_groups
    assert escape(m) == "\v"

    m_groups = ("\\'", "'")
    m = re.match("(\\')", "'")
    m.groups = m_groups
    assert escape(m) == "'"

    try:
        m_groups = ("\\", "")
        m = re.match("(\\)", "")
        m.groups = m_groups
        escape(m)
    except ValueError:
        pass

# Generated at 2022-06-13 17:55:05.166256
# Unit test for function escape
def test_escape():
    # Non-printable characters
    assert escape(re.match(r"\\n", r"\n")) == "\n"
    assert escape(re.match(r"\\x20", r"\x20")) == " "
    # Special characters
    assert escape(re.match(r"\\\'", r"\'")) == "'"
    assert escape(re.match(r'\\\"', r'\"')) == '"'
    assert escape(re.match(r"\\\\", r"\\")) == "\\"
    # Octal escapes
    assert escape(re.match(r"\\0", r"\0")) == "\x00"
    assert escape(re.match(r"\\7", r"\7")) == "\x07"

# Generated at 2022-06-13 17:55:07.860584
# Unit test for function escape
def test_escape():
	assert escape("\\x41") == "A"
	assert escape("\\123") == "{"

# Generated at 2022-06-13 17:55:15.919578
# Unit test for function escape
def test_escape():
    escaped_strings = [
        (b"\\", b"\\"),
        (b"\\x00", b"\\x00"),
        (b"\\00", b"\\00"),
    ]

    for escaped_string in escaped_strings:
        result = escape(re.match(r"\\(.+)", escaped_string[0]))
        assert result == escaped_string[1]
        # print(result)

# Generated at 2022-06-13 17:55:24.126902
# Unit test for function escape
def test_escape():
    assert escape("\\a").encode("utf-8") == b"\x07"
    assert escape("\\b").encode("utf-8") == b"\x08"
    assert escape("\\f").encode("utf-8") == b"\x0c"
    assert escape("\\n").encode("utf-8") == b"\x0a"
    assert escape("\\r").encode("utf-8") == b"\x0d"
    assert escape("\\t").encode("utf-8") == b"\x09"
    assert escape("\\v").encode("utf-8") == b"\x0b"
    assert escape("\\'").encode("utf-8") == b"'"
    assert escape('\\"').encode("utf-8") == b'"'
    assert escape

# Generated at 2022-06-13 17:55:28.766686
# Unit test for function escape
def test_escape():
    for i in range(256):
        c = chr(i)
        s = repr(c)
        assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", s)) == c



# Generated at 2022-06-13 17:55:32.309047
# Unit test for function evalString
def test_evalString():
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c

# Generated at 2022-06-13 17:55:40.090429
# Unit test for function escape
def test_escape():
    import unittest
    import re
    from . import stringlike

    class EscapeTest(unittest.TestCase):
        # Tests for the escape() function

        def test_simple_escape(self):
            # Test that simple backslash characters are handled properly
            m = re.match(r"\\(a|b|f|n|r|t|v|'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\a")
            s = stringlike.escape(m)
            self.assertEqual(s, "\a", "\\a didn't escape")


# Generated at 2022-06-13 17:56:13.556469
# Unit test for function escape
def test_escape():
    def _test_escape(all, tail, expected):
        class M:
            def group(self, i):
                return (all, tail)[i]

        assert escape(M()) == expected

    # Test octal escapes
    _test_escape('\\1', '1', '\001')
    _test_escape('\\11', '11', '\011')
    _test_escape('\\111', '111', 'I')

    # Test illegal octal escapes
    try:
        _test_escape('\\8', '8', '')
    except ValueError:
        pass
    else:
        assert False

    # Test hex escapes
    _test_escape('\\x1', 'x1', '\x01')
    _test_escape('\\x11', 'x11', '\x11')
    _test_escape

# Generated at 2022-06-13 17:56:14.328141
# Unit test for function test
def test_test():
  test()
  assert True

# Generated at 2022-06-13 17:56:23.742623
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\.", "\\a")) == "\a"
    assert escape(re.match(r"\\.", "\\b")) == "\b"
    assert escape(re.match(r"\\.", "\\f")) == "\f"
    assert escape(re.match(r"\\.", "\\n")) == "\n"
    assert escape(re.match(r"\\.", "\\r")) == "\r"
    assert escape(re.match(r"\\.", "\\t")) == "\t"
    assert escape(re.match(r"\\.", "\\v")) == "\v"
    assert escape(re.match(r"\\.", "\\'")) == "'"
    assert escape(re.match(r"\\.", '\\"')) == '"'

# Generated at 2022-06-13 17:56:34.762399
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\'", "'")) == "'"
    assert escape(re.match("\\'", "\\'")) == '\\'
    assert escape(re.match("\\\\", "\\")) == "\\"

    # test non-octal number
    try:
        escape(re.match("\\7", "\\7"))
    except ValueError:
        pass
    else:
        raise AssertionError("non-octal number did not raise ValueError")

    # test octal number with invalid digit
    try:
        escape(re.match("\\71", "\\71"))
    except ValueError:
        pass
    else:
        raise AssertionError("octal number with invalid digit did not raise ValueError")

    # test octal number with too many digits

# Generated at 2022-06-13 17:56:35.671746
# Unit test for function test
def test_test():
    assert test() == None



# Generated at 2022-06-13 17:56:44.470450
# Unit test for function escape
def test_escape():
    assert escape("\\b") == "\b"
    assert escape("\\t") == "\t"
    assert escape("\\n") == "\n"
    assert escape("\\v") == "\v"
    assert escape("\\f") == "\f"
    assert escape("\\r") == "\r"
    assert escape("\\x20") == " "
    assert escape("\\0") == "\x00"
    assert escape("\\1") == "\x01"
    assert escape("\\2") == "\x02"
    assert escape("\\00") == "\x00"
    assert escape("\\01") == "\x01"
    assert escape("\\02") == "\x02"
    assert escape("\\10") == "\x08"
    assert escape("\\011") == "\x09"

# Generated at 2022-06-13 17:56:53.972604
# Unit test for function escape
def test_escape():
    from pytest import raises

    # Test the valid escapes

# Generated at 2022-06-13 17:57:02.530173
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x", '\\x')) == '\\x'
    assert escape(re.match(r"\\a", '\\a')) == '\a'
    assert escape(re.match(r"\\b", '\\b')) == '\b'
    assert escape(re.match(r"\\f", '\\f')) == '\f'
    assert escape(re.match(r"\\n", '\\n')) == '\n'
    assert escape(re.match(r"\\r", '\\r')) == '\r'
    assert escape(re.match(r"\\t", '\\t')) == '\t'
    assert escape(re.match(r"\\v", '\\v')) == '\v'

# Generated at 2022-06-13 17:57:16.605867
# Unit test for function escape
def test_escape():
    m = re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\xab")
    assert escape(m) == chr(0xab)
    m = re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\0o0")
    assert escape(m) == chr(0)
    m = re.match(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\0o0")
    assert escape(m) == chr(0)

# Generated at 2022-06-13 17:57:24.924999
# Unit test for function escape

# Generated at 2022-06-13 17:57:44.230238
# Unit test for function escape
def test_escape():
    import pytest
    with pytest.raises(ValueError) as excinfo:
        escape(re.match(r"\\", "\\"))
    assert "invalid" in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        escape(re.match(r"\\x", "\\x"))
    assert "invalid" in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        escape(re.match(r"\\[", "\\["))
    assert "invalid" in str(excinfo.value)
    assert escape(re.match(r"\\'", "\\'")) == "'"
    assert escape(re.match(r'\\"', '\\"')) == '"'

# Generated at 2022-06-13 17:57:57.695680
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\[abfnrtv]", r"\a")) == "\a"
    assert escape(re.match(r"\\x..", r"\x00")) == "\x00"
    assert escape(re.match(r"\\0..", r"\000")) == "\000"
    try:
        escape(re.match(r"\\.", r"\q"))
    except ValueError as e:
        assert str(e) == "invalid string escape ('\\q')"
    try:
        escape(re.match(r"\\x..", r"\x0"))
    except ValueError as e:
        assert str(e) == "invalid hex string escape ('\\x0')"

# Generated at 2022-06-13 17:58:03.826028
# Unit test for function escape
def test_escape():
    assert escape("\\x41") == "A"
    assert escape("\\x4A") == "J"
    assert escape("\\x4a") == "J"
    assert escape("\\xff") == "ÿ"
    assert escape("\\xff") == "\u00FF"
    assert escape("\\u1234") == "u1234"  # This is not a valid escape sequence, let's test.
    assert escape("\\666") == "o"  # This is not a valid escape sequence, let's test.



# Generated at 2022-06-13 17:58:07.927731
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\a', r'\a')) == '\a'
    assert escape(re.match('\\b', r'\b')) == '\b'
    assert escape(re.match('\\f', r'\f')) == '\f'
    assert escape(re.match('\\n', r'\n')) == '\n'
    assert escape(re.match('\\r', r'\r')) == '\r'
    assert escape(re.match('\\t', r'\t')) == '\t'
    assert escape(re.match('\\v', r'\v')) == '\v'
    assert escape(re.match('\\\'', r'\'')) == '\''

# Generated at 2022-06-13 17:58:17.168063
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", r"\a")) == "\a"
    assert escape(re.match(r"\\(.)", r"\b")) == "\b"
    assert escape(re.match(r"\\(.)", r"\f")) == "\f"
    assert escape(re.match(r"\\(.)", r"\n")) == "\n"
    assert escape(re.match(r"\\(.)", r"\r")) == "\r"
    assert escape(re.match(r"\\(.)", r"\t")) == "\t"
    assert escape(re.match(r"\\(.)", r"\v")) == "\v"
    assert escape(re.match(r"\\(.)", r"\\")) == "\\"

# Generated at 2022-06-13 17:58:17.637369
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:28.451087
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\a")) == "\a"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\b")) == "\b"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\f")) == "\f"

# Generated at 2022-06-13 17:58:34.171091
# Unit test for function escape
def test_escape():
    print("----- Testing function escape -----")
    result = escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\\""))
    assert result == "\""

    result = escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\\'"))
    assert result == "'"

    result = escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\\x09"))
    assert result == "\x09"


# Generated at 2022-06-13 17:58:35.529229
# Unit test for function test
def test_test():
    try:
        test()
    except NameError:
        print("test_test failed")

# Generated at 2022-06-13 17:58:43.874065
# Unit test for function escape
def test_escape():
    """Test that function escape works correctly
       Input:
           [7, "a", "b", "f", "n", "r", "t", "v",
            "'", '"', "\\", "x01", "xba", "x00",
            "000", "777", "083", "0o83", "0o782", "0x1a"]
       Expected output:
           ["\a", "\b", "\f", "\n", "\r", "\t", "\v", "'", '"', "\\",
            "\x01", "\xba", "\x00", "\x00", "\x3f", "\x03", "\x03",
            "\x03", "\x03", "\x1a"]
    """

# Generated at 2022-06-13 17:59:15.558198
# Unit test for function test
def test_test():
    assert test() is None

# Generated at 2022-06-13 17:59:24.906460
# Unit test for function escape
def test_escape():
    res = escape(re.search(r"[abfnrtv]", "\\b"))
    assert res == "\b"

    res = escape(re.search(r"x.{0,2}", "\\x12"))
    assert res == "\x12"

    res = escape(re.search(r"[0-7]{1,3}", "\\7"))
    assert res == "\7"

    # Error message is better than an exception thrown at runtime
    assert "invalid octal string escape" in str(escape.__code__)
    assert "invalid hex string escape" in str(escape.__code__)

# Generated at 2022-06-13 17:59:32.835167
# Unit test for function escape
def test_escape():
    def check_escape(s, t):
        """Make sure escape(s) is t"""
        m = re.match(r'\\(.?)', s)
        assert t == escape(m)

    check_escape("\\x00", "\x00")
    check_escape("\\00", "\x00")
    check_escape("\\377", "\xff")
    check_escape("\\xFF", "\xff")
    check_escape("\\v", "\x0b")
    check_escape("\\x0a", "\n")
    check_escape("\\a", "\a")
    check_escape("\\0", "\x00")
    check_escape("\\1", "\x01")
    check_escape("\\11", "\t")
    check_escape("\\12", "\n")