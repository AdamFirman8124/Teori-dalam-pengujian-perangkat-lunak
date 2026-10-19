

# Generated at 2022-06-13 18:01:33.423086
# Unit test for method push of class Parser
def test_Parser_push():
    dfa = [None] * 2
    dfa[0] = []
    dfa[1] = [(0, 0)]
    dfa = (dfa, {})
    parser = Parser()
    parser.stack = [(dfa, 0, (1, None, None, []))]
    parser.push(1, dfa, 0, None)
    assert parser.stack == [(dfa, 0, (1, None, None, [])), (dfa, 0, (1, None, None, []))]


# Generated at 2022-06-13 18:01:39.143141
# Unit test for method push of class Parser
def test_Parser_push():
    from . import _parser
    parser = Parser(_parser.grammar)
    parser.setup()
    for i in range(2):
        for type in _parser.tok_dict:
            for value in _parser.tok_dict[type]:
                parser.push(type,  _parser.dfas[_parser.tok_dict[type]], 0, None)
    return parser

# Generated at 2022-06-13 18:01:48.586237
# Unit test for method pop of class Parser

# Generated at 2022-06-13 18:01:56.207864
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    class ParserTest(Parser):
        def __init__(self, grammar):
            Parser.__init__(self, grammar)

    parsertest = ParserTest(grammar.Grammar)
    assert parsertest.classify(token.LPAR, None, Context(1, 0)) == 1
    assert parsertest.classify(token.RPAR, None, Context(1, 0)) == 2
    assert parsertest.classify(token.LSQB, None, Context(1, 0)) == 3
    assert parsertest.classify(token.RSQB, None, Context(1, 0)) == 4
    assert parsertest.classify(token.COLON, None, Context(1, 0)) == 5

# Generated at 2022-06-13 18:01:59.108188
# Unit test for method shift of class Parser
def test_Parser_shift():
    p = Parser(Grammar([]), convert=lam_sub)
    p.setup()
    p.shift(5, 'text', 1, (1,2))
    assert p.rootnode.children == [Node(5, children=['text'], context=(1,2))]


# Generated at 2022-06-13 18:02:08.566957
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar
    from . import tokenize

    def convert(grammar: Grammar, node: RawNode) -> NL:
        # Convert to a pretty-printed version for testing; this is
        # not the right way to convert to an abstract syntax tree!
        assert node[3] is not None
        return Node(type=node[0], children=node[3], context=node[2])

    # Create a parser
    p = Parser(grammar, convert)
    try:            # Should raise ParseError
        p.addtoken(token.STRING, "abc", None)
    except ParseError as e:
        assert e.msg == "bad input" and e.type == token.STRING and e.value == "abc"

# Generated at 2022-06-13 18:02:16.576492
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from lib2to3.main import main
    from io import StringIO
    from sys import argv
    from os.path import abspath, dirname, join
    file = join(dirname(abspath(__file__)), 'examples', 'pprint.py')

    # Replace sys.stdin and sys.stderr with StringIO objects.
    # The output of the test is compared to what's in the file
    # 'examples' + 'parser.out'.
    import sys
    stdin = sys.stdin
    stderr = sys.stderr
    sys.stdin = StringIO(open(file, 'r', encoding='utf-8').read())
    sys.stderr = StringIO()

    # Initialize the parser.
    argv = ['-3', '-f', 'all']
   

# Generated at 2022-06-13 18:02:22.253200
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:02:28.200987
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar
    from . import driver

    g = grammar.Grammar(driver.pgen_grammar_str, driver.pgen_grammar_file)
    p = Parser(g, lam_sub)
    p.setup()
    p.addtoken(1, 'test1', (1, 1))
    p.addtoken(11, 'test11', (1, 11))
    p.addtoken(4, 'test4', (1, 4))
    p.pop()
    assert p.rootnode.children[0].children[0].value == 'test11'



# Generated at 2022-06-13 18:02:39.431204
# Unit test for method shift of class Parser
def test_Parser_shift():
    # Create a parser instance
    import blib2to3.pgen2.grammar as pgen_grammar
    import blib2to3.pgen2.pgen as pgen_pgen
    grammar = pgen_grammar.Grammar(pgen_pgen.driver.grammar.grammar())
    parser = Parser(grammar, convert=pgen_pgen.driver.convert)

    # Create a token
    class mock_Context:
        def __init__(self, ctxt):
            self.context = ctxt
    token = (1, "hello", mock_Context("context"))

    # Call method shift of class Parser
    parser.shift(*token)

    # Check the result
    assert parser.stack[-1][-1] == token[:-1] + (None,)


# Unit

# Generated at 2022-06-13 18:02:52.945264
# Unit test for method pop of class Parser
def test_Parser_pop():
    class MyParser(Parser):
        def __init__(self, grammar, convert=None):
            Parser.__init__(self, grammar, convert)
            self.rootnode_result: Optional[NL] = None

        def pop(self):
            Parser.pop(self)
            self.rootnode_result = self.rootnode

    def convert(grammar, node):
        return None  # type: ignore

    grammar = Grammar("") # type: ignore
    grammar.dfas[1] = grammar.dfas[2] = ([[(0, 0)]], set())
    p = MyParser(grammar, convert)
    p.setup()
    p.push(2, grammar.dfas[2], 0, None)
    p.pop()
    assert p.rootnode_result is None



# Generated at 2022-06-13 18:03:01.129726
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest

    class ParserTestCase(unittest.TestCase):
        # Unit test for method get_children of class Parser
        def test_get_children(self):
            from . import driver

            g = driver.load_grammar("Blib/Parser/Python.gram")
            p = Parser(
                g,
                convert=lam_sub,
            )
            p.setup()
            assert p.addtoken(3, "def", (1, 0))

    unittest.main()

# Generated at 2022-06-13 18:03:12.906835
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, tokenize
    from .token import token_to_string

    parser = Parser(grammar.Grammar())

    def parse(s):
        parser.setup()
        add = parser.addtoken
        for token in tokenize.generate_tokens(iter(s).__next__):
            if add(*token):
                break
        else:
            raise RuntimeError("unexpected EOF")

    def check(s, expected):
        parse(s)
        print("%s -> %s" % (repr(s), repr(parser.rootnode)))
        assert parser.rootnode == expected


# Generated at 2022-06-13 18:03:23.269161
# Unit test for method pop of class Parser
def test_Parser_pop():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('grammar')
    parser.add_argument('-V', '--verbose', action='store_true', default=False)
    args = parser.parse_args()

    grammar = Grammar(args.grammar)
    p = Parser(grammar)
    p.setup()

    def parseline(line):
        for type, value, context in tokenize.generate_tokens(tokenize.StringIO(line).readline):
            p.addtoken(type, value, context)

    if args.verbose:
        if p.stack and p.stack[-1] and p.stack[-1][-1]:
            print(p.stack[-1][-1])
            p.pop()

# Generated at 2022-06-13 18:03:37.967310
# Unit test for method shift of class Parser
def test_Parser_shift():
    from pprint import pprint
    import blib2to3.pgen2.parse as parse
    import blib2to3.pgen2.tokenize as tokenize
    import blib2to3.pgen2.driver as driver
    import blib2to3.pgen2.grammar as grammar
    import blib2to3.pgen2.convert as convert
    import io

    f = io.StringIO("""
word = 'hello'
""")
    g = driver.load_grammar()
    t = tokenize.generate_tokens(f.readline)
    p = parse.Parser(g)
    p.setup()
    for type, value, start, end, line in t:
        if p.addtoken(type, value, (start, end)):
            break
    p

# Generated at 2022-06-13 18:03:54.739210
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    g = grammar.Grammar(open(grammar.__file__))
    p = Parser(g, lam_sub)
    p.setup()
    tokens = [
        (token.NAME, "while", (1, 0)),
        (token.INDENT, "", (2, 0)),
        (token.NAME, "if", (2, 0)),
        (token.NAME, "else", (3, 0)),
        (token.DEDENT, "", (3, 0)),
        (token.NEWLINE, "", (3, 0)),
        (token.DEDENT, "", (4, 0)),
    ]
    for t, v, c in tokens:
        p.addtoken(t, v, c)
    root = p.rootnode
    assert len(root) == 2

# Generated at 2022-06-13 18:04:05.347250
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys
    import os
    # import pdb

    p = Parser(get_pickle())
    p.setup()

    tokens = list(tokenize("print a", "exec"))
    tokens.reverse()

    def addtokens(tokens):
        while tokens:
            type, value, begin, end, line = tokens.pop()
            classifier = sys.getrefcount(type)
            p.addtoken(type, value, (begin, end))
            print("%s %s %s %s %s %s %s" % (type, classifier, value, begin, end, line, p.stack))
            # pdb.set_trace()

    addtokens(tokens)

    sys.stderr.write("=== Next ===\n")


# Generated at 2022-06-13 18:04:13.481971
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2 import driver

    grammar = driver.load_grammar("Grammar/Grammar")
    converter = driver.load_converter(grammar)
    p = Parser(grammar, converter)
    p.setup()
    p.addtoken(token.NUMBER, "1", (1,0))
    p.addtoken(token.LSQB, None, (1,2))
    p.addtoken(token.RSQB, None, (1,3))
    assert p.rootnode.type == grammar.symbol2number["test_list"]
    assert p.rootnode.children[0].type == token.NUMBER
    assert p.rootnode.children[1].type == grammar.symbol2number["subscript_list"]

# Generated at 2022-06-13 18:04:19.636616
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .grammar import parse_grammar, Grammar
    from .token import Token
    from . import token

    # The fun begins here
    test_grammar = parse_grammar(
        """
        stmt: simple_stmt ';'
        simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
        small_stmt: flow_stmt
        """
    )
    p = Parser(test_grammar)
    p.setup()

    simple_stmt_token = Token(token.NAME, 'simple_stmt',(0,0),(0,0))
    newline_token = Token(token.NEWLINE, '', (0,0), (0,0))
    #push simple_stmt into stack

# Generated at 2022-06-13 18:04:22.349298
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    _test_Parser_addtoken()



# Generated at 2022-06-13 18:04:39.534238
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    def mksymbol(num: int, *kids: Union[Text, NL]) -> NL:
        return Node(type=num, children=kids)


# Generated at 2022-06-13 18:04:42.034258
# Unit test for method pop of class Parser
def test_Parser_pop():
    p = Parser(Grammar())
    p.stack = [('blah', 'blah', None)]
    try:
        p.pop()
    except Exception as e:
        assert type(e)==IndexError

# Generated at 2022-06-13 18:04:44.970099
# Unit test for method setup of class Parser
def test_Parser_setup():
    class TestPgenGrammar(Grammar):
        pass

    parser = Parser(grammar=TestPgenGrammar)
    parser.setup(1)
    assert parser.stack == [(TestPgenGrammar.dfas[1], 0, (1, None, None, []))]

# Generated at 2022-06-13 18:04:48.062453
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import pgen
    from sys import argv

    grammar = pgen.Grammar()
    with open(argv[1]) as file:
        grammar.parse(file)
    parser = Parser(grammar)
    parser.setup()
    parser.shift(token.NAME, 'name', 0, Context(1, 0))
    assert parser.stack[-1][2] == (0, None, None, None)



# Generated at 2022-06-13 18:04:50.226642
# Unit test for method pop of class Parser
def test_Parser_pop():
    global a_var
    a_var = 5
    def foo(a: int) -> None:
        nonlocal a_var
        a_var = a
        def bar() -> None:
            foo(a_var)
        bar()
    foo(a_var)

# Generated at 2022-06-13 18:05:01.674489
# Unit test for method pop of class Parser
def test_Parser_pop():
    # See http://bugs.python.org/issue4633
    class TestParser(Parser):
        def __init__(self, convert: Optional[Convert] = None) -> None:
            Parser.__init__(self, Grammar(), convert)
            self.stack: List[Tuple[DFAS, int, RawNode]] = []
            self.rootnode: Optional[Node] = None
    tp = TestParser()
    tp.grammar.dfas = {
        1: ([[(257, 1)], [(258, 2)], [(0, 3)]], {1: 1, 2: 2, 3: 3})
    }
    tp.grammar.labels = [(257, None), (258, None)]

# Generated at 2022-06-13 18:05:13.650010
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .pgen2.parse import driver
    from .pgen2.grammar import Grammar
    from .pgen2.pgen import generate_grammar

    grammar = Grammar(generate_grammar("Parser/Grammar"))
    p = Parser(grammar)
    p.setup()
    driver.tokenize = driver.tokenize_mine
    # Fake parser.shift
    def shift(
        type: int, value: Optional[Text], newstate: int, context: Context
    ) -> None:
        assert type == token.NEWLINE
        assert value == "\n"
        assert newstate == 1
        assert context is not None
        assert context.string == "\n"

    p.shift = shift
    # Fake parser.push

# Generated at 2022-06-13 18:05:24.748699
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    t = []

    p = Parser(grammar)
    p.setup()
    for type, value, context in [
        (token.NAME, "a", (1, 0)),
        (token.EQUAL, "=", (1, 1)),
        (token.NAME, "b", (1, 2)),
        (token.PLUSEQUAL, "+=", (1, 3)),
        (token.NAME, "c", (1, 4)),
        (token.NEWLINE, "\n", (1, 5)),
        (token.ENDMARKER, "", (1, 6)),
    ]:
        if p.addtoken(type, value, context):
            break

# Generated at 2022-06-13 18:05:35.258180
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import pgen2

    def test_Parser_shift_inner(
        type: int, value: Optional[Text], newstate: int, context: Context
    ) -> None:
        from . import token
        from blib2to3.fixer_util import Leaf
        from blib2to3.pgen2.parse import ParseError
        from blib2to3.pgen2.grammar import Grammar

        assert value is not None


# Generated at 2022-06-13 18:05:41.460072
# Unit test for method pop of class Parser
def test_Parser_pop():
    # Doc-tests tend to crash the whole program
    # A single test can be run via:
    #   python -c 'import blib2to3.pgen2.parser; blib2to3.pgen2.parser.test_Parser_pop()'
    assert Parser(None).pop() is None



# Generated at 2022-06-13 18:06:04.952477
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2.tokenize import generate_tokens
    from blib2to3.pgen2 import token, driver

    def get_next_token(buffer: Text) -> Tuple[int, Optional[Text], Context]:
        tokens = generate_tokens(buffer)
        token_type, token_value, _, _, _ = next(tokens)
        return token_type, token_value, _

    def get_label(lhs: Text, rhs: Sequence[Text]) -> Text:
        return lhs + " " + " ".join(rhs)

    def classify(p: Parser, buffer: Text) -> int:
        token_type, token_value, context = get_next_token(buffer)

# Generated at 2022-06-13 18:06:13.208103
# Unit test for method pop of class Parser
def test_Parser_pop():
    p = Parser(None)
    p.popdfa = 'popdfa'
    p.popstate = 'popstate'
    p.popnode = 'popnode'
    p.stack = []
    p.stack.insert(0, ('dfa', 'state', 'node'))
    from blib2to3.pytree import Leaf
    from blib2to3.pgen2.token import NAME
    from blib2to3.pgen2.grammar import Grammar
    from six import text_type
    class mock_Grammar(Grammar):
        def __init__(self):
            super(mock_Grammar, self).__init__()
        def convert(self, grammar, popnode):
            return Leaf(NAME, 'test_name', None)
    mock_grammar = mock

# Generated at 2022-06-13 18:06:14.720651
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # Test the addtoken() method for non-exceptions
    pass



# Generated at 2022-06-13 18:06:19.663786
# Unit test for method shift of class Parser
def test_Parser_shift():
    import blib2to3.pgen2.token as token
    import blib2to3.pgen2.grammar as grammar
    import blib2to3.pgen2.parse as parse
    import unittest

    class TestParser(unittest.TestCase):
        def setUp(self):
            self.grammar = grammar.grammar
            self.parser = parse.Parser(self.grammar)

        def test_shift(self):
            self.parser.setup()
            self.parser.addtoken(token.COMMENT, '#Comment', (1, 1))

    unittest.main()


# Generated at 2022-06-13 18:06:30.011529
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import dg
    from . import parser
    from . import literals as lit
    # prepare for parsing
    grammar = dg.load_grammar(
        """
        start: E $
        E: E "+" T
         | T
        T: T "*" F
         | F
        F: "(" E ")"
         | "x"
        %ignore "+"
        %ignore "*"
        %ignore "("
        %ignore ")"
        """
    )
    p = parser.Parser(grammar)
    p.setup()
    for t in lit.string_iter("x + x * x (x)"):
        if p.addtoken(t[0], t[1], t[2]):
            break
    # verify abstract syntax tree
    print("root node:")

# Generated at 2022-06-13 18:06:35.964199
# Unit test for method push of class Parser
def test_Parser_push():
    class Node(object):
        pass

    def func(grammar, node):
        return Node()

    parser = Parser(None, func)
    parser.stack = [(1, 2, Node()), (3, 4, Node())]
    result = parser.push(5, (6, 7), 8, None)
    assert parser.stack == [(1, 2, Node()), (3, 4, Node()), (5, 0, Node())]

# Generated at 2022-06-13 18:06:39.880713
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2.parse import parse_grammar
    import StringIO
    buf = StringIO.StringIO("""
    %start_symbol block
    %lexical_states FOO
    %ignore BAR
    %%
    block: stmt*;
    stmt: NAME ';';
    """)
    start = parse_grammar(buf, "input")
    p = Parser(start)
    p.setup()
    p.addtoken(token.NAME, "a", None)
    p.addtoken(token.SEMI, ";", None)
    p.shift(token.NAME, "b", None, None)

# Generated at 2022-06-13 18:06:45.600260
# Unit test for method classify of class Parser
def test_Parser_classify():
    import pprint
    import blib2to3.pgen2.grammar, blib2to3.pgen2.parse, blib2to3.pytree

    def check_raw_conversion(t, name, tree, raw):
        if tree != raw:
            t.fail("Testing " + name + ": " + "expected " + repr(raw) + ", got " + repr(tree))

    p = blib2to3.pgen2.parse.Parser(blib2to3.pgen2.grammar.grammar,
                                    blib2to3.pytree.convert)
    p.setup()
    # Check classify method
    def addtoken(type: int, value: Optional[Text] = None, context: Context = None) -> None:
        p.addtoken(type, value, context)

# Generated at 2022-06-13 18:06:57.464775
# Unit test for method push of class Parser
def test_Parser_push():
    class TestGrammar(Grammar):
        labels = ('A', 'B', 'C')
        dfas = {'A': ([[(2, 1), (0, 0)], [(1, 0), (0, 0)]], {0: 1}),
                'B': ([[(2, 1), (0, 0)]], {0: 1}),
                'C': ([[(1, 0), (0, 0)]], {0: 1})}
        start = 'A'

    parser = Parser(TestGrammar())
    parser.push('B', TestGrammar().dfas['B'], 0, None)
    parser.push('C', TestGrammar().dfas['C'], 0, None)
    # Pop a nonterminal.  (Internal)
    # The expected output is: [('

# Generated at 2022-06-13 18:07:03.333348
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver, grammar, token
    p = Parser(grammar)
    p.setup()
    t = driver.tokenize("foo")
    t.send(None)
    try:
        while True:
            if p.addtoken(next(t)[0], None, None):
                break
    except ParseError:
        raise AssertionError("could not parse foo")
    p.setup(start=7)
    t = driver.tokenize("foo")
    t.send(None)
    try:
        while True:
            if p.addtoken(next(t)[0], None, None):
                break
    except ParseError:
        pass
    else:
        raise AssertionError("parsed foo through start symbol 7")
    p.setup()

# Generated at 2022-06-13 18:07:24.601877
# Unit test for method shift of class Parser
def test_Parser_shift():
    code = """
print(1)
print(2)
"""
    tokens: Sequence[Tuple[int, Text, Context]] = tokenize.generate_tokens(StringIO(code).readline)
    p = Parser(g, convert)
    p.setup()
    for t, v, c in tokens:
        if p.addtoken(t, v, c):
            break
    print(p.rootnode)
    assert(p.rootnode == [FileInput([SimpleStmt([Printnl([Const([1])], None)]), Printnl([Const([2])], None)], None)])

# Generated at 2022-06-13 18:07:26.074612
# Unit test for method push of class Parser
def test_Parser_push():
    parser = None  # type: Parser
    parser.push(0, 0, 0, 0)

# Generated at 2022-06-13 18:07:37.102188
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import pygram
    from . import pytree
    from . import driver
    from . import tokens

    pygram.init_grammar(pygram.python_grammar)
    tr = driver.Driver(pygram.python_grammar, convert=pytree.convert)

    # 1. simple expression with (1+2)*3
    tr.setup()
    tr.addtoken(tokens.NAME, "*", (1, 0))
    tr.addtoken(tokens.NUMBER, "3", (1, 2))
    tr.addtoken(tokens.OP, ")", (1, 3))
    tr.addtoken(tokens.NUMBER, "2", (1, 4))
    tr.addtoken(tokens.OP, "+", (1, 5))

# Generated at 2022-06-13 18:07:44.730633
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys
    import io
    import unittest

    # Set up the grammar
    grammar = Grammar()
    grammar.start = "start"
    grammar.add_nonterminal("start", ["xor_expr", "NEWLINE", "EOF"])
    grammar.add_nonterminal("xor_expr", ["xor_expr", "XOR", "and_expr"])
    grammar.add_nonterminal("xor_expr", ["and_expr"])
    grammar.add_nonterminal("and_expr", ["and_expr", "AND", "shift_expr"])
    grammar.add_nonterminal("and_expr", ["shift_expr"])
    grammar.add_nonterminal("shift_expr", ["shift_expr", "LSHIFT", "a_expr"])
    grammar.add_

# Generated at 2022-06-13 18:07:47.360355
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .parser_test import test_Parser_pop
    return test_Parser_pop()


# Generated at 2022-06-13 18:07:55.441461
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, driver

    gram = grammar.Grammar(grammar.Grammar._Grammar__generate_pygram())
    p = Parser(gram)
    p.setup()
    for tok in driver.tokenize_str("if False: pass"):
        if p.addtoken(*tok):
            break
    else:
        assert False, "not finished"
    assert p.rootnode
    assert isinstance(p.rootnode, Node)

# Generated at 2022-06-13 18:08:04.158018
# Unit test for method classify of class Parser

# Generated at 2022-06-13 18:08:13.987096
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    PYTHON_GRAMMAR_FILE = "python37.grammar"

    pgen, token2symbol, type2name = grammar.load_grammar(PYTHON_GRAMMAR_FILE)

    parser = Parser(pgen, None)

    assert parser.classify(token.NAME, "True", None) == 2

    assert parser.classify(token.LPAR, None, None) == 33

    assert parser.classify(token.MINUS, None, None) == 34

    assert parser.classify(token.MULT, None, None) == 35

    assert parser.classify(token.DIV, None, None) == 41

# Generated at 2022-06-13 18:08:20.548112
# Unit test for method pop of class Parser

# Generated at 2022-06-13 18:08:27.913179
# Unit test for method shift of class Parser
def test_Parser_shift():
    class MockGrammar():
        def __init__(self):
            self.dfas = {'START': (1, 2),
                         'NAME': (1, 2)
                         }
        def classify(self, type: int, value: Union[Text, Text], context: Text) -> int:
            return type

    class MockNode():
        def append(self, node):
            self.children.append(node)
            return self

        def __init__(self):
            self.children = []

    input_data = [(10, 'name', 'line'), (20, 'def', 'line'), (30, 'function', 'line')]
    p = Parser(MockGrammar(), MockNode)
    p.setup()
    print(p.stack)
    print(p.rootnode)

# Generated at 2022-06-13 18:09:06.896781
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import doctest_support

    p = Parser(doctest_support.grammar)
    p.setup()
    for i in range(10):
        p.shift(doctest_support.leaf, None, 1, None)
    p.pop()
    p.push(0, 1, 1, None)
    p.pop()
    p.push(0, 1, 1, None)
    p.pop()


# Generated at 2022-06-13 18:09:21.028149
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2.grammar import Grammar

    # Create Parser
    grammar = Grammar(grammar_file="Grammar/Grammar",
                      symbol2number={"expr_stmt": 256},
                      token2number={"NAME": 257},
                      keywords={"foo": 258},
                      labels=[("expr_stmt", 256), ("NAME", 257)])
    parser = Parser(grammar)

    # Test error reporting
    try:
        parser.addtoken("foo", None, (1, 1))
    except ParseError as e:
        assert e.type == "foo"
        assert e.value is None
        assert e.context == (1, 1)
    else:
        assert False, "expected ParseError"

    # Test shift

# Generated at 2022-06-13 18:09:23.635852
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import driver
    g = driver.Grammar()
    parser = Parser(g)
    parser.setup()



# Generated at 2022-06-13 18:09:37.766101
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar, token
    grammar = grammar.Grammar(
        """
        input: items | empty ;
        items: item items ;
        empty: ;
        item: NAME | LPAR NAME RPAR ;
        """,
        __file__,
    )
    parser = Parser(grammar)
    parser.setup()
    newstate = parser.addtoken(token.NAME, "x", (1, 0))
    assert newstate
    newstate = parser.addtoken(token.LPAR, "(", (1, 2))
    assert not newstate
    newstate = parser.addtoken(token.NAME, "y", (1, 3))
    assert not newstate
    newstate = parser.addtoken(token.RPAR, ")", (1, 5))
    assert newstate



# Generated at 2022-06-13 18:09:44.847783
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, driver, token

    def _get_grammar(grammar: Text) -> Grammar:
        return grammar.Grammar(grammar, driver.grammar)

    def _parse_string(g: Grammar, s: Text) -> Optional[NL]:
        dt = driver.Driver(g, convert)
        return dt.parse_string(s)

    # Type1 is just an integer that encodes the
    # token type and the token value.

    def _create_tokens(s: Text) -> Sequence[int]:
        tokens = []
        for value in s.split():
            if value in driver.keyword_tokens:
                type = driver.keyword_tokens[value]
            elif value[0] == '"':
                type = token.STRING
            el

# Generated at 2022-06-13 18:09:50.951400
# Unit test for method shift of class Parser
def test_Parser_shift():
    grammar = Grammar(
        r"""
    # Test grammar for unit test of method shift of class Parser
    root_rule: a b c ;
    a: 'a' ;
    b: 'b' ;
    c: 'c' ;
    """)
    parser = Parser(grammar)
    parser.setup("root_rule")
    parser.addtoken(token.NAME, "a", (1, 0))
    parser.addtoken(token.NAME, "b", (1, 0))
    parser.addtoken(token.NAME, "c", (1, 0))

# Generated at 2022-06-13 18:10:00.443140
# Unit test for method pop of class Parser
def test_Parser_pop():
    import sys
    import blib2to3.pgen2.grammar
    from blib2to3.pgen2.parse import ParseError
    from blib2to3.pgen2 import token

    g = blib2to3.pgen2.grammar.grammar

    def lam_sub(grammar, node):
        assert node[3] is not None
        return Node(type=node[0], children=node[3], context=node[2])

    p = Parser(g, lam_sub)
    p.setup()
    p.addtoken(5, 5, 5)
    p.addtoken(6, 6, 6)
    p.pop()
    p.pop()
    try:
        p.pop()
    except ParseError:
        return

# Generated at 2022-06-13 18:10:06.751587
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .tokenize import generate_tokens

    from . import grammar

    test_grammar = grammar.Grammar(generate_tokens)

    from .driver import Driver

    test_driver = Driver(test_grammar, None)

    test_parser = Parser(test_grammar, None)

    test_parser.pop()

# Generated at 2022-06-13 18:10:16.421536
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class Token(object):
        def __init__(self, type: int, value: Optional[Text] = None) -> None:
            self.type = type
            self.value = value

    class MockGrammar(object):
        def __init__(self, dfas: Dict[int, DFAS], labels: Dict[int, Tuple[int, Text]]) -> None:
            self.dfas = dfas
            self.labels = labels

        def __getitem__(self, key: Any) -> Any:
            return self.dfas[key]

    class MockContext(object):
        def __init__(self, context: Sequence[Any]) -> None:
            self.context = context

        def __repr__(self) -> Text:
            return repr(self.context)


# Generated at 2022-06-13 18:10:26.177676
# Unit test for method shift of class Parser
def test_Parser_shift():
    # The first shift
    stack = [ (([[(0, 0)], [(1, 1)]], {0: 0, 1: 1}), 0, (2, None, None, []))]
    p = Parser(Grammar(
        start=2,
        dfas={2: ([[(0, 0)], [(1, 1)]], {0: 0, 1: 1})},
        labels={0: (1, None), 1: (3, None)},
        tokens={1: 0, 3: 1}
    ))
    p.stack = stack
    p.shift(1, '+', 1, None)