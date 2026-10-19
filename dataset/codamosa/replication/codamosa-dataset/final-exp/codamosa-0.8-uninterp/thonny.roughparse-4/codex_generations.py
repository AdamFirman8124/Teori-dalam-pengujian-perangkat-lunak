

# Generated at 2022-06-14 11:37:35.258411
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    from unittest.mock import MagicMock

    class MockText:
        def __init__(self):
            self.indent_width = self.tabwidth = 8

        def get(self, index1, index2):
            index1 = int(index1[: index1.index(".")]) - 1
            index2 = int(index2[: index2.index(".")]) - 1
            return self.lines[index1:index2]

        def index(self, index):
            index = int(index[: index.index(".")])
            return repr(index) + ".0"

        def mark_set(self, name, index):
            self.mark_set_index = index

    def test(lines, expected_result):
        text = MockText()
        text.lines = lines

# Generated at 2022-06-14 11:37:39.362093
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    code = dedent(
        """\
        v = 5
        \tdef f():
            pass
        """)
    blocks = RoughParser(code, 0).parse()
    assert blocks[0].indent == '\t'


# Generated at 2022-06-14 11:37:52.149931
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    def check(text, index):
        return HyperParser(text, index).is_in_code()


# Generated at 2022-06-14 11:37:57.923253
# Unit test for method get_last_stmt_bracketing of class RoughParser
def test_RoughParser_get_last_stmt_bracketing():
    def test(test_data):
        stmt, bracketing = test_data
        parser = RoughParser(stmt)
        parser_bracketing = parser.get_last_stmt_bracketing()

        if bracketing is None:
            assert parser_bracketing is None
        else:
            assert len(bracketing) == len(parser_bracketing)
            for b1, b2 in zip(bracketing, parser_bracketing):
                assert b1[0] == b2[0]
                assert b1[1] == b2[1]
    yields = ("yield", "yield 1", "yield x = y = 1")

# Generated at 2022-06-14 11:38:06.053458
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    """Method compute_bracket_indent should work for a variety of cases.
    This test case is really for the method study2.
    """
    for (
        statement,
        continuation,
        indent_width,
        tabwidth,
        expected,
    ) in compute_bracket_indent_tests:
        parser = RoughParser(statement, indent_width, tabwidth)
        assert continuation == parser.get_continuation_type()
        got = parser.compute_bracket_indent()
        assert got == expected, (
            'compute_bracket_indent() returned %r, expected %r for\n"""\n%s"""'
            % (got, expected, statement)
        )


# Generated at 2022-06-14 11:38:12.570646
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    hp = HyperParser(tkinter.Text(), "1.0")
    # Test that an error is raised if the index is before the analyzed
    # statement.
    try:
        hp.set_index("0.0")
    except ValueError:
        pass
    else:
        raise AssertionError

    # Test that an error is not raised if the index is in the analyzed
    # statement
    hp.set_index("1.0")

    # Test that an error is not raised if the index is after the
    # analyzed statement, but in a statement that would be analyzed too.
    hp.set_index("2.0 lineend")

    # Test that an error is raised if the index is after the analyzed
    # statement, but in a statement that would not be analyzed.

# Generated at 2022-06-14 11:38:15.853240
# Unit test for method is_block_closer of class RoughParser
def test_RoughParser_is_block_closer():
    rp = RoughParser("if True:\n pass\n\n")
    assert rp.is_block_opener() == True
    rp = RoughParser("if True:\n pass\n")
    assert rp.is_block_opener() == False
    
    rp = RoughParser("if True:\n pass\n")
    assert rp.is_block_closer() == True
    rp = RoughParser("if True:\n pass\n\n")
    assert rp.is_block_closer() == False
# unit test for RoughParser

# Generated at 2022-06-14 11:38:23.405508
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    import unittest
    import re

    class TestCase(unittest.TestCase):
        def test_get_surrounding_brackets(self):
            def test(text, pos, expected):
                """Test that get_surrounding_brackets returns expected
                when called on the given text and pos.

                If expected is None, that means that the function should
                raise an exception.
                """
                self.visited = False
                try:
                    parser = HyperParser(text, pos)
                    result = parser.get_surrounding_brackets()
                except:
                    self.assertIsNone(expected, "Unexpected exception")
                else:
                    if expected is None:
                        self.fail("Expected exception")
                    self.assertEqual(result, expected)
                self.visited = True

            # Visit

# Generated at 2022-06-14 11:38:33.314241
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    """Unit test for method HyperParser.is_in_string"""
    # NOTE: The order of the tests is important.
    # String in triple quote
    assert(
        _test_HyperParser("'''abc'''", False) == (9, False)
    ), "Triple quoted string beginning in line"
    assert(
        _test_HyperParser("'''abc'''xyz", False) == (9, False)
    ), "Triple quoted string ending in line"
    assert(
        _test_HyperParser("'''abc'''xyz'''", False) == (9, False)
    ), "Triple quoted string ending in other triple quoted string"

# Generated at 2022-06-14 11:38:37.796928
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    from source.logger import setup_logging
    from source.main import handle_io_error

    _, _ = setup_logging()

    handle_io_error(None, None, RoughParser().set_lo, None, None)

# Generated at 2022-06-14 11:39:19.457338
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    def test(s, index, mustclose, brackets):
        hp = HyperParser(s, index)
        actual = hp.get_surrounding_brackets(mustclose=mustclose)
        expected = tuple(
            "<%s>" % (s.index(index) + len(s) - s.index(bracket))
            if bracket is not None
            else None
            for bracket in brackets
        )
        print()
        print(s.replace("\n", "\\n"))
        print(index, mustclose, brackets, actual, expected)
        return expected == actual

    def test_format_error(s, index, mustclose, brackets):
        try:
            HyperParser(s, index)
            return False
        except ValueError:
            return True

    ok = True

    # test without any brackets

# Generated at 2022-06-14 11:39:29.597267
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    def test(text, index, expected_value):
        hyper_parser = HyperParser(text, index)
        assert hyper_parser.is_in_string() == expected_value


# Generated at 2022-06-14 11:39:39.716595
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    from idlelib.editor import EditorWindow

    # create a text widget to use for testing
    text = EditorWindow(None)
    text.text["insert"](0.0, "if foo:\n" "    if (x and y)\n" "        print(x|y)\n")
    text.text["insert"] = 0.0, " if foo:\n" "    if (x and y)\n" "        print(|x)\n"
    text.text["insert"] = 98.0, "1\n"
    text.text["insert"] = 100.0, "2\n"
    text.text["insert"] = 102.0, "3\n"
    text.text["insert"] = 104.0, "4\n"
    text.text["insert"] = 106.0, "5\n"
    text

# Generated at 2022-06-14 11:39:52.233964
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    def test(text, index, expected):
        try:
            # Verify if HyperParser.is_in_string() computes the same value
            # as string_is_in_string().
            result = HyperParser(text, index).is_in_string()
            assert result == expected, (
                "For index %s, result %d is different from" " expected %d." % (index, result, expected)
            )
        except:
            print("Error in HyperParser.is_in_string() at index %s." % index)
            raise

    import string

    # Test basic abilities of the HyperParser.
    test(string, "1.0", 0)
    test(string, "1.end", 1)
    test(string, "2.0", 1)
    test(string, "end-1c", 1)

# Generated at 2022-06-14 11:40:00.124189
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    rp = RoughParser()
    rp.set_str("""
    (1,
    2,
    3,# comment
    4,
    5)
    """)
    assert rp.compute_bracket_indent() == 4

    rp = RoughParser()
    rp.set_str("""
    (
    1,
    2,
    (3,))
    """)
    assert rp.compute_bracket_indent() == 4


# Generated at 2022-06-14 11:40:09.729841
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    import unittest

    class Test_HyperParser_get_expression(unittest.TestCase):

        def do_test(self, source, index, expected):
            # Once we become compatible with Python 3.8, replace the
            # following 2 lines with "source = source.encode('utf-8')"
            source = source.encode()
            index = index.encode()
            text = Text(source)
            tk = HyperParser(text, index)
            self.assertEqual(tk.get_expression(), expected)

        def test_simple(self):
            self.do_test("foo(1,2)", "1.0-1c", "")
            self.do_test("foo(1,2)", "1.0", "foo")

# Generated at 2022-06-14 11:40:21.357688
# Unit test for method get_num_lines_in_stmt of class RoughParser
def test_RoughParser_get_num_lines_in_stmt():
    # a one-liner
    rp = RoughParser("    x = 5", "", "")
    assert rp.get_num_lines_in_stmt() == 1
    # a two-liner
    rp = RoughParser("    x = 5 \\ \n    y = 6", "", "")
    assert rp.get_num_lines_in_stmt() == 2
    # a two-liner where the first line is a comment
    rp = RoughParser("    # x = 5 \\ \n    y = 6", "", "")
    assert rp.get_num_lines_in_stmt() == 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 11:40:30.312230
# Unit test for method get_num_lines_in_stmt of class RoughParser
def test_RoughParser_get_num_lines_in_stmt():
    # pylint: disable=redefined-builtin
    # pylint: disable=missing-docstring

    def do1(str_, expected):
        rp = RoughParser(str_)
        GOT = rp.get_num_lines_in_stmt()
        print(
            "input %r, expected %d, got %d" % (str_, expected, GOT),
            file=sys.stderr,
        )
        # assert expected == GOT

    do1("""\
if 1:
    if 1:
        a = 1
    else:
        a = 2
""", 3)

    do1(
        """\
if (
    b
):
    pass
""",
        3,
    )


# Generated at 2022-06-14 11:40:35.238396
# Unit test for method get_last_open_bracket_pos of class RoughParser
def test_RoughParser_get_last_open_bracket_pos():
    # pylint: disable=redefined-outer-name
    def eq(s, n):
        rp = RoughParser(s, indent_width=4, tabwidth=8)
        assert rp.get_last_open_bracket_pos() == n

    eq("[1,\n2]", 0)
    eq("  [1,\n2]", 2)
    eq("[1,\n2]\n", 5)
    eq("[1,\n2]\n#hi", 5)
    eq("[1,\n2]\n#hi\n", 7)
    eq("[1,\n2\n]\n", 5)
    eq("[1,\n2]\n#hi", 5)

# Generated at 2022-06-14 11:40:40.907851
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def assert_expr(text, index, expected):
        h = HyperParser(text, index)
        actual = h.get_expression()
        if actual != expected:
            print(
                "assertion failed for '%s' @ %s.\n"
                "returned '%s', expected '%s'" % (text.get("1.0", "end"), index, actual, expected)
            )

    def test_one(text):
        assert_expr(text, "1.0", "")
        assert_expr(text, "2.0", "")

        #----

        assert_expr(text, "1.1", "")
        assert_expr(text, "1.4", "")

        #----

        assert_expr(text, "2.2", "")

# Generated at 2022-06-14 11:42:39.113644
# Unit test for method compute_backslash_indent of class RoughParser

# Generated at 2022-06-14 11:42:51.954278
# Unit test for method is_block_closer of class RoughParser
def test_RoughParser_is_block_closer():
    from pygments.formatters import NullFormatter


# Generated at 2022-06-14 11:42:59.688391
# Unit test for method is_in_code of class HyperParser

# Generated at 2022-06-14 11:43:05.752631
# Unit test for method set_index of class HyperParser

# Generated at 2022-06-14 11:43:13.739827
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    rp = RoughParser("  if foo: pass\n")
    assert rp.compute_bracket_indent() == 2
    rp = RoughParser("  if foo: pass\n  pass\n")
    assert rp.compute_bracket_indent() == 4
    rp = RoughParser("  if (foo):\n    pass\n")
    assert rp.compute_bracket_indent() == 4
    rp = RoughParser("\n  if (foo):\n    pass\n")
    assert rp.compute_bracket_indent() == 4
    rp = RoughParser("if foo:\n  pass\n")
    assert rp.compute_bracket_indent() == 2
    rp = RoughParser("  if foo:\n    pass\n")
   

# Generated at 2022-06-14 11:43:25.891036
# Unit test for constructor of class HyperParser
def test_HyperParser():
    # We test the standard examples from the documentation

    # Case 1:
    text = text_widget(
        # Code
        "if x < 0:\n"
        "    print('negative')\n"
        "# Comment\n"
        "if x < 0:\n"
        "    print('nonpositive')\n",
        # Position (line, column)
        (3, 20),
    )
    hp = HyperParser(text, "2.0")
    assert hp.rawtext == "if x < 0:\n    print('nonpositive') "
    assert hp.bracketing == [
        (0, 0),
        (3, 1),
        (8, 1),
        (13, 0),
    ]

# Generated at 2022-06-14 11:43:36.191616
# Unit test for constructor of class HyperParser

# Generated at 2022-06-14 11:43:46.414281
# Unit test for constructor of class HyperParser
def test_HyperParser():
    starts = ["", "(", "[", "{", '"', "'", "def ", "def\t", "def\n"]

    def construct_stops(starts):
        return [
            "%s" % (start,)
            for start in starts
        ] + [
            "%s)" % (start,)
            for start in starts
        ] + [
            "%s]" % (start,)
            for start in starts
        ] + [
            "%s}" % (start,)
            for start in starts
        ] + [
            "%s#" % (start,)
            for start in starts
        ] + [
            "%s\"" % (start,)
            for start in starts
        ] + [
            "%s'" % (start,)
            for start in starts
        ]

    stops = construct_stops(starts)


# Generated at 2022-06-14 11:43:59.873594
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    "Test the method is_in_code of class HyperParser."

    # We test the method with a class which sets the method and
    # compares it to a given expected value.
    class TestCode:
        def __init__(self, rawtext, indexinrawtext, expected):
            self.rawtext = rawtext
            self.indexinrawtext = indexinrawtext
            self.expected = expected

        def check(self, hyperparser):
            result = hyperparser.is_in_code()
            if result == self.expected:
                return None
            if self.expected:
                return "Failed: is_in_code returned False for\n%s^%s\n" % (
                    self.rawtext[: self.indexinrawtext],
                    self.rawtext[self.indexinrawtext :],
                )


# Generated at 2022-06-14 11:44:12.141395
# Unit test for method compute_backslash_indent of class RoughParser