

# Generated at 2022-06-14 02:06:09.594828
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformer
    from typed_astunparse import unparse
    transformers = [ReturnFromGeneratorTransformer]

# Generated at 2022-06-14 02:06:18.390647
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    example_str = """
    def fn():
        yield 1
        if True:
            return 5
    """
    expected_str = """
    def fn():
        yield 1
        if True:
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    expected_ast = ast.parse(expected_str)
    actual_ast = ast.parse(example_str)
    ReturnFromGeneratorTransformer().visit(actual_ast)
    assert ast.dump(actual_ast) == ast.dump(expected_ast)

# Generated at 2022-06-14 02:06:25.341824
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import parse
    from ..utils.ast_utils import equal_ast
    code1 = """
            def foo():
                yield 1
                return 5
        """
    code2 = """
            def foo():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
        """

    tree1 = parse(code1)
    tree2 = parse(code2)
    tr = ReturnFromGeneratorTransformer()
    tree3 = tr.visit(tree1)

    assert equal_ast(tree2, tree3)

# Generated at 2022-06-14 02:06:37.462156
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import FunctionDef, Return, Load, Name, Str, Expr, Yield
    from typed_ast.ast3 import parse
    node = FunctionDef(
        name='fn',
        args=None,
        body=[Yield(value=Str(s='1')),
              Expr(value=Return(value=Str(s='5')))
        ],
        decorator_list=[],
        returns=None
    )

# Generated at 2022-06-14 02:06:45.196017
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """\
    def foo():
        yield 1
        return 2
    """
    expected = """\
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """
    node = ast.parse(code)
    ReturnFromGeneratorTransformer().visit(node)
    actual = ast.dump(node, annotate_fields=False)
    print(actual)
    assert expected == actual

# Generated at 2022-06-14 02:06:52.529249
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from .base import BaseNodeTransformer, _ChildContext

    class TestTransformer(BaseNodeTransformer):
        def __init__(self, always_change=False):
            self._always_change = always_change

        def visit_Name(self, node):  # type: ignore
            node.id = 'hi'
            return node

    class TestTransformer2(BaseNodeTransformer):
        def __init__(self, always_change=False):
            self._always_change = always_change

        def visit_Name(self, node):  # type: ignore
            node.id = 'hi2'
            return node

    class A:
        def foo1(self):
            return 5

    class B:
        def foo3(self):
            return 5

        def foo2(self):
            return

# Generated at 2022-06-14 02:07:06.122264
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse

    class Visitor(ast.NodeVisitor):
        def __init__(self, node: ast.AST) -> None:
            self.node = node

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            ReturnFromGeneratorTransformer().visit(self.node)

    source = """def fn():
        yield 1
        return 5"""
    expected = """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc"""
    node = parse(source)
    Visitor(node).visit(node)
    assert format(node) == expected

    source = """def fn():
        return 1"""
    node = parse(source)
    Visitor(node).visit(node)

# Generated at 2022-06-14 02:07:19.823212
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    src = '''
        class A:
            def __iter__(self):
                yield 1
                return 5

            def test2():
                return 5
        def fn():
            yield 1
            return 5
    '''

    expected_src = '''
        class A:
            def __iter__(self):
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc

            def test2():
                return 5
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''

    node = ast.parse(src)
    node = ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(node) == ast.dump(ast.parse(expected_src))

# Generated at 2022-06-14 02:07:23.738888
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
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
    module = ast.parse(source)
    module = ReturnFromGeneratorTransformer().visit(module)
    assert expected == astor.to_source(module)

# Generated at 2022-06-14 02:07:30.882328
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    from typed_astunparse import unparse

    source = '''
    def foo():
        yield 1
        return 5
    '''
    node = ast.parse(source)
    expected = '''
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''

    transformed = ReturnFromGeneratorTransformer.run(node)
    res = unparse(transformed)
    assert res == expected

# Generated at 2022-06-14 02:07:46.342966
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..testing_utils import assert_code_equal
    from ..testing_utils import (
        parse_ast_tree,
        expected_ast_tree,
        expected_source,
        )
    from .. import transforms

    tree = parse_ast_tree('''
        def fn():
            yield 1
            return 5
    ''')

    expected_tree = expected_ast_tree('''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    ''')

    transform = transforms.ReturnFromGeneratorTransformer

    with expected_source('''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''):
        tree = transform().visit(tree)
        assert_code

# Generated at 2022-06-14 02:07:55.172826
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..chain import Chain
    from ..compat import StringIO
    from textwrap import dedent

    transformer = Chain([
        ReturnFromGeneratorTransformer,
    ])
    snippet_to_test = dedent('''
        namespace = {}

        def fn():
            yield 1
            return 5
            yield 2
    ''')
    output = StringIO()
    transformer.write(snippet_to_test, output=output)

    expected = dedent('''
        namespace = {}

        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
            yield 2
    ''')
    assert output.getvalue() == expected

# Generated at 2022-06-14 02:08:03.403260
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse
    import typing
    import os

    from ..utils.test_utils import load_test_data

    test_data = load_test_data(os.path.dirname(__file__),
                               "ReturnFromGeneratorTransformer_visit_FunctionDef.input")
    test_cases = typing.cast(typing.List[typing.Tuple[ast.FunctionDef, str]], test_data)

    for test_case in test_cases:
        node, expected_output = test_case
        actual_output = astunparse.unparse(ReturnFromGeneratorTransformer().visit(node)).strip()
        assert actual_output == expected_output

# Generated at 2022-06-14 02:08:13.746541
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    functiondef_node1 = ast.FunctionDef(name='my_function1',
                                        args=ast.arguments(
                                            args=[],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[]),
                                        body=[
                                            ast.Yield(value=ast.Constant(value=1)),
                                            ast.Return(value=ast.Constant(value=5))],
                                        decorator_list=[],
                                        returns=None)

# Generated at 2022-06-14 02:08:27.808537
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class DummyNode:
        ...
    dummy_node = DummyNode()
    dummy_node2 = DummyNode()
    dummy_body = [DummyNode(), DummyNode()]
    dummy_body2 = [DummyNode(), DummyNode()]
    dummy_return = ast.Return()
    dummy_return2 = ast.Return()
    dummy_return2.value = '5'
    dummy_function = ast.FunctionDef()
    dummy_function.body = dummy_body
    dummy_function.body[0] = dummy_function
    dummy_function.body[1] = dummy_return
    dummy_function2 = ast.FunctionDef()
    dummy_function2.body = dummy_body2
    dummy_function2.body[0] = dummy_node
    dummy_function2.body[1] = dummy

# Generated at 2022-06-14 02:08:38.288086
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import parse_to_ast

    class_def = parse_to_ast('''
        class Class(object):
            def fn():
                yield 1
                return 5
    ''')

    class_def = ReturnFromGeneratorTransformer().visit(class_def)
    assert len(class_def.body) == 1  # type: ignore
    class_def = class_def.body[0]  # type: ignore

    assert len(class_def.body) == 1  # type: ignore
    fn = class_def.body[0]  # type: ignore

    assert len(fn.body) == 6  # type: ignore

    assert isinstance(fn.body[0], ast.Expr)  # type: ignore
    assert isinstance(fn.body[0].value, ast.Yield) 

# Generated at 2022-06-14 02:08:48.795925
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    module, output = compile_snippet(snippet, 'test_ReturnFromGeneratorTransformer_visit_FunctionDef')

    def assert_return_in_generator_transformed_correctly(fn_name):
        for func in module.body:
            if isinstance(func, ast.FunctionDef) and func.name == fn_name:
                func_output = output[module.body.index(func)]

                returns = ReturnFromGeneratorTransformer._find_generator_returns(
                    ReturnFromGeneratorTransformer(), func)
                for _, return_ in returns:
                    assert_code_equal(
                        ReturnFromGeneratorTransformer()._replace_return(func, return_),
                        func_output
                    )

    assert_return_in_generator_transformed_correctly('fn')
    assert_return

# Generated at 2022-06-14 02:09:01.906304
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:05.921939
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from . import from_pyversion
    transformer = from_pyversion(ReturnFromGeneratorTransformer)

    class TestCase(unittest.TestCase):
        pass


# Generated at 2022-06-14 02:09:18.915219
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class TestReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer):

        @property
        def _tree_changed(self):
            return self.__tree_changed

        @_tree_changed.setter
        def _tree_changed(self, val):
            self.__tree_changed = val

        def visit_Expr(self, node):
            return node

    node = ast.parse("""
    def fn():
        yield 1
        return 2
    """)
    transformer = TestReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)  # type: ignore
    assert transformer._tree_changed

# Generated at 2022-06-14 02:09:37.325003
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = '''\
    def single_yield():
        yield 2
        return 2
    def no_return():
        yield 2
    def simple_return():
        return 2
    '''
    expected = '''\
    def single_yield():
        yield 2
        exc = StopIteration()
        exc.value = 2
        raise exc
    def no_return():
        yield 2
    def simple_return():
        return 2
    '''
    assert ReturnFromGeneratorTransformer().visit(ast.parse(source)) == ast.parse(expected)

# Generated at 2022-06-14 02:09:48.188501
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTestCase

    class ReturnFromGeneratorTransformerTestCase(BaseNodeTestCase):
        transformer = ReturnFromGeneratorTransformer()
        target = (3, 2)
        node = "def fn():\n    \n    def inner():\n        a = 5\n        yield 3\n        return 2"
        expected = "def fn():\n    \n    def inner():\n        a = 5\n        yield 3\n        exc = StopIteration()\n        exc.value = 2\n        raise exc"

    ReturnFromGeneratorTransformerTestCase.check()
    ReturnFromGeneratorTransformerTestCase.check_not_changed("def fn():\n    \n    return 5")
    ReturnFromGeneratorTransformerTestCase.check_not_changed("")
    ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:59.559471
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    # Test 1
    module = ast.parse('''
    def fn(): 
        def fn1(): 
            yield 1 
            return 2
    ''')  # type: ast.AST
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(module)

    expected = '''
    def fn():
        def fn1():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
    '''
    assert ast.dump(module) == expected

    # Test 2
    module = ast.parse('''
    def fn():
        yield 1
        return 2
    ''')  # type: ast.AST
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(module)


# Generated at 2022-06-14 02:10:11.600041
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import transform_and_compile, check_transformation
    from .return_from_generator import ReturnFromGeneratorTransformer

    class TestCompile(transform_and_compile):
        def test_replace_return(self):
            class Test(transform_and_compile):
                transformer = ReturnFromGeneratorTransformer()
                code = """
                    def test():
                        yield 1
                        return 2
                """
                expected_code = """
                    def test():
                        yield 1
                        exc = StopIteration()
                        exc.value = 2
                        raise exc
                """
            Test()

        def test_ignore_return_inside_function(self):
            class Test(transform_and_compile):
                transformer = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:10:24.017084
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import unittest
    import typed_astunparse  # type: ignore

    class TestCase(unittest.TestCase):
        def test_change_on_return_in_generator(self):
            def test():
                def fn():
                    yield 5
                    return 6

            node = ast.parse(test.__doc__)
            ReturnFromGeneratorTransformer().visit(node)
            unparse_result = typed_astunparse.unparse(node)
            assert unparse_result == test.__doc__.strip()[:-1] + '''
    def fn():
        yield 5
        exc = StopIteration()
        exc.value = 6
        raise exc
'''.strip() + '\n'


# Generated at 2022-06-14 02:10:34.529285
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class FakeCode:
        _code = ""

        def __init__(self, code: str):
            self._code = code

        def co_filename(self) -> str:
            return "File"

        def co_firstlineno(self) -> int:
            return 1

        def __repr__(self) -> str:
            return self._code

    class FakeFuncCode:
        _code = None

        def __init__(self, code: str):
            self._code = FakeCode(code)

        def __repr__(self) -> str:
            return repr(self._code)

    source = """
                def func():
                    return 4
                """
    source_ast = ast.parse(source)

    source2 = """
                def func2():
                    return 4
                """
    source_ast

# Generated at 2022-06-14 02:10:36.662214
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_python import Function
    from typed_ast import ast3

# Generated at 2022-06-14 02:10:46.819451
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("""
        def fn(a, b):
            yield 1
            b.fn()
            return 4
        """)
    expected_node = ast.parse("""
        def fn(a, b):
            yield 1
            b.fn()
            exc = StopIteration()
            exc.value = 4
            raise exc
        """)
    actual_node = ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(actual_node) == ast.dump(expected_node)

# Generated at 2022-06-14 02:10:52.894578
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import ast
    import astunparse
    from ..utils.context import Context

    def parse_and_transform(code):
        module = ast.parse(code)
        transformer = ReturnFromGeneratorTransformer(Context())
        transformer.visit(module)
        return module


# Generated at 2022-06-14 02:11:04.734672
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class ReturnFromGeneratorTransformerSubclass(ReturnFromGeneratorTransformer):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            self._tree_changed = None
            return_node = ast.Return()

            code = '''
            def gen():
                yield 1
                return 5
            '''
            tree = ast.parse(code)
            node = tree.body[0]
            node: ast.FunctionDef

            return_from_generator_transformer = ReturnFromGeneratorTransformerSubclass()
            return_from_generator_transformer.visit(node)
            assert return_from_generator_transformer._tree_changed == True

# Generated at 2022-06-14 02:11:27.686127
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_helpers import run_transformer_on_function_body
    from .test_helpers import run_simple_function_test

    def test_function(a):
        yield a
        return True

    source = run_simple_function_test(test_function, "return_from_generator_transformer")


# Generated at 2022-06-14 02:11:34.663793
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("""
        def fn():
            x = yield 1
            return 5
    """)

    expected = ast.parse("""
        def fn():
            x = yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)

    actual = ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(expected) == ast.dump(actual)

# Generated at 2022-06-14 02:11:44.916457
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

    def test_basic():
        orig_code = """
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

        assert transformer.visit(ast.parse(orig_code)) == ast.parse(expected)

    def test_in_if_else():
        orig_code = """
        def fn():
            yield 1
            if True:
                return 5
            else:
                return 6
        """


# Generated at 2022-06-14 02:11:55.493560
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Test:
        """Test __init__.py in typed_astunparse/unparser.py"""
        def __init__(self):
            pass

        def fn1(self):
            yield 1
            return 5

        def fn2(self):
            if True:
                pass
            yield 1
            return 5

        def fn3(self):
            if True:
                pass
            yield 1
            if True:
                return 5
            return 10

        def fn4(self):
            yield 1
            try:
                return 5
            except:
                pass
            except:
                pass
            finally:
                pass
            return 10

        def fn5(self):
            pass
            return 10


# Generated at 2022-06-14 02:12:08.289229
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class TestReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer):
        def _find_generator_returns(self, node):
            return [
                (node, ast.Return(value=ast.Num(1))),
                (node, ast.Return(value=ast.Num(2)))
            ]

        def _replace_return(self, parent, return_):
            self.replaced_returns.append((parent, return_))


# Generated at 2022-06-14 02:12:17.414244
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from ..utils.source import source
    from .asserts import assert_program

    code = '''
    def fn():
        yield 1
        a = 1
        return 5
    '''

    module = ast.parse(code)
    transformer = ReturnFromGeneratorTransformer()
    module = transformer.visit(module)
    print(astor.to_source(module))
    expected = source('''
    def fn():
        yield 1
        a = 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    ''').strip()
    assert_program(module, expected)


# Generated at 2022-06-14 02:12:18.225860
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:19.386346
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:20.538293
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:22.986877
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_value import value_Transformer_visit_FunctionDef_Base

# Generated at 2022-06-14 02:13:02.348710
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    t = ReturnFromGeneratorTransformer()

    def test(node_str: str, expected: ast.AST) -> None:
        node = ast.parse(node_str)
        result = t.visit(node)
        assert ast.dump(result) == ast.dump(expected), node_str

    test('def fn(): yield 1',
         ast.parse('def fn(): yield 1'))
    test('def fn(): yield 1\nreturn',
         ast.parse('def fn(): yield 1\nreturn'))
    test('def fn(): yield 1\nreturn 5',
         ast.parse('def fn(): yield 1; exc = StopIteration(); exc.value = 5; raise exc'))

# Generated at 2022-06-14 02:13:04.334477
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:11.299747
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""def my_generator():
        yield 1
        return 5""")
    expected_tree = ast.parse("""def my_generator():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc""")
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)
    assert ast.dump(tree) == ast.dump(expected_tree)


# Generated at 2022-06-14 02:13:17.940178
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("""
        def fn():
            yield 1
            return 2
    """).body[0]
    desired = ast.parse("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
    """).body[0]
    actual = ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(desired) == ast.dump(actual)

# Generated at 2022-06-14 02:13:30.423234
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_equal_ast
    from ..parser import parse
    from .remove_return_value_from_none_transformer import RemoveReturnValueFromNoneTransformer
    from .inline_multiline_lambda_transformer import InlineMultilineLambdaTransformer

    # [return_value] -> return_value
    node = parse("""
        def fn():
            yield 1
            return 2
    """)

    expected = parse("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
    """)

    actual = ReturnFromGeneratorTransformer().visit(node)

    actual = RemoveReturnValueFromNoneTransformer().visit(actual)
    actual = InlineMultilineLambdaTransformer().visit(actual)



# Generated at 2022-06-14 02:13:33.187322
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()


# Generated at 2022-06-14 02:13:42.082654
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.fixtures import function_with_yield
    from .base import BaseNodeTransformer, parse

    class TestReturnFromGeneratorTransformer(BaseNodeTransformer):
        target = (3, 2)

        def visit_Yield(self, node):
            assert isinstance(node, ast.Yield)
            assert len(node.value.args) == 1
            return node

        def visit_Lambda(self, node):
            assert isinstance(node, ast.Lambda)
            assert len(node.args.args) == 1
            return node

    module_node = parse(function_with_yield.src)
    ReturnFromGeneratorTransformer(target=(3, 2)).visit(module_node)
    TestReturnFromGeneratorTransformer().visit(module_node)
    assert module_node

# Generated at 2022-06-14 02:13:51.035800
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import compile_snippet, compare_ast

    source = """
    def fn():
        yield 1
        return 5
    """

    expected_source = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    tree = ast.parse(source)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    actual_code = compile_snippet(tree)
    expected_tree = ast.parse(expected_source)
    compare_ast(expected_tree, tree)
    assert eval(actual_code) == 5



# Generated at 2022-06-14 02:14:02.184221
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.macros import treewalk
    from .nodes import FunctionDef, Return

    def fn():
        a = 1
        if a:
            return 5

    def fn():
        a = 1
        if a:
            yield 1
            return 5

    def fn():
        pass

    def fn():
        yield 1
        print(5)
        return 7

    def fn():
        yield 1
        print(5)
        return 7

    def fn():
        a = 1
        for i in range(10):
            if a:
                yield 5

            return 7


# Generated at 2022-06-14 02:14:15.725278
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    from .visit import visit

    code = """
        def simple_generator():
            yield 1
            return 5

        def simple_generator_with_yield_from():
            yield from range(5)
            return 5

        def simple_generator_with_if():
            yield 1
            return 5

        def simple_function():
            return 5

        def simple_function_with_if():
            return 5

        def simple_function_with_while():
            return 5

        def simple_function_with_while_and_if():
            return 5
    """