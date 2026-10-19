

# Generated at 2022-06-13 18:13:32.322319
# Unit test for function tokenize
def test_tokenize():
    s = " def f(): pass\n"
    result = []
    tokenize(s.splitlines().__iter__().__next__, result.append)

# Generated at 2022-06-13 18:13:34.753517
# Unit test for function tokenize
def test_tokenize():
    with open("Grammar.txt", "rb") as f:
        encoding = detect_encoding(f.readline)
    with open("Grammar.txt", "r", encoding=encoding) as f:
        tokenize(f.readline)



# Generated at 2022-06-13 18:13:46.042157
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(seq):
        for line in seq:
            yield line

    def test(seq, expected):
        assert detect_encoding(readlines(iter(seq))) == (expected, seq)

    test(["a"], "utf-8")
    test(["# coding: ascii"], "ascii")
    test(["# coding=ascii"], "ascii")
    test(["#!/usr/bin/python", "# coding: latin-1"], "iso-8859-1")
    test(["# This is the python code"], "utf-8")
    test(["\xef\xbb\xbf# coding: utf-8", "\n"], "utf-8-sig")

# Generated at 2022-06-13 18:13:50.523676
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from io import StringIO
    from tokenize import generate_tokens
    from .tokenize import TokenInfo
    txt = """print()
"""
    expected = 'print()\n'
    f = StringIO(txt)
    result = Untokenizer().untokenize(generate_tokens(f.readline, None))
    assert(result == expected)



# Generated at 2022-06-13 18:13:57.830252
# Unit test for function tokenize_loop
def test_tokenize_loop():
    rl = iter(
        [
            b'# -*- coding: latin-1 -*-\n',
            b'a = 2\n',
            b'b = [1,\n',
            b'2]\n',
            b'\xf6\n',
            b"'''\n",
            b'3\n',
            b"'''\n",
        ]
    ).__next__
    def eat(type, token, start, end, line):
        print(
            "%d,%d-%d,%d:\t%s\t%s"
            % (start[0], start[1], end[0], end[1], token.type, token.string)
        )

    tokenize_loop(rl, eat)
test_tokenize_loop.__test__

# Generated at 2022-06-13 18:14:01.498710
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from . import untokenize as untokenize_mod
    from . import tokenize as tokenize_mod

    txt = "def f():\n    1\n    for i in [1, 2]:\n        pass\n"
    result = untokenize_mod.untokenize(tokenize_mod.generate_tokens(txt.splitlines(True)))
    assert result == txt, repr(result)



# Generated at 2022-06-13 18:14:04.700314
# Unit test for function printtoken
def test_printtoken():
    print("test printtoken")
    printtoken(57, "test", (1,2), (3,4), "this is a test")


# Generated at 2022-06-13 18:14:09.332580
# Unit test for function detect_encoding
def test_detect_encoding():
    from unittest.mock import Mock
    from io import BytesIO

    def readline_mock(line):
        def readline():
            if line:
                return line
            raise StopIteration

        return readline

    first_line_in = b"# coding: utf-8\n"
    second_line_in = b"pass  # nothing here\n"
    third_line_in = b"# more stuff\n"

    # Test with a codec declared in first line
    readline = readline_mock(first_line_in)
    assert detect_encoding(readline) == ("utf-8", [first_line_in])

    # Test with a codec declared in second line
    readline = readline_mock(second_line_in)

# Generated at 2022-06-13 18:14:13.679205
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for line in lines:
            yield line


# Generated at 2022-06-13 18:14:21.415950
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import token
    import tokenize
    import unittest

    text = "def f(x): return 2*x\n"
    gt = generate_tokens(io.StringIO(text).readline)
    tok = tokenize.tokenize(io.StringIO(text).readline)
    for token in gt:
        _token = next(tok)
        assert _token == token
    try:
        next(tok)
    except StopIteration:
        pass
    else:
        raise AssertionError("Too many tokens from tokenize.tokenize")

    # Test DEDENT after empty line
    gt = generate_tokens(io.StringIO("if 1:\n  pass\n  \n  pass\n").readline)

# Generated at 2022-06-13 18:15:04.801827
# Unit test for function tokenize_loop
def test_tokenize_loop():
    text = "def f(x): return 2 * x"
    from io import StringIO

    tokenize_loop(StringIO(text).readline, printtoken)



# Generated at 2022-06-13 18:15:13.062721
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import token
    readline = io.StringIO(
        """\
while 1:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
"""
    ).readline
    # These tests are normally run when import tokenize is done,
    # and additional tests are added for the tokenize module itself.
    for tok in generate_tokens(readline):
        print(tok)


# Generated at 2022-06-13 18:15:21.073470
# Unit test for function tokenize_loop
def test_tokenize_loop():
    # Make sure we can call tokenize_loop with a tokenize()-style generator
    # and that we can catch exceptions in it
    def gen():
        try:
            yield (1, "one", (1, 1), (1, 2), "one\n")
            yield (2, "two", (2, 1), (2, 2), "two\n")
            raise RuntimeError("some exception")
            yield (3, "three", (3, 1), (3, 2), "three\n")
        except RuntimeError:
            pass

    L = []
    tokenize_loop(gen, L.append)

# Generated at 2022-06-13 18:15:30.320634
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        if lines:
            return lines.pop(0)
        else:
            raise StopIteration
    lines = [br'hi this is utf-16 \xe4\xf6\xfc',
             br'# coding:utf-8', br'']
    # the next line raises a SyntaxError:
    #     encoding problem: utf-8 with BOM
    # since the BOM is inconsistent with the cookie
    # self.assertRaises(SyntaxError, detect_encoding, readline)
    lines = [br'hi this is utf-16 \xe4\xf6\xfc', br'# -*- coding:utf-8 -*-']

# Generated at 2022-06-13 18:15:41.829682
# Unit test for function generate_tokens
def test_generate_tokens():
    def test(input: str, expected: str) -> None:
        tokens = []
        for token in generate_tokens(iter(input.splitlines()).__next__):
            tokens.append(token[:2])
        # print("%5s %s".format("", input))
        # print("%5s %s".format("", expected))
        # print("%5s %s".format("", tokens))
        assert tokens in expected, "Error: input: %s expected: %s tokens: %s" \
            % (input, expected, tokens)
    test("", "[(257, '')]")
    test("\n", "[(257, ''), (4, '')]")
    test("a", "[(1, 'a')]")

# Generated at 2022-06-13 18:15:48.685114
# Unit test for function generate_tokens
def test_generate_tokens():
    from tokenize import generate_tokens as ref_generate_tokens
    from io import StringIO
    def check(s, ref_tokens):
        f = StringIO(s)
        tokens = list(generate_tokens(f.readline))
        ref_tokens = list(ref_tokens)
        assert tokens == ref_tokens
    #

# Generated at 2022-06-13 18:15:51.565152
# Unit test for function tokenize_loop
def test_tokenize_loop():
    rl = iter(["print('Hello, world!');"]).__next__
    tokener = printtoken
    tokenize_loop(rl, tokener)


# for backwards compatibility

# Generated at 2022-06-13 18:15:57.334659
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from blib2to3.pygram import python_grammar_no_print_statement as python_grammar
    import io
    import re
    s = "Re#comment\nExtend(foo, firstprio#comment\n= bar,"

    f = io.StringIO(s)
    result = []

    def tokeneater(*args):
        result.append(args)

    grammar = Grammar(python_grammar)
    generate_tokens(f.readline, out=result)

# Generated at 2022-06-13 18:16:07.873678
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import unittest
    import sys

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.saved_stdin = sys.stdin
            sys.stdin = self.input = io.StringIO("# test\n")
            self.tokens = []

        def tearDown(self):
            sys.stdin = self.saved_stdin

        def tokenize_loop(self, readline, tokeneater):
            for token_info in generate_tokens(readline):
                tokeneater(*token_info)

        def tokeneater(self, type, token, start, end, line):
            self.tokens.append((type, token, start, end, line))


# Generated at 2022-06-13 18:16:20.460706
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    from io import StringIO
    import random
    import re

    # Test roundtrips

# Generated at 2022-06-13 18:16:50.456626
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import tokenize as tok
    r = io.BytesIO(b"def x(): pass\n")
    l = tok.tokenize_loop(r.readline, printtoken)
    while l:
        l = tok.tokenize_loop(r.readline, printtoken)
    return [""]



# Generated at 2022-06-13 18:16:56.952723
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for line in ["# coding: latin-1\n", "pass\n", "pass\n"]:
            yield line.encode("ascii")

    assert detect_encoding(readline) == ("iso-8859-1", ["# coding: latin-1\n".encode("ascii")])



# Generated at 2022-06-13 18:17:09.535770
# Unit test for function generate_tokens
def test_generate_tokens():
    def test(s, expected_tokens):
        result = [(t.type, t.string) for t in generate_tokens(iter(s.splitlines(True)).next)]
        if result != expected_tokens:
            msg = "tests failed:\ninput   : %r\nexpected: %r\nreceived: %r" % (
                s, expected_tokens, result)
            raise AssertionError(msg)

    test("a = 3\n", [(NAME, "a"), (OP, "="), (NUMBER, "3"), (NEWLINE, "\n")])
    test("a\t=\t3\n", [(NAME, "a"), (OP, "="), (NUMBER, "3"), (NEWLINE, "\n")])

# Generated at 2022-06-13 18:17:11.705402
# Unit test for function tokenize
def test_tokenize():
    readline = iter('"abc" # comment\n"def"\n123').__next__
    tokenize(readline)



# Generated at 2022-06-13 18:17:19.628499
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import token
    import tokenize

    readline = io.BytesIO(b"if 1:\n print(2)\n").readline
    tokens = generate_tokens(readline)
    # For comparison, tokens is a generator expression in the standard
    # library implementation:  tokens = tokenize.generate_tokens(readline)
    result = list(tokens)

# Generated at 2022-06-13 18:17:23.831066
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:17:26.821050
# Unit test for function generate_tokens
def test_generate_tokens():
    import StringIO
    import token
    tokeneater = TokenEater()
    s = StringIO.StringIO("for a in b: pass\n")
    tokeneater.tokenize(s.readline)



# Generated at 2022-06-13 18:17:28.473057
# Unit test for function tokenize
def test_tokenize():
    import io
    rio = io.StringIO("""if 1:
    #comment1
    pass  #comment2
""")
    def readline():
        return rio.readline()
    result = []
    tokenize(readline, result.append)
    return result


# Generated at 2022-06-13 18:17:36.401889
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io

    rl = io.StringIO(
        "def f():\n    print(1)\n"
    ).readline

    def collect_token_info(*token_info):
        token_info_list.append(token_info)

    token_info_list = []
    tokenize_loop(rl, collect_token_info)
    # Tests that tokenize_loop correctly builds up the token_info_list

# Generated at 2022-06-13 18:17:46.617849
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(s):
        for l in s.splitlines(keepends=True):
            yield l

    def test(s, exp_enc, exp_lines):
        got_enc, got_lines = detect_encoding(readlines(s))
        assert exp_enc == got_enc, (s, exp_enc, got_enc)
        assert exp_lines == got_lines, (s, exp_lines, got_lines)

    test("\xEF\xBB\xBF# coding: utf-8\n", "utf-8", ["# coding: utf-8\n"])
    test("# coding: latin-1\n", "iso-8859-1", ["# coding: latin-1\n"])

# Generated at 2022-06-13 18:18:44.327346
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        yield b"# -*- coding: iso-latin-1 -*-"
        yield b"# xx"
        yield b"\xc3"
    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"
    assert lines == [b"# -*- coding: iso-latin-1 -*-", b"# xx", b"\xc3"]



# Generated at 2022-06-13 18:18:55.065908
# Unit test for function generate_tokens
def test_generate_tokens():
    import token
    import io, tokenize
    test_tokenize = tokenize.generate_tokens(io.StringIO('Spam = "eggs"\n').readline)
    # Check it to make sure it's generating the expected tokens
    assert next(test_tokenize) == (token.NAME, 'Spam', (1, 0), (1, 4), 'Spam = "eggs"\n')
    assert next(test_tokenize) == (token.OP, '=', (1, 4), (1, 5), 'Spam = "eggs"\n')
    assert next(test_tokenize) == (token.STRING, '"eggs"', (1, 6), (1, 12), 'Spam = "eggs"\n')

# Generated at 2022-06-13 18:19:04.337242
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import tokenize

    def readline_iter(lines: List[Text]) -> Callable[[], bytes]:
        def readline() -> bytes:
            if not lines:
                raise StopIteration
            return lines.pop(0).encode("ascii")

        return readline

    def check(expected, lines):
        detect = tokenize.detect_encoding(readline_iter(lines))
        assert expected == detect, (expected, detect, lines)


# Generated at 2022-06-13 18:19:12.980333
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:19:19.996844
# Unit test for function detect_encoding
def test_detect_encoding():
    readline = iter(["# coding: utf-8\n", "\n", "1+1\n"]).__next__
    encoding, unused = detect_encoding(readline)
    assert encoding == "utf-8"

    readline = iter(["", "\n", "1+1\n"]).__next__
    encoding, unused = detect_encoding(readline)
    assert encoding == "utf-8"

    readline = iter([b"\xef\xbb\xbf# coding: utf-8\n", "\n", "1+1\n"]).__next__
    encoding, unused = detect_encoding(readline)
    assert encoding == "utf-8-sig"


# Generated at 2022-06-13 18:19:25.275797
# Unit test for function generate_tokens
def test_generate_tokens():
    def check_token_equal(t1, t2):
        for i in range(3):
            if t1[i] != t2[i]:
                print(t1)
                print(t2)
                assert False

# Generated at 2022-06-13 18:19:29.364031
# Unit test for function tokenize
def test_tokenize():
    import io

    s = io.StringIO("import sys\n")
    try:
        tokenize(s.readline)
    except StopTokenizing:
        pass



# Generated at 2022-06-13 18:19:39.396493
# Unit test for function generate_tokens
def test_generate_tokens():
    import re
    import string
    from io import StringIO
    from token import *
    from tokenize import tokenize, untokenize, generate_tokens, NUMBER, STRING
    with open(__file__) as fp:
        fp = StringIO(fp.read())
        g0 = tokenize(fp.readline)
        fp.seek(0)
        g1 = generate_tokens(fp.readline)
        while 1:
            tok1 = next(g0)
            tok2 = next(g1)
            if tok1[:2] != tok2[:2]:
                print("Tokens differ:", tok1, tok2)
            else:
                print(tok2)
import sys
from io import StringIO
from token import *

# Generated at 2022-06-13 18:19:45.448041
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        return [
            "# comment",
            "# coding: utf-8",
            "def foo():",
            "    return 1",
        ]

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"



# Generated at 2022-06-13 18:19:56.676362
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
    s = "abcdefg\n12345"
    u = Untokenizer()
    u.prev_row = 1
    u.prev_col = 0
    res = u.add_whitespace((1, 0))
    assert u.tokens == []
    res = u.add_whitespace((1, 1))
    assert u.tokens == [" "]
    res = u.add_whitespace((1, 2))
    assert u.tokens == ["  "]
    res = u.add_whitespace((1, 3))
    assert u.tokens == ["   "]
    res = u.add_whitespace((1, 4))
    assert u.tokens == ["    "]
    res = u.add_whitespace((1, 5))
    assert u

# Generated at 2022-06-13 18:20:45.992264
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO

    def token_stream(s: str, grammar: Optional[Grammar] = None) -> List[TokenInfo]:
        return list(generate_tokens(StringIO(s).readline, grammar))


# Generated at 2022-06-13 18:20:51.554515
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO
    from tokenize import tokenize

    s = '''def f(a):
    return a + 1'''
    with StringIO(s) as f:
        toks = tokenize(f.readline)
    u = Untokenizer()
    res = u.compat(next(toks), toks)
    assert res is None



# Generated at 2022-06-13 18:20:59.407489
# Unit test for function detect_encoding
def test_detect_encoding():
    def get_readline(lines: List[List[bytes]]) -> Callable[[], bytes]:
        def readline() -> bytes:
            if lines:
                return lines.pop()
            else:
                raise StopIteration

        return readline

    # Example from PEP 263
    sample = (
        "  # -*- coding: cp1252 -*-\n"
        + "# some comment\n"
        + "# another comment\n"
        + "a = 'test string'\n"
    )
    readline = get_readline([s.encode("utf-8") for s in sample.splitlines()])
    encoding, _ = detect_encoding(readline)
    assert encoding == "cp1252"

    # Only a coding cookie ("coding: <encoding>") should be accepted,
   

# Generated at 2022-06-13 18:21:14.043757
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO

    from . import tokenize

    def untokenize(input: Text) -> Text:
        output = StringIO()
        untok = Untokenizer()
        tokenize.tokenize(StringIO(input).readline, lambda toknum, tokval, *args: None)
        output.write(untok.compat((tokenize.ENCODING, "utf-8"), iter([])))
        tokenize.tokenize(StringIO(input).readline, untok.compat)
        return output.getvalue()

    assert untokenize("a = 1") == "a = 1"
    assert untokenize("def f():\n\ts=1") == "def f():\n\ts = 1"

# Generated at 2022-06-13 18:21:19.814016
# Unit test for function tokenize
def test_tokenize():
    import io
    from blib2to3.pgen2.tokenize import generate_tokens

    def readline(string):
        for c in string:
            yield c
        yield ''

    s = "def foo(a, b, c): pass"
    tokens = list(generate_tokens(readline(s)))
    print(tokens)

# Generated at 2022-06-13 18:21:29.734202
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:21:39.317988
# Unit test for function detect_encoding
def test_detect_encoding():
    line = b""
    def readline():
        nonlocal line
        try:
            r = line
            line = b""
            return r
        except IndexError:
            raise StopIteration
    def roundtrip(encoding, line1, line2):
        nonlocal line
        encoding, bom_found = detect_encoding(readline)
        line1 = line1.replace(r"\r\n", "\r\n").replace(r"\n", "\n")
        line2 = line2.replace(r"\r\n", "\r\n").replace(r"\n", "\n")
        line = line1.encode(encoding)
        if line2:
            line += line2.encode(encoding)
        encoding2, bom_found2 = detect_encoding(readline)
       

# Generated at 2022-06-13 18:21:40.560404
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    ut = _Test_compat_class()
    ut._test()

# Generated at 2022-06-13 18:21:53.580283
# Unit test for function generate_tokens
def test_generate_tokens():

    def remove_whitespace_tokens(tokens):
        return [t for t in tokens if t[0] != tokenize.NEWLINE]

    source = """\
    for i in range(10):
        print(i)
    """

# Generated at 2022-06-13 18:22:04.711588
# Unit test for function tokenize
def test_tokenize():
    import StringIO, token
    text = "def f(x): return 2*x"
    toks = tokenize(StringIO.StringIO(text).readline)
    print(toks)
    toks = list(tokenize(StringIO.StringIO(text).readline))