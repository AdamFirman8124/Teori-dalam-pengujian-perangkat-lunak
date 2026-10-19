

# Generated at 2022-06-13 17:50:17.166132
# Unit test for function evalString
def test_evalString():
	assert evalString(r'"\""') == '"'
	assert evalString(r"'\''") == "'"
	assert evalString(r"'\"'") == '"'
	assert evalString(r'"\'"') == "'"
	assert evalString(r"'\a\b\f\n\r\t\v\'\"\\'") == "\a\b\f\n\r\t\v'\"\\"
	assert evalString(r'"\a\b\f\n\r\t\v\'\"\\"') == "\a\b\f\n\r\t\v'\"\\"
	assert evalString(r"'\007\x07\x07'") == "\a\a\a"
	assert evalString(r'"\007\x07\x07"') == "\a\a\a"

# Generated at 2022-06-13 17:50:28.961096
# Unit test for function escape
def test_escape():
    # testing for escapes
    assert escape(re.match('\\\\a', '\\a')) == '\a'
    assert escape(re.match('\\\\b', '\\b')) == '\b'
    assert escape(re.match('\\\\f', '\\f')) == '\x0c'
    assert escape(re.match('\\\\n', '\\n')) == '\n'
    assert escape(re.match('\\\\r', '\\r')) == '\r'
    assert escape(re.match('\\\\t', '\\t')) == '\t'
    assert escape(re.match('\\\\v', '\\v')) == '\x0b'
    assert escape(re.match('\\\\\'', '\\\'')) == '\''

# Generated at 2022-06-13 17:50:33.063265
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
    assert escape('\\x01') == '\x01'
    assert escape('\\777') == '\x1f'
    assert escape('\\400') == '\x80'

# Generated at 2022-06-13 17:50:36.373354
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x22", r'\"')) == '"'
    assert escape(re.match(r"\\x22", r"'")) == "'"

# Generated at 2022-06-13 17:50:43.385190
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\a','\\a')) == "\a"
    assert escape(re.match('\\g','\\g')) == "g"
    assert escape(re.match('\\z','\\z')) == "z"
    assert escape(re.match('\\n','\\n')) == "\n"
    assert escape(re.match('\\x1F','\\x1F')) == "\x1F"
    assert escape(re.match('\\012','\\012')) == "\n"
    assert escape(re.match('\\377','\\377')) == "\xff"
    assert escape(re.match('\\468','\\468')) == "H"

# Generated at 2022-06-13 17:50:47.456864
# Unit test for function evalString
def test_evalString():
    assert evalString('"abc"') == 'abc'
    assert evalString('"\\n"') == '\n'
    assert evalString("'abc'") == 'abc'
    assert evalString("'\\n'") == '\n'

# Generated at 2022-06-13 17:50:53.150933
# Unit test for function escape
def test_escape():
    assert escape(re.search(r'\\x41', '\\x41')) == 'A'
    assert escape(re.search(r'\\x41', '\\\\x41')) == '\\x41'
    assert escape(re.search(r'\\x41', '\\x4')) == '\\x4'
    assert escape(re.search(r'\\x41', '\\')) == '\\'

# Generated at 2022-06-13 17:50:55.968857
# Unit test for function escape
def test_escape():
    m = re.match(r"\\(.|$)", "\\x41")
    assert m is not None
    assert escape(m) == chr(ord('A'))



# Generated at 2022-06-13 17:51:03.241041
# Unit test for function escape
def test_escape():
    m = re.match(r"\\([\'\"\\abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\a")
    assert escape(m) == "\a"

    m = re.match(r"\\([\'\"\\abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\x41")
    assert escape(m) == "\x41"

    m = re.match(r"\\([\'\"\\abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\x41g")
    assert escape(m) == "\x41"

# Generated at 2022-06-13 17:51:14.921362
# Unit test for function escape
def test_escape():
    # Testing simple escapes
    assert escape(re.match("\\a", r"\a")) == "\a"
    assert escape(re.match("\\b", r"\b")) == "\b"
    assert escape(re.match("\\f", r"\f")) == "\f"
    assert escape(re.match("\\n", r"\n")) == "\n"
    assert escape(re.match("\\r", r"\r")) == "\r"
    assert escape(re.match("\\t", r"\t")) == "\t"
    assert escape(re.match("\\v", r"\v")) == "\v"
    # Testing hex escapes
    assert escape(re.match("\\xFF", r"\xFF")) == "\xFF"

# Generated at 2022-06-13 17:51:36.132781
# Unit test for function escape
def test_escape():
    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\v'
    assert escape('\\x78') == 'x'
    assert escape('\\076') == '6'
    assert escape("\\'") == "'"
    assert escape('\\"') == '"'
    assert escape('\\\\') == '\\'
    try:
        escape("\\x")
    except ValueError:
        pass
    else:
        assert False
    try:
        escape("\\77")
    except ValueError:
        pass
   

# Generated at 2022-06-13 17:51:43.335575
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\"', '\\"')) == '"'
    assert escape(re.match("\\'", "\\'")) == "'"
    assert escape(re.match("\\n", "\\n")) == '\n'
    assert escape(re.match("\\x61", '\\x61')) == 'a'
    assert escape(re.match("\\xF", '\\xF')) == '\x0f'
    assert escape(re.match("\\x4F", '\\x4F')) == 'O'
    assert escape(re.match("\\077", "\\077" )) == '?'
    assert escape(re.match("\\377", "\\377" )) == chr(0xFF)

# Generated at 2022-06-13 17:51:43.803030
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:51:54.766312
# Unit test for function evalString
def test_evalString():
    import unittest
    from asteval import Evaluator

    eval_ = Evaluator()

    class TestEvalString(unittest.TestCase):
        def test_simple(self):
            self.assertEqual(eval_('"\a\b\f\n\r\t\v\'"'), "\x07\x08\x0c\n\r\t\x0b'")
            self.assertEqual(eval_('"\\a\\b\\f\\n\\r\\t\\v\\ \\""'), "\a\b\f\n\r\t\v  ")

# Generated at 2022-06-13 17:51:56.459729
# Unit test for function test
def test_test():
    assert test() is None

# Generated at 2022-06-13 17:52:03.715301
# Unit test for function escape
def test_escape():
    # Test simple escapes
    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"
    assert escape(re.match(r"\\v", "\\v")) == "\v"
    assert escape(re.match(r"\\'", "\\'")) == "'"

# Generated at 2022-06-13 17:52:05.786781
# Unit test for function escape
def test_escape():
    s = "\\xabcd"
    escaped = b"\\xabcd"
    assert escape(s) == str(escaped)[2:-1]


# Generated at 2022-06-13 17:52:14.929685
# Unit test for function test
def test_test():
    from importlib import reload

    import string

    reload(string)
    test = string.test
    del test

    # Test for issues fixed in 3.4b1
    assert evalString("'\\u2029'") == "\u2029"
    assert evalString("'\\U0001D120'") == "\U0001D120"
    assert evalString("'\\u{0001D120}'") == "\U0001D120"
    assert evalString("'\\u{1017A}'") == "\U0001017A"
    assert (
        evalString("'\\U00010001\\U00010002\\U00010003\\U00010004\\U00010005'") == "\U00010001\U00010002\U00010003\U00010004\U00010005"
    )



# Generated at 2022-06-13 17:52:15.698855
# Unit test for function test
def test_test():
    test()
    print('Success: test_test')

# Generated at 2022-06-13 17:52:18.242831
# Unit test for function test
def test_test():
    # Case when i is 0
    for i in range(-128, 256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        if e != c:
            print(i, c, s, e)

# Generated at 2022-06-13 17:53:02.648026
# Unit test for function escape
def test_escape():
    # type: () -> None
    """Test for internal function escape.

    Do not do a complete test, as this is an internal function.
    """
    assert escape(re.match('\\"', '\\"')) == '"'

# Generated at 2022-06-13 17:53:11.594299
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\b", "\\b")) == "\x08"
    assert escape(re.match("\\f", "\\f")) == "\x0c"
    assert escape(re.match("\\n", "\\n")) == "\n"
    assert escape(re.match("\\r", "\\r")) == "\r"
    assert escape(re.match("\\t", "\\t")) == "\t"
    assert escape(re.match("\\x1f", "\\x1f")) == "\x1f"
    assert escape(re.match("\\07", "\\07")) == "\x07"
    assert escape(re.match("\\77", "\\77")) == "?"
    assert escape(re.match("\\777", "\\777")) == "\xff"

# Generated at 2022-06-13 17:53:22.911129
# Unit test for function escape
def test_escape():
    m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\'")
    assert escape(m) == "'"

    m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x36")
    assert escape(m) == "6"
    try:
        m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x3")
        escape(m)
    except ValueError:
        pass


# Generated at 2022-06-13 17:53:23.344030
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:28.170561
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", r"\a")) == "\a"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", r"\b")) == "\b"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", r"\f")) == "\f"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", r"\n")) == "\n"

# Generated at 2022-06-13 17:53:29.588016
# Unit test for function escape
def test_escape():
    m = re.match(r'\\', "\\")
    assert escape(m) == '\\'


# Generated at 2022-06-13 17:53:35.498392
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\", "\\")) == "\\"
    assert escape(re.match(r"\\x", "\\x")) == "x"
    assert escape(re.match(r"\\x0", "\\x0")) == "x0"
    assert escape(re.match(r"\\x00", "\\x00")) == "\x00"
    assert escape(re.match(r"\\x000", "\\x000")) == "\x00"
    assert escape(re.match(r"\\x0000", "\\x0000")) == "\x00"
    assert escape(re.match(r"\\x00000", "\\x00000")) == "\x00"
    assert escape(re.match(r"\\x00000", "\\x00000")) == "\x00"

# Generated at 2022-06-13 17:53:46.008400
# Unit test for function escape
def test_escape():
  import pytest

  def test_all(m):
    return m.group(0)

  def test_tail(m):
    return m.group(1)

  # Basic hex
  m = re.match(r"\\xAA", r"\xAA")
  assert m is not None

  assert(escape(m) == chr(0xAA))
  assert(test_all(m) == r"\xAA")
  assert(test_tail(m) == "xAA")

  # Basic hex
  m = re.match(r"\\x6F", r"\x6F")
  assert m is not None

  assert(escape(m) == chr(0x6F))
  assert(test_all(m) == r"\x6F")

# Generated at 2022-06-13 17:53:48.671146
# Unit test for function test
def test_test():
    try:
        test()
        print("PASS")
    except:
        print("FAIL")

# Generated at 2022-06-13 17:53:58.304604
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\x0e", "\\x0e")) == "\x0e"
    assert escape(re.match("\\x0e", "\\x0e")) != "\x0e\n"
    assert escape(re.match("\\a", "\\a")) == "\a"
    assert escape(re.match("\\'", "\\'")) == "\'"
    assert escape(re.match("\\\"", "\\\"")) == "\""
    assert escape(re.match("\\\\", "\\\\")) == "\\"


# Generated at 2022-06-13 17:54:55.980227
# Unit test for function escape

# Generated at 2022-06-13 17:55:06.756611
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x42.{0,2}", r"\x42")) == 'B'
    assert escape(re.match(r"\\x42.{0,2}", r"\x42E")) == 'BE'
    assert escape(re.match(r"\\x42.{0,2}", r"\x42EF")) == 'BE'
    assert escape(re.match(r"\\x42.{0,2}", r"\x42EZ")) == 'B'
    assert escape(re.match(r"\\x42.{0,2}", r"\x42EZb")) == 'B'
    assert escape(re.match(r"\\[0-7]{3}", r"\777")) == '\o177'

# Generated at 2022-06-13 17:55:14.788304
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\x30', r'\x30')) == '0'
    assert escape(re.match(r'\\x3G', r'\x3G')) == '3'
    assert escape(re.match(r'\\x', r'\x')) == 'x'
    assert escape(re.match(r'\\x\{1\}', r'\x{1}')) == 'x'
    assert escape(re.match(r'\\x3\{1\}', r'\x3{1}')) == 'x3'
    assert escape(re.match(r'\\x3\{', r'\x3{')) == 'x3'

# Generated at 2022-06-13 17:55:23.254638
# Unit test for function escape
def test_escape():
    # Test on simple escapes
    for k, v in simple_escapes.items():
        m = re.search(r"\\" + re.escape(k), "\\" + k)
        assert m is not None
        e = escape(m)
        assert e == v

    # Test on octal escapes
    for i in range(256):
        c = chr(i)
        s = repr(c)[1:-1]
        m = re.search(r"\\[0-7]{1,3}", "\\" + s)
        assert m is not None
        e = escape(m)
        assert e == c

    # Test on hex escapes
    for i in range(256):
        c = chr(i)
        s = hex(i)[2:]

# Generated at 2022-06-13 17:55:24.067046
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:26.870382
# Unit test for function test
def test_test():
    # A trivial example
    test()

    # An example taken from the module documentation
    evalString('"Hello\\n\tor\n\tWorld!"')

# Generated at 2022-06-13 17:55:40.041473
# Unit test for function escape
def test_escape():
  mp = {"\\x00": '\x00', "\\x20": '\x20',
        "\\n": '\n',   "\\\\": '\\', "\\'": "'", "\\\"": '\"',
        r"\\x0g": ValueError, "\\800": ValueError, "\\0": ValueError, "\\1": "\1",
        r"\x0g": ValueError, "\800": ValueError, "\0": ValueError, "\1": "\1"}
  for s, v in mp.items():
    if type(v) is ValueError:
      try:
        escape(re.search(r'\\(.+)', s))
        assert False
      except ValueError:
        pass
    else:
      assert escape(re.search(r'\\(.+)', s)) == v


# Generated at 2022-06-13 17:55:49.864178
# Unit test for function escape
def test_escape():
    cases = [
        (r"\a", "\a"),
        (r"\b", "\b"),
        (r"\f", "\f"),
        (r"\n", "\n"),
        (r"\r", "\r"),
        (r"\t", "\t"),
        (r"\v", "\v"),
        (r"\'", "'"),
        (r'\"', '"'),
        (r"\\", "\\"),
        (r"\00", "\0"),
        (r"\08", "\0"),
        (r"\7", "\a"),
        (r"\11", "\t"),
        (r"\x01", "\x01"),
        (r"\x12", "\x12"),
        (r"\x7f", "\x7f"),
    ]


# Generated at 2022-06-13 17:55:50.396868
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:51.483799
# Unit test for function test
def test_test():
  assert test() == None

# Generated at 2022-06-13 17:57:36.985357
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:57:42.668646
# Unit test for function escape
def test_escape():
    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\"') == '"'
    assert escape('\\x10') == '\x10'
    assert escape('\\x1') == '\x01'
    assert escape('\\111') == 'I'
    assert escape('\\') == '\\'
    try:
        escape('\\x')
        assert False, "this must be an exception"
    except ValueError:
        pass
    try:
        escape('\\777')
        assert False, "this must be an exception"
    except ValueError:
        pass

# Generated at 2022-06-13 17:57:54.699227
# Unit test for function escape
def test_escape():
    m = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r'\x10')
    assert escape(m) == chr(0x10)
    m = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r'\10')
    assert escape(m) == chr(8)
    m = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r'\a')
    assert escape(m) == "\a"

# Generated at 2022-06-13 17:57:56.953426
# Unit test for function escape
def test_escape():
    import pytest
    assert escape(re.match("\n", "\\n")) == "\n"
    assert escape(re.match("\r", "\\r")) == "\r"
    with pytest.raises(ValueError):
        escape(re.match("\t", "\\t"))

# Generated at 2022-06-13 17:58:07.345477
# Unit test for function escape
def test_escape():
    # Parse octal string literals
    esc_00 = escape(re.search(r'\\0', '\\0'))
    assert esc_00 == '\0'
    esc_07 = escape(re.search(r'\\7', '\\7'))
    assert esc_07 == '\7'
    esc_057 = escape(re.search(r'\\577', '\\577'))
    assert esc_057 == '\u0237'
    # Parse hex string literals
    esc_x00 = escape(re.search(r'\\x00', '\\x00'))
    assert esc_x00 == '\0'
    esc_x7f = escape(re.search(r'\\x7f', '\\x7f'))
    assert esc_x7f == '\u007f'

# Generated at 2022-06-13 17:58:07.905676
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:08.806274
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:18.870280
# Unit test for function escape
def test_escape():
    """
    Verify that escape() returns what we expect
    """
    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\'", "\\'")) == "'"
    assert escape(re.match(r'\\"', '\\"')) == '"'
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"

# Generated at 2022-06-13 17:58:22.074140
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", r"\a")) == "\a"

# Generated at 2022-06-13 17:58:28.752070
# Unit test for function escape
def test_escape():
    from io import StringIO
    from unittest import main, TestCase
    from asteval.nersc_string_eval import escape
    import re
    class StringEscapeTestCase(TestCase):
        def test_escape(self):
            self.assertEqual(escape(re.match(r'\\b', r'\b')), '\b')
            self.assertEqual(escape(re.match(r'\\x41', r'\x41')), 'A')
            self.assertEqual(escape(re.match(r'\\41', r'\41')), '!')
            self.assertEqual(escape(re.match(r'\\41', r'\411')), '1')