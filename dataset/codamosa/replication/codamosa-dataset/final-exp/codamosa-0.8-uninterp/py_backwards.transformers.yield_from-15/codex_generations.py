

# Generated at 2022-06-14 02:39:12.402313
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import GenericASTWalker
    from .test_helpers import parse, compare_ast
    from typed_astunparse import unparse

    stmt_1 = """
yield from foo
"""
    expected_stmt_1 = """
exc = None
try:
    iterable = iter(foo)
    while True:
        try:
            yield next(iterable)
        except StopIteration as exc:
            if hasattr(exc, 'value'):
                exc = exc.value
            break
except BaseException as exc:
    raise exc
"""
    test_stmt_1 = parse(stmt_1)
    transformer = YieldFromTransformer()
    walker = GenericASTWalker(transformer)
    walker.walk(test_stmt_1)

# Generated at 2022-06-14 02:39:14.665990
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from_transformer = YieldFromTransformer()
test_YieldFromTransformer()

# Generated at 2022-06-14 02:39:22.036042
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # test with one yield from
    tree = ast.parse(
        """
raise
import
if True:
    a, b = yield from x
yield
if True:
    yield from z
    c = d
z = k
        """
    )
    # tree = ast.parse('y = yield from x')
    print(ast.dump(tree))
    transformer = YieldFromTransformer()
    tree = transformer.visit(tree)
    print(ast.dump(tree))
    ast.fix_missing_locations(tree)
    exec(compile(tree, '<string>', 'exec'))

# Generated at 2022-06-14 02:39:23.733212
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:28.285648
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .transpile import Transpile
    transpile = Transpile()
    for code in ['yield from some_func()']:
        tree = ast.parse(code, mode='exec')
        tree = Transpile()(tree)
        tree = YieldFromTransformer()(tree)
        tree = transpile(tree)

# Generated at 2022-06-14 02:39:38.304510
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        from ..utils.helpers import get_ast
        from ..utils.snippet import snippet
    except ImportError:
        return
    # tests for _handle_expressions
    for t in snippet, get_ast:
        node = t("""
        def f():
            yield from x
            yield from y
        """)
        YieldFromTransformer(None).visit(node)
        assert(isinstance(
            node.body[0].body[0].orelse[1].body[0].value, ast.YieldFrom))
        assert(isinstance(
            node.body[0].body[0].orelse[1].body[1].value, ast.YieldFrom))

    node = t("""
    def f():
        while True:
            yield from x
        """)
   

# Generated at 2022-06-14 02:39:40.148096
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.tree_builder import create_from_text
    from .async_ import AsyncTransformer
    

# Generated at 2022-06-14 02:39:41.341139
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Check create instance of YieldFromTransformer
    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:39:41.873984
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass #TODO

# Generated at 2022-06-14 02:39:48.658511
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from python2python.transformers.typed_ast_transformer import TypedAstTransformer
    src = 'yield from bar'
    test_ast = ast.parse(src)
    transformer = YieldFromTransformer()
    transformed_ast = transformer.visit(test_ast)
    transformed_ast_str = TypedAstTransformer(
        ).visit(transformed_ast)
    expected_ast_str = 'def _():\n    let(iterable)\n    iterable = iter(bar)\n    while True:\n        try:\n            yield next(iterable)\n        except StopIteration as exc:\n            if hasattr(exc, \'value\'):\n                pass\n            break'
    #TODO: fix after fixing all tests
    assert transformed_ast_str == expected_ast_str


#

# Generated at 2022-06-14 02:40:05.154569
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import get_ast
    from ..utils.test_helpers import assert_equal_ast
    import os.path as osp

    src_dir = osp.dirname(osp.abspath(__file__))
    src_path = osp.join(src_dir, "data", "code_for_test_YieldFromTransformer.py")
    src = open(src_path).read()  # type: ignore

    expected_path = osp.join(src_dir, "data", "expected_code_for_test_YieldFromTransformer.py")
    expected = open(expected_path).read()  # type: ignore
    ast_ = get_ast(src)
    print(ast.dump(ast_))
    ast_ = YieldFromTransformer().visit(ast_)

# Generated at 2022-06-14 02:40:06.512437
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None


# Generated at 2022-06-14 02:40:09.828955
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import BaseNodeTransformer

    YieldFromTransformer()
    assert isinstance(YieldFromTransformer(), BaseNodeTransformer)


# Generated at 2022-06-14 02:40:20.983501
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import _ast
    a = ast.parse('a = yield from b')
    c = YieldFromTransformer().visit(a)
    assert c.body[0].value.value.value.id == 'iter'
    assert c.body[0].value.value.args[0].id == 'b'
    assert type(c.body[0].value.value.args[0]) == _ast.Name
    assert type(c.body[0].value.value) == _ast.Call
    assert type(c.body[0].value) == _ast.Name
    assert c.body[0].value.id == 'iterable'
    assert type(c.body[0]) == _ast.Assign
    assert type(c.body[0].targets[0]) == _ast.Name
    assert c.body

# Generated at 2022-06-14 02:40:23.248963
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node_visitor = YieldFromTransformer()
    assert node_visitor is not None


# Generated at 2022-06-14 02:40:25.465592
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = ast.YieldFrom()
    t = YieldFromTransformer()
    r = t.visit(a)
    assert r is None

# Generated at 2022-06-14 02:40:26.905273
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    with YieldFromTransformer() as transformer:
        pass

# Generated at 2022-06-14 02:40:28.267544
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer(target=(3, 2))

# Generated at 2022-06-14 02:40:29.229632
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()



# Generated at 2022-06-14 02:40:30.597363
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Test that class YieldFromTransformer initializes correctly
    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:40:44.290539
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    arg = \
"""
import asyncio
async def main():
    a = await load()
    b = await load()
    return a + b
"""
    res = \
"""
import asyncio
async def main():
    a = yield from load()
    b = yield from load()
    return a + b
"""
    assert YieldFromTransformer().visit(ast.parse(arg)).body[0].body == ast.parse(res).body[0].body

# Generated at 2022-06-14 02:40:50.348643
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor  # type: ignore
    import sys
    sys.modules['astor'] = astor
    sys.modules['astor.code_gen'] = astor.code_gen
    sys.modules['astor.code_gen.SourceGenerator'] = astor.code_gen.SourceGenerator
    import _YieldFromTransformer
    _YieldFromTransformer.YieldFromTransformer()


# Generated at 2022-06-14 02:40:51.287820
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer

# Generated at 2022-06-14 02:41:01.172534
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # check that code is running without exception
    # this is just an example_code to check if something is going to raise an exception
    # does not mean anything
    tree = ast.parse('a = yield from b\n yield from c')
    node_transformer = YieldFromTransformer()
    node_transformer.visit(tree)

# Generated at 2022-06-14 02:41:05.767442
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import source_transform

    @source_transform
    def test(yield_from):
        a = yield_from
        yield yield_from

    assert test.__name__ == 'test'
    assert 'yield from' not in test.__source__
    assert 'yield from' in test.__dict__['_source']

# Generated at 2022-06-14 02:41:15.281051
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..serialize import to_string
    from .base import BaseNodeTransformer, NodeTransformer

    class BaseTransformer(NodeTransformer):
        def __init__(self, **kwargs) -> None:
            super().__init__()

    class YieldFromTransformer(BaseTransformer):
        """Compiles yield from to special while statement."""
        target = (3, 2)


# Generated at 2022-06-14 02:41:16.866200
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass



# Generated at 2022-06-14 02:41:18.996866
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer(None)
    expected = '<YieldFromTransformer>'
    assert str(a) == expected
    assert repr(a) == expected

# Generated at 2022-06-14 02:41:25.551543
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from test.parser.pattern import pattern

    code = """
    async def async_get_json(client, url):
        async with client.get(url) as response:
            assert response.status == 200
            return await response.json()
    """
    module = ast.parse(code)
    YieldFromTransformer().visit(module)
    assert pattern(code) == module

# Generated at 2022-06-14 02:41:29.511999
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    inst = YieldFromTransformer('module_name')
    assert isinstance(inst, YieldFromTransformer)
    assert isinstance(inst, BaseNodeTransformer)


# Generated at 2022-06-14 02:41:54.016727
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    y = YieldFromTransformer()
    assert isinstance(y, BaseNodeTransformer)


# Generated at 2022-06-14 02:41:55.383708
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)

# Generated at 2022-06-14 02:42:04.726339
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("def fun():\n"
                     "    yield from [1, 2]\n"
                     "print(fun)\n")
    expected = ast.parse("def fun():\n"
                         "    let(iterable)\n"
                         "    iterable = iter([1, 2])\n"
                         "    while True:\n"
                         "        try:\n"
                         "            yield next(iterable)\n"
                         "        except StopIteration as exc:\n"
                         "            break\n"
                         "print(fun)")
    transformed = YieldFromTransformer().visit(tree)
    assert ast.dump(expected) == ast.dump(transformed)

# Generated at 2022-06-14 02:42:11.430150
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert x.__str__() == '<YieldFromTransformer>'
    assert x._get_yield_from_index() is None
    assert x._emulate_yield_from() is None
    assert x._handle_assignments() is None
    assert x._handle_expressions() is None
    assert x.visit() is None


# Generated at 2022-06-14 02:42:12.403529
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()


# Generated at 2022-06-14 02:42:17.719396
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yft = YieldFromTransformer()
    tree = ast.parse('a = yield from (1, 2, 3)')
    transformed_tree = yft.visit(tree)
    transformed_code = ast.unparse(transformed_tree)
    assert transformed_code == '''iterable = iter((1, 2, 3))
while True:
    try:
        yield next(iterable)
    except StopIteration as exc:
        a = exc.value
        break'''

# Generated at 2022-06-14 02:42:18.970321
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None


# Generated at 2022-06-14 02:42:20.638462
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    obj = YieldFromTransformer()
    assert isinstance(obj, YieldFromTransformer)


# Generated at 2022-06-14 02:42:27.946936
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse('__yield_from = yield from __x', 'fake')
    expected = '__yield_from = None\n'\
               'for __yield_from in __x:\n'\
               '    __yield_from = __yield_from\n'\
               '    if hasattr(__yield_from, \'value\'):\n'\
               '        __yield_from = __yield_from.value'
    assert ast.dump(YieldFromTransformer().visit(tree)) == ast.dump(ast.parse(expected, 'fake'))

# Generated at 2022-06-14 02:42:29.172778
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:43:13.079515
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Not run this test
    pass

# Generated at 2022-06-14 02:43:24.954264
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    program_code = """
        i = 0
        while True:
            j = yield from b[i]
            i += 1
    """
    tree = ast.parse(program_code)
    YieldFromTransformer().visit(tree)

# Generated at 2022-06-14 02:43:26.552420
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    assert (isinstance(a, NodeTransformer))



# Generated at 2022-06-14 02:43:27.450303
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer(None)

# Generated at 2022-06-14 02:43:34.755267
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from . import compile_source

    assert YieldFromTransformer is not None
    assert compile_source(
        "def f():\n"
        "    x = yield from range(1)\n"
        "    print(x)") == compile_source(
        "def f():\n"
        "    exc = None\n"
        "    iterable = iter(range(1))\n"
        "    while True:\n"
        "        try:\n"
        "            yield next(iterable)\n"
        "        except StopIteration as exc:\n"
        "            x = exc.value\n"
        "            break\n"
        "    print(x)")
    assert compile_source(
        "def f():\n"
        "    yield from range(1)\n") == compile_

# Generated at 2022-06-14 02:43:44.096285
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_astunparse import unparse
    s = """
    def foo():
        yield from range(1)
    """
    tree = ast.parse(s)
    tree = YieldFromTransformer.run_pipeline(tree)
    result = unparse(tree)
    assert "iterable = iter(range(1))" in result

    s = """
    def foo():
        a = yield from range(1)
    """
    tree = ast.parse(s)
    tree = YieldFromTransformer.run_pipeline(tree)
    result = unparse(tree)
    assert "a = exc.value" in result


# Generated at 2022-06-14 02:43:49.986979
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    yft = YieldFromTransformer()  # type: ignore
    yft.visit(ast.Module(
                body=[
                    ast.Expr(
                        value=ast.YieldFrom(
                            value=ast.Name(id="iterable", ctx=ast.Load()),
                            lineno=2,
                            col_offset=4)
                    )
                ]
            )
    )

# Generated at 2022-06-14 02:43:51.606270
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor
    import sys
    import io

    sys.stdout = io.StringIO()


# Generated at 2022-06-14 02:43:53.243558
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()
    assert(t)

test_YieldFromTransformer()

# Generated at 2022-06-14 02:43:54.414697
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None, None)

# Generated at 2022-06-14 02:46:40.415616
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    '''Unit test for constructor of class YieldFromTransformer'''
    t = YieldFromTransformer()
    # the checker 'flake8' doesn't like the line below
    assert isinstance(t, YieldFromTransformer)


# Generated at 2022-06-14 02:46:45.438934
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    with open('tests/fixtures/yield_from.py') as f:
        source = f.read()

    tree = ast.parse(source)
    transformer = YieldFromTransformer()
    transformer.visit(tree)
    exec(compile(tree, '<dummy>', mode='exec'), {}, {})

# Generated at 2022-06-14 02:46:46.478897
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass    # TODO


# Generated at 2022-06-14 02:46:56.908035
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert not YieldFromTransformer.__init__.__annotations__
    assert YieldFromTransformer.target == (3, 2)
    assert not YieldFromTransformer.__dict__['__dict__']
    assert not YieldFromTransformer.__dict__['__weakref__']
    assert not YieldFromTransformer.__dict__['__doc__']
    assert YieldFromTransformer.__dict__['_get_yield_from_index'].__annotations__ == {'node': ast.AST, 'type_': Type[Holder], 'return': Optional[int]}
    assert YieldFromTransformer.__dict__['_emulate_yield_from'].__annotations__ == {'target': Optional[ast.AST], 'node': ast.YieldFrom, 'return': List[ast.AST]}
   

# Generated at 2022-06-14 02:46:59.222828
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.tree import print_tree


# Generated at 2022-06-14 02:47:00.234632
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Unit tests for class YieldFromTransformer"""
    YieldFromTransformer()

# Generated at 2022-06-14 02:47:04.357340
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import ast as python_ast
    from .base import BaseNodeTransformer
    from .yield_from_transformer import YieldFromTransformer

    # Unit test for method _get_yield_from_index

# Generated at 2022-06-14 02:47:06.761352
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .module import Module
    from ..utils import cst_to_ast
    from ..tests.test_execute import exec_code


# Generated at 2022-06-14 02:47:08.197981
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)

# Generated at 2022-06-14 02:47:08.987710
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__doc__ is not None