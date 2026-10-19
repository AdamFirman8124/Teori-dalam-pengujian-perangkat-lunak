

# Generated at 2022-06-14 11:38:23.405720
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def t(s, exp_s, index):
        parser = HyperParser(s, index)
        res = parser.get_expression()
        assert res == exp_s, "Case %r at index %r: returned %r, expected %r" % (
            s,
            index,
            res,
            exp_s,
        )

    # test the cases described in #1784
    t("if x == 10:\n    print(x)  ", "x", "2.6")
    t('if x == 10:\n    print(x)  ', 'x', "2.7")

    # Test error at beginning of string
    t("a", "", "1.0")
    t("a", "", "1.1")

    # Test whitespace
    t(" a ", "a", "1.1")


# Generated at 2022-06-14 11:38:31.720294
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    h = HyperParser("a=1 # string1\n'string2'", "1.9")
    assert h.is_in_string()
    h.set_index("1.12")
    assert h.is_in_string()
    h.set_index("1.2")
    assert not h.is_in_string()
    h.set_index("1.14")
    assert not h.is_in_string()
    h.set_index("1.17")
    assert not h.is_in_string()


# Generated at 2022-06-14 11:38:33.772300
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    rp = RoughParser()
    assert rp.set_lo


# Generated at 2022-06-14 11:38:45.807855
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:38:50.381797
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    cases = [
        ("a", True),
        ('a"', True),
        ('"a"', False),
        ("a '", True),
        ("'a'", False),
        ('#a', False),
        ('a#"', True),
        ('a#', True),
    ]

    for text, expected in cases:
        hp = HyperParser(text, "1.0")
        assert hpy(hp.is_in_code()) == expected, text


# Generated at 2022-06-14 11:38:58.630416
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # pylint: disable=redefined-builtin
    import doctest
    from lib2to3 import pgen2

    def ddd(s, expected, width=8, tabwidth=8):
        """Calls compute_backslash_indent on a whole suite of statements.

        s should have one or more complete statements, separated by ;'s.
        expected is a list of expected results.
        """
        strs = re.split(r";\s*", s)
        # Add a newline to the end of each substring, so the algorithm is
        # guaranteed to find str[-1] == "\n".
        strs = [s + "\n" for s in strs]
        # Accumulate results in a list.
        results = []

# Generated at 2022-06-14 11:39:04.414717
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():

    def get(init, index, expect):
        hp = HyperParser(Text(init, "1.0"), "1.0+%dc" % index)
        got = hp.get_expression()
        if got != expect:
            return (
                "Error: Init string: %s"
                " (index %d, raw=%s)"
                " gave expression %s when it should give %s."
                % (init, index, repr(hp.rawtext), repr(got), repr(expect))
            )
        return None


# Generated at 2022-06-14 11:39:16.989672
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    class MockEditWin:
        def __init__(self, text, index):
            self.text = text
            self.index = index

        def get(self, start, stop):
            startpos = int(float(start))
            stoppos = int(float(stop))
            return self.text[startpos:stoppos]

        def index(self, pos):
            pos = str(pos)
            if "." in pos:
                return pos
            else:
                return pos + ".0"

    def get_brackets(text, index):
        editwin = MockEditWin(text, index)
        hyperparser = HyperParser(editwin, index)
        return hyperparser.get_surrounding_brackets()


# Generated at 2022-06-14 11:39:29.490685
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    # Functions for testing get_expression
    def _assert_exp(code, expected_exp, index):
        parser = HyperParser(Text(code, 4), index)
        try:
            got_exp = parser.get_expression()
        except ValueError:
            got_exp = ""
        assert got_exp == expected_exp, (
            "get_expression doesn't work in %r, expected %r, got %r"
            % (code, expected_exp, got_exp)
        )

    def _assert_all_exps(code, expected_exps):
        for index, exp in zip(expected_exps[0], expected_exps[1]):
            _assert_exp(code, exp, index)

    # Pairs of simple expressions

# Generated at 2022-06-14 11:39:39.659411
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    import unittest
    from test.test_support import run_unittest
    from test import test_support

    class TestIsInString(unittest.TestCase):
        def __init__(self, testname, text, index, expected):
            unittest.TestCase.__init__(self, testname)
            self.text = text
            self.index = index
            self.expected = expected

        def shortDescription(self):
            return "Test HyperParser.is_in_string: " + self.expected

        def runTest(self):
            hp = HyperParser(self.text, self.index)
            if hp.is_in_string():
                actual = "in string"
            else:
                actual = "not in string"

# Generated at 2022-06-14 11:41:17.571542
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = Text()
    text.delete("1.0", "end")
    text.insert("1.0", "text = 'Hello world'[3:]")
    parser = HyperParser(text, "1.1")
    parser.set_index("1.0")
    assert parser.indexinrawtext == 12
    parser.set_index("1.1")
    assert parser.indexinrawtext == 11
    parser.set_index("1.12")
    assert parser.indexinrawtext == 0
    assert parser.indexbracket == 12


# Generated at 2022-06-14 11:41:22.610755
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    text = "foo('bar(')"
    hp = HyperParser(text, "2.0")
    assert hp.is_in_string(), "foo should not be in a string"
    hp = HyperParser(text, "3.0")
    assert hp.is_in_string(), "bar should be in a string"
    hp = HyperParser(text, "4.0")
    assert hp.is_in_string(), "bar should be in a string"
    hp = HyperParser(text, "5.0")
    assert not hp.is_in_string(), "r) should not be in a string"

    text = "foo( 'bar( ')"
    hp = HyperParser(text, "2.0")
    assert hp.is_in_string(), "foo should not be in a string"

# Generated at 2022-06-14 11:41:34.840120
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    rp = RoughParser("""
            foo(bar, (baz)(42),
                42
            )
            """, 0)
    i = rp.find_good_parse_start()
    assert i == 6

    rp = RoughParser("""
            foo(bar, (baz)(42),
                # comment
                42
            )
            """, 0)
    i = rp.find_good_parse_start()
    assert i == 6

    rp = RoughParser("""
            foo(bar, (baz)(42),
                # comment
                )
            """, 0)
    i = rp.find_good_parse_start()
    assert i == 6


# Generated at 2022-06-14 11:41:50.978234
# Unit test for constructor of class HyperParser
def test_HyperParser():
    from unittest import TestCase
    from unittest.mock import Mock

    class HyperParserTestCase(TestCase):
        def test_HyperParser_basic_use(self):
            self.assertEqual(h.is_in_string(), False)
            self.assertEqual(h.is_in_code(), True)

            self.assertEqual(h.get_expression(), "f")
            h.set_index("insert")
            self.assertEqual(h.get_expression(), "a")

        def test_HyperParser_bracket(self):
            self.assertEqual(h.get_surrounding_brackets(), ("1.0", "1.8"))
            self.assertEqual(h.get_surrounding_brackets(mustclose=True), None)
            h.set_index

# Generated at 2022-06-14 11:42:02.109913
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # pylint: disable=redefined-builtin,too-many-branches,too-many-statements

    for s in ["  \\\n  ", "  \\\t\n  ", "  \\\n\\\t\\\n  "]:
        assert RoughParser(s, 0).compute_backslash_indent() == 2

    for s in ["  \\\n  x", "  \\\t\n  x", "  \\\n\\\t\\\n  x"]:
        assert RoughParser(s, 0).compute_backslash_indent() == 3

    for s in ["  \\\n  x = 1", "  \\\t\n  x = 1", "  \\\n\\\t\\\n  x = 1"]:
        assert RoughParser(s, 0).comp

# Generated at 2022-06-14 11:42:10.005836
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    # These tests all assume Tk 4.2 dependent behavior, so only run
    # them if we have Tk 4.2.
    if hasattr(tkinter, "TkVersion") and tkinter.TkVersion < 4.2:
        return

    # Create a Text widget.
    root = tkinter.Tk()
    text = tkinter.Text(root)

    # Construct a HyperParser using the Text widget.
    text.insert("1.0", "a[b, c, d]")
    hp = HyperParser(text, "1.3")

    # Make sure we get the correct surrounding brackets.

# Generated at 2022-06-14 11:42:22.374856
# Unit test for method is_in_string of class HyperParser

# Generated at 2022-06-14 11:42:27.474046
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # pylint: disable=redefined-outer-name
    # pylint: disable=missing-docstring
    def verify_indent(s, expected):
        rp = RoughParser(s, bpc=0)
        assert rp.compute_backslash_indent() == expected

    verify_indent("""kk = 1
\\
""", 3)
    verify_indent("""kk = 1 \\
""", 3)
    verify_indent("""kk = 1 \\
""", 3)
    verify_indent("""kk = 1 \\\\
""", 3)
    verify_indent("""kk = 1 \\
   \\
""", 3)
    verify_indent("""kk = 1\\
   \\
""", 3)

# Generated at 2022-06-14 11:42:38.298268
# Unit test for constructor of class HyperParser
def test_HyperParser():
    text = Text()
    text.insert("insert", "a = 12 +\n  (34 +\n56)")
    pos = text.index("insert")
    hp = HyperParser(text, pos)
    print(hp.rawtext, repr(hp.bracketing), repr(hp.isopener), file=sys.__stderr__)
    for i in range(len(hp.rawtext)):
        print(repr(hp.rawtext[i]), file=sys.__stderr__)
        hp.set_index(text.index(repr(i) + ".0"))
        print(repr(hp.bracketing[hp.indexbracket]), file=sys.__stderr__)
    print(hp.get_expression(), file=sys.__stderr__)



# Generated at 2022-06-14 11:42:44.020206
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    # This test is currently implemented as a function instead of
    # a unittest test case to avoid depending on unittest.
    # TODO: Move to unittest and make sure it gets executed.

    class MockText:

        def __init__(self, rawtext, indent_width, tabwidth):
            self._rawtext = rawtext
            self.indent_width = indent_width
            self.tabwidth = tabwidth

        def get(self, start, stop):
            i_start = int(float(start))
            i_stop = int(float(stop))
            return self._rawtext[i_start:i_stop]

        def index(self, string):
            return repr(int(float(string))) + ".0"
