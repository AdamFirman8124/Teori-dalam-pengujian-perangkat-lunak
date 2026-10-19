

# Generated at 2022-06-13 18:01:48.056688
# Unit test for method classify of class Parser
def test_Parser_classify():
    from _frozen_importlib.builtins import FrozenModuleError
    import sys
    import builtins
    try:
        del builtins.__dict__['frozentest']
    except KeyError:
        pass
    except AttributeError:
        pass
    sys.modules['frozentest'] = object()
    from . import frozentest
    from . import parser

    p = parser.Parser(grammar=frozentest.grammar)
    num_code = p.classify(token.NUMBER, '0', (1, 1))
    str_code = p.classify(token.STRING, '"0"', (1, 2))
    name_code = p.classify(token.NAME, 'frozentest', (1, 3))

# Generated at 2022-06-13 18:01:55.699250
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver
    from . import cst_to_ast

    start = 999
    grammar = Grammar("grammar.txt")
    grammar.compile()
    p = Parser(grammar, cst_to_ast.convert)
    p.setup(start)
    p.addtoken(3, 'str', (1, 0))
    p.addtoken(3, 'str', (1, 0))
    p.addtoken(1, '+', (1, 0))
    p.addtoken(3, 'str', (2, 0))
    p.addtoken(3, 'str', (2, 0))
    p.addtoken(1, '+', (2, 0))
    p.addtoken(3, 'str', (3, 0))
    assert p.rootnode.type == start


# Generated at 2022-06-13 18:02:04.676446
# Unit test for method shift of class Parser
def test_Parser_shift():
    import unittest
    import warnings
    import blib2to3.pgen2.token as token
    import blib2to3.pgen2.grammar as grammar

    class TestParserShift(unittest.TestCase):
        def setUp(self):
            self.parser = Parser(grammar.Grammar())

        def test_bad_type(self):
            with self.assertRaises(ParseError):
                self.parser.shift(token.NAME, 'abcdefg', 0, None)

        def test_bad_value(self):
            with self.assertRaises(ParseError):
                self.parser.shift(token.NEWLINE, None, 0, None)

        def test_bad_context(self):
            with self.assertRaises(ParseError):
                self.parser.shift

# Generated at 2022-06-13 18:02:17.952195
# Unit test for method classify of class Parser
def test_Parser_classify():

    class TestParser(Parser):
        def __init__(self, grammar: Grammar):
            super().__init__(grammar)

        def classify(self, type: int, value: Optional[Text], context: Context) -> int:
            ilabel = super().classify(type, value, context)
            if type == token.NAME:
                if ilabel is None:
                    # This is a non-reserved name
                    return self.grammar.labels[-1][1]
            return ilabel

    class TestGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.tokens = {
                token.NAME: 1,
                token.NUMBER: 2,
                token.STRING: 3,
            }


# Generated at 2022-06-13 18:02:24.815099
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver, pgen
    from .grammar import Grammar
    from .tokenize import tokenize

    grammar = pgen.load_grammar("")
    parser = Parser(grammar)
    parser.setup()
    tokens = list(tokenize("@a"))
    parser.addtoken( tokens[0][0], tokens[0][1], Context(1, 0, "") )
    parser.addtoken( tokens[1][0], tokens[1][1], Context(1, 1, "") )



# Generated at 2022-06-13 18:02:31.253032
# Unit test for method shift of class Parser
def test_Parser_shift():
    parser = Parser(Grammar())
    parser.stack = [([[(0, 1)], [(1, 2)]], 1, 'node')]
    parser.shift(1, 'value', 2, 'context')
    assert parser.stack == [([[(0, 1)], [(1, 2)]], 2, 'node')]


# Generated at 2022-06-13 18:02:40.627047
# Unit test for method push of class Parser
def test_Parser_push():
    from .tokenize import generate_tokens
    from . import grammar, token
    
    # Create a parser instance
    p1 = Parser(grammar)
    
    # Prepare for parsing; called automatically by the constructor
    p1.setup()
    
    def addtokens(s: str) -> bool:
        type, value, context, line = generate_tokens(s).__next__()
        return p1.addtoken(type, value, context)
    
    # Push a nonterminal
    assert addtokens('if ') is False
    assert addtokens('True:') is False
    assert addtokens('None') is True
    

# Generated at 2022-06-13 18:02:48.293617
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest

    from .driver import Driver
    from . import parsetok

    class TestParser(unittest.TestCase):
        def _test_Parser_addtoken(self, grammar, input, output):
            driver = Driver(grammar, convert=None)
            for i, t in enumerate(reversed(input)):
                type, value, context = t
                if driver.parser.addtoken(type, value, context):
                    break
            else:
                assert i == len(input) - 1
                assert output == []
                return

            i += 1
            output = input[:i] + output
            driver.showast()
            for i, t in enumerate(output):
                type, value, context = t
                node = driver.tree.leaves()[i]

# Generated at 2022-06-13 18:02:58.103618
# Unit test for method classify of class Parser
def test_Parser_classify():
    """Test classify method."""
    import unittest
    from . import grammar

    class TestCase(unittest.TestCase):
        pass

    def make_suite():
        suite = unittest.makeSuite(TestCase)
        return suite

    def get_grammar(kind: Text, tabfile: Text) -> Grammar:
        if kind == 'python' or kind == 'python2':
            g = grammar.python_grammar
        elif kind == 'python3':
            g = grammar.python_grammar_no_print_statement
        elif kind == 'python3.5':
            g = grammar.python_grammar_no_print_statement
        elif kind == 'python3.6':
            g = grammar.python_grammar_36

# Generated at 2022-06-13 18:03:05.796553
# Unit test for method pop of class Parser
def test_Parser_pop():
    # A fake DFA, with just one state and a transition to itself on the label 0
    fake_dfa = ([(0, 0)], {0: 0})
    st = [
        (fake_dfa, 0, (0, None, None, None)),
        (fake_dfa, 0, (1, None, None, None))
    ]
    parser = Parser(Grammar(), None)
    parser.stack = st
    parser.pop()
    assert parser.stack == [(fake_dfa, 0, (0, None, None, [None]))]
    parser.pop()
    assert parser.stack == []
    assert parser.convert(Grammar(), (0, None, None, [None])) == (0, None, None, [None])

# Generated at 2022-06-13 18:03:22.904926
# Unit test for method push of class Parser
def test_Parser_push():
    grammar = Grammar()
    p = Parser(grammar, lam_sub)
    p.setup()
    p.push(467, ([], {}), 0, Context(NL(0, 1, []), ([], 0)))
    assert p.stack == [(grammar.dfas[467], 0, (467, None, None, []))], repr(p.stack)

test_Parser_push()

# Generated at 2022-06-13 18:03:37.784206
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver, token

    class MockGrammar(object):
        start = 0
        dfas = {}
        labels = {}
        keywords = {}
        tokens = {}

    class MockConverter(object):
        def __init__(self, grammar: MockGrammar, node: RawNode) -> None:
            self.grammar = grammar
            self.node = node

        def __call__(self):
            if self.node[1] is not None:
                node_value = self.node[1]
            else:
                node_value = "non-value"
            return "converted %s, %s" % (self.node[0], node_value)

    p = Parser(MockGrammar(), MockConverter)

# Generated at 2022-06-13 18:03:50.143417
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    def convert(grammar, node):
        type, value, context, children = node
        if children is not None:
            return Node(type, children, context)
        else:
            return None
    #
    # Create a parser
    parser = Parser(grammar.grammar, convert=convert)
    assert parser
    #
    # Test if the Parser is well-defined when there is an empty stack
    try:
        parser.shift(None, None, None, None)
        assert False
    except AssertionError:
        pass
    #
    # Test if the Parser is well-defined when there is a stack entry that is
    # either ill-formated or ill-defined.
    parser.stack = []
    parser.stack.append((None, None, None))

# Generated at 2022-06-13 18:03:59.825146
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import parsetok
    from . import tokenize
    from . import diff_match_patch

    tokenize.CLASSIFY = tokenize.DumbTokenTypeClassifier()
    p = Parser(parsetok.expr_grammar)
    dmp = diff_match_patch()
    d = dmp.diff_main('x + 2*y', 'x+2*y')
    # 'x+2*y' is the correct string
    assert d == [
        (0, 'x + 2*y'),
        (-1, ' '),
        (1, ''),
    ]  # 'x + 2*y' got changed to 'x+2*y' with diff type = -1
    p.setup()

# Generated at 2022-06-13 18:04:09.612106
# Unit test for method shift of class Parser
def test_Parser_shift():
    """[s2to3.Parser]  Test Parser.shift."""

    import textwrap

    from blib2to3.pgen2.tokenize import generate_tokens, untokenize
    from blib2to3.pygram import python_grammar_no_print_statement
    from blib2to3.pgen2.parse import ParseError

    def cst_to_ast(grammar, node):
        """Convert CST to AST"""
        child_tokens = []
        for child in node[3]:
            assert isinstance(child, list)
            child_tokens.extend(child)
        # The CST node must be a non-terminal , so value must be None
        assert node[1] is None
        # A non-terminal may contain a token

# Generated at 2022-06-13 18:04:17.180067
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    test_grammar = open("test/test1.grammar").read().encode("utf-8")
    import io
    import blib2to3.pgen2.pgen
    g = blib2to3.pgen2.pgen.generate_grammar(io.BytesIO(test_grammar))
    p = Parser(g)
    assert p.addtoken(3, "a", (1, 0)) == False
    assert p.addtoken(3, "b", (1, 0)) == True
    assert p.addtoken(3, "c", (1, 0)) == False
    assert p.addtoken(4, "d", (1, 0)) == False
    assert p.addtoken(4, "e", (1, 0)) == False

# Generated at 2022-06-13 18:04:21.582535
# Unit test for method classify of class Parser
def test_Parser_classify():
    from .gr_test import gr_test

    Parser = gr_test.Parser
    g = gr_test.grammar
    p = Parser(g)
    # The input grammar defines two tokens:
    # NAME, with label 257, and NUMBER, with label 258
    # that are used to recognize the tokens of the input grammar.
    assert p.classify(257, "foo", None) == 257
    assert p.classify(258, "123", None) == 258

# Generated at 2022-06-13 18:04:22.900118
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    assert Parser.addtoken(Parser, 'test1') == 'test1'

# Generated at 2022-06-13 18:04:26.963512
# Unit test for method shift of class Parser
def test_Parser_shift():
    p = Parser(Grammar())
    # pylint: disable=attribute-defined-outside-init
    p.stack = [("dfa", 0, (1, '', '', [None]))]
    p.stack[-1][2] = (1, '', '', [])
    p.shift(1, None, 2, None)

# Generated at 2022-06-13 18:04:36.074570
# Unit test for method pop of class Parser
def test_Parser_pop():
    pl = Parser(grammar, None)
    pl.stack = [('A','A','A','A'), ('B','B','B','B'), ('C','C','C','C')]
    pl.rootnode = 'X'
    pl.pop()
    assert pl.stack == [('A','A','A','A'), ('B','B','B','B')], pl.stack
    assert pl.rootnode == 'C'
    pl.pop()
    assert pl.stack == [('A','A','A','A')], pl.stack
    assert pl.rootnode == 'B'
    pl.pop()
    assert pl.stack == [], pl.stack
    assert pl.rootnode == 'A'

# Generated at 2022-06-13 18:04:59.134704
# Unit test for method push of class Parser
def test_Parser_push():
    import inspect
    from . import grammar

    # Assign to an untaken lineno to silence flake8 F821.
    inspect.currentframe().f_lineno = 1

    grammar = grammar.grammar
    convert = lambda g, n: n

    p = Parser(grammar, convert)
    p.setup()
    p.addtoken(3, "", (1, 0))
    p.addtoken(1, "", (1, 0))

    assert p.stack[0][2][-1][0] == 1
    assert p.stack[0][2][-1][-1] == [
        (token.NAME, "", (1, 0), None),
        (token.NEWLINE, "", (1, 0), None),
    ]

    # More tests.

# Generated at 2022-06-13 18:05:07.057252
# Unit test for method setup of class Parser
def test_Parser_setup():
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pgen2.pgen import pickle_grammar
    from io import StringIO
    import pickle
    g = pickle_grammar(StringIO(grammar1))
    g.start = None
    p = Parser(g)
    p.setup()
    assert p.stack[0][:2] == (g.dfas[g.start], 0)
    assert p.stack[0][2] == (g.start, None, None, [])
    p1 = pickle.loads(pickle.dumps(p))
    assert p1.stack[0][:2] == (g.dfas[g.start], 0)

# Generated at 2022-06-13 18:05:16.225565
# Unit test for method setup of class Parser
def test_Parser_setup():
    import blib2to3.pgen2.token as token
    import blib2to3.pgen2.driver as driver
    from . import grammar, parse

    g = grammar.grammar
    d = driver.Driver(g.dfas, g.labels)
    p = parser.Parser(g)
    t = d.make_actions_generator()

    p.setup()

# Generated at 2022-06-13 18:05:25.915015
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import ply.lex as lex

    class MyLexer(object):
        def __init__(self, test_input):
            self.lexer = lex.lex()
            self.lexer.input(test_input)

        def token(self) -> Tuple[int, str]:
            tok = self.lexer.token()
            if tok:
                return getattr(tok, 'type'), tok.value
            else:
                return None, None

    from . import driver

    g = driver.load_grammar('Python.asdl')
    p = Parser(g)

    s = 'x = None\n'
    p.setup()
    lexer = MyLexer(s)
    while True:
        typ, val = lexer.token()
        if typ is None:
            break
       

# Generated at 2022-06-13 18:05:34.699179
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar, tokenize
    from .token import TokenInfo

    # Create a parser from a dummy grammar
    p = Parser(grammar)

    # Create a dummy input token stream
    tokens = tokenize.generate_tokens(open(__file__))

    # Normalize the token stream to have NL tokens at the end of each line
    tokens = tokenize.untokenize(tokens)

    # Reset the parser
    p.setup()

    # Add tokens to the parser (the return value is ignored)
    for type, value, start, stop, line in tokens:
        p.addtoken(type, value, None)

# Generated at 2022-06-13 18:05:35.799410
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # TODO: Add some synthetic grammars and tests here
    return

# Generated at 2022-06-13 18:05:45.441597
# Unit test for method shift of class Parser
def test_Parser_shift():

    class MockGrammar(object):
        """Mock Grammar."""

        def __init__(self):
            self.dfas = {1: ([[(1, 1), (2, 0)], [(0, 1)]], {1: 0, 2: 1}), 0: ([], {})}
            self.labels = {1: (token.NAME, "x"), 2: (token.NAME, "y")}
            self.tokens = {token.NAME: 1}
            self.keywords = {}

    grammar = MockGrammar()

    def convert(grammar, node):
        pass

    parser = Parser(grammar, convert)
    parser.setup()
    parser.addtoken(token.NAME, "x", None)
    parser.addtoken(token.NAME, "y", None)

# Generated at 2022-06-13 18:05:53.693761
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    def check_classify(name: Text) -> None:
        parser = Parser(grammar, None)
        parser.setup()
        result = parser.classify(token.NAME, name, None)
        if name not in parser.grammar.keywords:
            assert result == parser.grammar.tokens[token.NAME]
        else:
            assert result == parser.grammar.labels[result][0]

    # Check that all keywords are recognized as keywords
    for name in grammar.keywords:
        check_classify(name)

# Generated at 2022-06-13 18:06:07.895173
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    grammar = Grammar()
    grammar.load_pgen(open("python3.7/Grammar/Grammar"))
    p = Parser(grammar)
    assert p.addtoken(1, "class", (1, 0)) == False
    assert p.addtoken(1, "def", (1, 0)) == False
    assert p.addtoken(1, "main", (1, 0)) == False
    assert p.addtoken(40, ":", (1, 0)) == False
    assert p.addtoken(1, "pass", (1, 0)) == True
    assert p.stack == []

if __name__ == "__main__":
    test_Parser_addtoken()

# Generated at 2022-06-13 18:06:08.420683
# Unit test for method pop of class Parser
def test_Parser_pop():
    pass

# Generated at 2022-06-13 18:06:55.359313
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from io import StringIO
    from .driver import Driver
    from . import grammar, tokenize
    from .parse import MyParser

    s = "3+4"
    g = grammar.grammar
    p = MyParser(g)
    p.setup()
    d = Driver(g, p, s)
    for typ, val, _, _, _ in tokenize.generate_tokens(StringIO(s).readline):
        d.addtoken(typ, val)
    assert p.rootnode[0] == "expr"

# Generated at 2022-06-13 18:07:02.524744
# Unit test for method classify of class Parser
def test_Parser_classify():
    """Unit test for method classify of class Parser.

    See test_parsetok.py for a full set of unit tests.

    """
    # Test data
    grammar_file = "Python.asdl"
    start_symbol = "file_input"
    tokens = [
        (token.NAME, "print"),
        (token.NAME, "False"),
        (token.NAME, "None"),
        (token.NAME, "print"),
        (token.NAME, "print"),
        (token.NAME, "print"),
    ]
    # Constructor
    grammar = Grammar(grammar_file)
    parser = Parser(grammar)
    parser.setup(start_symbol)
    # Iterate over input tokens

# Generated at 2022-06-13 18:07:03.949458
# Unit test for method push of class Parser
def test_Parser_push():
    g = Grammar()
    p = Parser(g)
    p.push(1, (), 0, ())

# Generated at 2022-06-13 18:07:12.640839
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class Fake_Grammar:
        dfas = {
            "a": ([[0, 1], [], [(1, 0)]], {0: 0, 1: 2}),
            "b": ([[0, 2], [(1, 0), (0, 2)], [(1, 2)], []], {0: 0, 1: 1, 2: 3}),
        }
        tokens = {}
        keywords = {}
        start = "a"
        symbols = {}
        labels = {0: (0, None), 1: (256, "b")}

    p = Parser(Fake_Grammar())
    p.setup()
    assert p.addtoken(0, None, None) is False
    assert p.stack == [(Fake_Grammar.dfas["a"], 1, (256, None, None, []))]

# Generated at 2022-06-13 18:07:20.770415
# Unit test for method pop of class Parser
def test_Parser_pop():
    """Test for Parser.pop()."""
    from . import grammar

    g = grammar.Grammar(grammar.grammar, grammar.symbol2number)
    p = Parser(g)
    p.setup()
    p.push(grammar.symbol2number["file_input"], (1, 2), 0, None)
    p.push(grammar.symbol2number["stmt"], (3, 4), 0, None)
    p.push(grammar.symbol2number["simple_stmt"], (5, 6), 0, None)
    p.push(grammar.symbol2number["small_stmt"], (7, 8), 0, None)
    p.push(grammar.symbol2number["expr_stmt"], (9, 10), 0, None)

# Generated at 2022-06-13 18:07:30.147895
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3 import pygram

    test_grammar = pygram.python_grammar
    test_tokens = pygram.python_symbols
    test_parser = Parser(test_grammar)
    test_parser.setup()
    test_parser.addtoken(test_tokens.NAME, "print", (1, 0))

# Generated at 2022-06-13 18:07:35.815520
# Unit test for method pop of class Parser
def test_Parser_pop():
    s = 'leaf'
    l = Leaf(1, s)
    n = (1, None, None, [l])
    p = Parser(Grammar(), lam_sub)
    p.stack.append((0, 0, n))
    p.pop()
    assert p.rootnode.value == s


# Generated at 2022-06-13 18:07:43.269434
# Unit test for method shift of class Parser
def test_Parser_shift():
    """Test for method shift of class Parser"""
    # 1: Input token is token.NUMBER
    # 1.1: Argument newstate is 0
    p1 = Parser(Grammar())
    p1.setup()
    p1.shift(token.NUMBER, "1", 0, None)
    assert p1.stack == [(DFA, 0)]
    # 1.2: Argument newstate is 1
    p1 = Parser(Grammar())
    p1.setup()
    p1.shift(token.NUMBER, "1", 1, None)
    assert p1.stack == [(DFA, 1)]


# Generated at 2022-06-13 18:07:54.410594
# Unit test for method pop of class Parser
def test_Parser_pop():
    results: Results = {}

    def _converter(grammar: Grammar, node: RawNode) -> Leaf:
        results[node[0]] = node[1]
        return Leaf(node[0], node[1])

    p = Parser(Grammar(g2, g2u), _converter)
    p.setup(1)
    for (type, value) in tokenize(s):
        p.addtoken(type, value, (1, 1))
    assert results[1] == "foo"
    assert results[2] == "bar"
    assert results[3] == "baz"



# Generated at 2022-06-13 18:08:03.472179
# Unit test for method pop of class Parser
def test_Parser_pop():
    # Arrange
    class MockGrammar(object):
        def __init__(self):
            self.dfas = {
                'type': ([], {}),
                'value': ([], {}),
            }
    class MockNode(object):
        def __init__(self, type: int, value: Optional[Text], context: Context, children: Sequence[Any]) -> None:
            self.type = type
            self.value = value
            self.context = context
            self.children = children
    from blib2to3.pgen2.driver import convert_to_new_style_grammar
    grammar = convert_to_new_style_grammar(MockGrammar())
    # Act
    parser = Parser(grammar)
    parser.setup(start=None)

# Generated at 2022-06-13 18:09:19.879874
# Unit test for method classify of class Parser
def test_Parser_classify():
    def classify(t: Union[int, Text]) -> Optional[int]:
        if isinstance(t, int):
            return t
        return grammar.tokens.get(t)

    from blib2to3.pgen2 import driver, token

    grammar = driver.load_grammar("Python.g4")
    parser = Parser(grammar)
    parser.setup()
    assert parser.classify(token.NAME, "if", (1, 0)) == classify("NAME")
    assert parser.classify(token.NAME, "def", (1, 0)) == classify("DEF")
    assert parser.classify(token.NUMBER, "10", (1, 0)) == classify("NUMBER")
    assert parser.classify(token.NEWLINE, "", (1, 0)) == classify("NEWLINE")
    assert parser

# Generated at 2022-06-13 18:09:28.918446
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class MockParseError(Exception):
        pass

    class MockNode(object):

        def __init__(self, type, children=None):
            self.type = type
            self.children = children
            self.value = str(type)

    class MockGrammar(object):
        start = 1
        tokens = {14: 256, 16: 257, 17: 258, 18: 259, 19: 260}

# Generated at 2022-06-13 18:09:35.226785
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2.driver import Driver
    driver = Driver(True)
    grammar = driver.load_grammar(driver.grammar_file)
    parser = Parser(grammar)
    parser.setup()
    parser.shift(1, "test", 1, (1, 1))
    assert parser.stack[0][0] == (parser.grammar.dfas[1], 1, (1, "test", (1, 1), None))

# Generated at 2022-06-13 18:09:47.003638
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2.token import tok_name

    # All tokens in a grammar

# Generated at 2022-06-13 18:09:57.322910
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest
    import io
    import tokenize
    import blib2to3.pgen2.driver
    import blib2to3.pygram as pygram

    class ParserTestCase(unittest.TestCase):
        def test_parser(self):
            stream = io.StringIO("""\
a = 0
raise NameError
""")
            grammar = blib2to3.pgen2.driver.load_grammar(pygram, "Grammar.txt")
            p = Parser(grammar)
            p.setup()
            for ttype, value, _, _, _ in tokenize.generate_tokens(stream.readline):
                if p.addtoken(ttype, value, None):
                    break
            self.failUnless(p.rootnode is not None)

   

# Generated at 2022-06-13 18:10:04.589750
# Unit test for method setup of class Parser
def test_Parser_setup():
    from pgen2.pgen import Grammar, Lark
    from pgen2.tokenize import generate_tokens, tokenize_file
    from pgen2.driver import Driver

    print("Testing Parser.setup")
    grammar = Lark.parse_grammar(Lark.example_grammar)
    with tokenize_file(Driver, grammar) as tokens:
        parser = Parser(grammar)
        for i in [2, None]:
            parser.setup(i)
            for token, value, context in tokens:
                if parser.addtoken(token, value, context):
                    break
            print(parser.rootnode)
    print("Done testing Parser.setup")
    # Indirectly tests all other methods
    return parser


# Generated at 2022-06-13 18:10:09.793629
# Unit test for method shift of class Parser
def test_Parser_shift():
    #
    # Create a grammar.
    #
    from blib2to3.pgen2 import token
    from blib2to3.pgen2 import parse
    from blib2to3.pgen2 import driver
    import io
    lines = [
        "cfg_1=a A B c",
        "cfg_1=a A B c d",
        "cfg_2=a B C",
        "cfg_3=a B D",
        "cfg_4=a E",
    ]
    g = parse.Parser(io.StringIO("\n".join(lines)))
    g.driver.parsed = False
    g.driver.parse_tokens(lines)
    #
    # Prepare for parsing.
    #
    from blib2to3.pgen2 import grammar

# Generated at 2022-06-13 18:10:13.048935
# Unit test for method shift of class Parser
def test_Parser_shift():
    p = Parser(Grammar())
    p.shift(token.PLUS, "+", 1, (1,1))
    p.shift(token.PLUS, "+", 1, (1,1))
    p.shift(token.PLUS, "+", 1, (1,1))

# Generated at 2022-06-13 18:10:16.595801
# Unit test for method push of class Parser
def test_Parser_push():
    def test_method_push(grammar, convert):
        p = Parser(grammar, convert)
        p.setup()
        p.push(1, 2, 3, 4)

    test_method_push(grammar=None, convert=None)


# Generated at 2022-06-13 18:10:26.212520
# Unit test for method pop of class Parser
def test_Parser_pop():
    """Unit tests for the method pop of class Parser.
    """

    def parser_pop_and_check(stack: List[Tuple[DFAS, int, RawNode]],
                             expected_stack: List[Tuple[DFAS, int, RawNode]],
                             expected_rootnode: Sequence,
                             grammar: Grammar) -> None:
        """Test pop with a given stack and a given expected result.

        The raw node is the root of a syntax tree.
        """
        parser = Parser(grammar)
        parser.stack = stack
        parser.pop()
        assert parser.stack == expected_stack
        assert parser.rootnode == expected_rootnode

    # Define a grammar