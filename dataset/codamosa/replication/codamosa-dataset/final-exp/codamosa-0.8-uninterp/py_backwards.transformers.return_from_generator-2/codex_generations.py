

# Generated at 2022-06-14 02:06:13.599815
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testing import get_ast, assert_transformed_ast
    from .transformers import Transformer

    source = """
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

    transformer = Transformer([
        ReturnFromGeneratorTransformer(),
    ])

    assert_transformed_ast(transformer, source, expected)



# Generated at 2022-06-14 02:06:22.327766
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse(r"""
        def fib(x):
            a, b = 1, 1
            while True:
                yield a
                a, b = b, a + b
            return 1
    """)
    correct_node = ast.parse(r"""
        def fib(x):
            a, b = 1, 1
            while True:
                yield a
                a, b = b, a + b
            exc = StopIteration()
            exc.value = 1
            raise exc
    """)
    node = ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(node) == ast.dump(correct_node)

# Generated at 2022-06-14 02:06:36.555164
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():  # pylint: disable=invalid-name
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    from ..utils.source import source_to_ast
    from ..unparse import Unparser
    from ..visitor import Visitor
    import textwrap

    python_code = textwrap.dedent("""\
        def fn():
            yield 1
            return 5
    """)

    expected_python_code = textwrap.dedent("""\
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)

    ast_tree = source_to_ast(python_code)
    ast_tree = ReturnFromGeneratorTransformer().visit(ast_tree)

    visitor = Visitor()

# Generated at 2022-06-14 02:06:41.788311
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

    class TestException(Exception):
        pass

    # Snippets of code to test the visit_FunctionDef method of the
    # ReturnFromGeneratorTransformer class

    # Test 1

# Generated at 2022-06-14 02:06:50.054775
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import transform, parse_ast

    code1 = """
    def fn():
        yield 1
        if True:
            yield 2
            return 2
        else:
            yield 3
            return 4

    def fn2():
        yield fn()
    """

    result1 = """
    def fn():
        yield 1
        if True:
            yield 2
            exc = StopIteration()
            exc.value = 2
            raise exc
        else:
            yield 3
            exc = StopIteration()
            exc.value = 4
            raise exc

    def fn2():
        yield fn()
    """

    result1 = parse_ast(result1)
    code1 = parse_ast(code1)

    assert transform(ReturnFromGeneratorTransformer, code1) == result1



# Generated at 2022-06-14 02:07:01.219378
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import samp
    from ..utils import astdump

    target = (3, 2)

    code = """
    def fn():
        yield 1
        return 5
    """
    code = samp.apply(code, target)

    tree = ast.parse(code)
    result = astdump.dumps(tree)


# Generated at 2022-06-14 02:07:07.461875
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import assert_code_equal

    code = """
    def fn():
        yield 1
        return 2
    """
    tree = ast.parse(code)

    ReturnFromGeneratorTransformer().visit(tree)

    expected_code = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """
    assert_code_equal(
        ast.fix_missing_locations(tree),
        ast.parse(expected_code))



# Generated at 2022-06-14 02:07:20.677323
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    assert ast.parse("""
        def fn():
            yield 1
            return 5
    """) == ReturnFromGeneratorTransformer().visit(ast.parse("""
        def fn():
            yield 1
            return 5
    """))

    assert ast.parse("""
        def fn():
            yield 1
            try:
                return 5
            except Exception:
                return
    """) == ReturnFromGeneratorTransformer().visit(ast.parse("""
        def fn():
            yield 1
            try:
                return 5
            except Exception:
                return
    """))


# Generated at 2022-06-14 02:07:21.596536
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:27.361612
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert ReturnFromGeneratorTransformer().visit(
        ast.parse("""
            def fn():
                yield 1
                return 5
        """)
    ) == ast.parse("""
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
        """)

# Generated at 2022-06-14 02:07:32.862439
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:40.752011
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Given
    code = """def foo():
    yield 1
    return 1"""
    expected = """def foo():
    yield 1
    exc = StopIteration()
    exc.value = 1
    raise exc"""
    transformer = ReturnFromGeneratorTransformer(verbose=False)
    # When
    result = transformer.run_pipeline(code, target=(3, 6))
    # Then
    assert result == expected



# Generated at 2022-06-14 02:07:51.952582
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    import sys

    code = """\
    def fn(a: int, b: int) -> None:
        def inner():
            yield 5
            return a + b
        """

    node = ast.parse(code)
    ast_to_modify = node.body[0]

    expected = """\
    def fn(a: int, b: int) -> None:
        def inner():
            yield 5
            exc = StopIteration()
            exc.value = a + b
            raise exc
        """

    ReturnFromGeneratorTransformer().visit(node)
    assert unparse(ast_to_modify) == expected


# Generated at 2022-06-14 02:08:03.625417
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    input_source = """
    def fn():
        try:
            yield None
            return
        except Exception as e:
            yield 2
            return 2 
        finally:
            try:
                yield 3
                return 3
            except Exception as e:
                yield 4
                return 4
            finally:
                try:
                    yield 5
                    return 5
                except Exception as e:
                    yield 6
                    return 6
                finally:
                    yield 7
                    return 7
    
    def fn2():
        try:
            return
        except Exception as e:
            pass
    """

# Generated at 2022-06-14 02:08:13.401999
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import assert_code_equal
    from ..utils import get_ast, get_func

    code = '''
        def fn():
            yield 1
            return 5
    '''
    # Add alias to avoid mypy type warnings.
    # See https://github.com/python/mypy/issues/3536
    C = ReturnFromGeneratorTransformer

    expected_code = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''

    node = get_ast(code)
    actual_node = C().visit(node)
    actual_code = get_func(actual_node)

    assert_code_equal(expected_code, actual_code)

# Generated at 2022-06-14 02:08:25.005058
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformerTestCase
    from ...utils.build_ast import build_ast
    from .. import annotations as ann

    class TestCase(BaseNodeTransformerTestCase):
        transformer = ReturnFromGeneratorTransformer

    code = '''def fn1():
        if True:
            yield 1
            return 5'''
    expected_code = '''def fn1():
        if True:
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc'''

    TestCase.assertTransformResult(build_ast(code), build_ast(expected_code),
                                   __test__=False)

# Generated at 2022-06-14 02:08:30.972423
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor

    transformer = ReturnFromGeneratorTransformer()
    example = astor.parse_file('example/example1.py').body[-1]
    assert 'return' in astor.to_source(example)
    example = transformer.visit(example)
    assert 'return' not in astor.to_source(example)

# Generated at 2022-06-14 02:08:38.252114
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""
        def generator():
            for i in range(10):
                yield i
            return i*i
    """)
    
    expected = """
        def generator():
            for i in range(10):
                yield i
            exc = StopIteration()
            exc.value = i*i
            raise exc
    """
    assert str(ReturnFromGeneratorTransformer().visit(tree)) == expected

# Code for testing the methods of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:41.637282
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import parse
    from ..utils.test_utils import assertAST, parse_dumps


# Generated at 2022-06-14 02:08:54.877031
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Arrange
    def fn():
        yield 1
        return 5

    node = ast.parse(inspect.getsource(fn)).body[0]
    transformer = ReturnFromGeneratorTransformer()

    # Act
    transformer.visit(node)

    # Assert

# Generated at 2022-06-14 02:09:11.054439
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    import typed_ast.ast3 as ast

    node = ast.parse('''
    def fn():
        yield 1
        return 5
    ''')

    transformer = ReturnFromGeneratorTransformer()
    transformed_node = transformer.visit(node)


# Generated at 2022-06-14 02:09:21.642481
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    code = """
    def f():
        yield 1
        return 5
    """
    module = ast.parse(code)
    transformer.visit(module)

# Generated at 2022-06-14 02:09:30.948574
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Eval(ast.NodeVisitor):
        def __init__(self, node: ast.FunctionDef):
            self.func_body: List[Any] = self._flatten(node.body)

        def _flatten(self, body: List[Any]) -> List[Any]:
            to_check = [x for x in body]  # type: ignore
            result = []

            while to_check:
                current = to_check.pop()

                if hasattr(current, 'value'):
                    to_check.append(current.value)
                elif hasattr(current, 'body') and isinstance(current.body, list):  # type: ignore
                    to_check.extend([x for x in current.body])

                result.append(current)
            return result


# Generated at 2022-06-14 02:09:42.678415
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..tests.utils import check_transformation
    from ..tests.utils import get_node as N

    class_ast = N(ast.ClassDef, name='A', body=[N(ast.FunctionDef, name='gen', args=N(ast.arguments, args=[N(ast.arg, arg='self')], defaults=[], kwonlyargs=[], kw_defaults=[], kwarg=None, vararg=None), body=[N(ast.Expr, value=N(ast.Yield, value=N(ast.Num, n=1))), N(ast.Return, value=N(ast.Num, n=5))])])

# Generated at 2022-06-14 02:09:43.848936
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:58.336077
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.ast_factory import ast_call, ast_attribute, ast_name, ast_yield, ast_yieldfrom, ast_return, ast_expr, ast_num, ast_if, ast_assign, ast_break, ast_continue
    from ..utils.ast_parse import parse


# Generated at 2022-06-14 02:10:00.115696
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor

# Generated at 2022-06-14 02:10:00.874551
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:08.206112
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    input_tree = ast.parse("""
        def fn():
            yield 1
            return 5
    """)
    expected_tree = ast.parse("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)
    transformer = ReturnFromGeneratorTransformer()
    output_tree = transformer.visit(input_tree)
    assert ast.dump(output_tree) == ast.dump(expected_tree)
    assert transformer._tree_changed == True



# Generated at 2022-06-14 02:10:11.917561
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import run_in_out_test
    run_in_out_test(ReturnFromGeneratorTransformer,
                    '''
                    def f():
                        yield 1
                        return 2
                    ''')

# Generated at 2022-06-14 02:10:32.174304
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def f():
        yield 1
        return 5
    def g():
        yield 1
        def h():
            yield 2
            return 6
            return 7
        yield 2
        return 6

    node = ast.parse(inspect.getsource(f))
    ReturnFromGeneratorTransformer().visit(node)
    fn = compile(node, '<snippet>', 'exec')
    g = fn.body[0].body

# Generated at 2022-06-14 02:10:44.093905
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    _code_gen = ReturnFromGeneratorTransformer()
    class_def = ast.parse(
        textwrap.dedent("""
        def fn():
            yield 1
            return 5
        """)
    ).body[0]
    result = _code_gen.visit_FunctionDef(class_def)
    expected = ast.parse(
        textwrap.dedent("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """)
    ).body[0]
    assert ast.dump(result) == ast.dump(expected)

# def _test_all():
#     _test_ReturnFromGeneratorTransformer_visit_FunctionDef()
#
#
# if __name__ == '__main__':
#     _test_all()

# Generated at 2022-06-14 02:10:57.932558
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    fn = ast.FunctionDef(
        name='fn',
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=[
            ast.Yield(value=ast.Num(n=1)),
            ast.Return(value=ast.Num(n=5)),
            ast.Expr(value=ast.Num(n=1))
        ],
        decorator_list=[],
        returns=None
    )

    result = ReturnFromGeneratorTransformer().visit(fn)


# Generated at 2022-06-14 02:11:08.536784
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    try:
        from typed_ast import ast3 as ast
        from typed_ast.ast3 import ClassDef, FunctionDef
    except ImportError:
        import ast
        from ast import ClassDef, FunctionDef  # type: ignore

    code = """
    def fn():
        yield 1
        return 2
    """

    tree = ast.parse(code, mode='exec')
    transformer = ReturnFromGeneratorTransformer()
    new_tree = transformer.visit(tree)

    assert isinstance(new_tree.body[0], FunctionDef)
    assert len(new_tree.body[0].body) == 2
    assert isinstance(new_tree.body[0].body[0], ast.Expr)
    assert isinstance(new_tree.body[0].body[0].value, ast.Yield)

# Generated at 2022-06-14 02:11:17.490001
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # No return statements in function
    node1 = ast.parse("""
    def fn():
        return 5
    """, mode='exec')
    assert not ReturnFromGeneratorTransformer(node1).visit_FunctionDef(node1.body[0])

    # Return statements in function
    node2 = ast.parse("""
    def fn():
        yield 1
        return 5
    """, mode='exec')
    assert ReturnFromGeneratorTransformer(node2).visit_FunctionDef(node2.body[0])


# Generated at 2022-06-14 02:11:23.968289
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from .base import BaseNodeTest

    class TestReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer, BaseNodeTest):
        pass

    TestReturnFromGeneratorTransformer.setUpClass()

    def test_transformer(code_in, code_out, tree_in):
        TestReturnFromGeneratorTransformer.test(
            ReturnFromGeneratorTransformer,
            code_in, code_out,
            tree_in=tree_in,
        )


# Generated at 2022-06-14 02:11:32.075661
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class_ = ReturnFromGeneratorTransformer

    code = '''
    def fn():
        yield 1
        return 5
    '''
    expected_result = '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''

    result = class_().visit(ast.parse(code))
    assert astor.to_source(result).strip() == expected_result



# Generated at 2022-06-14 02:11:42.808928
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Return, FunctionDef, Expr, Yield, YieldFrom, Name, Load, Call, Attribute, Str, Load, \
        Compare, List, Lt, Gt, Eq, And, Or, Num

    # Test 1
    node = FunctionDef(
        name='fn',
        args=None,
        body=[
            Return(Num(n=1)),
        ],
        decorator_list=[],
        returns=None
    )

    expected = FunctionDef(
        name='fn',
        args=None,
        body=[
            Return(Num(n=1)),
        ],
        decorator_list=[],
        returns=None
    )

    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(node)

# Generated at 2022-06-14 02:11:49.408942
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Test(unittest.TestCase):
        maxDiff = None

    if not hasattr(Test, 'assertCountEqual'):
        Test.assertCountEqual = Test.assertItemsEqual

    def check(input_, expected):
        input_ = ast.parse(input_)
        expected = ast.parse(expected)

        transformer = ReturnFromGeneratorTransformer()
        actual = transformer.visit(input_)

        Test.assertEqual(actual, expected)

    test_function_defs = [
        """
        def foo():
            yield 1
            return 5
            yield 2
            return 6
        """,
        """
        def bar():
            if True:
                yield 1
            for i in []:
                yield 1
                return 5
            return 5
        """,
    ]

    expected

# Generated at 2022-06-14 02:11:55.240500
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    tree = ast.parse('def foo():\n    yield 1;\n    return 2')
    transformer = ReturnFromGeneratorTransformer()
    output = transformer.visit(tree)
    expected = ast.parse(
        'def foo():\n    yield 1;\n    exc = StopIteration();\n    exc.value = 2;\n    raise exc'
    )
    assert ast.dump(output) == ast.dump(expected)

# Generated at 2022-06-14 02:12:22.615990
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent

    before = dedent('''\
        def fn():
            yield 1
            return 5''')

    expected = dedent('''\
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc''')

    fn = ast.parse(before).body[0]
    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(fn)

    assert ast.dump(result) == ast.dump(ast.parse(expected).body[0])

# Generated at 2022-06-14 02:12:29.872130
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ... import parse
    code = """
    def fn():
        yield 1
        return 5
    """
    tree = parse(code)
    new_tree = ReturnFromGeneratorTransformer().visit(tree)
    assert_transforms_to(code, """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """, new_tree)



# Generated at 2022-06-14 02:12:38.274705
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Test for visit_FunctionDef method"""
    from ast import parse
    from .base import BaseNodeTransformerTest, run_test

    class TestReturnFromGeneratorTransformer(BaseNodeTransformerTest):
        """docstring for TestReturnFromGeneratorTransformer"""
        transformer_class = ReturnFromGeneratorTransformer

        def test_yield(self):
            """Test for visit_FunctionDef method in ReturnFromGeneratorTransformer class"""

# Generated at 2022-06-14 02:12:47.527113
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
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
    node = ast.parse(source)

    transformer = ReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)

    source = ast.fix_missing_locations(new_node)
    compiled = compile(source, filename="<ast>", mode="exec")
    code = compiled.co_code
    expected_code = compile(expected, filename="<ast>", mode="exec").co_code
    assert code == expected_code

# Generated at 2022-06-14 02:12:54.000345
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typing import Iterator
    from .test_utils import transform, assert_exact
    from typed_ast import ast3 as ast

    code = """
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
    with assert_exact(expected):
        @transform(ReturnFromGeneratorTransformer)
        def fn() -> Iterator[int]:
            yield 1
            return 2



# Generated at 2022-06-14 02:12:58.410998
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import parse
    node = parse("""
        def a():
            yield x
            return y
    """)
    t = ReturnFromGeneratorTransformer()
    t.visit(node)
    expected_node = parse("""
        def a():
            yield x
            exc = StopIteration()
            exc.value = y
            raise exc
    """)
    assert node == expected_node

# Generated at 2022-06-14 02:13:08.025013
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typing import List
    from typed_ast import ast3 as ast

    a = '''
    def fn():
        yield 1
        return 5
    '''

    b = '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''

    t = ReturnFromGeneratorTransformer()
    t.visit(ast.parse(a))
    res = ast.dump(t.root)

    assert res == b

# Generated at 2022-06-14 02:13:10.618592
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import Return, Yield

    t = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:13:18.509224
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import codegen
    code = '''def fn():
        yield 1
        return 5
    '''

    exec_env = {}
    exec(code, {})

    returned = ReturnFromGeneratorTransformer().visit(ast.parse(code))
    codegen.to_source(returned)
    compiled = compile(returned, filename='<string>', mode='exec')
    exec(compiled, exec_env)

    gen = exec_env['fn']()
    assert gen.send(None) == 1
    with pytest.raises(StopIteration) as err:
        gen.send(None)
    assert err.value.value == 5

# Generated at 2022-06-14 02:13:30.134657
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer.

    It uses the class ReturnFromGeneratorTransformer to check that it replaces a return in a
    generator with a StopIteration exception.
    """
    node1 = ast.parse(return_from_generator.format(return_value=[1, 2, 3]))
    node2 = ast.parse(return_from_generator.get_body(return_value=[1, 2, 3]))
    transformer = ReturnFromGeneratorTransformer()
    new_node1 = transformer.visit(node1)
    new_node2 = transformer.visit(node2)
    assert ast.dump(new_node1) == ast.dump(new_node2)

# Generated at 2022-06-14 02:14:08.910426
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:14:14.031134
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    tr = ReturnFromGeneratorTransformer()
    example1 = ast.parse("""
    def foo():
        yield 1
        return
    """)  # type: ignore
    example1 = tr.visit(example1)
    assert ast.dump(example1, annotate_fields=False) == "Module(body=[FunctionDef(name='foo', args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Yield(value=Constant(value=1, kind=None))), Return(value=None)], decorator_list=[], returns=None)])"

    example2 = ast.parse("""
    def foo():
        yield 1
        return 5
    """)  # type: ignore
    example2

# Generated at 2022-06-14 02:14:21.435530
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..unittest_tools import assert_if_prints_nothing, assert_if_prints

    from typed_ast import ast3 as ast   # type: ignore


# Generated at 2022-06-14 02:14:36.311688
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    from .fix_python_version import fix_python_version

    node = ast.FunctionDef('fn', ast.arguments([], [], [], [], None, []),
                           [ast.Yield(ast.Constant(value=1)), ast.Return(ast.Constant(value=5))], [], None)
    new_node = ReturnFromGeneratorTransformer().visit(node)
    assert unparse(new_node) == "fn():\n" \
                                 "    yield 1\n" \
                                 "    exc = StopIteration()\n" \
                                 "    exc.value = 5\n" \
                                 "    raise exc\n"
    assert fix_python_version(unparse(node)) == "def fn():\n" \
                

# Generated at 2022-06-14 02:14:43.716795
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    expected_output = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    src = """
    def fn():
        yield 1
        return 5
    """

    module = ast.parse(src)
    transformer = ReturnFromGeneratorTransformer()
    assert transformer.visit(module) == ast.parse(expected_output)


# Generated at 2022-06-14 02:14:55.074364
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class TestReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer):
        pass

    assert_source_code_equal(
        TestReturnFromGeneratorTransformer().visit(
            ast.parse('''
            def test():
                return 3
            ''')
        ),
        ast.parse('''
        def test():
            exc = StopIteration()
            exc.value = 3
            raise exc
        ''')
    )


# Generated at 2022-06-14 02:15:06.927508
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils import TreeInstance, TreeDiffer
    from unittest import mock

    class TestReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer):
        pass

    p = mock.patch('logging.Logger.warning')
    with p, TreeInstance(ReturnFromGeneratorTransformer()) as instance:
        instance.visit_FunctionDef(ast.parse(textwrap.dedent('''
            def f():
                yield 1
                return 5
        ''')))
        differ = TreeDiffer(ReturnFromGeneratorTransformer())

# Generated at 2022-06-14 02:15:14.964177
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..tokenize_python import tokenize_python
    from ..ast_python import ast_to_source
    from ..sprint import sprint

    def check(source, expected):
        source_lines = source.split('\n')

        tree = ast.parse(source)
        tree = ReturnFromGeneratorTransformer().visit(tree)
        tree_source = ast_to_source(tree, source_lines)
        print(tree_source)

        print('--')

        expected_lines = expected.split('\n')
        sprint(expected_lines, tokenize_python(expected_lines))

        assert tree_source == expected


# Generated at 2022-06-14 02:15:26.289489
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """
    Test method visit_FunctionDef with argument of type ast.FunctionDef
    """
    # Test when node.body is an empty list
    # Case when return_from_generator is empty
    # Test when node.body is not an empty list
    # Case when return_from_generator is not empty
    
    # Test when node.body is an empty list
    node = ast.parse(
        """def foo():
            yield 1
            return 5
        """
    ).body[0]
    assert len(ReturnFromGeneratorTransformer()._find_generator_returns(node)) == 1

    # Case when return_from_generator is empty
    return_from_generator.set_body([])
    assert len(ReturnFromGeneratorTransformer()._find_generator_returns(node)) == 0

    #

# Generated at 2022-06-14 02:15:30.854055
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..testing import assert_program

    string = '''
        def fn():
            yield 1
            return 5
    '''

    expected_string = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''

    assert_program(string, expected_string, [ReturnFromGeneratorTransformer])
