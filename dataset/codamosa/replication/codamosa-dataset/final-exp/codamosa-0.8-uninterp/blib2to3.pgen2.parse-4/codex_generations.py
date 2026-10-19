

# Generated at 2022-06-13 18:01:39.550361
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar

    g = grammar.Grammar(
        grammar.start, grammar.dfas, grammar.labels, {}
    )  # type: ignore

    p = Parser(g)
    p.setup()
    p.pop()

# Generated at 2022-06-13 18:01:48.817323
# Unit test for method pop of class Parser
def test_Parser_pop():
    grammar = Grammar(
        "grammar.txt",
        convert=blib2to3.pgen2.convert,
        logger=blib2to3.pgen2.logger,
        driver=blib2to3.pgen2.driver,
        start_symbol_type=256,
    )
    parser = Parser(grammar)

    state = 0
    node = (type, None, None, [])
    dfa = ([(0,0)],0)
    popdfa = ([(0,0)],0)
    popnode = (257,str(257),None,[])
    stackentry = (dfa, state, node)

    # Test that popnode is indeed appended to node when stack is not empty.
    parser.stack = [stackentry]
    parser._Parser__pop

# Generated at 2022-06-13 18:01:58.469890
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2.tokenize import tokenize_lines
    from . import grammar
    from .convert import pytree

    # The If test in pgen2/convert.py -- we don't care about the
    # string representation of the tree.
    source = """\
if a:
    x
elif b:
    y
else:
    z"""

    # Generate a grammar from a string
    lines = [line + "\n" for line in source.split("\n")]
    tokens = tokenize_lines(lines, convert_charrefs=False)
    g = grammar.Grammar()
    g.parse(lines, tokens)

    # Instantiate the converter and configure the parser
    p = Parser(g, pytree)
    p.setup()

    # Generate input tokens

# Generated at 2022-06-13 18:02:05.367750
# Unit test for method classify of class Parser
def test_Parser_classify():
    import re
    from blib2to3.pgen2.parse import load_grammar
    grammar = load_grammar("blib2to3/Grammar.txt")
    parser = Parser(grammar)
    labels = parser.grammar.labels  # index i => (tok_or_sym, value)
    tokmap = parser.grammar.tokens
    # Test tokens
    for type, text in token.tok_name.items():
        if type not in (token.ERRORTOKEN, token.N_TOKENS):
            assert parser.classify(type, text, None) == tokmap[type]
    # Test symbols
    for i in range(len(labels)):
        t, v = labels[i]

# Generated at 2022-06-13 18:02:18.286053
# Unit test for method shift of class Parser
def test_Parser_shift():
    grammar = Grammar()
    p = Parser(grammar)
    p.setup()

    t = token.NAME
    v = 'test1'
    c = Context()
    ilabel = grammar.tokens.get(t)
    assert ilabel == 1

    dfa = [
        [(2, 3)],
        [(2, 4)],
        [(0, 2)],
        [(0, 3)],
        [(0, 4)],
    ]
    state = 0
    newstate = 3
    n = Node(type=t, value=v, context=c, children=[])

    p.stack.append((dfa, state, n))
    p.shift(t, v, newstate, c)
    assert p.stack == [(dfa, newstate, n)]


# Generated at 2022-06-13 18:02:24.161647
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import itertools

    def unit_test_Parser():
        try:
            p = Parser(Grammar)
            p.setup()
            for tup in itertools.permutations([1, 2, 3]):
                for t in tup:
                    p.addtoken(t, None, None)
        except ParseError:
            pass

    unit_test_Parser()



# Generated at 2022-06-13 18:02:29.389353
# Unit test for method pop of class Parser
def test_Parser_pop():
    grammar = Grammar()
    p = Parser(grammar)
    assert p.rootnode is None
    p.setup()
    p.pop()
    assert p.rootnode is not None


# Generated at 2022-06-13 18:02:40.137745
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    def parse(parser: Parser) -> Any:
        parser.addtoken(token.PLUS, "+", (1, 0))
        parser.addtoken(token.NAME, "x", (1, 1))
        parser.addtoken(token.NUMBER, "1", (1, 2))
        return parser.rootnode[2][1]
    #
    grammar = Grammar()
    grammar.start = 256
    grammar.keywords = {}
    grammar.tokens = {
        token.PLUS: 257,
        token.NUMBER: 258,
        token.NAME: 259,
    }
    tokens: List[int] = list(grammar.tokens.values())
    labels: Dict[int, Text] = {257: "+", 258: "NUMBER", 259: "NAME"}
    grammar.labels

# Generated at 2022-06-13 18:02:48.263024
# Unit test for method pop of class Parser
def test_Parser_pop():
    # First create a test grammar with a structure similar to the
    # grammar used by the blib2to3.pgen2.driver.Driver class
    #
    # See also:
    # http://docs.python.org/reference/grammar.html.
    #
    # The following grammar has the following EBNF-like definition:
    #
    #    start: expr
    #    expr:
    #         | atom
    #         | ( '+' expr )
    #         | ( '-' expr )
    #         | ( '-' expr ) '+' expr
    #         | expr '+' ( '-' expr )
    #    atom:
    #         | NAME
    #         | NUMBER
    #         | '(' expr
    #
    from blib2to3.pgen2 import token

# Generated at 2022-06-13 18:02:58.103083
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import driver

    class UnexpectedToken(Exception):
        pass

    class SlowParser(Parser):
        def classify(self, type, value, context):
            if type == token.NAME and value == "X":
                raise UnexpectedToken()
            return Parser.classify(self, type, value, context)

    grammar = driver.load_grammar("Grammar/Grammar", convert=lam_sub)
    parser = SlowParser(grammar)

    def parse(text, expected_error=None):
        parser.setup()
        driver.parse_string(
            text, parser=parser, convert=lam_sub, report_error=False
        )

# Generated at 2022-06-13 18:03:15.479103
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class MockGrammar(object):
        dfas: Dict[int, DFAS] = {}
        labels = {}
        tokens = {"foo": 42}
        keywords = {}

    mock_grammar = MockGrammar()

    parser = Parser(mock_grammar)

    class MockContext(object):
        def __init__(self, text: Optional[str] = None) -> None:
            self.text = text

    context = MockContext("mock context")

    parser.setup()
    parser.addtoken("foo", "foo", context)

    assert len(parser.stack) == 1
    assert parser.stack[0][2] == (1, None, context, [(42, "foo", context, [])])

# Generated at 2022-06-13 18:03:31.619838
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar
    from .token import NAME, NUMBER, OP
    class MockParser(Parser):
        def __init__(self):
            gram = grammar.Grammar()
            gram.symbol2number = {}
            gram.number2symbol = {}
            gram.dfas = {
                NAME: (None, None),
                NUMBER: (None, None),
                OP: (None, None),
            }
            self.grammar = gram

        def classify(self, type: int, value: Optional[Text], context: Context) -> int:
            return type

    # Prepare the test data
    parser = MockParser()
    root = parser.rootnode

# Generated at 2022-06-13 18:03:39.446559
# Unit test for method shift of class Parser
def test_Parser_shift():
    from sys import argv, exit, stderr
    if len(argv) > 1 and argv[1] == "-g":
        from .pgen import driver
        driver.main(argv[2:], write_tables=True, optimize=False)
        exit(0)
    if len(argv) < 2:
        print("Usage: %s grammar.txt ..." % (argv[0],), file=stderr)
        exit(2)
    try:
        g = Grammar(argv[1:])
    except IOError as e:
        print("error reading grammar file:", e, file=stderr)
        exit(2)
    p = Parser(g)
    start = g.start
    print("start:", start)
    p.setup(start)

# Generated at 2022-06-13 18:03:51.303586
# Unit test for method shift of class Parser
def test_Parser_shift():
    dfa = (
        [[(1, 2), (2, 1)], [(0, 2), (2, 1)], [(0, 2), (2, 1)]],
        {0: 0, 1: 1, 2: 2},
    )

    parser = Parser(Grammar())
    parser.stack = [(dfa, 0, ([], None, None, []))]
    parser.shift(0, None, 1, None)
    assert parser.stack == [(dfa, 1, ([], None, None, []))]
    parser.shift(0, None, 2, None)
    assert parser.stack == [(dfa, 2, ([], None, None, []))]
    parser.shift(0, None, 1, None)

# Generated at 2022-06-13 18:04:00.043682
# Unit test for method push of class Parser
def test_Parser_push():
    # Setup
    def convert(grammar: Grammar, raw_node: RawNode) -> RawNode:
        """Make a deal with the raw node."""
        return raw_node

    parser = Parser(Grammar())
    parser.setup()
    dfa = parser.grammar.dfas[grammar.LAMBDA]
    # Exercise
    parser.push(grammar.LAMBDA, dfa, 0, None)
    # Verify
    assert parser.stack == [(dfa, 0, (grammar.LAMBDA, None, None, [])), (dfa, 0, None)]


# Generated at 2022-06-13 18:04:09.821819
# Unit test for method classify of class Parser
def test_Parser_classify():
    import unittest
    import importlib.util
    import sys
    import os
    import logging
    import pprint
    # The module below must exist, or the unit test fails
    grammar_module_name = 'blib2to3.pgen2.driver'
    logging.basicConfig(level=logging.INFO)
    if importlib.util.find_spec(grammar_module_name):
        logging.info('Importing %s', grammar_module_name)
        module = importlib.import_module(grammar_module_name)
        # The following is a hack to make the module think it is
        # called differently; this is needed because we need the
        # driver module to load the grammar, and it loads the grammar
        # with a name derived from its own name.
        # The problem is that we already loaded the driver

# Generated at 2022-06-13 18:04:13.357480
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Arranges

    # Act
    try:
        p = Parser.shift(
            token.NAME,
            "popdfa",
            0,
            Context(None, None, True),
        )
        print("p:", p)
        if p != None:
            print("p not None")
    except Exception as e:
        print(e)  # Raises

    # Assert



# Generated at 2022-06-13 18:04:18.666322
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2 import grammar
    p = Parser(grammar.parse_grammar(grammar.tokenize_grammar(grammar.python_grammar)))
    p.setup(grammar.python_grammar.start)
    # Call p.pop()
    p.pop()
    # An exception should be raised:
    # *    def pop(self) -> None:
    # p.pop()
    # *  File "/usr/lib/python3.7/blib2to3/pgen2/pgen.py", line 194, in pop
    # *    if self.stack:
    # *RuntimeError: maximum recursion depth exceeded

# Generated at 2022-06-13 18:04:28.965192
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Open the Python grammar file
    import os
    import sys

    dir = os.path.dirname(sys.modules["blib2to3.pgen2"].__file__)
    path = os.path.join(dir, "Grammar.txt")
    g = Grammar(path)

    class MockParser:
        def __init__(self, grammar):
            self.grammar = grammar

    # Create a Parser instance
    p = Parser(g)

    # Set up parser
    g.add_keyword("class")
    p.setup()
    # token.NAME : 'class'
    p.shift(1, "class", 1, (1, 0))

    assert p.stack[0][2][0] == 0
    assert p.stack[0][2][1] == None

# Generated at 2022-06-13 18:04:34.331086
# Unit test for method setup of class Parser
def test_Parser_setup():
    grammar = Grammar()
    p = Parser(grammar, lam_sub)
    p.setup()
    assert len(p.stack) == 1
    dfa, state, node = p.stack[-1]
    assert dfa is grammar.dfas[grammar.start]
    assert state == 0
    assert node[0] == grammar.start


# Generated at 2022-06-13 18:04:55.572274
# Unit test for method shift of class Parser
def test_Parser_shift():
    """
    >>> from tokens import Token
    >>> from pgen2 import driver, token
    >>> pygram = driver.load_grammar("Python.gram")
    >>> p = Parser(pygram)
    >>> p.setup()
    >>> p.addtoken(token.NAME, "x", (1, 0))
    False
    >>> p.addtoken(61, "=", (1, 2))
    False
    >>> p.addtoken(token.DDOT, "..", (1, 4))
    False
    >>> p.addtoken(token.NAME, "y", (1, 6))
    False
    >>> p.addtoken(10, '\\n', (1, 7))
    True
    >>> p.rootnode
    <Node: stmt_list (1 children)>
    """

# Generated at 2022-06-13 18:05:05.178475
# Unit test for method shift of class Parser
def test_Parser_shift():
    import sys
    import blib2to3.pgen2.parse
    import StringIO
    fp = StringIO.StringIO(
        """\
%start stmt
%token NAME
%token endmarker NUMBER
%token LBRACE RBRACE STRING
%grammar
stmt: NAME endmarker
    | NUMBER endmarker
    | LBRACE RBRACE
    | STRING endmarker
"""
    )
    parser = blib2to3.pgen2.parse.parse_grammar(fp)
    fp.close()
    parser.initialize_dfas()
    # Create a parser instance
    p = Parser(parser, lam_sub)
    p.setup()
    # Parse a simple statement
    token_list = blib2to3.pgen2.tokenize

# Generated at 2022-06-13 18:05:15.119860
# Unit test for method classify of class Parser
def test_Parser_classify():
    """Test method classify of class Parser for external use.
    """
    from . import grammartools

    g1 = grammartools.Grammar()
    g1.start = 'dummy_start'
    g1.add_nonterminal('dummy_start')
    g1.add_nonterminal('dummy_nt')
    g1.add_token(token.NAME, 'dummy_name')
    p1 = Parser(g1)
    p1.setup('dummy_start')
    # NAME input
    assert p1.classify(token.NAME, 'dummy_name', (1, 4)) == 3
    # invalid token
    try:
        p1.classify(token.NEWLINE, '\r\n', (2, 0))
    except:
        pass
    # invalid

# Generated at 2022-06-13 18:05:24.378483
# Unit test for method pop of class Parser
def test_Parser_pop():
    from unittest.mock import patch
    from io import StringIO

    with patch("sys.stdout", new=StringIO()) as fake_out:
        grammar = Grammar.from_file("blib2to3.pgen2.pgen_grammar")
        parser = Parser(grammar)
        parser.setup()
        parser.stack = [[[0, [1]], 1, (1, None, None, [2])], [[0, [2]], 2, (2, None, None, None)]]
        parser.pop()
        assert parser.stack == [[[0, [1]], 1, (1, None, None, [2])]]
        assert parser.rootnode is None



# Generated at 2022-06-13 18:05:34.858325
# Unit test for method shift of class Parser
def test_Parser_shift():
    def reducer(grammar, node):
        assert node[3] is None
        return node[1]

    from . import grammar, tokenize

    tp = tokenize.generate_tokens(open("../tests/data/trivial.py", "rb"))
    tp = tokenize.untokenize(tp)
    tokens = tokenize.generate_tokens(tp.readline)
    g = grammar.Grammar()
    # Set some attributes on g to suppress warnings
    g.start = 0
    g.labels = {}
    g.keywords = {}
    g.tokens = {token.NAME: 0, token.NEWLINE: 1, token.DEDENT: 2, token.ENDMARKER: 3}

# Generated at 2022-06-13 18:05:45.347999
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar
    from . import parse

    # Load a grammar
    g = grammar.Grammar()
    g.load_file("Grammar/Grammar")
    # Create a parser
    p = Parser(g)
    # Parse
    p.setup()
    # Build all input tokens
    NUM_TOKENS = 10
    tokens = [None] * NUM_TOKENS
    for i in range(NUM_TOKENS):
        tokens[i] = (token.NUMBER, str(i), None)
    # Parse tokens
    for token in tokens:
        p.addtoken(*token)
    # Get root node
    root = p.rootnode

# Generated at 2022-06-13 18:05:56.341101
# Unit test for method shift of class Parser
def test_Parser_shift():
    import blib2to3.pgen2.token as token
    import blib2to3.pgen2.grammar as grammar

    g = grammar.Grammar()

    p = Parser(g)
    p.setup()
    p.addtoken(token.NAME, 'name', None)
    p.addtoken(token.EQUAL, 'equal', None)
    p.addtoken(token.STRING, '"aaa"', None)

    print(p.rootnode)
    print(p.rootnode.type)
    print(p.rootnode.children)
    print(p.rootnode.children[0].type)
    print(p.rootnode.children[0].children)
    print(p.rootnode.children[0].children[0].type)

# Generated at 2022-06-13 18:06:03.464069
# Unit test for method shift of class Parser
def test_Parser_shift():
    """Test the method shift of class Parser."""
    from . import driver
    from . import pgen
    from . import tokenize
    from .pytoken import NUMBER, NAME, OP, STRING, NEWLINE

    # Generate a grammar.
    grammar, _, _, _ = pgen.driver.generate_grammar()
    # Create a Parser object and have it parse a token stream:
    #   lambda: x\n    i.e., a function with argument 'x' and body 'None'.
    parser = Parser(grammar)
    parser.setup()
    tokenizer = tokenize.generate_tokens(driver.FileInput("lambda: x\n"))

# Generated at 2022-06-13 18:06:11.861908
# Unit test for method classify of class Parser
def test_Parser_classify():
    """Test the method classify of the class Parser."""
    # Prepare
    parser = Parser(Grammar(), None)

# Generated at 2022-06-13 18:06:16.281178
# Unit test for method push of class Parser
def test_Parser_push():
    p = Parser(Grammar(start=0))
    p.push(0, (1, 1), 0, (1, 2))
    assert p.stack == [((1, 1), 0, (0, None, (1, 2), []))]

# Generated at 2022-06-13 18:06:37.529114
# Unit test for method classify of class Parser
def test_Parser_classify():
    # Define a simplified version of the grammar
    tokens = {
        token.NUMBER: 1,
        token.ADD: 2,
        token.NAME: 3,
    }
    keywords = {"for": 2, "as": 3}
    labels = {1: (token.NUMBER, None), 2: (token.ADD, None), 3: (token.NAME, None)}
    symbols = {1: "exp", 2: "t1", 3: "t2"}
    rules = [([1], [2, 1]), ([2], ["for", 3, "as", 1]), ([2], [])]
    p = Parser(Grammar(tokens, start=1, labels=labels, keywords=keywords, symbols=symbols, rules=rules))
    p.setup()

# Generated at 2022-06-13 18:06:48.600480
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .pickletools import n_ops
    import blib2to3.pgen2.driver

    g = blib2to3.pgen2.driver.load_grammar("Python.g")
    p = Parser(g)
    p.setup()
    p.addtoken(token.NAME, "x", Context(0, 0))
    p.addtoken(token.OP, "=", Context(0, 0))
    p.addtoken("3", "3", Context(0, 0))
    p.addtoken(token.NEWLINE, "", Context(1, 0))


# Generated at 2022-06-13 18:06:54.599009
# Unit test for method shift of class Parser
def test_Parser_shift():
    import unittest.mock

# Generated at 2022-06-13 18:07:02.031164
# Unit test for method push of class Parser

# Generated at 2022-06-13 18:07:17.930200
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys
    # Ensure that the main parser doesn't import the test driver
    sys.modules['blib2to3.pgen2.driver'] = None
    try:
        from blib2to3.pgen2.driver import load_grammar

        g = load_grammar(
            'Python.asdl', 'blib2to3/pgen2', 'asdl.txt', asdl=True, tracking=False
        )
    finally:
        del sys.modules['blib2to3.pgen2.driver']
    p = Parser(g)
    p.setup()
    p.addtoken(11, 'def', (1, 0))
    p.addtoken(1, 'f', (1, 3))
    p.addtoken(9, '(', (1, 4))
    p.addtoken

# Generated at 2022-06-13 18:07:34.400218
# Unit test for method pop of class Parser
def test_Parser_pop():
    import pickle

# Generated at 2022-06-13 18:07:39.180822
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    for grammar in grammar.Grammar("test_grammar"), grammar.Grammar("python2_grammar"):
        p = Parser(grammar)
        p.setup("file_input")
        p.addtoken(token.NEWLINE, "\n", (1, 0))
        p.addtoken(token.NAME, "a", (1, 0))

# Generated at 2022-06-13 18:07:46.029985
# Unit test for method shift of class Parser
def test_Parser_shift():
    p = Parser(Grammar(dfas={}))
    p.stack = [(0, 0, None)]
    p.shift(1, None, 2, None)
    assert p.stack == [(0, 2, None)]
    p.shift(2, None, 3, None)
    assert p.stack == [(0, 3, None)]


# Generated at 2022-06-13 18:07:58.356290
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    class DummyGrammar(object):
        def __init__(self):
            self.start = 257
            self.labels = [(258, 'a'), (259, 'b'), (260, 'c')]
            self.dfas = {256: ([[(1, 0), (0, 1)]], set()), 257: ([[(1, 0), (0, 1)]], set())}

    class DummyParser(Parser):
        def __init__(self):
            self._last_shift = None
            self._last_state = None
            self._last_node = None
            self._last_pop = None
            self._last_roots = []
            Parser.__init__(self, DummyGrammar())


# Generated at 2022-06-13 18:08:08.043073
# Unit test for method shift of class Parser
def test_Parser_shift():

    from .driver import Driver

    from . import token, symbol
    from . import grammar
    from . import pygram, pytree

    # Pickle the grammar tables and load them.
    pygram.init_grammar()
    pygram.load_grammar()
    pytree.init_grammar()

    # Create a parser.
    p = Parser(pygram.python_grammar, pytree.convert)

    # Create a driver.
    d = Driver(p.grammar)

    # This is the program we will parse
    program = 'print(3)'

    # Generate a list of tokens.
    toks = []
    for type, value, context in d.tokenize(program):
        toks.append((type, value, context))

    # Call the setup method.
    p.setup()

    #

# Generated at 2022-06-13 18:08:21.496776
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import parsers
    from .token import INDENT

    parser = parsers.PythonParser()
    parser.setup()
    assert parser.addtoken(INDENT, '..', None)

# Generated at 2022-06-13 18:08:27.009680
# Unit test for method pop of class Parser
def test_Parser_pop():
    # Setup
    pgen = Parser(Grammar())
    pgen.stack = [(None, 0, None), (None, 0, (None, None, None, None))]
    pgen.convert = lambda _, node: node

    # Test
    pgen.pop()

    # Verify
    assert pgen.stack[-1] == (None, 0, (None, None, None, [None]))

# Generated at 2022-06-13 18:08:40.580555
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .tokenize import generate_tokens
    from io import StringIO
    from . import grammar
    import unittest

    def tokenize(s: Text) -> Sequence[
        Tuple[int, Optional[Text], Context, Sequence[Any]]
    ]:
        tokens = [
            t for t in generate_tokens(StringIO(s).readline) if t[0] != token.ENDMARKER
        ]
        return tokens

    class ParserTest(unittest.TestCase):
        def test_simple_addtoken(self) -> None:
            tokens = tokenize("foo(1+1)*3")
            parser = Parser(grammar.grammar)
            parser.setup()
            for type, value, context, d in tokens:
                parser.addtoken(type, value, context)
           

# Generated at 2022-06-13 18:08:48.033623
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2 import driver
    test_grammar = driver.load_grammar("Grammar/Grammar")
    test_parser = Parser(test_grammar)
    test_context = Context(1, 1)
    # Test: check if the values are assigned to the right places
    test_parser.shift(token.NAME, "test_value", 1, test_context)
    assert test_parser.stack[-1][1] == 1
    assert test_parser.stack[-1][2][3] is None
    assert test_parser.stack[-1][2][2] == test_context
    assert test_parser.stack[-1][2][1] == "test_value"
    assert test_parser.stack[-1][2][0] == token.NAME

# Unit

# Generated at 2022-06-13 18:09:04.476143
# Unit test for method shift of class Parser
def test_Parser_shift():

    from . import grammar
    from .grammar import Grammar
    from blib2to3.pygram import python_symbols as syms

    class DummyGrammar:
        def __init__(self):
            self.dfas = {"dummy_dfa": ([[], [(123, 0)]], [0])}
            self.labels = {
                123: (token.NAME, "dummy_token")
            }  # A dummy label to trigger conversion
            self.tokens = {}
            self.keywords = {}

    dummy_grammar = Grammar(grammar._grammar_file, DummyGrammar())

    # No conversion
    no_convert = DummyGrammar()

# Generated at 2022-06-13 18:09:19.446802
# Unit test for method shift of class Parser
def test_Parser_shift():

    class mock_Grammar:
        dfas = {'#start': mock_DFAS()}

        def __init__(self):
            self.tokens = {token.NAME: 1}
            self.dfas = {'#start': mock_DFAS()}
            self.keywords = {}

    class mock_Context:
        pass

    class mock_DFAS:
        def __init__(self):
            self.states = [[(0, 0)]]

    p = Parser(mock_Grammar())
    p.setup()

    # Assert that the concrete syntax tree is not being converted into an abstract syntax tree
    p.stack[0][2][3] = [None]
    p.shift(token.NAME, 'foo', 0, mock_Context())
    assert p.stack[0][2]

# Generated at 2022-06-13 18:09:22.471241
# Unit test for method classify of class Parser
def test_Parser_classify():
    from pathlib import Path
    from . import grammar

    g = grammar.Grammar(Path(__file__).parent / "Python.asdl")
    p = Parser(g)
    p.setup()
    p.addtoken(token.NAME, "a", Context(1, "a = 1\n"))
    assert p.used_names == {"a"}

# Generated at 2022-06-13 18:09:30.000633
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver
    from . import grammar
    from . import parse
    from . import python_grammar
    from . import tokenize
    from . import tokenizer
    from . import tokenizer_32

    # Initialize the grammar table
    python_grammar.initialize()

    # Create a parser
    parser = parse.Parser(grammar.grammar, convert=parse.lam_sub)
    parser.setup()

    # Create an input token generator
    driver.driver(tokenize.tokenize, tokenizer.generate_tokens, 'x = 1')

    # Parse the whole thing
    while True:
        tok = tokenizer_32.get_next_token()
        if tok is None:
            break
        assert parser.addtoken(tok[0], tok[1], tok[2])

# Generated at 2022-06-13 18:09:35.260136
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """Test the Parser.addtoken() method."""
    from . import grammar
    p = Parser(grammar.grammar)
    p.setup()
    for tok in range(300):
        if p.addtoken(tok, "token %d" % tok, (1, 2)):
            break
    p.stack.clear()
    p.setup()


# Generated at 2022-06-13 18:09:43.797919
# Unit test for method pop of class Parser
def test_Parser_pop():
    class ParserTest(Parser):
        def __init__(self, grammar):
            self.stack = []
            self.grammar = grammar
            self.stack.append((1, 2, (4, 5, 6)))
            self.used_names = set()

    parser_test = ParserTest(1)
    parser_test.stack.append((2, 3, (4, 5, 6)))
    parser_test.pop()
    assert parser_test.stack == [(1, 2, (4, 5, 6))]

# Generated at 2022-06-13 18:10:13.652679
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar
    from . import driver
    from .token import tok_name
    from . import pytree
    import sys

    if len(sys.argv) == 1:
        sys.argv.append("15.py")
    with open(sys.argv[1], "rb") as f:
        encoding = driver.detect_encoding(f.readline)
    with open(sys.argv[1], "rt", encoding=encoding) as f:
        g = grammar.Grammar(f.read())
    p = Parser(g)
    p.setup(g.start)
    tokgen = driver.tokenize_str(f.read())
    while True:
        try:
            tok = next(tokgen)
        except token.TokenError:
            break
       

# Generated at 2022-06-13 18:10:20.973855
# Unit test for method setup of class Parser
def test_Parser_setup():
    import sys

    if sys.version_info[:2] == (2, 3):
        return

    from . import grammar, token

    start = grammar.symbol2number['file_input']
    g = grammar.Grammar(grammar.dfas, grammar.labels, start)
    p = Parser(g)
    p.setup()
    p.addtoken(token.NAME, 'a', (0, 0))

# Generated at 2022-06-13 18:10:31.705517
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver, tokenize

    # This test requires the driver module, in turn requiring the
    # tokenize module.  Test that module first.
    test_tokenize_startprog()

    # Load the grammar
    grammar = driver.prepare_grammar()

    # Test the common cases
    def testcase(s: str) -> None:
        p = Parser(grammar)
        p.setup()
        for type, value, context in tokenize.generate_tokens(
            tokenize.StringIO(s).readline
        ):
            if p.addtoken(type, value, context):
                break
        else:
            raise ValueError("missing newline")
        if p.rootnode is None:
            raise ValueError("no root")
    # Test simple cases
    testcase("pass\n")

# Generated at 2022-06-13 18:10:47.461258
# Unit test for method push of class Parser
def test_Parser_push():

    def convert1(grammar, node):
        return node

    g = Grammar()

# Generated at 2022-06-13 18:10:56.733930
# Unit test for method shift of class Parser
def test_Parser_shift():
    class MyGrammar(Grammar):
        def __init__(self) -> None:
            self.start = 256
            self.root = 257
            self.tokens = {
                token.NUMBER: 258,
                token.DEDENT: 259,
                token.INDENT: 260,
                token.STRING: 261,
            }
            self.keywords = {}
            self.symbols = {
                self.root: 262,
                self.start: 263,
            }
            self.rejects = {}
            self.literals = {}

# Generated at 2022-06-13 18:10:59.998902
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar, tokenize

    g = grammar.grammar
    p = Parser(g)
    p.setup()
    for t in tokenize.find_tokens("[a, 'b']"):
        p.addtoken(*t)
    assert p.rootnode[0] == "testlist_gexp"

# Generated at 2022-06-13 18:11:08.364961
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    g = grammar.Grammar()
    p = Parser(g)

    class DummyGrammar:
        def __init__(self) -> None:
            self.tokens = dict()
            self.keywords = dict()
            self.dfas = dict()
            self.labels = list()

        def addlabel(self, is_token: bool, type: int, value: Text) -> int:
            assert value is not None
            if is_token:
                self.tokens[type] = len(self.labels)
            else:
                self.keywords[value] = len(self.labels)
            self.labels.append((type, value))
            return len(self.labels) - 1


# Generated at 2022-06-13 18:11:17.043367
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """Test case for Parser.addtoken()."""
    from textwrap import dedent

    from blib2to3 import pygram
    from . import tokenize, token

    g = pygram.python_grammar.copy()
    g.version = "3.6"
    p = Parser(g)
    p.setup("file_input")
    # Test case
    source = """\
        def f():
            global g
            nonlocal n
            del d
            class C:
                pass
        """
    #
    toks = list(tokenize.generate_tokens(dedent(source).lstrip))
    names = ["f", "g", "n", "d", "C"]
    for tok in toks:
        if p.addtoken(*tok):
            break

# Generated at 2022-06-13 18:11:26.935938
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import driver

    class DummyOpts:
        verbose = 0

    opts = DummyOpts()
    p = driver.load_grammar(opts)
    p.setup()
    p.addtoken(
        token.LBRACE, "{", driver.FileInput.context(1, 0, "while (1) {\n\tpass\n}\n")
    )
    assert p.addtoken(
        token.PASS, "pass", driver.FileInput.context(2, 0, "while (1) {\n\tpass\n}\n")
    )
    assert p.addtoken(
        token.RBRACE, "}", driver.FileInput.context(3, 0, "while (1) {\n\tpass\n}\n")
    )