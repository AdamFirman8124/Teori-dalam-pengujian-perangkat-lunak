

# Generated at 2022-06-13 18:01:37.869417
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import grammar

    p = Parser(grammar)
    p.setup()
    p.stack = [('foo', 'bar', ('baz', 'qux', 'quux', 'quuux'))]
    p.pop()



# Generated at 2022-06-13 18:01:47.610345
# Unit test for method push of class Parser
def test_Parser_push():
    from . import pygram
    from . import pytree
    from .pgen2 import driver

    grammar = pygram.python_grammar
    driver.build_grammar(grammar)

    parsed = driver.parse_string("import os")
    assert parsed.as_string(parsed) == "import os"
    parsed = driver.parse_string("from os import (path)\nimport os")
    assert parsed.as_string(parsed) == "from os import (path)\nimport os"
    parsed = driver.parse_string("from os import (path,\n)")
    assert parsed.as_string(parsed) == "from os import (path,\n)"

    parsed = driver.parse_string("if __name__ == '__main__': pass")

# Generated at 2022-06-13 18:01:53.459145
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver

    p = Parser(driver.grammar)
    p.setup()
    t = token.NAME
    v = 'if'
    c = Context(1, 0, '')
    assert not p.addtoken(t, v, c)
    c = Context(1, 0, '')
    v = ':'
    assert not p.addtoken(t, v, c)
    t = token.NEWLINE
    v = '\n'
    c = Context(1, 0, '')
    assert p.addtoken(t, v, c)

# Generated at 2022-06-13 18:02:02.059965
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import token


# Generated at 2022-06-13 18:02:16.241479
# Unit test for method pop of class Parser
def test_Parser_pop():
    # Simple test case:
    #
    # If a call to "pop" results in a node with a None 'children' attribute,
    # then convert that node to a leaf node.
    popdfa = (None, None)
    popstate = 0
    popnode = (None, None, None, None)
    p = Parser(None)
    p.stack = [popdfa, popstate, popnode]
    assert p.stack == [(popdfa, popstate, popnode)]
    p.pop()
    assert p.stack == []
    assert isinstance(p.rootnode, Leaf)
    # And if a call to "pop" results in a node with a list of children, don't
    # convert it to a leaf node.
    popdfa = (None, None)
    popstate = 0
    popnode

# Generated at 2022-06-13 18:02:26.816090
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from . import driver
    from . import grammar
    from . import token

    from .pgen2 import grammar as grammar_

    def _test(source: Text) -> Node:
        gl = grammar_.grammar()
        g = grammar.Grammar(gl, "Grammar")
        p = Parser(g)
        d = driver.Driver(g, convert=lam_sub)
        p.setup()
        tokens = list(d.tokenize(source))
        tokens.reverse()
        while tokens:
            t = tokens.pop()
            # print "Token", t.type, t.value
            if p.addtoken(t.type, t.value, t.context):
                break
        return p.rootnode


# Generated at 2022-06-13 18:02:37.829500
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar
    from . import driver
    from .tokenizer import generate_tokens
    from .pygram import python_symbols as syms
    from .pytree import Leaf

    tokens = list(
        generate_tokens(iter(["while", "True", ":", "pass"]).__next__)
    )
    g = grammar.grammar
    p = Parser(g)
    p.setup()
    for token in tokens:
        p.shift(*token)

    result = p.rootnode
    expected = Leaf(
        syms.while_stmt, value="while", context=Context(1, 0, 1, 5), children=[]
    )
    driver.assert_node(result, expected)



# Generated at 2022-06-13 18:02:43.218354
# Unit test for method pop of class Parser
def test_Parser_pop():
    def check(popnode):
        print(popnode)

    p = Parser(Grammar())
    p.stack = [('a', 'b', 'c'), ('d', 'e', 'f')]
    p.convert = check
    p.pop()

    # The following will fail, because check return None.
    # The check function should raise an exception.
    p.rootnode = 'g'


# Generated at 2022-06-13 18:02:54.279335
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class ParserTest(Parser):
        def __init__(self, grammar: Grammar, convert: Optional[Convert] = None) -> None:
            Parser.__init__(self, grammar, convert)
            self.seen = []  # type: Sequence[Tuple[int, int, Context]]

        def addtoken(self, type: int, value: Optional[Text], context: Context) -> bool:
            self.seen.append((type, len(self.stack), context))
            return Parser.addtoken(self, type, value, context)

    import blib2to3.pgen2.tokenize as tokenize

    tokengen = tokenize.generate_tokens(
        iter(["x = 3 + 42\n"]).__next__
    )  # type: ignore



# Generated at 2022-06-13 18:03:04.547176
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import nose

    class TestParser(object):
        def setup(self):
            import blib2to3.pgen2.driver
            self.g = blib2to3.pgen2.driver.load_grammar('Grammar/Grammar')
            self.p = Parser(self.g)

        def test_accept(self):
            self.p.setup()

# Generated at 2022-06-13 18:03:20.779315
# Unit test for method pop of class Parser
def test_Parser_pop():
    import unittest
    import textwrap
    from blib2to3.pgen2 import driver
    from blib2to3.pytree import convert
    text = textwrap.dedent("""
        def func():
            pass
    """)
    with driver.parse_string(text, debug=False) as parser:
        parser.pop()
        assert parser.rootnode.type == token.FILE_INPUT
        assert len(parser.rootnode.children) == 2
    with driver.parse_string(text, debug=False, convert=convert) as parser:
        parser.pop()
        assert parser.rootnode.type == token.file_input
        assert len(parser.rootnode.children) == 2

if __name__ == "__main__":
    test_Parser_pop()

# Generated at 2022-06-13 18:03:29.101058
# Unit test for method classify of class Parser
def test_Parser_classify():
    from .cst.grammar import CstGrammar
    from .cst.tree import CSTNode
    from .cst.converter import CST2CST

    grammar = CstGrammar()
    parser_raw = Parser(grammar)
    parser_cst = Parser(grammar, CST2CST)

    # Test 1
    assert parser_cst.classify(token.NAME, 'abc', None) == 1
    assert parser_cst.classify(token.NAME, 'while', None) == 4
    assert parser_cst.classify(token.NEWLINE, '\n', None) == 4
    assert parser_cst.classify(token.NEWLINE, '\n', None) == 5
    assert parser_cst.classify(token.INDENT, '\t', None)

# Generated at 2022-06-13 18:03:35.080656
# Unit test for method classify of class Parser
def test_Parser_classify():
    from .pgen2 import write_grammar, make_pgen, parse_grammar

    g = parse_grammar(make_pgen(write_grammar()), debug=0)
    p = Parser(g)
    p.setup()
    p.addtoken(token.STRING, '"a"', Context('<string>', 1, 0, 1, 3))


# Generated at 2022-06-13 18:03:40.781340
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    from pprint import pprint
    from blib2to3.pgen2.parse import tokenize
    from . import literals
    from . import punctuation
    from . import keywords
    from . import grammar
    from . import unparse

    def read_string(s: str) -> List[token.token]:
        return tokenize.generate_tokens(iter([s]).__next__)

    # Create a grammar and parser, feed in a program
    g = grammar.grammar
    p = Parser(g)
    p.setup()
    _tokenize = read_string("foo = '123' + 456")
    while True:
        try:
            t = _tokenize.__next__()
        except StopIteration:
            break

# Generated at 2022-06-13 18:03:51.840030
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import random
    import string

    class TestParser(Parser):
        def __init__(self):
            Parser.__init__(self, grammar)

    grammar = Grammar(
        dfas={
            0: ([[(1, 1), (2, 0)], [(1, 2), (0, 2)]], set()),
            1: ([[(2, 1)]], set()),
            2: ([[(2, 1)], [(0, 2)], [(0, 3)]], set()),
        },
        labels=[None, None, None, None],
        keywords={},
        tokens={},
        start=0,
    )

    # Test exception bad token.
    p = TestParser()
    p.setup()

# Generated at 2022-06-13 18:04:01.815430
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import grammar
    from . import tokenize
    from io import BytesIO

    # Testing normal shift
    g = grammar.Grammar()
    g.add_dfa(0, [0, 0, 0], {0: [(1, 2)], 1: [(2, 2)], 2: [(1, 2)]})
    g.add_token(token.NAME, "a")
    g.add_token(token.NUMBER, "b")
    parser = Parser(g)
    parser.setup()
    parser.addtoken(token.NUMBER, "1", (1, 0))

# Generated at 2022-06-13 18:04:11.410196
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    class TestGrammar(Grammar):
        keywords = {'def': 1, 'class': 2}
        tokens = {
            token.NAME: 1,
            token.NL: 2,
            token.INDENT: 3,
            token.DEDENT: 4,
            token.NUMBER: 5,
            token.LPAR: 6,
            token.RPAR: 7,
        }
        labels = [
            ('NAME', 1),
            ('NL', 2),
            ('INDENT', 3),
            ('DEDENT', 4),
            ('NUMBER', 5),
            ('LPAR', 6),
            ('RPAR', 7),
            ('def', 1),
            ('class', 2),
        ]
        start = 'file_input'
        dfas: Dict[int, DFAS] = {}
       

# Generated at 2022-06-13 18:04:16.796810
# Unit test for method push of class Parser
def test_Parser_push():
    # test if method push of class Parser works correctly
    dfa_dict = {1:([(1,1),(0,2)],{1:2}), 2:([],{})}
    p = Parser(Grammar(dfa_dict,{1:1,0:0},{1,0},{1:1,0:0},0,{0:0}))
    p.push(1, dfa_dict[1], 0, None)
    assert 1 == len(p.stack)
    assert (dfa_dict[1], 0, (1, None, None, [])) == p.stack[0]

# Generated at 2022-06-13 18:04:20.571867
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2.grammar import Grammar

    from blib2to3.pgen2.pgen import driver

    from . import token

    grammar = Grammar(driver.parse_grammar(grammar, "Grammar/Grammar"))
    parser = Parser(grammar)
    parser.classify(token.PLUS, "+", (1, 0))

# Generated at 2022-06-13 18:04:27.016082
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar

    parser = Parser(grammar.grammar)
    assert parser.classify(token.NAME, "while", (1, 0)) == grammar.syms.while_stmt
    assert parser.classify(token.NAME, "foo", (1, 0)) == grammar.tokens.NAME
    try:
        parser.classify(token.OP, "+", (1, 0))
    except ParseError:
        pass
    else:
        raise ValueError()

# Generated at 2022-06-13 18:04:51.611534
# Unit test for method push of class Parser
def test_Parser_push():
    s = "abc"
    lst = []
    assert len(lst) == 0
    lst.append(s)
    assert len(lst) == 1
    lst[0] = s
    assert len(lst) == 1
    assert lst[0] == s

# Generated at 2022-06-13 18:05:00.456264
# Unit test for method pop of class Parser
def test_Parser_pop():
    grammar = Grammar()

    class TestError(Exception): pass

    def fake_convert(grammar: Grammar, fakenode: RawNode) -> Optional[NL]:
        if fakenode[0] == ">|":
            raise TestError()
        return fakenode

    p = Parser(grammar, fake_convert)
    p.setup()

    for t in (token.NAME, token.NAME, token.OP, token.OP, token.OP):
        try:
            p.addtoken(t, "foo", None)
        except ParseError:
            pass

    try:
        p.pop()
    except TestError:
        pass
    else:
        raise AssertionError("No TestError was raised.")

# Generated at 2022-06-13 18:05:04.364505
# Unit test for method push of class Parser
def test_Parser_push():
    grammar = Grammar()
    parser = Parser(grammar)
    parser.setup()
    class Dfa:
        pass
    newdfa = Dfa()
    newdfa.s = 0
    parser.push(0, newdfa, 0, 0)
    assert parser.stack[0][0].s == 0

# Generated at 2022-06-13 18:05:08.479698
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import driver
    from . import grammar

    g = grammar.Grammar()
    p = Parser(g)
    p.setup()
    for t in driver.tokenize_string(r"1+1"):
        p.addtoken(t.type, t.value, t.context)
    assert p.rootnode.value == "+"
    assert p.rootnode.children[0].value == 1
    assert p.rootnode.children[1].value == 1

# End of unit test


# Generated at 2022-06-13 18:05:21.034529
# Unit test for method pop of class Parser
def test_Parser_pop():
    import sys, os
    from . import graminit, tokenize, token
    from . import driver
    from . import pgen

    # use test0.txt for grammar
    test_grammar = pgen.read_grammar(graminit.grammar, "test0.txt")
    # use test0.txt for input
    test_driver = pgen.make_pgen(test_grammar, bool(1))
    # assert test_driver(test0.txt) = True
    assert test_driver(test0.txt) == True
    test_scan = tokenize.generate_tokens(open(test0.txt))
    test_parse = test_driver.parse_tokens(test_scan)
    # assert test_parse = 'success'
    assert test_parse == 'success'
    test_grammar

# Generated at 2022-06-13 18:05:29.463017
# Unit test for method setup of class Parser
def test_Parser_setup():
    from . import pgen2
    import sys
    if sys.argv[1:]:
        filename = sys.argv[1]
    else:
        filename = "/home/bpp/python3.2/Lib/lib2to3/Grammar.txt"
    gr = pgen2.generate_grammar(filename)
    p = Parser(gr)
    p.setup()
    return p

if __name__ == "__main__":
    p = test_Parser_setup()
    print(p)

# Generated at 2022-06-13 18:05:32.520316
# Unit test for method push of class Parser
def test_Parser_push():
    grammar = Grammar()
    grammar.add_symbol(token.NAME, 'foo')
    dfa = {0: [(0, 0)], 1: [(0, 1)]}
    p = Parser(grammar)
    p.push(token.NAME, (dfa, {}), 1, None)
    assert len(p.stack) == 2
    assert p.stack[-1] == (dfa, 1, (token.NAME, None, None, []))



# Generated at 2022-06-13 18:05:36.045664
# Unit test for method shift of class Parser
def test_Parser_shift():
    from . import driver
    from . import pygram
    from .pytree import Leaf

    parser = Parser(pygram.python_grammar)
    parser.setup()

    tok = driver.tokenize_str('import sys')
    for type, value, context in tok:
        parser.shift(type, value, 0, context)

    dfa, state, node = parser.stack[-1]
    assert node[-1] == [Leaf(1, 'import'), Leaf(1, 'sys')]

# Generated at 2022-06-13 18:05:45.315423
# Unit test for method setup of class Parser
def test_Parser_setup():
    from blib2to3.pgen2.grammar import grammar
    from pprint import pprint  # debugging

    import sys
    import os

    # Uncomment to save the new version of the pickle
    # path_tokenize = os.path.join(os.path.dirname(sys.executable),
    #                              "lib2to3/Grammar.txt")
    # import tokenize
    # tokenize.tokenize(open(path_tokenize).readline)
    # import pickle
    # pickle.dump(grammar, open("Grammar.pickle", "wb"), protocol=2)

    p = Parser(grammar)
    p.setup()
    pprint(p.stack)
    print()



# Generated at 2022-06-13 18:05:54.957513
# Unit test for method pop of class Parser
def test_Parser_pop():
    from . import driver
    from . import token

    p = driver.Parser(driver.Grammar())

    # Test for empty stack
    p.stack = []
    p.pop()
    assert p.rootnode is None

    # Simple case
    p.stack = [
        (None, None, (token.INDENT, None, None, [])),
        (None, None, (token.INDENT, None, None, [])),
        (None, None, (token.INDENT, None, None, [])),
    ]
    p.pop()
    assert p.rootnode is None
    p.pop()
    assert p.rootnode.type == token.INDENT



# Generated at 2022-06-13 18:06:29.084183
# Unit test for method push of class Parser
def test_Parser_push():
    class MyParser(object):
        def __init__(self, token: Text) -> None:
            self.token = token

    p = MyParser("foo")

    # Case 1; newdfa = [(0, 0), (1, 1), (2, 2), (3, 3)]
    newdfa = [(0, 0), (1, 1), (2, 2), (3, 3)]
    newstate = 1
    p.push(4, newdfa, newstate, None)
    assert p.stack == [([(0, 0), (1, 1), (2, 2), (3, 3)], 0, None)]

    # Case 2; newdfa = [(0, 0), (1, 1), (2, 2), (3, 3)]

# Generated at 2022-06-13 18:06:38.485759
# Unit test for method shift of class Parser
def test_Parser_shift():
    """Unit test for method shift of class Parser"""
    # Create grammar instance
    grammar = Grammar("""
        start: item+ ENDMARKER
        item: NAME | NUMBER
        """)
    # Create parser instance
    parser = Parser(grammar)
    parser.setup()
    # For each expected results
    expected = [
        (token.NAME, "name", 1, False),
        (token.NAME, "name", 1, True),
        (token.NAME, "name", 1, True),
    ]

# Generated at 2022-06-13 18:06:49.199869
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    # Dummy items for leaf nodes
    ctx = Context()
    l0 = Leaf(type=0, value=None, context=ctx)
    l1 = Leaf(type=0, value=None, context=ctx)
    l2 = Leaf(type=0, value=None, context=ctx)
    l3 = Leaf(type=0, value=None, context=ctx)
    l4 = Leaf(type=0, value=None, context=ctx)

    # Create parser
    p = Parser(Grammar())
    # Create toy grammar
    g = Grammar()
    g.start = 1
    g.tokens = {}

# Generated at 2022-06-13 18:07:00.464218
# Unit test for method shift of class Parser
def test_Parser_shift():
    from typing import TYPE_CHECKING
    from blib2to3.pgen2.pgen import Grammar as Grammar_cls
    from blib2to3.pygram import python_symbols as sym

    if TYPE_CHECKING:
        from . import pytree

    class DummyGrammar(Grammar_cls):
        def __init__(self):
            Grammar_cls.__init__(self, "", "", {"test": 100})

    class DummyContext(Context):
        pass

    class DummyNode(pytree.Node):
        pass

    class DummyLeaf(pytree.Leaf):
        pass

    def convert(grammar: Grammar, node: RawNode) -> Union[Node, Leaf]:
        if node[0] == sym.test:
            return DummyNode

# Generated at 2022-06-13 18:07:05.854261
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import doctest
    from . import grammar
    from . import driver

    driver.setup_logging()

    doctest.testmod(grammar)
    doctest.run_docstring_examples(Parser.addtoken, globals())

# Generated at 2022-06-13 18:07:14.096176
# Unit test for method shift of class Parser
def test_Parser_shift():
    import sys
    if sys.version_info.major == 3:
        return
    from blib2to3.pgen2 import driver

    d = driver.Driver(
        grammar=None,
        convert=None,
        logger=None,
        picklefile="Parser/Python.grammar.pickle",
    )
    p = Parser(grammar=d.grammar, convert=d.convert)
    p.setup()
    p.addtoken(token.NAME, "test", None)

# Generated at 2022-06-13 18:07:21.627516
# Unit test for method pop of class Parser
def test_Parser_pop():
    # This test case was added in response to issue 11409
    import blib2to3.pgen2.tokenize as tokenize  # type: ignore
    import io

    def to_tokens(text: str) -> Sequence[Any]:
        "Return the sequence of tokens corresponding to text"
        lines = text.split("\n")
        readline = io.StringIO(text).readline
        return list(tokenize.generate_tokens(readline))

    parser = Parser(Grammar())
    tokens = to_tokens("x = 42\n")
    for type, value, context in tokens:
        parser.addtoken(type, value, context)

    assert parser.rootnode[1] == "file_input"
    assert parser.rootnode[3][0][1] == "stmt"

# Generated at 2022-06-13 18:07:22.864324
# Unit test for method push of class Parser
def test_Parser_push():
    from . import parser as _parser
    from . import pgen
    from . import tokenize
    import tempfile


# Generated at 2022-06-13 18:07:28.329049
# Unit test for method setup of class Parser
def test_Parser_setup():
    import unittest
    from . import grammar
    from . import driver
    from . import token
    from blib2to3.pgen2.parse import ParseError

    class ParserTestCase(unittest.TestCase):
        def setUp(self):
            self.parser = Parser(grammar)

        def test_setup(self):
            self.parser.setup()
            self.parser.setup(token.LNAME)

    unittest.main()


# Generated at 2022-06-13 18:07:35.625639
# Unit test for method shift of class Parser
def test_Parser_shift():
    import token
    import grammar

    gr = grammar.Grammar()
    
    p = Parser(gr, None)
    p.setup()

    # test for p._pending_nl
    nl_raw_node = ("NEWLINE", None, None, None)
    pop_node = ("small_stmt", None, None, [nl_raw_node])
    node = p.stack[0][2]
    nl_node = Node(
        type=token.NEWLINE, children=[], context=None
    )
    # test for p._pending_nl when p._pending_nl == True
    p._pending_nl = True
    node[-1].append(nl_node)
    # test for dfa, state, node
    p.shift(token.NEWLINE, None, 1, None)

# Generated at 2022-06-13 18:08:26.943122
# Unit test for method addtoken of class Parser
def test_Parser_addtoken():
    import blib2to3.pgen2.pgen
    import blib2to3.pgen2.parse
    import blib2to3.pgen2.tokenize
    import blib2to3.pgen2.driver
    import blib2to3.pgen2.grammar
    import blib2to3.pgen2.convert

    # Generate the tables from the grammar
    blib2to3.pgen2.pgen.generate_grammar(debug=False)

    # Open the tables and turn them into a grammar
    g = blib2to3.pgen2.parse.load_grammar()

    # Tokenize the sample program
    filename = blib2to3.pgen2.convert.__file__.replace(".pyc", ".py")
    tokengen

# Generated at 2022-06-13 18:08:33.817849
# Unit test for method classify of class Parser
def test_Parser_classify():
    from . import grammar, token
    from .literals import parse_string, parse_literal

    p = Parser(
        grammar.grammar,
        convert=parse_literal,
    )

    p.setup()
    p.addtoken(token.LPAR, "(", (1, 0))
    p.addtoken(token.NAME, "x", (1, 1))
    p.addtoken(token.RPAR, ")", (1, 2))



# Generated at 2022-06-13 18:08:44.876764
# Unit test for method push of class Parser
def test_Parser_push():
    from . import grammar, driver


# Generated at 2022-06-13 18:09:01.634902
# Unit test for method pop of class Parser
def test_Parser_pop():
    from .driver import Driver
    from . import grammar

    # Load the grammar
    g = grammar.Grammar(version="3.8")

    # Load the driver
    d = Driver(g, convert=lam_sub)

    # Define a couple of test cases
    p = Parser(g)

# Generated at 2022-06-13 18:09:10.226412
# Unit test for method classify of class Parser
def test_Parser_classify():
    import unittest

    class Test(unittest.TestCase):
        class MockGrammar:
            def __init__(self):
                self.tokens = {"__tokens": 1, "NAME": 2}
                self.keywords = dict()

        def test_classify(self):
            g = Test.MockGrammar()
            p = Parser(g)
            self.assertEqual(p.classify(token.NAME, "name", NL), 2)
            self.assertEqual(p.classify(token.NAME, "__tokens", NL), 1)
            with self.assertRaises(ParseError):
                p.classify(token.NAME, "symbol", NL)

    unittest.main()

if __name__ == "__main__":
    test

# Generated at 2022-06-13 18:09:23.615196
# Unit test for method shift of class Parser
def test_Parser_shift():
    def check(type, value, newstate, context, node, exp_dfa, exp_state, exp_node):
        p.shift(type, value, newstate, context)
        subs = {
            "type": type,
            "value": value,
            "newstate": newstate,
            "context": context,
            "node": node,
        }
        assert (p.stack[-1] == (exp_dfa, exp_state, exp_node))
    p = Parser(None)
    dfa = 0
    state = 1
    node = (2, 3, 4, 5)
    newstate = 6
    type = 7
    value = "value"
    context = Context(0)
    exp_dfa = dfa
    exp_state = newstate

# Generated at 2022-06-13 18:09:35.083069
# Unit test for method pop of class Parser
def test_Parser_pop():
    from blib2to3.pgen2 import driver

    grammar = driver.load_grammar(r'..\blib2to3\Grammar.txt', 'Grammar.txt')
    p = Parser(grammar)
    assert not p.stack
    dfa = [0, 1, 0, -1, 2, 0]
    p.stack.append((dfa, 0, (1, None, None, None)))
    p.stack.append((dfa, 1, (2, None, None, None)))
    p.pop()
    assert not p.stack


# Add test case for method addtoken of class Parser

# Generated at 2022-06-13 18:09:46.936745
# Unit test for method classify of class Parser
def test_Parser_classify():
    from blib2to3.pgen2.pgen import token
    from . import tokenize
    from . import grammar
    from . import driver

    tokenize.tokenprog = r"""
        from blib2to3.pgen2 import token
        from blib2to3.pgen2.tokenize import generate_tokens, untokenize, TokenInfo
        def tokenize(readline, tokeneater=None):
            if tokeneater is None:
                tokeneater = TokenInfo
            generate_tokens(readline, tokeneater)
        """

    driver.driver()
    g = grammar.grammar
    t = token.tok_name

    parser = Parser(g)
    parser.setup()
    # check special case of NAME

# Generated at 2022-06-13 18:09:54.336477
# Unit test for method shift of class Parser
def test_Parser_shift():
    import pprint, pgen2.pgen
    import pgen2.parse, pgen2.token, pgen2.tokenize

    grammar = pgen2.pgen.parse_grammar(test_grammar)
    parser = pgen2.parse.Parser(grammar)
    parser.setup()
    input = ["id", "(", "id", ")"]

    def tokenize():
        for x in input:
            yield pgen2.tokenize.Token(pgen2.token.NAME, x)
        yield pgen2.tokenize.Token(pgen2.token.ENDMARKER, "")

    for t in tokenize():
        parser.addtoken(t.type, t.string, (1, 0)) # pragma: no cover
    pprint.pprint(parser.rootnode.children)



# Generated at 2022-06-13 18:09:58.843280
# Unit test for method shift of class Parser
def test_Parser_shift():
    dfa = [[(0, 1)]], {}
    stack = [(dfa, 0, -1)]
    def convert(grammar, node):
        return node
    parser = Parser(None, convert)
    parser.stack = stack
    parser.shift(1, 2, 1, 3)
    assert stack == [(dfa, 1, -1)]
