

# Generated at 2022-06-14 02:17:17.131417
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    con = StarredUnpackingTransformer()

    result = ast.parse("[2, *range(10), 1]").body[0].value
    assert isinstance(result, ast.List)

    expected_result = ast.BinOp(
        left=ast.List(elts=[
            ast.Num(n=2),
        ]),
        right=ast.Call(
            func=ast.Name(id='list'),
            args=[
                ast.Call(
                    func=ast.Name(id='range'),
                    args=[
                        ast.Num(n=10),
                    ],
                    keywords=[]
                )
            ],
            keywords=[],
        ),
        op=ast.Add(),
    )

# Generated at 2022-06-14 02:17:28.705709
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():

    # Test for method _has_starred
    #
    # Test for empty expression
    assert not StarredUnpackingTransformer()._has_starred([])

    # Test for starred expression
    assert StarredUnpackingTransformer()._has_starred([ast.Starred()])

    # Test for non-starred expression
    assert not StarredUnpackingTransformer()._has_starred([ast.Name()])

    # Test for normal expression
    assert not StarredUnpackingTransformer()._has_starred([ast.Name(), ast.Name()])

    # Test for normal expression with starred expression
    assert StarredUnpackingTransformer()._has_starred([ast.Name(), ast.Name(), ast.Starred()])

    # Test for method _split_by_starred
    #
    # Test for empty expression
    assert Star

# Generated at 2022-06-14 02:17:37.745404
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    a = ast.parse("[2, *range(10), 1]")
    b = ast.parse("[2] + list(range(10)) + [1]")
    b_starred = ast.parse("[2] + *range(10)+ [1]")
    c = ast.parse("*range(10)+ [1]")
    c_starred = ast.parse("*range(10) + *range(10) + [1]")
    d = ast.parse("[2] + list(range(10)) + list(range(10)) + list(range(10)) + [1]")
    d_starred = ast.parse("[2] + *range(10)+ *range(10) + *range(10) + [1]")

# Generated at 2022-06-14 02:17:47.743603
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import textwrap
    from .. import js, utils

    print("\n" + "=" * 50, __name__)
    print("Test StarredUnpackingTransformer.visit_Call")

    # Let's try one
    source = textwrap.dedent("""\
    # Python 3.4+
    print(*[1, 2])
    """)
    tree = utils.ast_from_source(source)
    tree = StarredUnpackingTransformer().visit(tree)
    expected_js = textwrap.dedent("""\
    # Python 3.4+
    
    print.apply(void 0, [1, 2]);
    """)
    assert js(tree) == expected_js

# Generated at 2022-06-14 02:17:59.923572
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from textwrap import dedent
    from .base import BaseNodeTransformer
    from .const_fold import ConstantFoldingTransformer
    from .no_paren import NoParenthesesTransformer
    from .unwrap_const import UnwrapConstantTransformer
    from .unwrap_expr import UnwrapExpressionTransformer
    from .unwrap_noops import UnwrapNoopsTransformer
    from .unwrap_seq import UnwrapSequenceTransformer
    from .wrap_const import WrapConstantTransformer


# Generated at 2022-06-14 02:18:09.353295
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def test(before, after):
        t = StarredUnpackingTransformer()
        t.visit(ast.parse(before))
        assert t.dump() == after

    test("print(1, *[1])", "print(list([1]) + [1])")
    test("print(1, 2, *[1])", "print(list([1, 2]) + [1])")
    test("print(*[1], 1, 2, *[1])", "print(*(list([1]) + list([1, 2]) + [1]))")
    test("print(*[1, 2], 3, *[4])", "print(*(list([1, 2]) + [3] + list([4])))")

# Generated at 2022-06-14 02:18:20.511606
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast as test_ast
    test_ast_node = test_ast.parse('''print(*range(1), *range(3))''')
    star_unpack_transformer = StarredUnpackingTransformer()
    star_unpack_transformer.visit(test_ast_node)

# Generated at 2022-06-14 02:18:32.735236
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .unparser import CodeUnparser
    from .compiler import compile_code
    from .tests.test_utils import compare_trees

    code = """
        print(*range(1), *range(3))
    """

    # Create code tree
    tree = ast.parse(code)
    unparser = CodeUnparser()

    # Transform tree
    StarredUnpackingTransformer(tree).visit(tree)
    output = unparser.unparse(tree)

    # Compare with expected result
    actual = compile_code(output)
    expect = compile_code(code)

    compare_trees(expect, actual)



# Generated at 2022-06-14 02:18:41.842087
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .base import compile_source, dump_tree, iterate_nodes

    source = "[2, *range(10), 1]"
    expected_source = "[2] + list(range(10)) + [1]"
    tree = compile_source(source, 'exec')
    StarredUnpackingTransformer().visit(tree)
    dump_tree(tree)
    compiled = compile(tree, '<test>', 'exec')
    eval(compiled)
    tree2 = compile_source(expected_source, 'exec')
    assert dump_tree(tree) == dump_tree(tree2)


# Generated at 2022-06-14 02:18:49.338366
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    from .fix_missing_locations import InsertLineIfMissing
    from .base import BaseNodeTransformer
    # Given
    code = """
    print('first', *range(10))
    """
    expected_code = """
    print(*(['first'] + list(range(10))))
    """
    tree = ast.parse(code)
    # When
    tree = StarredUnpackingTransformer().visit(tree)
    InsertLineIfMissing().visit(tree)
    # Then
    assert astor.to_source(tree) == expected_code



# Generated at 2022-06-14 02:19:05.127093
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
        print(*[1], *[2])
        print(*[1], 1, *[2], 2)
        print(*[1], 1, *[2], 2, *[3, 4], *[5, 6])
        print(*[1], 1, *[2], 2, *[3, 4], *[5, 6], 7, 8, *[9])
    """

# Generated at 2022-06-14 02:19:10.156123
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    src = "[2, *range(10), 1]"
    # Compiled
    expected = "[2] + list(range(10)) + [1]"
    result = StarredUnpackingTransformer().visit(ast.parse(src))
    assert ast.dump(result) == expected


# Generated at 2022-06-14 02:19:17.252364
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import compile_to_ast
    from .base import compare_source

    code = 'print(*range(1), *range(3))'
    expected = 'print(*(list(range(1)) + list(range(3))))'

    transform = StarredUnpackingTransformer()
    ast_tree = compile_to_ast(code)
    new_ast = transform.visit(ast_tree)
    source = compare_source(new_ast)
    assert source == expected

# Generated at 2022-06-14 02:19:21.629025
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('print(*range(1), *range(3))')
    StarredUnpackingTransformer.run_check(tree)
    assert ast.dump(tree) == ast.dump(ast.parse('print(*(list(range(1)) + list(range(3))))'))

# Generated at 2022-06-14 02:19:33.194134
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()

    node_list1 = ast.List(
        elts=[
            ast.Name(id='a'),
            ast.Call(func=ast.Name(id='b'), args=[], keywords=[])])
    node_list2 = ast.List(elts=[ast.Name(id='c')])

    assert transformer.visit(node_list1) == node_list1
    assert transformer.visit(node_list2) == node_list2

    code_list1 = '[1, *a, *range(10), 2]'
    node_list1 = ast.parse(code_list1).body[0].value

# Generated at 2022-06-14 02:19:39.606393
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    # Should not be changed, empty list
    ast.parse("[2, 3, 4]")

    # Should not be changed, no starred
    ast.parse("[2, 3, *range(4), 5]")

    # Should produce same result as first variant
    ast.parse("[2] + list(range(10)) + [1]")

    # Should produce same result as second variant
    ast.parse("print(*(list(range(1)) + list(range(3))))")

# Generated at 2022-06-14 02:19:47.951247
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    example = [
        ast.List(
            elts=[
                ast.Num(n=2),
                ast.Starred(
                    value=ast.Call(
                        func=ast.Name(id='range'),
                        args=[
                            ast.Num(n=10)
                        ],
                        keywords=[]
                    )),
                ast.Num(n=1)
            ]
        )
    ]

# Generated at 2022-06-14 02:19:58.634315
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit-tests method visit_List of class StarredUnpackingTransformer.
    """
    node = ast.parse("[2, *range(10), 1]").body[0].value
    assert isinstance(node, ast.List)
    node = StarredUnpackingTransformer().visit(node)
    assert isinstance(node, ast.BinOp)
    assert isinstance(node.left, ast.List)
    assert isinstance(node.right, ast.List)
    assert isinstance(node.op, ast.Add)
    node = StarredUnpackingTransformer().visit(node)
    assert isinstance(node, ast.BinOp)


# Generated at 2022-06-14 02:20:05.130350
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert StarredUnpackingTransformer([ast.Call(
        func=ast.Name(id='foo'),
        args=[ast.Num(n=1), ast.Starred(value=ast.Name(id='a'))],
        keywords=[])]).result() == '[ast.Call(func=ast.Name(id="foo"), args=[ast.Starred(value=ast.BinOp(left=ast.List(elts=[ast.Num(n=1)]), right=ast.Call(func=ast.Name(id="list"), args=[ast.Name(id="a")], keywords=[]), op=ast.Add()))], keywords=[])]'



# Generated at 2022-06-14 02:20:18.145083
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node_call = ast.Call(func=ast.Name(id='print'),
                         args=[ast.List(elts=[ast.Starred(value=ast.Name(id='range'), ctx=ast.Load()),
                                               ast.Starred(value=ast.Name(id='range'), ctx=ast.Load())])],
                         keywords=[ast.keyword(arg='sep', value=ast.Str(s=','))], )

# Generated at 2022-06-14 02:20:28.557844
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer()

# Generated at 2022-06-14 02:20:35.231851
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import ast3 as ast
    from typed_ast import parse
    from .helpers import list_equal_ast

    tests = [
        ("[2, *range(10), 1]", "[2] + list(range(10)) + [1]"),
    ]
    for test in tests:
        s, out = test
        node = parse(s, "<string>", "exec")
        x = StarredUnpackingTransformer().visit(node)
        print(ast.dump(x))
        assert list_equal_ast(x, parse(out, "<string>", "exec"))



# Generated at 2022-06-14 02:20:38.921478
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    print("Testing for constructor of class StarredUnpackingTransformer")
    a = StarredUnpackingTransformer()
    assert(a._tree_changed == False)


# Generated at 2022-06-14 02:20:45.612231
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import ast3 as ast
    import sys
    import io
    from .codegen import to_source, parse

    p = parse('''
    test = [2, *range(10), 1]
    ''')

    t = StarredUnpackingTransformer()
    t.visit(p)

    c = to_source(p)

    assert c == '''
    test = [2] + list(range(10)) + [1]
    '''



# Generated at 2022-06-14 02:20:56.468432
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    """Test the constructor of class StarredUnpackingTransformer."""
    node = ast.List()
    transformer = StarredUnpackingTransformer(node)
    result = transformer._has_starred([])
    assert result == False
    node1 = ast.Starred()
    result = transformer._has_starred([node1])
    assert result == True
    node2 = ast.Name()
    node_list = [node2, node2, node2]
    result = transformer._split_by_starred(node_list)
    assert result == [[node2, node2, node2]]
    node_list = [node2, node2, node2, node1, node2, node2, node2]
    result = transformer._split_by_starred(node_list)
    assert result[1] == node1
    node

# Generated at 2022-06-14 02:20:58.407763
# Unit test for method visit_List of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:21:07.108302
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    inp = """
        print(*range(1), *range(3))
        print(*range(1))
        print(*range(3))
        """
    expected_out = """
        print(*(list(range(1)) + list(range(3))))
        print(*list(range(1)))
        print(*list(range(3)))
        """
    out = StarredUnpackingTransformer().visit(ast.parse(inp))
    assert ast.unparse(out) == expected_out


# Generated at 2022-06-14 02:21:10.777994
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("""
        print(*range(1), *range(3))
    """, mode='exec')
    result = StarredUnpackingTransformer().visit(tree)
    assert_equal_source("""
        print(*(list(range(1)) + list(range(3))))
    """, result)


# Generated at 2022-06-14 02:21:23.076541
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    @compile_to_ast('[2, *range(10), 1]')
    def test_List():
        return [2, *range(10), 1]

    @compile_to_ast('[2] + list(range(10)) + [1]')
    def test_List():
        return list([2, *range(10), 1])

    @compile_to_ast('[2, 3] + list(range(10)) + [1]')
    def test_List():
        return list([2, 3, *range(10), 1])

    @compile_to_ast('[2, 3] + list(range(10)) + [1, 2, 3]')
    def test_List():
        return list([2, 3, *range(10), 1, 2, 3])


# Generated at 2022-06-14 02:21:26.749745
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    a = StarredUnpackingTransformer()
    assert str(a) == 'StarredUnpackingTransformer'


# Generated at 2022-06-14 02:21:47.895925
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert isinstance(StarredUnpackingTransformer(), StarredUnpackingTransformer)

# Generated at 2022-06-14 02:21:58.399324
# Unit test for method visit_List of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:22:09.798942
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    def subtest(source: str, expected: str) -> None:
        result = StarredUnpackingTransformer().visit(ast.parse(source))
        assert ast.dump(result) == expected

    subtest(
        '[2, *range(10), 1]',
        'Module(body=[Expr(value=BinOp(left=List(elts=[Num(n=2)]), op=Add(), right=Call(func=Name(id=\'list\', ctx=Load()), args=[Call(func=Name(id=\'range\', ctx=Load()), args=[Num(n=10)], keywords=[])], keywords=[])))])'
    )


# Generated at 2022-06-14 02:22:15.975762
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astunparse

    transformer = StarredUnpackingTransformer()
    source = '[2, *range(10), 1]'
    tree = ast.parse(source)
    assert transformer.visit_List(tree.body[0].value) == ast.parse('[2] + list(range(10)) + [1]').body[0].value



# Generated at 2022-06-14 02:22:24.588244
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse('[2, *range(10), 1]')
    callback = StarredUnpackingTransformer()
    callback(node)
    assert ast.dump(node) == 'Expr(value=BinOp(left=List(elts=[Num(n=2)]), op=Add(), right=BinOp(left=Call(func=Name(id="list", ctx=Load()), args=[Call(func=Name(id="range", ctx=Load()), args=[Num(n=10)], keywords=[])], keywords=[]), op=Add(), right=List(elts=[Num(n=1)]))))'


# Generated at 2022-06-14 02:22:36.804614
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_utils import _deep_parse
    # Test cases

# Generated at 2022-06-14 02:22:45.253938
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call(): 
    from example_visitors.miniflask import parse
    from .is_equal_trees import is_equal_trees
    from .is_equal_trees import is_equal_lists
    from .is_equal_trees import is_equal_nodes
    from .is_equal_trees import is_equal_node


# Generated at 2022-06-14 02:22:50.104341
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = ast.parse("""subprocess.Popen('ls', '-l', '-a', *os.listdir() )""")
    obj = StarredUnpackingTransformer()
    new_source = obj.visit(source)
    expected = """subprocess.Popen(*(['ls', '-l', '-a'] + list(os.listdir())) )"""
    assert astor.to_source(new_source).strip() == expected


# Generated at 2022-06-14 02:23:00.903881
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    node_visited = transformer.visit(
        ast.parse("""
print(*list(range(10)), 10)
"""))
    node_expected = ast.parse("""
print(*(list(range(10)) + [10]))
""")
    assert ast.dump(node_visited) == ast.dump(node_expected)
    transformer = StarredUnpackingTransformer()
    node_visited = transformer.visit(
        ast.parse("""
print([10, *range(10), 10])
"""))
    node_expected = ast.parse("""
print([10] + list(range(10)) + [10])
""")
    assert ast.dump(node_visited) == ast.dump(node_expected)


# Generated at 2022-06-14 02:23:08.543660
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = 'print(*range(1), *range(3))'
    tree = ast.parse(code)
    expected_result = ast.parse('print(*(list(range(1)) + list(range(3))))')
    node = tree.body[0]
    transformer = StarredUnpackingTransformer()
    result = transformer.visit(node)
    assert transformer._tree_changed == True
    assert ast.dump(result) == ast.dump(expected_result.body[0])

# Generated at 2022-06-14 02:23:51.021293
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import typed_ast.ast3 as ast
    StarredUnpackingTransformer().visit(ast.parse('[4, *list, 3]'))


# Generated at 2022-06-14 02:23:55.423072
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astunparse
    import ast
    code = "[2, *range(10), 1]"
    expected = "[2] + list(range(10)) + [1]"

    tree = ast.parse(code)
    # ast.dump(tree)

    StarredUnpackingTransformer().visit(tree)
    result = astunparse.unparse(tree)
    assert result == expected

    code = "[*range(10), *range(3)]"
    expected = "list(range(10)) + list(range(3))"

    tree = ast.parse(code)
    # ast.dump(tree)

    StarredUnpackingTransformer().visit(tree)
    result = astunparse.unparse(tree)
    assert result == expected


# Generated at 2022-06-14 02:24:06.368457
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from .helpers import parse, roundtrip

    test_cases = """
        print(1, *args)
        print(1, *args, *args)
        print(1, *args, *args, 2)
        print(*args, 1, *args, *args)
        print(*args, *args, *args)
    """


# Generated at 2022-06-14 02:24:18.362677
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:24:27.001028
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    instance = StarredUnpackingTransformer()
    empty_list = ast.parse("[]")
    assert not instance.visit(empty_list).body[0]

    list1_list2 = ast.parse("[2, 3, 4] + [5, 6, 7]")
    assert instance.visit(list1_list2).body[0] == ast.List(
        elts=[ast.Num(n=2), ast.Num(n=3), ast.Num(n=4), ast.Num(n=5),
              ast.Num(n=6), ast.Num(n=7)])

    list1_list2_starred = ast.parse("[2, 3, 4] + [5, 6, 7] + [*range(10)]")

# Generated at 2022-06-14 02:24:37.532187
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import NodeTransformerTestCase
    from .base import parse

    class TestCase(NodeTransformerTestCase):
        target_node = ast.Call

        @classmethod
        def _prepare_stmt_text(cls, stmt_text: str) -> str:
            return 'print({})'.format(stmt_text)


# Generated at 2022-06-14 02:24:45.710924
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .transformer_test import TransformerTest
    from .transformer_test import parse_ast_tree

    source = """
        [2, *range(10), 1]
        for i in [*range(5), *range(10)]:
            print(i)
        print(*range(1), *range(3))
    """
    expected = """
        [2] + list(range(10)) + [1]
        for i in list(range(5)) + list(range(10)):
            print(i)
        print(*(list(range(1)) + list(range(3))))
    """
    tree = parse_ast_tree(source)
    node_transformer = StarredUnpackingTransformer()
    new_tree = node_transformer.visit(tree)
    assert TransformerTest.compare_

# Generated at 2022-06-14 02:24:51.031941
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Test method visit_List of class StarredUnpackingTransformer"""
    from . import compile_source
    code = "[2, *range(10), 1]"
    expected_code = "[2] + list(range(10)) + [1]"
    assert compile_source(StarredUnpackingTransformer, code) == expected_code


# Generated at 2022-06-14 02:25:03.687595
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_utils import parse, round_trip
    from typed_astunparse import unparse

    tree = parse("""[2, *range(10), 1]""")
    tree = StarredUnpackingTransformer().visit(tree)
    assert unparse(tree) == "[2] + list(range(10)) + [1]"
    round_trip(tree)

    # Empty list
    tree = parse("""[]""")
    tree = StarredUnpackingTransformer().visit(tree)
    assert unparse(tree) == "[]"
    round_trip(tree)

    # List without starred
    tree = parse("""[1, 2, 3]""")
    tree = StarredUnpackingTransformer().visit(tree)
    assert unparse(tree) == "[1, 2, 3]"

# Generated at 2022-06-14 02:25:10.029446
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import uncompyle6
    
    code = """
        print(*range(1), *range(3))
    """

    pyc = compile(code, '<string>', mode='exec', optimize=2)
    node = uncompyle6.decompile(pyc)
    mod = ast.Module([node])
    StarredUnpackingTransformer().visit(mod)
    code_target = '''\
print(*(list(range(1)) + list(range(3))))
'''
    assert ast.dump(mod) == ast.dump(ast.parse(code_target))


# Generated at 2022-06-14 02:26:42.711844
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from ..ut import AST_TEST_CASES, run_test_cases
    run_test_cases(StarredUnpackingTransformer, AST_TEST_CASES)
test_StarredUnpackingTransformer.__test__ = False

# Generated at 2022-06-14 02:26:44.709343
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    a = StarredUnpackingTransformer()
    print (a)


# Generated at 2022-06-14 02:26:54.675138
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # def a():
    #     x = [2, *range(10), 1]
    actual_program = \
"""def a():
    x = [2, *range(10), 1]"""
    expected_program = \
"""def a():
    x = [2] + list(range(10)) + [1]"""
    program_ast = ast.parse(actual_program)
    expected_ast = ast.parse(expected_program)
    actual_ast = StarredUnpackingTransformer().visit(program_ast)
    assert ast.dump(actual_ast) == ast.dump(expected_ast)
    assert ast.dump(actual_ast) == ast.dump(expected_ast)


# Generated at 2022-06-14 02:26:59.236177
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    src = ast.parse(
        "[2, *range(10), 1]",
        mode="eval")
    expected = ast.parse(
        "[2] + list(range(10)) + [1]",
        mode="eval")
    StarredUnpackingTransformer().visit(src)
    assert ast.dump(src, annotate_fields=False) == ast.dump(expected,
                                                            annotate_fields=False)

