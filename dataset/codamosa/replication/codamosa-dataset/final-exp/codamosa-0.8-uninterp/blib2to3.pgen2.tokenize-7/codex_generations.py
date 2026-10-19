

# Generated at 2022-06-13 18:15:09.343609
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    rl = iter([
        'token_info[0]\n',
        'token_info[1]\n',
        'token_info[2]\n',
        'token_info[3]\n',
        'token_info[4]\n',
        'token_info[5]\n',
        'token_info[6]\n',
    ]).__next__
    tokeneater = io.StringIO()
    tokenize_loop(rl, tokeneater.write)
    result = tokeneater.getvalue()

# Generated at 2022-06-13 18:15:15.205537
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        return next(lines)

    def readline_generator(
        lines_in: Iterable[bytes]
    ) -> Iterable[Callable[[], bytes]]:
        def readline() -> bytes:
            return next(lines_in)

        return readline

    lines_1 = [
        b"# coding=ascii\n",
        b"@\n",
        b"\n",
        b"def f():\n",
    ]
    lines_2 = [
        b"# coding=ascii\n",
        b"@\n",
        b"def f():\n",
    ]

# Generated at 2022-06-13 18:15:17.776559
# Unit test for function tokenize_loop
def test_tokenize_loop():
    tokenize_loop(iter(['a']).__next__, printtoken)
    # <BLANKLINE>
    # 1,0-1,1:    NAME    'a'



# Generated at 2022-06-13 18:15:22.846424
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    u = Untokenizer()
    assert u.untokenize([("a", "b")]) == "ab"
    assert u.untokenize([("a", "b"), ("NL", ""), ("c", "d")]) == "ab\nd"
    assert u.untokenize([("a", "b"), ("NL", ""), ("c", "d"), ("NL", "")]) == "ab\nd\n"
    assert u.untokenize([("a", "b"), ("NL", ""), ("c", "d"), ("NL", ""), ("e", "f")]) == "ab\nd\nf"
    # XXX test indents



# Generated at 2022-06-13 18:15:28.905922
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io

    test_cases = ["abc def\n"]

    for test_case in test_cases:
        readline = io.StringIO(test_case).readline
        for token_info in generate_tokens(readline):
            printtoken(*token_info)



# Generated at 2022-06-13 18:15:36.212153
# Unit test for function generate_tokens
def test_generate_tokens():
    from pygments.token import Token
    from pygments.token import *  # NOQA

    def test(s):
        print("Testing:", s)
        for tok in generate_tokens(iter(s.splitlines()).__next__):
            print(tok)

    # See http://www.python.org/doc/2.6/lib/node16.html#l2h-289

# Generated at 2022-06-13 18:15:41.946987
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline(b: bytes) -> Iterator[bytes]:
        for c in b.splitlines(True):
            yield c

    def read_or_stop(b: bytes) -> Iterator[bytes]:
        for c in b.splitlines(True):
            yield c
        raise StopIteration()

    assert detect_encoding(readline(b"# coding=utf-8\n")) == ("utf-8", [b"# coding=utf-8\n"])
    assert detect_encoding(readline(b"\xef\xbb\xbf# coding=utf-8\n")) == (
        "utf-8-sig",
        [b"# coding=utf-8\n"],
    )

# Generated at 2022-06-13 18:15:53.167509
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield lines.pop(0)

    # No encoding
    lines = [b"# -*- coding: latin-1 -*-\n"]
    assert detect_encoding(readline) == ("latin-1", lines)

    # With encoding
    lines = [b"# -*- coding: latin-1 -*-\n"]
    assert detect_encoding(readline) == ("latin-1", lines)

    # With BOM
    lines = [b"\xef\xbb\xbf# -*- coding: latin-1 -*-\n"]
    assert detect_encoding(readline) == ("utf-8-sig", lines)

    # With BOM and encoding

# Generated at 2022-06-13 18:15:56.084304
# Unit test for function generate_tokens
def test_generate_tokens():
    import re
    from io import StringIO
    from token import tokens
    # Test a variety of different tokens.

# Generated at 2022-06-13 18:16:02.082876
# Unit test for function tokenize
def test_tokenize():
    import io
    import token
    import tokenize

    class Readline:
        def __init__(self, lines):
            self.lines = io.StringIO(lines)
        def __call__(self):
            return self.lines.readline()

    def tokenize_print(type, token, start, end, line):
        print("%d,%d-%d,%d:\t%s\t%s" % (start + (token,)))

    tokenize.tokenize(Readline("def f(x): return 2*x\n"), tokenize_print)



# Generated at 2022-06-13 18:17:03.971548
# Unit test for function tokenize
def test_tokenize():
    import io
    import tokenize

    r = io.StringIO("1 + 1\n")
    tokenize.tokenize(r.readline)
    r = io.StringIO("a = 3 + 5\n")
    tokenize.tokenize(r.readline)
    r = io.StringIO("def f(x):\n  return x + 6\n\nf(1)\n")
    tokenize.tokenize(r.readline)



# Generated at 2022-06-13 18:17:09.552046
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():

    class C:
        def method(self):
            return "foo"

    unt = Untokenizer()

# Generated at 2022-06-13 18:17:19.792425
# Unit test for function detect_encoding
def test_detect_encoding():
    from tokenize import detect_encoding

    def read_or_stop(lines: List[bytes]) -> Callable[[], bytes]:
        def readline() -> bytes:
            try:
                return lines.pop(0)
            except IndexError:
                raise StopIteration

        return readline

    def check(lines: List[bytes], expected: str) -> None:
        lines = [l.encode("utf-8") for l in lines]
        encoding, _ = detect_encoding(read_or_stop(lines))
        if encoding != expected:
            raise AssertionError(
                f"{lines} results in {encoding}, expected {expected}"
            )

    # No encoding
    check([], "utf-8")
    check(["#!"], "utf-8")

    # ASCII default

# Generated at 2022-06-13 18:17:24.633750
# Unit test for function tokenize_loop
def test_tokenize_loop():
    text = "Go!\n"
    tokens = []
    tokeneater = lambda ttype, token, *args: tokens.append((ttype, token))
    tokenize_loop(iter(text).__next__, tokeneater)
    assert tokens == [(ENCODING, None), (NL, "\n"), (NAME, "Go"), (NEWLINE, "\n")]



# Generated at 2022-06-13 18:17:34.606929
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO
    from blib2to3.pgen2.tokenize import (
        untokenize,
        INDENT,
        NUMBER,
        DEDENT,
        ENDMARKER,
        NAME,
        ASYNC,
        AWAIT,
        NL,
    )

    def untokenize_compat(iterable):
        c = untokenize._Untokenizer()
        outstream = StringIO()
        c.compile = outstream.write
        out = []
        for item in iterable:
            if item[0] is ENDMARKER:
                break
            out.append(item)
        c.compat(out[0], out[1:])
        return outstream.getvalue()


# Generated at 2022-06-13 18:17:45.399355
# Unit test for function generate_tokens
def test_generate_tokens():
    def _test_generate_tokens(input, expected):
        # Python 3.7+ has the function `async_generator_asend` that is always
        # in the __all__, but is only valid syntax for 3.7+
        # In 3.6, this would always produce an error token
        if version_info < (3, 7):
            expected = [
                tok for tok in expected if not isinstance(tok[1], AsyncToken)
            ]
        actual = list(tokenize(io.StringIO(input).readline))
        assert actual == expected


# Generated at 2022-06-13 18:17:51.932822
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO

    with StringIO("for i in range(10): print(i)") as f:
        tokens = list(generate_tokens(f.readline))

    token_types = [token[0] for token in tokens]
    assert token_types == [
        NAME,
        NAME,
        NAME,
        LPAR,
        NUMBER,
        RPAR,
        COLON,
        NAME,
        LPAR,
        NAME,
        RPAR,
        NEWLINE,
        INDENT,
        NAME,
        LPAR,
        NAME,
        RPAR,
        NEWLINE,
        DEDENT,
        ENDMARKER,
    ]



# Generated at 2022-06-13 18:18:01.214035
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import tokenize
    for filename in ["test_tokenize.txt", "test_tokenize2.txt"]:
        with io.StringIO() as bytes_content:
            with open(filename, "rb") as f:
                bytes_content.write(f.read().decode('utf-8'))
            bytes_content.seek(0)
            print("# Test tokenizing %s" % filename)
            tokengen = tokenize.generate_tokens(bytes_content.readline)
            for tokentype, token, start, end, line in tokengen:
                print("%10s %-14r %r" % (
                    tokenize.tok_name.get(tokentype, tokentype),
                    token,
                    (start, end)
                ))


# Generated at 2022-06-13 18:18:10.836713
# Unit test for method untokenize of class Untokenizer

# Generated at 2022-06-13 18:18:20.368059
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    u = Untokenizer()
    assert u.untokenize([(3, "x")]) == "x"
    assert u.untokenize([(1, "abc"), (3, "x")]) == "abc x"
    assert u.untokenize([(0, "abc"), (1, "def"), (4, "ghi"), (0, "jkl")]) == "abcdef ghi jkl"
    assert u.untokenize([(2, "def"), (0, "ghi")]) == "def ghi"
    assert u.untokenize([(0, "test"), (0, "test"), (1, "test"), (0, "test")]) == "testtest test test"

    # Test handling of simple string literals

# Generated at 2022-06-13 18:19:25.312930
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        if readline.lines:
            return readline.lines.pop(0)
        raise StopIteration

    readline.lines = []

    # no encoding
    readline.lines = ["#! /usr/bin/env python", "", "x = 'foo'"]
    assert detect_encoding(readline) == ("utf-8", [])
    # bad encoding
    readline.lines = ["# -*- coding: blah -*-", "", "x = 'foo'"]
    assert detect_encoding(readline) == (
        "ascii",
        [b"# -*- coding: blah -*-"],
    )
    # good encoding

# Generated at 2022-06-13 18:19:34.817374
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:19:43.167752
# Unit test for function generate_tokens
def test_generate_tokens():
    """Simple unit test for function generate_tokens"""
    import token
    source = "1 + 1\n# A comment\nprint(2)\n"

# Generated at 2022-06-13 18:19:49.078101
# Unit test for function generate_tokens
def test_generate_tokens():
    import sys
    import re
    import string
    import token
    import StringIO
    import keyword

    tok_re = re.compile("(\\s+)|(#[^\\r\\n]*$)|(\\w+)|([(){}\\[\\]]|[^ \\t\\r\\n\\w#(){}\\[\\]])")
    all_keywords = keyword.kwlist + ["None"]
    all_keywords.sort()

    def generate_tokens_from_string(s: str) -> Iterator[TokenInfo]:
        return generate_tokens(iter(s.splitlines(1)).next)

    # Generate all tokens for the regular expressions.

# Generated at 2022-06-13 18:19:58.302801
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from io import StringIO

    import tokenize as pytokenize

    sample_untokenize = (
        (pytokenize.COMMENT, "# a comment"),
        (pytokenize.NL, "\n"),
        (pytokenize.NAME, "spam"),
        (pytokenize.NUMBER, "23"),
        (pytokenize.STRING, "'string'"),
        (pytokenize.OP, "*"),
    )

    untok = Untokenizer()
    stream = StringIO()
    untok.write_raw(sample_untokenize, stream.write)
    expected = "# a comment\nspam 23 'string' *\n"
    assert stream.getvalue() == expected, repr(stream.getvalue()) + "!=" + repr(expected)

# Generated at 2022-06-13 18:20:02.713477
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    from token import tok_name

    text = open(__file__).read()
    for token in generate_tokens(StringIO(text).readline):
        assert token.type == COMMENT or token.string.strip(), repr(token)
        assert token.string == token.line[token.start[1] : token.end[1]]
    return tok_name[token.type]



# Generated at 2022-06-13 18:20:05.616066
# Unit test for function generate_tokens
def test_generate_tokens():
  s = '''def foo():\n  pass\n\nassert foo() is None'''
  import io
  f = io.StringIO(s)
  t = generate_tokens(f.readline)
  for token in t:
    print(token)
test_generate_tokens()

#@title

# Generated at 2022-06-13 18:20:12.579943
# Unit test for function detect_encoding
def test_detect_encoding():
    try:
        from io import BytesIO as BytesIO
    except ImportError:
        from cStringIO import StringIO as BytesIO

    def readline(b: bytes) -> Iterator[bytes]:
        yield b

    g = readline(b"# coding: latin-1\n")
    assert detect_encoding(g) == ("iso-8859-1", [b"# coding: latin-1\n"])

    g = readline(b"\xef\xbb\xbf# coding: latin-1\n")
    assert detect_encoding(g) == ("utf-8-sig", [b"# coding: latin-1\n"])

    g = readline(b"\xef\xbb\xbf\n")

# Generated at 2022-06-13 18:20:24.480473
# Unit test for function generate_tokens
def test_generate_tokens():
    from tokenize import generate_tokens

# Generated at 2022-06-13 18:20:32.261170
# Unit test for function generate_tokens
def test_generate_tokens():
    # Simulate a file with a readline method
    class FileSimulator:
        def __init__(self, lines: List[str]) -> None:
            self.lines = lines
            self.index = 0

        def readline(self) -> Text:
            if self.index >= len(self.lines):
                raise StopIteration
            line = self.lines[self.index]
            self.index += 1
            return line

    lines = [
        'print("bar")\n',
        "foo( '''\n",
        "foo( ''')\n",
        'print("bar2")\n',
    ]
    generator = generate_tokens(FileSimulator(lines).readline)
    token_types: List[str] = []
    # (toknum, tokval, start, end,

# Generated at 2022-06-13 18:22:14.560323
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    untk = Untokenizer()

    source = ["a = 1", "b = 2", "c = 3", "", "def foo():", "    b = 4", "    c = 5"]
    token_source: List[TokenInfo] = []
    line_source = iter(source)
    for line in line_source:
        token_source.extend(generate_tokens(lambda: token_source.clear() or line))

    assert untk.compat(("NAME", "foobar"), token_source) is None
    assert untk.tokens == ["foobar"]

    untk.tokens.clear()
    assert untk.compat(("NAME", "foobar"), token_source) is None
    assert untk.tokens == ["foobar "]

    untk.tokens.clear

# Generated at 2022-06-13 18:22:24.563635
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        if not lines:
            raise StopIteration
        line = lines[0]
        del lines[0]
        return line
