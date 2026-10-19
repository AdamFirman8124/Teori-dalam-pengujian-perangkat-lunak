

# Generated at 2022-06-14 02:17:01.034950
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:17:05.509027
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    sut = StarredUnpackingTransformer()
    code = """foo(1, *x, 2)"""
    node = ast.parse(code)
    expected_code = """foo(*(1 + list(x) + 2))"""
    expected_node = ast.parse(expected_code)

    sut.visit(node)
    assert node == expected_node



# Generated at 2022-06-14 02:17:11.722407
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from ast_toolbox.to_source import to_source

    tree = ast.parse('[2, *range(10), 1]')

    transformer = StarredUnpackingTransformer()
    new_tree = tree.body[0].value
    transformer.visit(new_tree)
    assert to_source(new_tree) == '[2] + list(range(10)) + [1]'


# Generated at 2022-06-14 02:17:17.063703
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    srt = StarredUnpackingTransformer()
    code = "[2, *range(10), 1]"
    tree = ast.parse(code)
    result = srt.visit(tree)
    expected = ast.parse("[2] + list(range(10)) + [1]")
    assert ast.dump(result) == ast.dump(expected)



# Generated at 2022-06-14 02:17:27.676509
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_code = "[2, *range(10), 1]"
    expected = [ast.List(elts = [ast.Num(n = 2.0), ast.Call(func = ast.Name(id = 'list'), args = [ast.Call(func = ast.Name(id = 'range'), args = [ast.Num(n = 10.0)], keywords = [], starargs = None, kwargs = None)], keywords = [], starargs = None, kwargs = None), ast.Num(n = 1.0)], ctx = ast.Load())]

    tree = parse(test_code)
    StarredUnpackingTransformer.apply(tree)

    assert tree.body[0].elts == expected[0].elts


# Generated at 2022-06-14 02:17:37.885016
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .mst import parse_ast
    from .unparse import Unparser
    from .pprint import PrettyPrinter

    code1 = """print(*range(1), *range(3))"""
    code2 = """foo(*range(1), *range(3))"""
    code3 = """foo(1, *range(1), 2, 3, *range(3), 4)"""
    code4 = """foo(1, 2, *range(5), *range(6), 7, 8)"""

    for code in [code1, code2, code3, code4]:
        tree = parse_ast(code)
        StarredUnpackingTransformer().visit(tree)
        source = Unparser(tree)
        print(PrettyPrinter().pformat(tree))
        print(source)

# Generated at 2022-06-14 02:17:44.375150
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """
    Test StarredUnpackingTransformer.visit_Call(self, node: ast.List) -> ast.List of class StarredUnpackingTransformer
    """
    code = """
    foo(1, 2, 3)
    """
    exp_code = """
    foo(1, 2, 3)
    """
    node = ast.parse(code)
    expected_node = ast.parse(exp_code)
    transformer = StarredUnpackingTransformer()
    transformer.visit(node)
    assert ast.dump(node) == ast.dump(expected_node)


# Generated at 2022-06-14 02:17:45.753321
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:17:55.011798
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import typed_ast.ast3 as ast
    from typed_astunparse import unparse
    from .test_helper import check_equal_ast

    source = '''
        print(*range(1), *range(3))
    '''
    tree = ast.parse(source)
    expected_tree = ast.parse('''
        print(*(list(range(1)) + list(range(3))))
    ''')
    check_equal_ast(StarredUnpackingTransformer().visit(tree), expected_tree)


# Generated at 2022-06-14 02:18:00.930953
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = """
    [1, 2, 3, 4]
    """
    expected = """
    [1, 2, 3, 4]
    """
    node = ast.parse(code)
    StarredUnpackingTransformer().visit(node)
    actual = ast.dump(node)
    print(actual)
    assert actual == expected


# Generated at 2022-06-14 02:18:14.920852
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from compiler.transformer.compile import compile
    from compiler.transformer.transform import transform
    StarredUnpackingTransformer._tree_changed = False
    node = compile("[2, *range(10), 1]")
    transform(node, StarredUnpackingTransformer)
    assert StarredUnpackingTransformer._tree_changed
test_StarredUnpackingTransformer()

# Generated at 2022-06-14 02:18:23.334204
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("""print(*range(1), *range(3))""")
    expected = """print(*(list(range(1)) + list(range(3))))"""
    actual = StarredUnpackingTransformer().visit(node)
    actual = StarredUnpackingTransformer().visit(actual)
    actual = ast.unparse(actual)
    assert actual.strip() == expected.strip()


# Generated at 2022-06-14 02:18:34.128953
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class MockStarredUnpackingTransformer(StarredUnpackingTransformer):
        def __init__(self, node: ast.AST):
            super().__init__(args=())
            self._node = node
        
        def to_ast(self) -> ast.AST:
            return self.visit(self._node)

    assert str(MockStarredUnpackingTransformer(node=ast.parse('print(*[1, 2], *[3, 4], *[5, 6])')).to_ast()) == \
        "print(*([1, 2] + list([3, 4]) + list([5, 6])))"


# Generated at 2022-06-14 02:18:38.785807
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .utils import roundtrip

    test_code = """print(*range(1), *range(3))"""
    expected = """print(*(list(range(1)) + list(range(3))))"""
    assert roundtrip(test_code, StarredUnpackingTransformer) == expected



# Generated at 2022-06-14 02:18:46.217231
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse(
        "print(*range(1), *range(3))")

# Generated at 2022-06-14 02:18:53.709998
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .base import compile_to_ast

    cases = [
        "[2, *range(10), 1]",
        "[]",
        "[*range(1), 2]",
        "[2, *range(3)]",
        "[2, *range(3), *range(1)]",
        "[2, *range(3), *range(1), 1]",
        "[2, *range(3), *[1, 2], 1]",
    ]

# Generated at 2022-06-14 02:19:04.747586
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astunparse
    input_string = """assert len(args) >= 2 and isinstance(args[0], str),\n            "first argument must be string"\n"""
    expected_output_string = """assert len(list(args[:2]) + list(args[2:])) >= 2 and isinstance(args[0], str),\n            "first argument must be string"\n"""
    module_node = ast.parse(input_string)
    assert isinstance(module_node, ast.Module)
    assert len(module_node.body) == 1
    assert isinstance(module_node.body[0], ast.Assert)
    assert len(module_node.body[0].test.args) == 2
    assert isinstance(module_node.body[0].test, ast.Call)

# Generated at 2022-06-14 02:19:09.912971
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert astor.to_source(
        StarredUnpackingTransformer().visit(
            ast.parse('''
        print(*range(1), *range(3))
        '''))) == '''\
print(*(list(range(1)) + list(range(3))))
'''



# Generated at 2022-06-14 02:19:14.002377
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .helper import transform_and_run
    assert transform_and_run('print(*range(1), *range(3))', StarredUnpackingTransformer) == '[1, 2, 3]\n'



# Generated at 2022-06-14 02:19:23.741061
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('print(*range(1), *range(3))').body[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)

    transformer = StarredUnpackingTransformer()
    result = transformer.visit(node.value)  # type: ignore

# Generated at 2022-06-14 02:19:37.867580
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # Arrange
    node = ast.parse("a = [1, 2, 3, 4, 5]").body[0].value
    expected_result = "[1, 2, 3, 4, 5]"

    # Act
    new_node = StarredUnpackingTransformer().visit(node)
    result = astunparse.unparse(new_node)

    # Assert
    assert expected_result == result


# Generated at 2022-06-14 02:19:52.472129
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert ast.dump(StarredUnpackingTransformer().visit(ast.parse("[2, *range(10), 1]"))) == \
           "Expr(value=BinOp(left=List(elts=[Num(n=2)], ctx=Load()), op=Add(), right=BinOp(left=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Num(n=10)], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None), op=Add(), right=List(elts=[Num(n=1)], ctx=Load()))))"  # noqa


# Generated at 2022-06-14 02:19:58.720431
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import ast3
    from .utils import assert_programs_equivalent
    from .base import BaseNodeTransformer

    class MyStarredUnpackingTransformer(BaseNodeTransformer):
        def __init__(self, tree: ast3.AST):
            super().__init__(tree)
            self._transformer = StarredUnpackingTransformer(tree)

        def _visit_List(self, node: ast3.List) -> ast3.List:
            return self._transformer.visit_List(node)

    program0 = ast3.parse('[2, *range(10), 1]')
    program1 = ast3.parse('[2] + list(range(10)) + [1]')


# Generated at 2022-06-14 02:20:05.608512
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse("""[2, *range(10), 1]""")  # type: ast.AST
    StarredUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == \
           "Module(body=[Expr(value=BinOp(left=List(elts=[Num(n=2)]), op=Add(), right=BinOp(left=Call(args=[Call(" \
           "args=[Name(id='range', ctx=Load()), Num(n=10)], func=Name(id='range', ctx=Load()), keywords=[], " \
           "starargs=None, kwargs=None), ctx=Load()), op=Add(), right=List(elts=[Num(n=1)]))))])"



# Generated at 2022-06-14 02:20:11.345697
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('fn(1, *[1, 2], *[3, 4])')
    StarredUnpackingTransformer().visit(tree)
    expected_tree = ast.parse('fn(*(list([1, 2]) + list([3, 4])))')
    assert ast_diff(tree, expected_tree) == []

# Generated at 2022-06-14 02:20:18.806065
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = [2, *range(10), 1]

    source2 = [2, *[], 1]

    module = ast.parse(repr(source))

    module2 = ast.parse(repr(source2))

    StarredUnpackingTransformer().visit(module)

    StarredUnpackingTransformer().visit(module2)

    assert ast.dump(module) == ast.dump(ast.parse('[2] + list(range(10)) + [1]'))

    assert ast.dump(module2) == ast.dump(ast.parse('[2, 1]'))


# Generated at 2022-06-14 02:20:25.520065
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    for version in (3, 4):
        x = "f([2, *range(10), 1])"
        node = ast.parse(x, version=version).body[0].value

        expected = "f(list([2] + list(range(10)) + [1]))"
        expected = ast.parse(expected, version=version).body[0].value.args[0]

        result = StarredUnpackingTransformer(version=version).visit(node)
        assert result == expected

        x = "[2, 3, *range(10), 5, 6, 7, 1, 2, 3]"
        node = ast.parse(x, version=version).body[0].value


# Generated at 2022-06-14 02:20:37.152460
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import typed_astunparse
    import astunparser
    from .unwrap_parentheses import UnwrapParenthesesTransformer
    from .join_if import JoinIfTransformer
    from .factor_out_lambda_with_single_call import FactorOutLambdaWithSingleCallTransformer
    from .preprocess import PreprocessTransformer
    from .remove_in_constructor import RemoveInConstructorTransformer
    from .remove_is_constructor import RemoveIsConstructorTransformer
    from .constant_folding import ConstantFoldingTransformer
    from .remove_alias_import import RemoveAliasImportTransformer
    from .nonlocal_declaration_inheritance import NonlocalDeclarationInheritanceTransformer
    from .remove_not_in_constructor import RemoveNotInConstructorTransformer
    from .remove_none_comparison import RemoveNone

# Generated at 2022-06-14 02:20:48.058905
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse('[1, *x, 2]')
    result = StarredUnpackingTransformer().visit(node)

    assert isinstance(result, ast.BinOp)

    assert isinstance(result.left, ast.List)
    assert result.left.elts == [ast.Num(n=1)]

    assert isinstance(result.right, ast.BinOp)
    assert isinstance(result.right.left, ast.Call)
    assert isinstance(result.right.left.func, ast.Name)
    assert result.right.left.func.id == 'list'
    assert result.right.left.args[0] == ast.Name(id='x')
    assert result.right.right.elts == [ast.Num(n=2)]


# Generated at 2022-06-14 02:20:49.523626
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer(None) is not None

# Generated at 2022-06-14 02:21:04.440200
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('foo(1, *range(2), *range(2))')
    expected = ast.parse('foo(*(([1] + list(range(2))) + list(range(2))))')
    StarredUnpackingTransformer().visit(node)
    assert ast.dump(node) == ast.dump(expected)


# Generated at 2022-06-14 02:21:12.681049
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    node = ast.Call(
        func=ast.Name(id='print'),
        args=[ast.Num(n=1), ast.Starred(
            value=ast.List(elts=[ast.List(elts=[ast.Num(n=2)]), ast.List(elts=[ast.Num(n=3)])]))],
        keywords=[])

    transformed = transformer.visit(node)

    assert isinstance(transformed.args[0], ast.Starred)
    assert isinstance(transformed.args[0].value, ast.BinOp)
    assert isinstance(transformed.args[0].value.left, ast.List)
    assert isinstance(transformed.args[0].value.left.elts[0], ast.List)

# Generated at 2022-06-14 02:21:24.016935
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_AST = parse('''\
[2, *range(10), 1]''')
    node = test_AST.body[0]

    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.List)
    assert len(node.value.elts) == 3
    assert isinstance(node.value.elts[1], ast.Starred)
    assert isinstance(node.value.elts[1].value, ast.Call)
    assert isinstance(node.value.elts[1].value.func, ast.Name)
    assert node.value.elts[1].value.func.id == 'range'
    assert len(node.value.elts[1].value.args) == 1

# Generated at 2022-06-14 02:21:32.486056
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = """\
x = [2, 3, *range(10)]
y = [3, *range(5), 7]
z = [*range(5), 8]

list([1, *range(10)])
"""
    expected_result = """\
x = [2, 3] + list(range(10))
y = [3] + list(range(5)) + [7]
z = list(range(5)) + [8]

list([1, *(list(range(10)))])
"""
    assert_results(StarredUnpackingTransformer, source, expected_result)


# Generated at 2022-06-14 02:21:37.978632
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from . import BaseNodeTransformer

    transformer = StarredUnpackingTransformer(None, None)
    assert transformer

    from typed_ast import ast3 as ast
    assert transformer.visit(ast.List([ast.Num(1), ast.Starred(ast.Name(id='range'), ast.Load()), ast.Num(3)]))

# Generated at 2022-06-14 02:21:40.230652
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    # Asserting if class StarredUnpackingTransformer is initialised
    assert StarredUnpackingTransformer() is not None


# Generated at 2022-06-14 02:21:45.449977
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    statement = 'print(*range(1), *range(3))'
    expected_result = 'print(*(list(range(1)) + list(range(3))))'

    tree = ast.parse(statement)
    node_transformer = StarredUnpackingTransformer(tree)
    assert node_transformer.result == expected_result



# Generated at 2022-06-14 02:21:47.420157
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer(3, 4).target == (3, 4)

# Generated at 2022-06-14 02:21:57.709516
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert StarredUnpackingTransformer.subclass_visit_List("[2, 3, *[4], 5]") == "[2, 3, 4, 5]"

    assert StarredUnpackingTransformer.subclass_visit_List("[2, 3, *[4, 5], 6]") == "[2, 3, [4, 5], 6]"

    assert StarredUnpackingTransformer.subclass_visit_List("[*[1, 2, 3]]") == "list([1, 2, 3])"

    assert StarredUnpackingTransformer.subclass_visit_List("[*[1, *[2, *[3, *[4, *[5]]]]]]") == "list([1, 2, 3, 4, 5])"


# Generated at 2022-06-14 02:22:07.116961
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast
    import typed_ast.ast3 as typed_ast
    transformer = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:22:32.079114
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    transformer = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:22:37.508514
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse(
        'print(*range(1), *range(3))',
        mode='exec').body[0].value
    expected_node = ast.parse(
        'print(*(list(range(1)) + list(range(3))))',
        mode='exec').body[0].value
    actual_node = StarredUnpackingTransformer().visit(node)
    assert ast.dump(expected_node) == ast.dump(actual_node)

# Generated at 2022-06-14 02:22:47.901631
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    ast_to_compile = ast.parse("""
[1, 2, *range(10), 3, 4, *range(3)]
""")
    # Compile
    compiled = compile_source(ast_to_compile, StarredUnpackingTransformer)
    assert_equal(
        compiled,
        """
[1, 2, ] + list(range(10)) + [3, 4, ] + list(range(3))
""")


# Generated at 2022-06-14 02:22:54.984423
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from astor.code_gen import unparse
    from astor.source_repr import parse
    src = 'func1([1, 2, 3], e, f, *g)'
    node = parse(src).body[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    StarredUnpackingTransformer().visit(node)
    assert 'func1(list([1, 2, 3]) + list([e]) + list([f]) + list(g))' == unparse(node)


# Generated at 2022-06-14 02:23:01.741887
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    test_input = ast.parse('foo(*range(1), *range(3))')
    expected_output = 'foo(*(list(range(1)) + list(range(3))))\n'

    output = StarredUnpackingTransformer().visit(test_input)
    assert expected_output == astor.to_source(output)


# Generated at 2022-06-14 02:23:12.862267
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_code_1 = """
        [2, *range(10), 1]
    """
    test_ast_1 = ast.parse(test_code_1)
    expected_ast_1 = ast.parse("""
        [2] + list(range(10)) + [1]
    """)
    StarredUnpackingTransformer().visit(test_ast_1)
    assert ast.dump(test_ast_1, include_attributes=False) == ast.dump(expected_ast_1, include_attributes=False)



# Generated at 2022-06-14 02:23:23.937390
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse("[1, *range(10)]", mode='eval')
    tree = StarredUnpackingTransformer.run_on(node)
    result = ast.dump(tree)
    assert_equal(result, "Call(func=Name(id='list', ctx=Load()), args=[List(elts=[Num(n=1)], ctx=Load()), Call(func=Name(id='range', ctx=Load()), args=[Num(n=10)], keywords=[], starargs=None, kwargs=None)], keywords=[])\n")


# Generated at 2022-06-14 02:23:35.153755
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    trans = StarredUnpackingTransformer(path='')
    assert not trans._has_starred([])
    assert not trans._has_starred([ast.Num(n=1)])
    assert not trans._has_starred([ast.Num(n=1), ast.Num(n=2)])
    assert trans._has_starred([ast.Num(n=1), ast.Starred(value=ast.Call(func=ast.Name(id='range'), args=[ast.Num(n=10)], keywords=[])), ast.Num(n=2)])


# Generated at 2022-06-14 02:23:46.960803
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .transformers_test_utils import run_test_transformer
    from .transformers_test_utils import run_test_transformer_fixme
    from .transformers_test_utils import run_test_transformer_fail
    from .transformers_test_utils import run_test_transformer_doesnt_change

    code = """
print(*range(1), *range(3))
list(range(1), *range(3))
list([*range(1), *range(3)])
""".strip()

    expected = """
print(*(range(1) + range(3)))
list(range(1), *range(3))
list(*(range(1) + range(3)))
""".strip()

    run_test_transformer(StarredUnpackingTransformer, code, expected)


# Generated at 2022-06-14 02:23:56.130833
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("print(*range(1), *range(3))", mode="eval")
    expected_tree = ast.parse(
        "print(*(list(range(1)) + list(range(3))))",
        mode="eval")

    transformer = StarredUnpackingTransformer()
    result_tree = transformer.visit(tree)

    assert tree != result_tree
    assert ast.dump(expected_tree) == ast.dump(result_tree)



# Generated at 2022-06-14 02:24:39.542480
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    import unittest
    class Test(unittest.TestCase):
        def test_simple(self):
            code = 't.f(*range(2), *range(3))'
            expected = 't.f(*(list(range(2)) + list(range(3))))'
            
            node = ast.parse(code)
            node = node.body[0]
            assert isinstance(node, ast.Expr)
            node = node.value
            assert isinstance(node, ast.Call)
            
            xformer = StarredUnpackingTransformer()
            node = xformer.visit(node)
            self.assertEqual(expected, ast.dump(node))


# Generated at 2022-06-14 02:24:45.513272
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = """
    [2, *range(10), 1]
    """
    tree = ast.parse(code)
    expected = """
    [2] + list(range(10)) + [1]
    """
    result = StarredUnpackingTransformer().visit(tree)
    assert expected == astor.to_source(result)



# Generated at 2022-06-14 02:24:51.988555
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import typed_ast.ast3 as ast

    source = "[2, *range(10), 1]"
    expected = "[2] + list(range(10)) + [1]"

    tree = ast.parse(source)
    tree = StarredUnpackingTransformer.run_multiple([tree])
    result = compile(tree, '<string>', 'eval').co_consts[0]

    assert result == eval(expected)



# Generated at 2022-06-14 02:25:04.653069
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse("[2, *range(10), 1]")
    tree = StarredUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 02:25:10.555076
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def transform(tree):
        return StarredUnpackingTransformer().visit(tree)
    # Tests without star
    tree = ast.parse("""
        myfunc(1, 2, 3, 4, 5)""")
    new_tree = transform(tree)
    assert astor.to_source(new_tree) == "myfunc(1, 2, 3, 4, 5)"
    # Tests with star
    tree = ast.parse("""
        myfunc(1, 2, 3, *[4, 5], 6)""")
    new_tree = transform(tree)
    assert astor.to_source(new_tree) == "myfunc(*([1, 2, 3] + [4, 5] + [6]))"
    # Tests with star and call

# Generated at 2022-06-14 02:25:18.648261
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .. import compile_to_ast
    from ..utils import ast_to_str

    source = '[2, *range(10), 1]'
    expected = '[2] + list(range(10)) + [1]'

    transformer = StarredUnpackingTransformer()
    node = compile_to_ast(source)
    transfromed_node = transformer.visit(node)

    assert transformer._tree_changed
    assert ast_to_str(transfromed_node) == expected


# Generated at 2022-06-14 02:25:29.261732
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert compile(
            'print(2, 3)',
            '<test>', 'exec', ast.PyCF_ONLY_AST).body[0] == ast.parse(
        'print(2, 3)', '<test>', 'exec').body[0]
    assert compile(
            'print(*range(1), *range(2), 4)',
            '<test>', 'exec', ast.PyCF_ONLY_AST).body[0] == ast.parse(
        'print(*list(range(1)) + list(range(2)) + [4])', '<test>', 'exec').body[0]

# Generated at 2022-06-14 02:25:38.986275
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    node = ast.parse("[2, *range(10), 1]")
    test_obj = StarredUnpackingTransformer()
    expected = ast.parse("[2] + list(range(10)) + [1]")
    assert test_obj.visit(node) == expected
    test_obj = StarredUnpackingTransformer()
    node = ast.parse("print(*range(1), *range(3))")
    expected = ast.parse("print(*(list(range(1)) + list(range(3))))")
    assert test_obj.visit(node) == expected

test_StarredUnpackingTransformer()

# Generated at 2022-06-14 02:25:46.007845
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    src = "[2, *range(10), 1]"
    expected = "asttools.module_to_code(asttools.code_to_module('''\n[2] + list(range(10)) + [1]\n'''))"
    module = asttools.code_to_module(src=src)
    module = StarredUnpackingTransformer().visit(module)
    module = asttools.module_to_code(module)
    module = asttools.code_to_module(src=module)
    module = asttools.module_to_code(module)
    assert module == asttools.eval_(expected)



# Generated at 2022-06-14 02:25:55.403136
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    supt = StarredUnpackingTransformer()
    supt.visit(
        ast.parse(
            'print(*range(1), *range(3))'))
    assert supt.tree_changed
    assert ast.dump(supt.tree) == \
    "Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Starred(value=BinOp(left=BinOp(left=List(elts=[Num(n=1)]), right=List(elts=[Num(n=3)]), op=Add()), right=List(elts=[Num(n=3)]), op=Add()))], keywords=[]))])"
