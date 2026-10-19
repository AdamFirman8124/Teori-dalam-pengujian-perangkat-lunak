

# Generated at 2022-06-13 18:13:25.014078
# Unit test for function tokenize_loop
def test_tokenize_loop():
    text = "def f(x): return x"
    fake_readline = lambda: text
    token_list = []
    tokenize_loop(fake_readline, token_list.append)
    return token_list # [[1, 'def', (1, 0), (1, 3), "def f(x): return x"], [1, 'f', (1, 4), (1, 5), "def f(x): return x"], [40, '(', (1, 5), (1, 6), "def f(x): return x"], [1, 'x', (1, 6), (1, 7), "def f(x): return x"], [41, ')', (1, 7), (1, 8), "def f(x): return x"], [58, ':', (1, 8), (1, 9), "def f(x

# Generated at 2022-06-13 18:13:32.107435
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import BytesIO
    from token import tok_name as token_name

    string = b"'abc' # comment\n\\\n  continued comment \\ \\\n  second line comment\n"
    buf = BytesIO(string)
    result = list(generate_tokens(buf.readline))

# Generated at 2022-06-13 18:13:35.543122
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from io import StringIO
    import sys
    import token

    text = "def f(x): return 2*x\n"
    with StringIO(text) as file:
        tokens = tokenize(file.readline)
        untokens = Untokenizer()
        r = untokens.untokenize(tokens)
    if r != text:
        print(r)
        print(text)
        sys.exit(1)



# Generated at 2022-06-13 18:13:36.994370
# Unit test for function tokenize
def test_tokenize():
    # FIXME
    import io

    a = io.StringIO("print(1, # comment\n2)").readline
    list(tokenize(a))



# Generated at 2022-06-13 18:13:39.060503
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from .tokenize import untokenize
    from io import BytesIO
    import tokenize as tokenize_module
    s = b"\nprint(1)\n"
    print(repr(untokenize(tokenize_module.generate_tokens(BytesIO(s).readline))))



# Generated at 2022-06-13 18:13:46.440480
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"#!/usr/bin/python3\n"
        yield b"# coding: latin-1\n"
        yield b"pass\n"

    encoding, lines = detect_encoding(readline)
    expected = ("iso-8859-1", [b"#!/usr/bin/python3\n", b"# coding: latin-1\n"])

    assert encoding == expected[0]
    assert lines == expected[1]



# Generated at 2022-06-13 18:13:54.590516
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:14:01.380225
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import sys
    from tokenize import detect_encoding

    class ReadlineError(Exception):
        pass

    def readline():
        """Read a line for decode_line() test, or raise an exception."""
        if not lines:
            raise ReadlineError
        line = lines.pop(0)
        if isinstance(line, Exception):
            raise line
        return line

    # check handling of utf-8 byte order mark
    lines = [
        codecs.BOM_UTF8 + b'\n',
        b'# coding: latin-1\n',
        b'a = "foo"\n',
    ]
    encoding, _ = detect_encoding(readline)
    assert encoding == 'utf-8'

    # check handling of utf-8 byte order mark followed by coding spec


# Generated at 2022-06-13 18:14:05.587415
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def readline():
        yield 'class Betelgeuse(object):'
    def tokeneater(*args):
        pass
    tokenize_loop(readline(), tokeneater)



# Generated at 2022-06-13 18:14:09.863501
# Unit test for function printtoken
def test_printtoken():
    printtoken(NUMBER, str(3.5), (1, 5), (1, 7), "3.5")

# unit test
test_printtoken()



# Generated at 2022-06-13 18:14:37.385417
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def readline():
        for l in ["print('foo', file=sys.stderr)\n", "del x # delete x\n"]:
            yield l
    # tokeneater is a callable object
    tokeneater = printtoken
    try:
        tokenize_loop(readline, tokeneater)
    except StopTokenizing:
        pass



# Generated at 2022-06-13 18:14:43.634781
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from tokenize import untokenize
    from io import StringIO

    untok = Untokenizer()
    input_stream = StringIO(
        """\
if a:
    print(1)
"""
    )
    toks = untok.compat((NAME, "if"), input_stream)
    assert untokenize(toks) == """\
if a :
    print ( 1 )
"""



# Generated at 2022-06-13 18:14:51.032365
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import tokenize
    s = '''def f(x):
        return 2*x'''
    tokengen = tokenize.generate_tokens(io.StringIO(s).readline)
    for tokentype, token, start, end, line in tokengen:
        print(tokentype, token, start, end, line)

test_generate_tokens()


# Generated at 2022-06-13 18:15:03.348635
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    # No doctests in Python 3.6
    # test_input = [
    #     (NAME, "exec"),
    #     (OP, "("),
    #     (NAME, "data"),
    #     (OP, ")"),
    #     (NEWLINE, "\n"),
    #     (INDENT, "    "),
    #     (NAME, "print"),
    #     (NAME, "x"),
    #     (OP, ","),
    #     (NAME, "2"),
    #     (NEWLINE, "\n"),
    #     (DEDENT, ""),
    #     (NAME, "exec"),
    #     (OP, "("),
    #     (NAME, "data"),
    #     (OP, ")"),
    # ]
    untok = Untokenizer()
    #

# Generated at 2022-06-13 18:15:05.638353
# Unit test for function printtoken
def test_printtoken():
    printtoken(NUMBER, "1", (1, 2), (1, 3), "2")



# Generated at 2022-06-13 18:15:09.167127
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    import tokenize as tokenize_module

    f = io.StringIO("x = 1")
    tokens = tokenize_module.generate_tokens(f.readline)
    u = Untokenizer()
    result = u.untokenize(tokens)
    # print(result)
    assert result == "x = 1 "


# Utility functions

# Generated at 2022-06-13 18:15:16.225993
# Unit test for function tokenize_loop
def test_tokenize_loop():
    tokeneater = lambda *args: None

    def readline():
        return "\n"

    tokenize_loop(readline, tokeneater)
    readline = iter(["0=0"]).__next__

    def tokeneater(type, token, start, end, line):
        assert token == "0=0"
        assert type == tokenize.EQUAL

    try:
        tokenize_loop(readline, tokeneater)
    except StopIteration:
        pass



# Generated at 2022-06-13 18:15:18.920256
# Unit test for function tokenize
def test_tokenize():
    import io, token, tokenize
    r = io.BytesIO(b"\n")
    g = tokenize.generate_tokens(r.readline)
    for tok in g:
        print(tok)


# Generated at 2022-06-13 18:15:22.207451
# Unit test for function tokenize_loop
def test_tokenize_loop():
    # FIXME: write good tests
    import types
    assert type(tokenize_loop) is types.FunctionType, repr(type(tokenize_loop))



# Generated at 2022-06-13 18:15:23.198998
# Unit test for method untokenize of class Untokenizer

# Generated at 2022-06-13 18:16:52.565440
# Unit test for function detect_encoding
def test_detect_encoding():
    from codecs import lookup

    def readline(line=bytes()):
        for c in [line]:
            yield c

    def read(line1=bytes(), line2=bytes()):
        return detect_encoding(readline(line1 + line2))

    def readu(line1="", line2=""):
        return read(line1.encode("utf-8"), line2.encode("utf-8"))

    assert read() == ("utf-8", [])
    assert read(line1=b"#!/usr/bin/python3") == ("utf-8", [b"#!/usr/bin/python3"])

# Generated at 2022-06-13 18:17:05.149991
# Unit test for method compat of class Untokenizer

# Generated at 2022-06-13 18:17:17.326125
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield '# -*- coding: latin-1 -*-\n'.encode("ascii")
        yield 'import sys, os;\n'.encode("latin-1")

    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"
    assert lines == [
        '# -*- coding: latin-1 -*-\n'.encode("ascii"),
        'import sys, os;\n'.encode("latin-1"),
    ]
    encoding, lines = detect_encoding(lambda: b'')
    assert encoding == "utf-8"
    assert lines == []
    def readline():
        yield '\xef\xbb\xbf'.encode("utf-8")

# Generated at 2022-06-13 18:17:19.737852
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    ut = Untokenizer()
    s = ut.compat((1, ""), [(1, ""), (3, "")])



# Generated at 2022-06-13 18:17:28.509202
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import sys

    def reader():
        yield from io.BytesIO("# coding: latin-1\npass\n".encode("utf-8")).readlines()
        yield from ()

    encoding = detect_encoding(reader)
    if encoding != ("iso-8859-1", ["# coding: latin-1\n".encode("utf-8")]):
        print("ERROR: detect_encoding() #1")

    def reader():
        yield from io.BytesIO("# coding: latin-1\npass\n".encode("utf-8")).readlines()
        yield from io.BytesIO(
            """\
'''
# coding: utf-8
'''
pass
"""
        ).readlines()

    encoding = detect_encoding(reader)

# Generated at 2022-06-13 18:17:36.425838
# Unit test for function tokenize
def test_tokenize():
    import io
    import unittest
    import tokenize as tokenize_module

    class Test(unittest.TestCase):
        def test_tokenize(self):
            tokenize_module._builtin_open = open

# Generated at 2022-06-13 18:17:41.041404
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# -*- coding: utf-8 -*-\n"
        yield b"import os\n"
        yield b"print(1)\n"

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"
    assert b"".join(lines) == b"# -*- coding: utf-8 -*-\nimport os\n"

    def readline():
        yield b"# -*- coding: utf-8 -*-\n"

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"
    assert b"".join(lines) == b"# -*- coding: utf-8 -*-\n"


# Generated at 2022-06-13 18:17:49.194072
# Unit test for function detect_encoding
def test_detect_encoding():
    import io

    readline = io.BytesIO
    # Test non-UTF-8 encodings
    for encoding in ["iso-8859-1", "gb2312", "iso-2022-jp"]:
        for suffix in ["", "-sig"]:
            enc = encoding + suffix
            bom = getattr(codecs, "BOM_" + enc.upper().replace("-", "_"))
            if bom:
                data = bom + b'# -*- coding: %s -*-\npass\n' % enc.encode("ascii")
            else:
                data = b'# -*- coding: %s -*-\npass\n' % enc.encode("ascii")
            data = data.replace(b"#", b"\n#")
            rd = readline

# Generated at 2022-06-13 18:17:59.476389
# Unit test for function detect_encoding
def test_detect_encoding():
    # no encoding declared
    readline = iter(
        [
            bytes(
                b'# coding: ISO-8859-1\n'
                b'# stuff\n'
                b'# more stuff\n'
                b'#!/usr/bin/env python\n'
                b"'''hello world'''\n"
            )
        ]
    ).__next__
    assert detect_encoding(readline) == ("iso-8859-1", [])

    # encoding declared with BOM
    readline = iter(
        [
            bytes(
                b'# stuff\n'
                b'# more stuff\n'
                b'#!/usr/bin/env python\n'
                b"'''hello world'''\n"
            )
        ]
    ).__next__
   

# Generated at 2022-06-13 18:18:03.056156
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield ""
        yield "blah blah"
        yield "# -*- coding: klingon -*-"
        yield "blah blah"
        yield "more"
    encoding, lines = detect_encoding(readline)
    assert encoding == "klingon"
    assert lines[0] == b""
    assert lines[1] == b"blah blah"



# Generated at 2022-06-13 18:18:49.245054
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    from functools import partial  # type: ignore

    def readlines(s: List[str], buffer_size: int = io.DEFAULT_BUFFER_SIZE) -> Iterator[bytes]:
        yield from map(partial(bytes, encoding="utf-8"), s)

    def readlines_good(
        s: List[str], buffer_size: int = io.DEFAULT_BUFFER_SIZE
    ) -> Iterator[bytes]:
        return readlines(s, buffer_size)

    def readlines_bad(
        s: List[str], buffer_size: int = io.DEFAULT_BUFFER_SIZE
    ) -> Iterator[bytes]:
        return readlines(s, buffer_size)


# Generated at 2022-06-13 18:18:53.085494
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    # untokenize expects an iterable of tokens, not a generator
    tokens = generate_tokens(iter(['a, b']).__next__)
    u = Untokenizer()
    assert u.untokenize(tokens) == 'a , b '



# Generated at 2022-06-13 18:19:00.777504
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    import sys
    from test import support
    from . import tokenize

    def generate_tokens(s: str) -> Iterator[TokenInfo]:
        for tok in tokenize.tokenize(io.BytesIO(s.encode("utf-8")).readline):
            if tok[0] == tokenize.ENCODING:
                continue
            yield tok


# Generated at 2022-06-13 18:19:06.325947
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    input = [
        (NAME, "insert"),
        (OP, "+="),
        (STRING, "'was here'"),
        (NEWLINE, "\n"),
    ]
    ut = Untokenizer()
    output = ut.untokenize(input)
    assert output == "insert += 'was here'\n"


# Generated at 2022-06-13 18:19:11.355265
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    untok = Untokenizer()
    res = untok.compat((1, "foo"), [])
    assert res == None
    print("test_Untokenizer_compat passed.")



# Generated at 2022-06-13 18:19:21.193789
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from StringIO import StringIO

    stream = StringIO("class Test:\n  pass\n")
    result = []

    def tokeneater(*args):
        result.append(args)

    tokenize_loop(stream.readline, tokeneater)

# Generated at 2022-06-13 18:19:26.901811
# Unit test for function generate_tokens
def test_generate_tokens():
    global compteur
    compteur = 0
    with open('lignes.txt', 'r') as file:
        for i in range(1, 6):
            file.readline()
        for line in file:
            compteur += 1
            for token in generate_tokens(StringIO(line).readline):
                print(token)
            print("\n")
test_generate_tokens()

import tokenize

# Generated at 2022-06-13 18:19:35.509680
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline_mock(lines):
        def readline():
            return lines.pop(0)
        return readline


# Generated at 2022-06-13 18:19:43.198276
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        if not lines:
            raise StopIteration
        line = lines.pop()
        if isinstance(line, str):
            line = line.encode("ascii")
        return line

    def check(first, encoding, second):
        global lines
        lines = [first, second]
        found_encoding, _ = detect_encoding(readline)
        assert found_encoding == encoding

    check("", "utf-8", "")
    check("# -*- coding: latin-1 -*-", "iso-8859-1", "")
    check("# coding=utf-8", "utf-8", "")
    check("# coding=latin-1", "iso-8859-1", "")

# Generated at 2022-06-13 18:19:51.799591
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import tokenize
    output = io.StringIO()
    test_prog = [
        "def foo():\n",
        "  while True:\n",
        "    if x:\n",
        "      try:\n",
        "        print x\n",
        "      finally:\n",
        "        pass\n",
        "      if y:\n",
        "        break\n",
        "        # break should be dedented\n",
        "    return x\n",
    ]
    tokenize.generate_tokens(test_prog.pop, output.write)
    contents = output.getvalue()

# Generated at 2022-06-13 18:20:38.619253
# Unit test for function detect_encoding
def test_detect_encoding():
    from io import StringIO

    def reader(s, *args):
        for c in s:
            yield c
        while True:
            yield ""


# Generated at 2022-06-13 18:20:49.618159
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import os
    import tempfile

    # SF bug #1179797:  detect_encoding() doesn't ignore blank lines
    with tempfile.TemporaryDirectory() as tmpdir:
        s = '\n'.join(("# coding: latin-1", "", "# foo", "# bar"))
        fn = os.path.join(tmpdir, "test_pep263_blank_line.py")
        with open(fn, "wb") as fp:
            fp.write(s.encode("latin-1"))
        with open(fn, "rb") as fp:
            rl = fp.readline
            result = detect_encoding(rl)
            assert result == ("iso-8859-1", [])

    # SF bug #1571870: detect_encoding() reads lines too

# Generated at 2022-06-13 18:20:54.220447
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    ut = Untokenizer()
    ut.compat((NAME, "äöü"), [(NUMBER, "1.1"), (NAME, "x")])
    test_string = ut.tokens

# Generated at 2022-06-13 18:21:01.033892
# Unit test for function detect_encoding
def test_detect_encoding():
    import io

    def readline() -> Iterator[Text]:
        for line in [
            '# -*- coding: latin-1 -*-\n',
            '"""Module docstring"""\n',
            'class A:\n',
            "    def __init__(self):\n",
            "        self._x = None\n",
            '    @property\n',
            '    def x(self):\n',
            "        return self._x\n",
            "\n",
            "\n",
            '\n',
        ]:
            yield line


# Generated at 2022-06-13 18:21:14.721511
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    from pprint import pprint
    from token import tok_name
    text = (
        "def square(n):\n"
        "    return n*n\n"
        "\n"
        "print(square(5))\n"
    )
    f = StringIO(text)
    tokgen = generate_tokens(f.readline)
    toks = []
    for toknum, tokval, _, _, _ in tokgen:
        toks.append((tok_name[toknum], tokval))
    print("TOKENS:\n")
    pprint(toks)
    print()

# Generated at 2022-06-13 18:21:24.152839
# Unit test for function detect_encoding
def test_detect_encoding():
    from textwrap import dedent

    def readline(lines: List[bytes]) -> Callable[[], bytes]:
        def readline_inner() -> bytes:
            try:
                return lines.pop(0)
            except IndexError:
                raise StopIteration

        return readline_inner

    # No BOM
    assert detect_encoding(readline([b"# coding: utf-8\n", b"x = 1\n"])) == ("utf-8", [])
    assert detect_encoding(readline([b"\n", b"x = 1\n"])) == ("utf-8", [])

    # With BOM
    # Note that UTF-16 and UTF-32 are decoded before passed to detect_encoding.

# Generated at 2022-06-13 18:21:28.567823
# Unit test for function tokenize_loop
def test_tokenize_loop():
  # This is just the interface test.  The tests for various tokens are scattered
  # throughout the suite.
  def eat_tokens(type, token, start, end, line):
    assert (type, token, start, end, line)
  tokenize_loop(iter(["x = (1 + 2)"]).__next__, eat_tokens)



# Generated at 2022-06-13 18:21:31.164307
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    ut = Untokenizer()
    ut.compat((1, "for"), [(1, "for"), (1, "foo"), (1, "bar")])
    assert ut.tokens == ["for foo bar "]



# Generated at 2022-06-13 18:21:40.499807
# Unit test for function generate_tokens
def test_generate_tokens():

    def tokenize(s: Text) -> List[TokenInfo]:
        return list(generate_tokens(StringIO(s).readline))

    x = tokenize("1 + 1")
    assert x.pop() == TokenInfo(NAME, "1", (1, 0), (1, 1), "\n")
    assert x.pop() == TokenInfo(OP, "+", (1, 2), (1, 3), "\n")
    assert x.pop() == TokenInfo(NAME, "1", (1, 4), (1, 5), "\n")
    assert x.pop() == TokenInfo(ENDMARKER, "", (1, 5), (1, 5), "\n")
    assert not x

    x = tokenize("1 + 1\n")

# Generated at 2022-06-13 18:21:53.453164
# Unit test for function generate_tokens
def test_generate_tokens():
    gr = Grammar()
    rl = iter('abc def\nxyz').__next__
    expected = [
        (NAME, 'abc', (1, 0), (1, 3), 'abc def\n'),
        (NAME, 'def', (1, 4), (1, 7), 'abc def\n'),
        (NEWLINE, '\n', (1, 7), (1, 8), 'abc def\n'),
        (NAME, 'xyz', (2, 0), (2, 3), 'xyz'),
        (ENDMARKER, '', (2, 3), (2, 3), 'xyz'),
    ]
    for tok in generate_tokens(rl, grammar=gr):
        assert tok == expected.pop(0)
    # now test using a file
    import tempfile