

# Generated at 2022-06-13 18:14:36.737864
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    import io
    import tokenize
    from blib2to3.pygram import python_symbols as syms
    from blib2to3.pgen2.token import tok_name
    from tester import test_tokenize_untokenize

    # We feed in a pair of tokens, the second of which triggers the
    # "compatibility mode" branch in the untokenizer.
    untok = Untokenizer()
    class Readline:
        def __init__(self, *seq):
            self.seq = seq
            self.i = 0
        def __call__(self):
            if self.i >= len(self.seq):
                raise EOFError
            s = self.seq[self.i]
            self.i += 1
            return s

# Generated at 2022-06-13 18:14:41.670400
# Unit test for function tokenize
def test_tokenize():
    f = open(__file__)  # this file
    try:
        readline = f.readline
        for token in generate_tokens(readline):
            print(token)
    finally:
        f.close()



# Generated at 2022-06-13 18:14:49.163581
# Unit test for function tokenize_loop

# Generated at 2022-06-13 18:14:58.177315
# Unit test for function tokenize
def test_tokenize():
    import io
    import tokenize as _tokenize

    s = "def f(x):\n return x+1\n"
    f = io.StringIO(s)
    got_tokens = []

    def tokeneater(x, y, z, w, v):
        got_tokens.append((x, y, v))

    _tokenize.tokenize(f.readline, tokeneater)
    got_tokens = [
        (i, j, k[-1])
        for i, j, k, _, _ in got_tokens
        if i == tokenize.NAME and j != "f"
    ]

# Generated at 2022-06-13 18:15:03.385760
# Unit test for function generate_tokens
def test_generate_tokens():
    import sys, pprint

    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        fn = __file__

    f = open(fn)
    pprint.pprint(list(tokenize(f.readline)))
    input()


if __name__ == "__main__":
    test_generate_tokens()

# TODO(jeff,guido): ideally we'd have a way to auto-generate
# a skeleton implementation of detect_encoding that would
# work for all types of files.

# Generated at 2022-06-13 18:15:05.290754
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO


# Generated at 2022-06-13 18:15:12.099265
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:15:14.200295
# Unit test for function tokenize
def test_tokenize():
    import io

    with io.StringIO("#testing\n1+1") as f:
        tokenize(f.readline)



# Generated at 2022-06-13 18:15:17.364115
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    untok = Untokenizer()
    str = untok.untokenize([(a, b) for a, b in tokenize(b"x = 0\n")])
    assert str == "x = 0\n"



# Generated at 2022-06-13 18:15:31.885507
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        yield b"# -*- coding: latin-1 -*-"
        yield b""
        yield b"x = '# -*- coding: latin-1 -*-';"
    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1" and b"".join(lines) == b"# -*- coding: latin-1 -*-\n\n"
    def readline():
        yield b"#!/usr/bin/env python3"
        yield b"# -*- coding: latin-1 -*-"
        yield b"# -*- coding: iso-8859-1 -*-"
        yield b"# -*- coding: utf-8 -*-"
        yield b"# -*- coding: unknown -*-"

# Generated at 2022-06-13 18:16:52.705106
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    from . import untokenize as untokenize1
    from .tokenize import untokenize as untokenize2
    untokenize = untokenize1.untokenize

    def compare(iterable):
        # Choose one of the two untokenize functions.
        result1 = untokenize1.untokenize(iterable)
        result2 = untokenize2(iterable)
        # print repr(result1), repr(result2)
        assert result1 == result2

    compare([(1, "  "), (2, "text"), (3, "\n"), (0, ""), (1, "")])

# Generated at 2022-06-13 18:17:05.236277
# Unit test for function generate_tokens
def test_generate_tokens():
    from tokenize import tokenize
    from io import BytesIO
    from unittest import TestCase

    class Test(TestCase):
        def check(self, text:str) -> None:
            buffer = BytesIO(text.encode("utf-8"))
            expected = list(tokenize(buffer.readline))
            buffer.seek(0)
            got = list(generate_tokens(buffer.readline))
            self.assertEqual(got, expected)

    def test():
        test = Test("check")
        test.check("")
        test.check("#")
        test.check("\n")
        test.check("a")
        test.check("a + b")
        test.check("  a + b")
        test.check("\n  a + b")
        test.check

# Generated at 2022-06-13 18:17:17.233627
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from unittest.mock import Mock
    stream = [
        (NAME, "def"),
        (INDENT, ""),
        (NAME, "print"),
        (OP, "("),
        (STRING, "'x'"),
        (OP, ")"),
        (DEDENT, ""),
        (NAME, "def"),
        (OP, "("),
        (NAME, "x"),
        (OP, ")"),
        (OP, ":"),
        (NEWLINE, "\n"),
        (NAME, "print"),
        (OP, "("),
        (STRING, "'y'"),
        (OP, ")"),
        (NEWLINE, "\n"),
        (ENDMARKER, ""),
    ]
    # We check that each call to the mock function corresponds to a
    # token in

# Generated at 2022-06-13 18:17:28.354247
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io
    import sys

    # Verify that we can pass a StringIO object as the only 'readline' argument.
    f = io.StringIO("class A:\n\tpass")
    tokenize_loop(f.readline, printtoken)

    # Verify that we can pass a list of strings as the 'readline' argument.
    tokenize_loop(iter(["class A:", "    pass"]).__next__, printtoken)

    # Verify that we can pass a function as the 'readline' argument.
    def my_readline():
        return "class A:\n\tpass"

    tokenize_loop(my_readline, printtoken)

    # Verify that passing a function that returns None as the 'readline'
    # argument raises a ValueError exception.
    def my_readline_none():
        return

# Generated at 2022-06-13 18:17:36.358531
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from io import StringIO

    def get_untokenizer():
        import untokenize

        return untokenize.Untokenizer()

    untok = get_untokenizer()
    # Test for no dedents
    tests = [
        "a = 1",
        "b = 23",
        "c = 345",
    ]
    # Test for single dedent
    tests += [
        "def moo():",
        "   a = 1",
        "   b = 23",
        "   c = 345",
    ]
    # Test for multiple dedents
    tests += [
        "def moo():",
        "    def cow():",
        "        a = 1",
        "        b = 23",
        "        c = 345",
    ]
    # Test for single

# Generated at 2022-06-13 18:17:41.950652
# Unit test for function detect_encoding
def test_detect_encoding():

    def _test(s, expected, correct_result=True):
        stream = iter(s.splitlines(True))
        result = detect_encoding(lambda: next(stream))
        if correct_result:
            assert result == expected
        else:
            assert result != expected

    # If no encoding is specified, the default is UTF-8.
    _test("", ("utf-8", []))
    _test("#!/usr/bin/env python3\n", ("utf-8", []))
    _test("# coding=utf-8\n", ("utf-8", []))
    _test("# coding: utf-8\n", ("utf-8", []))

    # Valid encodings are normalized and the line ending stripped
    _test("# coding=UTF-8\n", ("utf-8", []))
   

# Generated at 2022-06-13 18:17:53.654509
# Unit test for function detect_encoding
def test_detect_encoding():
    # Test with no BOM
    readline = lambda: bytes( "# coding: latin-1", 'ascii')
    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"

    def readline():
        yield bytes("# coding: latin-1", 'ascii')
        yield bytes("x = 'Andr\\xe9'", 'latin-1')

    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"

    # Test BOM detection
    def readline():
        yield BOM_UTF8
        yield bytes("# coding: utf-8", 'ascii')
        yield bytes("x = 'Andr\\xe9'", 'utf-8')


# Generated at 2022-06-13 18:18:01.807328
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import unittest
    import unittest.mock

    class ReadlineMock(unittest.mock.MagicMock):
        def __call__(self):
            if not self.call_count:
                return b"# encoding = 'utf-8'\n"
            if self.call_count == 1:
                return b"\n"
            raise StopIteration()

    # This should just work.
    encoding, lines = detect_encoding(ReadlineMock())
    assert encoding == "utf-8"
    assert lines == [b"# encoding = 'utf-8'\n", b"\n"]

    # Blank lines and comments should be ignored before the magic
    # comment, but they should be returned.
    readline = unittest.mock.MagicMock()
    read

# Generated at 2022-06-13 18:18:07.810835
# Unit test for function detect_encoding
def test_detect_encoding():    
    import io
    def readline():
        if '\n' in line:
            line, leftover = line.split('\n', 1)
            yield line + '\n'
            line = leftover
        else:
            raise StopIteration
    for line in """\
#!/usr/bin/python
# -*- coding: latin-1 -*-
pass
""".splitlines():
        assert detect_encoding(readline) == ('latin-1', ['#!/usr/bin/python\n'])

    for line in """\
#!/usr/bin/python
# vim: set fileencoding=latin-1:
pass
""".splitlines():
        assert detect_encoding(readline) == ('latin-1', ['#!/usr/bin/python\n'])


# Generated at 2022-06-13 18:18:08.463155
# Unit test for function tokenize_loop
def test_tokenize_loop():
    pass



# Generated at 2022-06-13 18:18:45.435872
# Unit test for function detect_encoding
def test_detect_encoding():
    # fake open()
    def my_open(encoding, lines):
        def readline():
            if lines:
                return lines.pop(0) + b"\r\n"
            else:
                raise StopIteration

        return readline

    def test(expected, line1, line2, *rest):
        result, lines = detect_encoding(my_open(expected, [line1, line2] + list(rest)))
        assert result == expected, result
        assert not lines, lines

    test("utf-8", b"# -*- coding: utf-8 -*-", b"")
    test("ascii", b"# -*- coding: ascii -*-", b"")

# Generated at 2022-06-13 18:18:55.810814
# Unit test for function generate_tokens
def test_generate_tokens():
    def testit(input, output):
        result = [(toktype, tokval) for toktype, tokval, (sline, scol), (eline, ecol), ltext in generate_tokens(input)]
        if result != output:
            import pprint, sys
            print("\nInput :", input, file=sys.stderr)
            print("Expected:", output, file=sys.stderr)
            print("Received:", pprint.pprint(result), file=sys.stderr)
            assert result == output

    testit("\n", [(1, ''), (4, '')])
    testit("a = 3\n", [(1, 'a'), (1, '='), (1, '3'), (4, '')])

# Generated at 2022-06-13 18:19:00.646593
# Unit test for function generate_tokens
def test_generate_tokens():
    from tokenize import generate_tokens
    s = "def factorial(n):\n\tresult = n\n\tfor i in range(1,n):\n\t\tresult *= i\n\treturn result\n"\
        + "result = factorial(5)\nprint(result)\n"
    for t in generate_tokens(iter(s.splitlines()).__next__):
        print(t)

test_generate_tokens()


# Generated at 2022-06-13 18:19:10.771888
# Unit test for function generate_tokens
def test_generate_tokens():
    # Test that the tokenize() function can tokenize a Java file correctly
    try:
        from io import StringIO
    except ImportError:
        from StringIO import StringIO
    readline = iter(StringIO(java_example).readline, "").next
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        javatokens = list(tokenize.generate_tokens(readline))

    # We can't use assertEqual() for comparing token lists because the line
    # numbers are different.
    # Instead, we put the tokens in a string and compare the strings.
    # Eliminate the line numbers by replacing each tuple in the list by a
    # string representation of the tuple.
    # The strings are compared using difflib.
    strtokens = []

# Generated at 2022-06-13 18:19:14.556066
# Unit test for function tokenize_loop
def test_tokenize_loop():
    import io

    # Test iterator object
    stream = io.StringIO("a\n")
    tokenize_loop(stream.readline, printtoken)

    # Test iterator function
    def iter():
        yield from ["a\n"]

    tokenize_loop(iter().__next__, printtoken)


# backwards compatible interface

# Generated at 2022-06-13 18:19:18.930737
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    from blib2to3.pgen2.tokenize import generate_tokens, untokenize

    # Test that non-empty indents are correctly inserted into the output stream
    # before non-indent, non-dedent, non-newline tokens on the following line.
    # Also test that newlines are preserved.

# Generated at 2022-06-13 18:19:25.276152
# Unit test for function tokenize_loop
def test_tokenize_loop():
    # This code is in tokenize_loop() above, but putting it in its own
    # function allows the traceback to be more easily compared with the
    # expected traceback.
    for token_info in generate_tokens(lambda: '123'):
        tokeneater(*token_info)



# Generated at 2022-06-13 18:19:32.443156
# Unit test for function tokenize_loop
def test_tokenize_loop():
    # TODO: modify tokenize_loop to use new code from generate_tokens
    from io import StringIO
    from textwrap import dedent

    test_code = dedent(
        """
        import turtle
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
    """
    )
    test_file = StringIO(test_code)
    tokenize_loop(test_file.readline, printtoken)



# Generated at 2022-06-13 18:19:42.480580
# Unit test for function detect_encoding
def test_detect_encoding():
    def readline():
        if not lines:
            raise StopIteration()
        line = lines[0]
        del lines[0]
        return line


# Generated at 2022-06-13 18:19:44.211872
# Unit test for function tokenize
def test_tokenize():
    import io
    import token

# Generated at 2022-06-13 18:20:18.816898
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    u = Untokenizer()
    toks = [(3, 'print'), (59, '('), (6, '1'),
            (6, '+'), (6, '1'), (59, ')'), (59, ')'),
            (3, 'print'), (59, '('), (6, '3'),
            (6, '+'), (6, '3'), (59, ')'), (59, ')')]
    result = u.untokenize(toks)
    expect = "print(1+1)print(3+3)"
    assert result == expect



# Generated at 2022-06-13 18:20:21.908161
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    u = Untokenizer()
    assert u.compat((1, "a"), [(1, "b")]) == None


# Generated at 2022-06-13 18:20:27.560839
# Unit test for function detect_encoding
def test_detect_encoding():
    import io

    def readline():
        yield from io.BytesIO(b"\xff\xfe# coding: iso-8859-1\r\npass\r\n").readlines()

    assert detect_encoding(readline) == ("iso-8859-1", [b"# coding: iso-8859-1\r\n"])



# Generated at 2022-06-13 18:20:37.376312
# Unit test for method untokenize of class Untokenizer
def test_Untokenizer_untokenize():
    import io
    from unittest.mock import patch
    s = io.StringIO("def f():\n  print(42)\n")
    tok = tokenize(s.readline)
    with patch("builtins.print", lambda x: None):
        u = Untokenizer()
        u.untokenize(tok)
        assert u.tokens == [
            "def ",
            "f",
            "(",
            ")",
            ":",
            "\n",
            "  ",
            "print",
            "(",
            "42",
            ")",
            "\n",
        ]



# Generated at 2022-06-13 18:20:43.712029
# Unit test for function detect_encoding
def test_detect_encoding():
    x = b'# coding=iso-8859-1\npass\n['
    assert detect_encoding(iter(x.splitlines(True)).__next__) == ('iso-8859-1', [x])

    y = b'# coding=iso-8859-1\r\npass\r\n[\n'
    assert detect_encoding(iter(y.splitlines(True)).__next__) == ('iso-8859-1', [y])



# Generated at 2022-06-13 18:20:49.188281
# Unit test for function generate_tokens
def test_generate_tokens():
    from io import StringIO
    from token import tok_name
    g = generate_tokens(StringIO('for i in range(10): print(i)\n').readline)
    for toknum, tokval, _, _, _ in g:
        print(tok_name[toknum], tokval)
# test_generate_tokens()


# Generated at 2022-06-13 18:20:57.882168
# Unit test for function detect_encoding
def test_detect_encoding():
    import io
    import tempfile

    def bytes_to_line(b: bytes) -> Callable[[], bytes]:
        def nextline() -> bytes:
            return b

        return nextline

    def check_detect(line1: bytes, line2: bytes, exp_enc: str, exp_lines: Tuple[bytes, ...]) -> None:
        d_enc, d_lines = detect_encoding(bytes_to_line(line1) if line1 else lambda: b"")
        assert d_enc == exp_enc
        assert d_lines == [line1]
        d_enc, d_lines = detect_encoding(
            bytes_to_line(line1) if line1 else lambda: b"",
            bytes_to_line(line2) if line2 else lambda: b"",
        )

# Generated at 2022-06-13 18:21:13.468003
# Unit test for function detect_encoding

# Generated at 2022-06-13 18:21:17.746697
# Unit test for function generate_tokens
def test_generate_tokens():
    import sys, tokenize
    if len(sys.argv) > 1:
        tokenize.generate_tokens(open(sys.argv[1]).readline)
    else:
        tokenize.generate_tokens(sys.stdin.readline)

# Generated at 2022-06-13 18:21:26.965856
# Unit test for function detect_encoding
def test_detect_encoding():
    def readlines(seq):
        def genlines():
            for item in seq:
                yield item

        return genlines()

    # Check absence of both a BOM and cookie
    sample = "blah blah:\n    blah blah"
    assert detect_encoding(readlines([sample])) == ("utf-8", [sample])
    # Check presence of BOM
    sample = BOM_UTF8 + "blah blah:\n    blah blah"
    assert detect_encoding(readlines([sample])) == ("utf-8-sig", [sample])
    # Check BOM and coding cookie don't match
    sample = BOM_UTF8 + "blah blah # coding: latin-1\n    blah blah"

# Generated at 2022-06-13 18:22:01.729691
# Unit test for function tokenize_loop
def test_tokenize_loop():
    # Note that in Python 3, tokenize_loop only takes one argument,
    # readline.  These tests won't be valid, and will cause errors,
    # when run with Python 3.
    try:
        from io import StringIO  # Python 3
    except ImportError:
        from StringIO import StringIO  # Python 2
    from blib2to3.pgen2.tokenize import generate_tokens

    import token

    text = "1 + 1"
    toks_exc = StringIO()

    def tokeneater(*args):
        toks_exc.write(token.tok_name[args[0]] + " ")

    tokenize_loop(StringIO(text).readline, tokeneater)

# Generated at 2022-06-13 18:22:11.709527
# Unit test for method compat of class Untokenizer
def test_Untokenizer_compat():
    '''Unit test for method compat of class Untokenizer'''
    from . import tokenize

    untok = Untokenizer()
    # Test case from issue #11419.

# Generated at 2022-06-13 18:22:23.644329
# Unit test for function detect_encoding
def test_detect_encoding():
    """This doesn't test the edge cases of detect_encoding()."""

    def readline():
        if not hasattr(readline, "lines"):
            readline.lines = [
                "",
                "# comment",
                "# coding: latin-1",
                "",
                "print('fran\\xe7ais')",
            ]
        return readline.lines.pop(0)

    encoding, lines = detect_encoding(readline)
    assert encoding == "iso-8859-1"
    assert lines == ["# comment", "# coding: latin-1", ""]
