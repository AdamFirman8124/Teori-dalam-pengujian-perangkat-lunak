

# Generated at 2022-06-13 18:01:49.398231
# Unit test for method shift of class Parser
def test_Parser_shift():
    class SimpleGrammar(Grammar):
        def __init__(self):
            self.start = 256
            self.dfas = {
                256: (
                    [
                        [(257, 1), (0, 2)],
                        [(258, 1), (0, 2)],
                        [(0, 3)],
                        [],
                    ],
                    {1: 0, 2: 3, 3: 3},
                ),
                257: (
                    [
                        [(259, 1), (0, 0)],
                        [],
                    ],
                    {0: 0, 1: 1},
                ),
                258: (
                    [
                        [(260, 1), (0, 0)],
                        [],
                    ],
                    {0: 0, 1: 1},
                ),
            }
            self.keywords = {}  #

# Generated at 2022-06-13 18:01:58.640156
# Unit test for method shift of class Parser
def test_Parser_shift():
    import grammar as _grammar
    import sys as _sys
    try:
        _sys.argv[1]
    except IndexError:
        _sys.stderr.write('One argument required: module name\n')
        _sys.exit(2)
    module_name = _sys.argv[1]
    try:
        module = __import__(module_name)
    except ImportError as e:
        _sys.stderr.write('Failed to load module: %s\n%s\n' % (module_name, e))
        _sys.exit(2)
    globals: Dict[str, Any] = module.__dict__
    pdict = {}
    _sys.modules['pdict'] = pdict
    pdict['__builtins__'] = __builtins__
    p

# Generated at 2022-06-13 18:02:07.704885
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver, pgen
    from . import pygram
    from . import token as token_module
    from blib2to3.pgen2.grammar import Grammar
    import sys
    import os.path

    # Use cmdline as source for test
    # Build a tree from the commandline arguments
    cmdline = sys.argv[1:] or [""]
    tokname, tokens = driver.tokenize_cmdline(cmdline)
    # Start the parser
    p = Parser(Grammar(pygram.python_grammar))
    p.setup()
    # Feed in tokens
    for (type, value, start, end, line) in tokens:
        p.addtoken(type, value, (start, end))
    # No more tokens
    # Check that we get the same tree

# Generated at 2022-06-13 18:02:19.422389
# Unit test for method setup of class Parser
def test_Parser_setup():
    import unittest
    from blib2to3.pgen2.grammar import Grammar

    s = "a : '+' a | '-' a | '(' a ')' | 'x'\n"
    g = Grammar(s)
    p = Parser(g)
    assert p.stack == []
    assert p.rootnode is None

    class check_method(unittest.TestCase):
        def test_setup_without_args(self):
            p.stack = None
            p.rootnode = None
            p.setup()
            assert p.stack != []
            assert p.rootnode is None

        def test_setup_with_start(self):
            p.stack = None
            p.rootnode = None
            p.setup(1)
            assert p.stack != []
            assert p

# Generated at 2022-06-13 18:02:28.349598
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    # This is a rewrite of the SRE example from Demo/pgen/demo.py
    from . import grammar
    from . import token
    from . import pgen
    from .pgen2.parse import parse_grammar
    from .pgen2 import driver as pgen2_driver


# Generated at 2022-06-13 18:02:36.798882
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import driver
    from blib2to3.pgen2.token import tok_name
    p = driver.Driver(
        grammar=Blib2to3Grammar, convert=lam_sub
    ).create_parser()
    for kind in range(256):
        if kind in p.grammar.tokens:
            print(tok_name[kind], p.classify(kind, p.grammar.tokens[kind], None))



# Generated at 2022-06-13 18:02:45.615976
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import re
    import unittest
    from . import grammar
    from .tokenize import tokenize
    from . import token

    # These tokens are encoded as by the tokenize module.

# Generated at 2022-06-13 18:02:52.205069
# Unit test for method push of class Parser
def test_Parser_push():
    from .pgen2 import drive

    # Note that this method does not call the constructor of the class
    # so it needs to set all the self variables in order to pass the
    # exception test
    def exit_func(msg):
        self.fail(msg)

    # Abstract syntax tree node
    class ASTNode(object):
        def __init__(self, type, value, children):
            self.type = type
            self.value = value
            self.children = children

        def __str__(self):
            return '(' + self.type + ', ' + self.value + ', ' + str(self.children) + ')'

    def convert(grammar, node):
        assert node[3] is not None
        return ASTNode(type=node[0], value=node[1], children=node[3])

    # Error

# Generated at 2022-06-13 18:02:53.421746
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    pass


# Generated at 2022-06-13 18:03:04.406841
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import pgen
    from .grammar import Grammar

    def showtokens(tokens):
        return "".join(
            f"({t} {v})" if v is not None else f"({t})" for t, v in tokens
        )

    def create_parser(language: Text) -> Parser:
        # Load the grammar
        filename = f"{language}.grammar"
        with open(pgen.__file__.replace("__init__.py", filename), "r") as f:
            grammar = Grammar(f.read())
            return Parser(grammar)

    def run_parser(
        parser: Parser, input_tokens: Sequence[Tuple[int, Optional[Text]]]
    ) -> None:
        from .pytokenize import generate_tokens



# Generated at 2022-06-13 18:03:14.298001
# Unit test for method classify of class Parser
def test_Parser_classify():
    p = Parser(Grammar())
    assert p.classify(token.NAME, "foo", None) == 2
    try:
        p.classify(token.OP, "foo", None)
        assert 0, "classify() should raise ParseError"
    except ParseError:
        pass

# Generated at 2022-06-13 18:03:24.085564
# Unit test for method pop of class Parser
def test_Parser_pop():
    class Symbol:
        def __init__(self, name, symbol_type):
            self.name = name
            self.symbol_type = symbol_type

        def __repr__(self):
            return f"{self.symbol_type} {self.name}"

    class Grammar:
        def __init__(self, dfa) -> None:
            self.dfas = dfa

    class DFA:
        def __init__(self, states) -> None:
            self.states = states

    class DFAState:
        def __init__(self, arcs) -> None:
            self.arcs = arcs

    class DFAArc:
        def __init__(self, type, value, state) -> None:
            self.type = type
            self.value = value
            self.state = state



# Generated at 2022-06-13 18:03:31.681224
# Unit test for method shift of class Parser
def test_Parser_shift():
    """Define the grammar."""
    import io
    import blib2to3.pgen2.pgen

    grammar = blib2to3.pgen2.pgen.Grammar()
    # Setup the grammar instance

# Generated at 2022-06-13 18:03:36.951772
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar, token
    import io

    testargs = io.StringIO("""
        # Check that a comment is skipped
        # and the next rule recognized

        # A comment rule to test
        # a comment over two lines
        ccomment: '/*' (!'*/' <any ascii>)+ '*/'

    """)

    g = grammar.Grammar(grammar.python_grammar, convert=grammar.convert)
    # Build a parser from the grammar
    p = Parser(g)
    # Find the start symbol of the grammar
    p.setup(g.symbol2number["file_input"])
    t = token.TokenInfo(0, "comment")
    context = Context(str_or_bytes="", start="", end="")

# Generated at 2022-06-13 18:03:43.175064
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import pgen2

    grammar = pgen2.load_grammar("Grammar/Grammar")
    p = Parser(grammar)
    p.setup()
    assert p.addtoken(token.IF, "if", (1, 0)) is False
    assert p.addtoken(token.NAME, "x", (1, 3)) is False
    assert p.addtoken(token.COLON, ":", (1, 4)) is False
    assert p.addtoken(token.NEWLINE, "\n", (2, 0)) is False
    assert p.addtoken(token.INDENT, "indent", (3, 0)) is False
    p.addtoken(token.NAME, "y", (3, 0))

# Generated at 2022-06-13 18:03:52.729099
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    p = Parser(driver.grammar, driver.convert)
    p.setup()

    def _addtoken(type, value, context):
        if p.addtoken(type, value, context):
            return p.rootnode
        return None

    # Empty file
    assert p.addtoken(token.ENDMARKER, "", (0, 0))
    # Illegal token
    try:
        p.addtoken(token.NT_OFFSET, "", (0, 0))
    except ParseError:
        pass
    else:
        assert False, "expected ParseError"
    # Normal input
    r = _addtoken(token.NAME, "x", (1, 0))
    assert r is None

# Generated at 2022-06-13 18:03:55.042349
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2.pgen import gram
    parser = Parser(gram)
    parser.setup()
    parser.shift(1, "a", 0, None)

# Generated at 2022-06-13 18:04:05.715063
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver

    grammar = driver.load_grammar("Grammar.txt")
    parser = Parser(grammar)
    parser.setup()
    parser.addtoken(token.NAME, "x", Context(1, 0, "1.py"))
    parser.addtoken(token.EQUAL, "=", Context(1, 0, "1.py"))
    parser.addtoken(token.NUMBER, "1", Context(1, 0, "1.py"))
    parser.addtoken(token.NEWLINE, "\n", Context(1, 0, "1.py"))
    parser.addtoken(token.ENDMARKER, "", Context(1, 0, "1.py"))

# Generated at 2022-06-13 18:04:13.699555
# Unit test for method classify of class Parser
def test_Parser_classify():
    import unittest
    from .tokenize import generate_tokens
    from .driver import get_grammar

    class TestParser(unittest.TestCase):
        def test_classify(self):
            parser = Parser(get_grammar())
            parser.setup()
            for type, value, context in generate_tokens("0x1234"):
                parser.classify(type, value, context)
            for type, value, context in generate_tokens('"\x01\n\r\\"'):
                parser.classify(type, value, context)
            for type, value, context in generate_tokens('"\x01\n\r\\""\x01\n\r\\"'):
                parser.classify(type, value, context)

    unittest.main()

# Generated at 2022-06-13 18:04:22.491316
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    grammar_ = Grammar()
    grammar_.start = 1
    grammar_.labels = [(1, None), (2, None), (3, None)]
    grammar_.keywords: Dict[Text, int] = {}
    grammar_.nonterminals = set()
    grammar_.dfas = [
        [[(1, 0), (2, 1)], [(1, 0), (2, 1)], [(0, 2)]],
        [[(3, 3), (2, 4)], [(3, 4), (2, 5)], [(3, 6), (2, 7)]],
        [],
        [[(0, 3)], [(0, 4)], [(0, 5)], [(0, 6)], [(0, 7)]],
    ]
    p_ = Parser(grammar_)
    p_.setup()
    assert p

# Generated at 2022-06-13 18:04:37.184125
# Unit test for method push of class Parser
def test_Parser_push():
    class TestGrammar(object):
        labels = dict()
        tokens = dict()
        start = 0
        dfas = {0: ([[(1, 0), (2, 0)], [(3, 0), (4, 0)]], {0: 0, 1: 0, 2: 1, 3: 1})}

    class test_Parser(Parser):
        def push(self, type: int, newdfa: DFAS, newstate: int, context: Context) -> None:
            Parser.push(self, type, newdfa, newstate, context)
            self.stack_length = len(self.stack)
            self.stack_last = self.stack[-1]

    test_parser = test_Parser(TestGrammar())
    test_parser.setup()

# Generated at 2022-06-13 18:04:42.803216
# Unit test for method push of class Parser
def test_Parser_push():
    """Test the push method of class Parser"""
    test = Parser(Grammar())
    test.push(0, None, 0, Context(0, 0))
    test.push(1, None, 1, Context(1, 1))
    assert len(test.stack) == 2
    assert test.stack[0] == (None, 0, (0, None, Context(0, 0), []))
    assert test.stack[1] == (None, 1, (1, None, Context(1, 1), []))

# Generated at 2022-06-13 18:04:53.606842
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    g = grammar.grammar

    p = Parser(g)

    ilabel = p.classify(token.NAME, "hello", (None, None))
    assert ilabel == g.labels.index(("hello", None, None))

    p.setup()
    p.addtoken(token.NAME, "print", (None, None))
    p.addtoken(token.LPAR, "(", (None, None))
    p.addtoken(token.NAME, "hello", (None, None))
    p.addtoken(token.RPAR, ")", (None, None))
    p.addtoken(token.NEWLINE, "\n", (None, None))
    assert p.stack == []
    p.addtoken(token.ENDMARKER, None, (None, None))
    assert p

# Generated at 2022-06-13 18:05:03.701601
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:05:13.689165
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    _addtoken = Parser.addtoken.im_func
    class _DummyGrammar(object):
        def __init__(self, dfa: Sequence[Sequence[int]]) -> None:
            self.dfas = {0: (dfa, set())}
            self.labels = [(0, 0)]
    g = _DummyGrammar((((1, 2),),))
    p = Parser(g)
    p.stack.append((g.dfas[0], 0, (None, None, None, [])))
    _addtoken(p, 0, None, None)
    assert p.stack == [((((1, 1),),), 1, (None, None, None, []))]

# Generated at 2022-06-13 18:05:24.746072
# Unit test for method classify of class Parser
def test_Parser_classify():
    class _Rule_Grammar(Grammar):
        def __init__(self) -> None:
            self.start = 256

# Generated at 2022-06-13 18:05:30.742669
# Unit test for method pop of class Parser
def test_Parser_pop():
    import pickle

    class PickableConverter(object):
        def __init__(self):
            self.called = False

        def __call__(self, grammar, node):
            self.called = True
            return node

    def assert_called(called):
        if not called:
            raise RuntimeError("Converter was not called")

    x = Parser(pickle.loads(b"\x80\x03c__main__\nGrammar\nq\x00."))
    x.convert = PickableConverter()
    x.stack.append(((1, [((259, 0), 1)]), 0, ('a', None, None, [])))
    x.pop()
    assert_called(x.convert.called)

# Generated at 2022-06-13 18:05:36.482999
# Unit test for method classify of class Parser
def test_Parser_classify():
    example_grammar = Grammar('/Users/raul-cruz/TCC/tcc/blib2to3/pgen2/Grammar.txt')
    example_convert = lam_sub
    example_parser = Parser(example_grammar, example_convert)
    example_parser.setup()
    example_context = Context()
    example_type = None
    example_value = ''
    # Invoke method
    example_result = example_parser.classify(example_type, example_value, example_context)

# Generated at 2022-06-13 18:05:45.734790
# Unit test for method classify of class Parser
def test_Parser_classify():
    p = Parser(Grammar(Tokenizer('')))
    assert p.classify(token.INDENT, '', Context(0, 0)) == 4
    assert p.classify(token.DEDENT, '', Context(0, 0)) == 5
    assert p.classify(token.NEWLINE, '', Context(0, 0)) == 6
    assert p.classify(token.NAME, 'a', Context(0, 0)) == 1
    assert p.classify(token.NAME, 'def', Context(0, 0)) == 243
    assert p.classify(token.LPAR, 'a', Context(0, 0)) == -1
    # The following raises an exception

# Generated at 2022-06-13 18:05:56.625319
# Unit test for method pop of class Parser

# Generated at 2022-06-13 18:06:09.837416
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import driver
    from . import tokenize

    g = driver.load_grammar("Grammar.txt")
    p = Parser(g)

    def test_classify(input, type, value, expected):
        ctx = Context(1, 0)
        tok = tokenize.TokenInfo(type, value, ctx, None)
        got = p.classify(type, value, ctx)
        if got != expected:
            print(
                "test_Parser_classify: failed: expected %r, got %r" % (expected, got)
            )
            if value is not None:
                input = repr(value)
            else:
                input = "(none)"

# Generated at 2022-06-13 18:06:16.312993
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar

    g = grammar.Grammar(grammar.grammar, grammar.symbol2number)
    p = Parser(g)
    p.setup()
    p.addtoken(1, 'spam', SimpleContext())
    p.addtoken(2, 'eggs', SimpleContext())
    p.addtoken(3, 'ham', SimpleContext())
    assert p.stack == [(g.dfas[0], 0, (1, None, None, [])),
                       (g.dfas[1], 0, (2, None, None, [])),
                       (g.dfas[2], 0, (3, None, None, []))]


# Generated at 2022-06-13 18:06:16.924342
# Unit test for method setup of class Parser
def test_Parser_setup():
    pass

# Generated at 2022-06-13 18:06:28.779730
# Unit test for method push of class Parser
def test_Parser_push():
    import blib2to3.pgen2.grammar

    # (type, value, context, nodes)
    node_1 = (type, value, context, None)
    # (dfa, state, node)
    stackentry_1 = (dfa, state, node_1)
    # (type, value, context, nodes)
    node_2 = (type, value, context, [node_1])
    stackentry_2 = (dfa, state, node_2)

    # dfa and newdfa are both tuples (dfa, dict)
    dfa = newdfa = (DFA, dict())
    newstate = 0
    context = Context() # empty Context object

    # create empty parser object with
    # grammar as a grammar.Grammar object
    # and with empty convert function
    p = Pars

# Generated at 2022-06-13 18:06:38.210723
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    g = grammar.Grammar(open(grammar.DEFAULT_GRAMMAR + '.txt'))
    p = Parser(g)
    # Do a funny thing:  shift a Name token.  The resulting tree
    # is of the form ((NAME, 'value', ...), None, None), where ...
    # is a (lineno, offset) pair.
    p.setup()
    p.addtoken(token.NAME, 'value', (1, 1))
    assert p.stack == [
        (p.grammar.dfas[g.start], 0, (g.start, None, None, [(300, 'value', (1, 1), None)])),
        (p.grammar.dfas[300], 0, (300, 'value', (1, 1), None)),
    ]

# Generated at 2022-06-13 18:06:41.238840
# Unit test for method pop of class Parser
def test_Parser_pop():
    parser=Parser(Grammar())
    parser.stack=[(1,1,1)]
    parser.pop()
    print(parser.stack)

# Generated at 2022-06-13 18:06:49.231229
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    grammar = Grammar()
    grammar.load("Grammar/Grammar")
    grammar.start = "file_input"
    parser = Parser(grammar)
    parser.setup()
    for i in range(1, 6):
        parser.addtoken(token.NL, None, Context(i, 0))
    assert parser.stack == []
    assert parser.rootnode.type == grammar.symbol2number["file_input"]
    assert len(parser.rootnode.children) == 5
    assert parser.rootnode.used_names == set()
    assert parser.rootnode.context == Context(5, 0)



# Generated at 2022-06-13 18:07:00.507588
# Unit test for method shift of class Parser
def test_Parser_shift():
    import blib2to3.pgen2.parser as parser
    import blib2to3.pgen2.grammar as grammar
    import blib2to3.pgen2.token as token
    import blib2to3.pgen2.parse as parse

    try:
        imp = parse.generate_grammar()
        imp.update(parse.builtin_grammar)
    except IOError:
        raise
    g = grammar.Grammar(grammar.START, imp)
    # create an instance of Parser
    p = parser.Parser(g)

    # get DFA for start symbol
    st_DFA = g.dfas[g.start]

    # get labels for tokens
    nl = g.labels[g.tokens["NAME"]]
    ri = g.lab

# Generated at 2022-06-13 18:07:17.101513
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    def parse(input):
        p = Parser(driver.grammar)
        p.setup()
        for t in input.split():
            p.addtoken(driver.grammar.tokens[t], t, None)
        return p

    p = parse("LPAR RPAR")
    assert len(p.stack) == 1
    assert p.rootnode == Node(type=driver.grammar.symbols.get("file_input"),
                              children=[Leaf(type=token.LPAR, value="LPAR"),
                                        Leaf(type=token.RPAR, value="RPAR")])
    assert p.used_names == set()

    p = parse("if NAME NAME COLON suite else COLON suite")
    assert len(p.stack) == 1

# Generated at 2022-06-13 18:07:22.885624
# Unit test for method push of class Parser
def test_Parser_push():
    # method push requires a correct input of a tuple or NoneType
    # which is the type of the keyword None.
    # create a grammar instance
    grammar = Grammar()
    # create a new Parser instance
    p = Parser(grammar)
    test_grammar = grammar
    test_type = 0
    test_newdfa = None
    test_newstate = 0
    test_context = None
    # test if the correct input of the method push raises no exception
    try:
        p.push(test_type, test_newdfa, test_newstate, test_context)
    except:
        assert False, "test_Parser_push: Test case failed, expected result: Test succeeds."
    # create a new Parser instance
    p = Parser(grammar)
    test_grammar = grammar
    test_

# Generated at 2022-06-13 18:07:38.142770
# Unit test for method setup of class Parser
def test_Parser_setup():
    import lib2to3.pgen2.tokenize as tokenize
    import lib2to3.pgen2.driver as driver
    import lib2to3.pgen2.parse as parse

    def _test(input_source):
        """
        Takes a string input_source and parse it using lib2to3.
        Returns the root of the parse tree.
        """
        tokens = list(tokenize.generate_tokens(input_source))
        grammar = driver.load_grammar()
        p = parse.Parser(grammar)
        p.setup()
        for t in tokens:
            p.addtoken(t[0], t[1], t[4])
        return p.rootnode

    # use an empty program
    root = _test("")
    assert root is None

    # use a very simple program

# Generated at 2022-06-13 18:07:39.700926
# Unit test for method shift of class Parser
def test_Parser_shift():
    assert Parser(None).shift(0, None, 0, None) is None


# Generated at 2022-06-13 18:07:53.902420
# Unit test for method push of class Parser
def test_Parser_push():
    from blib2to3.pgen2.driver import Driver

    dr = Driver(grammar="Grammar/Grammar")
    parser = Parser(dr.grammar)
    node1: RawNode = (0, None, None, [])
    node2: RawNode = (0, None, None, [])
    dfas = [(0,0), (1,1), (0,1)]
    states = {0: [], 1: []}
    parser.stack.append(((dfas, states), 0, node1))
    parser.push(0, (dfas, states), 1, None)
    parser.stack.append(((dfas, states), 1, node2))
    assert parser.stack[-1] == ((dfas, states), 1, node2)
    parser.pop()
    assert parser

# Generated at 2022-06-13 18:07:59.466005
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import pgen

    with open('Grammar/Grammar') as grammarfile:
        grammar = pgen.Grammar(grammarfile.read())
    p = Parser(grammar)
    p.setup()
    # Unit test case: parser stack is empty
    assert p.pop() == None
    # Unit test case: parser stack contains one element
    # p.rootnode should equal popnode

# Generated at 2022-06-13 18:08:08.629427
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver
    from . import grammar

    t = driver.find_module("_testcapi")
    if not t:
        raise RuntimeError("test grammar file not found")
    g = grammar.Grammar()
    g.parse(t)
    p = Parser(g)
    p.setup()

    f = open(t)
    tokens = driver.tokenize(f.readline)
    f.close()

    for type, value, start, end, line in tokens:
        print(type, repr(value))
        if p.addtoken(type, value, (start, end, line)):
            break

    print()
    print(p.rootnode)
    print(p.rootnode.used_names)


if __name__ == "__main__":
    test_Parser_addtoken

# Generated at 2022-06-13 18:08:14.982220
# Unit test for method setup of class Parser
def test_Parser_setup():
    # Just a smoke test
    import sys
    import os
    import grammar

    testdir = sys.path[0]
    if not os.path.exists(testdir):
        testdir = os.path.dirname(os.path.abspath(sys.argv[0]))
        if not os.path.exists(testdir):
            print("WARNING: unable to find testdir")
    gendir = os.path.dirname(sys.path[0])
    gendir = os.path.join(gendir, "Lib", "lib2to3", "Grammar.txt")
    g = grammar.grammar(gendir)
    p = Parser(g)
    p.setup()

# Generated at 2022-06-13 18:08:26.084678
# Unit test for method shift of class Parser
def test_Parser_shift():
    class FakeGrammar(object):
        def __init__(self):
            self.dfas: Sequence[DFAS] = []
            self.convert: Convert = lam_sub

    class FakeNode(object):
        def __init__(self, node: Node) -> None:
            self.node = node

    fg = FakeGrammar()
    fg.dfas.append(([(1, 0)], [0]))
    p = Parser(fg)
    p.setup()
    context = None
    p.shift(token.NAME, "name", 1, context)
    dfa, state, node = p.stack[-1]
    assert node[0] == 0
    assert node[1] == None
    assert node[2] == None

# Generated at 2022-06-13 18:08:31.044525
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .driver import Driver
    import sys

    # Parse a snippet of Python code and print the syntax tree
    snippet = "2+2"
    d = Driver()
    p = d.parse_tokens(snippet)
    print(p.rootnode)

# Generated at 2022-06-13 18:08:34.223021
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .pgen2 import driver
    p = driver.Driver()

# Generated at 2022-06-13 18:08:34.945293
# Unit test for method setup of class Parser
def test_Parser_setup():
    pass

# Generated at 2022-06-13 18:09:07.383378
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import pdb
    debug = pdb.set_trace
    from . import driver

    # Use Python's non-recursive grammar
    g = Grammar(driver.python_grammar_no_print_statement)

    # Initialize the parser
    p = Parser(g)
    p.setup()

    # A simple assignment statement
    p.addtoken(token.NAME, "a", (1, 0))
    p.addtoken(token.EQUAL, "=", (1, 0))
    p.addtoken(token.NUMBER, "1", (1, 0))
    p.addtoken(token.NEWLINE, "\n", (1, 0))
    p.addtoken(0, "", (0, 0))

    # Check the program's syntax tree
    assert p.rootnode.type == g.symbol

# Generated at 2022-06-13 18:09:21.383588
# Unit test for method shift of class Parser

# Generated at 2022-06-13 18:09:27.107715
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2.token import PythonTokenTypes
    from typing import Dict

    p = Parser(Grammar(), None)
    labels: Dict[int, int] = PythonTokenTypes
    for token, value in (
        ("NAME", "foo"),
        ("NAME", "if"),
        ("NEWLINE", None),
        ("INDENT", "    "),
    ):
        ilabel = p.classify(token, value, None)
        assert ilabel == labels[token]



# Generated at 2022-06-13 18:09:39.614170
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    grammar = driver.load_grammar("Grammar", convert=False)
    pars = Parser(grammar)
    pars.setup()
    pars.addtoken(token.NUMBER, "1", (1, 1))
    pars.addtoken(token.NAME, "a", (1, 1))
    pars.addtoken(token.OP, "*", (1, 1))
    pars.addtoken(token.NAME, "b", (1, 1))
    pars.addtoken(token.OP, "+", (1, 1))
    pars.addtoken(token.NUMBER, "2", (1, 1))
    assert pars.addtoken(token.NEWLINE, "\n", (1, 1))

# Generated at 2022-06-13 18:09:40.071269
# Unit test for method pop of class Parser
def test_Parser_pop():
    pass

# Generated at 2022-06-13 18:09:41.090503
# Unit test for method classify of class Parser
def test_Parser_classify():
    pass


# Generated at 2022-06-13 18:09:47.593379
# Unit test for method push of class Parser
def test_Parser_push():
    import sys
    import blib2to3.pgen2
    grammar = blib2to3.pgen2.driver.load_grammar("Python.tokens", "Python.grammar")
    parser = Parser(grammar)
    parser.setup()
    parser.push(2, grammar.dfas[2], 1, [5,5])
    assert(parser.stack == [(grammar.dfas[2], 1, (2, None, [5, 5], []))])

# Generated at 2022-06-13 18:09:54.808279
# Unit test for method pop of class Parser
def test_Parser_pop():
    if __name__ != "__main__":
        import py.test
        py.test.skip("can't test when imported")
    from . import driver

    p = Parser(driver.grammar)
    p.setup()
    # Push one node
    p.push(grammar.Number, grammar.dfas[grammar.Number], 0, None)
    assert p.stack == [
        (driver.grammar.dfas[None], 0, ((None, None, None, []), 0, None)),
        (driver.grammar.dfas[grammar.Number], 0, ((grammar.Number, None, None, []), 0, None)),
    ]
    p.pop()
    assert p.stack == [((driver.grammar.dfas[None], 0, None))]
    # Push another node

# Generated at 2022-06-13 18:10:03.165020
# Unit test for method pop of class Parser
def test_Parser_pop():
    """Unit test for method pop of class Parser"""
    from .pgen import driver, tokenize
    from . import parse as parse_mod
    import sys

    grammarname = "Grammar.txt"
    if sys.platform == "win32":
        grammarname = "Grammar.txt"
    else:
        grammarname = "/usr/local/share/python3.1/Grammar.txt"
    with open(grammarname) as grammarfile:
        grammar = driver.parsestring(grammarfile.read(), grammarname)
    parser = Parser(grammar)
    parser.setup()

# Generated at 2022-06-13 18:10:10.267244
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .grammar import Grammar

    g = Grammar()
    g.load_grammar()
    p = Parser(g)
    p.setup()
    p.shift(0, "aa", 1, None)
    assert p.stack == [(g.dfas[1], 1, (1, None, None, None))]
    p.shift(1, "bb", 2, None)
    assert p.stack == [(g.dfas[1], 1, (1, None, None, None))]

# Generated at 2022-06-13 18:11:01.712531
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar

    class FakeConverter:
        def __init__(self):
            self.saw = set()

        def __call__(self, grammar, node):
            self.saw.add((node[0], node[1]))
            return [node[0], node[1]]

    grammar = grammar.grammar
    converter = FakeConverter()
    parser = Parser(grammar, converter.__call__)
    parser.setup()
    parser.addtoken(
        token.NUMBER, "1", (1, 0)  # type: ignore[arg-type] # https://github.com/python/mypy/issues/3002
    )

# Generated at 2022-06-13 18:11:09.853230
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:11:17.579431
# Unit test for method shift of class Parser
def test_Parser_shift():
    c_grammar = Grammar(token.NT_OFFSET, token.NT_OFFSET + token.N_TOKENS,
                        token.T_IGNORE)
    c_grammar.labels = {}
    c_grammar.keywords = {}
    c_grammar.tokens = {}
    # c_grammar attributes below are needed only by method shift
    c_grammar.dfas = {0: ([[(None, None), (None, None)],
                           [(None, None), (None, None)]], {})}
    obj = Parser(c_grammar)
    obj.stack = []
    class Struct:
        pass
    context = Struct()
    context.__dict__['filename'] = 'foo'
    context.__dict__['line'] = 0

# Generated at 2022-06-13 18:11:27.356759
# Unit test for method pop of class Parser
def test_Parser_pop():
    # Check that pop() correctly appends a node to its parent's children
    from . import driver

    def convert(grammar, node):
        assert node[3] is not None
        return (node[0], node[3])

    p = Parser(driver.grammar, convert)
    p.setup()
    p.addtoken(token.PLUS, "+", (1, 0))
    p.addtoken(token.PLUS, "+", (1, 0))
    p.addtoken(token.PLUS, "+", (1, 0))
    p.addtoken(token.PLUS, "+", (1, 0))
    p.addtoken(token.PLUS, "+", (1, 0))
    p.addtoken(token.PLUS, "+", (1, 0))