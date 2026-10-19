

# Generated at 2022-06-14 02:39:00.227948
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor

# Generated at 2022-06-14 02:39:01.368363
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert(YieldFromTransformer)

# Generated at 2022-06-14 02:39:04.087788
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yft = YieldFromTransformer()
    assert yft

# Unit tests for _get_yield_from_index of class YieldFromTransformer

# Generated at 2022-06-14 02:39:05.163379
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:06.829637
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = """
    def f():
        yield from f()
    
    a = yield from f()
    """
    assert isinstance(ast.parse(code), ast.Module)
    YieldFromTransformer().visit(ast.parse(code))

# Generated at 2022-06-14 02:39:12.560270
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # initing
    output = {"result": False}
    dummy_node = ast.Constant()
    dummy_node2 = ast.Constant()

    tree = ast.module()
    tree.body.append(dummy_node)
    tree.body.append(dummy_node2)

    # running
    YieldFromTransformer.visit(tree)

    # testing
    assert output["result"] is True
    assert tree.body[0] is dummy_node

# Generated at 2022-06-14 02:39:13.809491
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer


# Generated at 2022-06-14 02:39:15.401920
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    #This doesn't actually test anything.
    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:39:16.336143
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:19.119073
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ast import parse
    t = YieldFromTransformer()
    tree = parse("""
        for i in range(4):
            b = (yield from a) # a == 5")
            b = (yield from a + b)
    """)
    t.visit(tree)

# Generated at 2022-06-14 02:39:32.306447
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    ast_str = """
    def func():
        yield from gen()
        for elem in iter(gen()):
            yield from iter(gen())
    """

    transformer = YieldFromTransformer()
    result = transformer.visit(ast.parse(ast_str))
    assert isinstance(result, ast.Module)
    assert isinstance(result.body[0], ast.FunctionDef)
    first = result.body[0]
    assert isinstance(first.body[1], ast.While)
    second = first.body[1]
    assert isinstance(second.body[1], ast.Yield)
    assert isinstance(second.body[2], ast.Yield)

# Generated at 2022-06-14 02:39:33.663723
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transpiler = YieldFromTransformer()
    assert transpiler


# Generated at 2022-06-14 02:39:43.127469
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class Transformer(YieldFromTransformer):
        def visit_For(self, node):
            return node
        def visit_If(self, node):
            return node
    tree = ast.parse('a = yield from b')
    assert(ast.dump(tree, include_attributes=True) == 'Module(body=[Assign(targets=[Name(id="a", ctx=Store())], value=YieldFrom(value=Name(id="b", ctx=Load())))])')
    tree = Transformer().visit(tree)

# Generated at 2022-06-14 02:39:45.040920
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer()._generator, VariablesGenerator)


# Generated at 2022-06-14 02:39:54.070724
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .transformer import transformer_factory
    from .transformer import get_source_code
    from .transformer import get_ast_tree

    code_1 = "def foo():\n    yield from baz()\n"
    code_2 = "def foo():\n    bar = yield from baz()\n"
    code_3 = "def foo():\n    yield from bar = baz()\n"
    code_4 = "def foo():\n    bar = yield from baz()\n"
    code_5 = "def foo():\n    yield from bar = yield from baz()\n"
    code_6 = "def foo():\n    try:\n        yield from baz()\n    except Exception:\n        bar = baz()\n"

# Generated at 2022-06-14 02:39:56.226482
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # type: () -> None
    from ..utils.helpers import compare_source


# Generated at 2022-06-14 02:39:56.814368
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:39:58.168686
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass



# Generated at 2022-06-14 02:40:08.550615
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astunparse
    import textwrap
    code = textwrap.dedent("""
    def fun_1(values):
        x = yield from values
        return x

    def fun_2(values):
        yield from values


    def fun_3(values):
        for x in values:
            yield from x
        return x


    def fun_4(values):
        for x in values:
            yield from x
            for y in values:
                yield from y
                if x == y:
                    return x
    """)
    tree = ast.parse(code)
    # print(astunparse.dump(tree))
    YieldFromTransformer().visit(tree)
    # print(astunparse.dump(tree))

# Generated at 2022-06-14 02:40:09.634978
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()


# Generated at 2022-06-14 02:40:21.274841
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:30.197853
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .context import Context
    from .node_transformer_manager import NodeTransformerManager
    from ..utils.source_code import SourceCode
    import os
    import sys

    PATH = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, PATH)

    source = SourceCode.from_file(os.path.join(PATH, "data", "yield_from.py"))
    stage1 = NodeTransformerManager.get_transformed(source,
                                                    Context.from_code(source.code,
                                                                      target=(3, 5)))

    assert stage1.code == source.code

# Generated at 2022-06-14 02:40:41.173198
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import typed_astunparse
    code = """
for i in range(0, 10):
    a = (yield from generator())
    print(a)
    """
    tree = ast.parse(code)
    tree = YieldFromTransformer().visit(tree)
    print(typed_astunparse.unparse(tree))

    assert typed_astunparse.unparse(tree) == """
for i in range(0, 10):
    let(_iterable)
    _iterable = iter(generator())
    while True:
        try:
            yield next(_iterable)
        except StopIteration as _exc:
            if hasattr(_exc, 'value'):
                a = _exc.value
            break
    print(a)
    """

# Generated at 2022-06-14 02:40:43.313671
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import ast
    import astor

# Generated at 2022-06-14 02:40:47.593705
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    '''
    Unit test for the YieldFromTransformer class.
    '''

    class_yield_fromtransformer = YieldFromTransformer()
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:40:53.371260
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from . import ast_checker
    from ..utils.misc import Unhashable
    from ..utils.ast_helper import get_root
    from ..utils.helpers import assert_equal_ast

    with ast_checker.assert_errors(Unhashable):
        test = """
        def foo():
            yield from range(100)
            a = yield from range(100)
            yield from range(100)  # comment
            yield from range(100)
            yield from range(100)
        """
        root = get_root(test)
        assert_equal_ast(root, YieldFromTransformer)

# Generated at 2022-06-14 02:41:04.969368
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import verify

    test = verify(YieldFromTransformer)

    @test
    def test_yield_from_with_assignment():
        def fn():
            yield_from_with_assignment  # noqa

        should_be = """
        def fn():
            let(iterable)
            iterable = iter(yield_from_with_assignment)
            while True:
                try:
                    yield next(iterable)
                except StopIteration as exc:
                    yield_from_with_assignment = exc.value
                    break
        """

        fn()

    @test
    def test_yield_from_without_assignment():
        def fn():
            yield_from_without_assignment  # noqa


# Generated at 2022-06-14 02:41:06.766075
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer.__class__.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:41:07.707660
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:41:09.925367
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    assert a is not None


# Generated at 2022-06-14 02:41:32.143959
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None


# Generated at 2022-06-14 02:41:38.200466
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = "def foo(x):\n  if x > 0:\n    y = yield from bar(x)\n    print(y)"
    expected_code = "def foo(x):\n  if x > 0:\n    let(iterable)\n    iterable = iter(bar(x))\n    while True:\n        try:\n            yield next(iterable)\n        except StopIteration as exc:\n            if hasattr(exc, 'value'):\n                y = exc.value\n            break"
    tree = ast.parse(code)
    YieldFromTransformer().visit(tree)
    assert astor.to_source(tree) == expected_code

# Generated at 2022-06-14 02:41:39.247061
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer


# Generated at 2022-06-14 02:41:41.834696
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Constructor should set _tree_changed to False."""
    yft = YieldFromTransformer()
    assert yft._tree_changed == False


# Generated at 2022-06-14 02:41:44.029815
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test.testutils import roundtrip

    yft = YieldFromTransformer()

# Generated at 2022-06-14 02:41:51.961540
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from textwrap import dedent
    transpiler = YieldFromTransformer()
    tree = dedent('''\
        def example():
            __result__ = yield from f
            return __result__
    ''')
    assert str(transpiler(tree)) == dedent('''\
        def example():
            let(iterable)
            iterable = iter(f)
            while True:
                try:
                    yield next(iterable)
                except StopIteration as exc:
                    if hasattr(exc, 'value'):
                        __result__ = exc.value
                    break
            return __result__
    ''')
    tree = dedent('''\
        def example():
            __result__ = yield from f
            yield g(__result__)
    ''')

# Generated at 2022-06-14 02:41:53.970658
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:41:55.386577
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:41:58.945552
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class A:
        def __init__(self, a):
            self.a = a
            YieldFromTransformer(a)
            pass

    a = A(1)
    assert a.a == 1

# Generated at 2022-06-14 02:42:06.515294
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:42:49.038007
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None).__class__.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:42:50.519119
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

if __name__ == '__main__':
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:52.776428
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert issubclass(YieldFromTransformer, BaseNodeTransformer)
    assert YieldFromTransformer.target == (3, 2)


# Generated at 2022-06-14 02:43:00.391146
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    source = '''def mygen():
                    yield from range(3)
                    return
                '''
    tree = ast.parse(source)
    target = (3, 2)
    result = YieldFromTransformer.run(tree, target)
    expected = '''def mygen():
                    exc = object()
                    iterable = iter(range(3))
                    while True:
                        try:
                            yield next(iterable)
                        except StopIteration as exc:
                            pass
                            break
'''
    assert ast.dump(result) == expected

# Generated at 2022-06-14 02:43:01.954390
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()


# Generated at 2022-06-14 02:43:02.947139
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:43:04.853568
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(None), YieldFromTransformer)


# Generated at 2022-06-14 02:43:08.244850
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    # Instantiate the node
    x = YieldFromTransformer()
    # Check attributes
    assert x.target == (3,2)

# Generated at 2022-06-14 02:43:10.159081
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_helpers import get_node
    from ..transformer import Transformer

# Generated at 2022-06-14 02:43:18.037397
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tr = YieldFromTransformer()

    yield_from = ast.YieldFrom(value=ast.Name(id='generator', ctx=ast.Load()))

    # Test 1: one assignment
    target = ast.Name(id='_', ctx=ast.Store())
    assignment = ast.Assign(targets=[target], value=yield_from)
    node = ast.While(test=ast.Num(1), body=[assignment], orelse=[])
    res = tr.visit(node)
    assert len(res.body) == 1
    assert isinstance(res.body[0], ast.While)
    assert isinstance(res.body[0].test, ast.Name)
    assert len(res.body[0].body) == 1

    # Test 2: multi-assignment
    target

# Generated at 2022-06-14 02:45:24.970726
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print("Testing YieldFromTransformer class...")


# Generated at 2022-06-14 02:45:32.054994
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from astor import to_source
    from ..const_vars import in_, out
    this_module = ast.parse('yield_from = 3')
    # ast.parse('yield_from = 3').body[0].value = ast.parse('3')
    # ast.parse('yield_from = 3').body[0].targets[0].id = ast.parse('yield_from')
    # ast.parse('yield_from = 3').body[0].targets[0].ctx = ast.parse('Store')
    # ast.parse('yield_from = 3').body[0].lineno = 1
    # ast.parse('yield_from = 3').body[0].col_offset = 0

    # ast.parse('yield_from = 3').body[0].targets[0

# Generated at 2022-06-14 02:45:41.062163
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.tests import transform, parse, compare

    tree = parse('''
    def func():
        yield from coro(2)

    def func2():
        a = yield from coro(2)

    def func3():
        yield from coro(2)
        a = yield from coro(2)

    def func4():
        a = (1, yield from coro(2))

    def func5():
        a = {'': yield from coro(2)}

    def func6():
        a = {yield from coro(2): ''}

    def func7():
        a = [yield from coro(2)]
    ''')  # noqa: E501

    tree = transform(tree, YieldFromTransformer)

# Generated at 2022-06-14 02:45:45.427717
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from pprint import pprint
    from typed_ast.ast3 import parse
    from ..utils.helpers import dump_tree
    from ..utils.source import generate_code


# Generated at 2022-06-14 02:45:52.591701
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import BaseNodeTransformer

    assert issubclass(YieldFromTransformer, BaseNodeTransformer)
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'
    assert YieldFromTransformer.__doc__ == 'Compiles yield from to special while statement.'
    assert YieldFromTransformer().target == (3, 2)

# Generated at 2022-06-14 02:45:58.417264
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert issubclass(YieldFromTransformer, BaseNodeTransformer)
    assert YieldFromTransformer(None, None).__name__ == 'YieldFromTransformer'
    assert YieldFromTransformer(None, None).target == (3, 2)

# Generated at 2022-06-14 02:46:04.657988
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.testing import assert_equal_source
    from ..utils.misc import parse
    from .misc import remove_useless_imports
    from ..utils.tree import print_tree
    node = YieldFromTransformer()
    import_stmt = parse("import sys")
    yield_from_stmt = parse("_ = yield from (x for x in range(10))")
    module = ast.Module([import_stmt, yield_from_stmt])
    node.visit(module)
    module = remove_useless_imports().visit(module)

# Generated at 2022-06-14 02:46:06.124341
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:46:07.376057
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:46:16.277337
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..tests.testing import assert_node
    with open('tests/data/YieldFromTransformer.py', 'r') as f:
        node = ast.parse(f.read())
    for _ in range(3):
        node = YieldFromTransformer(options=None).visit(node)

    with open('tests/data/YieldFromTransformer_expected.py', 'r') as f:
        expected = ast.parse(f.read())
    assert_node(node, expected)