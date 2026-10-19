

# Generated at 2022-06-13 18:15:00.610668
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    """Test method match of class BasePattern."""
    node = Node(256, [])
    assert BasePattern().match(node)
    assert not BasePattern(257).match(node)
    a = Node(257, [])
    assert BasePattern(257).match(a)
    assert not BasePattern(257, "__add__").match(a)
    a.value = "__add__"
    assert BasePattern(257, "__add__").match(a)
    a.value = "__iadd__"
    assert not BasePattern(257, "__add__").match(a)
    a.value = None
    assert BasePattern().match(a)


# Generated at 2022-06-13 18:15:05.650037
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    p1 = LeafPattern(type=1)
    p2 = LeafPattern(type=2)
    
    leaf1 = Leaf(type=1)
    leaf2 = Leaf(type=2)
    leaf3 = Leaf(type=3)

    result = list(p1.generate_matches([leaf1, leaf2]))
    assert result == [(1, {})]
    
    result = list(p2.generate_matches([leaf1, leaf3]))
    assert result == []
    
    result = list(p2.generate_matches([leaf3, leaf3]))
    assert result == [(1, {})]


# Generated at 2022-06-13 18:15:07.695414
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    # TODO: Implement test
    pass


# Generated at 2022-06-13 18:15:16.107227
# Unit test for method depth of class Base
def test_Base_depth():
    class Node(Base):
        def _eq(self, other):
            return self.children == other.children
        def clone(self):
            return Node(self.children)

    class Leaf(Base):
        def _eq(self, other):
            return self.value == other.value
        def clone(self):
            return Leaf(self.value)

    s = Leaf('a')
    s.parent = Node([s])
    assert s.depth() == 1
    t = s.parent
    t.parent = Node([t])
    assert t.depth() == 1
    assert s.depth() == 2
    return
test_Base_depth()



# Generated at 2022-06-13 18:15:17.386418
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.NAME) == "NAME"



# Generated at 2022-06-13 18:15:20.870727
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    Base()  # to silence pyflakes


# Generated at 2022-06-13 18:15:29.838025
# Unit test for method clone of class Base
def test_Base_clone():
    from .pytree import Leaf, Node, Base, type_repr
    from .pygram import python_symbols as syms

    b = Base()
    l = Leaf(1, "x")
    n = Node(syms.classdef, [Leaf(1, "class"), Leaf(1, "X"), Leaf(3, ":"),])
    assert b.clone() is b
    assert l.clone() == l
    n1 = n.clone()
    assert n1 == n
    assert n1 is not n  # It's a deep clone
    n1.children[0].value = "x"
    assert n.children[0].value == "class"
    assert n1.children[0].value == "x"



# Generated at 2022-06-13 18:15:34.900258
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf, Node

    n = Node(1, [Leaf(1, "a"), Leaf(1, "b")])
    n.changed()
    n.replace(Leaf(1, "c"))
    assert n.children == [Leaf(1, "c")]



# Generated at 2022-06-13 18:15:44.335859
# Unit test for method post_order of class Base
def test_Base_post_order():
    import unittest
    import copy


    class TestableBase(Base):
        def _eq(self, n):
            return False

        def clone(self):
            return copy.deepcopy(self)

        def post_order(self):
            for child in self.children:
                yield from child.post_order()
            yield self

        def pre_order(self):
            yield self
            for child in self.children:
                yield from child.pre_order()

    class TestableLeaf(Base):
        def _eq(self, n):
            return False

        def clone(self):
            return copy.deepcopy(self)

        def post_order(self):
            yield self

        def pre_order(self):
            yield self



# Generated at 2022-06-13 18:15:54.974197
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    import _ast as ast
    import textwrap

    def assert_suffix(node, expected_suffix):
        assert node.get_suffix() == expected_suffix

    # Test node without trailing suffix
    node = ast.parse(textwrap.dedent("""\
    def foo():
        pass
    """))
    assert_suffix(node, "")

    # Test node with trailing suffix
    node = ast.parse(textwrap.dedent("""\
    def foo():
        pass
    def bar():
        pass
    """))
    assert_suffix(node.body[0], "def bar():")

    # Test node with empty trailing suffix
    node = ast.parse(textwrap.dedent("""\
    def foo():
        pass
    """))

# Generated at 2022-06-13 18:16:20.009949
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    t = Leaf(token.NAME, 'Leaf')
    t.pre_order()

# Generated at 2022-06-13 18:16:21.905384
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    """Test method __repr__ of class BasePattern"""
    pattern = BasePattern(0, 0, '', '')
    assert repr(pattern) is not None


# Generated at 2022-06-13 18:16:29.802511
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    p = WildcardPattern([[Leaf(token.NAME)]])
    assert isinstance(p, WildcardPattern)
    p = WildcardPattern([[Leaf(token.NAME)], [Leaf(token.NAME)]], name="bare_name")
    assert isinstance(p, WildcardPattern)
    p = WildcardPattern(min=1, max=1)
    assert isinstance(p, NodePattern)
    p = WildcardPattern(min=1, max=1, name="bare_name")
    assert isinstance(p, WildcardPattern)
    p = WildcardPattern(min=1, max=1, name="leaf")
    assert isinstance(p, NodePattern)
    p = WildcardPattern([[NodePattern(type=token.NAME)]], min=1, max=1)

# Generated at 2022-06-13 18:16:39.801510
# Unit test for method set_child of class Node
def test_Node_set_child():
    class Node(object):
        def __init__(self,parent=None):
            self.children = [1,2,3,4]
            self.parent = parent
        def __setitem__(self,i,child):
            self.children[i] = child
    class Leaf(object):
        def __init__(self,parent=None):
            self.parent = parent
        def __setitem__(self,i,child):
            self.children[i] = child
    # Test for method set_child of class Node
    n = Node()
    n.set_child(3,n)
    assert n.children==[1,2,3,n]
    l = Leaf()
    l.set_child(0,l)
    assert l.children == [l]

# Generated at 2022-06-13 18:16:50.785274
# Unit test for function generate_matches
def test_generate_matches():
    from .combinator import OrPattern, match_or
    from .matchers import NamePattern, LastNamePattern, FirstNamePattern
    from .model import Name, FirstInitial, LastInitial, Nickname, Suffix, Period
    from .lexer import tokenize

    match_or(["hello", "goodbye", "good night", "good morning", "good afternoon"])

    name = Name("Joe", LastInitial("Q"), "Smith", Suffix("III", Period(".")), Period("."))
    patterns = [
        OrPattern([NamePattern("name"), LastNamePattern("name")])
    ]
    pattern = OrPattern(patterns)
    assert tokenize("Joe Q Smith III.") == name
    pattern.match(name)

# Generated at 2022-06-13 18:16:52.171856
# Unit test for method get_lineno of class Base

# Generated at 2022-06-13 18:16:54.835908
# Unit test for method clone of class Base
def test_Base_clone():
    # test_Base_clone()
    assert False
    # Introduced in PyTree_Clone()



# Generated at 2022-06-13 18:17:02.093266
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    root = Node(1, [Leaf(1, "h"), Leaf(1, "e"), Leaf(1, "l"), Leaf(1, "l"), Leaf(1, "o")])
    l = [1, "h", 1, "e", 1, "l", 1, "l", 1, "o"]
    assert [x.type for x in root.pre_order()] == l



# Generated at 2022-06-13 18:17:12.162262
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    class Node(Base):
        def __init__(self, children):
            self.children = children
        def __eq__(self, other):
            return self.children == other.children
        def pre_order(self):
            yield self
            for child in self.children:
                yield from child.pre_order()
        def __repr__(self):
            return '<Node>'
    class Leaf(Base):
        def __eq__(self, other):
            return True
        def pre_order(self):
            yield self
        def __repr__(self):
            return '<Leaf>'
    a = Leaf()
    b = Leaf()
    c = Leaf()
    d = Node([a, b])
    e = Node([d, c])

# Generated at 2022-06-13 18:17:14.852393
# Unit test for method leaves of class Base
def test_Base_leaves():
    from . import driver
    grammar = Grammar(driver.grammar)
    test_program = """
foo = 123
"""
    root = grammar.parse_string(test_program)
    assert len(list(root.leaves())) == 8



# Generated at 2022-06-13 18:17:39.994357
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    # Patterns without attributes
    p = LeafPattern(42)
    assert repr(p) == 'LeafPattern(42)'

    p = LeafPattern(42, 'foo', 'bar')
    assert repr(p) == "LeafPattern(42, 'foo', 'bar')"

    p = NodePattern(42)
    assert repr(p) == 'NodePattern(42)'

    p = NodePattern(42, 'foo', 'bar')
    assert repr(p) == "NodePattern(42, 'foo', 'bar')"

    p = WildcardPattern(42)
    assert repr(p) == 'WildcardPattern(42)'

    # Patterns with attributes

# Generated at 2022-06-13 18:17:48.588274
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    from .pgen2.parse import ParseError

    _ParseError = ParseError
    from .pgen2.pgen import generate_grammar, _generate_tables, Grammar

    from . import token

    from .tokenize import detect_encoding

    from .pgen2 import driver

    from .pgen2 import tokenize

    from .tokenize import generate_tokens

    from .pgen2.parse import ParseError

    from .tokenize import untokenize

    from .tokenize import COMMENT

    from .tokenize import NL

    from .tokenize import generate_tokens


# Generated at 2022-06-13 18:17:59.031807
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    # test for ...
    pattern = WildcardPattern(min=3, max=3)
    assert pattern.match_seq([]) is False
    assert pattern.match_seq(["1"]) is False
    assert pattern.match_seq(["1", "2"]) is False
    assert pattern.match_seq(["1", "2", "3"]) is True
    assert pattern.match_seq(["1", "2", "3", "4"]) is False

    # test for .*
    pattern = WildcardPattern(min=0, max=HUGE)
    assert pattern.match_seq([]) is True
    assert pattern.match_seq(["1"]) is True
    assert pattern.match_seq(["1", "2"]) is True
    assert pattern.match_seq(["1", "2", "3"])

# Generated at 2022-06-13 18:18:06.550352
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    from .pytree import Node, Leaf
    tree = Node(1, [Leaf(1, "foo", (1, 0)), Leaf(2, "bar", (1, 3))])
    assert tree.get_lineno() == 1
    t = Node(1, [tree, Node(1, [Leaf(1, "baz", (2, 0))])])
    assert t.get_lineno() == 1
    t.changed()
    assert t.get_lineno() == 1



# Generated at 2022-06-13 18:18:08.734558
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.NAME) == "NAME"
    assert type_repr(python_symbols.token) == python_symbols.token



# Generated at 2022-06-13 18:18:12.010644
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    l = Leaf(56, "some_value")
    assert list(l.leaves()) == [l]


# Generated at 2022-06-13 18:18:23.253015
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    success = True
    P = WildcardPattern
    N = NegatedPattern
    assert P(min=1).generate_matches([]).__next__() == (0, {})
    assert P(min=0).generate_matches([]).__next__() == (0, {})
    assert P(min=1).generate_matches([]).__next__() == (0, {})
    assert N(P(min=0)).generate_matches([]).__next__() == (0, {})
    assert N(P(min=1)).generate_matches([]).__next__() == (0, {})
    assert N(P(min=2)).generate_matches([]).__next__() == (0, {})
    assert N(P(min=1)).generate

# Generated at 2022-06-13 18:18:29.135425
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    import re
    import sys
    import unittest

    from .pgen2.pgen import graminit

    class BasePatternTestCase(unittest.TestCase):
        def setUp(self):
            self.parser = graminit.build_parser("<string>")

        def test_optimize(self):
            p = self.parser.pattern("test")
            p = p.optimize()
            self.assertIsInstance(p, LeafPattern)
            self.assertEqual(p.type, self.parser.number2symbol[1])
            self.assertIs(p.content, None)

            p = self.parser.pattern("test", re.compile("hello"))
            p = p.optimize()
            self.assertIsInstance(p, LeafPattern)

# Generated at 2022-06-13 18:18:39.570203
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    pattern = LeafPattern("TEST", "TEST")

    def test(nodes: List[NL], result: bool) -> None:
        assert pattern.match_seq(nodes) == result

    test([], False)
    test([Leaf("TEST", "TEST")], True)
    test([Leaf("TEST", "X")], False)
    test([Leaf("TEST", "TEST"), Leaf("TEST", "TEST")], False)



# Generated at 2022-06-13 18:18:51.018262
# Unit test for function generate_matches
def test_generate_matches():
    pm = WildcardPattern()
    node = Node(1, [(0, "a"), (0, "b")])
    p = AnyNodePattern(type=1)

    for count, r in generate_matches([p], [node]):
        assert count == 1, count
        assert r == {}, r
    for count, r in generate_matches([p, pm], [node]):
        assert count == 1, count
        assert r == {}, r
        assert r[pm.name] == [node], r[pm.name]
    for count, r in generate_matches([pm], [node]):
        assert count == 0, count
        assert r == {}, r
        assert r[pm.name] == [], r[pm.name]

    pm = WildcardPattern(content=[[p]], min=1)

# Generated at 2022-06-13 18:19:11.099111
# Unit test for method clone of class Base
def test_Base_clone():
    from pgen2.parse import ParseError

    try:
        b = Base()
        b.clone()
        print("Expected ParseError")
    except ParseError:
        pass

# Generated at 2022-06-13 18:19:13.259442
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .pytree import PythonLeaf

    assert list(PythonLeaf.pre_order(Leaf(0, "")), ) == [Leaf(0, "")]



# Generated at 2022-06-13 18:19:20.069133
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    from .pgen2.parse import NFA

    nfa = NFA(0, {0: {1: [0, None]}, 1: {2: [0, None], 3: [0, None], 4: [0, None]}})
    print(nfa.check([]))
    name = "abc"
    #print(nfa._nonterms[0].to_tree())


# Generated at 2022-06-13 18:19:28.781730
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    with open('<stdin>', 'r') as sys_stdin:
        sys_stdin = open('<stdin>', 'r')
        global_vars = {'__name__': '__main__', '__file__': '<stdin>', '__doc__': None, '__package__': None}
        local_vars = {}
        exec(object(), global_vars, local_vars)
        import sys
        sys.stdin = sys_stdin
        along_a_way = local_vars['along_a_way']
        along_a_way(1)
        along_a_way(2)
        along_a_way(3)
        along_a_way(4)
        along_a_way(5)
        along_a_way(6)
        along

# Generated at 2022-06-13 18:19:36.505099
# Unit test for method remove of class Base
def test_Base_remove():
    from .pgen2 import driver
    from .pytree import convert

    d = driver.Driver(grammar=Grammar(), convert=convert)
    tree = d._parse_tokens([(0, "a", (1, 0), (1, 1))])
    assert tree.remove() == 0
    assert tree.remove() is None


# Generated at 2022-06-13 18:19:47.765021
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    from .pgen2 import token
    from .pgen2.parse import NotAny, Any
    from .pytree import Leaf as L, Node as N
    py_prefix = L(token.INDENT, "  ")
    py_body = L(token.INDENT, "    pass")
    py_node = N(syms.simple_stmt, [py_prefix, py_body])
    py_tree = N(syms.file_input, [py_node])
    pat = py_tree.pattern()
    # Check if optimization did not alter the original pattern
    assert pat == py_tree.pattern()
    # Check that pattern comparison is implemented
    assert pat == py_tree.pattern()
    # Check that optimization removed redundant Any()
    assert pat.optimize() == py_tree.pattern().pattern()
    # Check

# Generated at 2022-06-13 18:19:57.239589
# Unit test for method post_order of class Base
def test_Base_post_order():
    """Test a post order traversal of the sample tree"""

    # The sample tree

# Generated at 2022-06-13 18:20:04.417482
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    import unittest
    from .pytree import Leaf as L
    from .pytree import Node as N
    from .pygram import python_symbols as p

# Generated at 2022-06-13 18:20:12.372398
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from blib2to3.pgen2.parse import ParseError
    from blib2to3.pgen2.tokenize import generate_tokens
    from blib2to3.fixer_util import untokenize
    import blib2to3.pgen2.driver
    def test_get_suffix(code):
        # Verify that the suffix is correct
        try:
            tokens = list(generate_tokens(StringIO(code).readline))
        except ParseError as e:
            print(code)
            raise e
        tree = blib2to3.pgen2.driver.Driver(blib2to3.fixer_util.grammar, convert=blib2to3.fixer_util.convert_grammar_headers).parse_tokens(tokens)
       

# Generated at 2022-06-13 18:20:19.003186
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    """Regression test for http://bugs.python.org/issue1785
    """
    class EmptyPattern(BasePattern):
        def _submatch(self, node, results=None):
            return False
    e = EmptyPattern(123)
    repr(e)



# Generated at 2022-06-13 18:20:44.976039
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    a, ab, b, c, bc, ba, d, e, f, g, o, oo = map(LeafPattern, "abcdebfg")
    assert list(NegatedPattern().generate_matches([])) == [(0, {})]
    assert list(NegatedPattern(a).generate_matches([a])) == []
    assert list(NegatedPattern(a).generate_matches([b])) == [(0, {})]
    assert list(NegatedPattern(a + b).generate_matches([a, b])) == []
    assert list(NegatedPattern(a + b).generate_matches([b, a])) == []
    assert list(NegatedPattern(a + b).generate_matches([a])) == []

# Generated at 2022-06-13 18:20:55.258851
# Unit test for method remove of class Base
def test_Base_remove():
    import inspect
    import unittest
    from blib2to3.pgen2.pgen import Node

    class BaseTest(unittest.TestCase):
        def test_remove(self):
            node = Node(1, [])
            node2 = Node(2, [])
            node.children.append(node2)
            node3 = Node(3, [])
            node.children.append(node3)
            node4 = Node(4, [])
            node.children.append(node4)
            self.assertEqual(node.children[0], node2)
            self.assertEqual(node.children[1], node3)
            self.assertEqual(node.children[2], node4)
            self.assertIs(node2.parent, node)

# Generated at 2022-06-13 18:21:06.320688
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .driver import Driver
    from . import pytree
    from .pygram import python_symbols
    from .pgen2.generator import Generator

    driver = Driver(
        pygram.python_grammar,
        convert=pytree.convert,
        logger=sys.stdout.write,
        generator=Generator,
    )
    parser = driver.build_parser()
    tree = parser.parse_string("# comment")
    assert list(tree[0].leaves()) == [Leaf(type=python_symbols.COMMENT, value="# comment", context=None)]



# Generated at 2022-06-13 18:21:12.358036
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    # test two kinds of nodes
    a = Leaf(1, "abc")
    assert a.get_lineno() == 1
    b = Node(1, None, [a])
    assert b.get_lineno() == 1
    # assert c.get_lineno() == None
    # test_Base_get_suffix



# Generated at 2022-06-13 18:21:23.123911
# Unit test for function convert
def test_convert():
    from .pgen2 import driver

    gr = driver.load_grammar("Python.asdl")
    node = convert(gr, (1, None, None, [convert(gr, (2, None, None, None))]))
    assert isinstance(node, Node)
    assert isinstance(node.children[0], Leaf)
    assert node.children[0].type == 2
    assert node.type == 1

    node = convert(gr, (1, None, None, []))
    assert isinstance(node, Node)
    assert node.type == 1
    assert len(node.children) == 0

    node = convert(gr, (1, "int", None, None))
    assert isinstance(node, Leaf)
    assert node.type == 1
    assert node.value == "int"



# Generated at 2022-06-13 18:21:29.273410
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    tree = Node(2, None, None, (Leaf(1, "a"), Leaf(1, "b"), Leaf(2, None, None, (Leaf(1, "c"), Leaf(1, "d"), Leaf(1, "e")))))
    expected = [Leaf(1, "a"), Leaf(1, "b"), Leaf(2, None, None, (Leaf(1, "c"), Leaf(1, "d"), Leaf(1, "e")))]
    actual = list(tree.pre_order())
    assert actual == expected



# Generated at 2022-06-13 18:21:30.022040
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    pass



# Generated at 2022-06-13 18:21:39.864837
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    # Create a pattern for matching 'b' at the first position
    b_pattern = NodePattern(content=[LeafPattern(content="b")], name="b")
    # Create a pattern for matching 'b' or 'c' or 'd' at second position
    bc_pattern = NodePattern(content=[LeafPattern(content="b"), LeafPattern(content="c")], name="b_or_c")
    bcd_pattern = NodePattern(content=[LeafPattern(content="b"), LeafPattern(content="c"), LeafPattern(content="d")], name="b_or_c_or_d")
    # Create a pattern for matching one 'b' followed by zero or more 'c'

# Generated at 2022-06-13 18:21:42.550744
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    file = open('samples/example_1.py', 'r')
    lines = file.readlines()
    content = ''
    for line in lines:
        content += line
    return content


# Generated at 2022-06-13 18:21:45.857566
# Unit test for method remove of class Base
def test_Base_remove():
    node_1 = Base()
    node_2 = Base()
    node_3 = Base()
    node_3.parent = node_1
    node_3.remove()
    assert node_3.parent is None
    node_2.parent = node_1
    node_2.remove()
    assert node_2.parent is None