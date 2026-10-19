

# Generated at 2022-06-13 18:14:13.954114
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    assert hasattr(Base, 'pre_order')
    assert callable(Base.pre_order)
    assert Base.pre_order is not Base.pre_order.__func__

# Generated at 2022-06-13 18:14:16.789631
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    def f(self, node, results=None):
        raise NotImplementedError
    A = type('A', (BasePattern,), {'_submatch': f})
    x = A() ; assert x is x.optimize()



# Generated at 2022-06-13 18:14:24.931639
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    class TestPattern(BasePattern):
        def __init__(self, *args):
            self.args = args
            # Unit test for method match of class BasePattern
    def test_BasePattern_match():
        class TestPattern(BasePattern):
            def __init__(self, *args):
                self.args = args

        def _submatch(self, node, results):
            return True

        node = Leaf(0, "")
        p = TestPattern(1, 2, c=3)
        assert p.match(node) is True
        q = TestPattern(1, 2, c=4)
        assert p.match(node) is True



# Generated at 2022-06-13 18:14:34.050006
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    a, b, c, d, e = map(Leaf, "abcde")
    if a.match_seq([a, b, c, d, e]) != 1:
        raise RuntimeError
    if b.match_seq([a, b, c, d, e]) != 0:
        raise RuntimeError
    if c.match_seq([a, b, c, d, e]) != 0:
        raise RuntimeError
    if d.match_seq([a, b, c, d, e]) != 0:
        raise RuntimeError
    if e.match_seq([a, b, c, d, e]) != 0:
        raise RuntimeError
    if a.match_seq([a, b, c, d]) != 1:
        raise RuntimeError

# Generated at 2022-06-13 18:14:35.754169
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == 'NAME'



# Generated at 2022-06-13 18:14:42.090853
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    t = ast.parse('len("hello")')
    pattern1 = NodePattern(syms.atomtrailers,
                           [LeafPattern(token.LPAR, '('),
                            NodePattern(syms.atom,
                                        [LeafPattern(token.STRING, '"hello"')]),
                            LeafPattern(token.RPAR, ')')],
                           name='call')
    pattern2 = NegatedPattern(pattern1)
    print("Matches for NegatedPattern with pattern:")
    for c, r in pattern2.generate_matches(t.children):
        print(c, r)
    print("Matches for NegatedPattern without pattern:")
    pattern2 = NegatedPattern()

# Generated at 2022-06-13 18:14:46.239845
# Unit test for method depth of class Base
def test_Base_depth():
    """
    Test coverage for the depth method of class Base

    This test case verifies that the depth method of class Base works as
    expected when there is a parent above the node.
    """
    node = Node(0, None, (), [])
    node2 = Node(0, None, (), [])
    node.parent = node2
    assert node.depth() == 1

# Generated at 2022-06-13 18:14:57.275254
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    from lib2to3.pgen2 import token
    from lib2to3.pgen2.grammar import LeafPattern, BasePattern
    from lib2to3.pgen2 import driver
    from lib2to3.pgen2.parse import parse_grammar, convert_notation
    from .pgen2 import token

    def tokenize(text):
        driver._tokens = []
        tokenize_loop(text)
        return driver._tokens

    tokens = """
    NAME
    NUMBER
    STRING
    PLUS
    MINUS
    STAR
    EQUALS
    FOR
    WHILE
    if
    else
    def
    """.split()
    tokens = [NAME] + list(map(token.tok_name.__getitem__, tokens))

# Generated at 2022-06-13 18:14:58.137542
# Unit test for method post_order of class Base
def test_Base_post_order():
    check_post_order(Base)



# Generated at 2022-06-13 18:15:06.829764
# Unit test for method leaves of class Base
def test_Base_leaves():
    import _ast
    assert [l.type for l in Leaf(0, "x").leaves()] == [0]
    assert [l.type for l in Leaf(0, "x").clone().leaves()] == [0]
    node = _ast.parse("x + y")
    assert [l.type for l in node.leaves() if l.type != token.INDENT] == \
        [token.NAME, token.PLUS, token.NAME]



# Generated at 2022-06-13 18:15:35.406616
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    import unittest
    from .pgen2 import token
    from . import tokenize
    from io import StringIO
    from test.support import captured_stdout, captured_stderr

    class TestLeaf(unittest.TestCase):
        def test_pre_order(self):
            s = 'import sys; print("hello")'
            inps = tokenize.generate_tokens(StringIO(s).readline)
            a = []
            for t in inps:
                a.append(Leaf(*t))
            self.assertEqual(len(a), 8)
            self.assertEqual(a[0].type, token.NAME)
            self.assertEqual(a[0].value, "import")
            self.assertEqual(a[0].prefix, "")

# Generated at 2022-06-13 18:15:43.232387
# Unit test for method replace of class Base
def test_Base_replace():
    from .pygram import python_symbols as syms
    from .pytree import Node, Leaf
    foo = Node(syms.simple_stmt, [Leaf(1, "foo")])
    bar = Node(syms.simple_stmt, [Leaf(1, "bar")])
    baz = Node(syms.simple_stmt, [Leaf(1, "baz")])
    ifo = Node(syms.file_input, [foo, bar, baz])
    foo.replace(bar)
    assert ifo == Node(syms.file_input, [bar, baz])



# Generated at 2022-06-13 18:15:49.717813
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    def treedef(content, name='<treedef>'):
        t = ast.parse(content)
        return NodePattern(type=t.type, content=t.children, name=name)

    # all negative

    # negation of nothing
    tree = NegatedPattern()
    matches = sorted(tree.generate_matches([1]))
    assert matches == []

    # negation of non-empty sequence of nodes
    tree = NegatedPattern(content=treedef("1"))
    matches = sorted(tree.generate_matches([1]))
    assert matches == []

    # negation of empty sequence of nodes
    tree = NegatedPattern(content=treedef(""))
    matches = sorted(tree.generate_matches([1]))
    assert matches == [(0, {})]

    # neg

# Generated at 2022-06-13 18:15:55.726648
# Unit test for method update_sibling_maps of class Node
def test_Node_update_sibling_maps():
    # tests the method returns correct results with nodes in the expected
    # position
    tree_simple = Node(type=256,
                           children=[Leaf(1, 'a'), Leaf(1, 'b'), Leaf(1, 'c')])
    tree_simple.update_sibling_maps()
    assert tree_simple.next_sibling_map[id(tree_simple.children[0])] == \
        tree_simple.children[1]
    assert tree_simple.prev_sibling_map[id(tree_simple.children[1])] == \
        tree_simple.children[0]
    assert tree_simple.next_sibling_map[id(tree_simple.children[1])] == \
        tree_simple.children[2]

# Generated at 2022-06-13 18:16:04.497399
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import unittest
    import sys
    import os

    class UnitTest_BasePattern_generate_matches(unittest.TestCase):
        def test_1(self):
            from .pgen2 import token

            c = BasePattern()
            c.type = token.NAME
            c.content = "async"
            c.name = "name"
            self.assertEqual(list(c.generate_matches([])), [])

        def test_2(self):
            from .pgen2 import token

            c = BasePattern()
            c.type = token.COMMA
            c.name = "comma"
            c.content = None
            self.assertEqual(
                list(c.generate_matches([])),
                [],
            )


# Generated at 2022-06-13 18:16:12.245303
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    from .pgen2.grammar import Grammar
    from .pgen2.driver import Driver

    g = Grammar("""
    test: NAME
    """)
    d = Driver(g, convert)
    t = d.parse("a", start="test", eof=True)
    t.pretty_print()
    x = Node(g.symbol2number["test"], [], fixers_applied=[])
    assert x.optimize() is x



# Generated at 2022-06-13 18:16:20.472505
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    r"""
    Unit test for method pre_order of class Base
    This tests that pre-order traversal works properly, and also tests
    that the parent links are correct.
    """
    from .pytree import Node
    from .pygram import python_symbols as syms

    # Build tree

# Generated at 2022-06-13 18:16:24.083074
# Unit test for function convert
def test_convert():
    def check(gr):
        assert convert(gr, (0, "0", None, [])) == Leaf(0, "0", None)
        assert (
            convert(gr, (0, "0", None, [Node(0, [Leaf(0, "1", None)])])) == Node(0, [Leaf(0, "1", None)])
        )
        assert convert(gr, (0, "0", None, [Leaf(0, "1", None)])) == Leaf(0, "1", None)

    class Gr(Grammar):

        syms = {0: "a"}

    check(Gr())
    test_convert.__test__ = False  # type: ignore

# Generated at 2022-06-13 18:16:27.123955
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    class TestPattern(BasePattern):
        def match(self, node, results):
            return results is not None
    assert list(TestPattern().generate_matches([None])) == [(1, {})]


# Generated at 2022-06-13 18:16:37.908895
# Unit test for method post_order of class Base
def test_Base_post_order():
    from io import StringIO
    from typing import Iterable, Optional
    import unittest
    from .pytree import Node
    from .pygram import python_symbols

    class Node(Base, Node):
        pass

    class Leaf(Base, Node.Leaf):
        pass

    class TestError(Exception):
        pass

    class Test(unittest.TestCase):
        def test_post_order(self):
            test_cases = [
                ("# Comment\nprint(2)", [2]),
                ("f(1);g(2)", [2]),
                ("f(1)\n", [1, None]),
            ]
            for expr, expected in test_cases:
                expr_tree = compile(expr, "<test>", "exec", flags=0, dont_inherit=True)
                # Test default

# Generated at 2022-06-13 18:17:14.353490
# Unit test for method clone of class Base
def test_Base_clone():
    print("Method clone of class Base")
    # Test Node.__init__
    tree = Node(syms.funcdef, [Token("def", prefix="\n\n"),
                               Leaf(1, "f", [10, 0]),
                               Leaf(40, "(", [10, 3]),
                               Leaf(41, ")", [10, 4]),
                               Leaf(58, ":", [10, 5]),
                               Leaf(1, "pass", [11, 4])])
    clone = tree.clone()
    assert tree == clone
    assert tree is not clone
    assert tree.children[0] is not clone.children[0]
    # Test Leaf.__init__
    tree = Leaf(1, "f", [10, 0])
    clone = tree.clone()
    assert tree == clone

# Generated at 2022-06-13 18:17:24.805839
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    """Unit test for method generate_matches of class BasePattern"""
    import ast
    import sys

    node = Node(256, [ast.parse(sys.modules[__name__].__doc__, mode="exec")])
    assert list(BasePattern(257).generate_matches([node])) == []

    for k in range(1, 5):
        for n in range(k):
            assert list(BasePattern(256, fixers_applied=[None] * k).generate_matches([node])) == [(1, {})]

    for k in range(1, 5):
        for n in range(k):
            if n != 1:
                assert list(BasePattern(256, fixers_applied=[2, None, 3]).generate_matches([node])) == []



# Generated at 2022-06-13 18:17:34.787776
# Unit test for method set_child of class Node
def test_Node_set_child():
    from .pytree import Leaf, Node
    from .pygram import python_symbols
    r = Leaf(1, "c")
    print(r.parent)
    n = Node(python_symbols.power, [Leaf(1, "a"), Leaf(1, "b")])
    id_of_a = id(n.children[0])
    id_of_b = id(n.children[1])
    id_of_r = id(r)

    print(n)
    print(n.children[0])
    print(n.children[0].parent)
    print(n.children[1])
    print(n.children[1].parent)
    n.insert_child(1, r)
    print(n)
    print("replaced")

# Generated at 2022-06-13 18:17:42.512605
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == 1
    import sphinx.util.pycompat as pycompat
    # Use deque to preserve order of locals.
    lcls = pycompat.deque(globals())
    while lcls:
        name, val = lcls.popleft()
        if type(val) == int:
            _type_reprs[val] = name
    assert type_repr(1) == "test_type_repr"



# Generated at 2022-06-13 18:17:54.272774
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    """
    Test method Base.__eq__

    From test/pattern_match.py: test_match_with_items
    """
    from .pygram import python_symbols as syms

    from . import patcomp

    class NodeType(object):
        def __init__(self, string):
            self._string = string

        def __str__(self):
            return self._string

    nt = NodeType

    s = "test string"

    class MockNode(Base):
        def __init__(self, string, type, children=None, parent=None,
            lineno=0, prefix="prefix", parent_context=(),
            implicit=False, node_type=None,
            ):
            self._string = string
            self.type = type
            self.lineno = lineno

# Generated at 2022-06-13 18:18:02.255370
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    import lib2to3.pgen2.parse
    import lib2to3.pygram
    import lib2to3.pgen2.token
    g = lib2to3.pgen2.parse.make_grammar(lib2to3.pygram.python_grammar_no_print_statement)
    grammar_tree = lib2to3.pgen2.parse.parse_grammar(g, lib2to3.pgen2.token)
    assert grammar_tree.get_suffix() == "python_grammar_no_print_statement)"
# End unit test for method get_suffix of class Base

    def get_child_nodes(self) -> Iterator[NL]:
        for child in self.children:
            yield child
            if isinstance(child, Node):
                yield from child.get_child_

# Generated at 2022-06-13 18:18:09.921499
# Unit test for method leaves of class Base
def test_Base_leaves():
    p = Node(3, [Leaf(1, 'foo'), Node(3, [Leaf(1, 'bar'), Leaf(1, 'baz')]), Leaf(1, 'qux')])
    leaves = p.leaves()
    assert len(list(leaves)) == 4
    assert next(leaves) == Leaf(1, 'foo')
    assert next(leaves) == Leaf(1, 'bar')
    assert next(leaves) == Leaf(1, 'baz')
    assert next(leaves) == Leaf(1, 'qux')
    assert next(leaves, None) == None



# Generated at 2022-06-13 18:18:15.119968
# Unit test for method remove of class Base
def test_Base_remove():
    a = Leaf(1, "a")
    b = Leaf(1, "b")

    c = Node(2, [a, b])
    a.parent = c
    b.parent = c

    d = Node(3, [c])
    c.parent = d

    from copy import copy
    c.remove()
    assert copy(d.children) == []
    c.children = [a, b]
    d.children = [c]
    a.remove()
    assert copy(c.children) == [b]
    assert copy(d.children) == [c]
    b.remove()
    assert copy(c.children) == []
    assert copy(d.children) == [c]



# Generated at 2022-06-13 18:18:22.961945
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    # Test case covering more than half of the code branches
    nd0 = Node(0, [Leaf(1, ""), Leaf(2, ""), Leaf(3, "")])

    # Test case covering more than half of the code branches
    nd1 = Node(0, [Leaf(1, ""), Leaf(2, ""), Leaf(3, "")])

    # Test case covering more than half of the code branches
    nd2 = Node(0, [Leaf(1, ""), Leaf(2, ""), Leaf(3, "")])
    assert (nd0 == nd1) == (nd1 == nd2)

# Generated at 2022-06-13 18:18:31.205448
# Unit test for method __repr__ of class Node

# Generated at 2022-06-13 18:19:58.642236
# Unit test for method leaves of class Base
def test_Base_leaves():
    a = Node()
    b = Leaf(1)
    c = Leaf(2)
    a.children = [b, c]
    assert list(a.leaves()) == [b, c]



# Generated at 2022-06-13 18:20:04.916220
# Unit test for function generate_matches
def test_generate_matches():
    node1 = NL([NL(0), NL(1), NL(2)])
    node2 = NL([NL(3), NL(4), NL(5)])
    node3 = NL([NL(6), NL(7), NL(8)])
    p = BasePattern()
    p.generate_matches = lambda nodes: [
        (len(nodes[:i]), {0: nodes[:i]}) for i in range(1, len(nodes) + 1)
    ]
    for nodes in [], [node3], [node2, node3], [node1, node2, node3]:
        for pats in [[p], [p, p], [p, p, p]]:
            for count, results in generate_matches(pats, nodes):
                assert len(nodes[:count]) == count


# Generated at 2022-06-13 18:20:12.468324
# Unit test for method post_order of class Node

# Generated at 2022-06-13 18:20:25.161981
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from .pygram import python_symbols as syms
    from .pytree import Node, Leaf

    l1 = Leaf("a", 1, ("a", (1, 1)))
    l2 = Leaf("b", 1, ("b", (1, 2)))
    l3 = Leaf("c", 1, ("c", (1, 3)))
    l4 = Leaf("d", 1, ("d", (1, 4)))

    nd = Node(syms.file_input, [l1, l2, l3, l4])
    assert nd.pre_order() == [nd, l1, l2, l3, l4]


# Generated at 2022-06-13 18:20:32.489022
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    #pylint: disable=missing-docstring

    import lib2to3.pgen2.parse
    import lib2to3.pgen2.token
    import lib2to3.pytree

    grammar = lib2to3.pgen2.parse.generate_grammar("Grammar.txt")
    tokens = lib2to3.pgen2.tokenize.generate_tokens("for i in range(5): print(i)")

    tree = lib2to3.pytree.convert_tokens_to_tree(tokens, grammar)

    # `tree` is a single node, whose children are the contents of the
    # file.

    children = tree.children
    assert len(children) == 2
    assert children[0].type == grammar.symbol2number['file_input']



# Generated at 2022-06-13 18:20:37.771438
# Unit test for method post_order of class Node
def test_Node_post_order():
    from . import pytree
    from .pygram import python_symbols as syms

    # Tested by unit tests in Lib/test/test_pytree.py
    return

# Generated at 2022-06-13 18:20:39.926431
# Unit test for method post_order of class Node
def test_Node_post_order():
    node = Node(0, [], prefix= '', fixers_applied= [])
    node.post_order()


# Generated at 2022-06-13 18:20:42.001151
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    from .pgen2 import token

    class NodePattern(BasePattern):
        type = token.NAME

    local_object_0 = NodePattern()
    result = repr(local_object_0)
    assert isinstance(result, str)

    # assertEqual(result, "NodePattern(NAME, None, None)")

# Generated at 2022-06-13 18:20:45.438428
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    pattern = NegatedPattern(NodePattern(content=(LeafPattern(),)))
    assert list(pattern.generate_matches([])), list(pattern.generate_matches([Leaf(1)]))



# Generated at 2022-06-13 18:20:46.106291
# Unit test for method post_order of class Node
def test_Node_post_order():
    pass



# Generated at 2022-06-13 18:21:12.232344
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pgen2 import token
    from .pgen2.grammar import Grammar

    gr = Grammar(dedent_dedent_grammar_doc)
    p = LeafPattern(token.NAME)
    for m in p.generate_matches([Leaf(token.NAME, "foo")]):
        assert m == (1, {"NAME": Leaf(token.NAME, "foo")})



# Generated at 2022-06-13 18:21:22.956427
# Unit test for method post_order of class Base
def test_Base_post_order():
    import sys
    import os
    import lib2to3.pygram as pygram
    import lib2to3.pgen2 as pgen2
    old_name = pygram.python_grammar_no_print_statement
    pygram.python_grammar_no_print_statement = 'test_data/python_grammar_no_print_statement'
    base_path = os.path.dirname(__file__)
    python_grammar = os.path.join(base_path, 'test_data',
                                  'python_grammar_no_print_statement')
    with open(python_grammar) as f:
        grammar = pgen2.grammar.Grammar(f.read(), python_grammar)
    g = grammar._parse_grammar()
    pygram.python_grammar_no

# Generated at 2022-06-13 18:21:31.443785
# Unit test for function generate_matches
def test_generate_matches():
    class FakePattern:
        name = None

        def __init__(self, seq):
            self.seq = seq

        def generate_matches(self, tokens):
            seq = self.seq
            assert isinstance(seq, list)
            if not seq:
                yield 0, {"p": self}
            if not tokens:
                return
            if seq[0] == tokens[0]:
                for count, results in self.generate_matches(tokens[1:]):
                    r = {"p": self}
                    r.update(results)
                    yield count + 1, r

    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(generate_matches([], nodes)) == [(0, {})]

# Generated at 2022-06-13 18:21:40.642226
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    
    from .pgen2.tokenize import tokenize, untokenize
    
    # Test for pre-order traversal on a parse tree created for the string 'x+y'
    stmnt = 'x+y'
    # We do not need to create a parse tree for the entire file, so we tokenize
    # the statement and pass the resulting list of (token type, token value,
    # starting line number and column number) tuples to the method from_list,
    # which returns a parse tree
    tree = parser.stmt_list.from_list(tokenize(stmnt))
    # We iterate over the parse tree using the method pre_order, which returns
    # a pre-order iterator for that tree
    iterator = tree.pre_order()
    # We traverse through the iterator to get the contents of the parse tree


# Generated at 2022-06-13 18:21:44.461300
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    class TestPattern(BasePattern):
        def __init__(self):
            self.type = id(self)
        def _submatch(self, node, results=None):
            return True
    tp = TestPattern()
    tp2 = tp.optimize()
    assert tp == tp2, (tp, tp2)



# Generated at 2022-06-13 18:21:59.181155
# Unit test for method get_suffix of class Base

# Generated at 2022-06-13 18:22:10.540441
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    def match(pattern, nodes):
        r = []
        for n, m in pattern.generate_matches(nodes):
            assert n == 1
            r.append(m)
        return r
    
    n1 = Node(1, [Leaf(1, 'a')])
    n2 = Node(1, [Leaf(1, 'b')])
    n3 = Node(1, [Leaf(1, 'a'), Leaf(2, 'c')])
    n4 = Node(1, [Leaf(1, 'b'), Leaf(2, 'd')])
    
    assert match(LeafPattern(1, 'a'), [n1]) == [{}]
    assert match(LeafPattern(1, 'a'), [n2]) == []

# Generated at 2022-06-13 18:22:18.206330
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    n = NodePattern(42)
    assert repr(n) == "NodePattern(42, None, None)"
    l = LeafPattern(42)
    assert repr(l) == "LeafPattern(42, None, None)"
    w = WildcardPattern(42)
    assert repr(w) == "WildcardPattern(42, None, None)"