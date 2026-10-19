

# Generated at 2022-06-13 18:14:10.581556
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import unittest
    import unittest.mock
    
    mock_tokeneater = unittest.mock.Mock()
    def readline() -> Text:
        return io.StringIO('if True:\n    pass\n').readline()
    tokenize_loop(readline, mock_tokeneater)
    mock_tokeneater.assert_called()
    mock_tokeneater.assert_called_with(
        token.NAME, 'if', (1, 0), (1, 2), 'if True:\n'
    )
    mock_tokeneater.assert_called_with(
        token.NAME, 'True', (1, 3), (1, 7), 'if True:\n'
    )

# Generated at 2022-06-13 18:14:19.138232
# Unit test for function generate_tokens
def test_generate_tokens():
    text = """
            def f(x) :
                return 2*x
            """
    from StringIO import StringIO
    from token import tok_name
    from tokenize import generate_tokens
    from tokenize import NL, INDENT, DEDENT, NAME, NEWLINE
    result = [(toknum, tokval) for toknum, tokval, _, _, _ in generate_tokens(StringIO(text).readline)]

# Generated at 2022-06-13 18:14:27.101881
# Unit test for function generate_tokens
def test_generate_tokens():
    import pprint
    import io

    class TokenTest(unittest.TestCase):
        def tokens(self, s: str, grammar: Optional[Grammar] = None) -> Iterator[GoodTokenInfo]:
            return generate_tokens(io.StringIO(s).readline, grammar)

        def check(self, s: str, grammar: Optional[Grammar] = None):
            print("Trying:", s)
            result = list(self.tokens(s, grammar))
            print("Result:")
            pprint.pprint(result)

        def test_op(self):
            for op in "+-*/":
                for style in ["prefix", "infix", "postfix"]:
                    self.check(op + style)


# Generated at 2022-06-13 18:14:31.629529
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    untokenizer = Untokenizer()
    input_data = [(NAME, "as"), (NAME, "f"), (OP, "("), (NAME, "x"), (OP, ")"), (OP, ":")]
    expected = "as f ( x ) : "
    actual = untokenizer.compat((NAME, "as"), input_data)
    assert actual == expected, "expected %s but got %s" % (expected, actual)

# Generated at 2022-06-13 18:14:37.402421
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    a = [
        (1, "token1"),
        (0, " "),
        (2, "token2"),
        (3, "token3"),
        (0, "\n"),
        (4, "token4"),
        (5, "token5"),
        (0, " "),
        (6, "token6"),
        (7, "token7"),
        (0, "\n"),
    ]
    u = Untokenizer()
    result = u.untokenize(a)
    assert result == "token1 token2 token3\n  token4 token5 token6 token7\n"



# Generated at 2022-06-13 18:14:43.329435
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:14:53.517847
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import token
    import tokenize
    r = io.StringIO("def f(x): return x+1\n")
    t = tokenize.tokenize(r.readline)
    token_list = list(t)
    assert token_list[0] == (token.NAME, "def", (1, 0), (1, 3), "\n")
    assert token_list[1] == (token.NAME, "f", (1, 4), (1, 5), "\n")
    assert token_list[2] == (token.OP, "(", (1, 5), (1, 6), "\n")
    assert token_list[3] == (token.NAME, "x", (1, 6), (1, 7), "\n")

# Generated at 2022-06-13 18:15:00.450248
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    readline = io.StringIO("def f(x): return 2*x").readline
    tokeneater = lambda x, y, z, t, u: print(x, y, z, t, u)
    tokenize_loop(readline, tokeneater)



# Generated at 2022-06-13 18:15:07.740483
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    untok = Untokenizer()
    iterable = [(3, 'def'), (1, ' '), (1, 'f'), (1, '('), (1, ')'), (1, ':'), (4, ''), (0, ''), (4, '')]
    correct_result = "def f ( ) :"
    result = untok.compat((3, 'def'), iterable)
    assert result == correct_result, "Should be 'def f ( ) :'"

test_Untokenizer_compat()

# Generated at 2022-06-13 18:15:13.880608
# Unit test for function detect_encoding
def test_detect_encoding():
    import io

    def readline() -> bytes:
        return next(b_lines)

    b_lines = (line.encode("ascii") for line in [
        '# -*- coding: latin-1 -*-\n',
        '#!/usr/bin/env python3\n',
        '# This Python file uses the following encoding: utf-8\n'
    ])
    assert detect_encoding(readline) == ('iso-8859-1', [b'# -*- coding: latin-1 -*-\n'])

# Generated at 2022-06-13 18:16:07.170553
# Unit test for function detect_encoding
def test_detect_encoding():
    import codecs, re, tempfile
    try:
        from tokenize import detect_encoding, TokenError, open as py_open
    except ImportError:
        py_open = open

    def test(txt: str, enc: str, first: str) -> None:
        f = tempfile.TemporaryFile(mode="w+")
        f.write(first + txt)
        f.seek(0)
        # print(repr((txt, enc, first)))
        assert detect_encoding(f.readline) == (enc, [])
        f.close()

    with py_open(__file__, "rb") as f:
        sample = f.readline()

    test('"""bla\n"""', "utf-8", sample)

# Generated at 2022-06-13 18:16:14.440134
# Unit test for function generate_tokens
def test_generate_tokens():
    import sys
    import tokenize
    f = tokenize.untokenize(tokenize.generate_tokens(open('/Users/robindo/Downloads/pyinstaller-develop/tests/test_tokenize/test_tokens.py').__next__))
    f = f.encode('utf-8')
    sys.stdout.buffer.write(f)
test_generate_tokens()


# Generated at 2022-06-13 18:16:21.485358
# Unit test for function detect_encoding
def test_detect_encoding():
    # First case: default return
    readline = iter(["# coding: iso-8859-15\n", "# vim: set fileencoding=latin-1 :\n"])
    encoding, _ = detect_encoding(readline.__next__)
    assert encoding == "iso-8859-15"

    # Second case: default return with BOM
    readline = iter([BOM_UTF8, "# vim: set fileencoding=latin-1 :\n"])
    encoding, _ = detect_encoding(readline.__next__)
    assert encoding == "utf-8-sig"

    # Third case: Try with mismatching encodings

# Generated at 2022-06-13 18:16:29.435022
# Unit test for function generate_tokens
def test_generate_tokens():
    # Class of token types, used with the tokenize() generator.
    class TokenType:
        INDENT, DEDENT, NEWLINE, NAME, NUMBER, STRING, OPEN_PAREN, CLOSE_PAREN, \
        ADD_EQUALS, EQUALS, CLOSE_BRACE, OPEN_BRACE, CLOSE_BRACKET, OPEN_BRACKET, \
        PRINT, COMMENT, NL, ENCODING, ENDMARKER, \
        OP = list(range(25))


# Generated at 2022-06-13 18:16:34.398377
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    u = Untokenizer()
    t = u.untokenize(tokenize(b"def f(): pass\n"))
    assert t == "def f():\n    pass\n", repr(t)
    t = u.untokenize(tokenize(b"def f(): pass\n", None))
    assert t == "def f (): pass\n", repr(t)
    t = u.untokenize(tokenize(b"def f(): pass\n", None))
    assert t == "def f (): pass\n", repr(t)



# Generated at 2022-06-13 18:16:46.105207
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b'# -*- coding: latin-1 -*-'

    encoding, lines = detect_encoding(readline)
    assert encoding == 'iso-8859-1'
    assert lines == [b'# -*- coding: latin-1 -*-']

    def readline():
        yield b'\xef\xbb\xbf'  # UTF-8 BOM
        yield b'# coding: ascii'

    encoding, lines = detect_encoding(readline)
    assert encoding == 'utf-8-sig'
    assert lines == [b'\xef\xbb\xbf', b'# coding: ascii']

    def readline():
        yield b'# -*- coding: utf-8 -*-'

# Generated at 2022-06-13 18:16:53.493312
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(seq):
        for line in seq:
            yield line + "\n"

    for (inp, expected) in (([], "utf-8"), (["a"], "utf-8"), ([b"a"], "utf-8")):
        actual = detect_encoding(readlines(inp))[0]
        if actual != expected:
            print(actual, expected)

    def readlines_crlf(seq):
        for line in seq:
            yield line + "\r\n"

    for (inp, expected) in (([], "utf-8"), (["a"], "utf-8")):
        actual = detect_encoding(readlines_crlf(inp))[0]
        if actual != expected:
            print(actual, expected)


# Generated at 2022-06-13 18:17:05.516543
# Unit test for function detect_encoding
def test_detect_encoding():
    from test import support

    def readline():
        yield b"# coding: latin-1\n"
        yield b"#blah blah\n"
        yield b"blah blah\n"
        yield b"# -*- coding: iso-latin-1 -*-\n"
        yield b"blah blah\n"
        yield b"\n"
        yield b"# coding=utf-8\n"
        yield b"\n"
        yield b"# coding=utf-8\n"
        yield b"# coding=utf8\n"

    encoding, lines = detect_encoding(readline)
    support.unlink(support.TESTFN)



# Generated at 2022-06-13 18:17:17.327240
# Unit test for function generate_tokens
def test_generate_tokens():
    import io, token

# Generated at 2022-06-13 18:17:28.452004
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import tokenize as tokenize_mod
    f = io.StringIO("def f(): pass")
    result = []
    tokenize_mod.tokenize_loop(f.readline, result.append)
    import pprint
    pprint.pprint(result)

# Generated at 2022-06-13 18:18:02.704963
# Unit test for function tokenize
def test_tokenize():
    import io

    readline = io.StringIO("if 1:\n  pass").readline
    tokens = []
    tokenize(readline, tokens.append)
    print(tokens)
    print(len(tokens))
    assert len(tokens) == 5



# Generated at 2022-06-13 18:18:08.928590
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:18:12.764223
# Unit test for function tokenize_loop
def test_tokenize_loop():
    # for testing
    import io
    import sys

    s = io.StringIO("def foo(x):\n  return 2*x")
    tokenize_loop(s.readline, printtoken)



# Generated at 2022-06-13 18:18:18.458012
# Unit test for function tokenize
def test_tokenize():
    # TODO: Use unittest; this is a very simplified test to make sure
    # tokenize continues to work after I made some changes.
    from io import StringIO

    input = "def f(x, y): return x + y"
    tokenize(StringIO(input).readline)



# Generated at 2022-06-13 18:18:27.703818
# Unit test for function tokenize
def test_tokenize():
    import io
    import token

    r = io.StringIO("def x(): pass\n")
    l = []
    g = generate_tokens(r.readline)
    tokenize(r.readline, l.append)
    assert g == l

    r = io.StringIO("#")
    l = []
    tokenize(r.readline, l.append)
    assert l == [
        (token.COMMENT, "#", (1, 0), (1, 1), "\n"),
        (token.ENDMARKER, "", (2, 0), (2, 0), "\n"),
    ]

    r = io.StringIO("def x(): pass\x04\n")
    l = []
    tokenize(r.readline, l.append)

# Generated at 2022-06-13 18:18:34.201543
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        if lines:
            return lines.pop(0)
        else:
            raise StopIteration()

    lines = [b'\xef\xbb\xbf## coding: latin-1\n']
    assert detect_encoding(readline) == ("iso-8859-1", [])

    lines = [b'\xef\xbb\xbf## coding=iso-8859-1\n']
    assert detect_encoding(readline) == ("iso-8859-1", [])

    lines = [b'## coding: iso-8859-1\n']
    assert detect_encoding(readline) == ("utf-8", [b'## coding: iso-8859-1\n'])


# Generated at 2022-06-13 18:18:42.703960
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        return next(lines)

    # Checks that calling detect_encoding with a readline that produces
    # lines, and that calling detect_encoding with a readline that produces
    # lines ending with '\r\n' gives the same results.

    lines = iter(
        [
            b'\xef\xbb\xbf# -*- coding: utf-8 -*-\n',
            b"\n",
        ]
    )
    assert detect_encoding(readline) == ("utf-8-sig", [b"\n"])



# Generated at 2022-06-13 18:18:51.628780
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import token
    import tokenize
    r = io.BytesIO(
        b"def foo(a, b):\n  print(a, b)\n    print(a, b)"
        b"\nprint(a, b)\n\ndef foo():\n  print(a, b)\n"
    )
    g = tokenize.generate_tokens(r.readline)
    for toknum, tokval, _, _, _ in g:
        print(
            "%10s %-14s %-20r %r"
            % (token.tok_name.get(toknum, toknum), toknum, tokval, tokval)
        )

    # This test case is based on Lib/test/tokenize_tests.txt

# Generated at 2022-06-13 18:19:02.357333
# Unit test for function detect_encoding
def test_detect_encoding():
    import sys

    from doctest import DocFileSuite
    from test import support
    from test.support import TESTFN

    PythonVerbose = sys.version_info[:2] < (3, 8)
    expected_output = (
        "utf-8-sig",
        [
            b"\xef\xbb\xbf# coding: utf-8-sig\n",
        ],
    )
    with open(TESTFN, "w") as f:
        f.write("# coding: utf-8-sig\n")
    with support.CheckSuccessfulCleanup(TESTFN) as file:
        with open(file, "rb") as f:
            d = detect_encoding(f.readline)

# Generated at 2022-06-13 18:19:11.799119
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        if test_data[0]:
            line = test_data[0][0]
            test_data[0] = test_data[0][1:]
            return bytes(line, "ascii")
        raise StopIteration


# Generated at 2022-06-13 18:19:50.435400
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# -*- coding: latin-1 -*-"
        yield b"blah blah"
        yield b"# -*- coding: ascii -*-"
        yield b"blah blah"
        yield b"# -*- coding: iso-latin-9 -*-"
        yield b"blah"
        yield b"# coding: utf-8"
        yield b"blah blah"
        yield b"# -*- coding: cp-1252 -*-"
        yield b"blah blah"
        yield b"# -*- coding: iso-8859-2 -*-"
        yield b"blah blah"
        yield b"# -*- coding: utf-8-sig -*-"
        yield b"blah blah"

# Generated at 2022-06-13 18:19:55.193903
# Unit test for function tokenize_loop
def test_tokenize_loop():
    lines = ["def f(x): return x+1"]
    def readline():
        return lines.pop(0)
    def check_token(type, token, start, end, line):
        assert (type, token) == _token_string_map[line[start[1] : end[1]]]
    tokenize_loop(readline, check_token)


# Generated at 2022-06-13 18:20:03.119865
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    from tokenize import tokenize
    r = io.StringIO("if 1:\n  pass\n")
    all_tokens = list(tokenize(r.readline))
    assert len(all_tokens) == 7
    assert all_tokens[0].type == 57  # 'if' keyword
    assert all_tokens[1].type == 57  # '1' integer literal
    assert all_tokens[2].type == 57  # ':' operator
    assert all_tokens[3].type == 4  # newline character
    assert all_tokens[4].type == 57  # 'pass' keyword
    assert all_tokens[5].type == 4  # newline character
    assert all_tokens[6].type == 0

# Generated at 2022-06-13 18:20:07.378147
# Unit test for function tokenize_loop
def test_tokenize_loop():
    """ Test for tokenize_loop() """
    result = []
    tokeneater = result.append
    # Test empty string
    tokenize_loop(iter([""]).__next__, tokeneater)
    assert result == []

    result = []
    tokeneater = result.append
    # Test a simple expression
    tokenize_loop(iter(["x=1 + 2"]).__next__, tokeneater)

# Generated at 2022-06-13 18:20:10.387207
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from io import StringIO
    s = StringIO("def f(x): return x + 2")
    tokenize_loop(s.readline, printtoken)



# Generated at 2022-06-13 18:20:22.491744
# Unit test for function generate_tokens
def test_generate_tokens():
    def illegaltoken():
        yield from generate_tokens('def f():\n s=')
    with expected_exception(TokenError, "EOF in multi-line statement"):
        next(illegaltoken())

    def incomplete_input():
        yield from generate_tokens('def f():\n')
    with expected_exception(IndentationError):
        next(incomplete_input())

    def incomplete_unbalanced():
        yield from generate_tokens('(\n')
    with expected_exception(TokenError, "EOF in multi-line statement"):
        next(incomplete_unbalanced())



# Generated at 2022-06-13 18:20:25.447568
# Unit test for function tokenize_loop
def test_tokenize_loop():
    # do nothing, but check the types are right
    tokenize_loop(lambda: "", lambda *args: None)



# Generated at 2022-06-13 18:20:30.796823
# Unit test for function generate_tokens
def test_generate_tokens():
    for filename in ["tokenize_tests.txt", "tokenize_tests2.txt"]:
        with tokenize.open(filename) as f:
            all_tokens = []
            tokens = tokenize.generate_tokens(f.readline)
            for token in tokens:
                token_type, token_string, (srow, scol), (erow, ecol), logical_lineno = token
                ttext = tokenize.tok_name.get(token_type)
                token_desc = '%s%s' % (ttext, (token_string and repr(token_string) or ''))
                all_tokens.append((srow, token_desc))

            # Handle case where we parse an encoding cookie

# Generated at 2022-06-13 18:20:42.755532
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    from io import StringIO
    s = StringIO("print(1+1)\n")
    toks = []
    tokenize_loop(s.readline, toks.append)
    assert toks[0] == (NAME, "print", (1, 0), (1, 5), "print(1+1)\n")
    assert toks[1] == (OP, "(", (1, 5), (1, 6), "print(1+1)\n")
    assert toks[2] == (NUMBER, "1", (1, 6), (1, 7), "print(1+1)\n")
    assert toks[3] == (OP, "+", (1, 7), (1, 8), "print(1+1)\n")

# Generated at 2022-06-13 18:20:46.354926
# Unit test for function generate_tokens
def test_generate_tokens():
    tokens = generate_tokens(open("./test_tokens.py").readline)
    for tok in tokens:
        print(tok)


test_generate_tokens()

# to generate tokens in a string, use  a lambda expression to create a callable object

# Generated at 2022-06-13 18:21:22.399578
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def tokenize_loop_1(readline, tokeneater):
        for token_info in generate_tokens(readline):
            tokeneater(*token_info)

    def readline():
        return 'print("foo") #this is a comment'

    def tokeneater(*args):
        print(args)

    tokenize_loop_1(readline, tokeneater)



# Generated at 2022-06-13 18:21:31.848022
# Unit test for function tokenize_loop
def test_tokenize_loop():
    global seen
    seen = []
    def test(readline, tokeneater):
        try:
            tokenize_loop(readline, tokeneater)
        except StopTokenizing:
            pass
    def readline():
        global lines
        if not lines:
            raise EOFError
        line = lines[0]
        lines = lines[1:]
        return line
    def tokeneater(*args):
        seen.append(args)
    lines = ["def f(x): return 2*x", ""]
    test(readline, tokeneater)

# Generated at 2022-06-13 18:21:40.880497
# Unit test for function detect_encoding
def test_detect_encoding():
    def get_readline(string):
        def readline():
            if not string:
                raise StopIteration
            line = string[0]
            del string[0]
            return line
        return readline
    def roundtrip(s, expected_encoding, expected_bom):
        readline = get_readline([s])
        encoding, bom = detect_encoding(readline)
        if bom != expected_bom:
            raise RuntimeError("Encoding detection failed on %a" % (s,))
        if encoding != expected_encoding:
            raise RuntimeError("Encoding detection failed on %a" % (s,))
    def roundtrip_blob(s, expected_encoding, expected_blob):
        readline = get_readline(s.split("\n"))
        encoding, blob = detect_

# Generated at 2022-06-13 18:21:54.131695
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b'\xef\xbb\xbf'
        yield b'# -*- coding: latin-1 -*-\n'
    result = detect_encoding(readline())
    assert result == ('iso-8859-1',
                      [b'\xef\xbb\xbf', b'# -*- coding: latin-1 -*-\n'])

    def readline():
        yield b'# coding=utf-8\n'
    result = detect_encoding(readline())
    assert result == ('utf-8', [b'# coding=utf-8\n'])

    def readline():
        yield b'\xef\xbb\xbf# coding=utf-8\n'
    result = detect_encoding(readline())

# Generated at 2022-06-13 18:22:02.123979
# Unit test for function generate_tokens
def test_generate_tokens():
    def _tst_generate_tokens(lines: List[str], expected: List[GoodTokenInfo]):
        lines = iter(lines)
        result = list(generate_tokens(lines.__next__))
        assert result == expected


# Generated at 2022-06-13 18:22:07.817823
# Unit test for function tokenize
def test_tokenize():
    import io
    import token

    r = io.StringIO("x = 5\n")
    l = []  # type: List[Tuple[int, Text, Coord, Coord, Text]]
    tokenize(r.readline, l.append)
    assert l == [(token.NAME, "x", (1, 0), (1, 1), "x = 5\n"),
                 (token.OP, "=", (1, 2), (1, 3), "x = 5\n"),
                 (token.NUMBER, "5", (1, 4), (1, 5), "x = 5\n"),
                 (token.NEWLINE, "\n", (1, 5), (1, 6), "x = 5\n")]



# Generated at 2022-06-13 18:22:14.022470
# Unit test for function generate_tokens
def test_generate_tokens():
    src = "a = (1, 2)\nb = [3, 4]\n"
    from io import StringIO
    import pprint

    f = StringIO(src)
    f.readline()
    pprint.pprint([tok for tok in generate_tokens(f.readline)])

    # Test non-UTF8 encoding and lines with leading whitespace
    src = "a = \"\\xe4\\xf6\\xfc\"\nb = [3, 4]\n    b2 = 5\n"
    f = StringIO(src)
    pprint.pprint([tok for tok in generate_tokens(f.readline)])


# Generated at 2022-06-13 18:22:18.920954
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for line in [
            b'\xef\xbb\xbf# coding: latin-1\n',
        ]:
            yield line
    r = detect_encoding(readline)
    assert r == ('iso-8859-1', [])

