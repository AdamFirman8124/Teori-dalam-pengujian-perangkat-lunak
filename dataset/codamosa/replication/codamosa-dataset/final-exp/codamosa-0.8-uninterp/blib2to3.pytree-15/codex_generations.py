

# Generated at 2022-06-13 18:15:29.531882
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf

    t = Leaf(1, "")
    t.parent = t
    t.replace(Leaf(2, ""))
    assert t.parent is None



# Generated at 2022-06-13 18:15:30.353112
# Unit test for method depth of class Base
def test_Base_depth():
  assert Base().depth() == 0


# Generated at 2022-06-13 18:15:41.829905
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    def _test(nodes, pattern, exp_pairs):
        pairs = list(pattern.generate_matches(nodes))
        assert exp_pairs == pairs, (exp_pairs, pairs, pattern)
        for i, r in pairs:
            assert nodes[:i] == [r[pattern.name]], (i, r, pattern)
    for pattern_cls in [LeafPattern, NodePattern]:
        _test([Leaf(1, "a")], pattern_cls(1), [(1, {})])
        _test([Leaf(1, "a"), Leaf(1, "b")], pattern_cls(1), [(1, {})])
        _test([Leaf(1, "a"), Leaf(1, "b")], pattern_cls(1, "b"), [(1, {})])

# Generated at 2022-06-13 18:15:46.794957
# Unit test for constructor of class NodePattern
def test_NodePattern():
    t = NodePattern(type=1, content=[])
    assert t.type == 1
    assert t.content == []
    assert t.name
    t = NodePattern(type=1, content=['a'])
    assert t.type == 1
    assert t.content == ['a']
    assert t.name
    t = NodePattern(type=1, content=['a'], name='x')
    assert t.type == 1
    assert t.content == ['a']
    assert t.name == 'x'



# Generated at 2022-06-13 18:15:52.567146
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    bp = BasePattern()
    bp.type = 1
    bp.content = None
    bp.name = None
    nl: NL = Leaf(1, "1")
    nl.parent = None
    nl.children = []
    nl.bracket_depth = 0
    nl.opening_bracket = None
    nl.prefix = ""
    nl.used_names: Optional[Set[Text]] = None
    nl._prefix = ""
    nl.lineno = 0
    nl.column = 0
    nodes: List[NL] = [nl]
    it = bp.generate_matches(nodes)
    m = it.__next__()
    assert m == (1, {})


# Generated at 2022-06-13 18:15:58.183139
# Unit test for method post_order of class Base
def test_Base_post_order():
    import unittest
    import re
    class BaseTest(unittest.TestCase):
        def test_Base_post_order(self):
            from .pytree import Leaf, Node, Base
            from .pgen2 import token

            class ASTNode(Node):
                def __init__(self, type, children, leaf=None):
                    super(ASTNode, self).__init__(type, children, leaf)

                def __str__(self):
                    if self.children:
                        return "{} ({})".format(token.tok_name[self.type],
                            [str(child) for child in self.children])
                    return "{}".format(token.tok_name[self.type])

                def _eq(self, node):
                    return self.type == node.type


# Generated at 2022-06-13 18:16:03.520759
# Unit test for method leaves of class Base
def test_Base_leaves():
    class TestNode(Node):
        def leaves(self):
            for child in self.children:
                yield from child.leaves()

    node = TestNode(0, [])
    assert list(node.leaves()) == []

    leaves = [Leaf(1), Leaf(2), Leaf(3)]
    node = TestNode(0, leaves)
    assert list(node.leaves()) == leaves

    children = [Node(0, []), Leaf(2), TestNode(0, [])]
    node = TestNode(0, children)
    assert list(node.leaves()) == leaves


# Generated at 2022-06-13 18:16:11.356062
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    B = BasePattern

    class P0(B): pass
    class P1(B): type = 1
    class P2(B): type = 1; content = 1
    class P3(B): type = 1; name = 1
    class P4(B): content = 1
    class P5(B): name = 1
    class P6(B): content = 1; name = 1

    assert P0().optimize() is P0()
    assert P1().optimize() is P1()
    assert P2().optimize() is P2()
    assert P3().optimize() is P3()
    assert P4().optimize() is P4()
    assert P5().optimize() is P5()
    assert P6().optimize() is P6()



# Generated at 2022-06-13 18:16:18.954369
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pytree import Leaf
    from .pygram import python_symbols
    node = Leaf(python_symbols.minus, "-", prefix = "x")
    next_sib = Leaf(python_symbols.minus, "-", prefix = "y")
    node.append_child(next_sib)
    assert node.get_suffix() == "y"
test_Base_get_suffix()



# Generated at 2022-06-13 18:16:26.961967
# Unit test for method set_child of class Node
def test_Node_set_child():
    f = '''
    def f(a):
        for x in a:
            print(x)
    '''
    from .pytree import Leaf, Node, type_repr
    from . import pygram
    from . import pytree
    from . import python_symbols as syms
    from .parse import Lark
    from .pgen2.parse import ParseError
    p = Lark(pygram.python_grammar, start='file_input', parser='lalr')
    u = Lark(pygram.python_grammar, start='file_input', parser='earley', propagate_positions=True)
    t = p.parse(f)
    # print(t)
    t2 = pytree.type_repr(t.type)

# Generated at 2022-06-13 18:16:43.366936
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    node = [
        Node(1, [
            Leaf(1, "a"),
            Node(2, [
                Leaf(1, "b"),
                Node(2, [
                    Leaf(1, "c")]),
                Leaf(1, "d")]),
             Leaf(1, "e")]),
        Leaf(1, "f"),
        Leaf(1, "g"),
        Leaf(1, "h"),
        Node(2, [
            Leaf(1, "i"),
            Node(2, [
                Leaf(1, "j"),
                Node(2, [Leaf(1, "k")]),
                Leaf(1, "l"),
                Leaf(1, "m")]),
            Leaf(1, "n"),
            Leaf(1, "o")])]
    wild = WildcardPattern(None, 1)

# Generated at 2022-06-13 18:16:46.326919
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    import _ast
    test_Node_pre_order__1 = Node(1, [])
    test_Node_pre_order__1.pre_order()
test_Node_pre_order()



# Generated at 2022-06-13 18:16:49.649805
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    p = NegatedPattern(NodePattern(type=None))
    for c, r in p.generate_matches(nodes):
        assert False


# Generated at 2022-06-13 18:16:56.567604
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    leaf = Base()
    leaf.lineno = 1
    assert leaf.get_lineno == 1
    node = Base()
    node.children = [leaf]
    assert node.get_lineno == 1
    leafB = Base()
    leafB.lineno = 2
    node.children.append(leafB)
    assert node.get_lineno == 1


# Generated at 2022-06-13 18:17:08.403012
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    p = NegatedPattern()
    # If there is no argument, match an empty sequence
    assert [(c, r) for c, r in p.generate_matches([])] == [(0, {})]
    # Otherwise, match nothing
    p = NegatedPattern(LeafPattern(type=1))
    assert [(c, r) for c, r in p.generate_matches([Leaf(type=1)])] == []
    p = NegatedPattern(LeafPattern(type=1))
    assert [(c, r) for c, r in p.generate_matches([Leaf(type=2)])] == [(0, {})]


#
# Utility functions
#



# Generated at 2022-06-13 18:17:14.242911
# Unit test for function type_repr
def test_type_repr():
    from .pygram import python_symbols

    for name in dir(python_symbols):
        val = getattr(python_symbols, name)
        if type(val) == int:
            assert type_repr(val) == name


# Since these classes are all generated, we're not going to try to keep
# the type checker's view of these APIs very precise.

_N = TypeVar("_N", bound="Node")



# Generated at 2022-06-13 18:17:24.628690
# Unit test for method post_order of class Base
def test_Base_post_order():
    class Node(Base):
        def post_order(self):
            for child in self.children:
                for node in child.post_order():
                    yield node
            yield self
        def pre_order(self):
            yield self
            for child in self.children:
                for node in child.pre_order():
                    yield node
        def __iter__(self):
            return self.pre_order()
        def _eq(self, other):
            return self.children == other.children
        def clone(self):
            new = Node()
            new.children = self.children[:]
            for node in new.children:
                node.parent = new
            return new

    node1 = Node()
    node2 = Node()
    node3 = Node()

    node1.children.append(node2)
    node1

# Generated at 2022-06-13 18:17:28.942939
# Unit test for function type_repr
def test_type_repr():
    class PythonSymbols:
        a = 1
        b = 2
    assert type_repr(1) == "a"
    assert type_repr(2) == "b"
    assert type_repr(42) == 42



# Generated at 2022-06-13 18:17:29.797335
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    _assert(Base().get_lineno(), None)

# Generated at 2022-06-13 18:17:36.251348
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from . import token
    from .pgen2.grammar import Grammar
    from .pgen2.parse import parse_grammar_source
    from .pgen2.pgen import generate_grammar
    from .pgen2.driver import Driver
    from .pgen2.tokenize import generate_tokens
    from .pgen2.token import format_token_name
    rules = parse_grammar_source(dedent(r"""
    test: 'a' | 'b'
    """))
    g = Grammar(rules, 'test')
    driver = Driver(g, convert)
    t = driver.parse('ab', start="test")
    class Foo(BasePattern):
        def __init__(self, type: int, content: Any = None, name: Optional[Text] = None):
            self.type

# Generated at 2022-06-13 18:18:22.308610
# Unit test for method depth of class Base
def test_Base_depth():
    # Trivial test
    assert Node(1).depth() == 0
    # More complicated test
    aaa = Node(1, [Leaf(1, 'a'), Node(2, [Leaf(3, 'b')])])
    bbb = Node(4, [Leaf(5, 'c'), Leaf(6, 'c'), aaa])
    assert aaa.depth() == 1
    assert bbb.depth() == 0
    aaa.parent = bbb
    assert aaa.depth() == 1



# Generated at 2022-06-13 18:18:30.728202
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    from .pytree import Leaf, Node

    def maketree1():
        # Build the following tree:
        #   fob
        #   fob_oar
        #     obj
        #     obj_1
        #   oar
        fob = Leaf(1, "fob")
        oar = Leaf(2, "oar")
        obj = Leaf(1, "obj")
        obj_1 = Leaf(1, "obj")
        fob_oar = Node(3, [obj, obj_1])
        tree1 = Node(4, [fob, fob_oar, oar])
        return tree1


# Generated at 2022-06-13 18:18:47.716843
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .pytree import Leaf
    from . import pytree
    def t_pre_order(node):
        if isinstance(node, Leaf):
            yield node
        else:
            for ch in node.pre_order():
                yield ch
                yield node
    # Unit test for method post_order of class Base
    def t_post_order(node):
        if isinstance(node, Leaf):
            yield node
        else:
            yield node
            for ch in node.post_order():
                yield ch
    def test_tree(node):
        return list(t_pre_order(node)) == list(node.pre_order()) and list(t_post_order(node)) == list(node.post_order())

# Generated at 2022-06-13 18:18:49.357397
# Unit test for method post_order of class Node
def test_Node_post_order():
    one = Leaf(1, 'hello')
    two = Leaf(3, 'world')
    node = Node(2, [one, two])
    assert list(node.post_order()) == [one, two, node]


# Generated at 2022-06-13 18:18:58.244904
# Unit test for method remove of class Base
def test_Base_remove():
    node = Leaf(1, "")
    assert node.remove() is None

    node = Node(2, None, [])
    assert node.remove() is None

    node = Node(1, None, [Leaf(2, ""), Leaf(3, ""), Node(4, None, [])])
    assert node.remove() == 1
    assert node.children == [Leaf(2, ""), Leaf(3, ""), Node(4, None, [])]
    assert node.parent is None

    node = Node(1, None, [Leaf(2, ""), Leaf(3, ""), Node(4, None, [])])
    node = node.children[0]
    assert node.remove() == 0
    assert node.children == [Leaf(3, ""), Node(4, None, [])]
    assert node

# Generated at 2022-06-13 18:19:08.115980
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    """
    This verifies that the Base.get_sufix() method works as expected. This
    method is used in conjunction with the leaf.prefix() method for replacing
    nodes within the AST.
    """
    import six
    import ast
    import sys
    import unittest
    if six.PY3:
        import io
        StringIO = io.StringIO
    else:
        import StringIO

    # When we insert a new node into an AST, we want to modify the AST
    # so that the inserted node has the same string prefix as the
    # current node. This will ensure that the strings for the nodes
    # in the AST match the strings that originally created the AST.
    # In order to do this, we will look at the current node's next
    # sibling and use that node's prefix.
    #
    # However, the

# Generated at 2022-06-13 18:19:12.981016
# Unit test for function type_repr
def test_type_repr():
    def t(t):
        return type_repr(t)

    assert t(python_symbols.STRING) == "STRING"
    assert t(python_symbols.NAME) == "NAME"
    assert t(python_symbols.DOT) == "DOT"



# Generated at 2022-06-13 18:19:22.316718
# Unit test for constructor of class NodePattern
def test_NodePattern():
    from .pgen2.grammar import Grammar

    gr = Grammar(r"""
    root: (x='x' sp=' ')?
    """)
    xy: NodePattern
    sp: LeafPattern
    xy, sp = NodePattern(gr.symbol2number['root'], [
        NodePattern(gr.symbol2number['x'], content='x'),
        LeafPattern(gr.token2number[' '], content=' ')])
    assert xy.match_seq([])
    assert not xy.match_seq([Leaf(gr.token2number[':'], ':')])
    assert not xy.match_seq([Leaf(gr.token2number[':'], ':',
                                  prefix='\n'),
                             Leaf(gr.token2number[' '], ' ')])


# Generated at 2022-06-13 18:19:28.454613
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    for cls in LeafPattern, NodePattern, WildcardPattern:
        assert str(cls(1)), '%s("NAME")' % cls.__name__
        assert (
            str(cls(3, "xyz")),
            '%s("NAME", "xyz")' % cls.__name__,
        )
        assert (
            str(cls(3, "xyz", "name1")),
            '%s("NAME", "xyz", "name1")' % cls.__name__,
        )


# Generated at 2022-06-13 18:19:32.301602
# Unit test for method __repr__ of class Node
def test_Node___repr__():
    d = Node(type=257, children=[Leaf(value='hello', type=1), Leaf(value='world', type=1)])
    assert d.__repr__() == "Node(NAME, ['hello', 'world'])"


# Generated at 2022-06-13 18:19:43.328896
# Unit test for method depth of class Base
def test_Base_depth():
    assert Base().depth() == 0


# Generated at 2022-06-13 18:19:52.681507
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    class LeafPattern(BasePattern):
        def __init__(self, type, content=None, name=None):
            self.type = type
            self.content = content
            self.name = name

        def _submatch(self, node, results):
            return self.content is None or node.value == self.content

    class NodePattern(BasePattern):
        def __init__(self, type, content=None, name=None):
            self.type = type
            self.content = content
            self.name = name

        def _submatch(self, node, results):
            assert isinstance(node, Node), repr(node)
            return True

    def _test_submatch(cls, expected):
        import pickle

        p = cls(42)
        assert p.optimize() is p
        assert p

# Generated at 2022-06-13 18:19:58.189834
# Unit test for method pre_order of class Node
def test_Node_pre_order():
  from .pygram import python_symbols
  from .pgen2 import token
  node = Node(python_symbols.decorated,
              [Leaf(token.NAME, "f"),
               Node(python_symbols.decorator,
                    [Leaf(token.AT, "@"),
                     Leaf(token.NAME, "g")])])
  assert node.pre_order() == [node, node.children[0], node.children[1]]

# Generated at 2022-06-13 18:20:03.849865
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    from .grammar import parse_grammar, Rule

    def test(expr: str, found: bool) -> None:
        g = parse_grammar("""
            start: *;
            *: * | "abc";
        """)
        r = Rule("start", NegatedPattern(g.parse(expr)))
        m = r.match("x")
        assert bool(m) == found

    test("", True)
    test("x", True)
    test("abx", True)
    test("xy", False)
    test("xyz", False)
    test("abc", False)



# Generated at 2022-06-13 18:20:12.190340
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf
    from .python_grammar import PythonGrammar
    pygram: PythonGrammar = PythonGrammar()
    pygram.build_grammar()
    source = """
    def func():
        return True
    """
    tree = pygram.parse(source)
    leaves = list(tree.leaves())
    r_leaf = leaves[6]
    leaf = Leaf(type=1, value=2, context=None)
    leaf.parent = r_leaf.parent
    l_children = []
    found = False
    for ch in r_leaf.parent.children:
        if ch is r_leaf:
            assert not found, (r_leaf.parent.children, r_leaf, leaf)
            if leaf is not None:
                l_children.append(leaf)
            found

# Generated at 2022-06-13 18:20:22.395480
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    assert Base().get_lineno() is None
    t = Leaf(1, "foo", (1, 0))
    assert t.get_lineno() == 1
    t = Leaf(1, "foo", (10, 0))
    assert t.get_lineno() == 10
    u = Node(2, [t])
    assert u.get_lineno() == 10
    t = Leaf(1, "foo", (1, 0))
    v = Node(2, [Leaf(1, "foo", (2, 0)), t, Leaf(1, "foo", (1, 0))])
    assert v.get_lineno() == 2



# Generated at 2022-06-13 18:20:31.186199
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    file = open("testfiles/test.py")
    s = file.read()
    file.close()
    tree = grammar.parse_string(s)
    lineno = 0
    for subtree in tree.leaves():
        lineno = subtree.lineno
    print(lineno)
    last_leaf = None
    for leaf in tree.leaves():
        print(leaf.type)
        if leaf.type == token.COMMENT:
            if last_leaf is None:
                print("I am the first leaf")
            else:
                suffix = last_leaf.get_suffix()
                print("suffix is", suffix)
        last_leaf = leaf
        if leaf.type == token.NEWLINE:
            last_leaf = None


# Generated at 2022-06-13 18:20:36.948815
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    # case 1
    node = Leaf(1, "a", None, None)
    res = node.get_suffix()
    assert res is not None
    # case 2
    node = Leaf(2, "a", None, None)
    res = node.get_suffix()
    assert res is not None


# Generated at 2022-06-13 18:20:38.913232
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    with pytest.raises(NotImplementedError):
        BasePattern().generate_matches([])

    class MockPattern(BasePattern):
        pass

    pattern = MockPattern()
    with pytest.raises(TypeError):
        MockPattern.generate_matches(pattern, [])



# Generated at 2022-06-13 18:20:43.754973
# Unit test for method depth of class Base
def test_Base_depth():
    import pytree
    a = pytree.Leaf(56, "hihi")
    b = pytree.Leaf(56, "haha")
    c = pytree.Node(56, [a, b])
    assert a.depth() == 1
    assert b.depth() == 1
    assert c.depth() == 0


# Generated at 2022-06-13 18:21:09.297990
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from .pytree import Leaf, Node
    from .pygram import python_symbols as syms
    def _make_node(
        ntype: int,
        children: Union[List[NL], Optional[NL]],
        prefix: Optional[Text] = None,
    ) -> Node:
        if not isinstance(children, list):
            children = [children]
        return Node(
            ntype,
            children=[Leaf(1, child, prefix="") for child in children if child is not None],
            prefix=prefix,
        )
    # Need a way to define inline lambdas
    def _a(x): return x == 'a'
    def _b(x): return x == 'b'
    def _c(x): return x == 'c'

# Generated at 2022-06-13 18:21:15.433082
# Unit test for method depth of class Base
def test_Base_depth():
    assert Base().depth() == 0
    assert Leaf(0, "1", (1, 2)).depth() == 0
    n = Node(0, None, None, [Leaf(0, "1", (1, 2))])
    assert n[0].depth() == 1
    assert n.depth() == 0



# Generated at 2022-06-13 18:21:26.647745
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import pickle as pickle
    from .pgen2 import token
    from .pgen2 import driver
#     from . import driver
    from . import token
    driver = driver.Driver(convert)
    mod = driver.parse_string("1\n2\n3\n", "test")
    pattern = BasePattern()
#     pattern.generate_matches(mod.children)
#     print(pickle.loads(pickle.dumps(mod.children)))
    pattern.generate_matches(pickle.loads(pickle.dumps(mod.children)))
#     pattern.generate_matches(pickle.loads(pickle.dumps(mod.children)))
#     pattern.generate_matches(pickle.loads(pickle.dumps(mod.children)))
#     test_BasePattern_

# Generated at 2022-06-13 18:21:37.898021
# Unit test for function convert
def test_convert():
    from .pgen2 import driver
    from . import token

    source = """\
import os
import sys
"""
    gr = driver.load_grammar("Grammar/Grammar", convert=convert)
    parser = driver.Parser(gr)
    t = parser.parse(source, start="file_input")
    assert t.type == gr.symbol2number["file_input"]
    assert len(t.children) == 3
    assert t.children[0].type == token.NAME
    assert t.children[0].value == "import"
    assert t.children[0].prefix == "import "
    assert t.children[1].type == token.NAME
    assert t.children[1].value == "os"
    assert t.children[1].prefix == "\nimport "

# Generated at 2022-06-13 18:21:41.444003
# Unit test for method clone of class Base
def test_Base_clone():
    from .pytree import Leaf

    b = Leaf(1, "")
    c = b.clone()
    c.type = 2
    assert c.type == 2
    assert b.type == 1
    return c



# Generated at 2022-06-13 18:21:47.041372
# Unit test for method remove of class Base
def test_Base_remove():

    #
    # Global variable
    #
    p = Node(python_symbols.file_input, [])

    #
    # Method call 1
    #

    #
    # Method call 2
    #

    #
    # Method call 3
    #

    #
    # Method call 4
    #


# Generated at 2022-06-13 18:21:51.926372
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    # Test case for empty pattern
    pattern = NegatedPattern()
    assert tuple(pattern.generate_matches([])) == ((0, {}),)
    assert tuple(pattern.generate_matches([1])) == ()

    # Test case for non-empty pattern
    pattern = NegatedPattern(NodePattern(type=0))
    assert tuple(pattern.generate_matches([])) == ((0, {}),)
    assert tuple(pattern.generate_matches([1])) == ()
    assert tuple(pattern.generate_matches([0])) == ()



# Generated at 2022-06-13 18:22:00.760529
# Unit test for method post_order of class Base
def test_Base_post_order():
    from .pytree import Leaf
    from .pgen2 import token
    t = Leaf(token.NAME, 'foo')
    p = Leaf(token.LPAR, '(')
    q = Leaf(token.RPAR, ')')
    r = Leaf(token.COMMA, ',')
    u = Node(syms.testlist_comp, [p, t, q, r])

    nodes = [x for x in u.post_order()]
    assert nodes == [p, t, q, r, u]

# Generated at 2022-06-13 18:22:11.339672
# Unit test for method generate_matches of class NegatedPattern

# Generated at 2022-06-13 18:22:15.380633
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    try:
        Base()
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

