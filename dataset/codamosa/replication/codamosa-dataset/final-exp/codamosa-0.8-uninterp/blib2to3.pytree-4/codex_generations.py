

# Generated at 2022-06-13 18:14:36.356755
# Unit test for method get_lineno of class Base

# Generated at 2022-06-13 18:14:37.897585
# Unit test for method match of class BasePattern
def test_BasePattern_match():

    # Test BasePattern.match
    p = BasePattern()
    assert not p.match(Leaf(0, "x"))



# Generated at 2022-06-13 18:14:43.506509
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    class Base_1(Base):
        type = 1
        parent = 2
        children = 3
        was_changed = 4
        was_checked = 5

    class Base_2(Base):
        type = 1
        parent = 2
        children = 3
        was_changed = 4
        was_checked = 5

    assert Base_1() == Base_2()



# Generated at 2022-06-13 18:14:53.095281
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    pattern = WildcardPattern(
        content=[
            ["import_from"],
            ["import_name"],
            [WildcardPattern(content=[["dotted_name"], ["dotted_as_name"]])],
        ],
        min=1,
        max=1,
    )
    nodes = [
        Node(
            type=import_from,
            children=[
                Leaf(type=NAME, value="foo"),
                Leaf(type=DOT, value="."),
                Leaf(type=NAME, value="bar"),
            ],
        )
    ]
    for c, r in pattern.generate_matches(nodes):
        print(c)
        print(r)


# Parser Functions


# Generated at 2022-06-13 18:14:53.741942
# Unit test for method leaves of class Base
def test_Base_leaves():
    pass



# Generated at 2022-06-13 18:15:08.635318
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    from .pgen2 import tokenize

    def show(s):
        t = tokenize(s, "", False)
        return list(map(type, t.tokens))

    # testcase: single-alternative match
    pat = WildcardPattern([[LeafPattern(type=tokenize.COMMA)]])
    assert list(pat.generate_matches(show(","))) == [
        (1, {})
    ], list(pat.generate_matches(show(",")))

    # testcase: repeated comma
    pat = WildcardPattern([[LeafPattern(type=tokenize.COMMA)]])
    exp = list(map(tuple, [[(1, {})], [(1, {}), (2, {})], [(1, {}), (2, {}), (3, {})]]))


# Generated at 2022-06-13 18:15:18.490262
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    """
    >>> test_NegatedPattern_generate_matches()
    """
    import sys
    import unittest

    class ParserTestCase(unittest.TestCase):
        def assertMatch(self, parser, node, expected):
            matches = []
            for c, r in parser.generate_matches(node):
                matches.append((c, r))
            self.assertEqual(expected, matches)

    class TestParser(ParserTestCase):
        def test_empty(self):
            node = DummyNode("", None)
            parser = NegatedPattern()
            self.assertMatch(parser, [node], [(0, {})])

        def test_nonempty(self):
            node = DummyNode("", None)
            parser = NegatedPattern(NodePattern())

# Generated at 2022-06-13 18:15:28.704720
# Unit test for method clone of class Base
def test_Base_clone():
    from .pgen2 import token

    class Foo(Base):
        def __init__(self, type_num: int, value: Any, context: Context) -> None:
            super().__init__()
            self.type_num = type_num
            self.value = value
            self.context = context
            self.parent = None  # type: Optional[Node]
            self.children = []  # type: List[NL]

        def __eq__(self, other: Any) -> bool:
            if self.__class__ is not other.__class__:
                return NotImplemented
            return self.type_num == other.type_num and self.value == other.value
        def __hash__(self) -> int:
            return hash((self.type_num, self.value))


# Generated at 2022-06-13 18:15:32.848888
# Unit test for method clone of class Leaf
def test_Leaf_clone():
    from .pgen2 import token
    # Create a Leaf object
    a = Leaf(token.NAME, "foo", (None, (1, 2)))
    b:Leaf = a.clone()
    # Check if the Leaf object a is equal to the cloned object b
    assert a.__eq__(b)
    # Check if there is only one object in memory
    assert a is not b


# Generated at 2022-06-13 18:15:36.859012
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    test_node = Leaf(1, '', '', '')
    test_result = test_node.leaves()
    test_expected = [test_node]
    assert list(test_result) == test_expected


# Generated at 2022-06-13 18:15:55.562596
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import unittest
    from .pgen2 import token, driver

    class TestCase(unittest.TestCase):

        def test_generate_matches(self):
            d = driver.Driver(convert)
            gr = d.build_grammar(
                """
                expr: term ('+' term)*;
                term: factor ('*' factor)*;
                factor: '(' expr ')' | NUMBER;
                """
            )
            p = gr.pattern_parse("expr")
            p = p.optimize()
            expr = d.parse_string(gr, "(1)", start="expr")[0]
            matches = set(p.generate_matches(expr.post_order()))

# Generated at 2022-06-13 18:16:04.368366
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf, Internal, Node, type_repr, fromstring

    results = [
        (Leaf(1, "leaf"), None),
        (Internal(1, [Leaf(1, "leaf")]), None),
        (Internal(1, [Leaf(1, "leaf")]), [Leaf(2, "leaf2")]),
        (Internal(1, [Leaf(1, "leaf"), Leaf(2, "leaf2")]),
         [Leaf(1, "leaf"), Leaf(2, "leaf2")]),
        (Internal(1, [Leaf(1, "leaf")]),
         [Leaf(2, "leaf2"), Leaf(3, "leaf3")]),
    ]
    for orig, replacement in results:
        parent = Node(1, [orig, Leaf(2, "leaf")])


# Generated at 2022-06-13 18:16:10.137568
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pgen2.pgen import generate_matches

    class TestNode(Node):
        def __init__(self, value, type) -> None:
            self.type = type
            self.value = value

    assert list(generate_matches(TestNode(1, 1), None)) == [(1, {})]



# Generated at 2022-06-13 18:16:21.641096
# Unit test for method leaves of class Base
def test_Base_leaves():
    import lib2to3.fixer_base
    import lib2to3.fixer_util
    from lib2to3.fixer_util import Name, Comma
    from .pgen2 import token
    from .pygram import python_symbols as syms
    lib2to3.fixer_base.Base = Base
    lib2to3.fixer_util.Name = Name
    lib2to3.fixer_util.Comma = Comma
    lib2to3.pgen2.token = token
    lib2to3.pgen2.syms = syms
    n = Name("n")
    c = Comma()
    n.prefix = " "
    c.prefix = "\n"
    t = Name("t")
    f = Name("f")
    a = Name("a")
   

# Generated at 2022-06-13 18:16:22.605043
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    cv = Leaf(257, "class")
    cv.post_order()


# Generated at 2022-06-13 18:16:30.324176
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    import ast
    import asttokens
    import io
    import token as tk
    from .pgen2.token import tok_name

    source = """\
"""
    atok = asttokens.ASTTokens(source, parse=True)
    root = atok.tree
    l0 = atok.get_text_range(root)
    l1 = atok._original_start(root)
    l2 = atok._original_end(root)
    l3 = atok._original_text(root)
    result_repr = repr(root)

    lineno = 1
    column = 0
    atok = asttokens.ASTTokens(source, parse=True)
    root = atok.tree
    l0 = atok.get_text_range(root)
    l1 = at

# Generated at 2022-06-13 18:16:32.499015
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    class Subclass(Base):
        pass
    sub = Subclass()
    sub.children = [1, 2, 3]
    assert sub.get_lineno() == 1



# Generated at 2022-06-13 18:16:36.587969
# Unit test for function type_repr
def test_type_repr():
    x = [x for x in dir(python_symbols) if x.endswith("_KW")]
    x = [x[:-3] for x in x]  # strip off the "_KW"
    for x in x:
        if '_' in x:
            continue
        num = getattr(python_symbols, x + "_KW")
        assert type_repr(num) == x
test_type_repr()



# Generated at 2022-06-13 18:16:42.183724
# Unit test for function generate_matches
def test_generate_matches():
    import pprint
    pprint.pprint(list(generate_matches([], [])))
    assert list(generate_matches([], [])) == [(0, {})]
    pprint.pprint(list(generate_matches([NodePattern(1)], [Leaf(1)])))
    assert list(generate_matches([NodePattern(1)], [Leaf(1)])) == [(1, {})]
    pprint.pprint(list(generate_matches([NodePattern(1), NodePattern(2)], [Leaf(1), Leaf(2)])))
    assert list(generate_matches([NodePattern(1), NodePattern(2)], [Leaf(1), Leaf(2)])) == [(2, {})]

# Generated at 2022-06-13 18:16:45.429711
# Unit test for method post_order of class Base
def test_Base_post_order():
    """
    def test_Base_post_order(self):
        self.assertRaises(NotImplementedError, self.node.post_order)
    """
    pass



# Generated at 2022-06-13 18:17:25.442697
# Unit test for method post_order of class Node
def test_Node_post_order():
    
    from .pytree import Leaf, Node
    
    class Subclass(Node):
        def __str__(self):
            return 'Subclass(<%s>)' % ', '.join(map(str, self.children))
    
    leaf1 = Leaf(1, 'a')
    leaf1.lineno = 2
    leaf2 = Leaf(2, 'b')
    leaf2.lineno = 4
    leaf3 = Leaf(3, 'c')
    leaf3.lineno = 6
    
    
    #
    
    
    
    
    
    
    
    tree = Node(4, [leaf1, leaf2, leaf3])
    assert list(tree.post_order()) == [leaf1, leaf2, leaf3, tree]
    
    
    
    
    
    
    
    

# Generated at 2022-06-13 18:17:35.248879
# Unit test for method post_order of class Node
def test_Node_post_order():
    s = '''
        def f(x, (y, z)):
            return x + y + z
    '''

# Generated at 2022-06-13 18:17:45.169239
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    from .pytree import Node
    t = Node(1, [Leaf(1, "a"), Leaf(2, "\n"), Leaf(3, "b")])
    assert t.children[0].get_lineno() == 1
    assert t.get_lineno() == 1
    assert t.children[1].get_lineno() == 1
    assert t.children[2].get_lineno() == 2
    assert t.children[0].next_sibling.get_lineno() == 1
    assert t.children[1].next_sibling.get_lineno() == 2
    assert t.children[1].prev_sibling.get_lineno() == 1
    assert t.children[2].prev_sibling.get_lineno() == 1


# Generated at 2022-06-13 18:17:47.724508
# Unit test for method depth of class Base
def test_Base_depth():
    for _i in range(500000):
        n = Leaf(1, None)
        n.depth()


# Generated at 2022-06-13 18:17:58.506173
# Unit test for method set_child of class Node
def test_Node_set_child():
    from .pytree import Leaf, Node
    from .pygram import python_symbols, python_operators
    from .python_tree import TypeSpan

    l1 = Leaf(python_symbols.integer, "1")
    l3 = Leaf(python_symbols.integer, "3")
    l2 = Leaf(python_symbols.integer, "2")
    l4 = Leaf(python_symbols.integer, "4")

    l1.next_sibling = l3
    l3.prev_sibling = l1
    l3.next_sibling = l2
    l2.prev_sibling = l3
    l2.next_sibling = l4
    l4.prev_sibling = l2
    l4.next_sibling = None


# Generated at 2022-06-13 18:18:06.343533
# Unit test for method clone of class Base
def test_Base_clone():
    import unittest
    import inspect
    import blib2to3
    def test(self, expected:Optional[bool]):
        self.assertEqual(Base.clone.__func__ is inspect.getmethodobject(Base,
            "clone").__func__, expected)
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(
        type("Base_clone", (unittest.TestCase,), {"test": lambda self:
        test(self, True)})))
    return suite

# Generated at 2022-06-13 18:18:07.575221
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    assert BasePattern().__repr__() == 'BasePattern()'


# Generated at 2022-06-13 18:18:10.519454
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    t = Leaf(token.NAME, "A", (None, (1, 0)))
    assert [t] == list(t.leaves())

# Generated at 2022-06-13 18:18:20.318751
# Unit test for method __repr__ of class Node
def test_Node___repr__():
    """Test method __repr__ of class Node"""
    import sys
    import os
    import random
    import unittest
    from copy import copy
    from ..tree import Node as _A

    class Node(_A):

        def __init__(self, *args, **kwds):
            # generate the self.fixers_applied attribute
            self.fixers_applied = kwds.pop('fixers_applied', None)
            super(Node, self).__init__(*args, **kwds)
        def __repr__(self):
            return 'Node(%r, %r, fixers_applied=%r)' % (self.type, self.children, self.fixers_applied)

    import pickle

    n1 = Node(1, [2])

# Generated at 2022-06-13 18:18:23.390613
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pytree import Leaf
    from .pygram import python_grammar
    from . import pytree
    class DummyPattern(BasePattern):
        def __init__(self):
            self.type = 1
            self.name = "foo"
    nodes = [Leaf(1, "1"), Leaf(2, "2")]
    assert list(DummyPattern().generate_matches(nodes)) == [(1, {'foo': nodes[0]})]


# Generated at 2022-06-13 18:21:24.280460
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    """Unit test for method generate_matches of class BasePattern."""
    import re as re  # pytype: disable=import-error

    # Sample pattern which should match anything
    pattern = ContentPattern(re.compile(r".*"))
    # Sample sequence of nodes
    # 3 non-leaf nodes, the first with 2 children, the second with 1 child, the
    # third with 0 children
    nodes = []
    nodes.append(Node(259, [Leaf(1, "a"), Leaf(2, "b")]))
    nodes.append(Node(260, [Leaf(3, "c")]))
    nodes.append(Node(261, []))
    # This should match any of the three nodes, ie. all 1-element slices

# Generated at 2022-06-13 18:21:32.571803
# Unit test for method remove of class Base
def test_Base_remove():
    class TestNode(Node):
        def test_child(self):
            return self.children[0]
    node = TestNode(1, "Roo")
    child = TestNode(1, "Blah")
    node.append_child(child)
    pos = child.remove()
    assert pos == 0, "child should be at the first position in parent"
    assert child.parent is None, "child should no longer be part of the tree"
    assert node.was_changed, "the parent should be marked as changed"

    child2 = TestNode(1, "Blah")
    node.append_child(child2)
    pos = child2.remove()
    assert pos == 0, "child should be at the first position in parent"
    assert child2.parent is None, "child should no longer be part of the tree"


# Generated at 2022-06-13 18:21:36.767477
# Unit test for method set_child of class Node
def test_Node_set_child():
    n = Node(0, [])
    n.was_changed = False
    n.set_child(0, Leaf(0, 'a'))
    assert n.was_changed


# Generated at 2022-06-13 18:21:42.289954
# Unit test for method clone of class Base
def test_Base_clone():
    n = Node(type=0, children=[Leaf(1, ""), Leaf(0, "")])
    assert Node(type=0, children=[Leaf(1, ""), Leaf(0, "")]) == n.clone()
    assert Node(type=0, children=[Leaf(1, ""), Leaf(0, "")]) == n.clone()



# Generated at 2022-06-13 18:21:47.033779
# Unit test for method clone of class Leaf
def test_Leaf_clone():
    l = Leaf(1, 1)
    l2 = l.clone()
    assert l2 == l
    assert l.parent is None
    assert l2.parent is None
    assert l.parent == l2.parent
    assert l is not l2


# Generated at 2022-06-13 18:21:53.736314
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    ch_a = NodePattern(chr2node("a"))
    ch_b = NodePattern(chr2node("b"))
    ch_c = NodePattern(chr2node("c"))
    ch_d = NodePattern(chr2node("d"))
    wc_0_2 = WildcardPattern([[ch_a,ch_b,ch_c], [ch_d]], 0, 2)
    assert not list(wc_0_2.generate_matches([]))
    assert not list(wc_0_2.generate_matches([chr2node("a")]))
    assert list(wc_0_2.generate_matches([chr2node("a"),chr2node("b")])) == [(2, {})]

# Generated at 2022-06-13 18:22:06.825963
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    import pytest
    from .pgen2.parse import ParseError
    from .pytree import Leaf, Node

    class TestNode(Node):
        def _eq(self, other):
            return self.children == other.children and \
                self.type == other.type

    def test():
        grammar = Grammar(StringIO(r"""
        s: a=b+ c=b
        b: 'b'
        """))
        parser = grammar.parser()
        node = parser.parse(['b', 'b', 'b', 'b'])
        node_copy = TestNode(type=node.type, children=node.children,
                             parent=node.parent)
        assert node == node_copy

    test()

# Generated at 2022-06-13 18:22:11.783824
# Unit test for method post_order of class Node
def test_Node_post_order():
    n = Node(256, [Leaf(2, "foo"), Node(257, [Leaf(2, "bar")]), Leaf(5, "baz")])
    node_types = [x.type for x in n.post_order()]
    if node_types != [2, 257, 2, 256, 5]:
        return 1
    return 0



# Generated at 2022-06-13 18:22:20.225678
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    x = Leaf(1, "foo")
    y = Leaf(1, "bar")
    z = Leaf(1, "baz")
    a = Node(2, [x, y])
    b = Node(3, [z, a])
    assert [n.prefix for n in a.pre_order()] == ["foo", "bar"]
    assert [n.prefix for n in b.pre_order()] == ["baz", "foo", "bar"]

