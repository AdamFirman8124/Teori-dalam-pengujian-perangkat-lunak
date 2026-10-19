

# Generated at 2022-06-13 18:14:39.321227
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    x = Untokenizer()
    x.compat((1, "1"), [(1, "2")])


# Generated at 2022-06-13 18:14:48.437369
# Unit test for function tokenize
def test_tokenize():
    from io import StringIO

    def readline():
        return next(l)


# Generated at 2022-06-13 18:14:55.608997
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    # Based on test case from ntokenize.py.
    it = iter([(1, ''), (2, 'ab'), (3, 'c'), (3, ''), (5, 'a'), (5, ''), (4, '')])
    u = Untokenizer()
    assert u.compat((1, ''), it) is None
    assert u.tokens == []
    assert list(it) == [(2, 'ab'), (3, 'c'), (3, ''), (5, 'a'), (5, ''), (4, '')]




# Generated at 2022-06-13 18:15:03.233329
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from blib2to3.pgen2.tokenize import generate_tokens
    a = list(generate_tokens(iter(["\n"]).__next__))
    u = Untokenizer()
    u.compat(a[0], iter(a[1:]))
    assert u.tokens == ["\n"]


# Utility functions

# Generated at 2022-06-13 18:15:06.082979
# Unit test for function tokenize_loop
def test_tokenize_loop():
    tokenize_loop(test_tokenize_generate_tokens, printtoken)


# Unit tests for function tokenize

# Generated at 2022-06-13 18:15:16.362558
# Unit test for function tokenize
def test_tokenize():
    import io, token
    from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
    readline = io.BytesIO(
        b'f(x, y# comment\n, *args, **kwds)\n'
        b'"""docstring"""\n'
        b'class C: pass\n'
        b'a, b = 1, 2; c = 3; (d, e) = 4, 5\n'
    ).readline
    tokens = list(tokenize(readline))

# Generated at 2022-06-13 18:15:26.561688
# Unit test for function detect_encoding
def test_detect_encoding():
    import io, tokenize
    readline = io.BytesIO("a").readline
    assert tokenize.detect_encoding(readline) == ('utf-8', [b'a'])
    readline = io.BytesIO("# coding: latin-1\n" "a").readline
    assert tokenize.detect_encoding(readline) == ('iso-8859-1', [b'a'])
    readline = io.BytesIO("\xef\xbb\xbf" "a").readline
    assert tokenize.detect_encoding(readline) == ('utf-8-sig', [b'a'])
    readline = io.BytesIO("\xef\xbb\xbf" "# coding: latin-1\n" "a").readline
    assert tokenize.det

# Generated at 2022-06-13 18:15:35.407005
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO

    f = StringIO("def f(): return 42\n")
    result = list(generate_tokens(f.readline))

# Generated at 2022-06-13 18:15:41.209016
# Unit test for function detect_encoding
def test_detect_encoding():

    def readline_helper(lines):
        def readline():
            line = next(lines)
            if not isinstance(line, bytes):
                line = line.encode("ascii")
            return line

        return readline

    lines = [
        "# coding: latin-1\n",
        'print("nepůlnoční řeči")\n',
    ]
    encoding, _ = detect_encoding(readline_helper(iter(lines)))
    assert encoding == "iso-8859-1"

    lines = [
        'print("nepůlnoční řeči")\n',
        "# coding: latin-1\n",
    ]
    encoding, _ = detect_encoding(readline_helper(iter(lines)))


# Generated at 2022-06-13 18:15:48.228907
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO

    from typing import Text

    from .tokenize_rt import _string_to_tokens, _token_list_cmp

    # Test first line of a file
    fp = StringIO("# coding: utf-8\n")
    toks = list(tokenize.generate_tokens(fp.readline))

# Generated at 2022-06-13 18:18:39.147335
# Unit test for function tokenize
def test_tokenize():
    import io, token
    r = io.BytesIO(b"def x(): pass\n")
    tokenize(r.readline)

test_tokenize()



# Generated at 2022-06-13 18:18:50.537698
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        return b'\xef\xbb\xbf# -*- coding: latin-1 -*-\n'
    assert detect_encoding(readline) == ('iso-8859-1', [b'# -*- coding: latin-1 -*-\n'])
    def readline():
        return b'\xef\xbb\xbf# coding=latin-1\n'
    assert detect_encoding(readline) == ('iso-8859-1', [b'# coding=latin-1\n'])
    def readline():
        return b'\xef\xbb\xbf# -*- coding: ascii -*-\n'

# Generated at 2022-06-13 18:18:54.985257
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    tok = tokenize.Untokenizer()
    tok.compat((5, "if"), [(5, "if"), (1, " "), (4, ":"), (4, " "), (4, "pass")])
    assert tok.tokens == ["if ", ":", " ", "pass"]



# Generated at 2022-06-13 18:19:03.986509
# Unit test for function tokenize_loop
def test_tokenize_loop():
    s = "def f(x): return x+1"
    result = []
    tokenize_loop(iter(s.splitlines()).__next__, result.append)

# Generated at 2022-06-13 18:19:08.802754
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# coding: latin-1\n"
        yield b"#\n"
        yield b"a = 1; b = 2; c = 3\n"
        raise StopIteration

    res = detect_encoding(readline)
    assert res == ("iso-8859-1", [b"# coding: latin-1\n", b"#\n"])



# Generated at 2022-06-13 18:19:19.626963
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO
    from blib2to3.pgen2.tokenize import generate_tokens, untokenize
    from blib2to3.pgen2.token import tokenize
    for source in (
        '@a\n def g():\n  x = 1\n  return x',
        "if 1:\n print(2)\n",
        'try:\n 1/0\n except ZeroDivisionError:\n  print(1)\n else:\n  print(2)',
        "a = 1\n",
    ):
        g = generate_tokens(StringIO(source).readline)
        u = Untokenizer()
        result = u.untokenize(g)
        got = untokenize(tokenize(StringIO(source).readline)).strip()

# Generated at 2022-06-13 18:19:28.425673
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(seq):
        for i in seq:
            yield i

    def test(input, expected_encoding, expected_first_line=b""):
        encoding, first_line = detect_encoding(readlines(input))
        assert encoding == expected_encoding
        assert first_line == [expected_first_line]

    # test utf-8 bom
    test([BOM_UTF8 + b"#coding:cp1252"], "utf-8-sig", BOM_UTF8 + b"#coding:cp1252")
    test([BOM_UTF8 + b"#!/usr/bin/env python3", b"#coding:cp1252"], "utf-8-sig")

# Generated at 2022-06-13 18:19:36.187324
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# -*- coding: iso-8859-1 -*-"
        yield b"\x0a"
        raise StopIteration

    result = detect_encoding(readline())
    assert result == ("iso-8859-1", [b"# -*- coding: iso-8859-1 -*-\n"])

    def readline():
        yield b"# coding: iso-8859-1"
        yield b"\x0a"
        raise StopIteration

    result = detect_encoding(readline())
    assert result == ("iso-8859-1", [b"# coding: iso-8859-1\n"])

    def readline():
        yield b"# coding=iso-8859-1"
        yield b"\x0a"
       

# Generated at 2022-06-13 18:19:39.067516
# Unit test for function tokenize
def test_tokenize():
    s = "def f(): pass\n"
    l = s.split("\n")
    g = tokenize(l.__iter__().__next__)
    for t in g:
        pass



# Generated at 2022-06-13 18:19:46.300915
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        while True:
            yield b"# coding: latin-1\n"
            yield b"#! /usr/bin/env python\n"
            yield b"# coding: latin-2\n"
            yield b"# -*- coding: latin-3 -*-\n"
            yield b"# vim: set fileencoding=latin-4 :\n"
            yield b"# -*- coding: iso-latin-1 -*-\n"
            yield b"\n"
            yield b"# coding=iso-8859-1\n"
            yield b"# coding=iso-8859-15\n"
            yield b"# coding=ascii\n"
            yield b"# coding=utf-8\n"

# Generated at 2022-06-13 18:20:31.707775
# Unit test for function detect_encoding
def test_detect_encoding():
    # sample cookie with whitespace and extra junk
    x = " #   vim:set fileencoding=latin-1 :  "
    cookie_len = len(x) - 1
    def readline() -> bytes:
        return x


    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"
    assert lines == [x]
    # test BOM detection
    def readline() -> bytes:
        return BOM_UTF8 + x


    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8-sig"
    assert lines == [BOM_UTF8 + x]
    # test multiple lines
    def readline() -> bytes:
        return x + "\r\n"



# Generated at 2022-06-13 18:20:36.268795
# Unit test for function generate_tokens
def test_generate_tokens():
    import io
    r = io.StringIO("""\
      if 1:
          def f():
              pass
        """).readline
    result = list(tokenize.generate_tokens(r))

# Generated at 2022-06-13 18:20:46.285957
# Unit test for function tokenize
def test_tokenize():
    import io
    from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP

    f = io.StringIO("1 + 2\n")
    tokens = tokenize(f.readline)
    assert next(tokens) == (NUMBER, "1", (1, 0), (1, 1), "\n")
    assert next(tokens) == (OP, "+", (1, 2), (1, 3), "\n")
    assert next(tokens) == (NUMBER, "2", (1, 4), (1, 5), "\n")
    assert next(tokens) == (ENDMARKER, "", (2, 0), (2, 0), "")
    f = io.StringIO("1 + 2\n")
    tokens = list(tokenize(f.readline))

# Generated at 2022-06-13 18:20:54.686153
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    untok = Untokenizer()
    source = (
        (NAME, "def"),
        (NAME, "f"),
        (OP, "("),
        (OP, ")"),
        (OP, ":"),
        (NEWLINE, "\n"),
        (INDENT, "\t"),
        (NAME, "return"),
        (NAME, "None"),
        (NEWLINE, "\n"),
        (DEDENT, ""),
    )

    expected_result = "def f():\n\treturn None\n"
    result = untok.untokenize(source)
    assert result == expected_result



# Generated at 2022-06-13 18:21:08.290957
# Unit test for function generate_tokens
def test_generate_tokens():
    def tokenize_print(filename):
        """Print tokens corresponding to the Python source file filename."""
        with open(filename) as f:
            return list(generate_tokens(f.readline))

    def expect_tokenize_py2(filename, expected_tokenize_output):
        if sys.version_info < (3, 0):
            tokenize_output = tokenize_print(filename)
            check_tokenize_py2(filename, expected_tokenize_output, tokenize_output)

    def check_tokenize_py2(filename, expected, actual):
        def munge(tokens):
            result = []
            for tok in tokens:
                tok = list(tok[:])

# Generated at 2022-06-13 18:21:12.769194
# Unit test for function tokenize_loop
def test_tokenize_loop():
    """Test tokenize_loop."""
    from io import StringIO
    from tokenize import tokenize

    text = "a + b"
    FILE = StringIO(text)
    tokenize(FILE.readline, printtoken)



# Generated at 2022-06-13 18:21:23.289576
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    ut = Untokenizer()
    ut.compat((110, 'print('), iter([(57, '"hello"'), (41, ')')]))
    assert ut.tokens == ['print(', '"hello"', ') ']
    ut.tokens = []
    ut.compat((110, 'print('), iter([(57, '"hello"'), (55, '+'), (57, '"world"'), (41, ')')]))
    assert ut.tokens == ['print(', '"hello"', '+', '"world"', ') ']
    ut.tokens = []

# Generated at 2022-06-13 18:21:31.674582
# Unit test for function generate_tokens
def test_generate_tokens():
    import re
    import sys
    import token

    def _print_token(tok):
        if tok[0] == tokenize.ENCODING:
            return
        print(token.tok_name[tok[0]], tok[1], tok[2], tok[3], tok[4])

    def _token_stream(s):
        return tokenize.generate_tokens(io.StringIO(s).readline)

    def _check_token_stream(s, *expect):
        got = _token_stream(s)
        for x in expect:
            _print_token(next(got))
        try:
            _print_token(next(got))
        except StopIteration:
            pass

# Generated at 2022-06-13 18:21:40.780234
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO

    untok = Untokenizer()
    u = untok.compat
    u((NAME, "if"))
    u((NAME, "True"))
    u((OP, ":"))
    u((NEWLINE, "\n"))
    u((INDENT, "\t"))
    u((NAME, "x"))
    u((OP, "="))
    u((NUMBER, "1"))
    u((NEWLINE, "\n"))
    u((DEDENT, ""))
    u((NAME, "if"))
    u((OP, ":"))
    u((NEWLINE, "\n"))
    u((ENDMARKER, ""))

# Generated at 2022-06-13 18:21:44.782502
# Unit test for function tokenize_loop
def test_tokenize_loop():
    tokeneater = token.TokenInfo(ENDMARKER, "", (0, 0), (0, 0), "")
    assert(tokenize_loop(tokeneater, tokeneater) == None)



# Generated at 2022-06-13 18:22:15.978054
# Unit test for function tokenize_loop
def test_tokenize_loop():
    def tokenize_loop(readline, tokeneater):
        for token in generate_tokens(readline):
            tokeneater(*token)



# Generated at 2022-06-13 18:22:25.523591
# Unit test for function generate_tokens
def test_generate_tokens():
    import re
    import sys
    from token import STRING, NAME, NUMBER, OP, ERRORTOKEN, DEDENT, ENDMARKER

    def _main():
        args = sys.argv[1:]
        try:
            tokenize_print(args[0])
        except IOError as err:
            print(err)

    def tokenize_print(filename):
        with open(filename) as f:
            try:
                for token in generate_tokens(f.readline):
                    token_type = token_name(token[0])
                    print(token_type, token)
            except TokenError as err:
                print(err)

    def token_name(token_number: Any) -> str:
        """
        Return the name of the given token number
        """
        # See token.py