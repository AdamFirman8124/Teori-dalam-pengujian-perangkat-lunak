

# Generated at 2022-06-13 17:50:03.860507
# Unit test for function escape
def test_escape():
    tests = {
        "\\0": "\0",
        "\\a": "\a",
        "\\b": "\b",
        "\\f": "\f",
        "\\n": "\n",
        "\\r": "\r",
        "\\t": "\t",
        "\\v": "\v",
        "\\'": "'",
        "\\\"": '"',
        "\\x00": "\0",
        "\\x01": "\x01",
        "\\x7e": "\x7e",
        "\\x7f": "\x7f",
    }
    for s, expected in tests.items():
        actual = escape(s)
        assert actual == expected, "escape({!r}) == {!r}".format(s, actual)

# Generated at 2022-06-13 17:50:04.568196
# Unit test for function test
def test_test():
    assert test() is None

# Generated at 2022-06-13 17:50:10.914044
# Unit test for function evalString
def test_evalString():

    assert evalString('"\\141"') == "a"
    assert evalString('"\\x41"') == "A"
    assert evalString('"\\x\x41"') == "A"

    # Invalid escape sequences are caught by the compiler
    assert evalString('"\\x\x41"') == "A"
    assert evalString('"\\x\x41"') == "A"

# Generated at 2022-06-13 17:50:20.817134
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", "\\a")) == "\a"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", "\\b")) == "\b"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", "\\f")) == "\f"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", "\\n")) == "\n"
    assert escape

# Generated at 2022-06-13 17:50:30.143017
# Unit test for function escape
def test_escape():
    import unittest
    import re

    class TestEscape(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass


# Generated at 2022-06-13 17:50:30.660289
# Unit test for function escape
def test_escape():
    assert escape(Match)

# Generated at 2022-06-13 17:50:38.744386
# Unit test for function evalString
def test_evalString():
    import string
    import test.support
    from test.support import importhook
    from typing import Any

    class BadImport(Exception):
        pass

    class BadImportHook:
        def find_module(  # type: ignore
            self, fullname: Any, path: Any
        ) -> Any:
            if fullname == "test.string_tests":
                raise BadImport
            return importhook.exact_import(fullname, path)

    tests = ()
    with test.support.swap_attr(importhook, "exact_import", BadImportHook()):
        try:
            __import__("test.string_tests")
        except BadImport:
            pass
        else:
            raise AssertionError("import hook not called")


# Generated at 2022-06-13 17:50:45.942615
# Unit test for function evalString
def test_evalString():
    assert evalString("'python'") == 'python'
    assert evalString('"python"') == 'python'
    assert evalString("'''python'''") == 'python'
    assert evalString('"""""python"""') == '"""python'
    assert evalString("'\x06'") == chr(0x6)
    assert evalString("'\x06x'") == chr(0x6) + 'x'
    assert evalString("'\x06x'") == chr(0x6) + 'x'
    assert evalString("'\\x06x'") == chr(0x6) + 'x'
    assert evalString("'\\x06'") == chr(0x6)
    assert evalString("'\\x06'") == chr(0x6)
    assert evalString

# Generated at 2022-06-13 17:50:48.957280
# Unit test for function escape
def test_escape():
    assert escape("\\a\\b\\f\\n\\r\\t\\v\\\\\'\\\"\\x0d") == "\a\b\f\n\r\t\v\\\'\"\x0d"
    assert escape("\\x0D") == "\x0D"
    assert escape("\\x0x") == "\\x0x"

# Generated at 2022-06-13 17:50:50.987321
# Unit test for function escape
def test_escape():
    try:
        assert escape('\\x') == ValueError
    except:
        pass


# Generated at 2022-06-13 17:51:22.443768
# Unit test for function escape
def test_escape():
    from lib2to3 import pytree

    from .fix_literal_eval import escape

    class FixLiteralEvalChecker(object):
        def __init__(self, tree: pytree.Base, filename: Text) -> None:
            pass

        def run(self) -> None:
            pass

        @staticmethod
        def fix(m: Match[Text]) -> Text:
            all, tail = m.group(0, 1)
            assert all.startswith("\\")
            esc = escape(m)
            return esc

    import sys

    FixLiteralEvalChecker.fix(
        re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", sys.argv[1])
    )

# Generated at 2022-06-13 17:51:25.540157
# Unit test for function escape
def test_escape():
    m = re.search(r"\\(?P<tail>x.{0,2})", "\\x09")
    assert m
    assert escape(m) == "\t"


# Generated at 2022-06-13 17:51:35.210131
# Unit test for function escape
def test_escape():
    # Simple test case
    assert escape(re.match(r"\\(x..)", "\\xff")) == "\xff"

    # Test error handling
    try:
        escape(re.match(r"\\(x..)", "\\x54"))
        assert False, "previous statement should have raised ValueError"
    except ValueError as e:
        assert e.args[0] == "invalid hex string escape ('\\x54')"

    try:
        escape(re.match(r"\\(..)", "\\400"))
        assert False, "previous statement should have raised ValueError"
    except ValueError as e:
        assert e.args[0] == "invalid octal string escape ('\\400')"

    # Test non-string-returning expressions

# Generated at 2022-06-13 17:51:39.582995
# Unit test for function escape
def test_escape():
    assert escape('\\n') == '\n'
    assert escape('\\x20') == ' '
    assert escape('\\0') == '\x00'
    assert escape('\\01') == '\x01'
    assert escape('\\012') == '\n'

    try:
        escape('\\x')
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError')

    try:
        escape('\\x2')
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError')

    try:
        escape('\\')
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError')

    try:
        escape('\\9')
    except ValueError:
        pass

# Generated at 2022-06-13 17:51:49.480461
# Unit test for function escape
def test_escape():
    # Test simple escape
    assert escape(re.match('(\\b)', '\\b')) == "\b"
    assert escape(re.match('(\\n)', '\\n')) == "\n"
    assert escape(re.match('(\\t)', '\\t')) == "\t"

    # Test hex escape
    assert escape(re.match('(\\xA1)', '\\xA1')) == "\u00A1"
    assert escape(re.match('(\\xA)', '\\xA')) == "\u000A"
    assert escape(re.match('(\\x)', '\\x')) == "x"

    # Test octal escape
    assert escape(re.match('(\\1)', '\\1')) == "\u0001"

# Generated at 2022-06-13 17:51:59.030999
# Unit test for function escape
def test_escape():
    test_list = [
        ("abacaxi", "abacaxi"),
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
        ("\\*", "*"),
        ("\\x41", "A"),
        ("\\x61", "a"),
        ("\\u0041", "A"),
        ("\\u0061", "a"),
        ("\\U00000041", "A"),
        ("\\U00000061", "a"),
        ("\\U00000001", "\u0001"),
    ]


# Generated at 2022-06-13 17:52:05.025553
# Unit test for function escape
def test_escape():
    escapes = [
        ("\\a", "\a"),
        ("\\b", "\b"),
        ("\\f", "\f"),
        ("\\n", "\n"),
        ("\\r", "\r"),
        ("\\t", "\t"),
        ("\\v", "\v"),
        ("\\'", "'"),
        ('\\"', '"'),
        ("\\\\", "\\")
    ]
    for (esc, expected) in escapes:
        assert escape(re.match(r"\\(.+)", esc)) == expected

# Generated at 2022-06-13 17:52:11.194274
# Unit test for function escape
def test_escape():
    assert escape("\a") == "a"
    assert escape("\b") == "b"
    assert escape("\f") == "f"
    assert escape("\n") == "n"
    assert escape("\r") == "r"
    assert escape("\t") == "t"
    assert escape("\v") == "v"
    assert escape("\'") == "\'"
    assert escape("\"") == "\""
    assert escape("\\") == "\\"

# Generated at 2022-06-13 17:52:21.678343
# Unit test for function escape

# Generated at 2022-06-13 17:52:31.737040
# Unit test for function escape
def test_escape():
    assert escape(r"\n") == "\n"
    assert escape(r"\r") == "\r"
    assert escape(r"\t") == "\t"

    # test octal
    assert escape(r"\0") == "\0"
    assert escape(r"\1") == "\1"
    assert escape(r"\7") == "\7"
    assert escape(r"\123") == chr(0o123)
    assert escape(r"\1234") == chr(0o123) + "4"
    assert escape(r"\400") == chr(0o40)
    assert escape(r"\406") == chr(0o40) + "6"
    assert escape(r"\777") == chr(0o377)
    assert escape(r"\1234")

# Generated at 2022-06-13 17:53:22.947921
# Unit test for function escape
def test_escape():
    assert escape(re.search('\\{0}'.format(''), '\\')) == '\\'
    assert escape(re.search('\\{0}'.format('a'), '\\a')) == '\a'
    assert escape(re.search('\\{0}'.format('b'), '\\b')) == '\b'
    assert escape(re.search('\\{0}'.format('f'), '\\f')) == '\f'
    assert escape(re.search('\\{0}'.format('n'), '\\n')) == '\n'
    assert escape(re.search('\\{0}'.format('r'), '\\r')) == '\r'
    assert escape(re.search('\\{0}'.format('t'), '\\t')) == '\t'

# Generated at 2022-06-13 17:53:30.940829
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\a', 'a')) == '\a'  # \a
    assert escape(re.match('\\\\', 'a')) == '\\' # \\
    assert escape(re.match('\\xFF', 'a')) == '\xFF'  # \xFF
    assert escape(re.match('\\77', 'a')) == '?'  # \77
    assert escape(re.match('\\0', 'a')) == '\x00'  # \0
    assert escape(re.match('\\1', 'a')) == '\x01'  # \1
    assert escape(re.match('\\7', 'a')) == '\x07'  # \7
    assert escape(re.match('\\8', 'a')) == '\x08'  # \

# Generated at 2022-06-13 17:53:34.612455
# Unit test for function escape
def test_escape():
    output = evalString(r"\x19")
    assert output == "\x19"

    with pytest.raises(ValueError, match=r"invalid hex string escape"):
        evalString(r"\x1!")



# Generated at 2022-06-13 17:53:39.908343
# Unit test for function escape
def test_escape():
    # Test for simple escapes, should return the correct escape character
    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"
    assert escape(re.match(r"\\r", "\\r")) == "\r"
    assert escape(re.match(r"\\t", "\\t")) == "\t"
    assert escape(re.match(r"\\v", "\\v")) == "\v"
    assert escape(re.match(r"\\'", "\\'")) == "'"

# Generated at 2022-06-13 17:53:50.559938
# Unit test for function escape

# Generated at 2022-06-13 17:53:59.937755
# Unit test for function escape
def test_escape():
    assert escape(('\\x41', 'x41')).encode() == b'A'
    assert escape(('\\a', 'a')).encode() == b'\x07'
    assert escape(('\\r', 'r')).encode() == b'\r'
    assert escape(('\\xABCD', 'xABCD')).encode() == b'\xab'
    assert escape(('\\xA', 'xA')) == '\n'
    assert escape(('\\xA', 'xA')) == '\n'
    assert escape(('\\x6', 'x6')) == '\x06'
    assert escape(('\\x6', 'x6')) == '\x06'



# Generated at 2022-06-13 17:54:00.689510
# Unit test for function test
def test_test():
    pass

# Generated at 2022-06-13 17:54:11.453452
# Unit test for function escape

# Generated at 2022-06-13 17:54:13.140721
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\b','\b')) == '\b'

# Generated at 2022-06-13 17:54:13.819842
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:17.625427
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\([abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\\x1a')) == '\x1a'
    assert escape(re.match(r'\\([abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\\01')) == '\x01'
    assert escape(re.match(r'\\([abfnrtv]|x.{0,2}|[0-7]{1,3})', r"\\'")) == "'"
    assert escape(re.match(r'\\([abfnrtv]|x.{0,2}|[0-7]{1,3})', r'\\"')) == '"'

# Generated at 2022-06-13 17:55:26.789643
# Unit test for function escape
def test_escape():
    # Test escape on the default escapes
    assert escape(re.search("\\0", "\\0")) == "\0"
    assert escape(re.search("\\a", "\\a")) == "\a"
    assert escape(re.search("\\b", "\\b")) == "\b"
    assert escape(re.search("\\f", "\\f")) == "\f"
    assert escape(re.search("\\n", "\\n")) == "\n"
    assert escape(re.search("\\r", "\\r")) == "\r"
    assert escape(re.search("\\t", "\\t")) == "\t"
    assert escape(re.search("\\v", "\\v")) == "\v"
    # Test escape on the general escapes
    assert escape(re.search("\\0", "\\00")) == "\0"
   

# Generated at 2022-06-13 17:55:37.363303
# Unit test for function escape
def test_escape():
    assert escape("a") == r"a"
    assert escape("b") == r"b"
    assert escape("f") == r"f"
    assert escape("n") == r"n"
    assert escape("r") == r"r"
    assert escape("t") == r"t"
    assert escape("v") == r"v"
    assert escape("'") == r"'"
    assert escape('"') == r'"'

# Generated at 2022-06-13 17:55:47.209477
# Unit test for function escape
def test_escape():
  assert escape(re.search(r'\\b', r'\b')) == '\b', '\\b'
  assert escape(re.search(r'\\f', r'\f')) == '\f', '\\f'
  assert escape(re.search(r'\\n', r'\n')) == '\n', '\\n'
  assert escape(re.search(r'\\r', r'\r')) == '\r', '\\r'
  assert escape(re.search(r'\\t', r'\t')) == '\t', '\\t'
  assert escape(re.search(r'\\v', r'\v')) == '\v', '\\v'

# Generated at 2022-06-13 17:55:48.113876
# Unit test for function escape
def test_escape():
    assert escape("\\x00") == "\x00"

# Generated at 2022-06-13 17:55:48.726566
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:58.182476
# Unit test for function escape
def test_escape():

    assert escape(re.match(r'\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', '\\\'')) == '\'', \
        test_escape.__doc__
    assert escape(re.match(r'\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', '\\"')) == '"', \
        test_escape.__doc__
    assert escape(re.match(r'\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', '\\a')) == '\a', \
        test_escape.__doc__

# Generated at 2022-06-13 17:56:02.567505
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\b', r'\b')) == '\b'
    assert escape(re.match(r'\\f', r'\f')) == '\f'
    assert escape(re.match(r'\\n', r'\n')) == '\n'
    assert escape(re.match(r'\\r', r'\r')) == '\r'
    assert escape(re.match(r'\\t', r'\t')) == '\t'
    assert escape(re.match(r'\\v', r'\v')) == '\v'
    assert escape(re.match(r'\\\'', r'\'')) == '\''
    assert escape(re.match(r'\\"', r'"')) == '"'

# Generated at 2022-06-13 17:56:03.650833
# Unit test for function test

# Generated at 2022-06-13 17:56:12.198227
# Unit test for function escape
def test_escape():
    assert escape("\\'") == "'"
    assert escape("\\\"") == "\""
    assert escape("\\\\") == "\\"
    assert escape("\\b") == "\b"
    assert escape("\\f") == "\f"
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("\\x41") == "A"
    assert escape("\\072") == ":"


# Generated at 2022-06-13 17:57:48.792114
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:57:55.491873
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\x([0-9a-fA-F]{2})', '\\x5C')) == '\\'
    assert escape(re.match(r'\\x([0-9a-fA-F]{2})', '\\x5c')) == '\\'


# Generated at 2022-06-13 17:57:56.300110
# Unit test for function escape
def test_escape():
    assert escape('\\n'), '\\n' == '\n'


# Generated at 2022-06-13 17:57:56.789348
# Unit test for function test
def test_test():
    test()


# Generated at 2022-06-13 17:57:58.960249
# Unit test for function escape
def test_escape():
    test_escape_simple()
    test_escape_octal()
    test_escape_hex()
    test_escape_invalid()


# Generated at 2022-06-13 17:58:08.823312
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

    assert escape('\\x0a') == '\n'
    assert escape('\\xff') == chr(255)
    assert escape('\\377') == chr(255)

    with raises(ValueError):
        escape('\\')
    with raises(ValueError):
        escape('\\x')


# Generated at 2022-06-13 17:58:18.098359
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\x2f", "\\x2f")) == "/"
    assert escape(re.match(r"\\xff", "\\xff")) == "\xff"
    assert escape(re.match(r"\\377", "\\377")) == "\xff"
    assert escape(re.match(r"\\0", "\\0")) == "\0"
    assert escape(re.match(r"\\a", "\\a")) == "\a"
    assert escape(re.match(r"\\b", "\\b")) == "\b"
    assert escape(re.match(r"\\f", "\\f")) == "\f"
    assert escape(re.match(r"\\n", "\\n")) == "\n"

# Generated at 2022-06-13 17:58:18.559993
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:58:25.496234
# Unit test for function escape
def test_escape():
    assert escape('\\t') == '\t'
    assert escape('\\x11') == '\x11'
    assert escape('\\xF') == '\x0f'
    assert escape('\\xFA') == '\xfa'
    assert escape('\\xFAb') == '\xfab'
    assert escape('\\xFAbB') == '\xfabb'
    assert escape('\\xFAbB\\') == '\xfabb\\'
    assert escape('\\xFAbB\\t') == '\xfabb\t'
    assert escape('\\xFAbB\\x') == '\xfabb\\x'
    assert escape('\\xFAbB\\xT') == '\xfabb\\xT'
    assert escape('\\xFAbB\\xTT') == '\xfabb\\xTT'


# Generated at 2022-06-13 17:58:31.759888
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", "\\x2g")) == r"\x2g"  # noqa
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", "\\t")) == "t"
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", "\\7")) == "\\7"