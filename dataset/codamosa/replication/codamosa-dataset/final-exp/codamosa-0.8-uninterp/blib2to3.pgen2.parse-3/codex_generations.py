

# Generated at 2022-06-13 18:01:36.302018
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .grammar import Grammar

    g = Grammar(nodes={})
    p = Parser(g)

    assert not p.stack

    p.shift(token.NEWLINE, '\n', 1, Context(1, 1))
    assert p.stack == [(None, 1, ('', None, None, []))]

    p.shift(token.LPAR, '(', 2, Context(2, 1))
    assert p.stack == [(None, 1, ('', None, None, [])), (None, 2, ('', None, None, []))]

    p.shift(token.RPAR, ')', 3, Context(3, 1))

# Generated at 2022-06-13 18:01:46.518463
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .pygram import python_symbols, python_nonterminals
    from .grammar_parser import pgen
    from .pgen2 import tokenize

    source = 'if 1: pass\n'
    g = pgen(source)
    p = Parser(g)
    p.setup()
    addtoken = p.addtoken
    input_token_list = list(tokenize.generate_tokens(source.__iter__().__next__))
    # Do the equivalent of:
    # p.addtoken(token.IF, 'if', (1, 0))
    # p.addtoken(token.NUMBER, '1', (1, 3))
    # p.addtoken(token.COLON, ':', (1, 4))
    # p.addtoken(token.NAME, 'pass', (

# Generated at 2022-06-13 18:01:54.737949
# Unit test for method pop of class Parser
def test_Parser_pop():
    def test_grammar_parser(grammar_file, input_file):
        print("\n[Start] grammer_file:", grammar_file, input_file)
        from . import grammar

        g = grammar.grammar(grammar_file)
        p = Parser(g)
        p.setup()
        tokens = iter(grammar.tokenize(input_file))
        for type, value, context in tokens:
            try:
                if p.addtoken(type, value, context):
                    break
            except ParseError as e:
                print(e)
                return e
        p.rootnode = None
        return p.rootnode


    from . import driver, token

    rootnode = test_grammar_parser(driver.grammar, driver.test_grammar2)
    assert rootnode is None

# Generated at 2022-06-13 18:01:59.082365
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver
    from . import dgcheck

    p = driver.TestParser(driver.test_grammar)
    p.setup()
    # Make sure it doesn't crash
    dgcheck.check_parser(p)

if __name__ == "__main__":
    test_Parser_addtoken()

# Generated at 2022-06-13 18:02:08.529592
# Unit test for method setup of class Parser
def test_Parser_setup():
    import sys
    import os
    from .tokenize import untokenize
    from .pytokenize import tokenize, untokenize
    from .pgen import driver
    from blib2to3.pgen2 import token, grammar
    import io
    import pickle

    grammardir = os.path.dirname(sys.argv[0])
    grammars = driver.load_grammars(grammardir, ["Grammar.txt"])
    start = "file_input"
    converter = driver.load_converter("lam_sub.py")
    parser = driver.Parser(grammars, converter)
    parser.setup(start)
    assert parser.convert is converter

# Generated at 2022-06-13 18:02:14.794394
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .grammar import Grammar

    grammar = Grammar(open("Grammar/Grammar"))
    parser = Parser(grammar)
    parser.setup()
    parser.addtoken(token.NUMBER, "1", Context(None, 1, 0))
    parser.addtoken(token.PLUS, "+", Context(None, 1, 1))
    parser.addtoken(token.NUMBER, "2", Context(None, 1, 2))
    parser.addtoken(token.ENDMARKER, "\0", Context(None, 1, 3))
    assert parser.rootnode[0].value == "+"

# Generated at 2022-06-13 18:02:26.163915
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import token
    from blib2to3 import pytree
    from blib2to3.pgen2 import grammar

# Generated at 2022-06-13 18:02:37.881067
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys
    import blib2to3.pgen2.driver

    grammar = blib2to3.pgen2.driver.load_grammar(sys.argv[1])
    driver = blib2to3.pgen2.driver.Driver(grammar, convert=lam_sub)
    driver.prepare_node(grammar.start)
    dfa, state = driver.dfa
    stack = [(dfa, state, None)]
    while stack:
        dfa, state, node = stack[-1]
        arcs = dfa[state]
        if arcs == [(0, state)]:
            stack.pop()
            if stack:
                parent = stack[-1][2]
                if parent is not None:
                    if node is not None:
                        parent.append(node)

# Generated at 2022-06-13 18:02:41.827181
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Arrange
    parser = Parser(None)
    parser.stack = [(None, None, None)]
    # Act
    parser.shift(None, None, None, None)
    # Assert
    assert parser.stack == [(None, None, None)]


# Generated at 2022-06-13 18:02:44.543426
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import dfas

    p = Parser(dfas.grammar)
    assert isinstance(p.classify(4, None, None), int)
    assert isinstance(p.classify(5, None, None), int)

# Generated at 2022-06-13 18:02:58.343186
# Unit test for method shift of class Parser
def test_Parser_shift():
    import grammar
    import driver
    import test.support

    # This generates 2 ^ 5 = 32 parse trees; it takes awhile.
    # To test a single parse, remove a '*' from one of the lines below.

# Generated at 2022-06-13 18:03:08.883939
# Unit test for method setup of class Parser
def test_Parser_setup():
    class MockGrammar(object):
        def __init__(self, start):
            self.start = start
            self.dfas = {}
            self.dfas[start] = []

    class MockDFAS(object):
        def __init__(self, states, first):
            self.states = states
            self.first = first

    mock_dfas_0 = MockDFAS(states=[], first=[])
    mock_dfas_0.states.append([(1,2), (2,3)])
    mock_dfas_0.states.append([(0,1), (1,2)])
    mock_dfas_0.states.append([(0,2), (1,2)])
    mock_dfas_1 = MockDFAS(states=[], first=[])
    mock_dfas_

# Generated at 2022-06-13 18:03:19.580714
# Unit test for method push of class Parser
def test_Parser_push():
    def f1(grammar, node):
        return node
    def f2(grammar, node):
        return None
    p = Parser(None, f1)
    p.push(1, (None, None), 2, None)
    assert p.stack == [(None, 0, (1, None, None, [])), (None, 2, (1, None, None, []))]
    p.push(2, (None, None), 3, None)
    assert p.stack == [
        (None, 0, (1, None, None, [])),
        (None, 2, (1, None, None, [])),
        (None, 3, (2, None, None, [])),
    ]
    p = Parser(None, f2)

# Generated at 2022-06-13 18:03:27.964829
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    values = [
        (1, "a", (1, 2)),
        (1, "a", (1, 2)),
        (1, "b", (2, 3)),
    ]
    p = Parser(Grammar())
    # First, try with some real values
    p.stack = [(None, None, (1, "a", (1, 2), []))]
    msg = None
    try:
        p.addtoken(1, "a", (1, 2))  # type: ignore
    except ParseError as err:
        msg = err.msg
    assert msg == "bad input"
    # Second, test with a value not present in the dictionary
    p.stack = [(None, None, (1, "a", (1, 2), []))]
    p.grammar.labels = {}


# Generated at 2022-06-13 18:03:34.488619
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2.parse import load_grammar
    grammar = load_grammar("Grammar/Grammar")
    parser = Parser(grammar)
    parser.classify(token.NAME, "True", None)
    parser.classify(token.NAME, "FALSE", None)
    parser.classify(token.NAME, "None", None)

# Generated at 2022-06-13 18:03:40.231882
# Unit test for method setup of class Parser
def test_Parser_setup():
    import pprint
    from pathlib import Path
    from . import driver
    path = Path(__file__).parent / "testfiles/grammar.out"
    grammar = Grammar(path)
    p = Parser(grammar)
    p.setup()
    # Assert that the p has a stack of length 1
    assert len(p.stack) == 1
    for (t, v, c, n) in driver.parse_file(path):
        if p.addtoken(t, v, c):
            break
    # Assert that the p has a rootnode attribute that is not None:
    assert p.rootnode is not None
    # Assert that the p rootnode is a new-style class:
    assert isinstance(p.rootnode, type)
    # pprint the p rootnode to ensure that the whole tree

# Generated at 2022-06-13 18:03:56.722251
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .. import python_grammar
    from .pgen import generate_grammar
    from .tokenize import generate_tokens

    g = generate_grammar(python_grammar)
    parser = Parser(g)
    parser.setup(start=g.start)

    g = generate_grammar(python_grammar)
    parser1 = Parser(g)
    parser1.setup(start=g.start)
    # Note: 'c' is a valid name in Python 2.7.
    toks = list(generate_tokens("c"))

    parser1.addtoken(toks[0][0], toks[0][1], toks[0][2])
    parser1.pop()
    # Sanity check: the same as the corresponding statement above

# Generated at 2022-06-13 18:04:06.600730
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar

    fp = open(grammar.__file__.replace(".pyc",".py"), "rb") # type: ignore
    source = fp.read().decode("utf-8")
    fp.close()

    import blib2to3.pgen2.tokenize

    tokens = list(blib2to3.pgen2.tokenize.tokenize(source.encode("utf-8")))

    first_grammar = grammar.Grammar(tokens)

    dfa = first_grammar.dfas[first_grammar.start]

    parser = Parser(first_grammar)

    parser.setup()

    for token in tokens:
        parser.addtoken(*token)

    assert len(parser.stack) == 0


# Generated at 2022-06-13 18:04:12.273547
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver, token
    # A grammar with production 'x : x x | x'
    p = Parser(driver.testgrammar())
    p.setup()
    p.addtoken(token.NAME, "x", (1, 0))
    p.addtoken(token.NAME, "x", (1, 2))
    p.addtoken(token.NAME, "x", (1, 4))
    p.addtoken(token.NAME, "x", (1, 5))
    p.addtoken(token.NAME, "x", (1, 7))
    assert p.rootnode.children[0].children[0].children[0].children == []
    p.addtoken(token.NAME, "x", (1, 9))
    p.addtoken(token.NEWLINE, "\n", (2, 0))


# Generated at 2022-06-13 18:04:19.603531
# Unit test for method shift of class Parser
def test_Parser_shift():
    # a test node
    node: RawNode = (0, 0, 0, [])
    # a test grammar
    grammar = Grammar()
    grammar.labels = [(0, 2), (1, 1), (1, 1)]
    grammar.dfas = {1: ([[(0, 1)]], 0)}
    # a test parser
    testparser = Parser(grammar)
    testparser.stack = [(grammar.dfas[1], 0, node)]
    # test
    testparser.shift(0, 0, 1, 0)
    expected = ([[(1, 0)]], 0)
    assert testparser.stack[-1] == expected

# Generated at 2022-06-13 18:04:35.081511
# Unit test for method classify of class Parser
def test_Parser_classify():
    import pgen2.tokenize
    from io import StringIO
    from . import grammar

    g = grammar.grammar
    p = Parser(g)
    p.setup()
    p.addtoken(pgen2.tokenize.NAME, "def", None)
    p.addtoken(pgen2.tokenize.NAME, "f", None)
    p.addtoken(pgen2.tokenize.OP, "(", None)
    p.addtoken(pgen2.tokenize.OP, ")", None)
    p.addtoken(pgen2.tokenize.OP, ":", None)
    p.addtoken(pgen2.tokenize.DEDENT, "", None)

# Generated at 2022-06-13 18:04:43.663712
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest

    class Test(unittest.TestCase):
        def test_empty_program(self):
            self.assertTrue(self.pg.addtoken(token.ENDMARKER, None, Context(None, 0, 0)))

        def test_one_token(self):
            self.assertFalse(self.pg.addtoken(token.NAME, "spam", Context(None, 0, 0)))
            self.assertTrue(self.pg.addtoken(token.ENDMARKER, None, Context(None, 0, 0)))
            self.assertTrue(self.pg.rootnode is None)

        def test_useless_comment(self):
            self.assertFalse(self.pg.addtoken(token.COMMENT, "spam", Context(None, 0, 0)))

# Generated at 2022-06-13 18:04:53.408974
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    grammar = Grammar(
        grammar_token_map={0: 1, 1: 2},
        grammar_start=0,
        grammar_dfas=[
            ([], {}),
            ([], {0: [(0, 0)], 1: [(0, 0), (1, 1)]}),
            ([], {0: [(0, 0)], 1: [(0, 0), (2, 2)]}),
        ],
    )
    p = Parser(grammar)
    p.setup()
    assert not p.addtoken(0, "foo", None)
    assert not p.addtoken(1, "foo", None)
    assert p.addtoken(2, "foo", None)
    assert p.stack == []

# Generated at 2022-06-13 18:05:03.561408
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    g = grammar.Grammar(
        """\
        stmt: simple_stmt | compound_stmt
        simple_stmt: NAME '=' NAME
        compound_stmt: if_stmt | for_stmt
        for_stmt: 'for' NAME 'in' NAME ':' suite
        if_stmt: 'if' NAME ':' suite
        suite: '{' stmt '}'
        """
    )

    def convert(grammar, node):
        return node

    t1 = (token.NAME, "NAME1", None, None)
    t2 = (token.EQUAL, "=", None, None)
    t3 = (token.NAME, "NAME2", None, None)
    t4 = (token.NEWLINE, None, None, None)

    #

# Generated at 2022-06-13 18:05:14.631863
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import os.path
    from .tokenize import detect_encoding, generate_tokens, tokenize

    root = os.path.split(__file__)[0]
    path = os.path.join(root, 'Grammar.txt')
    with open(path, encoding=detect_encoding(path)) as f:
        encoding, lines = tokenize(f.readline)
        tokens = []
        for token in generate_tokens(lines.__next__):
            tokens.append(token)

    from . import grammar
    from .pgen import driver

    grammar, start, dfas = driver.load_grammar(path)
    p = Parser(grammar)
    p.setup(start)
    for t in tokens:
        p.addtoken(*t)
    assert p.rootnode

# Generated at 2022-06-13 18:05:25.042017
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import parsetok

    g = Grammar(
        [
            ("x", "foo"),
            ("y", "bar"),
            ("z", "foo bar"),
            ("w", ""),
        ],
        [
            "baz",
            "quux",
        ],
    )
    p = Parser(g)
    p.setup()
    p.addtoken(token.NAME, "foo", Context(0, 0, ""))
    assert p.stack[-1][1] == 0
    p.addtoken(token.NAME, "bar", Context(0, 0, ""))
    assert p.stack[-1][1] == 1
    p.addtoken(token.NAME, "baz", Context(0, 0, ""))

# Generated at 2022-06-13 18:05:35.525946
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3 import pytree
    from . import driver

    gr = Grammar()
    gr.keywords = {'a': 0, 'b': 1, 'c': 2}
    gr.tokens = {4: 3}
    gr.labels = [
        ('a', 0),
        ('b', 1),
        ('c', 2),
        ('token', 3),
        ('something', 4),
    ]
    gr.start = 0

# Generated at 2022-06-13 18:05:45.390844
# Unit test for method push of class Parser
def test_Parser_push():
    """tst_Parser_push() -> None.  Test method push for class Parser."""
    class MockGrammar(Grammar):
        def __init__(self):
            from blib2to3.pgen2.token import tok_name  # Import can't be at global level
            keywords = {"True": 1, "False": 2, "None": 3}
            tokens = {1: 4, 2: 5, 3: 6}
            labels = ["a", "True", "False", "None", "NAME", " "]

# Generated at 2022-06-13 18:05:56.341907
# Unit test for method pop of class Parser
def test_Parser_pop():
    import blib2to3.pgen2.token
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pgen2.parse import ParseError

    from . import driver

    def get_grammar(**kwds):
        return Grammar(driver.get_grammar_table(), 'file_input', **kwds)

    def get_converter():
        def convert(grammar, node):
            if node[0] in (
                token.INDENT,
                token.DEDENT,
                token.NEWLINE,
            ):
                return None
            return node
        return convert

    def get_parser(**kwds):
        return Parser(get_grammar(**kwds), get_converter())


# Generated at 2022-06-13 18:06:03.438691
# Unit test for method pop of class Parser
def test_Parser_pop():
    class MyNode(object):
        def __init__(self, children: Sequence[object]) -> None:
            self.children = children
    class MyGrammar(object):
        def __init__(self) -> None:
            self.start = 1
            self.tokens = {}
            self.keywords = {}
            self.labels = {}
            self.dfas = {}
    class MyParser(Parser):
        def __init__(self) -> None:
            Parser.__init__(self, MyGrammar())
        def convert(self, gram: Any, node: Any) -> MyNode:
            return MyNode(node[3])
    gram = MyGrammar()
    p = MyParser()
    p.setup(1)
    p.shift(0, "", 0, None)
   

# Generated at 2022-06-13 18:06:16.375339
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import token
    from . import nfa
    f = nfa.compile_grammar("""
        grammar:
        | rule+
        ;
        rule: 'x'
        ;
    """, convert=None, generate_bear_parser=False)
    p = Parser(f)
    p.setup()
    p.addtoken(token.NAME, 'x', Context(1, 0))
    p.shift(token.NAME, 'x', 1, Context(1, 1))
    p.addtoken(token.NAME, 'x', Context(2, 0))
    p.shift(token.NAME, 'x', 1, Context(2, 1))
    p.addtoken(token.NAME, 'x', Context(3, 0))

# Generated at 2022-06-13 18:06:25.138819
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2 import state
    first_grammar = Grammar(r"grammar.txt")
    first_parser = Parser(first_grammar, lam_sub)
    first_parser.setup()
    first_first_state = first_grammar.labels.index((token.NEWLINE, None))
    first_state = state.ParserState()
    first_parser.shift(token.NEWLINE, None, first_first_state, first_state)



# Generated at 2022-06-13 18:06:36.696496
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .driver import Driver
    from .parser import Parser
    driver = Driver()
    grammar = driver.load_grammar("Grammar/Grammar")
    parser = Parser(grammar)
    parser.setup()
    assert not parser.addtoken(token.NAME, 'foo', (0, 0))
    assert not parser.addtoken(token.EQUAL, '=', (0, 3))
    assert not parser.addtoken(token.NUMBER, '1', (0, 5))
    assert parser.addtoken(token.NEWLINE, '\n', (1, 0))
    root = parser.rootnode
    assert root.children[0].type == token.NAME
    assert root.children[0].value == 'foo'
    assert root.children[1].type == token.EQUAL
    assert root

# Generated at 2022-06-13 18:06:48.150221
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver, grammar, tokenize

    g = grammar.grammar
    p = Parser(g)
    p.setup()
    p.stack = [(g.dfas[g.start], 0, (g.start, None, None, []))]

    def check(type: int, value: Optional[Text], newstate: int, context: Context):
        t = tokenize.TokenInfo(type, value, context)
        p.shift(t.type, t.string, newstate, t.start)
        assert p.stack == [(g.dfas[g.start], newstate, (g.start, None, None, [t]))]


# Generated at 2022-06-13 18:06:59.912299
# Unit test for method pop of class Parser
def test_Parser_pop():
    import blib2to3.pgen2.driver
    test_grammar = blib2to3.pgen2.driver.load_grammar("Grammar/Grammar")
    test_parser = Parser(test_grammar)
    test_parser.setup()
    dfa, state, node = test_parser.stack[-1]
    assert state == 0
    assert dfa == test_grammar.dfas[1]
    assert node == (1, None, None, [])
    test_parser.stack[-1] = (dfa, 1, node)
    popdfa, popstate, popnode = test_parser.stack.pop()
    assert popdfa == dfa
    assert popstate == 1
    assert popnode == node
    assert test_parser.stack == []


# Generated at 2022-06-13 18:07:07.240083
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, tokenize

    p = Parser(grammar)
    p.setup()
    for tok in tokenize.generate_tokens(open(__file__)):
        p.addtoken(*tok)
    root = p.rootnode
    assert root[0].type == grammar.syms.file_input


# Generated at 2022-06-13 18:07:16.392341
# Unit test for method push of class Parser
def test_Parser_push():
    import sys
    sys.path.insert(0, 'lib2to3')
    from . import pygram
    import blib2to3.pgen2.driver
    if sys.version_info >= (3, 5):
        r = blib2to3.pgen2.driver.load_grammar('Python35.txt')
    elif sys.version_info >= (3, 4):
        r = blib2to3.pgen2.driver.load_grammar('Python34.txt')
    elif sys.version_info >= (3, 3):
        r = blib2to3.pgen2.driver.load_grammar('Python33.txt')

# Generated at 2022-06-13 18:07:26.036556
# Unit test for method pop of class Parser
def test_Parser_pop():  # unit test
    class MockNode(object):  # unit test
        def __init__(self, val):  # unit test
            self.children = [None] * val  # unit test

    grammar = Grammar()  # unit test
    parser = Parser(grammar)  # unit test
    parser.setup()  # unit test
    mock_dfa = (None, None)  # unit test
    mock_node = (1, 'TestString', None, [])  # unit test
    # unit test
    parser.stack = [(mock_dfa, 0, mock_node), (mock_dfa, 0, mock_node)]  # unit test
    parser.convert = lambda a, b: MockNode(len(b[-1]))  # unit test
    parser.pop()  # unit test
    assert parser

# Generated at 2022-06-13 18:07:33.804565
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .pgen2 import generate_grammar

    grammar = generate_grammar("Grammar.txt")
    p = Parser(grammar)
    p.setup()

    # addtoken()
    #
    #   Try to add a token when the stack is empty
    #

    # This is the expected output
    expected = "too much input"
    got = ""

    try:
        p.addtoken(token.AS, "as", (0, 0))
    except ParseError as pe:
        got = pe.msg
    assert got == expected, "Expected " + expected + ", got " + got

    #
    #   Try to add a token with an invalid type
    #

    # This is the expected output
    expected = "bad token"
    got = ""


# Generated at 2022-06-13 18:07:42.102806
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .tokenizer import generate_tokens, Untokenizer, INDENT, DEDENT, NEWLINE
    from .pgen2 import driver
    from blib2to3.pgen2 import token as token2
    from blib2to3.pgen2.pgen import Grammar, LABEL, DFA, DFAS

    def add_dfa(
        dfa: DFA,
        labels: Dict[int, Tuple[int, Optional[Text]]],
        name: Text,
        symbol: int,
        LAMBDA: int,
        tokens: List[Tuple[int, Optional[Text]]],
        results: Results,
    ) -> None:
        """Add a DFA to the result."""
        dfa[LAMBDA] = [(LAMBDA, LAMBDA)]
       

# Generated at 2022-06-13 18:07:56.899097
# Unit test for method push of class Parser
def test_Parser_push():
    import collections

    DFA = collections.namedtuple("DFA", ["state", "rule"])
    rules = collections.defaultdict(list)
    rule = {
        "A": 1,
        "B": 2,
        "C": 3,
    }
    grammar = Grammar(DFA, rules, rule, rule, rule, rule)
    stack = [("A", 0, {})]
    parser = Parser(grammar, None)
    parser.stack = stack
    parser.push("B", "B", 1, None)
    assert parser.stack == [("A", 0, {}), ("B", 0, {})]
    assert stack == [("A", 0, {}), ("B", 0, {})]

# Generated at 2022-06-13 18:08:04.556716
# Unit test for method push of class Parser
def test_Parser_push():
    class dummy:
        def __getitem__(self, key):
            return [(0,1)]
        def __len__(self):
            return 1

    dfa = dummy()
    node = ("", "", "", [])
    parser = Parser(None)
    parser.push(0, dfa, 1, "")
    assert parser.stack[0] == (dfa, 1, node)
    assert parser.stack[1] == (dfa, 0, node)


# Generated at 2022-06-13 18:08:09.411729
# Unit test for method classify of class Parser
def test_Parser_classify():
    tree = """
@grammar

simple_stmt = NAME "=" expr

expr = NAME
expr = testlist
expr = expr "+" test
expr = expr "-" test

test = NAME
test = "(" testlist ")"

testlist = testlist test
testlist = test

@end_grammar
"""

    import blib2to3.pgen2.driver
    import blib2to3.pgen2.parse
    from blib2to3.pgen2 import grammar
    from blib2to3.pgen2 import token

    g = grammar.parse_grammar(tree)
    assert g
    p = Parser(g)
    p.setup()
    p.addtoken(token.NAME, 'x', ((0, 0), (0, 1)))

# Generated at 2022-06-13 18:08:16.991657
# Unit test for method shift of class Parser
def test_Parser_shift():
    import io
    import tokens
    import blib2to3.refactor
    p = Parser(blib2to3.refactor.get_fixers_from_package("2to3.fixes"))
    p.setup()
    assert p.stack == []
    p.shift(tokens.NAME, 'Package', 0, None)
    assert p.stack == [(None, 0, (None, None, None, []))]
    p.shift(tokens.NAME, 'import', 1, None)
    assert p.stack == [(None, 1, (None, None, None, []))]

# Generated at 2022-06-13 18:08:21.295261
# Unit test for method push of class Parser
def test_Parser_push():
    grammar = Grammar()
    convert = lambda grammar, node: node
    parser = Parser(grammar, convert)

    type = 0
    value = 'a'
    context = None
    dfa: DFA = [(0, 0), (0, 1)]
    newdfa: DFAS = (dfa, {})
    newstate = 0
    parser.push(type, newdfa, newstate, context)

    expected = [(newdfa, newstate, (0, None, None, []))]
    assert parser.stack == expected
    assert parser.rootnode is None
    return


# Generated at 2022-06-13 18:08:25.391122
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar
    g = grammar.Grammar()
    p = Parser(g)
    p.classify(token.NAME, "foobar", 0)
    assert p.used_names == set(["foobar"])

# Generated at 2022-06-13 18:08:36.319210
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar, token
    
    def convert(grammar, node):
        return node

    p = Parser(grammar.grammar, convert)
    p.setup()
    p.push(grammar.sym.foo, (((1, 2),), {0: 0}), 0, (0,0))
    p.addtoken(token.NAME, "baz", (0,0))
    p.pop()
    assert p.stack == [((((0, 0),), {0: 0}), 0, (grammar.sym.file_input, None, None, [
        (grammar.sym.foo, None, None, [
            (token.NAME, "baz", (0, 0), None)
        ])
    ]))]

# Generated at 2022-06-13 18:08:46.142451
# Unit test for method pop of class Parser
def test_Parser_pop():
    import blib2to3.pgen2.driver
    Driver = blib2to3.pgen2.driver.Driver

    from . import token
    from blib2to3.pgen2.grammar import Grammar

    d = Driver(Grammar(token), convert=lam_sub)
    parser = d.parser
    parser.setup()

    for i in range(5, 1, -1):
        parser.push(i, 1, 1, 1)

    assert parser.stack == [(1, 1, 1), (2, 1, 1), (3, 1, 1), (4, 1, 1)]
    assert parser.pop() is None
    assert parser.stack == [(1, 1, 1), (2, 1, 1), (3, 1, 1)]
    assert parser.pop() is None

# Generated at 2022-06-13 18:09:03.056992
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class fake_grammar:
        start = 1
        dfas = {1: ([[(1, 1)], [(3, 2), (0, 1)], [(3, 3), (0, 2)], [(2, 4), (0, 3)]], {})}
        labels = {1: (token.ERRORTOKEN, None), 2: (token.NAME, "a"), 3: (token.NAME, "b")}
        tokens = {token.ERRORTOKEN: 1, token.NAME: 2}
        keywords = {}

    def fake_convert(grammar: Grammar, node: RawNode) -> Node:
        return Node(type=node[0], children=node[3], context=node[2])


# Generated at 2022-06-13 18:09:08.937403
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2.parse import PseudoToken

    def lam_sub(grammar: Grammar, node: RawNode) -> Optional[NL]:
        # type: (...) -> Optional[NL]
        if node[0] == "test" and len(node) == 2:
            return node[1]
        return None

    # Setup
    parser = Parser(PseudoToken.grammar, lam_sub)
    parser.setup("test")
    parser.addtoken(PseudoToken.NAME, "a", 2)
    parser.addtoken(PseudoToken.NAME, "b", 2)
    parser.addtoken(PseudoToken.NAME, "c", 2)
    parser.addtoken(PseudoToken.NAME, "d", 2)

# Generated at 2022-06-13 18:09:24.376353
# Unit test for method pop of class Parser
def test_Parser_pop():
    import sys
    # This is based on a test_parse_failing() test in
    # test_python_grammar.py in the Python distribution.
    from . import pgen2
    from . import driver
    from . import token
    from .tokenize import generate_tokens as tokenize
    for grammar in "Python", "Python 2.7":
        p = Parser(grammar=pgen2.load_grammar(grammar), convert=lam_sub)
        p.setup()
        # Tokenize the input string
        t = tokenize(
            iter(["raise () from"]).__next__
        )  # type: ignore # Python 2 compatibility
        # And feed the token stream to the parser

# Generated at 2022-06-13 18:09:38.066786
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver
    from blib2to3.pgen2 import tokenize

    def test(s: Text, expected: Text) -> None:
        tokengen = tokenize.generate_tokens(s.__iter__().__next__)
        parser = Parser(driver.grammar, driver.grammar.convert)
        parser.setup()
        for t in tokengen:
            if parser.addtoken(t.type, t.string, t.context):
                break
        assert expected == str(parser.rootnode)


# Generated at 2022-06-13 18:09:43.247411
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar
    from .token import NAME
    from . import symbol

    g = grammar.Grammar()
    p = Parser(g) # type: ignore
    p.setup()
    p.addtoken(NAME, "foo", (1, 0))
    p.push(symbol.term, g.dfas[symbol.term], 0, (1, 0))
    assert p.stack[1:] == [(g.dfas[symbol.term], 0, (symbol.term, None, (1, 0), []))]

# Generated at 2022-06-13 18:09:47.011933
# Unit test for method pop of class Parser
def test_Parser_pop():
    class Dummy:
        pass

    class DummyGrammar:
        dfas = Dummy

    p = Parser(DummyGrammar())
    dfa = [[(1, 2)], [(0, 2)]]
    dfa_v = {"duck": 0, "moo": 2}

    p.stack = [
        (Dummy, 0, ("duck", None, None, None)),
        (Dummy, 0, ("moo", None, None, None)),
    ]

    p.rootnode = None
    p.pop()
    assert not p.stack



# Generated at 2022-06-13 18:09:53.761442
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2 import parse

    g = Grammar()
    p = Parser(g)
    p.setup()
    p.addtoken(1, "a", (1, 2))
    p.addtoken(2, "b", (3, 4))

    t = parse("foo", "a = b\n", g)
    assert t.children[0].children[1].value == "b"
    # end of test_Parser_addtoken

# Generated at 2022-06-13 18:09:56.521804
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import Driver
    from . import grammar

    d = Driver.Driver(grammar, convert=lam_sub)
    d.parse_tokens([(token.NAME, "'abc'")])



# Generated at 2022-06-13 18:10:04.350351
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    assert issubclass(Parser, object)

    g = grammar.Grammar()
    g.load('Parser/Grammar.txt')
    p = Parser(g)

    # The following program has been taken from the Python 3.2 library.
    #
    # The program
    #    d = {k: k*k for k in range(7)}
    #    print(d)
    # produces the output
    #   {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

    p.setup()

# Generated at 2022-06-13 18:10:07.674801
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # Test data
    grammar = Grammar()

    # Unit test code
    p = Parser(grammar)
    assert not p.addtoken(token.ENDMARKER, None, None)
    assert p.stack == [
        (([[(0, 0), (0, 0)], [(0, 1), (0, 1)]], {0: {0}, 1: {}}), 0, (257, None, None, []))
    ]



# Generated at 2022-06-13 18:10:13.652049
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver

    p = driver.Driver()
    p.setup_parser()
    # Cause a pop to occur with no data on stack
    p.reset_parser()
    # Cause a pop to occur with some data on the stack
    p.addtoken(0, "")
    p.reset_parser()
    # Cause a pop to occur with some data on the stack and the rootnode set
    p.addtoken(0, "")
    p.stack.append(None)
    p.reset_parser()

# Generated at 2022-06-13 18:10:25.427630
# Unit test for method shift of class Parser
def test_Parser_shift():
    import sys
    import time

    # Import the table module generated by pgen
    sys.path.insert(0, ".")
    import pygram

    # Create a parser instance
    p = Parser(pygram.grammar, pygram.convert)

    # Prepare for parsing
    p.setup()

    # Input tokens
    def add(type, value=None, context=None):
        return p.addtoken(type, value, context)

    # Parse them
    print("fibonacci(10)")
    add(pygram.NUMBER, "1", None)
    add(pygram.NAME, "fibonacci", None)
    add(pygram.LSQB, None, None)
    add(pygram.NUMBER, "10", None)

# Generated at 2022-06-13 18:11:09.981794
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    g = grammar.Grammar(grammar.n_grammar_rules, grammar.n_grammar_dfas,
                        grammar.n_grammar_labels, grammar.n_grammar_symbol_ids)
    p = Parser(g)
    p.setup()
    t = token.TOKENNAMES
    for tup in [
        (t["NAME"], "foo"),
        (t["EQUAL"], "=="),
        (t["NAME"], "bar"),
        (t["NEWLINE"], "\n"),
        (t["ENDMARKER"], ""),
    ]:
        if p.addtoken(*tup):
            break
    assert p.rootnode is not None



# Generated at 2022-06-13 18:11:17.701300
# Unit test for method push of class Parser
def test_Parser_push():
    # Parser.push(type, newdfa, newstate, context)
    from blib2to3.pgen2.grammar import Grammar, DFA
    from blib2to3.pytree import Leaf

    grammar = Grammar(Grammar, DFA)
    def lam_sub(grammar, node):
        assert node[3] is not None
        return Leaf(node[0], node[3])

    parser = Parser(grammar, lam_sub)
    parser.setup()
    parser.addtoken(1, "a", None)
    parser.addtoken(2, "b", None)
    parser.addtoken(3, "c", None)
    parser.addtoken(4, "d", None)
    parser.addtoken(5, "e", None)

# Generated at 2022-06-13 18:11:27.472750
# Unit test for method setup of class Parser
def test_Parser_setup():
    import os
    import tempfile
    import tokenize
    import io
    from ._driver import Driver
    import blib2to3.pygram

    grammar = blib2to3.pygram.python_grammar2

    # Unfortunately, there are no public methods that return the
    # Python grammar in a format suitable for the Parser class, so we
    # have to use a private method to get the data we need.
    #
    # XXX This is a hack!
    #
    # pgen.pgen takes the following arguments:
    #
    #   pgen [ -h ] grammarin grammarout
    #
    # grammarin is the name of the CSV file containing the Python
    # grammar; grammarout is the name of the Python module in which the
    # compiled grammar is stored.
    #
    # The -h option prints the