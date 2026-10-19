

# Generated at 2022-06-13 17:50:04.319428
# Unit test for function escape
def test_escape():
    test_cases = [
        ("\\x41", "A"),
        ("\\x61", "a"),
        ("\\b", "\b"),
        ("\\f", "\f"),
        ("\\n", "\n"),
        ("\\r", "\r"),
        ("\\t", "\t"),
        ("\\v", "\v"),
    ]
    for tc in test_cases:
        assert escape(re.match(r"\\[xabfnrtv]|[xabfnrtv]", tc[0])) == tc[1], tc

# Generated at 2022-06-13 17:50:05.046790
# Unit test for function test
def test_test():
    assert test() is None

# Generated at 2022-06-13 17:50:13.340023
# Unit test for function escape
def test_escape():
    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\v'
    assert escape('\\\'') == '\''
    assert escape('\\"') == '"'
    assert escape('\\\\') == '\\'



# Generated at 2022-06-13 17:50:19.956136
# Unit test for function escape
def test_escape():
   assert escape('\\a') == '\a'
   assert escape('\\b') == '\b'
   assert escape('\\f') == '\f'
   assert escape('\\n') == '\n'
   assert escape('\\r') == '\r'
   assert escape('\\t') == '\t'
   assert escape('\\v') == '\v'
   assert escape('\\\'') == '\''
   assert escape('\\"') == '"'
   assert escape('\\\\') == '\\'
   assert escape('\\x41') == 'A'
   assert escape('\\x61') == 'a'
   assert escape('\\x1c') == '\x1c'
   assert escape('\\x6e') == 'n'

# Generated at 2022-06-13 17:50:25.101873
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x12", "\\x12")) == '\x12'
    assert escape(re.match(r"\\x2", "\\x2")) == '\\x2'
    assert escape(re.match(r"\\12", "\\12")) == '\n'
    assert escape(re.match(r"\\2", "\\2")) == '\\2'
    assert escape(re.match(r"\\'", "\\'")) == "'"



# Generated at 2022-06-13 17:50:33.807862
# Unit test for function evalString
def test_evalString():
    print(evalString("'abc'"))
    print(evalString("'\\x61\\x62\\x63'")) # should be the same
    print(evalString("'\\141\\142\\143'")) # should be the same
    print(evalString("'\\n\\t\\r\\b\\a\\f\\v'"))
    print(evalString("'\\x01\\x02\\x03\\x04\\x05\\x06'"))
    print(evalString("'\\x01\\x02\\x03\\x04\\x05\\x06\\x07'"))
    assert evalString("'\\x01\\x02\\x03\\x04\\x05\\x06\\x07'") == '\x01\x02\x03\x04\x05\x06\x07'

# Generated at 2022-06-13 17:50:42.858884
# Unit test for function escape

# Generated at 2022-06-13 17:50:54.220129
# Unit test for function evalString
def test_evalString():
    class _AssertRaisesContext:
        def __init__(self, exc, *args, **kwargs):
            self.exc = exc

        def __enter__(self, *args, **kwargs):
            return self

        def __exit__(self, *args, **kwargs):
            return 1

        def __getattr__(self, *args, **kwargs):
            return 1

    _assertRaises = _AssertRaisesContext(ValueError)

    # evalString should accept the same strings as eval()

    def test(s):
        return evalString(s) == eval(s)

    assert test("'hi'")
    assert test('"hi"')
    assert test("'''hi'")
    assert test('"""hi"')
    assert test("'\\''")

# Generated at 2022-06-13 17:51:02.076560
# Unit test for function escape
def test_escape():
    assert escape(re.match(r".*\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\a")) == '\a'
    assert escape(re.match(r".*\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\b")) == '\b'
    assert escape(re.match(r".*\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\f")) == '\x0c'


# Generated at 2022-06-13 17:51:02.611131
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:51:19.845083
# Unit test for function escape
def test_escape():
    """Test escape funtion

    >>> escape('\\x12')
    '\\x12'
    >>> escape('\\001')
    '\\x01'
    >>> escape('\\a')
    '\\x07'
    >>> escape('\\xff')
    Traceback (most recent call last):
      ...
    ValueError: invalid hex string escape ('\\xff')
    >>> escape('\\0')
    Traceback (most recent call last):
      ...
    ValueError: invalid octal string escape ('\\0')
    """

# Generated at 2022-06-13 17:51:22.486991
# Unit test for function escape
def test_escape():
    test_str = '\\n'
    assert escape(test_str) == '\n'



# Generated at 2022-06-13 17:51:33.070780
# Unit test for function escape
def test_escape():
    test_data = [
        ("\\'", "'"),
        ("\\\"", '"'),
        ("\\a", "\u0007"),
        ("\\b", "\b"),
        ("\\f", "\f"),
        ("\\n", "\n"),
        ("\\r", "\r"),
        ("\\t", "\t"),
        ("\\v", "\u000b"),
        ("\\x1A", "\u001a"),
        ("\\33", "\u0033"),
        ("\\45", "\u0045"),
        ("\\0", "\u0000"),
        ("\\272", "\\272"),
        ("\\xH", "\\xH"),
        ("\\x", "\\x"),
    ]


# Generated at 2022-06-13 17:51:33.552384
# Unit test for function test
def test_test():
    assert test() == None

# Generated at 2022-06-13 17:51:42.967145
# Unit test for function escape
def test_escape():
    import pytest

    assert escape(re.match(r"(.*)\\a(.*)", r"foo\abar")) == "\a"
    with pytest.raises(AssertionError):
        escape(re.match(r"(.*)\\a(.*)", r"fooabar"))
    assert escape(re.match(r"(.*)\\\\(.*)", r"foo\\bar")) == "\\"
    with pytest.raises(AssertionError):
        escape(re.match(r"(.*)\\a(.*)", r"foo\\bar"))
    assert escape(re.match(r"(.*)\\x0d(.*)", r"foo\x0dbar")) == "\r"

# Generated at 2022-06-13 17:51:51.262340
# Unit test for function escape
def test_escape():
    matched = escape(re.match(r"\\a", "\\a"))
    assert matched == "\a"
    matched = escape(re.match(r"\\b", "\\b"))
    assert matched == "\b"
    matched = escape(re.match(r"\\f", "\\f"))
    assert matched == "\f"
    matched = escape(re.match(r"\\n", "\\n"))
    assert matched == "\n"
    matched = escape(re.match(r"\\r", "\\r"))
    assert matched == "\r"
    matched = escape(re.match(r"\\t", "\\t"))
    assert matched == "\t"
    matched = escape(re.match(r"\\v", "\\v"))
    assert matched == "\v"

# Generated at 2022-06-13 17:51:59.902069
# Unit test for function escape
def test_escape():
    # Test exception
    def test_exception(input, exception):
        try:
            escape(input)
        except ValueError as e:
            if str(e) != exception:
                print('FAILED: test_exception({}, {})'.format(input, exception))
        else:
            print('FAILED: test_exception({}, {})'.format(input, exception))

    # Tests
    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\v'

# Generated at 2022-06-13 17:52:09.629777
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\.', r"\'")) == "'"
    assert escape(re.match(r'\\.', r'\"')) == '"'
    assert escape(re.match(r'\\.', r"\\")) == "\\"
    assert escape(re.match(r'\\.', r'\a')) == '\a'
    assert escape(re.match(r'\\.', r'\b')) == '\b'
    assert escape(re.match(r'\\.', r'\f')) == '\f'
    assert escape(re.match(r'\\.', r'\n')) == '\n'
    assert escape(re.match(r'\\.', r'\r')) == '\r'

# Generated at 2022-06-13 17:52:16.958291
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\\s", "foo\\\nbar")) is None
    assert escape(re.search(r"\\x27", "foo\\x27bar")) == "'"
    assert escape(re.search(r"\\270", "foo\\270bar")) == "p"
    assert escape(re.search(r"\\2", "foo\\2bar")) == "\x02"
    assert escape(re.search(r"\\", "foo\\bar")) == "\\"
    assert escape(re.search(r"\\5", "foo\\5bar")) == "5"
    assert escape(re.search(r"\\f", "foo\\fbar")) == "\x0c"



# Generated at 2022-06-13 17:52:26.822835
# Unit test for function escape
def test_escape():
    escaped = []
    not_escaped = []
    for k, v in simple_escapes.items():
        escaped.append("\\{}".format(k))
        escaped.append("A\\{}Z".format(k))
        not_escaped.append("\\{}Z".format(k))
    # octal
    escaped.append("\\033Z")
    escaped.append("\\0Z")
    escaped.append("\\0033Z")
    escaped.append("\\0033Z")
    not_escaped.append("\\0800Z")
    not_escaped.append("\\0800Z")
    # hex
    escaped.append("\\x1a")
    escaped.append("\\x1aZ")
    not_escaped.append("\\xZZ")

# Generated at 2022-06-13 17:52:39.645214
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\a', r'\a')) == '\a'
    assert escape(re.match(r'\\b', r'\b')) == '\b'
    assert escape(re.match(r'\\f', r'\f')) == '\f'
    assert escape(re.match(r'\\n', r'\n')) == '\n'
    assert escape(re.match(r'\\r', r'\r')) == '\r'
    assert escape(re.match(r'\\t', r'\t')) == '\t'
    assert escape(re.match(r'\\v', r'\v')) == '\v'
    assert escape(re.match(r'\\\'', r'\'')) == '\''
   

# Generated at 2022-06-13 17:52:43.717106
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\', '\x1b[0msome\\text')) == '\\'
    assert escape(re.match('\\t', '\x1b[0msome\\ttext')) == '\t'

# Generated at 2022-06-13 17:52:53.994137
# Unit test for function escape
def test_escape():
    assert escape("\\a") == "\a", "simple escapes are working"
    assert escape("\\b") == "\b", "simple escapes are working"
    assert escape("\\f") == "\f", "simple escapes are working"
    assert escape("\\n") == "\n", "simple escapes are working"
    assert escape("\\r") == "\r", "simple escapes are working"
    assert escape("\\t") == "\t", "simple escapes are working"
    assert escape("\\v") == "\v", "simple escapes are working"
    assert escape("\\'") == "'", "simple escapes are working"
    assert escape('\\"') == '"', "simple escapes are working"
    assert escape("\\\\") == "\\", "simple escapes are working"

    # assert escape("\\a") == "\a", "simple escapes are working"

# Generated at 2022-06-13 17:53:04.471109
# Unit test for function escape
def test_escape():

    if escape(re.match('\\n', '\n')) != '\n':
        raise AssertionError
    if escape(re.match('\\\\(\\\\\\\\)', '\\')) != '\\':
        raise AssertionError
    if escape(re.match('\\a', '\a')) != '\a':
        raise AssertionError
    if escape(re.match('\\b', '\b')) != '\b':
        raise AssertionError
    if escape(re.match('\\f', '\f')) != '\f':
        raise AssertionError
    if escape(re.match('\\r', '\r')) != '\r':
        raise AssertionError
    if escape(re.match('\\t', '\t')) != '\t':
        raise Ass

# Generated at 2022-06-13 17:53:06.485291
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x1234", "\\x1234")) == "\u1234"

# Generated at 2022-06-13 17:53:07.086030
# Unit test for function test
def test_test():
    pass

# Generated at 2022-06-13 17:53:14.500767
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\[abfnrtv]', '\\')) == '\\', 'backslash'
    assert escape(re.match(r'\\[abfnrtv]', '\\a')) == '\a', 'alert'
    assert escape(re.match(r'\\[abfnrtv]', '\\b')) == '\b', 'backspace'
    assert escape(re.match(r'\\[abfnrtv]', '\\f')) == '\f', 'formfeed'
    assert escape(re.match(r'\\[abfnrtv]', '\\n')) == '\n', 'linefeed'
    assert escape(re.match(r'\\[abfnrtv]', '\\r')) == '\r', 'carriage return'

# Generated at 2022-06-13 17:53:16.824308
# Unit test for function test
def test_test(): # type: ignore
    try:
        test()
    except ValueError as e:
        assert False, e

# Generated at 2022-06-13 17:53:18.914344
# Unit test for function test
def test_test():
    """Test for function test."""
    try:
        test()
    except SystemExit:
        pass



# Generated at 2022-06-13 17:53:25.172989
# Unit test for function escape

# Generated at 2022-06-13 17:53:39.066783
# Unit test for function escape
def test_escape():
    assert escape("\x01") == "\x01"
    assert escape("\x1E") == "\x1E"
    assert escape("\x7F") == "\x7F"
    #
    assert escape("\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f") == "\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f"
    #

# Generated at 2022-06-13 17:53:45.269645
# Unit test for function escape
def test_escape():
    result_escape = escape("\a")
    print(result_escape)
    result_escape = escape("\b")
    print(result_escape)
    result_escape = escape("\f")
    print(result_escape)
    result_escape = escape("\n")
    print(result_escape)
    result_escape = escape("\r")
    print(result_escape)
    result_escape = escape("\t")
    print(result_escape)
    result_escape = escape("\v")
    print(result_escape)
    result_escape = escape("a")
    print(result_escape)

# Generated at 2022-06-13 17:53:48.476310
# Unit test for function test
def test_test():
    """Make sure the full test executes without generating
    any exceptions.
    """
    test()
    print("Test of test runs without any failures")

# Generated at 2022-06-13 17:53:52.697297
# Unit test for function test
def test_test():
    import tempfile
    f = tempfile.NamedTemporaryFile()
    f.write(b'test_evalString_ok')
    f.flush()
    try:
        test()
    finally:
        f.close()

# Generated at 2022-06-13 17:53:54.243760
# Unit test for function test
def test_test():
    test()


# Generated at 2022-06-13 17:54:01.689687
# Unit test for function escape
def test_escape():
    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\v'
    assert escape('\\\'') == '\''
    assert escape('\\\"') == '\"'
    assert escape('\\\\') == '\\'
    assert escape('\\x7f') == '\x7f'
    assert escape('\\177') == '\x7f'



# Generated at 2022-06-13 17:54:12.001792
# Unit test for function escape
def test_escape():
    from pytest import raises

    assert(escape(re.match("", "")) == "")
    assert(escape(re.match("abc", "abc")) == "abc")
    assert(escape(re.match("abc", "")) == "")
    assert(escape(re.match("", "abc")) == "")

    assert(escape(re.match("\\a", "\\a")) == "\a")
    assert(escape(re.match("\\b", "\\b")) == "\b")
    assert(escape(re.match("\\f", "\\f")) == "\f")
    assert(escape(re.match("\\n", "\\n")) == "\n")
    assert(escape(re.match("\\r", "\\r")) == "\r")

# Generated at 2022-06-13 17:54:21.433549
# Unit test for function escape
def test_escape():
    from typing import Dict, Type, Any, Optional
    from pytype.pytype import File  # noqa
    from pytype.pytd import pytd_utils  # noqa
    from pytype.pytd import visitors  # noqa
    from pytype.pytd import pytd  # noqa
    from pytd import optimize  # noqa
    from pytd import pytd_utils  # noqa
    from pytd import visitors  # noqa
    from pytd import pytd  # noqa
    from pytype import pytd_utils  # noqa
    from pytype import visitors  # noqa
    from pytype import pytd  # noqa
    from typing import Dict, Type, Any, Optional
    from pytype.pytype import File  # noqa
    from pytype.pytd import pytd_utils  #

# Generated at 2022-06-13 17:54:31.997003
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", "\\a")) == "a"
    assert escape(re.match(r"\\(.)", "\\b")) == "b"
    assert escape(re.match(r"\\(.)", "\\f")) == "f"
    assert escape(re.match(r"\\(.)", "\\n")) == "n"
    assert escape(re.match(r"\\(.)", "\\r")) == "r"
    assert escape(re.match(r"\\(.)", "\\t")) == "t"
    assert escape(re.match(r"\\(.)", "\\v")) == "v"
    assert escape(re.match(r"\\(.)", "\\'")) == "'"

# Generated at 2022-06-13 17:54:33.054313
# Unit test for function test
def test_test():
    try:
        test()
    except:
        print("test broken")

# Generated at 2022-06-13 17:54:53.265200
# Unit test for function escape

# Generated at 2022-06-13 17:54:59.784137
# Unit test for function escape
def test_escape():
    # test simple escape sequences
    assert escape(re.search(r"\\a", r"\a")) == "\a"
    assert escape(re.search(r"\\b", r"\b")) == "\b"
    assert escape(re.search(r"\\f", r"\f")) == "\f"
    assert escape(re.search(r"\\n", r"\n")) == "\n"
    assert escape(re.search(r"\\r", r"\r")) == "\r"
    assert escape(re.search(r"\\t", r"\t")) == "\t"
    assert escape(re.search(r"\\v", r"\v")) == "\v"
    assert escape(re.search(r"\\\'", r"\'")) == "'"

# Generated at 2022-06-13 17:55:03.995565
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\(.)\Z', r'\a')) == '\x07'
    assert escape(re.match(r'\\(.)\Z', r'\b')) == '\x08'
    assert escape(re.match(r'\\(.)\Z', r'\f')) == '\x0c'
    assert escape(re.match(r'\\(.)\Z', r'\n')) == '\n'
    assert escape(re.match(r'\\(.)\Z', r'\r')) == '\r'
    assert escape(re.match(r'\\(.)\Z', r'\t')) == '\t'

# Generated at 2022-06-13 17:55:08.997388
# Unit test for function escape
def test_escape():
    t1 = r"\\x12"
    t1 = re.match(r"\\x..", t1)
    assert escape(t1) == chr(0x12)

    t2 = r"\\b"
    t2 = re.match(r"\\.", t2)
    assert escape(t2) == "\b"

# Generated at 2022-06-13 17:55:16.158613
# Unit test for function escape
def test_escape():
    assert escape("\\a") == '\a'
    assert escape("\\b") == '\b'
    assert escape("\\f") == '\f'
    assert escape("\\n") == '\n'
    assert escape("\\r") == '\r'
    assert escape("\\t") == '\t'
    assert escape("\\v") == '\v'
    assert escape("\\'") == "'"
    assert escape('\\"') == '"'
    assert escape("\\\\") == "\\"
    assert escape("\\x1") == "\x01"
    assert escape("\\xFF") == "\xFF"
    assert escape("\\xF") == "\x0F"
    assert escape("\\xF1") == "\xF1"
    assert escape("\\x9F") == "\x9F"


# Generated at 2022-06-13 17:55:24.332987
# Unit test for function escape
def test_escape():
    assert escape('\a') == '\a'
    assert escape('\b') == '\b'
    assert escape('\f') == '\f'
    assert escape('\n') == '\n'
    assert escape('\r') == '\r'
    assert escape('\t') == '\t'
    assert escape('\v') == '\v'
    assert escape("'") == "'"
    assert escape('"') == '"'
    assert escape('\\') == '\\'
    assert escape('\x00') == '\x00'
    assert escape('\xFF') == '\xFF'
    assert escape('\x2D') == '\x2D'
    assert escape('\x04') == '\x04'
    assert escape('\x00') == '\x00'


# Generated at 2022-06-13 17:55:25.770070
# Unit test for function test
def test_test():
    test()



# Generated at 2022-06-13 17:55:36.917607
# Unit test for function escape
def test_escape():
    assert escape("\\x01") == "\01"
    assert escape("\\01") == "\01"
    assert escape("\\001") == "\001"
    assert escape("\\x12") == "\x12"
    assert escape("\\x12") == "\x12"
    assert escape("\\12") == "\12"
    assert escape("\\012") == "\012"
    assert escape("\\x1234") == "\x12"
    assert escape("\\1234") == "\12"

    try:
        escape("\\")
        assert False
    except ValueError as e:
        assert "invalid" in str(e) and "('\\\\')" in str(e)

# Generated at 2022-06-13 17:55:37.827423
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:47.982240
# Unit test for function escape
def test_escape():
    # 4 cases of "normal" backslash escaping
    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\v'
    assert escape('\\\'') == '\''
    assert escape('\\\"') == '\"'
    assert escape('\\\\') == '\\'
    # 4 cases of hex code (2 digits) escaping
    assert escape('\\x41') == 'A'
    assert escape('\\x42') == 'B'
    assert escape('\\x43') == 'C'

# Generated at 2022-06-13 17:56:08.730367
# Unit test for function test
def test_test():
    import unittest

    class TestTest(unittest.TestCase):
        def test_test(self):
            test()

    unittest.main()

# Generated at 2022-06-13 17:56:17.453129
# Unit test for function escape
def test_escape():
    escape_test_cases = (
        # input, expected
        ("\\", "\\"),
        ("\\a", "\x07"),
        ("\\b", "\x08"),
        ("\\f", "\x0c"),
        ("\\n", "\n"),
        ("\\r", "\r"),
        ("\\t", "\t"),
        ("\\v", "\x0b"),
        ("\\x07", "\x07"),
        ("\\07", "\x07"),
        ("\\007", "\x07"),
    )
    for s, expected in escape_test_cases:
        assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", s)) == expected

# Generated at 2022-06-13 17:56:19.230429
# Unit test for function test
def test_test():
    try:
        test()
    except (AssertionError, ValueError):
        assert False

# Generated at 2022-06-13 17:56:27.358594
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\a', '\\a')) == '\a'
    assert escape(re.match('\\b', '\\b')) == '\b'
    assert escape(re.match('\\f', '\\f')) == '\f'
    assert escape(re.match('\\n', '\\n')) == '\n'
    assert escape(re.match('\\r', '\\r')) == '\r'
    assert escape(re.match('\\t', '\\t')) == '\t'
    assert escape(re.match('\\v', '\\v')) == '\v'
    assert escape(re.match("\\'", "\\'")) == "'"
    assert escape(re.match('\\"', '\\"')) == '"'

# Generated at 2022-06-13 17:56:31.964783
# Unit test for function escape
def test_escape():
    # Given
    m = type('', (),{'group': lambda self,arg: '\12' if arg == 1 else '\\12'})()

    # When
    result = escape(m)

    # Then
    assert result == '\n'

# Generated at 2022-06-13 17:56:35.063681
# Unit test for function test
def test_test():
    import sys
    import io
    try:
        buf = io.StringIO()
        sys.stdout = buf
        test()
    finally:
        sys.stdout = sys.__stdout__
    assert buf.getvalue() == ""

# Generated at 2022-06-13 17:56:42.910049
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\t")) == "\t"
    assert escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\xab")) == "\u00ab"
    assert escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\377")) == "\u00ff"

# Generated at 2022-06-13 17:56:46.373341
# Unit test for function escape
def test_escape():
    assert escape("\\\\") == "\\"
    assert escape("\\x0a") == "\n"
    assert escape("\\011") == "\t"
    assert escape("\\'") == "'"
    assert escape("\\\"") == '"'

# Generated at 2022-06-13 17:56:47.034005
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:56.728235
# Unit test for function escape
def test_escape():
    from unittest import TestCase, main as unit_test_main

    class MyTestCase(TestCase):
        def test_escape(self):
            import string

# Generated at 2022-06-13 17:57:41.483003
# Unit test for function escape
def test_escape():
    assert escape("\\xFF") == "\xFF"
    assert escape("\\0") == "\0"
    assert escape("\\123") == "\123"
    assert escape("\\b") == "\b"
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("\\\"") == "\""
    assert escape("\\'") == "'"
    assert escape("\\\\") == "\\"

# Generated at 2022-06-13 17:57:44.046865
# Unit test for function test
def test_test():
    try:
        test()
    except ValueError as e:
        print("Unexpected error", e)
        return
    print("Passed")

# Generated at 2022-06-13 17:57:55.410011
# Unit test for function escape
def test_escape():
    cases = [
        ("a", r"\a"),
        ("b", r"\b"),
        ("\n", r"\n"),
        ('"', r'"'),
        ("'", r"'"),
        ("\\", r"\\"),
        ("\u1234", r"\u1234"),
        ("xabcd", r"\xabcd"),
        ("\U00012345", r"\U00012345"),
    ]
    for input, output in cases:
        assert escape(re.match(r"\\(.+)", output)) == input

# Generated at 2022-06-13 17:57:56.999010
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\xab", r"\xab")) == "\xab"
    assert escape(re.search(r"\\xab", r"\xabab")) == "\xab"


# Generated at 2022-06-13 17:57:58.802915
# Unit test for function escape
def test_escape():
    assert escape('\\x1f\\x1f') == '\x1f\x1f'

# Generated at 2022-06-13 17:58:08.722006
# Unit test for function escape
def test_escape():
    # format: original_string, escaped_string
    tests = [
        ('\a','\\a'),
        ('\b','\\b'),
        ('\f','\\f'),
        ('\n','\\n'),
        ('\r','\\r'),
        ('\t','\\t'),
        ('\v','\\v'),
        ('\'','\''),
        ('\"','\\"'),
        ('\\','\\\\'),
        ('\\\\', '\\\\'),
        ('\\x1234', '\\x1234'),
        ('\\1234', '\\1234'),
        ('\\aA', '\\aA'),
        ('\aA', '\\aA'),
        ('\aA', '\\aA'),
    ]


# Generated at 2022-06-13 17:58:10.499637
# Unit test for function test
def test_test():
    from .exception_hierarchy import TestSkipped
    raise TestSkipped('test() needs to be updated to be a unit test')

# Generated at 2022-06-13 17:58:19.713109
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", "\\b")) == '\b'
    assert escape(re.match(r"\\(.)", "\\a")) == '\a'
    assert escape(re.match(r"\\(.)", "\\n")) == '\n'
    assert escape(re.match(r"\\(x..)", "\\xA")) == '\n'
    assert escape(re.match(r"\\(x..)", "\\x0000A")) == '\n'
    assert escape(re.match(r"\\(.)", "\\'")) == "'"
    assert escape(re.match(r"\\(.)", '\\"')) == '"'
    assert escape(re.match(r"\\(.)", "\\0")) == '\x00'

# Generated at 2022-06-13 17:58:22.186744
# Unit test for function escape
def test_escape():
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        if e != c:
            print(i, c, s, e)

# Generated at 2022-06-13 17:58:31.679895
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\x', '')) == 'x'
    assert escape(re.match('\\x', '')) == 'x'
    assert escape(re.match('\\a', '')) == '\a'
    assert escape(re.match('\\b', '')) == '\b'
    assert escape(re.match('\\f', '')) == '\f'
    assert escape(re.match('\\n', '')) == '\n'
    assert escape(re.match('\\r', '')) == '\r'
    assert escape(re.match('\\t', '')) == '\t'
    assert escape(re.match('\\v', '')) == '\v'
    assert escape(re.match('\\\\', '')) == '\\'
    assert escape(re.match('\\\'', ''))