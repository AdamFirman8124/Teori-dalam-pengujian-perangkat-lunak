

# Generated at 2022-06-14 02:39:06.571882
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert True

# Generated at 2022-06-14 02:39:09.744191
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert issubclass(YieldFromTransformer, BaseNodeTransformer)
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'
    assert YieldFromTransformer.target == (3, 2)



# Generated at 2022-06-14 02:39:12.191177
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print('Testing construction of YieldFromTransformer')
    m = YieldFromTransformer()

    assert isinstance(m, YieldFromTransformer)
    assert m._tree_changed == False


# Generated at 2022-06-14 02:39:13.116907
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:20.738597
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.Expr(ast.YieldFrom(ast.Name('test')))
    node = YieldFromTransformer().visit(node)
    assert(
        ast.dump(node) ==
        "Expr(value=Call(func=Name(id='next', ctx=Load()), "
        "args=[Call(func=Name(id='iter', ctx=Load()), args=[Name(id='test', ctx=Load())], keywords=[])], "
        "keywords=[]))"
    )


# Generated at 2022-06-14 02:39:23.329992
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import compile_to_ast
    from ..utils.helpers import evaluate


# Generated at 2022-06-14 02:39:29.374392
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    test_YieldFromTransformer.__name__ == '__main__' and unittest.main()

if __name__ == '__main__':
    result = unittest.main(exit=False)
    for err in result.result.errors:
        print(err)


from .utils import NodeTestCase, get_all_nodes_from, get_expected_ast
from .utils import transform_and_compare  # noqa: E402



# Generated at 2022-06-14 02:39:32.164826
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class DummyCompiler:
        pass

    compiler = DummyCompiler()

    class DummyContext:
        pass

    context = DummyContext()
    YieldFromTransformer(compiler, context)



# Generated at 2022-06-14 02:39:33.035320
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:35.012915
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """YieldFromTransformer()"""
    assert YieldFromTransformer("")

# Generated at 2022-06-14 02:39:51.066940
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        from typed_ast import ast3 as ast
        from . import YieldFromTransformer
    except:
        from typed_ast import ast3 as ast
        from from_st import YieldFromTransformer
    s = "def func():\n  a = yield from [1, 2, 3]\n  b = yield from (i for i in range(10))\n  c = yield from [1, 2, 3]\n  d = yield from (i for i in range(10))\n  e = yield from [1, 2, 3]\n  f = yield from (i for i in range(10))"

    node = ast.parse(s)
    YieldFromTransformer(node).visit(node)

# Generated at 2022-06-14 02:39:59.837686
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse('yield from gen')
    node = tree.body[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.YieldFrom)

    cls = YieldFromTransformer()
    result = cls.visit(tree)

    assert isinstance(result, ast.Module)
    assert len(result.body) == 1
    assert isinstance(result.body[0], ast.Assign)
    assert isinstance(result.body[0].value, ast.Call)
    assert isinstance(result.body[0].targets[0], ast.Name)
    assert isinstance(result.body[0].targets[0].ctx, ast.Store)
    yield_from_iterable = result.body[0].value
    assert isinstance

# Generated at 2022-06-14 02:40:00.921606
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:10.374194
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor

    assert YieldFromTransformer.__name__ == "YieldFromTransformer"
    assert isinstance(YieldFromTransformer.target, tuple)
    assert YieldFromTransformer.target == (3, 2)

    assert astor.to_source(YieldFromTransformer.result_assignment) == \
        "if hasattr(exc, 'value'):\n" +\
        "    target = exc.value\n"


# Generated at 2022-06-14 02:40:15.569437
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # We can't test much here as this class is not *that* unit-testable
    # being a visitor.
    class TestNode(object):
        body = []
        def __init__(self, name):
            self.name = name
    node = TestNode("TestNode")
    yft = YieldFromTransformer()
    assert yft.visit(node) is node

# Generated at 2022-06-14 02:40:16.909857
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    isinstance(YieldFromTransformer(), YieldFromTransformer)

# Generated at 2022-06-14 02:40:18.200257
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert hasattr(YieldFromTransformer, '__init__')



# Generated at 2022-06-14 02:40:19.774005
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:40:30.658694
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    test_code = "def f():\n    a = yield from b()\n    yield from c()\n    d = yield from e()\n"
    tree = ast.parse(test_code)
    transformed_tree = YieldFromTransformer().visit(tree)

# Generated at 2022-06-14 02:40:35.019848
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None).tree_changed == False
    assert isinstance(YieldFromTransformer(None).target, tuple)
    assert YieldFromTransformer(None).visit(None) == None


# Generated at 2022-06-14 02:40:51.474305
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import TransformerTestCase

    class Test(TransformerTestCase):
        transformer = YieldFromTransformer
        file = __file__
        code = '''
            def func(x):
                while True:
                    y = yield from x
                    return y

            def func2(x):
                while True:
                    yield from x
                    return

            def func3(x):
                while True:
                    y = x
                    yield from y
                    return y

            def func4(x):
                while True:
                    y = x
                    yield from y
                    return

            def func5(x):
                y = yield from x
                return y

            def func6(x):
                yield from x
                return
        '''

        def test_call(self):
            self.transform('func')
            self.transform

# Generated at 2022-06-14 02:40:53.575258
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:55.203200
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from pytest import raises

    with raises(TypeError):
        YieldFromTransformer()

# Generated at 2022-06-14 02:41:02.499484
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.ast import from_code
    from ..utils.helpers import compile_to_ast

    code = """
    def test():
        a = yield from func()
        yield from func()
        (yield from func())
        for item in (yield from func()):
            pass
    """
    tree = from_code(code)
    YieldFromTransformer().visit(tree)
    result = compile_to_ast(tree)

# Generated at 2022-06-14 02:41:03.518584
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None

# Generated at 2022-06-14 02:41:05.360261
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert repr(YieldFromTransformer('#')) == "YieldFromTransformer('#')"


# Generated at 2022-06-14 02:41:11.444472
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor
    import textwrap
    code = textwrap.dedent("""
    def gen():
        if True:
            yield from [1, 2, 3]
    """)
    tree = astor.parse_file(code)
    transformer = YieldFromTransformer(3, 2)
    transformer.visit(tree)
    print(astor.to_source(tree))


if __name__ == "__main__":
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:41:18.002095
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from grako.codegen import codegen
    from grako.tool import compile_
    from node_transformers.v3.sequence_transformer import SequenceTransformer

    source = '''
    def f():
        yield from 1
    '''
    print('source', source)

    tree = compile_(source, 'example')
    print('tree', tree, '\n')

    result = codegen(tree)
    print('result', codegen(tree))

    transformers = [
        YieldFromTransformer,
        SequenceTransformer,
    ]
    for transformer in transformers:
        print(transformer.__name__)
        transformer().visit(tree)
        result = codegen(tree)
        print('->', result)
        print()

# Generated at 2022-06-14 02:41:24.990659
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  "test for YieldFromTransformer"
  def test_init():
    # arrange
    expected = 'YieldFromTransformer()'
    # act
    actual = YieldFromTransformer()
    # assert
    assert str(actual) == expected
  # test_init

  # execute tests
  test_init()


# Generated at 2022-06-14 02:41:27.085376
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == "YieldFromTransformer"

# Generated at 2022-06-14 02:41:42.129912
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    def expect(expected, node):
        assert ast.dump(node) == expected

    tree = ast.parse("""
    def method():
        yield from gen
        yield from gen2
        if c:
            print(yield from gen3)
            yield from gen4
    """, mode='exec')
    transformer = YieldFromTransformer()
    transformer.visit(tree)

# Generated at 2022-06-14 02:41:50.338776
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helper_functions import compile_snippet, assert_matches
    # Check if constructor of class YieldFromTransformer
    # raises Exception when called without arguments
    with pytest.raises(Exception):
        YieldFromTransformer()
    # Check if constructor of class YieldFromTransformer
    # raises Exception when called with incorrect arguments types
    with pytest.raises(Exception):
        YieldFromTransformer("a", "d", 2, True)
    # Check if constructor of class YieldFromTransformer
    # raises Exception when called with incorrect arguments
    with pytest.raises(Exception):
        YieldFromTransformer(value='a')
    # Check if constructor of class YieldFromTransformer
    # raises Exception when called with missing argument
    with pytest.raises(Exception):
        YieldFrom

# Generated at 2022-06-14 02:42:01.559857
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    #Arrange
    from .python_parse import parse
    code = """def f():
  x = yield from g()"""
    expected = """def f():
    try:
        iterable = iter(g())
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                x = exc.value
                break
    except GeneratorExit as exc:
        pass"""
    node = parse(code)

    #Act
    result = YieldFromTransformer().visit(node)
    print(ast.dump(node, include_attributes=True))
    print(ast.dump(result, include_attributes=True))

    #Assert
    assert ast.dump(result) == ast.dump(parse(expected))


# Generated at 2022-06-14 02:42:02.423016
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor

# Generated at 2022-06-14 02:42:03.801694
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    c = YieldFromTransformer()
    assert isinstance(c, BaseNodeTransformer)

# Generated at 2022-06-14 02:42:05.477794
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)


# Generated at 2022-06-14 02:42:07.061848
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print('Test constructor of class YieldFromTransformer')
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:15.332881
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import parse_ast
    a = parse_ast('''
    def foo():
        yield from a
    ''')
    b = parse_ast('''
    def foo():
        exc = VariablesGenerator.generate('exc')
        iterable = iter(a)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                break
    ''')
    assert YieldFromTransformer().visit(a) == b
    # TODO: add more assert


# Generated at 2022-06-14 02:42:18.131092
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.source import source
    fr = source('''
        def foo():
            a = yield from foo()
    ''')
    node = ast.parse(fr)
    YieldFromTransformer().visit(node)
    print(ast.dump(node))

# Generated at 2022-06-14 02:42:20.431032
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert x.target == (3, 2)
    assert repr(x) == '<YieldFromTransformer(3, 2)>'

# Generated at 2022-06-14 02:43:00.181544
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.Module([ast.FunctionDef(name="foo", body=[ast.If(test=ast.Name(id="foo_body", ctx=ast.Load()), body=[ast.If(test=ast.Name(id="check", ctx=ast.Load()), body=[ast.Assign(targets=[ast.Name(id="x", ctx=ast.Store())], value=ast.YieldFrom(value=ast.Name(id="bar", ctx=ast.Load())))], orelse=[])], orelse=[])], decorator_list=[])], decorator_list=[])
    tree = YieldFromTransformer().visit(tree)
    assert tree.body[0].body[0].body[0].body[0].value.func.id == 'next'

# Generated at 2022-06-14 02:43:05.018321
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class_instance = YieldFromTransformer()
    assert class_instance.__class__.__name__ == "YieldFromTransformer"
    assert YieldFromTransformer.target[0] == 3
    assert YieldFromTransformer.target[1] == 2


# Generated at 2022-06-14 02:43:06.279055
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


# Generated at 2022-06-14 02:43:11.105814
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.stubgen import generate_stub
    from ..utils.helpers import dump_ast
    with open('py3kast.pyi', 'w') as f:
        f.write(generate_stub(YieldFromTransformer))


# Generated at 2022-06-14 02:43:12.113086
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:43:13.083478
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:24.954318
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = 'from typing import Iterator, Iterable, Optional\n'
    yield_from_transformer = YieldFromTransformer()
    assert yield_from_transformer.__class__.__name__ == 'YieldFromTransformer'
    assert yield_from_transformer.target == (3, 2)
    assert yield_from_transformer._get_yield_from_index(ast.parse(code).body,
                                                        ast.Assign) == None
    assert yield_from_transformer._get_yield_from_index(ast.parse(code).body,
                                                        ast.Expr) == None
    assert yield_from_transformer._emulate_yield_from(None, None) == None

# Generated at 2022-06-14 02:43:26.552249
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer._tree_changed == False



# Generated at 2022-06-14 02:43:30.705151
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    source_code = """yield from x"""
    try:
        node = ast.parse(source_code).body[0].value
    except AttributeError as e:
        print(f"AttributeError: {e}")
    else:
        transformer = YieldFromTransformer()
        transformer.visit(node)


# Generated at 2022-06-14 02:43:31.754821
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from = YieldFromTransformer()

# Generated at 2022-06-14 02:44:07.226860
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)

# Generated at 2022-06-14 02:44:10.158773
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        YieldFromTransformer()
    except TypeError:
        assert False
    assert True

# Generated at 2022-06-14 02:44:20.744232
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()
    assert t.transform_snippet('''
    def f():
        a = yield from b
    ''') == '''
    def f():
        let(iterable)
        iterable = iter(b)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                a = exc.value
                break
    '''

    assert t.transform_snippet('''
    def f():
        yield from b
    ''') == '''
    def f():
        let(iterable)
        iterable = iter(b)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                break
    '''


# Generated at 2022-06-14 02:44:30.196335
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    y = ast.YieldFrom()
    y.value = 'value'
    y.lineno = 1
    y.col_offset = 2
    y.end_lineno = 3
    y.end_col_offset = 4
    yft = YieldFromTransformer(None, None)

    exc = ast.Name()
    exc.id = 'exc'
    exc.ctx = 'ctx'
    exc.lineno = 5
    exc.col_offset = 6
    exc.end_lineno = 7
    exc.end_col_offset = 8

    target = ast.Assign()
    target.target = 'target'
    target.value = 'value'
    target.lineno = 9
    target.col_offset = 10
    target.end_lineno = 11

# Generated at 2022-06-14 02:44:38.850813
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import BaseNodeTransformer
    from .body import BodyTransformer
    from .function import FunctionDefTransformer
    from .loop import ForTransformer
    from .if_ import IfTransformer
    from .while_ import WhileTransformer
    from .try_ import TryTransformer
    from .raise_ import RaiseTransformer
    from .with_ import WithTransformer
    from .withitem import WithitemTransformer
    from .class_ import ClassDefTransformer
    from .arguments import ArgumentsTransformer
    from .decorator import DecoratorTransformer
    from .delete import DelTransformer
    from .import_ import ImportFromTransformer
    from .annotations import AnnAssignTransformer, ArgTransformer, ReturnTransformer
    from .subscript import SubscriptTransformer
    from .tuple import TupleTransformer

# Generated at 2022-06-14 02:44:44.890701
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        ast.parse("a = yield from b")
    except SyntaxError:
        pass

    t = YieldFromTransformer()
    t.visit(ast.parse("a = yield from b"))
    t.visit(ast.parse("yield from b"))

# Generated at 2022-06-14 02:44:47.731521
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print('Testing constructor of class YieldFromTransformer')
    transformer = YieldFromTransformer()
    assert transformer.target == (3, 2)


# Generated at 2022-06-14 02:44:51.241807
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        yield_from_transformer_test = YieldFromTransformer(None, None)
    except Exception:
        yield_from_transformer_test = None
    assert(yield_from_transformer_test is not None)

# Generated at 2022-06-14 02:44:52.521025
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:45:07.381397
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:46:13.552748
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.FunctionDef('f', None, ast.arguments(), [], [])
    transformer = YieldFromTransformer()
    transformed = transformer.visit(node)


# Generated at 2022-06-14 02:46:22.929303
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # snippet code for testing
    @snippet
    def snippet_YieldFromTransformer():
        let(foo)
        foo = yield from [1, 2, 3]
        let(bar)
        bar = yield from (1, 2, 3)
        let(baz)
        baz = (1, 2, 3)
        yield from baz

    # testing code
    import ast
    # convert snippet to AST
    node = ast.parse(snippet_YieldFromTransformer.__doc__)
    # compile snippet code
    cc = compile(node, '<test>', 'exec')
    # run snippet code
    exec(cc)
    # obj testing
    assert foo == 3
    assert bar == 3
    assert baz == 3

# Generated at 2022-06-14 02:46:24.398435
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().__class__.__name__ == "YieldFromTransformer"

# Generated at 2022-06-14 02:46:37.347490
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Private method _get_yield_from_index
    node = ast.parse("yield from")
    transformer = YieldFromTransformer()
    assert transformer._get_yield_from_index(node, ast.Expr) == 0
    assert transformer._get_yield_from_index(node, ast.Assign) is None

    node = ast.parse("a = yield from")
    transformer = YieldFromTransformer()
    assert transformer._get_yield_from_index(node, ast.Expr) is None
    assert transformer._get_yield_from_index(node, ast.Assign) == 0
    
    # Private method _emulate_yield_from
    node = ast.parse("yield from")
    transformer = YieldFromTransformer()
    node = transformer._emulate_yield_

# Generated at 2022-06-14 02:46:43.422916
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().transform([]) == []
    assert YieldFromTransformer().transform([1]) == [1]
    assert YieldFromTransformer().transform([1, 2, 3]) == [1, 2, 3]
    assert YieldFromTransformer().transform(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert YieldFromTransformer().transform(['a', 'b', 2, 3]) == ['a', 'b', 2, 3]
    assert YieldFromTransformer().transform([(1, 2), 3, 4]) == [(1, 2), 3, 4]

# Generated at 2022-06-14 02:46:52.410956
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    snippet = """\
try:
    result = yield from generator
except Exception as exc:
    pass
"""

    expected = """\
result = None
iterable = None
exc = None
iterable = iter(generator)
while True:
    try:
        result = next(iterable)
    except StopIteration as exc:
        if hasattr(exc, 'value'):
            result = exc.value
        break
"""

    node = ast.parse(snippet)
    YieldFromTransformer().visit(node)
    assert ast.dump(node) == expected


# Generated at 2022-06-14 02:47:01.402464
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import parse
    from ..utils.node_util import NodeUtil
    node = parse(
        "import sys\ndef func():\n"
        "    stmt1\n"
        "    a = yield from generator()\n"
        "    stmt2"
    )
    transformer = YieldFromTransformer()
    transformer.visit(node)

# Generated at 2022-06-14 02:47:08.855395
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__),'../..','utils'))
    from test_utils import assert_program

    code1_in = '''\
    n = 0
    for i in range(10):
        n = n + (yield from [1,2,3])
    '''


# Generated at 2022-06-14 02:47:10.432687
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    trans = YieldFromTransformer()
    assert trans is not None

# Generated at 2022-06-14 02:47:12.569048
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import sys
    transformer = YieldFromTransformer()
    assert(transformer)
    return transformer
