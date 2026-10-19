

# Generated at 2022-06-13 18:14:27.977083
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    t = Untokenizer()
    s = t.untokenize(
        [
            (1, "a"),
            (2, ","),
            (0, " "),
            (1, "b"),
            (2, ","),
            (0, "\n"),
            (2, "),\n"),
            (0, "  "),
            (3, "c"),
            (2, ","),
            (0, " "),
            (3, "d"),
        ]
    )
    assert s == "a , b ,\n),\n  c , d"



# Generated at 2022-06-13 18:14:30.151505
# Unit test for function tokenize
def test_tokenize():
    import io
    import token
    r = io.StringIO('print(1)\nprint(2)')
    for t in generate_tokens(r.readline):
        print(t)



# Generated at 2022-06-13 18:14:35.901880
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from test.test_tokenize import _TestTokenize
    from io import StringIO

    text = "the quick # comment\n"
    _TestTokenize.tokenize_loop(StringIO(text), _TestTokenize.tokeneater)
    text = "the quick\n# comment\n"
    _TestTokenize.tokenize_loop(StringIO(text), _TestTokenize.tokeneater)
    text = "the quick # comment"
    _TestTokenize.tokenize_loop(StringIO(text), _TestTokenize.tokeneater)



# Generated at 2022-06-13 18:14:42.170886
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import unittest


# Generated at 2022-06-13 18:14:47.176602
# Unit test for function tokenize
def test_tokenize():
    from io import StringIO

    def readline():
        return next(input)

    def tokeneater(type, token, xxx_todo_changeme2, xxx_todo_changeme3, line):
        (srow, scol) = xxx_todo_changeme2
        (erow, ecol) = xxx_todo_changeme3
        assert line == input.text
        assert input.pos == ecol, "pos = %d, ecol = %d" % (input.pos, ecol)
        input.pos = erow, ecol  # update position so it is equal to erow and ecol

# Generated at 2022-06-13 18:14:57.393763
# Unit test for function generate_tokens
def test_generate_tokens():
    import token
    import io
    import tokenize

    # For the tokenize module and Python version compatibiliy, the
    # full grammar is loaded.
    g = GATHER_GRAMMAR if python_version < 3.7 else FULL_GRAMMAR
    result = list(tokenize.generate_tokens(generate_tokens, g))
    expected = [
        (token.NUMBER, "7", (0, 0), (0, 1), "7"),
        (token.STRING, "foobar", (0, 2), (0, 8), "foobar"),
        (token.CHARACTER, "a", (0, 9), (0, 10), "a"),
        (token.NAME, "cat", (0, 11), (0, 14), "cat"),
    ]
    assert result == expected



# Generated at 2022-06-13 18:15:04.414715
# Unit test for function generate_tokens
def test_generate_tokens():
    def _test(input : str, expected : List[TokenInfo]) -> None:
        # _test, given a string and a list of tokens, breaks the string
        # in lines and generates the tokens from it.
        readline = iter(input.splitlines(True)).next
        result = list(generate_tokens(readline))
        _multiline_compare(result, expected)

# Generated at 2022-06-13 18:15:11.695348
# Unit test for function detect_encoding
def test_detect_encoding():

    def readline():
        yield b"s"
        yield b"#coding=utf-8\n"
        yield b""

    assert detect_encoding(readline) == ("utf-8", [b"s", b"#coding=utf-8\n"])

    def readline():
        yield b"s"
        yield b"#coding=utf-8\n"
        yield b"\xE7"
        yield b"#coding=iso-8859-1\n"
        yield b"\xE7"
        yield b""

    assert detect_encoding(readline) == (
        "utf-8",
        [b"s", b"#coding=utf-8\n", b"\xE7"],
    )


# Generated at 2022-06-13 18:15:17.217589
# Unit test for function generate_tokens
def test_generate_tokens():
    # Read input as byte stream, to avoid encoding issues.
    with open("test/data/tokenize_tests.txt", "rb") as fp:
        pairs = [(bytes(token), bytes(expect)) for (token, expect) in read_tests(fp)]

    # Test with and without the 'utf_8' encoding cookie.
    for encoding in "utf_8", "ascii":
        for (token, expect) in pairs:
            if encoding:
                token = b"# coding: " + encoding + b"\n" + token
            result = []

# Generated at 2022-06-13 18:15:31.837030
# Unit test for function generate_tokens
def test_generate_tokens():
    def lst2str(lst):
        return "".join(lst).replace(" ", "")

    def tokenize(input):
        tokens = generate_tokens(iter(input.splitlines(True)).__next__)
        return lst2str([token[1] for token in tokens])

    assert tokenize("x = 1\n") == "[NAME='x'][OP='='][NUMBER='1'][NEWLINE='']"
    assert (
        tokenize("if 1: # comment\n    x = 2\n")
        == "[NAME='if'][NUMBER='1'][OP=':'][NEWLINE=''][INDENT=''][NAME='x'][OP='=']"
        "[NUMBER='2'][NEWLINE=''][DEDENT='']"
    )

# Generated at 2022-06-13 18:15:59.113092
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
    untok = Untokenizer()
    untok.prev_row = 1
    untok.prev_col = 1
    untok.add_whitespace((2, 10))
    assert untok.tokens == [" " * 9]
    untok.add_whitespace((1, 10))
    assert untok.tokens == [" " * 9]
    untok.add_whitespace((1, 9))
    assert untok.tokens == [" " * 9]
    untok.add_whitespace((1, 8))
    assert untok.tokens == [" " * 9]
    untok.add_whitespace((1, 7))
    assert untok.tokens == [" " * 9]
    untok.add_whitespace((1, 6))

# Generated at 2022-06-13 18:16:07.748182
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(lines):
        def read():
            return lines.pop(0)
        return read

    def test(name, inp, expect):
        inp = inp.replace("\n", "\r\n")
        inp = inp.encode("utf-8")
        inp = inp.split(b"\r\n")
        encoding, lines = detect_encoding(readlines(inp))
        assert encoding == expect, "for '%s', got %s, expected %s" % (
            name,
            encoding,
            expect,
        )

    test("blank", "", "utf-8")
    test("spaces", "    ", "utf-8")
    test("ascii", "# coding: ascii", "ascii")

# Generated at 2022-06-13 18:16:12.813174
# Unit test for function generate_tokens
def test_generate_tokens():
    import tokenize
    from io import StringIO
    gt = generate_tokens(StringIO("def foo(): pass\n").readline)
    assert next(gt) == tokenize.tokenize(StringIO("def foo(): pass\n").readline)[0]

# Generated at 2022-06-13 18:16:16.398501
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO

    r = StringIO("1+1\n")
    for tok in tokenize.generate_tokens(r.readline):
        print(tok)


# Generated at 2022-06-13 18:16:22.348985
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    def _fails(src, msg):
        try:
            untokenize(src)
        except ValueError as e:
            if str(e) != msg:
                raise Exception(
                    f"Expected {repr(msg)}, got {repr(e)}") from e
        else:
            raise Exception(f"Expected ValueError({repr(msg)}), got no exception")
    def _check(src, expected):
        actual = untokenize(src)
        if actual != expected:
            raise Exception(
                f"Expected {repr(expected)}, got {repr(actual)}")

# Generated at 2022-06-13 18:16:30.155138
# Unit test for function generate_tokens
def test_generate_tokens():
    tests = [" ", "\t", "\\\n", "\\\r\n", "#"]
    for t in tests:
        print(t)
        print(list(generate_tokens(iter([t]).__next__)))
test_generate_tokens()

tests = [" ", "\t", "\\\n", "\\\r\n", "#"]
for t in tests:
    print(t)
    print(list(generate_tokens(iter([t]).__next__)))

print(list(generate_tokens(iter(["a=1\n"]).__next__)))
 

tests = "while 1: pass"
print(list(generate_tokens(iter([tests]).__next__)))

tests = "# Comment\nwhile 1: pass"

# Generated at 2022-06-13 18:16:39.262280
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    toks = [
        (NUMBER, "1", (1, 0), (1, 1), "1"),
        (NAME, "a", (1, 0), (1, 1), "a"),
        (NAME, "b", (1, 0), (1, 1), "b"),
        (NUMBER, "2", (1, 0), (1, 1), "2"),
    ]
    u = Untokenizer()
    result = u.compat(toks[0], iter(toks[1:]))
    assert result is None, repr(result)
    assert u.tokens == [
        "1 ",
        "a ",
        "b ",
        "2 ",
    ], repr(u.tokens)

# Generated at 2022-06-13 18:16:46.818799
# Unit test for function tokenize
def test_tokenize():
    from test.test_tokenize import rl, tokeneater

    tokenize(rl, tokeneater)
    #    for type, token, (srow, scol), (erow, ecol), line in generate_tokens(rl):
    #        print "%d,%d-%d,%d:\t%s\t%s" % (srow, scol, erow, ecol,
    #            tok_name[type], repr(token))



# Generated at 2022-06-13 18:16:53.841802
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import tokenize
    import unittest

    def ws(text):
        return "".join([x + "\n" for x in text.split("\n")])

    def t(t1, t2):
        return t1[:2] == t2[:2]

    class Test(unittest.TestCase):
        def testBasic(self):
            gt = tokenize.generate_tokens(io.StringIO("def f(x): return x**2").readline)
            self.assertTrue(t(next(gt), (tokenize.NAME, "def", 1, 0)))
            self.assertTrue(t(next(gt), (tokenize.NAME, "f", 1, 4)))

# Generated at 2022-06-13 18:17:00.106223
# Unit test for function generate_tokens
def test_generate_tokens():
    import io, token
    input = "def f(x): return 2*x"
    generator = tokenize.generate_tokens(io.StringIO(input).readline)
    tokens = list(generator)
    for token in tokens:
        print(token)

test_generate_tokens()


# Generated at 2022-06-13 18:19:00.579619
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(s: Text) -> Iterator[bytes]:
        size = len(s)
        i = 0
        while i < size:
            j = s.find("\n", i)
            if j < 0:
                j = size
            yield s[i : j + 1].encode("utf-8")
            i = j + 1


# Generated at 2022-06-13 18:19:10.593676
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for line in (b'\xef\xbb\xbf# coding=utf-8', b'# coding=latin-1', b'# blah blah blah', u'föö'.encode('utf-8')):
            yield line
    encoding, consumed = detect_encoding(readline().__next__)
    assert encoding == 'utf-8'
    assert consumed == [b'\xef\xbb\xbf# coding=utf-8', b'# blah blah blah']
    encoding, consumed = detect_encoding(readline().__next__)
    assert encoding == 'iso-8859-1'
    assert consumed == [b'# coding=latin-1', b'# blah blah blah']
    encoding, consumed = detect_encoding(readline().__next__)
    assert encoding

# Generated at 2022-06-13 18:19:20.512549
# Unit test for function detect_encoding
def test_detect_encoding():
    pass
#     def readline():
#         yield b'# -*- coding: latin-1 -*-\n'
#         yield b''
#     assert detect_encoding(readline) == ('iso-8859-1', [b'# -*- coding: latin-1 -*-\n'])
#     def readline():
#         yield b'\xef\xbb\xbf# coding: latin-1\n'
#         yield b''
#     assert detect_encoding(readline) == ('iso-8859-1', [b'# coding: latin-1\n'])
#     def readline():
#         yield b'# coding: latin-1\n'
#         yield b''
#     assert detect_encoding(readline) == ('utf-8', [

# Generated at 2022-06-13 18:19:36.507452
# Unit test for function generate_tokens
def test_generate_tokens():
    from tokenize import tokenize


# Generated at 2022-06-13 18:19:47.723896
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import functools

    def make_readline(
        lines: List[List[bytes]], errors: str = "strict"
    ) -> Callable[[], bytes]:
        def readline() -> bytes:
            return lines.pop(0)

        return readline

    def readlines(
        lines: List[List[bytes]], errors: str = "strict"
    ) -> Tuple[str, List[bytes]]:
        readline = make_readline(lines)
        return detect_encoding(readline)

    # No encoding
    assert detect_encoding(make_readline([[b"hello"]])) == ("utf-8", [])
    assert detect_encoding(make_readline([[b"hello"], []])) == ("utf-8", [])
    assert detect_enc

# Generated at 2022-06-13 18:19:57.200893
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline1() -> bytes:
        return b"peter was a sailor\n"

    def readline2() -> bytes:
        def gen() -> Iterator[bytes]:
            yield b"peter was a sailor\n"
            yield b"\n"
            yield b"peter piper picked a peck of pickled peppers\n"

        return gen()

    def readline3() -> bytes:
        def gen() -> Iterator[bytes]:
            yield b"# -*- coding: iso-8859-1 -*-\n"
            yield b"peter piper picked a peck of pickled peppers\n"

        return gen()


# Generated at 2022-06-13 18:19:59.806070
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    t = Untokenizer()
    t.compat((NAME, "x"), [(NAME, "="), (NUMBER, "2")])
    assert t.tokens == ["x = 2 "]

# Backwards compatible interface

# Generated at 2022-06-13 18:20:05.857992
# Unit test for function generate_tokens
def test_generate_tokens():
    import doctest
    import tokenize
    import io
    import unittest

    class TestGenerateTokens(unittest.TestCase):
        def test_tabsize(self):
            readline = io.StringIO("\t0123456789").readline
            tokens = list(tokenize.generate_tokens(readline))
            self.assertEqual(tokens[0], (tokenize.ERRORTOKEN, "\t", (1, 0), (1, 1), "\t0123456789"))


# Generated at 2022-06-13 18:20:15.378724
# Unit test for function detect_encoding
def test_detect_encoding():
    def tokenize_lines(lines):
        for line in lines:
            yield line
            yield "\n"

    def readline():
        return next(lines)

    def readlines():
        yield readline()
        for line in lines:
            yield line
        return


# Generated at 2022-06-13 18:20:27.913979
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# coding: latin-1\n"
        yield b"pass\n"

    assert detect_encoding(readline) == ("iso-8859-1", [b"# coding: latin-1\n"])

    def readline():
        yield b"# <?php\n"
        yield b"# coding: latin-1\n"
        yield b"pass\n"

    assert detect_encoding(readline) == ("iso-8859-1", [b"# <?php\n", b"# coding: latin-1\n"])

    def readline():
        yield b"# coding=latin-1\n"
        yield b"pass\n"


# Generated at 2022-06-13 18:21:08.950606
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def readline():
        for line in ['abc', '  def  ', 'ghi', '', 'jkl', ' ', '\t']:
            yield line
    tokens = []
    def tokeneater(*args):
        tokens.append(args)
    tokenize_loop(readline(), tokeneater)

# Generated at 2022-06-13 18:21:15.617634
# Unit test for function tokenize_loop
def test_tokenize_loop():
    data = "a = 5\nb = 6\n"
    result = []
    def tokeneater(*args):
        result.append(args)
    tokenize_loop(data.splitlines().__iter__().__next__, tokeneater)
    print(result)
test_tokenize_loop()



# Generated at 2022-06-13 18:21:23.124590
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    untok = Untokenizer()
    assert untok.compat((NAME, "for")) == None
    assert untok.compat((NUMBER, "2")) == None
    assert untok.compat((NL, "")) == None
    assert untok.compat((NEWLINE, "")) == None
    assert untok.compat((INDENT, "")) == None
    assert untok.compat((DEDENT, "")) == None
    assert untok.compat((ASYNC, "async")) == None
    assert untok.compat((AWAIT, "await")) == None

# End of unit test



# Generated at 2022-06-13 18:21:29.234608
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import sys

    # Test with a module that imports itself
    with io.StringIO() as sys.stdout:
        tokenize_loop(iter(["import tokenize_loop"]).__next__, printtoken)
        text_result = sys.stdout.getvalue()
        print(text_result)
        assert (
            text_result
            == "1,0-1,24:\tNAME\t'import'\n1,25-1,37:\tNAME\t'tokenize_loop'\n"
        )



# Generated at 2022-06-13 18:21:38.898667
# Unit test for function tokenize
def test_tokenize():
    from io import StringIO
    from unittest import TestCase

    class Test(TestCase):
        def check_tokenize(self, input, tokenslist):
            self.tokens = []

            def tokeneater(type, token, start, end, line):
                self.tokens.append((type, token, start, end, line))

            tokenize(StringIO(input).readline, tokeneater)
            self.assertEqual(self.tokens, tokenslist)


# Generated at 2022-06-13 18:21:44.245828
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    u = Untokenizer()
    input = [(0, 'foo'), (1, '+'), (0, 'bar'), (4, '\n'), (0, 'baz'), (1, '=')]
    output = u.compat((0, 'foo'), iter(input))
    assert u.tokens == ['foo ', '+', ' bar', '\n', 'baz ', '=']
    assert output is None


# Generated at 2022-06-13 18:21:58.800997
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import unittest
    import unittest.mock as mock

    # Test line end
    class TestTokenizeLoop(unittest.TestCase):
        def setUp(self):
            self.mock_readline = mock.Mock()
            self.expected_tokens = []
            self.expected_line = []
            self.mock_tokeneater = lambda type, token, xxx_todo_changeme, xxx_todo_changeme1, line: self.check_token(
                type, token, xxx_todo_changeme, xxx_todo_changeme1, line
            )


# Generated at 2022-06-13 18:22:10.280463
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield BOM_UTF8
        yield b"# -*- coding: latin-1 -*-\r\n"
        yield b"print('This is some Latin-1 text');\n"
    encoding, lines = detect_encoding(readline())
    assert encoding == "latin-1"
    assert lines == [
        BOM_UTF8 + b"# -*- coding: latin-1 -*-\r\n",
        b"print('This is some Latin-1 text');\n",
    ]

    def readline():
        yield b"# -*- coding: latin-1 -*-\r\n"
        yield BOM_UTF8
        yield b"print('This is some Latin-1 text');\n"

# Generated at 2022-06-13 18:22:23.234975
# Unit test for function detect_encoding
def test_detect_encoding():
    import tempfile
    import os
    import io

    def test(encoding: str, first: str, second: str, expect: Text) -> None:
        f = io.BytesIO(first.encode(encoding) + second.encode("ascii"))
        (found, _) = detect_encoding(f.readline)
        assert found == expect
        assert f.read()

    test("ascii", "", "# coding: latin-1\n", "latin-1")
    test("ascii", "", "# -*- coding: iso-latin-9 -*-\n", "iso-8859-15")
    test("ascii", "", "# coding=utf-8\n", "utf-8")