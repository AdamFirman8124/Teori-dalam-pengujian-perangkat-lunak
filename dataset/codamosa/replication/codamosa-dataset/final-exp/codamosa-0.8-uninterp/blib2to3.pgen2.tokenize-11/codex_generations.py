

# Generated at 2022-06-13 18:13:22.710230
# Unit test for function tokenize_loop
def test_tokenize_loop():
    readline = iter(b"if 1: #comment\n  pass").__next__

# Generated at 2022-06-13 18:13:30.707557
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import unittest
    from unittest.mock import (
        patch,
        Mock,
    )

    class TestCase(unittest.TestCase):

        def setUp(self):
            self.mock_stream = io.StringIO("abc xyz")
            self.mock_tokeneater = Mock()

        def test_HappyPath(self):
            self.mock_stream.readline.return_value = "abc xyz"
            tokenize_loop(self.mock_stream.readline, self.mock_tokeneater)


# Generated at 2022-06-13 18:13:37.159549
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    """
    This method tests whether untokenize method of class Untokenizer
    works as intended.
    """
    untokenizer = Untokenizer()
    iterable = [(tokenize.NUMBER, '1')]
    assert untokenizer.untokenize(iterable) == "1 "

    untokenizer = Untokenizer()
    iterable = [(tokenize.NAME, 'a')]
    assert untokenizer.untokenize(iterable) == "a "

    untokenizer = Untokenizer()
    iterable = [(tokenize.NEWLINE, '')]
    assert untokenizer.untokenize(iterable) == ""

    untokenizer = Untokenizer()
    iterable = [(1, 'a'), (0, ''), (0, ''), (1, 'b'), (4, '')]
    assert unt

# Generated at 2022-06-13 18:13:48.327857
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    u = Untokenizer()
    t = [
        (tokenize.NAME, "n1"),
        (tokenize.NEWLINE, "\n"),
        (tokenize.NAME, "n2"),
        (tokenize.NEWLINE, "\n"),
        (tokenize.NAME, "n3"),
        (tokenize.NEWLINE, "\n"),
        (tokenize.NAME, "n4"),
        (tokenize.ENDMARKER, ""),
    ]
    assert u.untokenize(t) == "n1\nn2\nn3\nn4\n"
    t = [(tokenize.NAME, "n1"), (tokenize.NEWLINE, "\n")]
    assert u.untokenize(t) == "n1\n"
    assert u.untokenize([]) == ""
    u = Unt

# Generated at 2022-06-13 18:13:56.072965
# Unit test for function detect_encoding
def test_detect_encoding():
    def _readlines(*seq: str) -> Iterator[bytes]:
        for s in seq:
            yield s.encode("utf-8")

    assert detect_encoding(_readlines()) == ("utf-8", [])
    assert detect_encoding(_readlines("# coding: latin-1\n")) == (
        "iso-8859-1",
        ["# coding: latin-1\n".encode("utf-8")],
    )
    assert detect_encoding(_readlines("#!/usr/bin/python\n", "# coding: latin-1\n")) == (
        "iso-8859-1",
        ["#!/usr/bin/python\n", "# coding: latin-1\n".encode("utf-8")],
    )

# Generated at 2022-06-13 18:14:07.593844
# Unit test for function generate_tokens
def test_generate_tokens():
    def _gen_tokens(s: str) -> Iterable[TokenInfo]:
        l: List[TokenInfo] = []
        for t in generate_tokens(iter(s.splitlines()).__next__):
            l.append(t)
        return l

    assert _gen_tokens("") == [
        (0, "", (1, 0), (1, 0), ""),
        (4, "", (1, 0), (1, 0), ""),
    ]
    assert _gen_tokens("abc") == [
        (1, "abc", (1, 0), (1, 3), "abc"),
        (0, "", (1, 3), (1, 3), "abc"),
        (4, "", (1, 3), (1, 3), "abc"),
    ]


# Generated at 2022-06-13 18:14:17.197362
# Unit test for function tokenize_loop
def test_tokenize_loop(): # htest #
    import io
    s = io.StringIO("if 1:\n  pass\n")
    def readline():
        line = s.readline()
        if not line:
            raise EOFError
        return line
    toks = []
    def tokeneater(*args):
        toks.append(args)
    tokenize_loop(readline, tokeneater)

# Generated at 2022-06-13 18:14:22.269738
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield bytes("# -*- coding: iso-8859-1 -*-\n", "ascii")
        yield bytes("\n", "ascii")
        yield bytes("# vim: syntax=python\n", "ascii")

    assert detect_encoding(readline) == ("iso-8859-1", [])

    def readline():
        yield bytes("# coding=iso-8859-1\n", "ascii")

    assert detect_encoding(readline) == ("iso-8859-1", [])

    def readline():
        yield bytes("\n", "ascii")
        yield bytes("#coding=iso-8859-1\n", "ascii")
        yield bytes("\n", "ascii")

    assert detect_encoding

# Generated at 2022-06-13 18:14:33.043479
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import BytesIO
    from blib2to3.pgen2.token import tokenize as generate_tokens

    codestring = b"# -*- coding: iso-8859-1 -*-\n" + b"\xf7"

    tokens = list(generate_tokens(BytesIO(codestring).readline))
    untok = Untokenizer()
    result = untok.untokenize(tokens)
    assert result == u"# -*- coding: iso-8859-1 -*-\n\ufffd ", (result, len(result))

    codestring = b"# -*- coding: iso-8859-1 -*-\n" + b"\xf7\n"

# Generated at 2022-06-13 18:14:39.708822
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:16:33.010292
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    from tokenize import tokenize
    from token import *


# Generated at 2022-06-13 18:16:38.988268
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    u = Untokenizer()
    it = iter([(1, "a"), (2, "b"), (3, "c"), (4, "d")])
    assert list(u.compat((1, "a"), it)) == [
        (2, "b"),
        (3, "c"),
        (4, "d"),
    ]

# End of unit test for method compat of class Untokenizer



# Generated at 2022-06-13 18:16:44.132138
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    import io
    import tokenize
    from io import StringIO

# Generated at 2022-06-13 18:16:50.571416
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    untok = Untokenizer()
    iterable = [
        (1, "ab"),
        (2, "cd"),
        (3, "ef"),
        (4, "gh"),
        (5, "ij"),
        (6, "kl"),
        (7, "mn"),
        (8, "op"),
        (9, "qr"),
        (10, "st"),
    ]
    # We don't care about one whitespace
    assert untok.untokenize(iterable) == "abcd efgh ijkl mnop qrst "



# Generated at 2022-06-13 18:17:04.670367
# Unit test for function detect_encoding
def test_detect_encoding():

    def readline():
        yield b"# -*- coding: iso-latin-1 -*-"

    assert detect_encoding(readline) == ("iso-8859-1", [b"# -*- coding: iso-latin-1 -*-"])

    def readline():
        yield b"# coding: iso-latin-1"

    assert detect_encoding(readline) == ("iso-8859-1", [b"# coding: iso-latin-1"])

    def readline():
        yield b"#!/usr/bin/python3"
        yield b"# -*- coding: iso-latin-1 -*-"


# Generated at 2022-06-13 18:17:09.644275
# Unit test for function printtoken
def test_printtoken():
    try:
        printtoken("token", "value", (0,0), (0,4), "")
    except Exception:
        assert False, "printtoken() failed test"
test_printtoken()



# Generated at 2022-06-13 18:17:16.387787
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        raise NotImplementedError()

    assert detect_encoding(readline) == ("utf-8", [])
    enc, lines = detect_encoding(readline)
    assert enc == "utf-8-sig" and lines == [b"# coding=utf-8"]
    enc, lines = detect_encoding(readline)
    assert enc == "iso-8859-1" and lines == [b"# -*- coding: iso-latin-1 -*-"]



# Generated at 2022-06-13 18:17:27.589579
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import unittest

    class MockLineReader:
        def __init__(self, lines):
            self._lines = lines
            self._counter = 0

        def __call__(self):
            if self._counter < len(self._lines):
                line = self._lines[self._counter]
                self._counter += 1
                return line
            else:
                raise StopIteration

    class Test(unittest.TestCase):
        def test_no_bom(self):
            lines = [b"#!/usr/bin/env python", b"# coding=utf-8"]
            reader = MockLineReader(lines)
            self.assertEqual(detect_encoding(reader), ("utf-8", lines))


# Generated at 2022-06-13 18:17:31.431802
# Unit test for function printtoken
def test_printtoken():
    assert printtoken(
        57, "de", (1, 2), (1, 4), "this is the line"
    ) == "%d,%d-%d,%d:\t%s\t%s" % (1, 2, 1, 4, tok_name[57], repr("de"))



# Generated at 2022-06-13 18:17:42.647480
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import token
    import tokenize
    r = io.BytesIO(b"for i in range(10):\n  print(i)\n")
    readline = r.readline
    tokeneater = tokenize.detect_encoding(readline)
    tokens = []
    while True:
        try:
            token_info = next(tokeneater)
        except tokenize.TokenError:
            continue
        except StopIteration:
            break
        else:
            tokens.append(token_info)

    # Test that the tokens equal the output of tokenize.
    tokens.reverse()
    generator = tokenize.generate_tokens(readline)
    while True:
        try:
            next_token = next(generator)
        except StopIteration:
            break
       

# Generated at 2022-06-13 18:19:23.168439
# Unit test for function tokenize
def test_tokenize():
    import os
    from . import tokenize as modtokenize

    def getline(filename):
        with open(filename, "rb") as f:
            encoding = modtokenize.detect_encoding(f.readline)[0]
        if encoding is None:
            encoding = "utf-8"
        with open(filename, "r", encoding=encoding) as f:
            lines = f.readlines()

        def gen():
            for line in lines:
                yield line

        return gen


# Generated at 2022-06-13 18:19:27.220119
# Unit test for function tokenize
def test_tokenize():
    import io
    from blib2to3.pgen2.tokenize import untokenize

    r = io.StringIO("def foo(): pass\n")
    a = []
    for t in generate_tokens(r.readline):
        a.append(t)
    newcode = untokenize(a)
    print(newcode)



# Generated at 2022-06-13 18:19:32.444489
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    u = Untokenizer()
    input = [(NUMBER, '42', (1, 0), (1, 2), '42'), (NAME, 'spam', (1, 2), (1, 6), 'spam')]
    assert u.untokenize(input) == '42 spam'


# wrapper to support tokenize.detect_encoding()

# Generated at 2022-06-13 18:19:42.481045
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        for line in iter(
            [
                bytes(
                    "# -*- coding: latin-1 -*-\n",
                    "utf-8",
                )
            ]
        ):
            yield line

    assert detect_encoding(readline) == ("iso-8859-1", [readline().next()])

    def readline() -> bytes:
        for line in iter(
            [
                bytes(
                    "# encoding: blah blah blah\n",
                    "utf-8",
                )
            ]
        ):
            yield line

    try:
        detect_encoding(readline)
    except SyntaxError:
        pass
    else:
        raise AssertionError("Expected SyntaxError")


# Generated at 2022-06-13 18:19:48.520391
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline(coding: str) -> Iterator[bytes]:
        yield "# coding: %s\n" % coding
    assert detect_encoding(readline("ascii")) == ("ascii", [b"# coding: ascii\n"])
    assert detect_encoding(readline("utf-8")) == ("utf-8", [b"# coding: utf-8\n"])
    assert detect_encoding(readline("utf-8-sig")) == ("utf-8-sig", [b"# coding: utf-8-sig\n"])
    assert detect_encoding(readline("latin-1")) == ("iso-8859-1", [b"# coding: latin-1\n"])
    assert detect_encoding(readline("iso-latin-1"))

# Generated at 2022-06-13 18:19:57.911909
# Unit test for function detect_encoding
def test_detect_encoding():
    # Fake readline() generator to be tested.
    def readline():
        for line in (
            b"# -*- coding: latin-1 -*-\r\n",
            b"# -*- coding: latin-1 -*-\n\n#!/bin/sh\r\n",
            b"# -*- coding: latin-1 -*-\n\n#!/bin/sh\n",
            b"# -*- coding: latin-1 -*-\n\n#!/bin/sh\r",
        ):
            yield line
        raise StopIteration

    # check a few variants
    assert detect_encoding(readline) == ("iso-8859-1", [b"#!/bin/sh\r\n"])

    # Fake readline() generator to be tested

# Generated at 2022-06-13 18:20:04.522968
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    
    def generate_tokens(readline):
        for token in tokenize.generate_tokens(readline):
            yield token
    
    def test():
        readline = iter(['print(1)\n', 'print(2)\n']).__next__
        tokens = list(generate_tokens(readline))

# Generated at 2022-06-13 18:20:14.375579
# Unit test for function generate_tokens
def test_generate_tokens():
    # test tokenize with string
    s = '''def foo():
    try:
        1/0
    finally:
        return 42'''
    g = generate_tokens(iter(s.splitlines(1)).next)
    l = [token for token in g]
    assert len(l) == 16
    for t in l:
        if t[0] is NAME:
            assert t[1] in ("def", "foo", "try", "return")
        elif t[0] is NUMBER:
            assert t[1] in ("1", "0", "42")

    # verify assumptions about token order when tab follows space
    s = 'if 1:\n    \tprint(2)'
    g = generate_tokens(iter(s.splitlines(1)).next)
    tokens = list(g)

# Generated at 2022-06-13 18:20:15.634282
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO


# Generated at 2022-06-13 18:20:19.806234
# Unit test for function tokenize
def test_tokenize():
    import io
    r = io.StringIO(
        "if 1:\n  print(1234)"
    )  # The StringIO class works just like a file
    tokenize(r.readline)



# Generated at 2022-06-13 18:21:20.789765
# Unit test for function tokenize
def test_tokenize():
    from io import StringIO

    s = "def f(x): return 2*x"
    tokeneater = []

    def tokenize_loop(readline, tokeneater=tokeneater.append):
        for token in generate_tokens(readline):
            tokeneater.append(token)

    tokenize(StringIO(s).readline)

# Generated at 2022-06-13 18:21:29.608347
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline(x=0):
        return (
            b"# -*- coding: iso-8859-1 -*-\n",
            b"\xef\xbb\xbf\n",
            b"\xef\xbb\xbf# coding: cp1252\n",
            b"\xef\xbb\xbf# -*- coding: cp1252 -*-\n",
            b"\xef\xbb\xbf\n",
            b"\n",
        )[x]

    def test(x):
        encoding, lines = detect_encoding(readline)
        print(encoding, lines)

    test(0)
    test(1)
    test(2)
    test(3)
    test(4)
    test(5)

    #

# Generated at 2022-06-13 18:21:39.175812
# Unit test for function detect_encoding
def test_detect_encoding():
    import io

    def readlines(s, as_list=False):
        if as_list:
            return [s]
        return io.BytesIO(s).readline

    def check(s, expected_encoding, expected_return):
        if expected_return is None:
            try:
                detect_encoding(readlines(s))
            except SyntaxError:
                pass
            else:
                raise Exception("SyntaxError should be raised")
        else:
            encoding, lines = detect_encoding(readlines(s))
            if encoding != expected_encoding:
                raise Exception(
                    "encoding should be %s, got %s" % (expected_encoding, encoding)
                )

# Generated at 2022-06-13 18:21:45.717064
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from collections import namedtuple
    from io import StringIO
    from tokenize import generate_tokens, untokenize

    Token = namedtuple('Token', 'type string start end line')

    class DummyToken(object):
        def __init__(self, type):
            self.type = type

        def __getitem__(self, type):
            if type == 0:
                return self.type
            elif type == 1 or type == 2 or type == 3:
                return (0, 0)
            elif type == 4:
                return ''
            else:
                raise IndexError

    # Test case:
    # abcdefghi
    #    ^ tab
    #  ^ space

# Generated at 2022-06-13 18:21:57.164859
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    from tokenize import generate_tokens, tok_name

    readline = StringIO(
        '''if 1:
    print('foo')
'''
    ).readline

    for tok in generate_tokens(readline):
        print(tok_name[tok[0]], tok[1])
"""
INDENT
if
NUMBER
:
NEWLINE
INDENT
NAME
print
OP
(
STRING
'foo'
OP
)
NEWLINE
DEDENT
DEDENT
"""
# End of unit test



# Generated at 2022-06-13 18:22:04.991386
# Unit test for function tokenize
def test_tokenize():
    import io
    from io import StringIO
    from tokenize import tokenize as tokenize_stdlib

    s = io.StringIO("a = [1, 2, 3]")
    tokens = [x[1] for x in tokenize_stdlib(s.readline)]
    tokenize(s.readline)
    s = io.StringIO("a = [1, 2, 3]")
    tokens = [x[1] for x in tokenize_stdlib(s.readline)]
    tokenize(s.readline)
    tokenize(s.readline)



# Generated at 2022-06-13 18:22:15.563125
# Unit test for function detect_encoding
def test_detect_encoding():
    def get_readline(lines: List[str]) -> Callable[[], Text]:
        def readline() -> Text:
            return lines.pop(0)

        return readline

    assert detect_encoding(get_readline(["# coding: UTF-8\n"])) == ("utf-8", ["# coding: UTF-8\n"])
    assert detect_encoding(get_readline(["# coding=UTF-8\n"])) == (
        "utf-8",
        ["# coding=UTF-8\n"],
    )
    assert detect_encoding(get_readline(["# coding = UTF-8\n"])) == (
        "utf-8",
        ["# coding = UTF-8\n"],
    )

# Generated at 2022-06-13 18:22:24.145913
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import tokenize

    def readline():
        yield io.BytesIO(b"# coding: latin-1\nf\xfatste=2").readline()

    assert detect_encoding(readline) == ("iso-8859-1", [b"# coding: latin-1\n"])

    def readline():
        yield io.BytesIO(b"#!/usr/bin/python\n# coding: latin-1\nf\xfatste=2").readline()

    assert detect_encoding(readline) == ("iso-8859-1", [b"#!/usr/bin/python\n"])

