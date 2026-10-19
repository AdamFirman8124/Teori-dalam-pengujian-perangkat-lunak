

# Generated at 2022-06-14 11:39:51.747668
# Unit test for method is_block_opener of class RoughParser
def test_RoughParser_is_block_opener():
    # test_RoughParser_is_block_opener
    
    # control data
    # case 1
    expected1= True
    actual1= RoughParser("a:").is_block_opener()
    assert actual1 == expected1, "actual1: %s  expected1: %s" % (actual1, expected1)
    # case 2
    expected2= True
    actual2= RoughParser("if True:").is_block_opener()
    assert actual2 == expected2, "actual2: %s  expected2: %s" % (actual2, expected2)
    # case 3
    expected3= True
    actual3= RoughParser("while True:").is_block_opener()

# Generated at 2022-06-14 11:39:57.948858
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    import unittest

    class TestCase(unittest.TestCase):
        def test_simple(self):
            rawtext = "foo ( (bar, baz,) )"
            for i in range(len(rawtext)):
                text = tk.Text()
                text.insert("insert", rawtext)
                hp = HyperParser(text, "1.%d" % i)
                res = hp.get_surrounding_brackets()
                if res:
                    self.assertEqual(res, ("1.3", "1.%d" % (len(rawtext) - 1)))
                else:
                    if i < 3 or i > len(rawtext) - 2:
                        self.assertEqual(res, None)


# Generated at 2022-06-14 11:40:01.344137
# Unit test for constructor of class HyperParser
def test_HyperParser():
    import doctest

    failure_count, test_count = doctest.testmod()
    if failure_count:
        raise ValueError("Failed %d/%d doctests" % (failure_count, test_count))

# Generated at 2022-06-14 11:40:08.512271
# Unit test for method get of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping_get():
    """Tests method get of class StringTranslatePseudoMapping"""
    r"""
    >>> whitespace_chars = ' \t\n\r'
    >>> preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    >>> mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
    >>> text = "a + b\tc\nd"
    >>> text.translate(mapping)
    'x x x\tx\nx'
    """



# Generated at 2022-06-14 11:40:17.902671
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    """
    Test case for method get_base_indent_string of class RoughParser.

    This method returns the leading whitespace of last interesting statement.
    """
    print("\nTesting get_base_indent_string() of class RoughParser")
    lines = ['\t# comment']
    try:
        rp = RoughParser(lines)
        print("leading whitespace of last interesting statement:",
              rp.get_base_indent_string())
    except Exception as e:
        print("FAILED: Exception: {0}".format(e))

# Generated at 2022-06-14 11:40:22.880144
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    """Test pos = RoughParser(string).compute_backslash_indent()"""
    # pylint: disable=redefined-builtin

    # Test the method giving the position of the next line
    # assuming the continuation is C_BACKSLASH.  It's better
    # to test this method separately that to derive the test
    # case from a complete test since it only depends on what
    # the previous line is.

    def run_one_test(text, expected_pos):
        """Run one test case"""
        info = RoughParser(text, None)
        if info.get_continuation_type() != C_BACKSLASH:
            raise RuntimeError(
                "Test case %r is not a backslash continuation" % text
            )
        actual_pos = info.compute_backslash_indent()
       

# Generated at 2022-06-14 11:40:30.914986
# Unit test for method get_last_stmt_bracketing of class RoughParser

# Generated at 2022-06-14 11:40:45.487421
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    # Test a simple case
    for expr, index, text in (
        ("None", 3, "no_such_function(None)"),
        ("no_such_function", 17, "no_such_function(None)"),
    ):
        hy = HyperParser(text, index)
        assert hy.get_expression() == expr

    # Test with various brackets

# Generated at 2022-06-14 11:40:54.210206
# Unit test for constructor of class HyperParser
def test_HyperParser():
    from unittest import TestCase

    class HyperParserTestCase(TestCase):
        """A class for testing HyperParser."""
        # The following attributes are set before each test method is
        # called (using setUp()).
        # text:            The Text widget.
        # parser:          The HyperParser instance.
        # text_index:      The index into text where we call the HyperParser
        #                  methods. This is set to "1.0" by default.
        # expected_bracketing: The expected result of parser.bracketing.
        # expected_isopener:   The expected result of parser.isopener.
        # expected_rawtext:    The expected result of parser.rawtext.
        text = None
        parser = None
        text_index = "1.0"
        expected_bracketing = None
       

# Generated at 2022-06-14 11:41:03.020741
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    rp = RoughParser('''a = 1
b = 2 # (1 + 2)
''')
    # print(rp.__dict__)
    print(rp.find_good_parse_start(0))
    print(rp.find_good_parse_start(2))
    print(rp.find_good_parse_start(3))
    print(rp.find_good_parse_start(4))
    print(rp.find_good_parse_start(7))
    print(rp.find_good_parse_start(10))
    print(rp.find_good_parse_start(12))
    print(rp.find_good_parse_start(13))


# test_RoughParser_find_good_parse_start()

# Generated at 2022-06-14 11:42:04.621932
# Unit test for method is_block_opener of class RoughParser
def test_RoughParser_is_block_opener():
    testcases = [
        "def f(x):\n    return x + 1\n\n",
        "def f(x):\n    return x + 1\n    \n",
        "def f(x):\n return x + 1\n\n",
        "def f(x):\n\n  return x + 1\n\n",
    ]
    for text in testcases:
        assert rp(text).is_block_opener(), text

# Generated at 2022-06-14 11:42:11.416718
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def do_test(lines, indentwidth, tabwidth, expected):  # pylint: disable=missing-function-docstring
        rough_parser = RoughParser("".join(lines), indentwidth, tabwidth)
        actual = rough_parser.compute_bracket_indent()
        if actual != expected:
            raise TestFailure(lines, indentwidth, tabwidth, expected, actual)
    # pylint: disable=missing-function-docstring

    class TestFailure(Exception):  # pylint: disable=missing-function-docstring
        def __init__(self, lines, indentwidth, tabwidth, expected, actual):
            self.lines = lines
            self.indentwidth = indentwidth
            self.tabwidth = tabwidth
            self.expected = expected
            self.actual = actual

# Generated at 2022-06-14 11:42:19.291959
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():

    def check(s, index, openers, mustclose, wanted):
        global Tk
        try:
            Tk
        except NameError:
            from tkinter import Text

        text = Text()
        text.insert("end", s)
        hp = HyperParser(text, index)
        res = hp.get_surrounding_brackets(openers, mustclose)
        text.destroy()
        assert res == wanted, "%r != %r" % (res, wanted)

    check(
        "bar()[2:3]",
        "1.8",
        "([",
        False,
        ("1.7", "1.11"),
    )

# Generated at 2022-06-14 11:42:30.380428
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    def check(src, expected_start, expected_cont):
        p = Parser(src)
        p.reset(src)
        stmtstart, continuation = p.find_good_parse_start(False)
        if stmtstart == len(src):
            stmtstart = 'EOF'
        if stmtstart == expected_start:
            if (continuation == expected_cont) or (
                continuation == C_STRING_FIRST_LINE and expected_cont == C_STRING_NEXT_LINES
            ):
                print("Ok.")
                return
        print("*** Failed ***")
        print(
            "Source string: %r"
            % (src[: stmtstart] + "###" + src[stmtstart :])
        )

# Generated at 2022-06-14 11:42:40.015807
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    def runtest(pr, expected):
        assert pr.compute_backslash_indent() == expected

    pr = RoughParser("spam(eggs,\\\n            ham)")
    runtest(pr, 16)
    pr = RoughParser("spam(eggs,\\\nham)")
    runtest(pr, 4)
    pr = RoughParser("spam(eggs,\n    ham)")
    runtest(pr, 4)
    pr = RoughParser("spam(eggs,\\\n\nham)")
    runtest(pr, 0)
    pr = RoughParser("spam(eggs,\n\nham)")
    runtest(pr, 0)
    pr = RoughParser("spam(eggs,\\\n    ham)")
    runtest(pr, 4)

# Generated at 2022-06-14 11:42:46.078349
# Unit test for method get_num_lines_in_stmt of class RoughParser
def test_RoughParser_get_num_lines_in_stmt():
    rough_parser = RoughParser("", indent_width=4)
    assert rough_parser.get_num_lines_in_stmt() == 0
    rough_parser = RoughParser("", indent_width=4)
    assert rough_parser.get_num_lines_in_stmt() == 0


# Generated at 2022-06-14 11:42:53.301751
# Unit test for constructor of class HyperParser
def test_HyperParser():
    from test.support import check_warnings

    _test_text = r"""# comment
    def inc_indent():
        # comment
        return 42
    def dec_indent():
        # comment
        return
    def get_indent():
        # comment
        return inc_indent() + dec_indent()
    # comment
        # comment
    get_indent()
    # comment
"""
    check_warnings(r"test_HyperParser", DeprecationWarning, test_HyperParser_main, _test_text)


# Generated at 2022-06-14 11:43:09.548841
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    # pylint: disable=redefined-builtin
    # pylint: disable=protected-access

    def test_string(str_, result):
        rp = RoughParser("", 0)
        rp.str = str_
        rp._study2()
        assert rp.get_base_indent_string() == result

    test_string("    a = 1 + 2\n        b = 3 + 4\n", "    ")
    test_string("    a = 1 + 2\n    b = 3 + 4\n", "    ")
    test_string("  a = 1 + 2\n      b = 3 + 4\n", "  ")
    test_string("a = 1 + 2\n        b = 3 + 4\n", "")

# Generated at 2022-06-14 11:43:12.885886
# Unit test for method get_last_open_bracket_pos of class RoughParser
def test_RoughParser_get_last_open_bracket_pos():
    rp = RoughParser("[a if b else c]")
    assert rp.get_last_open_bracket_pos() == 0


# Generated at 2022-06-14 11:43:25.784047
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    assert RoughParser("").get_base_indent_string() == ""
    assert RoughParser("\n").get_base_indent_string() == ""
    assert RoughParser(" \n").get_base_indent_string() == " "
    assert RoughParser("\t\n").get_base_indent_string() == "\t"
    assert RoughParser(" \t\n").get_base_indent_string() == " \t"
    assert RoughParser("  #  \n").get_base_indent_string() == "  "
    assert RoughParser("x = 3").get_base_indent_string() == ""
    assert RoughParser("  x = 3").get_base_indent_string() == "  "
    assert RoughParser("  x = 3\n").get_base_indent_string()

# Generated at 2022-06-14 11:44:02.504115
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    from lib2to3.fixer_util import untokenize
    from lib2to3.pygram import python_symbols as syms
    from lib2to3.pytree import Leaf, Node
    from lib2to3.pgen2.token import Token

    def test(src, indent):
        """
        Given a string of python code, return the amount of indentation
        that should occur on the next line of code.
        """
        lst = [Leaf(Token.INDENT, "", prefix="")]
        lst.extend(
            [Leaf(type_, val) for type_, val in untokenize.untokenize(src.splitlines())]
        )
        lst.append(Leaf(Token.NEWLINE, "\n", prefix=""))

# Generated at 2022-06-14 11:44:14.450428
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():

    hyper = HyperParser(f, '1.0')

    hyper.set_index('1.0')
    if hyper.get_surrounding_brackets(mustclose=True) is not None:
        print('1.0', 'is a bug')
    else:
        print('1.0', 'ok')

    hyper.set_index('1.1')
    if hyper.get_surrounding_brackets(mustclose=True) is not None:
        print('1.1', 'is a bug')
    else:
        print('1.1', 'ok')

    hyper.set_index('1.2')
    if hyper.get_surrounding_brackets(mustclose=True) is not None:
        print('1.2', 'is a bug')

# Generated at 2022-06-14 11:44:22.975976
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def check(input, output):
        if output is None:
            output = ""
        hp = HyperParser(input, input.index("insert"))
        got = hp.get_expression()
        if got != output:
            print(
                "For input <<%s>>. HyperParser returned <<%s>> instead of <<%s>>."
                % (input.get("1.0", "end-1c"), got, output)
            )

    t = Tk()
    t.destroy()
    i = Text(t)
    i.insert("1.0", "a(b.fun(c[1].d(e,f)+g+h.i*j[k],l).m)")
    i.mark_set("insert", "4.0")

# Generated at 2022-06-14 11:44:33.967820
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    """Unit test for method is_in_code of class HyperParser."""

    # We test this only on "simple" code.

# Generated at 2022-06-14 11:44:46.801320
# Unit test for method get_last_stmt_bracketing of class RoughParser
def test_RoughParser_get_last_stmt_bracketing():
    def get_RP(s):
        return RoughParser(s, indent_width=4, tabwidth=4)
    assert get_RP("").get_last_stmt_bracketing() is None
    assert get_RP("# comment").get_last_stmt_bracketing() is None
    assert get_RP("# comment\n").get_last_stmt_bracketing() is None
    assert get_RP("# comment\n\n").get_last_stmt_bracketing() is None
    assert get_RP("1+1").get_last_stmt_bracketing() == ((0,0), (3,0))
    assert get_RP("1 + 1").get_last_stmt_bracketing() == ((0,0), (4,0))

# Generated at 2022-06-14 11:44:54.401070
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    parser = RoughParser("    line 1\n    line 2", indent_width=4, tabwidth=8)
    assert parser.compute_bracket_indent() == 8
    parser = RoughParser("    line 1\n    line 2", indent_width=4, tabwidth=4)
    assert parser.compute_bracket_indent() == 4

# Generated at 2022-06-14 11:45:06.662237
# Unit test for constructor of class HyperParser
def test_HyperParser():
    "Unit test for constructor of class class HyperParser."
    from unittest import TestCase

    import inspect

    class Check(TestCase):
        def check(self, text, index, result):
            "Check that text.HyperParser(index).get_expression() == result."

            hp = HyperParser(text, index)
            self.assertEqual(hp.get_expression(), result)

    def hp_test(test_func):
        """Decorator for a class method of Check, to run it as a unit test.

        Finds the first occurrence of 'text =' in the function
        definition, and takes its value as the text to parse. The
        'index' is equal to the length of the string. The function's
        name is used as the expected value.
        """

        raw = inspect.getsource(test_func)

       

# Generated at 2022-06-14 11:45:19.552939
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = "abc (def ghi).jkl"
    def test(index, raw_indexinrawtext, raw_indexbracket):
        hp = HyperParser(text, index)
        if (hp.indexinrawtext != raw_indexinrawtext
            or hp.indexbracket != raw_indexbracket
        ):
            raise ValueError("%s: bug: %d %d" % (index, hp.indexinrawtext, hp.indexbracket))

    test("1.0", 0, 0)
    test("1.1", 1, 0)

    test("1.5", 0, 0)
    test("1.6", 1, 1)
    test("1.7", 2, 1)
    test("1.8", 3, 1)
    test("1.9", 4, 1)

# Generated at 2022-06-14 11:45:27.384736
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    import unittest

    class TestHyperParser(unittest.TestCase):
        def test_set_index(self):
            import re
            import textwrap

            # Test the HyperParser's ability to see whether or not it is
            # inside a string.
            code = """# comment
            class A:
                def m(self):
                    if self == 0:
                        rstrip()
            """

            i1 = code.index("rstrip")
            hparser = HyperParser(code, i1 + len("rstrip"))
            self.assertEqual(hparser.is_in_code(), True)
            self.assertEqual(hparser.is_in_string(), False)
            self.assertEqual(hparser.get_expression(), "self.rstrip")
            hparser.set_index(i1)
           

# Generated at 2022-06-14 11:45:40.290220
# Unit test for method is_block_closer of class RoughParser