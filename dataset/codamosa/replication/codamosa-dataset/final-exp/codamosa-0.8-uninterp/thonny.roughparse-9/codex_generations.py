

# Generated at 2022-06-14 11:41:02.978990
# Unit test for method compute_bracket_indent of class RoughParser

# Generated at 2022-06-14 11:41:15.415037
# Unit test for constructor of class HyperParser
def test_HyperParser():
    import unittest

    class HPTestCase(unittest.TestCase):
        def setUp(self):
            text = Text()
            self.text = text
            text.insert("1.0", "a=3\nif True:\n    pass\n")
            self.hp = HyperParser(text, "1.0")
            self.assertEqual(self.hp.indexbracket, 1)
            self.assertEqual(self.hp.indexinrawtext, 1)

        def test_get_surrounding_brackets(self):
            self.assertEqual(self.hp.get_surrounding_brackets(), (None, None))
            self.assertEqual(self.hp.get_surrounding_brackets(""), (None, None))

# Generated at 2022-06-14 11:41:20.900446
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    #pylint: disable=expression-not-assigned

    def eq(text, expected):
        if RoughParser(text).get_base_indent_string() != expected:
            print(repr(text))
            print(" " * 7 + "|")
            print(" " * 7 + repr(expected))

    eq("a = 1", "")
    eq("  a = 1", "  ")
    eq("if a:\n  b = 1\n  c = 2", "  ")
    eq("  if a:\n    b = 1\n    c = 2", "    ")
    eq("  if a:\n    b = 1\n  c = 2", "  ")
    eq("  if a:\n    b = 1\n    if c:\n      d = 3", "      ")



# Generated at 2022-06-14 11:41:25.767359
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    # pylint: disable=redefined-builtin
    r = RoughParser("a = [\n    1,\n    2,\n    3,\n]", 4)
    assert r.compute_bracket_indent() == 4



# Generated at 2022-06-14 11:41:31.983894
# Unit test for method __getitem__ of class StringTranslatePseudoMapping
def test_StringTranslatePseudoMapping___getitem__():
    text = "a + b\tc\nd"
    mapping = StringTranslatePseudoMapping(
        {ord(c): ord(c) for c in ' \t\n\r'}, ord('x'))
    assert mapping[ord('a')] == ord('x')
    assert mapping[ord(' ')] == ord(' ')



# Generated at 2022-06-14 11:41:39.661923
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    from textwrap import dedent

    def get_surrounding_brackets(src, i, openers="([{", mustclose=False):
        parser = HyperParser(dedent(src), "1.%d" % i)
        return parser.get_surrounding_brackets(openers, mustclose)

    def assert_surrounding_brackets(src, i, res):
        src = dedent(src)
        res = (src[res[0]], src[res[1] - 1])
        assert get_surrounding_brackets(src, i) == res

    # Test 1
    src = """\
    def f(self, a):
        if a:
            a.foo(
                5,
                (1,
                 2))"""

# Generated at 2022-06-14 11:41:53.524463
# Unit test for method is_block_opener of class RoughParser
def test_RoughParser_is_block_opener():
    def test(s, res):
        p = RoughParser(s)
        assert p.is_block_opener() == res
    test("def x():\n    pass\n", True)
    test("def x():\n    pass", True)
    test("def x():\n pass\n", False)
    test("def x():\n pass", False)
    test("def x():\n    pass #comment\n", True)
    test("def x():\n    pass #comment", True)
    test("def x():\n pass #comment\n", False)
    test("def x():\n pass #comment", False)
    test("def x():\n  pass\n", False)
    test("def x():\n  pass", False)

# Generated at 2022-06-14 11:42:04.471453
# Unit test for method get_last_open_bracket_pos of class RoughParser
def test_RoughParser_get_last_open_bracket_pos():
    lines = ["a = [1,\n", "2,\n", "3,\n", "4,]\n", "b = [\n", "]\n", "c = (\n", ")"]

    for i in range(len(lines)):
        pars = RoughParser("".join(lines[:i+1]))
        res = pars.get_last_open_bracket_pos()
        if i in [0, 5, 6]:
            assert res is None
        elif i in [1, 2, 3]:
            res_expected = sum(map(len, lines[:i]))
            assert res == res_expected
        elif i == 4:
            res_expected = sum(map(len, lines[:i])) + 1
            assert res == res_expected

# Generated at 2022-06-14 11:42:11.390875
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def _check(str_, expect):
        got = RoughParser(str_).compute_bracket_indent()
        if got != expect:
            print("test_RoughParser_compute_bracket_indent() failed")
            print("    string:    %r" % str_)
            print("    expected:  %r" % expect)
            print("    got:       %r" % got)

    _check("# test\n[", 1)
    _check("# test\n[a]", 1)
    _check("# test\na = [", 5)
    _check("# test\n[a] = [", 5)
    _check("# test\n[a] = [b]", 1)
    _check("# test\na = []", 1)

# Generated at 2022-06-14 11:42:13.649751
# Unit test for method set_str of class RoughParser
def test_RoughParser_set_str():
    readline = input = input("Type a piece of code: ")
    rp = RoughParser()
    rp.set_str(readline)



# Generated at 2022-06-14 11:42:41.442470
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    from unittest import TestCase

    class HyperParserUnitTest(TestCase):
        def test_set_index(self):
            from idlelib.EditorWindow import EditorWindow

            text = EditorWindow.EditorWindow(None)
            text.set_close_on_destroy_window(False)
            text.filename = ""
            text.set_insert_off(0)
            text.set_insert_on(1)
            text.set_insert_off(2)
            text.set_insert_on(3)
            text.set_insert_off(4)
            text.set_insert_on(5)
            text.set_insert_off(6)
            text.set_insert_on(7)
            text.set_insert_off(8)
            text.set_insert_on(9)
            text

# Generated at 2022-06-14 11:42:48.194599
# Unit test for constructor of class HyperParser
def test_HyperParser():
    text = Tk.Text()
    text.insert("1.0", "f(x, y, + 2, * 3, ** 4, a=1, b=2, c=3)\n")
    text.mark_set("test", "1.23")
    hp = HyperParser(text, "test")
    print(
        "f(x, y, + 2, * 3, ** 4, a=1, b=2, c=3)",
        "1.23",
        hp.rawtext,
        hp.bracketing,
        hp.isopener,
    )



# Generated at 2022-06-14 11:42:57.187668
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    text = EditorWindow(root, "")
    parser = HyperParser(text, "1.0")

    text.mark_set("insert", "1.0")
    text.insert("insert", '"""a string')
    assert not parser.is_in_code()

    text.mark_set("insert", "1.0")
    text.insert("insert", '"""a string"""')
    assert not parser.is_in_code()

    text.mark_set("insert", "1.0")
    text.insert("insert", '"""a string""" #')
    assert not parser.is_in_code()

    text.mark_set("insert", "1.0")
    text.insert("insert", '"""a string""" #comment')
    assert not parser.is_in_code()


# Generated at 2022-06-14 11:43:10.501494
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def check(text, indent):
        parser = RoughParser(text)
        assert parser.compute_bracket_indent() == indent

    check("if a:\n" * 3 + " b", 4)
    check("if a:\n" * 3 + " hello(", 8)
    check("if a:\n" * 3 + " [", 8)
    check("if a:\n" * 3 + " [1,", 8)
    check("if a:\n" * 3 + " [1,\n" + " " * 6 + "2", 12)
    check("if a:\n" * 3 + " {", 8)
    check("if a:\n" * 3 + " {1,", 8)
    check("if a:\n" * 3 + " {1:", 8)

# Generated at 2022-06-14 11:43:17.761484
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    # Simple
    h = HyperParser(Text(
        # 01234567890123456789012345678901234567890123
        "def f(x):\n    if x == 4:\n        return x\n",
    ), "1.5")
    h.set_index("1.5")
    eq(h.indexbracket, 3)
    h.set_index("1.3")
    eq(h.indexbracket, 2)

    # With a string
    h = HyperParser(Text(
        # 01234567890123456789012345678901234567890123
        'def f(x):\n    print("foo")\n    return x\n',
    ), "1.5")
    h.set_index("1.5")

# Generated at 2022-06-14 11:43:28.286190
# Unit test for constructor of class HyperParser
def test_HyperParser():
    def check(index, is_in_code, is_in_string, expression):
        p = HyperParser(text, text.index(index))
        if p.is_in_code() != is_in_code:
            print("is_in_code test failed for", repr(index), is_in_code)
        if p.is_in_string() != is_in_string:
            print("is_in_string test failed for", repr(index), is_in_string)
        if p.get_expression() != expression:
            print("expression test failed for", repr(index), expression)

    text = Text()
    text.insert(END, "ab\ncd = (\n   ef)")
    check("1.0", True, False, "")

# Generated at 2022-06-14 11:43:42.462715
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    text = "abcd efgh\n"
    hp = HyperParser(text, "1.0")
    assert hp.text == text
    assert hp.rawtext == "abcd efgh"
    assert hp.bracketing == [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
    ]
    assert hp.stopatindex == "2.end"
    assert hp.indexinrawtext == len(text) - len(text.index("3.0"))
    # Rawtext doesn't end with a newline, so this index isn't in rawtext anymore.
    hp.set_index("3.0")
    assert hp.indexin

# Generated at 2022-06-14 11:43:49.226052
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    """we will use the most important method of RoughParser: get_base_indent_string
    to write a test for this method.
    """
    def check(expected, source):
        parser = RoughParser(source, 0)
        actual = parser.get_base_indent_string()
        assert actual == expected, "%r %r %r %r" % (expected, actual, source, parser.stmt_bracketing)

    # 1. only whitespaces before first word
    check("    ", "    def foo():")
    check("    ", "    class foo():")
    check("    ", "    def foo(*args):")
    check("    ", "    class foo(*args):")
    check("    ", "    def foo(*args, **kwargs):")

# Generated at 2022-06-14 11:44:01.604053
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    def run_test(str, index, expected=None):
        if expected is None:
            expected = str
        p = HyperParser(str, index)
        assert p.get_expression() == expected

    run_test("foo.bar()", "1.end")
    run_test("foo.bar()", "1.16")
    run_test("foo.bar()", "1.2")
    run_test("foo.bar()", "1.0")
    run_test("foo.bar()", "0.0", "")
    run_test("foo\n.bar()", "1.end")
    run_test("foo(bar, baz)", "1.end")
    run_test("foo bar baz", "1.0", "")

# Generated at 2022-06-14 11:44:14.168423
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    # import Tkinter
    # t = Tkinter.Text()
    # t.pack()
    # t.focus_set()
    # t.insert(Tkinter.END, "a.b() . c .d")
    from unittest import TestCase

    class Test(TestCase):
        def do(self, text, index, expected):
            text = TextWrapper(text)
            hp = HyperParser(text, "%d.%d" % (index[0] + 1, index[1] + 1))
            result = hp.get_expression()
            self.assertEqual(result, expected)

    test = Test()
    test.do("a.b() . c .d", (0, 0), "")

# Generated at 2022-06-14 11:44:47.650425
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    rp = RoughParser("x=1\\\ny=2", 0)
    assert rp.compute_backslash_indent() == 2

# Generated at 2022-06-14 11:45:01.468616
# Unit test for method get_last_stmt_bracketing of class RoughParser
def test_RoughParser_get_last_stmt_bracketing():
    from xdress.utils import Parameter

    def test_get_last_stmt_bracketing(
        str_,
        indent_width=4,
        tabwidth=8,
    ):
        if isinstance(str_, Parameter):
            return
        p = RoughParser(str_, indent_width, tabwidth)
        return p.get_last_stmt_bracketing()

    r = test_get_last_stmt_bracketing
    assert r('x=1') == ((0, 0), (1, 0), (2, 0), (3, 0))
    assert r('x=1\ny=2') == ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0))


# Generated at 2022-06-14 11:45:08.880364
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    rp = RoughParser("[\n", 0)
    assert rp.compute_bracket_indent() == 1

    rp = RoughParser("[3,\n", 0)
    assert rp.compute_bracket_indent() == 3

    rp = RoughParser("[\n  foo,\n", 0)
    assert rp.compute_bracket_indent() == 3

    rp = RoughParser("[\n  foo,\n  [\n", 0)
    assert rp.compute_bracket_indent() == 5


# Generated at 2022-06-14 11:45:16.174897
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    text = "a=3+4\n"

    for i in range(len(text) + 1):
        h = HyperParser(text, repr(i) + ".0")
        if i >= 5:
            assert h.is_in_code() is False, "Wrong result for index %r" % i
        else:
            assert h.is_in_code() is True, "Wrong result for index %r" % i



# Generated at 2022-06-14 11:45:26.003348
# Unit test for constructor of class HyperParser
def test_HyperParser():
    from unittest import TestCase

    class TestHP(TestCase):
        def test_simple_parse(self):
            hp = HyperParser(text, index)
            hp.get_surrounding_brackets()
            hp.get_expression()

    from unittest import main

    main("idlelib.idle_test.test_hyperparser", verbosity=2, exit=False)

if __name__ == "__main__":
    text = Text()

# Generated at 2022-06-14 11:45:37.175893
# Unit test for method get_surrounding_brackets of class HyperParser

# Generated at 2022-06-14 11:45:49.888016
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    # pylint: disable=unused-variable

    # Find the rough start of a good parse for a single-line string,
    # after which we can then use the normal parser.

    def test(s, n):
        rp = RoughParser(s)
        assert rp.find_good_parse_start() == n

    test("if 1:\n  pass", 0)
    test("if 1:\n  pass\n", 0)
    test("if 1:\n\n  pass", 1)
    test("if 1:\n\n\n  pass", 2)
    test("if 1:\n\n\n\n  pass", 3)

    test("if 1:\n  pass\n#comment", 0)
    test("if 1:\n  pass\n#comment\n", 0)

# Generated at 2022-06-14 11:45:56.616339
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    def test(s, expect):
        result = compute_bracket_indent(s, tabwidth=TAB_WIDTH)
        if result != expect:
            print("failed test:", s)
            print("expected:", expect)
            print("     got:", result)
            print()

    test("if 1:", 4)
    test("if 1:\n    pass", 8)
    test("if 1:\n    pass\n", 4)
    test("if 1:\n    pass\n\n", 0)
    test("if 1:\n    pass\n    boo", 8)
    test("if 1: boo", 4)
    test("if 1: boo\n", 4)
    test("if 1: boo\n    pass", 8)

# Generated at 2022-06-14 11:46:11.700495
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    import unittest
    import unittest.mock

    class TestTextMock(unittest.mock.Mock):
        get = unittest.mock.Mock(return_value="")
        index = unittest.mock.Mock(return_value="")
        __getitem__ = unittest.mock.Mock(return_value="")

    class TestCase(unittest.TestCase):
        def assertExpression(self, text, index, expected):
            text = TestTextMock(indent_width=4, tabwidth=8)
            text.get.side_effect = lambda a, b: text[a:b]
            parser = HyperParser(text, index)
            text[:] = text.get.side_effect = text.__getitem__.side_effect = text

# Generated at 2022-06-14 11:46:23.610790
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start(): #@UnusedVariable
    def test(code):
        print("---code---\n" + code)
        mp = RoughParser(code)
        print("---result---")
        print(mp.find_good_parse_start())
    test("a = 0")
    test("a = 0\nb = ")
    test("a = 0\nb = '''\n")
    test("a = 0\nb = '''\n'''")
    test("a = 0\n'''\nb = ")
    test("a = 0\n'''\nb = ")
    test('''if True:
    if True:
        a = 0
        b = ''')
    test('''if True:
        if True:
            a = 0
            b = ''')

# Generated at 2022-06-14 11:48:23.899728
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    from unittest.mock import Mock


# Generated at 2022-06-14 11:48:32.474464
# Unit test for constructor of class HyperParser
def test_HyperParser():
    text = TkTextWrapper(None)
    text.insert("insert", "x = 10\n")
    text.mark_set("insert", "1.0")
    p = HyperParser(text, "insert")
    assert p.rawtext[p.indexinrawtext] == "x", repr(p.rawtext[p.indexinrawtext])
    assert p.is_in_code(), p.is_in_code()


# Generated at 2022-06-14 11:48:40.777212
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    text = "def f():\n    (1 +\n     2)\n"
    hp = HyperParser(text, "1.16")
    assert hp.get_surrounding_brackets() == ("1.8", "1.16")
    assert hp.get_surrounding_brackets(mustclose=True) is None

    text = "def f():\n    (1\n     + 2)\n"
    hp = HyperParser(text, "1.16")
    assert hp.get_surrounding_brackets() is None
    assert hp.get_surrounding_brackets(mustclose=True) is None

    text = "def f():\n    [1,\n     2, 3]\n"
    hp = HyperParser(text, "1.16")
    assert hp.get_surround