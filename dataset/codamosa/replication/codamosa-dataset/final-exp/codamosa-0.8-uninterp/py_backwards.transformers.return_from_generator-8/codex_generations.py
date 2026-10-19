

# Generated at 2022-06-14 02:06:10.046783
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("""
        def fn():
            yield 1
            return 5
    """)
    expected_node = ast.parse("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)

    ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(node) == ast.dump(expected_node)


# Generated at 2022-06-14 02:06:18.054153
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
        def fn():
            yield 1
            return 5
        for x in fn():
            pass
    """
    expected_code = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        for x in fn():
            pass
    """
    tree = ast.parse(code)
    transformer = ReturnFromGeneratorTransformer()
    tree = transformer.visit(tree)
    assert ast.dump(tree) == expected_code

# Generated at 2022-06-14 02:06:19.350364
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import typed_astunparse
    import astor


# Generated at 2022-06-14 02:06:28.488796
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source import source_to_ast
    from ..utils.compare import compare_ast
    from ..utils.transformers_utils import PrintNodeTransformer, FunctionDefNodeTransformer
    from ..utils.visitor import NodeVisitor
    from ..utils.compile_to_ast import compile_body

    class Visitor(NodeVisitor):
        def __init__(self, source):
            self.source = source
            self.returns = []
            self.has_yield = False
            self.names = []

        def generic_visit(self, node):
            self.names = []
            if isinstance(node, (ast.Yield, ast.YieldFrom, ast.Return)):
                for d in node._fields:
                    if hasattr(node, d):
                        self.names.append(d)

# Generated at 2022-06-14 02:06:33.906031
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    fn = ast.parse("""
    def fn():
        yield 1
        return 5
    """).body[0]
    expected = ast.parse("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """).body[0]
    actual = transformer.visit(fn)
    assert actual == expected

# Generated at 2022-06-14 02:06:46.442779
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from astor.dump_tree import dump_tree
    from . import unpythonize_str
    unpythonize_str(dump_tree(ReturnFromGeneratorTransformer().visit(ast.parse(
        """def fn():
            yield 1
            return 5""")))) == """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc"""


# Generated at 2022-06-14 02:06:48.053950
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import get_ast, compare_asts


# Generated at 2022-06-14 02:06:50.813319
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from ..utils import get_ast
    from ..utils.transformers import get_transformer


# Generated at 2022-06-14 02:06:57.865686
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    inp = '''
            def fn():
                yield 1
                return 5
                '''
    expected_output = '''
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
                '''
    tree = ast.parse(inp)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    assert ast.dump(tree) == ast.dump(ast.parse(expected_output))


# Generated at 2022-06-14 02:07:00.241614
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_helpers import assert_transformed_code_is

# Generated at 2022-06-14 02:07:09.703762
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    func_def_code = 'def fn():\n' \
                    '    yield 1\n' \
                    '    return 5\n'
    func_def_ast = ast.parse(func_def_code)
    func_def = func_def_ast.body[0]
    assert isinstance(func_def, ast.FunctionDef)

    ReturnFromGeneratorTransformer().visit(func_def_ast)

    assert func_def_ast.body[0].body[-1].value.func.id == 'raise'
    assert func_def_ast.body[0].body[-1].value.func.value.id == 'StopIteration'
    assert func_def_ast.body[0].body[-1].value.func.value.value.id == 'exc'

# Generated at 2022-06-14 02:07:18.459510
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """
    Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer.
    """
    code = """
    def fn():
        yield 1
        return 5
    """
    expected = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    tree = ast.parse(code)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)
    assert astor.to_source(tree).strip() == expected.strip()

# Generated at 2022-06-14 02:07:27.089140
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .codegen.ReturnFromGeneratorTransformer import ReturnFromGeneratorTransformerTestCase
    ReturnFromGeneratorTransformerTestCase("test_original_generator").runTest()
    ReturnFromGeneratorTransformerTestCase("test_return_not_last").runTest()
    ReturnFromGeneratorTransformerTestCase("test_return_last").runTest()
    ReturnFromGeneratorTransformerTestCase("test_return_last_after_yield").runTest()
    ReturnFromGeneratorTransformerTestCase("test_return_last_after_yield_function").runTest()
    ReturnFromGeneratorTransformerTestCase("test_return_last_after_yield_function_for").runTest()
    ReturnFromGeneratorTransformerTestCase("test_return_last_after_yield_function_with").runTest()
    ReturnFromGener

# Generated at 2022-06-14 02:07:28.233792
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:38.416352
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source_code = '''
    def f():
        yield 1
        return 1
    '''
    expected_code = '''
    def f():
        yield 1
        exc = StopIteration()
        exc.value = 1
        raise exc
    '''
    expected_ast = ast.parse(expected_code)
    transformer = ReturnFromGeneratorTransformer()
    source_ast = ast.parse(source_code)
    actual_ast = transformer.visit(source_ast)
    assert ast.dump(actual_ast) == ast.dump(expected_ast)


# Generated at 2022-06-14 02:07:52.306322
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # ARRANGE #
    from typed_ast import ast3 as ast
    from .non_local_transformer import NonLocalTransformer
    from .generator_transformer import GeneratorTransformer
    ast_data = ast.parse('''
        def fn():
            def inner(x):
                return x + 1
            yield fn()
            return 5
    ''')
    transformer1 = NonLocalTransformer()
    transformer2 = GeneratorTransformer()
    transformer3 = ReturnFromGeneratorTransformer()

    # ACT #
    transformer1.visit(ast_data)
    transformer2.visit(ast_data)
    transformer3.visit(ast_data)

    # ASSERT #
    import typed_astunparse

# Generated at 2022-06-14 02:08:03.666780
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import generate_transformer_test
    from testing.utils import source

    @generate_transformer_test(ReturnFromGeneratorTransformer)
    def test_method():
        def fn():
            yield 1
            return 6

        fn()

    @generate_transformer_test(ReturnFromGeneratorTransformer)
    def test_method_multiple_returns():
        def fn():
            yield 1
            yield 2
            return 6

        fn()

    @generate_transformer_test(ReturnFromGeneratorTransformer)
    def test_method_no_returns():
        def fn():
            yield 1

        for x in fn():
            print(x)


# Generated at 2022-06-14 02:08:09.107831
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    example = """def fn(x):
    for i in range(x):
        yield i
    return i
for i in fn(5):
    print(i)"""

    expected = """def fn(x):
    for i in range(x):
        yield i

    exc = StopIteration()
    exc.value = i
    raise exc

for i in fn(5):
    print(i)"""
    assert ReturnFromGeneratorTransformer().transform_source(example) == expected

# Generated at 2022-06-14 02:08:16.066806
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import unittest
    import unittest.mock

    transformer = ReturnFromGeneratorTransformer()

    # 1) No `return`
    node = ast.parse('def foo():\n\tpass\n')
    foo = node.body[0]
    expected = foo
    result = transformer.visit_FunctionDef(foo)
    assert result == expected

    # 1) No `yield`
    node = ast.parse('def foo():\n\tdef bar():\n\t\treturn\n')
    foo = node.body[0]
    bar = foo.body[0]
    expected = foo
    result = transformer.visit_FunctionDef(foo)
    assert result == expected

    # 3) `return` in `yield` generator

# Generated at 2022-06-14 02:08:18.598562
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        yield 1
        return 5


# Generated at 2022-06-14 02:08:34.518908
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class test:
        def fn():
            yield 1
            return 5

    node = ast.parse(textwrap.dedent(inspect.getsource(test.fn))).body[0]
    out = ReturnFromGeneratorTransformer().visit(node)

    class test:
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc

    expected = ast.parse(textwrap.dedent(inspect.getsource(test.fn))).body[0]

    assert ast.dump(out) == ast.dump(expected)

# Generated at 2022-06-14 02:08:39.394740
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .fixtures.fn_return_from_generator import fn_before
    from .fixtures.fn_return_from_generator import fn_after
    before = ast.parse(fn_before)
    after = ast.parse(fn_after)
    ReturnFromGeneratorTransformer().visit(before)
    assert before == after

# Generated at 2022-06-14 02:08:46.010214
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse

    source_code = '''
    def generator(a, *b, c: int):
        name = c
        yield "hello world"
        return 100
    '''
    node = ast.parse(source_code)
    ReturnFromGeneratorTransformer().visit(node)
    expected_node = ast.parse('''
    def generator(a, *b, c: int):
        name = c
        yield "hello world"
        exc = StopIteration()
        exc.value = 100
        raise exc
    ''')
    assert unparse(node) == unparse(expected_node)

# Generated at 2022-06-14 02:08:59.812553
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import assert_transformation
    from .test_utils import assert_source_equal

    assert_source_equal(
        """
        def generator():
            yield 1
            return '2'
        """,
        """
        def generator():
            yield 1
            exc = StopIteration()
            exc.value = '2'
            raise exc
        """
    )

    assert_source_equal(
        """
        def gen():
            if True:
                return 5
            yield 1
            return 2
        """,
        """
        def gen():

            if True:
                exc = StopIteration()
                exc.value = 5
                raise exc

            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
        """
    )


# Generated at 2022-06-14 02:09:09.261121
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from . import parse
    from .test_let import LetTransformer
    from .test_yield import YieldTransformer

    code = """
    def foo():
        yield 1
        return 5
    """
    expected_code = """
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    tree = parse(code)
    ReturnFromGeneratorTransformer(tree).visit(tree)
    YieldTransformer(tree).visit(tree)
    LetTransformer(tree).visit(tree)
    assert expected_code == ast.unparse(tree)

# Generated at 2022-06-14 02:09:20.836496
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    instance = ReturnFromGeneratorTransformer()

    def check(i, result):
        assert instance.visit(ast.parse(i)) == ast.parse(result)

    # no modifications
    check("def fn():\n    return", "def fn():\n    return")
    # yield and return
    check("def fn():\n    yield\n    return 123",
          "def fn():\n    exc = StopIteration()\n    exc.value = 123\n    raise exc\n    yield")
    # yield and return in try/except
    check("def fn():\n    try:\n        yield\n    except:\n        return 123",
          "def fn():\n    try:\n        yield\n    except:\n        exc = StopIteration()\n        exc.value = 123\n        raise exc")


# Generated at 2022-06-14 02:09:26.872197
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    from typed_astunparse import unparse
    from astunparse import unparse as astunparse
    from .base import BaseNodeTransformer

    # Generate source code from AST

# Generated at 2022-06-14 02:09:27.596816
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:43.096252
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    ast_tree = ast.parse(
        """
        def fn():
            yield 1
            return 5
        """
    )
    ReturnFromGeneratorTransformer().visit(ast_tree)

# Generated at 2022-06-14 02:09:57.472174
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    # test_return_empty
    def test_return_empty():
        def fn():
            yield 1

        assert not ReturnFromGeneratorTransformer.run(fn.__code__)

    # test_return_simple
    def test_return_simple():
        def test_return_simple():
            yield 1
            return 5

        assert ReturnFromGeneratorTransformer.run(test_return_simple.__code__)

    # test_return_nested
    def test_return_nested():
        def test_return_nested():
            def fn2():
                return 'not for real'

            assert fn2() == 'not for real'

            yield 1
            return 5

        assert ReturnFromGeneratorTransformer.run(test_return_nested.__code__)

    test_return_empty()
    test_return

# Generated at 2022-06-14 02:10:20.003163
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("def fn():\n\tyield 1\n\treturn 5\n")
    assert ast.dump(node, include_attributes=True) == "Module(body=[FunctionDef(body=[Expr(value=Yield(value=Num(n=1))), Return(value=Num(n=5))], decorator_list=[], name='fn', returns=None, type_comment=None)])"
    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(node)

# Generated at 2022-06-14 02:10:29.835884
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def testcase(node: ast.FunctionDef, expected):
        actual_ast = ReturnFromGeneratorTransformer().visit(node)
        actual = ast.dump(actual_ast)
        expected = ast.dump(expected)
        assert actual == expected

    # empty function
    fn = ast.parse('def fn(): pass').body[0]
    testcase(fn, fn)

    # function with return
    fn = ast.parse('def fn(): return 5').body[0]
    testcase(fn, fn)

    # function with different yields and returns

# Generated at 2022-06-14 02:10:42.677621
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Test(ast.AST):
        _fields = ("body",)
        _attributes = ("lineno",)

    class Test2(ast.AST):
        _fields = ("body",)
        _attributes = ("lineno",)

    class Test3(ast.AST):
        _fields = ("elts",)
        _attributes = ("lineno",)

    class Test4(ast.AST):
        _fields = ("value",)
        _attributes = ("lineno",)


    class Test6(ast.AST):
        _fields = ("value",)
        _attributes = ("lineno",)

    class Test7(ast.AST):
        _fields = ("value", "name")
        _attributes = ("lineno",)


# Generated at 2022-06-14 02:10:51.891207
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testutils import assert_equal_source

    generator_function = ast.FunctionDef(name='fn',
        body=[ast.Yield(value=ast.Num(n=1)),
            ast.Return(value=ast.Num(n=5))],
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), decorator_list=[], returns=None)


# Generated at 2022-06-14 02:10:53.735456
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_helpers import assert_transformation_result


# Generated at 2022-06-14 02:11:04.572409
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_base import compile_to_ast, compare_ast
    source = '''
        def fn():
            yield 1
            return 5
    '''
    expected = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''
    module = compile_to_ast(source, '<test>')
    node = module.body[0]
    assert isinstance(node, ast.FunctionDef)
    result = ReturnFromGeneratorTransformer().visit(node)
    assert result is not None
    compare_ast(result, expected)

    source = '''
        def fn():
            for x in lst:
                yield x
    '''

# Generated at 2022-06-14 02:11:18.145375
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    fn_ast = ast.parse(textwrap.dedent("""
    def fn():
        yield 1
        return 5
    """)).body[0]
    assert isinstance(fn_ast, ast.FunctionDef)

    transformer = ReturnFromGeneratorTransformer()
    new_fn_ast = transformer.visit(fn_ast)

    assert isinstance(new_fn_ast, ast.FunctionDef)
    assert new_fn_ast.body[0].names[0].name == 'exc'
    assert new_fn_ast.body[1].value.func.id == 'StopIteration'
    assert new_fn_ast.body[2].targets[0].id == 'exc'
    assert new_fn_ast.body[3].value.func.id == 'exc'

# Generated at 2022-06-14 02:11:24.227801
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def get_ast(src):
        return ast.parse(src)

    def check_source_equal(src1, src2):
        expected = get_ast(src2)
        actual = get_ast(src1)
        assert ast.dump(expected) == ast.dump(actual)

    def check_transformation_equal(src1, src2):
        expected = get_ast(src2)
        actual = get_ast(src1)
        t = ReturnFromGeneratorTransformer()
        t.visit(actual)
        assert ast.dump(expected) == ast.dump(actual)


# Generated at 2022-06-14 02:11:26.855309
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import expect_same

    # with return

# Generated at 2022-06-14 02:11:38.555781
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class PreTransformation(ast.AST):
        _fields = ('body',)
        _attributes = ('lineno', 'col_offset')
        _ast_fields = ('args', 'body', 'decorator_list', 'col_offset', 'lineno', 'name', 'returns')
    class PostTransformation(ast.AST):
        _fields = ('body',)
        _attributes = ('lineno', 'col_offset')
        _ast_fields = ('args', 'body', 'decorator_list', 'col_offset', 'lineno', 'name', 'returns')

    class PreTransformationStmt(ast.AST):
        _fields = ('body',)
        _attributes = ('lineno', 'col_offset')
        _ast_fields = ()

# Generated at 2022-06-14 02:12:11.381374
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    
    class ReturnFromGeneratorTransformer(BaseNodeTransformer):
        """Compiles return in generators like:
            def fn():
                yield 1
                return 5
        To:
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
        """
        target = (3, 2)
    
        def _find_generator_returns(self, node: ast.FunctionDef) -> List[Tuple[ast.stmt, ast.Return]]:
            """Using bfs find all `return` statements in function."""
            to_check = [(node, x) for x in node.body]  # type: ignore
            returns = []
            has_yield = False

# Generated at 2022-06-14 02:12:15.596279
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # type: () -> None
    """
    Test method visit_FunctionDef of class ReturnFromGeneratorTransformer.
    """
    from ..utils.testing import assert_code_equal, assert_tree_equal


# Generated at 2022-06-14 02:12:20.590263
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse(
        """
        def fn():
            yield 1
            return 5
        """)
    node = ReturnFromGeneratorTransformer().visit(node)
    assert node.body[0].body[1].value.func.value.id == "StopIteration"



# Generated at 2022-06-14 02:12:27.179505
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from blake.blake_utils import load_ast

    s = """
    def f():
        yield 1
        return 2
    """

    node = load_ast(s)
    t = ReturnFromGeneratorTransformer()
    out = t.visit(node)

    s2 = """
    def f():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """

    expect = load_ast(s2)
    assert t._tree_changed
    assert out.body[0] == expect.body[0]


# Generated at 2022-06-14 02:12:40.084586
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from . import process_ast
    import ast

    class ReturnFromGeneratorTransformerTester(ReturnFromGeneratorTransformer):
        def __init__(self):
            self.generic_visit = super().generic_visit

    code = \
    '''
    def foo():
        yield 1
        return 6
    '''
    expected = \
    '''
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 6
        raise exc
    '''
    node = ast.parse(code)
    ReturnFromGeneratorTransformerTester().visit(node)
    actual = process_ast(node)
    print(actual)
    assert actual == expected

    code = \
    '''
    def foo():
        yield 1
        return
    '''

# Generated at 2022-06-14 02:12:49.569118
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent
    from ..parser import parse_ast
    from ..codecompass.utils import CodeCompassVisitor

    input_code = dedent(
        """\
        def method():
            yield 1
            yield 2
            return 3
        """
    )
    expected_code = dedent(
        """\
        def method():
            yield 1
            yield 2
            exc = StopIteration()
            exc.value = 3
            raise exc
        """
    )

    tree = parse_ast(input_code)

    visitor = ReturnFromGeneratorTransformer()
    CodeCompassVisitor().visit(tree)

    assert tree.body[0]



# Generated at 2022-06-14 02:12:59.393145
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import transform

    src = """
    def foo():
        yield from bar()
        yield from bar()
        return 5
    """
    module = transform(src, ReturnFromGeneratorTransformer)
    assert module.body[0].body[2].value.name == 'StopIteration'
    assert module.body[0].body[3].value.value.value == 5
    assert module.body[0].body[4].value.value.value == 'foo'
    assert module.body[0].body[5].value.value == 4

    src = """
    def bar():
        yield 1
        return 5
    """
    module = transform(src, ReturnFromGeneratorTransformer)
    assert module.body[0].body[2].value.name == 'StopIteration'
    assert module.body[0].body

# Generated at 2022-06-14 02:13:07.968166
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    import ast

    source = """
    def foo():
      yield 1
      return 2
    """
    expected = """
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """
    module_ast = ast.parse(source)
    for node in ReturnFromGeneratorTransformer().visit(module_ast).body:
        assert unparse(node) == expected

# Generated at 2022-06-14 02:13:18.603426
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_helpers import get_visitor_output

    with let(module) as ast.Module:
        module = ast.Module([
            ast.FunctionDef(
                "fn",
                ast.arguments(
                    [],
                    None,
                    None,
                    [],
                    []),
                [
                    ast.Expr(
                        ast.Yield(
                            ast.Constant(1))),
                    ast.Return(
                        ast.Constant(2))],
                [],
                None)])

        visitor = ReturnFromGeneratorTransformer()
        visitor.visit(module)


# Generated at 2022-06-14 02:13:25.571181
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    fn = 'def fn():\n    if False:\n        pass\n    return 5\n'
    new_fn = 'def fn():\n    if False:\n        pass\n' \
             '    exc = StopIteration()\n    exc.value = 5\n    raise exc\n'
    assert ReturnFromGeneratorTransformer._replace_return(fn) == new_fn


# Generated at 2022-06-14 02:14:16.021866
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:14:22.942394
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ...tests.testing_utils import assert_code_equal

    code_in = """
    def fn():
        yield 1
        return 10
    """

    code_out = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 10
        raise exc
    """

    node = ast.parse(code_in)
    node = ReturnFromGeneratorTransformer().visit(node)

    assert_code_equal(code_out, node)

# Generated at 2022-06-14 02:14:31.482974
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..compiler import compile_src
    import pytest

    code = '''
    def fn():
        yield 1
        return 5
    '''

    @compile_src(code, transforms=[ReturnFromGeneratorTransformer])
    def fn():
        pass

    with pytest.raises(StopIteration) as exc_info:
        for _ in fn():
            pass
    assert exc_info.value.value == 5


# Generated at 2022-06-14 02:14:42.804170
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..transformer import transform
    from inspect import cleandoc

    source = cleandoc(
        """
        def fn():
            yield 1
            return 2
    """
    )
    node = ast.parse(source)
    transform(node)

# Generated at 2022-06-14 02:14:51.734750
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import inspect
    from typed_ast.ast3 import parse
    node = parse(inspect.getsource(test_ReturnFromGeneratorTransformer_visit_FunctionDef))
    node = node.body[0]

    assert(isinstance(node, ast.FunctionDef) and node.name == 'test_ReturnFromGeneratorTransformer_visit_FunctionDef')
    copy = ReturnFromGeneratorTransformer().visit(  # type: ignore
        copy.deepcopy(node))  # type: ignore
    assert(ReturnFromGeneratorTransformer().visit(node) == copy)  # type: ignore
    print(copy)

# Generated at 2022-06-14 02:15:01.534272
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    src = '''
    def fn():
        yield 1
        return 5
    '''
    module = ast.parse(src)
    transformer = ReturnFromGeneratorTransformer()
    node = transformer.visit(module)
    assert transformer._tree_changed
    expected_module = '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''
    expected_module = ast.parse(expected_module)
    assert ast.dump(node) == ast.dump(expected_module)

# Generated at 2022-06-14 02:15:10.757540
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # type: () -> None
    def fn():
        # type: () -> int
        yield 1
        yield 2
        return 5

    node = ast.parse(inspect.getsource(fn))
    node = ReturnFromGeneratorTransformer().visit(node)
    ns = {}
    exec(compile(node, '<ast>', 'exec'), ns)
    generator = ns['fn']()
    assert next(generator) == 1
    assert next(generator) == 2
    with pytest.raises(StopIteration):
        next(generator)

# Generated at 2022-06-14 02:15:17.233918
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(source: str, expected: str) -> None:
        tree = ast.parse(source)
        transformer = ReturnFromGeneratorTransformer()
        new_tree = transformer.visit(tree)
        result = compiler.ast.to_source(new_tree, indent_with=' ' * 4)
        assert result.strip() == expected.strip()


# Generated at 2022-06-14 02:15:23.661440
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = '''
    def fn():
        yield 1
        return 5
    '''
    tree = ast.parse(code)
    node = tree.body[0]
    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(node)
    assert transformer._tree_changed is True
    assert result.body[0].value.value == 1
    assert result.body[1].value.value == 5

# Generated at 2022-06-14 02:15:32.407474
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def run_test(input_source, expected_source):
        result = ReturnFromGeneratorTransformer().visit_FunctionDef(ast.parse(input_source).body[0])
        assert result == ast.parse(expected_source)
    run_test('\n'.join([
        'def func():',
        '    yield 10',
        '    return 20',
        ]), '\n'.join([
        'def func():',
        '    yield 10',
        '    exc = StopIteration()',
        '    exc.value = 20',
        '    raise exc',
        ]))