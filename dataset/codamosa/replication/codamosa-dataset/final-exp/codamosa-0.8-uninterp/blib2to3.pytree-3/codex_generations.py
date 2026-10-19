

# Generated at 2022-06-13 18:14:21.725530
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    l = Leaf(token.NAME, 'func', (None, (1, 0)), fixers_applied=[])
    l.pre_order()


# Generated at 2022-06-13 18:14:28.548269
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from blib2to3.pgen2 import driver
    from blib2to3.pgen2 import parse
    from blib2to3.pgen2 import tokenize

    filename = "test_Node_pre_order.py"
    f = StringIO()

    def add_line(line):
        f.write(line + "\n")

    add_line("x = 0")
    add_line("if x: # test")
    add_line("    x += 1")
    tree = parse.parse_string(f.getvalue(), filename, tokenize.detect_encoding(f.getvalue()))

    g22 = Grammar("Grammar22")
    driver.load_grammar("Grammar22", g22)
    g3 = Grammar("Grammar3")
    driver.load_gram

# Generated at 2022-06-13 18:14:29.581743
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    assert BasePattern().match(0) == False


# Generated at 2022-06-13 18:14:31.147676
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    """Unit test for method __repr__ of class BasePattern"""
    try:
        x = BasePattern()
    except NotImplementedError:
        pass



# Generated at 2022-06-13 18:14:34.331811
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    x = Leaf(type_=0, value="0", context=(None, (1, 1)))
    for c in x.post_order():
        assert c is x
    assert x.post_order() is x.post_order()



# Generated at 2022-06-13 18:14:38.422792
# Unit test for method depth of class Base
def test_Base_depth():
    import inspect

    class depth_test_class(Node):
        pass

    depth_test_instance = depth_test_class()
    example_method = getattr(depth_test_instance, 'depth')
    number_of_arguments = len(
        inspect.getfullargspec(example_method).args)
    assert number_of_arguments == 1



# Generated at 2022-06-13 18:14:44.226000
# Unit test for function convert
def test_convert():
    from .ast import parse
    from .tokenize import tokenize
    from .pgen2.parse import ParseError
    from .pgen2.driver import Driver

    def convert(gr, raw_node):
        return Node(raw_node[0], raw_node[-1])

    try:
        driver = Driver(None, convert)
        driver.parse_tokens(tokenize("1 + 1"))
    except ParseError as e:
        pass
    else:
        raise Exception("expected a parse error")

    def convert(gr, raw_node):
        return Leaf(raw_node[0], raw_node[1])

    driver = Driver(None, convert)
    node = driver.parse_tokens(tokenize("1 + 1"))
    assert node.type == 3

# Generated at 2022-06-13 18:14:50.330128
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    class Leaf:
        def __init__(self, val, type=None):
            self.value = val
            self.type = type
    # Handle special case - all nodes match
    leaves = [Leaf("x"), Leaf("y"), Leaf("z")]
    nodes = leaves
    for count in range(3):
        for c, r in WildcardPattern(min=count).generate_matches(nodes):
            if c > count:
                break
            assert c == count
    leaves = [Leaf("x"), Leaf("y"), Leaf("z")]
    nodes = leaves
    # The following is equivalent to "a b c | d e | f g h"
    content = (("a", "b", "c"), ("d", "e"), ("f", "g", "h"))

# Generated at 2022-06-13 18:14:58.883537
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pgen2 import token

    import re
    import unittest

    from .pgen2.grammar import Grammar
    from .pgen2.parse import parse_string  # type: ignore

    _VALID_IDENTIFIER = re.compile(r"[a-zA-Z_][a-zA-Z_0-9]*$")
    _VALID_NUMBER = re.compile(r"\d+$")

    OPERATORS = "PLUS MINUS TIMES DIVIDE LSHIFT RSHIFT POW"

    # Grammar rules

# Generated at 2022-06-13 18:15:05.427104
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    p = P.LeafPattern(1, "")
    eq_(list(p.generate_matches([])), [])
    eq_(list(p.generate_matches([Leaf(1, "")])), [(1, {})])
    eq_(list(p.generate_matches([Leaf(2, "")])), [])
    eq_(list(p.generate_matches([Leaf(1, ""), Leaf(2, "")])), [])
    p = P.LeafPattern(1, "", name="foo")
    eq_(
        list(p.generate_matches([Leaf(1, "")])),
        [(1, {"foo": Leaf(1, "")})],
    )
    p = P.LeafPattern(1, "", name="foo")
    eq

# Generated at 2022-06-13 18:15:48.627578
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    pass

# Generated at 2022-06-13 18:15:57.704602
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    from .pytree import Leaf, Node
    from .pygram import python_grammar

    t = Leaf(1, "foo", 1)
    u = Leaf(1, "foo", 1)
    t.add_prefix("#comment")
    assert t == u
    assert not t != u
    t = Leaf(1, "foo", 1)
    u = Leaf(1, "foo", 1)
    t.add_suffix("#comment")
    assert t == u
    assert not t != u
    t = Leaf(1, "foo", 1)
    u = Leaf(1, "foo", 1)
    t.add_prefix("bla")
    assert t == u
    assert not t != u
    u.add_prefix("bla")
    assert t == u
    assert not t != u

# Generated at 2022-06-13 18:16:05.455181
# Unit test for method clone of class Base
def test_Base_clone():
    #
    # Test the method clone of class Base.
    #
    # This test is for the method clone of the class Base. This method is an
    # abstract method which defines the interface for cloning a node.
    #
    # The method is tested by instantiating subclasses and calling clone to
    # ensure that exceptions are raised.
    #
    try:
        Base().clone()
    except NotImplementedError:
        pass
    else:
        raise Exception("Test failed: did not raise NotImplementedError")

    try:
        Node(1).clone()
    except NotImplementedError:
        pass
    else:
        raise Exception("Test failed: did not raise NotImplementedError")

    try:
        Leaf(1, "").clone()
    except NotImplementedError:
        pass

# Generated at 2022-06-13 18:16:10.326510
# Unit test for constructor of class NodePattern
def test_NodePattern():
    mypattern = NodePattern('mypattern', ('first', 'second', 'third'))
    assert mypattern.type == 'mypattern'
    assert len(mypattern.content) == 3
    assert mypattern.content[0].type == 'first'
    assert mypattern.content[1].type == 'second'
    assert mypattern.content[2].type == 'third'


# Generated at 2022-06-13 18:16:18.600331
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    import philly
    tree = philly.parse_string('''
        del y
        z = 2
    ''')
    leaves = list(tree.pre_order())
    assert leaves[0].type == python_symbols.del_stmt
    assert leaves[1].type == python_symbols.NAME
    assert leaves[1].value == "y"
    assert leaves[2].type == python_symbols.NEWLINE



# Generated at 2022-06-13 18:16:21.142762
# Unit test for method pre_order of class Node
def test_Node_pre_order():
  tree = Node.from_string("def foo(x, y):\n  return x+y\n")
  assert len(list(tree.pre_order())) == 13 
 

# Generated at 2022-06-13 18:16:29.068148
# Unit test for function generate_matches
def test_generate_matches():
    seq = [0, 0, 1, 1, 2, 2]
    patterns = [WildcardPattern(), NodePattern(type=0), WildcardPattern(), NodePattern(2)]
    assert list(generate_matches(patterns, seq)) == [
        (3, {}),
        (6, {}),
        (6, {3: [0, 1, 2]}),
        (6, {2: [0, 1, 2]}),
        (6, {2: [0, 1, 2], 3: [0, 1, 2]}),
    ]
    patterns = [
        WildcardPattern(name="star"),
        NodePattern(type=0, name="obj0"),
        WildcardPattern(name="star"),
        NodePattern(type=2, name="obj2"),
    ]

# Generated at 2022-06-13 18:16:35.730386
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    # This is a host for unit tests for class BasePattern.  When run
    # directly it does nothing.  When run via pytest, these tests are
    # run.
    import pytest
    from ..pgen2 import driver, token, grammar

    def p1():
        """
        An empty grammar, which should have an empty tree pattern.
        """
        p = driver.Driver(grammar.Grammar()).parse_trees[0]
        assert p.match(p.root)

    def p2():
        """
        A grammar with one rule, which should have a simple tree pattern.
        """
        p = driver.Driver(grammar.Grammar([("file_input", "foo")])).parse_trees[0]
        assert p.match(p.root)

# Generated at 2022-06-13 18:16:47.259301
# Unit test for method remove of class Base

# Generated at 2022-06-13 18:16:51.385726
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    class MockPattern(BasePattern):
        pass
    p = MockPattern()
    assert p.optimize() is p


# Generated at 2022-06-13 18:17:12.802894
# Unit test for method remove of class Base
def test_Base_remove():
    if getattr(_Base_in_this_module, "_Base_remove_in_this_module", None):
        class Node(Base):
            __slots__ = ["type", "children"]

            def __init__(self, type: int, children: Optional[List[NL]] = None):
                if children is None:
                    children = []
                self.type = type
                self.children = children

            def __repr__(self):
                return "<Node %s %s>" % (type_repr(self.type), self.children)

            def _eq(self, other):
                return (
                    self.type == other.type
                    and self.children == other.children
                )

            def clone(self):
                return Node(self.type, self.children[:])


# Generated at 2022-06-13 18:17:21.400886
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf, Node
    from .pygram import python_symbols as syms
    parent = Node(syms.file_input, [Leaf(1, "a"), Leaf(1, "b")])
    child = Leaf(1, "c")
    parent.children.append(child)
    child.parent = parent
    child.replace([Leaf(1, "d"), Leaf(1, "e")])
    assert parent.children == [Leaf(1, "a"), Leaf(1, "b"), Leaf(1, "d"), Leaf(1, "e")]
    # Unit test for method changed of class Base

# Generated at 2022-06-13 18:17:29.427387
# Unit test for method clone of class Base
def test_Base_clone():
    edge_cases = []
    def _Base_clone_helper(self, other):
    #self: Base, other: Base
        return self == other
    _Base_clone_helper = _Base_clone_helper
    class Abstract(Base):
        def __init__(self, first,second):
            self.first = first
            self.second = second
        def _eq(self, other):
            return _Base_clone_helper(self, other)
        def clone(self):
            return Abstract(self.first, self.second)
        def post_order(self):
            return self
        def pre_order(self):
            return self
    Abstract.__name__ = "Abstract"

# Generated at 2022-06-13 18:17:33.965006
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    # This can be run as "python -m idlelib.pyparser
    # WildcardPattern_generate_matches" or "python -m unittest
    # idlelib.pyparser.WildcardPattern_generate_matches".

    import idlelib.pyparser
    from idlelib.pyparser import SequenceNode as SN, Leaf as L

    if isinstance(__loader__, str):  # test was run directly
        print('1..3')  # tell TAP harness we plan on running 3 tests
        # Create a test sequence so we can check that results are valid.
        # This is something like:
        #   SN(2, ['\n',
        #          SN(1, [L(0, 'a'), L(0, 'b'), L(0, 'c')]),
        #          SN(1, [

# Generated at 2022-06-13 18:17:38.934182
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    tree = compile("1*4", "", "eval")
    assert isinstance(tree, Node)
    pattern = NodePattern(grm.expr_context)
    assert pattern.match(tree)

# Generated at 2022-06-13 18:17:46.334127
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    p = WildcardPattern(((LeafPattern(type=NAME, name='s'), LeafPattern(type=NUMBER)), LeafPattern(type=NUMBER, name='n'),))
    op = p.optimize()
    assert repr(op) == "WildcardPattern(((LeafPattern(type=NAME, name='s'), LeafPattern(type=NUMBER)), LeafPattern(type=NUMBER, name='n'),), min=1, max=1, name=None)"



# Generated at 2022-06-13 18:17:52.974256
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    # Construct a Node and check result of _pre_order
    node = Node(0, [Leaf(1, "hello"), Leaf(2, "world")])
    expected = [node, node.children[0], node.children[1]]
    actual = list(node.pre_order())
    for i in range(3):
        assert actual[i] is expected[i]



# Generated at 2022-06-13 18:17:58.215589
# Unit test for method post_order of class Node
def test_Node_post_order():
    assert Node(0, []).post_order() == [Node(0, [])]
    assert Node(0, [Leaf(0, 'a'), Leaf(0, 'b')]).post_order() == [Leaf(0, 'a'), Leaf(0, 'b'), Node(0, [Leaf(0, 'a'), Leaf(0, 'b')])]



# Generated at 2022-06-13 18:18:08.736368
# Unit test for function generate_matches

# Generated at 2022-06-13 18:18:15.195405
# Unit test for method clone of class Leaf
def test_Leaf_clone():
    # test cloned object has correct value of prefix
    leaf = Leaf(257,"Tree")
    assert leaf.clone().prefix == ""
    #test cloned object has correct value of type
    leaf = Leaf(257,"Tree")
    assert leaf.clone().type == 257
    #test cloned object has correct value of value
    leaf = Leaf(257,"Tree")
    assert leaf.clone().value == "Tree"
    #test cloned object has correct value of type
    leaf = Leaf(257,"Tree")
    assert leaf.clone().type == 257
    #test cloned object has correct value of context
    leaf = Leaf(257,"Tree",(None,(0,0)))
    assert leaf.clone().value == "Tree"
    #test cloned object has correct value of type

# Generated at 2022-06-13 18:18:35.892407
# Unit test for method depth of class Base
def test_Base_depth():
    assert Base().depth() == 0

# Generated at 2022-06-13 18:18:38.898739
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    p = BasePattern(type=1)
    q = p.optimize()
    assert p is q



# Generated at 2022-06-13 18:18:40.609163
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    # called Base
    pass

# Generated at 2022-06-13 18:18:50.982539
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    """
    Tests for the optimization routines in class BasePattern.

    Because these methods are implemented in subclasses, this test
    includes tests for all Pattern subclasses.
    """
    from .pgen2 import token

    def check(p, *args):
        assert p.optimize() == pytree.NodePattern(*args)

    p = pytree.Wildcard()
    check(p, "*")
    p = pytree.Wildcard(pytree.LeafPattern(token.COMMA), "*")
    check(p, pytree.LeafPattern(token.COMMA), "*")
    p = pytree.NodePattern(syms.testlist, pytree.Wildcard())
    check(p, syms.testlist, "*")

# Generated at 2022-06-13 18:18:56.217079
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    from .pytree import Node, PythonLeaf

    class Node_pre_order_class(Node):
        def pre_order(self):
            yield self
            for child in self.children:
                yield from child.pre_order()

    class Leaf_pre_order_class(PythonLeaf):
        def pre_order(self):
            yield self

    root = Node_pre_order_class(1, "root", [
        PythonLeaf(tokenize.INDENT, "    "),
        Node_pre_order_class(1, "a", [PythonLeaf(1, "a"), PythonLeaf(1, "b")]),
        PythonLeaf(tokenize.DEDENT, ""),
    ])
    node_a = root.children[1]

# Generated at 2022-06-13 18:19:00.674281
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.num_stmt) == "num_stmt"
    assert type_repr(1234567890) == 1234567890



# Generated at 2022-06-13 18:19:01.635982
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    node = ast_parse("pass")
    pattern = NodePattern(type=syms.simple_stmt)
    pattern.match(node)

# Generated at 2022-06-13 18:19:04.093114
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Leaf, Node
    l1 = Leaf(1, "foo")
    l2 = Leaf(1, "bar")
    l3 = Leaf(1, "baz")
    n1 = Node(1, [l1, l2])
    n2 = Node(1, [n1, l3])
    assert list(n2.leaves()) == [l1, l2, l3]



# Generated at 2022-06-13 18:19:08.178000
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    import unittest

    class Tests(unittest.TestCase):
        def check_optimize(self, pattern, expected):
            actual = pattern.optimize()
            msg = "Expected %r, got %r" % (expected, actual)
            assert actual == expected, msg

        def test_optimize(self):
            # No content; min=1, max=1
            self.check_optimize(WildcardPattern(min=1, max=1), NodePattern())
            # No content; min=0, max=HUGE
            self.check_optimize(WildcardPattern(), WildcardPattern())
            # Content with alternatives; min=1, max=1

# Generated at 2022-06-13 18:19:19.360802
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    # None attributes
    assert BasePattern(None, None, None).__repr__() == 'BasePattern(None, None, None)'
    assert BasePattern(None, 'b', None).__repr__() == "BasePattern(None, 'b', None)"
    assert BasePattern(None, 'b', 'c').__repr__() == "BasePattern(None, 'b', 'c')"
    assert BasePattern(None, None, 'c').__repr__() == "BasePattern(None, None, 'c')"
    # Non-None attributes
    assert BasePattern(1, None, None).__repr__() == 'BasePattern(1, None, None)'
    assert BasePattern(1, 'b', None).__repr__() == "BasePattern(1, 'b', None)"

# Generated at 2022-06-13 18:19:42.690261
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    from .load import load
    from .search_strings import Match
    from .compile import Compiler, compare
    from .tree import Node
    import re
    import io

    def _compile(pattern: str) -> Compiler:
        return Compiler(pattern, {})

    def _match(pattern: str, source: str) -> Match:
        return _compile(pattern).match(source)

    def _compile_result(pattern: str) -> Union[Any, Pattern]:
        return _compile(pattern).pattern

    def _load_result(pattern: str) -> Union[Any, Pattern]:
        return load(_compile(pattern).pattern, {})

    def _test(expect: Union[Any, Pattern], pattern: str) -> Pattern:
        cr = _compile_result(pattern)
        lr = _

# Generated at 2022-06-13 18:19:48.670381
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    r"""Unit test for method __eq__ of class Base"""
    global __test_func_context, __test_expectations, __test_expectation_index
    global __test_expectation
    __test_expectations = {
        1: "assert <class 'test_nodes.Base'> == <class 'test_nodes.Base'>",
        2: "<class 'test_nodes.Base'> != <class 'test_nodes.Base'>",
        3: "assert <class 'test_nodes.Base'> != <class 'test_nodes.Base'>",
        4: "<class 'test_nodes.Base'> == <class 'test_nodes.Base'>",
    }
    __test_expectation_index = 1
    __test_func_context = "c"

# Generated at 2022-06-13 18:19:50.420793
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    a = Leaf(1, "a")
    assert(list(a.leaves()) == [a])



# Generated at 2022-06-13 18:19:51.259443
# Unit test for method post_order of class Base
def test_Base_post_order():
    assert False, "Test Not Implemented"



# Generated at 2022-06-13 18:19:56.556612
# Unit test for method generate_matches of class WildcardPattern

# Generated at 2022-06-13 18:20:04.036994
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    def test1():
        def test(self):
            def __init__(self, a, b):
                pass
            return __init__
        return test

    t = Node(syms.decorator,
                [Leaf(token.AT, '@', prefix=' '),
                 Node(syms.dotted_name,
                      [Leaf(token.NAME, 'test1', prefix=''),
                       Leaf(token.NAME, 'test', prefix='.')]),
                Leaf(token.NEWLINE, '\n', prefix='')])

    def test_Leaf_post_order():
        def test(self):
            def __init__(self, a, b):
                pass
            return __init__
        return test


# Generated at 2022-06-13 18:20:12.244109
# Unit test for method __repr__ of class Leaf
def test_Leaf___repr__():
    """
    Unit test for method __repr__ of class Leaf.
    """
    from .pgen2.grammar import Nonterminal

    # Default values for instance variables
    type = Nonterminal("atom")
    value = "'None'"
    fixers_applied: List[Any] = []
    bracket_depth = 1
    opening_bracket = Leaf("'['")
    used_names: Optional[Set[Text]] = set(["foo", "bar"])
    lineno = 1
    column = 1
    node = Leaf(type, value, fixers_applied=fixers_applied,
                bracket_depth=bracket_depth, opening_bracket=opening_bracket,
                used_names=used_names, lineno=lineno, column=column)
    result = repr(node)
    assert result

# Generated at 2022-06-13 18:20:26.765974
# Unit test for method post_order of class Base
def test_Base_post_order():
    """Test method Base.post_order"""
    import sys
    from io import StringIO
    import unittest
    import lib2to3.pgen2.token as token
    from lib2to3.pytree import Leaf, Node, Base
    from lib2to3.pygram import python_grammar

    class TestNode(Node):
        def __init__(self, *args, **kwds):
            super(TestNode, self).__init__(*args, **kwds)

        def _eq(self, other):
            return self.type == other.type and self.children == other.children

        def clone(self):
            return TestNode(self.type, self.children)

        def post_order(self):
            yield self
            for child in self.children:
                yield from child.post_order()

       

# Generated at 2022-06-13 18:20:34.599497
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Node, Leaf
    # Predefined variables for testing purposes
    # A Node
    node = Node(1, [])
    # Assert the leaves method yields nothing because the node has no children
    assert list(node.leaves()) == []
    # A Leaf
    node = Node(1, [Leaf(1, "")])
    # Assert the leaves method yields just one leaf
    assert list(node.leaves())[0].type == 1

# Generated at 2022-06-13 18:20:39.419411
# Unit test for method remove of class Base
def test_Base_remove():
    grammar = Grammar()
    grammar.parse("""
a: ('b' 'c')*
""")
    parser = grammar.build_parser()
    tree = parser.parse("bcbcbc")
    print("before", tree.children[0].children[0].remove())
    print("after", tree)


# Generated at 2022-06-13 18:21:07.411299
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    from .pygram import python_symbols as syms
    from .pygram import python_operators as ops
    from .pgen2 import driver
    pgen = driver.Driver()
    pgen.load_grammar()

    # Test the empty parse tree
    p = NegatedPattern(None)
    assert tuple(p.generate_matches([])) == ((0, {}),)

    # Test missing matches
    p = NegatedPattern(NodePattern(syms.atom, [LeafPattern(ops.STAR)]))
    assert tuple(p.generate_matches([])) == ((0, {}),)
    assert tuple(p.generate_matches([pgen.syms[ops.STAR]])) == ()

    # Test existing matches

# Generated at 2022-06-13 18:21:13.027826
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    """
    Test for method post_order of class Leaf

    Not in a unit test, because it modifies self.children
    """
    from .pytree import Leaf

    l1 = Leaf(1, 'u')
    l2 = Leaf(1, 'v')
    l1.post_order()


# Generated at 2022-06-13 18:21:23.414312
# Unit test for method replace of class Base
def test_Base_replace():
    # test replacing node by a single node
    class Parent(Node):
        def __init__(self, children):
            super(Parent, self).__init__(syms.parent, children)

    class Child1(Leaf):
        _flds = ['leaf']

        def __init__(self, value):
            super(Child1, self).__init__(syms.child1, value, lineno=1)

    class Child2(Leaf):
        _flds = ['leaf']

        def __init__(self, value):
            super(Child2, self).__init__(syms.child2, value, lineno=2)

    leaf1 = Child1("leaf1")
    node = Parent([leaf1])

    leaf2 = Child2("leaf2")
    node.replace(leaf2)


# Generated at 2022-06-13 18:21:24.780611
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    t = Base()
    assert t.pre_order() == []



# Generated at 2022-06-13 18:21:32.642888
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import logging
    import unittest
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    class TestPattern(BasePattern):
        def match(self, node: NL, results: Optional[_Results] = None) -> bool:
            r: _Results = {}
            if node.type == 1:
                r["t"] = node
            elif node.type == 2:
                r["d"] = node
            if results:
                results.update(r)
            return False

    class IterateTests(unittest.TestCase):
        def test_generate_matches(self):
            a = Leaf(1, "a")
            b = Leaf(1, "b")
            d = Leaf(2, "d")

# Generated at 2022-06-13 18:21:42.970222
# Unit test for method post_order of class Node
def test_Node_post_order():
    from .pgen2.parse import ParseError
    from .pgen2.pgen import PgenParser, PgenLexer
    import blib2to3.parse
    p = PgenParser(blib2to3.parse.PythonParser(grammar=Grammar()),PgenLexer())
    s = "a = 1 + 2 # a comment.\n"
    res = p.parse(s, 'single_input')
    x = res.post_order()

# Generated at 2022-06-13 18:21:49.924641
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    a = None
    b = Leaf(1, '1', (None, (1, 1)), [])
    c = Leaf(1, '1', (None, (1, 1)), [])
    r = {'a': b}
    q = {'a': c}
    assert list(a.generate_matches([b])) == [(1, {'a': b})]
    assert list(a.generate_matches([c])) == [(1, {'a': c})]
    assert list(a.generate_matches([])) == []
    assert list(b.generate_matches([b])) == [(1, {'a': b})]
    assert list(b.generate_matches([c])) == []
    assert list(b.generate_matches([])) == []

# Generated at 2022-06-13 18:22:03.150345
# Unit test for method post_order of class Node
def test_Node_post_order():
    import unittest

    class TestNode(unittest.TestCase):

        def test_post_order_simple(self):
            n = Node(python_symbols.power, [
                Leaf(token.NAME, "a"),
                Leaf(token.NAME, "b")
            ])
            result = [n.type, n.children[0].type, n.children[1].type]
            self.assertEqual(result, [
                python_symbols.power,
                token.NAME,
                token.NAME
            ])
            self.assertEqual(list(n.post_order()), [
                n.children[0],
                n.children[1],
                n
            ])


# Generated at 2022-06-13 18:22:12.675285
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    import unittest


# Generated at 2022-06-13 18:22:20.459590
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf, Node

    n = Node(0, [Leaf(1, "1"), Leaf(2, "2")])
    n[1].replace(Leaf(3, "3"))
    assert n == Node(0, [Leaf(1, "1"), Leaf(3, "3")])
    n[1].replace([Leaf(4, "4"), Leaf(5, "5")])
    assert n == Node(0, [Leaf(1, "1"), Leaf(4, "4"), Leaf(5, "5")])
    n[1].replace([])
    assert n == Node(0, [Leaf(1, "1"), Leaf(5, "5")])
    n[1].replace(None)
    assert n == Node(0, [Leaf(1, "1")])
   