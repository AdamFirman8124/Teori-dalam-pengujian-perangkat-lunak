

# Generated at 2022-06-14 02:06:09.360768
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import CompilationError
    from .base import BaseTestCompiler

    class TestCompiler(BaseTestCompiler):
        TRANSFORMERS = [  ReturnFromGeneratorTransformer,
        ]


# Generated at 2022-06-14 02:06:18.718892
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():  # NOQA D100
    source = """
    def foo():
        a = 10
        yield 1
        return a
        a = 20
        yield a
        return 0
    """
    expected = """
    def foo():
        a = 10
        yield 1
        exc = StopIteration()
        exc.value = a
        raise exc
        a = 20
        yield a
        exc = StopIteration()
        exc.value = 0
        raise exc
    """
    real = compile_source(source, ReturnFromGeneratorTransformer)
    assert expected == real



# Generated at 2022-06-14 02:06:28.905637
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # type: () -> None
    def fn():
        # type: () -> None
        pass

    fn_def = ast.parse(inspect.getsource(fn)).body[0]
    tr = ReturnFromGeneratorTransformer()
    fn_def_ = tr.visit(fn_def)
    assert fn_def_ is fn_def

    def fn():
        # type: () -> Iterator[int]
        return 1

    fn_def = ast.parse(inspect.getsource(fn)).body[0]
    tr = ReturnFromGeneratorTransformer()
    fn_def_ = tr.visit(fn_def)
    assert fn_def_ is fn_def

    def fn():
        # type: () -> Iterator[int]
        yield 1
        return 5


# Generated at 2022-06-14 02:06:35.608200
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    t = ReturnFromGeneratorTransformer()

    def fn1():
        yield 3
        return 5

    fn1_tree = ast.parse(fn1.__doc__)
    fn1_tree = t.visit(fn1_tree)

# Generated at 2022-06-14 02:06:47.397846
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .testutils import round_trip
    from typed_ast.ast3 import Module, FunctionDef, Return, Name, Call, Attribute, YieldFrom


# Generated at 2022-06-14 02:06:59.061176
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""
        def fn():
            yield 1
            return 5
        def fn2():
            yield 1
        def fn3():
            return 2
        def fn4():
            yield 1
            return 5
            return 6
    """) # type: ast.Module

    node_transformer = ReturnFromGeneratorTransformer()
    tree = node_transformer.visit(tree)

    expected_tree = ast.parse("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        def fn2():
            yield 1
        def fn3():
            return 2
        def fn4():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
            return 6
    """) # type: ast.Module

# Generated at 2022-06-14 02:07:06.784238
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..tests.fixtures import simple_if_generator, simple_if_generator_target
    node = simple_if_generator()

    actual = ReturnFromGeneratorTransformer().visit(node)
    expected = simple_if_generator_target()

    print('actual')
    print(ast.dump(actual))
    print()
    print('expected')
    print(ast.dump(expected))
    print()
    
    assert ast.dump(actual, annotate_fields=False, include_attributes=False) == ast.dump(expected, annotate_fields=False, include_attributes=False)

# Generated at 2022-06-14 02:07:11.526191
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from . import compile_source
    source = '''
    def foo(a):
        if a:
            return a
        else:
            yield 1'''

    expected = '''
    def foo(a):
        if a:
            exc = StopIteration()
            exc.value = a
            raise exc
        else:
            yield 1'''

    assert compile_source(source, ReturnFromGeneratorTransformer) == expected

# Generated at 2022-06-14 02:07:16.168642
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source import source_to_ast
    from ..utils.source import source_to_function

    source = """
    def fn(x):
        if x:
            return 1
        elif x:
            yield 2
        else:
            return "wow"
    """
    
    class_name = "ReturnFromGeneratorTransformer"
    func_name = "visit_FunctionDef"
    expected = """
    def fn(x):
        if x:
            return 1
        elif x:
            yield 2
        else:
            exc = StopIteration()
            exc.value = "wow"
            raise exc
    """


# Generated at 2022-06-14 02:07:31.313895
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class FuncDef(ast.FunctionDef):
        def __init__(self, name, body):
            self.name = name  # type: ignore
            self.body = body  # type: ignore

    class Return(ast.Return):
        def __init__(self, value):
            self.value = value  # type: ignore

    class Yield(ast.Yield):
        def __init__(self, value):
            self.value = value  # type: ignore

    return_from_generator_expected_body = snippet.get_body(
        body=return_from_generator
    )

    node = FuncDef('name', [
        Return(5),
    ])
    assert ReturnFromGeneratorTransformer().visit(node) == node


# Generated at 2022-06-14 02:07:36.716613
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from astunparse import unparse

# Generated at 2022-06-14 02:07:44.073158
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import generate_code, assert_code_transformation

    code = generate_code('''
        def fn():
            yield from [1, 2]
            return 5
    ''')

    expected_code = generate_code('''
        def fn():
            yield from [1, 2]
            exc = StopIteration()
            exc.value = 5
            raise exc
    ''')

    assert_code_transformation(ReturnFromGeneratorTransformer, code, expected_code)

# Generated at 2022-06-14 02:07:51.228186
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..runner import run_all_nodes
    from ..utils import unparse
    from ..common import get_src

    src = get_src(ReturnFromGeneratorTransformer)
    node = run_all_nodes(src=src)
    node = ReturnFromGeneratorTransformer().visit(node)

    unparsed_source = unparse(node)

    assert unparsed_source.count('exc') >= 1
    assert unparsed_source.count('return') == 0

# Generated at 2022-06-14 02:07:57.848200
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source_code import source_code_from_ast
    from ..utils.testing import do_test

    do_test(ReturnFromGeneratorTransformer,
            expected_source=dedent('''\
                def fn():
                    yield 1
                    exc = StopIteration()
                    exc.value = 5
                    raise exc
            '''), actual_source=dedent('''\
                def fn():
                    yield 1
                    return 5
            '''), ast_transformer=source_code_from_ast())


# Generated at 2022-06-14 02:08:00.728088
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Input
    simple_input = ast.parse(return_from_generator.get_code(return_value=5)).body[0]
    # Output

# Generated at 2022-06-14 02:08:09.927328
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testing import verify, verify_node_matches
    from ..utils.testing import transform_and_compile_from_string

    code = """\
        def fn():
            yield 1
            return 5
    """
    expect = """\
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    verify(ReturnFromGeneratorTransformer, code, expect)
    verify_node_matches(ReturnFromGeneratorTransformer, code, expect)
    transform_and_compile_from_string(ReturnFromGeneratorTransformer, code, expect)

    # Test it doesn't break on normal functions
    code = """\
        def fn():
            return 5
    """
    expect = """\
        def fn():
            return 5
    """


# Generated at 2022-06-14 02:08:14.790982
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..cst_transformer import CstTransformer

    @snippet
    def foo():
        yield 1
        return 1

    expected = ast.parse(foo.to_string()).body[0]
    actual = CstTransformer().transform_ast(ast.parse(foo.to_string()))
    assert ast.dump(actual, include_attributes=False) == ast.dump(expected, include_attributes=False)

# Generated at 2022-06-14 02:08:19.575131
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..ast_converter import convert
    from ..unparser import Unparser
    from ..utils import source_to_unicode
    from ..unparse import UnparseVisitor


# Generated at 2022-06-14 02:08:31.429638
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import CompilerTestCase

    class Test1(CompilerTestCase):
        target = (3, 2)
        node = ast.parse("""
            def fn():
                yield 1
                return "a"
            """)

        def test_changes(self):
            self.assertEqual(len(self.returns), 1)
            self.assertEqual(self.returns[0].value.s, "a")
            self.assertTrue(self.tree_changed)

        def test_module(self):
            self.assertModule("""
                import typing as _typing
                def fn() -> _typing.Generator[int, None, str]:
                    yield 1
                    exc = StopIteration()
                    exc.value = "a"
                    raise exc
            """)


# Generated at 2022-06-14 02:08:32.461194
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:42.344916
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:49.519378
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typing import Generator

    def generator() -> Generator[int, None, int]:
        yield 1
        return 5

    old_src = generator.__code__.co_code
    new_src = ReturnFromGeneratorTransformer().visit(generator).__code__.co_code
    assert new_src != old_src

    def generator() -> Generator[int, None, None]:
        yield 1
        return 5

    old_src = generator.__code__.co_code
    new_src = ReturnFromGeneratorTransformer().visit(generator).__code__.co_code
    assert new_src == old_src



# Generated at 2022-06-14 02:08:59.468140
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import ast
    import astunparse

    code = """
async def f():
    while True:
        yield 42
        return 42

"""
    expected_code = """
async def f():
    while True:
        yield 42
        exc = StopIteration()
        exc.value = 42
        raise exc

"""
    tree = ast.parse(code)
    new_tree = ReturnFromGeneratorTransformer().visit(tree)
    output_code = astunparse.unparse(new_tree)
    assert output_code == expected_code

# Generated at 2022-06-14 02:09:10.879787
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .types_and_unittest_helper import ExampleFunction, get_original_and_transformed
    from .return_from_generator_transformer import ReturnFromGeneratorTransformer
    from ..Warnings import ReturnFromGeneratorWarning
    import unittest
    from unittest.mock import Mock

    class ReturnFromGeneratorWarnTestCase(unittest.TestCase):
        def test_normal_function(self):
            function_ast_returns = ExampleFunction.get_ast("""
                def normal_function():
                    return 5
            """)
            original, transformed, _ = get_original_and_transformed(
                function_ast_returns[0],
                ReturnFromGeneratorTransformer,
                Mock(side_effect=ReturnFromGeneratorWarning))

# Generated at 2022-06-14 02:09:21.589010
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .mock_node import MockNode
    from ..utils.source_code import SourceCode
    from .mock_visitor import MockVisitor

    a = ast.parse('def a(): yield 1\nreturn 42')
    b = ast.parse('def a():\n    yield 1;\n    exc = StopIteration();exc.value = 42;raise exc')
    source = SourceCode('<test>', 'def a(): yield 1\nreturn 42')
    mock = MockVisitor()
    node = MockNode(source, a)
    transformer = ReturnFromGeneratorTransformer(mock, node)
    transformer.visit_FunctionDef(node.node)


# Generated at 2022-06-14 02:09:29.411757
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""
    def fn():
        yield 1
        return 5
    """)

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)
    code = compile(tree, '', 'exec')
    code = ''.join(line.strip() for line in code.co_consts[0].co_code.split('\n')[1:-1])
    assert code == 'exc = StopIteration(); exc.value = 5; raise exc'

# Generated at 2022-06-14 02:09:36.151510
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    test_input = """
    def test():
        return 1
    """
    test_output = """
    def test():
        return 1
    """
    node = ast.parse(test_input, '<test>', mode='exec')
    ReturnFromGeneratorTransformer().visit(node)
    output = ast.unparse(node)
    assert output == test_output


# Generated at 2022-06-14 02:09:37.772958
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:38.440586
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:48.251928
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import parse_snippet, compare_final_nodes

    node = parse_snippet(
        """
        def fn():
            yield 1
            return 5
        """
    )
    expected_node = parse_snippet(
        """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """
    )

    assert compare_final_nodes(ReturnFromGeneratorTransformer().visit(node), expected_node)



# Generated at 2022-06-14 02:10:17.923085
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def assert_transform(before, after):
        actual = ast.parse(before)
        t = ReturnFromGeneratorTransformer()
        actual = t.visit(actual)
        actual = ast.fix_missing_locations(actual)
        assert ast.dump(ast.parse(after)) == ast.dump(actual)

    # Basic cases
    # Only return
    before = """
        def fn(x):
            return x + 1
    """
    after = """
        def fn(x):
            return x + 1
    """
    assert_transform(before, after)
    # Only yield
    before = """
        def fn(x):
            yield x
    """
    after = """
        def fn(x):
            yield x
    """
    assert_transform(before, after)
    # No return or yield

# Generated at 2022-06-14 02:10:23.460972
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = "def fn(): yield 1\nreturn 1"
    expected = "def fn(): yield 1\nexc = StopIteration()\nexc.value = 1\nraise exc"
    output = ReturnFromGeneratorTransformer(code=code).run().output
    assert expected == output


# Generated at 2022-06-14 02:10:34.218858
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.FunctionDef(
        name='fn',
        args=ast.arguments(
            args=[],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[],
        ),
        body=[
            ast.Yield(value=ast.Constant(value=1)),
            ast.Return(value=ast.Constant(value=5)),
        ],
        decorator_list=[],
        returns=None,
    )


# Generated at 2022-06-14 02:10:45.126383
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import itertools
    import random
    from ..utils.random_ast import random_ast
    from .base import BaseNodeTransformerTester as tester

    def _run_test(source: str, expected: str) -> None:
        tree = ast.parse(textwrap.dedent(source))
        visitor = ReturnFromGeneratorTransformer()
        new_tree = visitor.visit(tree)
        assert expected == ast.dump(new_tree)


# Generated at 2022-06-14 02:10:58.967383
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def _test_case(parent, return_):
        fd = ast.FunctionDef(
                name='test',
                args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                body=[parent],
                decorator_list=[],
                returns=None
        )
        rfg = ReturnFromGeneratorTransformer()
        rfg.visit(fd)

        exc = rfg._get_namespace().get('exc')
        assert exc, "Variable exc not found"
        assert isinstance(exc, ast.Name)
        assert isinstance(exc.ctx, ast.Store)

        raise_stmt = parent.body[-1]

# Generated at 2022-06-14 02:11:09.892095
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer"""
    fn = ast.parse('''
    def fn(a, b):
        yield 1
        return 5
    ''')

    visitor = ReturnFromGeneratorTransformer()
    fn = visitor.visit(fn)

    assert isinstance(fn.body[0], ast.FunctionDef)
    assert isinstance(fn.body[0].body, list)
    assert isinstance(fn.body[0].body[0], ast.Yield)
    assert isinstance(fn.body[0].body[1], ast.Assign)
    assert isinstance(fn.body[0].body[2], ast.Expr)
    assert isinstance(fn.body[0].body[2].value, ast.Raise)

# Generated at 2022-06-14 02:11:20.325882
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
    def a():
        yield 1
        return 5

    def b():
        yield 1
        if True:
            return 5
"""
    expected = """
    def a():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc

    def b():
        yield 1
        if True:
            exc = StopIteration()
            exc.value = 5
            raise exc
"""
    expected = ast.parse(expected)
    actual = ast.parse(code)
    t = ReturnFromGeneratorTransformer()
    t.visit(actual)
    assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 02:11:32.076217
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .utils import transform
    from .visitor import print_ast
    from .base import print_python
    from ..utils.asserts import assertEqual
    from typed_astunparse import unparse

    statement = """
    def fn():
        yield 1
        return 2
    """

    expected = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """

    ast_tree = ast.parse(statement)
    new_ast = transform(ast_tree, ReturnFromGeneratorTransformer)

    print_ast(new_ast)
    print_python(new_ast)
    assertEqual(unparse(new_ast), expected)

# Generated at 2022-06-14 02:11:41.040853
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    return_snippet = snippet('return 5')
    node = ast.parse('''
    def fn():
        yield 1
        yield 2
        return 5
    ''')

    expected = '''
    def fn():
        yield 1
        yield 2
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''

    class MockTransformer(ReturnFromGeneratorTransformer):
        """Mock transformer that doesn't actually change the tree."""
        _tree_changed = False

        def visit(self, node):
            if isinstance(node, ast.Return):
                return node

            return super().visit(node)

    actual = ast.fix_missing_locations(MockTransformer().visit(node))

    assert ast.dump(actual, include_attributes=True) == expected

# Generated at 2022-06-14 02:11:51.064513
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
    # Test for visit_FunctionDef with return value in function with yield
    # Input:
    node = ast.parse("""
    def fn():
        yield 1
        return 5
    """)
    # Output:
    expected = ast.parse("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """)
    # Test
    actual = ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(expected) == ast.dump(actual)

# Generated at 2022-06-14 02:12:33.165649
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import tests.test_visitor.utils as test
    test.test_single_transformer(
        ReturnFromGeneratorTransformer(),
        """
        def foo():
            yield 1
            return 5
        """,
        """
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """
    )

# Generated at 2022-06-14 02:12:39.726739
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
        tree = ast.parse(
            """def fn():
                yield 1
                return 5
            """
        )

        expected = """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc
"""
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(tree)
        assert transformer._tree_changed
        assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:12:43.435926
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    assert ast.parse('def fn(): yield 1; return 5') == ReturnFromGeneratorTransformer().visit(
        ast.parse('def fn(): yield 1; return 5'))

# Generated at 2022-06-14 02:12:53.752640
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Foo:
        def bar(self):
            yield 1
            return 5

        def baz():
            yield 1
            return 5

    foo_body = snippetable(Foo.bar.__code__)
    baz_body = snippetable(Foo.baz.__code__)

    expected_foo_body = snippetable(Foo.bar.__code__).replace(
        'yield 1\n    return 5',
        'yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc')
    expected_baz_body = snippetable(Foo.baz.__code__).replace(
        'yield 1\n    return 5',
        'yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc')

# Generated at 2022-06-14 02:13:00.850614
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Test case for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    from typed_ast.ast3 import parse
    from .base import BaseNodeTransformerTestCase
    from .base import BaseNodeTransformerTestCase as BNTCTC
    from .base import BaseNodeTransformerTestCase as bntctc
    transformer = ReturnFromGeneratorTransformer()
    def test_case(input: BNTCTC.Input, expected: BNTCTC.Expected):
        bntctc.assert_transformation(transformer, input, expected)
    ##################################################################
    # Test cases for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:06.370769
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import inspect
    import textwrap

    code = textwrap.dedent(inspect.getsource(test_ReturnFromGeneratorTransformer_visit_FunctionDef))

    node = ast.parse(code)
    node = ReturnFromGeneratorTransformer().visit(node)

    assert compile(node, '', 'exec')

# Generated at 2022-06-14 02:13:17.185676
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse
    import subprocess

    f1 = ast.parse(
        """
        def f1():
            yield 1
            return 5
        """)

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(f1)

    assert astunparse.unparse(f1) == "def f1():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc"
    assert subprocess.run(['python', '-c', 'def f1():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc'],
                          universal_newlines=True, stdout=subprocess.PIPE).stdout.strip() == "1"


# Generated at 2022-06-14 02:13:20.432703
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    '''Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer'''
    from ..utils.node_utils import node_to_str

# Generated at 2022-06-14 02:13:21.181535
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:32.444772
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def transform_test(unpatched_source):
        basic_patched_source = compile(unpatched_source, '<string>', 'single', optimize=2)
        patched_source = ReturnFromGeneratorTransformer().visit(ast.parse(unpatched_source))
        patched_source = compile(patched_source, '<string>', 'single', optimize=2)
        function = patched_source.__code__.co_consts[0]

        assert function.co_flags & 0x20  # check generator flag
        assert function.co_varnames == basic_patched_source.__code__.co_varnames
        assert function.co_consts[1] == StopIteration
        assert function.co_consts[2] == basic_patched_source.__code__.co_consts