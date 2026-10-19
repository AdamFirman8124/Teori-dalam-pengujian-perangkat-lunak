

# Generated at 2022-06-14 02:06:07.907768
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:17.543234
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

    # assert transformer.visit(ast.parse("def a():\
    #     def b():\
    #         return 5")) == ast.parse("def a():\
    #     def b():\
    #         return 5")

    assert transformer.visit(ast.parse("def a():\
        yield 1\
        return 5")) == ast.parse("def a():\
        yield 1\
        exc = StopIteration()\
        exc.value = 5\
        raise exc")

    assert transformer.visit(ast.parse("def a():\
        def b():\
            return 5")) == ast.parse("def a():\
        def b():\
            return 5")


# Generated at 2022-06-14 02:06:27.568825
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import unittest

    class TestReturnFromGeneratorTransformer_visit_FunctionDef(unittest.TestCase):
        def test_find_generator_returns(self):
            source = '''\
            def demo():
                yield 1
                return 5
            '''
            tree = ast.parse(source)


# Generated at 2022-06-14 02:06:37.721241
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """\
    def func():
        x = 1
        if x == 1:
            y = 2
            while y < 5:
                yield 1
                y += 1
                if y > 3:
                    return 2

        return 3

    def func2():
        x = 1
        if x == 1:
            y = 2
            while y < 5:
                yield 1
                y += 1
                if y > 3:
                    return x + 2

        return 3

    def func3():
        x = 1
        y = 2
        while y < 5:
            yield 1
            y += 1
            if y > 3:
                return x + 2

        return 3
    """


# Generated at 2022-06-14 02:06:48.359596
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from pprint import pprint
    from typed_astunparse import unparse
    from .stubgen import generate_stubs
    from .base import BaseNodeTransformer
    from .rename_builtins import RenameBuiltinsTransformer
    from .typing_imports import TypingImportsTransformer
    from .type_aliases_imports import TypeAliasesImportsTransformer
    import sys

    transforms = [RenameBuiltinsTransformer, TypingImportsTransformer, TypeAliasesImportsTransformer,
                  ReturnFromGeneratorTransformer]
    test_cases = generate_stubs('chaining', transforms=transforms)
    failures = []

    for source, target in test_cases:
        source_ast = ast.parse(source)

# Generated at 2022-06-14 02:06:53.129410
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    mod = ast.parse(textwrap.dedent('''\
        def goo():
            yield 1
            print(1)
            return 2
        '''))

    expected_mod = textwrap.dedent('''\
        def goo():
            yield 1
            print(1)
            exc = StopIteration()
            exc.value = 2
            raise exc
        ''')

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(mod)
    assert ast.unparse(mod) == expected_mod

# Generated at 2022-06-14 02:07:06.215328
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Expected result
    expected = """
    @types.coroutine
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    # Code to be transformed
    code = """
    @types.coroutine
    def fn():
        yield 1
        return 5
    """

    # Perform transformation
    module_ast = ast.parse(code)
    fn_ast = module_ast.body[0]
    ReturnFromGeneratorTransformer().visit(fn_ast)

    # Check that transformation was successfull
    module_code = compile(module_ast, filename="<ast>", mode="exec")
    namespace = {}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        exec(module_code, namespace)

# Generated at 2022-06-14 02:07:20.400174
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    return_value = ast.Num(n=10)
    return_from_generator_snippet = [
        ast.Assign(targets=[ast.Name(id='exc', ctx=ast.Store())],
                   value=ast.Call(func=ast.Name(id='StopIteration', ctx=ast.Load()),
                                  args=[], keywords=[])),
        ast.Assign(targets=[ast.Attribute(value=ast.Name(id='exc', ctx=ast.Load()),
                                          attr='value', ctx=ast.Store())],
                   value=return_value),
        ast.Raise(exc=ast.Name(id='exc', ctx=ast.Load()), cause=None)
    ]


# Generated at 2022-06-14 02:07:33.025158
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    test_case = ReturnFromGeneratorTransformer()

    class_node = ast.ClassDef('TestClass', [ast.arg('object', None)], [], [], [])

    return_node = ast.Return(ast.Constant(1))
    function_node = ast.FunctionDef('test_function',
                                    ast.arguments([], None, None, []),
                                    [ast.Expr(ast.Constant(None))],
                                    [],
                                    ast.arguments([], None, None, []),
                                    [return_node])

    class_node.body.append(function_node)

    new_parent = test_case.visit(class_node)

    assert len(new_parent.body) == 1
    assert isinstance(new_parent.body[0], ast.ClassDef)

   

# Generated at 2022-06-14 02:07:45.212106
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import cst_to_ast
    transformer = ReturnFromGeneratorTransformer()

    # before

# Generated at 2022-06-14 02:07:51.419065
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:00.720440
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # This is an example of the code that ReturnFromGeneratorTransformer gets as input
    # (only a part of it, the whole code is too big to appear here).
    #
    # Note that this example is taken from cpython/test_ast.py (test_genexp_return).
    # Also note that the code was slightly modified to fit the requirements of ReturnFromGeneratorTransformer.
    input = """\
if 0:
    def _gen():
        return (yield from (yield y for i in range(5)))
else:
    def _gen():
        yield from (yield from (yield y for i in range(5)))
"""
    # Here is what ReturnFromGeneratorTransformer is expected to produce.

# Generated at 2022-06-14 02:08:07.583951
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Simple case with single return
    code = "def fn():\n    yield 1\n    return 5"
    expected = "def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc"
    assert ReturnFromGeneratorTransformer().visit(ast.parse(code)) == ast.parse(expected)
    # TODO: more cases

# Generated at 2022-06-14 02:08:15.841970
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    return_value = ast.copy_location(
        ast.Name(id='None', ctx=ast.Load()),
        ast.Return(value=ast.Num(n=5), lineno=3, col_offset=8),
    )


# Generated at 2022-06-14 02:08:29.200530
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseTraceVisitor
    class_name = "ReturnFromGeneratorTransformer"
    function_name = "visit_FunctionDef"
    test_counter = 0
    test_counter += 1
    # test_counter is 1
    def test_f():
        def foo():
            yield 1
            return 5
        return foo
    visitor = BaseTraceVisitor(class_name, function_name, test_counter)
    ReturnFromGeneratorTransformer().visit(test_f())
    visitor.check(test_f())
    test_counter += 1
    # test_counter is 2
    def test_f():
        def foo():
            yield 1
            return 5
        def foo2():
            yield 2
            return 6
        return foo, foo2

# Generated at 2022-06-14 02:08:38.208600
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testing import transform_snippet, assert_snippet

    def fn():
        yield 1
        return 5

    assert type(fn()).__name__ == 'generator'
    x = next(fn())
    assert x == 1
    x = next(fn())
    assert x == 5

    result = transform_snippet(fn, ReturnFromGeneratorTransformer)
    expected = """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc"""

    assert_snippet(result, expected)

# Generated at 2022-06-14 02:08:44.188206
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .utils import from_source
    from .test_remove_decorator import test_RemoveDecoratorTransformer_visit_FunctionDef

    expected = test_RemoveDecoratorTransformer_visit_FunctionDef()


# Generated at 2022-06-14 02:08:51.586048
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from . import register

# Generated at 2022-06-14 02:09:03.063032
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Testing for the if condition
    def_node = ast.parse("""def fn():
        yield 1
        return 5
    """)
    transformer = ReturnFromGeneratorTransformer()
    res = transformer.visit(def_node)
    assert len(res.body[0].body) == 3
    assert isinstance(res.body[0].body[1], ast.Expr)
    assert isinstance(res.body[0].body[2], ast.Raise)

    # Testing for the else condition
    def_node = ast.parse("""def fn():
        yield 1
        yield 2
        return 5
    """)
    transformer = ReturnFromGeneratorTransformer()
    res = transformer.visit(def_node)
    assert len(res.body[0].body) == 5

# Generated at 2022-06-14 02:09:09.678346
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse  # type: ignore
    from ..test_utils import transform_test  # type: ignore

    code = '''
        def fn():
            yield 1
            return 5
    '''

    expected_code = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''

    transform_test(ReturnFromGeneratorTransformer, code, expected_code)

# Generated at 2022-06-14 02:09:24.766469
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import ast
    tree = ast.parse("""def fn():\n    yield 1\n    return 5""")
    tr = ReturnFromGeneratorTransformer()
    tr.visit(tree)

# Generated at 2022-06-14 02:09:27.953663
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import CompileError
    from .base_transformer_test import BaseTransformerTest, get_assert_equal_ast


# Generated at 2022-06-14 02:09:40.037373
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Test:
        def __init__(self):
            self._tree_changed = False
    Test._tree_changed = False
    Test._parent = None
    Test._stack = [None]
    Test.generic_visit = lambda self, node: node

    class AST_tree_1(ast.AST):
        _fields = ('body',)

    tree = AST_tree_1()
    tree.body = []

    obj = ReturnFromGeneratorTransformer()

    def test_func():
        def non_generator_no_returns():
            pass
        def non_generator_with_returns():
            return 1
        def generator():
            for i in range(10):
                yield i
        def generator_with_inner_returns():
            def inner():
                return "inner"
            return inner()


# Generated at 2022-06-14 02:09:50.275996
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.test_visitor import run_test
    from ..utils.source_to_snippet import source_to_snippet

    def test_fn(fn):
        fn_source = 'def fn():\n' + '\n'.join(['    ' + x for x in fn.split('\n')]) + '\n'
        fn_ast = source_to_snippet(fn_source)
        visitor = ReturnFromGeneratorTransformer()
        visitor.visit(fn_ast)

        # Result can be passed to snippet
        assert isinstance(fn_ast, ast.FunctionDef)


# Generated at 2022-06-14 02:09:56.984477
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class _C:
        @staticmethod
        def fn() -> int:
            for i in range(2):
                yield i
                return 5
    assert ReturnFromGeneratorTransformer._find_generator_returns(
        ast.parse(_C.fn.__doc__).body[0]) == [
            (ast.parse(_C.fn.__doc__).body[0].body[1],
             ast.parse(_C.fn.__doc__).body[0].body[1].body[1])
        ]



# Generated at 2022-06-14 02:10:09.890510
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import round_trip

    tr = ReturnFromGeneratorTransformer()
    tree1 = round_trip('''
        def fn():
            yield 5
            return 1
    ''')
    # The line `return 2` is not changed because a generator can return only one value.
    # The multiple return values are converted to a tuple and passed as the value.
    tree2 = round_trip('''
        def fn():
            yield 1
            return 2
            return 3
    ''')
    tree3 = round_trip('''
        def fn():
            yield 1
            return 2
            return 3
            raise Exception()
    ''')
    # The line `return None` is not changed because None is the default value of
    # the `value` field for the exception.
    tree4 = round_trip

# Generated at 2022-06-14 02:10:16.245642
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert_source_equal(
        ReturnFromGeneratorTransformer().visit(ast.parse("""
        @fn
        def f():
            yield 1
            return 1
        """)),
        """
        @fn
        def f():
            yield 1
            exc = StopIteration()
            exc.value = 1
            raise exc
        """
    )

# Generated at 2022-06-14 02:10:27.535121
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test 1: Test simple no return case
    fn = ast.FunctionDef(
        name="func",
        body=[
            ast.Expr(
                value=ast.Str(s="Hello world"),
            ),
        ],
    )

    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(fn)  # type: ignore
    assert result == fn

    # Test 2: Function returns generator with return
    fn = ast.FunctionDef(
        name="func",
        body=[
            ast.FunctionDef(
                name="simple_gen",
                body=[
                    ast.Return(
                        value=ast.Num(
                            n=5,
                        )
                    )
                ],
            ),
        ],
    )

    transformer = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:10:36.538004
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    '''Test of method visit_FunctionDef of class ReturnFromGeneratorTransformer'''
    # Test 1.

# Generated at 2022-06-14 02:10:50.582802
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..main import transform
    from .asserts import assert_program

    code = '''
        def fn():
            yield 1
            return 5
        fn()
    '''

    expected = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        fn()
    '''

    assert_program(
        transform(
            code,
            [ReturnFromGeneratorTransformer],
        ),
        expected,
    )

    code = '''
        def fn():
            try:
                yield 1
            finally:
                return 5
        fn()
    '''


# Generated at 2022-06-14 02:11:01.301358
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:02.748290
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import node_transformers

    # Initial ast

# Generated at 2022-06-14 02:11:16.728611
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.context import Context
    from ..utils.messages import Message

    generator = '''def fn():
    yield 1
    return 5'''

    expected = '''def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc'''

    tree = ast.parse(generator)
    ctx = Context(min_python_version=(3, 2), max_python_version=None)

    transformer = ReturnFromGeneratorTransformer(ctx)
    new_tree = transformer.visit(tree)
    generated_code = compile(new_tree, '<string>', 'exec')
    generated_code = str(generated_code)
    generated_code = generated_code[generated_code.index('def fn'):]

   

# Generated at 2022-06-14 02:11:18.194246
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import typed_ast.ast3 as ast

# Generated at 2022-06-14 02:11:25.983755
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_one_return():
        @snippet
        def fn():
            yield 1
            return 5

        t = ReturnFromGeneratorTransformer()
        t.visit(fn)
        assert fn() == [1]
        assert list(fn()) == [1]
        assert list(fn()) == []
        assert list(fn()) == []
        assert next(fn()) == 1
        assert next(fn()) == 5

    def test_two_returns():
        @snippet
        def fn():
            yield 1
            return 5
            yield 10

        t = ReturnFromGeneratorTransformer()
        t.visit(fn)
        assert fn() == [1]
        assert list(fn()) == [1]
        assert list(fn()) == []
        assert list(fn()) == []

# Generated at 2022-06-14 02:11:38.096155
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:40.347323
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:53.228204
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    snippet_1 = """
    def generator():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """
    expected_1 = """
    def generator():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """
    # Using snippets when assertion fails
    assert ReturnFromGeneratorTransformer.snippet_visit(
        snippet_1, check_snippets=True) == (snippet_1, expected_1)

    snippet_2 = """
    def generator():
        yield 1
        return 2
    """
    expected_2 = """
    def generator():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """

    assert ReturnFromGeneratorTransformer.snipp

# Generated at 2022-06-14 02:11:54.676590
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:07.418546
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    classifier = ReturnFromGeneratorTransformer()
    def f():
        yield 1
        return 2
    with_returns = ast.parse(inspect.getsource(f))
    assert (astor.to_source(with_returns) ==
            'def f():\n    yield 1\n    return 2\n')
    classifier.visit(with_returns)
    assert (astor.to_source(with_returns) ==
            'def f():\n    yield 1\n    exc = StopIteration()\n    exc.value = 2\n    raise exc\n')
    def f():
        yield 1
    without_returns = ast.parse(inspect.getsource(f))

# Generated at 2022-06-14 02:12:32.859204
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent
    from ..utils.source_gen import SourceGen
    from ..utils.tests import node_equal

    source = dedent('''
        def fn():
            yield 1
            return 5
    ''')
    expected = dedent('''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    ''')
    node = ast.parse(source)
    expected_node = ast.parse(expected)
    ReturnFromGeneratorTransformer(SourceGen()).visit(node)
    assert node_equal(node, expected_node)



# Generated at 2022-06-14 02:12:34.334760
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:42.365705
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class CollectVisitor(ast.NodeVisitor):
        def __init__(self):
            self.result = ''

        def visit_Return(self, node):
            if isinstance(node.value, ast.Str):
                self.result += node.value.s
            else:
                self.result += node.value.id

        def visit_Assign(self, node):
            self.result += node.targets[0].id

        def visit_Raise(self, node):
            self.result += 'raise_'


# Generated at 2022-06-14 02:12:44.974758
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    '''
    Test the ReturnFromGeneratorTransformer visitor method visit_FunctionDef
    '''


# Generated at 2022-06-14 02:12:47.149216
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
  """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer"""

# Generated at 2022-06-14 02:12:58.012598
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse
    from typed_ast.ast3 import Assign, Name, Store, FunctionDef, Return
    from typed_ast.ast3 import AugAssign, Add
    from typed_ast.ast3 import Try, TryExcept, ExceptHandler, Pass
    from typed_ast.ast3 import ExceptHandler
    from typed_ast.ast3 import Constant, Str, ExceptHandler

    def fn1():
        yield 1
        return 5

    def fn2():
        yield 1
        return
        yield 2

    def fn3():
        yield 1
        try:
            return 5
        except:
            pass

    def fn4():
        yield 1
        try:
            return 5
        finally:
            pass

    def fn5():
        yield 1
        except_instance_var = None

# Generated at 2022-06-14 02:13:11.578985
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code1 = """
    def fn():
        yield 1
        return 5
    """
    compiled_code1 = ast.parse(code1, "<string>")
    ReturnFromGeneratorTransformer().visit(compiled_code1)

# Generated at 2022-06-14 02:13:17.442149
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def gen():
        yield
        return 5

    def test():
        yield
        yield 5

    tree = ast.parse(dedent(gen.__doc__))
    tree2 = ast.parse(dedent(test.__doc__))

    assert ReturnFromGeneratorTransformer().visit(tree) == ReturnFromGeneratorTransformer().visit(tree2)

# Generated at 2022-06-14 02:13:28.862543
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """
    def f():
        pass
    """
    expected = """
    def f():
        pass
    """
    with override_config(
            'DICT_CMP',
            'ALWAYS_EAGER',
            'ORDER_RESULT',
            'USE_BARE_EXCEPT',
            'RETURN_FROM_GENERATORS',
            True):
        for input_code, expected_output in [
                (source, expected)
        ]:
            tree = ast.parse(input_code)
            tree = ReturnFromGeneratorTransformer().visit(tree)
            assert ast.dump(tree, include_attributes=False) == expected_output



# Generated at 2022-06-14 02:13:35.287964
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test-1a
    assert ReturnFromGeneratorTransformer().run_single(
        '''
        def fn():
            yield 1
            return 5
        '''
    ) == \
    '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''

    # Test-1b
    assert ReturnFromGeneratorTransformer().run_single(
        '''
        def fn():
            yield 1
            return 5
        '''
    ) == \
    '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''

    # Test-1c

# Generated at 2022-06-14 02:14:16.967884
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ast_toolbox.common import parse
    from ast_toolbox.common import dump
    ft1 = "def fn(): yield 1; return 5"
    ft2 = "def fn(): yield 1; return"
    ft3 = "def fn(): return 5"
    ft4 = "def fn(): return"
    ft5 = "def fn(): yield 1"

    ast_nodes = [parse(ft1), parse(ft2), parse(ft3), parse(ft4), parse(ft5)]
    t = ReturnFromGeneratorTransformer()
    for node in ast_nodes:
        t.generic_visit(node)
        print(dump(node))

# Generated at 2022-06-14 02:14:23.280020
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """def fn():
        yield 1
        return 5"""
    ast_ = ast.parse(code)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(ast_)

    expected = """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc"""
    expected_ast = ast.parse(expected)
    assert ast_.body[0].body == expected_ast.body[0].body


# Generated at 2022-06-14 02:14:35.875798
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    def fn(a: int, b: int) -> int:
        yield a
        return b

    func_def = ast.parse(fn.__text__).body[0]
    transformer = ReturnFromGeneratorTransformer()

    assert transformer.visit(func_def) == ast.parse(fn.__text__ + '\n').body[0]

    func_def = ast.parse(fn.__text__).body[0]
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(func_def)

    assert func_def == ast.parse(
        """@snippet
        def fn(a, b):
            yield a
            exc = StopIteration()
            exc.value = b
            raise exc""").body[0]

# Generated at 2022-06-14 02:14:46.231064
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    import textwrap

    source = textwrap.dedent('''\
    def f():
        yield 0
        return 1
    ''')
    source_ast = ast.parse(source)
    transpiled_ast = ReturnFromGeneratorTransformer().visit(source_ast)
    transpiled_source = astor.to_source(transpiled_ast)
    print(transpiled_source)

    assert transpiled_source == textwrap.dedent('''\
    def f():
        yield 0
        exc = StopIteration()
        exc.value = 1
        raise exc
    ''')

# Generated at 2022-06-14 02:14:54.837092
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    src_code = """
        def fn():
            yield 1
            return 2
    """
    expected_code = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
    """
    module = ast.parse(src_code)
    actual_module = ReturnFromGeneratorTransformer().visit(module)
    expected_module = ast.parse(expected_code)

    assert ast.dump(expected_module, include_attributes=True) == ast.dump(actual_module, include_attributes=True)


# Generated at 2022-06-14 02:15:02.674297
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_helpers import (
        assert_transformed_ast,
        read_snippet,
        assert_syntax_error
    )

    snippet = read_snippet('snippets/return_from_generator.py')

    assert_transformed_ast(
        ReturnFromGeneratorTransformer,
        snippet,
        'snippets/return_from_generator_transformed.py'
    )
    # TODO: Add syntax errors related to return from generator

# Generated at 2022-06-14 02:15:14.219595
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent
    from ..utils.source_helpers import source
    from ..utils.ast_helpers import dump, compare_source

    code1 = dedent("""
        def foo():
            yield 1
            return 5
    """)
    code2 = dedent("""
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)
    code3 = dedent("""
        def foo():
            return 5
    """)
    code4 = dedent("""
        def foo():
            yield 1
            return
            yield 2
            return 5
            return
            yield 3
            return 6
    """)

# Generated at 2022-06-14 02:15:16.529009
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..visitor import NodeTransformerVisitor
    from typed_ast import parse


# Generated at 2022-06-14 02:15:25.432863
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source import source

    source_
    def fn_before(x):
        for y in x:
            if y == 2:
                return 'a'
            yield y

    def fn_after(x):
        for y in x:
            if y == 2:
                exc = StopIteration()
                exc.value = 'a'
                raise exc
            yield y

    node = ast.parse(source(fn_before))
    node = ReturnFromGeneratorTransformer().visit(node)
    src = source(fn_after).strip()
    assert source(node) == src



# Generated at 2022-06-14 02:15:38.163116
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from python_minifier.transformers import ReturnFromGeneratorTransformer
    from python_minifier.utils.source import Source
    from python_minifier.utils.test import assert_no_difference
    from .test_base import BaseNodeTransformerTest

    class ReturnFromGeneratorTransformerTest(BaseNodeTransformerTest):
        transformer = ReturnFromGeneratorTransformer

        def test_simple(self):
            @assert_no_difference(
                """
                def f():
                    yield 5
                    return 9
                """
            )
            def test():
                def f():
                    yield 5
                    return 9
                self.transform(f)
