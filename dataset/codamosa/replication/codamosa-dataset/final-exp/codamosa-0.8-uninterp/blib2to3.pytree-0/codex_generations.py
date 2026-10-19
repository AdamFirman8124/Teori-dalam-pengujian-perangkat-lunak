

# Generated at 2022-06-13 18:14:47.516630
# Unit test for method replace of class Base
def test_Base_replace():
    class Node(Base):

        def __init__(self, children):
            self.children = children
            for child in children:
                child.parent = self

        def _eq(self, other):
            return (self.type == other.type) and (len(self.children) == len(other.children)) and all(
                [x == y for x, y in zip(self.children, other.children)])

        def clone(self):
            children = [child.clone() for child in self.children]
            return Node(children)

        def post_order(self):
            for child in self.children:
                yield from child.post_order()
            yield self

        def pre_order(self):
            yield self
            for child in self.children:
                yield from child.pre_order()


# Generated at 2022-06-13 18:14:57.432778
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Leaf
    from .pgen2 import token
    from .pgen2 import driver
    from . import pygram
    from .pygram import python_symbols
    from . import pytree

    print('>>> import python_grammar')
    print('>>> python_grammar = python_grammar.pgen_grammar')
    print('>>> pgen = pgen2.driver.load_grammar(python_grammar)')
    print('>>> pgen.parse(R"""print "hi" """)')
    print('<python_grammar.File instance at 0x...>')
    print('>>> pgen.parse(R"""print "hi" """).leaves()[0].type')
    print(token.NAME)
    print('')
    # Create the rules structure
    driver = driver.load

# Generated at 2022-06-13 18:15:04.469801
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import pytest
    from .pgen2.parse import ParseError
    from .pgen2.parse import is_nonterminal
    import sys
    import logging
    import hashlib
    import tempfile
    import filecmp
    import os
    import random
    import re
    import itertools
    from .pgen2 import tokenize
    from .pgen2 import driver
    from . import pgen2
    from .pgen2.pgen import YAMLParser
    from .pgen2.pgen import _gen_random
    from .pgen2.grammar import _build_node_matcher
    from .pgen2.grammar import _build_regexp_matcher
    from .pgen2.grammar import _build_sub_matches
    from .pgen2 import token

# Generated at 2022-06-13 18:15:12.598215
# Unit test for function type_repr
def test_type_repr():
    # The function type_repr is meant to be used in debug output, so
    # we don't bother testing the output format here.
    #
    # However, we need to know that when we pass an integer that isn't
    # in the symbol table, we get something back.
    assert type(type_repr(sys.maxsize)) == str
    assert type(type_repr(sys.maxsize + 1)) == int

# The following implements a pattern matching framework, similar to
# Lisp's "destructuring bind".  We use this to match the parse tree
# against patterns for the various transforms.
#
# The pattern language is fairly simple; the following types can be
# used in patterns:
#   - None: matches anything
#   - int: matches an int of that value
#   - tuple: matches a tuple of that size, whose items are

# Generated at 2022-06-13 18:15:20.817681
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    class TestNode(Base):
        def __init__(self, lineno):
            self.type = 0
            self.prefix = ""
            self.lineno = lineno
            self.value = None
            self.children = []

    class TestLeaf(Leaf):
        def __init__(self, lineno):
            self.type = 0
            self.prefix = ""
            self.lineno = lineno
            self.value = None

    # Test a tree of the form:
    #
    #    +-node
    #    | |
    #    | +-leaf1
    #    | |
    #    | +-leaf2
    #    | |
    #    | +-leaf3
    #    |
    #    +-node2
    #
    # The first node should have a suffix

# Generated at 2022-06-13 18:15:32.416682
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .pytree import Node
    class MyNode(Node):
        def _eq(self, other): 
            return True
        def clone(self): 
            return self
        def post_order(self): 
            yield self
        def pre_order(self): 
            yield self
    def check(a, b): 
        a.changed()
    def check(a, b): 
        assert a == b
    a = MyNode(1, children=[MyNode(2, children=[MyNode(3)]), MyNode(4)])
    b = MyNode(1, children=[MyNode(2, children=[MyNode(3)]), MyNode(4)])
    check(list(a.pre_order()), [a, a[0], a[0][0], a[1]])

# Generated at 2022-06-13 18:15:43.006956
# Unit test for method post_order of class Node
def test_Node_post_order():
    class MockNode(Node):
        def __init__(self, type, children, prefix=None):
            self.type = type
            self.children = list(children)
            self.prefix = prefix

    a = MockNode(1, [Leaf(1, "a"), Leaf(1, "b")], "a")
    b = MockNode(1, [Leaf(1, "c"), Leaf(1, "d")], "b")
    c = MockNode(1, [Leaf(1, "e"), Leaf(1, "f")], "c")
    d = MockNode(1, [Leaf(1, "g"), Leaf(1, "h")], "d")
    
    ab = Node(1, [a, b])
    cd = Node(1, [c, d])
    
    a.was

# Generated at 2022-06-13 18:15:53.822945
# Unit test for method clone of class Base
def test_Base_clone(): # type: () -> None

    class Leaf2(Leaf):

        def __init__(self, type: int, value: Text,
                          context: Optional[Context], prefix: Optional[Text]) -> None:
            super().__init__(type, value, context, prefix)
            self.extra = "hi"

        def clone(self) -> "Leaf2":
            return Leaf2(self.type, self.value, self.context, self.prefix)

    class Node2(Node):

        def clone(self) -> "Node2":
            return Node2(self.type, None, None, [child.clone() for child in self.children])

    l1 = Leaf2(1, "l1", None, "")
    l2 = Leaf2(2, "l2", None, "")

# Generated at 2022-06-13 18:16:01.630594
# Unit test for method replace of class Base
def test_Base_replace():
    n = Node(1, [Leaf(2, 'a'), Leaf(3, 'b')])
    e = Leaf(5, 'c')
    n.children[1].replace(e)
    if n.children[1] == e:
        n.children[1] = None
    # testing if the 'e' is inserted into the list.
    if n.children[1] is None:
        print("test_Base_replace: Success")
    else:
        print("test_Base_replace: Fail")

test_Base_replace()

# Generated at 2022-06-13 18:16:15.289939
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import unittest
    import copy
    import grammar.pgen2.parse as parse

    class TestCase(unittest.TestCase):

        def try_matches(self, pattern, input):
            tree = parse.parse(input)
            pat = parse.Pattern(pattern)
            matches = list(pat.generate_matches(tree.children[0]))
            print(input + ": " + str(matches))
            self.assertEqual(matches, eval(input))

    TestCase().try_matches("1", "(1)")
    TestCase().try_matches("'x'", "('x')")
    TestCase().try_matches("1", "(1 2)")
    TestCase().try_matches("1", "(1 (2))")

# Generated at 2022-06-13 18:16:32.559011
# Unit test for method remove of class Base
def test_Base_remove():
    class test_stmt:
        type = 131
        context = (1, 1)
        parent = None
        children = [test_expr(), test_expr()]

    class test_expr:
        type = 39
        context = (1, 1)
        parent = None
        children = []
    node = test_stmt()
    node.children[1].remove()
    assert node.children[0].type == 39

# Generated at 2022-06-13 18:16:36.630013
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    import collections
    import itertools
    import operator
    import typing
    import unittest
    import unittest.mock
    import ast

    import asttokens
    import asttokens.util

    import asdl

    class TestableNodePattern(NodePattern):
        def __init__(
                self,
                type: Optional[int] = None,
                content: Optional[Iterable[Text]] = None,
                name: Optional[Text] = None,
        ) -> None:
            super().__init__(type=type, content=content, name=name)
            self.is_submatch_called = False

        def _submatch(self, node, results=None) -> bool:
            self.is_submatch_called = True

# Generated at 2022-06-13 18:16:38.239160
# Unit test for method leaves of class Base
def test_Base_leaves():
    b = Base()
    assert isinstance(b.leaves(), Iterator)
test_Base_leaves()



# Generated at 2022-06-13 18:16:43.602823
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    import lib2to3.pgen2.parse
    parser = lib2to3.pgen2.parse

    node = parser.suite("x = 'a' + 'b'")
    pat = parser.expr.pattern.patterns[2][2]

    assert isinstance(pat, WildcardPattern), pat
    assert pat.min == 1, pat.min
    assert pat.max == 1, pat.max
    assert len(pat.content) == 1, pat.content
    assert len(pat.content[0]) == 1, pat.content[0]
    assert isinstance(pat.content[0][0], WildcardPattern), pat.content[0][0]
    assert pat.content[0][0].min == 0, pat.content[0][0].min

# Generated at 2022-06-13 18:16:45.750132
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    # Base#__eq__: NotImplemented
    assert Base().__eq__(Base()) is NotImplemented


# Generated at 2022-06-13 18:16:48.455835
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    nodes = Node(1, Node(2), Node(3))
    result = list(nodes.pre_order())
    assert result == [nodes, nodes.children[0], nodes.children[1]]



# Generated at 2022-06-13 18:17:00.564501
# Unit test for method post_order of class Base
def test_Base_post_order():
    from .pytree import Node, Leaf

    class MyBase(Base):
        def post_order(self):
            yield self

    tree = Node(1, [Leaf(1, "foo"), Leaf(1, "bar"), Leaf(1, "baz")])
    tree.changed()
    assert [list(x.post_order()) for x in tree.post_order()] == [
        [tree], [tree[0]], [tree[1]], [tree[2]]]
    assert tree.post_order() is not tree.post_order()

    tree = MyBase()
    assert list(tree.post_order()) == [tree]



# Generated at 2022-06-13 18:17:02.084222
# Unit test for method __repr__ of class Leaf
def test_Leaf___repr__():
    test_fixture_leaf = Leaf(0, "hi")
    result = test_fixture_leaf.__repr__()
    expected = "Leaf(0, 'hi')"
    assert (result == expected)
    return


# Generated at 2022-06-13 18:17:06.178409
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    import unittest


# Generated at 2022-06-13 18:17:09.145792
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.terminator) == "terminator"



# Generated at 2022-06-13 18:17:28.257496
# Unit test for method post_order of class Base
def test_Base_post_order():
    from blib2to3.pgen2.driver import Driver

    # We must import this locally, as we need to test private methods.
    from blib2to3.pgen2.parse import make_grammar

    g = make_grammar(StringIO(grammar_sample), "GrammarSample")
    d = Driver(g, convert=convert_tree)
    tree = d.parse_tokens(tokens_sample)
    test_tree(tree)

    leaves = list(tree.post_order())
    assert len(leaves) == 15
    # Test that the values of the leaves are what we expect.
    assert leaves[0].value == "1"
    assert leaves[1].value == "0"
    assert leaves[2].value == "2"

# Generated at 2022-06-13 18:17:36.324001
# Unit test for method get_suffix of class Base
def test_Base_get_suffix(): 
    from .pytree import Base, Leaf
    from .pygram import python_symbols as syms
    def _make_node(parent, type_):
        node = Leaf(type_, "", prefix="")
        if parent:
            parent.append_child(node)
        return node
    parent = _make_node(None, syms.power)
    child1 = _make_node(parent, syms.factor) 
    child2 = _make_node(parent, syms.factor)
    assert child1.get_suffix() == ""
    assert child2.get_suffix() == ""
    sib = _make_node(parent, syms.NUMBER)
    assert sib.get_suffix() == ""
    sib2 = _make_node(parent, syms.NUMBER)


# Generated at 2022-06-13 18:17:46.551919
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    from types import GeneratorType
    from astroid.builder import AstroidBuilder
    from snakefood.tests.test_sfood import builder
    from snakefood.sfood import BasePattern

    def t():
        pass

    abuilder = AstroidBuilder(manager)
    astroid = abuilder.string_build("def f():\n pass", __name__, __file__)
    b = BasePattern()
    assert b.match(astroid.body[0]) is True
    assert b.match(astroid.body[0], {}) is True
    assert b.match(abc.ABCMeta, {}) is False
    assert b.match(abc.ABCMeta) is False
    assert b.match(abc.ABCMeta, {}) is False
    assert b.match(astroid.body[0], {}) is True
    assert b

# Generated at 2022-06-13 18:17:57.594999
# Unit test for function generate_matches

# Generated at 2022-06-13 18:18:03.722124
# Unit test for function generate_matches
def test_generate_matches():
    p = NegatedPattern(NodePattern(type=Token.NAME))
    nodes = [tokenize_lines(["a", "b", "c"])[0], tokenize_lines(["d"])[0]]
    assert list(generate_matches([p, WildcardPattern(min=2)], nodes)) == [
        (3, {"bare_name": [nodes[0], nodes[1]]})
    ]



# Generated at 2022-06-13 18:18:08.003901
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Node, Leaf
    tree = Node(10, [Leaf(1, "foo"), Node(10, [Leaf(1, "bar")])])
    assert tuple(tree.leaves()) == tuple(tree.children[0].leaves()) + tuple(
        tree.children[1].leaves())



# Generated at 2022-06-13 18:18:10.112640
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == 1
# End unit test



# Generated at 2022-06-13 18:18:19.663066
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    # Test: get_suffix for a Leaf returns the correct suffix
    tree = parse_string("a = 1")
    assert isinstance(tree, Node)
    assert isinstance(tree.children[1], Leaf)
    assert tree.children[1].get_suffix() == " = 1"
    # Test: get_suffix for a Node returns the correct suffix (if any)
    tree = parse_string("a = 1")
    assert isinstance(tree, Node)
    assert isinstance(tree.children[1], Leaf)
    assert tree.children[1].get_suffix() == " = 1"
    assert tree.get_suffix() == "\n"
    tree = parse_string("a = 1\nb = 2")
    assert isinstance(tree, Node)
    assert isinstance(tree.children[1], Leaf)

# Generated at 2022-06-13 18:18:28.481431
# Unit test for method remove of class Base
def test_Base_remove():
    from .pytree import Node, Leaf, Internal
    from .python_grammar import python_grammar
    from .pygram import python_symbols
    from .pyparse import (
        Parser,
        ParseError,
        ParseSyntaxError,
        ParseFatalException,
        ParseError,
    )

    grammar = python_grammar
    grammar.check_lookahead = True
    p = Parser(grammar)
    # Parsing a module
    try:
        tree = p.parse_string(
            """for i in xrange(10):
    print i
""")
    except ParseError:
        raise Exception("Unable to parse snippet. ParseError.")
    except ParseSyntaxError:
        raise Exception("Unable to parse snippet. ParseSyntaxError.")

# Generated at 2022-06-13 18:18:30.474053
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    if hasattr(Leaf, 'post_order'):
        for x in Leaf.post_order(Leaf):
            assert type(x) is Leaf, str(x)

# Generated at 2022-06-13 18:18:50.316967
# Unit test for method post_order of class Base
def test_Base_post_order():
    from blib2to3.pgen2.pgen import _Node, _Leaf, _InternalNode
    assert isinstance(Base(), _Node)
    assert isinstance(Base(), _Leaf)
    assert isinstance(Base(), _InternalNode)
    assert Base.post_order() == Base()
    a = Base()
    b = Base()
    c = Base()
    d = Base()
    assert a != b
    assert a == c
    assert a != d
    assert True
    return



# Generated at 2022-06-13 18:18:57.916740
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    pass

    # Test get_suffix
    _r = None  # Suppress warning
    n = Leaf(1, "foo")
    assert n.get_suffix() == ''
    n2 = Leaf(1, "bar")
    n.append_child(n2)
    assert n.get_suffix() == 'bar'
    n3 = Leaf(1, "baz")
    n2.insert_child(0, n3)
    assert n.get_suffix() == 'baz'
    assert n2.get_suffix() == 'bar'
    assert n3.get_suffix() == ''



# Generated at 2022-06-13 18:19:04.080271
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pytree import Leaf, Node
    from .pygram import python_symbols

    def check(node, expected_suffix):
        node.next_sibling = expected_suffix
        assert node.get_suffix() == expected_suffix

    check(Leaf(1, ""), Leaf(1, ""))
    check(Leaf(1, "test"), Leaf(1, "test"))
    check(Leaf(1, ""), Leaf(2, ""))
    check(Node(python_symbols.atom, [Leaf(1, "")]), Node(2, [Leaf(2, "")]))



# Generated at 2022-06-13 18:19:12.754169
# Unit test for method remove of class Base
def test_Base_remove():
    # When a node is removed from a parent, its parent pointer should be
    # updated and its siblings should no longer reference it after their own
    # sibling maps are updated.
    import blib2to3.pytree as pytree
    from blib2to3.pgen2.parse import tokenize_str

    tree = pytree.Node(type=0, children=None, parent=None)
    node1 = pytree.Node(type=0, children=None, parent=tree)
    node2 = pytree.Node(type=0, children=None, parent=tree)
    node3 = pytree.Node(type=0, children=None, parent=tree)
    tree.children = [node2, node1, node3]

    node1.remove()
    assert node1.parent is None
    assert node1.prev_

# Generated at 2022-06-13 18:19:19.843927
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    import blib2to3.pytree
    from io import StringIO

    class TestNode(blib2to3.pytree.Node):
        pass

    class TestLeaf(blib2to3.pytree.Leaf):
        pass


# Generated at 2022-06-13 18:19:35.830738
# Unit test for function generate_matches
def test_generate_matches():
    patterns = [NodePattern(type=1), NodePattern(type=2), WildcardPattern()]
    nodes = [NL(type=1), NL(type=2)]
    for c, r in generate_matches(patterns, nodes):
        print("count =", c, "results =", r)
        assert c == 2, c

    patterns = [WildcardPattern(min=1, max=2), NodePattern(type=2)]
    nodes = [NL(type=1), NL(type=2)]
    for c, r in generate_matches(patterns, nodes):
        print("count =", c, "results =", r)
        assert c == 2, c

    patterns = [WildcardPattern(min=1, max=1), NodePattern(type=2)]

# Generated at 2022-06-13 18:19:47.267616
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    import unittest

    class _Test(unittest.TestCase):
        def test_leaf(self):
            results = {}
            self.assertTrue(p1.match(leaf1, results))
            self.assertEqual(results, {})
            self.assertFalse(p2.match(leaf1, results))
            self.assertEqual(results, {})

        def test_node(self):
            results = {}
            self.assertTrue(p2.match(node1, results))
            self.assertEqual(results, {})
            self.assertFalse(p1.match(node1, results))
            self.assertEqual(results, {})

    from . import test_pattern

    p1 = test_pattern.p1
    p2 = test_pattern.p2
    leaf1 = test_

# Generated at 2022-06-13 18:19:53.292702
# Unit test for method depth of class Base
def test_Base_depth():
    """Unit test for method depth of class Base"""

    node = Node(0, [], parent=None)
    assert node.depth() == 0
    node2 = Node(0, [], parent=node)
    assert node2.depth() == 1
    node3 = Node(0, [], parent=node2)
    assert node3.depth() == 2
    node4 = Node(0, [], parent=node3)
    assert node4.depth() == 3



# Generated at 2022-06-13 18:20:02.890806
# Unit test for method clone of class Node

# Generated at 2022-06-13 18:20:08.686890
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pgen2.parse import ParseError
    from .pgen2.driver import Driver

    from .pgen2 import token

    driver = Driver(convert, convert)

    # A common operation is to try to match the first token of a series
    def match_first_token(tokens):
        for _, result in tokens.generate_matches(nodes):
            return result
        raise ParseError("Expected %r" % (tokens,))

    def test(
        pos: int, pattern: BasePattern, input: Text, expected_result: _Results
    ) -> None:
        driver.setup_parser()
        driver.current_pos = pos
        nodes = list(driver.parse_string(input))
        results = {}

# Generated at 2022-06-13 18:20:30.190157
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.simple_stmt) == "simple_stmt"
    assert type_repr(python_symbols.foo) == python_symbols.foo
test_type_repr()


type = type_repr

# These lists are built by scan_grammar.py.
FIRST = {}  # type: Dict[int, Set[int]]
FOLLOW = {}  # type: Dict[int, Set[int]]
FIRST_EXPR = {}  # type: Dict[int, Set[int]]
FOLLOW_EXPR = {}  # type: Dict[int, Set[int]]

# The symbol table is a dict mapping symbol names (as returned by
# grammar.symbol2number) to a list of definitions.  Each definition
# is a tuple (function

# Generated at 2022-06-13 18:20:42.213267
# Unit test for method set_child of class Node
def test_Node_set_child():
    import os
    from .pytree import Leaf
    from .pygram import python_symbols
    from blib2to3.pgen2.grammar import Grammar
    from lib2to3.pygram import python_grammar
    from .pgen2 import token, tokenize, driver
    if not hasattr(python_grammar, "Grammar"):
        python_grammar.Grammar = Grammar()
    if not hasattr(python_grammar, "driver"):
        python_grammar.driver = driver
    if not hasattr(python_grammar, "python_symbols"):
        python_grammar.python_symbols = python_symbols
    if not hasattr(python_grammar, "python_grammar"):
        python_grammar.python_grammar = python_

# Generated at 2022-06-13 18:20:52.477038
# Unit test for method clone of class Base
def test_Base_clone():
    from .grammar import Grammar
    from .pytree import Leaf
    from .pgen2 import tokenize

    def assert_Eq(a, b):
        assert a == b

    def assert_Eq_Leaf(a, b):
        assert isinstance(a, Leaf)
        assert isinstance(b, Leaf)
        assert a == b

    grammar = """
    S: 'a'
    """
    tokens = iter(tokenize.generate_tokens(StringIO(grammar).readline))
    grammar = Grammar([(t) for t in tokens])
    tree = grammar.parse("a")
    clone = tree.clone()
    assert_Eq(tree, clone)
    (leaf,) = tree.leaves()

# Generated at 2022-06-13 18:20:56.407758
# Unit test for method post_order of class Base
def test_Base_post_order():
    from .pytree import Leaf
    from .node import Node
    root = Node(2, [Leaf(3, "abc"), Leaf(3, "def")])
    x = [i for i in root.post_order()]
    assert x == [root.children[0], root.children[1], root], x


# Generated at 2022-06-13 18:20:58.436626
# Unit test for method replace of class Base
def test_Base_replace():
    assert False, "Unimplemented"



# Generated at 2022-06-13 18:21:06.166893
# Unit test for method post_order of class Node
def test_Node_post_order():
    n = Node(0,[])
    assert list(n.post_order()) == [n]
    n = Node(0,[Node(1,[]),Node(2,[])])
    assert list(n.post_order()) == [Node(1,[]),Node(2,[]),n]


# Generated at 2022-06-13 18:21:14.143366
# Unit test for method set_child of class Node
def test_Node_set_child():
    from .pytree import Leaf, Node
    from .pygram import python_symbols as syms
    tree = Node(syms.file_input, [Leaf(1, "a"), Leaf(2, "b"), Leaf(3, "c")])
    assert str(tree) == "abc"
    tree.set_child(1, Leaf(4, "d"))
    assert str(tree) == "adc"
    assert str(tree.children[1]) == "d"

# Generated at 2022-06-13 18:21:23.900465
# Unit test for function generate_matches
def test_generate_matches():
    w = WildcardPattern(name="w")
    n = NodePattern(name="n")
    assert list(generate_matches([w], [])) == [(0, {})]
    assert list(generate_matches([w], [1, 2])) == [(0, {}), (1, {"w": [1]}), (2, {"w": [1, 2]})]
    assert list(generate_matches([w, n], [])) == []
    assert list(generate_matches([w, n], [1, 2])) == []
    assert list(generate_matches([w, n], [1, 2, 3])) == [(2, {"n": 2, "w": [1]})]

# Generated at 2022-06-13 18:21:25.653582
# Unit test for method post_order of class Node
def test_Node_post_order():
    assert Node(0,[]).post_order() == Node(0,[]).__iter__()



# Generated at 2022-06-13 18:21:32.263470
# Unit test for method depth of class Base
def test_Base_depth():
    """Test Base.depth."""
    node = Node(0, "")

    node1 = Node(0, "")
    node2 = Node(0, "")
    node.append_child(node1)
    node1.append_child(node2)

    assert node.depth() == 0
    assert node1.depth() == 1
    assert node2.depth() == 2

    node3 = Node(0, "")
    node.insert_child(0, node3)

    assert node.depth() == 0
    assert node1.depth() == 1
    assert node2.depth() == 2
    assert node3.depth() == 1



# Generated at 2022-06-13 18:22:04.530277
# Unit test for method leaves of class Base
def test_Base_leaves():
  from .. import fixer_base
  from ..fixer_util import Leaf, Node

  lines = 'i = 0\ni = 1\n'
  tree = compile(lines, '', 'exec', ast.PyCF_ONLY_AST)

  leaves = list(tree.body[0].leaves())
  assert len(leaves) == 4
  assert leaves[0].value == 'i'
  assert leaves[1].value == '='
  assert leaves[2].value == '0'
  assert leaves[3].value == '\n'

  assert next(tree.body[1].leaves()).value == '\n'

  new = Leaf('', lineno=0, column=0)
  tree.body[1].replace(new)
  leaves = list(tree.body[0].leaves())
  assert len

# Generated at 2022-06-13 18:22:07.531231
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.name) == "name"
    assert type_repr(1) == 1


# A parse tree node class.  This is basically a thin wrapper around a tuple.
# The tuple structure is described in grammar.txt.

# Generated at 2022-06-13 18:22:10.469518
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    """Check that Leaf.pre_order() returns a iterator over the leaf."""
    l = Leaf(1, "a")
    assert l.pre_order() == iter([l])

# Generated at 2022-06-13 18:22:22.728048
# Unit test for function convert
def test_convert():
    from .pgen2 import driver
    from .pgen2.parse import ParseError
    from .pgen2.pgen import _Generator
    from . import tokenize
    from io import StringIO

    driver = driver.Driver(grammar=_Generator("Grammar.txt", "Grammar.cfg"), convert=convert)

    source = """\
if True:
  print(42)
"""

    try:
        driver.parse_tokens(tokenize.generate_tokens(StringIO(source).readline))
    except ParseError as e:
        print("Syntax error")
    else:
        print("Parsed without error")
        print()
        print(driver.root)

