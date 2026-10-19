

# Generated at 2022-06-14 02:39:06.389713
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yft = YieldFromTransformer()
    print(yft)


if __name__ == '__main__':
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:39:10.600500
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        import typed_astunparse
    except ImportError:
        pass
    else:
        code = "a = yield from []"
        t = YieldFromTransformer()
        tree = ast.parse(code)
        t.visit(tree)
        assert typed_astunparse.unparse(tree) == "a = None\n"

# Generated at 2022-06-14 02:39:20.785669
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .fake_nodes import FakeTry
    try_body = [
        ast.FunctionDef(
            name='with_from',
            body=[
                ast.Expr(value=ast.YieldFrom(value=ast.Name('name', [], [], [], []))),
            ],
            returns=None,
            args=[],
            keywords=[],
        ),
    ]

# Generated at 2022-06-14 02:39:24.601185
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from vyper.parser.parser import VyperParser
    from vyper.parser.parser_utils import LLLnode

# Generated at 2022-06-14 02:39:25.129554
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:26.070281
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


# Generated at 2022-06-14 02:39:26.614546
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:28.010966
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # test that the constructor doesn't throws
    YieldFromTransformer(None)

# Generated at 2022-06-14 02:39:28.725856
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    inst = YieldFromTransformer()

# Generated at 2022-06-14 02:39:35.764442
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert hasattr(YieldFromTransformer, 'visit')
    assert hasattr(YieldFromTransformer, '_handle_assignments')
    assert hasattr(YieldFromTransformer, '_handle_expressions')
    assert hasattr(YieldFromTransformer, '_get_yield_from_index')
    assert hasattr(YieldFromTransformer, '_emulate_yield_from')
    assert hasattr(YieldFromTransformer, 'target')
    assert hasattr(YieldFromTransformer, '_tree_changed')


# Generated at 2022-06-14 02:39:43.089040
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Unit test for constructor of class YieldFromTransformer."""

# Generated at 2022-06-14 02:39:43.994143
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:50.147395
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    snippet_at_target = snippet(
        """
        # body of the snippet
        yield from some_iterable
        """
    )
    tree = snippet_at_target.get_tree()
    transformer = YieldFromTransformer()
    new_node = transformer.visit(tree)
    # Checking whether the snippet has been replaced with a different snippet
    assert transformer._tree_changed
    assert isinstance(new_node, ast.Module)

# Generated at 2022-06-14 02:39:55.680015
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.testing import run_transform_test

    code = """
    def foo():
        a = (yield from bar())
    """

    transformed = """
    def foo():
        let(iterable)
        iterable = iter(bar())
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    a = exc.value
                break
    """

    run_transform_test(YieldFromTransformer, code, transformed)

# Generated at 2022-06-14 02:39:56.437651
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yft = YieldFromTransformer()

# Generated at 2022-06-14 02:39:57.832107
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


# Generated at 2022-06-14 02:39:58.479398
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:39:59.785452
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    o = YieldFromTransformer()

# Generated at 2022-06-14 02:40:08.883527
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    b = ast.parse("""
            def foo():
                yield from bar()
            def baz():
               r = yield from q()
               v = yield from m()
               yield from u()
               return r
            def some():
                pass
            def unexp():
                yield from [1, 2, 3]
            """).body
    transformer = YieldFromTransformer()

    foo, baz, some, unexp = b
    foo = transformer.visit(foo)
    baz = transformer.visit(baz)
    some = transformer.visit(some)
    unexp = transformer.visit(unexp)

    # foo
    assert isinstance(foo, ast.FunctionDef)
    assert foo.name == "foo"

# Generated at 2022-06-14 02:40:09.971127
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:27.052620
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = 'def foo(): yield from [1, 2, 3]'
    expected = """def foo():
    iterable = iter([1, 2, 3])
    while True:
        try:
            yield next(iterable)
        except StopIteration as exc:
            break"""
    tree = ast.parse(code)
    YieldFromTransformer().visit(tree)
    assert ast.unparse(tree) == expected



# Generated at 2022-06-14 02:40:35.855347
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import sys
    from ..validators.base import CodeValidator

    if sys.version_info >= (3, 2):
        code_validator = CodeValidator()
        node = code_validator.parse('a = yield from b')
        YieldFromTransformer(node)
        assert str(node) == 'yield_from_emulator_6 = iter(b)\n'
        assert str(node.body[0]) == 'while True:\n    try:\n        temp_var_7 = next(yield_from_emulator_6)\n        yield temp_var_7\n    except StopIteration as exc_8:\n        a = exc_8.value\n        break'

        node = code_validator.parse('yield from a')
        YieldFromTransformer(node)
        assert str(node)

# Generated at 2022-06-14 02:40:37.398191
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None, None, None)


# Generated at 2022-06-14 02:40:49.423343
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import parse
    from .base import UnsupportedFeature
    import os
    import sys
    sys.path.append(os.path.dirname(__file__))
    import test_fib
    try:
        with open('test_fib_py3.py', 'r') as f:
            expected_code = f.read()
    except FileNotFoundError:
        print("'test_fib_py3.py' not found")
        return False
    try:
        compiled = YieldFromTransformer().visit(parse(test_fib.code))
    except UnsupportedFeature:
        print("UnsupportedFeature occurred with this class")
        return False
    assert compile(compiled, "<ast>", 'exec') == compile(expected_code, "<ast>", 'exec')
    return True

# Generated at 2022-06-14 02:40:50.779017
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert(isinstance(YieldFromTransformer(), BaseNodeTransformer))

# Generated at 2022-06-14 02:40:53.051742
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:04.625539
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_base import test_transform
    from typed_ast import ast3 as ast
    import sys

    # Python 3.3+
    if sys.version_info >= (3, 3):
        code1 = 'yield from range(5)'
        tree1 = ast.parse(code1, '<string>', mode='exec')
        transformer1 = YieldFromTransformer()
        new_tree1 = transformer1.visit(tree1)
        result1 = test_transform(code1, new_tree1)

# Generated at 2022-06-14 02:41:05.425423
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor

# Generated at 2022-06-14 02:41:06.457942
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:18.962047
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("""
    def foo(x):
        y = yield from range(x)
        z = yield from range(x)

    def foo2(x):
        y = yield from range(x)
        z = yield from range(x)
    """)

    YieldFromTransformer().visit(tree)


# Generated at 2022-06-14 02:41:42.296032
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


__transformer__ = YieldFromTransformer

# Generated at 2022-06-14 02:41:43.660273
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from standard_transformers import YieldFromTransformer
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:41:45.962679
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # test for function __init__
    trans = YieldFromTransformer()
    assert trans.target == (3, 2)
    assert trans._tree_changed == False
    

# Generated at 2022-06-14 02:41:46.814726
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:41:53.775820
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    source = """
        def foo():
            yield from [1, 2, 3]

        def bar():
            yield from [1, 2, 3]
            yield from [4, 5, 6]
            a=yield from [7, 8, 9]

        def baz():
            yield from [1, 2, 3]
            a=yield from [4, 5, 6]

        def func():
            yield from [1, 2, 3]
            a, b=yield from [4, 5, 6]
    """

    tree = ast.parse(source)
    transformer = YieldFromTransformer()
    new_tree = transformer.visit(tree)
    code = compile(new_tree, '<string>', 'exec')
    glob = {}
    exec(code, glob)


# Generated at 2022-06-14 02:41:54.763944
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    v = YieldFromTransformer()



# Generated at 2022-06-14 02:41:55.753586
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:41:56.794664
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    result =  YieldFromTransformer()
    assert result is not None

# Generated at 2022-06-14 02:41:59.487751
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer(): 
    assert YieldFromTransformer('YieldFromTransformer', {}).__class__.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:42:00.445568
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__doc__ is not None

# Generated at 2022-06-14 02:42:46.157268
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer().generic_visit(None),
                      YieldFromTransformer)

# Generated at 2022-06-14 02:42:46.746003
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():

    YieldFromTransformer()

# Generated at 2022-06-14 02:42:52.565978
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    a
    a._tree_changed = True
    a._tree_changed
    a._YieldFromTransformer__tree_changed
    a.target
    a._get_yield_from_index(None, None)
    a._emulate_yield_from(None, None)
    a._handle_assignments(None)
    a._handle_expressions(None)
    a.visit(None)
    a.generic_visit(None)

# Generated at 2022-06-14 02:42:54.094596
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:42:56.680430
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from=yield_from()
    result_assignment=result_assignment()
    
test_YieldFromTransformer()

# Generated at 2022-06-14 02:43:03.458251
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Test wrong 'target' parameter
    with pytest.raises(TypeError):
        YieldFromTransformer(target='3, 2')
    # Test wrong 'tree_changed' parameter
    with pytest.raises(TypeError):
        YieldFromTransformer(tree_changed=3)
    # Test wrong 'visit_once' parameter
    with pytest.raises(TypeError):
        YieldFromTransformer(visit_once='True')
    # Test good parameters
    YieldFromTransformer(target=(3, 2))
    YieldFromTransformer(tree_changed=True)
    YieldFromTransformer(visit_once=False)


# Generated at 2022-06-14 02:43:06.822023
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import inspect
    import sys
    lines = inspect.getsource(sys.modules[__name__])
    code = '\n'.join(lines)
    exec(code)
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:09.693244
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from_transformer = YieldFromTransformer()
    assert isinstance(yield_from_transformer, YieldFromTransformer)


# Generated at 2022-06-14 02:43:17.777311
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.testing import check_codegen
    from . import TransformTestCase
    from .ast_utils import Module, YieldFrom, Assign, Name, FunctionDef, Arguments, Return, Call
    from .ast_utils import generator_exp, Num, Dict, If
    from .ast_utils import List as ListNode
    from .ast_utils import Expr

    class YieldFromTestCase(TransformTestCase):
        transform = YieldFromTransformer

    test = YieldFromTestCase()

    testcode = """
    d = {'a': 1, 'b': 2}
    """
    test.test(testcode, "")

    testcode = """
    d = {'a': 1, 'b': 2}
    d['c'] = yield from range(10)
    """

# Generated at 2022-06-14 02:43:19.174026
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:45:16.094971
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
	# YieldFromTransformer()
	node = ast.Name('A')
	type_ = ast.Name('B')
	node_ = ast.Name('C')
	YieldFromTransformer()._get_yield_from_index(node, type_)
	YieldFromTransformer()._emulate_yield_from(node_, node)
	YieldFromTransformer()._handle_assignments(node)
	YieldFromTransformer()._handle_expressions(node)
	YieldFromTransformer().visit(node)
	# print(YieldFromTransformer().__doc__)


if __name__ == "__main__":
	test_YieldFromTransformer()

# Generated at 2022-06-14 02:45:17.289761
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    assert a


# Generated at 2022-06-14 02:45:18.684377
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None, None)

# Generated at 2022-06-14 02:45:21.403020
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from . import _common_testing_module
    _common_testing_module.test_module(
        YieldFromTransformer.__name__, YieldFromTransformer.target)

# Generated at 2022-06-14 02:45:21.897921
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:45:22.700436
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import parse


# Generated at 2022-06-14 02:45:25.261771
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_transformer import transform

    assert transform(YieldFromTransformer)


# Generated at 2022-06-14 02:45:26.497138
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:45:27.250155
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    return YieldFromTransformer()

# Generated at 2022-06-14 02:45:34.600123
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # AST to be transformed
    body: List[ast.AST] = []
    body.append(ast.Expr(value=ast.YieldFrom(value=ast.Name(id='test_yield_from',
        ctx=ast.Load()))))

    tree: ast.AST = ast.Module(body=body)

    # Constructor of class YieldFromTransformer test
    YieldFromTransformer()
