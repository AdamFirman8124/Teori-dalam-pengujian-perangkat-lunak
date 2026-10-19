

# Generated at 2022-06-14 11:40:21.142822
# Unit test for constructor of class HyperParser
def test_HyperParser():
    # Create a text box with sample program.
    from unittest.mock import Mock
    from idlelib.idle_test.mock_idle import Func

    root = Tk()
    text = Text(root)
    text.insert("insert", test_program)
    text.pack()

    # Now, walk through the indexes and check the results of HyperParser.
    for index in ("1.0", "1.7", "1.8", "1.9", "1.10", "1.11", "1.12", "3.0", "3.3", "3.5"):
        parser = HyperParser(text, index)

        # Get the surrounding brackets and print them.
        brackets = parser.get_surrounding_brackets()
        if brackets:
            start, end = brackets

# Generated at 2022-06-14 11:40:30.207787
# Unit test for method is_in_code of class HyperParser

# Generated at 2022-06-14 11:40:35.019384
# Unit test for constructor of class HyperParser
def test_HyperParser():
    # Some tests are specific to the width of 8, but most should pass with any width.
    # We may wish to add some tests for width != 8
    assert len(_build_char_in_string_func("1.0")) == 8
    from unittest import TestCase
    txt = TestCase()
    txt.text = TextWrapper("", width=8)
    txt.indent_width = 8
    txt.tabwidth = 8

# Generated at 2022-06-14 11:40:46.073392
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    py3 = sys.version_info >= (3,)
    def f(line, col, result):
        hp = HyperParser(str(Text(string=line)), str(col + "." + str(col)))
        r = hp.get_expression()
        if r != result:
            print("\nhp.get_expression() = %r, should be %r." % (r, result))
            print("Line: %r" % line)
            print("Col: %r" % col)
            print("hp.indexinrawtext: %r" % hp.indexinrawtext)
            for b in hp.bracketing:
                print("bracketing: %r" % (b,))
            print("hp.rawtext: %r" % hp.rawtext)

# Generated at 2022-06-14 11:41:00.085710
# Unit test for method get_expression of class HyperParser

# Generated at 2022-06-14 11:41:05.756553
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    # Unit test for method get_base_indent_string of class RoughParser
    print("Testing method get_base_indent_string of class RoughParser...")
    rough_parser = RoughParser(
        "  a = 2\n" "        # comment !\n" "  b = 3\n",
        0,
        None
    )
    a = rough_parser.get_base_indent_string()
    b = "  "
    if a == b:
        print("Ok.")
    else:
        print("Failed.")

# Generated at 2022-06-14 11:41:09.760981
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    text = Text()
    text.insert("1.0", "a.b.c")
    hp = HyperParser(text, "2.0")
    assert hp.get_expression() == "a.b"
# end.



# Generated at 2022-06-14 11:41:19.806660
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    # This tests that set_index raises ValueError if called with an
    # index which is not in the same statement, and that it doesn't
    # raise it otherwise. Note that this test is only useful if
    # the statement is simple enough to parse in one go.

    # We use a leading space to test that this doesn't affect the
    # result.

    # The text is divided into 2 statements by a line
    # continuation backslash
    cases = (
        "a.b",
        "a.b\\\nc.d",
        "a.b\nc.d",
        "a()",
        "a()\\\nc()",
        "a()\nc()",
    )

    for text in cases:
        hp = HyperParser(text, "1.0")

# Generated at 2022-06-14 11:41:32.820984
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    print("testing HyperParser.get_expression")

    def test_expression(text, index, expected):
        index = text.index(index)
        hp = HyperParser(text, index)
        if expected != hp.get_expression():
            print("failed:", text.get("1.0", "end"), "index:", index)
            print("returned:", hp.get_expression())
            print("expected:", expected)
            raise RuntimeError

    # Note: get_expression is not guaranteed to return a meaningful
    # result if the index is inside a comment or a string.

    # Testing in comments
    test_expression(tk.Text(None, width=80, height=20), "1.1", "")
    test_expression(tk.Text(None, width=80, height=20), "1.10", "")


# Generated at 2022-06-14 11:41:39.839991
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    def check_compute(code, tabwidth, expected):
        parser = RoughParser(code, tabwidth)
        actual = parser.compute_backslash_indent()
        msg = "\nfor code:\n%r\nexpected: %r\nbut got: %r" % (
            code,
            expected,
            actual,
        )
        assert actual == expected, msg

    # The next test data are from the original.  The comment before
    # each data tuple is the test name.

# Generated at 2022-06-14 11:42:32.559057
# Unit test for method compute_backslash_indent of class RoughParser

# Generated at 2022-06-14 11:42:41.709860
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():

    # See also Lib/test/test_tokenize.py for a more exhaustive set of tests.
    def f(source, expected_start, **kwds):
        parser = RoughParser(source, **kwds)
        result = parser.find_good_parse_start()
        if result != expected_start:
            raise AssertionError(
                "Test failed on input %s.\n" % (repr(source),)
                + "Expected start %d, got %d." % (
                    expected_start,
                    result,
                )
                + "Part of text in question:\n---\n"
                + source[max(0, result - 20) : result + 20]
                + "\n---\n"
            )

    f("", 0)
    f("# a comment\n", 0)

# Generated at 2022-06-14 11:42:53.091026
# Unit test for constructor of class HyperParser
def test_HyperParser():
    text = Text()
    text.insert("insert", "a + b\n")
    # try before start
    text.mark_set("insert", "1.0-1c")
    try:
        HyperParser(text, "insert")
    except ValueError:
        pass
    else:
        print("Should raise ValueError if index precedes analyzed statement")
    # try inside statement
    text.mark_set("insert", "1.1")
    parser = HyperParser(text, "insert")
    if parser.rawtext != "a + b":
        print("rawtext should be 'a + b'")
    if parser.stopatindex != "2.0":
        print("stopatindex should be 2.0")
    if not parser.is_in_code():
        print("parser should be in code")

# Generated at 2022-06-14 11:43:09.280983
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    class Mock_Text(object):
        def __init__(self, text):
            self.text = text

        def get(self, start, finish):
            return self.text[int(start) : int(finish)]

        def index(self, index):
            # We assume that index is an integer
            return index

    def test(text, index, expected):
        hp = HyperParser(Mock_Text(text), index)
        assert hp.text.text == text
        hp.set_index(index)
        assert hp.indexinrawtext == expected

    def test_fail(text, index):
        with pytest.raises(ValueError):
            hp = HyperParser(Mock_Text(text), index)
            hp.set_index(index)

    text = "# First line\n# Second line\n"

# Generated at 2022-06-14 11:43:17.415768
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    class ParserTester:
        def __init__(self, rawtext):
            self.rawtext = rawtext
        def index(self, index):
            return index
    def run(rawtext, index, res):
        p = HyperParser(ParserTester(rawtext), index)
        if p.is_in_code() == res:
            print('.', end=" ")
            return True
        print('F', end=" ")
        print(rawtext, index, "->", p.is_in_code(), "should be", res)
    run("",  "1.0", False)
    run(" ", "1.0", False)
    run("#", "1.0", False)
    run("#foo", "1.0", False)
    run("#foo", "1.1", False)

# Generated at 2022-06-14 11:43:28.129580
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    """Test HyperParser.get_expression for a few cases.
    """

    def get_expression(text, index, expected_expression):
        """Test and return result of HyperParser.get_expression.
        """
        if "|" in text:
            # The | in the text is the cursor position.
            text, expected_expression = text.split("|")
            index = "%d.%d" % (1 + text.count("\n"), len(text) - text.rfind("\n"))
        if "..." in expected_expression:
            expected_expression = expected_expression.replace("...", "") + text[index:]
        h = HyperParser(text, index)
        try:
            result = h.get_expression()
        except ValueError:
            result = None
        expected_result = expected_expression or None


# Generated at 2022-06-14 11:43:42.461379
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    class MockText:

        def __init__(self, text):
            self.text = text
            self.indent_width = 8
            self.tabwidth = 8

        def get(self, start, stop):
            return self.text[int(float(start)):int(float(stop))]

        def index(self, index):
            return int(float(index))

    def check(text, index, expected):
        hyper_parser = HyperParser(MockText(text), index)
        assert expected == hyper_parser.is_in_string(), "%s != %s" % (expected, hyper_parser.is_in_string())

    # Single quoted strings
    check("'abc'", "2.0", True)
    check("'abc'", "1.0", True)

# Generated at 2022-06-14 11:43:49.260766
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    tk = Tk()
    t = Text(tk)
    t.pack()
    # Insert a multiline code starting at line 1.
    t.insert(END, """\
print(1)  # This is a comment
print(2)  # Another comment
print(3)  # Yet another comment
# Now more code
print(4)
""")

    # Return true if hp.get_surrounding_brackets() is not None
    def check_code(cursor):
        hp = HyperParser(t, cursor)
        return hp.is_in_code()

    assert check_code("1.6")
    assert check_code("1.8")
    assert check_code("1.10")
    assert check_code("1.14")
    assert check_code("1.16")
    assert check

# Generated at 2022-06-14 11:44:01.604535
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    class M:
        def __init__(self, text):
            self.text = text

        def get(self, start, end):
            return self.text[int(start.split(".")[0]):int(end.split(".")[0])]

        def index(self, s):
            return str(s)


# Generated at 2022-06-14 11:44:14.172270
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    h = HyperParser("while (1):\n    for x in range(10):\n        pass", "insert")
    assert h.get_surrounding_brackets("(") == ("2.10", "2.14")
    assert h.get_surrounding_brackets("([{", True) == ("2.10", "2.14")
    assert h.get_surrounding_brackets("([{", False) == ("1.6", "1.10")
    h.set_index("1.10")
    assert h.get_surrounding_brackets("([{", True) is None
    assert h.get_surrounding_brackets("([{", False) == ("1.6", "1.10")
    h.set_index("2.11")
    assert h.get_surround

# Generated at 2022-06-14 11:45:51.063008
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    assert HyperParser('a.b.c.d', 'insert').get_expression() == 'a.b.c.d'
    assert HyperParser('spam(1).b.c.d', 'insert').get_expression() == 'spam(1).b.c.d'
    assert HyperParser('spam(1+2).c.d', 'insert').get_expression() == 'spam(1+2).c.d'
    assert HyperParser('spam(1+\n2).c.d', 'insert').get_expression() == 'spam(1+\n2).c.d'
    assert HyperParser('spam(1,\n2).c.d', 'insert').get_expression() == 'spam(1,\n2).c.d'

# Generated at 2022-06-14 11:45:57.501836
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from unittest import TestCase
    from idlelib import parenmatch

    class TestableHyperParser(parenmatch.HyperParser):
        # For testing, overwrite the original text.
        def __init__(self, text, index, new_text=None):
            self._orig_text = text
            self.text = new_text or text
            parenmatch.HyperParser.__init__(self, text, index)

        # When overwriting the original text, also overwrite the
        # original index.
        def set_index(self, new_index):
            self.index = new_index
            parenmatch.HyperParser.set_index(self, new_index)

        def get_dict_contents(self):
            return self.__dict__.copy()

    # Test data

# Generated at 2022-06-14 11:46:11.945884
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    from unittest.mock import Mock

    text = Mock()
    text.get = lambda x, y: "abcd"
    text.index = lambda x: 0

    parser = HyperParser(text, 0)

    # Test that a parser can be constructed.
    assert parser

    parser.set_index(0)
    assert not parser.is_in_string()
    parser.set_index(1)
    assert not parser.is_in_string()
    parser.set_index(2)
    assert not parser.is_in_string()
    parser.set_index(3)
    assert not parser.is_in_string()

    parser = HyperParser(text, 0)
    text.get = lambda x, y: '"abcd"'
    parser.set_index(0)
    assert parser.is_

# Generated at 2022-06-14 11:46:23.697061
# Unit test for method get_expression of class HyperParser

# Generated at 2022-06-14 11:46:31.564273
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def testfunc(teststring, index, expected_result):
        try:
            i = teststring.index(index)
        except ValueError:
            i = len(teststring) - len(index)
        hp = HyperParser(teststring, index)
        expr = hp.get_expression()
        if expr != expected_result:
            raise AssertionError(
                "HyperParser.get_expression failed on %r.\n"
                "Index is %r.\n"
                "Expected result: %r, got %r" % (teststring, index, expected_result, expr)
            )

    testfunc("a = [1, 2, 3]", "%d.end" % 1, "a")

# Generated at 2022-06-14 11:46:46.768660
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    # This should not open a new window
    root = Tk()
    root.withdraw()
    text = Text(root)
    text.insert("insert", "foo(a,b)")
    text.mark_set("insert", "1.1")
    assert HyperParser(text, "insert").is_in_string() == 0
    text.mark_set("insert", "1.2")
    assert HyperParser(text, "insert").is_in_string() == 0
    text.mark_set("insert", "1.3")
    assert HyperParser(text, "insert").is_in_string() == 0
    text.mark_set("insert", "1.4")
    assert HyperParser(text, "insert").is_in_string() == 0
    text.mark_set("insert", "1.5")


# Generated at 2022-06-14 11:46:48.759808
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    rp = RoughParser()

# Generated at 2022-06-14 11:47:00.456339
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    text = Text()
    text.end = 1.0
    text.insert("insert", "b)c")
    hyper = HyperParser(text, "1.0")
    assert hyper.get_surrounding_brackets() == ("1.0", "1.3"), hyper.get_surrounding_brackets()
    text.insert("insert", "d")
    text.insert("insert", "a(b")
    hyper = HyperParser(text, "1.5")
    assert hyper.get_surrounding_brackets() == ("1.4", "1.6"), hyper.get_surrounding_brackets()
    text.insert("insert", '"c"')
    hyper = HyperParser(text, "1.5")

# Generated at 2022-06-14 11:47:05.099128
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    test_cases = [
        "/* */ '/*' /* */",
        "a",
    ]

    for test in test_cases:
        hyper_parser = HyperParser(test, 2)
        text = hyper_parser.get_surrounding_brackets()



# Generated at 2022-06-14 11:47:17.567319
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = Text(None, "1.0", "end")

    text.insert('1.0', '"a" if b\n  # comment\n')
    h = HyperParser(text, '1.0')

    # Test index at the beginning of the string
    h.index = '2.0'
    h.set_index('1.0')
    assert h.indexbracket == 1
    assert h.indexinrawtext == 0

    # Test index at the end of the string
    h.index = '2.0'
    h.set_index('1.end')
    assert h.indexbracket == 1
    assert h.indexinrawtext == 3

    # Test index at the beginning of the statement
    h.index = '2.0'
    h.set_index('1.1')
   