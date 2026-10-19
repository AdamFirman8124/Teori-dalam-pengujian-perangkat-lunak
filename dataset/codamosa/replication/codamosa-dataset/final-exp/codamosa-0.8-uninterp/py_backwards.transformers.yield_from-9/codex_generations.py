

# Generated at 2022-06-14 02:39:03.875067
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:06.033430
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    c = YieldFromTransformer()
    assert c


# Generated at 2022-06-14 02:39:10.775403
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..unparse import Unparser
    from ..parser import parse
    import re
    from .try_except_transformer import TryExceptTransformer
    from .if_transformer import IfTransformer
    from .while_transformer import WhileTransformer
    from .function_def_transformer import FunctionDefTransformer
    from .module_transformer import ModuleTransformer

    class TestTransformer(TryExceptTransformer, IfTransformer, WhileTransformer, FunctionDefTransformer, ModuleTransformer, YieldFromTransformer):
        pass


# Generated at 2022-06-14 02:39:20.984737
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    from ..utils.tree import tree_to_str


# Generated at 2022-06-14 02:39:25.389095
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    exc = VariablesGenerator.generate('exc')
    # print(result_assignment.get_body(exc=exc, target=target))
    print(yield_from.get_body(generator=node.value, assignment=assignment, exc=exc))

# Generated at 2022-06-14 02:39:28.008091
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    o = YieldFromTransformer()
    assert isinstance(o, BaseNodeTransformer)
    assert isinstance(o, YieldFromTransformer)


# Generated at 2022-06-14 02:39:28.962242
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:38.899095
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import Compiler
    from ..target.python32.transformers_python32 import YieldFromTransformer
    from typed_ast import ast3 as ast
    from ..utils.snippet import generate_code

    class TestCompiler(Compiler):
        @property
        def transformers(self) -> List[BaseNodeTransformer]:
            return [YieldFromTransformer(self)]

    ast_tree = ast.parse(generate_code(
        """
        def f(n):
            if n:
                yield from g(n)
            return yield from g(n)

        def g(n):
            i = 0
            while i < n:
                yield i
                i += 1
        """))
    bytecode = TestCompiler().to_source(ast_tree)

# Generated at 2022-06-14 02:39:40.467151
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass
# vim: set tabstop=8 softtabstop=4 shiftwidth=4 expandtab:

# Generated at 2022-06-14 02:39:41.341458
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:39:55.680357
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astunparse
    target = (3, 2)
    tree = ast.parse(r'''def foo():
    yield from bar
    yield from baz
    ''')
    transformer = YieldFromTransformer(target)
    new_tree = transformer.visit(tree)

    printed = astunparse.unparse(new_tree)

# Generated at 2022-06-14 02:39:59.100201
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import parse_ast
    from astpretty import pprint
    node = parse_ast(YieldFromTransformer.__name__)
    pprint(node)

# Generated at 2022-06-14 02:40:00.354558
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass



# Generated at 2022-06-14 02:40:01.379420
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    y = YieldFromTransformer()
    assert y

# Generated at 2022-06-14 02:40:02.136805
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None, None)

# Generated at 2022-06-14 02:40:12.213171
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import print_ast
    from ..utils.mock import MockNode

    parent = ast.Module(body=[
        ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                   value=MockNode()),
        ast.Expr(value=MockNode()),
        ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                   value=MockNode()),
        ast.Expr(value=MockNode())
    ])
    print_ast(parent)

    YieldFromTransformer().visit(parent)
    print_ast(parent)


# Generated at 2022-06-14 02:40:14.690992
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.parsing import parse
    from ..utils.testing import dump, load


# Generated at 2022-06-14 02:40:15.639818
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:25.371503
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from dumbc.compiler.ast.nodes import UnaryOp, BinOp, YieldFrom, Module, Assign, Expr
    from dumbc.compiler.ast.types import Str, node_to_str
    from dumbc.utils.helpers import VariablesGenerator

    var_gen = VariablesGenerator()

    code = 'yield from val'
    node = Module(body=[
        Assign(targets=[var_gen.create()], value=YieldFrom(value=Str('test')))
    ])

    transformer = YieldFromTransformer()
    node = transformer.visit(node)

# Generated at 2022-06-14 02:40:34.717892
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import ast as ast_module
    class_def = ast_module.ClassDef
    as_type = ast_module.expr
    functions = ast_module.FunctionDef
    args = ast_module.arguments
    arg = ast_module.arg
    load = ast_module.Load
    as_node = ast_module.Name
    module = ast_module.Module
    assign = ast_module.Assign
    try_ = ast_module.Try
    body = ast_module.Body
    expr = ast_module.Expr
    value = ast_module.value
    yield_from = ast_module.YieldFrom
    from_module = ast_module.From
    import_ = ast_module.ImportFrom
    alias = ast_module.alias


# Generated at 2022-06-14 02:40:43.666032
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    globals()['result_assignment'] = lambda exc, target: None
    globals()['yield_from'] = lambda generator, exc, assignment: None
    globals()['VariablesGenerator'] = lambda: None
    setattr(VariablesGenerator, 'generate', lambda self, s: s)
    setattr(VariablesGenerator, 'generate', lambda self, s: s)

# Generated at 2022-06-14 02:40:46.228423
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = ast.YieldFrom()
    b = YieldFromTransformer()
    assert b._emulate_yield_from() == []

# Generated at 2022-06-14 02:40:54.087770
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.unparser import Unparser
    from .utils import parse_to_ast

    tree = parse_to_ast("""
    def foo(x):
        y = yield from x
        z = yield from x
        yield from x
    """)

    YieldFromTransformer().visit(tree.body[0])
    res = Unparser(tree)

# Generated at 2022-06-14 02:40:56.124988
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert not hasattr(YieldFromTransformer, 'func')

# Generated at 2022-06-14 02:41:00.915860
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import dump
    obj = YieldFromTransformer()
    assert (
        dump(obj) ==
        'YieldFromTransformer()'
    ), f'Expected:\nYieldFromTransformer(), but got:\n{dump(obj)}'


# Generated at 2022-06-14 02:41:05.457443
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().target == (3, 2)
    try:
        YieldFromTransformer()._emulate_yield_from
        YieldFromTransformer()._handle_expressions
        YieldFromTransformer()._handle_assignments
        YieldFromTransformer().visit
    except:
        assert False
    assert True

# Generated at 2022-06-14 02:41:14.930717
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    trans = YieldFromTransformer()
    tree = ast.parse('def x():\n    yield from func()')
    tree = ast.fix_missing_locations(tree)
    tree = trans.visit(tree)
    res = ast.dump(tree)

# Generated at 2022-06-14 02:41:23.226090
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:25.318310
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:41:26.784430
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer

# Generated at 2022-06-14 02:41:32.944685
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:41:34.524452
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transpiler = YieldFromTransformer(3)



# Generated at 2022-06-14 02:41:44.898808
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import roundtrip

    source = """
    def f():
        yield from g(a)
        if b:
            yield from h()
    def g():
        yield
        return 1
    """


# Generated at 2022-06-14 02:41:49.075689
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..tests.testing_utils import assert_equal_with_printing
    from ..utils.snippet import get_node

    node = get_node(open('../tests/samples/yield_from.py').read())
    modified = YieldFromTransformer().visit(node)
    assert_equal_with_printing(modified, node, context_size=100)

# Generated at 2022-06-14 02:41:50.868842
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # unit test for constructor of class YieldFromTransformer
    YieldFromTransformer()

test_YieldFromTransformer()

# Generated at 2022-06-14 02:41:53.312286
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Just for type check
    YieldFromTransformer()



# Generated at 2022-06-14 02:41:55.046311
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from pyt.transforms.yield_from import YieldFromTransformer
    assert YieldFromTransformer('3.2')

# Generated at 2022-06-14 02:41:55.778665
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    return YieldFromTransformer()


# Generated at 2022-06-14 02:41:57.479103
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import compile
    from ..utils.helpers import as_tuple


# Generated at 2022-06-14 02:42:08.543005
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # noinspection PyUnusedLocal
    def x():
        yield from (1, 2, 3)
        return
    
    # noinspection PyPep8Naming
    class YieldFromTransformer_test10(BaseNodeTransformer):
        """Compiles yield from to special while statement."""
        target = (3, 2)

        def _get_yield_from_index(self, node: ast.AST,
                                  type_: Type[Holder]) -> Optional[int]:
            if hasattr(node, 'body') and isinstance(node.body, list):  # type: ignore
                for n, child in enumerate(node.body):  # type: ignore
                    if isinstance(child, type_) and isinstance(child.value, ast.YieldFrom):
                        return n

            return None


# Generated at 2022-06-14 02:42:21.037663
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:42:24.951876
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .collector import Collector
    from .context_visitor import ContextVisitor
    from .loop_breaker import LoopBreaker
    from .loop_collector import LoopCollector
    from ..utils.helpers import print_ast


# Generated at 2022-06-14 02:42:37.072206
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  from .. import transform
  from ..utils import dump_ast
  # Code snippet to test
  code = """
  def f():
      yield from A()
  """
  # Expected AST snippet

# Generated at 2022-06-14 02:42:40.810084
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Unit tests for method _get_yield_from_index of class YieldFromTransformer

# Generated at 2022-06-14 02:42:45.915255
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert hasattr(YieldFromTransformer, 'target')
    assert isinstance(YieldFromTransformer.target, tuple)
    yft = YieldFromTransformer()
    assert hasattr(yft, 'visit')
    assert hasattr(yft, 'generic_visit')
    assert hasattr(yft, 'target')
    assert YieldFromTransformer.target == (3, 2)
    assert YieldFromTransformer.target == yft.target

# Generated at 2022-06-14 02:42:47.994933
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yft = YieldFromTransformer()
    pass

################################################################################
# Tests for method YieldFromTransformer._get_yield_from_index


# Generated at 2022-06-14 02:42:52.832023
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.fake_context import FakeContext
    from ..utils.source import source_code_lines
    from ..utils.typing import ASTLike
    from ..utils.helpers import parse
    from ..utils.source import function_to_test

    context = FakeContext()
    node = ast.parse(source_code_lines(function_to_test)[0])
    YieldFromTransformer.run_on_node(node, context)

    assert parse(context.get_transformed_code()) == parse('''
    def f():
        c = 0
        yield from range(100)
        print(c)
        if c != 100:
            raise ValueError(c)
    ''')

# Generated at 2022-06-14 02:43:02.413121
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .imports import Imports
    from .types import Types
    from .builtins import Builtins
    from ..compiler import Compiler
    from ..utils.source import Source

    source = Source("""
    def f():
        a = 1
        yield from g()
    
    def g():
        yield 1
    """)
    assert ('class_name', 'YieldFromTransformer') in str(YieldFromTransformer)
    module, handler = YieldFromTransformer.run(source)

# Generated at 2022-06-14 02:43:13.438906
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Assigment
    code = ast.parse('a = yield from b')
    node = YieldFromTransformer().visit(code)
    expected = ast.parse("""
    exc_0 = None
    iterable_0 = None
    iterable_0 = iter(b)
    while True:
        try:
            yield next(iterable_0)
        except StopIteration as exc_0:
            a = exc_0.value
            break
    """)
    assert ast.dump(node) == ast.dump(expected)

    # Expression
    code = ast.parse('yield from b')
    node = YieldFromTransformer().visit(code)

# Generated at 2022-06-14 02:43:14.891318
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:38.873285
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse('a = yield from b')
    x = YieldFromTransformer()
    x.visit(node)



# Generated at 2022-06-14 02:43:40.636086
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None


# Generated at 2022-06-14 02:43:42.115239
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == "YieldFromTransformer"

# Generated at 2022-06-14 02:43:49.287709
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse("""
    a = yield from(1)
    """).body[0]
    assert isinstance(node, ast.Assign)

    yield_from_transformer = YieldFromTransformer()
    yield_from_transformer.visit(node)

    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)
    assert node.value.func.id == 'yield_from'

# Generated at 2022-06-14 02:43:50.144188
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:43:51.222037
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:43:53.342899
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    from ..utils.test import check_in, check_out


# Generated at 2022-06-14 02:43:57.750060
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from = ast.YieldFrom()
    yield_from.value = ast.Name(id='a')
    expr = ast.Expr(value=yield_from)
    YieldFromTransformer.visit(expr)


# Generated at 2022-06-14 02:44:03.552515
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try_ = ast.Try([], [], [], [])
    try_.body.append(ast.Expr(value=ast.YieldFrom(None)))
    module = ast.Module([], [try_])
    t = YieldFromTransformer()
    assert t.apply(module)
    module = ast.Module([], [try_])
    t.apply(module)
    assert True

# Generated at 2022-06-14 02:44:06.715278
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    def __init__(self):
        self.target = (3, 2)
    YieldFromTransformer.__init__ = __init__

    assert type(YieldFromTransformer().target) == tuple



# Generated at 2022-06-14 02:45:27.982117
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Unit tests for methods that are inherited from class YieldFromTransformer."""
    # pylint: disable=unused-argument
    def visit(self, node):
        """Visit a single node."""
        pass
    YieldFromTransformer.visit = visit
    # pylint: enable=unused-argument


# Generated at 2022-06-14 02:45:30.397747
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None


# Generated at 2022-06-14 02:45:31.533267
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import ast

# Generated at 2022-06-14 02:45:32.991482
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_helpers import transform


# Generated at 2022-06-14 02:45:41.443114
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..transformers.base import BaseTransformer
    from ..utils import Source
    from ..utils.helpers import VariablesGenerator

    source = Source("""
    def a(x):
        y = yield from b(x)
    """)
    tree = source.parse()
    transformer = BaseTransformer(tree)
    assert transformer.tree == tree
    assert not transformer.tree_changed
    transformer = YieldFromTransformer(tree)
    assert transformer.tree == tree
    assert transformer.tree_changed

    #print(ast.dump(transformer.tree))
    #print("\n")
    
    exc = VariablesGenerator.generate('exc')
    assignment = result_assignment.get_body(exc=exc, target='y')
    assert(len(assignment) == 1)

    iterable = Vari

# Generated at 2022-06-14 02:45:48.084438
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    with open('tests/fixtures/yield_from.py') as f:
        tree = ast.parse(f.read())
    node = YieldFromTransformer().visit(tree)
    result = ast.dump(node, annotate_fields=False)
    with open('tests/fixtures/yield_from_expected.py') as f:
        expected = f.read()
    assert result == expected

# Generated at 2022-06-14 02:45:49.579770
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    ok = not YieldFromTransformer()

# Generated at 2022-06-14 02:45:51.103368
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()



# Generated at 2022-06-14 02:45:53.335167
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)


# Generated at 2022-06-14 02:45:54.225264
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:47:51.919628
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import ast as old_ast
    import typed_ast.ast3 as ast
    from ..visitors.ast_compiler_visitor import ASTCompilerVisitor
    from ..compiler import TypedPythonCompiler
    from ..utils.snippet import snippet
    from .. import preprocessors as pp


# Generated at 2022-06-14 02:47:54.446709
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yft = YieldFromTransformer()
    assert yft is not None

# Generated at 2022-06-14 02:47:56.889982
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print('For test constructor, please input a line with unit test')
    line = input()
    class_ = YieldFromTransformer()
    print(class_)


# Generated at 2022-06-14 02:47:58.732200
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert parse_types(YieldFromTransformer)

# Generated at 2022-06-14 02:48:08.966412
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    "test YieldFromTransformer by creating snippet for testing"
    # Test for YieldFromTransformer constructor
    yield_ = YieldFromTransformer()
    # test for snippet
    result = yield_._emulate_yield_from(None, ast.YieldFrom(value=None, lineno=None, col_offset=None))
    print(result)
    # test for snippet
    result = yield_._emulate_yield_from(None, ast.YieldFrom(value=None, lineno=None, col_offset=None))
    print(result)
    # test for snippet
    result = YieldFromTransformer._get_yield_from_index(yield_, ast.Module(body=result, lineno=None, col_offset=None), ast.Expr)
    print(result)
    # test

# Generated at 2022-06-14 02:48:17.290832
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    test_code_str = """
        def yield_from_test(number):
            for i in range(number):
                yield from [1]
    """

    assert_source(YieldFromTransformer, test_code_str,
                  '''
                  def yield_from_test(number):
                      let(iterable)
                      iterable = iter([1])
                      for i in range(number):
                          try:
                              yield next(iterable)
                          except StopIteration as exc:
                              break
                  ''')

# Generated at 2022-06-14 02:48:19.096822
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    trans = YieldFromTransformer()
    assert trans is not None


# Generated at 2022-06-14 02:48:28.937555
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    source = """
    def f():
        a = yield from g()
        yield from g()
        yield from g()
        b = c = yield from g()
        
    def g():
        pass
    """


# Generated at 2022-06-14 02:48:32.292817
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    new = YieldFromTransformer()
    print(new)


# Unit test
if __name__ == "__main__":
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:48:33.576468
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    to_test = YieldFromTransformer()
    assert to_test