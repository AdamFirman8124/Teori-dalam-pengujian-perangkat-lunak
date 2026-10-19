

# Generated at 2022-06-13 17:50:01.003486
# Unit test for function escape
def test_escape():
    # check that backslash followed by an integer is handled properly

    # good cases:
    for i in range(8):
        assert escape(re.match(r'\\%o' % i, r'\%o' % i)) == chr(i)
        assert escape(re.match(r'\\%03o' % i, r'\%03o' % i)) == chr(i)

    # bad cases:
    with pytest.raises(ValueError):
        escape(re.match(r'\\00', r'\00'))
    with pytest.raises(ValueError):
        escape(re.match(r'\\9', r'\9'))
    with pytest.raises(ValueError):
        escape(re.match(r'\\08', r'\08'))

# Generated at 2022-06-13 17:50:11.661372
# Unit test for function escape
def test_escape():
    from unittest import TestCase

    class T(TestCase):
        def test_one(self):
            def test_one(self):
                for c in "abfnrtv'" '"' "\\":
                    e = escape(re.match(r"\\" + c, "\\" + c))
                    self.assertEqual(e, c)
                for c in "abfnrtv'\"\\":
                    e = escape(re.match(r"\\" + c, "\\" + c))
                    self.assertEqual(e, c)

        def test_two(self):
            e = escape(re.match(r"\\x00", "\\x00"))
            self.assertEqual(e, "\x00")
            e = escape(re.match(r"\\xff", "\\xff"))
           

# Generated at 2022-06-13 17:50:21.240217
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv]|\\|'|\"|x.{0,2}|[0-7]{1,3})", "\\a")) == "\a", ""
    assert escape(re.match(r"\\([abfnrtv]|\\|'|\"|x.{0,2}|[0-7]{1,3})", "\\b")) == "\b", ""
    assert escape(re.match(r"\\([abfnrtv]|\\|'|\"|x.{0,2}|[0-7]{1,3})", "\\f")) == "\f", ""

# Generated at 2022-06-13 17:50:29.905424
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\a")) == "\a"
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\b")) == "\b"
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\f")) == "\f"

# Generated at 2022-06-13 17:50:31.306002
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:50:37.528251
# Unit test for function escape
def test_escape():
    import pytest
    from stringescape import escape
    assert escape("\\x26").encode("utf-8") == b"&"
    assert escape("\\x2f").encode("utf-8") == b"/"
    assert escape("\\x25").encode("utf-8") == b"%"
    with pytest.raises(ValueError):
        escape("\\x2")

# Generated at 2022-06-13 17:50:38.109194
# Unit test for function test
def test_test():
    assert test() == None

# Generated at 2022-06-13 17:50:45.563858
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\x61', '\\x61')) == 'a'
    assert escape(re.match('\\x22', '\\x22')) == '\x22'
    assert escape(re.match('\\x5c', '\\x5c')) == '\\'
    assert escape(re.match('\\062', '\\062')) == 'b'
    assert escape(re.match('\\012', '\\012')) == '\n'
    assert escape(re.match('\\157', '\\157')) == 'o'
    assert escape(re.match('\\117', '\\117')) == 'O'
    assert escape(re.match('\\077', '\\077')) == '\x1f'

# Generated at 2022-06-13 17:50:56.429500
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\a', r"\a")) == "\a"
    assert escape(re.match(r'\\b', r"\b")) == "\b"
    assert escape(re.match(r'\\f', r"\f")) == "\f"
    assert escape(re.match(r'\\n', r"\n")) == "\n"
    assert escape(re.match(r'\\r', r"\r")) == "\r"
    assert escape(re.match(r'\\t', r"\t")) == "\t"
    assert escape(re.match(r'\\v', r"\v")) == "\v"
    assert escape(re.match(r"\\\'", r"\'")) == "'"

# Generated at 2022-06-13 17:51:03.337507
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\b")) == "\b"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\77")) == "?"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x7f")) == chr(0x7f)



# Generated at 2022-06-13 17:51:23.526521
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
    assert escape(re.match(r"\\\'", "\\'")) == "'"

# Generated at 2022-06-13 17:51:25.158307
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\["a"]', r'\"a')) == '"'

# Generated at 2022-06-13 17:51:32.360194
# Unit test for function escape
def test_escape():
    m = re.match(r'\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', '\a')
    assert m is not None
    assert escape(m) == '\a'

# Generated at 2022-06-13 17:51:40.388860
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x62", r"\x62")) == "b"
    assert escape(re.match(r"\\x0a", r"\x0a")) == "\n"
    assert escape(re.match(r"\\x00", r"\x00")) == "\x00"
    assert escape(re.match(r"\\x0G", r"\x0G"))
    assert escape(re.match(r"\\x0", r"\x0"))
    assert escape(re.match(r"\\x", r"\x"))
    assert escape(re.match(r"\\\x62", r"\\b")) == "\\b"
    assert escape(re.match(r"\\\x0a", r"\\\n")) == "\\\n"
    assert escape

# Generated at 2022-06-13 17:51:50.077701
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\'")) == "'"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", '\\"')) == '"'
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\\\")) == "\\"

# Generated at 2022-06-13 17:51:50.651104
# Unit test for function test
def test_test():
    assert test() == None

# Generated at 2022-06-13 17:51:57.359897
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\x00", "\\x00")) == "\x00"
    assert escape(re.search(r"\\x7f", "\\x7f")) == "\x7f"
    assert escape(re.search(r"\\377", "\\377")) == "\xff"
    assert escape(re.search(r"\\xZZ", "\\xZZ")) == "Z"
    assert escape(re.search(r"\\0", "\\0")) == "\x00"

# Generated at 2022-06-13 17:51:59.659853
# Unit test for function test
def test_test():
    assert True

# Generated at 2022-06-13 17:52:09.336223
# Unit test for function evalString

# Generated at 2022-06-13 17:52:17.538022
# Unit test for function evalString
def test_evalString():
    assert evalString('"abc"') == 'abc'
    assert evalString("'xyz'") == 'xyz'
    assert evalString('"\\x61\\x62\\x63"') == 'abc'
    assert evalString("'\\161\\162\\163'") == 'abc'
    assert evalString('"\\u1234"') == '\u1234'

    # Make sure we can eval any valid string literal
    for line in open("test/test_repr.py", "rb"):
        # Skip comments and blank lines
        line = line.strip()
        if not line or line.startswith(b"#"):
            continue
        # We don't have to handle single-quoted strings
        if b"'" not in line:
            assert evalString(line.decode("utf-8")) == eval

# Generated at 2022-06-13 17:52:40.065591
# Unit test for function escape
def test_escape():

    # When regular string
    # Then return string back
    assert escape("hello") == "hello"

    # Given a string which starts with '\'
    # When string has escape codes (\a, \b, \f, \n, \r, \t, \v, \', \", \\)
    # Then translate the escape codes to their intended values
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

# Generated at 2022-06-13 17:52:40.630515
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:52.033964
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", r"\a")) == "\a"
    assert escape(re.match(r"\\(.)", r"\b")) == "\b"
    assert escape(re.match(r"\\(.)", r"\f")) == "\f"
    assert escape(re.match(r"\\(.)", r"\n")) == "\n"
    assert escape(re.match(r"\\(.)", r"\r")) == "\r"
    assert escape(re.match(r"\\(.)", r"\t")) == "\t"
    assert escape(re.match(r"\\(.)", r"\v")) == "\v"
    assert escape(re.match(r'\\(.)', r"\'")) == "'"

# Generated at 2022-06-13 17:53:03.371409
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x[a-f]\d")).group(0) == '\n'
    assert escape(re.match(r"\\x0\d")).group(0) == '\n'
    assert escape(re.match(r"\\xa\d")).group(0) == '\n'
    assert escape(re.match(r"\\x1\d")).group(0) == '\n'
    assert escape(re.match(r"\\x2\d")).group(0) == '\n'
    assert escape(re.match(r"\\x3\d")).group(0) == '\n'
    assert escape(re.match(r"\\x4\d")).group(0) == '\n'

# Generated at 2022-06-13 17:53:12.223071
# Unit test for function evalString
def test_evalString():
    import random
    import string
    from pygments.token import Token
    from pygments.lexers import get_lexer_by_name

    lexer = get_lexer_by_name("python")

    for _ in range(100000):
        s = ""
        for _ in range(10):
            if random.random() < 0.3:
                s += random.choice("'\"")
            elif random.random() < 0.2:
                s += random.choice("'\"") * 3
            else:
                c = random.choice("'\"")
                if random.random() < 0.5:
                    s += random.choice("{}\\") + c
                else:
                    s += c
                    s += random.choice("{}\\")


# Generated at 2022-06-13 17:53:14.023163
# Unit test for function escape
def test_escape():
    esc = escape("\\x34\\077")
    assert esc == "4?"

# Generated at 2022-06-13 17:53:14.828898
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:25.071994
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(.)", "\\a")) == "\a"
    assert escape(re.match(r"\\(.)", "\\b")) == "\b"
    assert escape(re.match(r"\\(.)", "\\f")) == "\f"
    assert escape(re.match(r"\\(.)", "\\n")) == "\n"
    assert escape(re.match(r"\\(.)", "\\r")) == "\r"
    assert escape(re.match(r"\\(.)", "\\t")) == "\t"
    assert escape(re.match(r"\\(.)", "\\v")) == "\v"
    assert escape(re.match(r"\\(.)", "\\'")) == "'"

# Generated at 2022-06-13 17:53:32.725351
# Unit test for function evalString
def test_evalString():
    strLiteral = "'Hello, world'"
    assert evalString(strLiteral) == "Hello, world"
    strLiteral = "'''Hello, world'''"
    assert evalString(strLiteral) == "Hello, world"
    strLiteral = '"Hello, world"'
    assert evalString(strLiteral) == "Hello, world"
    strLiteral = '"""Hello, world"""'
    assert evalString(strLiteral) == "Hello, world"
    strLiteral = "'\\x00'"
    assert evalString(strLiteral) == "\x00"
    strLiteral = "'\\x10'"
    assert evalString(strLiteral) == "\x10"
    strLiteral = "'\\xff'"
    assert evalString(strLiteral)

# Generated at 2022-06-13 17:53:39.770921
# Unit test for function escape
def test_escape():
    assert escape("a") == "\a"
    assert escape("b") == "\b"
    assert escape("f") == "\f"
    assert escape("n") == "\n"
    assert escape("r") == "\r"
    assert escape("t") == "\t"
    assert escape("v") == "\v"
    assert escape("'") == "'"
    assert escape('"') == '"'
    assert escape("\\") == "\\"
    
    # hex
    assert escape("\\x00") == "\0"
    assert escape("\\x3c") == "<"
    assert escape("\\xa5") == "¥"
    assert escape("\\x07") == "\007"
    
    # octal
    assert escape("\\000") == "\0"
    assert escape("\\003") == "\003"
   

# Generated at 2022-06-13 17:54:00.739104
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\'")).__eq__("'")
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\"")).__eq__("\"")
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\")).__eq__("\\")

# Generated at 2022-06-13 17:54:11.454148
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\\$', '\\$')) == '\\'
    assert escape(re.match(r'\\a', '\\a')) == '\a'
    assert escape(re.match(r'\\b', '\\b')) == '\x08'
    assert escape(re.match(r'\\f', '\\f')) == '\x0c'
    assert escape(re.match(r'\\t', '\\t')) == '\t'
    assert escape(re.match(r'\\n', '\\n')) == '\n'
    assert escape(re.match(r'\\r', '\\r')) == '\r'
    assert escape(re.match(r'\\v', '\\v')) == '\x0b'

# Generated at 2022-06-13 17:54:21.207843
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\' + chr(ord('a')), '\\a')) == '\a'
    assert escape(re.match('\\' + chr(ord('b')), '\\b')) == '\b'
    assert escape(re.match('\\' + chr(ord('f')), '\\f')) == '\f'
    assert escape(re.match('\\' + chr(ord('n')), '\\n')) == '\n'
    assert escape(re.match('\\' + chr(ord('r')), '\\r')) == '\r'
    assert escape(re.match('\\' + chr(ord('t')), '\\t')) == '\t'

# Generated at 2022-06-13 17:54:22.302724
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:54:22.849098
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:54:32.960567
# Unit test for function escape
def test_escape():
    import pytest
    assert escape(re.match(r"\\x([0-9a-fA-F]{2})", r"\x10")) == ""

# Generated at 2022-06-13 17:54:34.024175
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:54:43.752296
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\a")) == "\a"
    assert escape(re.match(r"\\('|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\b")) == "\b"
    assert escape(re.match(r"\\('|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\f")) == "\f"
    assert escape(re.match(r"\\('|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\n"))

# Generated at 2022-06-13 17:54:53.583529
# Unit test for function escape
def test_escape():
    # Basic cases
    assert escape(re.match(r'[\\][a]', '\\a')) == '\a'
    assert escape(re.match(r'[\\][b]', '\\b')) == '\b'
    assert escape(re.match(r'[\\][f]', '\\f')) == '\f'
    assert escape(re.match(r'[\\][n]', '\\n')) == '\n'
    assert escape(re.match(r'[\\][r]', '\\r')) == '\r'
    assert escape(re.match(r'[\\][t]', '\\t')) == '\t'
    assert escape(re.match(r'[\\][v]', '\\v')) == '\v'

# Generated at 2022-06-13 17:54:58.043271
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\0', '\\0')) == ('\\0', '0')
    assert escape(re.match('\\a', '\\a')) == ('\\a', 'a')
    assert escape(re.match('\\b', '\\b')) == ('\\b', 'b')
    assert escape(re.match('\\t', '\\t')) == ('\\t', 't')
    assert escape(re.match('\\\\', '\\\\')) == ('\\\\', '\\')

# Generated at 2022-06-13 17:55:13.888100
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:14.572358
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:17.369467
# Unit test for function test
def test_test():
    import pytest
    from . import dedent
    from . import test

    with pytest.raises(AssertionError, match="repr\\(\"\\x00\"\\)"):
        test()

# Generated at 2022-06-13 17:55:24.592103
# Unit test for function escape
def test_escape():
    assert escape("\n") == "\\n"
    assert escape("\x1f") == "\\x1f"
    assert escape("\x01") == "\\x01"
    assert escape("\x09") == "\\x09"

# Generated at 2022-06-13 17:55:25.537867
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:26.088061
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:36.341861
# Unit test for function escape
def test_escape():
    assert escape("\\\x03") == "\x03"
    assert escape("\\x45") == "E"
    assert escape("\\x69") == "i"
    assert escape("\\111") == "I"
    assert escape("\\111") == "I"
    assert escape("\\x69") == "i"
    assert escape("\\45") == "%"
    assert escape("\\\x03") == "\x03"
    assert escape("\\x45") == "E"
    assert escape("\\111") == "I"
    assert escape("\\x69") == "i"
    assert escape("\\45") == "%"
    assert escape("\\\x03") == "\x03"



# Generated at 2022-06-13 17:55:37.219952
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:46.940289
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\x20", "\\x20")) == " "

# Generated at 2022-06-13 17:55:47.515302
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:26.741500
# Unit test for function escape
def test_escape():
    # check that single character escapes work
    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"
    assert escape(re.match(r"\\v", "\\v")) == "\v"
    assert escape(re.match(r"\\'", "\\'")) == "'"

# Generated at 2022-06-13 17:56:33.308549
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\"', '"')) == '"'
    assert escape(re.match('\\x20', 'x20')) == ' '
    assert escape(re.match('\\x7f', 'x7f')) == '\x7f'
    assert escape(re.match('\\200', '200')) == '\x80'
    assert escape(re.match('\\377', '377')) == '\xff'

# Generated at 2022-06-13 17:56:38.841842
# Unit test for function escape
def test_escape():
    from unittest import TestCase, main

    class _escapeTest(TestCase):
        def test_simple_escapes(self):
            for escaped_char, escaped_value in simple_escapes.items():
                self.assertEqual(escape(re.match(r"\A\\" + escaped_char, "\\" + escaped_char)), escaped_value)

        def test_hex_escapes(self):
            self.assertEqual(escape(re.match(r"\A\\x00", "\\x00")), "\0")
            self.assertEqual(escape(re.match(r"\A\\x12", "\\x12")), "\x12")
            self.assertEqual(escape(re.match(r"\A\\x34", "\\x34")), "\x34")

# Generated at 2022-06-13 17:56:39.398275
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:41.894793
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:56:51.718066
# Unit test for function escape
def test_escape():
    assert escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\a")) == "\u0007"
    assert escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\b")) == "\u0008"
    assert escape(re.search(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\f")) == "\u000C"

# Generated at 2022-06-13 17:56:54.555848
# Unit test for function escape
def test_escape():
    assert escape('\\x123') == "S"
    assert escape('\\123') == chr(83)
    assert escape('\\n') == "\n"



# Generated at 2022-06-13 17:56:55.350696
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:57:00.369362
# Unit test for function escape
def test_escape():
    assert escape(re.match("a", "a")) == "a"
    assert escape(re.match("a", "\\a")) == "\a"
    assert escape(re.match("a", "\\xab a")) == "\n"
    assert escape(re.match("a", "\\xab")) == "\xab"

# Generated at 2022-06-13 17:57:02.613379
# Unit test for function test
def test_test():
    try:
        test()
    except:
        pass
    finally:
        pass

# Generated at 2022-06-13 17:58:03.862884
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:04.363193
# Unit test for function test
def test_test():
	assert callable(test)

# Generated at 2022-06-13 17:58:05.309511
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:10.184759
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([\'\"\\abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\t")) == "t"
    assert escape(re.match(r"\\([\'\"\\abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\r")) == "r"

# Generated at 2022-06-13 17:58:14.582592
# Unit test for function test
def test_test():
    from StringIO import StringIO
    import sys
    save_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        test()
        out.seek(0)
        assert out.read() == ""
    finally:
        sys.stdout = save_stdout

# Generated at 2022-06-13 17:58:22.413508
# Unit test for function escape
def test_escape():
    assert escape("\\0") == "\0"
    assert escape("\\1") == "\1"
    assert escape("\\7") == "\7"
    assert escape("\\11") == "\11"
    assert escape("\\111") == "\111"
    assert escape("\\1111") == "\1111"
    assert escape("\\22") == "\22"
    assert escape("\\222") == "\222"
    assert escape("\\2222") == "\2222"

    try:
        escape("\\0222")
        assert False, "escape let octal escape too long through"
    except ValueError:
        pass

    assert escape("\\'") == "'"
    assert escape("\\\"") == "\""
    assert escape("\\a") == "a"
    assert escape("\\b") == "\b"

# Generated at 2022-06-13 17:58:23.039582
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:25.302387
# Unit test for function test
def test_test():
  test()
  assert True

# Generated at 2022-06-13 17:58:32.634104
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\x0000', '')) == '\x00'
    assert escape(re.match('\\x0001', '')) == '\x01'
    assert escape(re.match('\\x0041', '')) == 'A'
    assert escape(re.match('\\000', '')) == '\x00'
    assert escape(re.match('\\001', '')) == '\x01'
    assert escape(re.match('\\041', '')) == '!'
    assert escape(re.match('\\a', '')) == '\a'
    assert escape(re.match('\\b', '')) == '\b'
    assert escape(re.match('\\f', '')) == '\x0c'
    assert escape(re.match('\\n', '')) == '\n'

# Generated at 2022-06-13 17:58:34.076105
# Unit test for function test
def test_test():
    try:
        test()
    except:
        pytest.fail()