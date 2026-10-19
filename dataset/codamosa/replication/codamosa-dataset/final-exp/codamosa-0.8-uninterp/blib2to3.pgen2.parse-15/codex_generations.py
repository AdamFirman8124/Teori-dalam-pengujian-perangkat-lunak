

# Generated at 2022-06-13 18:01:35.942240
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    def testit(method_name, input, output):
        from .pygram import python_symbols, python_grammar, python_grammar_no_print_statement  # type: ignore
        from .pgen import driver
        from .pgen2 import tokenize
        from io import StringIO
        if method_name == 'print':
            grm = python_grammar_no_print_statement
        else:
            grm = python_grammar
        parser = Parser(grm)
        parser.setup(python_symbols.file_input)
        infile = StringIO(input)
        tokengen = tokenize.generate_tokens(infile.readline)
        d = driver.Driver(parser, tokengen)
        d.setup()

# Generated at 2022-06-13 18:01:37.385978
# Unit test for method setup of class Parser
def test_Parser_setup():
    pass


# Generated at 2022-06-13 18:01:44.445041
# Unit test for method classify of class Parser
def test_Parser_classify():
    import unittest.mock
    from blib2to3 import pygram

    mockgrammar = unittest.mock.MagicMock(spec=pygram.Grammar)
    mockgrammar.tokens = {1: 2, 2: 3}
    parser = Parser(mockgrammar)

    assert parser.classify(1, None, None) == 2
    assert parser.classify(2, None, None) == 3
    with pytest.raises(ParseError):
        parser.classify(3, None, None)

# Generated at 2022-06-13 18:01:50.387276
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from blib2to3.pgen2.grammar import Grammar
    from blib2to3.pgen2.pgen import generate_grammar
    import sys

    grammar_file = sys.argv[1]
    g = Grammar(grammar_file, generate_grammar)
    p = Parser(g)
    p.setup()

    def tokenize(s):
        for t in s.split():
            yield int(t)

    for input in sys.argv[2:]:
        p.setup()
        for type in tokenize(input):
            p.addtoken(type, None, None)
        print(input, p.stack)


# Generated at 2022-06-13 18:01:58.390473
# Unit test for method classify of class Parser
def test_Parser_classify():
    from .tokenize import generate_tokens
    from . import token
    from . import python_grammar_no_print_statement
    from . import future_features

    for t in generate_tokens("__debug__"):
        print(t)

    grammar = python_grammar_no_print_statement
    parser = Parser(grammar)
    parser.setup()
    for type, value, _, _, _ in generate_tokens("__debug__"):
        m = token.tok_name.get(type)
        assert m is not None
        type = eval(m.upper())
        print(type)
        if parser.addtoken(type, value, None):
            break



# Generated at 2022-06-13 18:02:04.075932
# Unit test for method shift of class Parser
def test_Parser_shift():
    from .parse import pgen
    from .pgen2.parse import driver

    with open("Parser/Grammar.txt") as file:
        text = file.read()
    g = driver.load_grammar("<test>", text)
    p = Parser(g, lam_sub)
    p.setup(p.grammar.symbol2number["file_input"])
    p.shift(token.INDENT, "", 1, (1, 0))



# Generated at 2022-06-13 18:02:17.726396
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import pgen
    from .pythonparser import pygram

    class Dummy:
        pass

    dummy = Dummy()
    dummy.reporter = Dummy()

    # Source: "print('Hello World')"
    t = token
    tokens = [
        (t.NAME, "print"),
        (t.OP, "("),
        (t.STRING, "'Hello World'"),
        (t.OP, ")"),
        (t.NEWLINE, "\n"),
        (t.ENDMARKER, ""),
    ]

    # Parse the tokens
    p = Parser(grammar=pgen.pgen(pygram, "Grammar.txt", "Python.asdl", "Python.gram"), convert=pygram.convert)
    p.setup()

# Generated at 2022-06-13 18:02:23.612378
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver, grammar

    # Parse a small program and return the abstract syntax tree
    p = Parser(grammar, driver.convert)

    p.setup()
    for type, value, _ in driver.tokenize("from tkinter import *"):
        p.addtoken(type, value, (_, _))
    ast = p.rootnode
    assert ast.type == grammar.start



# Generated at 2022-06-13 18:02:28.172428
# Unit test for method push of class Parser
def test_Parser_push():
    from blib2to3.pgen2 import tokenize, driver
    from blib2to3.pgen2.parse import Parser

    gr = driver.load_grammar('Grammar/Grammar')
    p = Parser(gr)
    p.setup()

    for t in tokenize.generate_tokens(open('Grammar/Grammar')):
        p.addtoken(t.type, t.string, t.start)

# Generated at 2022-06-13 18:02:38.509553
# Unit test for method shift of class Parser
def test_Parser_shift():  # fix issue #210
    # This is an annotated version of a real-world test case.
    # In the test case, line 10 was raised an exception
    # with the message "AttributeError: 'Grammar' object has no attribute 'dfas'".
    # This is because the expected and actual 'grammar' objects are different,
    # though they are both grammar instances.

    # expected_grammar
    from blib2to3.pgen2 import parse
    g = parse.read_grammar(
        open("blib2to3/Grammar.txt"),
        parse.dequote_unicode,
        "exec",
        "blib2to3/Grammar.txt",
    )

# Generated at 2022-06-13 18:02:54.488612
# Unit test for method pop of class Parser
def test_Parser_pop():
    dfa = [
        [(0, 0), (1, 1)]
    ]
    dfas = (dfa, {0: 2, 1: 2})
    grammar = Grammar()
    grammar.dfas[42] = dfas
    grammar.labels = [
        (token.NUMBER, "NUMBER"),
        (token.NAME, "NAME"),
    ]
    parser = Parser(grammar)
    parser.stack = [
        (dfas, 0, (42, None, None, [])),
        (dfas, 1, (42, None, None, []))
    ]
    parser.rootnode = None
    parser.used_names = set()
    parser.pop()
    dfa, state, node = parser.stack.pop()
    assert dfa == dfas
    assert state == 1


# Generated at 2022-06-13 18:03:04.580538
# Unit test for method classify of class Parser
def test_Parser_classify():
    class MockGrammar(object):
        def __init__(self):
            self.keywords = {"and": 1, "or": 2}
            self.tokens = {
                token.NUMBER: 3,
                token.STRING: 4,
                token.NAME: 5,
                token.OP: 6,
                token.NEWLINE: 7,
                token.INDENT: 8,
                token.DEDENT: 9,
                -1: 10,
            }

        def __getattr__(self, name: Any) -> Any:
            return None

    # Make sure the keywords mapping overrides the tokens mapping
    p = Parser(MockGrammar())
    for x in ["and", "or"]:
        ilabel = p.classify(token.NAME, x, None)

# Generated at 2022-06-13 18:03:13.613363
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import pytree
    import driver
    d = driver.Driver()
    treebuilder = pytree.TreeBuilder()
    converter = pytree.convert
    p = Parser(d.grammar, converter)
    p.setup()
    for t in d.tokenize('print "Hello, world!"'):
        if p.addtoken(t.type, t.string, t.context):
            break
    n = p.rootnode
    assert n.children[1].children[0].value == 'Hello, world!'

# Generated at 2022-06-13 18:03:14.395712
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    assert False, "TODO: Write unit tests for method Parser.addtoken"

# Generated at 2022-06-13 18:03:23.922369
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():

    import unittest
    from pprint import pprint

    class PyTreeTestCase(unittest.TestCase):

        def __init__(self, methodName: Text, grammar: Grammar):
            super().__init__(methodName)
            self.grammar = grammar

        def test_addtoken(self) -> None:
            p = Parser(self.grammar)
            p.setup()

            # Test 1: Simple addition
            token_type = token.PLUS
            value = '+'
            context = Context('+')
            should_stop = p.addtoken(token_type, value, context)
            self.assertFalse(should_stop)
            token_type = token.NUMBER
            value = '3'
            context = Context('3')

# Generated at 2022-06-13 18:03:24.351064
# Unit test for method shift of class Parser
def test_Parser_shift():
    pass

# Generated at 2022-06-13 18:03:28.305243
# Unit test for method setup of class Parser
def test_Parser_setup():
    import pdb
    import blib2to3.pygram as pygram
    import blib2to3.pgen2.driver as driver
    import blib2to3.pgen2.parse as parse
    pdb.run("parse.setup(pygram.python_grammar)")
    pdb.run("driver.parse_string('1+1', pygram.python_grammar, 'eval_input')")

# Generated at 2022-06-13 18:03:38.255867
# Unit test for method push of class Parser
def test_Parser_push():

    # Stub function to return an object of type 'DFAS'
    def stub_dfas(dfas, state_dict):
        return (dfas, state_dict)

    # Instantiate the class
    parser_obj = Parser(Grammar())

    # Create arguments for method push
    type = token.NAME
    newdfa = stub_dfas([], {})
    newstate = 0
    context = Context(None)

    # Invoke the method
    parser_obj.push(type, newdfa, newstate, context)

    # Check the results
    assert parser_obj.stack == [(newdfa, newstate, (type, None, context, []))], (
        "Got: " + str(parser_obj.stack)
    )



# Generated at 2022-06-13 18:03:50.574312
# Unit test for method classify of class Parser
def test_Parser_classify():
    # Create some tokens
    rbrack = Leaf(token.RBRACK, "]", None)
    name = Leaf(token.NAME, "Name", None)
    number = Leaf(token.NUMBER, "42", None)
    # Create a grammar

# Generated at 2022-06-13 18:04:01.593250
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver
    g = driver.load_grammar("Grammar.txt")
    p = Parser(g)
    p.setup()
    token_list = [
        ("NAME", "a", (1, 0)),
        ("PLUS", "+", (1, 2)),
        ("NAME", "b", (1, 4)),
        ("SEMI", ";", (1, 5)),
        ("newline", "\n", (1, 6)),
    ]
    for type, value, context in token_list:
        p.addtoken(getattr(token, type), value, context)
    assert p.rootnode is not None
    assert p.rootnode[1] == "a"
    assert p.rootnode[-1] is not None

# Generated at 2022-06-13 18:04:16.076149
# Unit test for method shift of class Parser
def test_Parser_shift():
    class grammar:
        pass
    g = grammar()
    g.tokens = {1: 1}
    p = Parser(g)
    p.setup()
    p.shift(1, None, 1, None)



# Generated at 2022-06-13 18:04:22.971622
# Unit test for method push of class Parser
def test_Parser_push():
    from . import parsetok, parse
    from . import tokenize
    from . import pytree
    from . import python_grammar

    def convert(grammar, node):
        return node

    p = Parser(python_grammar, convert)
    p.setup()

    def assert_node_list_equal(list1, list2):
        for node1, node2 in zip(list1, list2):
            assert node1.type == node2.type
            assert node1.value == node2.value
            assert node1.context == node2.context
            if len(node1.children) > 0:
                assert_node_list_equal(node1.children, node2.children)

    # Test 1:
    source = """\
    class Foo:pass
    """

# Generated at 2022-06-13 18:04:24.304992
# Unit test for method pop of class Parser
def test_Parser_pop():
    assert Parser.pop(Parser(Grammar(), lam_sub)) == None

# Generated at 2022-06-13 18:04:31.834229
# Unit test for method classify of class Parser
def test_Parser_classify():
    from .driver import Driver
    import io

    test_code = """\
print 1
print "hello"
print "fob", "oar", "baz"
print 'fob', 'oar', 'baz'
print (x + 1), (y + 2), (z + 3)
"""
    grammar = Grammar()
    source = io.StringIO(test_code)
    d = Driver(grammar, source)

    p = Parser(grammar)
    p.setup()
    while True:
        t = d.get_input_token()
        if not t:
            break
        ilabel = p.classify(t.type, t.value, t.context)
        tok = grammar.labels[ilabel]
        print(tok)


# Generated at 2022-06-13 18:04:40.976257
# Unit test for method classify of class Parser
def test_Parser_classify():
    from textwrap import dedent
    from . import tokenize, untokenize
    import io

    def test(s: Text) -> None:
        s = dedent(s)
        f = io.StringIO(s)
        t = tokenize.generate_tokens(f.readline)
        t = list(t)
        assert untokenize(t) == s
        g = Grammar(t)
        p = Parser(g)
        p.setup()
        for t in p.grammar.grammar:
            if t[3] == "keyword":
                p.addtoken(t[4], t[1], (0, 0))
                assert p.used_names == {t[1]}

# Generated at 2022-06-13 18:04:52.615930
# Unit test for method push of class Parser
def test_Parser_push():
    class MockDFAS(object):
        def __init__(self, states, first):
            self.states = states
            self.first = first
        def __len__(self):
            return len(self.states)

    class MockGrammar(object):
        def __init__(self):
            self.dfas = {}
            for type in range(256, 257):
                states = {
                    0: {
                        (0, 2): (0, 2),
                        (0, 3): (0, 3),
                    },
                    1: {
                        (1, 2): (0, 2),
                        (1, 3): (0, 3),
                    },
                    2: {
                        (1, 2): (0, 2),
                        (1, 3): (0, 3),
                    },
                }

# Generated at 2022-06-13 18:05:01.772962
# Unit test for method push of class Parser
def test_Parser_push():
    from .grammar import Grammar


# Generated at 2022-06-13 18:05:09.483855
# Unit test for method pop of class Parser
def test_Parser_pop():
    import collections
    import pgen2.parse
    g = pgen2.parse.load_grammar(pgen2.parse.get_grammar())
    p = Parser(g)
    p.setup(g.start)
    # Iff the parser is actually a grammar parser, the following loop gives:
    #     File "pgen2/parse.py", line 626, in parse
    #       return parser.rootnode
    #     File "pgen2/pgen2.py", line 284, in rootnode
    #       self.rootnode.used_names = self.used_names
    #     AttributeError: 'Leaf' object has no attribute 'used_names'
    i = 0

# Generated at 2022-06-13 18:05:17.284835
# Unit test for method shift of class Parser
def test_Parser_shift():
    grammar = Grammar.from_string(test_grammar)
    parser = Parser(grammar)
    parser.setup()
    parser.shift(1, 'a', 1, None)
    parser.shift(1, 'b', 2, None)
    parser.shift(2, 'c', 3, None)
    parser.addtoken(1, 'd', None)

# Generated at 2022-06-13 18:05:26.534706
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2.tokenize import generate_tokens

    def test_classify(grammar: Grammar, input: Text) -> None:
        parser = Parser(grammar)
        parser.setup()
        for type, value, context in generate_tokens(StringIO(input)):
            parser.addtoken(type, value, context)
        #parser.addtoken(token.ENDMARKER, "", (1, 0))

    def test_grammar(grammar: Grammar) -> None:
        test_classify(grammar, "and")
        test_classify(grammar, "as")
        test_classify(grammar, "assert")
        test_classify(grammar, "break")
        test_classify(grammar, "class")
        test_

# Generated at 2022-06-13 18:06:11.085965
# Unit test for method pop of class Parser
def test_Parser_pop():
    class MethodWrapper:
        def __init__(self):
            self.called = False
        def __call__(self, grammar: Grammar, node: RawNode) -> Union[Node, Leaf]:
            self.called = True
            return node

    from .grammar import Grammar

    grammar = Grammar(open("Python.asdl"))
    parser = Parser(grammar, convert=MethodWrapper())
    parser.pop()
    assert parser.rootnode is not None
    assert parser.rootnode.called



# Generated at 2022-06-13 18:06:17.663171
# Unit test for method push of class Parser
def test_Parser_push():
    import pickle
    grammar = pickle.load(open(r"test\optimize\grammar.pickle", "rb"))
    parser = Parser(grammar)
    parser.setup()
    assert parser.addtoken(1, "abc", None) == False
    assert parser.addtoken(2, "abc", None) == False
    assert parser.addtoken(3, "abc", None) == True

# Generated at 2022-06-13 18:06:29.083750
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import pgen2

    class TestGrammar(pgen2.Grammar):
        grammar = r"""
        s: {a}
        """
        start = "s"

    def TestConvert(grammar, node):
        return node

    # Test that the correct node is generated and put into the tree
    # when parsing a token
    p = Parser(TestGrammar, TestConvert)
    p.setup()
    p.classify(token.NAME, "a", context.Context(1, 1))
    p.addtoken(token.NAME, "a", context.Context(1, 1))
    assert p.rootnode[0] == "s" and p.rootnode[1] is None

# Generated at 2022-06-13 18:06:37.045623
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, token
    from .pgen import driver

    gram = grammar.grammar

    p = Parser(gram)
    p.setup()
    t = driver.Driver(gram, convert=None)
    while True:
        try:
            typ, val, context = t.get_last_token()  # type: int, Text, Context
        except token.TokenError as err:
            raise err.__class__(err.args[0] + " -> " + str(context))
        if p.addtoken(typ, val, context):
            break

    root = p.rootnode
    # print(root)

# Generated at 2022-06-13 18:06:45.694809
# Unit test for method pop of class Parser
def test_Parser_pop():
    import sys
    from . import driver, token, test_grammar

    p = Parser(test_grammar.grammar)
    p.setup()
    p.stack.append((None, None, (1, None, None, None)))
    p.stack.append((None, None, (2, None, None, [])))
    p.pop()
    assert p.stack[-1][2] == (1, None, None, [Node(type=2, children=[],)])


# Top-level functions
# ===================


# Generated at 2022-06-13 18:06:57.604331
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar
    from . import tokenize
    from . import driver
    from blib2to3.pgen2.convert import convert_tree, fix_missing_locations

    class DummyFixer:
        """Fixer implementation used for testing."""

        def __init__(self) -> None:
            self.fixed = False

        def fix(self, node: Node) -> List[Node]:
            assert isinstance(node.parent, Node)
            assert node.parent.type in ("sometype", "dummy")
            assert node.children == []
            self.fixed = True
            return []

    p = Parser(grammar.grammar)
    p.setup()
    f = tokenize.StringIO(r"x=y")

# Generated at 2022-06-13 18:07:04.276412
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import grammar, tokenize
    g = grammar.grammar
    p = Parser(g)
    p.setup()
    gen = tokenize.generate_tokens(open("Grammar.txt"))
    while 1:
        try:
            type, value, context = gen.next()
        except StopIteration:
            break
        if p.addtoken(type, value, context):
            break
    from . import pytree
    print(pytree.to_str(p.rootnode))


if __name__ == "__main__":
    test_Parser_addtoken()

# Generated at 2022-06-13 18:07:13.023699
# Unit test for method classify of class Parser
def test_Parser_classify():
    # Save name tokens for later checking
    name_tokens = []
    # Synthesize the name of the test parser table
    test_table_filename = "test_Parser_classify"
    test_table_name = test_table_filename + "_table"
    # Synthesize a module importing the test parser table

# Generated at 2022-06-13 18:07:18.541733
# Unit test for method shift of class Parser
def test_Parser_shift():
    """
    input:
    (1, 'abc', (1, 2), None)
    output:
    (1, 'abc', (1, 2), None)
    """
    p = Parser(Grammar(grammar=[]))
    p.stack.append((1, 0, (1, None, None, None)))
    p.shift(1, 'abc', 0, (1, 2))
    assert p.stack[0][-1] == (1, None, None, None)


# Generated at 2022-06-13 18:07:35.141178
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import token
    from . import grammar
    from . import parse
    from . import pytree
    from .tokenize import detect_encoding, source_tokenize, TokenError

    def _get_tokens(filename):
        text = open(filename, "rb").read()
        encoding, _ = detect_encoding(text)
        try:
            tokens = list(source_tokenize(BytesIO(text).readline, encoding))
        except TokenError:
            return None
        else:
            return tokens

    class _Node(pytree.Base):
        pass

    class _Converter(parse.BaseParser):
        def p_none(self, args):
            """
            t :
            """

    def _run_parser(tokens, start):
        grammar = grammar.Grammar()
        grammar

# Generated at 2022-06-13 18:08:46.737198
# Unit test for method classify of class Parser
def test_Parser_classify():
    old_token_map = token.tok_name
    import blib2to3.pgen2.grammar as Grammar
    from blib2to3.pgen2 import token, driver

    gramm = Grammar.from_file(driver.find_grammar("Python.gram"))
    P = Parser(gramm)
    P.setup()
    token.tok_name[1] = 'RESERVED_WORD'
    grammar_token_map = P.classify(1, "yield", None)
    assert grammar_token_map == 674
    token.tok_name[1] = old_token_map

test_Parser_classify()

# Generated at 2022-06-13 18:08:57.560862
# Unit test for method pop of class Parser
def test_Parser_pop():
    class Parser(object):
        pass
    p = Parser()
    p.stack = []
    p.stack.append(("dfa1", 0, "node1"))
    p.stack.append(("dfa2", 0, "node2"))
    assert p.stack == [("dfa1", 0, "node1"), ("dfa2", 0, "node2")]
    p.pop()
    assert p.stack == [("dfa1", 0, "node1")]

# Generated at 2022-06-13 18:09:07.128998
# Unit test for method setup of class Parser
def test_Parser_setup():
    from blib2to3.pgen2 import (
        driver,
        tokenize,
        data,
        grammar,
        parse,
        pgen,
    )
    #driver.Driver(grammar.Grammar(data.pgen_grammar), convert=lam_sub,
    #              logger=pgen.NullLogger()).run()
    p = parse.Parser(grammar.Grammar(data.pgen_grammar), convert=lam_sub)
    p.setup()

    #def dumptokens(file: Text) -> Sequence[Tuple[int, Text, Optional[Text]]]:
    #    tokens = []
    #    for t in tokenize.generate_tokens(open(file)):
    #        typ = t[0]
    #        if typ == token.NAME

# Generated at 2022-06-13 18:09:18.210707
# Unit test for method setup of class Parser
def test_Parser_setup():
    class Checker:
        def __init__(self, classifier, tokens, keywords):
            self.classifier = classifier
            self.tokens = tokens
            self.keywords = keywords

    import grammar

    classifier = Checker(None, None, None)
    tokens = Checker(None, None, None)
    keywords = Checker(None, None, None)
    g = grammar.Grammar(classifier, tokens, keywords)
    p = Parser(g)
    p.setup()
    assert p.grammar is g
    assert p.convert is lam_sub


# Generated at 2022-06-13 18:09:22.957105
# Unit test for method shift of class Parser
def test_Parser_shift():
    parser = Parser(Grammar(), None)
    assert parser.stack[-1] == (None, None, None)
    parser.shift(1, 2, 3, 4)
    assert parser.stack[-1] == (1, 3, 2)

# Generated at 2022-06-13 18:09:37.333156
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # NOTE: this unit test only tests the method addtoken.
    #       Its test cases are only minimal examples,
    #       as this method is covered by the regression tests.
    class MockGrammar(object):
        def __init__(self) -> None:
            self.start = 3
            self.dfas = {3: ([[], [(2, 1), (3, 2)], [(0, 2)], [(0, 3)]], {0: 0, 1: 1})}
            self.tokens = {4: 1, 5: 2, 1: 3}
            self.labels = [(None, None), (4, None), (5, None), (1, None)]

    class MockConvert(object):
        def __init__(self) -> None:
            self.node = None
            self.values = []



# Generated at 2022-06-13 18:09:44.585260
# Unit test for method pop of class Parser
def test_Parser_pop():
    """Unit test for method pop of class Parser"""
    import os, sys
    import support
    import blib2to3.pgen2.pgen

    if len(sys.argv) > 1:
        support.set_testing_directory(sys.argv[1])

    test_dir = os.path.join(support.TEST_DIRECTORY, 'Parser')
    support.chdir(test_dir)

    parse = blib2to3.pgen2.pgen.PgenReader(support.findfile('Python.grammar'))
    parse.parse()
    grammar = parse.grammar
    parse.driver()
    _pickle = os.path.join(support.TEST_DIRECTORY, 'Parser', 'unpickled.grammar')
    f = open(_pickle, 'rb')


# Generated at 2022-06-13 18:09:50.159020
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import pickle as p

    gfile = 'blib2to3/pgen2/Grammar.txt'
    with open(gfile, 'br') as g:
        grammar = p.load(g)
    p = Parser(grammar)
    p.setup()
    assert p.addtoken(1, '', None) == False
    assert p.addtoken(2, '', None) == False
    assert p.addtoken(3, '', None) == True


# Generated at 2022-06-13 18:09:52.911501
# Unit test for method setup of class Parser
def test_Parser_setup():
    import pgen2.pgen
    g = pgen2.pgen.generate_grammar()
    p = Parser(g)
    p.setup()



# Generated at 2022-06-13 18:09:57.819427
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar
    from . import tokenize

    g = grammar.Grammar()
    p = Parser(g)
    p.setup()
    p.shift(tokenize.NUMBER, '1', 1, '')
    assert p.stack[-1][-1][0] == 1
    assert p.stack[-1][-1][1] == '1'

