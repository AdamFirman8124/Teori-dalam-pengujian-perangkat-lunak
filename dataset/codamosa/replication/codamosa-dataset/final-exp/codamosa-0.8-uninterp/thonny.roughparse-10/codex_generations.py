

# Generated at 2022-06-14 11:40:46.209593
# Unit test for method get_last_open_bracket_pos of class RoughParser

# Generated at 2022-06-14 11:41:00.192924
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    import unittest

    class RoughParserTest(unittest.TestCase):

        def test_get_base_indent_string_1(self):
            # empty string
            rp = RoughParser("", 0, "")
            rp.set_str("")
            self.assertEqual(rp.get_base_indent_string(), "")

        def test_get_base_indent_string_2(self):
            # only whitespace
            rp = RoughParser("", 0, "")
            rp.set_str("       ")
            self.assertEqual(rp.get_base_indent_string(), "       ")

        def test_get_base_indent_string_3(self):
            # indentation and stuff
            rp = RoughParser("", 0, "")


# Generated at 2022-06-14 11:41:06.355451
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    parser = HyperParser("'''abc''' 'abc' \"abc\" # abc", "8.0")
    tests = (
        (2, 3, False),
        (5, 10, True),
        (11, 15, False),
        (16, 20, True),
        (21, 24, True),
        (25, 35, False),
    )
    for i in range(len(tests)):
        parser.set_index("%d.%d" % tests[i][:2])
        assert parser.is_in_string() == tests[i][2], ("is_in_string test %d failed" % (i + 1))

# Generated at 2022-06-14 11:41:18.112955
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():

    def _r(s, indent_width=0, tabwidth=8):
        p = RoughParser(s, indent_width, tabwidth)
        if p.get_continuation_type() == C_BACKSLASH:
            return p.compute_backslash_indent()
        return None

    assert _r("x = 2 + \\\n     3") == _r("x = 2 + \\\r     3") == 10
    assert _r("x = 2 + \\") is None
    assert _r("x = 1 + \\\n1") == _r("x = 1 + \\\r1") == 7
    assert _r("x = 1 + \\\n      1") == _r("x = 1 + \\\r      1") == 15
    assert _r("x = 1 + \\\n    \\") is None


# Generated at 2022-06-14 11:41:31.766763
# Unit test for method get_continuation_type of class RoughParser

# Generated at 2022-06-14 11:41:36.536730
# Unit test for method is_block_opener of class RoughParser
def test_RoughParser_is_block_opener():
    text = "if 1:\n  pass\n"
    rp = RoughParser(text, indent_width=2, tabwidth=2)
    assert rp.is_block_opener() == 1
    text = "if 1:\n  pass"
    rp = RoughParser(text, indent_width=2, tabwidth=2)
    assert rp.is_block_opener() == 0



# Generated at 2022-06-14 11:41:51.591870
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    import unittest
    import re

    class GetExpressionTest(unittest.TestCase):
        """Test the method get_expression of class HyperParser."""

        # The set of built-in identifiers which are also keywords,
        # i.e. keyword.iskeyword() returns True for them
        ID_KEYWORDS = frozenset({"True", "False", "None"})

        # The set of keywords that are also special names for which
        # the special name rules are not applied.
        _KEYWORDS_SNA = {"not", "and", "or"}

        def test_empty_source(self):
            """Test if the text is empty."""
            self.check_get_expression_results(
                "", 0, True, [(0, "")],
            )


# Generated at 2022-06-14 11:42:02.943086
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    # pylint: disable=redefined-outer-name

    def t(str, indent_width, tab_width, result):
        rp = RoughParser(str, indent_width, tab_width)
        assert rp.compute_bracket_indent() == result

    t(
        "foo = {\n" "  'bar': [\n" "    {'biz': 1},\n" "    {'baz': 2},\n" "   ]\n" "}",
        indent_width=4,
        tab_width=8,
        result=4,
    )

# Generated at 2022-06-14 11:42:10.345922
# Unit test for method get_expression of class HyperParser

# Generated at 2022-06-14 11:42:22.630933
# Unit test for method set_lo of class RoughParser

# Generated at 2022-06-14 11:44:16.743542
# Unit test for constructor of class HyperParser
def test_HyperParser():
    #        0123456789012345678901234567890123456789012345678901234567890123456789
    text = ("\nimport os\nif x == 1:\n    print x\n" + 'y = "hello"\nprint y\n')
    #                                                           ^
    #                                                           |
    h = HyperParser(text, "24.0")
    if h.is_in_string():
        print("Failed: should not be in string")
    if not h.is_in_code():
        print("Failed: should be in code")
    if h.get_expression() != "y":
        print("Failed: expression is %r" % h.get_expression())

# Generated at 2022-06-14 11:44:23.873141
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    # {{{
    from idlelib import parenmatch

    def test_case(idle_format, stop_index, expected_output):
        """Replace stopindex with the tuple (line, column)"""
        if stop_index is not None:
            stop_index = parenmatch.make_index_pair(stop_index)

        output = idle_format.get_surrounding_brackets()
        if output != expected_output:
            raise AssertionError(
                "Wrong output. %s: got %s, expected %s"
                % (idle_format.get_expression(), str(output), str(expected_output))
            )


# Generated at 2022-06-14 11:44:30.030139
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():

    def check(s, expected):
        r = RoughParser(s, 0)
        r._study1()
        r._study2()
        actual = r.compute_backslash_indent()
        assert actual == expected, (s, expected, actual)

    check('a = \\\n  b', 4)
    check('a = \\\n  b + \\\n  c', 4)
    check('a = \\', 1)
    check('def f(a, b=\\\n  c, d=\\\n  e):\n  pass', 4)
    check('if a:\\\n  b\nelif c:\\\n  d\nelse:\\\n  e', 2)


_junkre = re.compile(r"^\s*(#|$)").match



# Generated at 2022-06-14 11:44:32.565344
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    h = HyperParser(
        tkinter.Text(), "1.0"
    )  # A dummy text box, which we don't need in the tests.

# Generated at 2022-06-14 11:44:45.483937
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    string = textwrap.dedent(
            """\
            def f():
                x = 0
                return x
            def g():
                x = 0
            x = 1
            """
        )
    rp = RoughParser(string)
    assert rp.find_good_parse_start(0, len(string)) == 0
    assert rp.find_good_parse_start(8, len(string)) == 8
    assert rp.find_good_parse_start(len(string), len(string)) == len(string)
    assert rp.find_good_parse_start(len(string) - 3, len(string)) == len(string) - 3
    assert rp.find_good_parse_start(len(string) - 4, len(string)) == len(string) - 4

# Generated at 2022-06-14 11:44:58.854390
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:45:09.057125
# Unit test for method is_in_string of class HyperParser

# Generated at 2022-06-14 11:45:21.318385
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    text = Text()
    text.insert(INSERT, "def is_in_code():\n  print('hi')\n")

    # Test line with code, inside code
    h = HyperParser(text, INSERT)
    assert is_in_code() == True

    # Test line with code, inside string
    text.mark_set(INSERT, '1.20')
    h = HyperParser(text, INSERT)
    assert is_in_code() == False

    # Test line with code, inside comment
    text.mark_set(INSERT, '1.28')
    h = HyperParser(text, INSERT)
    assert is_in_code() == False

    # Test line with string
    text.mark_set(INSERT, '2.0')
    h = HyperParser(text, INSERT)


# Generated at 2022-06-14 11:45:28.519041
# Unit test for method __iter__ of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping___iter__():
    whitespace_chars = ' \t\n\r'
    preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
    out = " ".join(map(chr, list(mapping)))
    assert out == " \t\n\r", repr(out)

# Generated at 2022-06-14 11:45:38.383229
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # pylint: disable=protected-access
    def do_test(input, expected, tabwidth=8, indentwidth=4):
        rp = _RoughParser(input, tabwidth, indentwidth)
        actual = rp.compute_backslash_indent()
        assert actual == expected, repr(
            (
                input,
                expected,
                actual,
                rp.str,
                rp.stmt_start,
                rp.continuation,
            )
        )

    do_test("""\
x = 1 + \\
    2
""", 5)

    do_test("""\
x = 1 + \\
      2
""", 8)

    do_test("""\
x = 1 + (\\
    2 +
    3) + 4
""", 5)

    do

# Generated at 2022-06-14 11:46:23.340183
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    import tkinter
    from idlelib.editor import EditorWindow
    tk = tkinter.Tk()
    tk.withdraw()
    editwin = EditorWindow(tk, None)
    text = editwin.text
    text.delete("1.0", "end")
    text.insert("1.0", "def f(a=0, b=1)\n" "def g(a=0, b=1)\n" "def h(a=0, b=1)\n")
    text.mark_set("insert", "1.2")
    parser = HyperParser(text, text.index("insert"))
    parser.set_index(text.index("1.10"))
    assert parser.indexinrawtext == 10
    parser.set_index(text.index("1.11"))
    assert parser.index

# Generated at 2022-06-14 11:46:31.410790
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = Text(None, {
        "undo": 1,
        "indentwidth": 4,
        "tabwidth": 4,
    })
    text.insert("insert", "a = [3,\n")
    text.mark_set("insert", "insert + 2l")
    text.insert("insert", "5]\n")

    parser = HyperParser(text, text.index("insert"))
    # If get_surrounding_brackets worked, we would just compare their
    # results. This way we find many more errors.
    assert parser.indexinrawtext == (
        len(parser.rawtext) - len(text.get("insert", parser.stopatindex))
    )
    assert parser.indexbracket == 1
    assert parser.isopener == [False, False, False]
    parser.set_

# Generated at 2022-06-14 11:46:46.676969
# Unit test for method compute_backslash_indent of class RoughParser

# Generated at 2022-06-14 11:46:59.421366
# Unit test for constructor of class HyperParser
def test_HyperParser():
    global test_HyperParser_text
    if not test_HyperParser_text:
        return
    print("Testing HyperParser")

    def test(text, index, code, string, identifier, brackets, expr):
        print("*" * 60)
        print("Testing HyperParser with index", index)
        print("Text:", repr(text))
        print("Index:", index, "->", repr(text.index(index)))
        hp = HyperParser(text, index)
        print("Rawtext:", repr(hp.rawtext))
        print("Bracketing:", hp.bracketing)
        print("Isopener:", hp.isopener)
        print("Indexbracket:", hp.indexbracket)
        print("Indexinrawtext:", hp.indexinrawtext)

# Generated at 2022-06-14 11:47:12.626700
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:47:20.223853
# Unit test for method set_index of class HyperParser

# Generated at 2022-06-14 11:47:25.720930
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    import unittest

    class IsInCodeTestCase(unittest.TestCase):
        """Test whether the HyperParser works properly.

        is_in_code is the key function of HyperParser.
        """

        def setUp(self):
            from idlelib.textView import TextViewer

            self.text = TextViewer(None)

# Generated at 2022-06-14 11:47:33.640021
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    # Bug 1154: Report for Hyperparser.is_in_code()
    """>>> test_HyperParser_is_in_code()
    True
    """
    root = Tk()
    root.withdraw()
    text = Text(root)
    text.insert('1.0', 'l = [1, 2, 3]\\n')
    text.insert('2.0', 'print l[1]\\n')
    h = HyperParser(text, '2.0')
    def test():
        print(h.is_in_code())
    test()
    root.destroy()


# Generated at 2022-06-14 11:47:47.084591
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    # pylint: disable=redefined-builtin
    rp = RoughParser(verbose=0)
    rp.set_lo("   ")
    assert rp.get_indent_width() == 3
    assert rp.get_base_indent_string() == "   "
    assert repr(rp.get_last_stmt_bracketing()) == "(   )"

    rp.set_lo("a = 2")
    assert rp.get_indent_width() == 0
    assert rp.get_base_indent_string() == ""
    assert repr(rp.get_last_stmt_bracketing()) == "(a = 2)"

    rp.set_lo("a = 1\nb = 2")
    assert rp.get_indent_width() == 0


# Generated at 2022-06-14 11:47:54.532014
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    # pylint: disable=redefined-builtin
    # test case 1: just a bracket
    rp = RoughParser("", 0, 0)
    rp.str = "helloworld(goodbye)"
    rp.goodlines = (0, 10)
    rp.continuation = 0
    rp.lastopenbracketpos = 10
    assert rp.compute_bracket_indent() == 11

    # test case 2: a bracket followed by an interesting statement
    rp = RoughParser("", 0, 0)
    rp.str = "helloworld(goodbye)\n    say(hello)"
    rp.goodlines = (0, 11)
    rp.continuation = 0
    rp.lastopenbracketpos = 10
    assert rp.compute_bracket_indent()