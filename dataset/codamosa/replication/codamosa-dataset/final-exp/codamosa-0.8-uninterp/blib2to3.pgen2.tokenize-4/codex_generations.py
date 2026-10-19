

# Generated at 2022-06-13 18:14:35.870269
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for line in [
            b"# -*- coding: latin-1 -*-\n",
            b"\n",
            b"#!/bin/env python\n",
            b"# -*- coding: iso-latin-1 -*-\n",
            b"\n",
        ]:
            yield line
        raise StopIteration()


# Generated at 2022-06-13 18:14:40.750398
# Unit test for function tokenize_loop
def test_tokenize_loop():
    s = "def f(x):\n    return x**2\n"
    g = generate_tokens(s.splitlines().__next__)
    l = list(g)
    tokenize_loop(s.splitlines().__next__, l.append)
    assert l == list(g)
    #
    def getline(cnt=[0]):
        cnt[0] += 1
        if cnt[0] == 4:
            return ""
        return "  \t x  =   0"
    def eat(*args):
        print(args)
    tokenize_loop(getline, eat)



# Generated at 2022-06-13 18:14:48.974766
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield bytes("\xef\xbb\xbf\n", "utf-8")
        yield bytes("# -*- coding: iso-8859-1 -*-\n", "iso-8859-1")
        yield bytes("# vim: set fileencoding=latin-1 :\n", "iso-8859-1")
        yield bytes("import os, sys\n", "iso-8859-1")
        raise StopIteration

    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"
    line = "".join(line.decode() for line in lines)
    assert line == "# -*- coding: iso-8859-1 -*-\n"


# Generated at 2022-06-13 18:14:53.755127
# Unit test for function generate_tokens
def test_generate_tokens():

    s = "# This is a comment\nclass foo:\n    pass"
    tokens = list(tokenize(BytesIO(s.encode("utf-8")).readline))
    assert tokens == [
        (NAME, "class"),
        (NAME, "foo"),
        (OP, ":"),
        (NEWLINE, "\n"),
        (INDENT, "    "),
        (NAME, "pass"),
        (DEDENT, ""),
        (ENDMARKER, ""),
    ]



# Generated at 2022-06-13 18:15:01.714860
# Unit test for function generate_tokens
def test_generate_tokens():
    import string
    import tokenize
    from io import StringIO


# Generated at 2022-06-13 18:15:11.834736
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def readline():
        yield 'def f(x):'
        yield '    return x**2'
    tokens = []
    tokenize_loop(readline, tokens.append)

# Generated at 2022-06-13 18:15:20.334504
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:15:30.073097
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import unittest
    import io

    class TestCase(unittest.TestCase):

        def test_simple(self):
            with io.StringIO("abc\nabc") as text:
                l = []
                tokenize_loop(text.readline, l.append)
                self.assertEqual(
                    l,
                    [
                        (token.NAME, "abc", (1, 0), (1, 3), "abc"),
                        (token.NEWLINE, "\n", (1, 3), (1, 4), "abc"),
                        (token.NAME, "abc", (2, 0), (2, 3), "abc"),
                        (token.ENDMARKER, "", (2, 3), (2, 3), "abc"),
                    ],
                )

    unittest.main()



# Generated at 2022-06-13 18:15:41.410486
# Unit test for function tokenize
def test_tokenize():
    import re
    import io
    from _tokenize import generate_tokens, untokenize, NUMBER, STRING, NAME

    def _format(tokens):
        # Format tokens into pseudo-Python source
        result = []
        indent = 0
        for token in tokens:
            tok_type, tok_string, begin, end, line = token
            if tok_type == tokenize.INDENT:
                indent += 1
            elif tok_type == tokenize.DEDENT:
                indent -= 1
            elif tok_type == tokenize.NEWLINE:
                pass
            elif tok_type == tokenize.ENCODING:
                result.append(tok_string)
            elif tok_string in (" ", "\t"):
                continue
            else:
                result.append

# Generated at 2022-06-13 18:15:52.791754
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import sys
    import tokenize


# Generated at 2022-06-13 18:16:47.482600
# Unit test for function tokenize_loop
def test_tokenize_loop():
    readline = iter(iterable).__next__
    tokeneater = lst.append
    tokenize_loop(readline, tokeneater)



# Generated at 2022-06-13 18:17:02.472527
# Unit test for function generate_tokens
def test_generate_tokens():
    def _tokens(s):
        return list(generate_tokens(io.StringIO(s).readline))
    assert _tokens('') == [(ENDMARKER, '', (1, 0), (1, 0), '')]
    assert _tokens('x = 1') == [
        (NAME, 'x', (1, 0), (1, 1), 'x = 1'),
        (OP, '=', (1, 2), (1, 3), 'x = 1'),
        (NUMBER, '1', (1, 4), (1, 5), 'x = 1'),
        (NEWLINE, '', (1, 5), (1, 5), 'x = 1'),
        (ENDMARKER, '', (1, 5), (1, 5), 'x = 1'),
    ]
   

# Generated at 2022-06-13 18:17:12.355279
# Unit test for function detect_encoding
def test_detect_encoding():
    from io import BytesIO

    def tokenize_by_lines(readline):
        while True:
            line = readline()
            if not line:
                break
            yield line

    def make_readline(s):
        def readline():
            return s.pop(0)

        return readline

    def assert_encoding(
        encoded: Union[str, bytes], result: str,
    ) -> None:
        if isinstance(encoded, bytes):
            encoded = encoded.decode()
        s = encoded.splitlines()
        assert detect_encoding(make_readline(s.copy())) == (result, s.copy())
        assert (
            detect_encoding(make_readline(s.copy()), None) == (result, s.copy())
        )

# Generated at 2022-06-13 18:17:19.736337
# Unit test for function tokenize
def test_tokenize():
    import io
    import token as tokenize

    def tokeneater(type, token, start, end, line):
        print("%s %s %s %s %s" % (tokenize.tok_name[type], repr(token), start, end, repr(line)))

    tokenize.tokenize(io.BytesIO(b"def f(x): return x+1;\n").readline, tokeneater)

    # Test line numbers
    io_obj = io.BytesIO(b"# comment\n\n\n\n# another comment\n")
    tokenize.tokenize(io_obj.readline, tokeneater)

    # Test 'string line continuation'
    io_obj = io.BytesIO(b"'''first \\\nsecond line\nthird'''")

# Generated at 2022-06-13 18:17:21.968050
# Unit test for function tokenize_loop
def test_tokenize_loop():
    with open('test_tokenize_loop.py') as f:
        tokenize_loop(f.readline, printtoken)


# Generated at 2022-06-13 18:17:32.345913
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import unittest
    import blib2to3.pgen2.tokenize as tokenize2
    import io

    class RoundtripTest(unittest.TestCase):
        def setUp(self):
            tokenize2.tokenize_loop(
                io.StringIO(self.data).readline, self.tokeneater
            )

        def tokeneater(self, type, token, start, end, line):
            self.tokens.append((type, token, start, end, line))

    class WhitespaceTest(RoundtripTest):
        data = "hello\nworld\n"

        def setUp(self):
            self.tokens = []
            RoundtripTest.setUp(self)


# Generated at 2022-06-13 18:17:43.664163
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import token

    def token_test(testcase):
        r = io.StringIO(testcase)
        result = list(generate_tokens(r.readline))
        r.close()
        return result

    # Test case 1
    t1 = "def f(x): return 2*x"
    r1 = token_test(t1)
    assert len(r1) == 11
    assert r1[0] == (token.NAME, "def", (1, 0), (1, 3), "def f(x): return 2*x")
    assert r1[1] == (token.NAME, "f", (1, 4), (1, 5), "def f(x): return 2*x")

# Generated at 2022-06-13 18:17:55.485800
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import tokenize as tokenize_m

    def tokenize(encoding, string):
        assert detect_encoding(io.BytesIO(string).readline)[0] == encoding

    tokenize("latin-1", b"# -*- coding: latin-1 -*-\n")
    tokenize("latin-1", b"# -*- coding: iso-latin-1 -*-\n")
    tokenize("iso-8859-1", b"# -*- coding: iso-8859-1 -*-\n")
    tokenize("iso-8859-15", b"# -*- coding: iso-8859-15 -*-\n")
    tokenize("ascii", b"# -*- coding: ascii -*-\n")

# Generated at 2022-06-13 18:18:06.341391
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from test.support import captured_stdout
    import io
    from . import tokenize
    from . import untokenize
    from . import token
    from . import tokenize
    from . import untokenize
    from blib2to3.pgen2.tokenize import _UNSET

    sample = io.StringIO("if 1:\n  pass\n")
    u = untokenize.Untokenizer()
    with captured_stdout() as stdout:
        tokenize.tokenize(sample.readline, u.compat)
        pass
    stdout.seek(0)
    expected = "if 1: pass\n"
    assert stdout.read() == expected
    pass


# Generated at 2022-06-13 18:18:08.541818
# Unit test for function printtoken
def test_printtoken():
    i = printtoken(NAME, "a", (0, 0), (0, 2), "a = 0")
    assert i == None

# Testing functions

# Generated at 2022-06-13 18:19:41.511620
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from test.test_tokenize import tokenize_loop_helper
    tokenize_loop_helper(tokenize_loop)



# Generated at 2022-06-13 18:19:51.485816
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import tokenize

    def readline():
        if not lines:
            raise StopIteration
        line = lines.pop(0)
        if isinstance(line, str):
            line = line.encode("utf-8")
        return line

    # Verify detection of first two lines
    for first in ("", "# -*- coding: latin-1 -*-", "# vim:fileencoding=utf-8"):
        for second in ("", "# blah blah blah", ""):
            lines = [first, second]
            assert tokenize.detect_encoding(readline) == ("utf-8-sig", lines)
            assert not lines, lines

    # Verify detection with just the second line present

# Generated at 2022-06-13 18:20:00.172774
# Unit test for function generate_tokens
def test_generate_tokens():
    import token
    import tokenize
    from io import BytesIO
    readline = BytesIO(b"if 1:\n    2\n").readline
    result = list(tokenize.generate_tokens(readline))
    assert result[0] == (token.NAME, b'if', (1, 0), (1, 2), b'if 1:\n')
    assert result[1] == (token.NUMBER, b'1', (1, 3), (1, 4), b'if 1:\n')
    assert result[2] == (token.OP, b':', (1, 4), (1, 5), b'if 1:\n')
    assert result[3] == (token.NEWLINE, b'\n', (1, 5), (2, 0), b'if 1:\n')
    assert result

# Generated at 2022-06-13 18:20:02.314500
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import tokenize
    s = io.StringIO('print(42)\n')
    tokenize.tokenize_loop(s.readline, None)



# Generated at 2022-06-13 18:20:11.818820
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# coding: latin-1\n"
        yield b"# a two-line comment\n"
        yield b"import blah blah blah\n"
    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"
    assert b"".join(lines) == b"# coding: latin-1\n# a two-line comment\nimport blah blah blah\n"
    def readline():
        yield b"# coding=utf-8\n"
        yield b"# a two-line comment\n"
        yield b"import blah blah blah\n"
    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"

# Generated at 2022-06-13 18:20:26.417890
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import sys

    def readline():
        return next(input)

    def _test(input, expected_encoding, *expected_lines):
        input = iter(input)
        encoding, lines = detect_encoding(readline)
        assert encoding == expected_encoding
        assert lines == list(expected_lines)

    # no encoding declaration
    _test(["#!/usr/bin/env python3\n"], "utf-8", b"#!/usr/bin/env python3\n")
    # valid utf-8 with BOM
    _test([BOM_UTF8 + b"#!/usr/bin/env python3\n"], "utf-8-sig", b"#!/usr/bin/env python3\n")
    # valid utf-8, no BOM

# Generated at 2022-06-13 18:20:29.683137
# Unit test for function printtoken
def test_printtoken():
    printtoken(STRING, "abc", (0, 0), (0, 0), "")

# Based loosely on the tokenize() extension written by Ka-Ping Yee


# Generated at 2022-06-13 18:20:36.588071
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
    u = Untokenizer()
    u.prev_row = 4
    u.prev_col = 32
    u.add_whitespace((4, 38))
    assert u.tokens == [' ' * 6]
    u.prev_col = 0
    u.add_whitespace((4, 0))
    assert u.tokens == [' ' * 6, '\n']



# Generated at 2022-06-13 18:20:46.605759
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def test_generate_tokens(st):
        result = list(generate_tokens(lambda: st))
        assert result == [
            (NAME, "x", (1, 0), (1, 1), "x"),
            (NEWLINE, "\n", (1, 1), (1, 2), "x\n"),
            (NUMBER, "3", (2, 0), (2, 1), "3"),
        ], result

    test_generate_tokens("x\n3")
    test_generate_tokens("x\n3\n")
    # XXX This test fails:
    #test_generate_tokens("x\n3\n\n")
    # The problem is that the NEWLINE at the end of the file is not
    # generated, even though it was in the

# Generated at 2022-06-13 18:20:56.525779
# Unit test for function generate_tokens
def test_generate_tokens():
    import token
    from io import StringIO
    from unittest import TestCase

    class Tests(TestCase):
        def test_tokenize(self):
            readline = iter(["while 1: #comment\n  pass\n"]).__next__
            result = list(tokenize(readline))
            expected = [
                (tokenize.NAME, "while"),
                (tokenize.NUMBER, "1"),
                (tokenize.OP, ":"),
                (tokenize.COMMENT, "#comment"),
                (tokenize.NEWLINE, "\n"),
                (tokenize.INDENT, "  "),
                (tokenize.NAME, "pass"),
                (tokenize.NEWLINE, "\n"),
                (tokenize.DEDENT, ""),
                (token.ENDMARKER, ""),
            ]