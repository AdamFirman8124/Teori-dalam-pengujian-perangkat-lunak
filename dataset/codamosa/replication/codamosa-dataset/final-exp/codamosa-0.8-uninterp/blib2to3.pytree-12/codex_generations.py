

# Generated at 2022-06-13 18:14:53.782026
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    s = u"""a\n"""
    tree = compile(s, "<>", "exec", _ast.PyCF_ONLY_AST)
    assert str(tree.get_suffix()) == "\\n"
    for node in tree.leaves():
        if node.prefix == "\\n":
            assert str(node.get_suffix()) == ""
    assert str(tree.children[0].get_suffix()) == "\\n"
    assert str(tree.children[0].children[0].get_suffix()) == "\\n"
    assert str(tree.children[0].children[0].children[0].get_suffix()) == ""



# Generated at 2022-06-13 18:15:06.457989
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    def method_leaves_test(self, tmp_path_factory):
        """Unit test for method leaves of class Leaf"""
        l1 = Leaf(1, "TEXT", prefix="A", fixers_applied=[], context=(1, 2))
        itr = l1.leaves()
        assert itr.__class__.__name__ == "generator"
        assert next(itr) is l1
        try:
            next(itr)
            assert False, "StopIteration not thrown"
        except StopIteration:
            pass
    method_leaves_test(Leaf, None)


# Generated at 2022-06-13 18:15:13.455951
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pgen2.driver import Driver
    from .pgen2.parse import parse_grammar

    source = Grammar()
    source.parse('a: "a"; b: "b"; c: "c"; d: "d";')
    ast = parse_grammar(source, '', '', Driver())
    pat = NodePattern(ast.symbol2number["b"], "b")

    res = [x[1] for x in pat.generate_matches(ast.node.children)]
    assert len(res) == 1, res



# Generated at 2022-06-13 18:15:15.367057
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    from pgen2.pgen import BasePattern
    from .pgen2.driver import Driver


# Generated at 2022-06-13 18:15:26.375852
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    """
    Test method match_seq of class WildcardPattern
    """
    np = NodePattern
    wp = WildcardPattern
    from program_synthesis.karel.dataset.parse import from_program
    from program_synthesis.karel.dataset.parse import parse
    from program_synthesis.karel.dataset.parser_util import ParserBase
    s = """4 2
    move
    pickbeeper
    turnoff
    """
    p = parse(s, ParserBase())
    root = from_program(p)
    assert (1, {}) == tuple(tuple(wp(name='bare_name').match_seq(root)))
    del s, p, root


# Generated at 2022-06-13 18:15:33.072576
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    print("test_BasePattern_match")
    b = BasePattern()
    assert b._submatch(b) == False
    b.type = 42
    assert b._submatch(b) == False
    b.content = 1
    assert b._submatch(b) == False
    assert b.match(b) == False
    assert b.match_seq([b]) == False
    assert b.generate_matches([b]) == []
    assert not list(b.generate_matches([]))
    assert repr(b) == "BasePattern(42, 1, None)"
    b.name = "foo"
    assert repr(b) == "BasePattern(42, 1, 'foo')"
    b2 = BasePattern()
    assert b != b2
    b.type = None
    assert b.type is None

# Generated at 2022-06-13 18:15:43.375822
# Unit test for function generate_matches
def test_generate_matches():
    head = NamePattern("head")
    tail = NamePattern("tail")
    tail_any = WildcardPattern(content=[(tail,)], min=0, max=HUGE)

    # Check that an empty pattern matches an empty sequence of nodes
    assert list(generate_matches([], [])) == [(0, {})]

    # Check that an empty pattern doesn't match a non-empty sequence of nodes
    assert list(generate_matches([], ["a"])) == []

    # Check that a non-empty pattern doesn't match an empty sequence of nodes
    assert list(generate_matches([tail], [])) == []
    assert list(generate_matches([NodePattern()], [])) == []
    assert list(generate_matches([tail_any], [])) == []

    # Check that a single pattern matches a single node
   

# Generated at 2022-06-13 18:15:49.851128
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    from pprint import pprint
    from . import ast
    from io import StringIO
    from .parse import Parser

    p = Parser(ast)
    pat = p.pattern('(a b)* !(a b c)')

    def eq(nodes, expected):
        got = list(pat.generate_matches(nodes))
        if got == expected:
            print("ok, got")
            pprint(got)
        else:
            print("*** ERROR")
            print("got")
            pprint(got)
            print("but expected")
            pprint(expected)

    # Test empty pattern
    eq([], [(0, {})])
    eq([ast.Leaf("a", 1), ast.Leaf("b", 2)], [(0, {})])

# Generated at 2022-06-13 18:15:53.616643
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    leaf1 = Leaf(1, "1")
    leaf2 = Leaf(2, "2")
    node3 = Node(1, [leaf1, leaf2])

    assert list(leaf1.leaves()) == [leaf1]
    assert list(node3.leaves()) == [leaf1, leaf2]

# Generated at 2022-06-13 18:16:01.813026
# Unit test for method post_order of class Node
def test_Node_post_order():
    from .pytree import Leaf, Node
    from .pygram import python_symbols
    import unittest
    from . import fixer_util

    class TestNode(unittest.TestCase):

        def test_post_order(self):
            node = Node(python_symbols.funcdef,
                [Leaf(token.NAME, "def"), Leaf(token.NAME, "f"),
                 Node(python_symbols.parameters,
                     [Leaf(token.LPAR, "("), Leaf(token.RPAR, ")")]),
                 Node(python_symbols.suite, [Leaf(token.NEWLINE, "\n")])])

# Generated at 2022-06-13 18:16:25.535292
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import unittest
    import test.test_lib2to3 as test_lib2to3
    from .pgen2 import driver

    class TestPattern(test_lib2to3.TestCase):

        grammar = r"""
        x: ;
        """

        def test_generate_matches(self):
            r = driver.parse_string(self.grammar)
            p = r.pattern
            n = r.root
            self.assertEqual(list(p.generate_matches([n])), [(1, {})])

    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        unittest.main()

# Generated at 2022-06-13 18:16:28.652363
# Unit test for constructor of class NodePattern
def test_NodePattern():
    p = NodePattern()
    p = NodePattern(type=256)
    p = NodePattern(type=256, content=(LeafPattern(type=1),))
    p = NodePattern(type=256, content=[LeafPattern(type=1)])



# Generated at 2022-06-13 18:16:31.578572
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Leaf, Internal
    t = Internal("", [Leaf("x", "NAME"), Leaf("=", "EQUAL"), Leaf("1", "NUMBER")])
    assert t.depth() == 0
    t2 = Internal("", [t])
    assert t2.depth() == 1


# Generated at 2022-06-13 18:16:35.351937
# Unit test for constructor of class NodePattern
def test_NodePattern():
    pattern = NodePattern(
        type=1,
        content=(
            WildcardPattern(),
            LeafPattern(1, "")
        ),
        name='test'
    )
    print(repr(pattern))
    assert pattern.wildcards == True
    assert pattern.type == 1
    assert pattern.content == [
        WildcardPattern(),
        LeafPattern(1, "")
    ]
    assert pattern.name == 'test'


# Generated at 2022-06-13 18:16:38.907785
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    leaf = Leaf(1, "value_foo")
    x = leaf.leaves()
    assert x.__next__() is leaf
    with pytest.raises(StopIteration):
        x.__next__()



# Generated at 2022-06-13 18:16:42.916443
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    l = Leaf(3, "test")
    leaf_list = list(l.post_order())
    assert leaf_list == [l]


# Generated at 2022-06-13 18:16:47.482746
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    import pickle; from cgrammar import cgrammar

    def optimize(p, expected_p=None, expected_str=None):
        p = WildcardPattern(*p)
        p = p.optimize()
        if expected_p is not None:
            p2 = WildcardPattern(*expected_p).optimize()
            assert pickle.loads(pickle.dumps(p)) == pickle.loads(
                pickle.dumps(p2)
            ), repr(p) + " vs " + repr(p2)
        if expected_str is not None:
            assert str(p) == expected_str
    optimize((None, 1, 1), (None, 1, 1))
    optimize(((None, 1, 1),), ((None, 1, 1),))

# Generated at 2022-06-13 18:17:02.401030
# Unit test for method remove of class Base
def test_Base_remove():
    class Leaf2(Leaf):
        """Test Leaf for node parse."""

        def _eq(self, other: "Leaf2") -> bool:
            return self.type == other.type

    class Node2(Node):
        """Test Node for node parse."""

        def _eq(self, other: "Node2") -> bool:
            return self.type == other.type and self.children == other.children

    node0 = Node2(0, [Leaf2(1), Leaf2(2), Leaf2(3)])
    node0.remove()
    assert node0.parent is None

    node1 = Node2(4, [Leaf2(5), Leaf2(6)])
    node0.replace(node1)
    assert node1.parent is None
    assert node0.parent is None


# Generated at 2022-06-13 18:17:12.321730
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(0) == 0
    assert type_repr(python_symbols.integer) == "integer"


# Terminals are named by int; they're just unique IDs.
# Nonterminals are named by str.
# Not used in the pattern matching code, only in the parser code in pgen2.py.
NUMBER = 1
STRING = 2
NAME = 3
NEWLINE = 4
INDENT = 5
DEDENT = 6
LPAR = 7
RPAR = 8
LSQB = 9
RSQB = 10
COLON = 11
COMMA = 12
SEMI = 13
PLUS = 14
MINUS = 15
STAR = 16
SLASH = 17
VBAR = 18
AMPER = 19
LESS = 20
GREATER = 21
EQUAL = 22
DOT = 23
PERCENT = 24

# Generated at 2022-06-13 18:17:21.295838
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    p = NegatedPattern(NodePattern(type=token.NAME, content=[LeafPattern(value="hello")]))
    assert list(p.generate_matches([Leaf(token.NAME, "foo")])) == [(0, {})]
    assert list(p.generate_matches([Leaf(token.NAME, "hello")])) == []
    assert list(p.generate_matches([])) == [(0, {})]
    q = NegatedPattern()
    assert list(q.generate_matches([Leaf(token.NAME, "foo")])) == []
    assert list(q.generate_matches([])) == [(0, {})]

# Generated at 2022-06-13 18:17:55.568486
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    pattern = WildcardPattern([[Leaf(tokenize.NAME, 'a')]])
    node = Leaf(tokenize.NAME, 'a')
    assert tuple(pattern.generate_matches([node])) == ((1, {}),)
    assert tuple(pattern.generate_matches([node, node])) == ((2, {}),)



# Generated at 2022-06-13 18:18:07.389422
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    import sys, _ast
    # Create the following tree:
    # 1
    # |\
    # 2 3
    # |
    # 4
    # |\
    # 5 6
    # |\
    # 7 8
    # |\
    # 9 10
    node1 = Node(grammar.syms.file_input, [])
    node2 = Leaf(grammar.tokens.NAME, 'abc', (1, 0))
    node3 = Leaf(grammar.tokens.NAME, 'foo', (2, 0))
    node4 = Node(grammar.syms.funcdef, [])
    node5 = Leaf(grammar.tokens.NAME, 'def', (3, 0))
    node6 = Leaf(grammar.tokens.NAME, 'foo', (3, 4))

# Generated at 2022-06-13 18:18:22.157002
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    from io import StringIO
    from lib2to3.pytree import Leaf as T
    from lib2to3.pytree import Node as N
    from lib2to3.pgen2.tokenize import generate_tokens, untokenize
    untok = untokenize

    t = T(1, "foo")
    u = T(1, "foo")
    assert t == u, (t, u)

    v = T(1, "bar")
    assert t != v, (t, v)

    # Make sure it works on Nodes too
    foo = N(1, [T(1, "foo")])
    bar = N(1, [T(1, "bar")])
    if False:
        foo = N(1, [T(1, "foo")])

# Generated at 2022-06-13 18:18:30.603218
# Unit test for method leaves of class Base
def test_Base_leaves():
    """Test the leaves method of class Base"""

    class TestNode(Base):
        """A dummy subclass of the Base class"""

        def __init__(self, children):
            Base.__init__(self)
            self.children = children

        def __eq__(self, other):
            if not isinstance(other, TestNode):
                return False
            if self.children == other.children:
                return True
            return False

        def clone(self):
            """Clone function for TestNode"""
            return TestNode(self.children)

        def pre_order(self):
            """Preorder implementation for TestNode"""
            yield self
            for child in self.children:
                yield from child.pre_order()

        def post_order(self):
            """Postorder implementation for TestNode"""

# Generated at 2022-06-13 18:18:47.687963
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from . import pytree
    from . pytree import (
        Leaf,
        Node,
        type_repr,
    )

    def _type_repr(type_num: int) -> Text:
        return type_repr(type_num)

    
    
    
    
    
    
    # VarDecl(identifier type_name, Leaf(token.INDENT, '    '), Container(
    #     simple_stmt,
    #     Leaf(token.INDENT, '    '),
    #     comment,
    #     simple_stmt,
    #     comment,
    # ))
    #
    # VarDecl(identifier type_name)
    # |- Leaf(token.INDENT, '    ')
    # |- Container(
    # |   simple_stmt,
    #

# Generated at 2022-06-13 18:18:57.411465
# Unit test for method remove of class Base
def test_Base_remove():
    parents = []

    class Node(Base):
        def __init__(self, typ, children=None):
            self.type = typ
            self.children = children or []

        def pre_order(self):
            for child in self.children:
                yield from child.pre_order()

        def clone(self):
            new = Node(self.type)
            for child in self.children:
                new.append_child(child.clone())
            return new

        def append_child(self, child):
            child.parent = self
            self.children.append(child)

        def _eq(self, other):
            if self.type != other.type:
                return False
            if len(self.children) != len(other.children):
                return False

# Generated at 2022-06-13 18:18:59.911786
# Unit test for method clone of class Base
def test_Base_clone():
    # TODO: Test here
    ...



# Generated at 2022-06-13 18:19:08.000444
# Unit test for method replace of class Base
def test_Base_replace():
    Base.parent = None
    Tree.parent = None
    Leaf.parent = None
    assert Base.parent is None
    assert Tree.parent is None
    assert Leaf.parent is None

    Base.children = None
    Tree.children = None
    Leaf.children = None
    assert Base.children is None
    assert Tree.children is None
    assert Leaf.children is None

    Base.was_changed = False
    Tree.was_changed = False
    Leaf.was_changed = False
    assert Base.was_changed == False
    assert Tree.was_changed == False
    assert Leaf.was_changed == False

# Generated at 2022-06-13 18:19:16.630958
# Unit test for function type_repr
def test_type_repr():
    from .pygram import python_symbols
    from .pgen2 import token
    for name, val in python_symbols.__dict__.items():
        if type(val) == int:
            assert type_repr(val) == name
    for name, val in token.__dict__.items():
        if name[0:1] != "_" and type(val) == int:
            assert type_repr(val) == name

type_t = TypeVar("type_t", bound="Node")



# Generated at 2022-06-13 18:19:22.758738
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    pt = WildcardPattern(
        [
            [LeafPattern(type="foo"), LeafPattern(type="bar"), LeafPattern(type="spam")],
            [LeafPattern(type="ham")],
        ],
        min=1,
        max=3,
        name="test_name",
    )
    result = []
    for c, r in pt.generate_matches((Leaf("foo"), Leaf("bar"), Leaf("spam"))):
        assert c == 3
        assert r == {"test_name": [Leaf("foo"), Leaf("bar"), Leaf("spam")]}
        result.append(c)
    assert result == [3]
    result = []

# Generated at 2022-06-13 18:19:51.168590
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    """Unit test for method __eq__ of class Base"""
    import pytest
    from lib2to3.pgen2.pgen import Base

    base = Base()
    pytest.raises(NotImplementedError, base.__eq__, base)



# Generated at 2022-06-13 18:19:59.944096
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from .pytree import Leaf, Node
    from .python_grammar import spaces, symbol_map

    def _build_node(tokens):
        root = Node(symbol_map["file_input"], [])
        child = root
        daughter = None
        for token in tokens:

            if token == "{":
                assert daughter is not None
                daughter.append_child(Node(symbol_map["suite"], []))
                child = daughter.children[-1]
                daughter = None

            elif token == "}":
                child = child.parent

            elif isinstance(token, list):
                if daughter is not None:
                    daughter.append_child(Node(symbol_map[token[0]], []))
                    daughter = daughter.children[-1]

# Generated at 2022-06-13 18:20:02.618081
# Unit test for function type_repr
def test_type_repr():
    global _type_reprs
    _type_reprs = {}
    for i in range(200):
        assert type_repr(i) in ("", i)
    assert type_repr(1) == "NAME"
    assert type_repr(55) == 55



# Generated at 2022-06-13 18:20:04.129741
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    print (Node(python_symbols.power, [Leaf(3, "foo"), Leaf(3, "bar")]).pre_order())

# Generated at 2022-06-13 18:20:12.271988
# Unit test for method replace of class Base
def test_Base_replace():
    class A:
        def __init__(self):
            self.x = 1
        def __eq__(self, other):
            return self.x == other.x
        def clone(self):
            return A()

    class B(Base):
        def __init__(self, x):
            self.x = x
            self.parent = None
            self.children = []
        def __eq__(self, other):
            return self.x == other.x
        def clone(self):
            return B(self.x)

    x = B(1)
    y = B(2)
    z = B(3)
    x.parent = y
    y.children.append(x)
    y.children.append(z)

    x.replace(B(4))

# Generated at 2022-06-13 18:20:14.050798
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    assert BasePattern().optimize() is BasePattern()

# Generated at 2022-06-13 18:20:17.689216
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    leaf = Leaf(1, "foo")
    leafs = leaf.leaves()
    for l in leafs:
        assert l == leaf

# Generated at 2022-06-13 18:20:23.457865
# Unit test for method clone of class Node
def test_Node_clone():
    from .pygram import python_symbols as syms
    from .pytree import Leaf, Node

    n = Node(syms.simple_stmt, [Leaf(0, "a")])
    nc = n.clone()
    assert n is not nc
    assert n == nc

# Generated at 2022-06-13 18:20:31.850573
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    Node = pytree.Node  # noqa
    Leaf = pytree.Leaf  # noqa
    op = Leaf(0, '+')
    x = Leaf(0, 'x')
    y = Leaf(0, 'y')
    expr = Node(0, [x, op, y])
    expr.prefix = ' '
    expr_match = [
        ([x], 1, {}),
        ([op], 1, {}),
        ([y], 1, {}),
        ([x, op], 2, {}),
        ([x, op, y], 3, {}),
    ]
    for p, l, r in expr_match:
        assert expr.match_seq(p) == (l, r)
    op_pattern = LeafPattern(0, '+')

# Generated at 2022-06-13 18:20:36.351050
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import unittest.mock as mock
    inputs = [
        (1, 2, 3),
        (1, 2),
        (),
    ]
    for input1 in inputs:
        nodes = list(input1)
        bp = BasePattern()
        bp.match = mock.Mock()
        bp.match.return_value = True
        actual = tuple(bp.generate_matches(nodes))
        expected = ((1, {}),)
        assert actual == expected
        bp.match.assert_called_with(nodes[0])
        bp.match.reset_mock()


# Generated at 2022-06-13 18:21:15.151595
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    import pytest_astng; pytest_astng.setup_function()
    assert Base(None).pre_order() is None



# Generated at 2022-06-13 18:21:20.710110
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .pygram import python_symbols
    from .pgen import token

    grammar = Grammar(
        r"""
    x ::= "foo"*
    """,
        python_symbols,
        [],
    )
    root = from_grammar(grammar, "foo", token.COMMENT)
    node = root.children[0]
    assert list(node.pre_order()) == [node, node]



# Generated at 2022-06-13 18:21:25.887184
# Unit test for method replace of class Base
def test_Base_replace():
    from . import parse

    tree = parse.parse('x = 1 + 1')
    plus = tree.children[1]
    assert plus.children[1].prefix == ' '
    plus.replace(parse.Leaf(type=parse.token.PLUS, value='+', prefix=''))
    assert plus.children[1].prefix == ''

# Generated at 2022-06-13 18:21:37.512049
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    p = WildcardPattern(
        [
            [WildcardPattern(min=1, max=1), NodePattern(), LeafPattern(name="lit")],
            [WildcardPattern(min=1, max=1), NodePattern(name="any"), LeafPattern()],
        ],
        min=1,
        max=1,
        name="wild",
    )
    q = p.optimize()
    assert isinstance(q, WildcardPattern)
    assert q.content[0][0].min == 1
    assert q.content[0][0].max == 1
    assert isinstance(q.content[0][1], NodePattern)
    assert isinstance(q.content[0][2], LeafPattern)
    assert q.content[1][0].min == 1
    assert q.content[1][0].max == 1
   

# Generated at 2022-06-13 18:21:43.124149
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    p = NegatedPattern(NodePattern(type=1, content=["keyword"]))
    s = "keyword True = 1"
    nodes = parser.expr('"""%s"""').totuple(0)[1][1:-1]
    print(list(map(repr,nodes)))
    print(list(p.generate_matches(nodes)))
test_NegatedPattern_generate_matches()


# Generated at 2022-06-13 18:21:48.375890
# Unit test for method clone of class Node
def test_Node_clone():
    from .pytree import Leaf, Node
    from ..fixer_util import Name
    import sys
    s_print = sys.stdout.write
    s_input = __import__("sys").stdin.readline
    l = Leaf(1, "hello")
    s_print("Original l: " + str(l) + "\n")
    s_print("Clone c: " + str(l.clone()) + "\n")
    c = Node(2, [Leaf(3, "hello"), Leaf(3, "there")])
    s_print("Original c: " + str(c) + "\n")
    s_print("Clone c2: " + str(c.clone()) + "\n")

# Generated at 2022-06-13 18:21:58.132049
# Unit test for method clone of class Leaf
def test_Leaf_clone():
    l = Leaf(token.DOT, '.', fixers_applied=[])
    c = l.clone()
    assert c is not l
    assert c == l
    assert c.prefix == l.prefix
    assert c.fixers_applied == l.fixers_applied
    l.fixers_applied = l.fixers_applied + ['foo']
    assert c.fixers_applied != l.fixers_applied


# Generated at 2022-06-13 18:22:09.876930
# Unit test for method clone of class Base
def test_Base_clone():
    from unittest import TestCase
    import StringIO
    import tokenize

    class TestBase(TestCase):

        def setUp(self):
            self.text = "            # Comment\n"
            tokengen = tokenize.generate_tokens(StringIO.StringIO(self.text).readline)
            self.leaf = Leaf(type=tokenize.COMMENT, value='# Comment', context=(self.text, (0, 0)))
            self.leaf.depth = 0
            self.leaf.changed = lambda: None
            self.leaf.parent = None
            self.empty_node = Node(type=tokenize.DEDENT, children=[], context=(self.text, (0, 0)))
            self.empty_node.depth = 0
            self.empty_node.changed = lambda: None
            self

# Generated at 2022-06-13 18:22:22.929533
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .pytree import Node, Leaf

    class ExampleNode(Node):
        pass

    class ExampleLeaf(Leaf):
        pass

    a: Union[Node, Leaf] = ExampleNode(ExampleLeaf(ExampleLeaf(ExampleNode())))
    b: Union[Node, Leaf] = ExampleLeaf(ExampleNode(ExampleLeaf(ExampleLeaf())))
    c: Union[Node, Leaf] = ExampleNode(ExampleNode(b))

    assert a.pre_order() == [a, a.children[0], a.children[0].children[0], a.children[0].children[1], a.children[0].children[1].children[0], a.children[0].children[1].children[1]]