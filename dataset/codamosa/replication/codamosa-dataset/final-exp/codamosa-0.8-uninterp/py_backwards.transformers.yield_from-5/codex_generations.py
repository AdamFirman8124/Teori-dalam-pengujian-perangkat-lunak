

# Generated at 2022-06-14 02:39:08.045082
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.visitor import to_source
    from ..utils.yield_from import transform
    from ..utils.helpers import show_all_trees

    tree = """
    def foo():
        a = yield from bar()
    """
    print(to_source(transform(tree)))
    show_all_trees(transform(tree))


# Generated at 2022-06-14 02:39:11.545439
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print("Testing constructor of class YieldFromTransformer")
    try:
        YieldFromTransformer()
        print("Passed Test: constructor of class YieldFromTransformer")
    except Exception as err:
        print("Failed Test: constructor of class YieldFromTransformer")
        print(err)


# Generated at 2022-06-14 02:39:13.076260
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    constructor_test_helper(YieldFromTransformer, 'target', (3, 2))


# Generated at 2022-06-14 02:39:14.098297
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass #TODO

# Generated at 2022-06-14 02:39:15.225427
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer(None)

# Generated at 2022-06-14 02:39:24.574296
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    gen = ast.parse('def test():\n    x = yield from func()')
    YieldFromTransformer().visit(gen)
    assert ast.dump(gen) == 'Module(body=[FunctionDef(name=\'test\', args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Name(id=\'x\', ctx=Store())], value=Call(func=Attribute(value=Name(id=\'func\', ctx=Load()), attr=\'__next__\', ctx=Load()), args=[], keywords=[]))], decorator_list=[], returns=None)])'

# Generated at 2022-06-14 02:39:29.054417
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.ast3 import parse, dump
    from ..converter import TypedPythonConversionVisitor

    node = parse("""
    def test():
        a = yield from generator()
        yield from generator()
    """)
    res = TypedPythonConversionVisitor.visit(node)
    assert dump(node) == dump(res)

# Generated at 2022-06-14 02:39:29.961762
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None

# Generated at 2022-06-14 02:39:38.589827
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    yft = YieldFromTransformer()
    assert isinstance(yft, BaseNodeTransformer)
    assert isinstance(yft, ast.NodeTransformer)
    assert yft._tree_changed == False
    assert yft._current_class == None
    assert yft._current_function == None
    assert yft._in_async_function == False
    assert yft._in_async_with == False
    assert yft._in_async_for == False
    assert yft._in_async_iter == False
    assert yft._current_finally_suite == False


# Generated at 2022-06-14 02:39:41.832600
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("""
    def foo(foo):
        yield from foo
        yield
    """)
    trans = YieldFromTransformer()
    tree = trans.visit(tree)

if __name__ == "__main__":
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:39:48.570274
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:49.468669
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()


# Generated at 2022-06-14 02:39:50.716496
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    assert repr(a) == '<YieldFromTransformer(target=(3, 2))>'

# Generated at 2022-06-14 02:39:54.871944
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert hasattr(x, 'target')
    assert hasattr(x, '_get_yield_from_index')
    assert hasattr(x, '_emulate_yield_from')
    assert hasattr(x, '_handle_assignments')
    assert hasattr(x, '_handle_expressions')
    assert hasattr(x, 'visit')

# Generated at 2022-06-14 02:39:56.713608
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert isinstance(transformer, BaseNodeTransformer)


# Generated at 2022-06-14 02:39:58.838301
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    assert isinstance(a, YieldFromTransformer)

# Generated at 2022-06-14 02:40:06.948217
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..tests.utils import NodeTransformerTestCase
    from ..parser import Parser

    class Test(NodeTransformerTestCase):
        TRANSFORMER = YieldFromTransformer
        PARSER = staticmethod(Parser.parse_expr)

        @staticmethod
        def transform(node, *args, **kwargs):
            return YieldFromTransformer(*args, **kwargs).visit(node)

        def test_nested(self):
            expr = self.transform('a = yield from (yield from b)')
            self.assertEqual(expr, 'a = (iter(b)).__next__()')

# Generated at 2022-06-14 02:40:10.104651
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        YieldFromTransformer()
    except Exception as exc:
        raise AssertionError("Can't instantiate an class") from exc



# Generated at 2022-06-14 02:40:11.199810
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print(YieldFromTransformer())


# Generated at 2022-06-14 02:40:13.967261
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        _ = YieldFromTransformer()
    except AssertionError as e:
        assert False, e

# Generated at 2022-06-14 02:40:32.960796
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typing import List, Optional
    from .base import NodeTransformer
    from ..utils.tree import get_node_code, get_node_lineage
    import astor

    class TestTransformer(NodeTransformer):
        def visit_YieldFrom(self, node: ast.YieldFrom) -> Optional[ast.AST]:
            return node

    tree = ast.parse('''
    def func():
        yield from some_generator()

    def func2():
        yield from other_generator()
        yield from another_generator()
    ''')

    tree = TestTransformer().visit(tree)
    print(astor.to_source(tree))



# Generated at 2022-06-14 02:40:35.029195
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    return a

# Generated at 2022-06-14 02:40:36.297904
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)

# Generated at 2022-06-14 02:40:37.037967
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:40:39.116086
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert 1

if __name__ == '__main__':
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:40:40.512208
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().target is (3, 2)


# Generated at 2022-06-14 02:40:51.679824
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = """
    def foo():
        y = yield from [1, 2, 3]
        z = yield from (y for y in range(3))
    """
    assert YieldFromTransformer().transform(code) == """\
    def foo():
        iterable = iter([1, 2, 3])
        while True:
            try:
                y = next(iterable)
                yield y
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    y = exc.value
                break
        iterable = iter(y for y in range(3))
        while True:
            try:
                z = next(iterable)
                yield z
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    z = exc.value
                break"""

# Generated at 2022-06-14 02:40:52.744515
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:41:04.226652
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    try:
        from typed_ast import ast3
    except ImportError:
        return
    from typed_ast.transforms.optimize import YieldFromTransformer
    from . import helper
    import os
    print("Running unit test for %s" % __file__)

    # Test YieldFromTransformer
    nodes = helper.load_test_files(os.path.dirname(__file__), 'test*.py')
    print("Run YieldFromTransformer test on files:")
    print([n[0] for n in nodes])
    result = helper.run_on_files(nodes,
                                 ast3.parse,
                                 YieldFromTransformer(ast3).visit)
    print("Run YieldFromTransformer test on files:")
    print([n[0] for n in result])
    helper

# Generated at 2022-06-14 02:41:05.590364
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:29.348257
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None


# Generated at 2022-06-14 02:41:38.900623
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.ast3 import Module
    from ..utils.helpers import Tree
    from ..utils.source import get_source

    m = Module([])

    tree = Tree(m)
    tree.create_node(m, None)
    root_node_id = tree.get_node(m)

    assert root_node_id.tag == m
    assert root_node_id.identifier == 0
    assert root_node_id.tag is not None
    assert root_node_id.parent == None

    assert len(tree.expand_tree(mode=Tree.WIDTH)) == 1
    YieldFromTransformer(tree)

# Generated at 2022-06-14 02:41:39.898765
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    return YieldFromTransformer()

# Generated at 2022-06-14 02:41:46.425350
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert x._tree_changed is False  # noqa: WPS421
    assert x._get_yield_from_index is None  # noqa: WPS421
    assert x._emulate_yield_from is None  # noqa: WPS421
    assert x._handle_assignments is None  # noqa: WPS421
    assert x._handle_expressions is None  # noqa: WPS421
    assert x.visit is None  # noqa: WPS421


# Generated at 2022-06-14 02:41:47.315155
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = YieldFromTransformer()
    return node

# Generated at 2022-06-14 02:41:47.832028
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:41:49.214031
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

if __name__ == '__main__':
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:41:51.902142
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()
    assert isinstance(x, BaseNodeTransformer)


# Generated at 2022-06-14 02:41:53.924305
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


# Generated at 2022-06-14 02:41:56.836360
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.ast3 import Try
    from typed_ast import ast3 as ast
    try_: Try = ast.Try()
    yield_fromtransformer = YieldFromTransformer()
    assert yield_fromtransformer

# Generated at 2022-06-14 02:42:41.039762
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:42:43.103633
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer(): YieldFromTransformer(ast.parse("""if True:
    a = yield from b"""), {})

# Generated at 2022-06-14 02:42:43.992745
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:42:51.598468
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Arrange
    test_tree = ast.Module(
        body=[ast.Expr(
            value=ast.YieldFrom(
                value=ast.Name(id='gen', ctx=ast.Load())
            ))]
    )

# Generated at 2022-06-14 02:43:01.736756
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Unit test for method _emulate_yield_from of class YieldFromTransformer
    def test_emulate_yield_from():
        x = YieldFromTransformer()
        y = YieldFromTransformer()

        assert x._emulate_yield_from(None, ast.YieldFrom(value='generator')) == y._emulate_yield_from(None, ast.YieldFrom(value='generator'))

    test_emulate_yield_from()

    # Unit test for method _get_yield_from_index of class YieldFromTransformer
    def test_get_yield_from_index():
        def body_node():
            return ast.Expr(value=ast.YieldFrom(value='iterator'))
        body = [body_node()]

        yield_from_

# Generated at 2022-06-14 02:43:12.993236
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..compiler import get_compiler
    # compile using this compiler
    compiler = get_compiler(versions=[(3, 2)])

    code = """
    class A:
        def __init__(self):
            self.x = 1


    class B:
        def __init__(self):
            self.a = A()
            self.a1 = self.a


    class C:
        def __init__(self):
            self.b = self.b1 = B()


    A()
    B()
    C()
    """


# Generated at 2022-06-14 02:43:15.812187
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()
    assert True

# Unit tests for _get_yield_from_index of class YieldFromTransformer

# Generated at 2022-06-14 02:43:16.506105
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert True

# Generated at 2022-06-14 02:43:29.818511
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    m = ast.parse("""
    def foo(a):
        x = yield from bar()
        yield from bar()
    """)
    m = YieldFromTransformer().visit(m)

    expected = """
    def foo(a):
        let(iterable)
        iterable = iter(bar())
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    x = exc.value
                break
        let(iterable)
        iterable = iter(bar())
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    exc.value
                break
    """
    expected = ast.parse(expected)

# Generated at 2022-06-14 02:43:31.125741
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None


# Generated at 2022-06-14 02:45:37.794921
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import check_transformation

    source = """
    def test():
        a = yield from b
        yield from c
        d = yield from e
    """

# Generated at 2022-06-14 02:45:46.173495
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from . import Python3SemanticAnalyzer
    from ..utils.helpers import from_source
    from ..utils.tree_compare import tree_compare

    source = '''
        def foo():
            yield from bar()

        def baz():
            yield from bar()

        def qux():
            yield from bar().baz()

        def goh():
            yield from bar() + 1

        def sum():
            yield from [foo, goh]
    '''

# Generated at 2022-06-14 02:45:47.647212
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:45:54.290544
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.examples import python_example_code_1

    YieldFromTransformer(
        {
            "filename": "",
            "to_yield": "python_example_code_1.py"
        }
    ).visit(ast.parse(python_example_code_1))

# Generated at 2022-06-14 02:45:55.851207
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:46:03.894950
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse("""
    def f():
        yield from g()
        c = yield from h()
        yield from i()
        yield from j()""")
    YieldFromTransformer().visit(node)
    assert node.body[0].body[0].body[0].value.id == 'g'
    assert node.body[0].body[0].body[0].value.args.args == []
    assert node.body[0].body[1].body[0].value.id == 'h'
    assert node.body[0].body[1].body[0].value.args.args == []
    assert node.body[0].body[1].body[1].value.id == 'i'
    assert node.body[0].body[1].body[1].value.args.args == []


# Generated at 2022-06-14 02:46:09.094626
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    module = ast.parse("result = yield from generator")
    assert 'YieldFromTransformer' in str(type(YieldFromTransformer()))
    assert str(node_to_str(YieldFromTransformer().visit(module))) == """result = yield from generator"""


# Generated at 2022-06-14 02:46:10.397054
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:46:11.633689
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    T = YieldFromTransformer()

# Generated at 2022-06-14 02:46:15.214041
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = """
    def example(x):
        i = yield from x
    """
    tree = ast.parse(code)
    transformer = YieldFromTransformer()
    transformer.visit(tree)
    print(transformer)