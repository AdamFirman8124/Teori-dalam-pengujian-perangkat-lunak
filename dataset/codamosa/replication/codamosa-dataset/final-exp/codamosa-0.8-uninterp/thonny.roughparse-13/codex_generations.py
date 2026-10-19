

# Generated at 2022-06-14 11:36:24.060984
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    class TkText:

        def __init__(self, text):
            self.text = text

        def get(self, start, end):
            if not start.startswith("insert"):
                raise ValueError("invalid start index: %r" % (start,))
            if not end.startswith("insert"):
                raise ValueError("invalid end index: %r" % (end,))
            if start.endswith(" lineend"):
                lstart = len(self.text.split("\n")[int(start[6])])
                return "\n"
            elif end.endswith(" lineend"):
                lend = len(self.text.split("\n")[int(end[6])])
                return self.text[lstart:lend] + "\n"

# Generated at 2022-06-14 11:36:33.680945
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    x = RoughParser("")
    assert x.compute_backslash_indent() == 0
    x = RoughParser("foo")
    assert x.compute_backslash_indent() == 0
    x = RoughParser("continue\n")
    assert x.compute_backslash_indent() == 8
    x = RoughParser("if 1: continue\n")
    assert x.compute_backslash_indent() == 12
    x = RoughParser("if 1:\\\n    continue\n")
    assert x.compute_backslash_indent() == 12
    x = RoughParser("if 1:\\\n    continue\\\n")
    assert x.compute_backslash_indent() == 12

# Generated at 2022-06-14 11:36:44.290078
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    cases = [
        (r'""', False),
        (r'"f"', False),
        (r'""', False),
        (r"'f'", False),
        (r"''", False),
        (r"#", False),
        (r"#f", False),
        (r"#\n", False),
        (r"f#", False),
        (r"f#f", False),
        (r"f#\n", False),
        (r"f", True),
        (r"f\n", True),
        (r"\\f", True),
        (r'\\f\n', True),
        (r'\\n', True),
    ]

    for case, result in cases:
        text = Text(tkinter.Text())
        text.insert("insert", case)

# Generated at 2022-06-14 11:36:57.846398
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    # pylint: disable=redefined-builtin
    parser = RoughParser("  if True:\n    pass\n")
    assert parser.get_base_indent_string() == "  "
    parser = RoughParser("if True:\n    pass\n")
    assert parser.get_base_indent_string() == ""
    parser = RoughParser("if True:\n\n    pass\n")
    assert parser.get_base_indent_string() == ""
    parser = RoughParser("if True:\n\npass\n")
    assert parser.get_base_indent_string() == ""
    parser = RoughParser("\n  ")
    assert parser.get_base_indent_string() == "  "
    parser = RoughParser("  # a comment\n")
    assert parser.get_base

# Generated at 2022-06-14 11:37:04.050041
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    import io
    import unittest

    # The standard library's own tests

    class Tests(unittest.TestCase):
        def test_compute_bracket_indent(self):
            _tabwidth = 8
            _indent_width = 4
            _parser = RoughParser("", _tabwidth, _indent_width)

            def b(s):
                _parser.set_str(s)
                return _parser.compute_bracket_indent()

            self.assertEqual(b("if 1:\n pass"), 4)
            self.assertEqual(b("if 1:\n  pass"), 4)
            self.assertEqual(b("if 1:\n   pass"), 4)
            self.assertEqual(b("if 1:\n    pass"), 4)

# Generated at 2022-06-14 11:37:11.362890
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    test_str = """\
a = b
if a:

    print('1')
    print('2')

c = d"""
    p = RoughParser(test_str, " ", 4)
    assert p.get_base_indent_string() == "    "
    p = RoughParser(test_str, " ", 2)
    assert p.get_base_indent_string() == "  "

# Generated at 2022-06-14 11:37:15.774877
# Unit test for method is_in_string of class HyperParser

# Generated at 2022-06-14 11:37:36.249873
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    from test.support import run_unittest

    class HyperParserTest(unittest.TestCase):
        def test_get_expression(self):

            def test(expr, pos, text, expected_expr):
                text = text.replace("@", " " * expr.indent_width)
                h = expr.HyperParser(expr, int(float(expr.index("insert"))))
                h.set_index("insert - %dc" % pos)
                result = h.get_expression()
                self.assertEqual(result, expected_expr, f"for {text!r} at position {pos}")

            # test the cases which lead to empty expressions
            # and those which lead to an error

            expr = Text()
            expr.insert("insert", "a [b] c [d] e")
            expr.mark_

# Generated at 2022-06-14 11:37:46.231539
# Unit test for constructor of class HyperParser
def test_HyperParser():
    """Test HyperParser and all its functions."""
    # We construct a text and HyperParser at the index we want.
    text = Text(None, "", 10, "{Tab} ")

    text.insert(END, "def a(self, arg=None):\n")
    text.insert(END, "    ")
    text.insert(END, "if )")
    text.insert(END, "if x:\n")
    text.insert(END, "    ")
    text.insert(END, "self.")
    text.insert(END, "self.method(x, ")
    text.insert(END, "method(1, 2" + ")")
    text.insert(END, "method(1, 2" + ")")
    text.insert(END, "self.")

# Generated at 2022-06-14 11:37:56.761486
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    def test(full_text, expected_chunk, expected_start_index, msg=None):
        # pylint: disable=undefined-variable
        R = RoughParser(full_text, 0)
        chunk, start = R.find_good_parse_start()
        assert chunk == expected_chunk, (chunk, expected_chunk, msg)
        assert start == expected_start_index, (start, expected_start_index, msg)

    test("", 0, 0)
    test("\n", 0, 0)
    test("# hi\n", 0, 0)
    test('if 1:\n    a', 0, 0)
    test('if 1:\n    a\n', 0, 0)
    test('if 1:\n    a\n    ', 0, 0)

# Generated at 2022-06-14 11:39:00.923785
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():

    def test(text, index, result, openers="([{", mustclose=False):
        h = HyperParser(tk.Text(None, "1.0", text), index)
        assert result == h.get_surrounding_brackets(openers, mustclose)

    test("(b) (c)", "1.2", ("1.1", "1.3"))
    test("a(b) (c)", "1.3", ("1.3", "1.5"))
    test("a(b) (c)", "2.2", ("1.3", "1.5"))
    test("a(b) (c)", "2.3", None)
    test("a(b) (c)", "1.0", ("1.0", "1.1"))

# Generated at 2022-06-14 11:39:12.509907
# Unit test for constructor of class HyperParser
def test_HyperParser():

    import unittest

    class HyperParserTestCase(unittest.TestCase):

        def test_constructor(self):
            tests = {
                "text": (
                    "class Class:\n"
                    "    def func(self):\n"
                    "        pass\n"
                    "    pass\n"
                    "\n"
                ),
                "parse_lines": (1, 2, 2, 2, 2, 4),
                "bracket_levels": (0, 1, 2, 1, 1, 0),
                "is_opener": (True, True, True, False, False, False),
                "expressions": ("", "", "", "self", "", ""),
            }
            i = "1.0"
            for j in range(5):
                i = "insert linestart\n"

# Generated at 2022-06-14 11:39:20.454525
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    rp = RoughParser("say(boo)")
    assert rp.compute_bracket_indent() == 4
    rp = RoughParser("say(boo,foo)", indent_width=3)
    assert rp.compute_bracket_indent() == 7
    rp = RoughParser("say(\nboo,\nfoo,)")
    assert rp.compute_bracket_indent() == 4
    rp = RoughParser("say[\nboo,\nfoo,]")
    assert rp.compute_bracket_indent() == 4
    rp = RoughParser("say(\nboo,\nfoo,)\n    pass")
    assert rp.compute_bracket_indent() == 8

# Generated at 2022-06-14 11:39:29.520182
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    test_code = "def f1():\n" "    print '''\n" "    kjkljklj\n" "    ''' # comment\n"

    def _test(h, expected):
        res = h.is_in_code()
        if res != expected:
            raise AssertionError(
                "is_in_code() returned %s instead of %s for %r" % (res, expected, test_code)
            )

    h = HyperParser(tkt.Text(test_code), "1.0")
    _test(h, True)
    h.set_index("1.3")
    _test(h, True)
    h.set_index("1.4")
    _test(h, False)
    h.set_index("2.4")
    _test

# Generated at 2022-06-14 11:39:39.689623
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    h = HyperParser(None, 0)

    assert h.is_in_code()

    h.isopener = [True]
    h.rawtext = ".py"
    h.bracketing = [(0, 1)]
    h.indexbracket = 0
    h.indexinrawtext = 0

    assert not h.is_in_code()

    h.isopener = [False]
    h.bracketing = [(2, 1)]
    h.indexbracket = 0
    h.indexinrawtext = 3

    assert h.is_in_code()

    h.isopener = [False]
    h.bracketing = [(0, 1)]
    h.indexbracket = 0
    h.indexinrawtext = 0

    assert h.is_in_code()


# Generated at 2022-06-14 11:39:51.309817
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    fname = "rough_parser_test.py"
    text = open(fname, "r").read()
    # It is important to know not to parse the docstring of a class
    # as a method
    text = text.replace("def f(self):", "def f(self):\n  return None\n")
    rp = RoughParser(text)
    start_pos, end_pos = rp.find_good_parse_start(len(text))
    # Now apply the parser on the good chunk of code
    node = pygram.python_symbols.suite_stmt.parse(text[start_pos:end_pos])
    print("node=%r" % node)
    return node



# Generated at 2022-06-14 11:40:02.049620
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    class DummyText:
        def __init__(self, ind, tab):
            self.indent_width = ind
            self.tabwidth = tab

        def get(self, index1, index2):
            return self.line[int(index1) : int(index2)]

        def index(self, index1):
            return int(index1.split(".")[0])

    text = DummyText(4, 4)

    # A simple test
    text.line = "def f(x):\n    return x * x\n"
    hp = HyperParser(text, "1.6")
    assert hp.is_in_code()
    assert hp.rawtext == "def f(x):"

# Generated at 2022-06-14 11:40:10.675702
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    rp = RoughParser("[1,\n2,\n3,\n]")
    assert rp.compute_bracket_indent() == 0
    rp = RoughParser("if 1:\n  pass\nelse:\n  [1,\n   2,\n   3,\n]")
    assert rp.compute_bracket_indent() == 3
    rp = RoughParser("foo = [1,\n2,\n3,\n]")
    assert rp.compute_bracket_indent() == 0
    rp = RoughParser("(1,\n2,\n3,\n)")
    assert rp.compute_bracket_indent() == 0

# Generated at 2022-06-14 11:40:23.098192
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    """This function tests the function find_good_parse_start"""

    # The following tests test the function find_good_parse_start from
    # importlib.util

# Generated at 2022-06-14 11:40:31.000356
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    from tkinter import Text, TclError
    from idlelib.idle_test.mock_idle import Func

    def assert_hyper(index, expected_opener_index, expected_closer_index=None):
        hp = HyperParser(text, index)
        actual_opener_index, actual_closer_index = hp.get_surrounding_brackets(")]}")
        assert expected_opener_index == actual_opener_index
        if expected_closer_index is None:
            assert actual_closer_index is None
        else:
            assert expected_closer_index == actual_closer_index

    def assert_hyper_code(index, expected_expression):
        hp = HyperParser(text, index)
        assert expected_expression == hp.get_expression()

    # Test get

# Generated at 2022-06-14 11:41:51.147323
# Unit test for method set_str of class RoughParser
def test_RoughParser_set_str():
    # pylint: disable=missing-docstring,too-many-lines,too-many-locals,too-many-branches
    # pylint: disable=too-many-statements,too-many-nested-blocks,no-self-use
    rp = RoughParser()
    rp.set_str("")
    assert rp.get_continuation_type() == C_NONE
    assert rp.get_num_lines_in_stmt() == 1
    assert not rp.is_block_opener()
    assert not rp.is_block_closer()

    rp.set_str("\n")
    assert rp.get_continuation_type() == C_NONE
    assert rp.get_num_lines_in_stmt() == 1
    assert not r

# Generated at 2022-06-14 11:42:02.205449
# Unit test for method compute_bracket_indent of class RoughParser

# Generated at 2022-06-14 11:42:10.035666
# Unit test for method compute_bracket_indent of class RoughParser

# Generated at 2022-06-14 11:42:22.375871
# Unit test for method get_last_stmt_bracketing of class RoughParser
def test_RoughParser_get_last_stmt_bracketing():
    # pylint: disable=redefined-builtin

    def t(s, expected):
        # see the test cases in _study2 for how to write s
        p = RoughParser(s, 0)
        got = p.get_last_stmt_bracketing()
        assert got == expected, (
            "for input {} got {} instead of {}".format(repr(s), got, expected)
        )

    t("", None)
    t("    ", None)
    t('    #  ', None)
    t('    "a"  ', ((0, 0), (5, 0)))
    t('    """a"""  ', ((0, 0), (9, 0)))

# Generated at 2022-06-14 11:42:27.450740
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    """Tests for HyperParser.set_index
    """

# Generated at 2022-06-14 11:42:38.297480
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    rp = RoughParser("")
    assert rp.find_good_parse_start() == 0
    rp = RoughParser("if 1:\n  pass\n ")
    assert rp.find_good_parse_start() == 0
    rp = RoughParser("if 1:\n  pass\n # comment\n ")
    assert rp.find_good_parse_start() == 0
    rp = RoughParser("if 1:\n  pass\n # comment\n\n ")
    assert rp.find_good_parse_start() == 0
    rp = RoughParser("if 1:\n  pass\n# comment\n")
    assert rp.find_good_parse_start() == 0
    rp = RoughParser("if 1:\n  pass\n# comment\n ")
    assert r

# Generated at 2022-06-14 11:42:44.019447
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    # Check when index is not in a string
    text = 'i = "a" + "b" + "c"'
    hp = HyperParser(text, "1.0")
    assert hp.is_in_string() == 0
    hp.set_index("2.0")
    assert hp.is_in_string() == 0
    hp.set_index("3.0")
    assert hp.is_in_string() == 0
    hp.set_index("4.0")
    assert hp.is_in_string() == 0
    hp.set_index("5.0")
    assert hp.is_in_string() == 0
    hp.set_index("6.0")
    assert hp.is_in_string() == 0
    hp.set_index("7.0")
    assert hp.is_

# Generated at 2022-06-14 11:42:52.657150
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    #This is just a small sampling of string inputs and their expected
    #output. For exhaustive testing, see the test suite in test/test_autopep8.py
    format_string = "{0:>" + str(len("text")) + "}\t{1:>" + str(len("expected")) + "}\t{2:>" + str(
        len("result")) + "}\t{3:>" + str(len("expected == result?")) + "}\t{4:>" + str(len("test name")) + "}"
    header = format_string.format("text", "expected", "result", "expected == result?", "test name")
    print(header)
    print("="*len(header))

    def _format_test_result(text, expected, result, test_name):
        if result == expected:
            passed_text

# Generated at 2022-06-14 11:43:08.855755
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from idlelib.textView import view_text

    text = view_text.ViewText()
    text.delete("1.0", "end")
    text.insert("1.0", "if 1:\n    a = 'a'\nif 2:\n    b = 'b'")
    assert text.index("end-1c") == "5.0"
    hp = HyperParser(text, "1.0")
    assert "a" == hp.get_expression()
    hp.set_index("2.3")
    assert "a" == hp.get_expression()
    hp.set_index("2.4")
    assert "" == hp.get_expression()
    hp.set_index("2.5")
    assert "" == hp.get_expression()
    hp.set_index("2.6")
   

# Generated at 2022-06-14 11:43:14.586498
# Unit test for method get_last_open_bracket_pos of class RoughParser
def test_RoughParser_get_last_open_bracket_pos():
    text = '''\
# testing method get_last_open_bracket_pos of class RoughParser
IFS=" "
a = "hello world"
ID_LIST="{$a}"
echo ${ID_LIST[@]}
'''
    parser = RoughParser(text)
    assert parser.get_last_open_bracket_pos() == 42
    assert parser.get_last_open_bracket_pos() == 42
