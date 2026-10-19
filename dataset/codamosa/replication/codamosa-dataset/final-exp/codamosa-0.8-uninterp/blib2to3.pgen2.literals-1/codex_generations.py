

# Generated at 2022-06-13 17:50:16.302125
# Unit test for function escape

# Generated at 2022-06-13 17:50:17.374593
# Unit test for function test
def test_test():
    capture = capture_stdout(test)
    assert capture == ""

# Generated at 2022-06-13 17:50:29.037272
# Unit test for function escape
def test_escape():
    assert escape("\\a") == "\a"
    assert escape("\\b") == "\b"
    assert escape("\\f") == "\f"
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("''") == "'"
    assert escape('""') == '"'
    assert escape("\\\\") == "\\"
    assert escape("\\x20") == " "
    assert escape("\\x2A") == "*"
    # assert escape("\\x") == error
    assert escape("\\x0") == "\x00"
    assert escape("\\x1") == "\x01"
    assert escape("\\x2") == "\x02"

# Generated at 2022-06-13 17:50:33.650083
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
    assert escape("\\\\") == '\\'
    assert escape("\\x5f") == '_'
    assert escape("\\x09") == '\t'
    assert escape("\\x1f") == '\x1f'
    assert escape("\\x1F") == '\x1F'
    assert escape("\\65") == 'e'
   

# Generated at 2022-06-13 17:50:42.725510
# Unit test for function escape
def test_escape():
    assert escape(re.escape("\x1b")) == "\x1b"
    assert escape(re.escape("\a")) == "\a"
    assert escape(re.escape("\b")) == "\b"
    assert escape(re.escape("\f")) == "\f"
    assert escape(re.escape("\n")) == "\n"
    assert escape(re.escape("\r")) == "\r"
    assert escape(re.escape("\t")) == "\t"
    assert escape(re.escape("\v")) == "\v"
    assert escape(re.escape('\x7f')) == '\x7f'
    assert escape(re.escape('\xff')) == '\xff'

    assert escape(re.escape("'", '"')) == "'"

# Generated at 2022-06-13 17:50:54.008798
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\a")) == "\a"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\b")) == "\b"
    assert escape(re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\f")) == "\f"

# Generated at 2022-06-13 17:51:02.769841
# Unit test for function escape
def test_escape():
    from random import choice, randrange

    def makechar(c):
        if c == "\n":
            return r"\n"
        elif c == "\t":
            return r"\t"
        elif c == "\\":
            return r"\\"
        else:
            return c

    chars = "\n\t\\"
    for i in range(32):
        chars += chr(i)
    chars = "".join([makechar(c) for c in chars])

    def genstring(n):
        return "".join([choice(chars) for i in range(n)])

    def check(s):
        q = "'" if ("'" not in s) else '"'
        s = q + s + q
        assert evalString(s) == eval(s)


# Generated at 2022-06-13 17:51:07.089685
# Unit test for function escape
def test_escape():
    # simple escapes
    assert escape(re.match(r'\\(t)', r'\t')) == '\t'
    assert escape(re.match(r'\\(n)', r'\n')) == '\n'
    assert escape(re.match(r'\\(0)', r'\0')) == '\x00'
    assert escape(re.match(r'\\(x07)', r'\x07')) == '\x07'
    assert escape(re.match(r'\\(x1)', r'\x1')) == '\x01'
    assert escape(re.match(r'\\(377)', r'\377')) == '\xff'

# Generated at 2022-06-13 17:51:08.460961
# Unit test for function test
def test_test():
    if __name__ == "__main__":
        test()

# Generated at 2022-06-13 17:51:19.510618
# Unit test for function escape
def test_escape():
    assert escape("\\x09") == "\x09"
    assert escape("\\x7F") == "\x7F"
    assert escape("\\x7f") == "\x7f"
    assert escape("\\x7ff") == "\x7f"
    assert escape("\\x7ff") == "\x7f"
    assert escape("\\x") is None
    assert escape("\\d") is None
    assert escape("\\c") is None
    assert escape("\\other") is None
    try:
        escape("\\x")
        raise AssertionError("should raise exception")
    except ValueError as e:
        assert e.args[0] == "invalid hex string escape ('\\x')"



# Generated at 2022-06-13 17:51:28.645568
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:51:32.994998
# Unit test for function escape
def test_escape():
    esc = '\\'
    for b1 in "abfnrtv'\"\\":
        # \e, \xHH, \OOO
        for b2 in "xo":
            res, _ = escape(f'{esc}{b2}')
            assert len(res) == 1


# Unit tests for function evalString

# Generated at 2022-06-13 17:51:39.213325
# Unit test for function escape
def test_escape():
    # test simple escapes
    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"
    assert escape(re.match(r"\\v", "\\v")) == "\v"
    assert escape(re.match(r"\\'", "\\'")) == "'"

# Generated at 2022-06-13 17:51:39.984823
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:51:46.148128
# Unit test for function escape
def test_escape():
    m = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\x0f")
    escape(m)
    m = re.match(r"\\('|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\xg")
    escape(m)

# Generated at 2022-06-13 17:51:57.520198
# Unit test for function escape
def test_escape():
    assert escape(re.search(r'\\x', '\\x')) == "x"
    assert escape(re.search(r'\\x', '\\xab')) == chr(0xab)
    assert escape(re.search(r'\\x', '\\xAB')) == chr(0xab)
    assert escape(re.search(r'\\x', '\\xarbitrary')) == chr(0xa)
    assert escape(re.search(r'\\x', '\\x0')) == chr(0x0)
    try:
        escape(re.search(r'\\x', '\\x'))
        assert False
    except TypeError:
        pass
    assert escape(re.search(r'\\x', '\\x'))  # type: ignore

# Generated at 2022-06-13 17:52:03.008440
# Unit test for function escape
def test_escape():
    assert escape(re.match("\\x2a", "\\x2a")) == "*"
    assert escape(re.match("\\146", "\\146")) == "F"

# Generated at 2022-06-13 17:52:09.674571
# Unit test for function escape
def test_escape():
    """
    >>> test_escape()
    [['\\x00', 'x00', '\\x00'], ['$0', '0', '\\x00'], ['\\x00', 'x00', '\\x00'], ['$0', '0', '\\x00']]
    """
    import re
    pattern = r"\\x"
    repl = "\\x"
    src = "\\x00"
    regex = re.compile(pattern)
    res = regex.subn(repl, src)
    print(res)

# Generated at 2022-06-13 17:52:11.389053
# Unit test for function test
def test_test():
    try:
        test()
    except Exception as e:
        print(e)
        assert False

# Generated at 2022-06-13 17:52:21.805793
# Unit test for function escape
def test_escape():
    assert escape(re.search(r'\\"', '"')) == '"'
    assert escape(re.search(r"\\'", "'")) == "'"

# Generated at 2022-06-13 17:52:35.181877
# Unit test for function escape
def test_escape():
    from unittest import TestCase

    class Test(TestCase):
        def test_escape(self):
            self.assertEqual(escape(re.match(r"\\'", r"\'")), "'")
            self.assertEqual(escape(re.match(r"\\x01", r"\x01")), "\x01")
            self.assertEqual(escape(re.match(r"\\000", r"\000")), "\000")

# Generated at 2022-06-13 17:52:46.910102
# Unit test for function escape
def test_escape():
    assert '\a' == escape(re.match(r"(\\a)", "\\a"))
    assert '\b' == escape(re.match(r"(\\b)", "\\b"))
    assert '\f' == escape(re.match(r"(\\f)", "\\f"))
    assert '\n' == escape(re.match(r"(\\n)", "\\n"))
    assert '\r' == escape(re.match(r"(\\r)", "\\r"))
    assert '\t' == escape(re.match(r"(\\t)", "\\t"))
    assert '\v' == escape(re.match(r"(\\v)", "\\v"))
    assert "'" == escape(re.match(r"(\\')", "\\'"))

# Generated at 2022-06-13 17:52:48.206881
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\x', '')) == ''
    assert escape(re.match(r'\\', '')) == ''
    assert escape(re.match(r'', '')) == ''

# Generated at 2022-06-13 17:52:49.064349
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:00.504141
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x", "\\x")) == "\\x"
    assert escape(re.match(r"\\x1", "\\x1")) == "\x01"
    assert escape(re.match(r"\\x12", "\\x12")) == "\x12"
    assert escape(re.match(r"\\x123", "\\x123")) == "\x123"
    assert escape(re.match(r"\\b", "\\b")) == "\x08"
    assert escape(re.match(r"\\08", "\\08")) == "\x08"
    assert escape(re.match(r"\\0a", "\\0a")) == "\n"

# Generated at 2022-06-13 17:53:10.563321
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv]|[0-7]{1,3})", "\\x0a")) == "\n"
    assert escape(re.match(r"\\([abfnrtv]|[0-7]{1,3})", "\\12")) == "\n"
    assert escape(re.match(r"\\([abfnrtv]|[0-7]{1,3})", "\\011")) == "\t"
    assert escape(re.match(r"\\([abfnrtv]|[0-7]{1,3})", "\\t")) == "\t"
    assert escape(re.match(r"\\([abfnrtv]|[0-7]{1,3})", "\\a")) == "\a"

# Generated at 2022-06-13 17:53:16.937805
# Unit test for function escape
def test_escape():
    # real
    assert escape("\\x41") == "A"
    assert escape("\\x61") == "a"
    assert escape("\\n") == "\n"
    assert escape("\\t") == "\t"
    assert escape("\\'") == "'"
    assert escape('\\"') == '"'
    assert escape("\\\\") == "\\"
    assert escape("\\a") == "\x07"
    assert escape("\\v") == "\x0b"
    assert escape("\\f") == "\x0c"
    assert escape("\\r") == "\r"
    assert escape("\\b") == "\x08"
    assert escape("\\x42x43x44x45") == "BCDE"
    assert escape("\\x0B") == "\x0b"

# Generated at 2022-06-13 17:53:26.290118
# Unit test for function escape
def test_escape():
    r = r"\367"
    m = re.compile(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})").match(r)
    assert escape(m) == chr(0x367)
    r = r"\a"
    m = re.compile(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})").match(r)
    assert escape(m) == chr(7)
    r = r"\n"
    m = re.compile(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})").match(r)
    assert escape(m) == chr

# Generated at 2022-06-13 17:53:35.956290
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\0', '\\0')) == '\x00'
    assert escape(re.match(r'\\0', '\\0')) != 'a'
    assert escape(re.match(r'\\1', '\\1')) == '\x01'
    assert escape(re.match(r'\\1', '\\1')) != 'a'
    assert escape(re.match(r'\\1', '\\1')) != 'b'
    assert escape(re.match(r'\\1', '\\1')) != 'c'
    assert escape(re.match(r'\\2', '\\2')) == '\x02'
    assert escape(re.match(r'\\2', '\\2')) != 'b'

# Generated at 2022-06-13 17:53:38.071230
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:54:08.506753
# Unit test for function test
def test_test():
    test()



# Generated at 2022-06-13 17:54:09.060915
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:54:12.656368
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x3f", "\\x3f")) == "?"
    try:
        escape(re.match(r"\\x", "\\x"))
    except ValueError:
        pass
    else:
        assert False, "ValueError should be raised"

# Generated at 2022-06-13 17:54:13.681414
# Unit test for function test
def test_test():
    """
    Test function test
    """
    test()

# Generated at 2022-06-13 17:54:18.111729
# Unit test for function escape
def test_escape():
    tests = {
        "\\x00": chr(0),
        "\\n": "\n",
        "\\07": chr(7),
        "\\'": "'",
    }

    for test in tests:
        assert escape((test, test[1])) == tests[test]



# Generated at 2022-06-13 17:54:26.553345
# Unit test for function escape
def test_escape():
    assert escape('\\') == '\\'
    assert escape('\\a') == '\x07'
    assert escape('\\n') == '\n'
    assert escape('\\t') == '\t'
    assert escape('\\x0') == '\x00'
    assert escape('\\x1') == '\x01'
    assert escape('\\xff') == chr(255)
    assert escape('\\xff') == '\xff'
    assert escape('\\377') == '\xFF'
    assert escape('\\777') == chr(511)
    assert escape('\\777') == '\xFF'

# Generated at 2022-06-13 17:54:35.111223
# Unit test for function escape

# Generated at 2022-06-13 17:54:39.436927
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\x01','\\x01')) == '\x01'
    assert escape(re.match(r'\\xF','\\xF')) == '\x0f'
    assert escape(re.match(r'\\x55','\\x55')) == 'U'

# Generated at 2022-06-13 17:54:41.072568
# Unit test for function test
def test_test():
    try:
        test()
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

# Generated at 2022-06-13 17:54:42.394068
# Unit test for function test
def test_test():
    # verify that test() doesn't crash
    test()

# Generated at 2022-06-13 17:55:03.770273
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:04.649392
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:12.152352
# Unit test for function test
def test_test():
    '''
    Test for escape function
    :return:
    '''
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = escape(s)
        if e != c:
            print(i, c, s, e)


if __name__ == "__main__":
    test()

# Generated at 2022-06-13 17:55:21.301368
# Unit test for function escape
def test_escape():
    test_str1 = r"\n"
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", test_str1)) == "\n"

    test_str1 = r"\xaa"
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", test_str1)) == "\xaa"

    test_str1 = r"\xAa"

# Generated at 2022-06-13 17:55:23.281440
# Unit test for function test
def test_test():
    try:
        test()
    except:
        assert False

# Generated at 2022-06-13 17:55:26.377437
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\x', 'test')) == 'x'
    assert escape(re.match('\\x', 'test')) == 'x'

# Generated at 2022-06-13 17:55:29.526626
# Unit test for function test
def test_test():
    import sys

    try:
        test()
    except AssertionError as ex:
        assert 0, ex


# Generated at 2022-06-13 17:55:40.611292
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\a', r'\a')) == '\x07'
    assert escape(re.match(r'\\b', r'\b')) == '\x08'
    assert escape(re.match(r'\\c', r'\c')) == '\x03'
    assert escape(re.match(r'\\f', r'\f')) == '\x0c'
    assert escape(re.match(r'\\n', r'\n')) == '\n'
    assert escape(re.match(r'\\r', r'\r')) == '\r'
    assert escape(re.match(r'\\t', r'\t')) == '\t'
    assert escape(re.match(r'\\v', r'\v'))

# Generated at 2022-06-13 17:55:41.402757
# Unit test for function test
def test_test():
    pass

# Generated at 2022-06-13 17:55:51.618181
# Unit test for function test
def test_test():
    for i in range(257):
        if i == 256:
            f = '\u0100'
        elif i == 257:
            f = '\u0101'
        elif i == 258:
            f = '\u0102'
        elif i == 259:
            f = '\u0103'
        elif i == 260:
            f = '\u0104'
        elif i == 261:
            f = '\u0105'
        elif i == 262:
            f = '\u0106'
        elif i == 263:
            f = '\u0107'
        elif i == 264:
            f = '\u0108'
        elif i == 265:
            f = '\u0109'

# Generated at 2022-06-13 17:56:12.494897
# Unit test for function test
def test_test():
    try:
        test()
    except:
        print("test() failed")

test_test()

# Generated at 2022-06-13 17:56:21.975205
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

# Generated at 2022-06-13 17:56:29.343400
# Unit test for function test
def test_test():
    import os
    import tempfile
    import shutil

    test_path = "eval_tests"
    test_data = b"\x00\x01\x02\x0f\x10\x7f\xc2\x80\xc3\x80\xff\x01\x0e\x7f\xc2\x81\xc3\x81\xff\x01"

    def _write_test_data(test_data):
        output_base_path = os.path.join(os.path.dirname(__file__), test_path)
        os.makedirs(output_base_path, exist_ok=True)
        output_file_path = tempfile.mkstemp(suffix=".bin", prefix="eval_test_", dir=output_base_path)[1]

# Generated at 2022-06-13 17:56:39.264705
# Unit test for function escape
def test_escape():
    assert escape('\'') == "'"
    assert escape('\'"') == '\''
    assert escape('\\') == '\\'
    assert escape('\\x') == 'x'
    assert escape('\\x1') == '\x01'
    assert escape('\\x10') == '\x10'
    try:
        escape('\\x11')
    except ValueError:
        pass
    else:
        assert False, 'Expected ValueError'

    assert escape('\\x11\\') == '\x11\\'
    assert escape('\\x1a') == '\x1a'
    assert escape('\\x20') == ' '
    assert escape('\\x7f') == '\x7f'
    assert escape('\\x7f\\') == '\x7f\\'


# Generated at 2022-06-13 17:56:46.330347
# Unit test for function escape
def test_escape():
    exp = '\xFF\n'
    for val, res in [(r"\377", exp), (r'\xFF', exp), (r"\xFF\n", exp + '\n')]:
        assert escape(re.match(r"\\(\377|xFF|xFF\n)", val)) == res, val

# Generated at 2022-06-13 17:56:47.347464
# Unit test for function test
def test_test():
    # Execute test function
    test()

# Generated at 2022-06-13 17:56:57.021706
# Unit test for function escape
def test_escape():
    class Test:
        def __init__(self, pattern: str, groups: str, string: str, escape_string: str):
            self.pattern = pattern
            self.groups = groups
            self.string = string
            self.escape_string = escape_string
            self.m = re.compile(self.pattern).match(self.string)
            self.expected = eval(self.groups)
            self.result = escape(self.m)


# Generated at 2022-06-13 17:57:04.050434
# Unit test for function escape
def test_escape():
    # test_escape_pass
    assert escape(re.search(r"\a", "abcdefghijklmnopqrstuvwxyz")) == "\a"
    assert escape(re.search(r"\n", "abcdefg" + "\n")) == "\n"
    assert escape(re.search(r"\x10", "abcdefghijklmnopqrstuvwxyz")) == "\x10"
    assert escape(re.search(r"\x1a", "abcdefghijklmnopqrstuvwxyz")) == "\x1a"
    assert escape(re.search(r"\x25", "abcdefghijklmnopqrstuvwxyz")) == "%"

# Generated at 2022-06-13 17:57:17.599375
# Unit test for function escape
def test_escape():
    assert escape(0) == '\x00'
    assert escape(r'\x00') == '\x00'
    assert escape(r'\x7f') == '\x7f'
    assert escape(r'\x80') == '\x80'
    assert escape(r'\xff') == '\xff'

    assert escape(r'\a') == '\x07'
    assert escape(r'\b') == '\x08'
    assert escape(r'\f') == '\x0c'
    assert escape(r'\n') == '\x0a'
    assert escape(r'\r') == '\x0d'
    assert escape(r'\t') == '\x09'
    assert escape(r'\v') == '\x0b'


# Generated at 2022-06-13 17:57:18.414159
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:01.219948
# Unit test for function test
def test_test():
    import io
    import sys
    save_stdout = sys.stdout
    try:
        out = io.StringIO()
        sys.stdout = out
        test()
        output = out.getvalue().strip()
        assert output == ""
    finally:
        sys.stdout = save_stdout

# Generated at 2022-06-13 17:58:04.036283
# Unit test for function test
def test_test():
    # pylint: disable=no-member
    test()

# Generated at 2022-06-13 17:58:17.054344
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x41", r"\x41")) == "A"
    assert escape(re.match(r"\\u0041", r"\u0041")) == "A"
    assert escape(re.match(r"\\U00000041", r"\U00000041")) == "A"
    assert escape(re.match(r"\\41", r"\41")) == "!"
    assert escape(re.match(r"\\041", r"\041")) == "!"
    assert escape(re.match(r"\\0041", r"\0041")) == "!"
    assert escape(re.match(r"\\u005c", r"\u005c")) == "\\"

# Generated at 2022-06-13 17:58:18.779399
# Unit test for function test
def test_test():
    """Test for evalString"""
    from test.test_support import captured_stdout

    with captured_stdout():
        test()

# Generated at 2022-06-13 17:58:21.917028
# Unit test for function test
def test_test():
    @strict_positive
    def f(x: int) -> int:
        return x + 1

    f(-1)

    # Test with a quick checker that doesn't type check:
    @quick_positive
    def g(x: int) -> int:
        return x + 1

    g(-1)



# Generated at 2022-06-13 17:58:27.122065
# Unit test for function test
def test_test():
    import pytest

    from typing import Callable

    test_test_cases: Dict[Callable, str] = {test: "test()"}
    for fn, reason in test_test_cases.items():
        fn = pytest.param(fn, marks=pytest.mark.unit, reason=reason)
        assert fn

# Generated at 2022-06-13 17:58:31.119441
# Unit test for function test
def test_test():
    """Test for the test function."""
    # pylint: disable=missing-docstring,no-member
    from io import StringIO

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    with patch("sys.stdout", new=StringIO()) as fake_out:
        test()
    output = fake_out.getvalue().strip()
    assert output == ""

# Generated at 2022-06-13 17:58:35.614458
# Unit test for function escape
def test_escape():
    # can't access re.Match object, so just a basic test
    assert escape('\\')=='\\'
    assert escape('\\n')=='\n'
    assert escape('\\x')=='x'
    assert escape('\\x1')=='\x01'


# Generated at 2022-06-13 17:58:36.475631
# Unit test for function test
def test_test():
    test()



# Generated at 2022-06-13 17:58:37.006531
# Unit test for function test
def test_test():
    test()