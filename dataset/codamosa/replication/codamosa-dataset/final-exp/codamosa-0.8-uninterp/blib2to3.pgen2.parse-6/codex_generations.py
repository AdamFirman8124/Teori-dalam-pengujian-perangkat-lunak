

# Generated at 2022-06-13 18:01:42.865856
# Unit test for method push of class Parser
def test_Parser_push():
    grammar = Grammar()
    p = Parser(grammar)
    p.setup()
    p.stack = [(None, None, None)]
    p.push(1, (None, None), 2, None)
    assert p.stack == [(None, None, None), (None, None, (1, None, None, []))]

# Generated at 2022-06-13 18:01:52.040037
# Unit test for method shift of class Parser
def test_Parser_shift():
    import sys

    def my_convert(grammar: Grammar, node: RawNode) -> NL:
        assert node[3] is not None
        return Node(type=node[0], children=node[3], context=node[2])

    p = Parser(Grammar(sys.modules[__name__].__dict__), my_convert)
    p.setup()
    assert p.addtoken(token.INDENT, " ", (1, 0))
    assert p.addtoken(token.INDENT, " ", (1, 0))
    assert p.addtoken(token.INDENT, " ", (1, 0))
    assert p.addtoken(token.INDENT, " ", (1, 0))
    assert p.addtoken(token.INDENT, " ", (1, 0))
    assert p.addtoken

# Generated at 2022-06-13 18:02:00.779830
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2.tokenize import generate_tokens, StringIO
    from blib2to3.pgen2 import driver, token, grammar
    import StringIO
    import unittest

    class TestParser(unittest.TestCase):
        """Tests for the Parser."""

        def test_simple(self):
            # Simple case for an empty file
            input = StringIO.StringIO("")
            grammar = driver.load_grammar("Grammar.txt")
            p = Parser(grammar)
            # Supply the input
            p.setup()
            for (type, value, context, dummy) in generate_tokens(input.readline):
                print(type, token.tok_name[type], value)
                p.addtoken(type, value, context)


# Generated at 2022-06-13 18:02:10.896035
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import doctest
    from . import grammar, token, tokenize
    import sys
    from .pytree import Leaf

    # Turn off tracing
    class Options(object):
        trace = False
    options = Options()
    gram = grammar.Grammar()
    gram.load_file("Grammar.txt")
    gram.dump()
    # Make sure we can parse simple_stmt
    parser = Parser(gram)
    parser.setup(gram.symbol2number["simple_stmt"])
    parser.stack
    for t in tokenize.generate_tokens(sys.stdin.readline):
        try:
            if parser.addtoken(t[0], t[1], t[2]):
                break
        except ParseError:
            raise
        parser.stack
    else:
        print

# Generated at 2022-06-13 18:02:17.107926
# Unit test for method shift of class Parser
def test_Parser_shift():
    result_node = Node(type=1, children=[Leaf(1, '1'), Leaf(2, '2'), Leaf(3, '3')],
                       context=Context(preceding=None, parent=None,
                                       file_encoding=None))
    parser = Parser(grammar=Grammar())
    parser.shift(1, '1', 0, Context())
    parser.shift(2, '2', 0, Context())
    parser.shift(3, '3', 0, Context())
    assert len(parser.stack) == 1
    assert parser.stack[0][-1] == result_node


# Generated at 2022-06-13 18:02:26.456262
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """
    from pprint import pprint
    from .token import tok_name

    def helper(p, token):
        print("token: %s" % tok_name[token.type]),
        print("value: %r" % token.value)
        p.addtoken(*token)
        pprint(p.stack)
        print()

    grammar = grammar.grammar
    p = Parser(grammar)
    p.setup()
    helper(p, Token(OP, "("))
    helper(p, Token(NUMBER, "1"))
    helper(p, Token(OP, "-"))
    helper(p, Token(NUMBER, "2"))
    helper(p, Token(OP, ")"))
    """

# Generated at 2022-06-13 18:02:38.177459
# Unit test for method classify of class Parser
def test_Parser_classify():
    """Test for method classify of class Parser"""
    # "grammar" must be initialized before using the Parser class
    grammar = Grammar()

# Generated at 2022-06-13 18:02:48.183505
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import io
    from ..pgen2.driver import Driver
    from . import token

    # Compile a grammar into a Parser instance
    driver = Driver(grammar_name="Grammar", output=io.StringIO())
    parser = driver.build_parser()

    # Feed input to the parser
    # (We use a hand-compiled version of eval_input; it's a bit complex.)
    parser.setup()
    assert parser.addtoken(token.NAME, "spam", (1, 0)) == False
    assert parser.addtoken(token.OP, "+", (1, 4)) == False
    assert parser.addtoken(token.NAME, "eggs", (1, 6)) == False
    assert parser.addtoken(token.ENDMARKER, "", (1, 10)) == True
    root = parser.root

# Generated at 2022-06-13 18:02:56.346855
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """Test the addtoken method of class Parser.

    The examples were taken from the original C implementation.

    """
    # Pare down the grammar so it isn't too large
    grammar = Grammar(
        """
        stmt: simple_stmt
            | compound_stmt
        simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
        small_stmt: pass_stmt
                  | flow_stmt
                  | print_stmt
        pass_stmt: 'pass'
        flow_stmt: return_stmt
        print_stmt: 'print'
        return_stmt: 'return'
        compound_stmt: if_stmt
        if_stmt: 'if'
        """
    )
    grammar.parser = Parser(grammar)


# Generated at 2022-06-13 18:03:01.409078
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar

    # Create mock for class Parser
    class MockParser:
        def __init__(self, grammar: Grammar, convert: Optional[Convert] = None) -> None:
            self.grammar = grammar
            self.convert = convert or lam_sub

    # Create mock for class Grammar
    class MockGrammar:
        def __init__(self) -> None:
            self.tokens = {
                token.NAME: 0,
                token.NUMBER: 1,
                token.STAR: 3,
                token.PLUS: 4,
                token.MINUS: 5,
                token.EQUAL: 6,
            }
            self.labels = [("NAME", 0), ("NUMBER", 1), ("PLUS", 4)]

# Generated at 2022-06-13 18:03:15.158788
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class MockGrammar:
        def __init__(self, token_to_label):
            self.tokens = token_to_label
            self.start = 257
            self.dfas = {257: ([[(268, 1)], [(0, 1)]], {1: 268})}
        def add_label(self, t):
            self.labels.append((t, None))
            return len(self.labels) - 1
        labels = [(token.LBRACE, None), (token.RBRACE, None)]
    class MockContext:
        pass
    p = Parser(MockGrammar({token.LBRACE: 0, token.RBRACE: 1}), None)
    p.setup()
    assert not p.addtoken(token.LBRACE, None, MockContext())
   

# Generated at 2022-06-13 18:03:20.475958
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2.parse import ParseError
    from blib2to3.pgen2 import grammar
    import StringIO

    g = grammar.Grammar(StringIO.StringIO(
        """
        # Grammar here
        """))
    p = Parser(g)
    p.setup()
    p.shift(0, None, 0, Context(None, 0))

# Generated at 2022-06-13 18:03:28.810723
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver as driver
    from . import literals as literals

    load_grammar = driver.load_grammar
    # The following are from test_analyze2.py

# Generated at 2022-06-13 18:03:38.466643
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2.tokenize import generate_tokens, untokenize
    from blib2to3.pgen2.parse import tokenize

    def nfa2dfa(nfa: DFA) -> DFA:
        if nfa is None:
            return None

        newnfa: DFA = []
        worklist: List[Set[int]] = [set(nfa[0])]

        while worklist:
            state = worklist.pop(0)
            arcs = {}
            #print('\nnewnfa:', newnfa)
            #print('state:', state)
            for s in state:
                for a, target in nfa[s]:
                    if a is not None:
                        arcs.setdefault(a, set()).add(target)
            #print('

# Generated at 2022-06-13 18:03:55.225302
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2 import tokenize
    from blib2to3.pgen2.parse import ParseError, get_yacc

    g = get_yacc()

    p = Parser(g)
    p.setup()
    p.addtoken(token.NL, '\n', (1, 0))
    p.addtoken(token.INDENT, '    ', (2, 0))
    p.addtoken(token.NAME, 'import', (2, 4))
    p.addtoken(token.NAME, 'foo', (2, 11))
    p.addtoken(token.DEDENT, '', (3, 0))
    p.addtoken(token.ENDMARKER, '', (3, 0))


# Generated at 2022-06-13 18:04:05.849623
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver
    import os
    import tempfile
    import textwrap
    import time

    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-13 18:04:10.961365
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import pygram

    stack = []
    parser = Parser(pygram.python_grammar)
    popdfa = [1, 2]
    popstate = 0
    popnode = "node"
    parser.stack.append((popdfa, popstate, popnode))
    parser.stack.append((3, 4, "node"))
    parser.pop()
    assert parser.stack == [(popdfa, popstate, popnode)]



# Generated at 2022-06-13 18:04:17.971793
# Unit test for method push of class Parser
def test_Parser_push():
    NullNode = None  # type: ignore
    class Grammar:
        dfas = {
            "test_Parser_push": (
                [[(0, 1)]],
                {0: {0: [(0, 0)]}, 1: {1: [(0, 1)], 257: [(0, 1)], 258: [(0, 1)]}},
            )
        }
        labels = {0: (257, None), 1: (258, None)}
        tokens = {257: 0, 258: 1}
        keywords = {}
    grammar = Grammar()
    p = Parser(grammar)
    p.setup("test_Parser_push")

# Generated at 2022-06-13 18:04:25.929840
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .pgen import Grammar, driver

    g = Grammar(driver.grammar, driver.keywords)
    p = Parser(g)
    p.setup()
    p.addtoken(token.NUMBER, "42", None)
    p.addtoken(token.NAME, "spam", None)
    p.addtoken(0, None, None)
    print(p.rootnode)
    #print(p.rootnode.leaves())


# Self-test code (fodder for test_parser)

# Generated at 2022-06-13 18:04:30.994087
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    # make sure that classify recognizes the keyword 'class'
    g = grammar.grammar
    p = Parser(g)
    p.setup()
    assert p.classify(token.NAME, "class", (0, 0)) == g.keywords['class']

# Generated at 2022-06-13 18:04:39.886203
# Unit test for method pop of class Parser
def test_Parser_pop():
    p = Parser(Grammar())
    p.setup()
    popdfa = []
    popstate = 0
    popnode = (1, None, None, [])
    p.stack.append((popdfa, popstate, popnode))
    p.pop()

# Generated at 2022-06-13 18:04:52.119889
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import io
    import re
    from . import driver
    from . import tokenize as tokenize_mod
    from . import parser

    # Construct a simple grammar to parse 'a+b'
    start = 257
    rules = [
        (start, [ "(", start, ")" ]),
        (start, [ start, "+", start ]),
        (start, [ "a" ]),
        (start, [ "b" ]),
    ]
    grammar = parser.pgen.make_grammar(tokenizer_mod.word_tokens, rules)

    # Construct a simple tokenizer from a source

    def nexttoken(src):
        """Token generator for the expression 'a+b'.

        This generator returns a series of (type, string) pairs,
        where type is an int and string is a string.

        """
       

# Generated at 2022-06-13 18:04:57.514859
# Unit test for method classify of class Parser
def test_Parser_classify():
    import blib2to3.pgen2.pgen

    grammar = blib2to3.pgen2.pgen.Grammar()
    parser = Parser(grammar)

    parser.classify(token.ADD, "+", (1, 0))

# Generated at 2022-06-13 18:05:02.888240
# Unit test for method setup of class Parser
def test_Parser_setup():
    import pprint
    import sys
    import tokenize
    from .driver import Driver
    import grammar
    import pgen2.parse
    import StringIO

    # Python grammar
    with open("Grammar/Grammar", "r") as gf:
        driver = Driver(grammar, gf.read())

    driver.pgen()

    # Tokenize a small Python program

# Generated at 2022-06-13 18:05:06.132981
# Unit test for method setup of class Parser
def test_Parser_setup():
    Parser(grammar=Grammar()).setup()
    Parser(grammar=Grammar()).setup('test symbol')


# Generated at 2022-06-13 18:05:10.995969
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    g = grammar.parse_grammar("Grammar.txt")
    p = Parser(g)
    p.setup()
    p.addtoken(token.LPAR, "(", Context(L, 0))
    p.addtoken(token.RPAR, ")", Context(L, 1))

# Generated at 2022-06-13 18:05:23.689205
# Unit test for method shift of class Parser
def test_Parser_shift():
    g = Grammar()
    p = Parser(g)
    # Use an instance of class Leaf
    p.convert = lambda gr, node: Leaf(type=node[0], value=node[1], context=node[2])
    p.setup()
    p.shift(1, "foo", 0, (1, 2))
    p.shift(2, "bar", 0, (1, 2))
    p.push(token.NAME, ([[(0, 0)], [(0, 0)]], {}), 0, (1, 2))
    p.shift(token.NUMBER, "42", 0, (1, 2))
    p.pop()
    assert p.stack == [(([[(0, 0), (0, 0)], [(0, 0)]], {}), 0, (1, None, None, []))]

# Generated at 2022-06-13 18:05:29.057505
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar, token
    g = grammar.Grammar()
    p = Parser(g)
    p.setup()
    # Check that there is only one element in the list 'stack'; its value must
    # be (0, 0, 0, None)
    assert len(p.stack) == 1
    assert p.stack[0] == (g.dfas[0], 0, (0, None, None, []))
    # Check that 'rootnode' is None
    assert p.rootnode is None
    p.addtoken(token.ENDMARKER, "", None)
    assert p.rootnode[0] == 0  # Check that 'rootnode' is the root of the parse tree


# Generated at 2022-06-13 18:05:33.840120
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    def addtoken(type, value, context):
        p.addtoken(type, value, context)
    from .grammar import Grammar
    from .token import NAME, NUMBER, NL

    g = Grammar("""
        start: NAME
        """)

    p = Parser(g)
    assert repr(p) == "<Parser for %r>" % g

    p.setup()
    addtoken(NAME, "foo", None)
    addtoken(NL, None, None)
    from .driver import Driver
    d = Driver(p)
    addtoken(NUMBER, "3", None)

    # Test a syntax error
    p.setup()
    try:
        addtoken(NUMBER, "3", None)
    except ParseError:
        pass
    else:
        assert 0, "expected ParseError"

# Generated at 2022-06-13 18:05:45.278875
# Unit test for method shift of class Parser
def test_Parser_shift():
    class DummyGrammar:

        def __init__(self, labels, charset):
            self.labels = labels
            self.charset = charset

    g = DummyGrammar(labels={1: (1, 'a'), 2: (token.NAME, 'b')},
                     charset={'a': 1, 'b': 2, 'c': 3})
    p = Parser(g)
    p.setup()
    # token.NAME == NAME < 2
    assert p.classify(token.NAME, 'b', None) == 2
    # 'a' == ID < 1
    assert p.classify(token.NAME, 'a', None) == 1
    # token.NAME == NAME < 2
    p.addtoken(token.NAME, 'b', None)
    # token.NAME == NAME

# Generated at 2022-06-13 18:06:02.973689
# Unit test for method pop of class Parser
def test_Parser_pop():
    import sys
    import os
    import pkg_resources
    import io
    import blib2to3.pgen2.parse
    import blib2to3.pgen2.driver
    import blib2to3.pgen2.pgen

    # Make parser instance
    grammar = blib2to3.pgen2.parse.make_grammar_instance(
        blib2to3.pgen2.driver.parse_grammar(io.StringIO(grammar_str), grammar_name)
    )
    convert = None
    parser = blib2to3.pgen2.pgen.Parser(grammar, convert)

    # Test method pop
    parser.setup(start=None)
    parser.shift(1, None, 1, Context(None, 2))

# Generated at 2022-06-13 18:06:11.122202
# Unit test for method push of class Parser
def test_Parser_push():
    # Type hints
    class Grammar:
        def __init__(self):
            self.dfas: Dict[int, DFAS] = {}
            self.dfas[0] = ([[(0, 0), (1, 1)]], {0: 0})
            self.dfas[4] = ([[(2, 0), (0, 0)], [(0, 1)]], {0: 0, 1: 1})

        def __getitem__(self, key):
            if key == 0:
                return 4
            elif key == 4:
                return [(0, self.dfas[0]), (1, self.dfas[0])]

    class Parser:
        def __init__(self, grammar):
            self.grammar = grammar
            self.stack = []
            self.test_stack = []


# Generated at 2022-06-13 18:06:20.809071
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver
    from .tokenize import untokenize
    from .syms import terminfo, tokens

    p = Parser(driver.RstGrammar, driver.RstConverter)
    p.setup()

# Generated at 2022-06-13 18:06:25.399183
# Unit test for method setup of class Parser
def test_Parser_setup():
    import pgen2
    p = pgen2.Parser(pgen2.Grammar(b"<a> ::= '1' '2' | '3'", b""))
    # test coverage:
    p.setup()


# Generated at 2022-06-13 18:06:33.842138
# Unit test for method push of class Parser
def test_Parser_push():
    from . import pgen
    parser = pgen.Driver()
    parser.load_grammar()
    g = parser.pgen.build_grammar()
    from . import ygen
    ygen.build_grammar(g, g.start())

    print(g.keywords)
    print(g.dfas)
    #print(g.labels)
    #print(g.symbols)


if __name__ == "__main__":
    test_Parser_push()

# Generated at 2022-06-13 18:06:40.922466
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver
    from . import grammar
    import io

    # Parse a Python source file and dump the abstract syntax tree
    stream = io.StringIO()
    driver.parse_file(grammar, "test.py", stream=stream)
    print(stream.getvalue())


if __name__ == "__main__":
    test_Parser_addtoken()

# Generated at 2022-06-13 18:06:47.562592
# Unit test for method classify of class Parser
def test_Parser_classify():
    # Make sure that the right number of tokens are added
    grammar = Grammar()
    convert = lam_sub
    parser = Parser(grammar, convert)
    parser.setup()
    num_added = 0
    for token in grammar.token_map:
        if token == token.COMMENT:
            continue
        parser.addtoken(token, 'test', Context())
        num_added += 1
    assert num_added == len(grammar.token_map) - 1

# Generated at 2022-06-13 18:06:55.175138
# Unit test for method setup of class Parser
def test_Parser_setup():
    import pkgutil
    import blib2to3.pgen2.driver

    grammar = blib2to3.pgen2.driver.load_grammar(pkgutil.get_data(__package__, "Python.g4"))
    parser = Parser(grammar)
    parser.setup()
    assert parser.stack
    assert parser.rootnode is None
    assert parser.used_names == set()


# Generated at 2022-06-13 18:07:00.549638
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .grammar import get_grammar, Grammar

    grammar = Grammar(get_grammar())
    parser = Parser(grammar)
    parser.setup()
    parser.shift(token.NUMBER, "1", 0, None)
    assert parser.stack[-1] == (grammar.dfas[1], 0, (1, None, None, [Leaf(token.NUMBER, "1")]))

# Generated at 2022-06-13 18:07:09.789461
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .token import LPAR, NUMBER, RPAR, NAME
    from . import grammar
    s = "(17)"
    p = Parser(grammar)
    p.setup()
    assert not p.addtoken(LPAR, "(", (1, 0))
    assert not p.addtoken(NUMBER, "17", (1, 1))
    assert not p.addtoken(RPAR, ")", (1, 3))
    assert p.addtoken(NAME, "blah", (1, 4))
    assert p.rootnode is not None and p.rootnode.children == [
        Leaf(NUMBER, "17", (1, 1))
    ]
    p.setup()

# Generated at 2022-06-13 18:07:33.055587
# Unit test for method shift of class Parser
def test_Parser_shift():
    p = Parser(Grammar())
    p.setup()
    p.shift(0, 1, 0, 2)

# Generated at 2022-06-13 18:07:41.593525
# Unit test for method shift of class Parser
def test_Parser_shift():
    import blib2to3.pgen2.convert
    import blib2to3.pgen2.driver
    import os
    import blib2to3.pygram.python_symbols as python_symbols
    import blib2to3.pygram
    import tokenize

    dfa = blib2to3.pgen2.driver.load_grammar(blib2to3.pygram.python_grammar_no_print_statement)
    assert not dfa.terminals.get(token.PRINT)
    parse = Parser(dfa, lambda grammar, node: blib2to3.pgen2.convert.convert_node(
        grammar, node, False, False, True))
    f = open(blib2to3.pgen2.convert.__file__)


# Generated at 2022-06-13 18:07:55.251793
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .tokenize import generate_tokens  # Consumes input.
    from .driver import parse_file

    import sys
    import datetime

    def settest(testname):
        def setvalue(value):
            nonlocal testname
            testname = value
        return setvalue

    def testvalue(testname):
        def getvalue():
            nonlocal testname
            return testname
        return getvalue

    testname = "none"
    gettestname = testvalue(testname)
    settestname = settest(testname)
    testname = "none"

    def set_testname(name: Text) -> None:
        """Set current test name.
        Required to create local variables in test procedure
        """
        nonlocal testname
        testname = name


# Generated at 2022-06-13 18:08:04.008208
# Unit test for method pop of class Parser
def test_Parser_pop():
    # test1
    import sys
    import os
    import unittest
    sys.path.insert(0,"./test")
    from test_pgen_master import test_pgen_master
    import blib2to3.pgen2.parse as parse
    import blib2to3.pgen2.token as token
    import blib2to3.pgen2.driver as driver
    import blib2to3.pygram as pygram

    class TestPop(unittest.TestCase):

        def test_pop(self):
            self.grammar = driver.load_grammar("python2-grammar")
            self.p = parse.Parser(self.grammar)
            self.p.setup()

            # test_addtoken_1
            # Call the method for testing
            self.p.addtoken

# Generated at 2022-06-13 18:08:13.565272
# Unit test for method push of class Parser
def test_Parser_push():
    from blib2to3.pgen2 import driver, token

    def convert(grammar, tree):
        print("convert", tree)
        if not tree:
            return None
        return str(tree)

    p = driver.load_grammar("Grammar.txt")
    parser = Parser(p, convert)

    def tokenize(s):
        for c in s:
            yield token.NAME, c, None

    parser.setup()
    for t in tokenize("aab"):
        parser.addtoken(t[0], t[1], None)
    assert parser.rootnode == "aa(b)"

# Generated at 2022-06-13 18:08:24.353101
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    grammar1 = grammar.parse_grammar('''
        start: "a"
        ''')
    grammar2 = grammar.parse_grammar('''
        start: NAME
        ''')
    grammar3 = grammar.parse_grammar('''
        start: NAME NAME
        ''')
    grammar4 = grammar.parse_grammar('''
        start: NAME NAME NAME
        ''')

    class FakeContext(object):
        def __init__(self, lineno: int, offset: int) -> None:
            self.lineno = lineno
            self.offset = offset

    context = FakeContext(1, 0)

    def fail(msg: Text) -> None:
        raise Exception(msg)


# Generated at 2022-06-13 18:08:29.482010
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import tokenize
    from . import driver
    from . import grammar
    from . import lrparser
    from . import lrparser2
    from . import parser
    from . import parsetok
    from .pgen2.tokenize import String
    p = parser.Parser(grammar.G, lrparser2.lr_convert)
    p.setup()
    f = String("a = 1")
    g = tokenize.generate_tokens(f.readline)
    for token in g:
        if p.addtoken(*token):
            break
    assert p.rootnode.children[1].children[2].value == "1"

# Generated at 2022-06-13 18:08:43.197598
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .parser import driver

    def parse(s):
        try:
            parser = driver.Driver(s, parser_driver.grammar)
            parser.setup()
            tok = parser.token()
            while 1:
                if parser.addtoken(tok.type, tok.string, tok.context):
                    break
                tok = parser.token()
            return parser.rootnode
        except ParseError as e:
            print((e.msg, e.type, e.value, e.context))
            raise

    # Simple test: Python variable
    assert parse("a123")[0].type == syms.power

    # Test error recovery
    try:
        parse("a123[")
    except ParseError:
        pass
    else:
        raise AssertionError("expected syntax error")

# Generated at 2022-06-13 18:08:47.647230
# Unit test for method shift of class Parser
def test_Parser_shift():
    """Tests method shift of Parser."""
    token.sym_to_tok.update({"PLUS": 1})
    parse_grammar = Grammar([], {"PLUS": 1}, {}, {}, {}, {}, "PLUS")
    p = Parser(parse_grammar)
    p.setup()
    p.shift(1, "+", 1, Context(1, 2))
    assert p.stack[0][0][0] == [(1, 1)]

# Generated at 2022-06-13 18:09:04.292468
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .pgen2.parse import pgen

    grammar = pgen("Grammar/Grammar", "Grammar")

    def get_tokens(text: Text) -> Sequence[Tuple[int, Text, Text]]:
        from blib2to3.pgen2.tokenize import generate_tokens

        fake_file = "<test_Parser_addtoken>"
        result = []
        for toktype, tokval, tokstart, _, _ in generate_tokens(iter((text,)).__next__):
            tokval = tokval.rstrip().rstrip("\r")
            result.append((toktype, tokval, tokstart))
        return result

    def lam_sub(grammar: Grammar, node: RawNode) -> Optional[Node]:
        assert node

# Generated at 2022-06-13 18:09:50.496240
# Unit test for method push of class Parser
def test_Parser_push():
    parser = Parser(None)
    parser.stack.append(None)
    parser.push(1, 2, 3, 4)
    assert parser.stack == [(2, 0, (1, None, 4, []))]


# Generated at 2022-06-13 18:10:00.033488
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar, tokenize
    from blib2to3.pgen2.parse import ParseError

    tokenize('a = 1\n')

    p = Parser(grammar.grammar)
    assert p.classify(*token.NAME) == grammar.syms.NAME
    assert p.classify(*token.EQUAL) == grammar.syms.EQUAL
    assert p.classify(*token.NUMBER) == grammar.syms.NUMBER
    assert p.classify(*token.INDENT) == grammar.syms.INDENT
    try:
        p.classify(*token.ENDMARKER)
    except ParseError as e:
        assert e.msg == 'bad token'
        assert e.type == token.ENDMARKER
        assert e.value == ''

# Generated at 2022-06-13 18:10:11.505775
# Unit test for method shift of class Parser

# Generated at 2022-06-13 18:10:25.474429
# Unit test for method shift of class Parser
def test_Parser_shift():
    grammar = Grammar("test_Parser_shift")
    parser = Parser(grammar)
    parser.setup()
    parser.shift(1, "a", 0, None)
    parser.shift(2, "b", 1, None)
    parser.shift(3, "c", 2, None)
    rootnode = parser.rootnode
    assert rootnode is not None
    assert rootnode[0] == 1
    assert rootnode[1] == "a"
    assert len(rootnode[2]) == 3
    assert rootnode[2][0] == 1
    assert rootnode[2][1] == "b"
    assert rootnode[2][2] == 2
    assert rootnode[3] is None


# Generated at 2022-06-13 18:10:33.066833
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .grammar import expr_grammar
    from .pgen import driver

    g = expr_grammar
    p = Parser(g)
    p.setup()
    for t, v in driver.tokenize("a + b * 3"):
        if p.addtoken(t, v, None):
            break
    print(p.rootnode)
    p.setup()
    for t, v in driver.tokenize("a + b * 3 + d"):
        if p.addtoken(t, v, None):
            break
    print(p.rootnode)

# Generated at 2022-06-13 18:10:48.876624
# Unit test for method shift of class Parser
def test_Parser_shift():
    import unittest
    import blib2to3.pgen2.convert
    class TestParser(unittest.TestCase):
        def test_shift(self):
            p = Parser(blib2to3.pgen2.convert.grammar)
            p.setup()
            self.assertEqual(p.addtoken(2, "test", 1), True)
            self.assertEqual(p.stack, [])
            self.assertEqual(p.rootnode.type, "file_input")
            self.assertEqual(p.rootnode.children[0].type, "stmt")
            self.assertEqual(p.rootnode.children[0].children[0].type, "NAME")

# Generated at 2022-06-13 18:10:57.371038
# Unit test for method shift of class Parser
def test_Parser_shift():
    import warnings
    import unittest
    import sys
    import io

    class MockToken(object):
        def __init__(self, type, value, context):
            self.type = type
            self.value = value
            self.context = context

    class ParserTest(unittest.TestCase):
        def setUp(self):
            self.stdout = sys.stdout
            sys.stdout = io.StringIO()
            warnings.simplefilter("ignore", category=DeprecationWarning)

        def tearDown(self):
            sys.stdout = self.stdout

        def test_shift(self):
            import blib2to3.pgen2.parse as parse
            import blib2to3.pgen2.driver as driver

            foo = MockToken(1, "foo", 1)
            bar

# Generated at 2022-06-13 18:10:58.533285
# Unit test for method shift of class Parser
def test_Parser_shift():
    raise NotImplementedError("could not find definition for unit test")

# Generated at 2022-06-13 18:11:02.919832
# Unit test for method pop of class Parser
def test_Parser_pop():
    assert Parser.pop(Parser([1, 2, 3], None)) is None

if __name__ == "__main__":
    test_Parser_pop()
    print("The module blib2to3.pgen2.parse is working correctly "
          "if you got this far.")

# Generated at 2022-06-13 18:11:10.189805
# Unit test for method push of class Parser
def test_Parser_push():
    import blib2to3.pgen2.tokenize as tokenize
    import blib2to3.pgen2.driver as driver
    import blib2to3.pgen2.parse as parse
    import sys
    #import cProfile
    #import pstats
    #src = file(sys.argv[1]).read()
    #cProfile.run("tokens = tokenize.generate_tokens(StringIO(src).readline)", "profile.log")
    #p = pstats.Stats("profile.log")
    #p.strip_dirs()
    #p.sort_stats("time")
    #p.print_stats()
    #return
    gram = driver.load_grammar("blib2to3/Grammar.txt")