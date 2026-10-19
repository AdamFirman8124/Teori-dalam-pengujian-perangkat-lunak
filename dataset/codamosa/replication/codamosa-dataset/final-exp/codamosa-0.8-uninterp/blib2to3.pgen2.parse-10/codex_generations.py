

# Generated at 2022-06-13 18:01:44.541457
# Unit test for method classify of class Parser
def test_Parser_classify():
    test_grammar = Grammar()
    test_grammar.tokens = {token.NAME: 0, token.NUMBER: 1}
    test_grammar.keywords = {"def": 2, "clss": 3}
    test_parser = Parser(test_grammar)
    test_parser.classify(
        token.NAME,
        "test",
        Context(previous_line="", last_line="test", last_offset=0),
    )
    assert test_parser.used_names == set("test")
    test_parser.classify(
        token.NAME,
        "def",
        Context(previous_line="", last_line="def", last_offset=0),
    )
    assert test_parser.used_names == set("def")

# Generated at 2022-06-13 18:01:56.850894
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """This is a test for the Parser.addtoken method."""
    import unittest


# Generated at 2022-06-13 18:02:02.562655
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # Test with a simple grammar
    import blib2to3.pgen2.pgen
    from . import driver

    g = blib2to3.pgen2.pgen.generate_grammar()
    p = Parser(g)
    p.setup()
    for t in driver.tokenize_file(__file__):
        if p.addtoken(t.type, t.string, t.context):
            break
    assert p.rootnode is not None
    #print p.rootnode

# Generated at 2022-06-13 18:02:15.789006
# Unit test for method shift of class Parser
def test_Parser_shift():
    # A Mocks
    class MockGrammar:
        def __init__(self):
            self.labels = [(0, None), (1, None)]
            pass

    mock_convert = lam_sub
    mock_type = 1
    mock_value = "mock_value"
    mock_context = (1,2)

    # Arrange
    grammar = MockGrammar()
    parser = Parser(grammar, mock_convert)
    parser.setup()

    # Act
    parser.shift(mock_type, mock_value, 1, mock_context)

    # Assert
    assert parser.stack == [(None, 1, (None, None, None, [None]))]


# Generated at 2022-06-13 18:02:26.782713
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, token, driver
    from . import pytree
    from .pygram import python_grammar, python_grammar_no_print_statement
    from .pgen2.parse import parse_grammar
    from .pgen2.tokenize import generate_tokens, untokenize, TokenError

    def get_grammar(version: Optional[Sequence[int]] = None) -> Grammar:
        # type: (Optional[Sequence[int]]) -> Grammar
        if version is None:
            return grammar.grammar
        return parse_grammar(
            python_grammar_no_print_statement if version <= (3,) else python_grammar,
            "test_Parser_addtoken.py",
            version,
        )


# Generated at 2022-06-13 18:02:38.177402
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # unit test demonstrating that addtoken of class Parser handles a
    # name token correctly by shifting it and returning False
    grammar = Grammar()
    parser = Parser(grammar)
    parser.setup(3)
    # Symbol 3 is a production of type NAME
    assert 3 in grammar.symbol2number
    assert grammar.symbol2number[3] == 3
    assert 3 == grammar.name
    # Token token.NAME is defined in the grammar
    assert grammar.symbol2label[3] == grammar.tokens[token.NAME]
    # Token token.NAME has label 0
    assert grammar.tokens[token.NAME] == 0
    # Token token.NAME is not a reserved keyword
    assert token.NAME not in grammar.keywords
    assert grammar.keywords.get(token.NAME) is None

# Generated at 2022-06-13 18:02:48.168157
# Unit test for method pop of class Parser
def test_Parser_pop():
    import sys
    import unittest
    from blib2to3.pgen2.parse import ParseError, Parser
    from blib2to3.pytree import get_node
    from .tokenize import generate_tokens
    from .parse import driver

    class Test(unittest.TestCase):
        def setUp(self):
            grammar = driver.load_grammar(sys.stdin)
            self.parser = Parser(grammar)
            self.parser.setup()

        def test_example(self):
            for ttype, tvalue, tstart, tend, tline in generate_tokens(
                "a + b"
            ):
                if self.parser.addtoken(ttype, tvalue, (tstart, tend)):
                    break
            root = self.parser.rootnode


# Generated at 2022-06-13 18:02:58.067296
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2 import driver

    def test(input: Sequence[Tuple[int, Any, Context]]) -> None:
        g = driver.load_grammar("Grammar/Grammar")
        p = Parser(g)
        for type, value, context in input:
            label = p.classify(type, value, context)
            if label not in g.labels:
                raise AssertionError("bad label: %r" % label)
            t, v = g.labels[label]
            if (t, v) != (type, value):
                raise AssertionError("bad label %r for (%r, %r)" % (label, type, value))


# Generated at 2022-06-13 18:03:00.019024
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    f = Parser(Grammar())
    assert f.addtoken(1, None, Context(None, None))

# Generated at 2022-06-13 18:03:05.384583
# Unit test for method shift of class Parser
def test_Parser_shift():
    grammar = Grammar()
    p = Parser(grammar)
    p._setup= lambda: None
    p.stack = [ (1, 0, None) ]
    p.convert = lambda x, y: None
    p.shift(1, 2, 3, 4)
    assert p.stack == [(1, 3, None)]

# Generated at 2022-06-13 18:03:21.135971
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar
    import os
    import sys

    def parse(s: Text, convert: Optional[Convert] = None, start: Optional[int] = None):
        return Parser(grammar.Grammar(g), convert=convert).parse(s, start=start)

    import unittest

    class ParserTest(unittest.TestCase):
        def test_addtoken(self):
            self.assertEqual(parse(""), None)
            self.assertEqual(parse("a"), "a")
            self.assertEqual(parse("a b"), "(a b)")
            self.assertEqual(parse("a b c"), "((a b) c)")
            self.assertEqual(parse("a b c d"), "(((a b) c) d)")


# Generated at 2022-06-13 18:03:27.201987
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver, grammar
    g = grammar.Grammar()
    p = Parser(g)
    p.setup()
    p.addtoken(token.NAME, "x", driver.FileInput("").context())
    assert p.rootnode[0] == "x"

# Generated at 2022-06-13 18:03:38.038968
# Unit test for method push of class Parser
def test_Parser_push():
    from blib2to3.pgen2.pgen import generate_grammar, write_grammar
    from blib2to3.pgen2.tokenize import tokenize

    grammar = generate_grammar()
    write_grammar(grammar, "/home/user/PycharmProjects/blib2to3/blib2to3/pgen2/Python.gram")
    parser = Parser(grammar)
    parser.setup()

    f = open("/home/user/PycharmProjects/blib2to3/blib2to3/tests/data/test_grammar.py")
    tokens = tokenize(f.readline)
    for t in tokens:
        parser.addtoken(t.type, t.string, t.start)

# Generated at 2022-06-13 18:03:50.379505
# Unit test for method pop of class Parser
def test_Parser_pop():
    import blib2to3.pytree
    import blib2to3.pgen2.pgen
    import blib2to3.pgen2.driver
    import blib2to3.pgen2.parse
    from .token import NAME
    from blib2to3.pgen2.grammar import Grammar
    pgen = blib2to3.pgen2.pgen.Pgen()
    grammar = pgen.load_grammar(blib2to3.pgen2.parse.__file__)
    parser = blib2to3.pgen2.parse.Parser(grammar, blib2to3.pytree.convert)
    parser.setup()
    parser.addtoken(NAME, 'test', None)
    parser.addtoken(0, '', None)
    parser.pop()

# Generated at 2022-06-13 18:03:59.878056
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Concrete syntax tree node
    leaf = (token.NAME, "spam", (1, 0), None)
    # Define a dummy grammar
    G = Grammar()
    G.dfas["name"] = [[(1, 0)], [(0, 1)]]
    G.dfas["spam"] = [[(0, 0)], None]
    G.labels = [("name", 0), ("name", 1)]
    G.tokens = {"name": 0}
    # Define a dummy conversion function
    def cf(G, node):
        assert isinstance(node, Leaf)
        assert node == leaf
        return None
    # Define a parser instance
    p = Parser(G, cf)
    # Create a stack entry
    node = (token.NAME, None, None, [])

# Generated at 2022-06-13 18:04:00.843941
# Unit test for method pop of class Parser
def test_Parser_pop():
    p = Parser()



# Generated at 2022-06-13 18:04:05.232090
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    g = grammar.load_grammar("Grammar/Grammar")
    p = Parser(g)
    p.setup()
    p.addtoken(0, "print", None)
    p.addtoken(1, "x", None)
    p.addtoken(4, None, None)
    assert p.rootnode.leaves() == ["print", "x", ";"]

# Generated at 2022-06-13 18:04:13.410694
# Unit test for method pop of class Parser

# Generated at 2022-06-13 18:04:22.330671
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import blib2to3.pgen2.token
    import blib2to3.pgen2.driver
    driver = blib2to3.pgen2.driver.Driver(convert=lam_sub, logger=None)
    g = driver.load_grammar('grammar-ng')
    p = Parser(g)
    p.setup()
    assert p.addtoken(blib2to3.pgen2.token.NAME, 'foo', None)
    assert p.addtoken(blib2to3.pgen2.token.NEWLINE, '', None)
    try:
        p.addtoken(blib2to3.pgen2.token.NAME, 'bar', None)
    except ParseError:
        pass
    else:
        assert 0, "ParseError not raised"
   

# Generated at 2022-06-13 18:04:29.655405
# Unit test for method classify of class Parser
def test_Parser_classify():
    print("Testing Parser_classify")
    p = Parser(Grammar(token, None))
    # test 1: classify integer
    ex = expect = token.NUMBER
    res = p.classify(token.NUMBER, "13", None)
    compare(ex, expect, res)
    # test 2: classify if keyword
    ex = expect = token.NAME
    res = p.classify(token.NAME, "if", None)
    compare(ex, expect, res)
    # test 3: classify for keyword
    ex = expect = token.NAME
    res = p.classify(token.NAME, "for", None)
    compare(ex, expect, res)



# Generated at 2022-06-13 18:04:53.152458
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2.parse import tokenize
    from blib2to3.pgen2.grammar import Grammar

    grammar = Grammar(r"test.txt", "file_input")
    parser = Parser(grammar, None)
    source = r"""
a = 1 + 2 + 3
"""
    parser.setup()
    for typ, value, context in tokenize.generate_tokens(source.splitlines(True)):
        try:
            if parser.addtoken(typ, value, context):
                break
        except ParseError:
            break
    assert parser.rootnode


# Generated at 2022-06-13 18:04:57.617672
# Unit test for method pop of class Parser
def test_Parser_pop():
    node = [1]

    # Test normal operation
    parser = Parser(None)
    parser.stack = [('dfa', 'state', node)]
    parser.pop()

    # Test when stack is empty
    parser.stack = []
    parser.pop()

# Generated at 2022-06-13 18:05:06.127593
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class FooBar:
        def __init__(self, parent) -> None:
            self.parent = parent
    class Context:
        def __init__(self, parent) -> None:
            self.parent = parent

# Generated at 2022-06-13 18:05:08.427793
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar

    g = grammar.grammar
    p = Parser(g)
    p.setup()

# Generated at 2022-06-13 18:05:16.792576
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Test with empty grammar.
    p = Parser(Grammar(b''))
    try:
        p.shift(0,1,2,None)
    except AttributeError:
        pass
    else:
        assert False
    # Test with a regular token.
    from . import token, symbol
    from .pygram import python_symbols as syms
    from blib2to3 import pygram
    pygr = pygram.python_grammar
    p = Parser(pygr)
    p.setup()
    # Test if an exception is raised.
    try:
        p.shift(1,1,1,None)
    except IndexError:
        pass
    else:
        assert False
    # Test if the token is shifted.
    p.addtoken(token.NAME, 'test', None)

# Generated at 2022-06-13 18:05:20.240727
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # type: () -> None
    import doctest
    import blib2to3.pgen2.driver

    doctest.testmod(blib2to3.pgen2.driver)
    doctest.testmod()

# Generated at 2022-06-13 18:05:31.336479
# Unit test for method shift of class Parser

# Generated at 2022-06-13 18:05:34.002765
# Unit test for method shift of class Parser
def test_Parser_shift():
    import blib2to3.pgen2.parse as parse
    g = parse.load_grammar("Grammar/Grammar")
    p = parse.Parser(g)
    p.setup()
    p.addtoken(1, "foo", (0, 0))
    # should not raise
    print("test_Parser_shift: ok")

test_Parser_shift()

# Generated at 2022-06-13 18:05:45.279241
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    pygram = grammar.Grammar()  # type: ignore
    pygram.parse_grammar(pygram.tokenizer.tokenize_grammar())
    p = Parser(pygram)
    p.setup()
    tokenize = pygram.tokenizer.tokenize_partial

    t, v, c = tokenize("if")
    p.addtoken(t, v, c)
    t, v, c = tokenize("if")
    p.addtoken(t, v, c)

    t, v, c = tokenize("0")
    p.addtoken(t, v, c)
    t, v, c = tokenize("0")
    p.addtoken(t, v, c)
    t, v, c = tokenize("0")

# Generated at 2022-06-13 18:05:53.910060
# Unit test for method pop of class Parser
def test_Parser_pop():
    g = Grammar
    # Test for empty stack; expect self.rootnode to be changed
    parser = Parser(Grammar)
    parser.stack = []
    popnode = (9, None, None, [])
    parser.pop()
    assert parser.rootnode == popnode
    # Test for non-empty stack; expect node[-1] to be changed
    parser = Parser(Grammar)
    node = (9, None, None, [])
    dfa = [[]]
    parser.stack = [(dfa, 0, node)]
    parser.pop()
    assert parser.rootnode is None

# Generated at 2022-06-13 18:06:46.771511
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, parse, driver
    if not hasattr(grammar, 'Grammar'):
        import sys
        print("test_Parser_addtoken skipped; no pgen", file=sys.stderr)
        return

    import unittest
    import io

    class TestParser(unittest.TestCase):
        def test_addtoken(self):
            g = grammar.Grammar()
            # p = parser.Parser(g)
            p = Parser(g)

            s = "x = 0"
            t = driver.Driver(g, convert=parse.convert).tokenize(s)

            p.setup()
            for type, value, context in t:
                self.assertFalse(p.addtoken(type, value, context))

# Generated at 2022-06-13 18:06:54.466431
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar
    _, t = grammar.parse_grammar("Grammar.txt")
    p = Parser(t)
    p.addtoken(3, "int", None)
    p.addtoken(4, "id", None)
    p.addtoken(6, "=", None)
    p.addtoken(5, "0", None)
    p.addtoken(7, ";", None)

# Generated at 2022-06-13 18:07:03.697206
# Unit test for method push of class Parser
def test_Parser_push():
    # The following test used to fail before commit a9082d5923a7
    # "Fix function push of module pgen2.parser"
    from .driver import Driver
    from .pgen import generate_grammar
    import sys
    src = open('../../Grammar/Grammar').read()
    drv = Driver(src.splitlines(), sys.stdout, True)
    drv.pgen()
    grm = generate_grammar('../../Grammar/Grammar')
    p = Parser(grm)
    p.setup()
    p.addtoken(0, 'tim2', (1, 2))
    p.addtoken(0, ':', (1, 2))
    p.addtoken(0, 'tim2', (1, 2))

# Generated at 2022-06-13 18:07:09.961322
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """Unit test for method addtoken of class Parser."""
    from . import driver
    from . import token

    grammar = driver.load_grammar("python2")
    p = Parser(grammar)
    p.setup()
    driver.parse_tokens("foo()", p, tokenize=True)
    assert p.rootnode.children == [
        Node(type=syms.simple_stmt, children=[Leaf(1, "foo"), Leaf(12, "("), Leaf(13, ")")]),
        Leaf(4, "\n"),
    ]

# Generated at 2022-06-13 18:07:18.555561
# Unit test for method pop of class Parser
def test_Parser_pop():
    import unittest
    import pgen2.driver

    # First make sure we clean up the test Parser class:
    Parser.__dict__['pop'].__func__.__dict__.clear()

    class TestParser(Parser):
        pass
    import pgen2.pgen
    g = pgen2.pgen.grammar
    tp = TestParser(g)

    # Make sure we can't define a class method with the same name
    # as a class method of the same instance:
    def test_instance():
        class TestParser():
            def pop():
                pass
    self.assertRaises(TypeError, test_instance)


# Generated at 2022-06-13 18:07:26.017165
# Unit test for method setup of class Parser
def test_Parser_setup():
    from .grammar import Grammar
    # Test that setup() resets the stack correctly
    grammar = Grammar()
    parser = Parser(grammar)
    parser.setup()
    # Make sure that stack gets reset
    assert parser.stack == [(grammar.dfas[grammar.start], 0, (grammar.start, None, None, []))]

# Generated at 2022-06-13 18:07:39.205992
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import pytest
    from .tokenizer import generate_tokens, untokenize
    from . import grammar

    _grammar = grammar.grammar

    # Test Parser.addtoken() with a small self-contained test

# Generated at 2022-06-13 18:07:53.358856
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys
    import io
    from . import driver

    # For testing, <string> is the same as <file>

# Generated at 2022-06-13 18:07:54.097629
# Unit test for method setup of class Parser
def test_Parser_setup():
    pass


# Generated at 2022-06-13 18:07:58.926110
# Unit test for method setup of class Parser
def test_Parser_setup():
    grammar = Grammar(grammar_file="Python.grammar")
    p = Parser(grammar)
    p.setup()
    assert p.stack == [(grammar.dfas[grammar.start], 0, [(grammar.start, None, None, [])])]
    assert p.rootnode is None
    assert p.used_names == set()



# Generated at 2022-06-13 18:09:19.942055
# Unit test for method classify of class Parser
def test_Parser_classify():
    class MockGrammar(Grammar):
        def __init__(self) -> None:
            super().__init__([])
            self.tokens = {token.NAME: 0, token.NUMBER: 1}
            self.keywords = {'elif': 2}

    grammar = MockGrammar()
    parser = Parser(grammar)
    assert parser.classify(token.NAME, "a", None) == 0
    assert parser.classify(token.NUMBER, "1", None) == 1
    assert parser.classify(token.NAME, "elif", None) == 2
    try:
        parser.classify(token.STRING, "a", None)
    except ParseError as e:
        assert e.type == token.STRING
        assert e.value == "a"
       

# Generated at 2022-06-13 18:09:24.568139
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pytree import Leaf
    parser = Parser(None, None)
    parser.shift(1, "hi", 6, (1, 2))
    assert parser.stack[0][2][3] == [Leaf(1, "hi", (1, 2))]


# Generated at 2022-06-13 18:09:38.192449
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    gram = grammar.Grammar("Grammar/Grammar")
    parser = Parser(gram)

    assert parser.classify(token.NAME, "test", None) == gram.labels.by_name["test"]

    try:
        parser.classify(token.NAME, "test2", None)
        assert False, "should raise an exception"
    except ParseError as pe:
        assert pe.value == "test2"
        assert pe.msg == "bad token"
        assert pe.type == token.NAME

    #
    # Test that classify returns symbol if appropriate
    #
    parser.setup()

    assert parser.classify(token.NAME, "test", None) == gram.labels.by_name["test"]

# Generated at 2022-06-13 18:09:41.518687
# Unit test for method setup of class Parser
def test_Parser_setup():
    import blib2to3.pgen2.grammar
    parser = Parser(blib2to3.pgen2.grammar.Grammar())
    parser.setup()



# Generated at 2022-06-13 18:09:47.131865
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    gram = grammar.Grammar()
    p = Parser(gram)
    p.setup()
    p.addtoken(token.NAME, "x", None)
    try:
        p.addtoken(token.NAME, "EOF", None)
        assert False  # pragma: no cover
    except ParseError:
        pass



# Generated at 2022-06-13 18:09:51.125059
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    g = grammar.grammar
    p = Parser(g)
    p.setup()
    assert p.addtoken(token.STRING, '"foo"', (1, 1))
    assert p.addtoken(token.COMMA, ',', (1, 5))
    assert p.addtoken(token.STRING, '"bar"', (1, 6))

# Generated at 2022-06-13 18:09:57.453063
# Unit test for method pop of class Parser
def test_Parser_pop():
    print("test_Parser_pop running...")
    p = Parser()
    # The correct behavior of the method is tested by the unit test
    # for method addtoken. This test case exercises the 'else' block
    # in the method body which sets self.rootnode.
    p.stack = []
    p.rootnode = None
    assert p.rootnode is None
    p.pop()
    assert p.rootnode is not None
    print("...test_Parser_pop finished")



# Generated at 2022-06-13 18:10:03.536617
# Unit test for method push of class Parser
def test_Parser_push():
    class SillyGrammar(object):
        dfas: Dict[int, DFAS] = {}
    sg = SillyGrammar()
    p = Parser(sg, None)
    p.push(
        "test_type",
        [[(0, 0)]],
        1,
        Context(None, 100, 200),
    )
    assert p.stack[-1] == (
        [[(0, 0)]],
        1,
        (
            "test_type",
            None,
            Context(None, 100, 200),
            [],
        ),
    )

# Generated at 2022-06-13 18:10:13.456765
# Unit test for method shift of class Parser
def test_Parser_shift():
    import blib2to3.pgen2.token
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pytree import Leaf, Parent, Mod

    def lam_sub(grammar, node):
        assert node[3] is None
        return Leaf(value=node[1], type=node[0], context=node[2])

    import os
    import sys

    # Locate the grammar
    dirname = os.path.dirname(__file__)
    py_grammar = os.path.join(dirname, 'py.g4' )
    assert os.path.exists(py_grammar)

    # Create a parser
    grammar = Grammar(open(py_grammar))
    parser = Parser(grammar, lam_sub)

    # Test

# Generated at 2022-06-13 18:10:22.824641
# Unit test for method push of class Parser
def test_Parser_push():
    from .pgen2.grammar import Grammar
    from .pgen2.parse import ParseError
    import cStringIO
    import pprint
    import sys
    import unittest

    class PushTest(unittest.TestCase):

        def test_all(self):
            grammar = Grammar("""
            s: a 'b'
              | c
            a: 'a'
            c: 'c'
            """)

            class Parser(Parser):

                def classify(self, token):
                    return token

            parser = Parser(grammar)

            parser.setup()