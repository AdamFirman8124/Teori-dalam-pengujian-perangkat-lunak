

# Generated at 2022-06-13 18:13:34.400216
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from . import tokenize


# Generated at 2022-06-13 18:13:45.151056
# Unit test for function detect_encoding
def test_detect_encoding():
    import io

    def readline() -> bytes:
        """Line reader for detect_encoding."""
        return bytes(line.pop(0) + "\n", "utf-8")

    def test(lines: List[str], expected: str) -> None:
        global line
        line = [l.encode("utf-8") for l in lines]
        assert detect_encoding(readline) == (expected, lines)

    test(["bogus"], "utf-8")
    test([BOM_UTF8 + "bogus"], "utf-8-sig")
    test(["# coding: bogas"], "bogas")
    test(["#!/usr/bin/python3", "# coding=aBcDeF-8"], "abcdef-8")

# Generated at 2022-06-13 18:13:50.302391
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    import tokenize
    from io import StringIO
    u = tokenize.Untokenizer()
    it = tokenize.generate_tokens(StringIO("hello 1.2+2j ([{}]\n)").readline)
    result = u.untokenize(it)
    assert result == "hello 1.2 + 2j ( [(]\n) "



# Generated at 2022-06-13 18:13:57.440108
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    from token import tok_name

    def token_type_name(tok) -> str:
        return tok_name.get(tok[0], "UNKNOWN")

    def show_token_tuple(tok) -> str:
        return "{:<15} {:<12} {:<10} {:<10} {}".format(
            token_type_name(tok),
            tok[1],
            tok[2],
            tok[3],
            repr(tok[4])[:55],
        )

    def all_token_tuples(source, verbose=True) -> Iterator[GoodTokenInfo]:
        if verbose:
            print("\n" + ("-" * 100))
            print("Source:", repr(source))

# Generated at 2022-06-13 18:14:08.368704
# Unit test for function generate_tokens
def test_generate_tokens():
    def test(s):
        list(tokenize.generate_tokens(StringIO(s).readline))
    test('@\n@\n')
    test('""\n""\n')
    test("'''\n'''\n'''\n")
    test('"""\n"""\n"""\n')
    test(r'"\n"\n"\n')
    test(r"'\n'\n'\\n'\n")
    test(r"'\n'\n'\n")
    test(r"'\n'\n")
    test(r"'''\n\n'''\n")
    test(r"'''\n\n'''\n'''\n")

# Generated at 2022-06-13 18:14:17.420559
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import token
    import unittest

    class TestTokenizeLoop(unittest.TestCase):
        def compare_tokenize_loop(self, expected, f):
            got = []
            tokenize_loop(
                f.readline,
                lambda t, s, b, e, l: got.append(
                    (t, s, b, e, l)  # type: ignore
                ),
            )
            self.assertEqual(expected, got)

        def test_empty(self):
            self.compare_tokenize_loop(
                [], io.StringIO(textwrap.dedent(""))  # type: ignore
            )


# Generated at 2022-06-13 18:14:23.114120
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
    untokenizer = Untokenizer()
    untokenizer.prev_row = 1
    untokenizer.prev_col = 9
    untokenizer.add_whitespace([1, 10])
    assert untokenizer.tokens == [" "]
    untokenizer.add_whitespace([1, 9])
    assert untokenizer.tokens == [" "]
    untokenizer.add_whitespace([1, 11])
    assert untokenizer.tokens == [" "]
    untokenizer.add_whitespace([2, 9])
    assert untokenizer.tokens == [" ", "\n"]


# Generated at 2022-06-13 18:14:30.567135
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield bytes([239, 187, 191]) + b"# coding=utf-8\n"
        yield b"a = 5\n"
        yield b"# coding=latin-1\n"
        yield b"b = 6\n"
    expected = [
        ("utf-8-sig", [b"a = 5\n"]),
        ("latin-1", [b"b = 6\n"]),
    ]
    for expected, lines in zip(expected, expected):
        assert detect_encoding(readline) == expected



# Generated at 2022-06-13 18:14:33.608542
# Unit test for function tokenize
def test_tokenize():
    def readline():
        yield "(a+b)"
        yield "print c"
        yield "def foo(): pass"
        yield ""
        yield ""

    tokenize(readline().__next__)


# Fill in the gaps in this generator!

# Generated at 2022-06-13 18:14:40.047932
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    untok = Untokenizer()
    # Single line
    out1 = untok.untokenize(
        [
            (token.NAME, "abc", (1, 0), (1, 3), "abc"),
            (token.NEWLINE, "\n", (1, 3), (2, 0), "abc\n"),
            (token.NAME, "def", (2, 0), (2, 3), "def"),
            (token.NEWLINE, "\n", (2, 3), (3, 0), "def\n"),
        ]
    )
    assert out1 == "abc\ndef\n", "untok failed"
    # Multi line

# Generated at 2022-06-13 18:15:27.655948
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
  untok = Untokenizer()
  t = (1, "")
  untok.add_whitespace(t)
  untok.add_whitespace((0, 0))
  untok.add_whitespace((0, 1))
  untok.add_whitespace((1, 1))
  try:
    untok.add_whitespace((0, -1))
  except:
    pass
  else:
    assert 0, "Failed to detect negative col"
  try:
    untok.add_whitespace((-1, 0))
  except:
    pass
  else:
    assert 0, "Failed to detect negative row"



# Generated at 2022-06-13 18:15:31.703937
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from io import StringIO
    from .token import test_tokenize
    for input, (output, n) in test_tokenize.tests:
        f = StringIO(input)
        l = []
        tokenize_loop(f.readline, l.append)
        assert n == len(l)
        assert output == l



# Generated at 2022-06-13 18:15:36.469729
# Unit test for function generate_tokens
def test_generate_tokens():
    import io, tokenize

    with io.StringIO("a = 3") as f:
        for token in tokenize.generate_tokens(f.readline):
            print(token)

test_generate_tokens()

# Test Suite

# Generated at 2022-06-13 18:15:45.373525
# Unit test for function tokenize
def test_tokenize():
    from . import tokenize
    from io import StringIO
    from token import tokenize, untokenize, NUMBER, NAME, STRING
    readline = StringIO("1+1\n").readline
    result = [(NUMBER, '1', (1, 0), (1, 1), '1+1\n'),
              (OP, '+', (1, 1), (1, 2), '1+1\n'),
              (NUMBER, '1', (1, 2), (1, 3), '1+1\n'),
              (NEWLINE, '\n', (1, 3), (1, 4), '1+1\n')]
    tokens = tokenize(readline)
    for (i, t) in enumerate(tokens):
        if t != result[i]:
            print('ann', t)


# Generated at 2022-06-13 18:15:47.871313
# Unit test for function generate_tokens
def test_generate_tokens():
    def test_ret(L, tokenize_func):
        for t in tokenize_func(L):
            print(t)
    lines = ["if 1:  # abc", '  print("abc")']
    test_ret(lines, generate_tokens)


# Generated at 2022-06-13 18:15:53.804686
# Unit test for function generate_tokens
def test_generate_tokens():
    def remove_u(s: str) -> str:
        return s.replace("u", "")

    def remap(x: TokenInfo) -> TokenInfo:
        return (x[0], remove_u(x[1]), x[2], x[3], remove_u(x[4]))

    def check(source: str, expected: Iterable[TokenInfo]) -> None:
        try:
            actual = generate_tokens(iter(source.splitlines(True)).next)
        except TokenError as e:
            raise AssertionError(
                'generate_tokens("""\\\n%s""") raised %s' % (source, e)
            )
        actual = list(remap(a) for a in actual)
        expected = list(remap(e) for e in expected)

# Generated at 2022-06-13 18:16:03.668859
# Unit test for function generate_tokens
def test_generate_tokens():
    import random

    def test_tokenize(input):
        try:
            result = list(tokenize(StringIO(input).readline))
        except:
            result = '<ERROR>'
        print('%-40r %r' % (input, result))

    # Test various combinations of line endings
    test_tokenize('print(1)\n')
    test_tokenize('print(1)\r\n')
    test_tokenize('print(1)\n\r')
    test_tokenize('print(1)\r\n\r\n')
    test_tokenize('print(1)\r\r')
    test_tokenize('\nprint(1)')
    test_tokenize('\r\nprint(1)')
    test_tokenize('\r\rprint(1)')
    test_

# Generated at 2022-06-13 18:16:16.757170
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import unittest
    import io
    from test.support import captured_stdout

    class TestTokenizeLoop(unittest.TestCase):
        def test_basic_functionality(self):
            lines = ["a = 1\n", "b = 2\n", "c = 3\n"]

# Generated at 2022-06-13 18:16:24.494488
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:16:28.539418
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import unittest

    class TestCase(unittest.TestCase):

        def test_tokenize_loop(self):
            mock_readline = io.StringIO(
                "x = 1\nprint(x)  # This is a comment.\n"
                "def myfunc(a, b):\n    c = a + b\n    return c\n"
            ).readline
            toklist = []

            def tokeneater(type, token, start, end, line):
                toklist.append((type, token))

            tokenize_loop(mock_readline, tokeneater)

# Generated at 2022-06-13 18:17:19.629270
# Unit test for function generate_tokens
def test_generate_tokens():
    def _make_tokenizer(s: str) -> Iterator[TokenInfo]:
        return generate_tokens(iter(s.splitlines()).next)

    def _make_tokenizer_and_cleaner(s: str) -> Iterator[TokenInfo]:
        it = _make_tokenizer(s)
        next(it)  # set line offset in cleaner
        return token_utils.generate_tokens_with_cleanup(it)

    def _decode_utf8(s: bytes) -> str:
        return s.decode("utf-8")

    def _check_decode_error(cookie: bytes) -> None:
        tokenizer = _make_tokenizer(cookie + "a=1")
        with pytest.raises(SyntaxError) as excinfo:
            list(tokenizer)


# Generated at 2022-06-13 18:17:29.270613
# Unit test for function tokenize
def test_tokenize():
    import io, token, tokenize
    readline = io.BytesIO(b"def f(x): return '%(x)s' % {'x': x}\n").readline
    tokens = []

    def tokeneater(*args):
        tokens.append(args)

    tokenize.tokenize(readline, tokeneater)

    # just check the first and last tokens
    assert tokens[0][:2] == (tokenize.NAME, "def")
    assert tokens[-3][0] == tokenize.ENDMARKER
    assert tokens[-2][0] == tokenize.ENCODING
    assert tokens[-1][0] == tokenize.NEWLINE



# Generated at 2022-06-13 18:17:36.818789
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import unittest
    source = io.BytesIO(
        b'\xef\xbb\xbf# -*- coding: iso-8859-1 -*-\n\n"""'
        + b"\xc3\xbf\xc3\xbe"
        + b'"\n'
    )
    encoding, consumed = detect_encoding(source.readline)
    assert encoding == "iso-8859-1"
    assert consumed == [b"\xef\xbb\xbf# -*- coding: iso-8859-1 -*-\n", b"\n", b"\xc3\xbf\xc3\xbe\n"]

    source = io.BytesIO(b"")
    encoding, consumed = detect_encoding(source.readline)
    assert encoding

# Generated at 2022-06-13 18:17:46.652273
# Unit test for function detect_encoding
def test_detect_encoding(): # htest #
    from io import StringIO
    from blib2to3.pytree import Leaf

    def readline() -> bytes:
        raise AssertionError("readline() should not be called")

    assert detect_encoding(readline) == ("utf-8", [])

    # try some variations on "coding" in a comment
    for coding in ["coding", "coding:", "coding=", "coding=="]:
        lines = ["#" + coding + " utf-8"]
        expected = ("utf-8", lines)
        assert detect_encoding(iter(lines).__next__) == expected

    # try some variations on spaces in a comment

# Generated at 2022-06-13 18:17:52.487311
# Unit test for function generate_tokens
def test_generate_tokens():
    from token import tok_name
    with tokenize.open("untokenize.py") as f:
        for token in generate_tokens(f.readline):
            print(token)


        
test_generate_tokens()

is_token_subtype(
    NUMBER,
    [
        "(",
        "NUMBER",
        "1",
        (1, 0),
        (1, 1),
        "False",
        False,
        None,
        None,
        None,
        None,
        None,
        0,
        0,
        None,
    ],
)

with tokenize.open("untokenize.py") as f:
    for token in tokenize.generate_tokens(f.readline):
        print(token)


# Generated at 2022-06-13 18:18:00.946458
# Unit test for function detect_encoding
def test_detect_encoding():
    import cStringIO
    import codecs

    def get_reader(text: bytes) -> Iterator[bytes]:
        stream = cStringIO.StringIO(text)
        readline = stream.readline
        yield readline()
        while True:
            yield readline()

    # Empty files
    res = detect_encoding(iter([]))
    assert res == ("utf-8", [])

    # Pass first line to detect_encoding
    res = detect_encoding(get_reader("# -*- coding: latin-1 -*-"))
    assert res == ("iso-8859-1", ["# -*- coding: latin-1 -*-"])

    # Pass first two lines to detect_encoding

# Generated at 2022-06-13 18:18:10.792502
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    input = [
        (token.NUMBER, "1", (1, 0), (1, 1), "1"),
        (token.NAME, "x", (1, 1), (1, 2), "x"),
        (token.NEWLINE, "\n", (1, 2), (2, 0), "\n"),
        (token.INDENT, "\t", (2, 0), (2, 0), None),
        (token.NUMBER, "2", (2, 0), (2, 1), "2"),
        (token.DEDENT, "", (2, 4), (2, 4), None),
        (token.NEWLINE, "\n", (2, 4), (3, 0), "\n"),
        (token.ENDMARKER, "", (3, 0), (3, 0), None),
    ]
    expected

# Generated at 2022-06-13 18:18:15.652852
# Unit test for function generate_tokens
def test_generate_tokens():
    types = set()
    for t in generate_tokens(
        """  ( ) [] {} ' ' 'a' " " "a" + - * / = , ''' ''' """
    ):
        type, value, _, _, _ = t
        types.add(type)
        assert value != "", str(t)
    assert types == set(
        (
            ERRORTOKEN,
            INDENT,
            DEDENT,
            LPAR,
            RPAR,
            LSQB,
            RSQB,
            LBRACE,
            RBRACE,
            SQUOTE,
            DQUOTE,
            PLUS,
            MINUS,
            STAR,
            SLASH,
            EQEQUAL,
            COMMA,
            NAME,
            ENDMARKER,
        )
    )

# Generated at 2022-06-13 18:18:24.273750
# Unit test for function generate_tokens
def test_generate_tokens():
    a = [
        "print('Hello')",
        "i = 7",
        "x == 2",
        "if True:",
        "    print('hello')",
        "    print('goodbye')",
        "print('done')",
    ]
    # 'import re; print (re.__doc__)'
    tokens = generate_tokens(iter(a).__next__)
    out = [t for t in tokens]
    print("\n".join(repr(x) for x in out))

# Generated at 2022-06-13 18:18:25.277059
# Unit test for function tokenize_loop
def test_tokenize_loop():
    tokeneater = TokenEater
    tokenize_loop(tokeneater)



# Generated at 2022-06-13 18:20:50.601934
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    u = Untokenizer()

    def helper(tokens):
        return u.untokenize(iter(tokens))

    assert helper([(1, "1"), (2, "2")]) == "1 2"
    assert helper([(1, "1"), (2, "2"), (3, "3"), (4, "4")]) == "1 2 3 4"
    assert helper([(1, "1"), (2, "2"), (3, "3"), (2, "2")]) == "1 2 3 2"

# Generated at 2022-06-13 18:20:54.062948
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def readline():
        print("tokenize_loop")
        return "tokenize_loop"

    def tokeneater(*argv):
        print("tokenize_loop", argv)

    tokenize_loop(readline, tokeneater)



# Generated at 2022-06-13 18:21:00.933791
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import io
    sample = b"# Test comment\n@attr\n"
    readline = io.BytesIO(sample).readline  # Function that acts as a file
    tokeneater = []
    tokenize_loop(readline, tokeneater.append)

    expected = [
        (tokenize.COMMENT, b"# Test comment", (1, 0), (1, 15), b"# Test comment"),
        (tokenize.OP, b"@", (2, 0), (2, 1), b"@attr"),
        (tokenize.NAME, b"attr", (2, 1), (2, 5), b"@attr"),
        (tokenize.NEWLINE, b"", (2, 5), (2, 5), b"@attr"),
    ]

    assert tokeneater == expected

# Generated at 2022-06-13 18:21:14.673901
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> bytes:
        return b"# coding: utf-8"

    assert detect_encoding(readline) == ("utf-8", [])
    readline.__code__.co_filename = "example"

    def readline() -> bytes:
        return b"#!/usr/bin/python3\n# coding: utf-8"

    assert detect_encoding(readline) == ("utf-8", [b"#!/usr/bin/python3\n"])
    readline.__code__.co_filename = "example"

    def readline() -> bytes:
        return b"\xef\xbb\xbf# coding: utf-8"

    assert detect_encoding(readline) == ("utf-8-sig", [])
    readline.__code__.co

# Generated at 2022-06-13 18:21:17.195413
# Unit test for function tokenize_loop

# Generated at 2022-06-13 18:21:26.554851
# Unit test for function detect_encoding
def test_detect_encoding():

    def readline():
        yield b"#!/usr/bin/python3"
        yield b"# vim: set fileencoding=latin-1 :"
        raise StopIteration

    assert detect_encoding(readline) == ("iso-8859-1", [b"#!/usr/bin/python3", b"# vim: set fileencoding=latin-1 :"])

    def readline():
        yield b"\xef\xbb\xbf# -*- coding: latin-1 -*-"
        raise StopIteration

    assert detect_encoding(readline) == ("iso-8859-1", [b"\xef\xbb\xbf# -*- coding: latin-1 -*-"])


# Generated at 2022-06-13 18:21:34.479391
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
  from . import tokenize
  import io
  from typing import cast, Any
  from blib2to3.pgen2.token import *
  rio = io.StringIO('')
  un = Untokenizer()
  for t in tokenize.generate_tokens(rio.readline):
    if t[0]==OP:
      un.compat(cast(Any,t),tokenize.generate_tokens(rio.readline))
      break


# Generated at 2022-06-13 18:21:44.498557
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    from token import *


# Generated at 2022-06-13 18:21:59.056101
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    import io
    import blib2to3.pygram as pygram
    import blib2to3.pytree as pytree
    import blib2to3.pgen2.tokenize as tokenize
    import blib2to3.pgen2.driver as driver

    # Test embedded newlines and indents
    u = Untokenizer()

# Generated at 2022-06-13 18:22:10.432067
# Unit test for function detect_encoding
def test_detect_encoding():

    def readline(s):
        for ch in s:
            yield ch

    def readline_iterable(s):
        def gen():
            yield s
        return gen

    def readlines(*args, **kwargs):
        return iter(args)

    s = b"# -*- coding: iso-8859-1 -*-\n# blah blah"
    assert detect_encoding(readline(s)) == ("iso-8859-1", [s])

    s = b"# -*- coding: iso-8859-1 -*-\r\n# blah blah\r\n"
    assert detect_encoding(readline(s)) == ("iso-8859-1", [s])

    s = b"# -*- coding=iso-8859-1 -*-\n# blah blah"
