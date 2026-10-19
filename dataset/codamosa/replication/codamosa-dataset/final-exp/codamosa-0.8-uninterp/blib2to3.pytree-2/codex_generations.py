

# Generated at 2022-06-13 18:14:49.723929
# Unit test for method post_order of class Base
def test_Base_post_order():
    assert False
    # are these the tests for class Base
    assert False

# Generated at 2022-06-13 18:14:58.442109
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pytree import Leaf

    a = Leaf(0, "end", (1, 1))
    b = Leaf(0, "art", (1, 1), prefix="start")
    b.set_suffix("suffix")
    c = Leaf(0, "end", (1, 1), prefix="start")
    assert a.get_suffix() == ""
    assert b.get_suffix() == "suffix"
    assert c.get_suffix() == ""

    # Ensure that b's suffix is not the same as c's prefix
    c.prefix = "suffix"
    try:
        assert b.get_suffix() == "suffix"
    except:
        pass
    else:
        raise Exception("b does not have the correct suffix")

    b.remove_suffix()
    assert b.get_

# Generated at 2022-06-13 18:15:05.129633
# Unit test for method __repr__ of class Node
def test_Node___repr__():
    """Test method Node.__repr__"""
    a = Node(256, [])
    assert repr(a) == "Node(NAME, [])"
    a.children = [Leaf(258, "abc")]
    assert repr(a) == "Node(NAME, [Leaf(258, 'abc')])"



# Generated at 2022-06-13 18:15:09.028936
# Unit test for method set_child of class Node
def test_Node_set_child():
    parse_tree = tools.build_tokens("1 + 2")
    parse_tree.changed()
    parse_tree.set_child(0, )
    assert parse_tree == tools.build_tokens(" + 2")


# Generated at 2022-06-13 18:15:18.920867
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    assert repr(BasePattern()) == 'BasePattern()'
    assert repr(BasePattern(None)) == 'BasePattern(None)'
    assert repr(BasePattern(None, None)) == 'BasePattern(None, None)'
    assert repr(BasePattern(1, 2, 3)) == 'BasePattern(1, 2, 3)'
    assert repr(BasePattern('a', 'b', 'c')) == "BasePattern('a', 'b', 'c')"
    assert repr(BasePattern(1)) == 'BasePattern(1)'
    assert repr(BasePattern(1, None)) == 'BasePattern(1)'
    assert repr(BasePattern(1, 2)) == 'BasePattern(1, 2)'
    assert repr(BasePattern(1, 2, None)) == 'BasePattern(1, 2)'

# Generated at 2022-06-13 18:15:22.312643
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    bp1 = BasePattern(0)
    assert repr(bp1) == 'BasePattern(0,'
    bp2 = BasePattern(0, 'value')
    assert repr(bp2) == "BasePattern(0, 'value')"
    bp3 = BasePattern(0, 'value', 'name')
    assert repr(bp3) == "BasePattern(0, 'value', 'name')"



# Generated at 2022-06-13 18:15:24.402711
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    leaf = Leaf(1,"")
    assert leaf.leaves() is not None
test_Leaf_leaves()

# Generated at 2022-06-13 18:15:33.299346
# Unit test for method replace of class Base
def test_Base_replace():
    class MyNode(Node):
        def _eq(self, other):
            return self.type == other.type and self.children == other.children

    my_node = MyNode(syms.simple_stmt, [Leaf(1, 'a'), Leaf(2, 'b'), Leaf(3, 'c')])
    assert my_node == MyNode(syms.simple_stmt, [Leaf(1, 'a'), Leaf(2, 'b'), Leaf(3, 'c')])
    my_node.replace(Leaf(42, 'd'))
    assert my_node == MyNode(syms.simple_stmt, [Leaf(42, 'd')])
    assert my_node.children == [Leaf(42, 'd')]
    my_node.replace(Leaf(42, 'e'))

# Generated at 2022-06-13 18:15:36.807248
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    # BasePattern.optimize()
    # This method should be overriden in subclasses
    b = BasePattern()
    raises(NotImplementedError, b.optimize)


# Generated at 2022-06-13 18:15:39.213385
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    pattern = BasePattern()
    assert pattern.optimize() is pattern
test_BasePattern_optimize()


# Generated at 2022-06-13 18:15:52.206320
# Unit test for method depth of class Base
def test_Base_depth():
    return 0


# Generated at 2022-06-13 18:15:55.009854
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Leaf, Node
    tree = Node(1, "", [Node(2, "", [Leaf(3, "abc")])])
    assert len(list(tree.leaves())) == 1



# Generated at 2022-06-13 18:15:58.023700
# Unit test for method depth of class Base
def test_Base_depth():
    node = Node(1, [])
    assert node.depth() == 0
    node.parent = Node(1, [])
    assert node.depth() == 1


# Generated at 2022-06-13 18:16:03.500357
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    from .pythonparser import SimpleParser
    from . import pytree
    from .pgen2 import token
    from . import python_tree
    p = SimpleParser()
    id = p.parse_string("foo")
    assert list(id.leaves()) == [id]
    idnb = p.parse_string("    foo")
    assert list(idnb.leaves()) == [idnb]
    s = pytree.Node(token.STRING, [id])
    assert list(s.leaves()) == [id]
    print("test_Leaf_leaves finished.")


# Generated at 2022-06-13 18:16:11.616452
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from .pytree import Leaf

    n = Node(1, [Leaf(2, "prefix"), Leaf(3, "")])
    i = n.pre_order()
    assert i.__next__() is n
    assert i.__next__().type == 2
    assert i.__next__().type == 3
    try:
        i.__next__()
    except StopIteration:
        pass
    else:
        assert False, "StopIteration not raised"



# Generated at 2022-06-13 18:16:15.510925
# Unit test for method __eq__ of class Base
def test_Base___eq__():

    assert Base().__eq__(Base()) == NotImplemented
    assert Base().__eq__(Leaf()) == NotImplemented

    # test method Base.__eq__ without assert statements



# Generated at 2022-06-13 18:16:17.708235
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    assert NodePattern(42).optimize() is NodePattern(42)
test_BasePattern_optimize()



# Generated at 2022-06-13 18:16:20.262342
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    """Unit test for method __repr__ of class BasePattern"""
    pattern = BasePattern()
    pattern.type = 256
    pattern.content = None
    pattern.name = 'name'
    actual = pattern.__repr__()
    assert actual == "BasePattern(256, None, 'name')"


# Generated at 2022-06-13 18:16:21.174058
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    l = Leaf(1,'')
    assert Leaf.pre_order(l)

# Generated at 2022-06-13 18:16:23.633364
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    for cls in [Node, Leaf, LeafMatch]:
        node = cls()
        assert node.get_lineno() is None


# Generated at 2022-06-13 18:17:01.530156
# Unit test for method __repr__ of class Node
def test_Node___repr__():
    """
    Unit test for method __repr__ of class Node.
    """
    node = Node(258, [])
    assert repr(node).startswith('Node(')


# Generated at 2022-06-13 18:17:11.867639
# Unit test for method leaves of class Base
def test_Base_leaves():
    class TestNode(Node):
        def __init__(self, children):
            self.children = children

    class TestLeaf(Leaf):
        def __init__(self, value):
            self.prefix = value

    l1 = TestLeaf("l1")
    l2 = TestLeaf("l2")
    l3 = TestLeaf("l3")
    l4 = TestLeaf("l4")

    n1 = TestNode([l1])
    n2 = TestNode([n1])
    n3 = TestNode([n2, l2, l3])
    n4 = TestNode([l4])

    assert [l.prefix for l in n1.leaves()] == ["l1"]
    assert [l.prefix for l in n2.leaves()] == ["l1"]

# Generated at 2022-06-13 18:17:13.520662
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.NAME) == "NAME"



# Generated at 2022-06-13 18:17:23.999459
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():

    a = LiteralPattern("A")
    b = LiteralPattern("B")
    c = LiteralPattern("C")

    # All the patterns below should yield exactly one match, that is,
    # match() should return True, and the match should always comprise
    # the entire sequence of nodes given.
    pattern = NegatedPattern(a)
    assert list(pattern.generate_matches([])) == [(0, {})]
    pattern = NegatedPattern(a)
    assert list(pattern.generate_matches(["A"])) == []
    pattern = NegatedPattern(a)
    assert list(pattern.generate_matches(["A", "A"])) == []
    pattern = NegatedPattern(a)
    assert list(pattern.generate_matches(["B"])) == [(1, {})]

# Generated at 2022-06-13 18:17:31.004185
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    """Unit test for method generate_matches of class WildcardPattern."""
    p = P("a") + P("b") | P("c")
    # This should find all the matches in the text.
    results = list(WildcardPattern(content=[p], name="test").generate_matches(Leaf(1, "abacbac")))
    assert results == [
        (0, {}),
        (2, {"test" : [Leaf(1, "a"), Leaf(1, "b")]}),
        (3, {"test" : [Leaf(1, "c")]}),
        (5, {"test" : [Leaf(1, "a"), Leaf(1, "b")]}),
        (6, {"test" : [Leaf(1, "c")]}),
    ]
    # This should

# Generated at 2022-06-13 18:17:37.443710
# Unit test for method clone of class Base
def test_Base_clone():
    import unittest
    import os

    # Since Base is an abstract base class, we need to fake a subclass.
    # Unfortunately, this means we also have to implement the methods we
    # aren't testing, but can't be bothered to do that...

    class FakeNode(Base):
        def __init__(self, type=0):
            self.type = type
            self.children = []

        def clone(self):
            raise NotImplementedError

        def pre_order(self):
            raise NotImplementedError

        def post_order(self):
            raise NotImplementedError

        def _eq(self, other):
            raise NotImplementedError

    # Ok, now we're ready to test.

    class TestBase(unittest.TestCase):
        def test_eq(self):
            n = Fake

# Generated at 2022-06-13 18:17:38.755811
# Unit test for method clone of class Base
def test_Base_clone():
    import doctest
    doctest.testmod()



# Generated at 2022-06-13 18:17:43.117116
# Unit test for method pre_order of class Node

# Generated at 2022-06-13 18:17:48.726080
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .pytree import Node
    r = Node(type=0)
    o = Node(type=1)
    o.parent = r
    r.children = [o]
    assert r == next(r.pre_order())
    assert o == next(r.pre_order())
    assert StopIteration == type(next(r.pre_order(), None))

# Generated at 2022-06-13 18:17:59.104896
# Unit test for method post_order of class Node
def test_Node_post_order():
    node = Node(258, [])
    l = list(node.post_order())
    assert len(l) == 1
    assert l[0] is node
    node = Node(
        258,
        [
            Leaf(2, "a"),
            Node(259, [Leaf(2, "b"), Leaf(2, "c"), Leaf(2, "d")]),
            Leaf(2, "e"),
        ],
    )
    l = list(node.post_order())
    assert len(l) == 7
    assert l[0].type == 2
    assert l[1].type == 259
    assert l[2].type == 2
    assert l[3].type == 2
    assert l[4].type == 2
    assert l[5].type == 2
    assert l[6].type == 258




# Generated at 2022-06-13 18:19:10.238256
# Unit test for method remove of class Base
def test_Base_remove():
    g = Grammar(r"a: 'a'")
    p = g.parse("")
    assert p.remove() is None
    assert p.children[0].remove() == 0
    

# Generated at 2022-06-13 18:19:11.230607
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    pass



# Generated at 2022-06-13 18:19:18.688751
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    def test(pattern, nodes, expected, msg=None):
        if msg is None:
            msg = "%s should match %s" % (pattern, nodes)
        actual = list(pattern.generate_matches(nodes))
        if actual != expected:
            print("\nExpected: %s" % (expected,))
            print("Actual  : %s" % (actual,))
            raise AssertionError(msg)

    test("a", [Leaf("a")], [(1, {"a": [Leaf("a")]})])
    test("a", [Leaf("a"), Leaf("a")], [(1, {"a": [Leaf("a")]})])
    test("a", [Leaf("b")], [])
    test("a", [], [(0, {})])

# Generated at 2022-06-13 18:19:34.595970
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    for p in [
        Pattern(0, 1),
        Pattern(0, 1, name="foo"),
        Pattern("test"),
        Pattern("test", name="foo"),
        Pattern("test", "one"),
        Pattern("test", "one", name="foo"),
    ]:
        assert list(p.generate_matches([])) == []
        assert list(p.generate_matches([Leaf(0, 1)])) == [(1, {})]
        assert list(p.generate_matches([Leaf(0, "one")])) == []
        assert list(p.generate_matches([Leaf(1, 1)])) == []
        assert list(p.generate_matches([Leaf(1, "one")])) == []

# Generated at 2022-06-13 18:19:36.425058
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    self = BasePattern()



# Generated at 2022-06-13 18:19:44.130993
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    from . import PythonPatternParser

    p = [[NodePattern(sym.name)]]
    wild = WildcardPattern(p, min=1, name="name")
    assert wild.optimize() is wild
    wild = WildcardPattern(p, min=0, name="name")
    assert wild.optimize() is wild
    wild = WildcardPattern(p, min=0, max=1, name="name")
    assert wild.optimize() is wild
    subwild = WildcardPattern(p, min=1, max=1, name="name")
    wild = WildcardPattern(subwild)
    assert wild.optimize() is subwild
    wild = WildcardPattern(subwild, min=1, max=1)
    assert wild.optimize() is subwild

# Generated at 2022-06-13 18:19:45.448042
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    t = Base()
    assert t.get_lineno() == None



# Generated at 2022-06-13 18:19:48.093011
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    pass


# Generated at 2022-06-13 18:19:57.565877
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import ply.lex as lex
    import ply.yacc as yacc
    import io
    input = """\
module "test":
c = b"""
    tokens = (
        "NAME",
    )
    literals = "="
    def t_NAME(token):
        r"[a-zA-Z_][a-zA-Z_0-9]*"
        return token
    def t_error(token):
        token.lexer.skip(1)
    lexer = lex.lex()
    from .pgen2 import driver
    parser = driver.build_parser(grammar, outputdir="", trace=False)
    s = parser.parsesuite(input)
    for m in s.matches(NodePattern(syms.file_input)):
        print(m)
    assert set

# Generated at 2022-06-13 18:20:00.303278
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    leaf1 = Leaf(1, "a")
    leaf2 = Leaf(2, "b")
    leaf3 = Leaf(3, "c")
    node = Node(4, [leaf1, leaf2, leaf3])
    for i in node.leaves():
        print(i)


# Generated at 2022-06-13 18:20:56.835292
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():

    def setup_tree() -> "Node":
        s = "def foo(x): return x + 42\n"
        grm = Grammar()
        t = grm.parse_string(s)
        assert isinstance(t, Node)
        return t

    t = setup_tree()
    assert t.get_lineno() == 1
    assert t.children[0].get_lineno() == 1
    assert t.children[2].get_lineno() == 1
    assert t.children[3].get_lineno() == 1
    assert t.children[3].children[1].get_lineno() is None
    assert t.children[3].children[2].get_lineno() == 1



# Generated at 2022-06-13 18:21:05.831544
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .pythonparser import PythonParserSingle
    tst = "bad something simple"
    p = PythonParserSingle(tst)
    tree = p.parse()
    assert len(list(tree.pre_order())) == 3
    assert len(list(tree.post_order())) == 3
    assert next(tree.pre_order()).type == python_symbols.simple_stmt
    assert next(tree.post_order()).type == python_symbols.simple_stmt



# Generated at 2022-06-13 18:21:16.322552
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    print("test_NegatedPattern_generate_matches()")
    # run the tests
    p_STAR = WildcardPattern()
    p_STAR_STAR = WildcardPattern(min=2)
    pattern = NodePattern(type='bar')
    for test_case in ((), (1,), (1, 2), (1, 2, 3), (1, 2, 3, 4), (1, 2, 3, 4, 5)):
        test_nodes = list(map(lambda x: Leaf(type='foo', value=x), test_case))
        for count, results in p_STAR_STAR.generate_matches(test_nodes):
            assert count == 0
        for count, results in p_STAR.generate_matches(test_nodes):
            assert count == len(test_nodes)
       

# Generated at 2022-06-13 18:21:27.183240
# Unit test for method __eq__ of class Base
def test_Base___eq__():
  assert Base.__class__.__eq__ is Base.__eq__
  assert Base.__class__.__eq__('x','x') == (Base,'x','x')
  assert Base.__class__.__eq__('x',2) is NotImplemented
  assert Base.__class__.__eq__('x',None) is NotImplemented
  assert Base.__class__.__eq__(2,'x') is NotImplemented
  assert Base.__class__.__eq__(None,'x') is NotImplemented
  assert Base.__class__.__eq__(None,None) is NotImplemented
  assert Base.__class__.__eq__(2,2) is NotImplemented
  assert Base.__class__.__eq__(2,None) is NotImplemented

# Generated at 2022-06-13 18:21:33.894887
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    assert LeafPattern(token.NUMBER).match_seq([Leaf(token.NUMBER, '1234')])
    assert LeafPattern(token.NUMBER).match_seq([Leaf(token.NUMBER, '1234')])
    assert not LeafPattern(token.NUMBER).match_seq([])
    assert not LeafPattern(token.NUMBER).match_seq([Leaf(token.NUMBER)])
    assert not LeafPattern(token.NUMBER).match_seq([
        Leaf(token.NUMBER), Leaf(token.NUMBER)])



# Generated at 2022-06-13 18:21:38.533844
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == 1
    class X(object):
        pass
    X.name = "NAME"
    assert type_repr(X) == "NAME"
    X.name = "NEW NAME"
    assert type_repr(X) == "NEW NAME"



# Generated at 2022-06-13 18:21:42.035687
# Unit test for method clone of class Base
def test_Base_clone():
    import unittest

    class TestBase(unittest.TestCase):
        def test_clone(self):
            self.assertRaises(NotImplementedError, Base().clone)

    unittest.main()



# Generated at 2022-06-13 18:21:43.560758
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == "NAME"
    assert type_repr(0) == 0



# Generated at 2022-06-13 18:21:46.265006
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == "NAME"


# These two exceptions are used by the tree-walking algorithms

# Generated at 2022-06-13 18:21:55.646316
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    l1 = Leaf(1, "a")
    l2 = Leaf(2, "b")
    l3 = Leaf(3, "c")
    l4 = Leaf(4, "d")

    l1.append_child(l2)
    l2.append_child(l3)
    l3.append_child(l4)

    assert [l1, l2, l3, l4] == list(l1.pre_order())
