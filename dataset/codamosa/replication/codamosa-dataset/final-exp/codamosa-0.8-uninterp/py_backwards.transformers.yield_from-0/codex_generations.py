

# Generated at 2022-06-14 02:39:05.977423
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        YieldFromTransformer
    except NameError:
        raise AssertionError('You need to implement a class named YieldFromTransformer')


# Generated at 2022-06-14 02:39:11.355783
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert repr(YieldFromTransformer(ast.parse("""
        def f():
            yield from data
    """))) == repr(YieldFromTransformer(ast.parse("""
        def f():
            let(iterable)
            iterable = iter(data)
            while True:
                try:
                    yield next(iterable)
                except StopIteration as exc:
                    break
    """)))

# Generated at 2022-06-14 02:39:12.520506
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:39:13.809614
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)

# Generated at 2022-06-14 02:39:16.829676
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from sys import version_info
    from ..utils import core as test

    assert version_info >= test.target  # type: ignore
    transformer = YieldFromTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:39:24.007853
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ast_parser.utils.examples import get_example_ast
    from ast_parser.utils.tree import dump_to_str
    from ast_parser.utils.helpers import get_string_from_module
    from typed_ast import ast3

    target = ast3.parse(get_string_from_module(get_example_ast), '<example>', 'exec')
    new_target = YieldFromTransformer().visit(target)
    assert dump_to_str(target) != dump_to_str(new_target)

# Generated at 2022-06-14 02:39:33.472606
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..transpile import Transpiler
    from ..transpile.fixers import MetaFixer
    from tests.utils import run_transpile
    import astunparse
    import textwrap

    class TestsTranspiler(Transpiler):

        fixers = MetaFixer.fixers + [YieldFromTransformer]

    transpiler = TestsTranspiler()


# Generated at 2022-06-14 02:39:42.938778
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..compiler import compile_to_python

    class TestTransformer(YieldFromTransformer):
        """Simple test transformer"""

        def __init__(self):
            super().__init__(
                lambda n: n.module,
            )

    test_code = """
        def test():
            a = yield from [1, 2, 3, 4]
            b = yield from test_2()
    """

# Generated at 2022-06-14 02:39:45.358587
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tr = YieldFromTransformer()
    assert tr is not None

if __name__ == "__main__":
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:39:54.197848
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.test_visitor import test
    from ..source import Source
    from .. import settings
    from .. import main
    from astor.code_gen import to_source

    settings.COMPILE_YIELD_FROM = True
    result = main.transpile_file(Source(
        'tests/resources/try_except.py',
        settings=settings
    ))


# Generated at 2022-06-14 02:40:00.865960
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:40:01.878869
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer

# Generated at 2022-06-14 02:40:02.502458
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None

# Generated at 2022-06-14 02:40:14.391486
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.example import example
    try:
        ast.parse('print(1)')
    except SyntaxError:
        return
    unit = example('''
        def generator():
            yield 1
            yield 2
            yield 3

        def main():
            a = 0
            b = yield from generator()
            print(a, b)
        ''')
    YieldFromTransformer().visit(unit)

# Generated at 2022-06-14 02:40:15.686593
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    constructor = YieldFromTransformer()
    assert constructor is not None

# Generated at 2022-06-14 02:40:27.090700
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # A test with module node
    mod = ast.parse('''
        def foo():
            try:
                yield from bar
            except Exception as e:
                pass
    ''')
    YieldFromTransformer().visit(mod)
    expected = '''
        def foo():
            try:  # noqa
                let(iterable)
                iterable = iter(bar)
                while True:
                    try:
                        yield next(iterable)
                    except StopIteration as exc:
                        pass
                        break
            except Exception as e:  # noqa
                pass
    '''
    assert ast.dump(mod) == expected
    # A test with class node

# Generated at 2022-06-14 02:40:29.229332
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer  # using just to shut up linter

# Unit tests for methods of class YieldFromTransformer

# Generated at 2022-06-14 02:40:33.486058
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..rewriter import Rewriter
    from ..sources import read_file

    # Testing that constructor of class YieldFromTransformer works
    # without raising an exception
    tree = ast.parse(read_file(__file__))
    transformer = YieldFromTransformer()
    Rewriter(ast_node=tree, transformers=[transformer])

# Generated at 2022-06-14 02:40:35.670745
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node_transformer = YieldFromTransformer()
    node_transformer.visit()

# Generated at 2022-06-14 02:40:47.980423
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.ast3 import parse

    source = '''
    def foo(a):
        x, y = a
        yield from range(x, y)
        x = yield from range(x, y)
        yield from range(x, y)
        return x
    '''


# Generated at 2022-06-14 02:40:55.537136
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:41:03.911636
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import make_test_cases, to_source
    from ..main import main

    bytearray_code = bytearray(open('test_cases/yield_from_transformer/main.py').read(), 'utf-8')
    expected = bytearray(open('test_cases/yield_from_transformer/main_expected.py').read(), 'utf-8')
    options = main(bytearray_code)
    result = options['result_tree']
    assert(to_source(result) == expected.decode("utf-8"))

# Generated at 2022-06-14 02:41:04.688215
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    b = YieldFromTransformer()



# Generated at 2022-06-14 02:41:09.681973
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.codegen import to_source
    from ..utils.helpers import parse
    from ..utils.visitor import NodeTransformerPass

    source = """
    def fn():
        temp = yield from [1, 2, 3]
        return temp
    """

    tree = parse(source)
    tree = NodeTransformerPass(tree, [YieldFromTransformer]).result()
    tree = to_source(tree)

# Generated at 2022-06-14 02:41:16.869901
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import get_ast, get_tree
    from ..utils.python import PythonNodeType
    from .base import TreeTransformer, NodeTransformer
    #from .base import *
    #from .base import __all__
    from .ast3 import *
    print(__all__)
    print(__name__)
    print(__package__)
    print(__file__)
    print(YieldFromTransformer.__qualname__)
    ast_ = get_ast('''
        yield from foo()

        def bar():
            yield from foo()
    ''')
    trans = YieldFromTransformer()
    tree = get_tree(ast_, trans)
    print(tree)

# Generated at 2022-06-14 02:41:21.169155
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor
    import sys

    if sys.version_info < (3, 3):
        return

    source = """
    def func(a):
        yield from a
        yield from a
        x = yield from a
        yield from a + 1
        yield from a or 1
        yield from a and 1
        yield from a[1]
        yield from 1, a
        yield from (a, 1)
    """

# Generated at 2022-06-14 02:41:22.541133
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:41:25.164846
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().target == (3, 2)



# Generated at 2022-06-14 02:41:38.878325
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    _tree_changed = False
    _target = (3, 2)

    def _get_yield_from_index(node: ast.AST, type_: Type[Holder]) -> Optional[int]:
        if hasattr(node, 'body') and isinstance(node.body, list):  # type: ignore
            for n, child in enumerate(node.body):  # type: ignore
                if isinstance(child, type_) and isinstance(child.value, ast.YieldFrom):
                    return n

        return None

    def _emulate_yield_from(target: Optional[ast.AST], node: ast.YieldFrom) -> List[ast.AST]:
        exc = VariablesGenerator.generate('exc')

# Generated at 2022-06-14 02:41:48.916909
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    module = ast.parse('def test(a):\n  return a')
    YieldFromTransformer().visit(module)
    module = ast.parse('def test(a):\n  yield from a\n  return a')
    YieldFromTransformer().visit(module)
    module = ast.parse('def test(a):\n  yield a')
    YieldFromTransformer().visit(module)
    module = ast.parse('def test(a):\n  a = yield from a\n  return a')
    YieldFromTransformer().visit(module)
    module = ast.parse('def test(a):\n  a = yield from a')
    YieldFromTransformer().visit(module)

# Generated at 2022-06-14 02:42:08.969258
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = "yield from (1, 2, 3)"
    node = ast.parse(code)
    transformer = YieldFromTransformer()
    node = transformer.visit(node)
    assert transformer.is_changed() is True
    assert node.body[0].value.func.id == 'iter'
    assert node.body[0].value.args[0].elts[0].n == 1
    assert node.body[0].value.args[0].elts[1].n == 2
    assert node.body[0].value.args[0].elts[2].n == 3
    assert code == ast.dump(node)

# Generated at 2022-06-14 02:42:13.499347
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    ast.parse("""
x = yield from expression1
expression2
yield from expression3
""")
    ast.parse("""
yield from expression1
""")
    ast.parse("""
yield from expression1
""")
    ast.parse("""
yield from expression1
""")

# Generated at 2022-06-14 02:42:14.350459
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__doc__ is not None

# Generated at 2022-06-14 02:42:21.122866
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        class EmptyClass():
            pass
    except:
        EmptyClass = type('EmptyClass', (object,), {})
    try:
        attr_1835630156 = YieldFromTransformer.__new__
        def new_impl(cls):
            return object.__new__(cls)
        YieldFromTransformer.__new__ = new_impl
    except:
        pass
    else:
        del attr_1835630156
    return YieldFromTransformer()

# Testing snippet for result_assignment

# Generated at 2022-06-14 02:42:22.731301
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


# Generated at 2022-06-14 02:42:30.156929
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import BaseASTMultiplyInheritTestCase
    from ..multitransform.yield_from import YieldFromTransformer

    class BaseTestCase(BaseASTMultiplyInheritTestCase):
        transformer = YieldFromTransformer
        target = (3, 2)

    class TestYieldFromTransformer(BaseTestCase):
        __test__ = True

        @staticmethod
        def transform(body):
            return [ast.Expr(v) for v in body]

        def test_simple_yield_from(self):
            yield 'yield from anything', """
                yield from anything
                """

            yield 'yield from (anything)', """
                yield from (anything)
                """

            yield 'yield from yield from anything', """
                yield from yield from anything
                """


# Generated at 2022-06-14 02:42:42.622267
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..combinators import TransformerCombinator
    from ..tree import Module
    from ..utils.helpers import VariablesGenerator
    from ..utils.snippet import let, extend
    from ..utils import serialize

    module = Module()
    module.body.append(let(var, var2, var3)['var = var2 = var3 = 10'])
    module.body.append(let(result)['result = yield from var'])
    module.body.append(let(var4)['var4 = yield from result'])
    ccomb = TransformerCombinator(YieldFromTransformer())
    ccomb.visit(module)

    mod = Module()
    exc = VariablesGenerator.generate('exc')
    assignment = result_assignment.get_body(exc=exc, target='result')
   

# Generated at 2022-06-14 02:42:47.733270
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.test import tree_to_str, compare_nodes
    from ..test_enumerate_precompiler import test_snippets

    nodes = [ast.parse(test_snippets[0])]

    expect = ast.parse(test_snippets[1])
    actual = YieldFromTransformer().visit(nodes[0])
    compare_nodes(expect, actual)
    print(tree_to_str(actual))



# Generated at 2022-06-14 02:42:52.798755
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer._get_yield_from_index(ast.AST(), ast.Expr) == None
    assert YieldFromTransformer._get_yield_from_index(ast.AST(), ast.Assign) == None
    assert YieldFromTransformer._get_yield_from_index(ast.Module(), ast.Expr) == None
    assert YieldFromTransformer._get_yield_from_index(ast.Module(), ast.Assign) == None
    assert YieldFromTransformer._get_yield_from_index(ast.Module(), ast.Expr) == None
    assert YieldFromTransformer._get_yield_from_index(ast.Module(), ast.Expr) == None


# Generated at 2022-06-14 02:42:58.237609
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .base import NodeTransformer
    assert issubclass(YieldFromTransformer, NodeTransformer)
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'
    try_yield_from = YieldFromTransformer()
    assert try_yield_from.tree is None
    assert try_yield_from.target == (3, 2)


# Generated at 2022-06-14 02:43:26.753713
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer.target == (3, 2)
    assert transformer.visit
    assert transformer.generic_visit
    assert transformer._get_yield_from_index
    assert transformer._emulate_yield_from
    assert transformer._handle_assignments
    assert transformer._handle_expressions

# Generated at 2022-06-14 02:43:30.477337
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..compiler import compile
    from ..generator import Generator

    @Generator
    def gen(a):
        for i in range(a):
            yield (yield from range(a)) + 1
    assert compile(gen, 3.6)


__all__ = ['YieldFromTransformer']

# Generated at 2022-06-14 02:43:31.446627
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:35.137828
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.transforms import YieldFromTransformer

    def test():
        yield_from = YieldFromTransformer()
        print(yield_from)

    test()

# Generated at 2022-06-14 02:43:37.587542
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..tests.test_transformers import run_transformers_tests
    run_transformers_tests(YieldFromTransformer)

# Generated at 2022-06-14 02:43:47.243566
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer.target == (3, 2)
    assert transformer._tree_changed is None
    assert not hasattr(YieldFromTransformer, "visit_Module")
    assert not hasattr(YieldFromTransformer, "visit_FunctionDef")
    assert not hasattr(YieldFromTransformer, "visit_For")
    assert not hasattr(YieldFromTransformer, "visit_If")
    assert not hasattr(YieldFromTransformer, "visit_Try")
    assert not hasattr(YieldFromTransformer, "visit_While")
    assert not hasattr(YieldFromTransformer, "visit_Assign")
    assert not hasattr(YieldFromTransformer, "visit_Expr")

# Generated at 2022-06-14 02:43:54.089130
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.FunctionDef(name='foo',
                           args=ast.arguments(args=[],
                                              kwonlyargs=[],
                                              vararg=None,
                                              kwarg=None,
                                              defaults=[],
                                              kw_defaults=[]),
                           body=[ast.Expr(value=ast.YieldFrom(value=ast.Num(n=1)))],
                           decorator_list=[],
                           returns=None)
    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:43:55.105949
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:44:05.341477
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("""
    def f():
        a = yield from range(2)
        b = yield from range(2)  # doctest: +SKIP
        print(a, b)  # doctest: +SKIP
    """
    )
    transformer = YieldFromTransformer()
    transformer.visit(tree)
    assert transformer.tree_changed

# Generated at 2022-06-14 02:44:06.764768
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)


# Generated at 2022-06-14 02:45:12.474619
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 02:45:15.702605
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    from .annotator import Annotator
    from .resolver import Resolver
    from .optimizer import Optimizer
    from .codegen import CodeGenerator
    from . import YieldFromTransformer


# Generated at 2022-06-14 02:45:16.600361
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:45:17.696590
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__doc__



# Generated at 2022-06-14 02:45:28.111816
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import typed_ast.ast3 as ast
    from ..utils.helpers import VariablesGenerator
    from ..utils.snippet import let, extend
    from ..utils.tree import insert_at
    from ..utils.helpers import format_source
    from .base import BaseNodeTransformer

    class YieldFromTransformer(BaseNodeTransformer):
        """Compiles yield from to special while statement."""
        target = (3, 2)


# Generated at 2022-06-14 02:45:30.046944
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from_transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:45:32.878617
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    gft = YieldFromTransformer()
    assert_type(gft, YieldFromTransformer)
    assert_equal(gft.target, (3, 2))



# Generated at 2022-06-14 02:45:41.402018
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse('\n'.join([
        "def func(a):",
        "    b =yield from c",
        "    yield from d",
        "    yield from e",
        "c = 10"
    ]))

    processor = YieldFromTransformer()
    processor.visit(tree)


# Generated at 2022-06-14 02:45:41.975155
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:45:43.336470
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:47:58.556345
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:48:08.858013
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from textwrap import dedent
    from typed_ast.ast3 import parse

    code = dedent('''
    def func():
        a,b = (yield from (1,2))
        c = yield from [3,4]

        yield from [5,6]
        yield from [7,8]
    ''')
    mod = parse(code)
    assert str(mod) == code

    trans = YieldFromTransformer()
    mod = trans.visit(mod)

# Generated at 2022-06-14 02:48:10.053300
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:48:22.850198
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import compile_source
    from ..utils.testing import expect_tree
    from ..utils.tree import tree_string
    from ..tests.examples import try_except, two_yield_froms

    code = """
    yield from func(value)
    
    """
    module = compile_source(code, YieldFromTransformer)
    expected = f"""
    let(iterable)
    iterable = iter(func(value))
    while True:
        try:
            yield next(iterable)
        except StopIteration as $var0:
            if hasattr($var0, 'value'):
                $var0 = $var0.value
            break
    
    """
    print(tree_string(module))
    expect_tree(module, expected)


# Generated at 2022-06-14 02:48:24.350734
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)



# Generated at 2022-06-14 02:48:25.133486
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()

# Generated at 2022-06-14 02:48:26.100012
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:48:33.217330
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:48:43.545626
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse("""
        def test():
            yield from f()
            yield from f()
            a = yield from f()
            b = yield from f()
            yield from f()
    """)

    transformation = YieldFromTransformer()
    transformation.visit(node)
    print(ast.dump(node))
    assert transformation.is_changed

# Generated at 2022-06-14 02:48:45.135369
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """
    @type node: ast.AST
    """
    YieldFromTransformer()
