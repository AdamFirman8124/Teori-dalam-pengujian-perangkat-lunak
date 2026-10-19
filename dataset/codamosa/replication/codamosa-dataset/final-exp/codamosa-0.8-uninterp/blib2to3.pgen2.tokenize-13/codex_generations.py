

# Generated at 2022-06-13 18:13:18.609425
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from blib2to3.pygram import python_symbols as syms
    untok = Untokenizer()

# Generated at 2022-06-13 18:13:19.645580
# Unit test for function printtoken
def test_printtoken():
    printtoken(6, 'hi', (1,2,), (3,4,), '')



# Generated at 2022-06-13 18:13:21.312895
# Unit test for function printtoken
def test_printtoken():
    # pass (tested in 2.2)
    pass

if __name__ == "__main__":
    test_printtoken()

# ____________________________________________________________
# Backward compatible interface



# Generated at 2022-06-13 18:13:25.483788
# Unit test for function generate_tokens
def test_generate_tokens():
    for t in generate_tokens(iter('''\
        def f(x):
            return 2*x'''.splitlines(True)).__next__):
        print(t)

test_generate_tokens()


# Generated at 2022-06-13 18:13:32.474021
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        return readlines.pop(0)

    # no encoding
    readlines = [bytes()]
    assert detect_encoding(readline) == ("utf-8", readlines)
    readlines = [b"blah blah blah \n"]
    assert detect_encoding(readline) == ("utf-8", readlines)

    # encoding specified by utf-8 BOM
    readlines = [BOM_UTF8]
    assert detect_encoding(readline) == ("utf-8-sig", readlines)
    readlines = [BOM_UTF8 + b"blah blah \n"]
    assert detect_encoding(readline) == ("utf-8-sig", readlines)
    # encoding specified by utf-8 BOM and encoding cookie

# Generated at 2022-06-13 18:13:43.062690
# Unit test for function detect_encoding
def test_detect_encoding():
    lines = ['encoding = "latin-1"\n',
             'a = "ä"\n',
             'b = "©"\n']
    def l() -> bytes:
        return lines.pop(0).encode("latin-1")
    assert detect_encoding(l) == ('latin-1', [])

    lines = ['# coding=iso-8859-1\n',
             'a = "ä"\n',
             'b = "©"\n']
    def l() -> bytes:
        return lines.pop(0).encode("ascii")
    assert detect_encoding(l) == ('iso-8859-1', [])


# Generated at 2022-06-13 18:13:46.275387
# Unit test for function tokenize
def test_tokenize():
    import sys

    if sys.argv[1:]:
        tokenize(open(sys.argv[1]).readline)
    else:
        tokenize(sys.stdin.readline)



# Generated at 2022-06-13 18:13:49.615478
# Unit test for function printtoken
def test_printtoken():
    data = '''
    if a == b:
        a = "hello\\
        wor\\
        ld"
    '''
    for token in generate_tokens(StringIO(data).readline):
        printtoken(*token)


# Generated at 2022-06-13 18:13:51.973234
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:13:56.071289
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    from .tokenize import tokenize

    u = Untokenizer()
    text = io.StringIO("def f():\n    pass\n\n").readline
    g = tokenize(text)
    assert u.untokenize(g) == "def f():\n    pass\n\n"


# Line numbers and offsets used by tokenize
tok_line_offset = 0
tok_char_offset = 0



# Generated at 2022-06-13 18:15:06.401847
# Unit test for function generate_tokens
def test_generate_tokens():
    import tokenize, io
    r = io.BytesIO(b"if 1:\n    pass\n")
    result = tokenize.tokenize(r.readline)

# Generated at 2022-06-13 18:15:12.651374
# Unit test for function detect_encoding
def test_detect_encoding():
    def read_helper(lines: List[bytes]) -> Callable[[], bytes]:
        def readline() -> bytes:
            return lines.pop(0) if lines else bytes()

        return readline

    def readlines_helper(lines: List[bytes]) -> Iterator[bytes]:
        return iter(lines)

    # The unicode line separator and paragraph separator guarantee that
    # readline returns an empty line.

# Generated at 2022-06-13 18:15:20.846678
# Unit test for function generate_tokens
def test_generate_tokens():
    import tokenize
    from io import StringIO

    text = "def f():\n  print('hello, world')\n"
    tokengen = generate_tokens(StringIO(text).readline)
    for tokid, tokval, _, _, _ in tokenize.generate_tokens(StringIO(text).readline):
        newtokid, newtokval, _, _, _ = next(tokengen)
        assert tokid == newtokid and tokval == newtokval

    text = 'if True:\n  pass\nx = "abc"'
    tokengen = generate_tokens(StringIO(text).readline)

# Generated at 2022-06-13 18:15:25.968442
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import token
    r = io.BytesIO(b"if 1:\n  pass\n")
    result = [(token.NAME, 'if'), (token.NUMBER, '1'), (token.COLON, ':'), 
                (token.NEWLINE, '\n'), (token.INDENT, ''), (token.NAME, 'pass'), 
                (token.NEWLINE, '\n'), (token.DEDENT, '')]
    for t in generate_tokens(r.readline):
        assert t[:3] == result.pop(0)

test_generate_tokens()

# Example of usage
if __name__ == '__main__':
    f = open("test.py")
    for t in generate_tokens(f.readline):
        print(t)

# Generated at 2022-06-13 18:15:35.347491
# Unit test for function generate_tokens
def test_generate_tokens():
    '''Unit test for generate_tokens
    '''
    from unittest import TestCase
    from token import NUMBER, NAME, OP, STRING, ENDMARKER, NEWLINE, INDENT, DEDENT
    import io

    class GenerateTokensTests(TestCase):
        def test_single_quoted_strings(self):
            gt = generate_tokens(io.StringIO("'one\\ntwo\\'three'"))
            self.assertEqual(next(gt), (STRING, "'one\\ntwo\\'three'", (1, 0), (1, 16), '\'one\\ntwo\\\'three\''))
            self.assertEqual(next(gt), (NEWLINE, '\n', (1, 16), (1, 17), '\'one\\ntwo\\\'three\''))

# Generated at 2022-06-13 18:15:44.716243
# Unit test for function generate_tokens
def test_generate_tokens():
    import token
    from io import BytesIO
    from typing import List

    # Test round-trip invariant for full input
    token_list: List[TokenInfo] = []
    with open('test_tokenize.py', 'rb') as f:
        for tokid, tokval, _, _, _ in generate_tokens(f.readline):
            token_list.append((tokid, tokval))

    # Retrieve source code from token list
    src = [t[1].decode('utf-8') for t in token_list]
    src = ''.join(src)

    # Check if the source code matches the input
    with open('test_tokenize.py', 'rb') as f:
        assert f.read().decode('utf-8') == src

    # Test round-trip invari

# Generated at 2022-06-13 18:15:47.962693
# Unit test for function generate_tokens
def test_generate_tokens():
    module_text = tokenize.__doc__
    module_tokens = list(tokenize.generate_tokens(BytesIO(module_text).readline))
    new_module_text = Untokenizer().untokenize(module_tokens)
    assert new_module_text == module_text

test_generate_tokens()

# Generated at 2022-06-13 18:15:57.251349
# Unit test for function detect_encoding
def test_detect_encoding():
    import io

    x = io.BytesIO(b"\xef\xbb\xbfabc")
    y = io.BytesIO(b"\xef\xbb\xbf# coding: utf-8\n")
    z = io.BytesIO(b"# coding: utf-8\n")
    w = io.BytesIO(b"# coding: bad\n")
    e = io.BytesIO(b"# coding:\n")
    q = io.BytesIO(b'\n# coding: "bad"\n')
    a = io.BytesIO(b'\n# coding: "bad"\n\n')
    assert detect_encoding(x) == ("utf-8-sig", [b"abc"])

# Generated at 2022-06-13 18:16:05.193753
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:16:09.226802
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    U = Untokenizer()
    input_tokens = (
        (NAME, "x", (1, 0), (1, 1), "x"),
        (PLUS, "+", (1, 1), (1, 2), "+"),
        (NAME, "y", (1, 2), (1, 3), "y"),
        (NEWLINE, "", (1, 3), (1, 3), "\n"),
        (NAME, "z", (2, 0), (2, 1), "z"),
        (PLUS, "+", (2, 1), (2, 2), "+"),
        (NAME, "x", (2, 2), (2, 3), "x"),
        (NEWLINE, "", (2, 3), (2, 3), "\n"),
    )

# Generated at 2022-06-13 18:17:04.357070
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    u = untokenize([(1, "a"), (2, "b"), (0, "c")])
    assert u == "a b c"



# Generated at 2022-06-13 18:17:15.890970
# Unit test for function tokenize

# Generated at 2022-06-13 18:17:26.702815
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    untok = Untokenizer()

# Generated at 2022-06-13 18:17:30.621602
# Unit test for function tokenize
def test_tokenize():
    import io
    rio= io.StringIO("""\
    # this is a comment
    if 1:
        print("done!")
    """)
    def readline():
        return rio.readline()
    tokenize(readline)


# Generated at 2022-06-13 18:17:37.188063
# Unit test for function generate_tokens
def test_generate_tokens():
    def chars_in_line(s):
        return set(s) - set("\r\n")

    t1 = generate_tokens(iter("def f(x): pass\n").next)
    assert chars_in_line(t1.next()[1]) == set("def")
    assert chars_in_line(t1.next()[1]) == set("f")
    assert chars_in_line(t1.next()[1]) == set("(")
    assert chars_in_line(t1.next()[1]) == set("x")
    assert chars_in_line(t1.next()[1]) == set(")")
    assert chars_in_line(t1.next()[1]) == set(":")

# Generated at 2022-06-13 18:17:46.682850
# Unit test for function detect_encoding
def test_detect_encoding():
    from io import StringIO

    def reader(s: str) -> Iterator[bytes]:
        for c in s:
            yield bytes([c])

    eq = lambda s: lambda: detect_encoding(reader(s))
    e = StringIO()
    print(e.encoding)
    eq("# coding: latin-1")()
    eq(" # coding=ascii")()
    eq("\ufeff# coding:utf-8")()
    eq('"""blah')("utf-8", [b'"', b'"', b'"blah'])
    eq('\n"""blah')("utf-8", [b'\n', b'"', b'"', b'"blah'])

# Generated at 2022-06-13 18:17:54.403611
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    import io
    import token

    untok = Untokenizer()
    uio = io.StringIO("def f():\n  pass\n")
    result = []
    try:
        tokenize(uio.readline, result.append)
    except tokenize.TokenError:
        pass
    assert untok.compat(("ENDMARKER", ""), iter(result)) is None
    assert "".join(untok.tokens) == "def f():\n  pass\n"



# Generated at 2022-06-13 18:18:02.351173
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import tokenize

    def detect_encoding(lines):
        stream = io.StringIO(lines)
        readline = stream.readline
        return tokenize.detect_encoding(readline)[0]

    def check(lines, encoding):
        detected = detect_encoding(lines)
        assert detected == encoding, (
            "Wrong encoding detected for %r, got %r instead of %r"
            % (lines, detected, encoding)
        )

    # no encoding
    check("", "utf-8")
    check("   \t   ", "utf-8")
    # no encoding, with funny whitespace
    check("\x0c\n", "utf-8")
    # UTF8 BOM

# Generated at 2022-06-13 18:18:10.433912
# Unit test for function tokenize_loop
def test_tokenize_loop():
    s = 'print("foo") # comment'
    toks = []
    tokenize_loop(s.splitlines().__next__, toks.append)
    assert toks == [(token.NAME, 'print', (1, 0), (1, 5), s),
                    (token.OP, '(', (1, 5), (1, 6), s),
                    (token.STRING, '"foo"', (1, 6), (1, 11), s),
                    (token.OP, ')', (1, 11), (1, 12), s),
                    (token.COMMENT, '# comment', (1, 12), (1, 21), s)]
test_tokenize_loop()



# Generated at 2022-06-13 18:18:20.274327
# Unit test for function detect_encoding
def test_detect_encoding():
    from io import StringIO

    def reader(s):
        sio = StringIO(s)
        while 1:
            line = sio.readline()
            if not line:
                raise StopIteration
            yield bytes(line, "utf-8")

    assert detect_encoding(reader("")) == ("utf-8", [])
    assert detect_encoding(reader("# -*- coding: latin-1 -*-")) == (
        "iso-8859-1",
        [b"# -*- coding: latin-1 -*-"],
    )

# Generated at 2022-06-13 18:19:01.704335
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    u = Untokenizer()
    result = u.compat((0, "this"), [(0, " "), (0, "is"), (0, " "), (0, "a"), (0, " "), (0, "test")])
    assert result == None

# Generated at 2022-06-13 18:19:05.465223
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield "# -*- coding: latin-1 -*-"
    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"



# Generated at 2022-06-13 18:19:17.832500
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        return next(lines)

    lines = iter(
        [
            b'# -*- coding: "iso-8859-1" -*-\n',
            b'\n',
            b'# -*- coding: "ascii" -*-\n',
            b'\n',
            b'# -*- coding: "ascii" -*-\n',
            b'\n',
        ]
    )
    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"


# Generated at 2022-06-13 18:19:24.144168
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import unittest

    class TestTokenizeLoop(unittest.TestCase):
        def test_tokenize_loop_simple(self):
            text = "a = 1"

            tok_list = []
            def tokeneater(type, token, start, end, line):
                tok_list.append((type, token))
            #
            tokenize_loop(io.StringIO(text).readline, tokeneater)

            self.assertEqual(tok_list,
                [(NAME, 'a'), (OP, '='), (NUMBER, '1')])

    unittest.main()

# Don't use unicode_literals here, TestSuite() compares against assertEqual()
# literals as byte strings.

# Generated at 2022-06-13 18:19:38.391730
# Unit test for function generate_tokens
def test_generate_tokens():
    s = """def f(x, y=42, *args, **kwargs):
    print(x, y, args, kwargs)"""
    tokens = list(tokenize.generate_tokens(StringIO(s).readline))

# Generated at 2022-06-13 18:19:50.088167
# Unit test for function generate_tokens
def test_generate_tokens():
    from tokenize import tokenize

    from io import StringIO

    r = StringIO(
        '''if 1:
    # comment
    print('foo#bar')
'''
    )
    tokens = list(tokenize(r.readline))
    # The first 3 tokens are (ENCODING, 'utf-8', (1, 0)).

# Generated at 2022-06-13 18:19:56.960959
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    u = Untokenizer()
    s = "for i in range(10):\n    print(i)\n"
    g = generate_tokens(s.__iter__().__next__)
    result = u.compat(next(g), g)
    assert u.tokens == [
        "for ",
        "i ",
        "in ",
        "range(10):\n",
        "    ",
        "print(",
        "i",
        ")\n",
    ]
# End unit test for method compat of class Untokenizer



# Generated at 2022-06-13 18:19:57.575579
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat(): pass


# Generated at 2022-06-13 18:20:04.770977
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        # check that readline doesn't get called more often than necessary
        assert False

    def readlines():
        yield bytes("text", "ascii")

    assert detect_encoding(readline) == ("utf-8", [])

    def readlines():
        yield bytes("# coding: latin-1", "ascii")
        yield bytes("text", "latin-1")

    assert detect_encoding(readlines) == ("latin-1", [bytes("text", "latin-1")])

    def readlines():
        yield bytes("# coding=iso-8859-1", "ascii")
        yield bytes("text", "latin-1")


# Generated at 2022-06-13 18:20:14.878786
# Unit test for function generate_tokens
def test_generate_tokens():
    def remove_start_end_markers(tokens):
        return [t for t in tokens if t[0] not in {ENDMARKER, ENCODING}]

    def test_tokenize(code, expected_tokens):
        if isinstance(code, str):
            code = code.encode("utf-8")
        readline = create_generate_tokens_reader(code)
        tokens = list(generate_tokens(readline))
        assert remove_start_end_markers(tokens) == expected_tokens
        untok = untokenize(tokens)
        readline_untok = create_generate_tokens_reader(untok)
        tokens_untok = list(generate_tokens(readline_untok))
        assert remove

# Generated at 2022-06-13 18:20:54.974302
# Unit test for function detect_encoding
def test_detect_encoding():
    for encoding in ("ascii", "latin-1"):
        for bom in ("", "\xef\xbb\xbf"):
            for line1, line2 in (
                ("", ""),
                ("", "# -*- coding: %s -*-" % encoding),
                ("#!/usr/local/bin/python", ""),
                ("# -*- coding: %s -*-" % encoding, ""),
                ("#!/usr/local/bin/python", "# -*- coding: %s -*-" % encoding),
            ):
                lines = [bom + b for b in (line1.encode(encoding), line2.encode(encoding))]

# Generated at 2022-06-13 18:21:09.009495
# Unit test for function generate_tokens
def test_generate_tokens():
    import token as tokenize
    input = "def f(a=''):  # comment\n  a # comment\n  "
    result = [t for t in tokenize.generate_tokens(input.splitlines().next)]

# Generated at 2022-06-13 18:21:15.713811
# Unit test for function tokenize_loop
def test_tokenize_loop():
    readline = iter(
        """\
if 1:
    print('foo#bar')
        """.splitlines(
            True
        )
    ).__next__
    tokeneater = generate_tokens(readline).__next__
    tokenize_loop(readline, tokeneater)


# @print_timing

# Generated at 2022-06-13 18:21:22.912195
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    untok = Untokenizer()
    tokens = [
        (NUMBER, "1", (1, 0), (1, 1), "1"),
        (OP, "+", (1, 1), (1, 2), "+"),
        (NUMBER, "1", (1, 2), (1, 3), "1"),
        (NEWLINE, "\n", (1, 3), (1, 4), "\n"),
        (NUMBER, "1", (2, 0), (2, 1), "1"),
    ]
    assert untok.untokenize(tokens) == "1 + 1\n1"



# Generated at 2022-06-13 18:21:32.160636
# Unit test for function generate_tokens
def test_generate_tokens():
    def test_tokenize(input: str, expected: List[GoodTokenInfo], grammar: Optional[Grammar] = None) -> None:
        result = []
        for token in generate_tokens(iter([input]).__next__, grammar=grammar):
            result.append(token)
        assert result == expected

    # Basic tests

# Generated at 2022-06-13 18:21:36.787542
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import untokenize
    import io
    f = io.BytesIO()

    untokenize.Untokenizer(f).untokenize([(1, 'def'), (2, False), (3, 'f'), (4, '('), (5, ')'), (0, ':')])

    assert f.getvalue() == b"def Falsef():"


# Generated at 2022-06-13 18:21:45.574390
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    from token import *
    from tokenize import tokenize
    readline = StringIO(
        "if 1: #\n  1 + 1\n #\n  2 + 2\n").readline
    tokens = generate_tokens(readline)
    result = []
    for toknum, tokval, _, _, _ in tokens:
        result.append((toknum, tokval))

# Generated at 2022-06-13 18:22:00.146390
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:22:08.094682
# Unit test for function tokenize_loop
def test_tokenize_loop():
    rl = iter(["print(x)"]).__next__
    tl = []
    def te(*args):
        tl.append(args)
    tokenize_loop(rl, te)
    assert tl == [(1, 'print', (0, 0), (0, 5), 'print(x)'),
                  (53, '(', (0, 5), (0, 6), 'print(x)'),
                  (1, 'x', (0, 6), (0, 7), 'print(x)'),
                  (53, ')', (0, 7), (0, 8), 'print(x)'),
                  (0, '', (0, 8), (0, 8), ''),
                  (4, '', (1, 0), (1, 0), '')]



# Generated at 2022-06-13 18:22:12.381598
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from .tokenize import tokenize

    code = 'def f():\n print(1)'
    tokens = list(tokenize(io.StringIO(code).readline))

    ut = Untokenizer()
    ut_code = ut.untokenize(tokens)

    # Untokenizer is a bit buggy, so I don't test the whole code here
    assert ut_code.endswith('print(1)')

