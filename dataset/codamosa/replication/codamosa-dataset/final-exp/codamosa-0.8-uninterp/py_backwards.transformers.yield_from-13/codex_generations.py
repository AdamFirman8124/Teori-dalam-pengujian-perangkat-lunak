

# Generated at 2022-06-14 02:39:04.756896
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer((3,2)).target == (3,2)

# Generated at 2022-06-14 02:39:05.810696
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    print(transformer._get_yield_from_index)

# Generated at 2022-06-14 02:39:16.066342
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ast_helper import parse, ast_pprint
    from unittest import TestCase
    from copy import copy
    try:
        from typed_ast import ast3
    except ImportError:
        from typed_ast import ast as ast3  # type: ignore # noqa

    from typed_astunparse import unparse
    from ..utils.context import Context
    from ..utils.helpers import VariablesGenerator

    with open(YieldFromTransformer.__module__.replace('.', '/') + '.py') as f:
        src = f.read()

    tree = parse(src)
    ctx = Context()
    YieldFromTransformer(ctx).visit(tree)
    assert isinstance(tree, ast3.Module)

    with open('/tmp/2.py', 'w') as f:
        f

# Generated at 2022-06-14 02:39:20.873570
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None).tree_changed == False
    YieldFromTransformer(None).generic_visit(None)
    assert YieldFromTransformer(None).visit(None) is None

# Unit tests for private methods of class YieldFromTransformer

# Generated at 2022-06-14 02:39:21.593903
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert 3

# Generated at 2022-06-14 02:39:23.229091
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:39:24.647407
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Currently there is no unit test for YieldFromTransformer
    pass

# Generated at 2022-06-14 02:39:25.251152
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:35.137130
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from io import StringIO
    from typed_astunparse import unparse
    from ..utils.test_visitor import VisitorTestCase

    class YieldFromTransformerTestCase(VisitorTestCase):
        transformer = YieldFromTransformer

        def test_node_removed(self) -> None:
            src = self.transform('''
                def foo():
                    yield from 1234
            ''')
            self.assertEqual(
                src,
                '''def foo():
    pass''',
            )

        def test_tuple_assignment_removed(self) -> None:
            src = self.transform('''
                def foo():
                    (a, b) = yield from 1234
            ''')

# Generated at 2022-06-14 02:39:36.028712
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:41.906377
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:47.471896
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse('''
try:
    yield from a
except GeneratorExit as e:
    pass
    ''')
    res = YieldFromTransformer(node).result
    expected = ast.parse('''
try:
    let(iterable)
    iterable = iter(a)
    while True:
        try:
            yield next(iterable)
        except StopIteration as exc:
            if hasattr(exc, 'value'):
                exc = exc.value
            break
except GeneratorExit as e:
    pass
    ''')
    assert ast.dump(res) == ast.dump(expected)

# Generated at 2022-06-14 02:39:50.983222
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert issubclass(YieldFromTransformer, BaseNodeTransformer)
    assert YieldFromTransformer.target == (3, 2)
    instance = YieldFromTransformer(None)
    assert isinstance(instance, YieldFromTransformer)


# Generated at 2022-06-14 02:39:51.873742
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:54.225776
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import get_code


# Generated at 2022-06-14 02:39:55.579300
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)

# Generated at 2022-06-14 02:39:58.115189
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from_transformer = YieldFromTransformer(None)
    yield_from_transformer.visit(A())


# Generated at 2022-06-14 02:40:00.251008
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """
    Test YieldFromTransformer class constructor
    """
    assert YieldFromTransformer()



# Generated at 2022-06-14 02:40:01.683227
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer._tree_changed == False

# Generated at 2022-06-14 02:40:12.484966
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from flake8_typing_extensions.transform import YieldFromTransformer
    from typed_ast import ast3 as ast
    from ..utils.ast_helpers import compare_source
    node = ast.parse("""
# comment

# comment
yield from [1, 2, 3]

# comment
foo = yield
yield from [1, 2, 3]
foo = yield from [1, 2, 3]
    """)
    YieldFromTransformer().visit(node)

# Generated at 2022-06-14 02:40:29.056629
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert isinstance(x, BaseNodeTransformer)
    assert hasattr(x, 'target')
    assert hasattr(x, '_get_yield_from_index')
    assert hasattr(x, '_emulate_yield_from')
    assert hasattr(x, '_handle_assignments')
    assert hasattr(x, '_handle_expressions')
    assert hasattr(x, 'visit')
    

# Generated at 2022-06-14 02:40:32.664383
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from jsparagus.generator import Generator
    with open(__file__,  encoding='utf-8') as fp:
        mod = ast.parse(fp.read())

    gen = Generator()
    gen.add_transformer(YieldFromTransformer)
    gen.generate(mod)

# Generated at 2022-06-14 02:40:35.307446
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:40:47.828003
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import fake_tree, assert_has_changes

    tree = fake_tree(
        body=[
            ast.FunctionDef(
                name='f',
                body=[
                    ast.Expr(ast.YieldFrom(ast.Call(ast.Name('g')))),
                    ast.Assign(
                        targets=[ast.Name('d')],
                        value=ast.YieldFrom(ast.Call(ast.Name('e')))
                    ),
                ]
            )
        ]
    )


# Generated at 2022-06-14 02:40:49.119067
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert ast.parse("yield from expr") == YieldFromTransformer().visit(ast.parse("yield from expr"))

# Generated at 2022-06-14 02:40:49.716564
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer(): assert True

# Generated at 2022-06-14 02:40:50.679267
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:00.828858
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_base import check_equal_ast
    input = """
        result = yield from 1
        result = yield from 2
        """


# Generated at 2022-06-14 02:41:05.878469
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.Try(
        body=[
            ast.Expr(value=ast.YieldFrom(value=ast.Name(id='a', ctx=ast.Load()))),
        ],
        handlers=[
            ast.ExceptHandler(
                body=[
                    ast.Expr(value=ast.YieldFrom(value=ast.Name(id='a', ctx=ast.Load()))),
                ],
            ),
        ],
        orelse=[
            ast.Expr(value=ast.YieldFrom(value=ast.Name(id='a', ctx=ast.Load()))),
        ],
        finalbody=[
            ast.Expr(value=ast.YieldFrom(value=ast.Name(id='a', ctx=ast.Load()))),
        ])

    result = YieldFromTrans

# Generated at 2022-06-14 02:41:07.029180
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:28.878717
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    with pytest.raises(Exception):
        YieldFromTransformer(None)



# Generated at 2022-06-14 02:41:30.281705
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node_transformer = YieldFromTransformer()
    assert node_transformer is not None

# Generated at 2022-06-14 02:41:32.828003
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Test constructor of class YieldFromTransformer
    node = None
    YieldFromTransformer(node)

# Generated at 2022-06-14 02:41:33.977475
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:41:35.598938
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None



# Generated at 2022-06-14 02:41:36.701236
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:41:46.618529
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import types
    import inspect
    import astunparse

    def get_func_ast(func, **kwargs):
        return ast.fix_missing_locations(
            ast.Module(body=[
                ast.FunctionDef(
                    name=func.__name__,
                    args=inspect.signature(func).parameters,
                    body=ast.parse(inspect.getsource(func)).body
                )
            ]).body[0]
        )

    def test_func(func, expected_result, **kwargs):
        # Create AST of input function
        func_ast = get_func_ast(func, **kwargs)
        # Get expected AST
        expected_

# Generated at 2022-06-14 02:41:51.549397
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    sample = """
        a = yield_from(b)
    """
    expected = """
    let(iterable)
    iterable = iter(b)
    while True:
        try:
            yield next(iterable)
        except StopIteration as exc:
            if hasattr(exc, 'value'):
                a = exc.value # type: ignore
            break
    """
    node = ast.parse(sample)
    YieldFromTransformer().visit(node)
    # Compare formatted strings.
    assert ast.dump(node).strip() == ast.parse(expected).body[0].body[0].body.strip()

# Generated at 2022-06-14 02:41:53.312297
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print(YieldFromTransformer)


# Generated at 2022-06-14 02:41:54.584665
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:42:35.682679
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:42:40.536329
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = """
    def f():
        return True

    class Test:
        def f(self):
            return True
    """
    tree = ast.parse(code)
    transformer = YieldFromTransformer()
    transformer.visit(tree)
    assert transformer.errors == []

# Generated at 2022-06-14 02:42:41.749016
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer(3, 2)

# Generated at 2022-06-14 02:42:42.515608
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()


# Generated at 2022-06-14 02:42:49.599984
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    if sys.version_info < (3, 2):
        return
    try:
        from typed_ast import ast3
    except ImportError:
        return
    from ..utils.check import check_equal

    y = ast3.YieldFrom()

    x = ast3.Expr(y)
    node = ast3.Module([x])
    node = YieldFromTransformer().visit(node)

# Generated at 2022-06-14 02:42:51.244530
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # class initialization
    yield_from = YieldFromTransformer()
    assert yield_from


# Generated at 2022-06-14 02:42:53.304534
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Test method for constructor of class YieldFromTransformer"""
    assert True


# Generated at 2022-06-14 02:42:55.848820
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_astunparse import unparse
    from .filters import NameFilter

    from .utils import should_transform_equal


# Generated at 2022-06-14 02:42:58.482360
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    module = ast.parse("def foo(): yield from bar")
    result = YieldFromTransformer().visit(module)
    assert isinstance(result, ast.Module)


# Generated at 2022-06-14 02:43:00.139392
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print("Testing YieldFromTransformer")
    YieldFromTransformer('',-1)

# Generated at 2022-06-14 02:44:36.538815
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = """
    class A:
        def __init__(self):
            pass
        """
    tree = ast.parse(code)
    YieldFromTransformer().visit(tree)
    assert(compile(tree, "<test>", 'exec'))


# Generated at 2022-06-14 02:44:39.982737
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    '''Test for constructor of class YieldFromTransformer'''
    transformer = YieldFromTransformer()
    assert transformer._tree_changed is False

# Generated at 2022-06-14 02:44:40.955794
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:44:46.814865
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    filename = __file__

    # Check basic case
    source = '''
        def foo():
            yield from 1, 2, 3
        '''
    tree = ast.parse(source)
    YieldFromTransformer().visit(tree)
    assert compile(tree, filename, 'exec')


# Unit Test for function _emulate_yield_from of class YieldFromTransformer

# Generated at 2022-06-14 02:44:56.191333
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .debug import DebugTransformer
    from ..utils.parser import parse_string
    from ..utils import dump_tree

    transformer = YieldFromTransformer()
    transformer = DebugTransformer(transformer)

    @snippet
    def test_yield_from():
        let(a)
        a = yield from [1, 2, 3]

    ast_ = parse_string(test_yield_from, 'test_snippet')
    ast_ = transformer.visit(ast_)
    print(dump_tree(ast_))

    @snippet
    def test_yield_from2():
        yield from [1, 2, 3]

    ast_ = parse_string(test_yield_from2, 'test_snippet')
    ast_ = transformer.visit(ast_)
    print

# Generated at 2022-06-14 02:45:00.495184
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # This test should be executed statement-by-statement, to see what each
    # statement returns.
    YieldFromTransformer(None)

# Unit tests for method _get_yield_from_index of class YieldFromTransformer

# Generated at 2022-06-14 02:45:01.335131
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()



# Generated at 2022-06-14 02:45:02.066271
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:45:05.377480
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from_transformer = YieldFromTransformer()
    assert isinstance(yield_from_transformer, BaseNodeTransformer)
    assert yield_from_transformer.target == (3, 2)

## Unit test for function _handle_assignments of class YieldFromTransformer

# Generated at 2022-06-14 02:45:12.773557
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = 'x = yield from y'
    node = ast.parse(code)
    result = YieldFromTransformer().visit(node)
    expected_result = ast.parse('x = None\niterable = iter(y)\nwhile True:\n    try:\n        x = next(iterable)\n    except StopIteration as exc:\n        if hasattr(exc, \'value\'):\n            x = exc.value\n        break')
    assert ast.dump(result) == ast.dump(expected_result)