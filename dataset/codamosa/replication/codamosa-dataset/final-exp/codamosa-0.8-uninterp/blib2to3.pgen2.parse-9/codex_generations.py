

# Generated at 2022-06-13 18:01:35.111184
# Unit test for method pop of class Parser
def test_Parser_pop():
    from ..pgen2 import driver
    from ..pgen2.tokenize import untokenize, generate_tokens, ENDMARKER

    import io
    import tokenize

    def read_from_string(string: str) -> Text:
        """Read from a string"""
        return io.BytesIO(string.encode("utf-8")).readline

    g = driver.load_grammar("Grammar/Grammar")


# Generated at 2022-06-13 18:01:45.947348
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest

    class Parser_addtokenTest(unittest.TestCase):
        def setUp(self):
            super().setUp()
            import sys

            import blib2to3.pgen2.driver

            driver = blib2to3.pgen2.driver
            grammar = driver.load_grammar(sys.argv[1])
            self.parser = Parser(grammar)

        def test_Parser_addtoken(self):
            stack = self.parser.stack
            self.parser.addtoken(0, 'asdf', ('', 1, 0))
            self.assertEqual([([([(1, 1)], 0)], 0, ('file_input', None, ('', 1, 0), []))], stack)

# Generated at 2022-06-13 18:01:57.420151
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .grammar import Grammar
    from .tokenize import generate_tokens, untokenize
    from . import token

    class mock_RawNode:
        pass

    class mock_Grammar:
        def __init__(self):
            self.dfas = [None]
            self.labels = [None]
            self.keywords = [None]
            self.tokens = [None]

    class mock_Context:
        pass

    mock_token = token.TYPE, token.NAME, mock_Context(), mock_Context()

    mock_tokens = [mock_token]
    assert mock_tokens == [mock_token]

    text = "Grammar"
    mock_tokens = generate_tokens(text)

# Generated at 2022-06-13 18:01:59.532527
# Unit test for method setup of class Parser
def test_Parser_setup():
    """Unit test for method setup of class Parser"""
    p = Parser(Grammar())
    p.setup()

# Generated at 2022-06-13 18:02:06.650857
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    ast, source = driver.parse_string(
        """
    if True:
        x = 5
        y = 6
        z = 7
    """
    )
    # print ast
    assert ast is not None
    assert len(source) > 0
    result = [[0, [1, [2, [3, [4, [], [5, [6, [7, [], []]], []]], [8, [9, [10, [], []]], []]]]]]]
    assert ast == result

# Generated at 2022-06-13 18:02:14.874808
# Unit test for method pop of class Parser
def test_Parser_pop():
    class FakeGrammar:
        keymap: Dict[Text, int] = {}
        dfas: Dict[int, DFAS] = {}
        labels: Dict[int, Tuple] = {}
        tokens: Dict[int, int] = {}
        start: int = 1
        keywords: Dict[Text, int] = {"print": 1}
    
    class FakeDFAS:
        def __init__(self, states: List[List], first: Dict[int, int]) -> None:
            self.states = states
            self.first = first
    
    grammar = FakeGrammar()

# Generated at 2022-06-13 18:02:26.257158
# Unit test for method shift of class Parser
def test_Parser_shift():
    """Test proper handling of context in Parser.shift()"""
    import sys
    from . import driver
    from blib2to3.pgen2 import token
    from blib2to3.pgen2.parse import ParseError
    from blib2to3.pytree import Leaf

    # Initialize parser driver and the parser itself
    drv = driver.Driver(None, None)
    p = drv.parser
    # We don't care about the actual grammar here, we are only interested
    # in the convert() method in the Parser class. In this particular test
    # we don't have to have a complete grammar

# Generated at 2022-06-13 18:02:27.655824
# Unit test for method shift of class Parser
def test_Parser_shift():
    pass

# Generated at 2022-06-13 18:02:38.428119
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest

    class Parser_addtoken_TestCase(unittest.TestCase):
        def check_addtoken(self, input, expected):
            # Preparing
            from blib2to3.pgen2 import driver

            start = "<start>"
            grammar = driver.load_grammar("Grammar/Grammar")
            # Parsing
            p = Parser(grammar)
            p.setup(start)
            for token in input:
                type, value, context = token
                if p.addtoken(type, value, context):
                    break
            # Testing
            self.assertEqual(p.rootnode, expected)

        def test_0(self):
            from blib2to3.pygram import python_symbols


# Generated at 2022-06-13 18:02:48.201370
# Unit test for method pop of class Parser
def test_Parser_pop():
    # The constructor has already been tested by test_Parser_init
    # The classifiers have already been tested by test_Parser_classify
    # The parser has already been tested by test_Parser_addtoken
    grammar_file = open("/home/xu/Documents/GitHub/ProgramTransformation/blib2to3/pgen2/Grammar.txt")
    grammar_source = grammar_file.read()
    grammar_file.close()
    grammar = Grammar(grammar_source)
    parser = Parser(grammar)
    parser.setup()
    parser.addtoken(1, None, None)
    parser.addtoken(2, None, None)
    parser.addtoken(3, None, None)
    parser.addtoken(4, None, None)

# Generated at 2022-06-13 18:03:04.547081
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys

    sys.path.insert(0, "..")

    from . import driver

    grammar = driver.load_grammar("Grammar.txt")
    driver.make_pgen(grammar, "Grammar.txt")

    def do_parse(text: Text, start: Optional[int] = None) -> NL:
        driver.make_grammar(grammar)
        driver.make_pgen(grammar, "Grammar.txt")
        parser = Parser(grammar)
        parser.setup(start)
        tokenizer = driver.make_tokenizer(grammar)
        for type, value, context in tokenizer.generate_tokens(text):
            parser.addtoken(type, value, context)
        return parser.rootnode


# Generated at 2022-06-13 18:03:17.312190
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar
    from blib2to3.fixer_base import FixerBase
    from blib2to3.fixer_util import Name, syms, Comma
    fixer = FixerBase()
    grammar = grammar.Grammar(fixer.grammar_pickle)
    convert_function = FixerBase.lam_sub(grammar)
    test_parser = Parser(grammar, convert_function)
    test_parser.setup()
    test_parser.addtoken(syms.NAME, "test", (1, 0))
    test_parser.addtoken(syms.NAME, "test2", (1, 0))
    test_parser.addtoken(token.COMMA, ",", (1, 0))

# Generated at 2022-06-13 18:03:23.233415
# Unit test for method setup of class Parser
def test_Parser_setup():
    from pprint import pprint

    from . import driver, grammar, tokens

    p = Parser(grammar)
    p.setup()

    # pprint(p.stack, indent=2)
    assert len(p.stack) == 1
    assert p.stack[0][0] is grammar.dfas[grammar.start]
    assert p.stack[0][1] == 0
    assert p.stack[0][2] == (grammar.start, None, None, [])



# Generated at 2022-06-13 18:03:30.041039
# Unit test for method shift of class Parser
def test_Parser_shift():
    import sys
    try:
        p = Parser(Grammar(sys.stdin.buffer, sys.stdout.buffer))
        p.shift(0, "test_value", 0, (0,0))
    except:
        assert False, "Failed to shift token"


# Generated at 2022-06-13 18:03:40.371768
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import token as t
    from . import grammar as g
    from . import driver
    test_grammar = """
    test: 'ab' | 'abc'
    """
    drv = driver.Driver(
        grammar=g.Grammar(test_grammar),
        convert_tuple_to_tree=False,
        logstream=None,
    )
    # Here's a tokenizer
    p = drv.parser
    p.setup()
    assert p.classify(t.STRING, "ab", None) == 2
    assert p.classify(t.STRING, "abc", None) == 2
    try:
        p.classify(t.NUMBER, None, None)
    except ParseError:
        pass
    else:
        assert False

# Generated at 2022-06-13 18:03:56.774340
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .pgen2 import driver

    grammar = driver.load_grammar("Grammar/Grammar")
    p = Parser(grammar)
    p.setup()

    s = """\
    for x in range(10):
        print(x)
    """


# Generated at 2022-06-13 18:04:03.921017
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    gram = driver.load_grammar('Python.g4')
    p = Parser(gram)
    p.setup()

    p.addtoken(token.NAME, 'import', (1, 0))
    p.addtoken(token.NAME, 'sys', (1, 7))
    p.addtoken(token.OP, '.', (1, 10))
    p.addtoken(token.NAME, 'stdout', (1, 11))
    p.addtoken(token.OP, '=', (1, 17))
    p.addtoken(token.NAME, 'sys', (1, 19))
    p.addtoken(token.OP, '.', (1, 22))
    p.addtoken(token.NAME, 'stdout', (1, 23))

# Generated at 2022-06-13 18:04:06.599198
# Unit test for method pop of class Parser
def test_Parser_pop():
    """Unit test for method pop of class Parser."""
    # For now, this is just to silence pyflakes
    p = Parser(Grammar())
    p.pop()

# Generated at 2022-06-13 18:04:10.533557
# Unit test for method classify of class Parser
def test_Parser_classify():

    def _test_case(test_case, token_type, token_value, label, keywords):
        """
        compare the label returned by Parser.classify and the value label
        """
        parser = Parser(Grammar())
        parser.grammar.keywords = keywords
        parser.grammar.tokens = {token_type: 3}
        assert parser.classify(token_type, token_value, None) == label

    # Test case 1:
    keywords = {'name': 5}
    _test_case(1, token.NAME, 'name', 5, keywords)

# Generated at 2022-06-13 18:04:15.995438
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import blib2to3.pgen2.grammar as grammar
    import blib2to3.pgen2.driver as driver

    g = grammar.Grammar(grammar.DEFAULT_GRAMMAR)
    p = Parser(g)
    p.setup()
    d = driver.Driver(g, p.addtoken)
    d.parse_tokens([(1, "foo"), (2, "bar")])
    assert [
        c.value for c in p.rootnode[-1][-1][-1]
    ] == ["foo", "bar"], "Invalid parse"



# Generated at 2022-06-13 18:04:30.035242
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    driver.verbose = 1
    debug = 0
    # debug = 1
    driver.debug = debug
    Grammar = driver.Grammar
    Parser = driver.Parser

    # Some test programs

# Generated at 2022-06-13 18:04:39.779233
# Unit test for method pop of class Parser
def test_Parser_pop():
    # this is a test for a case where the parser fails
    # the source of the problem is the convert function
    # def lam_sub(grammar, node):
    #   assert node[3] is not None
    #   return Node(type=node[0], children=node[3], context=node[2])
    # this function is supposed to return a Node
    # but if node[3] is empty, None gets returned
    # then the following line (where the assertion fails)
    #    assert node[-1] is not None
    # causes a problem in the function pop() of the class Parser
    from . import grammar

    class Mock_Node:
        def __init__(self, type, children, context):
            self.type = type
            self.children = children
            self.context = context


# Generated at 2022-06-13 18:04:50.162004
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import token, tokenize
    from blib2to3.pgen2 import grammar, parse
    p = Parser(grammar.grammar)
    p.setup()
    l = tokenize.generate_tokens(
        (x for x in ["2"]).__next__
    )  # type: ignore # https://github.com/python/mypy/issues/1182
    for t in l:
        p.addtoken(t[0], t[1], t[2])
    assert parse.parsest(p) == "Module(None, Stmt([Expr(Const(2))]))"


# Generated at 2022-06-13 18:04:59.774011
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    p = Parser(grammar)
    assert p.classify(token.NAME, "foo", Context(1, 0, "")) == p.grammar.tokens[token.NAME]
    assert p.classify(token.NUMBER, "1", Context(1, 0, "")) == p.grammar.tokens[token.NUMBER]
    assert p.classify(token.NAME, "False", Context(1, 0, "")) == p.grammar.keywords["False"]

    def fin(s):
        f = open(s, "rU")
        p = Parser(grammar)
        p.setup()
        while True:
            t = token.GENERIC_TOKEN.clone()
            t.get_token(f)

# Generated at 2022-06-13 18:05:04.520230
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    def g():
        return grammar.grammar

    parser = Parser(g())
    assert parser.classify(token.NUMBER, "42", None) in (1, 2)
    try:
        parser.classify(token.NAME, "function", None)
    except ParseError:
        pass
    else:
        assert False, "method classify didn't raise ParseError on unreserved NAME"


# Generated at 2022-06-13 18:05:09.932981
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2.tokenize import generate_tokens, tokenize, detect_encoding, token
    from blib2to3.pgen2.driver import load_grammar, load_grammar_file
    import tokenize
    import io
    import re
    import sys

    MOCK_FILE = "<testfile>"
    MOCK_ENCODING = "utf-8"

    def mock_open(filename):
        if filename == "parser.txt":
            return io.StringIO(u'print("hello world")')
        else:
            raise IOError("No such file: %r" % filename)

    f = mock_open("parser.txt")
    detect_encoding(f.readline)
    f = mock_open("parser.txt")

# Generated at 2022-06-13 18:05:17.513932
# Unit test for method shift of class Parser
def test_Parser_shift():
    import pgen2.driver
    import pgen2.parse
    import os
    import sys
    import unittest

    # Test case class
    class TestParserShift(unittest.TestCase):
        def setUp(self):
            self.statement = "a = 1 + 2 + 3"
            self.path = os.path.join(
                os.path.dirname(pgen2.driver.__file__), "Grammar.txt"
            )
            self.parser = pgen2.driver.load_grammar(self.path)
            self.parser.setup()

        def test_shift(self):
            self.tokens = iter(pgen2.parse.tokenize(self.statement))

# Generated at 2022-06-13 18:05:22.465564
# Unit test for method push of class Parser
def test_Parser_push():
    p = Parser(Grammar())
    p.setup()
    p.push(1, 2, 3, Context(None, 1))
    assert p.stack == [(([], {}), 0, (Grammar.START, None, None, [])), ((2, 3), 0, (1, None, Context(None, 1), []))]

# Generated at 2022-06-13 18:05:34.248717
# Unit test for method push of class Parser
def test_Parser_push():
    from . import driver, parser

    def main():
        p = parser.Parser(driver.Grammar, driver.convert)
        p.setup()
        p.addtoken(token.NAME, "def", Context(1, 0, "test"))
        p.addtoken(token.NAME, "foo", Context(1, 4, "test"))
        p.addtoken(token.OP, "(", Context(1, 7, "test"))
        p.addtoken(token.OP, ")", Context(1, 8, "test"))
        p.addtoken(token.OP, ":", Context(1, 9, "test"))
        assert p.used_names == set(["def", "foo"]), repr(p.used_names)
        tree = p.rootnode

# Generated at 2022-06-13 18:05:45.053803
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver

    input = "foo and bar"
    grammar = driver.parse_grammar(input)
    parser = Parser(grammar)
    parser.setup()
    parser.addtoken(token.NAME, "foo", Context(0, 0))
    parser.addtoken(token.AND, "and", Context(0, 3))
    parser.addtoken(token.NAME, "bar", Context(0, 6))
    parser.addtoken(token.NEWLINE, "\n", Context(0, 9))
    assert isinstance(parser.rootnode, ast.Boolop)

# Generated at 2022-06-13 18:06:07.731443
# Unit test for method shift of class Parser
def test_Parser_shift():
    p = Parser(None, lambda grammar, node: None)
    dfas = (
        [[(1, 2)], [(1, 2)], [(3, 2)]],
        {
            0: 2,
            1: 2,
            2: 2,
            3: 3,
        },
    )
    p.stack = [
        (dfas, 0, (0, None, None, [])),
        (dfas, 0, (1, None, None, [])),
    ]
    p.shift(token.PLUS, "+", 1, None)
    assert p.stack == [
        (dfas, 1, (0, None, None, [])),
        (dfas, 1, (1, None, None, [])),
    ]

# Generated at 2022-06-13 18:06:15.982113
# Unit test for method setup of class Parser
def test_Parser_setup():
    import unittest
    from . import grammar

    class TestCase(unittest.TestCase):
        def test_setup(self):
            p = Parser(grammar)
            p.setup()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    test_Parser_setup()

# Generated at 2022-06-13 18:06:25.003458
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    p = Parser(grammar)
    p.setup()
    # parse the phrase "3.14" in a toy grammar containing just the number
    # production
    p.addtoken(token.NUMBER, "3.14", (1, 0))
    # Check the results
    rootnode = p.rootnode
    assert rootnode.type == grammar.number
    assert len(rootnode) == 1
    node = rootnode[0]
    assert isinstance(node, Leaf)
    assert node.value == "3.14"

# Generated at 2022-06-13 18:06:29.874675
# Unit test for method classify of class Parser
def test_Parser_classify():
    grammar = grammar.Grammar()
    p = Parser(grammar)
    cases = ['if', 'temp']
    for c in cases:
        p.classify(token.NAME, c, None)
        assert c in p.used_names

# Generated at 2022-06-13 18:06:39.035559
# Unit test for method pop of class Parser
def test_Parser_pop():
    # test the case where stack has only one element
    # stack = [(popdfa, popstate, popnode)]
    # expected stack = []
    # expected rootnode = self.convert(self.grammar, popnode)
    mock_popdfa = [(0, 1), (1, 1)]
    mock_popstate = 0
    mock_popnode = (1, "mock_value", "mock_context", [])
    mock_rootnode = "mock_rootnode"
    mock_used_names = ["mock_name1", "mock_name2"]
    parser = Parser(None)
    parser.stack = [(mock_popdfa, mock_popstate, mock_popnode)]
    parser.convert = lambda mock_grammar, mock_popnode: mock_rootnode

# Generated at 2022-06-13 18:06:49.470709
# Unit test for method pop of class Parser

# Generated at 2022-06-13 18:07:00.632092
# Unit test for method pop of class Parser
def test_Parser_pop():
    import grammar
    import token

    class FakeParser(Parser):
        def __init__(self, grammar: Grammar, convert: Optional[Convert] = None) -> None:
            super().__init__(grammar, convert)

# Generated at 2022-06-13 18:07:09.895005
# Unit test for method pop of class Parser
def test_Parser_pop():
    global Node, lam_sub
    class Node:
        def __init__(self, type, children, context):
            self.type = type
            self.children = children
            self.context = context
            self.used_names = self.used_names

    def lam_sub(grammar, node):
        assert node[3] is not None
        return Node(type=node[0], children=node[3], context=node[2])

    from . import grammar
    from .grammar import Grammar
    from .token import TokenInfo, NAME, NEWLINE
    from . import tokenize
    from .tokenize import generate_tokens
    from blib2to3.pgen2.pgen import load_grammar
    import os
    import sys
    import unittest


# Generated at 2022-06-13 18:07:14.740215
# Unit test for method shift of class Parser
def test_Parser_shift():
    class Parser(object):
        def shift(
            self, type: int, value: Optional[Text], newstate: int, context: Context
        ) -> None:
            assert type == token.NAME
            assert value == "NAME"
            assert newstate == 10
            assert context == "context"

    parser = Parser()
    parser.shift(token.NAME, "NAME", 10, "context")

# Generated at 2022-06-13 18:07:22.074656
# Unit test for method shift of class Parser
def test_Parser_shift():
    class MockGrammar(object):
        pass
    from six import StringIO
    from . import tokenize

    grammar = MockGrammar()
    grammar.dfas = {
        "symbol": ([], set()),
        token.NAME: ([], set()),
        token.NUMBER: ([], set()),
    }
    grammar.labels = [
        (token.NAME, "name"),
        (token.NUMBER, "number"),
        ("symbol", "symbol"),
    ]
    p = Parser(grammar, None)
    p.setup()
    p.addtoken(token.NAME, "name", (1, 2))
    assert p.stack == [(grammar.dfas[token.NAME], 0, (token.NAME, "name", (1, 2), None))]


# Unit

# Generated at 2022-06-13 18:07:41.411238
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar
    from . import symbols

    g = grammar.Grammar()
    sym_expr_stmt = g.symbol("expr_stmt", "expr")
    g.add_mapping([sym_expr_stmt],
                  "expr_stmt",
                  "expr",
                  name_map={"expr": "expr"})
    g.symbol("expr", "term")

    p = Parser(g)
    p.setup(start=symbols.file_input)
    p.addtoken(token.NEWLINE, None, None)
    assert len(p.stack) == 1
    assert p.stack[0][2][0] == symbols.file_input

    p.push(sym_expr_stmt, g.dfas[sym_expr_stmt], 0, None)
   

# Generated at 2022-06-13 18:07:47.561850
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import sample_grammar

    g = sample_grammar.grammar
    p = Parser(g)
    p.setup()
    assert len(p.stack) == 1
    dfa, state, node = p.stack[0]
    assert node[0] == sample_grammar.start


# Generated at 2022-06-13 18:07:57.587942
# Unit test for method pop of class Parser
def test_Parser_pop():
    class TestGrammar:
        def __init__(self):
            self.start = 256
            self.labels = None
            self.keywords = {}
            self.tokens = {}
            self.dfas = {}

    test_dfas = {
        256: ([[(None, 1)], [(None, 2)]], set([1, 2])),
        257: ([[(None, 3)], [(None, 4)]], set([3, 4])),
        258: ([[(None, 5)], [(None, 6)]], set([5, 6])),
    }

    test_grammar = TestGrammar()
    test_grammar.dfas = test_dfas

    p = Parser(test_grammar)
    p.setup()

# Generated at 2022-06-13 18:08:05.920023
# Unit test for method shift of class Parser
def test_Parser_shift():
    # pylint: disable-msg=C0111
    from .grammar import grammar
    from .token import tok_name
    from .pgen2 import pgen
    from . import parse, driver
    from . import pytree

    g = grammar.Grammar()
    p = Parser(g, convert=None)
    p.setup()
    p.addtoken(token.NEWLINE, "\n", (1, 0))
    p.addtoken(token.NAME, "def", (1, 0))
    p.addtoken(token.NAME, "f", (1, 0))
    p.addtoken(token.LPAR, "(", (1, 0))
    p.addtoken(token.NAME, "x", (1, 0))

# Generated at 2022-06-13 18:08:16.926879
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver
    driver.dump_files(__file__)
    from . import test_parser

    # test empty stack
    P = Parser(test_parser.parser1_grammar, lam_sub)
    P.setup()
    P.pop()
    assert P.stack == []
    assert P.rootnode == None

    # test stack with depth 1
    P = Parser(test_parser.parser1_grammar, lam_sub)
    P.setup()
    P.addtoken(token.VALUE, "a", (1,1))
    P.push(3, test_parser.parser1_grammar.dfas[3], 0, (1,1))
    P.pop()

# Generated at 2022-06-13 18:08:26.978401
# Unit test for method classify of class Parser
def test_Parser_classify():
    # pylint: disable=import-outside-toplevel
    from .token import DEDENT, INDENT, NAME, NEWLINE, NL, NUMBER, STRING
    from .tokenize import generate_tokens
    # pylint: disable=import-outside-toplevel

    from . import grammar

    g = grammar.grammar

    t = generate_tokens("x = 10\n")
    p = Parser(g)
    p.setup()
    for typ, val, _, _, _ in t:
        if typ == NL:
            typ, val = NEWLINE, "\n"
        elif typ == INDENT:
            typ, val = NEWLINE, "\n"
        elif typ == DEDENT:
            typ, val = NEWLINE, "\n"

# Generated at 2022-06-13 18:08:38.041576
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2 import driver

    # Instantiate the driver
    d = driver.Driver("Grammar/Grammar", convert=lam_sub)
    p = d.parser

    # Create a tokenizer
    tokenizer = d.tokenize("[4+5]")

    # Add the opening bracket
    p.addtoken(d.grammar.symbol2number["'['"], None, (1, 0))
    assert len(p.stack) == 2
    assert p.stack[-1][1] == 0
    assert p.stack[-1][2][0] == d.grammar.symbol2number["listmaker"]
    assert p.stack[-1][2][-1] == []

# Generated at 2022-06-13 18:08:43.882794
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    p = Parser(grammar.grammar)
    p.setup()
    def check():
        assert p.stack == [(grammar.grammar.dfas[1], 0, (1, None, None, []))]
        p.addtoken(token.NAME, "a", (1, 0))
        assert p.stack == [(grammar.grammar.dfas[1], 0, (1, None, None, [])),
            (grammar.grammar.dfas[257], 0, (257, None, None, []))]
        p.addtoken(token.LSQB, "[", (1, 0))

# Generated at 2022-06-13 18:09:00.417246
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2 import tokenize

    from . import grammar, driver, pgen

    import sys

    # Dummy grammar for testing

# Generated at 2022-06-13 18:09:09.555722
# Unit test for method pop of class Parser
def test_Parser_pop():
    class MockGrammar(Grammar):
        def __init__(self) -> None:
            self.labels = {1: (257, None), 2: (258, None), 3: (259, None), 4: (260, None)}
            self.nonterminals = {257: None, 258: None, 259: None, 260: None}
            self.keywords = {}
            self.tokens = {1: 1, 2: 2, 3: 3, 4: 4}

# Generated at 2022-06-13 18:09:42.996993
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import pgen2.parser
    import pgen2.grammar
    import pgen2.tokenize

    g = pgen2.grammar.Grammar(pgen2.pgen.grammar_nts, pgen2.pgen.grammar_dfas)
    p = pgen2.parser.Parser(g)
    p.setup()
    # Test adding whitespace
    p.addtoken(pgen2.tokenize.NEWLINE, "\n", (1, 1))
    # Test adding a token
    p.addtoken(pgen2.tokenize.NAME, "foo", (1, 2))
    # Test adding a reserved word
    p.addtoken(pgen2.tokenize.NAME, "end", (1, 3))
    # Test adding a bad token

# Generated at 2022-06-13 18:09:51.577952
# Unit test for method pop of class Parser
def test_Parser_pop():
    import unittest
    from . import grammar
    from . import tokenize
    from . import driver

    class TestParser(unittest.TestCase):

        def setUp(self):
            self.p = Parser(grammar.python_grammar)
            self.p.setup()

        def test_pop(self):
            class t(object):
                def __init__(self):
                    self.p = Parser(grammar.python_grammar)
                    self.p.setup()

                def classify(self, type, value, context):
                    ilabel = self.p.grammar.tokens.get(type)

                    if ilabel is None:
                        raise ParseError("bad token", type, value, context)
                    return ilabel


# Generated at 2022-06-13 18:10:00.956395
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    grammar = driver.load_grammar("Grammar.txt")
    p = Parser(grammar)
    p.setup()
    assert p.addtoken(token.NAME, "a", Context(1, 0))

# Generated at 2022-06-13 18:10:12.605448
# Unit test for method classify of class Parser
def test_Parser_classify():
    import sys
    from . import driver, token, grammar  # type: ignore

    class Dummy:
        pass

    fake_token = Dummy()
    fake_token.__class__ = token.Token
    fake_token.type = token.N_TOKENS - 1
    fake_token.value = None
    fake_token.lineno = 1
    fake_token.offset = 0

    driver.copy_token = lambda: fake_token

    fp = open(grammar.__file__, "r")
    contents = fp.read()
    fp.close()

    driver.set_grammar_source(contents)
    g = driver.create_grammar()
    p = Parser(g)
    p.setup()


# Generated at 2022-06-13 18:10:22.293184
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class MockParser(Parser):
        def __init__(self, grammar):
            Parser.__init__(self, grammar)
            self.stack = []  # type: List[Tuple[DFAS, int, RawNode]]
            self.rootnode = None  # type: Optional[Node]
            self.used_names = set()  # type: Set[str]

    import os.path
    import pickle
    from blib2to3.pgen2 import driver

    def mysetup(start, convert):
        MockParser.setup(start, convert)
        self.stack = []
        self.rootnode = None
        self.used_names = set()

    file_path = os.path.join(os.path.dirname(__file__), "python2.7.pickle")

# Generated at 2022-06-13 18:10:27.630780
# Unit test for method push of class Parser
def test_Parser_push():
    import sys, os
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], ".."))
    import blib2to3.pgen2.pgen

    p = blib2to3.pgen2.pgen.Parser(blib2to3.pgen2.pgen.grammar, None)
    p.push(100, 0, 0, 0)

# Generated at 2022-06-13 18:10:30.037054
# Unit test for method setup of class Parser
def test_Parser_setup():
    p = Parser(grammar.Grammar())
    p.setup()


# Generated at 2022-06-13 18:10:38.782064
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # The parser gets confused on this line.
    p = Parser(Grammar(grammar, symbols, dfas, labels))
    # Force p to run the initializer first, then we can monkey with it.
    p.setup()
    state = p.stack[0]
    assert state == (dfas[symbols['file_input']], 0, (symbols['file_input'], None, None, []))
    p.addtoken(token.INDENT, 'mumble', (1, 0))
    state = p.stack[0]
    assert state == (dfas[symbols['file_input']], 1, (symbols['file_input'], None, None, []))
    state = p.stack[1]

# Generated at 2022-06-13 18:10:49.628735
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class Mock_Grammar:
        def __init__(self) -> None:
            self.start = 1
            self.dfas: Dict[int, DFAS] = {}

    Mock_Grammar.dfas[1] = ([[(2, 2)], [(3, 3)], [(4, 4)], [(0, 4)]], {1: 2, 3: 4})
    p = Parser(Mock_Grammar())
    p.setup()
    assert not p.addtoken(2, "<repr()>", "<context>")
    assert not p.addtoken(3, "<repr()>", "<context>")
    assert p.addtoken(4, "<repr()>", "<context>")
    p.setup()

# Generated at 2022-06-13 18:10:57.914010
# Unit test for method pop of class Parser
def test_Parser_pop():
    class FakeGrammar(object):
        def __init__(self):
            self.start = 1
            self.dfas = {1: ([([(0, 1)], [('ENDMARKER', 1)])], {})}
            self.labels = {1: ('ENDMARKER', 1)}
            self.tokens = {'ENDMARKER': 1}
            self.keywords = {}

    class FakeConverter(object):
        def __init__(self):
            self.conversions = {}

        def __call__(self, grammar, node):
            self.conversions[node] = node

    grammar = FakeGrammar()
    converter = FakeConverter()
    parser = Parser(grammar, converter)
    parser.setup()