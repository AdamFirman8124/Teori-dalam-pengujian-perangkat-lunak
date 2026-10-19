

# Generated at 2022-06-14 02:39:04.250279
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass # TODO

# Generated at 2022-06-14 02:39:04.855774
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:39:13.457130
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import ast_transformer
    from ..utils.helpers import to_code
    # class declaration

# Generated at 2022-06-14 02:39:14.856089
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer


# Generated at 2022-06-14 02:39:18.055317
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    def f():
        yield from range(3)

    tree = ast.parse(inspect.getsource(f))

# Generated at 2022-06-14 02:39:27.220826
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().visit(
        ast.parse("""
        from typing import Iterator
        from functools import partial
        """))

# Generated at 2022-06-14 02:39:28.238932
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    return YieldFromTransformer()


# Generated at 2022-06-14 02:39:29.146355
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:32.642099
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class A():
        def __init__(self):
            self.a = 1
            self.b = 2
    a = A()
    assert YieldFromTransformer.__init__(a) is None
    assert a.target == (3, 2)


# Generated at 2022-06-14 02:39:33.697785
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:40.554604
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  yield_from_transformer = YieldFromTransformer()
  assert(yield_from_transformer is not None)


# Generated at 2022-06-14 02:39:43.304294
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'
    assert hasattr(YieldFromTransformer, 'target')


if __name__ == '__main__':
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:39:44.730939
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YFT = YieldFromTransformer()
    assert YFT is not None

# Generated at 2022-06-14 02:39:54.006886
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.parser import parse_to_ast

    def check_code(code_before, code_after):
        ast_before = parse_to_ast(code_before)
        ast_after = parse_to_ast(code_after)
        ast_transformed = YieldFromTransformer().visit(ast_before)

        assert ast_transformed == ast_after


# Generated at 2022-06-14 02:39:55.306858
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert(YieldFromTransformer)


# Generated at 2022-06-14 02:40:06.205692
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = create_function(['a'], 'yield from a')
    assert YieldFromTransformer().visit(node) == create_function(['a'], """
        try:
            iterable = iter(a)
            while True:
                try:
                    yield next(iterable)
                except StopIteration as exc:
                    exc = exc.value
                    break
        except StopIteration as exc:
            exc = exc.value
    """)

    node = create_function(['a'], 'b = yield from a')

# Generated at 2022-06-14 02:40:07.193050
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    return YieldFromTransformer()

# Generated at 2022-06-14 02:40:11.021766
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Test that the class is instantiable and all methods are implemented."""
    transform = YieldFromTransformer()
    assert all([hasattr(transform, attr) for attr in dir(transform) if not attr.startswith('_')])

# Generated at 2022-06-14 02:40:12.064237
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer


# Generated at 2022-06-14 02:40:12.842779
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:40:24.977577
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        YieldFromTransformer()
    except TypeError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 02:40:26.827702
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Unit test for constructor of class YieldFromTransformer"""
    YieldFromTransformer()


# Generated at 2022-06-14 02:40:35.693492
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    def verify(code, expected):
        tree_in = ast.parse(code.strip())
        tree_out = ast.parse(expected.strip())
        YieldFromTransformer().visit(tree_in)
        assert ast.dump(tree_in) == ast.dump(tree_out)

    # Tests for the following case:

    ## def f():
    ##     a = (yield from b) + 1

    code = """
        def foo():
            a = (yield from bar()) + 1
    """
    expected = """
        def foo():
            a = None
            while True:
                try:
                    a = next(bar())
                    yield a
                except StopIteration as exc:
                    result_assignment(exc, a)
                    break
            a = a + 1
    """

# Generated at 2022-06-14 02:40:47.985240
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse('''\
yield from c_1
yield from c_2
''')
    YieldFromTransformer().visit(tree)

    assert ast.dump(tree) == '''\
Module(body=[
    While(test=NameConstant(value=True), body=[
        Try(body=[
            Expr(value=Call(func=Name(id='next', ctx=Load()), args=[Name(id='iterable', ctx=Load())], keywords=[])),
            Break()],
            orelse=[],
            finalbody=[],
            handlers=[ExceptHandler(type=Name(id='StopIteration', ctx=Load()), name='exc', body=[Break()])]),
    ], orelse=[],
    nl=[])
])'''



# Generated at 2022-06-14 02:40:48.928153
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)

# Generated at 2022-06-14 02:40:50.177398
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yf = YieldFromTransformer()


# Generated at 2022-06-14 02:41:00.217766
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("""
try:
        yield from a
except Exception as e:
        pass
    """)  # type: ast.Try

    from .test_lets import LetTransformer
    from .test_name_inference import NameInferenceTransformer
    from ..utils import Transformer

    t = Transformer(YieldFromTransformer, NameInferenceTransformer, LetTransformer)

    tree = t.run_on(tree)

    assert str(tree) == """\
try:
    __let_iterable
    __let_iterable = iter(a)
    while True:
        try:
            yield next(__let_iterable)
        except StopIteration as e:
            e = e.value
            break
except Exception as e:
    pass\
"""

# Generated at 2022-06-14 02:41:04.969184
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = ast.parse('x = yield from y')
    t = YieldFromTransformer(3, 2).visit(t)
    assert ast.dump(t) == "y = iter(y)\nwhile True:\n    try:\n        a = next(y)\n    except StopIteration as e:\n        x = e.value\n        break"

# Generated at 2022-06-14 02:41:05.954547
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:12.311242
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_helpers import assert_equal_source
    from .test_helpers import generate_source_from_fn
    from ..utils.helpers import import_module_from_source
    from ..utils.helpers import get_function_from_module


# Generated at 2022-06-14 02:41:29.082378
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .miniutils import assert_source

    class_node = YieldFromTransformer()
    assert_source(class_node,
                  """
    def mygen():
        yield from range(10)
    """,
                  """
    def mygen():
        __iterator_0 = iter(range(10))
        while True:
            try:
                yield next(__iterator_0)
            except StopIteration as __iterator_exc:
                break
    """)


# Generated at 2022-06-14 02:41:34.114298
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from code_monkey.node_transforms.py3to2.base import NodeTransformer
    test_object = YieldFromTransformer()
    assert isinstance(test_object, NodeTransformer)
    assert test_object.target == (3, 2)
    assert test_object._tree_changed == False


# Generated at 2022-06-14 02:41:35.705928
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

test_YieldFromTransformer()

# Generated at 2022-06-14 02:41:37.210424
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:41:42.018049
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import ast_transforms  # pylint: disable=import-outside-toplevel
    from ..testing.utils import TreeBuilder

    tree = TreeBuilder().with_module().body(
        [
            let(x).assign(0),
            let(generator).assign(
                ast.YieldFrom(
                    value=ast.Name(id='x', ctx=ast.Load()),
                    lineno=0,
                    col_offset=0
                )
            ),
            let(y).assign(
                next(generator)
            )
        ]
    ).get()

    tree = ast_transforms.YieldFromTransformer(tree).result()


# Generated at 2022-06-14 02:41:50.274317
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Unit test for method _get_yield_from_index of class YieldFromTransformer
    def test_YieldFromTransformer__get_yield_from_index():
        pass

    # Unit test for method _emulate_yield_from of class YieldFromTransformer
    def test_YieldFromTransformer__emulate_yield_from():
        pass

    # Unit test for method _handle_assignments of class YieldFromTransformer
    def test_YieldFromTransformer__handle_assignments():
        pass

    # Unit test for method _handle_expressions of class YieldFromTransformer
    def test_YieldFromTransformer__handle_expressions():
        pass

    # Unit test for method visit of class YieldFromTransformer
    def test_YieldFromTransformer_visit():
        pass

# Generated at 2022-06-14 02:41:51.340670
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:41:59.524524
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .juggle_nodes import JuggleNodesTransformer
    from .. import Backend
    from ..utils.helpers import dump_tree

    backend = Backend.as_backend(r'print(eval("yield from (x for x in [])"))')
    tree = backend.ast_tree
    tree = JuggleNodesTransformer(backend).visit(tree)
    tree = YieldFromTransformer().visit(tree)
    dump_tree(tree)



# Generated at 2022-06-14 02:42:00.697909
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(True)

# Generated at 2022-06-14 02:42:01.870831
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # We create a YieldFromTransformer object
    YieldFromTransformer()


# Generated at 2022-06-14 02:42:20.638918
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.fixtures import make_test_function
    from .base import BaseNodeTransformer
    from ..utils.helpers import dump_ast

    def test():
        lst = []
        for i in range(5):
            lst.append(i)
            yield from i

    node = make_test_function(test)
    YFT = YieldFromTransformer()
    bnt = BaseNodeTransformer()

    assert isinstance(YFT, YieldFromTransformer)
    assert isinstance(bnt, BaseNodeTransformer)
    assert isinstance(YFT, BaseNodeTransformer)
    assert isinstance(bnt, YieldFromTransformer)
    assert node == YFT.visit(node)

# Generated at 2022-06-14 02:42:22.466331
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:29.958935
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.test import assert_subtree, assert_tree
    from ..utils.test import get_node as N
    from ..utils.test import get_children as C

    tree = N(ast.Module, C(
        N(ast.Assign, C(
            N(ast.Name, C(
                N(ast.Store, C(
                    N(ast.Str, C('y'))))))))),
        N(ast.Expr, C(
            N(ast.YieldFrom, C(
                N(ast.Call, C(
                    N(ast.Name, C(
                        N(ast.Store, C(
                            N(ast.Str, C('func'))))))),
                    N(ast.arguments, C()))))))),

# Generated at 2022-06-14 02:42:31.125157
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()


# Generated at 2022-06-14 02:42:31.893617
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:42:39.387245
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("""
yield_from_transformer = YieldFromTransformer()
""")
    assert str(tree) == "Module(body=[Assign(targets=[Name(id='yield_from_transformer', ctx=Store())], value=Call(func=Name(id='YieldFromTransformer', ctx=Load()), args=[], keywords=[]))])"

# Generated at 2022-06-14 02:42:40.016216
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print(YieldFromTransformer())


# Generated at 2022-06-14 02:42:41.621593
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert False, "Not implemented yet"

# Generated at 2022-06-14 02:42:42.413262
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:43.178296
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    return None


# Generated at 2022-06-14 02:43:06.922382
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == "YieldFromTransformer"
    assert YieldFromTransformer.__qualname__ == __name__ + ".YieldFromTransformer"

# Generated at 2022-06-14 02:43:08.506886
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert x is not None


# Generated at 2022-06-14 02:43:10.053247
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    case = ast.AST()
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:12.702288
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert hasattr(x, 'visit_FunctionDef')
    assert hasattr(x, 'visit_YieldFrom')

# Generated at 2022-06-14 02:43:15.587871
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yft = YieldFromTransformer()
    assert type(yft) == YieldFromTransformer
    return yft


# Generated at 2022-06-14 02:43:19.431705
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None

# Unit tests for method YieldTransformer._get_yield_from_index
# of class YieldTransformer

# Generated at 2022-06-14 02:43:20.907850
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:27.170885
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    y = YieldFromTransformer()
    assert y.target == (3, 2)
    assert y._get_yield_from_index(None, None) is None
    assert y._handle_assignments(None) is None
    assert y._handle_expressions(None) is None
    assert y.visit(None) is None


# Generated at 2022-06-14 02:43:34.597718
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    module = ast.parse(
        'def foo(a):\n'
        '    x = yield from bar(a)\n'
        '    yield from baz(a)\n'
        'def foo2(a):\n'
        '    foo(a)\n'
        '    yield from bar2(a)\n'
    )
    transformer = YieldFromTransformer()
    transformer.visit(module)

    assert transformer.tree_changed is True

# Generated at 2022-06-14 02:43:41.201654
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert ast.dump(YieldFromTransformer().visit(ast.parse(textwrap.dedent("""
    def a():
        yield from [1, 2, 3]
    """)))) == textwrap.dedent("""
    def a():
        iterable = iter([1, 2, 3])
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                pass
    """)


# Generated at 2022-06-14 02:44:37.697443
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.ast3 import parse

    node = parse("""\
a = yield from b + c
a = yield from {1, 2, 3}
a = yield from [1, 2, 3]
a = yield from (1, 2, 3)
a = yield from F(1, 2, 3)
""")
    node = YieldFromTransformer().visit(node)
    print(ast.dump(node))

# Generated at 2022-06-14 02:44:48.915038
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    parser = ast.PyCF_ONLY_AST.parse
    source = '''def f():
    yield from iterable'''
    tree = parser(source)
    transformed = YieldFromTransformer().visit(tree)
    emulated = parser('''def f():
    iterable_ = iter(iterable)
    while True:
        try:
            yield next(iterable_)
        except StopIteration as exc:
            break''')
    assert ast.dump(transformed) == ast.dump(emulated)



# Generated at 2022-06-14 02:44:57.907545
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node0 = ast.parse('def f(): yield from 0')
    node1 = ast.parse('def f(): a = yield from 0')
    node2 = ast.parse('def f(): (yield from 0)')
    node3 = ast.parse('def f(): [yield from 0]')
    node4 = ast.parse('def f(): {yield from 0}')
    node5 = ast.parse('def f(): (a for a in (yield from 0))')
    node6 = ast.parse('def f(): yield from 0 + a')
    node7 = ast.parse('def f(): (yield from 0) ** 2')
    node8 = ast.parse('def f(): (yield from 0) == 2')
    node9 = ast.parse('def f(): (yield from 0) is 2')
    node10

# Generated at 2022-06-14 02:45:00.136106
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(False).target == (3, 2)

# Generated at 2022-06-14 02:45:10.774982
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("""
a = (yield from b)
b = (yield from c)
c = (yield from d)
d = (yield from e)
""")
    transformer = YieldFromTransformer()
    transformer.visit(tree)
    assert transformer._tree_changed is True

# Generated at 2022-06-14 02:45:11.247079
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert True

# Generated at 2022-06-14 02:45:12.096898
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:45:21.630891
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .tree_transformers import TreeTransformers  # pylint: disable=
    from .compile_py import compile_py_tree  # pylint: disable=
    from ..utils.source import source_to_ast  # pylint: disable=
    from ..utils.helpers import get_tree_string  # pylint: disable=
    from ..utils.pytree import PyTree  # pylint: disable=
    from ..utils.helpers import VariablesGenerator  # pylint: disable=

    tt = TreeTransformers()
    tt.transformers.append(YieldFromTransformer)
    source = """
    def foo(x: int) -> List[int]:
        s = yield from x
        return s
    """
    tree = PyTree(source_to_ast(source))
   

# Generated at 2022-06-14 02:45:30.296568
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import typed_astunparse
    from .. import module_inliner
    from ..utils.helpers import get_ast

    text = (
        '''
        def f():
            (a, b) = yield from g()
            return a + b
        '''
    )
    tree = get_ast(text)
    tree = module_inliner.inline_imports(tree)
    tree = YieldFromTransformer().visit(tree)

# Generated at 2022-06-14 02:45:31.491048
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:47:19.987852
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yieldFromTransformer = YieldFromTransformer()

# Generated at 2022-06-14 02:47:29.168568
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = "def f():\n    yield from gen\n"
    tree = ast.parse(code)
    YieldFromTransformer().visit(tree)
    expected = '''def f():
    let(iterable)
    iterable = iter(gen)
    while True:
        try:
            yield next(iterable)
        except StopIteration as exc:
            if hasattr(exc, 'value'):
                exc.value
            break
'''
    assert expected == astunparse.unparse(tree)

# Generated at 2022-06-14 02:47:32.935191
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        assert issubclass(YieldFromTransformer, BaseNodeTransformer)
    except:
        print_exc()
        return False
    else:
        return True


# Generated at 2022-06-14 02:47:34.272011
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)


# Generated at 2022-06-14 02:47:42.791238
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    with preimport._context({'typed_ast': (0, 6, 0)}):
        from typed_ast import ast3
        from typed_ast import ast27

        transformer = YieldFromTransformer()
        tree = ast3.parse('from __future__ import generators\n'
                          'def func():\n'
                          '    yield from range(10)')
        tree = transformer.visit(tree)
        source = ast27.unparse(tree).strip()

# Generated at 2022-06-14 02:47:48.313190
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # arrange
    node = """
        a = yield from b
    """
    expected = """
        let(iterable)
        iterable = iter(b)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                a = exc.value
                break
    """
    node = ast.parse(node).body[0]

    # act
    actual = YieldFromTransformer(target=(3, 2)).visit(node)

    # assert
    assert expected == ast.unparse(actual)

# Generated at 2022-06-14 02:47:54.620621
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse('def foo():\n'
                     '    a = (yield from foo())\n')
    YieldFromTransformer().visit(node)
    assert str(node) == ('def foo():\n'
                         '    iterable = iter(foo())\n'
                         '    while True:\n'
                         '        try:\n'
                         '            yield next(iterable)\n'
                         '        except StopIteration as exc:\n'
                         '            a = exc.value\n'
                         '            break')

    node = ast.parse('def foo():\n'
                     '    yield from foo()\n')
    YieldFromTransformer().visit(node)

# Generated at 2022-06-14 02:48:01.338920
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = """
        def test():
            a = yield from b()
            yield from c()
        """
    expected = """
        def test():
            let(iterable)
            iterable = iter(b())
            while True:
                try:
                    yield next(iterable)
                except StopIteration as exc:
                    if hasattr(exc, 'value'):
                        a = exc.value
                    break
            let(iterable)
            iterable = iter(c())
            while True:
                try:
                    yield next(iterable)
                except StopIteration as exc:
                    break
        """
    assert str(YieldFromTransformer().visit(ast.parse(code))) == expected


# Generated at 2022-06-14 02:48:03.505988
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    y = YieldFromTransformer()

# Generated at 2022-06-14 02:48:04.767918
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()
    assert t is not None