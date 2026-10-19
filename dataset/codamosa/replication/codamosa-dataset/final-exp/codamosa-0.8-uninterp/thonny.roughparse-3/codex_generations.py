

# Generated at 2022-06-14 11:41:11.561367
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    test = '''
try:
        if True:
            def func():
                # comment
                pass
            func()
'''
    p = RoughParser(test, 0)
    assert p._study2() == None
    assert p.get_base_indent_string() == '        '
    assert p.continuation == C_NONE


# Generated at 2022-06-14 11:41:20.565740
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:41:33.310584
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    from unittest import TestCase
    from textwrap import dedent

    # Cases to test
    # (text, index, result)

# Generated at 2022-06-14 11:41:40.075957
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    rp = RoughParser(None)

    # test 1
    l1 = " \n"
    l2 = "  xx\n"
    l3 = "   xx\n"
    l4 = "    xx\n"
    hp = "Hello"
    source = l1 + l2 + l3 + l4 + hp
    rp.set_lo(0, source)
    assert rp.lo == 3

    # test 2
    source = l2 + l3 + l4 + hp
    rp.set_lo(0, source)
    assert rp.lo == 2

    # test 3
    source = l3 + l4 + hp
    rp.set_lo(0, source)
    assert rp.lo == 1

    # test 4
    source = l4 + hp

# Generated at 2022-06-14 11:41:53.732559
# Unit test for method get_expression of class HyperParser

# Generated at 2022-06-14 11:42:04.634035
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from test.support import captured_stdout

    for ind in range(21):
        text = Text(
            """\
if 1:
    if 1:
        "string".find()
    if 1: pass
    if 1: pass
    if 1: pass
    try:
        pass
    except:
        pass
    if 1: pass
    while 1:
        if 1:
            if 1:
                pass
            if 1:
                pass
            if 1:
                pass
            if 1:
                pass
        if 1:
            pass
    if 1: pass
        """
        )
        # text.insert('0.0', '\n')
        # text.insert(repr(ind)+'.0', '\n')
        hp = HyperParser(text, repr(ind) + ".0")
        hp

# Generated at 2022-06-14 11:42:06.910242
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    rp = RoughParser("if foo:", 0)
    res = rp.compute_bracket_indent()
    expected = 3
    assert res == expected


# Generated at 2022-06-14 11:42:20.200292
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    # pylint: disable=redefined-builtin
    parser = RoughParser("import sys\nimport os", 0)
    assert parser.get_base_indent_string() == ""
    parser = RoughParser(
        """\
    import sys\n
        import os\n""", 0
    )
    assert parser.get_base_indent_string() == "    "
    parser = RoughParser(
        """\
    import sys\n
    \timport os\n""", 0
    )
    assert parser.get_base_indent_string() == "    \t"
    parser = RoughParser(
        """\
\timport sys\n
\timport os\n""", 0
    )
    assert parser.get_base_indent_string() == "\t"

# Generated at 2022-06-14 11:42:31.258182
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    def _set_and_test(is_in_code, code, index='insert'):
        global hp
        hp = HyperParser(text, index)
        print(
            '%s %s %s'
            % (
                'PASS' if hp.is_in_code() == is_in_code else 'FAIL',
                repr(code),
                repr(index),
            )
        )

    def _set_and_is_in_code(code, index='insert'):
        global hp
        hp = HyperParser(text, index)
        return hp.is_in_code()

    def _test_is_in_code(is_in_code, code):
        _set_and_test(is_in_code, code)

# Generated at 2022-06-14 11:42:40.821829
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def runcase(before, after):
        def index(offset):
            return repr(before.count("\n", 0, offset) + 1) + "." + repr(offset)
        hp = HyperParser(tkinter.Text(None), index(len(before)))
        test = hp.get_expression()
        if test == after:
            return True
        print("for text")
        print(before)
        print('expected', repr(after), 'got', repr(test))
        return False

    fails = 0
    fails += not runcase("42", '')
    fails += not runcase("42\n", '')
    fails += not runcase("   42", '')
    fails += not runcase("42#bla\n", '')
    fails += not runcase("def f(x):\n pass", '')


# Generated at 2022-06-14 11:43:45.402631
# Unit test for constructor of class HyperParser

# Generated at 2022-06-14 11:43:59.028726
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    h = HyperParser(tk.Text(), "1.0")
    h.rawtext = "foo bar"
    h.text = mock.Mock(spec_set=tk.Text)
    h.text.index.side_effect = lambda pos: ("1.0", "1.3").index(pos)
    h.text.get.side_effect = lambda a, b: "1.0" in (a, b) and h.rawtext[a:] or ""
    h.stopatindex = "1.0"
    h.bracketing = [[0, 0]]
    h.isopener = [False]
    h.indexinrawtext = len(h.rawtext)
    h.indexbracket = 0


# Generated at 2022-06-14 11:44:06.154583
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():

    def f(text, expected):
        # pylint: disable=missing-docstring
        p = RoughParser(text, 0)
        got = p.find_good_parse_start()
        assert got == expected, '<%r> != <%r>' % (got, expected)

    # pylint: disable=line-too-long
    f("class A:\n\tdef __init__(self):\n\t\tself.some_var = 0", 8)
    f("class A:\n\tdef __init__(self):\n\t\tself.some_var = 0\n\tdef some_method(self):\n\t\treturn self.some_var\n\tdef other_method(self):\n\t\treturn self.some_var", 33)
    f

# Generated at 2022-06-14 11:44:19.295682
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = Text()
    text.insert("insert", "hi")
    hp = HyperParser(text, "insert")
    hp.set_index("insert")
    assert hp.get_expression() == "hi"
    hp.set_index("insert-1c")
    assert hp.get_expression() == "hi"
    text.insert("insert", " there")
    try:
        hp.set_index("insert")
    except Exception:
        pass
    else:
        raise AssertionError("Error not raised")
    hp = HyperParser(text, "insert")
    assert hp.get_expression() == "hi there"
    hp.set_index("insert-1c")
    assert hp.get_expression() == "hi"
    hp.set_index("insert-2c")
    assert hp.get_expression

# Generated at 2022-06-14 11:44:32.019817
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def test(code, index_at, index_to, index_call, index_else, exp_at, exp_to, exp_call, exp_else):
        hp = HyperParser(code, index_at)
        if exp_at != hp.get_expression():
            return 0
        hp.set_index(index_to)
        if exp_to != hp.get_expression():
            return 0
        hp.set_index(index_call)
        if exp_call != hp.get_expression():
            return 0
        hp.set_index(index_else)
        if exp_else != hp.get_expression():
            return 0
        return 1

    code1 = "self.after(1000, self.update)\n"

# Generated at 2022-06-14 11:44:44.924150
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # pylint: disable=redefined-builtin
    def test(expect, input):
        assert RoughParser(input).compute_backslash_indent() == expect

    input = "a = 1 + 2 +\\\n    3 + 4"
    test(5, input)

    input = "a = 1 + 2 +\\\n    3 + 4 +\\\n    5 + 6"
    test(5, input)

    input = """\
a = 1 + 2 +\\
    3 + 4 +\\
    5 + 6 +\\
    7 + 8 +\\
    9 + 10"""
    test(5, input)


# Generated at 2022-06-14 11:44:52.410699
# Unit test for method compute_bracket_indent of class RoughParser

# Generated at 2022-06-14 11:45:05.366343
# Unit test for method is_in_string of class HyperParser

# Generated at 2022-06-14 11:45:12.108023
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    import unittest

    class TestCase(unittest.TestCase):
        def __init__(self):
            self.hyp = None
            unittest.TestCase.__init__(self, methodName="test")

        def setUp(self):
            # import here to avoid circularity
            from idlelib.textView import TextViewer

            # Create a textviewer with a document to analyze
            data = "ab(cde)fg\ncode before 'string'\ncode #comment\n"
            text = TextViewer.TextViewer(None, None, None)
            text.set_text(data)
            # Move the cursor in the right place
            self.hyp = HyperParser(text, "%d.0" % 3)

        def tearDown(self):
            pass


# Generated at 2022-06-14 11:45:23.911749
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    assert RoughParser("  \n  \n").find_good_parse_start() == 4
    assert RoughParser("  \n  #\n").find_good_parse_start() == 4
    assert RoughParser("  \n  \n  #\n").find_good_parse_start() == 6
    assert RoughParser("  \n  #\n  #\n").find_good_parse_start() == 6
    assert RoughParser("  \n  \n  \n").find_good_parse_start() == 6
    assert RoughParser("  \n  \n  \n  #\n").find_good_parse_start() == 6
    assert RoughParser("  \n  \n  #\n  #\n").find_good_parse_start() == 6

# Generated at 2022-06-14 11:46:15.841981
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    """This method tests the HyperParser.set_index() method.
    
    The test is quite extensive, in order to test a variety of
    corner cases.
    """

    # We create a very simple text, with a single line of code.
    text = Text(None, "    abcdef")

    # Create a HyperParser for it.
    hp = HyperParser(text, "6.0")

    # Check the start and end of the text are in the correct bracket.
    assert hp.bracketing == [(0, 0), (7, 0), (8, 0)]

    # The end of the text should be in a non-opener bracket
    assert not hp.isopener[2]

    # We will use this function to verify the results of get_expression()

# Generated at 2022-06-14 11:46:24.158567
# Unit test for method compute_bracket_indent of class RoughParser

# Generated at 2022-06-14 11:46:31.726629
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    from idlelib.idle_test.mock_idle import Func

    # This is a subset of the definitions in idlelib.colorizer.ColorDelegator.
    # It tests that certain lines do not raise an exception and returns the
    # result for each line.
    def line_is_code(text):
        pos = text.index("|")
        # The line must end in a newline.
        text += "\n"
        # Create a text widget and insert the line
        text_tk = tkinter.Text()
        text_tk.insert("1.0", text)
        # Create a ColorDelegator and bind it to the text widget.
        colorizer = idlelib.colorizer.ColorDelegator()
        colorizer.insertfilter(text_tk)
        # Create a HyperParser for the text and position.

# Generated at 2022-06-14 11:46:46.852779
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    from idlelib import parenmatch

    print("Hyperparser test")

    # class to get a text widget for testing HyperParser
    class MyText:
        def __init__(self, text, index):
            self.text = text
            self.index = index

        def index(self, index):
            return index

        def get(self, firstindex, lastindex):
            return self.text[firstindex:lastindex]

        def indent_width(self):
            return 4

        def tabwidth(self):
            return 8

    # a test case is a tuple
    # (text, index,parenmatch.OPENERS,parenmatch.CLOSERS, mustclose)

# Generated at 2022-06-14 11:46:59.564496
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    # Test of a bad input at the end
    assert HyperParser("foo()", "1.3").get_surrounding_brackets() is None
    assert HyperParser("foo()", "1.3").get_surrounding_brackets(mustclose=True) is None
    # Test of a bad input at the beginning
    assert HyperParser("()foo", "1.0").get_surrounding_brackets() is None
    assert HyperParser("()foo", "1.0").get_surrounding_brackets(mustclose=True) is None
    # Test of a bad input in the middle
    assert HyperParser("foo()bar", "1.4").get_surrounding_brackets() is None
    assert HyperParser("foo()bar", "1.4").get_surrounding_brackets(mustclose=True) is None

# Generated at 2022-06-14 11:47:12.929771
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    def f(str, errors, goodline, expected):
        rp = RoughParser(str, errors)
        actual = rp.find_good_parse_start()
        assert actual == expected, (
            "expected %s, got %s" % (expected, actual)
        )
        if expected is not None:
            errors.seek(0)
            actual_errs = errors.readlines()
            assert actual_errs == []

    import io
    import random

    # Note that the tests below can't reliably test the case where the
    # good parse start is before where the error start is supposed to be,
    # because the reported error start is approximate.

    # First, test the trivial case where no errors occur
    f("def f():\n return 42\n", io.BytesIO(), 1, (1, 2))

    #

# Generated at 2022-06-14 11:47:20.314417
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    # pylint: disable=too-many-branches,too-many-statements,too-many-locals,too-many-nested-blocks
    def compare_results(source, index, expected):
        """Given a source string and an index into it, and an expected result,
        call HyperParser.get_expression on the source and index and compare
        the result with the expected result.
        """
        index = source.index(index)
        hp = HyperParser(source, index)
        actual = hp.get_expression()
        if actual != expected:
            _tests_failed.append(
                "In\n%s\nHyperParser.get_expression found %s at %s instead of %s"
                % (source, actual, index, expected)
            )


# Generated at 2022-06-14 11:47:31.958905
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():

    s = "for a in [\n" + (
        "6,\n" * 20
        + "7,\n" * 50
        + "8,\n" * 30
        + "9]:\n" * 10
        + "\tprint(a)\n"
        + "\n"
        + "\n"
    )
    parser = RoughParser(s)
    parser._study2()
    print(len(s))
    print(len(parser.str))
    print(parser.get_num_lines_in_stmt())
    print(parser.compute_bracket_indent())


# Generated at 2022-06-14 11:47:46.731444
# Unit test for method get_expression of class HyperParser

# Generated at 2022-06-14 11:47:54.243628
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():

    p = RoughParser("]", False, 0, 0)
    p._set_lo("[")
    assert p.lastopenbracketpos == 0

    p = RoughParser("]", False, 0, 0)
    p._set_lo("()")
    assert p.lastopenbracketpos == 1

    p = RoughParser("]", False, 0, 0)
    p._set_lo("")._set_lo("(")
    assert p.lastopenbracketpos == 1

    p = RoughParser("]", False, 0, 0)
    p._set_lo("(]")._set_lo("(")
    assert p.lastopenbracketpos == 1

    p = RoughParser("]", False, 0, 0)
    p._set_lo("(")
    assert p.lastopenbracketpos == 1

