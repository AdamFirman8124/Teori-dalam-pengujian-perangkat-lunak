

# Generated at 2022-06-13 18:01:38.928925
# Unit test for method classify of class Parser
def test_Parser_classify():
    # Test: check for reserved word 'class'
    from . import grammar

    g = grammar.parser()
    p = Parser(g)
    p.setup()

    assert p.classify(token.NAME, "class", None) == g.keywords["class"]
    assert p.classify(token.NAME, "x", None) == g.tokens[token.NAME]

# Generated at 2022-06-13 18:01:48.411000
# Unit test for method shift of class Parser
def test_Parser_shift():
    test1_stack = [(None, 0, (0, None, None, []))]
    test1_type = token.NAME
    test1_value = "test"
    test1_newstate = 1
    test1_context = (1, 0)
    test1_nodes = [("test", "test", (1, 0), None)]

    p = Parser(Grammar("test"))
    p.stack = test1_stack

    p.shift(test1_type, test1_value, test1_newstate, test1_context)
    assert len(p.stack) == 1
    assert p.stack == [(None, 1, (0, None, None, test1_nodes))]

    test2_stack = [(None, 0, (0, None, None, []))]
    test2_type

# Generated at 2022-06-13 18:01:56.030068
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import pgen2

    # create a parser from the file 'example.py' using a Grammar object
    parser = pgen2.driver.load_grammar('example.py')

    # initialize parser with the start symbol
    parser.setup()
    assert not parser.stack

    # parse token NAME with value 'name' and context (1, 0)
    type = token.NAME
    value = 'name'
    context = (1, 0)
    assert parser.classify(type, value, context) == 5
    assert parser.stack
    assert parser.stack[-1][1] == 0
    parser.shift(type, value, 5, context)
    assert len(parser.stack) == 1
    assert parser.stack[-1][1] == 5

    # parse token NEWLINE with value '\n' and context (

# Generated at 2022-06-13 18:02:12.596237
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import pgen2, driver
    from .tokenize import generate_tokens
    from io import StringIO
    import sys

    # Fake out the parser by faking out the grammar
    class Classifier:
        def __init__(self):
            self.tokens = {}
            self.labels = {}
            self.keywords = {}

        def add_token(self, typ):
            self.tokens[typ] = len(self.tokens)
            self.labels[self.tokens[typ]] = (typ, "")

    classifier = Classifier()
    classifier.add_token(token.NUMBER)
    classifier.add_token(token.NAME)
    classifier.add_token(token.STRING)

    # Build a fake parser

# Generated at 2022-06-13 18:02:19.480394
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    G = grammar.Grammar(grammar.symbol2number)  # type: ignore
    P = Parser(G)
    P.setup()
    try:
        P.classify(token.NAME, "for", ())
    except ParseError:
        pass
    else:
        raise ValueError("expected exception")



# Generated at 2022-06-13 18:02:25.436439
# Unit test for method shift of class Parser
def test_Parser_shift():
    stack = [(('A',), 0, ('A', None, None, None))]
    newnode: RawNode = ('B', 'v', None, None)
    stack_after = [(('A',), 0, ('A', None, None, ['B']))]
    p = Parser(None, lam_sub)
    p.stack = stack
    p.shift(1, 'v', 0, None)
    assert p.stack == stack_after

# Generated at 2022-06-13 18:02:28.762213
# Unit test for method setup of class Parser
def test_Parser_setup():
    Parser({})
    Parser({}).setup()
    Parser({}, None).setup()


# Generated at 2022-06-13 18:02:38.752025
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver
    from . import token
    from . import grammar
    from . import symbol
    import io

    if __name__ == '__main__':
        basetable = None

    with open('testdata/basetable.txt') as f:
        basetable = eval(f.read())

    with io.StringIO(basetable) as f:
        g = grammar.Grammar(f)

    def convert(grammar, node):
        return node
    p = Parser(g, convert)
    p.setup(symbol.eval_input)
    d = driver.Driver(g, p.addtoken)

# Generated at 2022-06-13 18:02:48.201294
# Unit test for method pop of class Parser
def test_Parser_pop():
    # pylint: disable=unused-variable,unused-import
    from . import grammar
    from . import driver
    from .token import INDENT
    from .token import DEDENT
    from .token import NUMBER
    from .token import STRING
    from .token import NAME
    from .token import NEWLINE
    from .token import COMMENT
    from .token import OP
    from .grammar import NUMBER as NUMBER_SYMBOL
    grammar = grammar.Grammar()
    parser = Parser(grammar)
    stack = []
    dfa1, state1, node1 = stack[-1]
    newnode: RawNode = 1, None, None, [1]
    stack[-1] = (dfa1, state1, node1)

# Generated at 2022-06-13 18:02:56.168409
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar

    yg = grammar.Grammar(
        start="start",
        dfas={
            "start": [[[(1, 1), (3, 1)], [(0, 1), (2, 2), (3, 3)]], [[(0, 3), (2, 3)]]],
            "slist": [[[(4, 1), (0, 1)], [(4, 2)]], [[(4, 2), (0, 2)], [(4, 1)]]],
        },
        labels=[
            ("start", "start"),
            ("\n", "\n"),
            ("slist", "slist"),
            (";", ";"),
        ],
    )
    parser = Parser(yg)
    parser.setup()
    return parser


# Generated at 2022-06-13 18:03:08.444624
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import gram2 as g

    def lam_sub2(grammar: Grammar, node: RawNode) -> NL:
        if len(node[1]) == 1:
            return Leaf(type=g.NAME, value=node[1][0].value, context=node[2])
        else:
            return Node(type=g.NAME, children=node[1], context=node[2])

    p = Parser(g, lam_sub2)
    p.setup(start=g.identifier)
    p.addtoken(g.NAME, "a", 1)
    p.addtoken(g.PERIOD, ".", 1)
    p.addtoken(g.NAME, "b", 1)
    p.addtoken(g.PERIOD, ".", 1)

# Generated at 2022-06-13 18:03:19.256269
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    def show(type, value, context):
        if value is None:
            return repr(type)
        else:
            return repr(value)

    p = Parser(grammar)
    for type in range(256):
        t = show(type, None, None)
        if t in grammar.keywords:
            label = p.classify(type, None, None)
            assert label == grammar.keywords[t]
        else:
            try:
                label = p.classify(type, None, None)
            except ParseError:
                pass
            else:
                assert grammar.tokens.get(type) == label
    word = '_'
    while word < 'zzzzz':
        t = show(token.NAME, word, None)

# Generated at 2022-06-13 18:03:27.906857
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    dfa1 = [
        [(2, 3)],
        [(1, 2), (0, 3), (0, 3)],
        [(0, 3)],
        [],
    ]
    dfas = {
        grammar.symbol.expr: (dfa1, set([1, 2])),
    }
    g = grammar.Grammar(dfas, {}, {}, 0)
    p = Parser(g)
    p.setup(grammar.symbol.expr)
    p.addtoken(token.NUMBER, "1", (1, 0))
    p.addtoken(token.PLUS, "+", (1, 1))
    p.addtoken(token.NUMBER, "2", (1, 2))

# Generated at 2022-06-13 18:03:38.323899
# Unit test for method pop of class Parser
def test_Parser_pop():
    import unittest

    class TestParserPop(unittest.TestCase):

        def setUp(self):
            self.parser = Parser(Grammar())

        def test_symbol_pops_if_parser_is_not_empty(self):
            node = [None]
            self.parser.stack.append(((
                [
                    [(0, 0)],
                    [(0, 0)],
                ],
                {0: 0}
            ), 0, (42, None, None, node)))

            self.parser.pop()

            self.assertEqual(node[0], [])
            self.assertEqual(self.parser.rootnode, None)

        def test_symbol_becomes_root_if_parser_is_empty(self):
            node = [None]

# Generated at 2022-06-13 18:03:55.058508
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .grammar import Grammar

    g = Grammar()
    g.start = 257
    g.labels = [
        (257, None),
        (258, None),
        (259, None),
        (260, None),
        (261, None),
        (262, None),
        (263, None),
        (264, None),
        (265, None),
        (266, "+"),
        (267, "*"),
        (268, "-"),
        (269, "/"),
        (270, "("),
        (271, ")"),
    ]
    g.keywords = {}
    g.keyword_tokens: Dict[int, int] = {}

# Generated at 2022-06-13 18:04:05.760410
# Unit test for method push of class Parser
def test_Parser_push():
    # Arrange
    grammar = Grammar(dict(start=256, dfas={256: ([[(1, 0), (2, 0)], [(0, 1), (2, 1)], [(0, 2), (2, 2)]], {0: 1, 1: 0, 2: 0})}, symbols=[None, 'class', 'def']))
    parser = Parser(grammar)
    parser.setup()
    # Act
    parser.push(
        type=256,
        newdfa=([[(1, 0), (2, 0)], [(0, 1), (2, 1)], [(0, 2), (2, 2)]], {0: 1, 1: 0, 2: 0}),
        newstate=0,
        context=Context(None, None, None, None),
    )

# Generated at 2022-06-13 18:04:11.045893
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class FakeGrammar:
        pass

    class FakeNode:
        pass

    g = FakeGrammar()
    g.dfas = {1: ([[(4, 5), (4, 6)], [(4, 7)]], {4: 1, 5: 0, 6: 1, 7: 1}),
              2: ([[(4, 5), (4, 6)], [(4, 7)]], {4: 1, 5: 0, 6: 1, 7: 1})}
    g.labels = {1: (1, None), 2: (-1, None), 3: (2, None),
                # 4 is the magic "anything" in the label dictionary
                4: (0, None)}
    p = Parser(g)
    p.setup(1)
    p.addtoken(3, None, None) 

# Generated at 2022-06-13 18:04:18.036838
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class Ctx(object):
        def __init__(self, lineno, lineoffset):
            self.__dict__.update(locals())

        def __repr__(self):
            return "Ctx(%r)" % self.__dict__

    g = Grammar("""
        s: a
        a: NAME
        """)

    c = Parser(g)

    def t(input, output):
        c.setup()
        for type, name, ctx in input:
            done = c.addtoken(type, name, ctx)
            assert not done
        done = c.addtoken(0, "", None)
        assert done
        assert c.rootnode.children == output


# Generated at 2022-06-13 18:04:27.579351
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2.parse import ParseError

    class ParserTest(Parser):
        def shift(self, type, value, newstate, context):
            if value in ("x", "y"):
                raise ParseError("mismatched input", type, value, context)
            super().shift(type, value, newstate, context)

    g = Grammar()
    p = ParserTest(g)
    p.setup()
    p.addtoken(token.NAME, "x", (1, 0))
    p.addtoken(token.NAME, "y", (1, 5))
    p.addtoken(token.NAME, "z", (1, 10))



# Generated at 2022-06-13 18:04:37.667210
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class TestGrammar(object):
        def __init__(self, dfas: Dict[int, DFAS]) -> None:
            self.dfas = dfas

    grammar = TestGrammar({0: ([[(1, 1),]], {})})

    class TestContext(object):
        def __init__(self, filename: Text, node: Optional[RawNode]) -> None:
            self.filename = filename
            self.node = node

    class TestConvert(object):
        def __init__(self, retval: NL) -> None:
            self.retval = retval

        def __call__(self, grammar: Grammar, node: RawNode) -> NL:
            return self.retval


# Generated at 2022-06-13 18:04:50.114385
# Unit test for method push of class Parser
def test_Parser_push():
    testcases = [
        "a = 1",
        "a = 1\n",
        "a = 1\n\n",
        "def f():\n    pass\n",
        "def f():\n    pass\n\n",
        "def f():\n    pass\n#\n",
        "def f():\n\tpass\n\n",
        "def f():\n\tpass\n\n#",
    ]
    for text in testcases:
        Parser.setup(text)



# Generated at 2022-06-13 18:04:59.742614
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    """Test method addtoken of class Parser"""
    import blib2to3.pgen2.token as token
    import blib2to3.pgen2.driver as driver
    import blib2to3.pgen2.grammar as grammar

    d = driver.Driver(blib2to3.pgen2, convert=lam_sub, verbose=True)
    d.grammar = d.load_grammar("Grammar.txt")
    p = Parser(d.grammar, d.convert)
    p.setup()

# Generated at 2022-06-13 18:05:07.364119
# Unit test for method push of class Parser
def test_Parser_push():
    # Create a dummy grammar
    class dummyGrammar:
        start = 0
        tokens = {"NUMBER": 2, "NAME": 3, "PLUS": 4}
        keywords = {"foo": 3}
        labels = [(2, "NUMBER"), (3, "NAME"), (4, "PLUS")]

# Generated at 2022-06-13 18:05:16.345114
# Unit test for method pop of class Parser
def test_Parser_pop():
    import unittest
    class TestParserPop(unittest.TestCase):
        def setUp(self):
            self.x = Parser(Grammar())
            self.x.stack = [(None, None, [None, None]), (None, None, [None, 1])]
        def test_pop_when_stack_is_not_empty(self):
            self.x.pop()
            self.assertEqual(self.x.stack, [(None, None, [None, 1, 1])])
            self.x.pop()
            self.assertEqual(self.x.stack, [])
        def test_pop_when_stack_is_empty(self):
            self.x.pop()
            self.x.stack = []
            self.x.pop()

# Generated at 2022-06-13 18:05:26.006949
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2.parse import parse_grammar

    source = """
    %start_symbol foo
    %python_precedence_grammar

    a = 'a' b c
    b = 'b' c | 'b' 'c'
    c = 'c'
    """
    tree = parse_grammar(source, "python")
    p = Parser(tree)

    p.setup()
    leaf1 = Leaf(token.NAME, "a", (1,1))
    leaf2 = Leaf(token.NAME, "b", (1,2))
    leaf3 = Leaf(token.NAME, "c", (1,3))

    assert not p.addtoken(token.NAME, "a", (1, 1))

# Generated at 2022-06-13 18:05:36.240386
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar, token

    g = grammar.grammar
    p = Parser(g)

    check_classify = p.classify

    assert check_classify(token.NAME, "foo", None) == token.NAME
    assert check_classify(token.NAME, "def", None) == g.sym.funcdef
    assert check_classify(token.NAME, "all", None) == g.sym.or_test
    assert check_classify(token.NAME, "is", None) == g.sym.comp_op
    assert check_classify(token.NAME, "class", None) == g.sym.classdef
    assert check_classify(token.NAME, "async", None) == g.sym.async_funcdef

# Generated at 2022-06-13 18:05:44.245909
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from .pgen2 import driver

    # Example from the documentation
    grammar = driver.load_grammar("Grammar.txt")
    p = Parser(grammar)
    p.setup()
    for s in "def f(): return 42":
        tok = tokenize_c.tokenize_func(s, "??")
        if p.addtoken(*tok):
            break

    # Another example; we should get an error
    p.setup()
    for s in "def f(): return":
        tok = tokenize_c.tokenize_func(s, "??")
        if p.addtoken(*tok):
            break

# Generated at 2022-06-13 18:05:51.473513
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar
    from .pygram import python_grammar_no_print_statement
    from .pytree import Node

    p = Parser(grammar.grammar_from_pgen_grammar(python_grammar_no_print_statement))
    p.setup()
    p.addtoken(token.NAME, "abc", None)
    p.pop()
    assert p.rootnode.children == [Leaf(token.NAME, "abc", None)]

# Generated at 2022-06-13 18:05:53.532814
# Unit test for method setup of class Parser
def test_Parser_setup():
    gram = Grammar()
    p = Parser(gram)
    p.setup()

# Generated at 2022-06-13 18:06:08.493886
# Unit test for method pop of class Parser

# Generated at 2022-06-13 18:06:20.921364
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys, os
    from . import driver, parse

    gramfile = os.path.join(os.path.split(sys.modules['blib2to3.pgen2'].__file__)[0],
                            "Grammar/Grammar")
    gram = driver.load_grammar(gramfile)


# Generated at 2022-06-13 18:06:30.722663
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import textwrap
    import random
    import string
    import sys

    if len(sys.argv) == 1:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit(2)

    from . import driver

    # Parse the grammar
    print('Parsing grammar', file=sys.stderr)
    g = driver.load_grammar('Grammar.txt')

    # Make a parser instance
    p = Parser(g)

    # Read test strings and parse them
    for arg in sys.argv[1:]:
        print('Parsing file', arg, file=sys.stderr)
        f = open(arg, 'r')
        s = f.read()
        f.close()
        tokens = driver.tokenize

# Generated at 2022-06-13 18:06:39.549525
# Unit test for method pop of class Parser
def test_Parser_pop():
    test_objects = []
    test_objects.append("self.stack == []")
    test_objects.append("self.rootnode == newnode")
    test_objects.append("self.rootnode.used_names == self.used_names")
    test_objects.append("return")
    print("  %-20s %-20s %-20s" % ("return type", "expected value", "actual value"))
    print("  %-20s %-20s %-20s" % ("------------", "---------------", "-------------"), end='')
    if test_objects.pop() == "return":
        print("OK")
    else:
        print("FAIL")
    print("  %-20s %-20s %-20s" % ("------------", "---------------", "-------------"), end='')

# Generated at 2022-06-13 18:06:46.133836
# Unit test for method shift of class Parser
def test_Parser_shift():
    class MockGrammar:
        def __init__(self):
            pass

    class MockNode:
        def __init__(self, grammar, node):
            pass

    parser = Parser(MockGrammar())
    parser.convert = MockNode
    parser.shift(1, 'x', 2, None)
    assert parser.stack == [(None, 2, (None, [None]))]

# Generated at 2022-06-13 18:06:58.216161
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2.parse import ParseError
    from blib2to3.pgen2.convert import convert_python_2_3

    # This is a minimal grammar with a single non-terminal "a"
    grammar = Grammar()
    grammar.symbol2number = dict([(u"a", 256), (u"b", 257), (u"c", 258)])
    grammar.number2symbol = dict([(256, u"a"), (257, u"b"), (258, u"c")])
    grammar.keywords = dict()
    grammar.tokens = dict([(token.NUMBER, 259)])
    grammar.start = 256
    grammar.labels = [u"a", u"b", u"c", u"NUMBER"]

# Generated at 2022-06-13 18:07:06.324254
# Unit test for method setup of class Parser
def test_Parser_setup():  # Unused
    from blib2to3.pgen2.grammar import Grammar

    def verify_parser_setup(
        parser: Parser, grammar: Grammar, convert: Optional[Convert] = None
    ) -> None:
        assert parser.grammar == grammar
        assert parser.convert == convert
        assert parser.stack == []
        assert parser.rootnode is None

    # Empty grammar
    g = Grammar()
    p = Parser(g)
    verify_parser_setup(p, g)

    # Nonempty grammar
    def convert(grammar, node):
        assert node[-1] is None
        return node

    g = Grammar(start=256)

# Generated at 2022-06-13 18:07:27.538944
# Unit test for method pop of class Parser
def test_Parser_pop():
    p = Parser(Grammar())
    p.stack = [
        (
            ([[(0, 0)]], {0: 0}),
            0,
            (1, None, 0, [None, 2, [None, None, None, None]]),
        )
    ]
    p.grammar.labels = [
        (token.NAME, "<NAME>"),
        (token.INDENT, "<INDENT>"),
        (token.DEDENT, "<DEDENT>"),
    ]
    p.grammar.start = 1
    p.grammar.dfas = [([[(0, 0)]], {0: 0})]
    p.pop()

# Generated at 2022-06-13 18:07:38.177731
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pygram import python_grammar_no_print_statement
    from blib2to3.pgen2 import driver
    from blib2to3 import pytree

    def classify(tokens: Sequence[Tuple[int, Text]]) -> None:
        parser = Parser(python_grammar_no_print_statement)
        parser.setup()
        for type, value in tokens:
            parser.classify(type, value, pytree.Leaf(type, value))
        print("OK")

    classify([(tokenize.NAME, "a")])
    classify([(tokenize.NAME, "print")])
    classify([(tokenize.NAME, "foo")])
    classify([(tokenize.NAME, "def")])

# Generated at 2022-06-13 18:07:43.209539
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    g = grammar.grammar
    p = Parser(g)
    p.setup()
    assert p.classify(token.NUMBER, 3, None) == 0
    assert p.classify(token.NAME, 'foo', None) == 1

# Generated at 2022-06-13 18:07:56.459540
# Unit test for method push of class Parser
def test_Parser_push():
    import unittest
    import sys

    if sys.version_info[0] >= 3 and sys.version_info[1] >= 4:
        import importlib.util

        class TestParser(unittest.TestCase):
            def setUp(self):
                s = importlib.util.spec_from_file_location(
                    'grammar-stub', './Grammar/grammar-stub.py'
                )
                self.grammar = importlib.util.module_from_spec(s)
                s.loader.exec_module(self.grammar)

            def test_push(self):
                p = Parser(self.grammar)
                p.setup()
                for i, n in enumerate(self.grammar.symbols):
                    x = (n, None, None, [])

# Generated at 2022-06-13 18:08:08.658397
# Unit test for method shift of class Parser
def test_Parser_shift():
    # The simplest grammar
    #program = (any_name : NAME)
    #any_name = name &NAME
    #name = NAME
    import pickle

# Generated at 2022-06-13 18:08:13.997000
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # Make sure that addtoken is actually testing all code paths.
    # This test passes if it compiles.
    p = Parser(None)

    def _assert_no_tokens(p=p):
        assert p.addtoken(0, None, None)

    _assert_no_tokens()
    try:
        p.addtoken(0, None, None)
    except ParseError:
        pass
    for i in range(2):
        p.setup()
        _assert_no_tokens()
        try:
            p.addtoken(0, None, None)
        except ParseError:
            pass

# Generated at 2022-06-13 18:08:20.547885
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar

    def read(filename):
        file = open(filename, "r")
        content = file.read()
        return content

    def write(filename, content):
        file = open(filename, "w")
        file.write(content)
        file.close()

    def check(filename):
        result = os.popen(
            "mypy --ignore-missing-imports --pretty --follow-imports=skip %s"
            % filename
        ).read()
        if not "Success" in result:
            print(result)
            return False
        else:
            return True

    def cleanup(filename):
        try:
            os.remove(filename)
        except:
            pass

    def run():
        filename = "parser_push.py"

# Generated at 2022-06-13 18:08:27.925322
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:08:41.248943
# Unit test for method classify of class Parser
def test_Parser_classify():
    """
    Unit test for method classify of class Parser.

    For method classify, we need to have a grammar, and a Parser object
    instantiated from that grammar.

    """
    import blib2to3.pgen2.grammar as grammar

    # Build a test dictionary that is 'like' a real one.
    # The first element is the token type, the second element is the
    # token value.

    testdict = {token.NAME: ('foo', None),
                token.NUMBER: ('42', None)}

    testgrammar = grammar.Grammar(grammar.parse(StringIO("")))

    # This will raise an exception, because the grammar is empty.
    testparser = Parser(testgrammar)

# Generated at 2022-06-13 18:08:46.366028
# Unit test for method push of class Parser
def test_Parser_push():
    grammar = Grammar()
    grammar.dfas = {
        1: ([[(2, 1)]], {1: 1}),
    }
    S = Parser(grammar)
    S.setup(start=1)
    S.push(1, grammar.dfas[1], 0, None)
    assert S.stack == [
        (grammar.dfas[1], 0, (1, None, None, [])),
        (grammar.dfas[1], 0, (1, None, None, [])),
    ]

# Generated at 2022-06-13 18:08:52.524148
# Unit test for method classify of class Parser
def test_Parser_classify():
    # The test can only succeed if the parser has been initialized and
    # the start symbol is an integer > 256, a nonterminal.
    from . import driver
    from . import token

    def compare(type, value):
        # Return label for token (type, value)
        p = Parser(driver.driver.grammar)
        return p.classify(type, value, None)

    if driver.driver.grammar.start >= 256:
        # Should set label of NAME token to the label of the start symbol
        assert compare(token.NAME, "start") == driver.driver.grammar.start
        # Should set label of NAME token to the label of the token
        assert compare(token.NAME, "pass") == driver.driver.grammar.keywords["pass"]
        # Should set label of NAME token to the label of the token


# Generated at 2022-06-13 18:08:57.780646
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar
    
    def test_Parser_addtoken_aux(self, type, value, context,
                                 expected_exception):
        # Arrange
        p = Parser(grammar.Grammar())
        p.setup()
        # Act
        if expected_exception:
            with self.assertRaises(expected_exception):
                p.addtoken(type, value, context)
        else:
            p.addtoken(type, value, context)
        # Assert
        
    def test_Parser_addtoken_gen(self, type, value, context, expected_exception):
        test_method_name = 'test_Parser_addtoken_%s' % (type)

# Generated at 2022-06-13 18:09:06.669946
# Unit test for method pop of class Parser
def test_Parser_pop():
    import blib2to3.pgen2.pgen as pgen
    import blib2to3.pgen2.driver as driver
    import blib2to3.pygram as pygram

    p = pgen.ParserGenerator("Grammar.txt")
    p.parse()
    gr = driver.load_grammar("Grammar.txt", p.grammar(), pygram.python_grammar)
    if gr:
        parser = Parser(gr)
        parser.setup()
        # Test correctness of code when emptying the stack.
        while parser.stack:
            parser.pop()
        # Test that no exception is raised when the stack is empty.
        parser.pop()
    return True


# Test case

# Generated at 2022-06-13 18:09:20.856370
# Unit test for method push of class Parser
def test_Parser_push():
    # There should be an assert in line 312 of Python/parser.c
    # (in function _PyParser_AddToken in the PyPy tree)
    # saying that the same line number and byte offset should be reached
    # more than once, but that's not the case.
    #
    # Instead, _PyParser_AddToken should track each position reached
    # in used_names and raise an error when it is reached a second time.
    p = Parser(Grammar())
    p.setup()
    p.addtoken(0, "x", (1, 0))
    try:
        p.addtoken(0, "x", (1, 0))
    except ParseError:
        pass
    else:
        raise SystemError("ParseError not raised")
    p = Parser(Grammar())
    p.setup()

# Generated at 2022-06-13 18:09:38.962542
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar
    from .pgen import driver

    g = grammar.grammar

    with open("Python.asdl", "rb") as fin:
        file_encoding = driver.get_file_encoding(fin)
    with open("Python.asdl", "r", encoding=file_encoding) as fin:
        pyc = fin.read()

    d = driver.Driver(g, convert=lam_sub)
    tree = d.parse_tokens(pyc, "<string>")
    assert tree.type == 286
    # These should be the same values
    assert tree.children[0].type == 288
    assert tree.children[1].type == 288
    assert tree.children[1].children[0].type == 288
    assert tree.children[1].children[1].type == 288
    assert tree

# Generated at 2022-06-13 18:09:44.796902
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar

    # Build the grammar
    gr = grammar.Grammar("grammars/Grammar")

    # Build the parser
    p = Parser(gr)
    p.setup()

    # Handle the tokens
    for t in tokenize("def f(): pass"):
        p.addtoken(t.type, t.string, t.context)

    assert isinstance(p.rootnode, Node)
    assert p.rootnode[0] == "file_input"
    p.rootnode.pretty_print()
    funcdef = p.rootnode[1]
    assert isinstance(funcdef, Node)
    assert funcdef[0] == "funcdef"
    fname = funcdef[3]
    assert isinstance(fname, Leaf)
    assert fname[0] == "NAME"


# Generated at 2022-06-13 18:09:50.353686
# Unit test for method shift of class Parser
def test_Parser_shift():
    from blib2to3.pgen2 import tokenize as tokenize_, driver

    gendefs = driver.load_grammar("/home/yogev/workspace/Python-3.6.0/Grammar/Grammar")
    grammar = driver.load_grammar(gendefs)
    parser = Parser(grammar)
    parser.setup()
    parser.addtoken(tokenize_.NAME, "a", Context(0,0))

    return parser


# Generated at 2022-06-13 18:09:59.863148
# Unit test for method addtoken of class Parser

# Generated at 2022-06-13 18:10:00.410126
# Unit test for method shift of class Parser
def test_Parser_shift():
    assert 0 == 1

# Generated at 2022-06-13 18:10:04.539476
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import unittest

    class ParserTestCase(unittest.TestCase):
        def test_Parser_addtoken(self):
            g = Grammar(grammar)
            p = Parser(g)
            p.setup()
            self.assertFalse(p.addtoken(token.NAME, "start", (1, 0)))
            self.assertRaises(Parser.ParseError, p.addtoken, token.NAME, "stop", (1, 0))


# Generated at 2022-06-13 18:10:05.873347
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import pgen2

    p = pgen2.driver.load_grammar("Grammar/Grammar")
    parser = Parser(p)
    parser.setup()

# Generated at 2022-06-13 18:10:13.291821
# Unit test for method pop of class Parser
def test_Parser_pop():
    p = Parser(Grammar())
    p.stack = [(None, None, (1, None, None, [])), (None, None, (2, None, None, []))]
    p.pop()
    assert p.stack == [(None, None, (1, None, None, [2, None, None, []]))]
    p.pop()
    assert p.stack == []
    assert p.rootnode.type == 1
    assert len(p.rootnode.children) == 1
    assert p.rootnode.children[0].type == 2

#
# Testing interface
#


# Generated at 2022-06-13 18:10:22.689363
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar
    from grammar_parser.lexer import Lexer
    import io
    import unittest


# Generated at 2022-06-13 18:10:27.681344
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    g1 = grammar.grammar
    p = Parser(g1)
    ilabel = p.classify(token.NAME, "abc", None)
    assert ilabel == 78  # is 'NAME'
    ilabel = p.classify(token.NAME, "def", None)
    assert ilabel == 78  # is 'NAME'
    return True

# Generated at 2022-06-13 18:10:45.554072
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar
    from . import token as token_module

    g = grammar.grammar
    p = Parser(g)
    p.setup()

    for name in token_module._token.__all__:
        if name.startswith("t_") and name != "t_error":
            tok = getattr(token_module, name.replace("t_", ""))
            ilabel = p.classify(tok, tok.__doc__, None)
            t, v = g.labels[ilabel]
            assert t == tok

# Generated at 2022-06-13 18:10:54.170948
# Unit test for method push of class Parser
def test_Parser_push():
    from . import driver

    g = driver.load_grammar("Grammar.txt")
    p = Parser(g)
    p.setup()
    p.addtoken(1, "print", (1, 0))
    p.addtoken(4, "(", (1, 0))
    assert len(p.stack) == 2
    p.push(2, [[(1, 0)], []], 0, (1, 0))
    assert len(p.stack) == 3
    p.addtoken(1, "x", (1, 0))
    assert len(p.stack) == 3
    p.addtoken(5, ")", (1, 0))
    assert len(p.stack) == 2
    p.addtoken(0, "", (1, 0)) # endmarker


# Generated at 2022-06-13 18:10:58.441161
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import sys
    from blib2to3.pgen2.parse import driver

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input"
    driver(filename)

# Generated at 2022-06-13 18:11:02.801742
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import driver
    o = driver.Driver()
    o.setup("no_ending_newline")
    o.parse_tokens("print('hello, world')")
    o.parse_tokens("print('hello, world')")



# Generated at 2022-06-13 18:11:10.140962
# Unit test for method shift of class Parser
def test_Parser_shift():
    t = token
    g = Grammar()
    g.keywords = {'if': 1, 'while': 1}
    g.tokens = {t.NAME: 1, t.NUMBER: 1, t.ENDMARKER: 1}
    p = Parser(g)
    p.setup()
    testnode = (0, None, None, [])
    p.shift(t.NAME, 'if', 1, None)
    assert p.stack[0][2] == testnode
    testnode = (0, None, None, [(1, 'if', None, None)])
    p.shift(t.NAME, 'while', 1, None)
    assert p.stack[0][2] == testnode

# Generated at 2022-06-13 18:11:17.816748
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import grammar

    def test(text: Text, start: int, *expect: Sequence[Text]) -> None:
        g = grammar.Grammar(text)
        p = Parser(g)
        p.setup(start)
        result = [t for t, v in map(g.labels.__getitem__, [e[0] for e in p.stack])]
        assert result == list(expect)


# Generated at 2022-06-13 18:11:25.726037
# Unit test for method push of class Parser
def test_Parser_push():
    from . import parsetok

    # Prepare grammar (see test_grammar.py for details)
    grammar = parsetok.grammar
    # Wrap tokenize for the parser
    tests = "ab + c * d"
    tokens = list(parsetok.tokenize(tests))
    # Build parser
    p = Parser(grammar)
    p.setup()  # Prepare for parsing
    # Add tokens
    for t in tokens:
        p.addtoken(*t)  # Perform the parsing
    # Success!
    assert p.rootnode is not None