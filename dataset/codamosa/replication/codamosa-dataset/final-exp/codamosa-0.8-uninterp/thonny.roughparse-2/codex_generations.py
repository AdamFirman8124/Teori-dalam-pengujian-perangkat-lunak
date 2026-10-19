

# Generated at 2022-06-14 11:39:21.475740
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    # test set_index of class HyperParser
    #
    # Expected behaviour:
    # The set_index method takes a char index, and sets the position
    # of the internal index of the class so that the indexbracket
    # and indexinrawtext attributes will reflect the position of the
    # given index.
    #
    # When we are at a closing bracket, we belong to the bracketing
    # that comes before it.
    #
    # When we are at the beginning of a line, we belong to the
    # previous line, and not to the initial indent.
    #
    # When we are at the end of a line, we belong to the bracketing
    # of the last char in the line.
    #
    import random

    # This function generates random bracketing lists.
    # It is used to test parser.set_str

# Generated at 2022-06-14 11:39:36.937853
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    def assert_indent(code, indent):
        rp = RoughParser(code)
        assert rp.compute_backslash_indent() == indent

    # Check escapes
    assert_indent("\\\n", 0)
    assert_indent("  \\  \n", 2)
    assert_indent("a = \\\n", 0)

    # Check last character
    assert_indent("for x in y:\\\n", 4)
    assert_indent("for x in y:  \\  \n", 4)
    assert_indent("for x in y: \\\n", 4)
    assert_indent("for x in y:\\\n", 4)
    assert_indent("xxx(\\\n", 4)
    assert_indent("xxx(  \\  \n", 4)

# Generated at 2022-06-14 11:39:49.388876
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    from idlelib.idle_test.htest import run

    def hyper_test(text, point, expected, mustclose):
        h = HyperParser(text, "insert")
        h.set_index("insert")
        result = h.get_surrounding_brackets("([{", mustclose)
        if result is None:
            result = "None"
        else:
            result = (result[0], result[1])
        if result != expected:
            print("%s %s %s %s %s %s" % (text.index("insert"), point, "Failed", expected, result, mustclose))


# Generated at 2022-06-14 11:39:56.956634
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    """If this function raises an exception, the unit test failed."""


# Generated at 2022-06-14 11:40:08.098479
# Unit test for constructor of class HyperParser
def test_HyperParser():
    import unittest

    # We need to subclass unittest.TestCase to use assertEqual and friends
    # (they are added in Python 2.7)
    class HyperParserTest(unittest.TestCase):
        def assertEqual(self, a, b):
            unittest.TestCase.assertEqual(self, a, b)

        def assertTrue(self, v):
            unittest.TestCase.assertTrue(self, v)

        def assertFalse(self, v):
            unittest.TestCase.assertFalse(self, v)

        def _make_hyperparser(self, text, index):
            text = _build_text(text)
            hp = HyperParser(text, index)
            self.assertEqual(text.get("1.0", "insert"), hp.rawtext)
           

# Generated at 2022-06-14 11:40:21.084900
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    def get(s, expected, expected_continuation):
        parser = RoughParser(s, 0)
        start, continuation = parser.find_good_parse_start()
        if start != expected:
            print("FAILED")
            print("input: %r" % s)
            print("expected start: %r" % expected)
            print("got start: %r" % start)
            raise ValueError
        if continuation != expected_continuation:
            print("FAILED")
            print("input: %r" % s)
            print("expected continuation:", expected_continuation)
            print("got continuation: %r" % continuation)
            raise ValueError
        if continuation == C_NONE:
            return

        actual_continuation = parser.get_continuation_type()
        # assert parser.get_continuation_

# Generated at 2022-06-14 11:40:30.181034
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    def assert_indent(s, expected):
        parser = RoughParser(s, indent_width=4, tabwidth=4)
        i = parser.compute_backslash_indent()
        assert i == expected, "got %d, expected %d" % (i, expected)

    assert_indent("""\
a = \\
  1
""", 2)
    assert_indent("""\
a = bar(
  a = 1,
  b = 2,
  c = 3,
  )
""", 2)
    assert_indent("""\
if 1:
  a = bar(
    a = 1,
   b = 2,
  c = 3,
  )
""", 2)
    assert_indent("""\
a = \\
  1
""", 2)

# Generated at 2022-06-14 11:40:45.307760
# Unit test for constructor of class HyperParser

# Generated at 2022-06-14 11:40:54.098519
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    import unittest
    import unittest.mock

    class Test(unittest.TestCase):
        def setUp(self):
            self.hp = HyperParser(
                unittest.mock.Mock(
                    indent_width=4, tabwidth=4, get=lambda a, b: "", index=lambda x: 0
                ),
                "index",
            )

        def test_failures(self):
            from idlelib import hyperparser

            hp = hyperparser.HyperParser
            self.assertRaises(ValueError, hp(None, None).get_expression)
            self.assertRaises(ValueError, hp(None, None).is_in_code)
            self.assertRaises(ValueError, hp(None, None).is_in_string)


# Generated at 2022-06-14 11:40:56.245433
# Unit test for constructor of class HyperParser
def test_HyperParser():
    # This should not raise an exception.
    HyperParser(tk.Text(), "1.0")



# Generated at 2022-06-14 11:41:51.536700
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    import doctest
    import sys

    failures, tests = doctest.testmod(HyperParser, report=False)

    if failures:
        raise Exception("%d/%d doctest failed" % (failures, tests))


test_HyperParser_get_surrounding_brackets()

# Generated at 2022-06-14 11:41:58.874541
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    rp = RoughParser("a = '''\\\n'", 0, 4)
    res = rp.compute_backslash_indent()
    assert res == 1, res

    rp = RoughParser('assert foo(a)\\\nand bar(b)\\\nand baz(c)', 0, 4)
    res = rp.compute_backslash_indent()
    assert res == 5, res




# Generated at 2022-06-14 11:42:07.909740
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def test(s):
        rough_parser = RoughParser(s, 0)
        return rough_parser.compute_bracket_indent()
    # pylint: disable=bad-whitespace
    assert test("[\n  1,\n  2,\n]") == 2
    assert test("[\n  1,\n  2,\n]\n") == 0
    assert test("[\n  [\n    1,\n    2,\n  ],\n]\n") == 2
    assert test("[\n  1,\n  2,\n  3,\n]\n") == 2
    assert test("[\n  1,\n  2,\n  \n") == 2

# Generated at 2022-06-14 11:42:20.792592
# Unit test for constructor of class HyperParser
def test_HyperParser():
    import unittest

    class _TestHyperParser(unittest.TestCase):
        @staticmethod
        def _index_helper(text, expected, index):
            hp = HyperParser(text, index)
            self._assert_bracketing(text, expected, hp.bracketing)

        @staticmethod
        def _set_index_helper(text, expected, start, index):
            hp = HyperParser(text, start)
            hp.set_index(index)
            self._assert_bracketing(text, expected, hp.bracketing)

        @staticmethod
        def _assert_bracketing(text, expected, result):
            _fb = _build_char_in_string_func("1.0")
            b_expected = _paren_finder(expected, 0, len(expected), _fb)

# Generated at 2022-06-14 11:42:27.709796
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    # test a few cases
    def check(hp, index, expected_indexbracket):
        hp.set_index(index)
        got = hp.indexbracket
        if got != expected_indexbracket:
            raise AssertionError("got %s for %s, expected %s" % (got, index, expected_indexbracket))


# Generated at 2022-06-14 11:42:38.431866
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    from unittest.mock import Mock

    text = Mock()
    text.indent_width = 8
    text.tabwidth = 8
    # Here we test various cases of indentation that could occur.
    # The parser should be able to figure out the nesting from the
    # indentation alone.
    text.get.return_value = """\
        \t\t\t    "foo"
            a (
        """
    hp = HyperParser(text, "1.0")
    assert hp.is_in_string()
    hp.set_index("1.15")
    assert not hp.is_in_string()
    hp.set_index("1.16 linestart")
    assert hp.is_in_string()
    hp.set_index("1.16 lineend")
    assert hp.is_in

# Generated at 2022-06-14 11:42:51.308432
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    def ki(s, indent_width=4, tabwidth=8):
        return RoughParser(s, indent_width, tabwidth).compute_backslash_indent()

    # Everything in column 0
    assert ki("if 1:") == 0
    assert ki("if 1:\n  pass") == 0
    assert ki("if 1:\n  pass\n  pass") == 0
    assert ki("if 1:\n  pass\n  pass\n") == 0
    assert ki("if 1:\n  pass\n  pass\n\n") == 0
    assert ki("if 1:\n  pass\n  pass\n\n\n") == 0
    assert ki("if 1:\n  pass\n\npass\n") == 0

# Generated at 2022-06-14 11:42:59.144199
# Unit test for method compute_backslash_indent of class RoughParser

# Generated at 2022-06-14 11:43:11.451753
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    fail_list = []

# Generated at 2022-06-14 11:43:17.990664
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    import sys
    import unittest

    class Test(unittest.TestCase):
        def test_1(self):
            t = Text(wrap='none', undo=False, autoseparators=False)
            t.tag_configure("test", background="white", relief="sunken")
            t.delete("1.0", "end")
            t.mark_set("insert", "1.0")

            # Test with get_surrounding_brackets