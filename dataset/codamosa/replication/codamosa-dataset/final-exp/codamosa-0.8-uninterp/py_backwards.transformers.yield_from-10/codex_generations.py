

# Generated at 2022-06-14 02:39:16.816846
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast

    t = YieldFromTransformer()

# Generated at 2022-06-14 02:39:18.663776
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():  # noqa
    assert YieldFromTransformer().__class__ == YieldFromTransformer

# Generated at 2022-06-14 02:39:24.324111
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("yield from x")
    transformer = YieldFromTransformer()
    transformer.visit(tree)
    node = transformer.get_node()
    assert_tree(node,
                tree1=ast.parse("""
                iterable = iter(x)
                while True:
                    try:
                        yield next(iterable)
                    except StopIteration as exc:
                        break
                """))



# Generated at 2022-06-14 02:39:30.810895
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    body = [ast.FunctionDef(name='foo',
                            args=ast.arguments(args=[], vararg=None,
                                               kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[ast.Expr(value=ast.YieldFrom(value=ast.Num(n=3))),
                                  ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                                             value=ast.YieldFrom(value=ast.Num(n=4)))],
                            decorator_list=[],
                            returns=None)]
    mod = ast.Module(body)
    res = YieldFromTransformer().visit(mod)

# Generated at 2022-06-14 02:39:33.077884
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import transformers
    transformer = transformers.YieldFromTransformer()
    assert transformer is not None



# Generated at 2022-06-14 02:39:42.630675
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .codetransformer import CodeTransformer
    from ..parser.parser import Parser
    from ..parser.visitors.visitor import Visitor
    from ..parser import ast_parse
    from ..parser.visitors.liner import Liner
    import sys

    class TestTransformer(CodeTransformer):
        def visit_Module(self, node):
            return self.visit(node.body[0])

        def visit_Try(self, node):
            return ast.Try(body=node.body,
                           handlers=[self.visit(node.handlers[0])],
                           orelse=[],
                           finalbody=[])

        def visit_ExceptHandler(self, node):
            return self.visit(node.body[0])

        def visit_Expr(self, node):
            return ast.Expr

# Generated at 2022-06-14 02:39:43.904360
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Mocks

# Generated at 2022-06-14 02:39:45.874177
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)

# Generated at 2022-06-14 02:39:46.799214
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.ast3 import parse

# Generated at 2022-06-14 02:39:48.110198
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    obj = YieldFromTransformer()
    assert obj.target == (3, 2)

# Generated at 2022-06-14 02:40:00.866805
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .unroll_loops import UnrollLoopsTransformer
    from .remove_assignments import RemoveAssignmentsTransformer
    from ..utils.helpers import transform, run
    source = """
    for x in y:
        yield from x
    """
    tree = ast.parse(source)
    UnrollLoopsTransformer().visit(tree)
    RemoveAssignmentsTransformer().visit(tree)
    YieldFromTransformer().visit(tree)

    run(tree)

# Generated at 2022-06-14 02:40:10.624556
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import textwrap
    from ..utils.helpers import compile_source
    from ..utils.source import Source
    from ..utils.tree import dump_tree
    from .uncurry import UncurryTransformer
    from .helpers import NodeTransformerTestCase

    class TestYieldFromTransformer(NodeTransformerTestCase):
        transformer = YieldFromTransformer
        transformer_class = YieldFromTransformer

        def test_yield_from(self):
            source = Source(textwrap.dedent("""\
                def simple():
                    yield from range(3)

                def assign():
                    x = yield from range(3)
                """), filename='<test>')

# Generated at 2022-06-14 02:40:11.749048
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:13.285602
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer, object)


# Generated at 2022-06-14 02:40:27.225844
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # pylint: disable=missing-docstring
    # pylint: disable=no-value-for-parameter
    from .unused_import import UnusedImportTransformer
    tree = ast.parse('def a():\n    a = yield from b()')
    original_node = tree.body[0]
    node = original_node
    for cls in UnusedImportTransformer, YieldFromTransformer:
        node = cls(debug=True).visit(node) # type: ignore
    assert node != original_node

# Generated at 2022-06-14 02:40:35.198247
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = ast.YieldFrom()
    x.value = ast.Name()
    x.value.id = 'a'
    x.value.ctx = ast.Load()
    x.lineno = 1
    x.col_offset = 1
    x.ctx = ast.Load()

    test = ast.Expr()
    test.value = x

    test1 = ast.YieldFrom()
    x.value = ast.Name()
    test1.value.id = 'b'
    test1.value.ctx = ast.Load()
    test1.lineno = 1
    test1.col_offset = 1
    test1.ctx = ast.Store()

    test2 = ast.Assign()
    test2.targets = [ast.Name()]

# Generated at 2022-06-14 02:40:37.398125
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer

# Unit tests for methods of class YieldFromTransformer

# Generated at 2022-06-14 02:40:46.589271
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import textwrap
    code = textwrap.dedent("""
        def func():
            yield from [1, 2, 3]
        """)
    tree = ast.parse(code)
    func = tree.body[0]
    assert isinstance(func, ast.FunctionDef)
    assert isinstance(func.body[0].value, ast.YieldFrom)

    YieldFromTransformer().visit(tree)
    func = tree.body[0]
    assert isinstance(func, ast.FunctionDef)
    assert not isinstance(func.body[0].value, ast.YieldFrom)

# Generated at 2022-06-14 02:40:48.407864
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None
    

# Generated at 2022-06-14 02:40:49.422683
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    g = YieldFromTransformer([])

# Generated at 2022-06-14 02:41:02.316808
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from_transformer=YieldFromTransformer()
    assert(len(yield_from_transformer.__annotations__)>0)

# Generated at 2022-06-14 02:41:17.708520
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.testing import get_tree
    from ..utils.testing import assert_equal_ast

    tf = YieldFromTransformer()

    tree = get_tree('''
        def fn(iterable):
            a = 0
            b = yield from iterable
            c = yield from range(1)
            d = a + b
            return d + c
        fn(range(10))
    ''')
    tf(tree)

# Generated at 2022-06-14 02:41:21.211135
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Unit-test for constructor"""
    import astor, inspect
    from ..utils.helpers import get_random_name

# Generated at 2022-06-14 02:41:22.960041
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:41:32.980796
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse('''
        def foo(x):
            l = yield from x
            yield from x
            z = print(yield from x)
            yield from print(x)
            print(yield from x)
    ''')
    obj = YieldFromTransformer()
    new_tree = obj.visit(tree)
    print(new_tree)
    print(obj._tree_changed)
# test_YieldFromTransformer()

# Generated at 2022-06-14 02:41:34.113203
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:41:35.758105
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:41:38.018541
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer(None)
    assert isinstance(t, BaseNodeTransformer)

# Generated at 2022-06-14 02:41:47.464713
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import assert_equal
    from .imports import ImportsCollector

    source = """
        a = yield from b(1)
    """

    correct = """
        let(exc)
        let(iterable)
        iterable = iter(b(1))
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    a = exc.value
                break
    """

    def check(before_source):
        tree = ast.parse(before_source)
        transform = YieldFromTransformer()
        transform.visit(tree)
        imports = ImportsCollector().visit(tree)
        return imports.get_code() + ast.unparse(tree)


# Generated at 2022-06-14 02:41:48.578259
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None


# Generated at 2022-06-14 02:42:11.221989
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:42:20.078558
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node_transformer = YieldFromTransformer()
    # Unit test for method: _get_yield_from_index
    assert node_transformer._get_yield_from_index(node=None,
                                                  type_=None) is None
    # Unit test for method: _emulate_yield_from
    assert node_transformer._emulate_yield_from(target=None,
                                                node=None) is not None
    # Unit test for method: _handle_assignments
    assert node_transformer._handle_assignments(node=None) is None
    # Unit test for method: _handle_expressions
    assert node_transformer._handle_expressions(node=None) is None
    # Unit test for method: visit

# Generated at 2022-06-14 02:42:29.079107
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .translator import Translator
    import astor

    tree = ast.parse("yield from some_iterable")
    YieldFromTransformer().visit(tree)
    assert "yield from some_iterable" not in astor.to_source(tree)
    tree = ast.parse("yield from some_iterable")
    Translator("", [YieldFromTransformer()]).visit(tree)
    assert "yield from some_iterable" not in astor.to_source(tree)

    tree = ast.parse("foo = yield from some_iterable")
    YieldFromTransformer().visit(tree)
    assert "yield from some_iterable" not in astor.to_source(tree)
    tree = ast.parse("foo = yield from some_iterable")

# Generated at 2022-06-14 02:42:30.549759
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:33.021572
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(print).__class__.__name__ == 'YieldFromTransformer'


# Generated at 2022-06-14 02:42:34.733439
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()
    assert t is not None

# Generated at 2022-06-14 02:42:36.948049
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert str(YieldFromTransformer(3, 2)) == "<YieldFromTransformer(3, 2)>"

# Generated at 2022-06-14 02:42:40.810930
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yieldfromtransformer = YieldFromTransformer()
    assert yieldfromtransformer.target == (3, 2)


# Generated at 2022-06-14 02:42:42.220960
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:43.822430
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:43:30.280825
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_constructor import test_constructor
    test_constructor(YieldFromTransformer)

# Unit tests for method _get_yield_from_index of class YieldFromTransformer

# Generated at 2022-06-14 02:43:31.314003
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
	assert YieldFromTransformer()


# Generated at 2022-06-14 02:43:43.370656
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    #def transform(self, tree: ast.Module) -> ast.Module:
    def transform(tree: ast.Module) -> ast.Module:
        tree = YieldFromTransformer().visit(tree)
        return tree

    # test 1
    from ast_toolbox import ast_to_str, compile_and_run, compile_and_run_ast
    # print("ast_to_str(tree):", ast_to_str(tree))
    tree = ast.parse("yield from gen")
    test_result = transform(tree)
    # print("ast_to_str(test_result):", ast_to_str(test_result))
    # print("compile_and_run(test_result):", compile_and_run(test_result))

# Generated at 2022-06-14 02:43:52.756418
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer.visit(None) is None

# Generated at 2022-06-14 02:43:55.514879
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert repr(YieldFromTransformer) == '<YieldFromTransformer(target=(3, 2))>'

# Generated at 2022-06-14 02:43:59.686001
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer.target == (3, 2)
    assert transformer.module is None
    assert transformer._tree_changed == False

# test for _get_yield_from_index

# Generated at 2022-06-14 02:44:01.059010
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None


# Generated at 2022-06-14 02:44:05.739881
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """
    Tests that the 'YieldFromTransformer' class works as intended
    """
    # Init objects
    node = ast.Yield()
    remap = [("bast.visitors.YieldFromTransformer.YieldFromTransformer", "YieldFromTransformer")]
    # Test constructor
    instance = YieldFromTransformer(node, remap)
    assert isinstance(instance, YieldFromTransformer)


# Generated at 2022-06-14 02:44:11.574976
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.source import source_to_unicode as u
    try:
        import typed_ast.ast3 as typed_ast
    except ImportError:
        import typed_ast as typed_ast
    try:
        import astor
    except ImportError:
        import astor.codegen as astor

# Generated at 2022-06-14 02:44:21.957619
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    def test_snippets(source: str, expected: str):
        trans = YieldFromTransformer()
        module = ast.parse(source)
        module = trans.visit(module)
        assert ast.dump(ast.fix_missing_locations(module)) == expected

    test_snippets('yield from iterable',
                  'Module(body=[Expr(value=Yield(value=Name(id=\'iterable\', ctx=Load())))])')

    test_snippets('a = yield from iterable',
                  'Module(body=[Assign(targets=[Name(id=\'a\', ctx=Store())], value=Yield(value=Name(id=\'iterable\', ctx=Load())))])')


# Generated at 2022-06-14 02:47:53.848213
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import Visitor
    from ..compiler import compile
    from ..utils.source import source
    from ..utils.helpers import dump_ast
    
    @source
    def test(gen):
        yield 1
        yield from gen
        yield 2
        
    @source
    def expected():
        let(iterable)
        iterable = iter(gen)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    yield exc.value
                break
        yield 2

    tree = compile(test, YieldFromTransformer, Visitor)
    assert expected.get_source() == dump_ast(tree)

# Generated at 2022-06-14 02:47:59.889781
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    test_node = ast.parse("a = yield from b")
    assert isinstance(test_node, ast.Module)
    result_node = YieldFromTransformer().visit(test_node)
    print('test_YieldFromTransformer output:')
    print(ast.dump(result_node))
    assert isinstance(result_node, ast.Module)
    assert isinstance(result_node.body[0], ast.Assign)
    assert isinstance(result_node.body[1], ast.While)
    assert len(result_node.body[1].body) == 2


# Generated at 2022-06-14 02:48:03.209135
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer(): 
    x = YieldFromTransformer()
    assert x
    assert x.target == (3, 2)


# Generated at 2022-06-14 02:48:07.872257
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    #
    # Tests that the default args of the constructor are correct
    #
    x = YieldFromTransformer()
    assert x.target == '3.2'
    assert x.future_import == False
    assert x.coerce_objects == False
    #
    # Tests the access to the arg through the property mechanism
    #
    x.future_import = True
    assert x.future_import == True

# Generated at 2022-06-14 02:48:20.426544
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ... import from_source
    from .base import BaseNodeTransformer

    # Unit test for method _get_yield_from_index
    def test_get_yield_from_index():
        t = YieldFromTransformer()
        tree = from_source('def foo():\n    yield from [1, 2, 3]')[0]
        assert t._get_yield_from_index(tree.body[0], ast.Expr) == 0
        tree = from_source('def foo():\n    yield from [1, 2, 3]')[0]
        assert t._get_yield_from_index(tree.body[0], ast.Assign) is None
        tree = from_source('def foo():\n    x = yield from [1, 2, 3]')[0]
        assert t._

# Generated at 2022-06-14 02:48:29.566230
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.test_utils import transform
    from .fixtures.test_yieldfrom import c
    from ..utils.helpers import get_ast
    from ..utils.errors import (
        YieldFromError,
    )
    from astunparse import dump

    # test_yieldfrom case 1
    def test_case_1():
        node = get_ast(c, 1)
        assert isinstance(node, ast.Node)
        ast_origin = dump(node)
        # use YieldFromTransformer
        node = YieldFromTransformer().visit(node)
        ast_target = dump(node)
        # check the result
        ast_expected = transform(get_ast(c, 2))
        assert ast_expected == ast_target
        assert ast_origin != ast_target

    # test_yield

# Generated at 2022-06-14 02:48:31.411854
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()
    

# Generated at 2022-06-14 02:48:41.911197
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # constructor
    t = YieldFromTransformer()

    # method _emulate_yield_from

# Generated at 2022-06-14 02:48:43.479094
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    instance = YieldFromTransformer(None)
    assert isinstance(instance, YieldFromTransformer)

# Generated at 2022-06-14 02:48:46.389029
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Test 1
    x = YieldFromTransformer()
    assert x._get_yield_from_index is not None

    # Test 2
    x = YieldFromTransformer()
    assert x._emulate_yield_from is not None