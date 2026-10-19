

# Generated at 2022-06-13 18:14:33.441356
# Unit test for function tokenize_loop
def test_tokenize_loop():
    # test for basic non-comment tokens
    s = "'''hi'''  #  ''  ''  ''"
    l = s.split("\n")
    g = tokenize_loop(iter(l).__next__, printtoken)


# backwards compatible interface
generate_tokens = tokenize_loop



# Generated at 2022-06-13 18:14:39.967638
# Unit test for function generate_tokens
def test_generate_tokens():
    def check_token_stream(source, expected_tokens):
        import re
        assert len(source.splitlines()) == len(expected_tokens)
        pairs = zip(tokenize.generate_tokens(io.StringIO(source).readline), expected_tokens)
        for (token, (type_, string, (srow, scol), (erow, ecol), line)), (expected, expected_string) in pairs:
            assert token == type_ and string == expected_string, (
                "Got {}, {}, {}, {}, {}. Want {}, {}, _, _, _".format(
                    token, string, srow, scol, line, expected, expected_string))

# Generated at 2022-06-13 18:14:47.837994
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from . import tokenize

    u = Untokenizer()
    source = "class Klass:\n    pass\n"
    result = u.untokenize(tokenize.generate_tokens(source.encode().splitline))
    assert result == source

    source = r"class Klass:\n    def __init__(self):\n        pass\n"
    result = u.untokenize(tokenize.generate_tokens(source.encode().splitline))
    assert result == source

    source = r"class Klass:\n    pass"
    result = u.untokenize(tokenize.generate_tokens(source.encode().splitline))
    assert result == source



# Generated at 2022-06-13 18:14:57.590819
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    class CommentTokenizer:
        def tokenize(self, text):
            return [tok for tok in generate_tokens(StringIO(text).readline)
                    if tok[0] != tokenize.COMMENT]
    import unittest
    import io
    import tokenize
    class TestUntokenizer(unittest.TestCase):
        def test_untokenize_tokens(self):
            ut = Untokenizer()
            ut.tokens = [("COMMENT", "#test"), ("NL", "\n")]
            self.assertEqual(ut.untokenize([]), "#test\n")
        def test_optional_whitespace(self):
            ut = Untokenizer()

# Generated at 2022-06-13 18:15:09.773761
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from io import StringIO

    def compare(input, output, trace=None):
        input = iter(tokenize(StringIO(input).readline))
        output = output.split()
        try:
            for tok in output:
                compare(*tok)
        except AssertionError:
            if trace is None:
                raise
            else:
                trace(input, tok)

    cout = StringIO()
    cout.write("hi\n")
    cout.write("  there\n")
    cout.write("how\tare\tyou?\n")
    cout.write("\tI'm\tfine\n")
    cout.seek(0)
    data = cout.read()

    cin = StringIO(data)
    u = Untokenizer()

# Generated at 2022-06-13 18:15:19.460629
# Unit test for function tokenize
def test_tokenize():
    import io
    from tokenize import tokenize as tokenize_orig
    import token as tokenize_token

    def make_tokenize(code: str) -> Iterator[Tuple[int, str, Coord, Coord, Text]]:
        return generate_tokens(io.StringIO(code).readline)

    def tokeneater(*args: object) -> None:
        tokeneater.tokens.append(args)

    # Test Python's tokenize module
    # Test that empty file is handled properly
    tokeneater.tokens = []
    tokenize("".join(tokenize_orig(io.StringIO("").readline)))

# Generated at 2022-06-13 18:15:28.096792
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from typing import List
    from .tokenize import RBrace, LBrace, Name, NEWLINE, COMMENT, INDENT
    untokenizer = Untokenizer()
    actual = untokenizer.untokenize(
        [
            (RBrace, "}"),
            (LBrace, "{"),
            (Name, "foo"),
            (Name, "bar"),
            (NEWLINE, "\n"),
            (COMMENT, "# test comment"),
            (INDENT, "    "),
        ]
    )
    expected = "} {\n    foo bar\n    # test comment\n"
    assert actual == expected



# Generated at 2022-06-13 18:15:35.613590
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for line in source:
            yield line

    source = ["# -*- coding: latin-1 -*-\n", "a = 1\n"]
    res = detect_encoding(readline)
    assert res == ("iso-8859-1", ["# -*- coding: latin-1 -*-\n", "a = 1\n"])

    source = ["a = 1\n", "# -*- coding: latin-1 -*-\n"]
    res = detect_encoding(readline)
    assert res == ("utf-8", ["a = 1\n", "# -*- coding: latin-1 -*-\n"])

    source = [" # -*- coding: latin-1 -*-\n", "a = 1\n"]

# Generated at 2022-06-13 18:15:41.398554
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield '\xef\xbb\xbf# coding=utf-8\n'.encode("utf-8")
        yield '\r\n'.encode("latin-1")
        yield '\n'.encode("latin-1")
    encoding = 'utf-8-sig'
    lines = [
        '\xef\xbb\xbf# coding=utf-8\n'.encode("utf-8"),
        '\r\n'.encode("latin-1"),
        '\n'.encode("latin-1"),
    ]
    assert detect_encoding(readline) == (encoding, lines)
    def readline():
        yield '# coding=latin-1\n'.encode("latin-1")

# Generated at 2022-06-13 18:15:52.785752
# Unit test for function detect_encoding
def test_detect_encoding():
    # This could be moved to a module in the test suite, but the test
    # suite doesn't exist yet.
    import io

    def readline() -> bytes:
        return b"# coding: utf-8"

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"
    assert not lines

    def readline() -> bytes:
        return b"#!/usr/bin/python3\n# coding: utf-8"

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"
    assert lines == [b"#!/usr/bin/python3"]

    def readline() -> bytes:
        return b"\xff\xfe\x00\x00\x00\x00\x00\x00"

    encoding, lines = detect

# Generated at 2022-06-13 18:16:32.571284
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    from token import tok_name

    text = "def f(x): return 2*x\n"

    with io.StringIO(text) as lines:
        tokens = list(tokenize(lines.readline))

# Generated at 2022-06-13 18:16:44.487581
# Unit test for function tokenize
def test_tokenize():
    import unittest

    class TestCase(unittest.TestCase):
        def test_r(self):
            self.assertTrue(re.match(r"\w+", "a_b"))
            self.assertFalse(re.match(r"\w+", "--"))
            self.assertTrue(re.match(r"\W+", "--"))
            self.assertFalse(re.match(r"\W+", "a_b"))
            self.assertTrue(re.match(r"\d+", "2"))
            self.assertFalse(re.match(r"\d+", "__"))
            self.assertTrue(re.match(r"\D+", "__"))
            self.assertFalse(re.match(r"\D+", "2"))

    unittest.main()

# Generated at 2022-06-13 18:16:52.598625
# Unit test for function generate_tokens
def test_generate_tokens():
    def match(tokval, toktype, start, end, line):
        assert toksource(tok) == tokval
        if isinstance(toktype, tuple):
            assert tok.type in toktype
        else:
            assert tok.type == toktype
        assert tok.start == start
        assert tok.end == end
        assert tok.line == line

    def toksource(tok):
        return tok.string[tok.start[1] : tok.end[1]]

    def gen_tokens(s):
        for tok in generate_tokens(StringIO(s).readline):
            assert tok.start[0] == 1
            yield tok

    s = "def f(x, y): return min(x, y)\n"

# Generated at 2022-06-13 18:17:05.148702
# Unit test for function tokenize
def test_tokenize():
    import io
    import token
    from tokenize import generate_tokens
    from tokenize import untokenize
    data = b"def f(): a = 5+3\n"
    f = io.BytesIO(data)
    g = generate_tokens(f.readline)
    tokens = list(g)

# Generated at 2022-06-13 18:17:17.230632
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(sequence: Iterable[bytes]):
        for item in sequence:
            yield item

    assert detect_encoding(readlines([b'# -*- coding: latin-1 -*-']))[0] == "iso-8859-1"
    assert detect_encoding(readlines([b'# -*- coding: latin-1 -*-', b'']))[0] == "iso-8859-1"
    assert detect_encoding(readlines([b'']))[0] == "utf-8"
    assert detect_encoding(
        readlines([b'\xef\xbb\xbf# coding: latin-1'])
    )[0] == "utf-8-sig"

# Generated at 2022-06-13 18:17:26.702496
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    toklist = [
        (NAME, "func"),
        (OP, "("),
        (OP, ")"),
        (OP, ":"),
        (NEWLINE, "\n"),
        (INDENT, "\t"),
        (NAME, "pass"),
        (NEWLINE, "\n"),
        (DEDENT, ""),
        (ENDMARKER, ""),
    ]
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", "has become a reserved word")
        u = Untokenizer()
        s = u.compat(toklist[0], toklist[1:])
    assert s == "func():\n\tpass\n"



# Generated at 2022-06-13 18:17:35.051894
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    """
    This unit test is just to keep PyCharm happy
    """
    def assert_equal_with_printing(first, second):
        assert first == second
        if first != second:
            print("first = %r, second = %r" % (first, second))

    u = Untokenizer()
    result = u.compat((NAME, "if"), ((INDENT, "  "), (NAME, "a"), (DEDENT, "")))
    assert result is None
    assert_equal_with_printing(u.tokens, ['if ', '  a'])
    assert_equal_with_printing(u.prev_row, 1)
    assert_equal_with_printing(u.prev_col, 2)



# Generated at 2022-06-13 18:17:45.465125
# Unit test for function tokenize
def test_tokenize():
    import io
    import unittest.mock

    class ReadlineMock:
        def __init__(self, lines: List[Text]) -> None:
            self.lines = lines

        def __call__(self) -> Text:
            if len(self.lines) == 0:
                raise EOFError
            line = self.lines[0]
            self.lines = self.lines[1:]
            return line

    class TokenEaterMock(unittest.mock.Mock):
        pass


# Generated at 2022-06-13 18:17:52.716923
# Unit test for function generate_tokens
def test_generate_tokens():
    # Test bare "except:" and "except E, V:" clauses
    for s in [
        "try: pass\nexcept: pass\n",
        "try: pass\nexcept E, V: pass\n",
        "try: pass\nexcept (E1,E2): pass\n",
    ]:
        all_tokens = list(tokenize(s))
        assert all_tokens[-7][1] == "pass"  # tail end of input
    # Test "async def"
    stream = tokenize("async def foo(): pass")
    assert next(stream) == (ASYNC, "async", (1, 0), (1, 5), "async def foo(): pass")

# Generated at 2022-06-13 18:18:01.116238
# Unit test for function detect_encoding
def test_detect_encoding():

    def readline() -> bytes:
        if not lines:
            raise StopIteration
        return lines.pop(0)

    lines = [
        b"ham",
        b"# -*- coding: latin-1 -*-\n",
        b"spam\n",
        b"# vim:set fileencoding=utf-8 :\n",
        b"eggs\n",
        b"# -*- coding: unknown -*-\n",
        b"# -*- coding: iso-8859-15 -*-\n",
    ]
    print(detect_encoding(readline))

    lines.reverse()
    print(detect_encoding(readline))


# Generated at 2022-06-13 18:19:14.901871
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    s = "\n".join(
        [
            'def foo(bar):',
            '    if bar:',
            '        print("bar")',
            '    elif spam:',
            '        print("spam")',
            '    else:',
            '        print("else")',
        ]
    )
    assert Untokenizer().untokenize(generate_tokens(s)) == s



# Generated at 2022-06-13 18:19:22.987879
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def test_tokenize(s, expected):
        result = []
        tokenize_loop(s.splitlines().__iter__().__next__, result.append)
        assert result == expected, "%r != %r" % (result, expected)
    test_tokenize("", [])
    test_tokenize("\t  \n", [])
    test_tokenize("a", [
        (NAME, "a", (1, 0), (1, 1), "a")
    ])

# Generated at 2022-06-13 18:19:30.112009
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import tokenize
    mystr = b"def f():\n    pass\n\nx = 3"
    myf = io.BytesIO(mystr)
    tokens = list(tokenize.generate_tokens(myf.readline))

# Generated at 2022-06-13 18:19:37.299440
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    from tokenize import generate_tokens, tok_name
    for input in ("2+2", '"""a"""'):
        output = []
        for token in generate_tokens(StringIO(input).readline):
            output.append((tok_name[token[0]], token[1]))
        assert output == [("NUMBER", "2"), ("OP", "+"), ("NUMBER", "2")]


# Generated at 2022-06-13 18:19:49.020521
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield "\357\273\277# coding: ascii\n"
        yield "#!python\n"
        yield "\n"
        yield "a = 1\n"

    final_results = detect_encoding(readline())
    assert final_results == ("ascii", ["\n", "a = 1\n"])

    def readline():
        yield "#!python\n"
        yield "\n"
        yield "a = 1\n"

    final_results = detect_encoding(readline())
    assert final_results == ("utf-8", ["#!python\n", "\n", "a = 1\n"])

    def readline():
        yield "# -*- coding: latin-1 -*-\n"
        yield "\n"

# Generated at 2022-06-13 18:19:54.517366
# Unit test for function generate_tokens
def test_generate_tokens():
    def get_token_list(input_string):
        return list(generate_tokens(input_string.splitlines(1).__next__))

    assert get_token_list("") == [
        (3, "", (1, 0), (1, 0), ""),
        (0, "", (1, 0), (1, 0), ""),
    ]
    assert get_token_list("# test") == [
        (4, "# test", (1, 0), (1, 6), "# test"),
        (3, "", (1, 6), (1, 6), ""),
        (0, "", (1, 6), (1, 6), ""),
    ]

# Generated at 2022-06-13 18:20:00.806538
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    import test.support
    import io
    import tokenize

    with test.support.captured_stdout() as s:
        try:
            tokengen = tokenize.generate_tokens(test.support.findfile("tokenize_test.py"))
            Untokenizer().compat((NAME, "for"), tokengen)
        except tokenize.TokenError:
            pass
    result = s.getvalue()
    assert result == "def f(x):\n"



# Generated at 2022-06-13 18:20:11.439334
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    def untokcompat(s: str) -> str:
        u = Untokenizer()
        return u.compat(tokenize(s.splitlines(True)), iter([]))
    assert untokcompat("#foobar\n") == ""
    assert untokcompat("1\n") == "1 "
    assert untokcompat("12323\n") == "12323 "
    assert untokcompat("a\n") == "a "
    assert untokcompat("async\n") == "async "
    assert untokcompat("def\n") == ""
    assert untokcompat("\n") == ""
    assert untokcompat("\n\n") == ""
    assert untokcompat("  \n") == "  "

# Generated at 2022-06-13 18:20:23.517918
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    import tokenize

    def undo(tokens: Iterator[TokenInfo]) -> Text:
        io_obj = io.StringIO()
        tokenize.untokenize(tokens, io_obj.write)
        return io_obj.getvalue()

    assert undo(tokenize.generate_tokens(iter(["1"]).__next__)) == "1 "
    assert undo(tokenize.generate_tokens(iter(["1 + 1"]).__next__)) == "1 + 1 "

# Generated at 2022-06-13 18:20:26.620217
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    import io
    
    f = io.StringIO("def f():\n  print(1)\n")
    u = Untokenizer()
    it = tokenize(f.readline)
    it.next()
    u.compat(it.next(), it)
    assert u.untokenize([]).replace("\r\n", "\n") == "def f():\n  print 1\n"



# Generated at 2022-06-13 18:21:32.999427
# Unit test for function tokenize_loop
def test_tokenize_loop():
    global tokeneater
    tokeneater = printtoken
    tokenize_loop(readline, tokeneater)



# Generated at 2022-06-13 18:21:43.275478
# Unit test for function detect_encoding
def test_detect_encoding():
    def rl(s):
        for c in s:
            yield c
        raise StopIteration

    def readline():
        return next(rl_gen)

    def get_default_encoding():
        try:
            import locale
        except ImportError:
            return "ascii"
        encoding = locale.getpreferredencoding()
        if encoding.lower() == "utf-8":
            encoding = "utf_8"
        return encoding

    # Bug 776311
    rl_gen = rl("\xef\xbb\xbf")
    assert detect_encoding(readline)[0] == "utf-8-sig"

    # Test no encoding
    rl_gen = rl("")
    assert detect_encoding(readline)[0] == "utf-8"
    rl_

# Generated at 2022-06-13 18:21:58.235154
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import sys
    import unittest
    import tokenize

    class GCTest(unittest.TestCase):
        text = None

        def get_tokens(self, text, convert_char_literals=False):
            tokens = tokenize.generate_tokens(io.StringIO(text).readline)
            tokens = list(tokens)
            if convert_char_literals:
                tokens = [(t, v.replace("'", "")) for t, v, (srow, scol), (erow, ecol), l in tokens]
            return tokens

        def test_line_number(self):
            text = self.text
            tokens = self.get_tokens(text, convert_char_literals=True)

# Generated at 2022-06-13 18:22:00.586783
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    import io
    import tokenize
    u = tokenize.Untokenizer()

# Generated at 2022-06-13 18:22:03.659999
# Unit test for function tokenize
def test_tokenize():
    # Test helper function for tokenize.
    def showtokens(readline):
        tokenize(readline)

    #
    # Sample input
    #

# Generated at 2022-06-13 18:22:14.377961
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import BytesIO
    from tokenize import generate_tokens, tokenize
    from tokenize import NUMBER, STRING, NAME, OP

    # Test round-trip invariant
    text = b"1 + 1\n"
    f = BytesIO(text)
    gt = list(generate_tokens(f.readline))
    f = BytesIO(untokenize(gt))
    tt = list(tokenize(f.readline))
    assert gt == tt
    # Test line numbers
    text = b"1 + 1\n2 + 2\n"
    gt = generate_tokens(BytesIO(text).readline)
    gtt = next(gt)
    assert gtt[2][0] == 1
    assert gtt[3][0] == 1


# Generated at 2022-06-13 18:22:24.496384
# Unit test for function generate_tokens
def test_generate_tokens():
    for filename in ["tokenize_tests.txt"]:
        test_file = Path(_TOOLS).joinpath("lib2to3", filename)
        with test_file.open(encoding="utf-8") as f:
            encoding = "utf-8"
            source = f.read()
        source = source.replace("\r", "")  # strip DOS line endings
        lines = source.split("\n")
        source = "".join(line + "\n" for line in lines)