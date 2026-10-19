

# Generated at 2022-06-13 18:01:49.858859
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver   # For Driver class
    from . import parsetok # For Parser class

    # Create a grammar and an instance of Parser
    d = driver.Driver(parsetok.pgen, convert=lam_sub)
    p = Parser(d.grammar)

    # Test tokens
    tokens = [(token.NAME, 'a'), (token.NAME, 'b'), (token.NEWLINE, '\n')] * 3
    # Get the expected result
    expected = [
        [token.NAME, 'a'],
        None,
        [token.NAME, 'b'],
        None,
        token.NEWLINE
    ] * 3
    expect_end_parsing = True

    # Prepare the parser, then add the tokens
    p.setup()

# Generated at 2022-06-13 18:01:58.755658
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:02:07.836195
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver, tokenizer
    from .driver import Driver, EXPECT, EXPECT_ERROR

    # Unit test for method addtoken of class Parser, case 1
    def test_case1(driver, gram,
                   inp, exp, exp_err):
        # case 1 of calling addtoken of Parser,
        # when the token is eof, or when the token is not eof and
        # the state of stack does not have a transition for the token

        # reset
        parser.setup(grammar.start)
        lexer.setup(inp)

        # tokenize
        tok = lexer.gettoken()
        if (tok[0] == token.ENDMARKER):
            return


# Generated at 2022-06-13 18:02:15.757291
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # Need a grammar first
    from . import driver

    grammar, symbols, _ = driver.load_grammar("Python.asdl")
    p = Parser(grammar)
    p.setup()
    p.addtoken(token.NUMBER, "1", None)
    p.addtoken(token.NAME, "a", None)
    p.addtoken(token.DOT, ".", None)
    p.addtoken(token.NAME, "b", None)

# Generated at 2022-06-13 18:02:23.838166
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import pprint, time
    import unittest

    # Make a few tokens
    class Token:
        def __init__(self, type, value):
            self.type = type
            self.value = value
            # Token instances must have a lineno and lexpos
            # attribute for the parser to work
            self.lineno = 2
            self.lexpos = 2

        def __repr__(self):
            return "Token(%r, %r)" % (self.type, self.value)

    t1 = Token("NAME", "foo")
    t2 = Token("PLUS", "+")
    t3 = Token("NAME", "bar")
    t4 = Token("STAR", "*")
    t5 = Token("NAME", "baz")

    # Make a parser
    grammar = Grammar()

# Generated at 2022-06-13 18:02:26.241107
# Unit test for method shift of class Parser
def test_Parser_shift():
    assert Parser(None).shift(1, 2, 3, None) == None


# Generated at 2022-06-13 18:02:37.981420
# Unit test for method pop of class Parser
def test_Parser_pop():
    import copy
    g = Grammar(open("Grammar.txt"))
    # A sample parser engine
    p = Parser(g)
    # Some random data
    dfa = [
        [(1, 0), (2, 0)],
        [(0, 1)],
        [(0, 2)],
        [(0, 3)],
    ]
    state = 2
    node = (token.STRING, "foobar", (1, 1), [])
    stack = [
        (dfa, state, node),
        (dfa, state, node),
    ]
    p.stack = stack
    p.pop()
    # Check for clobbering
    assert stack == [(dfa, state, node)]
    assert p.stack == [(dfa, state, node)]
    # Check for copy.deepcopy

# Generated at 2022-06-13 18:02:48.169130
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar
    from .tokens import tokens
    from blib2to3.pgen2.parse import ParseError

    # Test with parsing an empty input
    p = Parser(grammar.grammar, convert=None)
    p.setup(grammar.suite_stmt)
    with pytest.raises(ParseError):
        p.pop()
    assert p.rootnode is None

    # Test with converting nodes but no node to convert
    p = Parser(grammar.grammar, convert=lam_sub)
    p.setup(grammar.suite_stmt)
    p.addtoken(tokens.NEWLINE, "", (1, 0))
    with pytest.raises(ParseError):
        p.pop()
    assert p.rootnode is None


#

# Generated at 2022-06-13 18:02:58.067071
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():

    # Initialize the parser
    parser = Parser(Grammar())

    # Test 1
    parser.setup()
    # Validate the parser
    assert parser.stack == [(parser.grammar.dfas[256], 0, (256, None, None, []))]
    assert parser.rootnode == None
    assert parser.used_names == set([])

    # Test 1.1
    parser.addtoken(token.NAME, 'input', (2, 0))
    # Validate the parser
    assert parser.stack == [
        (parser.grammar.dfas[256], 8, (256, None, None, [(1, 'input', (2, 0), None)])),
    ]
    assert parser.rootnode == None
    assert parser.used_names == set(['input'])

    # Test 1.2


# Generated at 2022-06-13 18:03:08.831521
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import python_grammar, python_symbol
    import test_pgen

    class MockParser(Parser):
        def __init__(self, grammar: Grammar, convert: Optional[Convert] = None) -> None:
            Parser.__init__(self, grammar, convert)
            self.labels = []

        def classify(
            self, type: int, value: Optional[Text], context: Context
        ) -> int:
            ilabel = Parser.classify(self, type, value, context)
            self.labels.append((type, value, context, ilabel))
            return ilabel

    class MockGrammar(Grammar):
        def __init__(self, *args, **kwds):
            Grammar.__init__(self, *args, **kwds)
            self.lab

# Generated at 2022-06-13 18:03:26.302164
# Unit test for method pop of class Parser
def test_Parser_pop():
    def convert(grammar, node):
        if node[0] == grammar.symbol2number['simple_stmt']:
            return node[3][0]
        elif node[0] == grammar.symbol2number['if_stmt']:
            return Node(type='if_stmt', children=node[3])
        else:
            return Node(type=grammar.number2symbol[node[0]], children=node[3])

    import test.test_parser
    p = Parser(test.test_parser.grammar, convert)
    p.setup()
    p.addtoken(token.IF, 'if', (1, 0))
    p.addtoken(token.NAME, 'x', (1, 3))
    p.addtoken(token.COLON, ':', (1, 4))

# Generated at 2022-06-13 18:03:39.195898
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Create a parser instance
    import blib2to3.pgen2.parse

    g = blib2to3.pgen2.parse.load_grammar()
    p = Parser(g, lam_sub)
    # Start parsing
    p.setup()
    # Add a token
    p.addtoken(token.NAME, "print", (1, 0))
    # Check the state
    assert p.stack == [
        (
            g.dfas[1],
            1,
            (1, None, None, [Node(type=1, children=[Leaf(type=1, value="print")])]),
        )
    ]
    # Complete the parsing
    p.addtoken(1, "(", (1, 0))
    p.addtoken(1, "42", (1, 0))
    p

# Generated at 2022-06-13 18:03:51.090254
# Unit test for method classify of class Parser
def test_Parser_classify():
    import os
    import sys
    from blib2to3.pgen2 import driver
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pgen2.parse import ParseError

    stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')

# Generated at 2022-06-13 18:04:01.762414
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import word
    from .pgen import generate_grammar

    parser = Parser(generate_grammar(word))
    parser.setup()
    assert parser.addtoken(token.NAME, "zero", (1, 0)) is True
    assert parser.rootnode.leaf == "zero"
    assert parser.rootnode.children == []

    parser.setup()
    assert parser.addtoken(token.NAME, "one", (1, 0))
    assert parser.addtoken(token.PLUS, "+", (1, 1))
    assert parser.addtoken(token.NAME, "two", (1, 2))
    assert parser.addtoken(token.EQUAL, "=", (1, 3))
    assert parser.addtoken(token.NAME, "three", (1, 4))

# Generated at 2022-06-13 18:04:11.410120
# Unit test for method pop of class Parser
def test_Parser_pop():
    class MyParser(Parser):
        def pop(self) -> None:
            return super().pop()

    p = MyParser(Grammar(None), None)
    p.stack: List[Tuple[DFAS, int, RawNode]] = [(None, 0, RawNode(None, None, None, None))]
    p.rootnode = None
    p.used_names = set()
    assert p.pop() is None
    assert p.stack == []
    assert p.rootnode is None
    assert p.used_names == set()

    p = MyParser(Grammar(None), None)
    p.stack = [(None, 0, RawNode(None, None, None, None))]
    p.rootnode = None
    p.used_names = set()
    assert p.pop() is None

# Generated at 2022-06-13 18:04:18.012226
# Unit test for method shift of class Parser
def test_Parser_shift():
    class TestConvert:
        def __init__(self) -> None:
            self.type = None  # type: Optional[int]
            self.value = None  # type: Optional[Text]
            self.context = None  # type: Context
            self.children = None  # type: Optional[Sequence[Any]]

        def __call__(self, grammar: Grammar, node: RawNode) -> Any:
            self.type, self.value, self.context, self.children = node
            return None

    convert = TestConvert()
    parser = Parser(Grammar(), convert)
    parser.stack = [(None, None, None)]
    parser.shift(1, "1", 2, (1, 1))
    assert convert.type == 1
    assert convert.value == "1"
    assert convert.context

# Generated at 2022-06-13 18:04:28.494219
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest
    import sys
    import blib2to3.refactor as refactor

    class ParserTest(unittest.TestCase):
        def setUp(self):
            grammar = refactor.get_fixers_package(
                "lib2to3.fixes").Grammar(
                sys.modules[__name__].__file__, "Grammar.txt", "grammar")
            self.parser = Parser(grammar)
            self.parser.setup("file_input")
        def test_Parser_addtoken(self):
            self.assertFalse(self.parser.addtoken(0, "", (0, 0)))
            self.assertFalse(self.parser.addtoken(0, "", (0, 0)))

# Generated at 2022-06-13 18:04:38.575892
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    def dfa(n: int) -> DFAS:
        return ([[(n, n)]], {n: n})

    # Test both branches of 'if ilabel == 0', at the top level
    p = Parser(Grammar([[0, "", "", [], [], {}]]))
    p.setup()
    p.addtoken(1, "A", (1, 1))  # Pop and expect another token
    # Test the shift and push & pop branches
    p = Parser(Grammar([[0, "", "", [], [], {}], [1, "", "", [], [], {}]]))
    p.setup()
    p.addtoken(1, "A", (1, 1))
    # Test the 'while' loop for shifting

# Generated at 2022-06-13 18:04:50.888845
# Unit test for method shift of class Parser
def test_Parser_shift():
    def mock_raw_node(token_type=None, value=None, context=None):
        return token_type, value, context, None
    def mock_update_node(grammar, node):
        return node
    grammar = Grammar([], [], [], [], [], [], [], {})
    parser = Parser(grammar, convert=mock_update_node)
    dfa = [
        [(1, 1), (2, 3)],
        [(0, 1)],
        [(0, 3)],
        [(0, 3)],
        [(0, 4)],
    ]

# Generated at 2022-06-13 18:05:02.514609
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:05:25.184194
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver

    g = driver.load_grammar("Python.gram")
    p = Parser(g)

    # A single node with no children.
    p.pop()
    assert p.rootnode is None

    # A single node with one child.
    p.push(1, p.grammar.dfas[1], 0, None)
    n1: RawNode = (1, None, None, [])
    n2: RawNode = (2, "twenty", Context(1, 0), None)
    p.stack[-1] = (p.grammar.dfas[1], 0, n1)
    p.shift(2, "twenty", 1, Context(1, 0))
    p.pop()
    assert p.rootnode.type == 1

# Generated at 2022-06-13 18:05:35.635463
# Unit test for method shift of class Parser
def test_Parser_shift():
    class FakeGrammar:
        def __init__(self):
            self.dfas = {1: ([[(3, 0), (0, 1)], [(4, 2), (0, 1)], [(0, 1)], [(0, 1)]], {0: 1, 1: 2, 2: 3, 3: 4})}
            self.labels = {3: (256, 'x'), 4: (257, 'y')}
            self.tokens = {256: 4, 257: 4}

    class FakeObject:
        def __init__(self):
            self.grammar = FakeGrammar()
            self.convert = lambda s, t: t
            self.stack = [(self.grammar.dfas[1], 1, None)]

    f = FakeObject()

# Generated at 2022-06-13 18:05:45.441332
# Unit test for method push of class Parser
def test_Parser_push():
    import io
    import os
    import sys
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pgen2.tokenize import generate_tokens
    from blib2to3.pgen2.parse import Parser, ParseError
    from blib2to3.pgen2.convert import convert_tree
    from blib2to3.pygram import python_grammar
    from blib2to3.pygram import python_symbols as syms
    from blib2to3.pgen2.pgen import GrammarError
    g = Grammar(python_grammar)
    p = Parser(g)
    p.setup(syms.file_input)

# Generated at 2022-06-13 18:05:56.377837
# Unit test for method pop of class Parser
def test_Parser_pop():
    grammar = Grammar(r"""
    p: "1" "+" "2"
    """)

    def convert(grammar, node):
        return node

    p = Parser(grammar, convert)

    p.setup()
    dfa, state, node = p.stack[-1]
    assert dfa == grammar.dfas[1]
    assert state == 0
    assert node == (1, None, None, [])

    p.addtoken(token.NUMBER, "1", None)
    dfa, state, node = p.stack[-1]
    assert dfa == grammar.dfas[1]
    assert state == 1
    assert node == (1, None, None, [(token.NUMBER, "1", None, None)])

    p.addtoken(43, "+", None)
    d

# Generated at 2022-06-13 18:06:06.051187
# Unit test for method pop of class Parser
def test_Parser_pop():
    class Mock:
        def __init__(self) -> None:
            self.converted = []  # type: List[Any]
            self.dfas: Dict[int, DFAS] = {}

        def convert(self, grammar: Grammar, node: RawNode) -> Optional[Any]:
            converted = self.converted.append
            converted(node)
            return node

    # Create a test parser
    m = Mock()
    m.dfas[0] = ([[(1, 0), (2, 1), (3, 2)]], {0: 0, 1: 1, 2: 0, 3: 0})
    p = Parser(m, m.convert)
    p.setup(0)
    p.addtoken(None, 1, None)
    p.addtoken(None, 2, None)
   

# Generated at 2022-06-13 18:06:10.932199
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:06:18.019989
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver

    tree = driver.parse_string("a = 1")
    tree = driver.parse_file("pgen2/a.py")  # Does not actually reach a real file
    tree = driver.parse_file("../blib2to3/pgen2/a.py")

    # Now do partial parsing...
    p = Parser(grammar.grammar)
    p.setup()
    p.addtoken(token.NAME, "a", (1, 0))
    p.addtoken(token.EQUAL, "=", (1, 2))
    p.addtoken(token.NUMBER, "1", (1, 4))
    p.addtoken(token.NEWLINE, "", (1, 5))


# Generated at 2022-06-13 18:06:22.653366
# Unit test for method classify of class Parser
def test_Parser_classify():
    from .driver import Driver
    d = Driver()
    p = Parser(d.grammar)
    assert p.classify(token.NAME, 'foo', None) == 1
    assert p.classify(token.STRING, 'foo', None) == 3

# Generated at 2022-06-13 18:06:31.472056
# Unit test for method pop of class Parser
def test_Parser_pop():
    import unittest
    import textwrap

    class TestParser(unittest.TestCase):
        def compare_nodes(self, expected, actual):
            self.assertEqual(expected.type, actual.type)
            self.assertEqual(expected.value, actual.value)
            self.assertEqual(expected.children, actual.children)

        def test_pop(self):
            grammar = Grammar(textwrap.dedent("""\
                stmt: simple_stmt | compound_stmt
                simple_stmt: 'pass'
                compound_stmt: simple_stmt
                """))
            parser = Parser(grammar)
            parser.setup()
            parser.addtoken(token.NAME, "pass", Context(1, 0))

# Generated at 2022-06-13 18:06:37.705732
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar
    from . import tokenize
    import io
    import sys

    class FakeGrammar(grammar.Grammar):
        def __init__(self, symbol_map, token_list, keywords, labels):
            super().__init__()
            self.symbol2number = symbol_map
            self.number2symbol = {v: k for k, v in symbol_map.items()}
            self.tokens = token_list
            self.keywords = keywords
            self.labels = labels

    teststr = """print(1+2) # comment"""

# Generated at 2022-06-13 18:06:54.230169
# Unit test for method shift of class Parser
def test_Parser_shift():
    grammar = Grammar()
    parser = Parser(grammar)
    parser.setup()
    parser.shift(1, 'a', 2, None)
    assert parser.stack == [(None, 2, None)]
    parser.shift(1, 'b', 3, None)
    assert parser.stack == [(None, 3, None)]


# Generated at 2022-06-13 18:07:01.841153
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .grammar import Grammar
    from .pgen import write_grammar

    # add new symbol 'MySymbol' with value 10
    g = Grammar(write_grammar)
    g.add_symbol("MySymbol", 10)

    # create parser
    p = Parser(g)
    p.setup()

    # create token
    type = token.NAME
    value = "MySymbol"
    context = (1, 0)

    # classify token to symbol by 'classify' method
    ilabel = p.classify(type, value, context)

    # do shift
    dfa, state, node = p.stack[-1]
    states, first = dfa
    arcs = states[state]
    # Look for a state with this label
    for i, newstate in arcs:
        t

# Generated at 2022-06-13 18:07:17.872526
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # This test is based on Lib/test/test_pgen.py, method test_expr.
    import Grammar as Grammar, Driver as Driver
    g = Grammar.Grammar("Grammar/Grammar", "single")
    d = Driver.Driver(g.grammar, g.start, g.dfas)
    p = Parser(g.grammar, lambda grammar, node: node)
    p.setup()
    while True:
        if p.addtoken(d.type, d.value, d.context):
            break
        d.next()
    node = p.rootnode
    assert node[0] == g.start
    assert node[1] is None
    assert node[2] is None
    assert node[3] is not None
    expr = node[3][0]
    assert expr

# Generated at 2022-06-13 18:07:34.400121
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import pprint
    from ..pgen2 import token, driver

    if __name__ == '__main__':
        # Only run in self-test mode
        grammar = driver.load_grammar('Grammar/Grammar')
    else:
        # Initialize the grammar variables
        from . import grammar, literals

        literals.initialize_literals()
        grammar.initialize_grammar()

    # pylint: disable=redefined-outer-name
    # This is OK; we want to test it.
    def run_test(source, type, value, expect):
        """Unit test helper for Parser.addtoken."""
        # (Re)initialize the parser
        p = Parser(grammar)
        p.setup()
        # Create a contextualized dummy token

# Generated at 2022-06-13 18:07:42.152222
# Unit test for method pop of class Parser
def test_Parser_pop():
    class AllNewNode(object):
        pass
    newnode = AllNewNode()
    p = Parser(None)
    p.stack = [('dfa', 'state', 'node')]
    p.convert = lambda grammar, node: newnode
    p.pop()
    assert p.stack == [('dfa', 'state', 'node')]
    assert p.rootnode == newnode
    del p.stack[0]
    dfa, state, node = p.stack.pop()
    assert p.stack == []
    assert dfa == 'dfa'
    assert state == 'state'
    assert node == ['node', newnode]



# Generated at 2022-06-13 18:07:55.534706
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2 import driver, tokenize
    parser = driver.load_grammar("Grammar.txt").parser
    testcases = [
        ("1", "NUMBER", "1"),
        ("!=", "NOTEQUAL", "!="),
        ("a", "NAME", "a"),
        ("if", "IF", "if"),
        ("True", "NAME", "True"),
        ("False", "NAME", "False"),
        ("None", "NAME", "None"),
        ("abcdefg", "NAME", "abcdefg"),
        (" ", "INDENT", " "),
        ("\t", "INDENT", "\t"),  # for better error messages
    ]

# Generated at 2022-06-13 18:08:04.235573
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar
    from blib2to3.pgen2 import token

    argv = ["--Grammar.txt"]
    g = grammar.grammar(argv)
    p = Parser(g)
    p.setup()
    p.addtoken(token.NEWLINE, "\n", (1, 0))

    # A name
    assert p.classify(token.NAME, "foo", (1, 0)) == 256
    # A keyword
    assert p.classify(token.NAME, "and", (1, 0)) == 0
    # A punctuation symbol
    assert p.classify(token.LPAR, "(", (1, 0)) == 3
    # An operator
    assert p.classify(token.VBAR, "|", (1, 0)) == 6
    # A string
    assert p

# Generated at 2022-06-13 18:08:15.289381
# Unit test for method push of class Parser
def test_Parser_push():
    from blib2to3.pgen2.tokenize import generate_tokens, TokenInfo
    from blib2to3.pgen2 import driver
    import io
    f = io.StringIO("import sys")
    lst = list(generate_tokens(f.readline))
    f.close()
    drv = driver.Driver(b"blib2to3.fixes", "test")
    p = Parser(drv.grammar, drv.convert)
    p.setup()
    p.addtoken(lst[0][0], lst[0][1], TokenInfo(lst[0][0], lst[0][1], 0, 0, (1, 0), (1, 6), ""))

# Generated at 2022-06-13 18:08:23.351117
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import dfas
    from . import tokens

    grammar = Grammar(dfas, tokens)

    p = Parser(grammar)
    p.setup()
    p.addtoken(1, "ab", None)
    p.addtoken(3, "cd", None)
    p.addtoken(5, "ef", None)
    p.pop()

    while True:
        try:
            if p.addtoken(5, "ef", None):
                break
        except ParseError:
            break


__all__ = ["ParseError", "Parser"]

# Generated at 2022-06-13 18:08:30.649930
# Unit test for method push of class Parser
def test_Parser_push():
    grammar = Grammar()
    # Load grammar tables
    import os
    import sys
    import blib2to3.pgen2.driver as driver
    sys.modules["driver"] = driver
    here = os.path.dirname(os.path.realpath(__file__))
    # Load grammar
    gramfile = "Grammar.txt"
    if sys.version_info >= (3, 6):
        gramfile = "Grammar3.6.txt"
    driver.load_grammar(grammar, gramfile, here)
    parser = Parser(grammar)
    parser.setup()
    parser.addtoken(token.INDENT, "  ", None)
    parser.addtoken(token.NAME, "a", None)
    assert parser.stack[-1][2][-1][0] == symbol

# Generated at 2022-06-13 18:09:07.280381
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pgen2.parse import ParseError
    from blib2to3.pgen2.tokenize import generate_tokens, untokenize
    import unittest

    class ParserTest(unittest.TestCase):
        def test_pop(self):
            # The tokens that make up the grammar
            tokens = {
                "NAME": "ID",
                "OP": "OP",
                "COMMA": ",",
                "RIGHTBRACKET": "]",
            }

            # The nonterminals
            nt_list = "list"
            nt_item = "item"

            # The rules

# Generated at 2022-06-13 18:09:08.926880
# Unit test for method shift of class Parser
def test_Parser_shift():
    raise NotImplementedError


# Generated at 2022-06-13 18:09:23.017144
# Unit test for method pop of class Parser
def test_Parser_pop():
    def check(st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12, st13, st14, st15, st16, st17):
        if (st1 != "        " or st2 != "        " or st3 != "        " or st4 != "        " or st5 != "        " or st6 != "        " or st7 != "        " or st8 != "        " or st9 != "        " or st10 != "        " or st11 != "        " or st12 != "        " or st13 != "        " or st14 != "        " or st15 != "        " or st16 != "        " or st17 != "        "):
            raise Exception("stack is corrupted")
    def nodify(node):
        return node

# Generated at 2022-06-13 18:09:34.450263
# Unit test for method classify of class Parser
def test_Parser_classify():
    """Unit test for method classify of class Parser"""

    p = Parser(Grammar())

    def check(t, v, c, result):
        # This is ugly; we don't want to expose the internal
        # implementation of the grammar object.
        g = p.grammar
        assert p.classify(t, v, c) == g.keywords.get(v) or g.tokens[t]

    # Check a few tokens
    for t, v in [(token.PLUS, "+"), (token.NAME, "and"), (token.NUMBER, "42")]:
        check(t, v, None, t)

    # Check reserved words

# Generated at 2022-06-13 18:09:46.474372
# Unit test for method shift of class Parser
def test_Parser_shift():
    def gen_pgen_grammar():
        class grammar(Grammar):
            def __init__(self):
                self.dfas = {1: (
                    [[(1, 1), (1, 1)], [(1, 1), (1, 1)]],
                    {1: 1, 2: 0}
                )}
                self.labels = [(1, 1), (1, 1)]
                self.start = 1
                self.tokens = {1: 1}
            def p_1(self, args):
                return args[0]

        return grammar()

    parser = Parser(gen_pgen_grammar())
    parser.setup()

# Generated at 2022-06-13 18:09:53.967185
# Unit test for method setup of class Parser
def test_Parser_setup():
    """Unit test for method setup of class Parser"""
    from pprint import pprint
    from . import token

    # Test cases

# Generated at 2022-06-13 18:10:01.760713
# Unit test for method push of class Parser
def test_Parser_push():
    from . import driver
    from .pgen import generate_grammar
    import sys
    import os

    python_grammar = generate_grammar(sys.version_info >= (3, 6))
    parse = driver.driver(python_grammar, convert=lam_sub)
    p = Parser(python_grammar, convert=lam_sub)
    p.setup()
    p.push(1, "a", 2, 3)
    p.push(2, "b", 3, 4)
    p.push(3, "c", 4, 5)
    p.pop()
    p.pop()
    p.pop()
    print(p.stack)
    print(p.rootnode)

# Generated at 2022-06-13 18:10:13.257211
# Unit test for method push of class Parser
def test_Parser_push():
    import sys

    from . import grammar, tokenize, token

    # Test data
    # See the doc string for pgen.
    grammar1 = """\
      calc: item ('+' item)* ;
      item: 'num' | '(' calc ')' ;
    """


# Generated at 2022-06-13 18:10:22.657632
# Unit test for method pop of class Parser
def test_Parser_pop():
    class TestGrammar(object):
        """A fake grammar for testing."""
        def __init__(self) -> None:
            self.dfas = {
                "A": ([[(-1, -1)], [(-1, -1)], [(-1, -1), (0, 2)]], {}),
                "B": ([[(-1, -1)], [(-1, -1)], [(-1, -1), (0, 2)]], {}),
                "D": ([[(-1, -1), (1, 1)], [(0, 0), (-1, -1)], [(-1, -1), (0, 1)]], {}),
            }
            self.labels = [(256, "A"), (257, "B"), (258, "D")]
            self.tokens = {}
           

# Generated at 2022-06-13 18:10:33.141451
# Unit test for method classify of class Parser
def test_Parser_classify():
    import pprint
    from blib2to3.pgen2 import tokenize

    def get_token_names(source_text, version=None):
        '''Get the token names of the tokens in `source_text`.'''
        tokens, _ = tokenize.generate_tokens(
            iter(source_text).__next__, version=version)
        return [token.__name__ for (_, token, _, _, _) in tokens]

    import os
    import re
    import sys
    from . import pgen

    def dump_tokens(tokens):
        for tok in tokens:
            t, v = tok
            name = token.tok_name.get(t)
            if v >= ' ' and v <= '~':
                tok = name + ":" + v
           