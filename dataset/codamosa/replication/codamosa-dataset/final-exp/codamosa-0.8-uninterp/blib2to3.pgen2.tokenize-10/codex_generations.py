

# Generated at 2022-06-13 18:14:17.273059
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io

# Generated at 2022-06-13 18:14:24.190301
# Unit test for function generate_tokens
def test_generate_tokens():
    def check_token(tok: TokenInfo, name: str, attrs: Tuple[Any, ...]) -> None:
        assert tok[0] == name
        assert len(tok) == len(attrs) + 1
        for i, tokattr in enumerate(tok[1:]):
            assert tokattr == attrs[i]

    s = "a = 1 + 2\nb = [3, 4]\n"
    i = 0
    for tok in generate_tokens(iter(s.splitlines(True)).__next__):
        i = i + 1
        if i == 1:
            check_token(
                tok,
                "NAME",
                ("a", (1, 0), (1, 1), "a = 1 + 2\n"),
            )

# Generated at 2022-06-13 18:14:30.550501
# Unit test for function generate_tokens
def test_generate_tokens():
    # Some test cases for the tokenize() generator.

    from io import StringIO
    from token import *

    readline = StringIO("if 1:\n  pass\n").readline
    g = generate_tokens(readline)
    for tok in g:
        print(tok)
    print('-' * 60)

    # Test untokenize() with a tab before an ENDMARKER:
    readline = StringIO("if 1:\n\tpass").readline
    g = generate_tokens(readline)
    print(list(g))
    print(untokenize(g))
    print('-' * 60)

    # Test tokenize() with a tab before an ENDMARKER:
    from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP

# Generated at 2022-06-13 18:14:35.474191
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import tokenize
    readline = iter(
        [
            "'''",
            '   abc',
            '   123',
            '''  ''' + '"',
            '"',
        ]
    ).__next__
    toks = tokenize.generate_tokens(readline)
    untok = Untokenizer()
    assert untok.untokenize(toks) == '   abc   123   ""'



# Generated at 2022-06-13 18:14:46.239765
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import unittest

    def readline():
        line = next(lines)
        return line.encode()

    lines = iter(["# -*- coding: utf-8 -*-\n"])
    encoding_name, lines = detect_encoding(readline)
    self.assertEqual(encoding_name, "utf-8")
    lines = iter(['# coding: utf-8 \n'])
    encoding_name, lines = detect_encoding(readline)
    self.assertEqual(encoding_name, "utf-8")
    lines = iter(['# coding=utf-8 \n'])
    encoding_name, lines = detect_encoding(readline)
    self.assertEqual(encoding_name, "utf-8")

# Generated at 2022-06-13 18:14:57.274331
# Unit test for function generate_tokens
def test_generate_tokens():  # htest #
    r = StringIO(dedent(
        """
            a = 1
            b = 2
            def f():
                pass
        """
    ))
    tokengen = generate_tokens(r.readline)
    types = []
    for token in tokengen:
        typ, val, _, _, _ = token
        types.append(typ)
    types = tuple(types)

# Generated at 2022-06-13 18:15:04.468709
# Unit test for function printtoken
def test_printtoken():
    return printtoken(
        0, "token", (0, 0), (0, 0), "line"
    ) is None and printtoken(
        0, "token", (0, 0), (0, 6), "line"
    ) is None and printtoken(
        1, "token", (5, 8), (5, 8), "line"
    ) is None



# Generated at 2022-06-13 18:15:11.722812
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io

    def _some_code(some_file):
        some_file.write(
            """\
foo = '''\
bar
baz'''
print('foo')
"""
        )

    with io.StringIO() as some_file, io.StringIO() as out:
        _some_code(some_file)
        some_file.seek(0)
        tokenize_loop(some_file.readline, out.write)
        out.seek(0)

# Generated at 2022-06-13 18:15:19.460843
# Unit test for function tokenize
def test_tokenize():
    import sys
    import blib2to3.pgen2.token as token


# Generated at 2022-06-13 18:15:29.454743
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import unittest
    import io

    class BytesIO(io.BytesIO):
        def readline(self):
            return io.BytesIO.readline(self).rstrip()

    s = b"# coding: utf-8\nprint(1)\n"

# Generated at 2022-06-13 18:16:45.928637
# Unit test for function tokenize
def test_tokenize():
    import io
    from blib2to3.pgen2.tokenize import (
        detect_encoding,
        untokenize,
        untokenize_with_newlines,
    )

    encoding = "utf-8"
    readline = io.StringIO(
        "# coding: utf-8\nan int: 2  \n" + ("a" * 100000) + "\n"
    ).readline
    rv = list(tokenize(readline))
    assert rv[0][:2] == (ENCODING, encoding)
    assert rv[1][:2] == (COMMENT, "# coding: utf-8")
    assert rv[2][:2] == (NEWLINE, "\n")
    assert rv[3][:2] == (NAME, "an")
    assert rv

# Generated at 2022-06-13 18:16:53.395462
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(seq: List[bytes]) -> Callable[[], bytes]:
        return lambda: seq.pop(0)


# Generated at 2022-06-13 18:17:06.654957
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO

# Generated at 2022-06-13 18:17:14.329405
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import unittest

    class TestTokenize(unittest.TestCase):
        example_text = "# coding: utf-8\n# comment\n\npass\npass"

        def test_detect_utf8(self):
            with io.BytesIO(self.example_text.encode()) as f:
                encoding, lines = detect_encoding(f.readline)
                self.assertEqual(encoding, "utf-8")
                self.assertEqual("".join(line.decode("utf-8") for line in lines),
                                 self.example_text)

        def test_detect_utf8_with_bom(self):
            with io.BytesIO(BOM_UTF8 + self.example_text.encode("utf-8")) as f:
                encoding

# Generated at 2022-06-13 18:17:24.718478
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> Iterator[bytes]:
        yield b"# coding: utf-8\n"
        yield b"# some other comment\n"
        yield b"# coding: latin-1\n"
        yield b"# coding: iso-8859-1\n"
        yield b"4 + 4\n"
        yield b"# coding=ascii\n"
        yield b"# coding=ascii123\n"
        yield b"# coding=hello\n"
        yield b"5 + 5\n"
    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"

# Generated at 2022-06-13 18:17:34.680046
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO
    from . import tokenize
    from . import untokenize

    data = (
        "def f(): yield from g()\n"
        "d = {1: ('a', 'b'): (('a', 'b'), ('c', 'd'), ('e', 'f'))}"
    )
    compare = "def f ( ) : yield from g ( ) \n" "d = { 1 : ( 'a' , 'b' ) : ( ( 'a' , 'b' ) , ( 'c' , 'd' ) , ( 'e' , 'f' ) ) } "
    f = StringIO(data)
    tokens = tokenize.generate_tokens(f.readline)
    untok = untokenize.Untokenizer()

# Generated at 2022-06-13 18:17:40.666808
# Unit test for function detect_encoding
def test_detect_encoding():
    import tokenize, io

    def utf8_bom(s):
        return '\ufeff' + s

    def utf8_cookie(s):
        return '# -*- coding: utf-8 -*-\n' + s

    def utf8_both(s):
        return utf8_cookie(utf8_bom(s))

    def readline(s):
        for c in io.BytesIO(s.encode("utf-8")):
            yield c


# Generated at 2022-06-13 18:17:48.971412
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from textwrap import dedent
    from io import StringIO
    from test.support import captured_stdout
    from . import tokenize

    def roundtrip(s):
        io = StringIO(s)
        tokens = list(tokenize.tokenize(io.readline))
        io.seek(0)
        return "".join(tokenize.untokenize(tokens))

    def compare(s):
        assert roundtrip(s) == dedent(s) + "\n"

    compare("\n")
    compare("a = 1; b = 2; c = 3\n")
    compare("a = 1\nif a == 1:\n    print(1)\n")
    compare("a = 1\nb = 2\nprint(a + b)\n")

# Generated at 2022-06-13 18:17:55.059708
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from io import StringIO
    # Testing with a real file object
    with open(__file__, "r") as fileobj:
        tokenize_loop(fileobj.readline, printtoken)
    # Testing with a StringIO instance
    fileobj = StringIO("print('hello world')\n")
    tokenize_loop(fileobj.readline, printtoken)



# Generated at 2022-06-13 18:18:02.695048
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import sys

    def test(s, expected):
        tokeneater = []
        readline = io.StringIO(s).readline
        tokenize_loop(readline, tokeneater.append)
        actual = [t[:4] for t in tokeneater]
        assert actual == expected, "%r != %r" % (actual, expected)

    test('foo = 1; bar = 2', [(1, 'foo', (1, 0), (1, 3), 'foo = 1; bar = 2')])
    test('foo #lalala= 1', [(1, 'foo', (1, 0), (1, 3), 'foo #lalala= 1')])

# Generated at 2022-06-13 18:20:31.392238
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        if not lines:
            raise StopIteration
        line = lines[0]
        del lines[0]
        return line


# Generated at 2022-06-13 18:20:43.282988
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from io import BytesIO
    from tokenize import tokenize, COMMENT, ENCODING, NAME, OP, generate_tokens
    for data in [b"def f():\n  return", b"def f(): #\n  return # comment\n"]:
        stream = BytesIO(data)
        toklist = list(tokenize(stream.readline))
        toklist_w = list(generate_tokens(stream.readline))
        assert len(toklist) == len(toklist_w)
        for token, token_w in zip(toklist, toklist_w):
            assert token[:2] == token_w[:2]

# Generated at 2022-06-13 18:20:53.552630
# Unit test for function detect_encoding
def test_detect_encoding():
    from io import BytesIO
    from pickle import dumps, loads
    from sys import getdefaultencoding
    from textwrap import dedent

    def _readline() -> bytes:
        return next(lines)

    lines = [line.encode("ASCII") for line in dedent("""
    # coding: latin1
    # comment
    # coding: cp424
    # comment
    """).split("\n")]

    assert detect_encoding(_readline) == ("iso-8859-1", [])
    assert detect_encoding(_readline) == ("cp424", [b"# coding: latin1"])
    assert detect_encoding(_readline) == ("cp424", [b"# coding: latin1", b"# comment"])
    # Restore the list of lines to be able to read it again

# Generated at 2022-06-13 18:21:00.663744
# Unit test for function generate_tokens
def test_generate_tokens():
    class myparser(object):
        def __init__(self, lines: Iterable[Text]):
            self.nextline = lines.__iter__().__next__

        def __iter__(self):
            return self

        def __next__(self):
            return generate_tokens(self.nextline)

        def error_leader(self, line):
            return line

    from pprint import pprint


# Generated at 2022-06-13 18:21:14.542979
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    from encodings.utf_8_sig import utf_8_sig_decode

    def reader(xs):
        for x in xs:
            yield bytes(x, "ASCII")

    def readline():
        try:
            return next(readlines)
        except StopIteration:
            return None

    # No encoding
    readlines = reader(["def f():\n", "  pass\n"])
    assert detect_encoding(readline) == ("utf-8", [])

    # # coding: utf-8
    readlines = reader(["# coding: utf-8\n", "def f():\n"])
    assert detect_encoding(readline) == ("utf-8", [])

    # # coding=utf-8

# Generated at 2022-06-13 18:21:24.112565
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        return next(lines)

    # try coding spec in first two lines only
    lines = iter(
        [
            b"#!/usr/bin/python3\n",
            b"# -*- coding: latin-1 -*-\n",
            b"# stuff before\n",
            b"# -*- coding: latin-1 -*-\n",
            b"# stuff after\n",
        ]
    )
    eq = assert_equal
    eq(detect_encoding(readline), ("latin-1", [b"# stuff before\n", b"# stuff after\n"]))

    # try coding spec in last line only

# Generated at 2022-06-13 18:21:32.233463
# Unit test for function tokenize_loop
def test_tokenize_loop():
    "Test tokenize loop"
    s = "if 1: # comment\n  print(1)\n"
    result = [
        (token.NAME, "if"),
        (token.NUMBER, "1"),
        (token.COLON, ":"),
        (token.NEWLINE, "\n"),
        (token.INDENT, "  "),
        (token.NAME, "print"),
        (token.OP, "("),
        (token.NUMBER, "1"),
        (token.OP, ")"),
        (token.NEWLINE, "\n"),
        (token.DEDENT, ""),
    ]
    it = generate_tokens(s.__iter__().__next__)

# Generated at 2022-06-13 18:21:37.391163
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        return (yield).encode()

    it = readline()
    it.__next__()
    next(it)
    # If no encoding is specified, the default is utf-8.
    assert detect_encoding(it.send) == ("utf-8", [])
    # BOM is always overridden by Python encoding.
    it.__next__()
    assert detect_encoding(it.send(BOM_UTF8)) == ("utf-8-sig", [])
    # BOM is always overridden by Python encoding.
    it.__next__()
    assert detect_encoding(it.send(BOM_UTF8 + "utf-8".encode())) == ("utf-8-sig", [])
    # BOM is not overridden by Python encoding.

# Generated at 2022-06-13 18:21:42.929694
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield '# -*- coding: latin-1 -*-\n'.encode('latin-1')
        yield '# coding: ascii\n'.encode('ascii')
    enc = detect_encoding(readline)
    assert enc == ('iso-8859-1',
                   ['# -*- coding: latin-1 -*-\n'.encode('latin-1')])



# Generated at 2022-06-13 18:21:49.864196
# Unit test for function detect_encoding
def test_detect_encoding():
    def t(sample, expected):
        sample = [line.encode("ascii") for line in sample]
        encoding, lines = detect_encoding(iter(sample).__next__)
        assert expected == encoding

    t(["# coding: latin-1"], "iso-8859-1")
    t([u"\ufeff# coding: latin-1"], "iso-8859-1")
    t([u"# coding: latin-1", u"\ufeff# coding: latin-1"], "iso-8859-1")
    t([u"# coding: latin-1", u"\ufeff"], "iso-8859-1")
    t([u"\ufeff"], "utf-8")
    t([u" "], "utf-8")
    t([], "utf-8")