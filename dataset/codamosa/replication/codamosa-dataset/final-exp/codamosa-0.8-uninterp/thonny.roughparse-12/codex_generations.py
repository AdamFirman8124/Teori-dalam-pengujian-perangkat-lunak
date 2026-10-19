

# Generated at 2022-06-14 11:39:38.164810
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def helper(input, tabwidth, expected):
        p = RoughParser(input, tabwidth)
        got = p.compute_bracket_indent()
        if expected != got:
            print("test failed")
            print("input   : %r" % (input,))
            print("tabwidth:", tabwidth)
            print("expected:", expected)
            print("got     :", got)
    helper(
        "foo(\n"
        "   42,\n"
        "   spam(3,\n"
        "       (1, 2, 3),\n"
        "   ),\n"
        "   [4, 5, 6],\n"
        ")", 4, 7
    )

# Generated at 2022-06-14 11:39:51.477912
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:40:02.442855
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    import unittest
    class Test(unittest.TestCase):
        def test(self, input_, start):
            x = RoughParser(input_)
            self.assertEqual(x.find_good_parse_start(), start)

# Generated at 2022-06-14 11:40:10.854055
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    """Test proper indentation is being computed for statements that
    were broken with a backslash"""
    rp = RoughParser("foo = \\\n1\n", indent_width=4, tab_width=8)
    assert rp.compute_backslash_indent() == 4
    rp = RoughParser("foo = bar(\\\n1,\n", indent_width=4, tab_width=8)
    assert rp.compute_backslash_indent() == 8
    rp = RoughParser("foo = bar(\\\n    1,\n", indent_width=4, tab_width=8)
    assert rp.compute_backslash_indent() == 12

# Generated at 2022-06-14 11:40:16.388231
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = Text(None, "")
    text.insert("end", "a = 4 + (5 +\n")
    parser = HyperParser(text, "end-1c")
    parser.set_index("end")
    assert parser.indexinrawtext == 8
    assert parser.indexbracket == 3


# Generated at 2022-06-14 11:40:26.829737
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    rp = RoughParser(tabsize=4, indent_width=4)
    s = """hello
    # This is a comment
    # here is another
    world
    hello
    """
    rp.set_str(s)
    assert rp.find_good_parse_start() == 0
    rp.set_lo(1)
    assert rp.find_good_parse_start() == 0
    rp.set_lo(15)
    assert rp.find_good_parse_start() == 0
    rp.set_lo(18)
    assert rp.find_good_parse_start() == 18
    rp.set_lo(30)
    assert rp.find_good_parse_start() == 18
    rp.set_lo(31)
    assert rp.find

# Generated at 2022-06-14 11:40:43.726466
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    text = Tkinter.Text()
    text.insert('1.0', '"""This is a test"""\n')
    parser = HyperParser(text, "1.0")
    status = parser.is_in_code()
    assert status == 0, 'Wrong result from is_in_code'

    text = Tkinter.Text()
    text.insert('1.0', '"""This is a test"""\n')
    parser = HyperParser(text, "1.6")
    status = parser.is_in_code()
    assert status == 0, 'Wrong result from is_in_code'

    text = Tkinter.Text()
    text.insert('1.0', '"""This is a test"""\n')
    parser = HyperParser(text, "1.13")
    status = parser.is_

# Generated at 2022-06-14 11:40:53.393319
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    # Test is_in_string within a string.
    h = HyperParser("'123'", "2.0")
    assert h.is_in_string()

    # Test is_in_string outside of a string.
    h = HyperParser("'123'", "3.0")
    assert not h.is_in_string()

    # Test is_in_string at end of string.
    h = HyperParser("'123'", "4.0")
    assert not h.is_in_string()

    # Test is_in_string within a string, after an escaped character.
    h = HyperParser(r"'1\'23'", "3.0")
    assert h.is_in_string()

    # Test is_in_string not within a string, after an escaped character.

# Generated at 2022-06-14 11:41:03.215541
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():

    def test(s, expected, tbw=8):
        p = RoughParser("x = " + s, tbw)
        got = p.compute_bracket_indent()
        assert expected == got, f"compute_bracket_indent result for x = {s!r} should be {expected!r}, not {got!r}"
        return got

    test("[\n1,\n2]", 0)
    test("[\n1\n]", 3)
    test("[\n(1,\n2\n)]", 3)
    test("foo(\n1,\n2\n)", 3)
    test("foo(\n1, [\n2,\n3\n],\n4\n)", 3)

# Generated at 2022-06-14 11:41:15.564643
# Unit test for method set_lo of class RoughParser
def test_RoughParser_set_lo():
    def get_goodlines(parser, continuation):
        parser.set_lo('asd\n\n\ndfg\n\n\nhij')
        assert parser.get_num_lines() == 5
        if continuation == C_NONE:
            assert parser.get_continuation_type() == C_NONE
            assert list(parser.get_good_lines()) == [0, 4, 8, 12]
        elif continuation == C_BRACKET:
            assert parser.get_continuation_type() == C_BRACKET
            assert list(parser.get_good_lines()) == [0, 4, 8, 13]
            assert parser.get_num_lines_in_stmt() == 5
        elif continuation == C_BACKSLASH:
            assert parser.get_continuation_type() == C_BACK

# Generated at 2022-06-14 11:42:00.038347
# Unit test for method find_good_parse_start of class RoughParser

# Generated at 2022-06-14 11:42:08.664943
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    import unittest

    import test.test_support

    class HyperParserTest(unittest.TestCase):
        def test_sanity(self):
            # Test with a minimal text. It contains:
            # - no string or comment,
            # - no escaped newline or backslash,
            # - no newline
            # - no backslash at end of lines
            # - only (, ), augmented assignment, and a few operators.
            text = "(a+b)\n(a+=b)\n"
            numlines = len(text.splitlines())
            parser = HyperParser(text, "1.0")
            # the bracketing must be in sync with the text indices
            bracketing = parser.bracketing

            self.assertEqual(len(bracketing), 6)

# Generated at 2022-06-14 11:42:21.169502
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    def do(text, index_text, expected):
        hp = HyperParser(text, index_text)
        if hp.is_in_code() != expected:
            print("Test failed:", text, index_text, expected)
            print("             ", hp.text.get("1.0", "end"), hp.indexinrawtext)
            print("             ", hp.rawtext)
            print("             ", hp.bracketing)
            print("             ", hp.isopener)
            print("             ", hp.indexbracket, hp.isopener[hp.indexbracket])

    # Simplest cases
    do("a", "1.1", True)
    do("a # comment", "1.3", False)
    do("# comment", "1.0", False)

# Generated at 2022-06-14 11:42:31.258186
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    text = TestTextWidget(tabwidth=8)
    text.insert("insert", """\
    # This is a comment
    'This is a string'
    "This is also a string"
    # Now we are in normal code
    a = b
    a = "A string"
    """)
    h = HyperParser(text, "1.0")
    assert not h.is_in_code()
    h.set_index("1.5")
    assert not h.is_in_code()
    h.set_index("2.0")
    assert not h.is_in_code()
    h.set_index("2.5")
    assert h.is_in_code()
    h.set_index("4.0")
    assert h.is_in_code()
    h.set_index

# Generated at 2022-06-14 11:42:40.488437
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    text = Text()
    text.insert("insert", "")
    data = {
        "start": "x((y((z))[w])",
        "end": "q",
        "pos": [2, 3, 6, 11, 19, 21, 22],
        "exp": [
            ("(", ")"),
            ("(", ")"),
            ("(", ")"),
            ("(", "]"),
            ("((z))[w]", ")"),
            ("(y((z))[w])", ")"),
            ("x((y((z))[w]))", ""),
        ],
    }
    for i in range(len(data["pos"])):
        text.delete("1.0", "end")
        text.insert("1.0", data["start"])

# Generated at 2022-06-14 11:42:52.721330
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    # pylint: disable=star-args
    def f(args):
        return RoughParser(*args).find_good_parse_start()

    f.description = "RoughParser.find_good_parse_start"
    f.example = """\
    >>> f = RoughParser("class C:\\n  pass\\n").find_good_parse_start
    >>> f()
    4"""

    assert f("class C:\\n  pass\\n") is None
    assert f("class C:\\n  pass\\n\\nx = 3") == 4
    assert f("\\nclass C:\\n  pass\\n") == 1
    assert f("\\n\\nclass C:\\n  pass\\n") == 2
    assert f("pass\\n\\nclass C:\\n  pass\\n") == 5

# Generated at 2022-06-14 11:43:08.912573
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    def check(s, result, is_full_block=False):
        rp = RoughParser(s, "xyz.py", 0)
        rp.is_full_block = is_full_block
        assert rp.find_good_parse_start() == result

    check("", 0)
    check("\n", 0)
    check("\n\n", 2)
    check("\n\n\n", 4)
    check("#\n", 2)
    check("#\n\n", 2)
    check("\n#\n", 2)
    check("x\n", 1)
    check("x\n\n", 1)
    check("x\n#\n", 1)
    check("x\n#\n\n", 1)

# Generated at 2022-06-14 11:43:17.245658
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    from idlelib.idle_test.htest import run


# Generated at 2022-06-14 11:43:28.050327
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    rp = RoughParser("  \n\n  # comment\n")
    print(rp.find_good_parse_start())  # 1
    rp = RoughParser("\n\n")
    print(rp.find_good_parse_start())  # 0
    rp = RoughParser("\n\n  # comment\n")
    print(rp.find_good_parse_start())  # 0
    rp = RoughParser("\n\n  # comment\n\n")
    print(rp.find_good_parse_start())  # 0
    rp = RoughParser("\n\n  # comment\n\n  ")
    print(rp.find_good_parse_start())  # 0

# Generated at 2022-06-14 11:43:42.472957
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    def assertEqual(actual, expected):
        assert actual == expected, "%r != %r" % (actual, expected)

    def check(text):
        parser = RoughParser(text, "utf-8")
        assertEqual(parser.find_good_parse_start(), len(text.lstrip()))

    # Trigger UnicodeDecodeError in parse_start_pos.
    check("\xff")
    # Trigger EOFError in parse_start_pos.
    check("\n")
    # Trigger IndentationError in parse_start_pos.
    check(" ")
    # Trigger EOFError in find_good_parse_start.
    check("\n\n")
    # Trigger IndentationError in find_good_parse_start.
    check("\n ")
    # Trigger SyntaxError in find_good

# Generated at 2022-06-14 11:44:48.493141
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():

    assert(HyperParser(None,None).is_in_code() is None)


# Generated at 2022-06-14 11:45:02.856981
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    # pylint: disable=redefined-builtin
    rp = RoughParser("   ")
    assert rp.get_base_indent_string() == "   "

    rp = RoughParser("a = 1\nif x:\n  y = 2\n")
    assert rp.get_base_indent_string() == "  "

    rp = RoughParser("if x:\n  y = 2")
    assert rp.get_base_indent_string() == ""

    rp = RoughParser(
        "a = 1\nif x:\n  y = 2\n  \n  \n  \n  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    )
    assert rp.get_base

# Generated at 2022-06-14 11:45:10.746115
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    # pylint: disable=redefined-builtin

    # This is a simplified version of test_compute_bracket_indent.
    # See that test if you're trying to fix this code.
    #
    # There is no need to test the invalid arguments, since any
    # calls to this method in this module will be preceded by a
    # state check.

    def test_it(str, indent_width, tabwidth):
        # pylint: disable=redefined-builtin
        p = RoughParser(str, indent_width, tabwidth)
        return p.compute_bracket_indent()

    # try all variations of \n and \t
    test_it('[\n  1,\n  2,\n]', 8, 8)

# Generated at 2022-06-14 11:45:22.326767
# Unit test for method find_good_parse_start of class RoughParser

# Generated at 2022-06-14 11:45:33.504474
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    thetext = "a\nb\n\nc\n"
    assert 0 == HyperParser(thetext, "1.0").indexbracket
    assert 0 == HyperParser(thetext, "1.1").indexbracket
    assert 0 == HyperParser(thetext, "2.0").indexbracket
    assert 0 == HyperParser(thetext, "2.1").indexbracket
    assert 0 == HyperParser(thetext, "3.0").indexbracket
    assert 1 == HyperParser(thetext, "4.0").indexbracket
    assert 1 == HyperParser(thetext, "4.1").indexbracket
    assert len(HyperParser(thetext, "4.1").bracketing) == 2



# Generated at 2022-06-14 11:45:41.202463
# Unit test for constructor of class HyperParser
def test_HyperParser():
    print("Testing HyperParser")
    import os

    text = tkinter.Text()
    text = TextWrapper(text)
    text.insert("end", "(a=b) and (c=d)")
    hyper = HyperParser(text, "3.0")
    assert hyper.is_in_code()
    assert not hyper.is_in_string()
    assert hyper.get_surrounding_brackets() == ("1.0", "5.0")

    text.delete("1.0", "end")
    text.insert("end", 'print("1")')
    hyper = HyperParser(text, "3.0")
    assert hyper.is_in_code()
    assert not hyper.is_in_string()
    assert hyper.get_surrounding_brackets() is None
