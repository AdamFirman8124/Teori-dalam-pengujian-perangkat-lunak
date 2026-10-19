

# Generated at 2022-06-14 02:17:11.095933
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astor
    source = "[2, *range(10), 1]"
    tree = ast.parse(source)
    expected = ast.parse("[2] + list(range(10)) + [1]")
    transformer = StarredUnpackingTransformer()
    transformed = transformer.visit(tree)
    transformed_as_code = astor.to_source(transformed)
    expected_as_code = astor.to_source(expected)
    assert transformed_as_code == expected_as_code


# Generated at 2022-06-14 02:17:21.107943
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    code = """
    x = [1, *range(10), 2]
    y = [1, *range(10), 2]
    def f(x, *args):
        x = 1
        z = 2
        y = 1
        print(x, *args)
        return x, *args
    print(1, *range(10), 2)
    """
    tree = ast.parse(code)
    tree = StarredUnpackingTransformer().visit(tree)
    compiler = ast.PyCF_ONLY_AST | getattr(compile, 'PyCF_DONT_IMPLY_DEDENT', 0)
    code2 = compile(tree, '<test>', 'exec', flags=compiler)
    locals_: Dict[str, List[int]] = {}

# Generated at 2022-06-14 02:17:33.211715
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert _test_StarredUnpackingTransformer_visit_List.example_good_0() == ([2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1], [2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1])
    assert _test_StarredUnpackingTransformer_visit_List.example_good_1() == ([2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1], [2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1])

# Generated at 2022-06-14 02:17:34.892081
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer([])

# Generated at 2022-06-14 02:17:41.118673
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .compile import compile_source
    source = '''
    print(*range(1), *range(2))
    [1, *range(10), 2]
    [1, *range(10), 2, *range(5), 3]
    '''
    transformed = StarredUnpackingTransformer().visit(
        compile_source(source, mode='single')
    )
    code = compile(transformed, '', 'single')
    eval(code)

# Generated at 2022-06-14 02:17:45.452203
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    visitor = StarredUnpackingTransformer()
    result = visitor.visit(ast.parse('''[2, *range(10), 1]'''))
    expectation = ast.parse('''[2] + list(range(10)) + [1]''')
    assert ast.dump(result) == ast.dump(expectation)

# Generated at 2022-06-14 02:17:53.073009
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def transpile(code: str) -> str:
        tree = ast.parse(code)
        StarredUnpackingTransformer().visit(tree)
        return tree

    assert transpile('print(1, *args)') == \
        ast.parse('print(*((1,) + tuple(args)))')  # type: ignore
    assert transpile('print(1, *args, 2)') == \
        ast.parse('print(*(((1,) + tuple(args)) + (2,)))')  # type: ignore
    assert transpile('func(*args)') == \
        ast.parse('func(*tuple(args))')  # type: ignore



# Generated at 2022-06-14 02:17:58.938446
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import ast
    import textwrap
    print(ast.dump(ast.parse(textwrap.dedent(r"""
        [2, *range(10), 1]
        print(*range(1), *range(3))
        """))))

# Generated at 2022-06-14 02:18:02.932630
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # test input
    input = """\
print(*range(1), *range(3))
    """
    # expected output
    output = """\
print(*(list(range(1)) + list(range(3))))
    """
    # actual output
    actual = compile(input, filename='', mode='exec')
    # check
    assert output == actual

# Generated at 2022-06-14 02:18:11.887709
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = ast.parse('[2, *range(10), 1]')
    result = StarredUnpackingTransformer().visit(code)
    assert isinstance(result, ast.Expr)
    assert isinstance(result.value, ast.BinOp)
    assert isinstance(result.value.left, ast.List)
    assert isinstance(result.value.right, ast.List)
    assert isinstance(result.value.right.elts[0], ast.Call)
    assert isinstance(result.value.right.elts[1], ast.Num)
    assert result.value.right.elts[0].func.id == 'list'
    assert result.value.right.elts[1].n == 1
    assert result.value.op.__class__ == ast.Add


# Generated at 2022-06-14 02:18:20.430963
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    from .base import BaseNodeTransformer
    from .starred_unpacking import StarredUnpackingTransformer
    from .unpacking_unpacking_transformer import UnpackingUnpackingTransformer
    from .unpacking_transformer import UnpackingTransformer

    code = astor.to_source(
        ast.parse(
            """
        print([1, 2, 3] + list(range(5)) + list(x + 2 for x in range(6)))
        print(*[1, 2, 3], *range(5), *list(x + 2 for x in range(6)))
        """
        )
    )
    vars = {}
    exec(code, globals(), vars)  # pylint: disable=exec-used

    call1 = vars['call1']

# Generated at 2022-06-14 02:18:33.494736
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .base import BaseTestTransformer
    from _ast import parse
    from astunparse import dump
    from io import StringIO

    class Test(BaseTestTransformer):
        transformer = StarredUnpackingTransformer

        def test_basic(self):
            inp = """
            [2, *range(10), 1]
            """
            outp = """
            [2] + list(range(10)) + [1]
            """
            self.check(inp, outp)

        def test_complex(self):
            inp = """
            [1, *[2], *range(10), *tuple(range(5))]
            """
            outp = """
            [1] + list([2]) + list(range(10)) + list(tuple(range(5)))
            """

# Generated at 2022-06-14 02:18:43.435814
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('foo(*range(10), *range(15))')
    StarredUnpackingTransformer().visit(tree)
    result = ast.dump(tree)
    expected = "Call(func=Name(id='foo'), args=[Starred(value=BinOp(left=Call(func=Name(id='list'), args=[Call(func=Name(id='range'), args=[Num(n=10)], keywords=[])], keywords=[]), right=Call(func=Name(id='list'), args=[Call(func=Name(id='range'), args=[Num(n=15)], keywords=[])], keywords=[]), op=Add()))], keywords=[])"
    assert result == expected


# Generated at 2022-06-14 02:18:50.486821
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast,typed_ast.ast3 as ast3
    source_code = 'print(*range(1), *range(3))'
    source_ast = ast.parse(source_code)
    typed_ast = ast3.parse(source_code)
    typed_ast = StarredUnpackingTransformer().visit(typed_ast)
    assert ast.dump(source_ast) == ast.dump(typed_ast)


# Generated at 2022-06-14 02:19:01.831795
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # [2, *range(10), 1] -> [2] + list(range(10)) + [1]
    code = "[2, *range(10), 1]"
    node_before = ast.parse(code)
    result_before = compile(node_before, '<test>', 'eval')
    assert eval(result_before) == [2, *range(10), 1]

    transformer = StarredUnpackingTransformer()
    node_after = transformer.visit(node_before)
    result_after = compile(node_after, '<test>', 'eval')
    assert eval(result_after) == [2, *range(10), 1]

    # [2, 3, 4] -> [2, 3, 4]
    code = "[2, 3, 4]"

# Generated at 2022-06-14 02:19:06.297166
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    module = ast.parse('print(*range(1), *range(3))')
    StarredUnpackingTransformer(module).run()
    expected = ast.parse('print(*(list(range(1)) + list(range(3))))')
    assert ast_to_code(module) == 'print(*(list(range(1)) + list(range(3))))'


# Generated at 2022-06-14 02:19:18.056443
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import typed_astunparse
    # Test 1
    input_string = """
    a = [1, *range(10), 1]
    """
    expected_string = """
    a = [1] + list(range(10)) + [1]
    """
    node = ast.parse(input_string)
    StarredUnpackingTransformer().visit(node)
    actual_string = typed_astunparse.unparse(node)
    assert actual_string == expected_string
    # Test 2
    input_string = """
    a = [1, 2, *range(10), 1]
    """
    expected_string = """
    a = [1, 2] + list(range(10)) + [1]
    """
    node = ast.parse(input_string)

# Generated at 2022-06-14 02:19:30.678175
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    @compile_to_ast("print(*x)")
    def _():
        x = [1, 2, 3]
        print(*x)

    x1 = _.body[1].value
    assert isinstance(x1, ast.Starred)
    assert isinstance(x1.value, ast.Call)
    assert isinstance(x1.value.func, ast.Name)
    assert x1.value.func.id == 'list'
    assert isinstance(x1.value.args[0], ast.Name)

    @compile_to_ast("print(*x, *y)")
    def _():
        x = [1, 2, 3]
        y = [4, 5, 6]
        print(*x, *y)

    x1 = _.body[1].value
    assert isinstance

# Generated at 2022-06-14 02:19:31.634875
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    pass

# Generated at 2022-06-14 02:19:32.930649
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer()


# Generated at 2022-06-14 02:19:46.034031
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    node_transformer = StarredUnpackingTransformer()
    '''
    example tree = ast.parse("[2, *range(10), 1]")
    result = node_transformer.visit(example_tree)
    print(ast.dump(result))
    '''
    example_tree = ast.parse("print(*range(1), *range(3))")
    result = node_transformer.visit(example_tree)
    # print(ast.dump(result))
    expected_tree = ast.parse("print(*(list(range(1)) + list(range(3))))")
    if ast.dump(result) != ast.dump(expected_tree):
        assert False, 'error: transformer is wrong'
    else:
        print('Transformer test OK')


# Generated at 2022-06-14 02:19:53.128453
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('print(*range(1), *range(3))')

    transformer = StarredUnpackingTransformer()
    new_tree = transformer.visit(tree)

    expected_tree = ast.parse(
        'print(*(list(*range(1)) + list(*range(3))))')
    assert ast.dump(new_tree) == ast.dump(expected_tree)


# Generated at 2022-06-14 02:19:57.897869
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """print(*range(1), *range(3))"""
    expected = """print(*(list(range(1)) + list(range(3))))"""

    tree = ast.parse(source)
    StarredUnpackingTransformer().visit(tree)
    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 02:20:04.957694
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    tree = ast.parse("""
foo(1, *range(2), 3, *range(4), 5)
""")
    tree=transformer.visit(tree)
    code = compile(tree, "<test>", "exec")

    assert 'foo(1, *(list(range(2)) + list(range(4)) + [3, 5]))' == ast.unparse(tree).strip()
    assert transformer.tree_changed



# Generated at 2022-06-14 02:20:18.085795
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    star = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:20:20.948541
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    assert isinstance(StarredUnpackingTransformer(), BaseNodeTransformer)

# Generated at 2022-06-14 02:20:28.481046
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .compiler_test_case import CompilerTestCase

    source = """
        print(*range(1), *range(3))
    """
    expected = """
        print(*(list(range(1)) + list(range(3))))
    """
    CompilerTestCase.compile(
        transformer=StarredUnpackingTransformer(),
        source=source,
        expected=expected)



# Generated at 2022-06-14 02:20:33.514470
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = 'foo([1, 2, *range(0, 10), 5])'
    expected = 'foo([1, 2] + list(range(0, 10)) + [5])'

    tree = ast.parse(source, mode='exec')
    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)
    assert transformer.is_changed() == True
    assert transformer.unparse(tree) == expected



# Generated at 2022-06-14 02:20:39.180533
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    prog = ast.parse("[2, *range(10), 1]")
    transformer = StarredUnpackingTransformer()
    result = transformer.visit(prog)
    assert transformer.tree_changed == True
    assert isinstance(result.body[0].value.value, ast.BinOp)



# Generated at 2022-06-14 02:20:40.798461
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    t = StarredUnpackingTransformer()
    assert t


# Generated at 2022-06-14 02:20:54.593006
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    result = transformer.visit(ast.parse("print(*range(3), *range(1))"))
    expected = ast.parse("print(*(list(range(3)) + list(range(1))))")
    assert ast.dump(result) == ast.dump(expected)



# Generated at 2022-06-14 02:21:08.102572
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .nodes import parse_ast

    import textwrap
    code = textwrap.dedent('''
    [2, *range(10), 1]
    ''').strip()
    ast_tree = parse_ast(code)
    result = StarredUnpackingTransformer().visit(ast_tree)

    assert result.body[0].value.left.left.n == 2
    assert result.body[0].value.left.right.func.id == 'list'
    assert result.body[0].value.left.right.args[0].value.func.id == 'range'
    assert result.body[0].value.left.right.args[0].value.args[0].n == 10
    assert result.body[0].value.left.right.args[0].value.args[1] is None


# Generated at 2022-06-14 02:21:16.993864
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    inp = ast.parse(textwrap.dedent('''
        print([1, 2, 3, *range(3)])
        print(1, 2, *range(4))
    '''))
    expected = ast.parse(textwrap.dedent('''
        print(*(([1, 2, 3] + list(range(3)))))
        print(*(([1, 2] + list(range(4)))))
    '''))

    assert expected.body == StarredUnpackingTransformer().visit(inp)



# Generated at 2022-06-14 02:21:31.715052
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    def compile_string(source) -> ast.AST:
        return compile(source, '<string>', 'exec', ast.PyCF_ONLY_AST)
    
    example_list_with_starred = '''
[2, *range(10), 1]
'''
    node = StarredUnpackingTransformer()(compile_string(example_list_with_starred))

# Generated at 2022-06-14 02:21:42.458550
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse("[2, *range(10), 1]")
    expected = ast.parse("[2] + list(range(10)) + [1]")
    transformer = StarredUnpackingTransformer('example/example1.py')
    result = transformer.visit(node)
    assert ast.dump(result) == ast.dump(expected)

    node = ast.parse("[*range(10)]")
    expected = ast.parse("list(range(10))")
    transformer = StarredUnpackingTransformer('example/example1.py')
    result = transformer.visit(node)
    assert ast.dump(result) == ast.dump(expected)

    node = ast.parse("[*range(10), 2]")
    expected = ast.parse("list(range(10)) + [2]")
   

# Generated at 2022-06-14 02:21:54.379189
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from typed_ast import ast3 as ast
    node = ast.parse("3")
    expected = ast.parse("3")
    assert expected == StarredUnpackingTransformer().visit(node)

    node = ast.parse("[2, *range(10), 1]")
    expected = ast.parse("[2] + list(range(10)) + [1]")
    assert expected == StarredUnpackingTransformer().visit(node)

    node = ast.parse("[[x] * [y] * [z] * 10]")
    expected = ast.parse("[[x] * [y] * [z] * 10]")
    assert expected == StarredUnpackingTransformer().visit(node)

    node = ast.parse("[[x] * [y] * [z]]")

# Generated at 2022-06-14 02:22:00.555895
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('print(*range(1), *range(3))')
    new_tree = StarredUnpackingTransformer().visit(tree)
    expected_tree = ast.parse('print(*(list(range(1)) + list(range(3))))')
    assert ast.dump(new_tree, include_attributes=False) == \
        ast.dump(expected_tree, include_attributes=False)


# Generated at 2022-06-14 02:22:05.201896
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    x = 1
    ast_tree = ast.parse("[2, *range(10), 1]")
    expected_ast_tree = ast.parse("[2] + list(range(10)) + [1]")
    assert StarredUnpackingTransformer().visit(ast_tree) == expected_ast_tree



# Generated at 2022-06-14 02:22:13.083036
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    old_node = ast.parse("[2, *range(10), 1]").body[0].value

    new_node = transformer.visit(old_node)
    assert isinstance(new_node, ast.BinOp)

    old_node = ast.parse("x[2, *range(10), 1]").body[0].value
    new_node = transformer.visit(old_node)
    assert isinstance(new_node, ast.Subscript)



# Generated at 2022-06-14 02:22:17.118917
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    with open('test/test_visit_List_input.py') as f:
        tree = ast.parse(f.read())
    expected = ast.parse('test/test_visit_List_expected.py')
    transformed = StarredUnpackingTransformer().visit(tree)
    assert transformed == expected.body[0].value



# Generated at 2022-06-14 02:22:31.547625
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast
    from .util import dump
    from .compat import ordered_dict

    code = "def f():\n    print(1, *(1, 2, 3), 4, 5, 6)\n"
    node = ast.parse(code)
    StarredUnpackingTransformer(node).visit(node)

# Generated at 2022-06-14 02:22:41.593516
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from six import StringIO as StringIO
    from typed_ast import parse
    from .base import BaseNodeTransformer

    # Simple test case
    # =======================
    code = 'print(*range(1), *range(3))'
    tree = parse(code)
    expected = "print(*(list(range(1)) + list(range(3))))"
    out = StringIO()
    BaseNodeTransformer.dump_code(expected, out)
    StarredUnpackingTransformer().visit(tree)
    actual = out.getvalue()
    assert expected == actual

    code = 'print(*range(1))'
    tree = parse(code)
    expected = "print(*(list(range(1))))"
    out = StringIO()
    BaseNodeTransformer.dump_code(expected, out)
    StarredUnpacking

# Generated at 2022-06-14 02:22:45.245159
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import parse

    code = """
print(*range(1), *range(3))
"""
    expected = """"""
    node = parse(code)
    transformer = StarredUnpackingTransformer()
    assert transformer.visit(node) == expected


# Generated at 2022-06-14 02:22:46.168686
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:22:53.030064
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Arrange
    input_tree = ast.parse('print(*range(1), *range(3))')
    expected_tree = ast.parse('print(*(list(range(1)) + list(range(3))))')

    # Act
    actual_tree = StarredUnpackingTransformer().visit(input_tree)

    # Assert
    assert ast.dump(actual_tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:22:58.974517
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('foo(3, *range(10), 1)')
    StarredUnpackingTransformer().visit(node)
    assert ast.dump(node) == ast.dump(ast.parse('foo(*(list(range(3)) + list(range(10)) + list(range(1))))'))

# Generated at 2022-06-14 02:23:11.277345
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astunparse
    from .transformer import TransformImports
    from .if_simplifier import IfSimplifier
    from .while_simplifier import WhileSimplifier
    from .attr_simplifier import AttrSimplifier
    from .isinstance_simplifier import IsInstanceSimplifier
    from .is_simplifier import IsSimplifier
    from .assert_simplifier import AssertSimplifier
    from .function_simplifier import FunctionSimplifier
    from .for_simplifier import ForSimplifier
    from .common import CommonNodeTransformer

    code = """
print(*range(1), *range(2))
    """
    expected = """
print(*(list(range(1)) + list(range(2))))
"""
    module = ast.parse(code)

# Generated at 2022-06-14 02:23:14.084347
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = 'print(*range(1), *range(3))'
    tree = ast.parse(code)
    expected = 'print(*(list(range(1)) + list(range(3))))'

    StarredUnpackingTransformer().visit(tree)

    assert astor.to_source(tree).strip() == expected


# Generated at 2022-06-14 02:23:27.517177
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    import inspect
    import dill

    tree = ast.parse("""
print(*[1, 2, 3], *[4, 5, 6])
    """)
    expected = """
print(*(([1, 2, 3] + [4, 5, 6])))
    """

    transformer = StarredUnpackingTransformer()
    tree = transformer.visit(tree)
    actual = astor.to_source(tree)
    assert expected == actual

    code = compile(tree, '<test>', 'exec')
    dill.loads(dill.dumps(code))
    func = dill.loads(dill.dumps(inspect.getsource(code)))

    # Check that it works
    func()


# Generated at 2022-06-14 02:23:37.132864
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast
    from .context import context

    src = ast.parse('foo(1, *range(3), 4)')
    tr = StarredUnpackingTransformer(context)
    tr.visit(src)

# Generated at 2022-06-14 02:23:48.259321
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    trans = StarredUnpackingTransformer()
    src = "def f(a, b, c): return a + b + c"
    a = ast.parse(src)
    # assign a to b (then a and b will point to the same object)
    b = a
    trans.visit(b)
    assert b is a
    assert ast.dump(b, include_attributes=True) == ast.dump(a, include_attributes=True)

# Generated at 2022-06-14 02:23:56.420920
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    node = ast.parse('''
x = [1, *range(3), 4, *range(5, 7), *range(8, 10)]
''')
    transformer.visit(node)
    print(ast.dump(node))

# Generated at 2022-06-14 02:24:03.625747
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    result = StarredUnpackingTransformer().visit(
        ast.parse(textwrap.dedent(r"""
            print(*list(range(1)))
        """)).body[0])

    assert isinstance(result, ast.Call)
    assert isinstance(result.args[0], ast.Starred)
    assert isinstance(result.args[0].value, ast.Call)
    assert isinstance(
        result.args[0].value.func,
        ast.Attribute)

# Generated at 2022-06-14 02:24:12.333956
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    try:
        # What happens if None is passed?
        a = StarredUnpackingTransformer(None)
    except Exception as e:
        print(e)
        print("These are the most common errors which can be fixed:\n1. Class attributes are not specified using 'self'\n2. Class attributes are not declared\n3. Class attribute name is used instead of Instance attribute name\n4. The Class attribute value is not used in the function body")
        assert False


# Generated at 2022-06-14 02:24:22.719458
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer().visit(ast.parse('[1, 2, 3]')) == ast.parse('[1, 2, 3]')
    assert StarredUnpackingTransformer().visit(ast.parse('[*[1,2,3], 4]')) == ast.parse('[1, 2, 3, 4]')
    assert StarredUnpackingTransformer().visit(ast.parse('[1, *[2,3], 4]')) == ast.parse('[1, 2, 3, 4]')
    assert StarredUnpackingTransformer().visit(ast.parse('[1, 2, *[3,4], 5]')) == ast.parse('[1, 2, 3, 4, 5]')

# Generated at 2022-06-14 02:24:30.722075
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    source = """
        a = [2, *range(10), 1]
        b = [2, range(10), 1]
    """
    expected = """
        a = [2] + list(range(10)) + [1]
        b = [2, range(10), 1]
    """
    tree = ast.parse(source)
    t = StarredUnpackingTransformer()
    t.visit(tree)
    assert astor.to_source(tree) == expected


# Generated at 2022-06-14 02:24:32.531551
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    class_object = StarredUnpackingTransformer()
    assert isinstance(class_object, StarredUnpackingTransformer)

# Generated at 2022-06-14 02:24:40.626831
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = "[2, *range(10), 1]"

    expected_ast = ast.Module(
        body=[ast.Expr(value=ast.BinOp(
            left=ast.List(elts=[
                ast.Num(n=2),
                ast.Call(
                    func=ast.Name(id='list'),
                    args=[
                        ast.Call(
                            func=ast.Name(id='range'),
                            args=[
                                ast.Num(n=10)],
                            keywords=[])],
                    keywords=[])]),
            right=ast.List(elts=[ast.Num(n=1)]),
            op=ast.Add()))])

    actual_ast = compile_to_ast(code)

    StarredUnpackingTransformer().generic_visit(actual_ast)
    assert_asts

# Generated at 2022-06-14 02:24:46.310466
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = 'print(*range(1), *range(3))'
    tree = ast.parse(source)
    StarredUnpackingTransformer().visit(tree)
    expected = 'print(*(list(range(1)) + list(range(3))))'
    assert ast.dump(tree) == ast.dump(ast.parse(expected))


# Generated at 2022-06-14 02:24:52.955932
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # Input
    node = ast.parse("[2, *range(5), *range(1), 1]").body[0].value
    # Expected output
    expected = ast.parse("[2] + list(range(5)) + list(range(1)) + [1]").body[0].value

    transformer = StarredUnpackingTransformer()
    actual = transformer.visit(node)
    assert ast.dump(expected) == ast.dump(actual)


# Generated at 2022-06-14 02:25:12.656537
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse("[2, *range(10), 1]")
    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)
    assert transformer._tree_changed == True
    assert ast.dump(tree) == "Module(body=[Expr(value=BinOp(left=List(elts=[Num(n=2)]), op=Add(), right=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Num(n=10), Num(n=1)], keywords=[])], keywords=[])))])"


# Generated at 2022-06-14 02:25:23.260919
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from . import NodeTransformerTestCase
    from . import check_transformer

    class Test(NodeTransformerTestCase):
        transform = StarredUnpackingTransformer

        def test_list_1(self):
            lst = self.transform(self.parse_expr('[2, *range(1), *range(3), 1]'))
            self.assertEqual(lst, self.parse_expr('[2] + list(range(1)) + list(range(3)) + [1]'))

        def test_call_1(self):
            call = self.transform(self.parse_expr('print(*range(1), *range(3))'))
            self.assertEqual(call, self.parse_expr('print(*(list(range(1)) + list(range(3))))'))


# Generated at 2022-06-14 02:25:32.212441
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source_code = 'x = [2, *range(10), 1]'
    tree = ast.parse(source_code)
    transformer = StarredUnpackingTransformer(tree)
    transpiled = transformer.visit(tree)

    expected_code = 'x = [2] + list(range(10)) + [1]'
    expected_tree = ast.parse(expected_code)

    assert ast.dump(transpiled) == ast.dump(expected_tree)


# Generated at 2022-06-14 02:25:43.664397
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_programs = {
        # Before
        "[2, *range(10), 1]":
        # After
        "[2] + list(range(10)) + [1]",

        "[1, *[*[1, 2], *[3, 4]], 5]":
        "[1] + list(list(list([1, 2]) + list([3, 4]))) + [5]",

        "[1, *[1, *[2, *[3, 4]]], 5]":
        "[1] + list([1] + list([2] + list([3, 4]))) + [5]"
    }
    for before, after in test_programs.items():
        module = ast.parse(before, "test.py")
        transformer = StarredUnpackingTransformer(module)
        transformed = ast.fix

# Generated at 2022-06-14 02:25:54.878241
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from .base import TestTransformer

    call_test_str = "print(*range(1), *range(3))"

    # Tests for cases when the method visit_Call does not make any changes

# Generated at 2022-06-14 02:26:07.675352
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    # set up a compiler
    from hpc.autoscript.compile.compiler import _Compiler
    compiler = _Compiler()
    compiler.ast_transformers.append(StarredUnpackingTransformer)

    # a function
    code = '''def f():
        return [1, 2, 3]
    '''
    node = compiler._parse(code)
    # compile the function
    compiled = compiler._ast2obj(node)

    # set up a new compiler
    compiler1 = _Compiler()
    compiler1.ast_transformers.append(StarredUnpackingTransformer)

    # compile the function
    compiled1 = compiler1._ast2obj(node)
    # assert
    assert compiled1.__code__.co_code == compiled.__code__.co_code




# Generated at 2022-06-14 02:26:16.210666
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import astor
    from .base import TestCase

    class StarredUnpackingTransformerTest(TestCase):
        TRANSFORMER = StarredUnpackingTransformer
        TEST_FILE = __file__

        def test_starred_in_list(self):
            self.assert_rewrite(
                'foo = [1, 2, *range(3)]',
                'foo = [1, 2] + list(range(3))'
            )

        def test_starred_in_list_of_calls(self):
            self.assert_rewrite(
                'foo([1, 2, *range(3)])',
                'foo(list([1, 2]) + list(range(3)))'
            )


# Generated at 2022-06-14 02:26:26.514399
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from unittest.mock import MagicMock
    from ...transpilers.Javascript import JsTranspiler
    from ...abc import Tree
    from ...visitors import NodeCloner

    class Transpiler(JsTranspiler):
        def __init__(self, tree):
            super().__init__(tree)
            self._visitor.ast_transformer = [StarredUnpackingTransformer]

        def visit_List(self, node: ast.List) -> str:
            return 'list'

        def visit_Call(self, node: ast.Call) -> str:
            return 'call'

        def visit_Starred(self, node: ast.Starred) -> str:
            return '*'

        def visit_Name(self, node: ast.Name) -> str:
            return node.id


# Generated at 2022-06-14 02:26:38.265531
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import ast3 as ast, parse

    node = parse('''[2, *range(10), 1]''').body[0]

# Generated at 2022-06-14 02:26:45.994672
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    expected_ast = ast.parse("print(*((list(range(1)) + list(range(3)))))")
    code = "print(*range(1), *range(3))"
    expected_code = "print(*((list(range(1)) + list(range(3)))))".replace(" ", "").replace("\n", "")

    tree = ast.parse(code)
    transformer = StarredUnpackingTransformer()
    new_tree = transformer.visit(tree)
    transformer.generic_visit(new_tree)  # type: ignore
    assert transformer._tree_changed  # nosec
    code_after_transformation = unparse(new_tree).replace(" ", "").replace("\n", "")
    assert code_after_transformation == expected_code  # nosec