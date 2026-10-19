

# Generated at 2022-06-14 11:38:07.222613
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    rp = RoughParser("foo = some_very_long_function_call() \\", "")
    assert rp.compute_backslash_indent() == 0
    rp = RoughParser("foo = some_very_long_function_call()\\", "")
    assert rp.compute_backslash_indent() == 0
    rp = RoughParser("    foo = some_very_long_function_call() \\", "")
    assert rp.compute_backslash_indent() == 4
    rp = RoughParser("    foo = some_very_long_function_call()\\", "")
    assert rp.compute_backslash_indent() == 4
    rp = RoughParser("foo = some_very_long_function_call() # comment", "")
    assert rp

# Generated at 2022-06-14 11:38:17.235585
# Unit test for method is_in_string of class HyperParser

# Generated at 2022-06-14 11:38:23.712778
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    tests = ["'''", 'u"""', "r'''", 'ur"""', 'b"', 'br"', 'u"', 'ur"', "r'", "rb'"]
    for t in tests:
        h = HyperParser(t, len(t))
        assert h.is_in_string(), t

# Generated at 2022-06-14 11:38:25.407396
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    def t1():
        """check simple cases"""

        text = Text()

# Generated at 2022-06-14 11:38:33.662121
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    """Test method is_in_code of class HyperParser"""

    test_code = "'''\nEating string and comments\n'''"
    text = ParserTextWrapper(test_code)

    parser = HyperParser(text, "1.0")
    assert not parser.is_in_code()

    parser.set_index("1.12")
    assert not parser.is_in_code()

    parser.set_index("1.11")
    assert not parser.is_in_code()

    for charindex in ("1.8", "1.10", "1.11", "1.12", "1.13", "1.14"):
        parser.set_index(charindex)
        assert parser.is_in_code()


# Generated at 2022-06-14 11:38:45.758513
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    if True:
        # Test with a trivial string
        assert RoughParser("xx").compute_bracket_indent() == 2
        # Test with a trivial string and a non-standard indent_width
        assert RoughParser("xx", indent_width = 3).compute_bracket_indent() == 3

    if True:
        # Test with a string with a open bracket without continuation
        assert RoughParser("foo([])").compute_bracket_indent() == 3
        # Test with a string with a open bracket without continuation and a non-standard indent_width
        assert RoughParser("foo([])", indent_width = 2).compute_bracket_indent() == 2

    if True:
        # Test with a string with a open bracket with continuation
        assert RoughParser("foo(\n  []\n)").compute_bracket_ind

# Generated at 2022-06-14 11:38:53.294447
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    def test(text, index, wanted):
        got = HyperParser(text, index).is_in_string()
        if got != wanted:
            print(
                """Method is_in_string of class HyperParser fails on
                text "%s", index %s, wanted %s, got %s."""
                % (text, index, wanted, got)
            )

    test('"""a"""', "1.1", 0)
    test('"a"', "1.2", 1)
    test('"a" #b', "1.3", 1)
    test('"a" #b', "1.4", 1)
    test('"""a""" #b', "1.5", 0)
    test('"""a""" #b', "1.6", 0)

# Generated at 2022-06-14 11:39:00.456930
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def test(s):
        p = RoughParser(s)
        indent = p.compute_bracket_indent()
        return indent

    assert test(
        """
        if x == 3:
            y = 2
        elif x == 2:
            y=1
        else:
            some_fn_call(x)
        """.strip()
    ) == 4
    assert test(
        """
        if x == a:
            if y == b:
                c = x + y
        elif x > 3:
            some_fn_call(x)
        """.strip()
    ) == 4
    assert test(
        """
        if x == 1:
            y == 2
        else:
            if x == 3:
                y == 4
        """.strip()
    ) == 8
   

# Generated at 2022-06-14 11:39:05.084589
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # pylint: disable=undefined-variable,invalid-name
    import doctest

    # RoughParser.compute_backslash_indent() is actually
    # quite hard to test, since it is intimately tied up with
    # cStringIO.StringIO and StringO.seek().  We use this
    # carefully coded little class to fake StringIO for the
    # tests.
    class StringIO_Switcher:
        # pylint: disable=invalid-name
        # original StringIO
        orig = None

        def __enter__(self):
            self.orig = StringIO
            StringIO = self.StringIO
            return self

        def __exit__(self, *args, **kwds):
            StringIO = self.orig


# Generated at 2022-06-14 11:39:17.653619
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    from unittest import main

    class Test(unittest.TestCase):
        def test_method(self):
            for s in (
                "abcd",
                '"abcd"',
                '"""abcd"""',
                '"abcd',
                "abcd''",
                r"abcd\'",
                "abcd\\'",
                "abcd\"",
                r"abcd\"",
                "abcd\\\"",
            ):
                for i, in_s in enumerate(
                    [False, True, True, True, False, False, False, False, False, False]
                ):
                    p = HyperParser(s, "%d.0" % i)
                    self.assertEqual(p.is_in_string(), in_s)

    main()



# Generated at 2022-06-14 11:39:56.164903
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():

    def check(tests):
        for text, index, mustclose, answer in tests:
            if isinstance(text, str):
                text = text.replace("<tab>", "\t")
            hp = HyperParser(text, index)
            r = hp.get_surrounding_brackets(mustclose=mustclose)
            if r != answer:
                if answer is None:
                    print('\nError: while analyzing "%s" at index "%s" with' "mustclose=%s" % (text, index, mustclose))
                    print("Expected None, got %s" % r)
                else:
                    print('\nError: while analyzing "%s" at index "%s" with' "mustclose=%s" % (text, index, mustclose))

# Generated at 2022-06-14 11:40:07.791284
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    for input_text, indent, msg in [
        ('for i in range(10):\\\n', 8, "normal case"),
        ('for i in range(10):\\\n# hello\n', 8, "with comment"),
        ('x,\\\n', 4, "one-line stmt"),
        ('for i,\\\n', 8, "one-line assignment"),
        ('for\\\n', 4, "one-line non-assignment"),
    ]:
        check = RoughParser(input_text, 0).compute_backslash_indent()
        assert check == indent, msg


# ========================
# = Class PrettyPrinter =
# ========================
# The class that actually does the work.
#
# The interface is the method pformat().
#
# The method is able to format a number of

# Generated at 2022-06-14 11:40:21.020034
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    import unittest

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.text = Tkinter.Text()
            self.text.insert("insert", self.sample)
            self.hp = HyperParser(self.text, "insert")

        def tearDown(self):
            self.text.destroy()
            del self.text
            del self.hp

        def test_get_surrounding_brackets(self):
            self.assertEqual(self.hp.get_surrounding_brackets(), self.result)

    def create_TestCase_subclass(sample, result):
        return type(sample + "TestCase", (TestCase,), {"sample": sample, "result": result})


# Generated at 2022-06-14 11:40:30.153224
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    import sys
    import __main__

    # Obtain the name of this test file
    fname = sys.argv[0]

    # Obtain the length of this test file
    with open(fname, "rb") as f:
        code_text = f.read()
    # Remove the first two lines (they contain the docstring)
    code_text = code_text[code_text.find(b"\n") + 1 :]
    code_text = code_text[code_text.find(b"\n") + 1 :]

    # Create a text which contains the text of this file
    text = Text(code_text)

    # The index at the start of the text
    index = text.index("1.0")
    # The HyperParser will analyze the surroundings of this index

# Generated at 2022-06-14 11:40:45.084225
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = EditorWindow(None)
    text.set_root_widget(tkinter.Text())
    text.tabwidth = 8
    text.indentwidth = 8
    text.set("if blah:\n    pass\n")
    index = text.index("1.4")
    parser = HyperParser(text, index)
    parser.set_index(index)
    assert parser.indexinrawtext == 4
    assert parser.indexbracket == 1
    assert parser.bracketing[parser.indexbracket][0] == 4
    assert parser.bracketing[parser.indexbracket][1] == 1
    assert parser.is_in_code()
    assert not parser.is_in_string()
    assert parser.get_expression() == "blah"


# Generated at 2022-06-14 11:40:53.982828
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    x = RoughParser("")
    assert x.compute_backslash_indent() == 0
    x = RoughParser("\\")
    assert x.compute_backslash_indent() == 1
    x = RoughParser("  \\")
    assert x.compute_backslash_indent() == 3
    x = RoughParser("  a\\")
    assert x.compute_backslash_indent() == 3
    x = RoughParser("a  \\\n   b")
    assert x.compute_backslash_indent() == 5
    x = RoughParser("a  \\ \\ \\\n   b")
    assert x.compute_backslash_indent() == 5
    x = RoughParser("a  \\ \\\n   b")
    assert x.compute_backslash_

# Generated at 2022-06-14 11:41:03.468799
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    import unittest

    class TestHyperParserGetSurroundingBrackets(unittest.TestCase):
        CONTENT = (
            "class foo:\n"
            "    def bar():\n"
            "        if (True):\n"
            "            pass\n"
            "        elif (False):\n"
            "            pass\n"
            "        else:\n"
            "            pass\n"
            "\n"
            "print(foo())\n"
            "\n"
            "    class baz:\n"
            "        pass\n"
        )

        def setUp(self):
            text = Text()
            text.insert("1.0", self.CONTENT)
            self.parser = HyperParser(text, "1.0")


# Generated at 2022-06-14 11:41:15.823551
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def get_expression(rawtext, index):
        hp = HyperParser(Text(None, rawtext), "%d.%d" % (index + 1, 0))
        return hp.get_expression()

    def testcase(rawtext, index, expected):
        result = get_expression(rawtext, index)
        assert result == expected, "get_expression(%r, %d) == %r != %r" % (
            rawtext,
            index,
            result,
            expected,
        )

    testcase("abc", 2, "")
    testcase(" abc", 2, "")
    testcase("a.b", 2, "a")
    testcase("a. b", 2, "a")
    testcase("a.  b", 2, "a")

# Generated at 2022-06-14 11:41:25.000989
# Unit test for method get_base_indent_string of class RoughParser

# Generated at 2022-06-14 11:41:36.147931
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    bnch = TixTestBench()
    master = bnch.tix.Tk()
    w = tk.Text(master)
    # Modify the text, then adjust the index in x, then expect y.

# Generated at 2022-06-14 11:42:39.538252
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    def run_test(
        text,
        indent_width=4,
        tab_width=8,
        over_indent_width=0,
        dedent_width=0,
        expected_indent_width=0,
    ):
        print_("text:\n%r" % text)
        parser = RoughParser(
            text,
            indent_width=indent_width,
            tab_width=tab_width,
            over_indent_width=over_indent_width,
            dedent_width=dedent_width,
        )
        indent_width = parser.compute_backslash_indent()
        print_("... indent_width: %r" % indent_width)
        print_("... expected_indent_width: %r" % expected_indent_width)
       

# Generated at 2022-06-14 11:42:52.482161
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    """Test HyperParser method set_index.

    This is not included in test_hyperparser, since it needs access to
    the internal attributes.
    """

    def do(index, bracketing, indexbracket):
        hyperpars.set_index(index)
        if hyperpars.bracketing != bracketing:
            return False
        if hyperpars.indexbracket != indexbracket:
            return False
        return True

    text = r"""
    def foo(a, b,
             c,
             d="a b c",
             e=("a", "b", "3"),
             f={"a":"b"},
             g=[1, "a"]):
        return a, b, c, d, e, f, g
    """

    text += " "  # Used internally by PyParse

# Generated at 2022-06-14 11:42:57.878884
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    str_ = """
if True:
    pass
else:
    pass

"""
    rp = RoughParser(str_)
    assert rp.get_base_indent_string() == "    "

    str_ = """
if True:
    pass
else:
    pass

foo = 5

"""
    rp = RoughParser(str_)
    assert rp.get_base_indent_string() == ""



# Generated at 2022-06-14 11:43:10.799306
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    text = textwidget.Text()
    for openers, s, mustclose in [
        ("([{", "foo(bar", False),
        ("([{", "foo(bar)", True),
        ("([{", "x = foo(bar", False),
        ("([{", "x = foo(bar)", True),
        ("([{", "x = foo(bar) + 1", False),
        ("([{", "x = foo(bar) + 1", True),
        ("([{", "x = foo(bar)+1", True),
        ("([{", "x = foo(bar.baz)", True),
    ]:
        hp = HyperParser(text, "1.0")
        text.insert("1.0", s)
        res = hp.get_surrounding_brackets(openers, mustclose)


# Generated at 2022-06-14 11:43:21.938379
# Unit test for constructor of class HyperParser
def test_HyperParser():
    # Rough example, which must provide a valid result.
    text = r"""
# A comment
a = (b +    # Another comment
     c) +\
    d
"""
    # A valid result is:
    # rawtext:           '\na = (b +    # Another comment\n     c) +\n    d\n '
    # bracketing:        [(2, 0), (3, 0), (12, 1), (21, 0), (22, 1), (31, 0), (32, 1), (40, 0)]
    # stopatindex:       '7.4'
    # indexbracket:      5
    # indexinrawtext:    31

    testobj = HyperParser(tk.Text(None), "1.0")
    testobj.text.insert("1.0", text)
    testobj

# Generated at 2022-06-14 11:43:29.605677
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    class DummyText:
        def __init__(self, content):
            self.content = content
            self.indent_width = 8
            self.tabwidth = 8

        def get(self, start, stop):
            return self.content[start - 1 : stop - start + 1]

        def index(self, i):
            return i

        def __getitem__(self, i):
            return self.content[i - 1 : i]

    class DummyParser:
        def __init__(self, brackets):
            self.bracketing = brackets

        def get_lo(self):
            return 0

        def get_str(self):
            return "This is a test string."

    class DummyHyperParser:
        def __init__(self, text, index, bracketing):
            self.text = text


# Generated at 2022-06-14 11:43:43.287579
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    "test_RoughParser_get_base_indent_string()"
    # Test 1
    s = 'def f():\n    "for testing"\n    return "cheese"'
    r = RoughParser(s)
    assert r.get_base_indent_string() == '    '
    # Test 2
    s = 'def f():\n    "for testing"\n        return "cheese"'
    r = RoughParser(s)
    assert r.get_base_indent_string() == '        '
    # Test 2
    s = 'def f():\n    "for testing"\n        return "cheese"'
    r = RoughParser(s)
    assert r.get_base_indent_string() == '        '
    # Test 3

# Generated at 2022-06-14 11:43:49.426702
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def check(s, w):
        parser = RoughParser(s)
        result = parser.compute_bracket_indent()
        if result != w:
            raise ValueError("for |%s| expected %s but got %s" % (s, w, result))

    check("[", 1)
    check("[a,\n", 1)
    check("[a,\n    ", 5)
    check("[\n    a,\n", 5)
    check("[\n    a,\n    ", 9)
    check("[\n    a,\n    b", 10)
    # Don't increase indentation for dedent token
    check("[\n    a,\n    b\n]", 5)
    # Don't increase indentation for blank lines

# Generated at 2022-06-14 11:44:01.673886
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    def check(thismodule, index, text):
        parser = thismodule.HyperParser(text, index)
        assert text.get(index, parser.stopatindex) == parser.rawtext[parser.indexinrawtext :]
        assert parser.bracketing[parser.indexbracket][0] <= parser.indexinrawtext

    from unittest.mock import Mock

    text = Mock()
    text.indent_width = 8
    text.tabwidth = 4
    text.get.side_effect = lambda start, end: end[:-2]
    text.index.side_effect = lambda index: str(int(float(index))) + ".0"

    check(HyperParser, "1.0", text)
    check(HyperParser, "2.0", text)

# Generated at 2022-06-14 11:44:07.891495
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    # This tests a non-ASCII identifier.
    text = "a_\N{LATIN SMALL LETTER C WITH CEDILLA}=1"
    hp = HyperParser(text, text.index("_"))
    assert hp.is_in_code()

    text = text + '#'
    hp = HyperParser(text, text.index("_"))
    assert hp.is_in_code()

    text = text + '""""'
    hp = HyperParser(text, text.index("_"))
    assert not hp.is_in_code()

    text = text + 'a.b'
    hp = HyperParser(text, text.index("_"))
    assert hp.is_in_code()

    text = text + '""""'
    hp = HyperParser(text, text.index("_"))
