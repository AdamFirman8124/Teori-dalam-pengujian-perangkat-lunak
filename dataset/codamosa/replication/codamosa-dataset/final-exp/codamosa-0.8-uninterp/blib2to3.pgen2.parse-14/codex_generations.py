

# Generated at 2022-06-13 18:01:43.509549
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """
    >>> import grammar, token
    >>> g = grammar.Grammar("Methods/Grammar")
    >>> p = Parser(g)
    >>> p.setup()
    >>> p.addtoken(token.NUMBER, "1", (1, 0))
    False
    >>> p.addtoken(token.NAME, "foo", (1, 0))
    False
    >>> p.addtoken(token.OP, "(", (1, 0))
    False
    >>> p.addtoken(token.OP, ")", (1, 0))
    False
    >>> p.addtoken(token.SLSH, "//", (1, 0))
    True
    >>> p.rootnode.type
    258

    """
    pass

# Generated at 2022-06-13 18:01:44.659433
# Unit test for method shift of class Parser
def test_Parser_shift():
    grammar = Grammar(grammar_file)
    p = Parser(grammar)
    p.setup()
    p.shift(0, 1, 2, 3)



# Generated at 2022-06-13 18:01:48.094182
# Unit test for method shift of class Parser
def test_Parser_shift():
    def lam_sub(grammar, node):
        print(node)
        assert len(node) == 4
        assert node[3] is None
        return node

    test_grammar = {'keywords': {}, 'tokens': {}, 'dfas': {'test': ([[0,0], [1,1]], [(1, 0)])},
                    'labels': [(0, 258), (2, 257), (1, 258)], 'start': 258}

    parser = Parser(test_grammar, lam_sub)
    parser.setup(258)
    parser.addtoken(258, 'test', Context(1))

# Generated at 2022-06-13 18:01:54.585648
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver
    if driver.main:
        # Called as a script, run unit tests
        import unittest
        import pgen2.parsergenerator
        import pgen2.driver
        grammar = pgen2.driver.load_grammar(
            pgen2.parsergenerator.DEFAULT_GRAMMAR_FILE
        )
        parser = Parser(grammar)
        parser.setup()
        parser.shift(1, u"test", 1, Context(u"", 1, 0, 1, 1))
        assert parser.stack[0][2][-1][-1][0].value == u"test"



# Generated at 2022-06-13 18:01:58.279721
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver

    source = """
    """
    p = driver.Parser()
    p.setup()
    p.addtoken(token.INDENT, "    ", (0, 0))
    p.pop()
    assert p.pop() == None


# Generated at 2022-06-13 18:02:03.810152
# Unit test for method classify of class Parser
def test_Parser_classify():
    foo = Parser(Grammar())
    # This should raise an exception
    try:
        foo.classify(token.NAME, 'hello', (1, 0))
    except ParseError:
        pass
    else:
        raise AssertionError("no exception")

# Generated at 2022-06-13 18:02:12.624284
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:02:24.933318
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver, grammar

    def test(s):
        driver.grammar = grammar
        p = Parser(grammar)
        p.setup()
        for t in driver.tokenize(s):
            p.addtoken(*t)
        return p.rootnode

    def check(s, expected, *, print_tree=False):
        tree = test(s)
        if print_tree:
            print(tree.pretty())
        return tree == expected

    assert check('+', RawNode([Token(PLUS, '+', (1, 0), (1, 0))]))

# Generated at 2022-06-13 18:02:36.614709
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import driver
    import sys
    import io
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    #test_Parser_addtoken() works only for Python version >= 3.3
    if sys.version_info >= (3, 3):
        a = driver.Driver(grammar="Grammar/Grammar",
                          convert=lam_sub,
                          outputdir=".",
                          outputfile="blib2to3/pgen2/driver_py33.py")
        a.run()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

# Generated at 2022-06-13 18:02:38.132904
# Unit test for method pop of class Parser
def test_Parser_pop():
    p = Parser(Grammar())
    p.pop()

# Generated at 2022-06-13 18:02:52.479115
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import token
    from . import driver
    from . import pgen2
    import pprint
    import sys
    # Read a grammar specification and create a grammar object
    if len(sys.argv) < 2:
        sys.stderr.write("usage: %s [grammar-file]\n" % sys.argv[0])
        raise SystemExit(1)
    with open(sys.argv[1], "rb") as stream:
        grammar = pgen2.driver.load_grammar(stream)
    if not grammar:
        raise SystemExit(1)
    driver.fixup_grammar(grammar)
    pprint.pprint(grammar)
    # Create a parser
    parser = Parser(grammar)
    # Prepare for parsing
    parser.setup()
    # Parse a

# Generated at 2022-06-13 18:02:58.476518
# Unit test for method shift of class Parser
def test_Parser_shift():
    p = Parser(None)
    p.shift(1, 2, 3, 4)
    assert p.stack[0] == (None, 3, (None, None, 4, [
        # a dummy node containing the shifted token
        (1, 2, 4, None)
    ]))

# Generated at 2022-06-13 18:03:08.988114
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .grammar import Grammar
    from . import token


# Generated at 2022-06-13 18:03:19.670146
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2 import driver
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pytree import Leaf

    grammar = Grammar(driver.tokenize_grammar("Grammar/Grammar", "Grammar"))

    # test with single token
    p = Parser(grammar)
    p.setup()
    p.addtoken(1, 'grammar', (0, 0))
    p.addtoken(1, 'grammar', (0, 0))
    assert p.rootnode == Leaf(1, 'grammar', (0, 0))

    # test with a parent node
    p = Parser(grammar)
    p.setup()
    p.addtoken(1, 'grammar', (0, 0))
    p.add

# Generated at 2022-06-13 18:03:27.069418
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, driver
    from .parse import Parser

    # load grammar
    f = open(grammar.__name__ + ".txt", "r")
    if "Python" in grammar.__name__:
        start = "file_input"
    else:
        start = None
    g = grammar.Grammar(f.read(), start)
    f.close()

    # build parser
    p = Parser(g)
    p.setup(start)

    # parse string
    d = driver.Driver(p.grammar, p.convert)
    d.set_debuglevel(0)
    d.input("a = 1")
    d.parse()

# Generated at 2022-06-13 18:03:30.572733
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar
    g = grammar.Grammar(grammar.grammar)
    p = Parser(g)
    p.setup()

# Generated at 2022-06-13 18:03:39.097669
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    global test_Parser_addtoken
    test_Parser_addtoken = True
    from . import driver, token
    from blib2to3.pgen2.parse import ParseError
    from .pygram import python_grammar

    parser = Parser(python_grammar)
    driver.generate_tokens(test_Parser_addtoken, token.tok_name)
    results = parser.addtoken(token.ENDMARKER, "", Context(0, 0))
    if not results:
        raise ParseError("", 0, "", Context(0, 0))

# Generated at 2022-06-13 18:03:55.889357
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    r"""Test method addtoken of class Parser."""
    #
    # Construct an instance of class Parser
    #
    from blib2to3.pgen2.grammar import Grammar
    from .token import INDENT, DEDENT, NAME
    from .tokenize import detect_encoding, TokenInfo, generate_tokens

    grammar = Grammar()
    grammar.start = 257  # start symbol
    grammar.tokens = {NAME: 257, INDENT: 258, DEDENT: 259}  # token values
    grammar.labels = [None] * 260
    for token_value, symbol_number in grammar.tokens.items():
        grammar.labels[symbol_number] = (token_value, None)
    #
    # A grammar with a single rule with the following structure:
    #


# Generated at 2022-06-13 18:04:06.429641
# Unit test for method classify of class Parser
def test_Parser_classify():
    import unittest
    import blib2to3.pgen2.token as token
    import blib2to3.pgen2.grammar as grammar
    import blib2to3.pytree as pytree
    from blib2to3.pgen2.parse import ParseError

    class TestParser(Parser):
        def __init__(self, grammar, convert=None):
            Parser.__init__(self, grammar, convert)
            self.labels = {}

        def classify(self, type, value, context):
            if type == token.NAME:
                if value in self.labels:
                    label = self.labels[value]
                else:
                    label = self.grammar.tokens.get(type)
                    self.labels[value] = label

# Generated at 2022-06-13 18:04:14.019183
# Unit test for method classify of class Parser

# Generated at 2022-06-13 18:04:29.396620
# Unit test for method pop of class Parser

# Generated at 2022-06-13 18:04:39.345442
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pygram import python_grammar
    from . import driver

    def test(src: Text, expected: Results, convert: Optional[Convert] = None) -> None:
        parser = Parser(python_grammar, convert)
        parser.setup()
        tok = driver.tokenize_str(src)
        # see that the parser can categorize each token
        for type, value, context in tok:
            ilabel = parser.classify(type, value, context)
            assert ilabel
        tok.seek(0)
        # go through all the tokens and add them to the parser

# Generated at 2022-06-13 18:04:44.677058
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar, tokenize

    p = Parser(grammar)
    p.setup()
    t = tokenize.generate_tokens(BytestringIO(b'1+2').readline)
    t1 = next(t)
    assert t1.type == token.NUMBER
    assert t1.string == '1'
    assert t1.start == (1, 0)
    assert t1.end == (1, 1)
    assert t1.line == '1+2'



# Generated at 2022-06-13 18:04:54.441386
# Unit test for method pop of class Parser
def test_Parser_pop():
    def convert(grammar: Grammar, node: RawNode) -> Union[Node, Leaf]:
        return node

    p = Parser(grammar.Grammar, convert)
    rawnode: RawNode = (5, "", "", [])
    p.stack.append(((0, 0), 0, rawnode))
    p.pop()
    rawnode = (5, "", None, [])
    p.stack.append(((0, 0), 0, rawnode))
    p.pop()
    rawnode = (5, "", 0, [])
    p.stack.append(((0, 0), 0, rawnode))
    p.pop()


# Generated at 2022-06-13 18:05:04.329692
# Unit test for method pop of class Parser
def test_Parser_pop():
    class PartialGrammar:
        """A partial class for the parser, to test Parser.pop."""

        def setup(self, start: Optional[int] = None) -> None:
            """Prepare for parsing.

            This *must* be called before starting to parse.

            The optional argument is an alternative start symbol; it
            defaults to the grammar's start symbol.

            You can use a Parser instance to parse any number of
            programs; each time you call setup() the parser is reset to
            an initial state determined by the (implicit or explicit)
            start symbol.

            """
            if start is None:
                start = self.grammar.start
            # Each stack entry is a tuple: (dfa, state, node).
            # A node is a tuple: (type, value, context, children),
            # where children is a list

# Generated at 2022-06-13 18:05:07.745926
# Unit test for method classify of class Parser
def test_Parser_classify():
    import unittest
    from .grammar import Grammar

    class TestParser(unittest.TestCase):
        def test_classify(self):
            grammar = Grammar()
            # The following raises an exception, as it should
            parser = Parser(grammar)
            self.assertRaises(ParseError, parser.classify, token.NAME, "", None)

    unittest.main()

# Generated at 2022-06-13 18:05:14.810867
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar
    g = grammar.Grammar(grammar.parse_grammar('Grammar/Grammar'))
    p = Parser(g)
    assert p.classify(token.NAME, "class", None) == g.tok_NAME
    assert p.classify(token.NAME, "def", None) == g.tok_NAME
    assert p.classify(token.NAME, "class", None) == g.tok_NAME
    assert p.classify(token.NAME, "def", None) == g.tok_NAME

# Generated at 2022-06-13 18:05:25.112652
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2.parse import Parser
    from blib2to3.pgen2.tokenize import generate_tokens
    from blib2to3.pgen2.driver import Driver
    from blib2to3.pgen2.grammar import Grammar

    driver = Driver()
    filename = "./blib2to3/grammar.txt"
    driver.load_grammar(filename)
    parser = Parser(driver.grammar)
    parser.setup()
    with open(filename, 'r', encoding='utf-8') as f:
        for tup in generate_tokens(f.readline):
            if parser.addtoken(*tup):
                break
    assert isinstance(driver.grammar, Grammar)
    assert parser.stack
    assert parser.root

# Generated at 2022-06-13 18:05:35.598453
# Unit test for method push of class Parser
def test_Parser_push():
    if not locals().get('__file__', ''):
        from types import ModuleType
        for name, obj in list(globals().items()):
            if isinstance(obj, ModuleType):
                obj.__file__ = name + '.py'

    import sys
    import unittest
    import warnings

    from . import pygram, pytoken

    # The exceptions to test for
    class TestError(Exception):
        pass

    class TestSyntaxError(TestError):
        pass

    class TestIndentationError(TestSyntaxError):
        pass

    class TestTabError(TestIndentationError):
        pass

    # The tokenizer
    class Tokenizer:
        def __init__(self, grammar):
            self.grammar = grammar
            self.type = pytoken.ENDMARKER
            self.value

# Generated at 2022-06-13 18:05:45.410670
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import io
    import collections

    # In the following, arrow_tokens is a list of pairs (token_number, token_value).
    # The format of the other tables is described in the user guide of pgen2.

    # Test for builtins.py

# Generated at 2022-06-13 18:05:58.575635
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar

    # Pick an obscure Python grammar symbol to test with
    p = Parser(grammar, None)
    p.setup("funcdef")

    # Try to cause a crash
    p.push("None", None, 0, None)
    p.pop()

# Generated at 2022-06-13 18:06:07.450575
# Unit test for method shift of class Parser
def test_Parser_shift():
    # pylint: disable=too-many-branches,too-many-statements,too-many-locals
    # long method, many branches
    """Unit test for method shift of class Parser."""
    import sys
    from . import pgen2
    from . import tokenize  # Just for the startprog and endprog constants
    if hasattr(sys, "frozen"):
        # Keeps the debuggers from choking on Library.zip
        _, _, _ = tokenize.startprog, tokenize.endprog, sys.frozen
    # Test the Parser class
    # pylint: disable=too-many-statements,too-many-branches,too-many-locals
    # long method, many branches
    # Build a simple grammar

# Generated at 2022-06-13 18:06:18.737051
# Unit test for method pop of class Parser
def test_Parser_pop():
    test_dfa = [
        [(1, 2)],
        [(3, 2)],
        [(4, 2)],
        [(3, 2)],
        [(4, 2)],
        [(0, 5)],
    ]
    test_dfas = (test_dfa, {})
    test_stack = [
        (test_dfas, 0, (1, None, None, [])),
        (test_dfas, 0, (2, None, None, [])),
        (test_dfas, 0, (3, None, None, [])),
        (test_dfas, 0, (4, None, None, [])),
        (test_dfas, 0, (5, None, None, [])),
    ]
    parser = Parser(Grammar)
    parser.stack

# Generated at 2022-06-13 18:06:29.262890
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # The grammar used is a "simplified" version of Python's grammar,
    # suitable for testing only (it can't parse real Python programs)
    g = Grammar(
        """
        STMT: simple_stmt | compound_stmt
        simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
        small_stmt: expr_stmt
        expr_stmt: NAME '=' NAME
        compound_stmt: if_stmt | while_stmt
        if_stmt: 'if' NAME ':' suite 'else' ':' suite
        while_stmt: 'while' NAME ':' suite
        suite: simple_stmt
        """
    )
    p = Parser(g)
    p.setup()
    p.addtoken(token.NAME, "x", None)

# Generated at 2022-06-13 18:06:38.610302
# Unit test for method pop of class Parser
def test_Parser_pop():
    import blib2to3.pgen2.pgen as pgen
    p = Parser(pgen.get_grammar())
    p.setup()
    token1 = (1, "token1", 2)

    # push something on the stack
    p.push(1, (), 0, token1)
    assert p.stack == [((), 0, (1, None, 2, [])), ((), 0, (1, None, 2, []))]
    p.pop()
    assert not p.stack
    assert p.rootnode is not None
    assert p.rootnode.type == 1
    assert p.rootnode.value is None
    assert p.rootnode.context == p.rootnode.prefix == p.rootnode.prefix_end == token1

# Generated at 2022-06-13 18:06:48.070604
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest
    from blib2to3.pgen2.token import tok_name
    from blib2to3.pgen2 import driver, tokenize

    class TestCase(unittest.TestCase):
        def test_shift(self):
            with driver.load_grammar() as grammar:
                p = Parser(grammar)
                p.setup()
                for _type in range(256):
                    if grammar.tokens.get(_type) is not None:
                        p.addtoken(_type, tok_name[_type], (1, 1))

    unittest.main("__main__", verbosity=2, exit=False)



# Generated at 2022-06-13 18:06:59.868731
# Unit test for method push of class Parser
def test_Parser_push():
    from .grammar import parse_grammar

    g = parse_grammar(
        """
        start: number
        number: DIGIT+
        """
    )

    p = Parser(g)

    # prepare the parser
    p.setup()

    # add a token
    p.addtoken(token.DIGIT, "1", None)

    # test the stack
    assert len(p.stack) == 1
    assert p.stack[0][2][0] == 0
    assert p.stack[0][2][1] == None
    assert p.stack[0][2][2] == None
    assert len(p.stack[0][2][3]) == 1

    # add a token
    p.addtoken(token.DIGIT, "1", None)

    # test the stack
    assert len

# Generated at 2022-06-13 18:07:12.330569
# Unit test for method shift of class Parser
def test_Parser_shift():
    from unittest import mock
    from blib2to3.pgen2.grammar import Grammar
    parse = Parser(mock.MagicMock(spec_set=Grammar))
    parse.stack = [(mock.sentinel.dfas, mock.sentinel.state, mock.sentinel.node)]
    parse.shift(mock.sentinel.type, mock.sentinel.value, mock.sentinel.newstate, mock.sentinel.context)
    assert parse.stack == [(mock.sentinel.dfas, mock.sentinel.newstate, mock.sentinel.node)]

# Generated at 2022-06-13 18:07:12.948820
# Unit test for method shift of class Parser
def test_Parser_shift():
    pass

# Generated at 2022-06-13 18:07:14.064034
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:07:33.698525
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar
    from . import tokenize

    # Create a parser
    pg = Parser(grammar.grammar)
    # Read the grammar file
    with open(grammar.__file__) as f:
        source = f.read()
    # Parse the grammar
    pg.setup()
    tokens = tokenize.generate_tokens(source)
    while 1:
        try:
            t = next(tokens)
        except StopIteration:
            break
        pg.addtoken(t.type, t.string, Context(t.start, t.end, t.line))
    # Done

# Generated at 2022-06-13 18:07:38.059771
# Unit test for method pop of class Parser
def test_Parser_pop():
    """
    def test_Parser_pop(self):
        p = Parser(Grammar())
        stack = [(1, 2, (3, 4, 5, None)), (6, 7, (8, 9, 10, None))]
        p.stack = stack
        p.pop()
        assert p.stack == stack[:-1]
    """

# Generated at 2022-06-13 18:07:43.767426
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar
    from . import token

    with open("Python.tbl", "rb") as f:
        g = grammar.Grammar(f.read())

    p = Parser(g)
    assert p.classify(token.STRING, "foo", None) == 1
    assert p.classify(token.NAME, "x", None) == 3
    assert p.classify(token.NAME, "if", None) == 2
    assert p.classify(token.NEWLINE, "\n", None) == 5
    assert p.classify(token.COMMENT, "# comment\n", None) is None

# Generated at 2022-06-13 18:07:56.232105
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar, tokenize
    from .tokenize import generate_tokens
    from .convert import fix_missing_locations

    with open("test.gram") as f:
        g: Grammar = grammar.grammar(f)

    p = Parser(g)
    p.setup()

    r = []
    for tok in generate_tokens(open("test.py").readline):
        typ, val, _, _, _ = tok
        if typ == tokenize.NAME and val in ["def", "class"]:
            val = "NAME"
        r.append((typ, val))
    r.append((token.ENDMARKER, ""))

    for i in r:
        p.addtoken(i[0], i[1], None)


# Generated at 2022-06-13 18:07:56.826595
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    assert Parser

# Generated at 2022-06-13 18:08:07.100077
# Unit test for method push of class Parser
def test_Parser_push():
    n = Node
    # We do some simple tests of push by pushing a series of tokens
    # into it.  We have to make up an artificial grammar for that
    g = Grammar(
        start=256,
        dfas={
            256: ([[(1, 0), (0, 0), (0, 1)]], {0: 0, 1: 1}),
            257: ([[(2, 1)], [(2, 2)]], {1: 0, 2: 1}),
            258: ([[(0, 1)], [(0, 2)]], {1: 0, 2: 1}),
        },
        labels=[
            None,
            (257, None),
            (258, None),
        ],
    )
    p = Parser(g)
    p.setup()

# Generated at 2022-06-13 18:08:17.024542
# Unit test for method push of class Parser
def test_Parser_push():
    def test_msg(parser, type, value, context, msg):
        try:
            parser.push(type, value, context, msg)
        except ParseError as e:
            print("ParseError:", e.msg)

    g = Grammar("test_grammar_push")

    test_msg(Parser(g), None, None, None, "type = None")
    test_msg(Parser(g), 0, (None, None), None, "type = 0")
    test_msg(Parser(g), 2, (None, None), None, "type = 2")

    g.dfas[0] = ([[(0, 0)]], set([(0, 2)]))
    test_msg(Parser(g), 1, (None, None), None, "t > 256: type = 1")

    g.dfas

# Generated at 2022-06-13 18:08:21.356004
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    g = grammar.Grammar(grammar.grammar)
    p = Parser(g)
    p.addtoken(token.NAME, 'a', Context(0, ""))
    assert p.used_names == {"a"}

    p.addtoken(token.NAME, 'b', Context(0, ""))
    assert p.used_names == {"a", "b"}

    p.setup()
    # reset
    assert p.used_names == set()

    p.addtoken(token.NAME, 'c', Context(0, ""))
    assert p.used_names == {"c"}

# Generated at 2022-06-13 18:08:29.804084
# Unit test for method classify of class Parser
def test_Parser_classify():
    class TestToken:
        def __init__(self, type, value, context):
            self.type = type
            self.value = value
            self.context = context
    class TestGrammar:
        def __init__(self):
            self.tokens = {token.NAME: 16}
            self.keywords = {'def': 16}
    test_grammar = TestGrammar()
    parser = Parser(test_grammar)
    kw_token = TestToken(token.NAME, 'def', None)
    assert parser.classify(kw_token.type, kw_token.value, kw_token.context) == 16
    def_token = TestToken(token.NAME, 'def', None)

# Generated at 2022-06-13 18:08:43.433975
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar
    from . import tokenize
    from . import token

    class TestParser(Parser):
        def __init__(self, grammar: Grammar):
            Parser.__init__(self, grammar)

        def classify(self, type: int, value: Optional[Text], context: Context) -> int:
            return type

        def push(self, type: int, newdfa: DFAS, newstate: int, context: Context) -> None:
            print("push", self.grammar.number2symbol[type])
            Parser.push(self, type, newdfa, newstate, context)

        def shift(
            self, type: int, value: Optional[Text], newstate: int, context: Context
        ) -> None:
            print("shift", token.tok_name[type])
           

# Generated at 2022-06-13 18:09:44.074658
# Unit test for method classify of class Parser

# Generated at 2022-06-13 18:09:52.182542
# Unit test for method shift of class Parser
def test_Parser_shift():
    import test_grammar_marshal as test_marshal

    test_shift_cache = {}
    # fmt: off

# Generated at 2022-06-13 18:10:01.221642
# Unit test for method push of class Parser
def test_Parser_push():
    from . import driver

    g = Grammar(
        """
        expression: expression PLUS term
                  | expression MINUS term
                  | term
        term:       term TIMES factor
                  | term DIVIDE factor
                  | factor
        factor:     NUMBER
        """,
        start='expression',
    )

    p = Parser(g)

    def test(input, output):
        p.setup()
        for t in driver.tokenize(input):
            if p.addtoken(*t):
                break
        else:
            assert False, "not done with parsing"

        assert str(p.rootnode) == output

    test('1 + 2', 'expression\n  term\n    factor\n      NUMBER\n  PLUS\n  term\n    factor\n      NUMBER')

# Generated at 2022-06-13 18:10:07.894792
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    p = Parser(grammar.Grammar(token.tok_name))
    p.classify(token.NAME, "var", 1)
    assert 'var' in p.used_names
    p.classify(token.KW, "var", 1)
    assert 'var' in p.used_names

# Generated at 2022-06-13 18:10:10.466392
# Unit test for method setup of class Parser
def test_Parser_setup():
    pass

# Generated at 2022-06-13 18:10:19.873939
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import token
    from . import grammar
    import codecs
    
    with codecs.open("blib2to3/pgen2/Grammar.txt", encoding="utf-8") as fp:
        grammar = grammar.Grammar(fp)
    parser = Parser(grammar)
    parser.setup()
    parser.addtoken(token.COMMENT, "# comment", Context(1, 0, "", 1))
    parser.addtoken(token.NEWLINE, "\n", Context(2, 0, "", 1))
    parser.addtoken(token.DEDENT, None, Context(2, 0, "", 0))
    parser.addtoken(token.NEWLINE, "\n", Context(3, 0, "", 0))
    

# Generated at 2022-06-13 18:10:28.188537
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import blib2to3.pgen2.driver
    import blib2to3.pgen2.tokenize

    p = Parser(blib2to3.pgen2.driver.load_grammar(), blib2to3.pgen2.grammar.convert)
    p.setup()
    tokens = blib2to3.pgen2.tokenize.generate_tokens(iter('').__next__)
    for (type, v, (srow, scol), (erow, ecol), line) in tokens:
        if p.addtoken(type, v, (srow, scol)):
            break

# Generated at 2022-06-13 18:10:37.771356
# Unit test for method pop of class Parser
def test_Parser_pop():
    # a fake grammar, dfa, and stack
    class FakeGrammar:
        def __init__(self, dfa1, dfa2, dfa3):
            self.dfas = dict(a=dfa1, b=dfa2, c=dfa3)
        def __getitem__(self, type):
            return self.dfas[type]
    dfa1 = ([(1, 0), (2, 0)], set([1, 2]))
    dfa2 = ([(1, 0)], set([1]))
    dfa3 = ([(1, 0)], set([1]))
    grammar = FakeGrammar(dfa1, dfa2, dfa3)
    arc1_1 = (1, 0)
    arc1_2 = (2, 0)
    state1

# Generated at 2022-06-13 18:10:50.258826
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import tokens, parsetok

    # Create a parser instance
    from .python import pygram
    from .python.pygram import python_grammar

    p = Parser(grammar=pygram, convert=parsetok.convert)
    assert p is not None

    # Add tokens
    p.setup(python_grammar.start)
    for t in tokens:
        if p.addtoken(t.type, t.string, t.context):
            break

    # Check the result
    assert len(tokens) == 79
    assert p.rootnode is not None
    assert len(p.rootnode) == 1

# Generated at 2022-06-13 18:10:57.511925
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .grammar import Grammar

    def check(input: Sequence[Any], expected: Sequence[int]) -> None:
        parser = Parser(Grammar())
        parser.setup()
        for x in input:
            assert parser.addtoken(*x)
        assert parser.rootnode is not None
        assert [t.type for t in parser.rootnode.pre_order()] == expected

    check([(token.NAME, "name", (1, 2))], [1, 4, 2])
    check([(token.NUMBER, '"number"', (1, 2)), (token.NEWLINE, '', (2, 3))], [1, 6, 3])