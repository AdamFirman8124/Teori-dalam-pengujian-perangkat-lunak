

# Generated at 2022-06-13 18:15:10.701674
# Unit test for method pre_order of class Node
def test_Node_pre_order():
  # Test case for Node.pre_order.
  import io
  import unittest
  from .pytree import Leaf, Node
  from . import pygram
  from . import pytree
  from . import python_symbols
  from .pgen2 import driver
  from .pgen2 import token
  from . import pygram
  from . import pytree
  from . import python_symbols
  from .pgen2 import driver
  from .pgen2 import token
  # Successful cases.
  # Basic setup - just a single leaf.
  l = Leaf(1, 'value')
  assert l.pre_order() == [l], 'Error_0'
  # Basic setup - 2 leaves.
  l1 = Leaf(1, 'value')
  l2 = Leaf(2, 'value')

# Generated at 2022-06-13 18:15:13.366998
# Unit test for function type_repr
def test_type_repr():
    # Make sure some type codes get stringified; we don't care which.
    assert isinstance(type_repr(python_symbols.not_test), Text)



# Generated at 2022-06-13 18:15:18.243896
# Unit test for function convert
def test_convert():
    import random
    from pgen2.parser import Parser

    p = Parser()
    g = p.grammar
    for i in range(100):
        type = random.randrange(0, 256)
        context = None
        value = None
        children = []
        for j in range(10):
            child = Leaf(random.randrange(0, 256), str(j))
            children.append(child)
        if random.random() < 0.3:
            type = g.symbol2number["atom"]
            children = []
        if random.random() < 0.3:
            value = str(i)
        n = Node(type, children, value=value, context=context)
        n1 = convert(g, (type, value, context, children))
        assert n == n1



# Generated at 2022-06-13 18:15:31.909839
# Unit test for method post_order of class Base
def test_Base_post_order():
    import pytree
    r = pytree.pygram().parse("a = 1 + 2")
    a = r.post_order()
    assert next(a) == r.children[2]
    assert next(a) == r.children[1]
    assert next(a) == r.children[0]
    assert next(a) == r

# Generated at 2022-06-13 18:15:40.792557
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pgen2.token import LPAR
    from . import parse

    # Create a pattern
    pat = LeafPattern(LPAR, "(");

    # The pattern matches one node
    for nnodes, results in pat.generate_matches([Tree(LPAR, '(')]):
        assert nnodes == 1
        assert len(results) == 0

    # The pattern doesn't match another
    for nnodes, results in pat.generate_matches([Tree(0, '')]):
        assert False, "The pattern shouldn't match the input"



# Generated at 2022-06-13 18:15:52.115709
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    from typing import List, Optional

    from .grammar import Grammar, Leaf, Node

    def _check(
        p: Optional[Union[BasePattern, List[BasePattern]]], expected: List[BasePattern]
    ):
        if p is None:
            optimized = None
        else:
            if isinstance(p, list):
                optimized = [x.optimize() for x in p]
            else:
                optimized = p.optimize()
        assert optimized == expected

    test_grammar = Grammar(
        """
        A -> B (C | D)* E
        B -> 'b'
        C -> 'c'
        D -> 'd'
        E -> 'e'
        """
    )

    _check(test_grammar.produce("A"), [NodePattern(name="A")])

    _check

# Generated at 2022-06-13 18:16:00.609814
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(0) == 0
    assert type_repr(4) == "and_test"
# End of function test_type_repr


# def print_node(node, out=None, indent=""):
#     """Print a node to a file using pretty-print."""
#     if out is None:
#         out = sys.stdout
#     write = out.write
#     write(indent + type_repr(node.type))
#     if node.value is not None:
#         write(f"({node.value!r})")
#     if len(node.children) == 1:
#         make_lines = node.children[0].type in NEWLINES
#     else:
#         make_lines = False
#     # TODO: make this configurable
#     if make

# Generated at 2022-06-13 18:16:01.780575
# Unit test for method leaves of class Base
def test_Base_leaves():
    assert list(Base().leaves()) == []

# Generated at 2022-06-13 18:16:15.412101
# Unit test for function generate_matches
def test_generate_matches():
    n = Node("")
    nodes = [n, n, n]
    p1 = NodePattern()
    p2 = NodePattern()
    p3 = NodePattern(name="p")
    p4 = NodePattern(name="p")

    assert list(generate_matches([], nodes)) == [(0, {})]
    assert list(generate_matches([p1], nodes)) == [(1, {})]
    assert list(generate_matches([p1, p2], nodes)) == [(2, {})]
    assert list(generate_matches([p3, p4], nodes)) == [(2, {"p": [n, n]})]
    assert list(generate_matches([p1, p2, p3], nodes)) == [(3, {"p": [n]})]

# Generated at 2022-06-13 18:16:25.033679
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from pprint import pprint
    from .pytree import Node, Leaf, type_repr
    from . import pygram

    for t in pygram.python_grammar.number2symbol:
        if t >= 256:
            t = type_repr(t)
            break
    else:
        assert False, 'no non-terminals in python grammar?'
    node = Node(t, [Leaf(1, ""), Leaf(2, "")])
    node.changed()
    prefixed_children = [child for child in node.pre_order()]
    assert prefixed_children == [node, node.children[0], node.children[1]]
    for child in prefixed_children:
        assert isinstance(child, (Node, Leaf)), pprint(prefixed_children)



# Generated at 2022-06-13 18:17:02.771373
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Leaf
    from .pygram import python_symbols as syms

    def t_n(type, value, *children):
        return Node(type, value, children)

    def t_l(type, value):
        return Leaf(type, value)

    t = t_n(
        syms.file_input, "<file_input>",
        t_n(
            syms.simple_stmt, "<simple_stmt>",
            t_l(syms.NAME, "x"),
            t_l(syms.EQUAL, "="),
            t_l(syms.NAME, "y")
        ),
        t_l(token.NEWLINE, "\n")
    )

    assert t.depth() == 0
    assert t.children[0].depth() == 1

# Generated at 2022-06-13 18:17:04.662088
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    n = NegatedPattern(content=WildcardPattern())
    assert list(n.generate_matches([])) == [(0, {})]
    assert list(n.generate_matches([None])) == []
    assert list(n.generate_matches([None, None])) == []



# Generated at 2022-06-13 18:17:14.980863
# Unit test for constructor of class NodePattern
def test_NodePattern():
    NodePattern(257, "a", "foo")
    NodePattern(257, ["a", "b"])
    NodePattern(257, name="foo")
    NodePattern(257, content=["a", "b"], name="foo")
    NodePattern(257, ["a", "b"], name="foo")
    NodePattern(257, nodes=["a", "b"], name="foo")
    NodePattern(257, nodes=["a", "b", "c"], name="foo")
    NodePattern(nodes=["a", "b", "c"], type=257, name="foo")
    NodePattern(content=["a", "b"], type=257, name="foo")



# Generated at 2022-06-13 18:17:24.941669
# Unit test for method clone of class Base
def test_Base_clone():
    """
    >>> from .pytree import Leaf, Node
    >>> from .pygram import python_symbols
    >>> n = Node(python_symbols.power, [Leaf(1, 'a'), Leaf(1, 'b')])
    >>> n2 = n.clone()
    >>> n2.type == python_symbols.power
    True
    >>> n2 == n
    True
    >>> n2 is not n
    True
    >>> n3 = n.clone()
    >>> n3.replace(n2.children)
    >>> n3 == n
    True
    >>> n4 = n.clone()
    >>> n4.children[0].value = 'c'
    >>> n4 == n
    False
    """



# Generated at 2022-06-13 18:17:32.715886
# Unit test for method set_child of class Node
def test_Node_set_child():
    from . import pytree
    from .pgen2 import token
    import unittest

    class TestNode(unittest.TestCase):
        
        def test_set_child(self):
            """verify that a child node gets parented when it is set with set_child"""
            node1 = pytree.Node(token.TEST, [])
            node2 = pytree.Node(token.TEST_NOCASE, [])
            node1.set_child(0, node2)
            self.assertEqual(node1, node2.parent)


# Generated at 2022-06-13 18:17:43.948068
# Unit test for function generate_matches
def test_generate_matches():
    from .parse import PyCF_ONLY_AST

    code = """
        # Comments may have double quotes
        for x in [1,2,3]:
            print("%d" % x)
        """
    tree = parse(code, mode="exec")
    print(ast.dump(tree, True, True))

    # Match a For node with a list comprehension
    pat = NodePattern(
        type=ast.For,
        content=[
            NamePattern("var"),
            NodePattern(type=ast.ListComp, content=[NamePattern("elt")]),
        ],
    )

    # Match For nodes with different contents

# Generated at 2022-06-13 18:17:51.076425
# Unit test for function generate_matches
def test_generate_matches():

    pattern = Sequence(
        NodePattern(type=1),
        NodePattern(type=2),
        NodePattern(type=3),
        NodePattern(type=4),
        NodePattern(type=5),
    )
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]

    for count, result in generate_matches(pattern.content, nodes):
        assert count == 5
        assert result == {}

    pattern = Sequence(
        NodePattern(type=1),
        NodePattern(type=2),
        NodePattern(type=3),
        WildcardPattern(min=1, max=1),
        NodePattern(type=5),
    )
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]

    count, result = next

# Generated at 2022-06-13 18:17:52.744923
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    x = BasePattern()
    x.match_seq(nodes=[True])
    x.generate_matches(nodes=[True])

# Generated at 2022-06-13 18:17:55.973336
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    import ast
    import astunparse
    input = """
if a:
    pass
elif b:
    pass
"""
    module = ast.parse(input)

    #assert False, astunparse.dump(module)
    assert astunparse.dump(module) == input

    leafs = list(module.body[0].body[0].post_order())
    assert type(leafs[0]) == ast.If
    assert type(leafs[1]) == ast.Name
    assert type(leafs[2]) == ast.Pass
    assert type(leafs[3]) == ast.Pass


# Generated at 2022-06-13 18:18:07.430632
# Unit test for method post_order of class Node
def test_Node_post_order():
    import lib2to3.fixer_util
    import lib2to3.pygram
    import lib2to3.pgen2
    import logilab.common.sourceutils
    from lib2to3.fixes.fix_dict import MappingProxyType
    import six
    import sys
    import types
    import unittest
    import unittest.mock
    if sys.version_info < (3,):
        import imp
    else:
        imp = None
    import_success = True
    try:
        import collections.abc
    except:
        import_success = False
    else:
        del collections.abc
        import_success = True
        if import_success:
            import_success = False
            try:
                import typing
            except:
                pass
            else:
                del typing

# Generated at 2022-06-13 18:18:37.074363
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    try:
        Base().get_suffix()
    except NotImplementedError:
        pass
    else:
        raise AssertionError("did not raise NotImplementedError")
Base.get_suffix.__test__ = False


# Generated at 2022-06-13 18:18:49.877495
# Unit test for function generate_matches
def test_generate_matches():
    from .grammar import Operand
    from .grammar import Operator
    from .grammar import Expr

    a, b, c = NL("a"), NL("b"), NL("c")
    x, y, z = NL("x"), NL("y"), NL("z")
    expr_end = NodePattern(type=tokenize.ENDMARKER)

    # Each test case is a 4-tuple:
    #     (sequences of patterns, sequence of nodes, answers, failure message)
    # where the answers are either True or False,
    # and if True, the answers are the total number of matches.

# Generated at 2022-06-13 18:18:55.352809
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    import random
    import unittest

    def generate_random_AST(max_depth, terminal_ratio, bfactor=2):
        name = "A" + str(random.randint(0, 20))
        t = random.randint(0, 100 * terminal_ratio)
        if max_depth == 1 or t < terminal_ratio:
            return [Leaf(name, "")]
        r = 1 + random.randint(0, bfactor)
        return [
            Node(
                name,
                [
                    generate_random_AST(max_depth - 1, terminal_ratio, bfactor)
                    for i in range(r)
                ],
            )
        ]

    def is_terminal(node):
        return isinstance(node, Leaf)


# Generated at 2022-06-13 18:19:00.971407
# Unit test for method leaves of class Base
def test_Base_leaves():
    foo = Node(1, children=[Leaf(1, "a"), Leaf(2, "b"), Leaf(3, "c")])
    res = [i.value for i in foo.leaves()]
    assert res == ["a", "b", "c"]

# Generated at 2022-06-13 18:19:11.187042
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    for r in generate_matches([LeafPattern("a"), LeafPattern("b")], iter(["a", "b"])):
        assert False
    for r in generate_matches([LeafPattern("a"), LeafPattern("b")], iter(["a", "b", "c"])):
        assert False
    assert list(generate_matches([LeafPattern("a")], iter(["a"]))) == [(1, {})]
    assert list(generate_matches([LeafPattern("a")], iter(["b"]))) == [(0, {})]
    assert list(generate_matches([LeafPattern("a")], iter(["a", "a"]))) == [(1, {})]

# Generated at 2022-06-13 18:19:18.712179
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    a = WildcardPattern([[LeafPattern(token.NAME, "a")]], min=0)
    b = WildcardPattern([[LeafPattern(token.NAME, "b")]], min=0)
    p = WildcardPattern([[a, b]], min=0)
    p1 = p.optimize()
    p1.min = 0
    p1.max = HUGE
    assert p1 == p, p.optimize()

    a = LeafPattern(token.NAME, "a")
    b = LeafPattern(token.NAME, "b")
    p = WildcardPattern([[a, b]], min=1)
    p1 = p.optimize()
    p1.min = 1
    p1.max = 1
    assert p1 == p, p.optimize()

    a = Wildcard

# Generated at 2022-06-13 18:19:21.460313
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    nodes = [Node(0, [])]
    bp = BasePattern()
    assert bp.match_seq(nodes) == False


# Generated at 2022-06-13 18:19:24.616991
# Unit test for method __eq__ of class Base
def test_Base___eq__():

    # AssertionError: Cannot instantiate Base
    assert Base()
    # AssertionError: Cannot instantiate Base
    assert Base()



# Generated at 2022-06-13 18:19:37.371290
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    from .pytree import Whitespace, Keyword, Name, parse

    tree = parse("x = 5")
    found = False
    for subtree in tree.post_order():
        if (
            isinstance(subtree, Name)
            and subtree == Name(None, "x", prefix="")
        ):
            found = True
            break
    assert found
    found = False
    for subtree in tree.post_order():
        if (
            isinstance(subtree, Keyword)
            and subtree == Keyword(None, "x", prefix="")
        ):
            found = True
            break
    assert not found



# Generated at 2022-06-13 18:19:45.789574
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    # TODO: need more tests
    assert repr(BasePattern(56, 'content', 'name')) == "BasePattern(56, 'content', 'name')"
    assert repr(BasePattern(56, None, None)) == 'BasePattern(56)'
    assert repr(BasePattern(56, 'content', None)) == "BasePattern(56, 'content')"
    assert repr(BasePattern(56, None, 'name')) == "BasePattern(56, None, 'name')"
    assert repr(BasePattern(None, None, None)) == 'BasePattern(None)'


# Generated at 2022-06-13 18:20:04.043674
# Unit test for function generate_matches
def test_generate_matches():
    f = File(name=u"f", type=10)
    g = File(name=u"g", type=10)
    h = File(name=u"h", type=10)
    patterns = [WildcardPattern(name=u"a"), NodePattern(name=u"b"), WildcardPattern(name=u"c")]
    a, b, c = patterns


# Generated at 2022-06-13 18:20:07.714543
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Node
    n = Node(1)
    n.parent = Node(1)
    n.parent.parent = Node(1)
    assert n.depth() == 2


# Generated at 2022-06-13 18:20:17.500427
# Unit test for method set_child of class Node
def test_Node_set_child():
    """Unit test for set_child method of class Node"""
    from .pytree import Node, Leaf
    from .pygram import python_symbols as syms

    a = Leaf(1, "a")
    b = Leaf(1, "b")
    target = Node(syms.a, [a, b])
    replacement = Leaf(1, "c")
    target.set_child(1, replacement)
    assert target.children == [a, replacement]
    assert replacement.parent == target
    assert b.parent is None



# Generated at 2022-06-13 18:20:29.070339
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    """Test match() and generate_matches() of WildcardPattern."""

    def gen_match(pattern, nodes, trace=False):
        """
        Run generate_matches and return the results.

        Args:
            pattern: a pattern
            nodes: sequence of nodes
            trace: if True, print debugging info

        Returns:
            the last returned results dict
        """
        count = 0
        if trace:
            print("###", " ".join(str(node) for node in nodes))
            print("### pattern", pattern)
        for count, results in pattern.generate_matches(nodes):
            if trace:
                print(count, results)
        if trace:
            print("### total", count)
        return results

    # The following are the various tests:

    # Simplest case:
    assert gen_match

# Generated at 2022-06-13 18:20:34.560171
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    """Unit test for BasePattern.generate_matches"""
    print("test_BasePattern_generate_matches")
    from .pgen2.token import NAME, NUMBER
    from .pgen2.parser import sequence2st
    from .pytree import NodePattern as N, LeafPattern as L

    with warnings.catch_warnings(record=True) as w:
        b = BasePattern()
        assert b.generate_matches([]) == iter([])
        assert b.generate_matches([L(NAME)]) == iter([])
        assert len(w) == 2

    n = N("expr")
    l = L(NUMBER)
    assert n.generate_matches([]) == iter([])
    assert n.generate_matches([L(NAME)]) == iter([])

# Generated at 2022-06-13 18:20:35.840718
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    from .pgen2 import token

    assert isinstance(BasePattern(token.WILD).optimize(), WildcardPattern)



# Generated at 2022-06-13 18:20:38.755209
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    global root1
    root1 = Node(syms.file_input, [Leaf(token.ENDMARKER, "", (1, 0))])
    return "pass"

# Generated at 2022-06-13 18:20:48.098907
# Unit test for constructor of class NodePattern
def test_NodePattern():
    assert NodePattern(symbol.dictorsetmaker, [LeafPattern(token.NAME)])
    raises(AssertionError, NodePattern, symbol.dictorsetmaker, [])
    raises(AssertionError, NodePattern, symbol.dictorsetmaker, ["test"])
    raises(AssertionError, NodePattern, symbol.dictorsetmaker, [1])
    assert NodePattern(symbol.dictorsetmaker, name="test")
    raises(AssertionError, NodePattern, symbol.dictorsetmaker, ["test"], name="test")
    raises(AssertionError, NodePattern, symbol.dictorsetmaker, [LeafPattern(token.NAME)], name="test")



# Generated at 2022-06-13 18:20:50.860521
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    class MyPattern(BasePattern):
        type = 2
    pat = MyPattern()
    node = Leaf(2, 3)
    assert list(pat.generate_matches([node])) == [(1, {})]
    pat.name = "foo"
    assert list(pat.generate_matches([node])) == [(1, {"foo": node})]



# Generated at 2022-06-13 18:20:53.977927
# Unit test for method depth of class Base
def test_Base_depth():
    if Base.depth(object()) != 0:
        return False
    if Base.depth(type) != 3:
        return False
    if Base.depth(object.__new__) != 3:
        return False
    return True



# Generated at 2022-06-13 18:21:09.681769
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from . import driver

    pattern = driver.LeafPattern(1, "abc")
    assert list(pattern.generate_matches([driver.Leaf(1, "abc")])) == [(1, {})]



# Generated at 2022-06-13 18:21:21.273550
# Unit test for method get_lineno of class Base

# Generated at 2022-06-13 18:21:29.999460
# Unit test for function generate_matches

# Generated at 2022-06-13 18:21:32.761668
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    print("test_Base___eq__")
    n = Node(1, "b", None)
    assert n == n




# Generated at 2022-06-13 18:21:43.048434
# Unit test for method post_order of class Node
def test_Node_post_order():
    from . import pytree

    # pass  # TODO: implement your test here
    import io
    import os
    import unittest

    from blib2to3.fixer_base import BaseFix
    from Lib2to3 import pygram
    from Lib2to3.pgen2 import driver, token, tokenize
    from Lib2to3.pygram import python_symbols as syms
    from Lib2to3.pytree import Base, Leaf, Node

    class TestNode(unittest.TestCase):
        node_class = Node
        leaf_class = Leaf
        def setUp(self):
            super().setUp()
            #       0
            #      /|\
            #     1 2 3
            #    / \
            #   4   5
            #   |
            #   6
            #

# Generated at 2022-06-13 18:21:48.309871
# Unit test for method post_order of class Node
def test_Node_post_order():
    import unittest
    import sys
    import io
    import tokenize
    from unittest.mock import patch
    from pgen2.tokenize import generate_tokens
    from pgen2.pgen import driver
    import pgen2.pgen
    from pgen2.parser import Parser
    import pgen2.grammar
    grammar = pgen2.grammar.Grammar()

# Generated at 2022-06-13 18:22:01.275828
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    # Test case based on bug #16251
    pattern = NegatedPattern(NodePattern(type=_token.INDENT, name="INDENT"))
    # Should match any INDENT with children
    matched, results = pattern.match_seq([(
        _token.INDENT,
        " ",
        [(
            _token.STRING,
            "foo",
            [(
                _token.DEDENT,
                "",
                []
            )]
        )]
    )])
    assert not matched
    assert not results
    matched, results = pattern.match_seq([(
        _token.DEDENT,
        "",
        []
    )])
    assert matched
    assert results == {}


# Generated at 2022-06-13 18:22:11.274676
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    assert eval(repr(LeafPattern(25, "a"))) == LeafPattern(25, "a")
    assert eval(repr(LeafPattern(25, "a", "name"))) == LeafPattern(25, "a", "name")
    assert eval(repr(NodePattern(26, "a"))) == NodePattern(26, "a")
    assert eval(repr(NodePattern(26, "a", "name"))) == NodePattern(26, "a", "name")
    assert eval(repr(WildcardPattern(27, "a"))) == WildcardPattern(27, "a")
    assert eval(repr(WildcardPattern(27, "a", "name"))) == WildcardPattern(27, "a", "name")


# Generated at 2022-06-13 18:22:23.531531
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Leaf, Node
    from .pygram import python_symbols

    t = Node(python_symbols.prog, [
        Node(python_symbols.funcdef, [
            Node(python_symbols.parameters, [
                Leaf(token.LPAR, "("),
                Leaf(token.RPAR, ")"),
                ], prefix=""),
            Node(python_symbols.suite, [
                Leaf(token.NEWLINE, "\n"),
            ]),
        ]),
     ])
    s = "def foo():\n"
    assert "".join(l.value for l in t.leaves()) == s
    assert "".join(l.value for l in t.children[0].leaves()) == s