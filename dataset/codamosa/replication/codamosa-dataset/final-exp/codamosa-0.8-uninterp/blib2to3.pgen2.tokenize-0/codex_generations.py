

# Generated at 2022-06-13 18:14:07.181944
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from . import token
    from .tokenize import NAME, NUMBER
    ut = Untokenizer()
    s = ut.untokenize(
        [
            (NAME, "func"),
            (token.OP, "("),
            (NAME, "arg"),
            (token.OP, ")"),
            (token.NEWLINE, "\n"),
        ]
    )
    assert s == "func(arg)\n"



# Generated at 2022-06-13 18:14:16.826690
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    r = io.StringIO("def foo(arg): pass\n")
    # Feed the file text into generate_tokens;
    # it'll get buffered by readline if necessary.
    g = tokenize.generate_tokens(r.readline)
    try:
        for toknum, tokval, _, _, _ in g:
            print("%d %-14s %s" % (toknum, tokenize.tok_name[toknum], repr(tokval)))
    except tokenize.TokenError as ex:
        print(ex)


if __name__ == "__main__":
    test_generate_tokens()


# Standard library
import string
import sys
import tokenize


# Generated at 2022-06-13 18:14:22.162549
# Unit test for function detect_encoding
def test_detect_encoding():
    # Whitespace only
    assert detect_encoding(iter([b' \t\f\n\r']).__next__) == ('utf-8', [b' \t\f\n\r'])
    assert detect_encoding(iter([b' \t\f\n\r', b' \t\f\n\r']).__next__) == ('utf-8', [b' \t\f\n\r', b' \t\f\n\r'])
    # Whitespace and comment
    assert detect_encoding(iter([b' \t\f\n\r#']).__next__) == ('utf-8', [b' \t\f\n\r#'])

# Generated at 2022-06-13 18:14:33.080114
# Unit test for function generate_tokens
def test_generate_tokens():
    import re

    my_string = """
    "This is a test", said Fred.
    'So is this.'
    # And this is a comment.
    '''This, too, is a test.
    '''
    "Next comes a blank line."

    '''
    Now a blank line, with comments.
    # This is the last line.
    '''

    # The following line is indented.
        # It should generate an INDENT token.
    """
    my_string = re.sub("\s+#.*$", "", my_string, flags=re.MULTILINE)
    my_string = re.sub("\s+'{3}", " '''", my_string, flags=re.MULTILINE)

# Generated at 2022-06-13 18:14:40.300522
# Unit test for function tokenize
def test_tokenize():
    import io
    import token as tokenizer
    import blib2to3.pgen2.token as tok

    # Test multiple tokens
    toks = tokenize(io.BytesIO(b"from unittest import *").readline)
    assert next(toks) == (tok.NAME, "from", (0, 0), (0, 4), b"from unittest import *")
    assert next(toks) == (
        tok.NAME,
        "unittest",
        (0, 5),
        (0, 13),
        b"from unittest import *",
    )
    assert next(toks) == (
        tok.NAME,
        "import",
        (0, 14),
        (0, 20),
        b"from unittest import *",
    )
   

# Generated at 2022-06-13 18:14:45.826144
# Unit test for function generate_tokens
def test_generate_tokens():
    import tokenize

    def rl(s):
        return list(tokenize.tokenize(io.BytesIO(s.encode("utf-8")).readline))

    s = "def f():\n '''\n foo \n '''\n return 3\n"
    t = rl(s)

    for token in generate_tokens(io.BytesIO(s.encode("utf-8")).readline):
        assert token[:2] == next(t)[:2]

    s = "def g():\n if True:\n  print('foo')\n else:\n  return\n"
    t = rl(s)

# Generated at 2022-06-13 18:14:57.152479
# Unit test for function tokenize
def test_tokenize():
    import io
    import token
    # Test with BytesIO
    input_stream = io.BytesIO(b'test data')
    tokens = []
    for tok in generate_tokens(input_stream.readline):
        tokens.append(tok)
    assert tokens == [
        (token.ENCODING, 'utf-8', (1, 0), (1, 0), 'utf-8'),
        (token.NAME, 'test', (1, 0), (1, 4), 'test data'),
        (token.NAME, 'data', (1, 5), (1, 9), 'test data'),
        (token.ENDMARKER, '', (2, 0), (2, 0), ''),
    ]
    # Test with StringIO
    input_stream = io.StringIO('test data')

# Generated at 2022-06-13 18:15:04.191626
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    untokenize = Untokenizer().compat

# Generated at 2022-06-13 18:15:11.608341
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import unittest

    # Complete, valid input
    inputstr = (
        "def function(x):\n"
        '    return "result is " + repr(x)\n'
        '\n'
        "print(function(23))\n"
    )

# Generated at 2022-06-13 18:15:14.067239
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import StringIO
    s = StringIO.StringIO("ROT13 = 'trnlf'\n")
    print(tokenize_loop(s.readline, printtoken))


# Generated at 2022-06-13 18:15:43.847859
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    from io import StringIO
    import sys
    import unittest

    class TestTokenize(unittest.TestCase):
        # use the same examples for all tests (see issue #14946)
        code = "\n".join(
            [
                "def f():",
                "    '''abc'''",
                "    print(42)",
                '    x = "abc"',
                "",
                "# def g(): pass",
                "# ",
                "#",
                "#",
            ]
        )
        filename = "<test>"

        def test_tokenize(self):
            with tokenize.open(self.filename) as f:
                result = list(tokenize.generate_tokens(f.readline))
            self.assertEqual(result, self.expected)


# Generated at 2022-06-13 18:15:54.595540
# Unit test for function tokenize
def test_tokenize():
    from . import tokenize as tok

    def testit(s, expected):
        result = []
        tok.tokenize(s.splitlines(1), result.append)
        assert result == expected, (result, expected)

    testit("", [])
    testit("\n#\n", [("NL", "\n", (1, 0), (1, 1), "\n"), ("COMMENT", "#\n", (2, 0), (2, 2), "#\n")])
    testit("a = 0\n", [("NAME", "a", (1, 0), (1, 1), "a = 0\n"), ("OP", "=", (1, 2), (1, 3), "= 0\n"), ("NUMBER", "0", (1, 4), (1, 5), "0\n")])



# Generated at 2022-06-13 18:16:03.883177
# Unit test for function detect_encoding
def test_detect_encoding():
    # No encoding
    eq = (lambda s: s.encode("ascii"))
    for line in [
        b"",
        b"\n",
        b"\n\n\n",
        b" \n",
        b" \n\t\n",
        b"#\n",
        b"# \n",
        b"# \n\t\n",
    ]:
        eq(detect_encoding(iter([line]).__next__)[0]), "utf-8"

# Generated at 2022-06-13 18:16:16.785136
# Unit test for function tokenize
def test_tokenize():
    s = "(this (is a) test\n (of tokenize.generate_tokens))"

# Generated at 2022-06-13 18:16:25.740173
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
    """
    Test method add_whitespace for class Untokenizer.
    """
    un = Untokenizer()
    un.prev_col = 2
    un.tokens = ["bla"]
    start = (1, 2)
    un.add_whitespace(start)
    assert un.tokens == ["bla"]
    start = (1, 3)
    un.add_whitespace(start)
    assert un.tokens == ["bla ", ""]
    start = (1, 6)
    un.add_whitespace(start)
    assert un.tokens == ["bla ", "   "]
    start = (1, 6)
    un.add_whitespace(start)
    assert un.tokens == ["bla ", "   "]

# Generated at 2022-06-13 18:16:35.394735
# Unit test for function detect_encoding
def test_detect_encoding():
    import unittest

    class Test(unittest.TestCase):
        def test(self):

            def readlines(iterable):
                for line in iterable:
                    yield bytes(line, "utf-8")

            eq = self.assertEqual
            eq(
                detect_encoding(readlines(iter(["# coding: latin-1\n".splitlines()])).__next__),
                ("iso-8859-1", [b"# coding: latin-1\n"]),
            )
            eq(
                detect_encoding(readlines(iter(['# coding=utf-8\n'.splitlines()]))).__next__,
                ("utf-8", [b"# coding=utf-8\n"]),
            )

# Generated at 2022-06-13 18:16:46.922731
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    def compare(test, want):
        tuple(compare_untokenize(test, want))

    def compare_untokenize(test, want):
        u = Untokenizer()
        res = u.untokenize(tokenize_loop(iter(test.splitlines(True)).__next__, None))
        if res != want:
            raise ValueError(
                "untokenize() returned %a but expected %a" % (res, want)
            )

    def compare_roundtrip(start):
        compare(start, start)

    compare_roundtrip("")
    compare_roundtrip("a")
    compare_roundtrip("a = 1")
    compare_roundtrip("a  =  1")
    compare_roundtrip('a = """multiline\nstring\n"""')

# Generated at 2022-06-13 18:16:53.316614
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from blib2to3.pgen2.token import tok_name

    def tokens(s: Text) -> Iterable[TokenInfo]:
        for toknum, tokval, _, _, _ in generate_tokens(iter(s.splitlines(True)).__next__):
            yield TokenInfo(toknum, tokval)

    u = Untokenizer()
    s = """def f(x):\n  return x+1\n"""
    res = u.untokenize(tokens(s))
    assert res == s, "untokenize() fails to reproduce original source (%r != %r)" % (
        res,
        s,
    )



# Generated at 2022-06-13 18:17:00.219583
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from .tokenize import Untokenizer

    def get_tokenizer():
        def false_tokenizer():
            yield (OP, ".")
        return false_tokenizer

    untok = Untokenizer()
    with pytest.raises(TypeError):
        untok.untokenize(get_tokenizer())

untokenize = Untokenizer().untokenize



# Generated at 2022-06-13 18:17:08.193144
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    untok = Untokenizer()
    first_token = [
        (NAME, 'foo', (1, 0), (1, 3), "foo"),
        (NAME, 'bar', (1, 3), (1, 6), "bar"),
        (OP, '+', (1, 6), (1, 7), "+"),
        (NAME, 'baz', (1, 7), (1, 10), "baz"),
        (NAME, 'blah', (2, 0), (2, 4), "blah"),
        (NEWLINE, '', (2, 4), (2, 4), "\n")
    ]
    assert untok.untokenize(first_token) == 'foo bar + baz\nblah\n'

# Generated at 2022-06-13 18:17:45.364404
# Unit test for function generate_tokens
def test_generate_tokens():
    import tokenize
    import io
    import token
    import codecs
    readline = (
        u"# -*- coding: latin-1 -*-\n"
        + u"from __future__ import division, unicode_literals, print_function\n"
    ).splitlines(False)
    with io.StringIO() as stream:
        tokengen = tokenize.generate_tokens(readline.next)

# Generated at 2022-06-13 18:17:51.982372
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# coding=utf-8"
    assert detect_encoding(readline) == ("utf-8", [b"# coding=utf-8"])

    def readline():
        yield b"#!/usr/bin/env python3\n"
        yield b"# coding=utf-8"
    assert detect_encoding(readline) == ("utf-8", [b"#!/usr/bin/env python3\n",
                                                   b"# coding=utf-8"])

    def readline():
        yield b"# coding: utf-8\n"
        yield b"pass"
    assert detect_encoding(readline) == ("utf-8", [b"# coding: utf-8\n", b"pass"])

    def readline():
        yield b

# Generated at 2022-06-13 18:17:57.635941
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from .tokenize import untokenize

    s = '"abc"; x = 3'
    result = []
    tokenize_loop(s.splitlines().__iter__().__next__, result.append)
    assert untokenize(result) == s

    s = "'abc'; x = 3"
    result = []
    tokenize_loop(s.splitlines().__iter__().__next__, result.append)
    assert untokenize(result) == s



# Generated at 2022-06-13 18:18:08.145792
# Unit test for function tokenize
def test_tokenize():
    import io
    import tokenize as _tokenize  # in 3.x, repr(token) is wrong

    def badsyntax(a, b, c, d, e):
        raise RuntimeError("I don't like {}".format(b))

    print(
        "TEXT:\n",
        "\n".join(
            '%d:\t%r' % (i + 1, line)
            for i, line in enumerate(open(__file__).readlines())
        ),
    )

    print(
        "\nINTERNAL REPR:\n",
        "\n".join(
            "#%d:\t%r" % (i, t)
            for i, t in enumerate(_tokenize.generate_tokens(open(__file__).readline))
        ),
    )


# Generated at 2022-06-13 18:18:09.665616
# Unit test for function tokenize_loop
def test_tokenize_loop():
    assert tokenize_loop(iter(["pass"]).__next__, None) is None



# Generated at 2022-06-13 18:18:13.219012
# Unit test for function tokenize
def test_tokenize():
    import io

    s = "def test(): pass"
    g = generate_tokens(io.StringIO(s).readline)
    for token in g:
        printtoken(*token)



# Generated at 2022-06-13 18:18:18.417549
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    import tokenize
    r = StringIO("if 1:\n  print(2)\n")
    res = []
    for x in tokenize.generate_tokens(r.readline):
        res.append(x)
    res

# Generated at 2022-06-13 18:18:30.698642
# Unit test for function generate_tokens
def test_generate_tokens():
    def generate_tokens(str):
        """
        Reads from a string, returning a sequence of token iterms as
        described in the `tokenize()` docstring.
        """
        l = Lexer()
        l.input(str)
        while True:
            tok = l.token()
            if not tok:
                break
            yield tok

    def gettoken(str):
        """
        Returns (type, token) tuple
        """
        for token in generate_tokens(str):
            return (token.type, token.value)

    # Test of ID Token
    assert gettoken("100") == ("NUMBER", "100")
    assert gettoken("100.5") == ("NUMBER", "100.5")
    assert gettoken("abc") == ("NAME", "abc")
    assert get

# Generated at 2022-06-13 18:18:47.747197
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO


# Generated at 2022-06-13 18:18:53.675699
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    utok = Untokenizer()
    # This example from PEP 0263
    result = utok.untokenize(
        (
            (NAME, "print"),
            (OP, "("),
            (STRING, '"Hello World"'),
            (OP, ")"),
            (NEWLINE, "\n"),
        )
    )
    assert result == "print('Hello World')\n"



# Generated at 2022-06-13 18:20:22.909370
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    source = "def f(x, y):\n    return x + y + z\n"
    expected_result = "def f ( x , y ) :\n    return x + y + z\n"
    tokens = list(tokenize(BytesIO(source.encode("utf-8")).readline))

    # Skip the encoding token if it's present
    if tokens[0][0] == token.ENCODING:
        del tokens[0]

    result = Untokenizer().untokenize(tokens)
    assert result == expected_result, (
        "Unexpected result.\n" "Expected:\n" + expected_result + "\nGot:\n" + result
    )



# Generated at 2022-06-13 18:20:31.650699
# Unit test for function generate_tokens
def test_generate_tokens():
    def test(s):
        # Testing generator version
        all = list(generate_tokens(StringIO(s).readline))
        for i in range(len(all)-1):
            a, b = all[i], all[i+1]

# Generated at 2022-06-13 18:20:43.584441
# Unit test for function generate_tokens
def test_generate_tokens():
    readline = iter(['if 1: #comment\n', '  print(1)\n']).__next__
    result = [x for x in generate_tokens(readline)]

# Generated at 2022-06-13 18:20:46.616611
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    u = Untokenizer()
    assert (
        u.untokenize([(STRING, "'abc'"), (OP, ';'), (NEWLINE, "\n")])
        == "    'abc';\n"
    )



# Generated at 2022-06-13 18:20:54.479956
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def _readline(s):
        for c in s:
            yield c
        yield ""
    tokeneater = lambda s: setattr(_test, "ONE", s)
    _test = type("", (object,), {"ONE": None})()
    tokenize_loop(_readline("1"), tokeneater)
    assert _test.ONE == (
        1,
        "1",
        (1, 0),
        (1, 1),
        "1",
    )
test_tokenize_loop()


ENCODING = "utf-8"



# Generated at 2022-06-13 18:21:08.005397
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def _readline():
        if _readline.i == 0:
            _readline.i = 1
            return "def foo():"
        elif _readline.i == 1:
            _readline.i = 2
            return "    pass"
        else:
            raise ValueError("I don't wanna")

    _readline.i = 0

    def _tokeneater(type, token, start, end, line):
        assert (
            (type, token, start, end, line)
            == (57, "def", (1, 0), (1, 3), "def foo():")
            or (type, token, start, end, line)
            == (4, "    ", (2, 0), (2, 4), "    pass")
        )


# Generated at 2022-06-13 18:21:20.702869
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield None
        yield "abc"
        raise StopIteration

    def readline_with_bom():
        yield bytes(BOM_UTF8)
        yield None
        yield "abc"
        raise StopIteration

    def readline_with_cookie():
        yield "# -*- coding: ascii -*-"
        yield None
        yield "abc"
        raise StopIteration

    def readline_with_both():
        yield bytes(BOM_UTF8)
        yield "# -*- coding: latin-1 -*-"
        yield None
        yield "abc"
        raise StopIteration

    def readline_with_both_and_blank_line():
        yield bytes(BOM_UTF8)
        yield None

# Generated at 2022-06-13 18:21:29.536536
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    untok = Untokenizer()
    try:
        import StringIO
    except ImportError:
        import io as StringIO

    data = "a = 1+2\nprint(a)\n"
    f = StringIO.StringIO(data)
    tokenize(f.readline, untok.untokenize)
    assert untok.tokens == data.split()
    data = "a = 1+2\n\nprint(a)\n"
    f = StringIO.StringIO(data)
    untok = Untokenizer()
    tokenize(f.readline, untok.untokenize)
    assert untok.tokens == data.split()
    data = "a = 1+2\nprint(a)\n\n"
    f = StringIO.StringIO(data)
    tokenize

# Generated at 2022-06-13 18:21:39.108179
# Unit test for function detect_encoding
def test_detect_encoding():
    try:
        import blib2to3.pgen2.tokenize
    except ImportError:
        blib2to3.pgen2.tokenize = __import__("tokenize")
    source = b"# -*- coding: latin-1 -*-\n"
    readline = iter([source]).__next__
    assert blib2to3.pgen2.tokenize.detect_encoding(readline) == ("iso-8859-1", [source])

    readline = iter([source[:5], source[5:]]).__next__
    assert blib2to3.pgen2.tokenize.detect_encoding(readline) == ("iso-8859-1", [source])

    source = b"# coding=latin-1\n"

# Generated at 2022-06-13 18:21:47.120264
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        if not readline.lines:
            raise StopIteration
        return readline.lines.pop(0)
    readline.lines = []
    readline.lines.append(b"# -*- coding: iso-8859-1 -*-\n")
    assert detect_encoding(readline) == ("iso-8859-1", [])
    readline.lines.append(BOM_UTF8)
    readline.lines.append(b"# coding: utf-8\n")
    assert detect_encoding(readline) == ("utf-8-sig", [])
    readline.lines.append(BOM_UTF8)
    readline.lines.append(b"# coding: latin-1\n")