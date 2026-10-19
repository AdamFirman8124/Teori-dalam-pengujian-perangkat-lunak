

# Generated at 2022-06-13 18:13:45.784192
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    leaf = Leaf(1, 'b', prefix='a')
    assert list(leaf.pre_order()) == [leaf]


# Generated at 2022-06-13 18:13:55.225946
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    import pytest
    from .pgen2.token import tok_name
    from .pgen2.pgen import Grammar, BasePattern, convert, generator

    gr = Grammar()

    g = generator.Generator(gr)

    nl1 = convert(gr, g.generate("print"))
    nl2 = convert(gr, g.generate("(x)"))
    nl3 = convert(gr, g.generate("def f(): pass"))

    class TestPattern(BasePattern):
        def __init__(self, type, content=None, name=None):
            self.type = type
            self.content = content
            self.name = name

    def t(nodelist):
        return [tok_name[n.type] for n in nodelist]


# Generated at 2022-06-13 18:14:04.641183
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    import ast
    import sys

    class Pattern(BasePattern):
        def __init__(self, name: Text) -> None:
            BasePattern.__init__(self)
            self.name = name

        def match(self, node, results=None) -> bool:
            assert isinstance(node, ast.AST)
            return isinstance(node, ast.FunctionDef)

        def generate_matches(self, nodes) -> Iterator[Tuple[int, _Results]]:
            assert isinstance(nodes, list)
            r = {}
            r[self.name] = []
            for node in nodes:
                assert isinstance(node, ast.AST)
                if isinstance(node, ast.FunctionDef):
                    r[self.name].append(node)
                    break
            yield 1, r

    p = Pattern

# Generated at 2022-06-13 18:14:16.447157
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    import unittest
    import pgen2

    class EmptyPattern(pgen2.pattern.BasePattern):

        def __repr__(self):
            return self.__class__.__name__

        def match(self, node, results):
            return False

        def match_seq(self, nodes, results):
            return False

    class SimplePattern(pgen2.pattern.BasePattern):

        def __init__(self, name, node_type, value=None):
            pgen2.pattern.BasePattern.__init__(self, node_type, value, name)

        def _submatch(self, node, results):
            if results is not None:
                results[self.name] = node
            return True


# Generated at 2022-06-13 18:14:22.131340
# Unit test for constructor of class NodePattern
def test_NodePattern():
    import unittest

    class Data:
        def __init__(self, type, content, name, expected):
            self.type = type
            self.content = content
            self.name = name
            self.expected = expected

    class TestCase(unittest.TestCase):
        def test(self):
            for d in data:
                node = NodePattern(d.type, d.content, d.name)
                self.assertEqual(node.type, d.expected[0])
                self.assertEqual(node.content, d.expected[1])
                self.assertEqual(node.name, d.expected[2])


# Generated at 2022-06-13 18:14:30.496924
# Unit test for method post_order of class Node
def test_Node_post_order():
    from .pytree import Leaf, Node
    from .pygram import python_symbols
    from .python_tree import mod
    argv = [sys.argv[0], "--from3", "--emit3", "--print", "test/test_node.py"]
    mod(argv)
    tree = mod._main_tree

# Generated at 2022-06-13 18:14:32.587383
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == 1
    assert type_repr(python_symbols.NAME) == "NAME"



# Generated at 2022-06-13 18:14:42.807991
# Unit test for method remove of class Base
def test_Base_remove():
    import random
    import unittest

    def get_random_tree(n):
        tree = Node(random.randint(0, 256))
        for i in range(n):
            tree.append_child(Node(random.randint(0, 256)))
        return tree

    def is_tree_in_order(tree):
        for i, c in enumerate(tree.children):
            for c2 in tree.children[:i]:
                if c is c2:
                    return False
        for c in tree.children:
            if not is_tree_in_order(c):
                return False
        return True


    class BaseTest(unittest.TestCase):
        def test_remove(self):
            tree = get_random_tree(100)

# Generated at 2022-06-13 18:14:53.750976
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    pattern = NodePattern(1)
    actual: Text = repr(pattern)
    expected = 'NodePattern(1, None, None)'
    assert actual == expected, '%r != %r' % (actual, expected)

    pattern = NodePattern(1, name='test_name', content=1)
    actual: Text = repr(pattern)
    expected = "NodePattern(1, 1, 'test_name')"
    assert actual == expected, '%r != %r' % (actual, expected)

    pattern = LeafPattern(1)
    actual: Text = repr(pattern)
    expected = 'LeafPattern(1, None, None)'
    assert actual == expected, '%r != %r' % (actual, expected)

    pattern = LeafPattern(1, name='test_name', content=1)
    actual: Text = repr

# Generated at 2022-06-13 18:14:58.013986
# Unit test for method post_order of class Node
def test_Node_post_order():
    instance = Node(1, [])
    result = list(instance.post_order())
    assert result == [instance]


# Generated at 2022-06-13 18:15:51.692297
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    import support
    r_test_Base___eq__ = None
    r_test_Base___eq__ = None
    r_test_Base___eq__ = None
    r_test_Base___eq__ = None
    support.compare(r_test_Base___eq__, "Base.__eq__")

# Generated at 2022-06-13 18:15:53.980937
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    t = Leaf(4, 'a')
    for child in t.pre_order():
        assert child.type == 4
        assert child.value == 'a'

# Generated at 2022-06-13 18:16:03.808937
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    from . import pygram
    from .pgen2 import driver

    # TODO: Track down and fix the bug where I go wrong if I start
    # by reading the prefix of the first node.
    gr = pygram.python_grammar_no_print_statement
    pat = NodePattern(type=gr.number2symbol[gr.syms.simple_stmt], name="stmt")
    pat = pat.compile(gr)
    d = driver.Driver(gr, convert)
    t = d.parse_string("a\nb", "file")
    it = pat.generate_matches(t.children)
    assert next(it) == (1, {"stmt": t.children[0]})
    assert next(it) == (1, {"stmt": t.children[1]})

# Generated at 2022-06-13 18:16:12.436977
# Unit test for method clone of class Leaf
def test_Leaf_clone():
    # Leaf.clone
    a = Leaf(1, "abc")
    a._prefix = " + "
    b = a.clone()
    a.value = "def"
    assert b.value == "abc"
    a._prefix = " - "
    assert b.prefix == " + "
    a.prefix = " + "
    assert b.prefix == " + "
    a.prefix = " - "
    assert b.prefix == " + "

    a = Leaf(1, "abc")
    a.prefix = "defg"
    b = a.clone()
    assert a.prefix == b.prefix
    assert a.prefix == "defg"
    a.prefix = "hijk"
    assert b.prefix == "defg"
    assert a.prefix == "hijk"



# Generated at 2022-06-13 18:16:15.039746
# Unit test for method depth of class Base
def test_Base_depth():
    leaf = Leaf(1, 'test')
    node = Node(1, [leaf])
    assert node.depth() == 0



# Generated at 2022-06-13 18:16:16.235982
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    leaf = Leaf(3, "ab")
    assert leaf.pre_order() == iter([leaf])



# Generated at 2022-06-13 18:16:25.500747
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    from .pgen2.grammar import COLON, COMMA, DEDENT, ENDMARKER, INDENT, NAME, NEWLINE, NUMBER, RPAR, string_build

    def init(pattern):
        return pattern.match_seq(tokens)

    tokens = [Leaf(NUMBER, "1")]
    pattern = LeafPattern(NUMBER)
    assert init(pattern), "LeafPattern.match_seq: 1"

    tokens = [Leaf(COLON, ":")]
    pattern = LeafPattern(COLON)
    assert init(pattern), "LeafPattern.match_seq: 2"

    tokens = [Leaf(NAME, "foo")]
    pattern = LeafPattern(NAME)
    assert init(pattern), "LeafPattern.match_seq: 3"


# Generated at 2022-06-13 18:16:33.284562
# Unit test for method post_order of class Node
def test_Node_post_order():
    import lib2to3.tests
    pygram = lib2to3.tests.support.pygram
    pytree = lib2to3.tests.support.pytree
    from .tree import _Node
    from .tree import _Leaf
    from .pygram import python_symbols
    n = Node(python_symbols.file_input, [
        Node(1, [
            Leaf(4, 'print'),
            Node(5, [
                Leaf(6, '"'),
                Leaf(7, 'Hello'),
                Leaf(7, 'World!'),
                Leaf(6, '"'),
            ]),
            Leaf(8, '\n'),
        ]),
    ])
    assert isinstance(n, _Node)
    assert n.type == pygram.python_symbols.file_input
   

# Generated at 2022-06-13 18:16:45.380698
# Unit test for method replace of class Base
def test_Base_replace():
    #         0
    #        / \
    #       1   2
    #      /
    #     3
    root = Node(0, [Leaf(1, "L"), Leaf(2, "R")])
    root.children[0].parent = root
    root.children[1].parent = root
    root.children[0].children.append(Leaf(3, "M"))
    root.children[0].children[0].parent = root.children[0]
    root.invalidate_sibling_maps()
    root.replace(Leaf(4, "N"))
    assert root.children[0].type == 4
    assert root.children[0].prefix == "N"
    assert root.children[0].parent == root
    assert root.children[0].next_sibling.prefix == "R"


# Generated at 2022-06-13 18:16:51.241791
# Unit test for method leaves of class Base
def test_Base_leaves():
    import unittest
    from .pytree_Leaf import Leaf
    from .pytree_Node import Node
    from .pygram import python_symbols
    unittest.TestCase()
    Node(python_symbols.file_input, [Leaf(1, "1"), Leaf(1, "2")])
    Node(python_symbols.file_input, [Node(python_symbols.funcdef, [Leaf(1, "4"), Leaf(1, "5")]), Leaf(1, "6")])


# Generated at 2022-06-13 18:17:28.256689
# Unit test for constructor of class NodePattern
def test_NodePattern():
    # Test for type >= 256
    NodePattern(257)
    try:
        NodePattern(255)
    except AssertionError:
        err = sys.exc_info()[1]
        if not err.args:
            raise
        assert err.args[0].startswith("type")
    # Test for content not str
    try:
        NodePattern(257, "spam")
    except AssertionError:
        err = sys.exc_info()[1]
        if not err.args:
            raise
        assert err.args[0].startswith("content")



# Generated at 2022-06-13 18:17:34.604616
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Leaf
    from .pytree import Node
    from .pytree import Leaf
    d = Node(symbol.funcdef, [Leaf(1, 'foo'), Leaf(3, '('), Leaf(4, ')'), Leaf(5, ':'), Leaf(6, '\n'), Leaf(7, '    '), Leaf(8, 'pass'), Leaf(9, '\n')])
    assert d.depth() == 0
    a = Node(symbol.suite, [d])
    assert d.depth() == 1
    assert a.depth() == 0
    b = Node(symbol.suite, [a])
    assert d.depth() == 2
    assert a.depth() == 1
    assert b.depth() == 0
    c = Node(symbol.suite, [b])

# Generated at 2022-06-13 18:17:45.398146
# Unit test for method remove of class Base
def test_Base_remove():
    from . import pytree

    t1 = pytree.Node(1, [])
    t2 = pytree.Node(42, [], prefix=" ")
    t3 = pytree.Node(42, [], prefix=" ")
    t4 = pytree.Node(4, [], prefix="\n")
    t1.append_child(t2)
    t1.append_child(t3)
    t1.append_child(t4)
    t1.remove()
    assert t1.remove() is None
    t1.append_child(t2)
    t1.append_child(t3)
    t1.append_child(t4)

    assert t2.remove() == 1
    assert len(t1.children) == 2
    assert t1.children[0] is t3

# Generated at 2022-06-13 18:17:51.927594
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    g = Grammar()
    l = Leaf(1, '', (1, 1))
    n = Node(1, '', (2, 2), [l])
    assert n.get_lineno() == 1
    p = Node(1, '', (3, 3), [l, n])
    assert p.get_lineno() == 1


# Generated at 2022-06-13 18:17:53.808678
# Unit test for method __repr__ of class Node
def test_Node___repr__():
    assert repr(Node(257, [Leaf(1, '')])) == "Node(file_input, [Leaf(1, '')])"


# Generated at 2022-06-13 18:17:58.446770
# Unit test for method depth of class Base
def test_Base_depth():
    for meth in [Base.__init__, Base.__eq__, Base.__new__, Base.__hash__]:
        assert meth is Base.depth, (meth, Base.depth)
    a = Base()
    try:
        a.depth()
    except BaseException:
        pass

# Generated at 2022-06-13 18:18:04.130799
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Leaf, Node
    leaf1 = Leaf('leaf1', 1)
    leaf2 = Leaf('leaf2', 1)
    node1 = Node('node1', [leaf1, leaf2])
    node2 = Node('node2', [node1])
    assert list(node2.leaves()) == [leaf1, leaf2]


# Generated at 2022-06-13 18:18:06.862013
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    b = Base()
    try:
        b.get_lineno()
        assert 0
    except NotImplementedError:
        pass


# Generated at 2022-06-13 18:18:21.870409
# Unit test for method clone of class Node
def test_Node_clone():
    import pgen2
    import pprint
    import pyparsing
    g = pgen2.pgen(pgen2.tokenize.detect_encoding(sys.stdin.buffer.readline)[0], "Grammar.txt")
    mod = g.parseFile(sys.stdin, parseAll=True)
    assert mod.was_changed == False
    assert mod.was_checked == False
    assert mod.fixers_applied is None
    assert mod.used_names is None
    assert mod.type == python_symbols.file_input
    assert mod.parent is None
    assert len(mod.children) == 1
    assert mod.children[0].type == python_symbols.stmt
    assert mod.children[0].parent is mod
    assert mod.children[0].prefix == ''

# Generated at 2022-06-13 18:18:30.409513
# Unit test for method post_order of class Leaf

# Generated at 2022-06-13 18:19:06.294764
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
  l=Leaf(1,"a")
  assert l.type==1
  assert l.value=="a"
  assert l.post_order()==1


# Generated at 2022-06-13 18:19:14.635749
# Unit test for method remove of class Base
def test_Base_remove():
    from . import pytree

    def check(parent_input, child_input, expected):
        # Construct parent and child
        parent, child = eval(parent_input), eval(child_input)

        # Check that child is in parent's children, then remove it
        assert child in parent.children
        i = parent.children.index(child)
        result = child.remove()

        # Make sure the index of removal is as expected
        assert result == i, "Expected: {} Got: {}".format(i, result)

        # Make sure the child is removed
        assert parent.children == expected, "Expected: {} Got: {}".format(expected, parent.children)

    check("Name('abc')", "'def'", [])
    check("Name('abc')", "Name('def')", [])

# Generated at 2022-06-13 18:19:22.855442
# Unit test for method clone of class Base
def test_Base_clone():
    import unittest
    from unittest import mock

    from .pytree import Node, Leaf

    class A(Node):
        """Node type."""

    class B(Leaf):
        """Leaf type."""

    class BaseTestCase(unittest.TestCase):

        def test_Node(self):
            n = A(1, [Leaf(1, "ha"), Leaf(1, "llo"), Leaf(1, "!")])
            n2 = n.clone()
            assert n == n2, "Clone changed something"
            assert n.children[1] == n2.children[1], "Child mismatch"
            n.children = [A(1, [Leaf(1, "yes")])]
            assert n != n2, "Clone didn't change when it should have"


# Generated at 2022-06-13 18:19:30.112749
# Unit test for constructor of class NodePattern
def test_NodePattern():
    assert NodePattern(257).type == 257
    assert NodePattern(257, ["hello"]).content == ["hello"]
    assert NodePattern(257, ["hello"], "a_node").name == "a_node"
    try:
        NodePattern(257, "hello")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError")
    try:
        NodePattern(257, 1)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError")
    try:
        NodePattern(257, [1])
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError")

# Generated at 2022-06-13 18:19:40.396258
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    # base.py: Base.get_lineno
    # tests only
    from lib2to3.pgen2.tokenize import generate_tokens, untokenize
    # pylint:disable=E1101

# Generated at 2022-06-13 18:19:46.219095
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
        t = NodePattern(
            type = 10,
            content = alt(NodePattern(type = 11), NodePattern(type = 12))
        )
        r = WildcardPattern(
            min = 1,
            max = 3,
            content = [[NodePattern(type = 20)], [NodePattern(type = 21)]]
        )
        x = WildcardPattern(
            min = 2,
            max = 5,
            content = [[t]]
        )

# Generated at 2022-06-13 18:19:49.006291
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    l = Leaf(1, "")
    assert next(l.post_order()) == l



# Generated at 2022-06-13 18:19:51.477594
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(3) == "NUMBER"
    assert type_repr(5) == 5


# Pattern Matcher (implementation of find())



# Generated at 2022-06-13 18:19:52.192922
# Unit test for method replace of class Base
def test_Base_replace():
    pass



# Generated at 2022-06-13 18:20:00.992387
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from . import parso
    from .pgen2 import tokenize
    from .pytree import Leaf

    s = 'z = 42\nprint(z)\n'
    grammar = parso.load_grammar()
    module = grammar.parse(s)

    # Find the node corresponding to the integer 42
    assignment_node = module.children[0]
    z_node = assignment_node.children[0]
    z_leaf = z_node.children[0]
    z_leaf_next_sibling = z_leaf.next_sibling
    print(z_leaf_next_sibling)

    # Check that z_leaf_next_sibling.prefix is the same as z.next_sibling.prefix
    # (the goal of this test is to make sure that Base.get_suffix() is
    # consistent with

# Generated at 2022-06-13 18:20:28.553176
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    bp1 = BasePattern()
    bp2 = BasePattern(type=1)
    bp3 = BasePattern(type=1, content="a")
    bp4 = BasePattern(type=1, content="a", name="b")
    assert repr(bp1) == 'BasePattern()'
    assert repr(bp2) == 'BasePattern(1, None, None)'
    assert repr(bp3) == 'BasePattern(1, "a", None)'
    assert repr(bp4) == 'BasePattern(1, "a", "b")'



# Generated at 2022-06-13 18:20:40.134490
# Unit test for method replace of class Base
def test_Base_replace():
    """
    >>> test_Base_replace()
    """
    ns_stmt = Nonterminal("small_stmt", (range(3),), None, None)
    ns_suite = Nonterminal("suite", (range(2),), None, None)
    l1 = Leaf(1, "print", (1, 0))
    l2 = Leaf(1, "x", (1, 1))
    l3 = Leaf(1, "print", (1, 2))
    l4 = Leaf(1, "y", (1, 3))
    ns_stmt.children = [l1, l2]
    ns_suite.children = [ns_stmt]
    l1.parent = ns_stmt
    l2.parent = ns_stmt
    ns_stmt.parent = ns_suite


# Generated at 2022-06-13 18:20:50.818511
# Unit test for constructor of class NodePattern
def test_NodePattern():
    #
    # This is unit test for the constructor of the class NodePattern
    # The test parameters are (type, content, expected error)
    #
    test_data = [
        (0, None, AssertionError),
        (0, ["a"], AssertionError),
        (255, ["a"], AssertionError),
        (256, None, None),
        (256, ["a"], None),
        (256, "a", TypeError),
        (256, ["a"], None),
        (256, [], None),
        (256, [BasePattern()], None),
        (256, [[]], TypeError),
    ]


# Generated at 2022-06-13 18:20:53.916356
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    bp = BasePattern()
    bp.match = lambda x, y: True
    bp.match_seq = lambda x, y: True
    # Slow, but simple
    assert list(bp.generate_matches([1])) == [(1, {})]



# Generated at 2022-06-13 18:21:07.171962
# Unit test for method remove of class Base
def test_Base_remove():
    group_1 = Node(syms.testlist, [Leaf(1, "test"), Leaf(1, "test2")])
    group_2 = Node(syms.testlist, [Leaf(1, "test3"), Leaf(1, "test4")])
    node = Node(syms.or_test, [group_1, Leaf(257, "or"), group_2])
    assert list(node.children) == [group_1, Leaf(257, "or"), group_2]
    ret = group_1.remove()
    assert ret == 0
    assert node.children == [Leaf(257, "or"), group_2]
    assert group_1.parent is None
    assert list(node.children) == [Leaf(257, "or"), group_2]
    # https://github.com/python/

# Generated at 2022-06-13 18:21:12.550076
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    """
    Unit test for method optimize of class BasePattern
    """
    from .pgen2.parse import Pattern

    assert Pattern(1).optimize().type == 1
    assert Pattern(1, 2).optimize().type == 1
    assert Pattern(1, 2).optimize().content == 2
    assert Pattern(1, None, "foo").optimize().name == "foo"



# Generated at 2022-06-13 18:21:15.576951
# Unit test for method post_order of class Node
def test_Node_post_order():
    n = Node(256, [])
    for e in n.post_order(): assert isinstance(e, Node)

# Generated at 2022-06-13 18:21:18.871042
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    n = Node(1, [])
    assert BasePattern().match_seq([n]) == False, "Not expecting match"

# Generated at 2022-06-13 18:21:23.413533
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Node, Leaf
    node = Node(1, [Leaf(1, 'a'), Node(2, [Leaf(3, 'c'), Leaf(4, 'd')])])
    assert node.depth() == 0
    assert node.children[1].depth() == 1
    assert node.children[1].children[1].depth() == 2



# Generated at 2022-06-13 18:21:31.766597
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    pattern = BasePattern()
    try:
        pattern.generate_matches([])
        assert False, "Expected exception ValueError"
    except ValueError:
        pass
    pattern.type = 1
    result = list(pattern.generate_matches([Leaf(1, "")]))
    assert result == [(1, {})], result
    result = list(pattern.generate_matches([Node(1, [Leaf(1, "")])]))
    assert not result, result
    pattern.type = None
    result = list(pattern.generate_matches([Leaf(1, "")]))
    assert result == [(1, {})], result
    result = list(pattern.generate_matches([Node(1, [Leaf(1, "")])]))