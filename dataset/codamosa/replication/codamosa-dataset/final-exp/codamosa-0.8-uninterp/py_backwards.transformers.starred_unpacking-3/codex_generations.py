

# Generated at 2022-06-14 02:17:08.735285
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import typed_ast.ast3

    node = typed_ast.ast3.parse("[0]")
    node = typed_ast.ast3.fix_missing_locations(node)

    transformer = StarredUnpackingTransformer()
    node = transformer.visit(node)

    assert typed_ast.ast3.dump(node) == "[0]"



# Generated at 2022-06-14 02:17:16.839911
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    node = ast.parse(
        'print(a, b, c[3], *range(10), 1, *range(5))',
        mode='exec',
    )
    expected_node = ast.parse(
        'print(*list(list([a, b, c[3]]) + list(list(range(10)) + list([1])) + list(range(5))))',
        mode='eval',
    )
    actual_node = transformer.visit(node)
    assert actual_node == expected_node


# Generated at 2022-06-14 02:17:23.465828
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """
    Unit test for method visit_Call of class StarredUnpackingTransformer
    """
    #print("StarredUnpackingTransformer.test_visit_Call")
    
    
    source = 'print(*range(1), *range(3))'
    tree = ast.parse(source)
    node = tree.body[0].value
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    node = node.value
    
    
    result = StarredUnpackingTransformer.visit_Call(node)
    assert isinstance(result, ast.Call)
    assert ast.dump(result) == ast.dump(ast.parse('print(*(list(range(1)) + list(range(3))))'))

    # Alternative case

# Generated at 2022-06-14 02:17:34.513987
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from libcst.testing.utils import UnitTest, data_provider
    from libcst.metadata import PositionProvider


# Generated at 2022-06-14 02:17:40.038370
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    expected_source = "print(*(list(range(1)) + list(range(3))))"
    source = "print(*range(1), *range(3))"
    node = ast.parse(source, mode='exec')
    transformer = StarredUnpackingTransformer()
    node = transformer.visit(node)
    source = ast.unparse(node)
    assert source == expected_source


# Generated at 2022-06-14 02:17:42.988127
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert isinstance(StarredUnpackingTransformer().visit_Call(ast.parse("print(*range(1), *range(3))").body[0].value), ast.Call)



# Generated at 2022-06-14 02:17:47.457065
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import ast, astunparse
    test_tree = ast.parse('[2, 4, *[6, 8]]')
    StarredUnpackingTransformer().visit(test_tree)
    assert(astunparse.unparse(test_tree) == '[2, 4] + list([6, 8])')


# Generated at 2022-06-14 02:17:54.869161
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = """
l = [2, *range(10), 1]
"""
    source = ast.parse(code)
    expected_source = ast.parse("""
l = [2] + list(range(10)) + [1]
""")
    t = StarredUnpackingTransformer()
    new_source = t.visit(source)
    assert ast.dump(new_source) == ast.dump(expected_source)


# Generated at 2022-06-14 02:17:57.909306
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    stl = StarredUnpackingTransformer()
    assert(stl is not None)


# Generated at 2022-06-14 02:18:06.894462
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .test_utils import make_test_function
    from .unpacking import UnpackingTransformer
    from .call_expression import CallExpressionTransformer

    tree = make_test_function("[2, *range(10)]")
    tree = UnpackingTransformer().visit(tree)
    tree = StarredUnpackingTransformer().visit(tree)
    assert tree.body[0].value.func.id == 'list'

    tree = make_test_function("print(*range(1), *range(3))", (3, 6))
    tree = UnpackingTransformer().visit(tree)
    tree = StarredUnpackingTransformer().visit(tree)
    tree = CallExpressionTransformer().visit(tree)
    print(ast.dump(tree))
    assert tree.body[0].value.func.id

# Generated at 2022-06-14 02:18:18.541489
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .helper import get_node_str
    from .unparsing import Case
    source = 'print(*range(1), *range(3))'
    expected = 'print(*(list(range(1)) + list(range(3))))'
    transformer = StarredUnpackingTransformer()
    transformer.apply_to_call(Case(source, expected), 'visit_Call')


# Generated at 2022-06-14 02:18:27.935471
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert StarredUnpackingTransformer().visit(
        ast.parse('print(1, *[3, 3], 2, *[4, 4, 4], sep="")').body[0].value) == \
        ast.parse('print(*list(1, *[3, 3], 2, *[4, 4, 4], sep=""))').body[0].value

# Generated at 2022-06-14 02:18:33.085922
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = "[*range(3), 2, 4, *[1]]"
    expected = "list(range(3)) + [2, 4] + list([1])"
    result = StarredUnpackingTransformer(source).result()
    assert str(ast.parse(result).body[0]) == str(ast.parse(expected).body[0])



# Generated at 2022-06-14 02:18:39.007248
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("print(*range(1), *range(3))", mode='eval')
    StarredUnpackingTransformer().visit(node)

    node = ast.parse("print(*(list(range(1)) + list(range(3))))", mode='eval')
    compare_ast(node, StarredUnpackingTransformer().visit(node))


# Generated at 2022-06-14 02:18:46.415781
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # test for simple call
    tree = ast.parse("print('Hello world!')")
    visitor = StarredUnpackingTransformer()
    new_tree = visitor.visit(tree)
    expected_tree = ast.parse("print('Hello world!')")
    assert ast.dump(new_tree) == ast.dump(expected_tree)

    # test for call with multiple args
    tree = ast.parse("print(1, 2, 3)")
    visitor = StarredUnpackingTransformer()
    new_tree = visitor.visit(tree)
    expected_tree = ast.parse("print(1, 2, 3)")
    assert ast.dump(new_tree) == ast.dump(expected_tree)

    # test for call with starred args
    tree = ast.parse("print(*[1, 2, 3])")


# Generated at 2022-06-14 02:18:53.887498
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    name_node = ast.Name(id='name')
    list_node = ast.List(elts=[])
    call_node1 = ast.Call(func=name_node, args=[], keywords=[])
    call_node2 = ast.Call(func=name_node, args=[list_node], keywords=[])
    call_node3 = ast.Call(func=name_node, args=[call_node1, call_node2], keywords=[])

    tree_before = call_node3

# Generated at 2022-06-14 02:18:55.180449
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:19:05.923507
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.List(
        elts=[
            ast.Num(n=2),
            ast.Starred(
                value=ast.Call(
                    func=ast.Name(id='range'),
                    args=[
                        ast.Num(n=10)],
                    keywords=[
                        ast.keyword(
                            arg=None,
                            value=None)]),
                ctx=ast.Load()),
            ast.Num(n=1)],
        ctx=ast.Load())
    visitor = StarredUnpackingTransformer()
    result = visitor.visit(node)
    assert isinstance(result, ast.BinOp)
    assert isinstance(result.left, ast.List)
    assert result.op == ast.Add()
    assert isinstance(result.right, ast.Call)

# Generated at 2022-06-14 02:19:08.061095
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    """Unit test for constructor of class StarredUnpackingTransformer"""

# Generated at 2022-06-14 02:19:18.995245
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert str(StarredUnpackingTransformer()) == 'StarredUnpackingTransformer'


# Unit tests for class StarredUnpackingTransformer


# Generated at 2022-06-14 02:19:41.070033
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert ast.dump(StarredUnpackingTransformer().visit(
        ast.parse('print(*range(1), *range(3))')),
        include_attributes=True) == \
"""Module(body=[
  Expr(value=Call(
    func=Name(id='print', ctx=Load()),
    args=[Starred(value=BinOp(
      left=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Num(n=1)], keywords=[])], keywords=[]),
      op=Add(),
      right=List(elts=[])))),
    keywords=[],
    starargs=None,
    kwargs=None))])"""

# Generated at 2022-06-14 02:19:44.602540
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert (
        StarredUnpackingTransformer(
            [ast.parse('[2, *range(10), 1]')]).visit() ==
        'list([2]) + list(range(10)) + list([1])')


# Generated at 2022-06-14 02:19:52.635430
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():   # pylint: disable=invalid-name
    """Unit test for method visit_Call of class StarredUnpackingTransformer"""

    source = """range(1, *range(3))"""
    expected = """list(range(1)) + list(range(3))"""

    node = ast.parse(source)
    StarredUnpackingTransformer().visit(node)
    assert astor.to_source(node) == expected

# Generated at 2022-06-14 02:20:03.554451
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:20:14.925258
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    # From
    code = """
[2, *range(10), 1]
print(*range(1), *range(3))
    """
    expected = """
[2] + list(range(10)) + [1]
print(*(list(range(1)) + list(range(3))))
    """
    # When
    actual = StarredUnpackingTransformer().visit(ast.parse(code))
    # Then
    print("ACTUAL:")
    print(astunparse.unparse(actual))
    print("EXPECTED:")
    print(expected)
    assert astunparse.unparse(actual) == expected

# Generated at 2022-06-14 02:20:25.053904
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse('[2, *range(10), 1]')
    splitted = StarredUnpackingTransformer._split_by_starred(node.body[0].value.elts)
    prepared = tuple(StarredUnpackingTransformer._prepare_lists(splitted))
    merged = StarredUnpackingTransformer._merge_lists(prepared)

    assert splitted == [[ast.Num(2)], ast.Starred(value=ast.Call(func=ast.Name(id='range'), args=[ast.Num(10)], keywords=[])), [ast.Num(1)]]

# Generated at 2022-06-14 02:20:33.598512
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    e = ast.Call(
            func=ast.Name(id='func_1'),
            args=[
                ast.Starred(value=ast.Name(id='arg1')),
                ast.Name(id='arg2'),
                ast.Starred(value=ast.Name(id='arg3')),
                ast.Name(id='arg4'),
                ast.Starred(value=ast.Name(id='arg5'))],
            keywords=[])

# Generated at 2022-06-14 02:20:45.376696
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    with open("carrots/tests/test_ast_compilers/temp.py", "w") as f:
        f.write("lista = [3, *range(3), *range(5)]")

    root = ast.parse(source=open("carrots/tests/test_ast_compilers/temp.py", "rt").read())
    StarredUnpackingTransformer().visit(root)


# Generated at 2022-06-14 02:20:56.330659
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    _StarredUnpackingTransformer = StarredUnpackingTransformer.__new__(StarredUnpackingTransformer)
    assert _StarredUnpackingTransformer._has_starred([]) == False
    assert _StarredUnpackingTransformer._has_starred([ast.Starred(value=ast.Name(id='starred'))]) == True
    assert _StarredUnpackingTransformer._has_starred([ast.Name(id='name')]) == False
    assert _StarredUnpackingTransformer._split_by_starred([ast.Name(id='name')]) == ([ast.Name(id='name')], [], [])

# Generated at 2022-06-14 02:20:58.326874
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer()

# Generated at 2022-06-14 02:21:32.991857
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    s = StarredUnpackingTransformer()
    assert ast.dump(s.visit(ast.parse('[1, 2, 3]'))) == 'Module(body=[Expr(value=List(elts=[Num(n=1), Num(n=2), Num(n=3)], ctx=Load()))])'

# Generated at 2022-06-14 02:21:40.002978
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List of class StarredUnpackingTransformer"""

    source = """
[2, *range(10), 1]
    """

    tree = ast.parse(source)
    visitor = StarredUnpackingTransformer()
    tree = visitor.visit(tree)
    assert_source_equal("[2] + list(range(10)) + [1]", tree)

    # def visit_Call(self, node: ast.Call) -> ast.Call:


# Generated at 2022-06-14 02:21:52.619507
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def check(code, expected):
        node = ast.parse(code)
        result = StarredUnpackingTransformer().visit(node)
        assert ast.dump(result) == expected

    check('print(*range(2))', 'Module(body=[Expr(value=Call(func=Name(id="print", ctx=Load()), args=[Starred(value=List(elts=[Call(func=Name(id="range", ctx=Load()), args=[Constant(value=2)], keywords=[])]))], keywords=[]))])')

# Generated at 2022-06-14 02:21:56.763234
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import __t
    source = """
    print(*[x for x in range(10)], 1)
    """

    assert StarredUnpackingTransformer(source).result == """
    print(*(list([x for x in range(10)]) + [1]))
    """


# Generated at 2022-06-14 02:22:01.133872
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    node = ast.parse('[2, *range(10), 1]')
    expected = ast.parse('[2] + list(range(10)) + [1]')
    actual = StarredUnpackingTransformer().visit(node)

    assert ast.dump(actual) == ast.dump(expected)

# Generated at 2022-06-14 02:22:08.865897
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
print(1, *[2, *range(3), 4], 5)
print(6, *range(7), 8, *range(9), 10, *range(10), 11)
"""
    expected = """
print(*(list([1]) + list([2, 3, 4, 5])))
print(*(list([6, 7, 8]) + list([9]) + list([10, 11])))
"""
    tree = ast.parse(code)
    StarredUnpackingTransformer().visit(tree)
    actual = compile(tree, '', 'exec')
    assert expected == actual.co_code

# Generated at 2022-06-14 02:22:19.450730
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert 'list([2]) + list([1, 2, 3])' == ''.join(x.code for x in compile_to_ast('''
    [2] + [1, 2, 3]
    '''))

    assert 'list([]) + list([1, 2])' == ''.join(x.code for x in compile_to_ast('''
    [] + [1, 2]
    '''))

    assert 'list(range(1)) + list(range(3)) + list([4, 5])' == ''.join(x.code for x in compile_to_ast('''
    [*range(1), *range(3), 4, 5]
    '''))


# Generated at 2022-06-14 02:22:27.524524
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import textwrap

    from .base import BaseNodeTest

    class Test(BaseNodeTest):
        transformer = StarredUnpackingTransformer()
        target = (3, 4)

        def test_call_starred_arg_simple(self):
            before = textwrap.dedent("""
            print(*range(10))
            """)
            after = textwrap.dedent("""
            print(*list(range(10)))
            """)
            self.transformation_test(before, after)

        def test_call_multiple_starred_args(self):
            before = textwrap.dedent("""
            print(*range(5), *range(6))
            """)
            after = textwrap.dedent("""
            print(*(list(range(5)) + list(range(6))))
            """)
            self

# Generated at 2022-06-14 02:22:35.396672
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
        def foo(a, b):
            pass

        foo(1, *range(10))

        foo(*range(10), *range(15))
    """
    expected_code = """
        def foo(a, b):
            pass

        foo(1, *list(range(10)))

        foo(*(list(range(10)) + list(range(15))))
    """

    transformer = StarredUnpackingTransformer()
    assert transformer.run(code) == expected_code


# Generated at 2022-06-14 02:22:45.726371
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    # Arrange
    ast_tree = ast.parse('''[2, *range(10), 1]
    print(*range(1), *range(3))''')

    # Act
    tr = StarredUnpackingTransformer()
    tr.visit(ast_tree)
    printed = ast.dump(ast_tree, annotate_fields=True, include_attributes=True)
    file = open('output/startred-test.txt', 'w')
    file.write(printed)
    file.close()

    # Assert
    # Check the third statement of the ast_tree
    # Expect is:   print(*(list(range(1)) + list(range(3))))
    assert len(ast_tree.body) == 2
    assert isinstance(ast_tree.body[1], ast.Expr)
   

# Generated at 2022-06-14 02:23:39.828329
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = "[2, *range(10), 1]"
    expected = "[2] + list(range(10)) + [1]"
    tree = ast.parse(source)
    assert ast.dump(tree) == source
    transformer = StarredUnpackingTransformer()
    tree = transformer.visit(tree)
    assert ast.dump(tree) == expected
    assert transformer.is_changed()


# Generated at 2022-06-14 02:23:51.434522
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class TestContext():
        def __init__(self):
            self.result = {}

    tctx = TestContext()

    class TestTransformer(BaseNodeTransformer):
        def visit_Call(self, node):
            tctx.result["visit_Call"] = node
            return self.generic_visit(node)

    test_input = ast.parse("print(*range(1), *range(3))")
    StarredUnpackingTransformer().visit(test_input)
    TestTransformer().visit(test_input)
    assert tctx.result["visit_Call"].args[0].value.right.right.elts[0].value.args[0].n == 1
    assert tctx.result["visit_Call"].args[0].value.right.left.elts[0].value.args

# Generated at 2022-06-14 02:24:02.931054
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import ast3
    from typed_ast import parse

    code = ' [2, *range(10), 1] '
    tree = parse(code)
    copy_tree = StarredUnpackingTransformer().visit(tree)
    expected_result = ast3.parse(
        ' [2] + list(range(10)) + [1] ', mode='eval')
    assert ast3.dump(copy_tree) == ast3.dump(expected_result)

    code = ' [2, *range(10), 1]  + [2, *range(10), 1] '
    tree = parse(code)
    copy_tree = StarredUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 02:24:05.493922
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    x = StarredUnpackingTransformer()
    assert x

if __name__ == '__main__':
    test_StarredUnpackingTransformer()

# Generated at 2022-06-14 02:24:15.338017
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()

    i = 0
    for test_case, expected in get_test_cases_for_visit_Call():
        i += 1
        print(f"Test {i}: {test_case}")
        node = ast.parse(test_case).body[0]
        got = transformer.visit(node)

        print(ast.dump(got))
        print(ast.dump(ast.parse(expected)))
        assert ast.dump(got) == ast.dump(ast.parse(expected))



# Generated at 2022-06-14 02:24:25.013718
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    input_code = """
        print(1)
    """
    expected_code = """
        print(1)
    """
    StarredUnpackingTransformer(input_code=input_code, expected_code=expected_code).test_equivalence()

    input_code = """
        print(*range(2))
    """
    expected_code = """
        print(*list(range(2)))
    """
    StarredUnpackingTransformer(input_code=input_code, expected_code=expected_code).test_equivalence()

    input_code = """
        print(*range(2), *range(4))
    """
    expected_code = """
        print(*(list(range(2)) + list(range(4))))
    """

# Generated at 2022-06-14 02:24:26.117881
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    c = StarredUnpackingTransformer()
    assert c

# Generated at 2022-06-14 02:24:32.673937
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    transpiler = StarredUnpackingTransformer()
    assert transpiler.target == (3, 4)
    assert transpiler.transpile('[2, *range(10), 1]') == '[2] + list(range(10)) + [1]'
    assert transpiler.transpile('print(*range(1), *range(3))') == 'print(*(list(range(1)) + list(range(3))))'



# Generated at 2022-06-14 02:24:40.666671
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    t = StarredUnpackingTransformer()
    node = ast.parse("print(*range(1), *range(3))")
    t.visit(node)
    assert isinstance(node, ast.Module)
    assert isinstance(node.body[0], ast.Expr)
    assert isinstance(node.body[0].value, ast.Call)
    call_node = node.body[0].value
    assert isinstance(call_node.func, ast.Name)
    assert isinstance(call_node.args[0], ast.Starred)
    assert isinstance(call_node.args[0].value, ast.BinOp)
    assert isinstance(call_node.args[0].value.op, ast.Add)

# Generated at 2022-06-14 02:24:51.408168
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import print_ast

    code1 = 'print(0, *range(10), 1)'
    code2 = 'print(*range(10))'
    code3 = 'print(*range(10), 1)'

    ast1 = compile(code1, '<string>', mode='exec', optimize=0)
    ast2 = compile(code2, '<string>', mode='exec', optimize=0)
    ast3 = compile(code3, '<string>', mode='exec', optimize=0)

    node_transformer = StarredUnpackingTransformer()
    print_ast(ast1)
    print()
    node_transformer.visit(ast1)
    print()
    print_ast(ast1)
    print()

    print_ast(ast2)
    print()
    node_transformer.visit

# Generated at 2022-06-14 02:26:42.011930
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = "[2, *range(10), 1]"
    expected_code = "[2] + list(range(10)) + [1]"
    test_code = transform_code(StarredUnpackingTransformer, code)
    assert test_code == expected_code



# Generated at 2022-06-14 02:26:50.013528
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Given
    source = 'print(*range(1), *range(3))'
    expected = 'print(*(list(range(1)) + list(range(3))))'
    node = ast.parse(source)

    # When
    actual = StarredUnpackingTransformer().visit(node)

    # Then
    assert ast.dump(actual, annotate_fields=False) == ast.dump(ast.parse(expected), annotate_fields=False)



# Generated at 2022-06-14 02:26:55.795313
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_util import roundtrip_unparse
    s = "print(*range(1), *range(3))"
    expected = "print(*(list(range(1)) + list(range(3))))"
    actual = roundtrip_unparse(ast.parse(s), StarredUnpackingTransformer)
    assert actual == expected, f'{actual} != {expected}'

