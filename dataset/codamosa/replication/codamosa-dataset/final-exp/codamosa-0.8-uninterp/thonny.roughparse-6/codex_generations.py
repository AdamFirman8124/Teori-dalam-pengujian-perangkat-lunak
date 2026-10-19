

# Generated at 2022-06-14 11:38:49.931621
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    # Test with a sample file which is the same for Python 2 and 3
    sample = load_sample_file("sample2.py")

    # Test first line
    hyper = HyperParser(sample, "1.0")
    assert hyper.is_in_string() == False

    hyper = HyperParser(sample, "1.8")
    assert hyper.is_in_string() == True

    hyper = HyperParser(sample, "1.10")
    assert hyper.is_in_string() == True

    hyper = HyperParser(sample, "1.13")
    assert hyper.is_in_string() == False

    # Test second line
    hyper = HyperParser(sample, "2.0")
    assert hyper.is_in_string() == True

    hyper = HyperParser(sample, "2.5")
    assert hyper.is_

# Generated at 2022-06-14 11:38:58.116209
# Unit test for constructor of class HyperParser
def test_HyperParser():
    sample = """
    # -*- coding: isocode -*-

    # This is a comment
    a = "a"
    b = 'b'
    (a, b) = (1,
    2)
    c = [3, 4]
    """

    def test(index, expectedindexinrawtext, expectedindexbracket, expectedisopener):
        h = HyperParser(Text(sample), index)
        assert h.indexinrawtext == expectedindexinrawtext
        assert h.indexbracket == expectedindexbracket
        assert h.isopener == expectedisopener

    test("1.0", 0, 0, [])
    test("2.0", 0, 0, [])
    test("3.0", 0, 0, [])
    test("4.0", 0, 0, [])

# Generated at 2022-06-14 11:39:05.970793
# Unit test for method get of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping_get():
    """
    Test for method get of class StringTranslatePseudoMapping
    """
    if not hasattr(StringTranslatePseudoMapping, "get"):
        raise AttributeError
    # test 1:
    # map all characters except whitespace to 'x'
    # replace all whitespace with ' '
    # check whether the result is as expected
    whitespace_chars = " \t\n\r"
    preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
    text = "a + b\tc\nd"
    actual_result = text.translate(mapping)
    expected_result = "x x x\tx\nx"

# Generated at 2022-06-14 11:39:18.184902
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    l = []

# Generated at 2022-06-14 11:39:29.547299
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    def check(text, index, openers, mustclose, result):
        """Run get_surrounding_brackets for the given text, index and
        openers, then check that the result is as expected.

        The result is given as a tuple of result[0] which is True or
        False according to whether the check passed, and result[1] is
        the error message.
        """

        from idlelib.pyshell import PseudoFile

        hp = HyperParser(text, index)
        result = hp.get_surrounding_brackets(openers, mustclose)
        if result == expected:
            return True, ""

# Generated at 2022-06-14 11:39:39.688876
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    # The test uses this function, but it is not used otherwise.
    def test_expression(text, index, expected_res):
        """ Check that get_expression returns the expected result
        with the given text and index. """
        hp = HyperParser(text, index)
        res = hp.get_expression()
        if res != expected_res:
            # Report error
            raise ValueError(
                "Failed test.\n"
                "Expected result: %s\n"
                "Obtained result: %s\n"
                "for index %d in text: %s" % (expected_res, res, index, text)
            )

    # This is the array of tests. Each test is a triple of:
    #   - test description
    #     (a string that will be used to describe the test
    #     in

# Generated at 2022-06-14 11:39:52.129353
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():

    def check(s, expected_start, expected_goodlines):
        # pylint: disable=redefined-builtin
        rp = RoughParser(s, None)
        start, goodlines = rp.find_good_parse_start()
        assert expected_start == start, (
            "expected start %r, got %r" % (expected_start, start)
        )
        assert expected_goodlines == goodlines, (
            "expected goodlines %r, got %r" % (expected_goodlines, goodlines)
        )

    yield check, "", 0, [0]
    yield check, " ", 1, [1]
    yield check, " \n", 2, [1, 2]
    yield check, "\n ", 2, [1, 2]
    yield check, "foo", 0, [0]


# Generated at 2022-06-14 11:39:58.116506
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    from idlelib.idle_test.htest import run

    run(None, test_HyperParser_get_expression, "HyperParser_get_expression")

    # returns a string with the Python import statement that ends at
    # index, which is empty if there is no real one

    def get_import_statement(hp):
        rawtext = hp.rawtext
        bracketing = hp.bracketing
        brck_index = hp.indexbracket
        brck_limit = bracketing[brck_index][0]
        pos = hp.indexinrawtext

        # include from and import from the import statement
        from_index = min(brck_limit + 1, pos - len("from "))
        import_index = min(brck_limit + 1, pos - len("import "))

# Generated at 2022-06-14 11:40:05.512239
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    with pytest.raises(AssertionError):
        p = RoughParser("", 0)
        p.compute_backslash_indent()

    p = RoughParser("if a:\\\n    print b\n", 0)
    assert p.compute_backslash_indent() == 4

    p = RoughParser("if a:\\\n    print b\\\n    print c\n", 0)
    assert p.compute_backslash_indent() == 4


# Generated at 2022-06-14 11:40:11.208307
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    # We test with this string
    text = """
    text[:1+1:1][:]
"""
    h = HyperParser(text, "5.5")
    h.set_index("5.5")
    h.set_index("5.4")
    h.set_index("5.3")
    h.set_index("5.2")
    h.set_index("5.1")
    h.set_index("5.0")
    try:
        h.set_index("4.0")
        raise RuntimeError("Bad index should have been detected.")
    except:
        pass


# Generated at 2022-06-14 11:41:03.954468
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    """Unit test for HyperParser.set_index."""

    text = Tkinter.Text()
    text.insert("insert", " \n\t ( ) [[]")
    hp = HyperParser(text, "2.0")
    try:
        hp.set_index("1.0")
        assert 0
    except ValueError:
        pass
    else:
        assert 0
    if hp.is_in_string():
        assert 0
    if not hp.is_in_code():
        assert 0
    if hp.get_surrounding_brackets("([") != ("2.0", "2.4"):
        assert 0
    if hp.get_surrounding_brackets("([", True) is not None:
        assert 0
    if hp.get_expression() != "":
        assert 0

   

# Generated at 2022-06-14 11:41:10.007689
# Unit test for method get of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping_get():
    mapping = StringTranslatePseudoMapping({ord('a'): ord('x')}, ord('z'))
    assert mapping.get(ord('a')) == ord('x')
    assert mapping.get(ord('c')) == ord('z')
test_StringTranslatePseudoMapping_get()

# Generated at 2022-06-14 11:41:19.907873
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    """Unit test for method get_surrounding_brackets of class HyperParser"""


# Generated at 2022-06-14 11:41:23.606222
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    r = RoughParser("""foo = '''\
    bar
    '''""")
    assert r.compute_backslash_indent() == 4


# Generated at 2022-06-14 11:41:24.809191
# Unit test for method is_in_code of class HyperParser

# Generated at 2022-06-14 11:41:33.878215
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    import unittest
    import test.test_support

    class HyperParserTestCase(unittest.TestCase):
        def setUp(self):
            self.hp = HyperParser(self.text, self.index)

        def test_is_in_code(self):
            self.hp._is_in_code()

    class IsInCode(HyperParserTestCase):
        """Test is_in_code on methods, classes and functions."""

        def setUp(self):
            self.text = text = Text()

# Generated at 2022-06-14 11:41:40.325267
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    # pylint: disable=redefined-builtin
    # pylint: disable=eval-used
    # pylint: disable=invalid-name

    def test(str, indent_width, tab_width, expected):
        rp = RoughParser(str, indent_width, tab_width)
        result = rp.compute_bracket_indent()
        assert result == expected, "%r != %r for\n%r" % (result, expected, str)


# Generated at 2022-06-14 11:41:41.731723
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    import unittest


# Generated at 2022-06-14 11:41:54.692275
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    h = HyperParser(tkinter.Text(), "1.0")

    h.text = tkinter.Text()
    h.text.insert("1.0", "foo(a, (b, c))\n")
    h.rawtext = "foo(a, (b, c))\\n"

# Generated at 2022-06-14 11:42:05.297673
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    from unittest import TestCase, main

    class Test(TestCase):
        def check_brackets(self, s, index, bopen, cbopen, bclose, cbclose):
            text = Text(s, "utf-8")
            hp = HyperParser(text, index)
            res = hp.get_surrounding_brackets(bopen, cbopen)
            if bclose is None:
                self.assertIsNone(res, "Problem in: %s" % s)
            else:
                self.assertEqual(res, (bclose, cbclose), "Problem in: %s" % s)


# Generated at 2022-06-14 11:43:15.983174
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    # Create a Text for testing
    text = tkinter.Text()
    text.insert("insert", """\
if blah:
    blah(#|
if blah:
    blah(blah,
        #|
if blah:
    blah(blah,
        blah,
            #|
if blah:
    blah(blah,
        blah,
            blah)
                #|
if blah:
    blah('|#
if blah:
    blah("|#
""")
    text.tag_add("sel", "1.19", "1.22")
    text.tag_add("sel", "2.21", "2.24")
    text.tag_add("sel", "3.30", "3.33")
    text.tag_add("sel", "4.46", "4.49")
   

# Generated at 2022-06-14 11:43:27.322536
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = Text()
    text.insert("1.0", 'if 1:\n\tpass\n\tpass')
    parser = HyperParser(text, "1.2")
    if parser.rawtext != "if 1:\n\tpass\n\tpass\n ":
        print("test_HyperParser_set_index failed with rawtext=%r" % parser.rawtext)
    else:
        parser.set_index("1.3")
        if parser.rawtext != 'if 1:\n\tpass\n\tpass\n ':
            print("test_HyperParser_set_index failed with rawtext=%r" % parser.rawtext)
        else:
            parser.set_index("1.7")

# Generated at 2022-06-14 11:43:36.220185
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    text = """
    a = (i *
         i for i in range(10))
    foo(x, y(
        z))
    """

# Generated at 2022-06-14 11:43:45.274907
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    T = Text()
    p = HyperParser(T, "1.0")
    p.set_index("1.0")
    assert p.indexinrawtext == 0
    assert p.indexbracket == 0
    p.set_index("1.3")
    assert p.indexinrawtext == 3
    assert p.indexbracket == 0
    p.set_index("2.0")
    assert p.indexinrawtext == 4
    assert p.indexbracket == 1
    p.set_index("2.1")
    assert p.indexinrawtext == 5
    assert p.indexbracket == 1

# Generated at 2022-06-14 11:43:58.918775
# Unit test for constructor of class HyperParser
def test_HyperParser():
    import unittest

    text = Text()
    text.insert("1.0", "def frq(x, y=-1, *args):  # frq comment\n    a = []")
    text.insert("2.0", "    b = {}\n    c = 12\n    x = '''")
    text.insert("3.0", "    '''")
    text.insert("4.0", "\n    '''")

    class HyperParserTest(unittest.TestCase):
        def test_1(self):
            parser = HyperParser(text, "1.0")
            self.assertEqual(parser.get_expression(), "")
            self.assertEqual(parser.get_surrounding_brackets(), None)


# Generated at 2022-06-14 11:44:05.431097
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    from test import test_support

    # Note the complete test case is done in Lib/idlelib/run.py.
    str_ = "def foo(x):  # comment\n    print(x)"
    parser = RoughParser(str_)
    start = parser.find_good_parse_start()
    assert start == 0 or start == (len(str_) - 1)

    parser = RoughParser("{\n{\n{\n}\n}\n}\n")
    assert parser.find_good_parse_start() == len(parser.str) - 1

    parser = RoughParser("\n\n")
    assert parser.find_good_parse_start() == len(parser.str) - 1

# Generated at 2022-06-14 11:44:16.454689
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    rp = RoughParser("")
    # assert rp.find_good_parse_start(0) == 0
    assert rp.find_good_parse_start(1) == 0
    rp = RoughParser("1")
    assert rp.find_good_parse_start(0) == 0
    assert rp.find_good_parse_start(1) == 1
    rp = RoughParser("1\n")
    assert rp.find_good_parse_start(0) == 0
    assert rp.find_good_parse_start(1) == 1
    assert rp.find_good_parse_start(2) == 1
    rp = RoughParser("1\n\n")
    assert rp.find_good_parse_start(0) == 0
    assert rp.find_good_

# Generated at 2022-06-14 11:44:23.821565
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():

    def helper(s, b, tabwidth, expected):
        assert RoughParser(s, tabwidth).compute_bracket_indent() == expected

    helper('  # comment\n  x = {1: 2}\n', False, 8, 2)
    helper('x = {\n    1: 2\n}\n', False, 8, 4)
    helper('x = {\n    (1, 2)\n}\n', False, 8, 4)
    helper('x = {(1,\n          2)\n}\n', False, 8, 10)
    helper('x = {\n    1: 2\n', False, 8, 4)
    helper('x = {\n    [1, 2]\n}\n', False, 8, 4)

# Generated at 2022-06-14 11:44:34.299260
# Unit test for constructor of class HyperParser
def test_HyperParser():
    text = EditorWindow(None)
    text.insert("insert", "def f(a, b):\n" "  a = b = 5\n" "  if a == b: print(a)\n")
    text.update()

    hp = HyperParser(text, "1.18")
    assert hp.is_in_code()
    assert not hp.is_in_string()
    assert hp.get_expression() == "b"
    assert hp.get_surrounding_brackets("()[]", False) == ("1.15", "1.20")

    hp.set_index("1.20")
    assert hp.is_in_code()
    assert not hp.is_in_string()
    assert hp.get_expression() == "a"

# Generated at 2022-06-14 11:44:47.046060
# Unit test for constructor of class HyperParser
def test_HyperParser():
    import unittest

    text = idlelib.textView.TextView()  # editingwindow.EditorWindow().text
    text.insert("end", "a = 1")
    text.mark_set("insert", "2.0")
    parser = HyperParser(text, "insert")
    text.insert("insert", "(")
    parser.set_index("insert")

    # If the following test fails, it is likely because of a tabs
    # problem.
    s = "a = 1 (\n"
    # parser.set_index must be called before parser.rawtext is used
    assert parser.rawtext == s, parser.rawtext
    assert parser.is_in_code(), "Should be in code"
    assert not parser.is_in_string(), "Should not be in string"
    paren_index = parser.get_