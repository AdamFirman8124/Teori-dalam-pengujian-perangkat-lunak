

# Generated at 2022-06-13 18:14:32.458078
# Unit test for method post_order of class Base
def test_Base_post_order():
    import lib2to3.pgen2.driver
    p = lib2to3.pgen2.driver.load_grammar(Grammar())
    n = p.parse(
        """while 1:
    continue
"""
    )
    most_basic_test(n)



# Generated at 2022-06-13 18:14:38.692627
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    nodes = [
        Symbol(2, 3, 4, 5, 6),
        Symbol(2, 3, 4, 5, 6),
        Symbol(2, 3, 4, 5, 6),
        Symbol(2, 3, 4, 5, 6),
        Symbol(2, 3, 4, 5, 6),
    ]
    for content in None, NodePattern(4, [WildcardPattern()]), NodePattern(4):
        pattern = NegatedPattern(content)
        print(pattern)
        for c, r in pattern.generate_matches(nodes):
            print(c, r)

# ---------- Helper functions ----------

# Generated at 2022-06-13 18:14:47.873759
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    import sys
    import io
    import os.path
    import tempfile
    try:

        import ast
        import tokenize
    except ImportError:
        print('Test requires ast and tokenize')
        return

    src = 'def f():\n  pass\n'

    # create input file
    with tempfile.TemporaryDirectory() as d:
        fn = os.path.join(d, 'tmp_src')
        with open(fn, 'w') as f:
            f.write(src)

        # tokenize
        with open(fn, 'r') as f:
            toks = tuple(tokenize.generate_tokens(f.readline))

        # build AST
        tree = ast.parse(src)
        mod = Node(python_symbols.file_input, [], None)


# Generated at 2022-06-13 18:14:54.749037
# Unit test for method post_order of class Node
def test_Node_post_order():
    import pytree
    l1 = pytree.Leaf(1, "a")
    l2 = pytree.Leaf(1, "b")
    l3 = pytree.Leaf(1, "c")
    l4 = pytree.Leaf(1, "d")
    l5 = pytree.Leaf(1, "e")
    l6 = pytree.Leaf(1, "f")
    l7 = pytree.Leaf(1, "g")
    l8 = pytree.Leaf(1, "h")
    l9 = pytree.Leaf(1, "i")
    l10 = pytree.Leaf(1, "j")
    l11 = pytree.Leaf(1, "k")
    n1 = pytree.Node(2, [l1, l2])

# Generated at 2022-06-13 18:14:59.558323
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    x = Leaf(1, "hello")
    assert list(x.post_order()) == [x]

test_Leaf_post_order()

# Generated at 2022-06-13 18:15:10.514188
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf
    from .pygram import python_grammar

    tree = python_grammar.parsed("x = 1")
    tree.replace(Leaf(1, "y"))
    assert str(tree) == "y = 1"
    tree = python_grammar.parsed("x = 1")
    tree.children[-1].replace(Leaf(1, "y"))
    assert str(tree) == "x = y"
    tree = python_grammar.parsed("x = 1")
    tree.children[-1].replace([Leaf(1, "y"), Leaf(1, "z")])
    assert str(tree) == "x = yz"
    tree = python_grammar.parsed("x = 1")

# Generated at 2022-06-13 18:15:15.303182
# Unit test for function generate_matches
def test_generate_matches():
    class TestPattern(NodePattern):
        def __init__(self, type, content=None) -> None:
            NodePattern.__init__(self, type, content)

        def generate_matches(self, nodes):
            i = 0
            for n in nodes:
                if n.type == self.type:
                    r = {}
                    if self.name:
                        r[self.name] = n
                    yield i + 1, r
                i += 1

    # Tuple of (count, results)
    assert list(generate_matches([], [])) == [(0, {})]
    assert list(generate_matches([TestPattern(1)], [])) == []
    assert list(generate_matches([TestPattern(1)], [NL(1, None)])) == [(1, {})]

# Generated at 2022-06-13 18:15:31.045717
# Unit test for method leaves of class Base
def test_Base_leaves():
    class Mock(Base):
        children = []

        def __init__(self, children):
            self.children = children

        def post_order(self):
            for child in self.children:
                yield from child.post_order()
            yield self

        def pre_order(self):
            yield self
            for child in self.children:
                yield from child.pre_order()

        def _eq(self, other):
            return self.children == other.children

        def clone(self):
            return self

        @property
        def prefix(self):
            return ""

    class Mock2(Mock):
        pass  # Some nodes don't need __init__

    class MockLeaf(Base):
        def post_order(self):
            yield self

        def pre_order(self):
            yield self


# Generated at 2022-06-13 18:15:35.674582
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    nl = Leaf(2, "2", (None, (None, None)), None)
    assert list(nl.leaves()) == [Leaf(2, "2", (None, (None, None)), None)]

# Generated at 2022-06-13 18:15:39.384361
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    node = Leaf(1, 'a')
    it = node.post_order()
    for el in it:
        print(el, end='')

test_Leaf_post_order()


# Generated at 2022-06-13 18:15:58.775192
# Unit test for method post_order of class Base
def test_Base_post_order():
    from . import pytree
    root = pytree.Node(type = 1,
                       children = [pytree.Leaf(type = 2, value = "a"),
                                   pytree.Node(type = 3,
                                               children = [pytree.Leaf(type = 4, value = "b"),
                                                           pytree.Leaf(type = 5, value = "c"),
                                                           pytree.Leaf(type = 6, value = "d")]),
                                   pytree.Leaf(type = 7, value = "e")])
    root.changed()
    po_list = list(root.post_order())
    #    print("po_list=%r" % po_list)

# Generated at 2022-06-13 18:16:05.426283
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    bp = BasePattern()

    class N(Node):

        """This is used to test that match_seq doesn't choke on other types."""

        def match_seq(self, nodes, results=None):
            return True

    assert bp.match_seq([]) == False  # #54
    assert bp.match_seq([Leaf(1, "")]) == False
    assert bp.match_seq([Leaf(1, ""), Leaf(1, "2")]) == False  # #54
    assert bp.match_seq([N(1, [])]) == False
    assert bp.match_seq([N(1, []), N(1, [])]) == False  # #54



# Generated at 2022-06-13 18:16:10.716354
# Unit test for method post_order of class Base
def test_Base_post_order():
    from .pytree import Node, Leaf

    tree = Node(None, [Leaf(1), Node(2, [Leaf(3)])])
    res = [x.type for x in tree.post_order()]
    assert res == [3, 2, 1], res



# Generated at 2022-06-13 18:16:18.057514
# Unit test for method post_order of class Base
def test_Base_post_order():
    """Unit test for method Base.post_order"""

    class BasePlus(Base):
        def __init__(self, type, parent, children=None):
            self.type = type  # int: token number (< 256) or symbol number (>= 256)
            self.parent = parent  # Parent node pointer, or None
            self.children = children  # List of subnodes
        def _eq(self, other):
            return self.type == other.type and self.children == other.children
        def clone(self):
            return BasePlus(self.type, self.parent, self.children)
        def post_order(self):
            for child in self.children or []:
                assert child is not self  # sanity check
                for node in child.post_order():
                    yield node
            yield self

# Generated at 2022-06-13 18:16:26.802471
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    from .pattern_grammar import pattern

    def _gen_matches(pattern, nodes):
        pat = pattern.parse(Text(pattern))
        for c, r in pat.generate_matches(nodes):
            yield c, r

    # Unit tests for method generate_matches of class NegatedPattern
    nodes = [
        NodePattern(value=1),
        NodePattern(value=2),
        NodePattern(value=3),
        NodePattern(value=4),
        NodePattern(value=5),
    ]
    assert list(_gen_matches(r"\A", [])) == [(0, {})]
    assert list(_gen_matches(r"\A", nodes)) == []
    assert list(_gen_matches(r"\A . . . . . \z", nodes)) == []
    assert list

# Generated at 2022-06-13 18:16:33.997026
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    assert repr(LeafPattern(1)) == 'LeafPattern(NUMBER)'
    assert repr(LeafPattern(1, "0")) == 'LeafPattern(NUMBER, \'0\')'
    assert repr(LeafPattern(2, content=Wildcard("stuff"))) == 'LeafPattern(NAME, content=Wildcard(...))'
    assert repr(LeafPattern(1, "0", "number")) == 'LeafPattern(NUMBER, \'0\', \'number\')'
    assert repr(NodePattern(256, "yada")) == 'NodePattern(yada)'
    assert repr(NodePattern(257)) == 'NodePattern(file_input)'
    assert repr(NodePattern(257, "yada")) == 'NodePattern(file_input, \'yada\')'

# Generated at 2022-06-13 18:16:37.259155
# Unit test for method post_order of class Node
def test_Node_post_order():
    grammar = Grammar(StringIO("""
        start:
            print(3)
    """))
    node = grammar.start
    assert node.post_order()


# Generated at 2022-06-13 18:16:44.256840
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from .pytree import Node, Leaf
    from .pygram import python_symbols as syms

    # Partially defined the grammar, since we are not concerned with the if
    # statement itself, only the stuff in the body of the if.
    #
    # Test equal number of children
    #
    # >>> simple_if_stmt = Node(syms.simple_stmt,
    # ...                       [Node(syms.small_stmt,
    # ...                             [Node(syms.expr_stmt,
    # ...                                   [Node(syms.testlist,
    # ...                                         [Node(syms.test,
    # ...                                               [Leaf(1, 'if'),
    # ...                                                Node(syms.or_test,
    # ...                                                     [Node(syms.

# Generated at 2022-06-13 18:16:47.786448
# Unit test for method remove of class Base
def test_Base_remove():
    child = Leaf("", "", "", "", "", 0)
    parent = Node("", [child], None, None, None, None)
    child.parent = parent
    assert child._Base__remove() == 0
    assert parent.children == []


# Generated at 2022-06-13 18:16:54.456139
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    class TestPattern(BasePattern):
        type = 51
        content = "ab"
        name = "A"

    p1 = TestPattern()
    p2 = TestPattern()
    assert p1.optimize() is p1
    assert p1.optimize() is p2.optimize()



# Generated at 2022-06-13 18:17:14.354609
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    import os
    from .pytree import PythonParser
    from .pgen2 import grammar

    dirname = os.path.dirname
    filename = os.path.join(dirname(dirname(__file__)), "test", "input", "Grammar.txt")
    with open(filename, "rt", encoding="utf8") as f:
        text = f.read()

    parser = PythonParser()
    tree = parser.parse(text, debug=False, start="file_input")
    assert tree.type == grammar.syms.file_input
    assert len(tree.children) > 3
    first = tree.children[0]
    assert first.type == grammar.syms.NEWLINE
    assert len(first.children) == 1
    first = tree.children[1]
    assert first.type == grammar.t

# Generated at 2022-06-13 18:17:23.306146
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    p = NodePattern(1, None)
    assert repr(p) == "NodePattern(\"'NAME'\", None)"
    #
    p = LeafPattern(2, "\n", None)
    assert repr(p) == "LeafPattern(\"'NEWLINE'\", '\\n', None)"
    #
    p = NodePattern(1, None, "x")
    assert repr(p) == "NodePattern(\"'NAME'\", None, 'x')"
    #
    p = LeafPattern(2, "\n", None, "y")
    assert repr(p) == "LeafPattern(\"'NEWLINE'\", '\\n', None, 'y')"

# Generated at 2022-06-13 18:17:29.000793
# Unit test for method leaves of class Base
def test_Base_leaves():
    import StringIO
    import sys
    import unittest

    class Class(unittest.TestCase):
        def test_method(self):
            s = StringIO.StringIO()
            saved = sys.stdout
            try:
                sys.stdout = s
                n = Module((1, 2))
                n.remove()
                n.type = "ab"
                print(n)
                self.assertEqual(s.getvalue(), "Node(ab, None, None)\n")
            finally:
                sys.stdout = saved

    t = Class()
    t.test_method()

# Generated at 2022-06-13 18:17:33.579268
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    from . import VBAR, DEDENT, INDENT, DEDENTS

    def p(pattern, seq, expected_count_results):
        count_results = []
        for c, r in pattern.generate_matches(seq):
            count_results.append((c, r))
        assert_equal(count_results, expected_count_results)

    # Test recursive wildcards
    p(WildcardPattern(), [], [(0, {})])
    p(WildcardPattern(min=1), [], [])

    #             0 1 2 3 4 5
    # Expected:  [a,b,c,d,e,f]
    p(WildcardPattern(), [], [(0, {})])
    p(WildcardPattern(min=1), [], [])

    #             0 1 2 3 4 5
    #

# Generated at 2022-06-13 18:17:44.896626
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Node, Leaf
    from . import python_symbols
    import textwrap

    code = textwrap.dedent("""\
        for x in y:
            print(x)
        """)

    tree = compile(code, "", "exec", _ast.PyCF_ONLY_AST)

    # Get the FOR node.
    for_node = tree.body[0]
    assert for_node.depth() == 1

    # Get the body (SUITE) node.
    suite_node = tree.body[0].body
    assert suite_node.depth() == 2

    # Get the PRINT node.
    print_node = tree.body[0].body.body[0]
    assert print_node.depth() == 3

    # Get the x node (the name in the print statement).
   

# Generated at 2022-06-13 18:17:56.654723
# Unit test for function generate_matches
def test_generate_matches():
    from . import parse
    from . import tree

    # Test an empty pattern
    assert list(generate_matches([], [])) == [(0, {})]
    assert list(generate_matches([], [NL("(", "("), NL("1", "1"), NL(")", ")")])) == [
        (0, {})
    ]

    # Test a non-empty pattern
    ast = parse.parse("(1 (2 3) 4)", mode="eval")
    assert list(generate_matches([NodePattern()], ast.children)) == [(3, {})]
    assert list(generate_matches([NodePattern()], ast[1][1].children)) == [(1, {})]

    # Test a pattern that fails
    ast = parse.parse("(1 (2 3) 4)", mode="eval")
   

# Generated at 2022-06-13 18:18:02.265070
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    """Unit test for method optimize of class BasePattern"""
    t = Token("NAME", "test")
    tp = t.optimize()
    assert tp is t
    n = Node("file_input", [t])
    np = n.optimize()
    assert np is n
    p = BasePattern()
    pp = p.optimize()
    assert pp is p

# Generated at 2022-06-13 18:18:07.229430
# Unit test for method __repr__ of class Node
def test_Node___repr__():
    class DummyGrammar(object):
        def __init__(self):
            self.symbol2number = {'dummy': 666}
    node = Node(666, [])
    node.grammar = DummyGrammar()
    assert repr(node) == "Node(dummy, [])"

# Generated at 2022-06-13 18:18:11.915976
# Unit test for method set_child of class Node
def test_Node_set_child():
    import tokenize
    from .tree import Node, Leaf
    obj = Node(1, [Leaf(3, ""), Leaf(3, "")])
    obj.set_child(1, Leaf(3, "test"))
    assert obj.children == [Leaf(3, ""), Leaf(3, "test")]


# Generated at 2022-06-13 18:18:14.802346
# Unit test for method leaves of class Base
def test_Base_leaves():
    Grammar()
    g = Grammar()
    s = StringIO()
    g.dump_grammar(s)
    g.parse_string(s.getvalue())
    tree = g.tree
    for _ in tree.leaves():
        assert(True)

# Generated at 2022-06-13 18:18:34.615187
# Unit test for method remove of class Base
def test_Base_remove():
    from .pytree import Leaf, Node
    x = Node(2, None, [Leaf(1, ""), Leaf(1, "")])
    assert x.children[1].remove() == 1
    assert len(x.children) == 1

# Generated at 2022-06-13 18:18:39.845182
# Unit test for constructor of class NodePattern
def test_NodePattern():
    from .pgen2.grammar import SymbolDef
    from .pattern_lib import NAME, NUMBER

    for t in range(256):
        assert NodePattern(type=t)
    for t in range(256, 264):
        assert NodePattern(type=t)
    for t in [None, NUMBER]:
        assert NodePattern(type=t)
    for t in [SymbolDef(None), NUMBER]:
        assert NodePattern(type=t).type == NUMBER.type
    for t in [0, NAME]:
        assert NodePattern(type=t)
    for t in [None, NUMBER]:
        assert len(NodePattern(type=t).content) == 0
    for t in [None, NUMBER]:
        assert NodePattern(type=t, content=())

# Generated at 2022-06-13 18:18:46.084837
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    x = BasePattern._BasePattern__new__(BasePattern)
    x._BasePattern__init__(LeafPattern)
    x._BasePattern__init__(NodePattern)
    x._BasePattern__init__(WildcardPattern)
# unit tests for module ast27

# Generated at 2022-06-13 18:18:56.229001
# Unit test for method clone of class Base
def test_Base_clone():
    import unittest

    class Derived(Base):
        """A class that can be instantiated."""

        def __init__(self):
            pass

        def _eq(self, other):
            return True

        def clone(self):
            return Derived()

        def post_order(self):
            return []

        def pre_order(self):
            return []

    class TestBase(unittest.TestCase):
        def setUp(self):
            self.derived = Derived()

        def test_eq(self):
            self.assertEqual(self.derived.__eq__(Derived()), True)

        def test_clone(self):
            cloned = self.derived.clone()
            self.assertEqual(self.derived, cloned)

    unittest.main()


# Unit test

# Generated at 2022-06-13 18:19:02.633501
# Unit test for method leaves of class Base
def test_Base_leaves():
    from blib2to3.pgen2 import token
    from .pytree import Leaf
    x = Leaf("abc", 1, parent="parent")
    y = Leaf("def", 2, parent="parent")
    z = Leaf("ghi", 3, parent="parent")
    tree = Base(token.NEWLINE, [x, y, z], "newline")
    assert list(tree.leaves()) == [x, y, z]



# Generated at 2022-06-13 18:19:05.626187
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    _t = Leaf(3, "3", None, None, None)
    if (_t.pre_order()):
        next(iter(_t.pre_order()))

# Generated at 2022-06-13 18:19:14.064093
# Unit test for function generate_matches
def test_generate_matches():
    from . import ast3 as ast  # type: ignore
    from .pytree import Leaf, Node

    # Test the case with no patterns
    assert tuple(generate_matches([], [Leaf(1, "a"), Leaf(2, "b"), Leaf(3, "c")])) == (
        (0, {}),
    )

    # Test the case with a single pattern
    assert tuple(
        generate_matches(
            [WildcardPattern(None, name="a")],
            [Leaf(1, "a"), Leaf(2, "b"), Leaf(3, "c")],
        )
    ) == ((3, {"a": [Leaf(1, "a"), Leaf(2, "b"), Leaf(3, "c")]}),)

    # Test the case with a single NodePattern

# Generated at 2022-06-13 18:19:15.984733
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.power) == 'power'
    assert type_repr(python_symbols.atom) == 'atom'



# Generated at 2022-06-13 18:19:18.273320
# Unit test for method remove of class Base
def test_Base_remove():
    root = Node(type=0)
    leaf = Leaf(type=0, value='')
    root.append_child(leaf)
    assert next(iter(root.children)).remove() == 0
    assert leaf.parent is None



# Generated at 2022-06-13 18:19:24.085035
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    from . import tokenize

    def f(source):
        t = tokenize.generate_tokens(StringIO(source).readline)
        return [x[1] for x in t]

    def g(source, min=0, max=HUGE):
        sp = WildcardPattern(content=f(source), min=min, max=max)
        for c, r in sp.generate_matches(f("0 1 2 3")):
            print(c, r)

    print("g('1')")
    g("1")
    print("g('1 2')")
    g("1 2")
    print("g('1 2', min=1)")
    g("1 2", min=1)
    print("g('1 2 3', max=2)")

# Generated at 2022-06-13 18:19:40.667206
# Unit test for method post_order of class Node
def test_Node_post_order():
    nl = Node(256, [Leaf(1, "a"), Leaf(1, "b")])
    assert list(nl.post_order()) == [Leaf(1, "a"), Leaf(1, "b"), Node(256, [Leaf(1, "a"), Leaf(1, "b")])]
    nl = Node(256, [Leaf(1, "a")])
    assert list(nl.post_order()) == [Leaf(1, "a"), Node(256, [Leaf(1, "a")])]
test_Node_post_order()


# Generated at 2022-06-13 18:19:45.221165
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Leaf, Node
    n = Node(1, [Leaf(2, "a"), Leaf(2, "b"), Leaf(2, "c")])
    assert [x.value for x in n.leaves()] == ["a", "b", "c"]

# Generated at 2022-06-13 18:19:56.639948
# Unit test for method update_sibling_maps of class Node
def test_Node_update_sibling_maps():
    import copy
    a, b, c, d, e, f, g, h, i  = [Node(x, []) for x in xrange(1,10)]
    a.children = [b, c, d, e, f, g, h, i]
    d.children = [h]
    b.children = [c, d]
    h.children = [i]
    a.update_sibling_maps()
    assert a.next_sibling_map[id(e)] is f and a.next_sibling_map[id(f)] is g and a.next_sibling_map[id(g)] is None

# Generated at 2022-06-13 18:19:57.499218
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(0) == 0



# Generated at 2022-06-13 18:20:04.712797
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    # Test class: Base
    # Method: pre_order
    # Tests for:
    # pre_order
    # Test for:
    # pre_order
    # Base pre_order
    # Leaf pre_order
    # Node pre_order
    node = Node(1, [Leaf(1, "foo"), Leaf(1, "bar"), Node(1, [Leaf(1, "baz")])])

# Generated at 2022-06-13 18:20:08.416158
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    assert BasePattern().match_seq([]) == False


# Generated at 2022-06-13 18:20:21.887032
# Unit test for method update_sibling_maps of class Node
def test_Node_update_sibling_maps():
    import copy
    import os
    import tempfile
    from .pgen2 import tokenize
    from .pygram import python_symbols
    from .pytree import Leaf, Node
    
    tmp = tempfile.mktemp()
    f = open(tmp, 'w')
    f.write('x = 1\n')
    f.close()
    
    # First we need to test that the method actually works.
    f = open(tmp, 'r')
    tokens = tokenize.generate_tokens(f.readline)
    tree = python_grammar.parse(tokens)
    
    assert tree.next_sibling is None
    assert tree.prev_sibling is None
    
    assert tree.children[0].next_sibling is None
    assert tree.children[0].prev_s

# Generated at 2022-06-13 18:20:25.756141
# Unit test for method set_child of class Node
def test_Node_set_child():

    from .pygram import python_symbols

    a = Node(python_symbols.file_input, [])
    b = Leaf(0)
    a.set_child(0, b)
    assert b.parent == a
    a.set_child(0, Leaf(2))
    assert b.parent == None
test_Node_set_child()

# Generated at 2022-06-13 18:20:29.609290
# Unit test for method set_child of class Node
def test_Node_set_child():
    from . import pytree as p
    t = p.Node(type=0, children=[p.TypeIgnore()])
    t.set_child(0, p.TypeIgnore())
    return t

# Generated at 2022-06-13 18:20:41.546568
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    assert WildcardPattern(min=0, max=1).optimize() is WildcardPattern(min=0, max=1)
    assert WildcardPattern(min=1, max=1).optimize() is WildcardPattern(min=1, max=1)
    assert WildcardPattern(min=1, max=1).optimize() is NodePattern()
    # The below optimization is not safe with double underscore methods,
    # because those might appear in the expression itself, and then the implicitly
    # generated names would collide with the method names.
    assert (
        WildcardPattern(content=[["spam"]], min=0, max=1).optimize()
        is WildcardPattern(content=[["spam"]], min=0, max=1)
    )

# Generated at 2022-06-13 18:20:59.282555
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    np=NegatedPattern()
    assert np.match_seq([])
    assert np.match_seq([])
    np=NegatedPattern(NodePattern(type=token.NAME, name="bare_name"))
    assert not np.match_seq([])
    assert not np.match_seq([Leaf(token.NAME, "x")])
    assert np.match_seq([Leaf(token.NAME, "x"), Leaf(token.NAME, "x")])
    assert np.match_seq([Leaf(token.NAME, "x"), Leaf(token.NAME, "y")])



# Generated at 2022-06-13 18:21:00.920265
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    print(Base)



# Generated at 2022-06-13 18:21:04.935706
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    def test_Leaf_pre_order():
        single_leaf = Leaf(257, '1234')
        assert [single_leaf] == list(single_leaf.pre_order())

# Generated at 2022-06-13 18:21:08.330868
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    assert(Leaf(1, "1").pre_order() == iter([Leaf(1, "1")]))

# Generated at 2022-06-13 18:21:13.617499
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.testlist) == "testlist"
    assert type_repr(python_symbols.NAME) == "NAME"
    assert type_repr(python_symbols.NUMBER) == "NUMBER"
    assert type_repr(0) == 0


# Generated at 2022-06-13 18:21:16.228457
# Unit test for method replace of class Base
def test_Base_replace():
    n = Leaf(0, "")
    n.parent = n
    n.replace(None)
    assert n.parent is None


# Generated at 2022-06-13 18:21:27.153848
# Unit test for method generate_matches of class NegatedPattern

# Generated at 2022-06-13 18:21:34.548022
# Unit test for method depth of class Base
def test_Base_depth():
    foo = Leaf(123, "foo")
    assert foo.depth() == 0
    bar = Leaf(123, "bar")
    baz = Leaf(123, "baz")
    bam = Node(123, [foo, bar, baz])
    assert foo.depth() == 1
    assert bar.depth() == 1
    assert baz.depth() == 1
    assert bam.depth() == 0
    foo.parent = bam
    bar.parent = bam
    baz.parent = bam
    assert foo.depth() == 1
    assert bar.depth() == 1
    assert baz.depth() == 1
    assert bam.depth() == 0



# Generated at 2022-06-13 18:21:40.289074
# Unit test for method remove of class Base
def test_Base_remove():
    node_to_remove = Node(1, [Leaf(2, u"test"), Leaf(3, u"test2")])
    parent = Node(4,[node_to_remove])
    node_to_remove.parent = parent
    node_to_remove.remove()
    assert node_to_remove.parent is None
    assert parent.children == []


# Generated at 2022-06-13 18:21:52.520885
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == 1
    for i in range(256):
        assert type_repr(i) != i

# A regular expression used to find bracketing pairs of opcodes.
# Note:  the match won't be right if the code contains strings with
# the same contents as one of these opcode names.
BRACK_RE = """
(?P<LBRACE>{)
|(?P<RBRACE>})
|(?P<LPAREN>\()
|(?P<RPAREN>\))
|(?P<LSQB>[)
|(?P<RSQB>]}
|(?P<COLON>:)
"""

# An augmented version of the above for use in finding unmatched
# brackets.  Of course, this does not solve all possible problems
# (e.g.

# Generated at 2022-06-13 18:22:10.077759
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    def _mock_getattr(attr):
        if attr == '__class__':
            return lambda: Base
        if attr == '_eq':
            return lambda: Base._eq
        if attr == '_eq':
            return lambda: Base._eq
    Base.__getattr__ = _mock_getattr
    Base.__class__ = lambda: Base
    Base.__name__ = 'Base'

    # Call the method (used in other test cases)
    r = Base.__eq__(Base)
    assert r == NotImplemented
Base.__eq__._required_methods = ['_eq']


# Generated at 2022-06-13 18:22:23.085247
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    from .parser import PythonParser

    pattern = PythonParser.compile(r"[a-f]*")
    assert isinstance(pattern, WildcardPattern)
    assert pattern.min == 0
    assert pattern.max == HUGE
    assert isinstance(pattern.content[0][0], DotRange)
    pattern = pattern.optimize()
    assert isinstance(pattern, DotRange)
    assert pattern.name == "bare_name"
    pattern = PythonParser.compile(r"a*")
    assert isinstance(pattern, WildcardPattern)
    pattern = pattern.optimize()
    assert pattern == NodePattern(name="Literal")
    pattern = PythonParser.compile(r"a+")
    assert isinstance(pattern, WildcardPattern)
    pattern = pattern.optimize()
    assert isinstance(pattern, NodePattern)