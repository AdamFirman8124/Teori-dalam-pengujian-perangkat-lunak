

# Generated at 2022-06-13 17:50:03.860582
# Unit test for function escape
def test_escape():
    assert escape(re.match('\\n', '\\n')) == '\n'
    assert escape(re.match('\\x00', '\\x00')) == '\x00'
    assert escape(re.match('\\x00', '\\x0')) == '\x00'
    assert escape(re.match('\\x00', '\\x')) == '\x00'
    assert escape(re.match('\\x00', '\\')) == '\x00'
    assert escape(re.match('\\n', '\\')) == '\n'
    assert escape(re.match('\\oct', '\\')) == '\n'

# Generated at 2022-06-13 17:50:16.034089
# Unit test for function escape
def test_escape():
    assert escape('\\\a') == '\a'
    assert escape('\\\b') == '\b'
    assert escape('\\\f') == '\f'
    assert escape('\\\n') == '\n'
    assert escape('\\\r') == '\r'
    assert escape('\\\t') == '\t'
    assert escape('\\\v') == '\v'
    assert escape("\\\'") == "'"
    assert escape('\\\"') == '"'

# Generated at 2022-06-13 17:50:23.452756
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
    assert escape("\\x0a") == "\n"
    assert escape("\\012") == "\n"
    assert escape("\\xFF") == "\xff"
    assert escape("\\377") == "\xff"
    assert escape("\\xH") == "xH"
    assert escape("\\xHZ") == "xHZ"
   

# Generated at 2022-06-13 17:50:31.451591
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
  assert escape("\\\"") == "\""
  assert escape("\\\a") == "\a"
  assert escape("\\3") == "3"
  assert escape("\\03") == "\x03"
  assert escape("\\003") == "\x03"
  assert escape("\\0003") == "\x03"
  assert escape("\\x9") == "\t"
  assert escape

# Generated at 2022-06-13 17:50:41.637271
# Unit test for function escape
def test_escape():
    assert escape('\\a') == '\a'
    assert escape('\\\a') == '\\\a'
    assert escape('\\b') == '\b'
    assert escape('\\f') == '\f'
    assert escape('\\n') == '\n'
    assert escape('\\r') == '\r'
    assert escape('\\t') == '\t'
    assert escape('\\v') == '\v'
    assert escape('\\\'') == '\\\''
    assert escape('\\\"') == '\\\"'
    assert escape('\\\\') == '\\\\'
    assert escape('\\x41') == 'A'
    assert escape('\\x1') == '\\x1'
    assert escape('\\x') == '\\x'
    assert escape('\\x0') == '\\x0'

# Generated at 2022-06-13 17:50:48.874949
# Unit test for function escape
def test_escape():
    test_case = r"\a\b\f\n\r\t\v\\\'\"\x00\x7f\xff\123\0123"
    expected = "\a\b\f\n\r\t\v\\\'\"\x00\x7f\xffS{"
    patched = re.sub(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", escape, test_case)
    assert patched == expected
    # deal with error test
    expected_error = ValueError("invalid hex string escape ('\\x0')")

# Generated at 2022-06-13 17:50:58.922265
# Unit test for function escape
def test_escape():
    assert escape("\\'") == "\'"
    assert escape("\\''") == "\'"
    assert escape("\\\"") == '"'
    assert escape("\\a") == "\a"
    assert escape("\\b") == "\b"
    assert escape("\\f") == "\f"
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("\\x0a") == "\n"
    assert escape("\\x61") == "a"
    assert escape("\\377") == "\xFF"
    assert escape("\\378") == "8"
    assert escape("\\378\\1") == "8\\1"
    assert escape("\\x") == "x"

# Generated at 2022-06-13 17:51:01.304634
# Unit test for function test
def test_test():
    with pytest.raises(AssertionError):
        test()

# Generated at 2022-06-13 17:51:08.887073
# Unit test for function escape
def test_escape():
    m = re.search(r"\\(.)", "\\t")
    assert escape(m) == "\t"
    m = re.search(r"\\(.)", '\\"')
    assert escape(m) == '"'
    m = re.search(r"\\(.)", "\\'")
    assert escape(m) == "'"
    m = re.search(r"\\(.)", "\\xFF")
    assert escape(m) == "\xFF"
    m = re.search(r"\\(.)", "\\xABCD")
    assert escape(m) == "\xAB\xCD"
    m = re.search(r"\\(.)", "\\xABC")
    assert escape(m) == "\xAB"

# Generated at 2022-06-13 17:51:12.335500
# Unit test for function escape
def test_escape():
    assert escape("\\a") == "\a"
    print("Test passed!")

test_escape()

# Generated at 2022-06-13 17:51:32.123788
# Unit test for function evalString
def test_evalString():

    # Tests
    test_strings = [
        '"A"',
        "'A'",
        '"\\"A\\""',
        "'\\'A\\''",
        '"\\\'"',
        "'\\\"'",
        '"A\\"',
        "'A\\'",
        '"\\u1234"',
        "'\\u1234'",
        '"\\U00001234"',
        "'\\U00001234'",
        '"\\\n"',
        '"\\\t"',
        '"""foo"""',
        '"""\\"\\"\\\"""',
        '"\\"\\"\\""',
    ]
    for t in test_strings:
        evalString(t)

# Generated at 2022-06-13 17:51:37.190054
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\[\w]", "\\z")) == "z"
    assert escape(re.match(r"\\[\w]", "\\\\")) == "\\"
    assert escape(re.match(r"\\[\w]", "\\a")) == "\a"
    assert escape(re.match(r"\\[\w]", "\\xab")) == "\xab"
    assert escape(re.match(r"\\[\w]", "\\xaa")) == "\xaa"

# Generated at 2022-06-13 17:51:47.257246
# Unit test for function evalString
def test_evalString():
    import ast
    from .tokenize import generate_tokens
    from .token import *

    def eval_string(s):
        (result, end) = evalString(s)
        if end != len(s):
            raise ValueError("result %r didn't use all of input %r" % (result, s))
        return result

    def test_all(s):
        if s[0] in '"\'':
            test_all(repr(eval_string(s)))
        elif s == "None":
            assert eval_string(s) is None
        elif s == "Ellipsis":
            assert eval_string(s) is Ellipsis
        else:
            eval_string(s)

    test_all("[]")
    test_all("()")
    test_all("{}")

# Generated at 2022-06-13 17:51:57.743872
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\([abfnrtv\'\"\\])', '\\a')) == "\a"
    assert escape(re.match(r'\\([abfnrtv\'\"\\])', '\\b')) == "\b"
    assert escape(re.match(r'\\([abfnrtv\'\"\\])', '\\f')) == "\f"
    assert escape(re.match(r'\\([abfnrtv\'\"\\])', '\\n')) == "\n"
    assert escape(re.match(r'\\([abfnrtv\'\"\\])', '\\r')) == "\r"
    assert escape(re.match(r'\\([abfnrtv\'\"\\])', '\\t')) == "\t"

# Generated at 2022-06-13 17:52:07.471360
# Unit test for function evalString
def test_evalString():
    assert evalString('"foo"') == 'foo'
    assert evalString("'foo'") == 'foo'
    assert evalString("'foo''bar'") == "foobar"
    assert evalString("'foo' 'bar'") == "foobar"
    assert evalString("'foo''''''bar'") == "foo''bar"
    assert evalString("'foo\\nbar'") == "foo\nbar"
    assert evalString("'foo\\x01\\nbar'") == "foo\x01\nbar"
    assert evalString("'foo\\001\\nbar'") == "foo\x01\nbar"
    assert evalString("'foo\\x0001\\nbar'") == "foo\x00\x01\nbar"
    assert evalString("'foo\\,'") == "foo\\,"

# Generated at 2022-06-13 17:52:08.043158
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:52:16.535082
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\\'")) == "'"
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\\"")) == '"'
    assert escape(re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\\v")) == "\v"

# Generated at 2022-06-13 17:52:17.879206
# Unit test for function test
def test_test():
    try:
        test()
    except UnboundLocalError:
        assert False

# Generated at 2022-06-13 17:52:21.457226
# Unit test for function escape
def test_escape():
    assert escape("\\x05") == "\x05"
    assert escape("\\01") == "\01"
    assert escape("\\ab") == "ab"
    assert escape("\\n") == "\n"


# Generated at 2022-06-13 17:52:31.413844
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

    assert escape("\\x0A") == "\n"
    assert escape("\\x0a") == "\n"
    assert escape("\\xff") == chr(255)
    assert escape("\\xFF") == chr(255)

    assert escape("\\10") == "\n"
    assert escape("\\7") == "\a"
   

# Generated at 2022-06-13 17:52:52.206952
# Unit test for function escape

# Generated at 2022-06-13 17:52:53.043035
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:03.933683
# Unit test for function escape
def test_escape():
    def check_exception(exception_class, check, *args):
        """Call check() with *args and raise an exception if it does not
        raise the expected exception_class type.
        """
        try:
            check(*args)
        except exception_class:
            return
        else:
            raise AssertionError(
                "function %s(*%s) does not raise %s" % (check.__name__, args, exception_class)
            )

    check_exception(ValueError, escape, re.match(r"\\", "\\"))
    check_exception(ValueError, escape, re.match(r"\\.", "\\a"))
    check_exception(ValueError, escape, re.match(r"\\.", "\\b"))

# Generated at 2022-06-13 17:53:04.503061
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:53:15.051073
# Unit test for function escape
def test_escape():
    import ast
    import io
    from typing import Union
    from tokenize import tokenize, untokenize, TokenInfo, NAME, OP, STRING

    def compile_escapes(s: Text) -> TokenInfo:
        readline = io.BytesIO(s.encode("utf-8")).readline
        tokgen = tokenize(readline)
        for (toktype, tokval, _, _, _) in tokgen:
            if toktype == NAME:
                return tokval
        raise AssertionError("No NAME token")

    def compile_expr(expr: Text) -> ast.Expression:
        return ast.parse(expr).body[0]

    def eval_expr(expr: Text) -> Text:
        return eval(expr)


# Generated at 2022-06-13 17:53:20.947194
# Unit test for function escape
def test_escape():
    assert escape('\b') == '\b'
    assert escape('\n') == '\n'
    assert escape('\t') == '\t'
    assert escape('a') == 'a'
    assert escape('x10') == '\x10'
    assert escape('xff') == '\xff'


# Generated at 2022-06-13 17:53:35.725870
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
    assert escape("\\x20") == " "
    assert escape("\\x20") == escape("\\x20")
    assert escape("\\x20") == escape("\\x20")
    assert escape("\\x20") == escape("\\x20")
    assert escape("\\x20") == escape("\\x20")

# Generated at 2022-06-13 17:53:46.168734
# Unit test for function escape
def test_escape():
    import pytest
    from .evalString import escape

    m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\n")
    assert escape(m) == "\n"
    m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\x1a")
    assert escape(m) == "\x1a"
    m = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", "\\777")
    assert escape(m) == "\x1f"

# Generated at 2022-06-13 17:53:47.755702
# Unit test for function evalString
def test_evalString():
    assert evalString('"\\0"') == "\0"

# Generated at 2022-06-13 17:53:58.434120
# Unit test for function escape
def test_escape():
    # For example, let's test if it correctly decodes:
    # '\N{LATIN SMALL LETTER E WITH ACUTE}' (Python 2)
    # '\N{LATIN SMALL LETTER E WITH ACUTE}' (Python 3)
    import sys
    if sys.version_info.major == 3:
        test_string = "\\N{LATIN SMALL LETTER E WITH ACUTE}"
    else:
        test_string = "\\xe9"
    assert escape(re.match(r"\\x(.{0,2})", test_string)) == u"\xe9"

# Generated at 2022-06-13 17:54:22.353641
# Unit test for function evalString
def test_evalString():

    assert evalString('""') == ""
    assert evalString("''") == ""

    assert evalString('"a"') == "a"
    assert evalString("'a'") == "a"

    assert evalString('"\\n"') == "\n"
    assert evalString("'\\n'") == "\n"
    assert evalString(r'"\n"') == "\n"
    assert evalString(r"'\n'") == "\n"

    assert evalString('"\\xff"') == "\xff"
    assert evalString('"\\377"') == "\xff"
    assert evalString('"\\x00"') == "\x00"
    assert evalString('"\\0"') == "\x00"

    assert evalString('"\\377"') == "\xff"

# Generated at 2022-06-13 17:54:24.181191
# Unit test for function escape
def test_escape():
    assert escape("\\x61") == "a"
    assert escape("\\n") == "\n"



# Generated at 2022-06-13 17:54:26.452648
# Unit test for function test
def test_test():
    try:
        test()
    except:
        assert False
    assert True


# Generated at 2022-06-13 17:54:35.017735
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\([xX][0-9a-fA-F]{2}|[0-7]{1,3})', '\\xA1')) == '\xa1'
    assert escape(re.match(r'\\([xX][0-9a-fA-F]{2}|[0-7]{1,3})', '\\xa1')) == '\xa1'
    assert escape(re.match(r'\\([xX][0-9a-fA-F]{2}|[0-7]{1,3})', '\\40')) == ' '

# Generated at 2022-06-13 17:54:44.265234
# Unit test for function escape
def test_escape():

    test_map = {
        "1\\n": r"1\n",
        "\\n": r"\n",
        "\\a": r"\a",
        "\\b": r"\b",
        "\\f": r"\f",
        "\\r": r"\r",
        "\\v": r"\v",
        "\\t": r"\t",
        "\\\\": r"\\",
        "\\'": r"\'",
        '\\"': r'\"',
        "\\x00": r"\x00",
        "\\00": r"\00",
        "\\123": r"\123",
    }


# Generated at 2022-06-13 17:54:53.995317
# Unit test for function escape
def test_escape():
    from itertools import chain
    from string import ascii_letters, printable, punctuation

    assert escape('\\a') == "\a"
    assert escape('\\b') == "\b"
    assert escape('\\f') == "\f"
    assert escape('\\n') == "\n"
    assert escape('\\r') == "\r"
    assert escape('\\t') == "\t"
    assert escape('\\v') == "\v"
    assert escape('\\"') == '"'
    assert escape("\\'") == "'"
    assert escape('\\\\') == "\\"

    assert escape('\\x61') == 'a'
    assert escape('\\xfF') == 'ÿ'

    assert escape('\\0') == "\0"
    assert escape('\\00') == "\0"
    assert escape('\\000')

# Generated at 2022-06-13 17:54:54.445937
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:55:05.780901
# Unit test for function escape
def test_escape():
    ''' Test for escape() function
    '''
    assert escape(re.match(r"\\'", r"\'")).__eq__(simple_escapes["'"])
    assert escape(re.match(r'\\"', r'\"')).__eq__(simple_escapes['"'])
    assert escape(re.match(r"\\\\", r"\\")).__eq__(simple_escapes["\\"])
    assert escape(re.match(r"\\a", r"\a")).__eq__(simple_escapes["a"])
    assert escape(re.match(r"\\b", r"\b")).__eq__(simple_escapes["b"])
    assert escape(re.match(r"\\f", r"\f")).__eq__(simple_escapes["f"])

# Generated at 2022-06-13 17:55:20.945245
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\'", r"\'")) == "'"
    assert escape(re.match(r'\\"', r'\"')) == '"'
    assert escape(re.match(r'\\a', r'\a')) == "\a"
    assert escape(re.match(r"\\b", r'\b')) == "\b"
    assert escape(re.match(r"\\f", r'\f')) == "\f"
    assert escape(re.match(r"\\n", r'\n')) == "\n"
    assert escape(re.match(r"\\r", r'\r')) == "\r"
    assert escape(re.match(r"\\t", r'\t')) == "\t"

# Generated at 2022-06-13 17:55:28.153434
# Unit test for function test
def test_test():
    # assert test() is None
    assert evalString('"\x00\x01\x02"') == "\x00\x01\x02"
    assert evalString("'\x00\x01\x02'") == "\x00\x01\x02"
    assert evalString("'a'") == "a"
    assert evalString("'ab'") == "ab"

# Generated at 2022-06-13 17:55:55.812047
# Unit test for function evalString
def test_evalString():
    assert evalString('"abcde"') == 'abcde'
    assert evalString("'abcde'") == 'abcde'
    assert evalString("'\\''") == "'"
    assert evalString('"\\""') == '"'

    assert evalString(r'"\\"') == '\\'
    assert evalString(r'"\\"') == '\\'
    assert evalString(r'"\"') == '"'
    assert evalString(r'"\a"') == '\a'
    assert evalString(r'"\b"') == '\b'
    assert evalString(r'"\f"') == '\f'
    assert evalString(r'"\n"') == '\n'
    assert evalString(r'"\r"') == '\r'

# Generated at 2022-06-13 17:56:02.984980
# Unit test for function escape
def test_escape():
    # Tests for single char escapes
    assert escape(re.match("\\a", "\\a")) == "\a"
    assert escape(re.match("\\b", "\\b")) == "\b"
    assert escape(re.match("\\f", "\\f")) == "\f"
    assert escape(re.match("\\n", "\\n")) == "\n"
    assert escape(re.match("\\r", "\\r")) == "\r"
    assert escape(re.match("\\t", "\\t")) == "\t"
    assert escape(re.match("\\v", "\\v")) == "\v"
    assert escape(re.match("\\x", "\\x")) == "\\x"
    assert escape(re.match("\\'", "\\'")) == "'"

# Generated at 2022-06-13 17:56:05.377078
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([a-zA-Z0-9])", "\\u")) == "\\u"


# Generated at 2022-06-13 17:56:06.856608
# Unit test for function escape
def test_escape():
    assert escape("\\x41") == "A"

# Generated at 2022-06-13 17:56:09.807382
# Unit test for function test
def test_test():
    import io
    from contextlib import redirect_stdout
    s = io.StringIO()
    with redirect_stdout(s):
        test()
    output = s.getvalue()
    assert not output

# Generated at 2022-06-13 17:56:13.413784
# Unit test for function escape
def test_escape():
    match = re.match(r"\\(\'|\"|\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})", r"\xA4")
    assert escape(match) == "¤"

# Generated at 2022-06-13 17:56:14.499635
# Unit test for function test
def test_test():
    """Does test() pass?"""
    assert test() is None

# Generated at 2022-06-13 17:56:23.861896
# Unit test for function evalString
def test_evalString():
    assert evalString("'\t'") == "\t", evalString("'\t'")
    assert evalString("'\\t'") == "\t", evalString("'\\t'")
    assert evalString("'\\n'") == "\n", evalString("'\\n'")
    assert evalString("'\\r'") == "\r", evalString("'\\r'")
    assert evalString("'\\b'") == "\b", evalString("'\\b'")
    assert evalString('"\t"') == "\t", evalString('"\t"')
    assert evalString('"\\t"') == "\t", evalString('"\\t"')
    assert evalString('"\\n"') == "\n", evalString('"\\n"')
    assert evalString('"\\r"') == "\r", eval

# Generated at 2022-06-13 17:56:34.801289
# Unit test for function escape
def test_escape():
    import ast
    from io import StringIO

    from typing import Optional

    from typing.re import Pattern
    from ast import AST, Expression, Module

    from typing_extensions import final
    from .errors import UnsafeExpression, UnsafeEvalException

    @final
    class UnsafeEvalAstVisitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.unsafe_expr: Optional[Expression] = None

        def visit_Expr(self, node: Expression) -> None:
            if isinstance(node.value, (ast.Dict, ast.List, ast.Tuple, ast.Set)):
                self.unsafe_expr = node.value
            elif isinstance(node.value, ast.NameConstant) and node.value.value is None:
                self.unsafe

# Generated at 2022-06-13 17:56:43.845824
# Unit test for function evalString
def test_evalString():
    assert '"' == evalString('"\\""')
    assert '"' == evalString("'\\\"'")
    assert "'" == evalString('"\\\'"')
    assert "'" == evalString("'\\''")
    assert "\\" == evalString('"\\\\"')
    assert "\\" == evalString("'\\\\'")
    assert "\b" == evalString('"\\b"')
    assert "\b" == evalString("'\\b'")
    assert "\f" == evalString('"\\f"')
    assert "\f" == evalString("'\\f'")
    assert "\v" == evalString('"\\v"')
    assert "\v" == evalString("'\\v'")
    assert "\a" == evalString('"\\a"')

# Generated at 2022-06-13 17:57:14.862086
# Unit test for function escape
def test_escape():
    # Make sure it handles octal escapes
    for c_oct in range(0o100, 0o400):
        c = chr(c_oct)
        s = "\\o%03o" % c_oct
        assert escape(s) == c

    # Make sure it handles hex escpapes
    for c_hex in range(0x100, 0x400):
        c = chr(c_hex)
        s = "\\x%02x" % c_hex
        assert escape(s) == c

    # Make sure it handles simple escapes

# Generated at 2022-06-13 17:57:24.276291
# Unit test for function escape
def test_escape():
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    assert escape("\\t") == "\t"
    assert escape("\\v") == "\v"
    assert escape("\\b") == "\b"
    assert escape("\\f") == "\f"
    assert escape("\\'") == "'"
    assert escape('\\"') == '"'
    assert escape("\\\\") == "\\"

    assert escape("\\x41") == 'A'
    assert escape("\\x") == 'x'
    assert escape("\\x4") == '4'

    # '\1' is equivalent to '\x01'
    assert escape("\\1") == "\u0001"
    assert escape("\\01") == "\u0001"
    assert escape("\\001") == "\u0001"

# Generated at 2022-06-13 17:57:24.783482
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:57:35.900420
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\"', '\\"')) == '"'
    assert escape(re.match(r'\\\'', "\\'")) == "'"
    assert escape(re.match(r'\\a', '\\a')) == "\a"
    assert escape(re.match(r'\\b', '\\b')) == "\b"
    assert escape(re.match(r'\\f', '\\f')) == "\f"
    assert escape(re.match(r'\\n', '\\n')) == "\n"
    assert escape(re.match(r'\\r', '\\r')) == "\r"
    assert escape(re.match(r'\\t', '\\t')) == "\t"

# Generated at 2022-06-13 17:57:42.455097
# Unit test for function evalString
def test_evalString():
    assert evalString("'a string'") == "a string"
    assert evalString('"a string"') == "a string"
    assert evalString("'''a string'''") == "a string"
    assert evalString('"""a string"""') == "a string"
    assert evalString(r"'a \\string'") == r"a \string"
    assert evalString(r'"a \\string"') == r"a \string"
    assert evalString(r"'''a \\string'''") == r"a \string"
    assert evalString(r'"""a \\string"""') == r"a \string"
    assert evalString(r"'\b\f\n\r\t\v\'\"\\'") == "\b\f\n\r\t\v\'\"\\"


# Generated at 2022-06-13 17:57:43.124736
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:57:53.266969
# Unit test for function evalString
def test_evalString():
    assert evalString("r'abc\\''") == "abc'"
    assert evalString(r"'abc\\\\'") == "abc\\"
    assert evalString(r"'\\\\\\\''") == "\\\\\\'"
    assert evalString(r"'\x61\x62\x63'") == "abc"
    assert evalString(r"'\61\62\63'") == "123"
    assert evalString(r"'\n\r\b\t\v\f'") == "\n\r\b\t\v\f"
    assert evalString(r"'\o123\o12'") == "S\n"

# Generated at 2022-06-13 17:58:02.477580
# Unit test for function escape
def test_escape():
    assert escape(re.match(r'\\[abfnrtv]', '\\a')) == '\a'
    assert escape(re.match(r'\\[abfnrtv]', '\\b')) == '\b'
    assert escape(re.match(r'\\[abfnrtv]', '\\f')) == '\f'
    assert escape(re.match(r'\\[abfnrtv]', '\\n')) == '\n'
    assert escape(re.match(r'\\[abfnrtv]', '\\r')) == '\r'
    assert escape(re.match(r'\\[abfnrtv]', '\\t')) == '\t'

# Generated at 2022-06-13 17:58:17.190873
# Unit test for function escape
def test_escape():
    from hypothesis import given
    from hypothesis import strategies as st

    def escape_hypothesis(s: Text) -> None:
        # s should pass the regex r"\\(\\|'|\"|[abfnrtv]|x.{0,2}|[0-7]{1,3})".
        # Note this does not include non-standard \+nnn escapes
        r = re.compile(r"(\\)(\\|'" + '"' + r"|[abfnrtv]|x.{0,2}|[0-7]{1,3})")
        m = r.match(s)
        if m:
            escape(m)


# Generated at 2022-06-13 17:58:19.420336
# Unit test for function escape
def test_escape():
    assert escape(re.match(r"\\([abfnrtv'\"\\]|x.{0,2}|[0-7]{1,3})", r"\n")) == "\n"

# Generated at 2022-06-13 17:58:44.683524
# Unit test for function escape
def test_escape():
    # check basic escapes
    assert escape(re.match("\\a", "\\a")) == "\a"
    assert escape(re.match("\\b", "\\b")) == "\b"
    assert escape(re.match("\\f", "\\f")) == "\f"
    assert escape(re.match("\\n", "\\n")) == "\n"
    assert escape(re.match("\\r", "\\r")) == "\r"
    assert escape(re.match("\\t", "\\t")) == "\t"
    assert escape(re.match("\\v", "\\v")) == "\v"
    assert escape(re.match("\\'", "\\'")) == "'"
    assert escape(re.match('\\"', '\\"')) == '"'

# Generated at 2022-06-13 17:58:47.258493
# Unit test for function escape
def test_escape():
    assert escape("\\x41") == "A"
    assert escape("\\033") == "\033"
    assert escape("\\a") == "\a"
    assert escape("\\n") == "\n"
    assert escape("\\r") == "\r"
    asser

# Generated at 2022-06-13 17:58:48.833948
# Unit test for function escape
def test_escape():
    assert escape("\\x10") == "\x10"

# Generated at 2022-06-13 17:58:49.265192
# Unit test for function escape
def test_escape():
    pass

# Generated at 2022-06-13 17:58:54.866821
# Unit test for function escape
def test_escape():
    assert escape("\a") == "\\a"
    assert escape("\b") == "\\b"
    assert escape("\f") == "\\f"
    assert escape("\n") == "\\n"
    assert escape("\r") == "\\r"
    assert escape("\t") == "\\t"
    assert escape("\v") == "\\v"
    assert escape("'") == "\\'"
    assert escape('"') == '\\"'
    assert escape("\\") == "\\\\"
    assert escape("\x00") == "\\x00"
    assert escape("\x08") == "\\x08"
    assert escape("\x0f") == "\\x0f"
    assert escape("\x10") == "\\x10"

# Generated at 2022-06-13 17:59:03.179759
# Unit test for function escape
def test_escape():
    assert escape(re.search("\\a", "")) == "\a"
    assert escape(re.search("\\b", "")) == "\b"
    assert escape(re.search("\\f", "")) == "\f"
    assert escape(re.search("\\n", "")) == "\n"
    assert escape(re.search("\\r", "")) == "\r"
    assert escape(re.search("\\t", "")) == "\t"
    assert escape(re.search("\\v", "")) == "\v"
    assert escape(re.search("\\'", "")) == "'"
    assert escape(re.search('\\"', "")) == '"'
    assert escape(re.search("\\\\", "")) == "\\"
    assert escape(re.search("\\x08", "")) == "\b"

# Generated at 2022-06-13 17:59:04.347801
# Unit test for function test
def test_test():
    test()

# Generated at 2022-06-13 17:59:10.841151
# Unit test for function escape
def test_escape():
    try:
        escape(re.match(r'\\x', ''))
        escape(re.match(r'\\1', ''))
        escape(re.match(r'\\7', ''))
        escape(re.match(r'\\8', ''))
        escape(re.match(r'\\9', ''))
    except ValueError:
        pass
    else:
        assert False, "Did not catch invalid escape sequence"

# Generated at 2022-06-13 17:59:16.896144
# Unit test for function escape
def test_escape():
    escape_test_data = [
        (r'\\"', '"'),
        (r'\\x30', '0'),
        (r"\\'", "'"),
    ]
    for s, e in escape_test_data:
        try:
            r = escape(re.match(r'\\', s))
            assert e == r
        except ValueError:
            raise ValueError("invalid octal string escape ('%s')" % s) from None



# Generated at 2022-06-13 17:59:28.393228
# Unit test for function escape
def test_escape():
    """
    Most of its behavior is tested by evalString, since escape is called
    by re.sub, with groups
    """
    assert escape(re.match(r'\\a', '\\a')) == '\a'
    assert escape(re.match(r'\\b', '\\b')) == '\b'
    assert escape(re.match(r'\\f', '\\f')) == '\f'
    assert escape(re.match(r'\\n', '\\n')) == '\n'
    assert escape(re.match(r'\\r', '\\r')) == '\r'
    assert escape(re.match(r'\\t', '\\t')) == '\t'
    assert escape(re.match(r'\\v', '\\v')) == '\v'
