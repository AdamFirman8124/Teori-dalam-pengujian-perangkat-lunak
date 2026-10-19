

# Generated at 2022-06-13 18:14:39.122806
# Unit test for function generate_tokens
def test_generate_tokens():
    import keyword
    import token
    import tokenize
    r = tokenize.generate_tokens("if 1:\n  pass")
    alltokens = []
    for toknum, tokval, _, _, _ in r:
        alltokens.append((toknum, tokval))
    assert alltokens == [(token.NAME, "if"),
                         (token.NUMBER, "1"),
                         (token.OP, ":"),
                         (token.NEWLINE, "\n"),
                         (token.INDENT, "  "),
                         (token.NAME, "pass"),
                         (token.DEDENT, "")]

    r = tokenize.generate_tokens("if 1:\n  pass\n")
    alltokens = []

# Generated at 2022-06-13 18:14:44.637583
# Unit test for function generate_tokens
def test_generate_tokens():
    from tokenize import generate_tokens, untokenize, NUMBER, STRING, NAME, OP
    from io import BytesIO
    readline = BytesIO(b'if 1:\n print(2)\n').readline
    result = list(generate_tokens(readline))

# Generated at 2022-06-13 18:14:56.157922
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
    u = Untokenizer()
    u.prev_row = 1
    u.prev_col = 0
    u.add_whitespace((1, 0))
    assert u.tokens == []
    u.add_whitespace((1, 1))
    assert u.tokens == [" "]
    u = Untokenizer()
    u.prev_row = 1
    u.prev_col = 0
    u.add_whitespace((2, 0))
    assert u.tokens == ["\n"]
    u = Untokenizer()
    u.prev_row = 1
    u.prev_col = 0
    u.add_whitespace((2, 1))
    assert u.tokens == ["\n", " "]



# Generated at 2022-06-13 18:15:07.312554
# Unit test for function detect_encoding
def test_detect_encoding():
    class Reader:
        lines = (
            "",
            "  \t # -*- coding: iso-latin-1-unix -*-\r\n",
            "blahh",
        )

        def __call__(self):
            return self.lines.pop(0).encode("latin1")

    reader = Reader()
    encoding, lines = detect_encoding(reader)
    assert not lines
    assert encoding == "iso-8859-1"
    assert reader.lines == ["blahh"]

    reader = Reader()
    encoding, lines = detect_encoding(reader)
    assert lines == [b'blahh']
    assert encoding == "iso-8859-1"

    reader = Reader()
    reader.lines.pop()

# Generated at 2022-06-13 18:15:12.573691
# Unit test for function tokenize_loop
def test_tokenize_loop():
    global tabsize
    tabsize = 8
    f = open("tokenize_tests.txt")
    readline = f.readline
    readline.__module__ = "tokenize"  # kludge
    tokeneater = printtoken
    try:
        tokenize_loop(readline, tokeneater)
    except StopTokenizing:
        pass
    finally:
        f.close()



# Generated at 2022-06-13 18:15:14.835854
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    assert isinstance(Untokenizer().compat((1, "")), None)

# vim:ts=4:sw=4:et:

# Generated at 2022-06-13 18:15:22.096722
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    from token import tok_name
    prog = "def foo() :\n pass"
    f = io.StringIO(prog)
    for token in tokenize.generate_tokens(f.readline):
        print("%s\n" % tok_name[token[0]], end="")


if __name__ == "__main__":
    test_generate_tokens()

# Eventually, I'll cut and paste the rest in here...


# The following function was copied from the Python 3.5.1 standard library:
# tokenize.py
#     def tokenize_loop(
#         readline: Callable[[], Optional[str]],
#         tokeneater: Callable[..., None],
#         grammar: Optional[GrammarType] = None,
#

# Generated at 2022-06-13 18:15:30.492041
# Unit test for method add_whitespace of class Untokenizer

# Generated at 2022-06-13 18:15:42.042798
# Unit test for function generate_tokens
def test_generate_tokens():
    input_string = b'\nabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc\nabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc\nabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc\nabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc\n'
    output_string = ''
    output_string += b'\n'
    output

# Generated at 2022-06-13 18:15:45.911165
# Unit test for function generate_tokens
def test_generate_tokens():
    from token import tok_name

    src = "for i in range(10): print i\n"
    from io import StringIO
    from tokenize import generate_tokens
    gt = generate_tokens(StringIO(src).readline)
    for token in gt:
        print(tok_name[token[0]], token[1], token[2:])

# Generated at 2022-06-13 18:16:35.638147
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    def check(expected: str, input: Iterable[TokenInfo]) -> None:
        assert expected == Untokenizer().untokenize(input)

    check("", [])
    check("a + b", [(NAME, "a", (1, 0), (1, 1), "a"), (PLUS, "+", (1, 2), (1, 3), "+"), (NAME, "b", (1, 4), (1, 5), "b")])
    check("a + b", [(NAME, "a", (1, 0), (1, 1), "a"), (PLUS, "+", (1, 2), (1, 3), "+"), (NAME, "b", (1, 4), (1, 5), "b")])

# Generated at 2022-06-13 18:16:41.867933
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from io import StringIO
    s = "print(1)"
    contents = "".join(s)
    f = StringIO(contents)
    def readline():
        return f.readline()
    def tokeneater(*args):
        pass
    tokenize_loop(readline, tokeneater)
test_tokenize_loop.__test__ = False



# Generated at 2022-06-13 18:16:51.144746
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO
    from unittest import main, TestCase

    class TestCase(TestCase):
        def assertEqual(self, first, second):
            if first != second:
                raise AssertionError(f"{first} != {second}")

    class Test(TestCase):

        def validate_token_stream(self, token_stream: List[TokenInfo], expect: str) -> None:
            self.assertEqual(Untokenizer().compat(token_stream[0], iter(token_stream[1:])), expect)

        def test_compat(self):
            self.validate_token_stream([(NAME, "print"), (LPAR, "("), (NAME, "x"), (RPAR, ")")], "print( x )")

# Generated at 2022-06-13 18:17:05.056231
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(s):
        lines = s.splitlines(True)
        def readline():
            if lines:
                return lines.pop(0)
            else:
                raise StopIteration
        return readline
    def read_from_file(filename, s):
        f = open(filename, "wb")
        f.write(s)
        f.close()
        return readlines(slines)
    def test_file(filename, slines, expected_encoding, expected_first_line, reason):
        readline = read_from_file(filename, slines)
        encoding, lines = detect_encoding(readline)
        line = lines[0]
        if expected_encoding is None:
            assert encoding == "utf-8", reason
        else:
            assert encoding == expected_encoding, reason

# Generated at 2022-06-13 18:17:10.142032
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    r = io.StringIO("def foo(arg='foo'):\n return None")
    for token in generate_tokens(r.readline):
        print(token)

# Generated at 2022-06-13 18:17:20.412209
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import unittest

    # Issue 17650
    # This example is from the docstring of detect_encoding.
    s = u"\ufeffcoding=utf-8"
    with io.BytesIO(s.encode("utf-8")) as f:
        encoding, consumed = detect_encoding(f.readline)
        assert encoding == "utf-8-sig"
        assert consumed == [b"coding=utf-8"]

    # no BOM or encoding cookie
    s = u"""\
#!/usr/bin/env python
# -*- coding: utf-8 -*-
print('some string')
"""
    with io.BytesIO(s.encode("utf-8")) as f:
        encoding, consumed = detect_encoding(f.readline)

# Generated at 2022-06-13 18:17:28.173048
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    import io
    import tokenize as test_tokenize

    untokenize_compat = Untokenizer().compat

    u = Untokenizer()
    source = iter(
        test_tokenize.generate_tokens(
            io.BytesIO(b"def f():\n    pass\n").readline
        )
    )
    untokenize_compat(next(source), source)
    result = u.untokenize(iter([]))
    assert result == "def f():\n    pass\n"



# Generated at 2022-06-13 18:17:33.575600
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    class TestableUntokenizer(Untokenizer):

        def __init__(self):
            super().__init__()
            self.tokens = []
            self.prev_row = 1
            self.prev_col = 0

    ut = TestableUntokenizer()
    _i = [(1, "a"), (5, "b")]
    ut.compat((1, "a"), _i)
    assert ut.tokens == ["a "]



# Generated at 2022-06-13 18:17:38.936305
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    u = Untokenizer()
    u.compat((NAME, "one"), [(NUMBER, "1"), (NAME, "two"), (NUMBER, "2")])
    #print("".join(u.tokens))


# Generated at 2022-06-13 18:17:47.833508
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for line in (
            b'# -*- coding: latin-1-test -*-\n',
            b'#!/usr/bin/env python\n',
            b'# -*- coding: utf-8 -*-\n',
            b'# vim:fileencoding=latin-1\n',
            b'\xef\xbb\xbfimport sys\n',
            b'#!/usr/bin/env python\n',
            b'# -*- coding: iso-8859-1 -*-\n',
            b'# vim:fileencoding=ascii\n',
        ):
            yield line
    result = detect_encoding(readline)

# Generated at 2022-06-13 18:18:29.071437
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from io import BytesIO
    import token
    token_type = token.ENDMARKER
    token_string = ""
    start = (0, 0)
    end = (0, 0)
    line = ""

    def readline():
        return ""

    def tokeneater(token_type, token_string, start, end, line):
        # The first argument is an integer
        assert isinstance(token_type, int)
        # Check that token_type is an attribute of token module
        assert getattr(token, tok_name[token_type], None) is not None
        # token_string is a string
        assert isinstance(token_string, str)
        # start and end are both coordinates
        assert isinstance(start, tuple)
        assert len(start) == 2

# Generated at 2022-06-13 18:18:38.158929
# Unit test for function generate_tokens
def test_generate_tokens():
    import tokenize
    readline = tokenize.generate_tokens(open("/home/jukka/Dev/pypy/bin/pypy").readline)
    ln = 0
    for token in readline:
        if token[0] == tokenize.NL:
            ln += 1
        print(ln, token)
test_generate_tokens()


# Generated at 2022-06-13 18:18:44.925836
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# coding: latin-1\n"
        yield b"# foo\n"
        yield b"# coding: latin-1\n"
        yield b"# foo\n"
        yield b"# coding: latin-1\n"
        yield b"b'x'"
    try:
        detect_encoding(readline)
    except SyntaxError:
        assert True
    else:
        assert False



# Generated at 2022-06-13 18:18:50.230558
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import tokenize
    s = io.StringIO("def foo(): pass\n")
    # s2 = io.StringIO("def foo(): pass\n")  # TODO: add test for non-"\n" end-of-line
    tokenize.tokenize_loop(s.readline, printtoken)



# Generated at 2022-06-13 18:18:58.868939
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import unittest

    def _run_loop(raw, expected):
        tokens = []
        tokeneater = tokens.append
        tokenize_loop(iter(raw).__next__, tokeneater)
        # Strip the line numbers
        tokens = [(toktype,) + tuple(tok[1:]) for tok in tokens]
        self.assertEqual(tokens, expected)


# Generated at 2022-06-13 18:19:05.466020
# Unit test for function tokenize_loop
def test_tokenize_loop():
    s = "from math import *\n"
    from io import StringIO

    def readline():
        return s

    def tokeneater(type, token, start, end, line):
        print(
            "type",
            type,
            "token",
            token,
            "start",
            start,
            "end",
            end,
            "line",
            line,
        )

    tokenize_loop(readline, tokeneater)



# Generated at 2022-06-13 18:19:13.881427
# Unit test for function tokenize
def test_tokenize():
    import io
    r = io.StringIO("def f(x): return 2*x").readline
    l = []
    tokenize(r, l.append)

# Generated at 2022-06-13 18:19:20.624351
# Unit test for function generate_tokens
def test_generate_tokens():
    "Test the generate_tokens() generator."
    import re
    import token
    import io

    with open("tokenize_test.txt") as fp:
        fp = io.StringIO(fp.read())  # Work around missing non-ASCII chars

    type_map = {"'": token.STRING, '"': token.STRING, "`": token.STRING}

    # A map from token.NUMBER-type string to token.NUMBER (as well as
    # token.OP for those that should be token.OP-s).

# Generated at 2022-06-13 18:19:36.581602
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io

    s = io.StringIO("def f(x): return x+1")
    tokeater = cast(TokenEater, lambda t,v,s,e,l: print(t,v,s,e,l))
    tokenize_loop(s.readline, tokeater)
    # Expected output:
    # 1 def (1, 0) (1, 3) 'def f(x): return x+1'
    # 1 f (1, 4) (1, 5) 'def f(x): return x+1'
    # 53 ( (1, 5) (1, 6) 'def f(x): return x+1'
    # 1 x (1, 6) (1, 7) 'def f(x): return x+1'
    # 54 ) (1, 7) (1, 8)

# Generated at 2022-06-13 18:19:47.765047
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io, tokenize
    test_cases = (
        "a + b",
        "(a + b) / (c + d)",
        """a + b
+ c
+ d""",
        """# this is a comment
x = "hi"
# So is this
y = 'there'
""",
    )
    for test_case in test_cases:
        f = io.StringIO(test_case)
        expected_output = f.read()
        f = io.StringIO(test_case)
        untok = Untokenizer()
        tokens = tokenize.generate_tokens(f.readline)
        output = untok.untokenize(tokens)

# Generated at 2022-06-13 18:20:24.913848
# Unit test for function tokenize
def test_tokenize():
    from io import BytesIO
    from collections import namedtuple

    Token = namedtuple("Token", "type string start end line")

    # These tests don't check line number or start/end values.

    def check_tokenize(s, toks):
        toks = [Token(*t) for t in toks]
        toklist = list(generate_tokens(BytesIO(s.encode("utf-8")).readline))
        assert toks == toklist

    def check_tokenize_tabs(s, ts, toks):
        toks = [Token(*t) for t in toks]
        toklist = list(generate_tokens(BytesIO(s.encode("utf-8")).readline, ts))
        assert toks == toklist

    check_tokenize

# Generated at 2022-06-13 18:20:27.683215
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    unittest.TestCase.assertEqual(
        Untokenizer().compat(token.tokenize(StringIO('x=1 ').readline), token.tokenize),
        None,
    )


# Generated at 2022-06-13 18:20:28.798175
# Unit test for function tokenize_loop
def test_tokenize_loop():
    return tokenize



# Generated at 2022-06-13 18:20:40.743925
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import token
    import blib2to3.pygram as pygram
    import blib2to3.pytree as pytree
    from blib2to3.pgen2.tokenize import generate_tokens, COMMENT, ENDMARKER, NL
    # Test tokenize_loop()
    def _test_tokenize_loop(s, types):
        g = generate_tokens(io.StringIO(s).readline)
        toktype = token.tok_name[types[0]]
        tok = next(g)
        if toktype != tok[0]:
            raise ValueError("%s != %s" % (toktype, tok[0]))

# Generated at 2022-06-13 18:20:44.022336
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def readline():
        return 'a b c'

# Generated at 2022-06-13 18:20:50.567104
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        if not lines:
            raise StopIteration
        line = lines[0]
        del lines[0]
        return line

    lines = [b"# coding: latin-1\n"]
    assert detect_encoding(readline) == ("iso-8859-1", lines)
    lines = [b"#!/usr/bin/python\n", b"# coding: latin-1\n"]
    assert detect_encoding(readline) == ("iso-8859-1", lines)
    lines = [b"\xf7# coding: latin-1\n"]
    assert detect_encoding(readline) == ("utf-8", lines)
    lines = [b"#!/usr/bin/python\n", b"\xf7# coding: latin-1\n"]
   

# Generated at 2022-06-13 18:20:58.728441
# Unit test for function detect_encoding
def test_detect_encoding():
    from io import StringIO

    def readline(str):
        return StringIO(str).readline

    def check(expected, *args):
        assert expected == detect_encoding(readline(*args))

    check(("iso-8859-15", [b"# -*- coding: iso-8859-15 -*-\n"]),)

    check(
        ("iso-8859-15", [b"a = '\xfc'; print a\n"]),
        b"\xa4\xbc\xe4\xbb\x96\xa4\xba\xcc\x8c\xa4\xbf\xc6\x92\xa1\xa3",
    )


# Generated at 2022-06-13 18:21:04.395317
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for x in ["# coding: utf-8-sig", "# coding: utf-8"]:
            yield x

    first = readline()
    encoding, lines = detect_encoding(lambda: next(first))
    assert encoding == "utf-8-sig"



# Generated at 2022-06-13 18:21:15.827684
# Unit test for function detect_encoding
def test_detect_encoding():
    def make_readline(lines: bytes) -> Callable[[], bytes]:
        def readline() -> bytes:
            return lines.pop()

        return readline

    def testlines(lines: bytes) -> Tuple[str, List[bytes]]:
        return detect_encoding(make_readline(lines))

    # No encoding
    assert testlines([b"\x00"]) == ("utf-8", [b"\x00"])
    assert testlines([b"\x00"]) == ("utf-8", [b"\x00"])
    assert testlines([b"\x00"]) == ("utf-8", [b"\x00"])

    # Valid UTF-8 + BOM

# Generated at 2022-06-13 18:21:26.613774
# Unit test for function tokenize
def test_tokenize():
    def tokenize_lines():
        l = """
for i in range(10):
    print(i)
"""
        for t in tokenize(l.splitlines()):
            print(t)

    def tokenize_file():
        f = open("/tmp/t.py", "w")
        try:
            f.write("for i in range(10):\n    print(i)\n")
            f.close()
            f = open("/tmp/t.py", "r")
            try:
                tokenize_loop(f.readline, printtoken)
            finally:
                f.close()
        finally:
            os.unlink(f.name)

    tokenize_lines()
    print()
    tokenize_file()

