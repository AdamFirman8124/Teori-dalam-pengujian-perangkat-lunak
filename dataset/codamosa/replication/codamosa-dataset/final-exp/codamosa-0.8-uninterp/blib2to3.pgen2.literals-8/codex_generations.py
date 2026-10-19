

# Generated at 2022-06-13 17:49:57.629598
# Unit test for function escape
def test_escape():
    escaped = escape(r"\b")
    assert escaped == "\b"
    escaped = escape(r"\x62")
    assert escaped == "b"
    escaped = escape(r"\62")
    assert escaped == "b"
    escaped = escape(r"\\")
    assert escaped == "\\"
    escaped = escape(r"\x2")
    assert escaped == "\\x2"
    escaped = escape(r"\x20")
    assert escaped == " "


# Generated at 2022-06-13 17:50:06.296185
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\)", "'")) == "'"
    assert escape(re.match(r"\\('|\"|\\)", '"')) == '"'
    assert escape(re.match(r"\\('|\"|\\)", "\\")) == "\\"
    assert escape(re.match(r"\\('|\"|\\)", "a")) == "\a"
    assert escape(re.match(r"\\('|\"|\\)", "b")) == "\b"
    assert escape(re.match(r"\\('|\"|\\)", "f")) == "\f"
    assert escape(re.match(r"\\('|\"|\\)", "n")) == "\n"
    assert escape(re.match(r"\\('|\"|\\)", "r")) == "\r"

# Generated at 2022-06-13 17:50:07.660565
# Unit test for function evalString
def test_evalString():
    e = evalString('"\'"')
    return e == "'"

# Generated at 2022-06-13 17:50:12.382548
# Unit test for function escape
def test_escape():
    m = re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x5f5")
    e = escape(m)
    assert e == "_"

# Generated at 2022-06-13 17:50:21.611841
# Unit test for function evalString
def test_evalString():
    assert evalString("''") == ""
    assert evalString("'a'") == "a"
    assert evalString("'\\'") == "'"
    assert evalString('"\\""') == '"'
    assert evalString("'\\x00'") == "\x00"
    assert evalString("'\\xFF'") == "\xFF"
    assert evalString("'\\n'") == "\n"
    assert evalString("'\\377'") == "\377"
    assert evalString("'\\0'") == "\0"
    assert evalString("'\\001'") == "\001"
    assert evalString("'\\1111'") == "\031"
    assert evalString("'\\1111'") == "\031"
    assert evalString("'\\11'") == "\t"

# Generated at 2022-06-13 17:50:22.194918
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:50:30.509764
# Unit test for function evalString
def test_evalString():
    assert evalString('"\\a\\b\\f\\n\\r\\t\\v\\\'\\\"\\\\"') == "\a\b\f\n\r\t\v\'\"\\"
    assert evalString('"\\x1\\x12\\x123\\x1234"') == "?\u0012?\u1234"
    assert evalString('"\\0\\00\\000\\0001"') == "\x00\x00\x00\x01"
    assert evalString('"\\"\\"\\"\\"\\""') == "\"\"\"\"\""
    assert evalString("''") == ''
    assert evalString("'a'") == 'a'
    assert evalString("'\\'a\\''") == "'a'"
    assert evalString('"a"') == 'a'

# Generated at 2022-06-13 17:50:31.599344
# Unit test for function escape
def test_escape():
    assert escape(re.match('a', 'a')) == "a"

# Generated at 2022-06-13 17:50:32.661386
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:50:42.110489
# Unit test for function escape
def test_escape():
    # Tests for plain ASCII characters
    for i in range(32):
        assert escape(re.match(r"\\[abfnrtv]'", '\\' + chr(i) + "'")) == chr(i)
        assert escape(re.match(r"\\x..", '\\x' + hex(i)[2:])) == chr(i)
        assert escape(re.match(r"\\x..", '\\x' + hex(i)[2:].zfill(2))) == chr(i)
        assert escape(re.match(r"\\[0-7]{1,3}", '\\' + oct(i)[2:])) == chr(i)

# Generated at 2022-06-13 17:51:08.375305
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\.', '\\a')) == "\a"
    assert escape(re.match(r'\\.', '\\b')) == "\b"
    assert escape(re.match(r'\\.', '\\f')) == "\f"
    assert escape(re.match(r'\\.', '\\n')) == "\n"
    assert escape(re.match(r'\\.', '\\r')) == "\r"
    assert escape(re.match(r'\\.', '\\t')) == "\t"
    assert escape(re.match(r'\\.', '\\v')) == "\v"
    assert escape(re.match(r'\\.', '\\\'')) == "'"

# Generated at 2022-06-13 17:51:19.000176
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
    assert escape("\\x07") == "\a"
    assert escape("\\x65") == "e"
    assert escape("\\x077") == "e"


# Generated at 2022-06-13 17:51:23.142114
# Unit test for function escape
def test_escape():
    # Test normal escapes from Source [1]
    assert escape(Match(re.compile(r"\\"), 'a', "\\a")) == "\a"
    assert escape(Match(re.compile(r"\\"), 'b', "\\b")) == "\b"
    assert escape(Match(re.compile(r"\\"), 'f', "\\f")) == "\f"
    assert escape(Match(re.compile(r"\\"), 'n', "\\n")) == "\n"
    assert escape(Match(re.compile(r"\\"), 'r', "\\r")) == "\r"
    assert escape(Match(re.compile(r"\\"), 't', "\\t")) == "\t"
    assert escape(Match(re.compile(r"\\"), 'v', "\\v")) == "\v"

# Generated at 2022-06-13 17:51:33.382104
# Unit test for function escape
def test_escape():
    test_match = [
        (r"\\a", "\a", None),
        (r"\\b", "\b", None),
        (r"\\f", "\f", None),
        (r"\\n", "\n", None),
        (r"\\r", "\r", None),
        (r"\\t", "\t", None),
        (r"\\v", "\v", None),
        (r"\\'", "'", None),
        (r'\\"', '"', None),
        (r"\\x41", "A", None),
        (r"\\357", None, ValueError),
        (r"\\x", None, ValueError),
    ]
    for pat, exp_return, exp_exc in test_match:
        m = re.match(pat, "")

# Generated at 2022-06-13 17:51:39.482044
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\\'", "\\'")) == "'"
    assert escape(re.match(r"\\\"", "\\\"")) == '"'
    assert escape(re.match(r"\\\\", "\\\\")) == "\\"
    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"

# Generated at 2022-06-13 17:51:47.477473
# Unit test for function escape
def test_escape():
    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\v'
    assert escape("\\'") == "'"
    assert escape('\\"') == '"'
    assert escape('\\x7f') == '\\x7f'
    assert escape('\\777') == '\\777'


# Generated at 2022-06-13 17:51:57.480726
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
    assert escape('\\x0A') == '\n'
    assert escape('\\010') == '\b'
    assert escape('\\101') == 'A'
    assert escape('\\101') == 'A'



# Generated at 2022-06-13 17:51:59.659841
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:04.987793
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\'", "\\'")) == "'"
    assert escape(re.match(r"\\x7E", "\\x7E")) == chr(0x7E)
    assert escape(re.match(r"\\0", "\\0")) == chr(0)
    assert escape(re.match(r"\\077", "\\077")) == chr(0o77)

# Generated at 2022-06-13 17:52:05.768822
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:44.728180
# Unit test for function test
def test_test():
    """
    test_test()

    A loop in the main functions of this module.  Useful for debugging
    or to make sure code doesn't crash due to unit testable errors.
    """
    test()

# Generated at 2022-06-13 17:52:45.336012
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:52.272442
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv]|x)$", "\\b")) == "\b"
    assert escape(re.match(r"\\([abfnrtv]|x)$", "\\f")) == "\f"
    assert escape(re.match(r"\\([abfnrtv]|x)$", "\\n")) == "\n"
    assert escape(re.match(r"\\([abfnrtv]|x)$", "\\r")) == "\r"
    assert escape(re.match(r"\\([abfnrtv]|x)$", "\\t")) == "\t"
    assert escape(re.match(r"\\([abfnrtv]|x)$", "\\v")) == "\v"

# Generated at 2022-06-13 17:52:56.511417
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(')", r"\'")) == "'"
    assert escape(re.match(r"\\(x0)", r"\x0")) == "\x00"

# Generated at 2022-06-13 17:52:57.217458
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:58.061654
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:03.698426
# Unit test for function escape
def test_escape():
    from StringEval import escape

    s = r"\x00"
    assert escape(s) == chr(int("00", 16))

    s = r'\xab\xcd\xef\x01\02\03'
    assert escape(s) == chr(int("ab", 16)) + chr(int("cd", 16)) + chr(int("ef", 16)) + chr(int("01", 16)) + "\\x02" + "\\x03"

# Generated at 2022-06-13 17:53:04.922351
# Unit test for function test
def test_test():
    test()


# Generated at 2022-06-13 17:53:05.513404
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:06.791470
# Unit test for function test
def test_test():
    # If function test fails, it will raise an exception
    test()

# Generated at 2022-06-13 17:54:23.601992
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:54:33.499929
# Unit test for function escape
def test_escape():
    import unittest

    class Test_escape(unittest.TestCase):
        def setUp(self):
            self.e = escape

        def test_a(self):
            self.assertEqual(self.e(re.match(r"\\a", "")), "\a")

        def test_b(self):
            self.assertEqual(self.e(re.match(r"\\b", "")), "\b")

        def test_f(self):
            self.assertEqual(self.e(re.match(r"\\f", "")), "\f")

        def test_n(self):
            self.assertEqual(self.e(re.match(r"\\n", "")), "\n")


# Generated at 2022-06-13 17:54:42.525452
# Unit test for function escape
def test_escape():
    assert escape("\\'") == "'"
    assert escape("\\'") == "'"
    assert escape("\\\"") == "\""
    assert escape("\\a") == "\a"
    assert escape("\\b") == "\b"
    assert escape("\\f") == "\f"
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("\\x00") == "\x00"
    assert escape("\\xFF") == "\xFF"
    assert escape("\\0") == "\0"
    assert escape("\\2") == "\2"

# Generated at 2022-06-13 17:54:52.662775
# Unit test for function escape
def test_escape():
    import pickletools
    escapes = [r"\a", r"\b", r"\f", r"\n", r"\r", r"\t", r"\v", r"\'", r'\"',
               r"\]", r"\\"]
    for esc in escapes:
        assert pickletools.escape(esc) == evalString(esc)
    for i in range(8):
        assert pickletools.escape(r"\%o" % (i,)) == evalString(
            r"\%o" % (i,)
        )
    for i in range(8):
        assert pickletools.escape(r"\0%o" % (i,)) == evalString(
            r"\0%o" % (i,)
        )
    for i in range(8):
        assert pick

# Generated at 2022-06-13 17:55:01.634966
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x1")) == '\x01'
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\00")) == '\x00'
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\xab")) == '\xab'
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\n")) == '\n'

# Generated at 2022-06-13 17:55:02.180215
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:11.845491
# Unit test for function escape
def test_escape():
    def _test(value, expected):
        assert escape(re.match('x', value)) == expected

    _test(r'\a', '\a')
    _test(r'\b', '\b')
    _test(r'\f', '\f')
    _test(r'\n', '\n')
    _test(r'\r', '\r')
    _test(r'\t', '\t')
    _test(r'\v', '\v')
    _test(r'\'', '\'')
    _test(r'\"', '\"')
    _test(r'\\', '\\')
    _test(r'\x1a', '\x1a')
    _test(r'\xff', '\xff')

# Generated at 2022-06-13 17:55:13.201723
# Unit test for function escape
def test_escape():
    import ctypes
    assert escape(re.match(r"\\[']", r"\'")) == r"'"

# Generated at 2022-06-13 17:55:13.727169
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:22.722563
# Unit test for function escape
def test_escape():
    # Test escaping of a string literal with a backslash followed by an ASCII character
    assert escape(re.match(r"\\\w", "\\f")) == "\f"

    # Test escaping of a string literal with a backslash followed by a tab character
    assert escape(re.match(r"\\\w", "\\t")) == "\t"

    # Test escaping of a string literal with a backslash followed by a line feed character
    assert escape(re.match(r"\\\w", "\\n")) == "\n"

    # Test escaping of a string literal with a backslash followed by a carriage return character
    assert escape(re.match(r"\\\w", "\\r")) == "\r"

    # Test escaping of a string literal with a backslash followed by a vertical tab character

# Generated at 2022-06-13 17:57:58.933961
# Unit test for function escape

# Generated at 2022-06-13 17:57:59.797058
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:07.587483
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\"', '\\"')) == '\\"'
    assert escape(re.match("\\x", "\\x42")) == 'B'
    assert escape(re.match("\\001", "\\001")) == "\x01"
    assert escape(re.match("\\o", "\\o")) == "o"


# Generated at 2022-06-13 17:58:09.122229
# Unit test for function test
def test_test():
    test() # expect no output

# Generated at 2022-06-13 17:58:18.932340
# Unit test for function test

# Generated at 2022-06-13 17:58:28.657530
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\[a-z]", "\\t")) == '\t'
    assert escape(re.match(r"\\[0-9]", "\\1")) == '\x01'
    assert escape(re.match(r"\\x[0-9a-fA-F]", "\\xff")) == '\xff'
    assert escape(re.match(r"\\[\"\']", "\\'")) == "'"
    assert escape(re.match(r"\\[\"\']", '\\"')) == '"'
    assert escape(re.match(r"\\\\", "\\\\")) == '\\'


# Generated at 2022-06-13 17:58:39.132337
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\a', '\\a')) == '\a'
    assert escape(re.match('\\b', '\\b')) == '\b'
    assert escape(re.match('\\f', '\\f')) == '\f'
    assert escape(re.match('\\n', '\\n')) == '\n'
    assert escape(re.match('\\r', '\\r')) == '\r'
    assert escape(re.match('\\t', '\\t')) == '\t'
    assert escape(re.match('\\v', '\\v')) == '\v'
    assert escape(re.match("\\\'", "\\\'")) == "'"
    assert escape(re.match('\\"', '\\"')) == '"'

# Generated at 2022-06-13 17:58:44.881670
# Unit test for function escape
def test_escape():
  assert escape("\\x61") == "a"
  assert escape("\\61") == "1"
  assert escape("\\061") == "1"
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


# Generated at 2022-06-13 17:58:45.352901
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:45.838237
# Unit test for function test
def test_test():
    test()