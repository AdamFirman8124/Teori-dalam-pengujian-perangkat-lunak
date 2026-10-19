

# Generated at 2022-06-14 11:36:47.006721
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    class FakeText(textwidget.Text):
        def __init__(self, content, index, tabwidth):
            self.content = content
            self.index = index
            self.tabwidth = tabwidth

        def get(self, index1, index2=None):
            if index2 is None:
                return self.content[self.index(index1) :]
            else:
                return self.content[self.index(index1) : self.index(index2)]

        def index(self, index):
            global index_call_count
            index_call_count += 1
            return index

    global index_call_count
    tabwidth = 4
    index_call_count = 0

# Generated at 2022-06-14 11:36:55.543623
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    rp = RoughParser(
        textwrap.dedent(
            """\
        def fn(x):
            print(x)
        """
        )
    )
    assert rp.get_base_indent_string() == "        "

    rp = RoughParser(textwrap.dedent("print('hi')"))
    assert rp.get_base_indent_string() == ""

    rp = RoughParser(textwrap.dedent("[1,\n2, 3]"))
    assert rp.get_base_indent_string() == ""


# Generated at 2022-06-14 11:37:02.195219
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    """Test the method compute_bracket_indent of class RoughParser."""
    # pylint: disable=redefined-builtin,undefined-variable,invalid-name,line-too-long
    get_bracket_indent = RoughParser.compute_bracket_indent.__func__
    class testcase():
        """Test case class"""
        def __init__(self, input_string, output_string):
            self.input = input_string
            self.output = output_string
        def __str__(self):
            return "input: %s\n  expected output: %s" % (self.input, self.output)
    class testcase_exception(testcase):
        """Test case class for exceptions"""

# Generated at 2022-06-14 11:37:08.285411
# Unit test for method __len__ of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping___len__():
    whitespace_chars = " \t\n\r"
    preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    mapping = StringTranslatePseudoMapping(preserve_dict, ord("x"))
    assert len(mapping) == len(whitespace_chars)

# Generated at 2022-06-14 11:37:14.048763
# Unit test for method get of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping_get():
    whitespace_chars = " \t\n\r"
    preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    mapping = StringTranslatePseudoMapping(preserve_dict, ord("x"))
    assert mapping.get(ord("a")) == ord("x")
    assert mapping.get(ord(" ")) == ord(" ")



# Generated at 2022-06-14 11:37:42.848339
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    from idlelib.idle_test.mock_idle import Func

    rp = RoughParser("  \t  foo()\n  #  \nbar()")
    got = rp.get_base_indent_string()
    assert got == "    "
    rp = RoughParser("  \t  #\nfoo()")
    assert not rp.get_base_indent_string()
    rp = RoughParser("  \t  foo")
    assert not rp.get_base_indent_string()
    # This is based on an actual IDLE bug.  The last line has a continuation
    # but it's a comment, so it isn't incomplete, and RoughParser says it
    # has no indentation.  This causes code to be left on one line.

# Generated at 2022-06-14 11:37:56.014177
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    def check(s, index, should_be):
        hp = HyperParser(s, index)
        is_in_string = hp.is_in_string()
        if is_in_string != should_be:
            raise ValueError(
                "The HyperParser analysis fails on '%s'. Index '%s' should be %s but it is '%s'"
                % (s, index, should_be, is_in_string)
            )

    #                                 012345678901234567890123456789
    check('   print "foo" # comment\n', "10.0", True)
    check('   print "foo" # comment\n', "11.0", True)
    check('   print "foo" # comment\n', "12.0", True)

# Generated at 2022-06-14 11:37:57.977428
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from unittest import TestCase
    from io import StringIO
    try:
        from idlelib.percolator import Percolator
    except ImportError:
        print('Warning: percolator not available.')
        return

# Generated at 2022-06-14 11:38:06.098429
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    h = HyperParser("'hello'", "1.0")
    if h.is_in_string():
        print("passed test 1")
    else:
        print("failed test 1")

    h = HyperParser('"hello"', "1.0")
    if h.is_in_string():
        print("passed test 2")
    else:
        print("failed test 2")

    h = HyperParser("  'hello'", "1.2")
    if h.is_in_string():
        print("passed test 3")
    else:
        print("failed test 3")

    h = HyperParser("  'hello'", "1.4")
    if not h.is_in_string():
        print("passed test 4")
    else:
        print("failed test 4")

    h = Hyper

# Generated at 2022-06-14 11:38:12.549389
# Unit test for method __getitem__ of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping___getitem__():
    # >>> whitespace_chars = ' \t\n\r'
    whitespace_chars = ' \t\n\r'
    # >>> preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    # >>> mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
    mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
    # >>> text = "a + b\tc\nd"
    text = "a + b\tc\nd"
    # >>> text.translate(mapping)
    # 'x x x\tx\nx'

# Generated at 2022-06-14 11:39:40.205709
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    tk = Tk()
    text = Text(tk)
    text.insert("1.0", """class foo:
        def bar(x, y):
            if x in y:
                pass

    class foo:
        def bar(x, y):
            if x in y:
                pass
""")
    text.pack()

    from test.support import run_unittest

    class TestHyperParser(unittest.TestCase):
        def test_empty_expression(self):
            text.mark_set("insert", "1.1")
            self.assertIsNone(HyperParser(text, "insert").get_surrounding_brackets())

        def test_empty_expression_in_code(self):
            text.mark_set("insert", "1.10")

# Generated at 2022-06-14 11:39:52.548163
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():

    # Test class used to make it easier to write the unit tests
    class HyperParserTest:

        def __init__(self, rawtext, expr_index, openers):

            # Raw text
            self.rawtext = rawtext

            # Expression index
            self.expr_index = expr_index

            # Openers to use
            self.openers = openers

            # Expected result
            self.expected_result = None

            # Parser used
            self.parser = HyperParser(None, 0)

            # Split rawtext in lines
            self.lines = self.rawtext.splitlines()

            # Build the text object
            self.build_text()

            # Build the parser
            self.build_parser()


# Generated at 2022-06-14 11:40:04.757572
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    pl = [0, 0, 0, 0, 0, 0]
    rp = RoughParser("", pl)
    assert rp._find_good_parse_start() == 0
    pl[0] = 1
    assert rp._find_good_parse_start() == 1
    pl[1] = 2
    assert rp._find_good_parse_start() == 2
    pl[2] = 3
    rp.badchars = "abcd"
    assert rp._find_good_parse_start() == 2
    pl[2] = 4
    assert rp._find_good_parse_start() == 2
    pl[3] = 4
    assert rp._find_good_parse_start() == 2
    pl[4] = 5

# Generated at 2022-06-14 11:40:09.679013
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    import pprint
    rp = RoughParser("a = '''\n1\n\n2\n\n'''")
    rp.find_good_parse_start()
    assert rp.str == "\na = '''\n1\n\n2\n\n'''", pprint.pformat(rp.str)
    assert rp.continuation == C_STRING_FIRST_LINE
    assert rp.goodlines == [1, 2, 4, 5], rp.goodlines
    rp = RoughParser("a = '''\n1\n\n2\n\n'''")
    rp = RoughParser("a =\nb =\n")
    rp.find_good_parse_start()
    assert rp.str == "\na =\nb =\n", pprint

# Generated at 2022-06-14 11:40:22.292726
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():

    parser = RoughParser("", 0)
    for i in range(len(parser.str)):
        if parser.find_good_parse_start(i) != i:
            print("Wrong! i:", i)

    parser = RoughParser("#", 0)
    for i in range(len(parser.str)):
        if parser.find_good_parse_start(i) != i:
            print("Wrong! i:", i)

    parser = RoughParser("#", 1)
    for i in range(len(parser.str)):
        if parser.find_good_parse_start(i) != i:
            print("Wrong! i:", i)

    parser = RoughParser("#\n", 2)

# Generated at 2022-06-14 11:40:30.688382
# Unit test for method get_last_open_bracket_pos of class RoughParser
def test_RoughParser_get_last_open_bracket_pos():
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            rp = RoughParser("<string>", "foo((bar)\n")
            self.assertEqual(rp.get_last_open_bracket_pos(), 3)

    unittest.main(module=__name__, exit=False)


# Get a "rough parser" object; this is an instance of class RoughParser.
# The object is used to look at the first interesting line in the text
# and determine, to some extent, the context.  If a parse error occurs
# (for example, because a string wasn't closed), the context is set to
# C_NONE.  Otherwise, the context is C_BRACKET if the last interesting
# statement ended with an open bracket, C_STRING if it ended inside a


# Generated at 2022-06-14 11:40:45.422597
# Unit test for method compute_backslash_indent of class RoughParser

# Generated at 2022-06-14 11:40:54.181061
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # pylint: disable=redefined-outer-name

    class TestCase(object):
        # pylint: disable=too-few-public-methods
        def __init__(self, src, indent):
            self.src = src
            self.indent = indent

    def test(test_cases):
        for test_case in test_cases:
            src, indent = test_case.src, test_case.indent
            parser = RoughParser(src)
            indent_ = parser.compute_backslash_indent()
            if indent != indent_:
                raise ValueError("bad indent %s in: %s" % (indent_, src))


# Generated at 2022-06-14 11:41:03.542077
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    import unittest

    class Test(unittest.TestCase):
        def do(self, rawtext, pos, expected, comment=""):
            print("Testing", rawtext, pos, "->", expected, comment, file=sys.stderr)
            hp = HyperParser("\n" + rawtext + "\n", "1.%d" % pos)
            self.assertEqual(hp.get_expression(), expected, "Testing %s" % rawtext)

    Test().do("", 0, "")
    Test().do("a b c", 1, "")
    Test().do("a b c", 2, "")
    Test().do("a b c", 3, "")
    Test().do("a b c", 4, "c")
    Test().do("a b c", 3, "b", "whitespace")

# Generated at 2022-06-14 11:41:15.894586
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    tabwidth = 4
    from token import LPAR, RPAR, LBRACE, RBRACE, LSQB, RSQB
    from tokenize import generate_tokens
    from io import BytesIO
    from tokenize import untokenize
    

# Generated at 2022-06-14 11:42:11.792631
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    def _test_HyperParser_is_in_code(text, positions, expected_result):
        text = _dedent(text)
        h = HyperParser(text, "insert")
        for pos in positions:
            h.set_index(pos)
            result = h.is_in_code()
            if result != expected_result:
                for line in text.splitlines():
                    print("%4d %s" % (len(line) + 1, repr(line)))
                for i in range(len(line)):
                    if i == pos:
                        print("^", end="")
                    else:
                        print(" ", end="")
                print("\n %s %s" % (result, expected_result))
            assert result == expected_result

    # Test in_code with some comments and strings

# Generated at 2022-06-14 11:42:19.726415
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():

    import inspect
    import tokenize

    # pylint: disable=bad-whitespace

# Generated at 2022-06-14 11:42:30.701044
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def t(s, s_indent, expected):
        l = dedent(s).rstrip("\n")
        p = RoughParser(l, 0)
        assert p.compute_bracket_indent() == expected

    # no interesting stmt?  back up to first preceding newline
    t("blah\nspam\n" * 8 + "(" + " " * 8 + "x = 2\n" + " " * 12 + "print 'hi'\n\n",
        0,
        8)
    # one line
    t("(x = 2)\n", 0, 0)
    # one line, with comment
    t("(x = 2)   # C\n", 0, 0)
    # many lines

# Generated at 2022-06-14 11:42:32.853157
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    rough_parser = RoughParser('')
    rough_parser.set_lo(0)
    assert(isinstance(rough_parser.indent_width,int))


# Generated at 2022-06-14 11:42:41.308757
# Unit test for method get_continuation_type of class RoughParser
def test_RoughParser_get_continuation_type():
    # pylint: disable=redefined-outer-name
    """
    Test that get_continuation_type() returns the correct value.

    Values:
      C_NONE
      C_BACKSLASH
      C_STRING_FIRST_LINE
      C_STRING_NEXT_LINES
      C_BRACKET
    """
    from idlelib.idle_test.mock_idle import Func
    from idlelib.idle_test.htest import run


    # pylint: disable=too-many-statements

    source1 = """\
x = 1
y = 2

print(
    x,
    y
)
"""
    expected1 = C_NONE
    source2 = """\
x = 1
y = 2

print x, y
"""
    expected2

# Generated at 2022-06-14 11:42:46.873611
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    rp = RoughParser("", "")
    rp.find_good_parse_start('"""\n"""\n"""\n"""\n""""""\n""""""\n"""')
    result = rp.goodlines == [1, 1, 1, 6, 9, 12]


# Generated at 2022-06-14 11:42:55.298586
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    from unittest import TestCase, main
    import unittest

    class HPTest(TestCase):
        def _test(self, s, index, expect):
            hp = HyperParser(s, index)
            self.assertEqual(hp.is_in_string(), expect)
            self.assertEqual(hp.indexinrawtext, len(hp.rawtext) - len(s.get(index, "end")))

        # Tests for is_in_string
        def test_is_in_string_1(self):
            self._test("x = 'y'", "1.0", 0)
        def test_is_in_string_2(self):
            self._test("x = 'y'", "1.2", 0)
        def test_is_in_string_3(self):
            self

# Generated at 2022-06-14 11:43:01.531792
# Unit test for constructor of class HyperParser
def test_HyperParser():
    # _whitespace_chars should include all whitespace chars
    for c in HyperParser._whitespace_chars:
        assert c.isspace()


# Generated at 2022-06-14 11:43:12.347128
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    text = ScrolledText(None, bg="white", width=80, height=25)
    text.pack(expand=YES, fill=BOTH)

    text.insert(END, 'foo = "bar"')
    text.insert(END, "\n")

    text.insert(END, 'foo = "bar')
    text.insert(END, "\n")

    text.insert(END, "foo = 'bar")
    text.insert(END, "\n")

    text.insert(END, "foo = 'bar'")
    text.insert(END, "\n")

    text.mark_set("insert", "1.2")
    assert not HyperParser(text, "insert").is_in_string()

    text.mark_set("insert", "1.6")

# Generated at 2022-06-14 11:43:25.110091
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from unittest import TestCase

    from idlelib import HyperParser

    class TestHyperParserIndex(TestCase):

        """Test the HyperParser class in a single string."""

        def _test(self, string, index, result):
            """Check the HyperParser result for a single string.

            The result is a tuple of different items belonging to the parser
            and computed by the set_index and get_expression methods.
            """
            import tkinter

            text = tkinter.Text()
            text.insert(tkinter.END, string)
            hp = HyperParser(text, index)
            self.assertEqual(
                (hp.rawtext, hp.stopatindex, hp.indexinrawtext, hp.indexbracket),
                result[:4],
            )

# Generated at 2022-06-14 11:44:50.430516
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    hp = HyperParser(text, index)
    assert hp.is_in_code() == True

# Generated at 2022-06-14 11:45:03.908766
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    """Test of method HyperParser.get_surrounding_brackets"""
    import unittest

    class TestCase(unittest.TestCase):
        def testit(self, text, index, exp_brackets, exp_mustclose=None):
            if exp_mustclose is None:
                exp_mustclose = [False, False]
            hp = HyperParser(text, index)
            br = hp.get_surrounding_brackets(mustclose=exp_mustclose[0])
            exp = exp_brackets[0]
            if br is None:
                self.assertIsNone(exp, "return value is None, expected %r" % (exp,))
            else:
                self.assertIsNotNone(exp, "return value is not None, expected None")

# Generated at 2022-06-14 11:45:11.311128
# Unit test for method compute_backslash_indent of class RoughParser

# Generated at 2022-06-14 11:45:14.777515
# Unit test for method is_block_closer of class RoughParser
def test_RoughParser_is_block_closer():
    from importnb import Notebook

    with Notebook():
        from .test_parser import test_RoughParser_is_block_closer
    return test_RoughParser_is_block_closer()



# Generated at 2022-06-14 11:45:17.063331
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = Tk.Text()

# Generated at 2022-06-14 11:45:26.350292
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    # Test is_in_code
    text = r"""\
# This is a comment.
# This is another comment.

print(# This is a comment in a print statement.
"""
    h = HyperParser(text, "1.0")
    assert not h.is_in_code()
    h = HyperParser(text, "2.0")
    assert not h.is_in_code()
    h = HyperParser(text, "3.0")
    assert h.is_in_code()
    h = HyperParser(text, "4.0")
    assert not h.is_in_code()
    h = HyperParser(text, "5.0")
    assert h.is_in_code()
    h = HyperParser(text, "6.0")
    assert h.is_in_code()


# Generated at 2022-06-14 11:45:30.732617
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    # A positive test
    assert HyperParser(EditBoxTestSupport.text0, "2.0").is_in_string()
    # A negative test
    assert not HyperParser(EditBoxTestSupport.text0, "0.0").is_in_string()



# Generated at 2022-06-14 11:45:39.443068
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    import unittest
    import textwrap

    class Test(unittest.TestCase):
        def _test(self, code, openers, mustclose, expected):
            self._test_one(code, openers, mustclose, expected)
            self._test_one(code + ' ', openers, mustclose, expected)
            self._test_one(code + '\n', openers, mustclose, expected)
            self._test_one(code + ' # comment', openers, mustclose, expected)
            self._test_one(code + '\n# comment', openers, mustclose, expected)

        def _test_one(self, code, openers, mustclose, expected):
            code = textwrap.dedent(code)
            hp = HyperParser(code, "1.0")

# Generated at 2022-06-14 11:45:51.978333
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from unittest import TestCase
    from test.test_support import is_resource_enabled, run_unittest

    class HyperParser_set_index(TestCase):
        def setUp(self):
            self.text = Tkinter.Text(Tkinter._default_root, name="test")

        def tearDown(self):
            self.text.destroy()
            del self.text

        def test_HyperParser_set_index(self):
            text = self.text
            hp = HyperParser(text, "1.0")
            self.assertEqual(hp.set_index("1.0"), None)
            text.insert("1.0", "()")
            self.assertEqual(hp.set_index("1.0"), None)

# Generated at 2022-06-14 11:45:57.862073
# Unit test for method compute_backslash_indent of class RoughParser