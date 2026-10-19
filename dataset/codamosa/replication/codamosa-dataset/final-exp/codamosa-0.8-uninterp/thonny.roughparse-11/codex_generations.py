

# Generated at 2022-06-14 11:37:31.039483
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    class Fake:
        text = None

        @staticmethod
        def index(i):
            return i

    def test(hyperp, text, should_be):
        text = textwrap.dedent(text)
        hyperp.text = Fake()
        hyperp.text.text = text + "\n"
        for i in range(len(text)):
            hyperp.set_index(str(i))
            got = hyperp.get_expression()
            if got != should_be:
                print("Wrong value for line %i.\nGot %s\nShould be %s" % (i, got, should_be))


# Generated at 2022-06-14 11:37:36.307915
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    # Test functions
    def do(input, output):
        "Test get_expression with the given input and output."
        if output is Stop:
            output = input
        t = Tk()
        try:
            text = Text(t, width=1, height=1)
            text.pack()
            text.insert("insert", input)
            text.mark_set("insert", "end - 1c")
            hp = HyperParser(text, "insert")
            value = hp.get_expression()
            t.destroy()
            if value != output:
                raise AssertionError("expected %r got %r" % (output, value))
        except:
            t.destroy()
            raise

    # Test cases
    do("x = (3)", "x")
    do("x = 3 + 4", "x")
   

# Generated at 2022-06-14 11:37:45.846817
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    # This function tests RoughParser.compute_backslash_indent when
    # continuation is C_BACKSLASH.
    from idlelib.idle_test.htest import mock, run

    def indented(str, indent=0):
        return " " * indent + str

    def check_backslash(rp, expected):
        """Check that compute_backslash_indent returns the expected value"""
        assert rp.compute_backslash_indent() == expected, (
            "compute_backslash_indent() should return %r, not %r"
            % (expected, rp.compute_backslash_indent())
        )

    assert_compile = run.assert_compile

    # Trivial test, one line
    rp = RoughParser("a = 1")


# Generated at 2022-06-14 11:37:56.504070
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    from unittest import mock

    class Mock:
        def __init__(self, value):
            self.value = value

        def __getitem__(self, i):
            return self.value[i]

        def __len__(self):
            return len(self.value)

        def index(self, i):
            if i == "%s-%dc" % (self.stopatindex, len(self.rawtext) - self.bracketing[before][0]):
                return "b"
            elif i == "%s" % self.stopatindex:
                return "a"
            elif i == "%s-%dc" % (self.stopatindex, len(self.rawtext) - (self.bracketing[after][0] - 1)):
                return "e"

# Generated at 2022-06-14 11:38:04.491301
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():

    def test(input_string, expected):
        hp = HyperParser(input_string, len(input_string) - 1)
        input_string = input_string.splitlines()[0]
        actual = hp.get_expression()
        print(actual)
        if expected != actual:
            print("test on string '%s' failed.\n"
                  "Expected: '%s'\n"
                  "  Actual: '%s'" % (input_string, expected, actual))
        assert expected == actual

    test("", "")
    test("a = b.c(d.e)", "e")
    test("a = b.c(d.", "")
    test("a = b.c(d?.e)", "e")
    test("a = b.c(d?", "")

# Generated at 2022-06-14 11:38:12.572110
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    if not _tkinter_available:
        return

    root = Tk()
    text = Text(root, width=40, height=20)
    text.pack()
    row = 0

    def insert_test(msg, surrounding_brackets, mustclose=False):
        nonlocal row
        print(msg)
        text.insert("insert", msg)
        text.insert("insert", "\n")
        row += 1
        if isinstance(surrounding_brackets, str):
            text.tag_add(str(row), "insert", "insert")
            text.insert("insert", "  ")
            text.insert("insert", surrounding_brackets)
            text.insert("insert", "\n\n")
            row += 1
            return
        text.insert("insert", "  ")

# Generated at 2022-06-14 11:38:19.596984
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    from idlelib.idle_test.mock_idle import Func
    from idlelib.idle_test.mock_idle import MockText
    mock_text = MockText

    def test(index, expected):
        mock_text.mark_set("insert", index)
        h = HyperParser(mock_text, index)
        actual = h.is_in_string()
        if actual != expected:
            print(
                "Failure in test of HyperParser.is_in_string: "
                "expected %r, got %r" % (expected, actual)
            )

    # Test various positions with respect to the last '"'
    mock_text.insert("1.0", '"a"\n"""b""""')
    test("1.0", True)
    test("1.1", True)


# Generated at 2022-06-14 11:38:31.481188
# Unit test for method compute_bracket_indent of class RoughParser
def test_RoughParser_compute_bracket_indent():
    # pylint: disable=redefined-builtin,unused-variable

    def do(s, ind, tabwidth=8):
        rp = RoughParser(s, tabwidth)
        return rp.compute_bracket_indent()

    # zero indent
    assert do("[\n") == 0
    assert do("[#\n") == 0
    assert do("[ ]\n") == 0
    assert do("[# ]\n") == 0
    assert do("[\n]") == 0
    assert do("[ \n]") == 0
    assert do("[\n#\n]") == 0
    assert do("[\n# ]\n") == 0
    assert do("[#\n# ]\n") == 0
    assert do("[a]\n") == 0

# Generated at 2022-06-14 11:38:33.258695
# Unit test for method get_base_indent_string of class RoughParser

# Generated at 2022-06-14 11:38:45.415739
# Unit test for method find_good_parse_start of class RoughParser

# Generated at 2022-06-14 11:39:41.584237
# Unit test for method set_index of class HyperParser
def test_HyperParser_set_index():
    # test positions in file with statements like this.
    t = """\
    foo = bar(1,
              2, 3)
    spam = ['a',
            'b', 'c']
    eggs = [
        'foo',
        'bar', 'baz']
    """
    # set_index should be able to handle 4 positions in the file.
    # position 0 should be handled.
    # positions 1, 2 and 3 should be handled.
    # positions 4 and 5 should be handled.
    # position 6 should not be handled.
    # positions 7, 9, 11 and 14 should be handled.
    # positions 10 and 12 should not be handled.
    # positions 13 and 15 should be handled.
    # position 16 should not be handled.
    # positions 17, 18 and 20 should be handled.
    # positions 19 and 21 should not be

# Generated at 2022-06-14 11:39:45.201022
# Unit test for method is_block_closer of class RoughParser
def test_RoughParser_is_block_closer():
    assert not RoughParser("").is_block_closer()
    assert not RoughParser("\n").is_block_closer()
    assert RoughParser("return\n").is_block_closer()


# Generated at 2022-06-14 11:39:55.132525
# Unit test for method find_good_parse_start of class RoughParser
def test_RoughParser_find_good_parse_start():
    parser = RoughParser("# foo\npass # spam\n")
    assert parser.find_good_parse_start() == 5

    parser = RoughParser("\n# foo\npass # spam\n")
    assert parser.find_good_parse_start() == 6

    parser = RoughParser("\n# foo\npass # spam")
    assert parser.find_good_parse_start() == 6

    parser = RoughParser("def foo(baz): pass # spam\n")
    assert parser.find_good_parse_start() == 15

    parser = RoughParser("def foo(baz):\npass # spam\n")
    assert parser.find_good_parse_start() == 16

    parser = RoughParser("def foo(baz):\npass # spam")
    assert parser.find_good_parse_start()

# Generated at 2022-06-14 11:39:58.261304
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    raise unittest.SkipTest("This has been ported to https://github.com/python/cpython/pull/1039")


# Generated at 2022-06-14 11:40:08.810427
# Unit test for constructor of class HyperParser
def test_HyperParser():
    import unittest

    class TestHyperParser(unittest.TestCase):
        def setUp(self):
            class Text:
                def __init__(self):
                    self.indent_width = 1
                    self.tabwidth = 1

            self.text = Text()
            self.text.get = lambda start, end: self.text.rawtext[
                int(float(start)) : int(float(end))
            ]


# Generated at 2022-06-14 11:40:21.412285
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    import unittest
    from idlelib.idle_test.mock_idle import Func
    from idlelib.idle_test.mock_tk import Text

    class MockTk(Mock):
        call = Func(lambda self, cmd, *args: cmd)
        get = Func(lambda self, *args: ' ')

    class MockText(Text):
        @staticmethod
        def index(s):
            return s

    class Test(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.orig_Tk = idlelib.HyperParser.Tk
            idlelib.HyperParser.Tk = MockTk
            cls.orig_text = idlelib.HyperParser.text
            idlelib.HyperParser.text = MockText


# Generated at 2022-06-14 11:40:25.718360
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    """Test HyperParser.get_surrounding_brackets method.

    The test passes if the method gives correct results for various
    scenarios. Otherwise, an AssertionError is raised.
    """
    from unittest import TestCase, main

    class Test_HyperParser_get_surrounding_brackets(TestCase):
        """Test class for the HyperParser.get_surrounding_brackets method"""

        def setUp(self):
            """Create a text box with a sample of text for testing"""
            from idlelib.idle_test.mock_idle import Func
            from tkinter import Text
            from tkinter.ttk import Scrollbar

            self.text = Text()

# Generated at 2022-06-14 11:40:43.127618
# Unit test for method is_in_string of class HyperParser
def test_HyperParser_is_in_string():
    class DummyText:
        def __init__(self, string):
            self.string = string

        def index(self, name):
            return name

        def get(self, start, end):
            return self.string[int(start) : int(end)]

        def __getitem__(self, key):
            return self.string[key]

    string = ("'''\nThis is a multi-line string.\n" "It ends here:\n'''")
    t = DummyText(string)
    parser = HyperParser(t, "3.9")
    if not parser.is_in_string():
        raise ValueError("HyperParser.is_in_string failed for a multi-line string.")
    parser = HyperParser(t, "4.0")

# Generated at 2022-06-14 11:40:53.066358
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    assert HyperParser("# abc\n", "1.0").is_in_code()
    assert HyperParser("x # abc\n", "1.0").is_in_code()
    assert HyperParser("x # abc\n", "1.1").is_in_code()
    assert HyperParser("'#'\n", "1.0").is_in_code()
    assert HyperParser("'#'\n", "1.1").is_in_code()

    assert not HyperParser("'#'\n", "1.2").is_in_code()
    assert not HyperParser("'#'#\n", "1.2").is_in_code()
    assert not HyperParser("'#'#\n", "1.3").is_in_code()


# Generated at 2022-06-14 11:40:54.356312
# Unit test for method find_good_parse_start of class RoughParser

# Generated at 2022-06-14 11:43:12.655048
# Unit test for method get_expression of class HyperParser
def test_HyperParser_get_expression():
    # TODO
    pass



# Generated at 2022-06-14 11:43:25.458227
# Unit test for method get_expression of class HyperParser

# Generated at 2022-06-14 11:43:36.191500
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    "Test HyperParser.is_in_code()"


# Generated at 2022-06-14 11:43:46.377706
# Unit test for method compute_backslash_indent of class RoughParser
def test_RoughParser_compute_backslash_indent():
    def b0(s):
        return RoughParser(s, 0, None).compute_backslash_indent()

    assert b0("a = b + \\\nfoo()\n") == 4
    assert b0("if 1: x \\\n= 2\n") == 2
    assert b0("if 1: x \\\n= 2  # hello\n") == 2
    assert b0("if 1: x \\\n= 2  # hello\\\nworld\n") == 2
    assert b0("if 1: x \\\n= 2  # hello\\\nworld\n") == 2
    assert b0("for x in range(10): print x,\\\nx**2\n") == 8

# Generated at 2022-06-14 11:43:59.873627
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    class MockText(object):
        def __init__(self, content):
            self.content = content

        def get(self, start, end):
            return self.content[self.content.index(start):self.content.index(end)]

        def index(self, string):
            return self.content.index(string)

        def __repr__(self):
            return self.content
    
    content = """\
if a:
    def f():
        pass
    """

    for index in ["1.0", "1.4", "2.4", "2.8", "3.0", "3.12", "3.13", "3.14", "3.15", "3.16"]:
        text = MockText(content)
        parser = HyperParser(text, index)

# Generated at 2022-06-14 11:44:12.141108
# Unit test for method get_base_indent_string of class RoughParser
def test_RoughParser_get_base_indent_string():
    rp = RoughParser(
        "\n\nif x: print(x)\nprint(y)", indent_width=4, tabwidth=8
    )
    assert rp.get_base_indent_string() == "    "

    rp = RoughParser(
        "\n\nif x: print(x)\n    print(y)", indent_width=4, tabwidth=8
    )
    assert rp.get_base_indent_string() == "    "

    rp = RoughParser(
        "\n\nif x:\n    print(x)\n    print(y)", indent_width=4, tabwidth=8
    )
    assert rp.get_base_indent_string() == "    "


# Generated at 2022-06-14 11:44:22.483124
# Unit test for constructor of class HyperParser
def test_HyperParser():
    # Test that we are not in a string before string, or in a comment
    # before the comment, etc.
    def test():
        global HP
        hp = HP
        hp.set_index("1.0")

# Generated at 2022-06-14 11:44:33.718360
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    import unittest
    import unittest.mock

    class MockText(object):
        __slots__ = ["indent_width", "tabwidth", "get", "index"]

        def __init__(self):
            self.indent_width = 4
            self.tabwidth = 8
            self.get = unittest.mock.Mock(return_value="")
            self.index = unittest.mock.Mock(side_effect=lambda arg: arg)

    class SyntaxError(Exception):
        pass

    class TestClass(unittest.TestCase):
        def test_nonexistent_index(self):
            hp = HyperParser(MockText(), "1.0")
            with self.assertRaises(ValueError) as ex:
                hp.set_index("1.1000")

# Generated at 2022-06-14 11:44:46.698667
# Unit test for method is_in_code of class HyperParser
def test_HyperParser_is_in_code():
    def check(text, index, expect):
        hp = HyperParser(TkTextWrapper(text, None), index)
        got = hp.is_in_code()
        success = got == expect
        if success:
            print("OK   ", end=" ")
        else:
            print("ERROR", end=" ")
        print(repr(text), "index=" + repr(index), ", expect", repr(expect), "got", repr(got))

    check('print("spam")', "1.4", False)
    check('print("spam")', "1.5", True)
    check('print("spam")', "1.6", True)
    check('print("spam")', "1.15", True)
    check('print("spam")', "1.16", True)

# Generated at 2022-06-14 11:45:00.657226
# Unit test for method get_surrounding_brackets of class HyperParser
def test_HyperParser_get_surrounding_brackets():
    class MockText(str):
        def __init__(self, s):
            str.__init__(self, s)
            self.indent_width = 4
            self.tabwidth = 8

        def __getitem__(self, index):
            if isinstance(index, str):
                return str.__getitem__(self, self.translate_index(index))
            else:
                return str.__getitem__(self, index)

        def index(self, index):
            return self.translate_index(index)

        def translate_index(self, index):
            if index == "1.0":
                return 0
            elif index == "insert":
                return len(self)
