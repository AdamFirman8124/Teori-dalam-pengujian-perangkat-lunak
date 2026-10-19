

# Generated at 2022-06-13 18:14:45.659727
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    # This is a test for the BasePattern method match_seq.
    # The method match_seq is effectively a specialized version of the
    # method match, with a hard-coded value of 1 for the length of the
    # sequence.  The value 1 is appropriate for non-wildcard patterns.
    # The test is to make sure that the methods match and match_seq
    # agree with each other for all patterns that are not wildcard
    # patterns.  The method ensure_match_seq in the NodePattern class
    # is used to verify this requirement during testing.
    pass


# Generated at 2022-06-13 18:14:53.910945
# Unit test for method leaves of class Base
def test_Base_leaves():
  from .pytree import Node, Leaf
  n = Node(None, [Leaf(0,"0"), Node(None, [Leaf(1,"1"), Leaf(2,"2")]), Leaf(3,"3")])
  i = n.leaves()
  assert next(i).value == "0"
  assert next(i).value == "1"
  assert next(i).value == "2"
  assert next(i).value == "3"


# Generated at 2022-06-13 18:15:08.733572
# Unit test for method post_order of class Base
def test_Base_post_order():
    import _ast
    import blib2to3.pytree as pytree
    a = pytree.Node(1, [
        pytree.Leaf(1, "foo"),
        pytree.Node(2, [
            pytree.Leaf(1, "bar"),
            pytree.Leaf(2, "biz"),
            pytree.Leaf(3, "baz"),
            ]),
        ])
    b = pytree.Leaf(1, "huzzah")
    # test_Base_post_order.test:
    assert [x.type for x in a.post_order()] == [1, 1, 2, 1, 2, 3]
    assert [x.type for x in b.post_order()] == [1]

# Generated at 2022-06-13 18:15:14.156496
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    a = BasePattern()
    print(a)


# class LeafPattern(BasePattern):
#     """
#     A pattern that matches a leaf node.
#     """
#
#     def _submatch(self, node: NL, results: Optional[_Results] = None) -> bool:
#         return self.content.match(node.value, results)


# Generated at 2022-06-13 18:15:23.755537
# Unit test for method depth of class Base
def test_Base_depth():
    assert Base().depth() == 0
    assert Base(parent=Leaf(1, "")).depth() == 1
    assert Leaf(1, "").depth() == 0
    assert Node(1, None, [Leaf(1, "")]).depth() == 0
    assert Node(1, None, [Node(1, None, [Leaf(1, "")])]).depth() == 1



# Generated at 2022-06-13 18:15:26.653919
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    # Add unit tests for Base.pre_order
    raise AssertionError


# Generated at 2022-06-13 18:15:34.217821
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    from .lib2to3 import pytree
    from .pgen2.grammar import Grammar
    from .pgen2.parse import ParseError
    from .pgen2.pgen import generate_grammar
    grammar = Grammar(
        """
        atom:
            | NAME
            | NUMBER
            | '(' yield_expr ')'
            | '[' listmaker ']'
            ;
        test:
            atom
            | test '+' test
            | test '**' test
            | test '-' test
            | test '*' test
            | test '/' test
            | test '%' test
            | test '//' test
            ;
        """,
        generate_grammar=generate_grammar,
    )


# Generated at 2022-06-13 18:15:38.802967
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    sp1 = NodePattern(content=[Leaf(value='a')], name='sp1')
    sp2 = NodePattern(content=[Leaf(value='b')], name='sp2')
    sp3 = NodePattern(content=[Leaf(value='c')], name='sp3')
    sp4 = NodePattern(
        type=40,
        content=[Leaf(value='d'), Leaf(value='e')],
        name='sp4')
    sp5 = NodePattern(content=[Leaf(value='f')], name='sp5')
    sp6 = NodePattern(content=[Leaf(value='e')], name='sp6')
    sp7 = NodePattern(content=[Leaf(value='e')], name='sp7')
    sp8 = NodePattern(content=[Leaf(value='g')], name='sp8')

# Generated at 2022-06-13 18:15:42.645326
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    s = BasePattern(type=2, content=None, name=None)
    assert repr(s) == "BasePattern(2, None, None)"
    s = BasePattern(type=3, content=6, name=None)
    assert repr(s) == "BasePattern(3, 6, None)"
    s = BasePattern(type=5, content=None, name=8)
    assert repr(s) == "BasePattern(5, None, 8)"
    s = BasePattern(type=7, content=9, name=10)
    assert repr(s) == "BasePattern(7, 9, 10)"



# There are two ways to match a leaf node: by exact value (the default) or using
# a regular expression.


# Generated at 2022-06-13 18:15:46.699544
# Unit test for method generate_matches of class BasePattern
def test_BasePattern_generate_matches():
    from .pgen2.grammar import Grammar

    g = Grammar()
    g.add_production("single", [g.symbol("leaf")])
    singletree = Node(g.symbol2number["single"], [Leaf(g.number2symbol[257], "leaf")])
    assert len(list(BasePattern(257, "leaf").generate_matches([singletree]))) == 1



# Generated at 2022-06-13 18:16:11.416992
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    assert (BasePattern(1, b"foo").optimize() ==
            BasePattern(1, b"foo"))



# Generated at 2022-06-13 18:16:18.684760
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    # Test case with the argument content set to None
    p = NegatedPattern()
    # sequence of no nodes
    assert list(p.generate_matches([])) == [(0, {})]
    # sequence of one node (any node)
    assert len(list(p.generate_matches([1]))) == 0

    # Test case with the argument content set to a pattern
    p = NegatedPattern(LeafPattern(1))

    # sequence of no nodes
    assert list(p.generate_matches([])) == [(0, {})]
    # sequence of one node, that matches the pattern/content
    assert len(list(p.generate_matches([1]))) == 0
    # sequence of one node, that does not match the pattern/content
    assert list(p.generate_matches([2]))

# Generated at 2022-06-13 18:16:27.649629
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    # This is a generator test
    def check(pat, string, result):
        if not isinstance(pat, BasePattern):
            pat = NormalPattern(pat)
        assert list(pat.generate_matches(string)) == result

    check(NegatedPattern(NodePattern(4)), "abc", [(0, {})])
    check(NegatedPattern(NodePattern(4)), "abcd", [])
    check(NegatedPattern(NodePattern(4)), "", [(0, {})])
    check(NegatedPattern(), "", [(0, {})])
    check(NegatedPattern(), "a", [(0, {})])
    check(NegatedPattern(NegatedPattern()), "", [])
    check(NegatedPattern(NegatedPattern()), "a", [])
    # TODO: check that the following test works


# Generated at 2022-06-13 18:16:34.645887
# Unit test for method generate_matches of class NegatedPattern
def test_NegatedPattern_generate_matches():
    class Node:
        value = None

    class LeafNode(Node):
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return 'LeafNode({})'.format(self.value)
    class NonLeafNode(Node):
        def __init__(self, children):
            self.children = children
        def __repr__(self):
            return 'NonLeafNode({})'.format(self.children)


# Generated at 2022-06-13 18:16:46.238811
# Unit test for method set_child of class Node
def test_Node_set_child():
    import lib2to3.fixer_base
    import lib2to3.pgen2.parse
    import lib2to3.pygram
    import lib2to3.pytree
    import lib2to3.fixer_util
    import six
    import sys
    grammar = lib2to3.pygram.python_grammar_no_print_statement
    # We do this the long way, because we need a non-terminal symbol.
    nonterm = grammar._nonterms[list(grammar._nonterms.keys())[0]]
    node = lib2to3.pytree.Node(nonterm, [])
    a = lib2to3.pytree.Leaf(1, 'a')
    b = lib2to3.pytree.Leaf(1, 'b')
    node.append_child(a)


# Generated at 2022-06-13 18:16:51.337247
# Unit test for method remove of class Base
def test_Base_remove():

    class testNode(Base):
        def __init__(self, children, parent):
            self.children = children
            self.parent = parent
    nodeA = testNode([1], None)
    nodeB = testNode([2], None)
    nodeC = testNode([3], None)
    testNode([nodeA, nodeB], None).remove()
    assert nodeA.parent == None
    assert nodeB.parent == None
    assert nodeC.parent == None


# Generated at 2022-06-13 18:17:04.802310
# Unit test for function generate_matches
def test_generate_matches():
    p = parse_pattern("a [b c] [d e] f")
    assert p.match_seq([a, b, c, d, e, f])
    check_gen_match(p, [a, b, c, d, e, f], 1)
    check_gen_match(p, [a, b, d, e, f], 1)
    check_gen_match(p, [a, b, c, d, f], 1)
    check_gen_match(p, [a, b, c, d], 0)
    check_gen_match(p, [a, b, d, f], 0)

    p = parse_pattern(".* a .*")
    assert p.match_seq([b, a, c])

# Generated at 2022-06-13 18:17:12.118141
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    """

    try:
        import ast
    except ImportError:
        import _ast as ast
    tree = ast.parse("""
try:
    x = 1
finally:
    x = 2
""")
    rootnode = nodes.from_ast(tree)
    for n in preorder(rootnode):
        print(n.prefix, n)
    """

# Generated at 2022-06-13 18:17:14.149932
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    instance = BasePattern()
    r = repr(instance)
    assert r == "BasePattern(None, None, None)", r

# Generated at 2022-06-13 18:17:18.994679
# Unit test for method post_order of class Node
def test_Node_post_order():
    SYM = Grammar.symbol
    node = Node(SYM.single_input, [Leaf(1, "print "), Leaf(1, "1"), Leaf(1, "\n")])
    assert list(node.post_order()) == [node.children[0], node.children[1], node]


# Generated at 2022-06-13 18:17:31.825175
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    # Leaf.pre_order() -> Iterator[Leaf]
    # Return a pre-order iterator for the tree.
    node = Leaf(1,'a', (None, (1,0)))
    assert str(node) == "a"
    assert str(node.pre_order()) == "a"


# Generated at 2022-06-13 18:17:33.342967
# Unit test for method leaves of class Leaf
def test_Leaf_leaves():
    l=Leaf(1,"key")
    assert l.leaves()==l


# Generated at 2022-06-13 18:17:34.785064
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(0) == 0
    assert type_repr(python_symbols.power) == "power"



# Generated at 2022-06-13 18:17:43.537841
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():

    class pattern(BasePattern):
        def __init__(self, type, content, name):
            self.type = type
            self.content = content
            self.name = name

        def _submatch(self, node, results=None):
            if not node.prefix:
                return False
            if results is not None:
                results['prefix'] = node.prefix
            return True
            return True

    assert repr(pattern(3, '', 'prefix')) == "pattern(3, '', 'prefix')"

    assert repr(pattern(3, '', None)) == "pattern(3, '')"


# Generated at 2022-06-13 18:17:53.788592
# Unit test for method replace of class Base
def test_Base_replace():
    x = Base()
    x.parent = 'x.parent'
    assert x.was_checked == False
    assert x.was_changed == False
    assert x.parent == 'x.parent'
    assert x.children == []
    assert x.type == None
    try:
        x.replace(new=None)
    except NotImplementedError as e:
        assert str(e) == 'replace() must be implemented'
    else:
        assert False
    try:
        x.replace(new=None)
    except NotImplementedError as e:
        assert str(e) == 'replace() must be implemented'
    else:
        assert False


# Generated at 2022-06-13 18:17:54.874532
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    l = Leaf(1, 'asdf')
    assert list(l.pre_order()) == [l]


# Generated at 2022-06-13 18:18:06.872620
# Unit test for method match of class BasePattern
def test_BasePattern_match():
    from .pgen2.grammar import Grammar

    gr = Grammar()
    t = gr.symbol2number["simple_stmt"]
    x = gr.symbol2number["x"]
    pattern = NodePattern(t)
    result = pattern.match(Node(t, []))
    assert not result
    result = pattern.match(Leaf(t, None))
    assert not result
    result = pattern.match(Leaf(x, None))
    assert not result
    result = pattern.match(Node(x, []))
    assert not result
    class CustomNode(Node):
        parent: Optional[Any] = None  # type: ignore
        type: Optional[int] = None  # type: ignore
    result = pattern.match(CustomNode(t, []))
    assert result
    result = pattern.match

# Generated at 2022-06-13 18:18:10.064859
# Unit test for method pre_order of class Leaf
def test_Leaf_pre_order():
    x = Leaf(0, "fooo")
    assert x.pre_order() == x



# Generated at 2022-06-13 18:18:19.663327
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    a, b, c, d, e, f, g, h = "abcd efgh".split()
    w1 = WildcardPattern([[a, b, c], [d, e], [f, g], [h]])
    w2 = WildcardPattern([[a, b, c], [d, e], [f, g], [h]], min=1)
    w3 = WildcardPattern([[a, b, c], [d, e], [f, g], [h]], max=1)
    w4 = WildcardPattern([[a, b, c], [d, e], [f, g], [h]], min=2)
    w5 = WildcardPattern([[a, b, c], [d, e], [f, g], [h]], max=2)
    w6 = Wildcard

# Generated at 2022-06-13 18:18:23.715596
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq():
    n0 = Node(0, [])
    n1 = Node(1, [])
    n2 = Node(2, [])
    assert BasePattern().match_seq([])
    assert not BasePattern().match_seq([n0, n1])
    assert BasePattern().match_seq([n0])
test_BasePattern_match_seq()

# Generated at 2022-06-13 18:18:47.514396
# Unit test for method match_seq of class WildcardPattern
def test_WildcardPattern_match_seq():
    assert (
        WildcardPattern(min=1, max=1, content=[[Leaf(token.NAME, "x")]]).match_seq(
            (Leaf(token.NAME, "x"),)
        )
        == True
    )
    assert (
        WildcardPattern(min=0, max=1, content=[[Leaf(token.NAME, "x")]]).match_seq(
            ()
        )
        == True
    )
    assert (
        WildcardPattern(min=1, max=1, content=[[Leaf(token.NAME, "x")]]).match_seq(
            ()
        )
        == False
    )


_ALL_PATTERNS = {
    Leaf: LeafPattern,
    Node: NodePattern,
    Wildcard: WildcardPattern,
}



# Generated at 2022-06-13 18:18:57.414348
# Unit test for method replace of class Base
def test_Base_replace():
    from . import pytree
    from .pgen2 import token
    from .pygram import python_symbols as syms
    a = pytree.Leaf(token.NUMBER, "1", prefix=" ")
    b = pytree.Leaf(token.NUMBER, "2", prefix=" ")
    c = pytree.Leaf(token.NUMBER, "3", prefix=" ")
    n = pytree.Node(syms.exprlist, [a, b, c])
    assert a.parent is n
    assert b.parent is n
    assert c.parent is n
    a.replace(pytree.Node(syms.xor_expr, [b]))
    assert a.parent is None
    assert b.parent is n.children[0]
    assert c.parent is n


# Generated at 2022-06-13 18:19:04.945719
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    from .pgen2 import token
    from .pytree import Leaf, Base, Node
    from .pygram import python_symbols

    def t(type, *children):
        return Node(type, list(children), prefix="", context=(None, (0, 0)))

    e = t(python_symbols.error)
    l = t(python_symbols.terminator)
    a = t(python_symbols.atom, e)
    b = t(python_symbols.atom, e)
    c = t(python_symbols.atom, l)
    assert a == b
    assert a != c
    assert a != 1
    assert a != "foo"
    assert a != None
    assert a != t(python_symbols.atom)

# Generated at 2022-06-13 18:19:15.081627
# Unit test for method remove of class Base
def test_Base_remove():
    from .tokenize import generate_tokens

    i = 0
    tokens = generate_tokens("def x(): pass")  # three ENDMARKERs
    while i < 3:
        tok = next(tokens)
        if tok.type == 3:  # ENDMARKER
            i += 1

    assert tok.type == 3
    tok.remove()  # should not raise exception
    try:
        tok.remove()
    except Exception as e:
        assert str(e) == "Leaf: cannot remove from tree"
    else:
        assert False, "should not get here"



# Generated at 2022-06-13 18:19:20.809067
# Unit test for function generate_matches
def test_generate_matches():
    p1 = StringPattern("x")
    p2 = StringPattern("y")
    lst = [(0, {}), (1, {"x": "x"}), (2, {"x": "x", "y": "y"})]
    assert list(generate_matches([p1], "xy")) == lst
    assert list(generate_matches([p1, p2], "xy")) == lst
    assert list(generate_matches([p1, p2], "x")) == []



# Generated at 2022-06-13 18:19:24.999214
# Unit test for method leaves of class Base
def test_Base_leaves():
    a = Node(3, None, None, [Leaf(1, "a"), Leaf(2, "b")])
    assert list(a.leaves()) == [Leaf(1, "a"), Leaf(2, "b")]



# Generated at 2022-06-13 18:19:33.155834
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    import parso.tree
    import collections
    import parso.tree
    t = parso.tree.Node([parso.tree.Leaf(0, "a")], prefix=" ")
    assert list(t.pre_order()) == [t, t.children[0]]
    t1 = parso.tree.Node([t], prefix=" ")
    assert list(t.pre_order()) == [t, t.children[0]]
    assert list(t1.pre_order()) == [t1, t, t.children[0]]



# Generated at 2022-06-13 18:19:41.973991
# Unit test for method replace of class Base
def test_Base_replace():
    from blib2to3.pgen2.tokenize import generate_tokens

    text = "2+2"
    comments = []
    tokens = []
    for tok in generate_tokens(StringIO(text).readline):
        tokens.append(Leaf(tok[0], tok[1], tok[2]))
    n = Node(tokens[0].type, tokens)
    assert n.children[0] is tokens[0]
    n.replace(Leaf(tokens[1].type, "42", tokens[2]))
    assert n.children[0].type == tokens[1].type
    assert n.children[0].value == "42"


# Generated at 2022-06-13 18:19:48.169893
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from . import pytree

# Generated at 2022-06-13 18:19:57.612276
# Unit test for method __eq__ of class Base
def test_Base___eq__():
    a = Base()
    b = Base()
    assert a == "a"
    # Tuple is an unhashable type, so cannot be used in set/dict
    #c = (a, "a")
    #assert c == ("a", b)
    assert isinstance(a, Base) == True
    assert isinstance(a, Leaf) == False
    assert isinstance(a, Node) == False
    d = Leaf(1, "a")
    e = Leaf(1, "a")
    assert d == e
    assert isinstance(d, Base) == True
    assert isinstance(d, Leaf) == True
    assert isinstance(d, Node) == False
    f = Node(1, [])
    g = Node(1, [])
    assert f == g
    assert isinstance(f, Base) == True

# Generated at 2022-06-13 18:20:29.798344
# Unit test for method pre_order of class Node
def test_Node_pre_order():
    from lib2to3.pgen2 import token
    from lib2to3.pgen2 import tokenize
    from lib2to3.pgen2.grammar import Grammar
    from lib2to3.pgen2.convert import fix_indentation
    from lib2to3.pgen2.parse import ParseError
    from lib2to3 import pytree
    from lib2to3 import pygram
    pygram.python_symbols.__dict__
    g = Grammar(grammar_file="Grammar.txt")
    t = g.parse( 
        """
        def foo():
            a = 1
            b = 2
        """)
    pytree.fix_missing_locations(t) # type: ignore
    t = fix_indentation(t)
    #print(t

# Generated at 2022-06-13 18:20:40.086014
# Unit test for method replace of class Base
def test_Base_replace():
    tree = [1, 2, 3, 4, 5]
    tree[1].replace([7, 8])
    assert tree == [1, 7, 8, 3, 4, 5]
    tree = [1, 2, 3, 4, 5]
    tree[1].replace([7])
    assert tree == [1, 7, 3, 4, 5]
    tree = [1, 2, 3, 4, 5]
    tree[1].replace([])
    assert tree == [1, 3, 4, 5]
    tree = [1, 2, 3, 4, 5]
    tree[3].replace(None)
    assert tree == [1, 2, 3, 5]



# Generated at 2022-06-13 18:20:42.471527
# Unit test for method __repr__ of class BasePattern
def test_BasePattern___repr__():
    assert repr(BasePattern(type=2, content=3, name="test")) == "BasePattern(2, 3, 'test')"
    assert repr(BasePattern(type=2, content=3)) == "BasePattern(2, 3)"
    assert repr(BasePattern(type=2)) == "BasePattern(2)"


# Generated at 2022-06-13 18:20:49.838477
# Unit test for method leaves of class Base
def test_Base_leaves():
    from .pytree import Node, Leaf
    from .pygram import python_symbols
    from . import pygram
    from .pgen2 import token
    from .tokenizer import untokenize
    import io, sys

    # stdout = sys.stdout
    # try:
    #     sys.stdout = io.StringIO()
    #     Node(symbol=python_symbols.file_input,
    #                 children=[Node(symbol=python_symbols.simple_stmt,
    #                               children=[Leaf(type=token.PRINT, value='PRINT',
    #                                              context=(u'stmt', (1, 0)))]),
    #                           Node(symbol=python_symbols.simple_stmt,
    #                               children=[Leaf(type=token

# Generated at 2022-06-13 18:20:58.221248
# Unit test for method pre_order of class Base
def test_Base_pre_order():
    expected = "[[1, [2], [3, [4], [5]]], [6], [7, [8], [9], [10]]]"
    root = Node(1)
    root.append_child(Leaf(1, b"", context=None))
    root.append_child(Leaf(2, b"", context=None))
    root.append_child(Node(3))
    root.children[-1].append_child(Leaf(4, b"", context=None))
    root.children[-1].append_child(Leaf(5, b"", context=None))
    root.append_child(Leaf(6, b"", context=None))
    root.append_child(Node(7))

# Generated at 2022-06-13 18:21:04.668541
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    from . import pytree

    t = pytree.Node(42, [pytree.Leaf(1, "hello, "), pytree.Leaf(1, "world")])
    assert t.get_lineno() == 1



# Generated at 2022-06-13 18:21:10.152228
# Unit test for method post_order of class Base
def test_Base_post_order():
    from .pytree import Leaf, Node
    mod = Node(257, [Leaf(1, "a"), Leaf(1, "b")])
    assert list(mod.post_order()) == [Leaf(1, "a"), Leaf(1, "b"), mod]



# Generated at 2022-06-13 18:21:21.535537
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    line = 3
    node = Base()
    assert node.get_lineno() == None, "get_lineno() did not return None"
    leaf = Leaf(1, "", (None, (line, 5)))
    assert leaf.get_lineno() == line, "get_lineno() did not return 3"
    assert leaf.clone().get_lineno() == line, "get_lineno() did not return 3"

    node.children = [leaf]
    assert node.get_lineno() == line, "get_lineno() did not return 3"

    node = Leaf(1, "", (None, (line, 5)))
    assert node.get_lineno() == line, "get_lineno() did not return 3"

    node = Node(2, [], (None, (line, 5)))
    assert node

# Generated at 2022-06-13 18:21:24.997271
# Unit test for method optimize of class BasePattern
def test_BasePattern_optimize():
    import sys

    class SpecialLeafPattern(LeafPattern):
        def optimize(self):
            return sys.modules['lib2to3.pgen2.pattern'].EMPTY


EMPTY = BasePattern()



# Generated at 2022-06-13 18:21:25.621716
# Unit test for method match_seq of class BasePattern
def test_BasePattern_match_seq(): pass

# Generated at 2022-06-13 18:21:50.142646
# Unit test for function type_repr
def test_type_repr():
    assert type_repr(42) == 42


# Generated at 2022-06-13 18:21:55.873675
# Unit test for method generate_matches of class WildcardPattern
def test_WildcardPattern_generate_matches():
    a = Leaf(0, "a")
    b = Leaf(0, "b")
    c = Leaf(0, "c")
    d = Leaf(0, "d")
    p = WildcardPattern([[a, b], [c]], 0, 1, name='wild')
    for count, result in p.generate_matches([a, b, c, d]):
        assert result == {}
    for count, result in p.generate_matches([a, b]):
        assert count == 2 and result == {'wild': [a, b]}
    for count, result in p.generate_matches([a, b, c, a, b]):
        assert count == 4 and result == {'wild': [a, b, c]}

# Generated at 2022-06-13 18:22:08.382402
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    import random
    import pytest
    from lib2to3.fixer_util import Leaf, Node, String
    from lib2to3.fixer_util import find_root, Comment
    from lib2to3.fixer_util import syms

    def build_tree(type_, value, parent=None):
        if type_ == syms.simple_stmt:
            node = SStmt(value)
        elif type_ == syms.name:
            node = Name(value)
        elif type_ == syms.power:
            node = Power(value)
        elif isinstance(value, Leaf):
            node = value
        else:
            assert False, "Unidentified token type %s" % type_
        if parent:
            parent.append_child(node)
        return node


# Generated at 2022-06-13 18:22:15.369747
# Unit test for method get_suffix of class Base
def test_Base_get_suffix():
    import pytree, blib2to3.pygram


# Generated at 2022-06-13 18:22:25.086933
# Unit test for method get_lineno of class Base
def test_Base_get_lineno():
    # class Base:
    #   def get_lineno(self):
    #     node = self
    #     while not isinstance(node, Leaf):
    #       if not node.children:
    #         return None
    #       node = node.children[0]
    #     return node.lineno

    import unittest

    class Test_Base_get_lineno(unittest.TestCase):

        def test__1(self):
            # testing Base.get_lineno()
            from .pytree import Leaf
            from .pygram import python_symbols as syms
