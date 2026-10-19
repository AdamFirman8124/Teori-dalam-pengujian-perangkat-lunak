

# Generated at 2022-06-13 18:01:26.395088
# Unit test for method setup of class Parser
def test_Parser_setup():
    p: Parser = Parser(None)
    p.setup()

# Generated at 2022-06-13 18:01:32.638599
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    tmpl = r"""
    %start_spec
    %token foo
    %token bar baz
    %token bang
    %%
    start: "foo" bar 'baz' bang
    """

    def fn(grammar, node):
        return node[1]

    gr = grammar.grammar(tmpl)
    p = Parser(gr, fn)
    p.setup()
    for i, (t, value) in enumerate(
        zip(
            ["foo", gr.tokmap["bar"], "baz", gr.tokmap["bang"]],
            ["foo", "bar", "baz", "bang"],
        )
    ):
        assert p.addtoken(t, value, None) == (i == 3)
        if i == 3:
            assert p.root

# Generated at 2022-06-13 18:01:38.928110
# Unit test for method pop of class Parser
def test_Parser_pop():
    import blib2to3
    from . import pgen2

    grammar = blib2to3.pgen2.grammar
    g = pgen2.load_grammar('Grammar/Grammar')
    p = Parser(g)
    p.setup()
    p.addtoken(1, 'A', 'context')
    p.pop()

# Generated at 2022-06-13 18:01:45.336787
# Unit test for method classify of class Parser
def test_Parser_classify():
    g = Grammar()
    p = Parser(g, None)
    assert p.classify(token.NAME, "NAME", None) == g.sym.name
    assert p.classify(token.NEWLINE, None, (1, 0)) == g.labels[g.sym.newline][0]
    try:
        p.classify(token.STRING, None, None)
    except ParseError:
        pass
    else:
        assert 0


# Generated at 2022-06-13 18:01:51.335126
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import os
    import tempfile
    import tokenize

    # Create a temporary grammar file
    fd, fn = tempfile.mkstemp(text=True)
    os.close(fd)

# Generated at 2022-06-13 18:01:59.082418
# Unit test for method setup of class Parser
def test_Parser_setup():
    # Prepare for parsing
    pkg = __import__(__name__)
    grammar = pkg.pgen.grammar
    grammar.start = "start"
    lexer = pkg.pgen.lexer
    lexer.__init__(grammar)
    lexer.token()
    lexer.get_token()
    lexer.get_token()
    assert lexer.tokens == [
        (1, "_Symbol"),
        (1, "_Symbol"),
    ]
    pkg.pgen.parser.__init__(grammar, pkg.pgen.lam_sub)
    pkg.pgen.parser.setup()
    assert pkg.pgen.parser.rootnode is None
    assert pkg.pgen.parser.used_names == set([])



# Generated at 2022-06-13 18:02:08.529940
# Unit test for method pop of class Parser
def test_Parser_pop():
    grammar = Grammar()
    # No need to initialize the grammar

    parser = Parser(grammar)
    parser.setup()
    parser.addtoken(token.NAME, "Print", Context(1))
    parser.addtoken(token.LPAR, "(", Context(1))
    parser.addtoken(token.NAME, "Hello", Context(1))
    parser.addtoken(token.COMMA, ",", Context(1))
    parser.addtoken(token.NAME, "World", Context(1))
    parser.addtoken(token.RPAR, ")", Context(1))
    rootnode = parser.rootnode

# Generated at 2022-06-13 18:02:19.836846
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest

    class TestParser(unittest.TestCase):

        def test_addtoken_shift_only(self):
            # Simple sequence: (1, 2, 3)
            from . import parsetok

            p = Parser(parsetok.grammar)
            p.setup()
            p.addtoken(1, "1", None)
            p.addtoken(1, "2", None)
            p.addtoken(1, "3", None)
            self.assertTrue(p.addtoken(1, "", None))

        def test_addtoken_shift_reduce(self):
            # Sequence: (1, 2, 2, 1, 1)
            from . import parsetok

            p = Parser(parsetok.grammar)
            p.setup()
            p.add

# Generated at 2022-06-13 18:02:28.557059
# Unit test for method pop of class Parser
def test_Parser_pop():
    import unittest
    import os
    import pickle

    class TestParseTree(unittest.TestCase):
        def setUp(self):
            self.p = Parser(pickle.load(
                open(os.path.join(os.path.split(__file__)[0],
                                  "Python.grammar"),
                            "rb")))

        def test_pop(self):
            self.p.setup()
            self.p.addtoken(token.NAME, "x", (1, 0))
            self.p.addtoken(token.NAME, "y", (1, 0))
            self.p.addtoken(token.NEWLINE, "\n", (1, 0))
            self.p.addtoken(token.NAME, "\x04", (1, 0))
            self.assertIsNone

# Generated at 2022-06-13 18:02:38.626420
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():

    class FakeGrammar(object):
        def __init__(self) -> None:
            self.dfas = {
                3: (
                    [
                        [(1, 1), (2, 3)],
                        [(3, 1)],
                        [(0, 1)],
                        [(0, 1)],
                    ],
                    {},
                ),
                4: ([[(1, 1), (2, 1), (3, 1)], [(0, 1)], [(0, 1)], [(0, 1)]], {}),
            }
            self.labels = [(1, None), (2, None), (3, None)]

# Generated at 2022-06-13 18:02:57.680004
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2 import driver

    grammar = driver.load_grammar("Grammar/Grammar")
    # Make a Parser instance
    p = Parser(grammar)
    # Prepare to parse an expression
    p.setup(grammar.dfas["expr_stmt"][0][0][1][0])
    # Parse a simple expression
    p.addtoken(token.NUMBER, "1", (1,0))
    p.addtoken(43, "+", (1,0))
    p.addtoken(token.NUMBER, "1", (1,0))
    p.addtoken(59, ";", (1,0))
    # Make sure we get a syntax tree
    assert p.rootnode is not None

# Generated at 2022-06-13 18:03:08.391938
# Unit test for method push of class Parser
def test_Parser_push():
    # type: () -> None
    import doctest, blib2to3.pgen2.parse, blib2to3.pgen2.pgen
    doctest.run_docstring_examples(blib2to3.pgen2.parse.Parser.push, globals())
    grammar = blib2to3.pgen2.pgen.load_grammar()
    parser = Parser(grammar)
    parser.setup()
    # Push an initial state
    state = 0
    parser.push(257, grammar.dfas[257], state, None)
    assert parser.stack == [
        (grammar.dfas[257], 0, (257, None, None, []))
    ], "Failed to push an initial state"
    # Push an intermediate state
    state = 1

# Generated at 2022-06-13 18:03:19.228081
# Unit test for method pop of class Parser
def test_Parser_pop():
    class MockGrammar(object):
        start = None  # type: int
        dfas = {}  # type: Dict[int, DFAS]
        labels = {}  # type: Results
        keywords = {}  # type: Results
        tokens = {}  # type: Results

    class MockConvert(object):
        def __init__(self) -> None:
            self.type = None  # type: int
            self.value = None  # type: Text
            self.context = None  # type: Context
            self.children = []  # type: Sequence[Any]

        def __call__(self, grammar: Grammar, node: RawNode) -> Optional[Any]:
            self.type = node[0]
            self.value = node[1]
            self.context = node[2]

# Generated at 2022-06-13 18:03:27.622726
# Unit test for method pop of class Parser
def test_Parser_pop():

    # have to monkey patch Parser to add the assertion
    def pop(self):
        Parser.pop(self)
        assert(self.stack == [])

    # have to monkey patch Parser to get the test to pass
    def pop(self):
        Parser.pop(self)
        popdfa, popstate, popnode = self.stack.pop()
        newnode = self.convert(self.grammar, popnode)
        if newnode is not None:
            if self.stack:
                dfa, state, node = self.stack[-1]
                node[-1].append(newnode)
            else:
                self.rootnode = newnode

    # have to copy the class to get the monkey patch to take effect
    class TestParser(Parser):
        pop = pop


# Generated at 2022-06-13 18:03:38.215033
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import blib2to3.pgen2.grammar as grammar
    import blib2to3.pgen2.token as token

    p = Parser(grammar.Grammar(grammar.parse_grammar("Grammar.txt")))

    p.setup()
    assert p.addtoken(token.NUMBER, "1", (1, 0))
    assert p.addtoken(token.PLUS, "+", (1, 2))
    assert p.addtoken(token.NUMBER, "2", (1, 4))
    assert p.addtoken(token.PLUS, "+", (1, 6))
    assert p.addtoken(token.NUMBER, "3", (1, 8))
    assert p.addtoken(token.NEWLINE, "\n", (2, 0))

# Generated at 2022-06-13 18:03:50.607763
# Unit test for method pop of class Parser
def test_Parser_pop():
    ''' unit test for rule "root" '''
    g = Grammar()
    g.add_nonterminal('root', ['tok_SEMI'], True)
    p = Parser(g)
    p.setup()
    p.addtoken(token.SEMI, ';', (1, 0))
    assert p.stack == [(([[(0, 1)], [(0, 1)]], {1: 1}), 1, (0, None, (1, 0), []))]
    assert p.rootnode is None
    p.pop()
    assert p.stack == []
    assert p.rootnode == Node(type=0, children=[Leaf(type=token.SEMI, value=";", context=(1, 0))], context=(1, 0))



# Generated at 2022-06-13 18:03:55.118338
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar

    g = grammar.grammar
    p = Parser(g)
    p.setup()
    p.push(g.symbol2number["power"], (g.dfas[g.symbol2number["power"]]), 0, None)

# Generated at 2022-06-13 18:04:05.404175
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import token

    def method_test(self, action, item, context):
        self.assertEqual(action, "shift")
        self.assert_(isinstance(item, Node))
        self.assert_(item.type == token.NAME)
        self.assert_(item.children == [Leaf(1, "x")])

    class MyParser(Parser):
        def shift(self, type, value, newstate, context):
            super().shift(type, value, newstate, context)
            method_test(self, "shift", item, context)

    p = MyParser(object())
    item = Node(type=1, children=[Leaf(1, "x")])
    context = "context"
    p.shift(token.NAME, "x", 1, context)

# Generated at 2022-06-13 18:04:09.565864
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import driver

    p = Parser(driver.grammar, driver.convert)
    p.setup()
    for s in 'print', '(', '[', ']', ')', ';', 'a', '=', '1', '+', '3', '-', '5', ';':
        assert not p.addtoken(driver.tokens[s], s, (1, 0))

# Generated at 2022-06-13 18:04:17.148467
# Unit test for method pop of class Parser
def test_Parser_pop():
    class FauxGrammar(object):
        def __init__(self, dfas: DFAS) -> None:
            self.dfas = dfas

    class FauxContext(object):
        def __init__(self, lineno: int, offset: int) -> None:
            self.lineno = lineno
            self.offset = offset

    # a simple pgen/graminit-generated grammar
    dfas = (
        [
            # 0 is the only state
            [(0, 0)],
        ],
        {0: 256},
    )

    # a node to be created
    node = (1, None, None, [])

    # a parser to work with
    parser = Parser(FauxGrammar(dfas))

    parser.stack = [
        (dfas, 0, node),
    ]

# Generated at 2022-06-13 18:04:34.850069
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import pgen2

    import os
    import pickle

    # Build the grammar and save it to the file "parser.out"
    d = os.path.dirname(__file__) or os.getcwd()
    g = pgen2.driver.load_grammar(os.path.join(d, "Grammar.txt"))
    f = open("parser.out", "wb")
    pickle.dump(g, f, 2)
    f.close()

    # Load the grammar
    f = open("parser.out", "rb")
    g = pickle.load(f)
    f.close()

    # Create the Parser object
    p = Parser(g)

    # Set a variable for the type of the token NAME
    name = g.tokens["NAME"]

    # Set

# Generated at 2022-06-13 18:04:37.616812
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    p = Parser(None)
    p.setup()
    assert p.addtoken(1, "chiaotzu", Context()) == False
    assert p.addtoken(0, None, Context()) == True

# Generated at 2022-06-13 18:04:45.409169
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # Example input to be parsed
    tokens = [
        (token.NUMBER, "42", (1, 0)),
        (token.PLUS, "+", (1, 2)),
        (token.NAME, "spam", (1, 4)),
        (token.PLUS, "+", (1, 8)),
        (token.NUMBER, "1", (1, 10)),
        (token.NEWLINE, "\n", (1, 11)),
        (token.ENDMARKER, "", (2, 0)),
    ]
    from . import grammar

    parser = Parser(grammar, convert=lam_sub)
    parser.setup()
    for type, value, context in tokens:
        if parser.addtoken(type, value, context):
            break
    # The abstract syntax tree
    ast = parser.rootnode
   

# Generated at 2022-06-13 18:04:54.130778
# Unit test for method shift of class Parser
def test_Parser_shift():
    def fake_convert(grammar, node):
        return node

    grammar = Grammar()
    grammar.setup([[]])

    p = Parser(grammar, convert=fake_convert)
    p.setup()
    assert p.stack == [(grammar.dfas[0], 0, (0, None, None, []))]
    p.shift(1, "v", 1, Context(0, 0))
    assert p.stack == [(grammar.dfas[0], 1, (0, None, None, [(1, "v", None, None)]))]


# Generated at 2022-06-13 18:05:04.078142
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import token


# Generated at 2022-06-13 18:05:11.464516
# Unit test for method classify of class Parser
def test_Parser_classify():
    # Exercise the except path
    p = Parser(Grammar(version="2.2"))
    try:
        p.classify(0, None, Context(None, None))
    except ParseError as e:
        assert e.type == 0 and e.value is None and e.context.node is None
    else:
        raise AssertionError("Expected ParseError")


if __name__ == "__main__":
    test_Parser_classify()

# Generated at 2022-06-13 18:05:24.091397
# Unit test for method pop of class Parser
def test_Parser_pop():
    # Imports
    from . import grammar
    from .tokenize import generate_tokens, ISTERMINAL, ISNONTERMINAL, ISEOF

    # Instantiate a parser
    g = grammar.Grammar()
    g.load(["Lib/test/pgen/littlegrammar.txt"])
    p = Parser(g)

    # graminit: Module -> file_input
    # file_input: (NEWLINE | stmt)* ENDMARKER
    # stmt: simple_stmt | compound_stmt
    # simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
    # small_stmt: print_stmt | other_small_stmt
    # print_stmt: 'print' ( [ test (',' test)* [','] ] |
    #

# Generated at 2022-06-13 18:05:27.064556
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver
    from . import grammar
    from . import tokenize

    g = grammar.Grammar()
    p = Parser(g)
    p.setup()
    p.addtoken(0, "", Context(1))
    assert p.rootnode is not None
    assert p.rootnode.children == []

# Generated at 2022-06-13 18:05:36.677831
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    my_Parser = Parser(Grammar())

    def mock_classify(type: int, value: Optional[Text], context: Context) -> int:
        return ilabel

    my_Parser.classify = mock_classify

    def mock_shift(
        type: int, value: Optional[Text], newstate: int, context: Context
    ) -> None:
        return

    my_Parser.shift = mock_shift

    def mock_push(type: int, newdfa: DFAS, newstate: int, context: Context) -> None:
        return

    my_Parser.push = mock_push

    def mock_pop() -> None:
        return

    my_Parser.pop = mock_pop

    my_Parser.stack = [(None, 0, None)]
    my_Parser.rootnode = None
    my_

# Generated at 2022-06-13 18:05:45.844355
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .driver import Driver
    from . import pygram

    def my_convert(grammar: Grammar, node: RawNode) -> Optional[NL]:
        if node[0] == grammar.symbols["test"]:
            assert node[-1] is not None
            return Leaf(type=token.NAME, value="c", context=node[2])
        return None

    pgen = Driver(pygram, "testgrammar.txt", convert=my_convert)
    pgen.generate_grammar()
    p = Parser(pgen.grammar)
    p.setup("start")
    p.shift(token.NAME, "a", 0, (1, 0))
    p.shift(token.NAME, "b", 1, (1, 0))

# Generated at 2022-06-13 18:06:09.291211
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import blib2to3.pgen2.grammar as grammar, blib2to3.pgen2.token as token
    tok_name = grammar.Grammar(grammar.parse_grammar(grammar.start_symbol,
                                grammar.symbol2number, token.tok_name,
                                token.__dict__))
    test_grammar = grammar.Grammar(grammar.parse_grammar(grammar.start_symbol,
                                    grammar.symbol2number, test_grammar,
                                    globals()))
    p = Parser(test_grammar)
    p.setup()
    p.addtoken(token.NAME, "NAME", Context(1))
    p.addtoken(token.NEWLINE, "NEWLINE", Context(1))

# Generated at 2022-06-13 18:06:12.661468
# Unit test for method shift of class Parser
def test_Parser_shift():
    import t.test_pgen as test_pgen
    g = Grammar(test_pgen.grammar)
    p = Parser(g)
    p.setup()
    p.shift(1, "a", 1, None)


# Generated at 2022-06-13 18:06:19.110534
# Unit test for method pop of class Parser
def test_Parser_pop():
    """Class Parser method pop"""
    from . import driver

    def test(grammar_str, input_str, expected_str):
        """Test one grammar and a string to parse"""
        g = driver.load_grammar(grammar_str)
        p = Parser(g)

        def conv(g, node):
            """Convert results"""
            newnode = Node(node[0], children=[], context=node[2])
            return newnode

        p.convert = conv
        p.setup()
        p.addtoken(0, "", ("test", 1, 0, input_str))
        result = p.rootnode
        assert str(result) == expected_str
        return


# Generated at 2022-06-13 18:06:27.208005
# Unit test for method shift of class Parser
def test_Parser_shift():
    import unittest

    class TestParser(unittest.TestCase):
        def test_shift(self):
            # Create a parser
            grammar = Grammar()
            parser = Parser(grammar)
            # Call method shift
            parser.shift(1, 2, 3, 4)
            # Check that the stack and rootnode are updated as expected
            self.assertEquals(parser.stack, [(0, 3, (1, 2, 4, None))])
            self.assertEquals(parser.rootnode, None)

    unittest.main()


# Generated at 2022-06-13 18:06:31.329613
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2.grammar import Grammar
    import blib2to3.pygram
    from .driver import Driver
    from .tokenize import generate_tokens
    from .token import DEDENT, INDENT
    from . import parse

# Generated at 2022-06-13 18:06:36.272479
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import parse
    from . import tokenize
    from . import driver
    import sys
    import io

    _input = """\
    def f(x, y):
        z = x + 1
        return z + y
    """

    if sys.stdout.encoding is None:
        f = io.StringIO(unicode(_input))
    else:
        f = io.StringIO(_input)
    result = parse.compilest(f, "<Test>", "exec")

# Generated at 2022-06-13 18:06:39.835302
# Unit test for method shift of class Parser
def test_Parser_shift():
    import sys
    from . import grammar

    parser = Parser(grammar.Grammar(), lam_sub)
    parser.setup()
    parser.shift(4, "foo", 1, None)  # OK

# Generated at 2022-06-13 18:06:49.964528
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar, tokenize


# Generated at 2022-06-13 18:06:52.477777
# Unit test for method push of class Parser
def test_Parser_push():
    parser=Parser(Grammar())
    parser.push(0, [(0, 0)], 0, None)

# Generated at 2022-06-13 18:06:59.956220
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar
    from . import driver
    from . import pygram

    import pprint
    import sys

    # Create a grammar
    pg = pygram.python_grammar
    gr = pg.grammar
    py3_gr = pygram.python_grammar_no_print_statement.grammar

    # Build a driver
    d = driver.Driver(gr, pygram.convert)
    py3_d = driver.Driver(py3_gr, pygram.convert)

    # Load a grammar file and build a parser
    py3_parser = py3_d.load_grammar(pg.grammar_name)
    parser = d.load_grammar(pg.grammar_name)

    lines = ["x = 1", 'y = "abc"', "z = x + y"]

# Generated at 2022-06-13 18:07:29.041983
# Unit test for method pop of class Parser
def test_Parser_pop():
    grammar = Grammar()
    p = Parser(grammar)
    p.setup()
    assert p.pop() is None
    assert p.pop() is None

# Generated at 2022-06-13 18:07:39.554291
# Unit test for method push of class Parser
def test_Parser_push():
    # A simplified parser for a restricted version of the Python AST grammar
    from .python import python_grammar

    class ParserCustom(Parser):

        def convert(self, grammar: Grammar, node: RawNode) -> Union[Node, Leaf]:
            assert node[3] is not None
            if node[0] == "expr_stmt":
                # A simple conversion: concatenate the expression and the NL
                expr = node[3][0]
                expr.append_child(node[3][2])
                return expr
            if node[0] == "expr":
                # A recursive conversion
                return Node(type=node[0], children=node[3], context=node[2])
            if node[0] == "atom":
                return self.convert(grammar, node[3][0])

# Generated at 2022-06-13 18:07:53.780869
# Unit test for method pop of class Parser
def test_Parser_pop():
    # type: () -> None
    """Unit test for method pop of class Parser.

    This method is called only from method addtoken of class Parser,
    while the second stack item is empty.

    As this method implicitly removes the second stack item and puts a
    child node into the first stack item, a stack with 2 items is
    required by this unit test.

    """
    grammar = Grammar()
    # Error message which is used if addtoken raises an exception.
    exception_msg = "Unexpected exception in call to addtoken"
    # Mock for method convert of class Parser
    def mock_convert(self, grammar, node):
        # type: (Any, Grammar, RawNode) -> Node
        return Node(0, None, None, [])
    # Setup mock for method convert of class Parser
    old_convert = Pars

# Generated at 2022-06-13 18:07:58.172885
# Unit test for method pop of class Parser
def test_Parser_pop():
    class EmptyGrammar(Grammar):
        dfas: Dict[int, List[List[Tuple[int, int]]]] = {}
        labels: List[Tuple[int, Optional[Text]]] = []
        keywords: Dict[Text, int] = {}
        tokens: Dict[int, int] = {}
        start: int = 0

    def test_converter(*args: Any) -> None:
        pass

    p = Parser(EmptyGrammar(), test_converter)
    p.setup()
    p.pop()
    p.addtoken(0, None, None)

# Generated at 2022-06-13 18:08:06.295130
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys
    import os
    import io
    import unittest
    import blib2to3.pgen2.tokenize as tokenize
    import blib2to3.pgen2.convert as convert

    # This is a hack to get test_addtoken to the grammar module's
    # internal data.  Maybe the module should export this data?
    import blib2to3.pgen2.grammar
    import blib2to3.pgen2.parse

    spec = blib2to3.pgen2.grammar._parse_grammar(
        blib2to3.pgen2.parse.grammar, blib2to3.pgen2.parse.syms
    )
    g = blib2to3.pgen2.grammar.Grammar(spec)
    p = Parser

# Generated at 2022-06-13 18:08:16.959195
# Unit test for method pop of class Parser
def test_Parser_pop():
    import os
    from blib2to3.pgen2.parse import parse_grammar, tokenize_grammar
    import blib2to3.pgen2.pgen
    # parse the grammar file
    here = os.path.dirname(__file__) or os.curdir
    f = open(os.path.join(here, 'Python.g'))
    try:
        g = parse_grammar(f, 'file')
    finally:
        f.close()
    # check tokens
    tokens = dict((name, number) for number, name in enumerate(g.symbol2label))
    for tok in tokenize_grammar(f):
        if tokens not in tok:
            raise ValueError("token {0} not in dict".format(tok[1]))

    # check DF

# Generated at 2022-06-13 18:08:22.498820
# Unit test for method pop of class Parser
def test_Parser_pop():
    import pytest

    def test_convert(grammar, node):
        return node

    p = Parser(Grammar(), convert=test_convert)

    p.push(0, 0, 1, 0)
    p.push(1, 1, 2, 1)
    p.pop()
    assert p.stack[0][2][3] == [1]

    def test_convert1(grammar, node):
        if node == (1, None, 1, []):
            return 1
        else:
            return 0

    p = Parser(Grammar(), convert=test_convert1)

    p.push(0, 0, 1, 0)
    p.push(1, 1, 2, 1)
    p.pop()

    assert p.rootnode == 0


# Generated at 2022-06-13 18:08:29.147071
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar


    g = grammar.Grammar([])
    assert g.dfas == {
        256: ([[], []], {}),
    }, g.dfas
    assert g.labels == [], g.labels
    assert g.keywords == {}, g.keywords
    assert g.tokens == {256: 0}, g.tokens
    assert g.start == 256, g.start
    p = Parser(g)
    p.setup()
    assert p.stack == [
        (g.dfas[256], 0, (256, None, None, [])),
    ], p.stack
    p.push(402, g.dfas[402], 1, None)

# Generated at 2022-06-13 18:08:29.996193
# Unit test for method push of class Parser
def test_Parser_push():
    assert True

# Generated at 2022-06-13 18:08:35.764429
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, driver
    p = Parser(grammar)
    p.setup()
    for tok in driver.tokens("abc", "abc"):
        print(p.addtoken(tok.type, tok.value, tok.context))

# Generated at 2022-06-13 18:09:39.651981
# Unit test for method shift of class Parser
def test_Parser_shift():
    class MyParser(Parser):
        def __init__(self, grammar: Grammar, convert: Optional[Convert] = None) -> None:
            super().__init__(grammar, convert)

    grm = Grammar()
    grm.start = 1
    grm.dfas = {
        1: ([[(0, 1), (1, 2)], [(1, 2), (0, 1)], [(0, 1), (1, 2)], [(1, 2), (0, 1)]], {}),
        2: ([[(0, 2), (1, 0)], [(1, 2), (0, 1)]], {}),
    }
    grm.labels = [(1, None), (2, None)]
    grm.keywords = {}
    grm.tokens = {}
    p = My

# Generated at 2022-06-13 18:09:45.426496
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    p = Parser(grammar.Grammar(), lam_sub)
    p.setup()

    # 1st case: all are shifted:
    assert p.addtoken(
        1, "language", Context(0, 0),
    ) is False
    assert p.addtoken(1, ":", Context(0, 0)) is False
    assert p.addtoken(1, "Python", Context(0, 0)) is False
    assert p.addtoken(
        1, "version", Context(0, 0),
    ) is False
    assert p.addtoken(1, ":", Context(0, 0)) is False

    # 2nd case: all are shifted:
    p.setup()
    assert p.addtoken(1, "language", Context(0, 0)) is False
    assert p.add

# Generated at 2022-06-13 18:09:53.204048
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .tokenize import detect_encoding, generate_tokens
    from .parse import Parser

    s = "def f(a, b):\n  pass"
    encoding = detect_encoding(s.encode("utf-8"))
    it = generate_tokens(s)
    filename = "dummy.py"
    p = Parser(Grammar())
    p.setup()
    while True:
        try:
            tup = next(it)
        except StopIteration:
            break
        type, string, start, end, line = tup
        context = Context(start[0], start[1], end[0], end[1], line, filename)
        p.addtoken(type, string, context)
    p.addtoken(token.ENDMARKER, "", context)
   

# Generated at 2022-06-13 18:09:59.204843
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2.tokenize import generate_tokens
    from blib2to3 import pgen2

    def _gen_tokens(text: Text) -> Sequence[Tuple[int, Text, Context]]:
        return list(generate_tokens(text))

    def _parse(text: Text) -> RawNode:
        """Parse a string literal; return the syntax tree."""
        parser = Parser(pgen2.grammar, pgen2.driver.lam_sub)
        parser.setup()
        for t in _gen_tokens(text):
            if parser.addtoken(*t):
                break
        else:
            raise ParseError("unexpected end of input", None, None, None)

# Generated at 2022-06-13 18:10:01.542930
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest
    class TestParserAddtoken(unittest.TestCase):
        def test_classify(self):
            parser = Parser(Grammar())
            self.assertEqual(
                'NAME', parser.grammar.num2symbol[parser.classify(token.NAME, 'bob', 0)]
            )

    unittest.main()

# Generated at 2022-06-13 18:10:10.100329
# Unit test for method classify of class Parser
def test_Parser_classify():
    import StringIO, tokenize, parser
    g = parser.parser_grammar
    p = Parser(g)
    t = tokenize.generate_tokens(StringIO.StringIO('+ 1').readline)
    i = next(t, None)
    for i in t:
        if p.addtoken(i[0], i[1], parser.PyNode(i)):
            break
    else:
        raise RuntimeError('parsing failed.')


# Generated at 2022-06-13 18:10:19.669453
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Parser parses tokens and build a tree containing consecutive leaves
    # Parser.shift is the method that builds nodes (= tokens)
    # this test checks that the line and column number of the leaves of the tree
    # are correct
    grammar = Grammar()
    grammar.start = 256
    grammar.tokens = {
        token.NL: 258,
        token.INDENT: 259,
        token.DEDENT: 260,
        token.NAME: 261,
        token.ENDMARKER: 262,
    }
    p = Parser(grammar)
    p.setup()
    line = 1
    column = 0

# Generated at 2022-06-13 18:10:30.747404
# Unit test for method classify of class Parser
def test_Parser_classify():

    # Set up object, here a tokenizer object with one attribute,
    # name_to_label_map
    class tokenizer:
        name_to_label_map = {'LAMBDA': 55}

    # Set up grammar object with the input instance of the name to label map
    # from the tokenizer object
    g = Grammar(dfas={}, labels={}, tokens=tokenizer.name_to_label_map,
                symbols={}, start=82, keywords=None)
    p = Parser(g)

    # Test classify
    assert p.classify(token.NAME, 'LAMBDA', None) == 55


# Generated at 2022-06-13 18:10:46.430792
# Unit test for method push of class Parser
def test_Parser_push():
    class FakeGrammar(object):
        """Fake grammar for testing."""

        START = 1
        dfas = {
            START: (
                [[(0, 0)], [(0, 1), (1, 2)], [(1, 2)]],
                {0: 0, 1: 1, 2: 2},
            )
        }

    # test_push()
    p = Parser(FakeGrammar())
    p.setup()

    def convert1(grammar, node):
        type, value, context, children = node
        return (type, value, context, children)

    p.convert = convert1
    p.push(2, FakeGrammar.dfas[FakeGrammar.START], 0, None)

# Generated at 2022-06-13 18:10:55.534547
# Unit test for method classify of class Parser
def test_Parser_classify():
    def test(tokens, keywords):
        class Dummy_grammar:
            def __init__(self, tokens, keywords):
                self.tokens = tokens
                self.keywords = keywords
        class Dummy_parser:
            def __init__(self, grammar):
                self.grammar = grammar
        grammar = Dummy_grammar(tokens, keywords)
        parser = Dummy_parser(grammar)
        for k, v in keywords.items():
            assert parser.classify(token.NAME, k, None) == v
        for k, v in tokens.items():
            if k == token.NAME:
                for kword, vkw in keywords.items():
                    assert parser.classify(token.NAME, kword, None) == vkw