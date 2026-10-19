

# Generated at 2022-06-14 02:06:02.496038
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:04.461073
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from . import sample_python, get_ast


# Generated at 2022-06-14 02:06:14.543084
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .return_from_generator import ReturnFromGeneratorTransformer
    import astunparse, ast

# Generated at 2022-06-14 02:06:15.389646
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:16.465850
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:26.763971
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import FunctionDef, Return, Name, Load, Yield, Expr
    from .base import create_ir_and_transform
    from .base import FunctionDef as IRFunctionDef
    from .base import Return as IRReturn
    from .base import Name as IRName
    from .base import Load as IRLoad
    from .base import Yield as IRYield
    from .base import Raise as IRRaise
    from .base import Assign as IRAssign
    from .base import Attribute as IRAttribute
    from .base import Call as IRCall
    from .base import LoadStore as IRLoadStore
    from .base import LoadLoad as IRLoadLoad
    from .base import StoreLoad as IRStoreLoad
    from .base import NameConstant as IRNameConstant


# Generated at 2022-06-14 02:06:37.282931
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Arrange
    code = """
        def generator():
            yield 1
            return
    """
    expected_code = """
        def generator():
            yield 1
            exc = StopIteration()
            raise exc
    """
    expected_ast = ast.parse(expected_code)

    # Act
    tree = ast.parse(code)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)
    actual_ast = tree

    # Assert
    assert ast.dump(actual_ast) == ast.dump(expected_ast)



# Generated at 2022-06-14 02:06:43.592877
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    func = ast.parse("""def fn():\n  yield 1\n  return 5\n""", mode="exec")
    assert ReturnFromGeneratorTransformer().visit(func) == ast.parse("""def fn():\n  yield 1\n  exc = StopIteration()\n  exc.value = 5\n  raise exc\n""", mode="exec")


# Generated at 2022-06-14 02:06:49.414120
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..testing.utils import build_and_run

    @snippet
    def before():
        def fn():
            yield 1
            return 5

    @snippet
    def after():
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc

    src = before.getsource()
    expected_src = after.getsource()
    result_src, _, _ = build_and_run(src, ReturnFromGeneratorTransformer)
    assert result_src == expected_src



# Generated at 2022-06-14 02:06:59.285778
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test 1: Empty body and generator
    node = ast.parse('def f():\n    pass')
    transformer = ReturnFromGeneratorTransformer(None)
    ast.fix_missing_locations(node)
    transformer.visit(node)
    assert ast.dump(node) == 'def f():\n    pass'

    # Test 2: Empty body and not generator
    node = ast.parse('def f():\n    pass\n    yield 1')
    transformer = ReturnFromGeneratorTransformer(None)
    ast.fix_missing_locations(node)
    transformer.visit(node)
    assert ast.dump(node) == 'def f():\n    pass\n    yield 1'


# Generated at 2022-06-14 02:07:09.804215
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import assert_program

    @snippet
    def test_gen():
        yield 1
        return 2

    @snippet
    def test_gen_both():
        yield 1
        try:
            raise AssertionError
        except AssertionError:
            pass
        return 2

    @snippet
    def test_gen_both_nested():
        yield 1
        try:
            raise AssertionError
        except AssertionError:
            try:
                raise AssertionError
            except AssertionError:
                pass
        return 2

    @snippet
    def test_gen_nested():
        yield 1
        try:
            raise AssertionError
        except AssertionError:
            pass
        return 2


# Generated at 2022-06-14 02:07:18.054239
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Setup
    node = ast.parse(
        """
        def fn():
            yield 1
            return 5
        """
    )
    expected_node = ast.parse(
        """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """
    )

    # Run
    node = ReturnFromGeneratorTransformer().visit(node)

    # Assert
    assert ast.dump(node) == ast.dump(expected_node)

# Generated at 2022-06-14 02:07:20.108567
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # type: () -> None
    def test_1():
        def fn():
            yield 1
            return 5

# Generated at 2022-06-14 02:07:26.864850
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    generator_return = ast.Return(value=ast.Constant(5))
    method_def = ast.FunctionDef(name='fn', body=[ast.Yield(value=ast.Constant(0)), generator_return])

# Generated at 2022-06-14 02:07:27.678180
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert False

# Generated at 2022-06-14 02:07:39.241105
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    assert astor.to_source(ast.parse(test_ReturnFromGeneratorTransformer_visit_FunctionDef.__doc__)) == astor.to_source(ast.parse(test_ReturnFromGeneratorTransformer_visit_FunctionDef.__annotations__['return']))

test_ReturnFromGeneratorTransformer_visit_FunctionDef.__doc__ = \
'''def fn():
    yield 1
    return 5'''

test_ReturnFromGeneratorTransformer_visit_FunctionDef.__annotations__ = {'return': '''def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc'''}

# Generated at 2022-06-14 02:07:44.777399
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def run(s_old, s_new):
        node_old = ast.parse(s_old)
        node_new = ast.parse(s_new)

        transformer = ReturnFromGeneratorTransformer()
        node_result = transformer.visit(node_old)

        assert ast.dump(node_result) == ast.dump(node_new)

    # Test function without generator

# Generated at 2022-06-14 02:07:51.027042
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .transpile_function import assert_function_transpile
    from mixt import Mixt

    def foo():
        yield 1
        return 2

    def foo_expected():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc

    assert_function_transpile(Mixt(ReturnFromGeneratorTransformer), foo, foo_expected)



# Generated at 2022-06-14 02:07:59.819355
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def run_test(function_def_input, function_def_expected, *_):
        class _MockVisitor(ast.NodeVisitor):
            def __init__(self):
                self.body = ast.parse(function_def_input).body

            def visit_FunctionDef(self, node):
                return node
        node = ast.parse(function_def_input).body[0]
        v = _MockVisitor()
        transformer = ReturnFromGeneratorTransformer()
        assert (ast.dump(transformer.visit(v.visit_FunctionDef(node))) ==
                ast.dump(ast.parse(function_def_expected).body[0]))


# Generated at 2022-06-14 02:08:06.348719
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_visitor import assert_visitor

    tree = ast.parse("""
    def _do(self):
        try:
            self.seq.__next__()
        except StopIteration as e:
            return _mock_curve(e.value)
    """)

    assert_visitor(tree, ReturnFromGeneratorTransformer)

# Generated at 2022-06-14 02:08:28.446826
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import Transformer
    code_to_test = '''
    def generator():
        yield 1
        return 5

    def normal():
        return 5

    def useless():
        yield 1
        yield 2
    '''

# Generated at 2022-06-14 02:08:36.552615
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..context import Context
    import astor

    source = """
    def fn():
        yield 1
        return 5
    """
    tree = ast.parse(textwrap.dedent(source))
    fn = tree.body[0]
    expected = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    tree.body[0] = ReturnFromGeneratorTransformer(Context()).visit(fn)
    actual = astor.to_source(tree)
    assert actual == textwrap.dedent(expected)

# Generated at 2022-06-14 02:08:43.591265
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    snippet_initial = """
        def fn():
            yield 1
            return 5
    """
    snippet_transformed = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    ast_initial = ast.parse(snippet_initial)
    ast_transformed = ast.parse(snippet_transformed)
    transformer = ReturnFromGeneratorTransformer()
    actual_output = transformer.visit(ast_initial)
    assert astor.to_source(actual_output) == astor.to_source(ast_transformed)



# Generated at 2022-06-14 02:08:55.908511
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test 1
    x = ast.parse("""def f():
    yield 1
    return 5""")
    trans = ReturnFromGeneratorTransformer()
    trans.visit(x)
    assert ast.dump(x) == """def f():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc"""

    # Test 2
    x = ast.parse("""def f():
    return 5""")
    trans = ReturnFromGeneratorTransformer()
    trans.visit(x)
    assert ast.dump(x) == """def f():
    return 5"""

    # Test 3
    x = ast.parse("""def f():
    yield 1
    return""")
    trans = ReturnFromGeneratorTransformer()
    trans.visit(x)

# Generated at 2022-06-14 02:09:02.480573
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from typed_ast import ast3
    class Test:
        @staticmethod
        def test_transform_source(func_source, target_source):
            node = ast.parse(func_source)
            ReturnFromGeneratorTransformer().visit(node)
            assert astor.to_source(node).strip() == target_source
    # end class Test


# Generated at 2022-06-14 02:09:04.235382
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:15.229912
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def run_test(code, transformed_code):
        tree = ast.parse(code)
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(tree)
        result = astor.to_source(tree)
        assert result == transformed_code

    def fn1():
        yield 1
        return 3

    def fn2():
        yield 1
        return

    def fn3():
        a = 1
        return a

    def fn4():
        yield 1
        a = 1
        return a

    def fn5():
        return 3


# Generated at 2022-06-14 02:09:18.892399
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("def fn():\n    yield 1\n    return 5")
    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(node)
    assert(ast.dump(ast.parse("def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise e")) == ast.dump(result))

# Generated at 2022-06-14 02:09:32.138392
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.context import Context
    from ..utils.source import Source
    from ..utils.error import CompilerError

    # Setup
    context = Context()
    source = Source('<string>', """
        def fn():
            yield 1
            return 5
    """)
    source.ast = ast.parse(source.text)

    # Test
    ReturnFromGeneratorTransformer(context).visit(source.ast)
    assert context.errors == []

# Generated at 2022-06-14 02:09:43.974856
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class MyVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef):
            self.functionDef = node

    expected_str = """def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc"""

    # Scenario 1 - Test the input
    input_str = """def fn():
            yield 1
            return 5"""
    tree_input = ast.parse(input_str)
    visitor = MyVisitor()
    visitor.visit(tree_input)
    actual_input = ast.dump(visitor.functionDef)

    # Scenario 2 - Test the output
    expected_tree = ast.parse(expected_str)
    transformer = ReturnFromGeneratorTransformer()
    visitor = MyVisitor()

# Generated at 2022-06-14 02:10:07.939583
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Given
    transformer = ReturnFromGeneratorTransformer()
    @let(f_)
    def f_():
        yield 1
        return 2 + 3
    @let(f_expected_)
    def f_expected_():
        yield 1
        exc = StopIteration()
        exc.value = 2 + 3
        raise exc

    # When
    module = ast.Module([f_.node])
    transformed_module = transformer.visit(module)  # type: ignore
    transformed_function = transformed_module.body[0]
    expected_function = f_expected_.node  # type: ignore

    # Then
    assert transformer._tree_changed is True
    assert transformed_function == expected_function

# Generated at 2022-06-14 02:10:13.726518
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
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
    assert expected.strip() == ReturnFromGeneratorTransformer(code).get_tree().strip()



# Generated at 2022-06-14 02:10:26.504612
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(code: str, expected: str) -> None:
        module = ast.parse(return_from_generator.get_snippet())
        module.body.pop()  # remove `return_from_generator` FunctionDef node
        module.body.append(ast.parse(code))
        module.body[0].body[0].decorator_list.pop()  # remove `@snippet` decorator
        ReturnFromGeneratorTransformer().visit(module)
        assert ast.dump(module) == expected


# Generated at 2022-06-14 02:10:35.983812
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3, parse
    from .base import BaseNodeTransformerTestCase
    from .base import transform
    from ..utils import a, b, c, d, e


# Generated at 2022-06-14 02:10:48.517235
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
        def some_generator():
            yield 1
            return 5
    """
    expected = """
        def some_generator():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    transformer_class = ReturnFromGeneratorTransformer()
    transformer_class._tree_changed = False

    module = ast.parse(code)
    transformer_class.visit(module)
    assert transformer_class._tree_changed

    expected_module = ast.parse(expected)
    assert ast.dump(module) == ast.dump(expected_module)


# Generated at 2022-06-14 02:10:59.655583
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformerTestCase
    from ..utils import python_to_python_ast

    class ReturnFromGeneratorTransformerTestCase(BaseNodeTransformerTestCase):
        def test_return_from_generator(self):
            transformer = ReturnFromGeneratorTransformer()
            source = """
            def fn(n):
                yield n
                return n
                """
            expected_ast = python_to_python_ast(source)
            fn = expected_ast.body[0]
            ast.fix_missing_locations(fn)

            transformer.visit(expected_ast)
            self.assertEqual(expected_ast, transformer.visit(python_to_python_ast(source)))

    ReturnFromGeneratorTransformerTestCase.run()

# Generated at 2022-06-14 02:11:10.550385
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class DummyNode(ast.AST):
        _fields = []
    class MockNode(ast.AST):
        def __init__(self, body, value = None):
            self.body = body
            self.value = value
        _fields = ['body', 'value']
    class DummyFunctionDef(ast.AST):
        _fields = ['body']
    class DummyReturn(ast.AST):
        _fields = ['value']
    def create_dummy_node(node_type, body, value = None):
        if node_type == 'stmt':
            return DummyNode()
        elif node_type == 'return':
            return MockNode(body, value)
        elif node_type == 'FunctionDef':
            if body is None:
                body = []
            return DummyFunctionDef(body)


# Generated at 2022-06-14 02:11:21.803987
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    child = ast.FunctionDef(name="child", args=ast.arguments(args=[], vararg=None, kwarg=None, defaults=[]),
                            body=[ast.Return(value=ast.Constant(value=42, kind=None))], decorator_list=[], returns=None)
    gen_fn = ast.FunctionDef(name="fn", args=ast.arguments(args=[], vararg=None, kwarg=None, defaults=[]),
                             body=[ast.Yield(value=ast.Constant(value=1, kind=None)),
                                   ast.Return(value=ast.Constant(value=5, kind=None)),
                                   child], decorator_list=[], returns=None)

# Generated at 2022-06-14 02:11:29.963241
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    t = ReturnFromGeneratorTransformer()
    test_ast = ast.parse("""
    def fn():
        yield 1
        return 2
    """)

    final_ast = ast.parse("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """)

    t.visit(test_ast)

    assert ast.dump(final_ast) == ast.dump(test_ast)


# Generated at 2022-06-14 02:11:35.290199
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
    def generator():
        if True:
            yield 1

        if True:
            return 5
    """
    assert ReturnFromGeneratorTransformer().visit(ast.parse(code)) == ast.parse("""
    def generator():
        if True:
            yield 1

        if True:
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)

# Generated at 2022-06-14 02:12:08.648158
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testing_utils import normalize_code
    from ..utils.code_gen import code_gen

    from .v import V

    input_code = '''
    def fn():
        yield 1
        return 5
    '''

    actual_ast, = ReturnFromGeneratorTransformer().run(input_code)
    expected_code = normalize_code('''
    def fn():
        yield 1
        _ = StopIteration()
        _.value = 5
        raise _
    ''')
    actual_code = normalize_code(code_gen(actual_ast))

    # ast.dump(actual_ast)
    # print(ast.dump(expected_ast))

    assert actual_code == expected_code

    actual_code = V.as_python_code(actual_ast)
    expected_

# Generated at 2022-06-14 02:12:14.958452
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import compile_source

    source = """
    def fn():
        yield 1
        return 5
    """

    transformer = ReturnFromGeneratorTransformer()
    tree = compile_source(source, mode='exec')
    transformer.visit(tree)

    expected = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 02:12:16.507572
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    ts = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:12:24.071977
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = '''def f():
    yield 1
    return 5
    '''
    expected = ast.parse('def f():\n    '
                         'yield 1\n    '
                         'exc = StopIteration()\n    '
                         'exc.value = 5\n    '
                         'raise exc')
    tree = ast.parse(source)
    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(tree)
    assert result == expected


# Generated at 2022-06-14 02:12:32.785007
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    klass = ReturnFromGeneratorTransformer()
    node = ast.parse(
        dedent('''
        def fn(a):
            yield 1
            return a
        ''')).body[0]
    result = klass.generic_visit(node)  # type: ignore

    expected = ast.parse(
        dedent('''
        def fn(a):
            yield 1
            exc = StopIteration()
            exc.value = a
            raise exc
        '''))

    assert ast.dump(result) == ast.dump(expected)

# Generated at 2022-06-14 02:12:39.286639
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source_code = """
    def f():
        return 1

    def f():
        return 1
    """
    expected_code = """
    def f():
        return 1

    def f():
        return 1
    """
    assert ReturnFromGeneratorTransformer().visit(ast.parse(source_code)) == ast.parse(expected_code)



# Generated at 2022-06-14 02:12:50.810136
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    @snippet
    def fn():
        yield 1

    @snippet
    def fn2():
        yield 1
        return 1

    @snippet
    def fn3():
        yield 1
        return


# Generated at 2022-06-14 02:12:51.516161
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:01.041931
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""def fn():
                        yield 1
                        return 5
                        """)
    transformer = ReturnFromGeneratorTransformer()
    new_tree = transformer.visit(tree)

# Generated at 2022-06-14 02:13:12.909592
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from .base import TestCase

    def generator():
        yield 1
        return 5  # pragma: python2

    code = '\n'.join(["def generator():",
                      "    yield 1",
                      "    return 5",
                      "",
                      "for x in generator():",
                      "    print(x)",
                      ""])
    generator_def = astor.code_to_ast(code)
    node_transformer = ReturnFromGeneratorTransformer()
    transformed_generator_def = node_transformer.visit(generator_def)

# Generated at 2022-06-14 02:13:58.359577
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.ast_helpers import assert_source


# Generated at 2022-06-14 02:14:07.400567
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .function import FunctionDefTransformer
    from .decorator import DecoratorTransformer
    from .class_ import ClassDefTransformer
    from .callback import CallbackTransformer

    src = """
    @callback
    def a():
        pass

    def b():
        yield 1
        return 1

    def c():
        def d():
            def e():
                def f():
                    yield 1
                    return 1
                return f()
            return e()
        return d()


    @callback
    class A:
        def b(self):
            yield 1
            return 1
    """

# Generated at 2022-06-14 02:14:18.797956
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformer
    from .codegen import compile_code

    code = """
        def fn():
            yield 1
            return 5
    """
    BaseNodeTransformer.clear_caches()
    root = compile_code(code, 3)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(root)
    fn = root.body[0]
    assert isinstance(fn, ast.FunctionDef)
    assert isinstance(fn.body[2], ast.Return)
    assert len(fn.body) == 3

# Generated at 2022-06-14 02:14:31.811542
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # ARRANGE
    function_def = ast.parse('''
        def fn():
            yield 1
            return 5
    ''').body[0]
    class_def = ast.parse('''
        class Cls:
            def fn():
                yield 1
                return 5
    ''').body[0]
    class_inherit_def = ast.parse('''
        class Cls(object):
            def fn():
                yield 1
                return 5
    ''').body[0]
    async_function_def = ast.parse('''
        async def fn():
            yield 1
            return 5
    ''').body[0]

# Generated at 2022-06-14 02:14:33.174745
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:14:34.402738
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:14:40.133479
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    with open('tests/fixtures/ast_fixtures/functiondef_return.py') as f:
        code = f.read()
    tree = ast.parse(code)

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)

    with open('tests/fixtures/ast_fixtures/functiondef_return_to_raise.py') as f:
        expected_code = f.read()
    expected_tree = ast.parse(expected_code)

    assert ast.dump(tree, include_attributes=True) == ast.dump(expected_tree, include_attributes=True)


# Generated at 2022-06-14 02:14:50.987098
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Compiles to
    # def test():
    #     yield 1
    #     exc = StopIteration()
    #     exc.value = 5
    #     raise exc
    test_string = """def test():
        yield 1
        return 5"""
    test_ast = ast.parse(test_string)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(test_ast)

# Generated at 2022-06-14 02:15:04.262210
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    class MockNodeTransformer:
        def __call__(self, node):
            node.test_field = "Success"
            return node

    mock_node_transformer = MockNodeTransformer()

    mock_function_def = ast.FunctionDef(body = [
        ast.Expr(value = ast.Yield(value = ast.Num(n = 3))),
        ast.Return(value = ast.Num(n = 5)), ast.Expr(value = ast.Yield(value = ast.Num(n = 7)))
    ])


# Generated at 2022-06-14 02:15:14.300539
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import setup_test_env
    setup_test_env()
    from .. import loader

    code = '''
            def fn():
                yield 1
                return 5
            '''
    old_ast = ast.parse(code)
    # old_ast.body[0].body[1].value.s = '5'
    new_ast = loader.visit(old_ast)

    code = '''
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
            '''
    expected = ast.parse(code)

    assert ast.dump(new_ast, include_attributes=True) == ast.dump(expected, include_attributes=True)