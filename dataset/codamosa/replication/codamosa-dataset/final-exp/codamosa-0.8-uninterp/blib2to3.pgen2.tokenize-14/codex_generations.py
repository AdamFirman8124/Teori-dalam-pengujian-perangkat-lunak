

# Generated at 2022-06-13 18:14:16.978194
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    from .tokenize import (
        generate_tokens,
        TokenInfo,
        NL,
        COMMENT,
        NAME,
        OP,
        ERRORTOKEN,
        ENCODING,
        NEWLINE,
        NUMBER,
        STRING,
    )
    from . import token

    def test():
        with tokenize.open(__file__) as f:
            first_line = next(f)
            encoding = tokenize.detect_encoding(f.readline)[0]
        with tokenize.open(__file__, encoding=encoding) as f:
            ut = Untokenizer()
            tokgen = generate_tokens(f.readline)
            tokgen = iter(tokgen)
            first_token = next(tokgen)

# Generated at 2022-06-13 18:14:23.957380
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO
    from .tokenize import untokenize as real_untokenize
    from .tokenize import generate_tokens
    from .pytokenize import untokenize as fake_untokenize

    # Write a small Python program
    prog = StringIO("def f(x): return 2*x")
    untok = Untokenizer()
    tokgen = generate_tokens(prog.readline)
    result = untok.compat(next(tokgen), tokgen)
    # Assert that fake_untokenize is identical to real_untokenize
    # Note that we're not comparing the tokens against each other
    # since it's possible for them to be in a different order
    assert fake_untokenize(prog.getvalue()) == real_untokenize(prog.getvalue())

# Generated at 2022-06-13 18:14:33.953339
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> Text:
        if not lines:
            raise StopIteration
        line = lines.pop(0)
        return line if isinstance(line, bytes) else line.encode("utf-8")

    # No coding spec specified
    lines = ["spam", "eggs"]
    encoding, consumed = detect_encoding(readline)
    assert encoding == "utf-8"
    assert consumed == []

    # Only encoding cookie given
    lines = ["# coding=utf-8", "spam", "eggs"]
    encoding, consumed = detect_encoding(readline)
    assert encoding == "utf-8"
    assert consumed == [x.encode("utf-8") for x in lines]

    # Invalid coding cookie
    lines = ["# coding=invalid", "spam", "eggs"]
   

# Generated at 2022-06-13 18:14:41.103876
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from .token import generate_tokens
    from io import StringIO

    untok = Untokenizer()

    def untokenize(code: Text) -> Text:
        return untok.untokenize(generate_tokens(StringIO(code).readline))


# Generated at 2022-06-13 18:14:44.965612
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO
    from tokenize import tokenize

    text = "class C:\n    pass\n"
    file = StringIO(text)
    tokgen = tokenize(file.readline)
    Untokenizer().compat(next(tokgen), tokgen)



# Generated at 2022-06-13 18:14:56.884839
# Unit test for function generate_tokens
def test_generate_tokens():
    # Test basic tokenizing of a string
    token_list = list(generate_tokens(io.StringIO("print('foo')").readline))
    assert len(token_list) == 5
    assert token_list[0][:2] == (NAME, "print")
    assert token_list[1][:2] == (OP, "(")
    assert token_list[1][4] == "print('foo')"
    assert token_list[2][:2] == (STRING, "foo")
    assert token_list[2][4] == "print('foo')"
    assert token_list[3][:2] == (OP, ")")
    assert token_list[3][4] == "print('foo')"
    assert token_list[4][:2] == (ENDMARKER, "")

# Generated at 2022-06-13 18:15:09.548617
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import tokenize as tokenize2

    def tokenize2_loop(readline, tokeneater):
        try:
            tokenize2.tokenize(readline, tokeneater)
        except tokenize2.TokenError as e:
            print(f"TokenError: {e!r}")

    def test(*inputs):
        r = io.StringIO(input="".join(inputs))
        tokenize_loop(r.readline, printtoken)
        r = io.StringIO(input="".join(inputs))
        tokenize2_loop(r.readline, printtoken)
        print()


# Generated at 2022-06-13 18:15:14.784313
# Unit test for function tokenize
def test_tokenize():
    import io
    import token
    import tokenize
    r = io.StringIO("print(1)\n  1")
    tokeneater = lambda *args, **kwargs: print(*args, **kwargs)
    tokenize.tokenize(r.readline, tokeneater)

test_tokenize()



# Generated at 2022-06-13 18:15:19.448258
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for i in range(4):
            yield bytes([i, 0, 0, 0])

    def check(first, second, expected):
        encoding, lines = detect_encoding(readline())
        assert encoding == expected, (first, second, encoding)
        assert len(lines) == 2, (first, second, lines)
        assert lines[0] == bytes([first, 0, 0, 0])
        assert lines[1] == bytes([second, 0, 0, 0])

    yield check, 0, 0, "utf-8"
    yield check, 255, 0, "utf-8"
    yield check, 0, 255, "utf-8"
    yield check, 255, 255, "utf-8"



# Generated at 2022-06-13 18:15:29.460357
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        # This function mimicks the iteration protocol of readline()
        # methods of file-like objects.
        for line in [
            b'# -*- coding: latin-1 -*-\n',
            b'import sys\n',
        ]:
            yield line

    ret = detect_encoding(readline)
    assert ret[0] == 'iso-8859-1'
    assert len(ret[1]) == 2

    def readline():
        for line in [
            b'\xef\xbb\xbf# -*- coding: latin-1 -*-\n',
            b'\xef\xbb\xbfimport sys\n',
        ]:
            yield line

    ret = detect_encoding(readline)

# Generated at 2022-06-13 18:15:59.622676
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline() -> Iterator[bytes]:
        for line in [
            b'Why are canaries yellow?\n',
            b'\n',
            b'To match the color of their legs!\n',
        ]:
            yield line

    encoding, consumed = detect_encoding(readline)
    assert encoding == "utf-8"
    assert consumed == [
        b'Why are canaries yellow?\n',
        b'\n',
        b'To match the color of their legs!\n',
    ]

    def readline() -> Iterator[bytes]:
        for line in [b'\ufeffWhy are canaries yellow?\n', b'\n']:
            yield line

    encoding, consumed = detect_encoding(readline)
    assert encoding == "utf-8-sig"
   

# Generated at 2022-06-13 18:16:08.228443
# Unit test for function detect_encoding
def test_detect_encoding():
    # Test detection based on the BOM
    def readline():
        yield BOM_UTF8
        yield b'# -*- coding: cp1252 -*-\n'

    enc, lines = detect_encoding(readline)
    assert enc == 'utf-8-sig'
    assert lines == [BOM_UTF8, b'# -*- coding: cp1252 -*-\n']

    # Test detection based on the coding spec
    def readline():
        yield b'# -*- coding: cp1252 -*-\n'
        yield b'#!/usr/bin/env python\n'

    enc, lines = detect_encoding(readline)
    assert enc == 'cp1252'

# Generated at 2022-06-13 18:16:20.609400
# Unit test for function tokenize_loop
def test_tokenize_loop():
    from io import StringIO
    from types import BuiltinFunctionType

    def test_generator(s):
        for c in s:
            yield c

    s = "if 1: # One\n  pass  # Two\n"
    result = []
    tokenize_loop(test_generator(s).__next__, result.append)

# Generated at 2022-06-13 18:16:25.758378
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        while 1:
            yield ""

    assert detect_encoding(readline) == ("utf-8", [])

    def readline():
        yield b"# coding: latin-1\n"

    assert detect_encoding(readline) == ("iso-8859-1", [b"# coding: latin-1\n"])

    def readline():
        yield b"\xEF\xBB\xBF# coding: latin-1\n"

    assert detect_encoding(readline) == ("utf-8-sig", [b"# coding: latin-1\n"])

    def readline():
        yield b"# coding: latin-1\n"
        yield b"\xEF\xBB\xBF# coding: ascii\n"


# Generated at 2022-06-13 18:16:30.818781
# Unit test for function detect_encoding
def test_detect_encoding():
    first = b"# coding: latin-1\n"
    second = b"# vim:fileencoding=utf-8\n"

    def readline():
        yield first
        yield second

    encoding, lines = detect_encoding(readline())
    assert encoding == "latin-1"
    assert lines == [first, second]

# Generated at 2022-06-13 18:16:41.673607
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO


# Generated at 2022-06-13 18:16:50.533023
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from textwrap import dedent
    from cStringIO import StringIO
    from .tokenize import tokenize as _tokenize
    ut = Untokenizer()
    utokens = ut.compat(
        next(_tokenize(StringIO(dedent("""\
            pass
            5
            x = 5
            "string"
            def f(x):
                return x
            """)).readline)),
        iter(_tokenize(StringIO(dedent("")))),
    )
    expected = "pass 5 x = 5 \"string\" def f(x): return x\n"
    assert utokens == expected, repr(utokens)

# Test transformation
from .tokenize import detect_encoding, read_random_lines

# Generated at 2022-06-13 18:17:04.208901
# Unit test for function generate_tokens
def test_generate_tokens():
    import token
    from io import BytesIO
    from typing import List
    from typing_extensions import Literal

    def _format(tokens: List[GoodTokenInfo]) -> str:
        return "".join(_format_token(token) for token in tokens)


# Generated at 2022-06-13 18:17:15.727141
# Unit test for function generate_tokens
def test_generate_tokens():
    import unittest
    import sys
    import re


# Generated at 2022-06-13 18:17:25.895413
# Unit test for function tokenize
def test_tokenize():
    import io
    import token
    r = io.StringIO(
        """while 1:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
"""
    )
    result = []
    tokeneater = result.append
    tokenize(r.readline, tokeneater)

# Generated at 2022-06-13 18:18:26.545640
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    untok_prog = re.compile(r"\w+")
    compat_prog = re.compile(r"\d+")
    for s in [
        "a b+1 2",
        "a\n4\n5",
        "\n4\n5",
        "for i in range(10):\n print i\n",
    ]:
        untok = Untokenizer()
        def test_tokeneater(
            x: int,
            y: str,
            z: Tuple[int, int],
            z1: Tuple[int, int],
            z2: str,
        ) -> None:
            pass

        tokenize(s.splitlines(True).__iter__, test_tokeneater)

# Generated at 2022-06-13 18:18:37.120250
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
    # Empty token list
    u = Untokenizer()
    assert u.tokens == []
    # Not adding whitespace
    u.add_whitespace((2, 3))
    # Adding whitespace
    u.add_whitespace((1, 1))
    assert u.tokens == ["\n", "\n"]
    # Adding whitespace on same row
    u.tokens = []
    u.add_whitespace((1, 2))
    assert u.tokens == [" "]
    # Adding whitespace on same row, but different column
    u.tokens = []
    u.add_whitespace((1, 3))
    assert u.tokens == ["  "]
    # Adding whitespace on same row, but different column, with a single newline
    u.tokens

# Generated at 2022-06-13 18:18:39.203769
# Unit test for function printtoken
def test_printtoken():
    printtoken(3, 'abc', (0, 10), (0,20), 'def')


# Generated at 2022-06-13 18:18:50.549281
# Unit test for method add_whitespace of class Untokenizer
def test_Untokenizer_add_whitespace():
    def check(a, b):
        u = Untokenizer()
        u.prev_row = a[0]
        u.prev_col = a[1]
        u.add_whitespace(b)
        assert u.prev_row == b[0]
        assert u.prev_col == b[1]

    yield check, (1, 1), (1, 1)
    yield check, (1, 1), (1, 2)
    yield check, (1, 1), (1, 10)
    yield check, (1, 1), (2, 1)
    yield check, (2, 1), (2, 1)
    yield check, (1, 2), (1, 1)
    yield check, (1, 1), (2, 2)
    yield check, (2, 2), (2, 3)


# Generated at 2022-06-13 18:18:51.866931
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import tokenize as tk
    with io.StringIO('a = 3') as file:
        tk.tokenize_loop(file.readline, print)

# backwards compatible interface

# Generated at 2022-06-13 18:19:00.225570
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(*lines: bytes) -> Callable[[], bytes]:
        if len(lines) == 0:
            raise StopIteration()
        else:
            return lambda: lines[0]

    def assert_enc(expected: str, *lines: bytes):
        assert detect_encoding(readlines(*lines)) == (expected, list(lines))

    # no encoding declaration

# Generated at 2022-06-13 18:19:10.220514
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    from io import StringIO
    import tokenize

    class Readline:
        def __init__(self, lines):
            self.lines = iter(lines)

        def __call__(self):
            try:
                return next(self.lines)
            except StopIteration:
                return ""

    def check(iterable, want):
        f = StringIO()
        tokenize.untokenize(iterable, f.write)
        got = f.getvalue()
        assert want == got


# Generated at 2022-06-13 18:19:13.809459
# Unit test for function printtoken
def test_printtoken():
    printtoken(NUMBER, "3", (1, 3), (1, 5), "abc 3 def")
    printtoken(NAME, "abc", (1, 2), (1, 5), "abc 3 def")
    printtoken(NAME, "abc", (1, 2), (1, 5), "abc 3 def")



# Generated at 2022-06-13 18:19:15.696829
# Unit test for function printtoken
def test_printtoken():
    printtoken(
        tokenize.STRING, "test", (1, 2), (3, 4), "this is a line for testing"
    )

# Generated at 2022-06-13 18:19:23.312161
# Unit test for function generate_tokens
def test_generate_tokens():
    src = "def f():\n return 0\n"
    result = list(tokenize.generate_tokens(iter(src.splitlines(keepends=True)).__next__))

# Generated at 2022-06-13 18:20:13.306378
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:20:27.398191
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:20:39.237222
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    out = [
        "def foo():\n",
        "  print (42)\n",
        "  if sys.stdin.readline() in ('y', 'Y'):\n",
        "    return (1)\n",
        "  else:\n",
        "    return (2)\n",
        "  ",
    ]

    from .tokenize import generate_tokens

    with open("/tmp/foo.txt", "w") as f:
        f.write("".join(out))

    with open("/tmp/foo.txt") as f:
        tokens = generate_tokens(f.readline)

    result = Untokenizer().compat(next(tokens), tokens)
    assert "".join(out) == "".join(result)



# Generated at 2022-06-13 18:20:50.129729
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        for line in ("\xEF\xBB\xBFa" "\n# coding: latin-1\n",
                     "\n# coding: latin-1\n",
                     '\n# coding: invalid-charset\n',
                     '\n# coding: latin-1\n\n', '', '\n', 'b'):
            yield line.encode()

    def test(expected_encoding, expected_lines=()):
        enc, lines = detect_encoding(readline)
        if enc != expected_encoding or lines != [x.encode() for x in expected_lines]:
            raise AssertionError(f"encoding, lines = {enc, lines}")

    test("utf-8-sig", ("", "# coding: latin-1\n"))


# Generated at 2022-06-13 18:20:55.343256
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    data = (
        "def f():\n"
        "    a = b + c\n"
        "    return a"
    )
    expected = "def f():\n" \
               "    a = b + c\n" \
               "    return a "
    ut = Untokenizer()
    actual = ut.untokenize(generate_tokens(data.splitlines(True)))
    assert expected == actual, actual



# Generated at 2022-06-13 18:21:09.467316
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    import tokenize
    r = io.StringIO("print('hello world')").readline
    g = tokenize.generate_tokens(r)
    tokens = list(g)
    assert len(tokens) == 4
    t = tokens[0]
    assert t.type == tokenize.NAME
    assert t.string == "print"
    assert t.start == (1, 0)
    assert t.end == (1, 5)
    assert t.line == "print('hello world')\n"
    t = tokens[1]
    assert t.type == tokenize.OP
    assert t.string == "("
    t = tokens[2]
    assert t.type == tokenize.STRING
    assert t.string == "'hello world'"
    t = tokens[3]

# Generated at 2022-06-13 18:21:11.592755
# Unit test for function generate_tokens

# Generated at 2022-06-13 18:21:15.765374
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def my_tokenizer(token_info):
        print(token_info)

    for token_info in tokenize_loop(b'4\n4\n4\n', my_tokenizer):
        pass



# Generated at 2022-06-13 18:21:19.018345
# Unit test for function generate_tokens
def test_generate_tokens():
    for t in generate_tokens(iter(("\xB2 = 3\n",)).__next__):
        print(t)


# Generated at 2022-06-13 18:21:25.741235
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    import tokenize
    untok = Untokenizer()
    source = '''def f():
    print('hello world')
'''
    with open('tokenize_test.py', 'w') as f:
        f.write(source)
    with open('tokenize_test.py', 'rb') as f:
        tokens = list(tokenize.tokenize(f.readline))
    os.remove('tokenize_test.py')
    source_annotated = untok.untokenize(tokens)
    assert source_annotated == source
