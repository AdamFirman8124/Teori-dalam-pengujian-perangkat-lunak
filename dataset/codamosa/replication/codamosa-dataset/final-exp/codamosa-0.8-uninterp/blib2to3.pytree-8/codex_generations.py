

# Generated at 2022-06-13 18:13:45.974699
# Unit test for method clone of class Base
def test_Base_clone():
    pass

# Generated at 2022-06-13 18:13:48.883882
# Unit test for method __repr__ of class Leaf
def test_Leaf___repr__():
    from ..pgen2 import token
    l = Leaf(token.NAME, 'foo')
    assert repr(l) == "Leaf(NAME, 'foo')"


# Generated at 2022-06-13 18:13:57.039868
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    pattern = NegatedPattern()
    assert list(pattern.generate_matches([])) == [(0, {})], list(pattern.generate_matches([]))
    pattern = NegatedPattern(((LeafPattern('a'), ),))
    assert list(pattern.generate_matches(['b'])) == [(0, {})], list(pattern.generate_matches(['b']))
    pattern = NegatedPattern(((LeafPattern('a'), ), (LeafPattern('b'), )))
    assert list(pattern.generate_matches(['a'])) == [], list(pattern.generate_matches(['a']))
    assert list(pattern.generate_matches(['b'])) == [], list(pattern.generate_matches(['b']))

# Generated at 2022-06-13 18:13:57.878974
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    # todo implement test_Leaf_post_order()
    pass

# Generated at 2022-06-13 18:14:00.599886
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.NAME) == "NAME"
    assert type_repr(1) == 1
    assert python_symbols.NAME == 2

# --------------------------------------------------------------------
#
# Utility functions, macros; may be useful in other applications



# Generated at 2022-06-13 18:14:03.671288
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    l = Leaf(0, 'value', prefix='')
    assert next(l.leaves()) == l

# Generated at 2022-06-13 18:14:11.405804
# Unit test for method clone of class Base
def test_Base_clone():
    import sys
    import lib2to3

    # testing method clone of class Base
    node = lib2to3.pgen2.token.LBRACE()
    assert node.parent is None
    assert node.children == []
    assert node.was_changed == False
    assert node.was_checked == False
    assert node.type == 1
    assert node.prefix == "{ "
    # Workaround for 'mypy' error:
    #   Callable expected as 2nd argument to 'assertRaises' (got Type[Base])
    #   [mypy-error]
    try:
        node.test__eq__()  # type: ignore
    except NotImplementedError:
        pass
    except Exception as e:
        print("unexpected exception:", e)
        print(sys.exc_info())
        raise
   

# Generated at 2022-06-13 18:14:19.576072
# Unit test for method replace of class Base
def test_Base_replace():
    class NodeSub(Base):
        def __init__(self, type, parent):
            self.type = type
            self.parent = parent
            self.children = []

        def _eq(self, other):
            return self.type == other.type

        def clone(self):
            return NodeSub(self.type, None)

        def post_order(self):
            for child in self.children:
                yield from child.post_order()
            yield self

        def pre_order(self):
            yield self
            for child in self.children:
                yield from child.pre_order()

        def __repr__(self):
            return "NodeSub(%r)" % (self.type,)

    def _build_tree():
        n0 = NodeSub(0, None)

# Generated at 2022-06-13 18:14:25.435374
# Unit test for method remove of class Base
def test_Base_remove():
	# setup sample input
	node = Leaf(0,1,2,3)
	child = Leaf(0,1,2,3)
	node.children = [child]
	child.parent = node
	node.next_sibling = None
	node.prev_sibling = None
	child.parent = node
	child.next_sibling = node
	child.prev_sibling = node
	node.invalidate_sibling_maps()
	child.invalidate_sibling_maps()
	# run the test method
	node.remove()
	# check that the results are correct
	assert(node.parent is None)
	assert(node.children is None)
	assert(child.parent is None)
	assert(child.children is None)
	assert(node.next_sibling is None)
	

# Generated at 2022-06-13 18:14:31.490528
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pgen2 import token
    from .pytree import Leaf
    from .pygram import python_symbols as syms
    #
    #       if x:
    #           x = 3  # comment
    #       x = 4
    #
    ifleaf = Leaf(token.IF, "if")
    xleaf = Leaf(token.NAME, "x")
    colonleaf = Leaf(token.COLON, ":")
    #

# Generated at 2022-06-13 18:15:16.080072
# Unit test for constructor of class NodePattern
def test_NodePattern():
    n = NodePattern(type=1, content=[], name="foo")
    assert n.type == 1, n.type
    assert n.content == [], n.content
    assert n.name == "foo", n.name
    n = NodePattern(content=[])
    assert n.type is None, n.type
    assert n.content == [], n.content
    assert n.name is None, n.name
    n = NodePattern(content=LeafPattern())
    assert n.type is None, n.type
    assert n.content == [LeafPattern()], n.content
    assert n.name is None, n.name
    n = NodePattern(content=[LeafPattern(), WildcardPattern()])
    assert n.type is None, n.type

# Generated at 2022-06-13 18:15:18.858429
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    # Default implementation for non-wildcard patterns
    d = BasePattern()
    e = BasePattern()
    assert not d.match_seq([Node(1, [])], {})
    assert d.match_seq([Node(256, [])], {})
    assert not d.match_seq([Node(0, [])], {})
    assert e.match_seq([Node(0, [])], {})
    pass

# Generated at 2022-06-13 18:15:29.043424
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    #        10
    #      /    \
    #    20      30
    #    / \
    #   40  50
    #     / \
    #    60 70
    # Create a parse tree:
    # Pre-create the leaves of the tree
    n40 = Leaf(40, (40, 40))
    n50 = Leaf(50, (50, 50))
    n60 = Leaf(60, (60, 60))
    n70 = Leaf(70, (70, 70))
    n20 = Node(20, [n40, n50])
    n30 = Node(30, [])
    n10 = Node(10, [n20, n30])
    # Test that all the next_siblings are correct
    assert n20.next_sibling == n30, "next sibling of 20 is not 30"
   

# Generated at 2022-06-13 18:15:36.268127
# Unit test for method clone of class Base
def test_Base_clone():
    """Unit test for Base.clone

    Note: if you modify this function, you should also change the test in
    tests/test_node_classes.py.
    """
    class Node(Base):

        def __init__(self, type, parent, children):
            # type: (int, Optional[Node], List[NL]) -> None
            self.type = type
            self.parent = parent
            # Putting this in a list call triggers an optimization bug in
            # PyPy 2.6.0, so don't do that.
            self.children = children

        def _eq(self, other):
            # type: (Node) -> bool
            return (self.type, self.children) == (other.type, other.children)


# Generated at 2022-06-13 18:15:38.227154
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == "NAME"
    assert type_repr(HUGE) == HUGE



# Generated at 2022-06-13 18:15:44.171585
# Unit test for method set_child of class Node
def test_Node_set_child():
    """Test if a change on the parent of a node is reflected in the node."""
    # get the object to test
    node = parse_python3_post_comments(
        test_code='(a, b[1])', validate=False)
    # get a child
    child = node.children[0]
    # set the child's parent to something else
    child.parent = node.children[1]
    # check if the child's parent is the node
    assert child.parent != node

# Generated at 2022-06-13 18:15:45.833624
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    l1 = Leaf(1, 2)
    assert l1.post_order() == l1

# Generated at 2022-06-13 18:15:47.073260
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    r = NodePattern(1)
    assert r is r.optimize()


# Generated at 2022-06-13 18:15:52.595571
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    from .pgen2.grammar import Token

    assert LeafPattern(1).__repr__() == "LeafPattern(1)"
    assert LeafPattern(1, "foo").__repr__() == "LeafPattern(1, 'foo')"
    assert LeafPattern(1, "foo", "bar").__repr__() == "LeafPattern(1, 'foo', 'bar')"
    assert NodePattern(Token).__repr__() == "NodePattern(Token)"
    assert NodePattern(Token, "foo").__repr__() == "NodePattern(Token, 'foo')"
    assert NodePattern(Token, "foo", "bar").__repr__() == "NodePattern(Token, 'foo', 'bar')"



# Generated at 2022-06-13 18:15:56.258539
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    nodes = [Leaf(1, '1')]
    p = BasePattern(type=1, content=None, name=None)
    assert list(p.generate_matches(nodes)) == [(1, {})]

# Generated code for method generate_matches of class BasePattern
# Comments starting with ### are retained in the generated code

# The generated code for this class is a bit hacked to be able to
# use the {previous,next}_match functions.



# Generated at 2022-06-13 18:16:28.072380
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    # set up a Node with a Leaf child
    leaf = Leaf(type=1, value="leaf1", prefix=" ", parent=None, children=[])
    node = Node(
        type=2,
        value=None,
        prefix="",
        parent=None,
        children=[leaf])

    # check that get_suffix on the Node returns the Leaf child's prefix
    assert node.get_suffix() == " ", "Unexpected value for method get_suffix"

    # check that get_suffix on the Leaf returns the empty string
    assert leaf.get_suffix() == "", "Unexpected value for method get_suffix"


# --------------------------------------------------------------------

T = TypeVar("T")  # generic type to represent a parsed object

# --------------------------------------------------------------------



# Generated at 2022-06-13 18:16:33.323835
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.NAME) == "NAME"
    assert type_repr(python_symbols.NUMBER) == "NUMBER"
    assert type_repr(python_symbols.STRING) == "STRING"
    assert type_repr(python_symbols.NEWLINE) == "NEWLINE"
    assert type_repr(10) == 10
    assert type_repr(-10) == -10


# Cache of compiled patterns.
_pattern_cache: Dict[str, Any] = {}



# Generated at 2022-06-13 18:16:34.765469
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    Leaf.post_order()

# Generated at 2022-06-13 18:16:46.327302
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    import hypothesis
    import hypothesis.strategies as st
    import string

    @hypothesis.given(st.data())
    def test_hypothesis(data):
        node_a = data.draw(hypothesis.strategies.builds(Leaf, st.text()))
        node_b = data.draw(hypothesis.strategies.builds(Leaf, st.text()))
        if node_a.value == node_b.value:
            assert node_a == node_b, "a: %s b: %s" %(node_a.value, node_b.value)
        else:
            assert node_a != node_b, "a: %s b: %s" %(node_a.value, node_b.value)
    test_hypothesis()
# Unit

# Generated at 2022-06-13 18:16:49.038350
# Unit test for method post_order of class Node
def test_Node_post_order():
    n = Node(0, [Leaf(1, "", None), Leaf(2, "", None)])
    assert list(n.post_order())[-1] == n


# Generated at 2022-06-13 18:17:03.310806
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    import ast
    from .pytree import Leaf, Node, Base

    x = Leaf(0, 1, None, None, None)
    assert list(x.post_order()) == [x]

    x = Leaf(0, 1, None, None, None)
    y = Leaf(0, 1, None, None, None)
    z = Leaf(0, 1, None, None, None)
    p = Node(0, [x, y, z], None, None, None)
    assert list(p.post_order()) == [x, y, z, p]
    assert list(x.post_order()) == [x]
    assert list(y.post_order()) == [y]
    assert list(z.post_order()) == [z]

    x = Leaf(0, 1, None, None, None)
   

# Generated at 2022-06-13 18:17:04.397066
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    leaf = Leaf(1, '1')
    lst = list(leaf.post_order())
    assert lst == [leaf]


# Generated at 2022-06-13 18:17:15.991924
# Unit test for method replace of class Base
def test_Base_replace():
    class TestNode(Node):
        """Mock Node for unit test"""

        def _eq(self, other) -> bool:
            return self._similar(other, deep=True)

        def clone(self) -> Node:
            return self  # Undo parent pointer

    tree = TestNode(
        symbol=python_symbols.file_input,
        children=[
            Base(type=54, value="a"),
            TestNode(
                symbol=python_symbols.simple_stmt,
                children=[
                    TestNode(symbol=python_symbols.small_stmt, children=[
                        Base(type=4, value="b")
                    ])
                ]
            ),
            Base(type=54, value="c"),
        ]
    )


# Generated at 2022-06-13 18:17:21.626470
# Unit test for function convert
def test_convert():
    from .pgen2 import pgen
    from .pgen2 import token

    grammar = pgen.yacc.load_grammar("src/test/test_grammar.txt")


    def token_raw(type: int, value: Optional[Text] = None) -> RawNode:
        """Helper function to build raw node tuples."""
        return type, value, None, []


    def node_raw(
        type: int,
        children: List[RawNode],
        value: Optional[Text] = None,
    ) -> RawNode:
        """Helper function to build raw node tuples."""
        return type, value, None, children


    def build_tree() -> NL:
        """Build a syntax tree for unit testing."""

# Generated at 2022-06-13 18:17:26.272742
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    arg = []
    t = BasePattern()
    assert list(t.generate_matches(arg)) == []

    t.type = 1
    assert list(t.generate_matches(arg)) == []

    t.type = 1
    arg.append(object())
    assert list(t.generate_matches(arg)) == [(1, {})]


# Generated at 2022-06-13 18:17:46.518762
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    from pgen2.grammar import Grammar, GrammarError
    from pgen2.pgen import Pgen
    from .pytree import Leaf, Node

    from .pygram import python_grammar_no_print_statement

    g = Grammar(python_grammar_no_print_statement, python_grammar_no_print_statement.symbol2number)
    p = Pgen(g)
    foo, bar = p.parse("foo", "<test>").children
    node = Node(syms.simple_stmt, [foo, bar])
    node.children[0] = Leaf(token.NAME, "foo", (1, 0))

    assert node.get_lineno() == 1

    # Test that we get a meaningful error message when get_lineno is called
    # on a node that has a child that is None

# Generated at 2022-06-13 18:17:57.556041
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    a = Leaf(10, "Test", (1,2))
    b = Leaf(11, "Test2", (1,2))
    c = Node(1000, [a, b], None)
    assert c._eq(c)
    assert not c._eq(a)
    assert not c._eq(b)
    assert c != a
    assert c != b
    assert c != 1000
    c.changed()
    assert c.was_changed
    c.changed()
    c.changed()
    c.changed()
    c.changed()
    assert a.parent == c
    assert b.parent == c
    a.replace(b)
    assert a.parent == None
    assert b.parent == c
    assert c.children == [b]
    assert b.children == []
    assert b.parent == c


# Generated at 2022-06-13 18:18:07.269787
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf

    node = Base()
    node.parent = Leaf(1, 'hi')
    node.parent.children = [node]
    node.replace(None)

    node.parent = Leaf(1, 'hi')
    node.parent.children = [node, Leaf(1, 'pizza')]
    node.replace(None)

    node.parent = Leaf(1, 'hi')
    node.parent.children = [node, Leaf(1, 'pizza')]
    node.parent.invalidate_sibling_maps()
    node.replace([Leaf(1, 'bye'), Leaf(1, 'baby'), Leaf(1, 'doll')])


# Generated at 2022-06-13 18:18:14.919136
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    from collections import namedtuple
    from unittest import TestCase
    from nltk.tree import Tree

    class PatternTestCase(TestCase):
        class FakeNode(object):
            pass

        def runTest(self):
            pass

        FAKE_NODE = FakeNode()

        def assertGenerateMatches(self, pattern, nodes, expected):
            expected = tuple(expected)

            actual = tuple(pattern.generate_matches(nodes))
            self.assertEqual(
                actual,
                expected,
                msg=(
                    "Expected pattern %r to generate %r on input %r, "
                    + "but it generated %r instead"
                )
                % (pattern, expected, nodes, actual),
            )

    t = namedtuple("t", "label, children")
    g = namedt

# Generated at 2022-06-13 18:18:17.878212
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    import doctest
    doctest.run_docstring_examples(BasePattern.__repr__, globals())

# Generated at 2022-06-13 18:18:27.431174
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    import unittest

    class _TestVisitor(object):
        def __init__(self):
            self.nodes = []

        def default_visit(self, node):
            self.nodes.append(node)

    class NodeTest(unittest.TestCase):
        def test_pre_order_simple(self):
            from .pgen2 import driver

            g = driver.load_grammar("Grammar.txt")
            pg = driver.make_pgen(g)
            tree = pg.parse("x = 10")
            visitor = _TestVisitor()
            for node in tree.pre_order():
                visitor.default_visit(node)
            self.assertEqual(7, len(visitor.nodes))


# Generated at 2022-06-13 18:18:28.723811
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    from .patcomp import compile
    p = compile("a")
    assert p is p.optimize()


# Generated at 2022-06-13 18:18:34.709674
# Unit test for method depth of class Base
def test_Base_depth():
    global ast
    # Create Node and Leaf nodes
    n = Node(0, [], prefix="prefix1")
    l = Leaf(0, "leaf", prefix="leafprefix", lineno=1)
    n2 = Node(0, [], prefix="prefix2")
    n3 = Node(0, [], prefix="prefix3")
    n4 = Node(0, [], prefix="prefix4")

    # Check depth with not parents
    assert l.depth() == 0
    assert n.depth() == 0

    # Create tree
    n.append_child(l)
    n2.append_child(n)
    n3.append_child(n2)
    n4.append_child(n3)

    # Check depth of nodes and leaves
    assert l.depth() == 3
    assert n.depth() == 2


# Generated at 2022-06-13 18:18:36.577826
# Unit test for method remove of class Base
def test_Base_remove():
    Base()


# Generated at 2022-06-13 18:18:49.705159
# Unit test for method leaves of class Base
def test_Base_leaves():
    tree1 = Node(0, "", [])
    tree2 = Leaf(0, "1", (0, 0))
    tree3 = Node(0, "", [], parent=tree1)
    tree4 = Node(0, "", [], parent=tree1)
    tree5 = Node(0, "", [], parent=tree1)
    tree6 = Node(0, "", [], parent=tree4)
    tree7 = Node(0, "", [], parent=tree4)
    tree8 = Node(0, "", [], parent=tree4)
    tree9 = Node(0, "", [], parent=tree4)
    tree10 = Node(0, "", [], parent=tree4)
    tree11 = Leaf(0, "1", (0, 0))

# Generated at 2022-06-13 18:19:22.317370
# Unit test for method replace of class Base
def test_Base_replace():
    from blib2to3.pytree import Leaf, Node, Base
    class DummyNode(Base):
        def __init__(self, val):
            super().__init__()
            self.val = val
        def _eq(self, other):
            return self.val == other.val

        def clone(self):
            return DummyNode(self.val)

        def post_order(self):
            yield self

        def pre_order(self):
            yield self
    a, b, c = DummyNode(1), DummyNode(2), DummyNode(3)
    d = Node(0, [a, b, c])
    e = d.clone()
    assert id(d) != id(e)
    assert d == e
    a.replace([b])
    assert d != e
    f

# Generated at 2022-06-13 18:19:29.539523
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    check_pattern = "((atom))*"
    pattern = parse_pattern(check_pattern, "bare_name")
    assert isinstance(pattern, NodePattern)
    check_pattern = "(atom)*"
    pattern = parse_pattern(check_pattern, "bare_name")
    assert isinstance(pattern, WildcardPattern)
    pattern = pattern.optimize()
    assert isinstance(pattern, NodePattern)
    check_pattern = "((atom)*)*"
    pattern = parse_pattern(check_pattern, "bare_name")
    pattern = pattern.optimize()
    assert isinstance(pattern, WildcardPattern)
    assert pattern.min == 2
    assert pattern.max == 2


# Functions for parsing patterns #########################################


# Generated at 2022-06-13 18:19:30.903753
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    pass



# Generated at 2022-06-13 18:19:35.233788
# Unit test for constructor of class Node
def test_Node():
    Node(256, [])
    Node(256, [], context=None, prefix="")
    Node(256, [], context=None, prefix="", fixers_applied=[1, 2, 3])
    Node(256, [], fixers_applied=[])
    Node(256, [], context=None)
    Node(256, [], context=None, fixers_applied=[])
    Node(256, [], context=None, prefix="", fixers_applied=[])



# Generated at 2022-06-13 18:19:41.190880
# Unit test for method leaves of class Base
def test_Base_leaves():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Leaf(1)
    e = Leaf(2)
    c.append_child(d)
    b.append_child(c)
    b.append_child(e)
    a.append_child(b)
    leaves = a.leaves()
    assert(next(leaves) is d)
    assert(next(leaves) is e)
    assert(next(leaves) is None)



# Generated at 2022-06-13 18:19:46.799794
# Unit test for method remove of class Base
def test_Base_remove():
    str_file = "abc"
    file_node = FileInput("", [Leaf(1, "abc")])
    file_node.remove()
    assert not file_node.parent == None
    file_node.children.pop()
    assert str_file == file_node.children[0].value
    file_node.children.pop()
    assert str_file == file_node.children[0].value

# Generated at 2022-06-13 18:19:56.839148
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf, Node  # type: ignore
    a = Leaf("block", 0, "a")
    b = Leaf("stmt", 1, "b")
    c = Leaf("line", 2, "c")
    node = Node("root", [a, b, c])
    assert a.parent is node
    assert b.parent is node
    assert c.parent is node
    a.replace(b)
    assert a.parent is None
    assert b.parent is node
    assert c.parent is node
    assert node.children == [b, b, c]
    a.replace(None)
    assert node.children == [b, c]
    b.replace([])
    assert node.children == [c]
    c.replace([a, b])
    assert node.children == [a, b]


# Generated at 2022-06-13 18:20:03.662379
# Unit test for constructor of class NodePattern
def test_NodePattern():
    from . import token, symbol

    p = NodePattern(symbol.expr_stmt, [LeafPattern(1, "spam")])
    node = Node(
        symbol.expr_stmt,
        [
            Leaf(token.NAME, "spam"),
        ],
    )
    results = {}
    assert p.match(node, results)
    assert results["NAME"].value == "spam"

    p = NodePattern(symbol.suite, [LeafPattern(1, "spam")])
    node = Node(
        symbol.suite,
        [
            Leaf(token.NAME, "spam"),
        ],
    )
    results = {}
    assert p.match(node, results)
    assert results["NAME"].value == "spam"



# Generated at 2022-06-13 18:20:06.911741
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    r = Base()
    r.type = 0
    assert r.__eq__(Base()) == NotImplemented



# Generated at 2022-06-13 18:20:10.349808
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    # pylint: disable=redefined-outer-name
    l = Leaf(0, 'name')
    assert l.pre_order().__next__() is l


# Generated at 2022-06-13 18:20:47.753466
# Unit test for function generate_matches
def test_generate_matches():
    # A simple unit test
    import re
    import sys
    import tokenize
    pat = re.compile("def[ \t]+([a-zA-Z_][a-zA-Z0-9_]*)")
    code = open(__file__, "r", encoding="utf-8").read()
    tokens = tokenize.generate_tokens(lambda: code)
    nodes = list(tokenize.untokenize(tokens))
    for typ, value in nodes:
        if not typ == tokenize.NAME:
            continue
        m = pat.match(value)
        if not m:
            continue
        print(m.group(1))
        toks = value.split()
        pats = []
        for tok in toks:
            if tok.isupper():
                p

# Generated at 2022-06-13 18:20:54.221343
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    import random
    import unittest
    import pgen2.grammar
    import pgen2.parse

    # A specific grammar.
    py_grammar = pgen2.grammar.Grammar(pgen2.parse.pgen_grammar)

    # A specific parse tree.
    source = "foo(1, 2, 3)\nbar(4)"
    st = pgen2.parse.parse_string(py_grammar, source)

    # Mapping from a regular expression to a set of node types.
    # This is not the complete set of node types in the grammar.
    # It's here just for testing.

# Generated at 2022-06-13 18:21:02.686830
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    import inspect

    def test(pattern, expected):
        pattern = WildcardPattern(
            pattern,
            name="bare_name"
        )
        pattern = pattern.optimize()
        assert isinstance(pattern, expected), "expected %s, got %s" % (expected, type(pattern))

    test(None, NodePattern)
    test([[NodePattern(97)]], NodePattern)
    test([[WildcardPattern(None, 1, 1)]], WildcardPattern)



# Generated at 2022-06-13 18:21:10.007053
# Unit test for function convert
def test_convert():
    class DummyGrammar:
        def number2symbol(i):
            return i
    gr = DummyGrammar()
    d = dict(type=1, value="testing", context=(None, None), children=[])
    assert convert(gr, d) == Leaf(1, "testing", context=(None, None))
    d["children"] = [Leaf(1, "test")]
    assert convert(gr, d) == Node(1, [Leaf(1, "test")])
    d["children"] = [Leaf(1, "test"), Leaf(2, "other")]
    assert convert(gr, d) == Node(1, [Leaf(1, "test"), Leaf(2, "other")])



# Generated at 2022-06-13 18:21:21.492198
# Unit test for method post_order of class Base
def test_Base_post_order():
    """Unit test for method post_order of class Base"""
    import unittest
    import copy

    class TestNode(Node):
        """A simple node class for testing."""

        def __init__(self, type, value, parent=None, children=None):
            """Initialize a test node."""
            super().__init__(type, value, parent, children)

        def _eq(self, other):
            """Equivalence comparison for testing."""
            return self.type == other.type

        def clone(self):
            """Clone method for testing."""
            return TestNode(self.type, self.value, None,
                            [child.clone() for child in self.children])

    class TestLeaf(Leaf):
        """A simple leaf class for testing."""


# Generated at 2022-06-13 18:21:31.268330
# Unit test for method post_order of class Base
def test_Base_post_order():
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util
    import lib2to3.fixer_util

# Generated at 2022-06-13 18:21:34.816396
# Unit test for method depth of class Base
def test_Base_depth():
    n = Node(syms.root)
    assert n.depth() == 0
    n2 = Node(syms.simple_stmt)
    n.append_child(n2)
    assert n2.depth() == 1


# Generated at 2022-06-13 18:21:40.748438
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .. import pytree
    from . import python_grammar_no_print_statement as python_grammar

    # A simple test
    s = "def f(): pass"
    tree = pytree.PyTree.create_from_grammar(python_grammar, s)
    assert tree.get_suffix() == "\n"

    # A more complex test

# Generated at 2022-06-13 18:21:54.070764
# Unit test for method post_order of class Node
def test_Node_post_order():
    from .pytree import Node, Leaf, type_repr

    nil = Node(python_symbols.nil, [])
    dots = Node(python_symbols.dots, [])
    attr = Node(python_symbols.atom, [Leaf(1, 'a')])
    string = Node(python_symbols.atom, [Leaf(1, '"foo"')])
    number = Node(python_symbols.atom, [Leaf(1, '1')])
    expr_stmt = Node(python_symbols.expr_stmt, [attr, Leaf(1, '='), string])
    comp_for = Node(python_symbols.comp_for, [Leaf(1, 'for'), attr, Leaf(1, 'in'), number])

# Generated at 2022-06-13 18:22:06.738664
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    # First, a single wildcard, which should be equivalent to a
    # repeated single NodePattern.
    wc = WildcardPattern(min=1, max=2)
    for i in range(1, 5):
        expected = [(1,), (2,), (3,)]
        if i < 3:
            expected = expected[:i]
        results = list(wc.generate_matches([None] * i))
        assert results == expected, results
    # Next, a single wildcard, with alternatives.
    wc = WildcardPattern([[LeafPattern("a"), LeafPattern("b")]], min=1, max=2)