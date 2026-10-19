

# Generated at 2022-06-14 11:40:17.900690
# Unit test for constructor of class HyperParser

# Generated at 2022-06-14 11:40:27.534349
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    text = Text()
    text.insert(END, r"""
# Hooray!
x = 12 + ['a',
         'b']
y = f(
    x,
    g(x))
""")
    # A simple case
    hyper = HyperParser(text, text.index("1.0"))
    assert hyper.get_surrounding_brackets() == ("1.12", "1.15")
    # Same, with a line indicator
    hyper = HyperParser(text, text.index("1.0 lineend"))
    assert hyper.get_surrounding_brackets() == ("1.12", "1.15")
    # Same, with a line indicator and a selection
    text.tag_add("sel", "1.0", "1.15")

# Generated at 2022-06-14 11:40:44.300514
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    from pytest import raises

    def test_string(text, index, expected):
        parser = HyperParser(text, index)
        assert parser.is_in_code() == expected

    text = Text(
        state=tkinter.NORMAL,
        wrap=tkinter.NONE,
        undo=False,
        maxundo=-1,
        width=80,
        height=1,
        font=("courier", 10, "normal"),
    )

    text.insert(tkinter.END, "a = b + c")
    test_string(text, "1.1", True)  # 1
    test_string(text, "1.2", True)  # 2
    test_string(text, "1.3", True)  # 3
    test_string(text, "1.4", True) 

# Generated at 2022-06-14 11:40:53.587876
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    """

    """
    text = TextWithLogging()
    text.set("abc def")
    hp = HyperParser(text, index=text.index("end"))
    assert hp.is_in_code()

    text.set("abc 'def'")
    hp = HyperParser(text, index=text.index("end"))
    assert not hp.is_in_code()

    text.set("# comment")
    hp = HyperParser(text, index=text.index("end"))
    assert not hp.is_in_code()

    text.set("abc # comment")
    hp = HyperParser(text, index=text.index("end"))
    assert hp.is_in_code()

    text.set("abc# comment")
    hp = HyperParser(text, index=text.index("end"))

# Generated at 2022-06-14 11:40:55.787054
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    from idlelib.idle_test.htest import run
    run(HyperParser_is_in_code)

# Generated at 2022-06-14 11:41:01.106687
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    rp = RoughParser('  x = 23 \\', indent_width=4, tabwidth=8)
    rp.set_str('  x = 23 \\', indent_width=4, tabwidth=8)
    assert rp.get_num_lines_in_stmt() == 1
    assert rp.compute_backslash_indent() == 6



# Generated at 2022-06-14 11:41:08.154046
# Unit test for constructor of class HyperParser
def test_HyperParser():  # htest #
    import unittest
    import Tkinter

    class TestHyperParser(unittest.TestCase):
        def test_parser_self(self):
            # Based on test_parser in test_support.
            text = Tkinter.Text()
            text.insert("1.0", """\
            def f():
                if 1:
                    pass
                elif 2:
                    pass
                elif 3:
                else:
                    pass
            """)
            n = 23
            pos = "1.%d" % n
            text.mark_set("test", pos)
            hp = HyperParser(text, pos)
            self.assertEqual(hp.indexinrawtext, n)
            self.assertEqual(hp.bracketing[2][1], 1)
            self.assertEqual

# Generated at 2022-06-14 11:41:19.076485
# Unit test for method is_in_string of class HyperParser

# Generated at 2022-06-14 11:41:32.379361
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    import unittest

    # The test consists of a tuple of (string, index, result), where
    # string is the string to be parsed and index is the position of
    # the cursor in the string. result is the expected result of
    # HyperParser(string, index).is_in_string()
    test_cases = (
        ('"', 1, True),
        ("'", 1, True),
        ('"""', 3, True),
        ("'''", 3, True),
    )

    class TestCase(unittest.TestCase):
        def test(self):
            for case, index, result in test_cases:
                text = EditorWindow(io.StringIO())
                text.insert("insert", case)

# Generated at 2022-06-14 11:41:39.659511
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    h = HyperParser("[0, 1, 2]", "1.0")
    h.set_index("1.1")
    if h.indexinrawtext != 1:
        raise ValueError("Bad index")
    if h.indexbracket != 1:
        raise ValueError("Bad bracket index")

    h = HyperParser("[0, 1, 2]", "1.1")
    h.set_index("1.2")
    if h.indexinrawtext != 2:
        raise ValueError("Bad index")
    if h.indexbracket != 2:
        raise ValueError("Bad bracket index 2")

    h = HyperParser("[0, 1, 2]", "1.2")
    h.set_index("1.3")

# Generated at 2022-06-14 11:42:09.039746
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    for text, index, wanted in [
        ("(abc", 3, ("(", ")"))
    ]:

        hp = HyperParser(text, index)
        got = hp.get_surrounding_brackets()

        if got != wanted:
            print(
                "Error in HyperParser_get_surrounding_brackets:",
                "text=%r, index=%r, wanted=%r, got=%r" % (text, index, wanted, got),
            )



# Generated at 2022-06-14 11:42:21.429055
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    global test_HyperParser_is_in_code_failed, test_HyperParser_is_in_code_counter

    test_HyperParser_is_in_code_counter += 1

    def test_case(text, index, expected):
        if expected:
            expect = "in code"
        else:
            expect = "not in code"

        hp = HyperParser(text, index)
        value = hp.is_in_code()


# Generated at 2022-06-14 11:42:32.600883
# Unit test for constructor of class HyperParser
def test_HyperParser():
    text = """\
a = b and c or d
a2 = b2 and c2 and d2
"a3 = b3 and c3 and d3"
# a4 = b4 and c4 and d4
a5 = b5 and c5 and d5
"""
    first = "1.0"
    last = repr(len(text.splitlines(1))) + ".0"
    for i in range(len(text)):
        for index in ("%d.%d" % (i + 1, i + 1), "%d.%d" % (i + 1, i + 2)):
            h = HyperParser(text, index)
            # Test __init__
            eq = "HyperParser(%s): %s" % (index, text[h.indexinrawtext :])

# Generated at 2022-06-14 11:42:41.199085
# Unit test for method is_in_code of class HyperParser

# Generated at 2022-06-14 11:42:53.030738
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():

    def test(s, expected, debug=False):
        if debug:
            print("\n" + s + "\n" + (" " * len(s) + expected))

        p = RoughParser(s, len(s), 0)
        assert p.get_continuation_type() == C_BACKSLASH
        indent = p.compute_backslash_indent()
        # The expected string is a sequence of spaces and tabs.
        # Replace each tab by the appropriate number of spaces.
        expected = expected.expandtabs(p.tabwidth)
        assert indent == len(expected)

    # Test an assignment statement
    test("""\
x = '''
   hello
   world
'''
""", "   ", True)

    # Test another assignment statement

# Generated at 2022-06-14 11:43:09.225959
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    def do_test(code, base_indent_string):
        parser = RoughParser(code)
        assert parser.get_base_indent_string() == base_indent_string

    do_test('', '')
    do_test('\n', '')
    do_test(' ', ' ')
    do_test('  ', '  ')
    do_test('   ', '   ')
    do_test('\t', '\t')
    do_test('\t ', '\t ')
    do_test('\t  ', '\t  ')
    do_test('\t\t', '\t\t')
    do_test('\t\t  ', '\t\t  ')
    do_test('a', '')

# Generated at 2022-06-14 11:43:17.387606
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    # pylint: disable=redefined-builtin
    def f(input, expected_start, expected_level, expected_continuation):
        parser = RoughParser("    " + input, 4)
        start = parser.find_good_parse_start()
        level = parser.compute_bracket_indent()
        continuation = parser.get_continuation_type()
        assert start == expected_start, "for input %r expected %d, got %d" % (
            input,
            expected_start,
            start,
        )
        assert level == expected_level, "for input %r expected %d, got %d" % (
            input,
            expected_level,
            level,
        )
        assert (
            continuation == expected_continuation
        ), "for input %r expected %r, got %r"

# Generated at 2022-06-14 11:43:28.103826
# Unit test for constructor of class HyperParser
def test_HyperParser():
    from unittest import TestCase


# Generated at 2022-06-14 11:43:42.461361
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    """Test that HyperParser.get_surrounding_brackets gives the right
    result. Run by test_parenmatch.py.
    """

    def assertIdx(idx, text, openers, mustclose, expected):
        assert expected == HyperParser(text, idx).get_surrounding_brackets(openers, mustclose)

    # empty openers means we only look for '(' (or '[' or '{')
    assertIdx("1.0", "foo(bar", "", False, ("1.0", "1.10"))
    assertIdx("1.0", "foo(bar", "", True, ("1.0", "1.10"))

    # empty openers means we only look for '(' (or '[' or '{')

# Generated at 2022-06-14 11:43:49.072712
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    parser = RoughParser()

# Generated at 2022-06-14 11:44:19.948806
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    from idlelib.percolator import Percolator
    p = Percolator("")
    assert p.compute_bracket_indent() == 0

    p = Percolator("[")
    assert p.compute_bracket_indent() == 0

    p = Percolator("[x")
    assert p.compute_bracket_indent() == 0

    p = Percolator("[x]")
    assert p.compute_bracket_indent() == 0

    p = Percolator("[x,")
    assert p.compute_bracket_indent() == 0

    p = Percolator("[x, y")
    assert p.compute_bracket_indent() == 0

    p = Percolator("[\n  x,")
    assert p.compute_br

# Generated at 2022-06-14 11:44:32.400978
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    # pylint: disable=redefined-builtin
    def _test(str_, indent_width, tabwidth):
        return RoughParser(str_, indent_width, tabwidth).compute_bracket_indent()

    assert _test("if 1:\n    foo()\n", 8, 8) == 8
    assert _test("if 1:\n    foo()\n", 4, 8) == 4
    assert _test("if 1:\n    # comment\n", 8, 8) == 8
    assert _test("if 1:\n    foo(\n", 8, 8) == 12

    assert _test("if 1:\n  foo()\n", 2, 8) == 2
    assert _test("if 1:\n  # comment\n", 2, 8) == 2

# Generated at 2022-06-14 11:44:45.275255
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    import types

    strs = [
        """\
        if (not arg) or (arg == '-'):
            stdin = sys.stdin
        else:
            stdin = open(arg, 'r')
        """,
        """\
        if True:
            pass
        elif False:
            a = 1
        else:
            b = 2
        """,
    ]

    indent_width, tabwidth = 4, 8

    def test(str, expected):
        parser = RoughParser(str, indent_width, tabwidth)
        parser.set_str(str)
        result = parser.compute_backslash_indent()
        assert result == expected

    for str in strs:
        test(str, indent_width)

    # unit tests for specific bugs found while developing this code


# Generated at 2022-06-14 11:44:58.577851
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    class text_widget:
        """A text widget like class for testing.

        self.get(start, stop) returns the text between the two indices.
        self.index(index) returns the numeric index of a given index.
        """

        def __init__(self):
            self._text = "\n" + (
                "def f(a, b):\n"
                "    if a:\n"
                '        print("xx\'x")\n'
                '    elif b:\n'
                '        print("yy"y")\n'
                "    else:\n"
                '        print("zz\'z")\n'
                "f(1, 2)\n"
            )


# Generated at 2022-06-14 11:45:00.018629
# Unit test for method get of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping_get():
    mapping = StringTranslatePseudoMapping({97: 98}, 99)
    assert mapping.get(97) == 98
    assert mapping.get(96) == 99
    assert mapping.get(95, 100) == 100

# Generated at 2022-06-14 11:45:09.578573
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    """Unit test for method get_surrounding_brackets of class HyperParser"""

    if verbose_tests:
        print("Running test_HyperParser_get_surrounding_brackets")

    # If a test fails, it should print something to be printed
    # in this test.
    for i in range(6):
        for j in range(6):
            ok = True

            if verbose_tests:
                print("i = %d, j = %d" % (i, j))

            # We will test with a total of 6 different cases,
            # with i indicating the type of the first bracket
            # and j indicating the type of the last bracket.

            # 0 is for ()
            # 1 is for [],
            # 2 is for {}
            # 3 is for <>,
            # 4 is for quotes
            # 5

# Generated at 2022-06-14 11:45:13.085874
# Unit test for method compute_bracket_indent of class RoughParser

# Generated at 2022-06-14 11:45:24.460164
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    from idlelib.idle_test import dummy_editwin, run_unittest

    class Test(unittest.TestCase):
        def setUp(self):
            flist = dummy_editwin()
            self.text = flist.open("test")

        def tearDown(self):
            self.text.close()

        def test(self):

            self.text.set("42\n" "a = 1\n" 'b = "2"\n')
            hp = HyperParser(self.text, "1.0")
            self.assertFalse(hp.is_in_code())
            hp = HyperParser(self.text, "1.1")
            self.assertTrue(hp.is_in_code())
            hp = HyperParser(self.text, "1.2")

# Generated at 2022-06-14 11:45:36.028717
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    def base_indent_string(s):
        return RoughParser(s, 0).get_base_indent_string()

    assert base_indent_string('') == ''
    assert base_indent_string('    ') == '    '
    assert base_indent_string('\t') == '\t'
    assert base_indent_string('  # foo') == '  '
    assert base_indent_string('\t# foo') == '\t'
    assert base_indent_string('  pass') == '  '
    assert base_indent_string('\tpass') == '\t'
    assert base_indent_string('  if foo:\n  pass') == '  '
    assert base_indent_string('  pass\n  ') == '  '

# Generated at 2022-06-14 11:45:41.869997
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    import unittest
    from test.support import captured_stdout

    class TestHyperParser(unittest.TestCase):
        def setUp(self):
            self.hp = HyperParser("", "")

        def test_identifier(self):
            cases = [
                # (code, pos, exp)
                ("foo", 4, "foo"),
                ("foo", 3, "foo"),
                ("foo", 2, "foo"),
                ("foo", 1, "foo"),
                (" foo", 5, "foo"),
                ("foo ", 4, "foo"),
                ("foo(", 4, "foo"),
                ("foo.bar", 8, "bar"),
            ]

            for code, pos, exp in cases:
                self.hp.rawtext = code
                self.hp.indexinrawtext = pos

# Generated at 2022-06-14 11:46:23.611590
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = Text()
    text.insert(END, "1+1")
    parser = HyperParser(text, text.index(END))
    assert parser.indexinrawtext == 3
    assert parser.indexbracket == 0
    assert parser.rawtext == "1+1"
    assert parser.stopatindex == "1.end"

    parser.set_index(text.index("1.0"))
    assert parser.indexinrawtext == 0
    assert parser.indexbracket == 0
    assert parser.rawtext == "1+1"
    assert parser.stopatindex == "1.end"
    parser.set_index(text.index("1.1"))
    assert parser.indexinrawtext == 1
    assert parser.indexbracket == 1
    assert parser.rawtext == "1+1"
    assert parser

# Generated at 2022-06-14 11:46:31.540366
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    from tkinter import Tk

    tk = Tk()
    text = Text(tk)
    text.insert(1.0, "def f(x):\n    print(x)")
    text.pack()
    # cursor at (2,0)
    text.mark_set("insert", "2.0")

    hp = HyperParser(text, "insert")
    # We are not in a string.
    assert hp.is_in_code()
    # Also not in a comment.
    assert hp.is_in_code()
    # Not in a string
    assert not hp.is_in_string()

    # Now, a string.
    text.insert("insert", '"string"    ')
    hp = HyperParser(text, "insert")
    assert not hp.is_in_code()


# Generated at 2022-06-14 11:46:46.769274
# Unit test for method find_good_parse_start of class RoughParser

# Generated at 2022-06-14 11:46:59.517026
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:47:12.776418
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    test_text = '"""strings"""\n"""strings"""\n"""strings"""\n"""strings"""\n"""strings"""\n"""strings"""\n"""strings"""\n"""strings"""'
    for i in range(len(test_text)):
        #print(test_text[i])
        text = tk.Text(None)
        text.insert(0.0, test_text)
        hyperparser = HyperParser(text, str(int(i)) + ".0")
        string = hyperparser.is_in_string()

# Generated at 2022-06-14 11:47:23.256330
# Unit test for constructor of class HyperParser
def test_HyperParser():
    from tests.support import requires

    requires("gui")

    import unittest

    class TestHyperParser(unittest.TestCase):
        def _test_hyper_parser(self, text, index, res):
            hp = HyperParser(text, index)
            self.assertEqual(
                (hp.is_in_string(), hp.is_in_code(), hp.get_expression()), res
            )

        def test_hyper_parser_0(self):
            text = Text(None, {})
            text.insert("0.0", "'''\n" "def foo():\n" "    pass\n" "    pass\n" "'''")
            self._test_hyper_parser(text, "3.3", (False, True, "pass"))

# Generated at 2022-06-14 11:47:33.639919
# Unit test for method is_in_code of class HyperParser

# Generated at 2022-06-14 11:47:47.074083
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def helper(test_str, cursor_pos, expected_expression, **kwds):
        test_str = test_str.replace("(*cursor*)", "")
        cursor_pos = test_str.index("(*cursor*)")
        test_str = test_str.replace("(*cursor*)", "")

        kwds.setdefault("indent", "    ")
        kwds.setdefault("tabwidth", 8)

        text = Text(test_str, kwds["indent"], kwds["tabwidth"])
        hp = HyperParser(text, "%d.0" % (cursor_pos + 1))

        # Check that it gives right results
        expression = hp.get_expression()
        print("Get expression: %s" % repr(expression))
        if expression != expected_expression:
            raise

# Generated at 2022-06-14 11:47:54.532375
# Unit test for method is_in_code of class HyperParser

# Generated at 2022-06-14 11:48:05.690874
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    text = """print 'it is a string'"""
    for t in text, text + "\n", text + " ":
        p = HyperParser(t, index="insert")
        assert p.is_in_string()
        p.set_index("end")
        assert not p.is_in_string()
        p.set_index("end-7c")
        assert p.is_in_string()
        p = HyperParser(t, index="end")
        assert not p.is_in_string()
        p.set_index("insert-2c")
        assert not p.is_in_string()
        p = HyperParser(t, index="end-4c")
        assert p.is_in_string()
        p = HyperParser(t, index="end-6c")
        assert p.is_