

# Generated at 2022-06-13 18:01:48.959513
# Unit test for method setup of class Parser
def test_Parser_setup():
    import sys
    from . import token
    from .pgen import Grammar
    from .pgen import driver
    if "test.test_parser" in sys.modules:
        test_mode = True
        from . import token
        from .pgen import Grammar
        from .pgen import driver
    else:
        test_mode = False

    if test_mode:
        class Tokenizer:
            def __init__(self):
                self.count = 0
            def __call__(self):
                self.count += 1
                if self.count > 10:
                    return token.ENDMARKER, ""
                return token.NAME, "x"

    gr = driver.load_grammar("Grammar.txt")
    p = gr._parser
    p.setup()

# Generated at 2022-06-13 18:01:58.518237
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver, token, symbol, parser

    # Set up the parser
    p = parser.Parser(driver.Symbol, driver.Grammar)
    # Start parsing
    p.setup()
    # Simulate the tokens that are returned by the tokenizer
    id = symbol.name
    num = symbol.test
    punct = token.DOT
    for tok in [(id, "a", (1,0)),
                (punct, ".", (1,1)),
                (id, "b", (1,2)),
                (punct, ".", (1,3)),
                (id, "c", (1,4)),
                (punct, ".", (1,5))]:
        if p.addtoken(*tok):
            break

    # Check the resulting tree
    t = p.rootnode

# Generated at 2022-06-13 18:02:05.386736
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver
    from . import tokenize
    from . import grammar

    g = grammar.Grammar()
    g.initialize()
    # Initialize the parser
    p = Parser(g, lam_sub)
    p.setup()

    import io

    f = io.StringIO("x = 3 + 4")
    t = tokenize.Tokenizer(f.readline)
    d = driver.Driver(p.grammar, p.addtoken)
    d.setup()
    for token in t.generate_tokens():
        if d.addtoken(*token):
            break
    d.finish()

    # Retrieve the abstract syntax tree
    ast = p.rootnode
    print("Abstract syntax tree:", ast)


if __name__ == "__main__":
    test_Parser_

# Generated at 2022-06-13 18:02:11.729642
# Unit test for method push of class Parser
def test_Parser_push():
    Grammar = blib2to3.pgen2.grammar.Grammar
    g = Grammar(
        blib2to3.pgen2.grammar.grammar_nt, blib2to3.pgen2.grammar.grammar_dfas
    )
    p = Parser(g)
    p.setup()
    p.push(1, (None, None), 0, None)
    assert p.stack == [(None, None), (None, 0, (1, None, None, []))]

# Generated at 2022-06-13 18:02:24.490021
# Unit test for method shift of class Parser
def test_Parser_shift():
    # pylint: disable=import-error
    from . import driver
    from . import grammar
    from io import StringIO

    class MockParser(Parser):
        def __init__(self, *args, **kwargs):
            Parser.__init__(self, *args, **kwargs)
            self.mock_stack = []

        def shift(self, *args, **kwargs):
            self.mock_stack.append((args[0], args[-1]))

    parser = MockParser(grammar.grammar, convert=lambda u, v: v)
    parser.setup(driver.test_blib2to3)

# Generated at 2022-06-13 18:02:36.545941
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Create a Grammar instance
    from . import gram, token

    g = gram.Grammar()
    # Add a token
    g.add_token(token.NUMBER, 'NUMBER')
    # Add a rule
    g.add_production('atom', ('NUMBER',), 1, None)
    g.finalize_grammar()
    # Create a Parser instance
    parser = Parser(g)

    # State before the shift method is called
    assert parser.grammar == g
    assert parser.convert == lam_sub
    assert parser.stack == []
    assert parser.rootnode is None
    # Call the shift method
    parser.shift(token.NUMBER, '5', 1, None)
    #Test the Parser instance after the shift method was called
    assert parser.grammar == g
    assert parser

# Generated at 2022-06-13 18:02:45.272640
# Unit test for method shift of class Parser
def test_Parser_shift():
    import sys
    from . import driver, token, driver_grammar
    def p_list(*args):
        return [x for x in args if x is not None]
    def p_list_rec(p):
        if len(p) == 2:
            list = p[0]
            item = p[1]
            list.append(item)
            return list
        elif len(p) == 1:
            item = p[0]
            return [item]
        else:
            return None
    def p_list_item(p):
        item = p[0]
        return item
    def p_list_item_rec(p):
        if len(p) == 2:
            list = p[0]
            item = p[1]
            list.append(item)
            return list
        el

# Generated at 2022-06-13 18:02:51.897500
# Unit test for method push of class Parser
def test_Parser_push():
    # Constructor
    gr = Grammar()
    gr.start = 257
    gr.labels = [None, None, None, None, (1, "a"), (257, None)]
    gr.transitions = [[0, 1, 2, 3], [], [], []]
    gr.dfas = [(gr.transitions, [4]), ([[(4, 0), (0, 1)]], [4])]
    gr.states = [[4], [4]]
    gr.keywords = {}
    gr.tokens = {1: 4}

    # Setup
    p = Parser(gr)
    p.setup()

    # Push
    p.push(257, gr.dfas[257], 0, None)

    # Results

# Generated at 2022-06-13 18:03:03.536601
# Unit test for method push of class Parser
def test_Parser_push():
    import blib2to3.pgen2.grammar as pgen2_grammar
    import blib2to3.pgen2.parse as pgen2_parse
    import blib2to3.pytree as pytree
    import blib2to3.fixer_util as fixer_util
    import os
    from io import BytesIO

    g = pgen2_grammar.grammar_from_file(pgen2_parse.__file__.replace('_parse.py', '.grammar'))
    f = BytesIO()
    f.write(b"123")
    f.seek(0)

    # Get tokens, which also creates a grammar object.
    tokens = list(pgen2_parse.tokenize(f))

# Generated at 2022-06-13 18:03:12.279611
# Unit test for method classify of class Parser
def test_Parser_classify():
    from .pgen import driver

    filename = 'Python.grammar'
    dg = driver.Driver(filename, 'Python.tokens')
    parser = Parser(dg.grammar)
    parser.setup()
    parser.addtoken(token.NAME, "print", None)
    parser.addtoken(token.EQUAL, "=", None)
    parser.addtoken(token.RPAR, ")", None)
    parser.addtoken(token.EOF, "<EOF>", None)


# Generated at 2022-06-13 18:03:22.303402
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys

    sys.stderr.write("Running test_Parser_addtoken...\n")
    from . import driver

    d = driver.Driver(None, None)
    g = d.grammar
    p = Parser(g)
    p.setup()
    for s in d.tokenize("if 1: pass"):
        if p.addtoken(*s):
            break



# Generated at 2022-06-13 18:03:37.529228
# Unit test for method push of class Parser
def test_Parser_push():
    class MockGrammar(object):
        start = 256
        tokens = {1: 1}
        labels = [(1, token.NAME)]
        dfas = {
            256: ([[], [(1, 1), (1, 1)]], [1])
        }  # type: Dict[int, DFAS]

    class MockNode(object):
        type: int

        def __init__(self, type: int) -> None:
            self.type = type

    class MockConvert(object):
        def __init__(self) -> None:
            self.nodes: List[MockNode] = []

        def __call__(self, grammar, node) -> MockNode:
            m = MockNode(node[0])
            self.nodes.append(m)
            return m

    c = MockConvert()

# Generated at 2022-06-13 18:03:49.912602
# Unit test for method classify of class Parser
def test_Parser_classify():
    class Grammar(object):
        def __init__(self, labels: List[Tuple[int, int]]) -> None:
            self.labels = labels
            # Map names to index numbers
            self.tokens = {}  # type: ignore
            self.keywords = {}  # type: ignore
            self.dfas = {}  # type: ignore
            self.start = 1
            self.labels = labels
    g = Grammar([(0, 0), (1, 0), (2, 0), (3, 0)])
    p = Parser(g)

    p.classify(0, "foo", None)
    p.classify(1, "foo", None)
    p.classify(2, "foo", None)
    p.classify(3, "foo", None)

# Generated at 2022-06-13 18:03:59.742263
# Unit test for method pop of class Parser
def test_Parser_pop():
    # creates a dummy grammar which has the following production rules:
    #   start: A B C
    #   A: 'A'
    #   B: 'B'
    #   C: 'C'
    #   B:
    #   C:
    # The first three rules are added twice, but the production rule
    #   C:
    # is added twice only.  This is to verify that if a production
    # rule is added twice, and the method pop() is called twice, the
    # correct production rule will be popped (and not the duplicated
    # production rule).
    import collections
    grammar = collections.namedtuple('grammar', ['dfas', 'labels', 'tokens'])
    dfas = collections.defaultdict(list)

# Generated at 2022-06-13 18:04:09.533156
# Unit test for method classify of class Parser
def test_Parser_classify():
    # Get the Python grammar
    from . import python as p
    p.initialize()
    # Construct a Parser instance
    parser = Parser(p.grammar)
    # Test classify()
    assert parser.classify(token.NAME, "class", (1, 1)) == p.syms.classdef
    assert parser.classify(token.NAME, "foo", (1, 1)) == p.tokens.NAME
    assert parser.classify(token.MINUS, "-", (1, 1)) == p.tokens.MINUS
    assert parser.classify(token.LPAR, "(", (1, 1)) == p.tokens.LPAR
    assert parser.classify(token.NEWLINE, "\n", (1, 1)) == p.tokens.NEWLINE

# Generated at 2022-06-13 18:04:16.188073
# Unit test for method classify of class Parser
def test_Parser_classify():
    import unittest
    from . import driver as pgen

    class ClassifyTestCase(unittest.TestCase):
        def _test_classify(self, token_strs):
            # These are known to succeed
            tokens = []
            grammar = pgen.pgen("Grammar.txt")
            # Create the tokens
            for token_type, token_value in token_strs:
                tokens.append((token_type, token_value, None))
            # Prepare parser
            parser = Parser(grammar)
            parser.setup()
            # Parse
            for token_type, token_value, _ in tokens:
                parser.addtoken(token_type, token_value, None)
            assert parser.rootnode is not None


# Generated at 2022-06-13 18:04:23.044027
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class MockParser(Parser):
        def __init__(self, grammar, convert=None, test=None):
            Parser.__init__(self, grammar, convert)
            assert test is not None
            self.test = test
            self.i = 0
            self.x = 0

        def classify(self, type, value, context):
            return self.test[self.i][1]

        def shift(self, type, value, newstate, context):
            self.i += 1
            self.x += 1

        def push(self, type, newdfa, newstate, context):
            self.i += 1
            self.x -= 1

        def pop(self):
            self.x += 1


# Generated at 2022-06-13 18:04:30.999256
# Unit test for method pop of class Parser
def test_Parser_pop():
    from ..pgen2.grammar import Grammar
    from ..pgen2.tokenize import tokenize_strings

    grammar = Grammar()
    # Add some rules to the grammar
    grammar.add_rule("S", [("S", ("S", "S")), "T"], lambda children: ("S", children[0]))
    grammar.add_rule("S", ["T"], lambda children: ("S", children[0]))
    grammar.add_rule("T", [("T", "T")], lambda children: ("T", children[0]))
    grammar.add_rule("T", ["NAME"], lambda children: ("T", children[0]))
    # Add some keywords to the grammar
    grammar.add_keyword("class")
    # Add some tokens to the grammar
    grammar.add_token("NAME", "\w+")


# Generated at 2022-06-13 18:04:33.915626
# Unit test for method setup of class Parser
def test_Parser_setup():
    from .grammar import Grammar, definition
    g = Grammar(definition)
    p = Parser(g)
    for s in g.symbol2number:
        p.setup(s)


# Generated at 2022-06-13 18:04:42.765910
# Unit test for method shift of class Parser
def test_Parser_shift():  # for pyre-ignore
    from . import driver
    from . import grammar
    from types import SimpleNamespace

    g = grammar.Grammar("tests/test_grammar")
    p = Parser(g)
    p.setup()
    assert p.addtoken(token.NUMBER, "2", SimpleNamespace(lineno=1, offset=0)) is False
    assert p.addtoken(token.PLUS, "+", SimpleNamespace(lineno=1, offset=2)) is False
    assert p.addtoken(token.NUMBER, "3", SimpleNamespace(lineno=1, offset=3)) is False
    assert p.addtoken(
        token.NEWLINE, "\n", SimpleNamespace(lineno=1, offset=4)
    ) is True
    assert p.rootnode
    assert "expr"

# Generated at 2022-06-13 18:04:59.742151
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class MockGrammar:
        def __init__(self, dfa, labels, kwds, toks, start):
            self.dfas = dfa
            self.labels = labels
            self.keywords = kwds
            self.tokens = toks
            self.start = start
        def __repr__(self):
            return "MockGrammar(%r, %r, %r, %r)" % (
                self.dfas, self.labels, self.keywords, self.tokens)
    dfa1 = [(1, 0), (2, 0)]
    dfa2 = [(3, 0), (4, 0)]
    dfa3 = [(5, 0), (6, 0)]
    dfa4 = [(7, 0), (8, 0)]

# Generated at 2022-06-13 18:05:02.382456
# Unit test for method setup of class Parser
def test_Parser_setup():
    """Test for class Parser, method setup"""
    p = Parser(Grammar([], [], [], [], [], [], []))
    p.setup()
    p.setup()



# Generated at 2022-06-13 18:05:09.842411
# Unit test for method shift of class Parser

# Generated at 2022-06-13 18:05:17.462229
# Unit test for method push of class Parser
def test_Parser_push():
    """
    We check if push() sets the correct new state.
    """
    from blib2to3.pgen2 import parse

    # Fill a dummy grammar with test data

# Generated at 2022-06-13 18:05:26.616022
# Unit test for method pop of class Parser
def test_Parser_pop():
    # A simple grammar with two symbols
    g = Grammar(
        start = "a",
        tokens = [],
        symbols = {
            "a": [("b", ("a", "b"))],
            "b": [("b", ("b", "c"))],
        },
    )
    p = Parser(g)
    p.setup()
    assert p.rootnode is None
    #
    #                 *a
    #                /
    #               a
    #              / \
    #            *b   b
    #           /     |
    #          b      c
    #         /
    #        b
    #       / \
    #      b   c
    #     /
    #    b
    #   /
    #  c
    #
    # The root of the Abstract Syntax Tree

# Generated at 2022-06-13 18:05:36.524194
# Unit test for method pop of class Parser
def test_Parser_pop():
    # When we call pop, we should get back the node on the top of the stack
    # and that node should return None when we call convert on it
    # We should also check to see if the other nodes are processed correctly
    # as well.
    class MockNode(list):
        def __init__(self, node_type, parent):
            self.type = node_type
            self.parent = parent
        def append(self, node):
            self.append(node)

    class MockParentNode(list):
        def __init__(self, node_type, parent):
            self.type = node_type
            self.parent = parent
        def append(self, node):
            if not self.parent:
                self.append(node)
            elif self.parent:
                self.parent.append(node)

    # Pop

# Generated at 2022-06-13 18:05:42.835586
# Unit test for method shift of class Parser
def test_Parser_shift():
    """Test case for Parser.shift."""
    from .tokenize import generate_tokens

    def _infer_parens(s: Text) -> Sequence[Tuple[int, Text]]:
        return [t for t in generate_tokens(s) if t[0] is not token.NL]

    from .pgen import load_grammar
    from .pgen import token

    grammar = load_grammar()
    parser = Parser(grammar)
    parser.setup()
    # Function with a docstring
    tokens = _infer_parens(
        'def f(a, b):\n    """Docstring."""\n    return a + b\n'
    )

# Generated at 2022-06-13 18:05:54.266759
# Unit test for method setup of class Parser
def test_Parser_setup():
    # Test the setup method of the Parser class
    import sys
    import os
    import tempfile
    from . import driver, token, pgen2
    # Use a temporary file for the output
    with tempfile.TemporaryFile("w+", encoding="utf-8") as output:
        # Construct a parser generator
        pg = pgen2.driver.Driver(output, "<unknown>")
        # Create a parser using the grammar
        parser = pg.pgen()
        if sys.version_info[:2] >= (3, 6):
            # make sure that the parser is empty
            assert parser.stack == []
            assert parser.rootnode == None
            # Set up a parser with the start symbol
            parser.setup()
            # make sure that the parser is not empty
            assert parser.stack != []
            assert parser.rootnode

# Generated at 2022-06-13 18:05:58.004507
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar

    g = grammar.Grammar()
    p = Parser(g)
    p.setup(1)
    p.setup()

# Generated at 2022-06-13 18:06:09.814050
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar as G
    from .token import INDENT, DEDENT, NAME
    p = Parser(G)
    p.setup()
    p.addtoken(NAME, "class", (1, 0))
    p.addtoken(NAME, "Foo", (1, 6))
    p.addtoken(INDENT, None, (2, 0))
    p.addtoken(NAME, "def", (2, 0))
    p.addtoken(NAME, "__init__", (2, 4))
    p.addtoken(DEDENT, None, (3, 0))
    p.addtoken(NAME, "pass", (4, 0))
    assert p.rootnode
    assert len(p.rootnode) == 1
    class_stmt = p.rootnode[0]

# Generated at 2022-06-13 18:06:31.290374
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    stack = [
        (None, 0, (None, None, None, [])),
        (None, 1, (None, None, None, [])),
        (None, 2, (None, None, None, [])),
    ]
    p = Parser(None)
    p.stack = stack
    p.grammar = None
    p.addtoken(
        1, None, [],
    )
    assert p.stack == [
        (None, 2, (None, None, None, [])),
        (None, 1, (None, None, None, [])),
        (None, 2, (None, None, None, [])),
    ]



# Generated at 2022-06-13 18:06:37.310905
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar, driver
    grammar = grammar.grammar
    driver = driver.Driver(parser=Parser, grammar=grammar)
    driver.setup()
    driver.addtoken(token.NAME, 'test', '(1, 0)')
    driver.addtoken(token.NAME, 'test', '(1, 0)')
    driver.endtoken()
    #print(driver.rootnode)
    assert driver.rootnode[0].type == grammar.syms.file_input

# Generated at 2022-06-13 18:06:48.504955
# Unit test for method pop of class Parser
def test_Parser_pop():
    """Test method pop of class Parser."""
    parser = Parser(Grammar(tokenize.grammar, convert), convert)
    parser.stack = [
        (None, None, (0, None, None, ["hello", "world", "!"])),
        (None, None, (1, None, None, [])),
        (None, None, (2, None, None, [])),
    ]
    parser.pop()
    assert parser.stack == [
        (None, None, (0, None, None, ["hello", "world", "!"])),
        (None, None, (1, None, None, [])),
    ]
    # Test unconverted node
    parser.convert = None
    parser.pop()

# Generated at 2022-06-13 18:06:53.990707
# Unit test for method push of class Parser
def test_Parser_push():
    class TestParser(Parser):
        def push(self, type: int, newdfa: DFAS, newstate: int, context: Context) -> None:
            Parser.push(self, type, newdfa, newstate, context)
            if self.stack[-1][-1][-1] is None:
                self.stack[-1][-1][-1] = []
    test_parser = TestParser(None, None)
    test_parser.setup()
    test_parser.push(0, None, 0, None)
    test_parser.push(1, None, 0, None)
    assert test_parser.stack[-1][-1][-1] == []


# Generated at 2022-06-13 18:06:56.585610
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2 import driver

    if __debug__:
        driver.ParserDriver().run_for_debugging([__file__])

# Generated at 2022-06-13 18:07:12.572524
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar
    from . import token

    g = grammar.grammar
    p = Parser(g)
    p.setup()
    assert not p.addtoken(token.NAME, "def", Context(1, 4))
    assert p.addtoken(token.NAME, "f", Context(1, 8))
    assert not p.addtoken(token.OP, "(", Context(1, 9))
    assert p.addtoken(token.OP, ")", Context(1, 10))
    assert not p.addtoken(token.OP, ":", Context(1, 11))
    assert not p.addtoken(token.NEWLINE, "\n", Context(1, 12))
    assert p.addtoken(token.INDENT, "", Context(2, 0))

# Generated at 2022-06-13 18:07:20.738389
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # The following test is written assuming the dfas was built with
    # a start symbol of 256 (file_input
    # Test []
    # Test [], ()
    # Test [], (), []
    # Test [], (), [], (), []
    # Test [], (), [], (), [], (), []
    # Test [], (), [], (), [], (), [], ()
    # Test [], (), [], (), [], (), [], (), []
    # Test [], (), [], (), [], (), [], (), [], ()
    # Test [], (), [], (), [], (), [], (), [], (), []
    from . import grammar

    g = grammar.grammar

    start = 256
    end = g.dfas[start][1][-1]
    p = Parser(g)
    p.setup(start)
    assert p

# Generated at 2022-06-13 18:07:37.203325
# Unit test for method shift of class Parser
def test_Parser_shift():
    class grammar_:
        def __init__(self):
            self.dfas = {
                0: ([([(0, 2)], 0)] * 2 + [([(0, 2)], 0)] * 2 + [([(0, 0)], 0)] * 2, {})
            }

# Generated at 2022-06-13 18:07:44.795963
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2 import graminit

    p = Parser(graminit.Grammar())
    p.setup()

    # feed a token
    p.addtoken(token.NUMBER, "3", None)
    # get the root of one-node syntax tree
    r = p.rootnode
    assert isinstance(r, Leaf)
    assert r.value == "3"
    assert r.type == token.NUMBER
    assert r.context is None

    # feed another token
    p.addtoken(token.PLUS, "+", None)
    # get the root of two-node syntax tree
    r = p.rootnode
    assert isinstance(r, Node)
    assert r.type == 294
    assert r.children
    assert len(r.children) == 1

# Generated at 2022-06-13 18:07:48.558189
# Unit test for method pop of class Parser
def test_Parser_pop():
    # See https://github.com/python/typeshed/issues/2385
    # And https://github.com/python/typeshed/pull/2386
    assert False


# Generated at 2022-06-13 18:08:28.993403
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys
    import io
    import tokenize
    from blib2to3.pgen2.grammar import Grammar

    # Create a parser
    grammar = Grammar()
    grammar.parse(io.StringIO("""
    # This is a comment
    start: s_expr
    s_expr: atom
          | "(" ")"
          | "(" s_expr seq_expr ")"
    seq_expr:
          | seq_expr s_expr
    atom: "x"
        | "y"
        | "z"
    """))
    parser = Parser(grammar)

    # Prepare for parsing
    parser.setup()

    # Make sure it works with an empty input
    t = tokenize.generate_tokens(lambda: b"")

# Generated at 2022-06-13 18:08:39.785876
# Unit test for method classify of class Parser
def test_Parser_classify():

    # Test for a token type that exists in the grammar
    p = Parser(Grammar())
    assert p.classify(token.NAME, "token", None) == 0

    # Test for a token type that does not exist in the grammar
    p = Parser(Grammar())
    try:
        p.classify(token.STRING, "token", None)
    except ParseError:
        pass
    else:
        assert False, "Token type does not exist, it should raise ParseError"

    # Test for a token value that is None
    p = Parser(Grammar())
    try:
        p.classify(token.NAME, None, None)
    except ParseError:
        pass
    else:
        assert False, "Token value should not be None, it should raise ParseError"

   

# Generated at 2022-06-13 18:08:47.447316
# Unit test for method push of class Parser
def test_Parser_push():
    from . import driver
    from . import test_grammar as test_grammar
    import re

    p = Parser(test_grammar)
    p.setup()
    driver.add_tokens(p, re.split(r'\s+', 'suite: simple_stmt endl ENDMARKER'))
    # assert p.stack[0][2] == (337, None, None, [(2, None, None, [(5, None, None, [(1, 'suite', None, None)])])])
    assert p.stack[0][2][3] == [(5, None, None, [(1, "suite", None, None)])]
    p.pop()
    assert p.stack == []
    assert p.rootnode.prefix == "suite"

# Generated at 2022-06-13 18:09:04.182349
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar, tokens
    from .pygram import python_symbols as syms
    from .pygram import python_operators as ops
    from blib2to3.pgen2.parse import parse_grammar
    p = Parser(parse_grammar(grammar.grammar, tokens))
    p.setup()
    p.addtoken(syms.decorator, None, (1, 0))
    p.addtoken(syms.decorated, None, (1, 0))
    p.addtoken(syms.decorator, None, (1, 0))
    p.addtoken(stmt, None, (1, 0))
    p.addtoken(ops.ENDMARKER, None, (1, 0))

# Generated at 2022-06-13 18:09:17.611114
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    grammar = Grammar([
        ("r0",
         [("r1", "r2")]),
        ("r1",
         [("r2", "r3")]),
        ("r2",
         [("ID",)])])
    from blib2to3.pgen2.driver import Driver
    p = Parser(grammar, None)
    d = Driver()
    d.set_grammar(grammar)
    d.prepare()
    p.setup()
    for tree in d.parse_tokens([(3, "id"), (3, "id"), (3, "id")]):
        assert tree.children[0].children[0].children[0].value == "id"
        assert tree.children[0].children[1].children[0].value == "id"
        assert tree.children

# Generated at 2022-06-13 18:09:23.013339
# Unit test for method shift of class Parser
def test_Parser_shift():
    import unittest
    import blib2to3.pgen2
    #from blib2to3.pygram import python_symbols as syms
    import blib2to3.pygram
    from blib2to3 import pytree

    class ParseErrorTest(unittest.TestCase):
        """Testcase for the Parser engine."""

        #def _test_ParseError(self, input, type, value, context, msg):
        #    self._test_lexer(input, tokenize.generate_tokens)
        #    parser = Parser(blib2to3.pgen2.grammar)
        #    parser.setup()
        #    try:
        #        parser.addtoken(type, value, context)
        #        self.fail("Expected ParseError")


# Generated at 2022-06-13 18:09:37.333508
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    p = Parser(grammar, lam_sub)
    p.setup()


# Generated at 2022-06-13 18:09:40.119432
# Unit test for method setup of class Parser
def test_Parser_setup():
    def test_func1(grammar, node):
        return node

    test_obj = Parser(grammar=None, convert=test_func1)
    r = test_obj.setup(start=None)
    return r


# Generated at 2022-06-13 18:09:43.217182
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    gram1 = grammar.Grammar()
    p = Parser(gram1)
    p.setup()
    for i in range(5):
        p.addtoken(token.NAME, "x" + str(i), Context(i, i))
    assert p.rootnode is not None

# Generated at 2022-06-13 18:09:44.685427
# Unit test for method setup of class Parser
def test_Parser_setup():
    test_Parser_setup.__self__.setup()


# Generated at 2022-06-13 18:11:03.354529
# Unit test for method push of class Parser
def test_Parser_push():
    import os
    from . import gram, driver
    from . import _ast
    # This code relies on the fact that token IDs are 1,2,...
    grammar = gram.Grammar()
    grammar.method = "LALR"
    grammar.start = "start"

# Generated at 2022-06-13 18:11:12.994710
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """Test the method addtoken of class Parser"""
    from .grammar import Grammar

    pg = Grammar()
    p = Parser(pg)

    try:
        p.addtoken(1, "hello", (0, 0))
        assert False
    except ParseError:
        pass

    p.setup()

    assert not p.addtoken(token.LPAR, "(", (0, 0))
    assert p.addtoken(token.RPAR, ")", (0, 0))

    p.setup()

    assert not p.addtoken(token.NAME, "a", (0, 0))
    assert p.addtoken(token.NEWLINE, "\n", (0, 0))

    p.setup()

    assert not p.addtoken(token.NAME, "a", (0, 0))
    assert not p

# Generated at 2022-06-13 18:11:19.668607
# Unit test for method setup of class Parser
def test_Parser_setup():
    def _check_Parser_setup(
        grammar: Grammar,
        convert: Optional[Convert] = None,
        start: Optional[int] = None,
        stack: Sequence[Tuple[DFAS, int, RawNode]] = [(grammar.dfas[grammar.start],0,(grammar.start,None,None,[]))],
        rootnode: Optional[int] = None,
        used_names: Set[str] = set()
    ) -> None:
        p = Parser(grammar, convert)
        p.setup(start)
        assert p.stack == stack
        assert p.rootnode == rootnode
        assert p.used_names == used_names
    # Check with default values
    _check_Parser_setup(grammar)
    # Check with custom values
    # TODO: If possible

# Generated at 2022-06-13 18:11:27.840324
# Unit test for method shift of class Parser
def test_Parser_shift():
    # build a dummy grammar
    from blib2to3.pgen2.token import Token
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pgen2.parse import ParseError
    foo = Token("foo", 1, passthrough=True)
    grammar = Grammar(dict(start = ([foo], None), foo = (("bar", "baz"), None)),
                      {}, {}, {}, {}, {})
    
    def lam_sub(grammar, node):
        dfa, state, node = node
        return dfa, state, node  # just return the unmodified node
    
    parser = Parser(grammar, lam_sub)
    parser.setup()
    
    # test a token with token.NAME