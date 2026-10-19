

# Generated at 2022-06-13 17:50:06.421609
# Unit test for function escape
def test_escape():
    # Test simple escape characters that should be the same before and after evalString
    for esc in simple_escapes:
        assert escape(f'\\{esc}') == simple_escapes[esc]

    # Test different hex escapes
    for esc in ["\\x41", "\\xe4", "\\x4a"]:
        # The raw escape (e.g. \x4a) should be translated to the correct character
        assert escape(esc) == chr(int(esc[-2:], 16))

    # Test invalid hex escapes
    for esc in ["\\x", "\\x1", "\\x12"]:
        try:
            escape(esc)
        except ValueError as e:
            pass

    # Test valid octal escapes

# Generated at 2022-06-13 17:50:17.858169
# Unit test for function escape
def test_escape():
    from hypothesis import given, assume, HealthCheck
    from hypothesis.strategies import characters, text

    def check_escape(s):
        s = "\\" + s
        assume(s in simple_escapes or re.match(r"\\x\w", s) or re.match(r"\\\d\d\d", s))
        return escape(re.search(r"\\(\w|\d)", s))

    @given(characters(max_codepoint=255))
    def test_escape_hypothesis(s):
        assume(s not in simple_escapes)
        assert check_escape(s) == "\\" + s

    @given(text(max_size=10))
    def test_escape_hypothesis(s):
        assume(s == "")

# Generated at 2022-06-13 17:50:26.758532
# Unit test for function test
def test_test():
    class StubIO:
        def __init__(self) -> None:
            self.output = ""

        def write(self, block: str) -> None:
            self.output += block

        def flush(self) -> None:
            self.output = ""

    io = StubIO()
    save_stdout = __import__("sys").stdout
    try:
        __import__("sys").stdout = io
        test()
    finally:
        __import__("sys").stdout = save_stdout
    assert io.output.strip() == ""

# Generated at 2022-06-13 17:50:34.400331
# Unit test for function escape
def test_escape():
    # A string containing all characters from 0 to 255
    zero_to_255 = ("".join([chr(i) for i in range(256)]))

    # Case 0
    m = re.match("(a)", "a")
    assert escape(m) == "\a"

    # Case 1
    m = re.match("(b)", "b")
    assert escape(m) == "\b"

    # Case 2
    m = re.match("(f)", "f")
    assert escape(m) == "\f"

    # Case 3
    m = re.match("(n)", "n")
    assert escape(m) == "\n"

    # Case 4
    m = re.match("(r)", "r")
    assert escape(m) == "\r"

    # Case 5

# Generated at 2022-06-13 17:50:35.837216
# Unit test for function escape
def test_escape():
    esc = '\\x'
    assert escape(esc) == '\\x'

# Generated at 2022-06-13 17:50:38.584039
# Unit test for function escape
def test_escape():
    assert evalString(r"'''") == "\'\'\'"
    assert evalString(r'"""') == '"""\n'

# Generated at 2022-06-13 17:50:45.835388
# Unit test for function escape
def test_escape():
    assert escape(re.match('a', '\\a')) == "\a"
    assert escape(re.match('b', '\\b')) == "\b"
    assert escape(re.match('f', '\\f')) == "\f"
    assert escape(re.match('n', '\\n')) == "\n"
    assert escape(re.match('r', '\\r')) == "\r"
    assert escape(re.match('t', '\\t')) == "\t"
    assert escape(re.match('v', '\\v')) == "\v"
    assert escape(re.match('"', '\\"')) == '"'
    assert escape(re.match("'", "\\'")) == "'"
    assert escape(re.match('\\', '\\\\')) == "\\"


# Generated at 2022-06-13 17:50:50.311674
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"(\\a)", r"\a")) == "\a"
    assert escape(re.match(r"(\\b)", r"\b")) == "\b"
    assert escape(re.match(r"(\\f)", r"\f")) == "\f"
    assert escape(re.match(r"(\\n)", r"\n")) == "\n"
    assert escape(re.match(r"(\\r)", r"\r")) == "\r"
    assert escape(re.match(r"(\\t)", r"\t")) == "\t"
    assert escape(re.match(r"(\\v)", r"\v")) == "\v"
    assert escape(re.match(r"(\\'\\)", r"\'\\")) == "\'"

# Generated at 2022-06-13 17:50:59.924298
# Unit test for function escape
def test_escape():
    for ch in "abfnrtv'\"\\":
        assert escape(re.match(r'\\' + ch, '\\' + ch)) == simple_escapes[ch]

    assert escape(re.match(r"\\xFF", "\\xFF")) == chr(255)
    assert escape(re.match(r"\\xA", "\\xA")) == chr(10)
    assert escape(re.match(r"\\x2F", "\\x2F")) == chr(47)

    assert escape(re.match(r"\\123", "\\123")) == chr(83)
    assert escape(re.match(r"\\01", "\\01")) == chr(1)
    assert escape(re.match(r"\\127", "\\127")) == chr(127)


# Generated at 2022-06-13 17:51:08.277323
# Unit test for function escape
def test_escape():
  assert escape('a') == r'a', repr(escape('a'))
  assert escape('\\\\') == r'\\', repr(escape('\\\\'))
  assert escape('\n') == r'\n', repr(escape('\n'))
  assert escape('\n  ') == r'\n', repr(escape('\n  '))
  assert escape('\nx') == r'\n', repr(escape('\nx'))
  assert escape('\n\n') == r'\n', repr(escape('\n\n'))
  assert escape('\n\n  ') == r'\n', repr(escape('\n\n  '))
  assert escape('\n\nx') == r'\n', repr(escape('\n\nx'))

# Generated at 2022-06-13 17:51:24.948543
# Unit test for function escape
def test_escape():
    assert escape.__doc__
    assert escape(re.match(r"\\x0", "\\x0")) == "\x00"
    assert escape(re.match(r"\\x4a", "\\x4a")) == "J"
    assert escape(re.match(r"\\x41", "\\x41")) == "A"
    assert escape(re.match(r"\\x5A", "\\x5A")) == "Z"
    assert escape(re.match(r"\\x7a", "\\x7a")) == "z"  # lowercase hex works
    assert escape(re.match(r"\\x7A", "\\x7A")) == "z"
    assert escape(re.match(r"\\x7F", "\\x7F")) == "\x7f"

# Generated at 2022-06-13 17:51:33.371186
# Unit test for function escape
def test_escape():
    tests = [
        ("\\x", ValueError),
        ("\\x1", ValueError),
        ("\\x12", ValueError),
        ("\\x123", ValueError),
        ("\\x1a", "\x1a"),
        ("\\x1a1", "\x1a1"),
        ("\\x1a12", "\x1a12"),
        ("\\x1a123", "\x1a123"),
    ]
    for s, v in tests:
        try:
            assert escape(re.match(r"\\(x.{0,2})", s)) == v
        except ValueError:
            pass

# Generated at 2022-06-13 17:51:42.701729
# Unit test for function escape
def test_escape():
    assert escape('\a') == '\a'
    assert escape('\b') == '\b'
    assert escape('\f') == '\f'
    assert escape('\n') == '\n'
    assert escape('\r') == '\r'
    assert escape('\t') == '\t'
    assert escape('\v') == '\v'
    assert escape('\'') == '\''
    assert escape('\"') == '\"'
    assert escape('\\') == '\\'

    assert escape('\\a') == '\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'

# Generated at 2022-06-13 17:51:43.115336
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:51:53.792012
# Unit test for function escape

# Generated at 2022-06-13 17:51:58.703322
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x24", "x24")) == "$"
    assert escape(re.match(r"\\500", "500")) == "\x00"
    assert escape(re.match(r"\\a", "a")) == "\a"

# Generated at 2022-06-13 17:52:01.041131
# Unit test for function escape
def test_escape():
    # Check non-escaped string
    assert escape('\n') == '\n'
    # Check for escaped string
    assert escape('\\\n') == '\\\n'


# Generated at 2022-06-13 17:52:10.828128
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([0-7]{1,3})", "\\0")) == "\0"
    assert escape(re.match(r"\\([0-7]{1,3})", "\\001")) == "\x01"
    assert escape(re.match(r"\\([0-7]{1,3})", "\\0010")) == "\x10"
    assert escape(re.match(r"\\([0-7]{1,3})", "\\001000")) == "\x10"

    assert escape(re.match(r"\\(x[0-9A-Fa-f]{2})", "\\x00")) == "\x00"

# Generated at 2022-06-13 17:52:21.414382
# Unit test for function escape
def test_escape():
    # \0
    assert escape(re.match(r"^\\0", r"\0")) == "\0"
    # \1
    assert escape(re.match(r"^\\1", r"\1")) == "\1"
    # \a
    assert escape(re.match(r"^\\a", r"\a")) == "\a"
    # \b
    assert escape(re.match(r"^\\b", r"\b")) == "\b"
    # \f
    assert escape(re.match(r"^\\f", r"\f")) == "\f"
    # \n
    assert escape(re.match(r"^\\n", r"\n")) == "\n"
    # \r

# Generated at 2022-06-13 17:52:31.373202
# Unit test for function escape
def test_escape():
    test_cases = [
        ("\\a", "\a"),
        ("\\b", "\b"),
        ("\\f", "\f"),
        ("\\n", "\n"),
        ("\\r", "\r"),
        ("\\t", "\t"),
        ("\\v", "\v"),
        ("\\'", "'"),
        ('\\"', '"'),
        ("\\\\", "\\"),
        ("\\x1B", chr(27)),
        ("\\x61", chr(97)),
        ("\\x61a", chr(97)),
        ("\\x", "\\x"),
        ("\\x6", "\\x6"),
        ("\\x6a", "\\x6a"),
        ("\\41", chr(33)),
        ("\\177", chr(127)),
    ]


# Generated at 2022-06-13 17:52:55.310242
# Unit test for function escape
def test_escape():
    assert_equal(escape(re.match('(ab)', 'ab')), 'ab')
    assert_equal(escape(re.match('(a\\)b)', 'a\\)b')), 'a\\)b')
    assert_equal(escape(re.match('(a\\\\)b)', 'a\\\\b')), 'a\\\\b')
    assert_equal(escape(re.match('(a\\nb)', 'a\nb')), 'a\nb')
    assert_equal(escape(re.match('(a\\rb)', 'a\rb')), 'a\rb')
    assert_equal(escape(re.match('(a\\tb)', 'a\tb')), 'a\tb')

# Generated at 2022-06-13 17:52:56.300493
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:56.973062
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:57.568346
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:05.934873
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x[0-9a-f]", '\\x9')) == '\t'
    assert escape(re.match(r"\\x\d{2}", '\\x09')) == '\t'
    assert escape(re.match(r"\\[0-7]\d", '\\19')) == '\t'
    assert escape(re.match(r"\\[0-7]{2}", '\\09')) == '\t'
    assert escape(re.match(r"\\[0-7]{3}", '\\009')) == '\0'
    assert escape(re.match(r"\\x", '\\x')) == 'x'

# Generated at 2022-06-13 17:53:10.109247
# Unit test for function escape
def test_escape():
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", s))
        if e != c:
            print(i, c, s, e)

# Generated at 2022-06-13 17:53:16.621787
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x41", r"\x41")) == "A"
    assert escape(re.match(r"\\x64", r"\x64")) == "d"
    assert escape(re.match(r"\\x10", r"\x10")) == "\x10"
    assert escape(re.match(r"\\x0d", r"\x0d")) == "\x0d"
    assert escape(re.match(r"\\x00", r"\x00")) == "\x00"
    assert escape(re.match(r"\\x0a", r"\x0a")) == "\n"
    assert escape(re.match(r"\\x5c", r"\x5c")) == "\\"

# Generated at 2022-06-13 17:53:26.481058
# Unit test for function escape
def test_escape():
    assert escape('\\"') == '"'
    assert escape("\\'") == "'"
    assert escape('\\a') == '\x07'
    assert escape('\\b') == '\x08'
    assert escape('\\f') == '\x0c'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\x0b'
    assert escape('\\x07') == '\x07'
    assert escape('\\x7f') == '\x7f'
    assert escape('\\x00') == '\x00'
    assert escape('\\04') == '\x04'
    assert escape('\\0') == '\x00'


# Generated at 2022-06-13 17:53:36.131358
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\\a', '\\\a')) == '\a'
    assert escape(re.match('\\\b', '\\\b')) == '\b'
    assert escape(re.match('\\\f', '\\\f')) == '\f'
    assert escape(re.match('\\\n', '\\\n')) == '\n'
    assert escape(re.match('\\\r', '\\\r')) == '\r'
    assert escape(re.match('\\\t', '\\\t')) == '\t'
    assert escape(re.match('\\\v', '\\\v')) == '\v'
    assert escape(re.match('\\\'', '\\\'')) == '\''

# Generated at 2022-06-13 17:53:46.332040
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv]|x.{1,2}|[0-7]{1,3})", "\\b")) == "\b"
    assert escape(re.match(r"\\([abfnrtv]|x.{1,2}|[0-7]{1,3})", "\\a")) == "\a"
    assert escape(re.match(r"\\([abfnrtv]|x.{1,2}|[0-7]{1,3})", "\\v")) == "\v"
    assert escape(re.match(r"\\([abfnrtv]|x.{1,2}|[0-7]{1,3})", "\\r")) == "\r"

# Generated at 2022-06-13 17:54:25.814028
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\a" )) == "\a"
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\b" )) == "\b"
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\f" )) == "\f"

# Generated at 2022-06-13 17:54:34.785060
# Unit test for function escape
def test_escape():
    m = re.match(r"\\(x[0-9a-fA-F]{2}|[0-7]{1,3})", "\\xa")
    assert escape(m) == "\n"

    m = re.match(r"\\(x[0-9a-fA-F]{2}|[0-7]{1,3})", "\\777")
    assert escape(m) == "\xff"

    m = re.match(r"\\(x[0-9a-fA-F]{2}|[0-7]{1,3})", "\\077")
    assert escape(m) == "?"


# Generated at 2022-06-13 17:54:41.799772
# Unit test for function escape
def test_escape():
    from re import match
    def test_escape_helper(s, expected):
        m = match(r'\\(.*)', s)
        result = escape(m)
        assert result == expected, (s, result)
    for c in range(256):
        test_escape_helper('\\' + chr(c), chr(c))
    test_escape_helper('\\x11', '\x11')
    test_escape_helper('\\x1', 'x1')
    test_escape_helper('\\', '\\')

# Generated at 2022-06-13 17:54:52.005332
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
    assert escape("\\x00") == "\0"
    assert escape("\\x7F") == "\x7f"
    assert escape("\\xFF") == "\xff"
    assert escape("\\242") == "\x82"
    assert escape("\\0") == "\0"
    assert escape("\\068") == "\068"
   

# Generated at 2022-06-13 17:54:57.327785
# Unit test for function escape
def test_escape():

    test_str = '''This is a string with \a \b \f \n \r \t \v escapes \\ escaped and \' escaped and " escaped'''

    result = re.sub(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})",escape,test_str)

    expected_result = '''This is a string with \x07 \x08 \x0c \n \r \t \x0b escapes \ escaped and ' escaped and " escaped'''

    assert(result == expected_result)


# Generated at 2022-06-13 17:54:58.569893
# Unit test for function test

# Generated at 2022-06-13 17:55:09.466455
# Unit test for function escape
def test_escape():
    # Simple escapes
    assert "ab" == escape(re.match(r"\\a", "\\a"))
    assert "\b" == escape(re.match(r"\\b", "\\b"))
    assert "cd" == escape(re.match(r"\\c", "\\c"))
    assert "ef" == escape(re.match(r"\\e", "\\e"))
    assert "\f" == escape(re.match(r"\\f", "\\f"))
    assert "\n" == escape(re.match(r"\\n", "\\n"))
    assert "op" == escape(re.match(r"\\o", "\\o"))
    assert "\r" == escape(re.match(r"\\r", "\\r"))

# Generated at 2022-06-13 17:55:16.920331
# Unit test for function escape
def test_escape():
    import pytest

    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"
    assert escape(re.match(r"\\v", "\\v")) == "\v"
    assert escape(re.match(r"\\'", "\\'")) == "'"

# Generated at 2022-06-13 17:55:25.125716
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

# Generated at 2022-06-13 17:55:26.699850
# Unit test for function test
def test_test():
    test()



# Generated at 2022-06-13 17:56:31.623622
# Unit test for function escape
def test_escape():
    assert escape(re.search("\\x20", ' ')) == ' '
    assert escape(re.search("\\xFFFF", ' ')) == ' '
    assert escape(re.search("\\xqqq", ' ')) == ' '
    assert escape(re.search("\\x", ' ')) == ' '

# Generated at 2022-06-13 17:56:41.089354
# Unit test for function escape

# Generated at 2022-06-13 17:56:51.457275
# Unit test for function escape

# Generated at 2022-06-13 17:56:58.864669
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2})", "\\n")) == "\n"
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2})", "\\x0a")) == "\n"
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2})", "\\x0A")) == "\n"
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2})", "\\x0aa")) == "\n"
    assert escape(re.search(r"\\([abfnrtv]|x.{0,2})", "\\x")) is None


# Generated at 2022-06-13 17:57:04.245657
# Unit test for function escape
def test_escape():
    # Test escape of single quote or a double quote.
    assert escape(re.match(r"\\['\"]", r"\'")).encode() == b"'"
    assert escape(re.match(r"\\['\"]", r'\"')).encode() == b'"'
    # Test escape of a character with 3-digit octal
    assert escape(re.match(r"\\[0-7]{3}", r"\007")).encode() == b"\a"
    # Test escape of a character with 2-digit hex
    assert escape(re.match(r"\\x[0-9a-fA-F]{2}", r"\x1b")).encode() == b"\033"
    # Test escape of a character with 1-digit octal

# Generated at 2022-06-13 17:57:06.644993
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\[abfnrtv]', "\\a")) == "\a"



# Generated at 2022-06-13 17:57:19.447660
# Unit test for function escape
def test_escape():
    assert not re.search(r"\\", escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\n")))
    assert not re.search(r"\\", escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\t")))
    assert not re.search(r"\\", escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\a")))

# Generated at 2022-06-13 17:57:26.895403
# Unit test for function escape
def test_escape():
    match = re.match('\\a', '\\a')
    assert escape(match) == "\a"
    match = re.match('\\b', '\\b')
    assert escape(match) == "\b"
    match = re.match('\\f', '\\f')
    assert escape(match) == "\f"
    match = re.match('\\n', '\\n')
    assert escape(match) == "\n"
    match = re.match('\\r', '\\r')
    assert escape(match) == "\r"
    match = re.match('\\t', '\\t')
    assert escape(match) == "\t"
    match = re.match('\\v', '\\v')
    assert escape(match) == "\v"
    match = re.match("\\'", "\\'")

# Generated at 2022-06-13 17:57:36.377502
# Unit test for function escape

# Generated at 2022-06-13 17:57:43.346751
# Unit test for function escape
def test_escape():

    from pytype.pyc import compat

    m = compat.mock.Mock()

    # Test a simple escape
    m.group = compat.mock.MagicMock(return_value=(r"\f","f"))
    result = escape(m)
    assert result == "\f"

    # Test a hex string escape
    m.group = compat.mock.MagicMock(return_value=(r"\x1B","x1B"))
    result = escape(m)
    assert result == "\x1B"

    # Test a octal string escape
    m.group = compat.mock.MagicMock(return_value=(r"\033","033"))
    result = escape(m)
    assert result == "\x1B"

    # Test an invalid escape
    m.group = compat.mock.MagicM

# Generated at 2022-06-13 17:59:39.046220
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:59:40.094942
# Unit test for function test
def test_test():
    test()


# Generated at 2022-06-13 17:59:40.577308
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:59:45.807992
# Unit test for function escape
def test_escape():
    esc = escape(re.match('\\x00', '\\x00'))
    assert esc == '\0'

    esc = escape(re.match('\\x7F', '\\x7F'))
    assert esc == '\x7f'

    esc = escape(re.match('\\x81', '\\x81'))
    assert esc == '\x81'

    esc = escape(re.match('\\xFF', '\\xFF'))
    assert esc == '\xff'

    esc = escape(re.match('\\256', '\\256'))
    assert esc == '\uffff'

