

# Generated at 2022-06-14 02:17:17.441278
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    class MyTransformer(StarredUnpackingTransformer):
        def __init__(self):
            super(MyTransformer, self).__init__()
            self.call_count = 0

        def generic_visit(self, node: ast.AST) -> ast.AST:
            self.call_count += 1
            return super(MyTransformer, self).generic_visit(node)

    for test_code in (
"""
l = [1, 2, *range(3), 4]
""",
"""
l = [1, 2, *range(3), 4, 5, 6, 7, 8]
""",
"""
l = [1, 2, *range(3)]
"""):
        a = ast.parse(test_code)
        MyTransformer().visit(a)
        assert MyTransformer().call_

# Generated at 2022-06-14 02:17:31.847704
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Given
    class_ = StarredUnpackingTransformer()
    node_ = ast.parse("print(*range(1), *range(3))")
    args = node_.body[0].value.args

    # When
    actual = class_.visit(args)
    # Then

# Generated at 2022-06-14 02:17:37.733044
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node_list = ast.parse('[2, *range(10), 1]').body[0].value
    expected_node_list = ast.parse('[2] + list(range(10)) + [1]').body[0].value
    transformer = StarredUnpackingTransformer()
    transformer.visit(node_list)
    assert expected_node_list == transformer.result


# Generated at 2022-06-14 02:17:46.552492
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = """[2, *range(10), 1]"""
    expected_code = """[2] + list(range(10)) + [1]"""
    module_node = ast.parse(code)
    StarredUnpackingTransformer().visit(module_node)
    actual_code = compile(module_node, '', 'exec')
    exec(actual_code)
    my_list = ast.parse(expected_code).body[0].value
    expected_code = compile(my_list, '', 'exec')
    exec(expected_code)
    assert actual_code == expected_code

# Generated at 2022-06-14 02:17:55.364634
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """
    Checks if StarredUnpackingTransformer.visit_Call works properly.
    Returns:
        True: if two given nodes are equal.
        False: otherwise.

    """
    node1 = ast.Call(
        func=ast.Name(id='sum'),
        args=[
            ast.Starred(
                value=ast.List(
                    elts=[
                        ast.List(
                            elts=[ast.Num(n=1)],
                            ctx=ast.Load()),
                        ast.List(
                            elts=[ast.Num(n=2)],
                            ctx=ast.Load())
                    ],
                    ctx=ast.Load())
            ),
            ast.Num(n=3)
        ],
        keywords=[])

# Generated at 2022-06-14 02:18:06.800221
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    t = StarredUnpackingTransformer()
    node = ast.parse("print(*range(1), *range(3))")
    node = t.visit(node)
    assert ast.dump(node) == "Module([Call(Name('print', Load()), [Starred(Call(Name('list', Load()), [Call(Name('range', Load()), [Num(1)], [], None, None)], [], None, None), Starred(Call(Name('list', Load()), [Call(Name('range', Load()), [Num(3)], [], None, None)], [], None, None)], [], None, None)], [])])"

# Generated at 2022-06-14 02:18:15.567386
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.List(elts=[ast.Num(n=2), ast.Starred(value=ast.Call(func=ast.Name(id='range'),
        args=[ast.Num(n=10)], keywords=[]), ctx=ast.Load()), ast.Num(n=1)])

# Generated at 2022-06-14 02:18:25.194351
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse("[*print() for _ in range(1)]")
    sut = StarredUnpackingTransformer()
    sut.visit(node)
    assert type(node.body[0].value) == ast.Call
    assert node.body[0].value.func.id == "list"
    assert type(node.body[0].value.args[0]) == ast.Starred
    assert type(node.body[0].value.args[0].value) == ast.Call


# Generated at 2022-06-14 02:18:32.677659
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    r = StarredUnpackingTransformer()
    node = ast.Call(
        func=ast.Name(id='print'),
        args=[ast.Name(id='*range(1)')],
        keywords=[])
    node = r.visit(node)
    assert isinstance(node, ast.Call)
    assert isinstance(node.args[0], ast.Starred)
    assert isinstance(node.args[0].value, ast.Call)
    assert isinstance(node.args[0].value.func, ast.Name)
    assert node.args[0].value.func.id == 'list'
    assert isinstance(node.args[0].value.args[0], ast.Name)
    assert node.args[0].value.args[0].id == 'range(1)'


# Generated at 2022-06-14 02:18:44.075036
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    node = ast.parse('[*range(10)]').body[0].value
    result = transformer.visit(node)
    assert ast.dump(result) == 'Call(func=Name(id="list", ctx=Load()), args=[Starred(value=Name(id="range", ctx=Load()), ctx=Load())], keywords=[])'

    node = ast.parse('[2, *range(10), 1]').body[0].value
    result = transformer.visit(node)

# Generated at 2022-06-14 02:19:03.226286
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    for i in range(1, 8):
        for j in range(1, 8):
            x = "print(*range(%s), *range(%s))" % (i, j)
            tree = ast.parse(x)
            assert tree.body and isinstance(tree.body[0], ast.Expr)
            StarredUnpackingTransformer().visit(tree)
            expected = "print(*(list(range(%s)) + list(range(%s))))" % (i, j)
            assert ast_to_code(tree) == expected


# Generated at 2022-06-14 02:19:08.173635
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = "[2, *range(10), 1]"
    expected = "[2] + list(range(10)) + [1]"
    result = StarredUnpackingTransformer().transform_code(code)
    assert result == expected



# Generated at 2022-06-14 02:19:15.968433
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from test.base import create_tree

    tree = create_tree(
        "[2, *range(10), 1]",
        "print(*range(1), *range(3))",
        version=(3, 7))
    result = StarredUnpackingTransformer()(tree)

    assert result == create_tree(
        "[2] + list(range(10)) + [1]",
        "print(*(list(range(1)) + list(range(3))))",
        version=(3, 7))

# Generated at 2022-06-14 02:19:20.452202
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    lines = [
        "print(*[1, 2, 3], *[4, 5, 6])",
    ]
    expected = [
        "print(*(([1, 2, 3]) + ([4, 5, 6])))",
    ]
    assert get_expected(StarredUnpackingTransformer, lines, expected) == expected



# Generated at 2022-06-14 02:19:28.748220
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .abstract_visitor import AbstractVisitor
    from .base import BaseNodeTransformer

    class Visitor(AbstractVisitor, StarredUnpackingTransformer):
        pass
    source = ast.parse("print(*range(1), *range(3))")
    visitor = Visitor()
    visitor.visit(source)

    expected_source = ast.parse(
        "print(*(list(range(1)) + list(range(3))))")

    assert ast.dump(source) == ast.dump(expected_source)


# Generated at 2022-06-14 02:19:37.915145
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    assert astor.to_source(StarredUnpackingTransformer().visit(ast.parse("""
    print(*range(1), *range(3))
    """).body[0])) == "print(*(list(range(1)) + list(range(3))))"
    assert astor.to_source(StarredUnpackingTransformer().visit(ast.parse("""
    print(*range(1), *range(3), b=1)
    """).body[0])) == "print(*(list(range(1)) + list(range(3))), b=1)"

# Generated at 2022-06-14 02:19:46.844426
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .ast_helpers import assert_matches_ast
    from typed_ast.ast3 import parse

    tree = parse(
        "[2, *range(10), 1]\n" +
        "print(*range(1), *range(3))\n"
    ).body

    expected = parse(
        "[2] + list(range(10)) + [1]\n" +
        "print(*(list(range(1)) + list(range(3))))\n"
    ).body

    assert_matches_ast(StarredUnpackingTransformer().visit(tree), [expected[0]])
    assert_matches_ast(StarredUnpackingTransformer().visit(tree), [expected[1]])

# Generated at 2022-06-14 02:19:52.215240
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast
    import typed_astunparse
    # Source code:
    # print(*range(1))
    node = ast.Call(
        func = ast.Name(id = "print"),
        args = [ast.Starred(value = ast.Call(
            func = ast.Name(id = "range"),
            args = [ast.Num(n = 1),],
            keywords = [],
        ),)],
        keywords = [],
    )

    # Compare
    node = StarredUnpackingTransformer().visit(node)
    assert typed_astunparse.dump(node) == "print(*(list(range(1))))"


# Generated at 2022-06-14 02:19:55.172191
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import BaseTester

    BaseTester.test_visit_of_class(StarredUnpackingTransformer, 'Call')


# Generated at 2022-06-14 02:20:03.452798
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Unit test for method visit_Call of class StarredUnpackingTransformer."""
    code = """
        print(*range(1), *range(3))"""
    ctx = compile(code, '<file>', 'exec', flags=0,
                  dont_inherit=True, optimize=-1)
    node = ast.parse(code)
    StarredUnpackingTransformer().visit(node)
    mod = type(ctx.getroot()).from_ast(node)
    exec(mod)


# Generated at 2022-06-14 02:20:23.756079
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer.__name__ == 'StarredUnpackingTransformer'
    assert StarredUnpackingTransformer.__doc__ == 'Compiles:\n        [2, *range(10), 1]\n        print(*range(1), *range(3))\n    To:\n        [2] + list(range(10)) + [1]\n        print(*(list(range(1)) + list(range(3))))\n        \n    '
    assert StarredUnpackingTransformer.target == (3, 4)

if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-14 02:20:30.437998
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    source = "[2, *range(10), 1]"
    target = "[2] + list(range(10)) + [1]"
    result = transformer.visit(ast.parse(source))
    expected = ast.parse(target)

    assert ast.dump(result) == ast.dump(expected)


# Generated at 2022-06-14 02:20:37.333636
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Test for bug https://github.com/serge-sans-paille/python-modernize/issues/29
    node = ast.parse('print(*range(10), sep=" ")')
    node_transformed = StarredUnpackingTransformer()
    node_transformed.visit(node)
    new_node_str = ast.unparse(node)
    expected_code = 'print(*(list(range(10))), sep=" ")\n'
    assert new_node_str == expected_code

# Generated at 2022-06-14 02:20:45.702272
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # https://docs.python.org/3/library/ast.html#abstract-grammar
    # Call(expr func, expr* args, keyword* keywords)

    tree_src = ast.parse("""\
print(*range(1), *range(3))
""")
    tree_dst = ast.parse("""\
print(*(list(range(1)) + list(range(3))))
""")
    transformer = StarredUnpackingTransformer()
    tree = transformer.visit(tree_src)
    assert tree == tree_dst


# Generated at 2022-06-14 02:20:52.487295
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_helpers import get_ast, assert_source
    source = 'print(*range(1), *range(3))'
    node = get_ast(source).body[0]
    expected = 'print(*(list(range(1)) + list(range(3))))'
    result = StarredUnpackingTransformer().visit(node)
    assert_source(expected, result)


# Generated at 2022-06-14 02:20:57.950674
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import inspect
    body = inspect.cleandoc('''
    print(*range(1), *range(3))
    a = [2, *range(10), 1]
    ''')
    t = StarredUnpackingTransformer()
    new_tree = t.visit(ast.parse(body))
    exec(compile(new_tree, '', 'exec'))
    assert a == [2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]


# Generated at 2022-06-14 02:21:09.209666
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from compile.loader import load_module
    from compile.loader.errors import LoadError
    from .utils import convert, dump
    source = '''
    def foo(x):
        pass

    foo(*range(10), *range(20))
    '''
    expected = '''
    def foo(x):
        pass
    foo(*(list(range(10)) + list(range(20))))
    '''

    module, _ = load_module(source)
    assert module is not None

    tr = StarredUnpackingTransformer()
    convert(tr, module)
    assert tr._tree_changed

    dumped = dump(module)
    assert dumped.strip() == expected.strip()


# Generated at 2022-06-14 02:21:17.085735
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Unit test for method visit_Call of class StarredUnpackingTransformer"""

    tree = ast.parse('print(*[0, *range(1), 2])')
    expected = ast.parse('print(*([0] + list(range(1)) + [2]))')

    StarredUnpackingTransformer().visit(tree)
    
    assert ast.dump(tree) == ast.dump(expected)
    

# Generated at 2022-06-14 02:21:29.495092
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from inspect import cleandoc

    def extract(src: str, target: int) -> str:
        module = ast.parse(cleandoc(src))
        StarredUnpackingTransformer().visit(module)
        return module.body[target].value.args[0].value.left.func.id

    node = extract('''
    class A:
        def __init__(self, test, *args, **kwargs):
            self.test, *_ = args
    A(0, *[1, 2, 3])
    ''', 1)
    assert node == 'list'

# Generated at 2022-06-14 02:21:40.591311
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('print(*range(5), 3, 4, *range(10))')
    StarredUnpackingTransformer.run_test(tree)
    ret = repr(tree)

# Generated at 2022-06-14 02:21:57.201241
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Description:
    Testing of visit_List method when
    there is no starred unpacking.
    """
    from .. import TranspileError

    SAMPLE_CODE = """[2, 3, 4]"""
    EXPECTED_OUTPUT = SAMPLE_CODE

    transformer = StarredUnpackingTransformer()
    try:
        actual_result = transformer.visit(ast.parse(SAMPLE_CODE))
    except TranspileError:
        actual_result = None
    assert str(actual_result) == EXPECTED_OUTPUT


# Generated at 2022-06-14 02:22:07.360313
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse('[2, *range(10), 1]', mode='eval')

    result = StarredUnpackingTransformer().visit(tree)

    expected = ast.List(
        elts=[
            ast.Num(n=2),
            ast.Call(
                func=ast.Name(id='list'),
                args=[
                    ast.Call(
                        func=ast.Name(id='range'),
                        args=[
                            ast.Num(n=10)
                        ],
                        keywords=[]
                    )
                ],
                keywords=[]
            ),
            ast.Num(n=1)
        ],
        ctx=ast.Load()
    )

    assert ast.dump(result, include_attributes=False) == ast.dump(
        expected, include_attributes=False)


# Unit

# Generated at 2022-06-14 02:22:17.662773
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from ..ast_transforms import StarredUnpackingTransformer
    import typing
    import ast
    expected_result = '\n'.join([
        "import typing",
        "",
        "",
        "def f(*args: typing.Tuple[int, ...]) -> None:",
        "    print(*args)",
        ""
    ])
    input_source = '\n'.join([
        "import typing",
        "",
        "",
        "def f(*args: typing.Tuple[int, ...]) -> None:",
        "    print(*list(range(1)),*list(range(3)))",
        ""
    ])
    input_ast = typing.cast(ast.FunctionDef, ast.parse(input_source).body[0])

# Generated at 2022-06-14 02:22:23.500464
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    code = 'print(*range(2), 3, *range(5))'
    expected = 'print(*(list(range(2)) + [3] + list(range(5))))'
    assert expected == astor.to_source(StarredUnpackingTransformer().visit(ast.parse(code))).strip()


# Generated at 2022-06-14 02:22:28.528271
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import BaseNodeTransformerTest
    from .test_helpers import assert_source_equal

    source = """\
    print(*range(10), *range(10))
    """
    expected = """\
    print(*(list(range(10)) + list(range(10))))
    """

    BaseNodeTransformerTest.test_visit(StarredUnpackingTransformer, source, expected, assert_source_equal)


# Generated at 2022-06-14 02:22:39.410190
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .. import compile_to_ast
    from . import AstTypeAssertion
    
    code = '[2, *range(10), 1]'
    
    ast_tree = compile_to_ast(code)
    ast_tree = AstTypeAssertion.parse(ast_tree)
    
    transformer = StarredUnpackingTransformer()
    result = transformer.visit(ast_tree)
    result = AstTypeAssertion.parse(result)
    

# Generated at 2022-06-14 02:22:43.869187
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse("[2, *range(10), 1]")
    StarredUnpackingTransformer.run_on_tree(tree, 4)
    expected = ast.parse("(2 + list(range(10)) + 1)")
    assert ast.dump(tree) == ast.dump(expected)


# Generated at 2022-06-14 02:22:51.680998
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Test if method visit_List in class StarredUnpackingTransformer works correctly."""
    input_list = [
        ast.List(elts=[ast.Num(n=1),
                       ast.Starred(value=ast.Name(id='range', ctx=ast.Load()), ctx=ast.Load()),
                       ast.Num(n=2)], ctx=ast.Load()),
        ast.List(elts=[ast.Num(n=1), ast.Num(n=2)], ctx=ast.Load())
    ]

# Generated at 2022-06-14 02:23:02.155918
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from ..tests.transformer_test_case import TransformerTestCase
    from ..transformer_module import TransformerModule
    from ..transformer_module_parametrized import TransformerModuleParametrized
    from ..utils import get_ast3 as get_ast
    
    # test case
    # [2, *range(10), 1]
    source = get_ast('''
        [2, *range(10), 1]
    ''')
    
    # expected result
    expected_tree = get_ast('''
        [2] + list(range(10)) + [1]
    ''')
    
    # create instance of a class and setting a new tree
    test_case = TransformerTestCase()
    test_case.test_target = StarredUnpackingTransformer
    test_case.test

# Generated at 2022-06-14 02:23:08.293944
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    src = 'range(0, *(1, 2, 3))'
    expected = 'range(0, *list((1,) + (2,) + (3,)))'
    tree = ast.parse(src)
    sut = StarredUnpackingTransformer()
    sut.visit(tree)
    assert astunparse.unparse(tree) == expected


# Generated at 2022-06-14 02:23:43.459673
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    trans = StarredUnpackingTransformer()
    node = ast.Call(func=ast.Name(id='F'), args=[ast.Num(1), ast.Starred(value=ast.Name(id='a'))])
    transformed = trans.visit(node)
    assert transformed == ast.Call(func=ast.Name(id='F'), args=[ast.Starred(value=ast.List(elts=[ast.Num(1)]),
                                                                              ctx=ast.Load()),
                                                                ast.Starred(value=ast.Call(func=ast.Name(id='list'),
                                                                                          args=[ast.Name(id='a')],
                                                                                          keywords=[]))])



# Generated at 2022-06-14 02:23:48.962535
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    callnode = translator.ast_from_code('print(*range(1), *range(3))')
    transformer = StarredUnpackingTransformer()
    new_node = transformer.visit(callnode)
    code = translator.unparse(new_node)
    assert code == "print(*(list(range(1)) + list(range(3))))"


# Generated at 2022-06-14 02:24:01.032574
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert StarredUnpackingTransformer().visit(ast.parse('[2, 3, 4]')).body[0].value.elts == [2, 3, 4]
    assert StarredUnpackingTransformer().visit(ast.parse('[2, *range(10), 4]')).body[0] == ast.parse('[2] + list(range(10)) + [4]')
    assert StarredUnpackingTransformer().visit(ast.parse('[2, *range(10), *range(3), 4]')).body[0] == ast.parse('[2] + list(range(10)) + list(range(3)) + [4]')
    assert StarredUnpackingTransformer().visit(ast.parse('[2, *range(10), *range(3), *range(3), 4]')).body

# Generated at 2022-06-14 02:24:06.627343
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    test_code = '''def do_list():
        print(*range(1), *range(3))
    '''
    node = ast.parse(test_code)
    transformer = StarredUnpackingTransformer()
    transformer.visit(node)
    compiled_code = compile(node, '<string>', 'exec')
    ns = {}
    exec(compiled_code, ns)
    ns['do_list']()


# Generated at 2022-06-14 02:24:10.453360
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    input = """
    def func(a, b):
        print(a, b)
    
    func(1, *range(5))
    """

# Generated at 2022-06-14 02:24:20.429432
# Unit test for method visit_List of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:24:31.903335
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = 'print(2, *range(3), 1)'
    tree = ast.parse(code)
    StarredUnpackingTransformer.run_visitor(tree)
    assert ast.dump(tree) == 'Expr(value=Call(func=Name(id=\'print\', ctx=Load()), args=[Starred(value=BinOp(left=BinOp(left=List(elts=[Num(n=2)]), right=Call(func=Name(id=\'list\', ctx=Load()), args=[Call(func=Name(id=\'range\', ctx=Load()), args=[Num(n=3)], keywords=[])], keywords=[])), right=List(elts=[Num(n=1)]), op=Add()))], keywords=[]))\n'


# Generated at 2022-06-14 02:24:38.826045
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse(
        'func(1, 2, 3, 4, 5, *[6, 7], 8, 9, 10, *range(1,11), 11, 12)'
    ).body[0].value
    expected = ast.parse(
        'func(*(list(range(1, 11)) + list([6, 7]) + [8, 9, 10, 11, 12]))'
    ).body[0].value
    actual = StarredUnpackingTransformer().visit(node)
    assert ast.dump(expected) == ast.dump(actual)

# Generated at 2022-06-14 02:24:41.184505
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    global StarredUnpackingTransformer
    StarredUnpackingTransformer()
    assert True


# Generated at 2022-06-14 02:24:45.459005
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse('[2, *range(10), 1]')
    result = StarredUnpackingTransformer().visit(tree)==ast.parse('[2] + list(range(10)) + [1]')
    assert result


# Generated at 2022-06-14 02:25:43.665341
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('print(*range(10), *range(20))').body[0]
    assert isinstance(node, ast.Expr) and isinstance(node.value, ast.Call), "Invalid test case"
    assert node.value.args == [ast.Starred(value=ast.Name(id='range', ctx=ast.Load()), ctx=ast.Load()),
                               ast.Starred(value=ast.Name(id='range', ctx=ast.Load()), ctx=ast.Load())], "Invalid test case"

    result = StarredUnpackingTransformer().visit(copy.copy(node))

# Generated at 2022-06-14 02:25:45.175669
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer()

# Generated at 2022-06-14 02:25:52.190133
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .utils import assert_ast_nodes_equal
    from .rewriter_test_helper import assert_code_equal
    code = """
    print(1,2,4,5,*range(10))
    """
    expected_code = """
    print(*(list([1,2,4,5])+list(range(10))))
    """
    assert_code_equal(
        expected_code,
        StarredUnpackingTransformer().visit(
            ast.parse(code)))

# Generated at 2022-06-14 02:25:58.863268
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    my_code = """print("hello", "world", *range(10), "hello")"""
    print("my_code is :", my_code)
    root = ast.parse(my_code)
    StarredUnpackingTransformer().visit(root)
    print("transform is :", ast.dump(root))
    

# Generated at 2022-06-14 02:26:10.360265
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import pprint
    from typed_ast import ast3 as ast
    from algoliasearch_django.transpiler import StarredUnpackingTransformer
    from algoliasearch_django.transpiler.helpers import dump_code, get_ast

    code = 'assert f(*[1, 2, 3], 5, *[1, 2, 5, 7], g(3))'
    node = get_ast(code)
    StarredUnpackingTransformer().visit(node)
    print(dump_code(node))
    assert dump_code(node) == dump_code(get_ast('assert f(*(list([1, 2, 3]) + list([5]) + list([1, 2, 5, 7]) + list([g(3)])),)'))


# Generated at 2022-06-14 02:26:21.635328
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from uncompyle6.parser import PythonParserSingle
    from uncompyle6.parsers.astnode import ASTCodeGenerator
    parser = PythonParserSingle()
    node = parser.parse_string('''
        print(*range(1), *range(3))
    ''')
    obj = StarredUnpackingTransformer()
    obj.visit(node)
    obj.generic_visit(node)
    result = ASTCodeGenerator(None, False).visit(node)
    with open('test_StarredUnpackingTransformer_visit_Call.out', 'w') as f:
        f.write(result)
    obj.print_tree(node)


# Generated at 2022-06-14 02:26:30.045716
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():

    node0 = ast.List(elts=[])
    node1 = ast.List(elts=[ast.Starred(value=ast.Name(id='a'), ctx=ast.Load())])
    node2 = ast.List(elts=[ast.Name(id='b', ctx=ast.Load())])
    node3 = ast.List(elts=[ast.Starred(value=ast.Name(id='a'), ctx=ast.Load()), ast.Starred(value=ast.Name(id='b'), ctx=ast.Load())])

# Generated at 2022-06-14 02:26:35.694324
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = "[2, *range(10), 1]"
    node = ast.parse(code)

    expected_code = "[2] + list(range(10)) + [1]"
    expected_node = ast.parse(expected_code)

    StarredUnpackingTransformer().visit(node)
    assert(compare_ast(node, expected_node))



# Generated at 2022-06-14 02:26:40.933814
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = '[2, *range(10), 1]'
    expected = '[2] + list(range(10)) + [1]'

    tree = ast.parse(source)
    transformer = StarredUnpackingTransformer()
    new_tree = transformer.visit(tree)

    compiled = compile(new_tree, '', 'eval')
    assert eval(compiled) == eval(expected)


# Generated at 2022-06-14 02:26:53.438127
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():

    class StarredUnpackingTransformer(BaseNodeTransformer):
        """Compiles:
            [2, *range(10), 1]
            print(*range(1), *range(3))
        To:
            [2] + list(range(10)) + [1]
            print(*(list(range(1)) + list(range(3))))
            
        """
        target = (3, 4)

        def _has_starred(self, xs: List[ast.expr]) -> bool:
            for x in xs:
                if isinstance(x, ast.Starred):
                    return True

            return False

        def _split_by_starred(self, xs: Iterable[ast.expr]) -> List[Splitted]:
            """Split `xs` to separate list by Starred."""
            lists = [[]]