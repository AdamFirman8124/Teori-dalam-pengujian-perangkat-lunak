

# Generated at 2022-06-13 18:14:31.627004
# Unit test for method clone of class Base
def test_Base_clone():
    from . import pytree
    from .pattern_parse import pattern

    def assert_clone_equal(o, clone):
        assert o.__class__ == clone.__class__, (o, clone)
        # test _eq
        assert o == clone, (o, clone)
        assert not o != clone, (o, clone)
        # test clone
        assert o.clone() == clone, (o, clone.clone())
        # test post_order
        assert list(o.post_order()) == list(clone.post_order()), (
            list(o.post_order()), list(clone.post_order()))
        # test pre_order
        assert list(o.pre_order()) == list(clone.pre_order()), (
            list(o.pre_order()), list(clone.pre_order()))

# Generated at 2022-06-13 18:14:41.942349
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    import os, tempfile
    from lib2to3.pgen2.parse import ParseError
    from lib2to3 import pytree

    _, path = tempfile.mkstemp()

    def parse(source):
        try:
            return pytree.convert.parse(source, debug=False, start="file_input",
                                        future_features={"print_function"})
        except ParseError as exc:
            print("ParseError (%s):\n%s" % (exc.__class__.__name__, exc),
                  file=sys.stderr)
            raise
        finally:
            try:
                os.remove(path)
            except OSError:
                pass


# Generated at 2022-06-13 18:14:43.634080
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    assert Leaf(1, "x").post_order().__next__().value == "x"


# Generated at 2022-06-13 18:14:53.571468
# Unit test for method remove of class Base
def test_Base_remove():
    a = Leaf(1, "abc")
    b = Leaf(1, "xyz")
    assert a.remove() == None
    assert b.remove() == None
    a.parent = b
    b.parent = a
    assert a.remove() == 0
    assert a.parent is None
    assert b.parent is None
    assert b.remove() == 0
    assert b.parent is None
    a.parent = b
    b.children = [a]
    assert a.remove() == 0
    assert a.parent is None
    assert b.parent is None
    assert a.children == []
    assert b.children == []
    assert b.remove() == None
    assert b.parent is None
    assert b.children == []
    b.parent = a
    a.children = [b]

# Generated at 2022-06-13 18:15:08.534014
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pytree import Leaf, Node
    from .pygram import python_symbols
    from .pgen2 import token
    from . import pytree
    from .pyparse import ParseError
    pytree_obj = pytree.pytree
    pytree_obj.main()
    assert pytree_obj.test_one("", False, False) == [Node(python_symbols.file_input, [])]
    assert pytree_obj.test_one("# testing\n", False, False) == [Node(python_symbols.file_input, [Leaf(token.COMMENT, "# testing"), Leaf(token.NEWLINE, "\n")])]

# Generated at 2022-06-13 18:15:12.975243
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    import unittest


# Generated at 2022-06-13 18:15:15.237298
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    test_pattern = NegatedPattern()
    test_pattern.generate_matches([]) == [(0, {})]



# Generated at 2022-06-13 18:15:17.249946
# Unit test for method post_order of class Base
def test_Base_post_order():
    assert True
    # assert False # TODO: implement your test here


# Generated at 2022-06-13 18:15:31.778555
# Unit test for method post_order of class Base
def test_Base_post_order():
    from .pytree import Leaf, Node
    from .python_tree import PythonLeaf, PythonNode

    def check(t, post):
        res = list(t.post_order())
        assert res == post, "{}\n{}".format(res, post)

    # Test Leaf
    t = Leaf(1, "x")
    check(t, [t])
    # Test a tree with mixed type
    t = Node(1, [t, PythonLeaf(2, "y")])
    check(t, [t, Leaf(1, "x"), PythonLeaf(2, "y")])
    # Test a tree with mixed type and mixed height
    t = Node(1, [t, PythonNode(2, [PythonLeaf(3, "z")])])

# Generated at 2022-06-13 18:15:39.925265
# Unit test for method remove of class Base
def test_Base_remove():
    source = b'x = y + z'
    from .pytree import convert
    from .parse import Parser
    parser = Parser()
    tree = convert(parser.parse_source(source))
    leaves = list(tree.leaves())
    # Get last leaf
    l = leaves[-1]
    # Delete last leaf
    l.remove()
    # Check there are now two leaves fewer
    assert len(leaves) == len(list(tree.leaves())) + 2



# Generated at 2022-06-13 18:15:59.296848
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    l1 = Leaf(0,"l1")
    l2 = Leaf(1,"l2")
    l3 = Leaf(2,"l3")
    l4 = Leaf(3,"l4")

    test_leaf = l2
    test = [l2]
    for item in test_leaf.post_order():
        assert(item in test)


# Generated at 2022-06-13 18:16:07.058655
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    # Since Base is an abstract class, we have to create a dummy subclass
    # with the minimal required functionality

    class _BaseSub(Base):

        def __init__(self, value):
            self.value = value

        def _eq(self, other):
            return self.value == other.value

        def clone(self):
            return _BaseSub(self.value)

        def post_order(self):
            return [self]

        def pre_order(self):
            return [self]

    a = _BaseSub(1)
    b = _BaseSub(1)
    c = _BaseSub(2)
    assert a == a
    assert a == b
    assert a != c



# Generated at 2022-06-13 18:16:15.325325
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    # Simplest case
    assert list(NegatedPattern(None).generate_matches([])) == [(0, {})]
    assert list(NegatedPattern(None).generate_matches([4, 5, 6])) == []

    # Basic case
    wp = WildcardPattern()
    np = NegatedPattern(wp)
    for i in [1, 4, 5, 6]:
        assert list(np.generate_matches([i])) == []
    assert list(np.generate_matches([])) == [(0, {})]

    # More complicated content
    wp = WildcardPattern(content=[(LeafPattern(58),), (LeafPattern(59),), (LeafPattern(60),)])
    np = NegatedPattern(wp)

# Generated at 2022-06-13 18:16:21.913504
# Unit test for method clone of class Base
def test_Base_clone():
    class Tester(Base):
        def __init__(self, parent, type, value=None, children=None):
            self.type = type
            self.parent = parent
            if children is None:
                self.children = []
            else:
                self.children = children
                for child in self.children:
                    child.parent = self

        def _eq(self, node):
            return (self.type == node.type and
                    self.children == node.children)

        def clone(self):
            return Tester(None, self.type, children=self.children)

        def pre_order(self):
            yield self
            for child in self.children:
                for x in child.pre_order():
                    yield x


# Generated at 2022-06-13 18:16:30.933001
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    import unittest

    class FooPattern(BasePattern):
        def _submatch(self, node, results):
            return node.value == "foo"

    class TestMatchSeq(unittest.TestCase):
        def test_match_seq_one(self):
            a = Leaf(1, "foo")
            p = FooPattern(1)
            self.assertTrue(p.match_seq([a]))

        def test_match_seq_fail_type(self):
            a = Leaf(2, "foo")
            p = FooPattern(1)
            self.assertFalse(p.match_seq([a]))

        def test_match_seq_fail_content(self):
            a = Leaf(1, "bar")
            p = FooPattern(1)

# Generated at 2022-06-13 18:16:39.065924
# Unit test for method pre_order of class Base
def test_Base_pre_order():

    g = Grammar()
    g.load_grammar('testdata/grammars/simple.grm')
    l = [
        Leaf(1, '11', (0, 1)),
        Node(2, [
            Leaf(3, '31', (1, 1)),
            Leaf(4, '41', (1, 1)),
        ], (1, 2)),
    ]
    n = g.build_ast(l)
    nl = list(n.pre_order())
    assert nl == [n, n.children[0], n.children[1], n.children[1].children[0], n.children[1].children[1]]


# Generated at 2022-06-13 18:16:45.194858
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .tree import Node
    n = Node(None, [Node(None, [Node(None, [])]), Node(None, [])])
    assert list(n.pre_order()) == [n, n.children[0], n.children[1], n.children[0].children[0], n.children[1].children[0]]


# Generated at 2022-06-13 18:16:51.338442
# Unit test for function type_repr
def test_type_repr():
    for n in range(20):
        assert type_repr(n) == n

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

# The following class and associated functions are used to track
# locations of literal strings in the source code.  This is used
# to generate accurate error messages when parsing Python.

# The class represents a contiguous location in the source code.
# It could be a location of a single symbol, such as an identifier,
# or a location spread across several lines, such as a multi-line
# string literal.

# Generated at 2022-06-13 18:16:56.178262
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    parse_tree = Node(1, [Leaf(1, ""), Leaf(1, "")])
    for node in parse_tree.pre_order():
        assert type(node) is Node or type(node) is Leaf



# Generated at 2022-06-13 18:17:09.076411
# Unit test for method depth of class Base
def test_Base_depth():
    from .pgen2 import tokenize
    from .pygram import python_symbols

    g = Grammar(getattr(python_symbols, "single_input"),
                getattr(python_symbols, "file_input"))
    s = "# comment\ndef foo():\n    return 0\n"
    toks = list(tokenize.generate_tokens(StringIO(s).readline))
    node = g.parse(toks)
    assert isinstance(node, Leaf)
    assert node.depth() == 0
    assert isinstance(node.parent, Node)
    assert node.parent.depth() == 1
    assert isinstance(node.parent.parent, Node)
    assert node.parent.parent.depth() == 2
    assert node.parent.parent.parent is None



# Generated at 2022-06-13 18:17:31.094339
# Unit test for method leaves of class Base
def test_Base_leaves():
    import lib2to3.pytree as pytree
    tree = pytree.Node(type=1,
                       children=[pytree.Node(type=2,
                                             children=[pytree.Leaf(type=3,
                                                                   value='a'),
                                                       pytree.Leaf(type=3,
                                                                   value='b'),
                                                       pytree.Leaf(type=3,
                                                                   value='c')]),
                                 pytree.Node(type=4,
                                             children=[pytree.Leaf(type=5,
                                                                   value='d'),
                                                       pytree.Leaf(type=5,
                                                                   value='e'),
                                                       pytree.Leaf(type=5,
                                                                   value='f')])])


# Generated at 2022-06-13 18:17:42.381444
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    from .pgen2.grammar import Grammar


# Generated at 2022-06-13 18:17:48.768986
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Leaf, Node
    from .pgen2 import token

    n = Node(token.NAME, [Leaf(token.NAME, 'spam'), Leaf(token.NAME, 'eggs')])
    assert n.depth() == 0

    n = Node(token.NAME, [n, Leaf(token.NAME, 'ham')])
    assert n.depth() == 1
test_Base_depth()  # noqa



# Generated at 2022-06-13 18:17:56.655079
# Unit test for method set_child of class Node
def test_Node_set_child():
    n = Node(NULL, [])
    n.set_child(0, n)
    n.set_child(1, n)
    n.set_child(2, n)
    n.set_child(3, n)
    n.set_child(4, n)
    n.set_child(5, n)
    n.set_child(6, n)
    n.set_child(7, n)
    n.set_child(8, n)
    n.set_child(9, n)



# Generated at 2022-06-13 18:18:07.650424
# Unit test for function generate_matches
def test_generate_matches():
    assert list(generate_matches([NodePattern(type=foo)], [NL(type=foo)])) == [(1, {})]
    assert list(generate_matches([NodePattern(type=foo)], [])) == []
    assert list(generate_matches([WildcardPattern()], [NL(type=foo)])) == [(1, {})]
    assert list(generate_matches([WildcardPattern()], [])) == [(0, {})]
    assert list(generate_matches([WildcardPattern()], [NL(type=foo), NL(type=bar)])) == [(2, {})]
    assert list(generate_matches([WildcardPattern(), NodePattern(type=foo)], [NL(type=foo)])) == [(1, {})]

# Generated at 2022-06-13 18:18:14.996688
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    # A pattern that matches either a single leaf or an arbitrary sequence
    # of leafs:
    dotdot = WildcardPattern(None, 0, HUGE)

    # A pattern that matches a sequence of length 1 or 2 consisting of
    # NAME, DOT, and/or DOTDOT nodes:
    import_stmt = WildcardPattern([[NodePattern(atom.DOT)], [NodePattern(atom.DOTDOT)]], 1, 2)

    # A pattern that matches a node with a single subpattern that
    # matches either a NAME or an "import_stmt"?
    dotted_name = NodePattern(
        type=atom.DOTTED_NAME,
        content=[[NodePattern(atom.NAME)], import_stmt],
    )

    # A pattern that matches a node with a single subpattern that
    # matches an "import_

# Generated at 2022-06-13 18:18:24.033153
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
  # Test that the first node in a leaf has the same line number and
  # the leaf
  node = Node(type=1, children=[Leaf(type=2, lineno=5)])
  assert node.get_lineno() == 5
  # Test that subsequent children have the same line number
  node = Node(
      type=1, children=[Leaf(type=2, lineno=5), Leaf(type=2, lineno=5)])
  assert node.get_lineno() == 5
  # Test that the first child node has a different line number
  node = Node(
      type=1, children=[Leaf(type=2, lineno=5), Node(type=1, lineno=8)])
  assert node.get_lineno() != 5
  assert node.get_lineno() != 8
  #

# Generated at 2022-06-13 18:18:28.146104
# Unit test for function convert
def test_convert():
    # TODO: Use unittest here
    from . import driver

    g = driver.load_grammar("Python.asdl")

# Generated at 2022-06-13 18:18:33.373242
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Leaf, Node
    # 0
    assert Base().depth() == 0
    # 1
    assert Leaf(1, "hi").depth() == 0
    assert Node(2, [Leaf(1, "hi")]).depth() == 0
    # 2
    assert Node(2, [Node(3, [Leaf(1, "hi")])]).depth() == 1
    assert Node(
        2,
        [
            Node(
                3,
                [
                    Node(
                        4,
                        [Leaf(1, "hi")]
                    )
                ]
            )
        ]
    ).depth() == 2
    # 3

# Generated at 2022-06-13 18:18:48.699204
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    def get_lineno_test(nodes, linenos):
        assert len(nodes) == len(linenos)
        for node, lineno in zip(nodes, linenos):
            assert node.get_lineno() == lineno

    get_lineno_test([Leaf(1, "foo", (1, 0))], [1])
    get_lineno_test([Node(1, [Leaf(1, "foo", (2, 0))]), Node(1, [Leaf(1, "foo", (2, 3))])], [2, 2])
    get_lineno_test([Leaf(1, "foo", (1, 0)), Node(1, [Leaf(1, "foo", (2, 3))])], [1, 2])

# Generated at 2022-06-13 18:19:39.880675
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    ll = Leaf(1, "hello")
    l = ll.leaves()
    print(list(l))
    
test_Leaf_leaves()

# Generated at 2022-06-13 18:19:43.374563
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    """Unit test for method leaves of class Leaf"""
    leaf = Leaf(0, "")
    yield assert_raises_typing, leaf.leaves, ()



# Generated at 2022-06-13 18:19:45.492567
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    assert isinstance(object(), object)
    assert not isinstance(1, object)
    assert not isinstance(Exception(), int)

# Generated at 2022-06-13 18:19:53.900151
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    """
    Check if the optimize function of class BasePattern behaves
    as expected.
    """
    # Check return of optimize if class is a LeafPattern
    if isinstance(BasePattern, LeafPattern):
        assert BasePattern.optimize() is BasePattern
    # Check return of optimize if class is a NodePattern
    elif isinstance(BasePattern, NodePattern):
        assert BasePattern.optimize() is BasePattern
    # Check return of optimize if class is a WildcardPattern
    else:
        assert BasePattern.optimize() is BasePattern



# Generated at 2022-06-13 18:20:02.974447
# Unit test for method set_child of class Node
def test_Node_set_child():
    import sys
    import io
    from contextlib import contextmanager

    @contextmanager
    def capture_stdout():
        old = sys.stdout
        capturer = io.StringIO()
        sys.stdout = capturer
        try:
            yield capturer
        finally:
            sys.stdout = old

    n = Node(256, [Leaf(1, ""), Leaf(2, "")])
    n.children[0].prefix = " "
    n.set_child(0, Leaf(1, ""))
    assert n.children[0].prefix == ""
    assert n.children[0].next_sibling.prefix == " "
    with capture_stdout() as out:
        print(n.children[0].next_sibling.prefix)
    assert out.getvalue() == ' '

#

# Generated at 2022-06-13 18:20:08.794917
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pgen2 import driver
    from .pygram import python_symbols
    drv = driver.Driver(start=python_symbols.file_input)
    # Test 1
    x = drv.parse_string("a = 1\n")
    leaf = x.children[0].children[1]
    assert leaf.get_suffix() == "\n"
    # Test 2
    x = drv.parse_string("a = 1\n  b = 2")
    leaf = x.children[0].children[1]
    assert leaf.get_suffix() == "\n  "
    # Test 3
    x = drv.parse_string("a = 1  b = 2")
    leaf = x.children[0].children[1]
    assert leaf.get_suffix() == "  "


# Generated at 2022-06-13 18:20:19.357503
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    from .firstsets import FirstSet
    p = BasePattern()
    f = FirstSet()
    f.add_nt("a")
    f.add_nt("b")
    f.add_nt("c")
    f.add_nt("d")
    f.add_nt("e")
    f.compute_lookahead()
    assert f.lookahead == {'a': {'a'}, 'b': {'b'}, 'c': {'c'}, 'd': {'d'}, 'e': {'e'}}
test_BasePattern_match_seq()


# Generated at 2022-06-13 18:20:28.516783
# Unit test for method depth of class Base
def test_Base_depth():
    _parent = Node(2, None, None, [Leaf(2, "5", (1, 0), None, None)])
    _child = Node(2, None, None, [Leaf(2, "5", (1, 0), None, None)])
    _child.parent = _parent
    _child.parent = _parent
    _parent.parent = None
    _child.parent = _parent
    _child.parent = _parent
    _parent.parent = None
    _child.parent = _parent
    _child.parent = _parent
    assert _child.depth() == 1, "test_Base_depth failed"



# Generated at 2022-06-13 18:20:33.651777
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    from .pgen2.token import tok_name

    p = LeafPattern(tok_name["NAME"], "foo")
    assert repr(p).startswith(
        "LeafPattern(NAME, "
    ), "Unexpected string representation for LeafPattern"
    p = NodePattern(tok_name["NAME"], "foo")
    assert repr(
        p
    ).startswith(
        "NodePattern(NAME, "
    ), "Unexpected string representation for NodePattern"
    p = WildcardPattern(tok_name["NAME"], "foo")
    assert repr(
        p
    ).startswith(
        "WildcardPattern(NAME, "
    ), "Unexpected string representation for WildcardPattern"



# Generated at 2022-06-13 18:20:34.965072
# Unit test for method pre_order of class Leaf

# Generated at 2022-06-13 18:21:20.658182
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    import unittest

    class Test(unittest.TestCase):

        def test_optimize(self):
            from .pgen2 import token

            src = "if x: pass"
            node = generate_grammar("Grammar", src, {}, {}).parse(src)
            assert node.children[-1].prefix == "\n"

            # Strip trailing whitespace.
            p = NodePattern(type=syms.simple_stmt, children=[LeafPattern(type=token.NAME, content="pass"), Pattern(r"[ \t]+\n")])

            stripped_node = p.optimize().apply(node)[0]
            assert len(stripped_node.children) == 2
            assert stripped_node.children[1] == Leaf(token.NEWLINE, "\n")

    suite = unittest.TestSu

# Generated at 2022-06-13 18:21:26.597055
# Unit test for method post_order of class Base
def test_Base_post_order():
    input_str = """\
    x
    y
    """
    module = python_grammar.parse(input_str)
    my_iter = module.post_order()
    assert next(my_iter).prefix == 'x'
    assert next(my_iter).prefix == '\n'
    assert next(my_iter).prefix == 'y'
    assert next(my_iter).prefix == '\n'
    assert next(my_iter).prefix == '\n'


# Generated at 2022-06-13 18:21:37.822461
# Unit test for method remove of class Base
def test_Base_remove():
    # get_sibling_nodes
    a = Node(type=python_symbols.arglist, children=[])

    # get_sibling_nodes
    b = Node(type=python_symbols.arglist, children=[])
    a.children.append(b)

    for node in [a, b]:
        for sibling in [a, b]:
            if node is not sibling:
                assert node.next_sibling is sibling
                assert node.prev_sibling is sibling

    # remove
    b.remove()
    assert a.next_sibling is None and a.prev_sibling is None
    assert b.next_sibling is None and b.prev_sibling is None

    # remove
    a.children.append(b)
    a.remove()

# Generated at 2022-06-13 18:21:45.826802
# Unit test for method post_order of class Base
def test_Base_post_order():
    from .pytree import Node

    def check_post_order(expected: List[int], node: Base) -> None:
        for i, leaf in enumerate(node.post_order()):
            assert isinstance(leaf, Leaf)
            assert leaf.value == expected[i]

    check_post_order(
        [1, 2, 3],
        Node(
            1,
            [
                Leaf(1, "a"),
                Node(
                    2,
                    [
                        Leaf(2, "b"),
                        Node(3, [Leaf(3, "c"), Leaf(3, "d")]),
                    ],
                ),
            ],
        ),
    )
    check_post_order([1], Node(1, []))



# Generated at 2022-06-13 18:21:52.342420
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    assert str(WildcardPattern().optimize()) == "."
    assert str(WildcardPattern([].optimize()).optimize()) == ".+"
    assert str(WildcardPattern(name="a").optimize()) == "a = ."
    assert str(WildcardPattern([], name="a").optimize()) == "a = .+"
    assert str(WildcardPattern([[]]).optimize()) == ".+"
    assert str(WildcardPattern([[], []]).optimize()) == ".+"
    assert str(WildcardPattern([[NodePattern()]]).optimize()) == ".+"
    assert str(WildcardPattern([[NodePattern()], []]).optimize()) == ".+"
    assert str(WildcardPattern([[NodePattern()], []]).optimize()) == ".+"

# Generated at 2022-06-13 18:21:57.199852
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    from . import pytree

    # Called on Base().  Should not crash.
    pytree.Base()._eq(pytree.Base())
    # Ensure that we get NotImplemented.
    assert pytree.Base()._eq(1) == NotImplemented



# Generated at 2022-06-13 18:22:06.277554
# Unit test for method clone of class Base
def test_Base_clone():
    from .pytree import Leaf, Node, Base, Whitespace
    orig = Node(1, [Leaf(1, "foo"), Node(1, [Leaf(1, "bar")]), Leaf(1, "baz")])
    clone = orig.clone()
    assert clone is not orig
    assert clone == orig
    assert clone.prefix == orig.prefix
    # Make sure the prefix can be set
    clone.prefix = "!"
    assert clone.prefix == "!"
    assert orig.prefix != clone.prefix
    # Make sure the children were cloned too
    assert orig.children[0] != clone.children[0]
    assert orig.children[1] != clone.children[1]
    orig.children[0].type = 2
    assert orig.children[0] != clone.children[0]
    # Make sure clone has

# Generated at 2022-06-13 18:22:14.615799
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Leaf
    l1 = Leaf(1, 'a')
    l2 = Leaf(1, 'b')
    l3 = Leaf(1, 'c')
    l4 = Leaf(1, 'd')
    l5 = Leaf(1, 'e')
    l6 = Leaf(1, 'f')
    l7 = Leaf(1, 'g')
    l8 = Leaf(1, 'h')
    tree = Node(1, [l1, Node(2, [l2, Node(3, [l3, Node(4, [l4, l5])]), l6]), l7, l8])
    assert [l for l in tree.leaves()] == [l1, l2, l3, l4, l5, l6, l7, l8]

# Generated at 2022-06-13 18:22:16.952371
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    from . import grammar

    g = grammar.Grammar()

    assert g.wild_id.optimize() is g.wild_id



# Generated at 2022-06-13 18:22:25.967150
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    import sys
    import pickle
    from pprint import pprint

    from . import pgen2
    from .pgen2 import driver

    d = driver.Driver(convert, pgen2.grammar, start="start", debug=False)
    p = d.parse("a = 1 + 2 * 3")
    assert p
