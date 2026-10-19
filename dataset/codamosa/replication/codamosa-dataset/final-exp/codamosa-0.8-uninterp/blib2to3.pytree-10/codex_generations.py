

# Generated at 2022-06-13 18:14:19.625785
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    import blib2to3.pgen2.tokenize as tokenize
    from io import StringIO
    import blib2to3.pygram as pygram
    import blib2to3.pgen2.parse as parse
    import blib2to3.pgen2.driver as driver
    import blib2to3.pgen2.pgen as pgen
    import blib2to3.pytree as pytree
    import blib2to3.fixer_base as fixer_base
    import blib2to3.fixer_util as fixer_util
    import blib2to3.patcomp as patcomp
    import blib2to3.pgen2.convert as convert
    import unittest
    import sys
    import ast


# Generated at 2022-06-13 18:14:27.129391
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Node, Leaf
    from .pgen2 import token
    from .pgen2.parse import PyParser
    from . import python_grammar
    from .lib2to3 import fixer_base, pytree

    grammar = python_grammar
    grammar_file = grammar.__file__
    parser = PyParser(grammar_file, "exec")
    source = """
a = ['spam', 'ham', 'eggs']
print(a)
"""
    tree = parser.parse(source)
    print(tree.totuple())
    new_tree = tree.clone()
    e = new_tree.next_sibling
    replacement = Leaf(token.NAME, "SPAM", prefix = " ")
    e.replace(replacement)
    print(new_tree.totuple())
   

# Generated at 2022-06-13 18:14:35.452338
# Unit test for method optimize of class WildcardPattern
def test_WildcardPattern_optimize():
    assert WildcardPattern().optimize() == WildcardPattern()
    assert WildcardPattern(min=1).optimize() == WildcardPattern(min=1)
    assert WildcardPattern(max=1).optimize() == WildcardPattern(max=1)
    assert WildcardPattern(min=1).optimize() == NodePattern()
    assert WildcardPattern(min=0, max=1).optimize() == WildcardPattern(min=0, max=1)
    assert WildcardPattern(min=1, max=1).optimize() == NodePattern()
    assert WildcardPattern(content=[[NodePattern(BAR)]]).optimize() == WildcardPattern(
        content=[[NodePattern(BAR)]]
    )

# Generated at 2022-06-13 18:14:41.756953
# Unit test for method post_order of class Base
def test_Base_post_order():
    import unittest
    import sys
    from . import pytree
    from .pygram import python_symbols as symbols
    from . import pygram

    class MockParser(object):
        @staticmethod
        def default_transformer(tree):
            return tree

    symbols_by_name = pygram.python_symbols.__dict__
    symbols_by_number = {v: k for k, v in symbols_by_name.items() if not k.startswith("_")}

    def node(*children):
        return pytree.Node(symbols.funcdef, None, children)

    def l(type, value, context=None):
        return pytree.Leaf(type, value, context)


# Generated at 2022-06-13 18:14:45.042609
# Unit test for method post_order of class Leaf
def test_Leaf_post_order():
    # The method post_order of class Leaf returns a generator.
    # We must use list to get all elements of the generator.
    assert list(p_UnitTest_Leaf_post_order().post_order()) == [p_UnitTest_Leaf_post_order()]


# Generated at 2022-06-13 18:14:57.069082
# Unit test for function generate_matches
def test_generate_matches():
    # This is an odd unit test because it doesn't test anything in this
    # file.  But it is really handy to test this function directly
    # rather than indirectly through the tree templates.
    test_patterns = [NodePattern(1), NodePattern(2), NodePattern(3)]
    test_nodes = [NL(1), NL(2), NL(3)]
    for c, r in generate_matches(test_patterns, test_nodes):
        if not (c == 3 and r == {}):
            raise AssertionError(c, r)
    wp = WildcardPattern()
    test_patterns = [NodePattern(1), wp]
    test_nodes = [NL(1), NL(2), NL(3)]

# Generated at 2022-06-13 18:15:09.633414
# Unit test for method generate_matches of class WildcardPattern

# Generated at 2022-06-13 18:15:19.361205
# Unit test for method replace of class Base
def test_Base_replace():
    from blib2to3.pgen2 import token
    from blib2to3.pgen2.parse import ParseError

    def check(s):
        s = s.strip()
        parse = grammar.parse
        t = parse(s)
        first = t.children[0]
        first.replace(Leaf(token.PLUS, "+"))
        assert str(t) == "(+)"
        second = t.children[0]
        old = first, second
        new = Leaf(token.MINUS, "-")
        second.replace(new)
        assert t.children[0] is new
        assert (first.parent, second.parent) == (None, None)
        t.children[0].replace([Leaf(token.PLUS, "+"), Leaf(token.DOT, ".")])
        assert str

# Generated at 2022-06-13 18:15:20.596423
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(1) == "TEST"



# Generated at 2022-06-13 18:15:30.265489
# Unit test for method post_order of class Node
def test_Node_post_order():
    l1 = Leaf(1, "foo")
    l2 = Leaf(2, "bar")
    l3 = Leaf(3, "baz")
    l4 = Leaf(4, "bax")
    n1 = Node(2, [l1, l2])
    n2 = Node(2, [l3, l4])
    n3 = Node(3, [n1, n2])
    n3_post_order = list(n3.post_order())
    assert len(n3_post_order) == 7, n3_post_order
    assert n3_post_order[0] is n1, n3_post_order
    assert n3_post_order[1] is l1, n3_post_order
    assert n3_post_order[2] is l2, n3_

# Generated at 2022-06-13 18:15:55.824776
# Unit test for method replace of class Base
def test_Base_replace():
    from .pytree import Leaf
    root = Node(syms.file_input, [])
    a = Leaf(1, "a")
    b = Leaf(1, "b")
    c = Leaf(1, "c")
    d = Leaf(1, "d")
    e = Leaf(1, "e")
    f = Leaf(1, "f")
    root.append_child(a)
    root.append_child(b)
    root.append_child(c)
    root.append_child(d)
    root.append_child(e)
    root.append_child(f)
    new = Leaf(2, "NEW")
    root.children[3].replace(new)
    assert root.children == [a, b, c, new, e, f]

# Generated at 2022-06-13 18:16:04.587206
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    import unittest
    import pgen2.token
    # A simple class for testing Base
    class MockNode(Base):
        __slots__ = ('tok', 'tok_val', 'children')

        def __init__(self, tok, tok_val, children=()):
            self.tok = tok
            self.tok_val = tok_val
            self.children = children

        def _eq(self, other):
            return self.tok == other.tok and self.tok_val == other.tok_val

        def __repr__(self):
            return f'<MockNode: {self.tok_val}>'

        def post_order(self):
            for child in self.children:
                yield child
            yield self


# Generated at 2022-06-13 18:16:10.265088
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(python_symbols.testlist) == "testlist"
    assert type_repr(python_symbols.DEDENT) == "DEDENT"
    assert type_repr(9999999) == 9999999
test_type_repr()


# Args for visit()
_NoArg = object()



# Generated at 2022-06-13 18:16:21.710060
# Unit test for method pre_order of class Base
def test_Base_pre_order():

    class _(Base):

        def __init__(self):
            super().__init__()
            self.type = 0
            self.children = [Leaf(0, ""), Leaf(0, "")]

        def _eq(self, other):
            return True

        def clone(self):
            return _()

        def post_order(self):
            return (x for x in [])

        def pre_order(self):
            return (x for x in [self])

        def __repr__(self):
            raise RuntimeError("shouldn't be called")

    assert len(list(_().pre_order())) == 1

    a = _()
    _()
    a.children = [Leaf(0, ""), _()]
    assert len(list(a.pre_order())) == 3


#

# Generated at 2022-06-13 18:16:22.852058
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    l = Leaf(1, "value", prefix="prefix")
    assert list(l.leaves()) == [l]


# Generated at 2022-06-13 18:16:31.453461
# Unit test for method depth of class Base
def test_Base_depth():
    from .pytree import Leaf, Node, convert_tree
    from .pygram import python_symbols as syms
    # This test tries to exercise the function Base.depth
    tree = convert_tree(
        """
        a = (1 + 2 * 3)
        b = a * 4
        c = a + b
        d = b - c
        """
    )
    assert tree.depth() == 0
    assert tree.children[0].depth() == 1
    assert tree.children[1].depth() == 1
    assert tree.children[0].children[0].depth() == 2
    assert tree.children[0].children[1].depth() == 2
    assert tree.children[0].children[2].depth() == 2
    b_node = tree.children[0].children[0]
    b_name = next

# Generated at 2022-06-13 18:16:36.204373
# Unit test for constructor of class NodePattern
def test_NodePattern():
    NodePattern().match(Leaf(1, "*"))
    NodePattern(1).match(Leaf(1, "*"))
    NodePattern(1).match(Node(2, [Leaf(1, "*")]))
    NodePattern(1, ["*"]).match(Node(1, [Leaf(1, "*")]))
    NodePattern(1, []).match(Node(1, []))
    with pytest.raises(AssertionError):
        NodePattern(0)
    with pytest.raises(AssertionError):
        NodePattern(1, [])


# Generated at 2022-06-13 18:16:47.489173
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    ## Unit test for Node.pre_order
    # Node.pre_order should be a generator
    # Node.pre_order should yield each Node exactly once
    # Node.pre_order should yield each Node in depth first order
    import pytree
    import unittest

    def walk_tree(root, iterator):
        yielded_nodes = []
        for node in iterator:
            yielded_nodes.append(node)
            if node.children:
                found = walk_tree(node, iterator)
                if not found:
                    return False
        return root in yielded_nodes


# Generated at 2022-06-13 18:17:00.888191
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    print("test WildcardPattern.generate_matches")
    from .compiler import Pattern
    pattern = Pattern("(a b | c d | e f) x")
    sample = "a b c d x e f x a b x c d e f x".split()
    expected = [(0, []), (3, [("NL0", ["a b x"])]), (3, [("NL0", ["a b c d x"])]),
                (3, [("NL0", ["a b x", "e f x"])]), (7, [("NL0", ["a b c d e f x"])])]
    assert list(generate_matches(pattern.pattern, sample)) == expected


# Generated at 2022-06-13 18:17:05.429133
# Unit test for method leaves of class Base
def test_Base_leaves():
    x = Base()
    x.parent = None
    x.children = []
    assert list(x.leaves()) == []

    y = Base()
    y.parent = x
    y.children = []
    x.children.append(y)
    assert list(x.leaves()) == []

    z = Base()
    z.parent = y
    z.children = []
    y.children.append(z)
    assert list(x.leaves()) == []



# Generated at 2022-06-13 18:17:17.608836
# Unit test for method changed of class Base
def test_Base_changed():
    pass # TODO



# Generated at 2022-06-13 18:17:28.719696
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    n1 = Node(256, [Leaf(1, "foo"), Leaf(2, "="), Leaf(3, "bar"), Leaf(4, "="),
                    Node(257, [Leaf(5, "baz")])])
    n2 = Node(256, [Leaf(1, "foo"), Leaf(2, "="), Leaf(3, "bar"), Leaf(4, "="),
                    Leaf(5, "baz")])
    p = NodePattern(257)
    assert p.match_seq(n1.children)
    assert not p.match_seq(n2.children)
    p = NodePattern(257, content=LeafPattern(5))
    assert p.match_seq(n1.children)
    assert not p.match_seq(n2.children)

# Generated at 2022-06-13 18:17:32.290382
# Unit test for constructor of class LeafPattern
def test_LeafPattern():
    pattern = LeafPattern(token.NAME, "str")
    assert pattern._submatch(Leaf(token.NAME, "str"))
    assert not pattern._submatch(Leaf(token.NAME, "int"))



# Generated at 2022-06-13 18:17:43.579909
# Unit test for method pre_order of class Base

# Generated at 2022-06-13 18:17:55.440226
# Unit test for method post_order of class Node
def test_Node_post_order():
    from .pygram import python_symbols as syms
    from .pytree import Leaf, Node
    from .pgen2.pgen import Grammar
    from .pgen2.token import NUMBER
    import sys
    import unittest
    import unittest.mock
    mock_input = unittest.mock.MagicMock(name='mock_input', return_value='x = 1')
    mock_open = unittest.mock.MagicMock(name='mock_open', return_value=unittest.mock.MagicMock(name='mock_file', read=unittest.mock.MagicMock(name='mock_read', return_value='x = 1')))

# Generated at 2022-06-13 18:17:59.506239
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    '''
    >>> leaf = Leaf(type=10, value='+', context=None, prefix='a')
    >>> leaf.pre_order()
    <generator object pre_order at 0x7fcd3c3a1af8>
    >>> list(leaf.pre_order())
    [Leaf(OP, '+')]
    '''

# Generated at 2022-06-13 18:18:09.796564
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    """
    Test for method get_lineno of class Base.
    """
    # Test 1: If the node has no leaves, it returns None
    node = Base()
    node.children = []
    assert node.get_lineno() == None

    # Test 2: If the node has leaves, it returns the lineno of the first leaf node
    leaf = Leaf(0, None, None, None)
    leaf.lineno = 4
    node.children = [leaf]
    assert node.get_lineno() == 4

    # Test 3: If the node is a leaf node, it returns its lineno
    leaf = Leaf(0, None, None, None)
    leaf.lineno = 7
    assert leaf.get_lineno() == 7

    # Test 4: If the node does not have a lineno, it returns None
    leaf

# Generated at 2022-06-13 18:18:11.857872
# Unit test for method set_child of class Node
def test_Node_set_child():
    o = Node(1, [Leaf(1, ' '), Leaf(2, ' ')])
    newNode = Leaf(2, ' ')
    o.set_child(1, newNode)


# Generated at 2022-06-13 18:18:23.202036
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .grammar import Symbol

    class t(Symbol):
        pass

    class s(Symbol):
        pass

    class X(BasePattern):

        def __init__(self, type, content=None):
            assert content is None
            self.type = type

    assert list(X(t).generate_matches([t()])) == [(1, {})]
    assert list(X(t).generate_matches([t()])) == [(1, {})]
    assert list(X(t).generate_matches([t()])) == [(1, {})]
    assert list(X(s).generate_matches([s()])) == [(1, {})]
    assert list(X(s).generate_matches([s()])) == [(1, {})]

# Generated at 2022-06-13 18:18:25.154764
# Unit test for function type_repr
def test_type_repr():
    # type: () -> None
    assert type_repr(python_symbols.string) == "string"



# Generated at 2022-06-13 18:19:18.260863
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    import lib2to3.pgen2.parse
    import lib2to3.pygram
    import lib2to3.pytree
    import blib2to3.pytree
    #
    # The following tests do not use the function "parse" from module "pytree"
    # because that function relies on the pytree module to have been initialized.
    #
    # Test with a simple node; the next-sibling pointer is None.
    node0 = lib2to3.pytree.Node(
        lib2to3.pygram.python_symbols.simple_stmt,
        [lib2to3.pytree.Leaf(lib2to3.token.NAME, "a")]
    )
    result = node0.get_suffix()
    assert result == ""
    #
    # Test with a simple statement

# Generated at 2022-06-13 18:19:28.401584
# Unit test for function generate_matches
def test_generate_matches():
    a = NodePattern(type=tokenize.NAME)
    b = WildcardPattern()
    c = WildcardPattern(content=((a,),))
    for i, r in generate_matches([a, b, c], [NL(1, 0, "a", "a", 1, "a"), NL(1, 0, "1", "1", 1, "1"), NL(1, 0, "a", "a", 1, "a")]):
        print(i, r)


# Generated at 2022-06-13 18:19:36.163405
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pygram import python_symbols

    def test_case(src, pos, ch):
        grammar = Grammar()
        grammar.parse(src)
        tree = grammar.pgen.ast2tuple(grammar.pgen.parses[0])
        t = tree  # type: Node
        t.changed()
        assert t.changed() is None, t.changed()
        assert t.next_sibling is None, t.next_sibling
        assert t.prev_sibling is None, t.prev_sibling
        assert t.next_sibling_map is None, t.next_sibling_map
        assert t.prev_sibling_map is None, t.prev_sibling_map
        assert t.get_suffix() == ch, t.get_suffix()
        assert t

# Generated at 2022-06-13 18:19:44.859633
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    Node(1, [Leaf(1, 'abc'), Node(1, [Leaf(1, 'def'), Leaf(1, 'ghi')]), Leaf(1, 'jkl')])
    root = Node(1, [Leaf(1, 'abc'), Node(1, [Leaf(1, 'def'), Leaf(1, 'ghi')]), Leaf(1, 'jkl')])
    expected = ['abc', 'def', 'ghi', 'jkl']
    for x, y in zip(root.pre_order(), expected):
        assert str(x) == y

# Generated at 2022-06-13 18:19:55.315360
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    from .pytree import Leaf, Node

    assert Leaf(1, "foo") == Leaf(1, "foo")
    assert Leaf(1, "foo") != Leaf(1, "bar")
    assert Leaf(1, "foo") != Leaf(2, "foo")
    assert Node(2, [Leaf(1, "foo")]) == Node(2, [Leaf(1, "foo")])
    assert Node(2, [Leaf(1, "foo")]) != Node(2, [Leaf(1, "bar")])
    assert Node(2, [Leaf(1, "foo")]) != Node(2, [Leaf(1, "foo"), Leaf(1, "bar")])



# Generated at 2022-06-13 18:19:57.373954
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    assert list(Leaf(1, "a").pre_order()) == [Leaf(1, "a")]


# Generated at 2022-06-13 18:19:58.796008
# Unit test for method depth of class Base
def test_Base_depth():
    assert Base().depth() == 0


# Generated at 2022-06-13 18:19:59.504955
# Unit test for method remove of class Base
def test_Base_remove():
  assert Base().remove() == None
  

# Generated at 2022-06-13 18:20:06.256278
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    from .pytree import Leaf, Node, Internal
    string = "Hello world"
    sub_prefix = " world"
    prefix_len = len(string) - len(sub_prefix)
    l = [Leaf(prefix = string[:prefix_len], type = token.NAME,
                value = string[:prefix_len])]
    r = Leaf(prefix = sub_prefix, type = token.NAME, value = sub_prefix)
    l_node = Internal(children = l)
    l_node.prefix = string
    r_node = Internal(children = [r])
    r_node.prefix = sub_prefix
    l_node.children.append(r_node)
    suffix = l_node.get_suffix()
    assert suffix == sub_prefix
    l_node.children.clear()

# Generated at 2022-06-13 18:20:10.223092
# Unit test for constructor of class NodePattern
def test_NodePattern():
    with pytest.raises(AssertionError):
        # type must be >= 256
        p = NodePattern(type=123)
    with pytest.raises(AssertionError):
        # content must be a sequence of patterns
        p = NodePattern(type=256, content=['a'])
    node_pattern = NodePattern(type=256, content=[LeafPattern(type=1)])



# Generated at 2022-06-13 18:20:34.179476
# Unit test for method clone of class Base
def test_Base_clone():
    try:
        node = Node(0, "")
        node.clone()
    except NotImplementedError:
        pass
    try:
        node = Leaf(0, "", (0, 0))
        node.clone()
    except NotImplementedError:
        pass
    # Test to make sure it doesn't fail without context
    node = Leaf(0, "")
    node.clone()


# Generated at 2022-06-13 18:20:38.720732
# Unit test for method clone of class Leaf
def test_Leaf_clone():
    n = Leaf(1,'hello')
    n.parent = 'something'
    m = n.clone()
    assert n.__eq__(m)
    assert n.value == m.value
    assert n.type == m.type
    assert n.prefix == m.prefix
    assert not n is m

# Generated at 2022-06-13 18:20:49.748289
# Unit test for constructor of class Node
def test_Node():
    from blib2to3.pygram import python_symbols as syms

    def_stmt = Node(syms.simple_stmt, [])
    print(def_stmt)

    def_stmt.append_child(Leaf(1, "def"))
    print(def_stmt)

    def_stmt.append_child(Leaf(1, "foo"))
    print(def_stmt)

    def_stmt.append_child(Leaf(11, ":"))
    print(def_stmt)

    def_stmt.insert_child(3, Leaf(1, "("))
    print(def_stmt)

    def_stmt.insert_child(4, Leaf(1, ")"))
    print(def_stmt)


# Generated at 2022-06-13 18:20:59.159282
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():

    def check(p, expected):
        r = repr(p)
        if r != expected:
            print("Input: %s" % p)
            print("Expected: %s" % expected)
            print("Got: %s" % r)
            assert 0

    from . import parse

    p = parse.NodePattern(parse.Token("NAME"))
    check(p, "NodePattern(NAME, None, None)")

    p = parse.NodePattern(parse.Token("NAME"), "foo")
    check(p, "NodePattern(NAME, 'foo', None)")

    p = parse.NodePattern(parse.Token("NAME"), name="bar")
    check(p, "NodePattern(NAME, None, 'bar')")

    p = parse.NodePattern(parse.Token("NAME"), "foo", "bar")
    check

# Generated at 2022-06-13 18:21:13.977896
# Unit test for function type_repr
def test_type_repr():
    from .pygram import python_symbols
    for name in dir(python_symbols):
        val = getattr(python_symbols, name)
        if type(val) == int:
            assert type_repr(val) == name


# Terminals

# There are also some special nodes that are not actual grammar
# productions, but useful nonetheless.  For example, NAME, NUMBER,
# STRING+COMMENT and ERRORTOKEN are all error productions, with the
# exception that ERRORTOKEN is not produced by the scanner and
# therefore not included in the first sets of any grammar rule.

# New in 2.6: ENDMARKER, ENCODING, N_TOKENS, NT_OFFSET, !!!

# New in 2.7: ASYNC, AWAIT

# New

# Generated at 2022-06-13 18:21:19.429128
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    """
    Unit test for method __repr__ of class BasePattern
    """
    import pytest

    type = -1
    content = -1
    name = -1
    cls = BasePattern
    BP = cls(type, content, name)
    pattern = BP

    with pytest.raises(NotImplementedError) as excinfo:
        repr(pattern)



# Generated at 2022-06-13 18:21:28.527458
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    import lib2to3.pgen2.grammar as grammar
    import lib2to3.pgen2.token as token


# Generated at 2022-06-13 18:21:38.487109
# Unit test for method post_order of class Node
def test_Node_post_order():
  from .pgen2 import token
  new = []
  root = Node(1000, new)
  for i in range(4):
    child = Leaf(token.NAME, "foo" + str(i))
    new.append(child)
    grandchild = Node(1000, [Leaf(token.NAME, "foo" + str(i) + "a")])
    child.append_child(grandchild)
    grandchild = Node(1000, [Leaf(token.NAME, "foo" + str(i) + "b")])
    child.append_child(grandchild)
  names = [x.value for x in root.post_order()]

# Generated at 2022-06-13 18:21:43.680051
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    test_node = Node(python_symbols.file_input, [])
    expected = [test_node]
    assert list(test_node.pre_order()) == expected
    test_node.children = [Node(python_symbols.simple_stmt, [])]
    expected.extend(test_node.children)
    assert list(test_node.pre_order()) == expected


# Generated at 2022-06-13 18:21:58.506823
# Unit test for function generate_matches
def test_generate_matches():
    # The following code should be indented within a function.
    lines = [
        ". ",
        "    match_results = []",
        "    for count, results in ",
        "        generate_matches([Num(123), Any()], [Node(1), Node(2), Node(3)]):",
        "        match_results.append((count, results))",
        "    assert match_results == [(1, {}), (2, {}), (3, {})]"
    ]
    for line in lines:
        print(line)
    match_results = []
    for count, results in generate_matches([Num(123), Any()], [Node(1), Node(2), Node(3)]):
        match_results.append((count, results))

# Generated at 2022-06-13 18:22:22.849833
# Unit test for method post_order of class Node
def test_Node_post_order():
    from .pygram import python_symbols
    from .pytree import Leaf, Node

    expr_stmt = Node(
        python_symbols.expr_stmt,
        [
            Leaf(1, "x"),
            Leaf(2, "="),
            Leaf(3, "1"),
        ],
    )
    test_stmt = Node(
        python_symbols.simple_stmt,
        [
            expr_stmt,
            Leaf(4, ""),
            Leaf(5, "\n"),
        ]
    )
    x = test_stmt.post_order()
    assert next(x) is expr_stmt
    assert next(x) is expr_stmt.children[0]
    assert next(x) is expr_stmt.children[1]