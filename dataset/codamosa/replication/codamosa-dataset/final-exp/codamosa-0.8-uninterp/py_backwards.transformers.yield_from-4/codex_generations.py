

# Generated at 2022-06-14 02:39:02.069695
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  print('Start test_YieldFromTransformer')
  py_code = """
  x = 1
  if x == 1:
    yield from iterable
  else:
    yield from iterable
  """
  py_ast = ast.parse(py_code)
  trans = YieldFromTransformer()
  try:
    a = trans.visit(py_ast)
  except Exception as e:
    print(e)
  print('End test_YieldFromTransformer')

# Generated at 2022-06-14 02:39:03.519507
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:39:06.447228
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().__class__.__name__ == 'YieldFromTransformer'


# Generated at 2022-06-14 02:39:16.593616
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import parse
    from .. import mypy
    from ..common import CompilationError

    class TestTransformer(YieldFromTransformer):
        def __init__(self):
            self._tree_changed = False

        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            assert len(node.args.args) == 0
            assert isinstance(node.body[0], ast.Expr)
            assert isinstance(node.body[0].value, ast.YieldFrom)
            assert isinstance(node.body[1], ast.Return)
            assert isinstance(node.body[1].value, ast.Name)
            assert node.body[1].value.id == 'x'
            return node


# Generated at 2022-06-14 02:39:19.785872
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Simple test of constructor of class `YieldFromTransformer`."""
    t = YieldFromTransformer()


# Get node of `snippet` `result_assignment`

# Generated at 2022-06-14 02:39:23.682234
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class A(YieldFromTransformer):
        pass

    assert A.__name__ == 'YieldFromTransformer'
    assert A.__qualname__ == 'YieldFromTransformer'


# Generated at 2022-06-14 02:39:24.693333
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()

# Generated at 2022-06-14 02:39:29.873046
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert_equal(YieldFromTransformer.__name__,
                 'YieldFromTransformer')
    assert_equal(YieldFromTransformer.__module__,
                 __name__)
    assert_equal(YieldFromTransformer.target,
                 (3, 2))
    assert_equal(YieldFromTransformer.__doc__,
                 'Compiles yield from to special while statement.')


# Generated at 2022-06-14 02:39:35.201007
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import codegen
    from ..utils.tree import print_tree
    from .utils import test_ast

    source = r"""
    def func(generator):
        a = yield from generator
        print(yield from generator)
        yield from generator
    """

    tree = test_ast(source, YieldFromTransformer)
    result = codegen.to_source(tree)
    print(result)

# Generated at 2022-06-14 02:39:43.816940
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import test_utils
    from .. import utils
    from ast_helpers import print_ast, to_source
    from ..utils import ast_utils
    import astor

    tree = test_utils.build_ast_from_snippet(yield_from)
    ex = YieldFromTransformer()
    tree_transformed = ex.generic_visit(tree)
    source = ast_utils.to_source(tree_transformed)
    assert source == """
    iterable = iter(generator)
    while True:
        try:
            yield next(iterable)
        except StopIteration as exc:
            target = exc.value
            break
    """
    args = {}
    args['generator'] = [1,2,3]
    exec(source, args)

# Generated at 2022-06-14 02:39:57.269317
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.tree import parse, dump
    from ..utils.helpers import compile_ as compile

    code = """
    def test_single_expr(x):
        yield from x

    def test_single_expr_with_target(x):
        a = yield from x

    def test_multiple_expr(x):
        a = 1
        yield from x
        a = 1

    def test_multiple_expr_with_target(x):
        a = 1
        b = yield from x
        a = 1

    """
    tree = parse(code)
    YieldFromTransformer().visit(tree)

    code_actual = compile(dump(tree), 'str', 'exec')

# Generated at 2022-06-14 02:40:03.014854
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_jscode_transformers import tree

    try:
        print("[+] Testing YieldFromTransformer")
        instance = YieldFromTransformer()
        instance.visit(tree)
        print("[-] Testing YieldFromTransformer")
    except Exception as exc:
        print("[x] Testing YieldFromTransformer")
        raise exc



# Generated at 2022-06-14 02:40:04.812117
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)

# Generated at 2022-06-14 02:40:09.663878
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .testing import assert_transformation_results
    assert_transformation_results(
        YieldFromTransformer,
        '''
        def test():
            x = yield from range(10)
        '''
    )


__all__ = ['YieldFromTransformer']

# Generated at 2022-06-14 02:40:23.777508
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()

    tree = ast.parse('def foo():\n    a = yield from b')
    transformed = ast.parse('def foo():\n    let(iterable)\n    iterable = iter(b)\n    while True:\n        try:\n            yield next(iterable)\n        except StopIteration as exc:\n            a = exc.value\n            break')

    assert transformer.visit(tree) == transformed

    tree = ast.parse('def foo():\n    yield from b')
    transformed = ast.parse('def foo():\n    let(iterable)\n    iterable = iter(b)\n    while True:\n        try:\n            yield next(iterable)\n        except StopIteration as exc:\n            break')

    assert transformer.visit(tree) == transformed

# Generated at 2022-06-14 02:40:33.537050
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Unit test for constructor of class YieldFromTransformer
    def test_get_yield_from_index(self):
        foo = ast.parse("foo()").body[0]
        self.assertIsNone(self._get_yield_from_index(foo, ast.Expr))
        self.assertIsNone(self._get_yield_from_index(foo, ast.Assign))

        yield_from = ast.parse("yield from foo()").body[0].value
        assign = ast.parse("x = yield from foo()").body[0]

        # Get YieldFrom node
        module = ast.Module([assign])
        self.assertEqual(self._get_yield_from_index(module, ast.Assign), 0)

        # Get another node

# Generated at 2022-06-14 02:40:45.969908
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import BaseNodeTransformerTest
    from ..utils.source import Source
    from typed_ast import ast3
    from textwrap import dedent

    yft = YieldFromTransformer()
    class Test(BaseNodeTransformerTest):
        transformer = yft
        code = Source(dedent('''
        def foo(x):
            import math

            y = yield from range(x)
            yield from y
        '''))

# Generated at 2022-06-14 02:40:54.021347
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .type_inference import TypeInferenceTransformer
    from .inline_functions import InlineFunctionsTransformer
    from .untype_variables import UntypeVariablesTransformer
    from ..utils.helpers import load_source, load_ast

    source = load_source('examples/yield_from.py')
    assert isinstance(source, str)
    tree = load_ast(source)
    assert isinstance(tree, ast.Module)
    assert not hasattr(tree, 'type_comments')

    tree = YieldFromTransformer.run_pipeline(tree)
    assert isinstance(tree, ast.Module)
    assert not hasattr(tree, 'type_comments')

    node = TypeInferenceTransformer.run_pipeline(tree)
    assert isinstance(node, ast.Module)


# Generated at 2022-06-14 02:41:05.765775
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    def test_case(input_str, expected):
        node = ast.parse(input_str)
        expected_node = ast.parse(expected)
        t = YieldFromTransformer()
        result = t.visit(node)
        assert ast.dump(result) == ast.dump(expected_node)

    test_case("""
yield from func()
""", """
let(iterable)
iterable = iter(func())
while True:
    try:
        yield next(iterable)
    except StopIteration as exc:
        break
""")


# Generated at 2022-06-14 02:41:13.382714
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer(ast.parse('x = yield from y'))
    assert x._get_yield_from_index(ast.parse('x = yield from y'), ast.Assign) == 0
    assert x._get_yield_from_index(ast.parse('x = yield from y'), ast.Expr) is None

# Generated at 2022-06-14 02:41:25.546141
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        YieldFromTransformer()
    except NameError:
        assert False

# Generated at 2022-06-14 02:41:33.066906
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    with open(os.path.join(os.path.dirname(__file__),
              '../../tests/data/YieldFrom.py'), 'r') as input_file:
        tree = ast.parse(input_file.read())
        tree = YieldFromTransformer().visit(tree)
        ast.fix_missing_locations(tree)
        print(ast.dump(tree))

# Generated at 2022-06-14 02:41:36.806326
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = 3
    y = 1
    try:
        x = 2
        y = 4
    except:
        pass
    else:
        pass
    finally:
        pass
    return x, y


# Generated at 2022-06-14 02:41:37.593585
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:41:40.242812
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 02:41:49.062969
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .fixtures import tree

    assert YieldFromTransformer._get_yield_from_index(tree, ast.Assign) == -1
    assert YieldFromTransformer._get_yield_from_index(tree, ast.Expr) == -1
    tree.body[1] = ast.Assign((), ast.YieldFrom(tree.body[1].value))
    assert YieldFromTransformer._get_yield_from_index(tree, ast.Assign) == 1
    assert YieldFromTransformer._get_yield_from_index(tree, ast.Expr) == -1
    tree.body[1] = ast.Expr(ast.YieldFrom(ast.Name('a', ast.Load())))

# Generated at 2022-06-14 02:41:50.834025
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer({})

    # test special case: yield from with multiple assignments

# Generated at 2022-06-14 02:42:02.423303
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = '''
    def foo():
        a = yield from range(6)
        yield from range(6)
        yield from range(6)
        yield from range(6)
    '''
    module = ast.parse(code)

# Generated at 2022-06-14 02:42:09.640495
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # First test 
    i = 0
    j = 0
    a = YieldFromTransformer()
    for i in range(1, 5):
        for j in range(1, 5):
            assert a is not None
    # Second test
    b = YieldFromTransformer()
    if b is not None:
        assert b is not None
    else:
        for i in range(1, 5):
            for j in range(1, 5):
                assert b is not None

# Generated at 2022-06-14 02:42:12.706926
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_astunparse import dump
    from typed_ast.ast3 import parse
    import astunparse
    import astor
    import ast


# Generated at 2022-06-14 02:42:23.873882
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer


# Generated at 2022-06-14 02:42:26.158471
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import convert
    from ..utils.helpers import should_raise
    import ast
    from ..utils.tree import tree_to_str


# Generated at 2022-06-14 02:42:27.822808
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    obj = YieldFromTransformer()
    assert obj is not None


# Generated at 2022-06-14 02:42:29.020782
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:42:32.160367
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Unit test for method __init__ of class YieldFromTransformer
    assert YieldFromTransformer().__class__.__name__ == 'YieldFromTransformer'


# Generated at 2022-06-14 02:42:32.887216
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:42:34.094056
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:42:35.266637
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:37.004419
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer(): # noqa
    YieldFromTransformer()


# Generated at 2022-06-14 02:42:44.479320
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import BaseNodeTransformer
    from .unpacking import UnpackingTransformer
    from .yield_from import YieldFromTransformer
    from .generator_transform import GeneratorTransformTransformer
    from .return_transform import ReturnTransformTransformer
    from .for_if_transform import ForIfTransformer
    from ..rewriter import Rewriter
    import ast
    import astunparse


# Generated at 2022-06-14 02:43:05.879165
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass
# vim: set tabstop=4 shiftwidth=4 expandtab fdm=indent

# Generated at 2022-06-14 02:43:08.593119
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        YieldFromTransformer()
    except Exception:
        assert False


# Unit tests for _get_yield_from_index function in class YieldFromTransformer

# Generated at 2022-06-14 02:43:17.195276
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # setup YieldFromTransformer instance
    x = YieldFromTransformer()

    # define a AST of yield from
    y = ast.YieldFrom(value=ast.Name('i', ast.Load()))
    e = ast.Expr(value=y)
    a = ast.Assign(value=y, targets=[ast.Name('x', ast.Store())])

    # add the AST to a node
    n = ast.Module(body=[e, a])

    # run the transformer
    n = x.visit(n)

    # define a AST which corresponds to the yield from AST
    o = ast.Expr(value=ast.Name('o', ast.Load()))
    _ = ast.Store()
    _1 = ast.Name('x', _)
    _2 = ast.Store()
    _3

# Generated at 2022-06-14 02:43:19.856102
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert x._tree_changed == False

# Generated at 2022-06-14 02:43:21.094918
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer

# Generated at 2022-06-14 02:43:22.957463
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)

# Generated at 2022-06-14 02:43:31.776074
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    source = """
    def f():
        a = yield from range(0,10)
        return a

    def g():
        yield from range(0,10)

    def h():
        yield from range(0,10)
        yield
        yield from range(0,10)
    """

    tree = ast.parse(source)
    YieldFromTransformer().visit(tree)
    module = compile(tree, filename='<test>', mode='exec')
    globals = {'f':None,'g':None,'h':None}
    exec(module,globals)

    assert globals['f']().send(None) == 0
    assert globals['g']().send(None) == 0
    assert globals['h']().send(None) == 0

# Generated at 2022-06-14 02:43:33.014463
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:43:44.314162
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import BaseNodeTransformer

    class YieldFromTransformer(BaseNodeTransformer):
        """Compiles yield from to special while statement."""
        target = (3, 2)

        def _get_yield_from_index(self, node: ast.AST,
                                  type_: Type[Holder]) -> Optional[int]:
            if hasattr(node, 'body') and isinstance(node.body, list):  # type: ignore
                for n, child in enumerate(node.body):  # type: ignore
                    if isinstance(child, type_) and isinstance(child.value, ast.YieldFrom):
                        return n

            return None


# Generated at 2022-06-14 02:43:47.600015
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node1 = ast.parse('''
while True:
    yield from func()''')

    node1 = YieldFromTransformer().visit(node1)
    assert node1 is not None or node1 is not None

# Generated at 2022-06-14 02:44:41.960503
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Testing constructor of class YieldFromTransformer"""


# Generated at 2022-06-14 02:44:43.234532
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    with pytest.raises(TypeError):
        YieldFromTransformer(None)

# Generated at 2022-06-14 02:44:44.548660
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pipeline = YieldFromTransformer()
    assert pipeline is not None

# Generated at 2022-06-14 02:44:46.116175
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:44:47.545907
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().target == (3, 2)



# Generated at 2022-06-14 02:44:56.758250
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.source import source

    tree = ast.parse(source('''
        class C:
            def g(self):
                yield from x

            yield from x
            yield from x + y
    '''))


# Generated at 2022-06-14 02:45:03.557401
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    if get_python_version() != (3,5):
        return
    from ..compat import StringIO

    # Test with class instantiation
    yield_from_transformer = YieldFromTransformer()

    # Test without class instantiation
    actual = StringIO()
    with redirect_stdout(actual):
        YieldFromTransformer.transform(None, None,
                                       "from future_builtins import map\n"
                                       "yield from map(f, i)")

        expected =  ""
        assert expected == actual.getvalue()

# Generated at 2022-06-14 02:45:05.761904
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .helpers import get_test_data

    root = get_test_data(__file__, "data/yield_from.py")
    YieldFromTransformer().visit(root)

# Generated at 2022-06-14 02:45:06.578396
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  assert True

# Generated at 2022-06-14 02:45:16.126984
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():

    assert issubclass(YieldFromTransformer, BaseNodeTransformer)

    # init test
    transformer = YieldFromTransformer()

    testcode = "def fun1(a):\n" \
               "    yield(frm)\n" \
               "    yield(from)\n" \
               "    yield\n" \
               "    yield from bla\n"
    expected_code = "\ndef fun1(a):\n" \
                    "    yield from bla\n" \
                    "    yield from bla\n" \
                    "    yield\n" \
                    "    yield from bla\n"
    tree = ast.parse(testcode)
    tree = transformer.visit(tree)
    print(ast.dump(tree))
    assert ast.dump(tree) == expected_code



# Generated at 2022-06-14 02:47:06.443356
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse('yield from result')
    YieldFromTransformer().visit(tree)
    yield_from_pass_body = ast.parse("""
        iterable = iter(result)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                break
    """)
    assert tree.body == yield_from_pass_body.body

# Generated at 2022-06-14 02:47:09.920372
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.node_finder import get_node_at
    from ..utils.helpers import compact_ast
    from ..context import Context
    from ..parser.parser import parse_text
    from ..parser.parser import parse_code
    from ..core import MicroMock


# Generated at 2022-06-14 02:47:12.023467
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer._create_subclass({}) is not None

# Generated at 2022-06-14 02:47:12.764929
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:47:14.015414
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:47:15.157189
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3

# Generated at 2022-06-14 02:47:17.253397
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:47:20.933705
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import to_source
    from ..utils.tree import get_ast

    source = '''
        def f():
            yield 1
            yield 2
    '''
    tree = get_ast(source)
    transformed = YieldFromTransformer().visit(tree)
    assert to_source(transformed) == source

# Generated at 2022-06-14 02:47:30.435150
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astunparse, astor
    code = """\
yield from x
"""
    code = code.strip()
    t = YieldFromTransformer()
    tree = ast.parse(code)
    t.visit(tree)
    code2 = astor.to_source(tree)
    code2 = code2.strip()
    assert code2 == """\
iterable = iter(x)
while True:
    try:
        yield next(iterable)
    except StopIteration as exc:
        break
""".strip()

# Generated at 2022-06-14 02:47:40.571992
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.testutil import object_eq_with_printing
    from ..utils import get_ast
    from .remove_type_ignore import RemoveTypeIgnore

    ast_1 = get_ast('''
        def test(got: int, expected: int):
            result = yield from test_helper(got, expected)
        ''')
    ast_2 = get_ast('''
        def test(got: int, expected: int):
            iterable = iter(test_helper(got, expected))
            while True:
                try:
                    yield next(iterable)
                except StopIteration as exc:
                    result = exc.value
                    break
        ''')
    ast_1 = RemoveTypeIgnore().visit(ast_1)