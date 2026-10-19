

# Generated at 2022-06-13 18:14:13.497620
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    from .pgen2.token import NAME

    n = Leaf(NAME, "foo", (0, 0))
    assert NodePattern(NAME).match(n)
    assert NodePattern(NAME, "foo").match(n)
    assert not NodePattern(NAME, "bar").match(n)



# Generated at 2022-06-13 18:14:23.643228
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pygram import python_symbols as syms
    from .pytree import Leaf, Node, bs, bso
    from .pgen2.parse import BasicParser

    parser = BasicParser()
    root = parser.parse_string("my_name = 'Sue'\n")

    root.children[0].children[0].prev_sibling = None
    assert root.children[0].children[0].get_suffix() == " "
    assert root.children[0].children[1].get_suffix() == " "
    assert root.children[0].children[2].get_suffix() == " "
    assert root.children[1].get_suffix() == "\n"


# Generated at 2022-06-13 18:14:33.920824
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    assert WildcardPattern().match_seq([])
    assert not WildcardPattern().match_seq(["a"])
    assert WildcardPattern().match_seq(["a"], {"a": ["a"]})
    p = WildcardPattern({"a", "b"})
    assert not p.match_seq([])
    assert not p.match_seq(["a", "c"])
    assert p.match_seq(["a", "b", "a", "b"], {"a": ["a", "b", "a", "b"]})
    assert not p.match_seq(["a", "b", "a", "b", "c"])
    p = WildcardPattern({"a", "b"}, min=1)
    assert not p.match_seq([])

# Generated at 2022-06-13 18:14:36.632252
# Unit test for method depth of class Base
def test_Base_depth():
    fld = _flatten(s_stmt)
    assert fld[1].depth() == 1
    assert fld[2].depth() == 2

# Generated at 2022-06-13 18:14:47.124802
# Unit test for method replace of class Base
def test_Base_replace():
    from .pgen2 import tokenize
    from .pytree import Leaf, Node, Base, type_repr

    source = """
        # This program doesn't do anything at all.
        a = 3 # I'm going to set the constant "a" to 3.
    """
    for node in tokenize.detokenize(list(tokenize.generate_tokens(StringIO(source).readline))):
        assert isinstance(node, Base)
    module = Node(python_symbols.file_input, [])
    a = Leaf(token.NAME, "a")
    a.parent = module
    module.children = [a]
    a.replace(Leaf(token.NAME, "b"))
    assert module.children[0].type == token.NAME
    assert module.children[0].value == "b"

# Generated at 2022-06-13 18:14:54.486027
# Unit test for method __repr__ of class Node
def test_Node___repr__():
    Node_0 = Node(256, [])
    Node_0.type = 256
    Node_0.children = []
    assert repr(Node_0) == "Node(NAME, [])"

    Node_1 = Node(257, [])
    Node_1.type = 257
    Node_1.children = []
    assert repr(Node_1) == "Node(NUMBER, [])"

    Node_2 = Node(258, [])
    Node_2.type = 258
    Node_2.children = []
    assert repr(Node_2) == "Node(STRING, [])"

    Node_3 = Node(259, [])
    Node_3.type = 259
    Node_3.children = []
    assert repr(Node_3) == "Node(NEWLINE, [])"

    Node_4

# Generated at 2022-06-13 18:15:09.073810
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    test_node = Node(
        257,
        [
            Leaf(token.NAME, "a", prefix=" "),
            Leaf(token.EQUAL, "=", prefix=" "),
            Leaf(token.NAME, "b", prefix=" "),
        ],
    )
    assert test_node.type == 257
    assert [x.value for x in test_node.leaves()] == ["a", "=", "b"]
    assert [x.value for x in test_node.post_order()] == ["a", "=", "b"]
    assert [x.value for x in test_node.pre_order()] == ["a", "=", "b"]
    assert test_node == test_node
    assert test_node.prefix == " "

# Generated at 2022-06-13 18:15:16.890255
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    import pytree
    root = pytree.Node(0, [pytree.Node(1, []), pytree.Node(2, [])])
    i = root.pre_order()
    assert next(i) == root
    assert next(i) == root.children[0]
    assert next(i) == root.children[1]
    assert list(i) == []

# Generated at 2022-06-13 18:15:30.282810
# Unit test for method clone of class Base
def test_Base_clone():
    """Unit test for method clone of class Base."""
    r = Leaf(0, "")
    r.children = [Leaf(0, "")]
    r.children[0].children = [Leaf(0, "")]
    assert r.clone() is not r
    assert r.children[0].clone() is not r.children[0]
    assert r.children[0].children[0].clone() is not r.children[0].children[0]
    assert r.clone().children[0].children[0].clone() == r.children[0].children[0]
    return



# Generated at 2022-06-13 18:15:41.757046
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    from .pytree import Leaf, Node
    from .pygram import python_symbols as syms
    def get_lineno(node: Node, prefix: Text = 'prefix') -> str:
        return str(node.get_lineno())
    expr = Node(syms.testlist, [Leaf(1, '1')])
    expr.set_line_info(2, 3)
    assert get_lineno(expr) == '2'
    expr = Node(syms.testlist, [expr])
    assert get_lineno(expr) == '2'
    expr = Node(syms.testlist, [Leaf(1, '1'), expr])
    assert get_lineno(expr) == 'None'
    expr = Node(syms.power, [Leaf(1, '1'), expr])
    expr

# Generated at 2022-06-13 18:16:47.700358
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    tree = Leaf(type = 10, value = "1.0", context = None, prefix = None, fixers_applied = [])
    iterator = tree.leaves()
    assert next(iterator) == tree
    #Generator should have been exhausted
    with raises(StopIteration):
        next(iterator)

# Generated at 2022-06-13 18:16:50.940623
# Unit test for method clone of class Base
def test_Base_clone():
    b = Base()
    assert not b.clone(), "Need to define Base.clone()"



# Generated at 2022-06-13 18:16:58.595685
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    import ast_parse
    import ast_matcher
    root = ast_parse.parse("1+1")
    p = ast_matcher.ASTMatcher()
    pat = p.parse("(expr(expr(NUMBER) '+' expr(NUMBER)))")
    p = NegatedPattern(pat)
    assert list(p.generate_matches(root.children)) == [(0, {})]
 


# Generated at 2022-06-13 18:17:10.324732
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    t = Symbol("test")
    m = Symbol("match")
    p1 = WildcardPattern([[Leaf(1, "a"), Leaf(2, "b")]])
    p2 = WildcardPattern([[t, m]])
    assert not p1.match_seq([])
    assert not p1.match_seq([Leaf(1, "a")])
    assert not p1.match_seq([Leaf(2, "c")])
    assert not p1.match_seq([Leaf(2, "b")])
    assert p1.match_seq([Leaf(1, "a"), Leaf(2, "b")])
    assert not p1.match_seq([Leaf(1, "a"), Leaf(2, "b"), Leaf(3, "c")])

# Generated at 2022-06-13 18:17:19.433269
# Unit test for function convert
def test_convert():
    from .pgen2.parse import load_grammar

    gr = load_grammar("Grammar.txt")
    l = gr.leaf("foo", "bar")
    r = convert(gr, (gr.symbol2number["foo"], "bar", 123, [l]))
    assert r is l
    r = convert(gr, (gr.symbol2number["foo"], "bar", 123, []))
    assert isinstance(r, Leaf)
    assert r.type == gr.symbol2number["foo"]
    assert r.value == "bar"
    r = convert(gr, (gr.symbol2number["stmt"], None, 123, [l]))
    assert isinstance(r, Node)
    assert r.type == gr.symbol2number["stmt"]
    assert r.children == [l]

# Generated at 2022-06-13 18:17:30.314671
# Unit test for method post_order of class Node
def test_Node_post_order():
    test = """
N(
  N(SYM(1)): N(N(SYM(1)), N(SYM(2))
  N(SYM(3))
)
"""

    class N(Node):
        def pref(self):
            return ""
    t = compile_tree(test, N)
    assert list(t.post_order()) == [t.children[0].children[1], t.children[0].children[0],
        t.children[0], t.children[1], t]
    assert list(t.pre_order()) == [t, t.children[0], t.children[0].children[0],
        t.children[0].children[1], t.children[1]]
    assert t.type == 1

# Generated at 2022-06-13 18:17:32.989962
# Unit test for method post_order of class Node
def test_Node_post_order():
    root = Node(1, [Leaf(1, 'a'), Node(2, [Leaf(3, 'b')]), Leaf(4, 'c')])
    assert [l.value for l in root.post_order()] == ['a', 'b', 'c']



# Generated at 2022-06-13 18:17:36.163932
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from pprint import pprint
    stmt = tree.stmt
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    stmt.append(x)
    stmt.append(y)
    stmt.append(z)
    for n in stmt.pre_order():
        pprint(n)



# Generated at 2022-06-13 18:17:41.856413
# Unit test for constructor of class NodePattern
def test_NodePattern():
    from . import parsetok

    # pylint: disable=unused-variable
    # The following variables are used in a test case
    # A class that does not know about these variables
    # will raise a false positive warning.
    for content_args in ({}, {None}, {None, None}, {"a"}, {"a", "b"}):
        # Reject strings as content (only leaf pattern may have
        # string content)
        content_nodes: Iterable[Text] = []
        for i in content_args:
            content_nodes.append(LeafPattern())
        fails = False
        try:
            NodePattern(256, content_nodes)
        except AssertionError:
            fails = True
        assert fails, "expected assertion"

        # Reject tokens as types (only leaf pattern may have
        # tokens as

# Generated at 2022-06-13 18:17:52.157655
# Unit test for method clone of class Node
def test_Node_clone():
    import lib2to3.pygram
    import lib2to3.pgen2.parse
    grammar = lib2to3.pgen2.parse.get_yapps_grammar(lib2to3.pygram, "file_input")

    nodes = lib2to3.pgen2.parse.make_parser(grammar).parse("1 + 1")
    cloned = nodes[0].clone()
    assert cloned == nodes[0]
    assert cloned is not nodes[0]
    assert cloned.children[1].clone() == nodes[0].children[1]
    assert cloned.children[1].clone() is not nodes[0].children[1]



# Generated at 2022-06-13 18:18:35.332823
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Leaf, Node

    def _gen_expected_results(parent):
        for child in parent.children:
            yield from _gen_expected_results(child)

    def _make_node_tree(num_children, depth):
        from .pytree import Leaf, Node

        if depth == 0:
            return Leaf(1, "")
        children = []
        for _ in range(num_children):
            children.append(_make_node_tree(num_children, depth - 1))
        return Node(1, children)

    def _check_expected_leaf(leaf):
        node = leaf
        while node.parent:
            node = node.parent
        leaves = node.leaves()
        assert next(leaves) == leaf

    # Test a tree with many levels

# Generated at 2022-06-13 18:18:40.195359
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    # Test with min = self.min, max = self.max
    for min in range(10):
        for max in range(min+1, min+10):
            for length in range(max+1):
                for repeat in range(length+1):
                    pattern = WildcardPattern(None, min, max)
                    nodes = [Node(0, [])]*repeat
                    matches = list(pattern.generate_matches(nodes))
                    if repeat < min:
                        assert matches == []
                    elif repeat > max:
                        assert matches == []
                    else:
                        assert len(matches) == 1
                        assert matches[0][0] == length
    # Make sure we can handle a zero-length min/max

# Generated at 2022-06-13 18:18:40.913216
# Unit test for method post_order of class Base
def test_Base_post_order():
    pass

# Generated at 2022-06-13 18:18:43.468088
# Unit test for method clone of class Base
def test_Base_clone():
    b = Base()
    assert not b.parent
    cloned = b.clone()
    assert cloned.parent is None


# Generated at 2022-06-13 18:18:49.809330
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    n1 = Builder.build_atom("(")
    assert n1.type == token.LPAR
    p1 = Builder.build_leaf_pattern(token.LPAR)
    assert p1.type == token.LPAR
    assert list(p1.generate_matches([n1])) == [(1, {})]
    assert list(p1.generate_matches([n1, n1])) == [(1, {})]
    assert list(p1.generate_matches([n1, n1, n1])) == [(1, {})]
    assert list(p1.generate_matches([Builder.build_atom("+")])) == []
    assert list(p1.generate_matches([])) == []

# Generated at 2022-06-13 18:18:58.621099
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    l = Leaf(1, 'aaaaaaaaa')
    # WildcardPattern(None) == NodePattern()
    assert WildcardPattern().optimize() == NodePattern()
    assert WildcardPattern(name='bare_name').optimize() == WildcardPattern(name='bare_name')
    # WildcardPattern(min=0, max=HUGE, content=None)
    # == WildcardPattern(min=1, max=HUGE, content=None)
    assert WildcardPattern().optimize() == WildcardPattern(min=1)
    # WildcardPattern(min=1, max=2, content=None)
    # == WildcardPattern(min=1, max=1, content=None)
    assert WildcardPattern(min=1, max=2).optimize() == WildcardPattern(min=1, max=1)
    #

# Generated at 2022-06-13 18:19:01.529464
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    leaf = Leaf(3, "bbb")
    post_order = list(leaf.post_order())
    assert len(post_order) == 1
    assert post_order[0] is leaf #check that post_order returns leaf itself


# Generated at 2022-06-13 18:19:04.544035
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    l = Leaf(1, 'a')
    assert list(l.pre_order())[0] == l



# Generated at 2022-06-13 18:19:05.770171
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    leaf = Leaf(255, "a_value")
    assert list(leaf.post_order()) == [leaf]



# Generated at 2022-06-13 18:19:14.171742
# Unit test for method post_order of class Base
def test_Base_post_order():
    class Concrete(Base):
        type: int
        prefix: Text
        value: Text
        parent: Optional[Node]
        children: List[NL]
        was_changed: bool = False
        was_checked: bool = False

        def __init__(self, type, value, context):
            self.type = type
            self.value = value
            self.context = context
            self.children = []
            self.parent = None

        def __str__(self):
            return "%s(%s)" % (type_repr(self.type), self.value)

        @property
        def prefix(self):
            return TypeError

        def clone(self):
            return NotImplementedError

        def _eq(self, other):
            return NotImplementedError


# Generated at 2022-06-13 18:19:42.799496
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    _pattern = BasePattern()
    _pattern.optimize()
    _pattern = BasePattern(type=10)
    _pattern.optimize()



# Generated at 2022-06-13 18:19:48.429638
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pgen2 import driver

    d = driver.Driver()
    g = d.build_grammar((), ())
    lp = LeafPattern(token.NAME)
    t1 = Leaf(token.NAME, "name", prefix="")
    t2 = Leaf(token.NAME, "NAME", prefix="")
    t3 = Leaf(token.NAME, "Name", prefix="")
    t4 = Leaf(token.NAME, "namE", prefix="")
    t5 = Leaf(token.NAME, "NAME", prefix="")
    t6 = Leaf(token.NAME, "nam", prefix="")
    t7 = Leaf(token.NAME, "Name1", prefix="")
    t8 = Leaf(token.NAME, "name", prefix="")
    t9 = Leaf(token.NAME, "name", prefix="")


# Generated at 2022-06-13 18:19:57.501834
# Unit test for method leaves of class Base
def test_Base_leaves():
    l1 = Leaf(1, "l1")
    l2 = Leaf(2, "l2")
    l3 = Leaf(3, "l3")
    l4 = Leaf(4, "l4")
    n1 = Node(5, [l1, Node(6, [l2, Node(7, [l3]), l4])])
    l5 = Leaf(0, "l5")
    n2 = Node(8, [n1, l5])
    leaves = list(n2.leaves())
    assert len(leaves) == 5
    assert leaves[0] is l1
    assert leaves[1] is l2
    assert leaves[2] is l3
    assert leaves[3] is l4
    assert leaves[4] is l5



# Generated at 2022-06-13 18:20:04.209980
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    # test Base.__eq__
    # base is abstract so we use Node
    parser = Grammar()
    s = StringIO("1 = 1")
    tree = parser.parse_stream(s)
    # test the elements in a simple tree are all equal to those from the same
    # tree
    assert tree == tree
    assert tree.children[0] == tree.children[0]
    if tree.children:
        assert tree.children[0] == tree.children[0]
        assert tree.children[0].children[0] == tree.children[0].children[0]
    # test non equal trees are non equal
    s2 = StringIO("1 = 2")
    tree2 = parser.parse_stream(s2)
    assert tree != tree2

# Generated at 2022-06-13 18:20:09.513439
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    o = BasePattern()

    o = BasePattern(1)
    assert repr(o) == "BasePattern(1)"
    o = BasePattern(1, None)
    assert repr(o) == "BasePattern(1, None)"
    o = BasePattern(1, None, None)
    assert repr(o) == "BasePattern(1, None, None)"

    o = BasePattern(1, 2)
    assert repr(o) == "BasePattern(1, 2)"
    o = BasePattern(1, 2, None)
    assert repr(o) == "BasePattern(1, 2, None)"

    o = BasePattern(1, 2, "abc")
    assert repr(o) == "BasePattern(1, 2, 'abc')"



# Generated at 2022-06-13 18:20:13.252542
# Unit test for method post_order of class Base
def test_Base_post_order():
    print('test_Base_post_order...')
    #
    # Method post_order of class Base is not implemented


# Generated at 2022-06-13 18:20:24.738608
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    r"""Unit test for method pre_order of class Base."""

    from __future__ import annotations

    import unittest

    from typing import Iterator

    from lib2to3 import pytree
    from lib2to3.pgen2 import driver, token

    class BasicTest(unittest.TestCase):
        def test_pre_order(self) -> None:
            grammar = driver.load_grammar("Grammar.txt", convert=True)
            tree = pytree.Leaf(token.NAME, "foo", (1, 0))
            p = grammar.p_file_input_start(tree)
            self.assertEqual(
                list(  # type: ignore
                    p.pre_order()
                ),
                [p, tree],
            )


# Generated at 2022-06-13 18:20:32.359285
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    test_pattern = NegatedPattern(None)
    assert not test_pattern.match_seq( [0] )
    assert not test_pattern.match_seq( [0, 1] )
    assert test_pattern.match_seq( [] )
    
    test_pattern = NegatedPattern(NodePattern(type=1))
    assert not test_pattern.match_seq( [0] )
    assert not test_pattern.match_seq( [0, 1] )
    assert not test_pattern.match_seq( [0, 1, 2] )
    assert test_pattern.match_seq( [] )
    assert test_pattern.match_seq( [1] )
    
    altTemplate = WildcardPattern(((NodePattern(type=2), ), ))
    test_pattern = NegatedPattern(altTemplate)
    assert not test_

# Generated at 2022-06-13 18:20:43.672043
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    # test class Base
    # This is the node type for whole numbers.
    class NUMBER(Leaf):
        __slots__ = 'tok', 'value', 'lineno', 'column'

    def Node(type_, children=None, lineno=None, column=None, prefix=''):
        if children is None:
            children = []
        n = Node(type_, children, prefix)
        if lineno is not None:
            n.lineno = lineno
        if column is not None:
            n.column = column
        return n

    lineno = NUMBER(0, '1', (1, 0), (1, 1), '')
    assert lineno.get_lineno() == 1

    lineno = Leaf(0, '1', (1, 0), (1, 1), '')

# Generated at 2022-06-13 18:20:47.164702
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.NAME) == "NAME"
    assert type_repr(python_symbols.test_token) == "test_token"
    assert type_repr(python_symbols.test_token+1) == python_symbols.test_token+1



# Generated at 2022-06-13 18:21:45.790377
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from . import pytree as py

    t = py.parse("""a + b\n""", mode='exec')
    print(type(t.next_sibling), t.next_sibling)
    print(type(t.children[0].next_sibling), t.children[0].next_sibling)
    print(type(t.children[1].next_sibling), t.children[1].next_sibling)
    print(type(t.children[1].children[0].next_sibling), t.children[1].children[0].next_sibling)

    assert t.children[0].get_suffix() == " + "
    assert t.children[1].get_suffix() == ""
    assert t.children[1].children[0].get_suffix() == ""
    # etc.

# Generated at 2022-06-13 18:22:00.335610
# Unit test for method __eq__ of class Base
def test_Base___eq__():

    class TestBase(Base):
        def __init__(self, val: int) -> None:
            self.val = val

        def _eq(self, other):
            return hasattr(other, 'val') and self.val == other.val

        def clone(self):
            return TestBase(self.val)

        def post_order(self):
            yield self

        def pre_order(self):
            yield self

    n1 = TestBase(1)
    n2 = TestBase(1)
    n3 = TestBase(2)

    assert n1 == n1
    assert n1 == n2
    assert not n1 != n2
    assert n2 != n3

    # Method __eq__ may not be defined for other classes

# Generated at 2022-06-13 18:22:05.134238
# Unit test for method clone of class Base
def test_Base_clone():
    """Test that Base.clone raises an exception."""
    class B(Base):
        def _eq(self, other):
            return True
        def pre_order(self):
            yield self
        def post_order(self):
            yield self

    b = B()
    try:
        b.clone()
    except NotImplementedError:
        pass
    else:
        assert False



# Generated at 2022-06-13 18:22:15.750814
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    from .nodes import Node
    from .parser import Nonterminal

    def test(pattern, nodes):
        for c, r in pattern.generate_matches(nodes):
            if c == len(nodes):
                return True
        return False

    def test_false(pattern, nodes):
        return not test(pattern, nodes)

    # Test that the generator function actually works

    p = WildcardPattern()
    assert p.match_seq([])
    assert p.match_seq([Leaf(1, "1")])
    assert not p.match_seq([Leaf(1, "1"), Leaf(2, "2")])

    assert test(p, [])
    assert test(p, [Leaf(1, "1")])