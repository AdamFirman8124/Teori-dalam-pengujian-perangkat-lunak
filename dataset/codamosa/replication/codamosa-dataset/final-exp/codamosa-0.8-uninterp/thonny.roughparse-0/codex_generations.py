

# Generated at 2022-06-14 11:37:31.039510
# Unit test for constructor of class HyperParser
def test_HyperParser():
    text = Tkinter.Text()
    text.insert(END, "def f():\n    if (1 and #comment\n        2) or 3:\n        pass")
    hp = HyperParser(text, "1.14")
    assert hp.is_in_code()
    assert hp.get_surrounding_brackets() == ("1.13", "1.17")
    assert hp.get_expression() == "2"
    assert not hp.is_in_string()

    hp = HyperParser(text, "1.11")
    assert hp.is_in_code()
    assert hp.get_surrounding_brackets() == ("1.10", "1.17")
    assert hp.get_expression() == ""
    assert not hp.is_in_string()


# Generated at 2022-06-14 11:37:36.307879
# Unit test for constructor of class HyperParser
def test_HyperParser():
    from unittest.mock import Mock

    def index2line(index):
        return int(float(index))

    tk = Mock()
    tk.id = "Text"
    tk.cget = lambda option: 0
    tk.configure = lambda option, value: None
    tk.event_info = lambda *args: {"index": "1.0"}
    text = EditorWindow(tk)
    text.index = lambda index: index
    text.compare = lambda index1, op, index2: bool(eval("%s %s %s" % (index1, op, index2), {"#": 1}))
    text.get = lambda index1, index2: repr(int(float(index1)) - int(float(index2)))
    text.indent_width = 8
    text.tab

# Generated at 2022-06-14 11:37:46.230606
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    global return_value
    return_value = "   "
    text = """if (True):\n"""
    global stmt_start
    stmt_start = 0
    global stmt_end
    stmt_end = 5
    roughParser = RoughParser(text, 0)
    global indent_width
    indent_width = 3
    global tabwidth
    tabwidth = 4
    study1_return_value = 1
    # pylint: disable=no-member
    RoughParser.study1 = Mock(return_value=study1_return_value)
    study2_return_value = 1
    # pylint: disable=no-member
    RoughParser.study2 = Mock(return_value=study2_return_value)
    expected = "   "
    actual = roughParser.get_base_indent_

# Generated at 2022-06-14 11:37:56.734926
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from idlelib.idle_test.mock_idle import Func
    from idlelib.idle_test.htest import run
    h = HyperParser('print(x,y)', '4.0')
    print(h.indexbracket, h.isopener)
    h.set_index('4.13')
    print(h.indexbracket, h.isopener)
    h.set_index('4.7')
    print(h.indexbracket, h.isopener)
    h.set_index('4.5')
    print(h.indexbracket, h.isopener)
    h.set_index('3.0')
    print(h.indexbracket, h.isopener)
    run(Func, h)



# Generated at 2022-06-14 11:38:01.853394
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    rp = RoughParser("")
    assert rp.set_lo(""), ""
    assert rp.set_lo("0"), "0"
    assert rp.set_lo("1"), "1"
    assert rp.set_lo("a"), "a"
    assert rp.set_lo("A"), "A"
    assert rp.set_lo("z"), "z"
    assert rp.set_lo("Z"), "Z"
    assert rp.set_lo("aa"), "aa"
    assert rp.set_lo("Ab"), "Ab"
    assert rp.set_lo("aB"), "aB"
    assert rp.set_lo("AB"), "AB"
    assert rp.set_lo("a0"), "a0"

# Generated at 2022-06-14 11:38:14.677665
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    text = Text()
    text.insert("1.0", """\
a = b.c[d].e(f)
g = "h.i[j].(k)"
l = m."n.o[p].q"
r = 's.t[u].v'
w = x.y[z].A
""")
    hp = HyperParser(text, "1.end")
    def test_index(index, expect):
        hp.set_index(index)
        result = hp.is_in_string()
        if result != expect:
            print("is_in_string(%s) returned %s, expected %s" % (index, result, expect))
    test_index("1.14", True)
    test_index("1.15", False)

# Generated at 2022-06-14 11:38:23.019514
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    rough_parser = RoughParser(
        "\n\n\n\n\n\n\n\n\n",  # str
        8,  # indent_width
        None,  # tabwidth
    )
    assert rough_parser.find_good_parse_start() == 8
    rough_parser = RoughParser(
        "\n\ntry:\n    print(0)\n    pass\nfinally:\n    pass\n\n",  # str
        4,  # indent_width
        None,  # tabwidth
    )
    assert rough_parser.find_good_parse_start() == 54

# Generated at 2022-06-14 11:38:29.096005
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # pylint: disable=redefined-builtin,invalid-name
    assert RoughParser('a = 1\\\nb = 2').compute_backslash_indent() == 5
    assert RoughParser('a = 1\\\nb = 2').compute_backslash_indent() != 6

# Generated at 2022-06-14 11:38:40.723507
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:38:48.161571
# Unit test for method is_block_opener of class RoughParser
def test_RoughParser_is_block_opener():
    def t(source, result):
        parser = RoughParser(source, 0)
        actual = parser.is_block_opener()
        assert actual == result, (
            "expected %s, got %s" % (result, actual) + ":" + source
        )

    # The opening of a class block
    t("   class Test:\n", True)
    t("   class Test(object):\n", True)
    t("   class Test(Test1, Test2):\n", True)

    # The opening of a function block
    t("   def test(self):\n", True)
    t("   def test(self, argument):\n", True)
    t("   def test(self, argument1, argument2):\n", True)

    # This is not the opening of a block
    # (the colon

# Generated at 2022-06-14 11:39:44.437265
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    _test_RoughParser_compute_indent(RoughParser.compute_backslash_indent)

# Generated at 2022-06-14 11:39:54.727255
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    k = RoughParser("")
    k.find_good_parse_start()
    assert k.goodlines == [0, 0]
    k2 = RoughParser("\n")
    k2.find_good_parse_start()
    assert k2.goodlines == [0, 1]
    k3 = RoughParser("a\n")
    k3.find_good_parse_start()
    assert k3.goodlines == [0, 0]
    k4 = RoughParser("\n\n")
    k4.find_good_parse_start()
    assert k4.goodlines == [0, 2]
    k5 = RoughParser("""a\n\n""")
    k5.find_good_parse_start()
    assert k5.goodlines == [0, 1]
    k6 = RoughParser

# Generated at 2022-06-14 11:40:06.677321
# Unit test for constructor of class HyperParser
def test_HyperParser():
    global testcount
    testcount = 0

    def compare(text, index, first, last, expression):
        global testcount

        text = text.replace("\t", " " * 8)
        hp = HyperParser(text, index)
        before = text.rfind("\n", 0, int(float(index))) + 1
        after = text.find("\n", int(float(index)))
        if after == -1:
            after = len(text)
        if first is not None:
            if first != text[before:int(float(index))]:
                raise RuntimeError(
                    "Expected first text `%s'; got `%s'" % (first, text[before:int(float(index))])
                )

# Generated at 2022-06-14 11:40:08.607585
# Unit test for method get_last_open_bracket_pos of class RoughParser
def test_RoughParser_get_last_open_bracket_pos():
    _test_RoughParser_open_bracket(method="get_last_open_bracket_pos")


# Generated at 2022-06-14 11:40:17.964159
# Unit test for method get_last_stmt_bracketing of class RoughParser
def test_RoughParser_get_last_stmt_bracketing():
    script = """\
    a = 1
    if a and b:
        a = 2
    elif a and c:
        a = 3
    """
    rp = RoughParser(script)
    assert rp.get_last_stmt_bracketing() == ((0, 0), (5, 1), (10, 0), (15, 0))
    rp = RoughParser(script, True)
    assert rp.get_last_stmt_bracketing() == ((0, 0), (5, 1), (10, 0), (15, 0))


# Generated at 2022-06-14 11:40:27.565520
# Unit test for constructor of class HyperParser
def test_HyperParser():
    import unittest

    class Test_HyperParser(unittest.TestCase):

        # Return the hyperparser instance under test
        def get_hp(self, *args, **kwargs):
            return HyperParser(*args, **kwargs)

        def get_expression(self, *args, **kwargs):
            hp = self.get_hp(*args, **kwargs)
            return hp.get_expression()

        # Debugging
        def assertEqual(self, first, second, msg=None):
            if first != second:
                print("got raw text",  first)
                print("was expecting", second)

            unittest.TestCase.assertEqual(self, first, second, msg)

        # Assert that the given expression is returned, and that no
        # exception is raised

# Generated at 2022-06-14 11:40:32.685090
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    for i in range(4):
        text = "a ' ' 'b' a"
        p = HyperParser(text, 3 - i)
        assert p.is_in_string() == (i == 0 or i == 2)
        p.set_index(5 - i)
        assert p.is_in_string() == (i == 0 or i == 2)
    # Test that HyperParser works with mixed tabs and spaces
    text = "a ' '\t'b' a"
    p = HyperParser(text, 3)
    assert p.is_in_string()
    p.set_index(5)
    assert p.is_in_string()



# Generated at 2022-06-14 11:40:40.711395
# Unit test for method get_last_stmt_bracketing of class RoughParser
def test_RoughParser_get_last_stmt_bracketing():
    import pprint
    pprint.pprint(RoughParser("print(1,\\n2).rstrip()\\n# comment\\n").get_last_stmt_bracketing())


if __name__ == "__main__":
    test_RoughParser_get_last_stmt_bracketing()

# Generated at 2022-06-14 11:40:42.759000
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    from idlelib.idle_test.htest import run
    run(RoughParserTest)


# Generated at 2022-06-14 11:40:52.920120
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():

    def tester(input, expected, mustclose=False):
        try:
            hp = HyperParser(input, "1.0")
            res = hp.get_surrounding_brackets("([{", mustclose)
            assert (
                res == expected
            ), "Input= %r expected= %r but result was %r" % (input.get("1.0", "end"), expected, res)
        except (ValueError, IndexError, AssertionError):
            print("Input was: %r" % input.get("1.0", "end"))
            raise


# Generated at 2022-06-14 11:41:38.736019
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    from unittest import TestCase

    class _Test(TestCase):
        def _check(self, text, index, expected):
            hp = HyperParser(text, index)
            self.assertEqual(hp.is_in_code(), expected, "%r should be %r" % (text, expected))

    _Test()._check("(", "1.0", False)
    _Test()._check("1 + (", "1.end", False)
    _Test()._check("1 + (2", "1.end", True)
    _Test()._check("1 + ", "1.end", True)
    _Test()._check("1\n    + ", "2.end", True)
    _Test()._check("1\n    + ", "1.end", False)

# Generated at 2022-06-14 11:41:45.266216
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    import unittest
    s = RoughParser()
    # test_RoughParser_set_lo is an alias of test_RoughParser_set_lo_for_string
    s._set_lo( "string")
    assert s.lo == "string"


# Generated at 2022-06-14 11:41:56.645256
# Unit test for constructor of class HyperParser
def test_HyperParser():
    # At the moment, this test is only for the constructor
    class DummyText:
        def __init__(self, content, index, tabwidth):
            self.content = content
            self.index = index
            self.tabwidth = tabwidth

        def get(self, startindex, stopindex):
            return self.content[startindex:stopindex]

        def index(self, index):
            return self.index + index


# Generated at 2022-06-14 11:42:05.396334
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    tk = Tk()
    text = Text(tk)
    text.insert("1.0", "if True:\n    if True:\n        [1].pop(0)")
    text.tag_add("sel", "1.0", "2.0")
    parser = HyperParser(text, "1.0")
    assert parser.is_in_string() == False
    parser.set_index("1.13")
    assert parser.is_in_string() == False
    parser.set_index("2.12")
    assert parser.is_in_string() == False
    parser.set_index("2.16")
    assert parser.is_in_string() == True

# Generated at 2022-06-14 11:42:18.859426
# Unit test for constructor of class HyperParser
def test_HyperParser():
    class DummyText:
        def __init__(self, string):
            self.string = string
            self.index = self.string.index
            self.get = self.string.__getitem__
            self.indentwidth = 8
            self.tabwidth = 8
    text = DummyText("import unittest\n")
    hyp = HyperParser(text, "1.end")
    assert hyp.get_expression() == "unit"
    assert hyp.get_surrounding_brackets("([", True) is None
    text.string = "((a+b)\n"
    hyp = HyperParser(text, "1.end")
    assert hyp.get_surrounding_brackets("([", True) == ("1.0", "1.end")
    hyp = HyperParser(text, "0.end")

# Generated at 2022-06-14 11:42:29.934610
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    """This function tests the HyperParser method get_surrounding_brackets.
    """

    from unittest import TestCase

    class HyperParserTest(TestCase):
        def setUp(self):
            text = Text()
            for s in (
                "if False:\n"
                "    print('Hello')\n"
                "    print('1', '2', '3')\n"
                "\n"
                "print('Goodbye')\n"
            ):
                text.insert("end", s)
            index = text.index("13.0")
            self.parser = HyperParser(text, index)
            self.text = text
            self.index = index


# Generated at 2022-06-14 11:42:39.761176
# Unit test for method find_good_parse_start of class RoughParser

# Generated at 2022-06-14 11:42:52.534460
# Unit test for method compute_bracket_indent of class RoughParser

# Generated at 2022-06-14 11:43:00.167383
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    rp = RoughParser()
    rp.set_lo(0, 0, 0)
    assert rp.level == 0
    assert rp.parenlev == 0
    assert rp.continuation == C_NONE
    assert rp.goodlines == [1]
    assert rp.stmt_start == rp.stmt_end == 0
    assert rp.lastch == ''
    assert rp.lastopenbracketpos is None
    assert rp.stmt_bracketing == ()
    rp.set_lo(1, 2, 3)
    assert rp.level == 1
    assert rp.parenlev == 2
    assert rp.continuation == C_NONE
    assert rp.goodlines == [1]
    assert rp.stmt_start == rp.stmt_

# Generated at 2022-06-14 11:43:11.837496
# Unit test for method is_block_opener of class RoughParser
def test_RoughParser_is_block_opener():
    import unittest
    from idlelib.idle_test.mock_idle import Func
    from idlelib.idle_test.mock_tk import Text
    class RoughParserTest(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            def rp_is_block_opener(event=None):
                text = cls.text
                text.tag_add('sel', '1.0', 'end')
                parser = RoughParser(cls.indentwidth, cls.tabwidth, text)
                cls.is_block_opener_result = parser.is_block_opener()
            cls.rp_is_block_opener = Func(rp_is_block_opener)


# Generated at 2022-06-14 11:44:32.399984
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:44:37.715322
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:44:48.728825
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    def hsgbs(s, *args):
        h = HyperParser(s, "1.0")
        return h.get_surrounding_brackets(*args)

    def do_test(s, expected, *args):
        result = hsgbs(s, *args)
        if expected != result:
            print("'%s' gave %s instead of %s" % (s, repr(result), repr(expected)))

    do_test("a(b[c].d()[e].f())", ("1.0", "1.15"))
    do_test("a(b[c].d()[e].f", None)
    do_test("a(b[c].d()[e].f", None, mustclose=True)



# Generated at 2022-06-14 11:44:54.150003
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    import unittest
    import textwrap

    class TestHyperParser(unittest.TestCase):
        def test_is_in_string(self):
            text = textwrap.dedent(
                """\
                str = """
                '"a\\nb'
                """"\\
                """
                '"\\"'
                """\
                """
                "a"
                '''"'''
                """\
                """
                '"a"'
                """
                """
            )
            #   01234
            #  56789012
            # '............\n............\n............\n............\n............\n............\n'
            # 0:^s
            # 1: s^
            # 2: st^
            # 3: str^
            # 4: str ^
           

# Generated at 2022-06-14 11:44:57.867918
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from test.support import requires
    from test.support.script_helper import assert_python_ok

    requires("gui")
    assert_python_ok("-m", "idlelib.idle")


# Generated at 2022-06-14 11:45:08.540882
# Unit test for method get_continuation_type of class RoughParser
def test_RoughParser_get_continuation_type():
    import py.test
    rough_parser = RoughParser("x=1\\\n + 1\n")
    continuation_type = rough_parser.get_continuation_type()
    py.test.raises(AttributeError, getattr, rough_parser, 'foo')
    py.test.raises(AttributeError, getattr, rough_parser, 'continuation')
    assert continuation_type == C_BACKSLASH
    rough_parser = RoughParser("x = (1,\\\n 2)\n")
    continuation_type = rough_parser.get_continuation_type()
    py.test.raises(AttributeError, getattr, rough_parser, 'foo')
    py.test.raises(AttributeError, getattr, rough_parser, 'continuation')
    assert continuation_type == C_BRACKET
    rough_parser

# Generated at 2022-06-14 11:45:20.821008
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def equal(s, expected):
        print(s)
        parser = RoughParser(s)
        actual = parser.compute_bracket_indent()
        print(actual, expected)
        assert actual == expected

    equal("foo = (\n        bad #)\n        good\n        )", 8)
    equal("foo = (\n        bad #)\n        good\n        (bad)", 8)
    equal("foo = (\n        bad #)\n        good\n        bad)", 8)
    equal("foo = (\n        bad #)\n        good\n        bad", 8)
    equal("foo = (\n        bad #)\n        #)\n        good", 4)
    equal("foo = (\n        bad #)\n        (bad)\n        good", 8)

# Generated at 2022-06-14 11:45:27.890353
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    def test(s):
        hp = HyperParser(s, "1.0")
        if hp.is_in_code():
            print("Code: %s" % s)
        else:
            print("Not code: %s" % s)

    test("a")
    test("'a'")
    test('"a"')
    test("#a")
    test("if 1:\n    a")
    test("if 1:\n    'a'")
    test("if 1:\n    \"a\"")
    test("if 1:\n    #a")
    test("def f():\n    a")
    test("def f():\n    'a'")
    test("def f():\n    \"a\"")
    test("def f():\n    #a")



# Generated at 2022-06-14 11:45:38.133173
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    import unittest

    # test data: three-tuples of strings, where the first string is the
    # Python code, the second string is the index in the code before
    # which the brackets are searched, and the third string is the
    # expected result

# Generated at 2022-06-14 11:45:39.307522
# Unit test for method get_num_lines_in_stmt of class RoughParser