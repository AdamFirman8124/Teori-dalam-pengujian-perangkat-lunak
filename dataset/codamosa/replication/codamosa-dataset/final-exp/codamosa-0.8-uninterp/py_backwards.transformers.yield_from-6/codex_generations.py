

# Generated at 2022-06-14 02:39:05.033517
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:06.362377
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # assert_raises()
    # assert_equal()
    pass

# Generated at 2022-06-14 02:39:16.493088
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ast import parse
    from .base import Compiler
    from .check_unused import CheckUnused
    from .pep8 import Pep8
    from .linter import Linter
    from .decorators import Decorators
    from .asserts import Asserts
    from .all_builtins import AllBuiltins
    from .imports import Imports
    from .long_integers import LongIntegers
    from .unpacking import Unpacking
    from .comprehensions import Comprehensions
    from .properties import Properties
    from .strings import Strings
    from .classes import Classes
    from .delegation import Delegation
    from .exceptions import Exceptions
    from .coercions import Coercions
    from .statements import Statements
    from .rename import Rename
    from .boolop import BoolOp

# Generated at 2022-06-14 02:39:19.050672
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.test_utils import _transform_and_compare


# Generated at 2022-06-14 02:39:22.813906
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class ExampleYieldFromTransformer(YieldFromTransformer):
        def visit(self, node):
            pass
    x = ExampleYieldFromTransformer()
    assert isinstance(x, YieldFromTransformer)
    assert x.target == (3, 2)
    assert isinstance(x.generic_visit, object)


# Generated at 2022-06-14 02:39:23.832567
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer({})


# Generated at 2022-06-14 02:39:29.463584
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import gather
    from astor.source_repr import dump
    from textwrap import dedent

    cls = YieldFromTransformer()
    code = dedent("""
    def helper(arg):
        yield from arg is None

    async def func():
        value = yield from helper([2])
    """)

    module = gather(code)
    cls.visit(module)
    print(dump(module))

# Generated at 2022-06-14 02:39:31.127011
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Instantiating YieldFromTransformer object
    u = YieldFromTransformer()

# Generated at 2022-06-14 02:39:32.132822
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:41.569123
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from darglint.processor import Processor
    from ..main import darglint
    from .pep8 import PEP8Checker
    from .base import BaseNodeTransformer

    class TestChecker(PEP8Checker):
        pass

    assert BaseNodeTransformer in TestChecker.__mro__
    assert PEP8Checker in TestChecker.__mro__

    args = (['darglint', '-v', '--checkers', 'TestChecker',
            'tests/data/yield_from_examples/yield_from.py'],)
    options, _ = darglint.parse_args(*args)
    processor = Processor(options, TestChecker)

# Generated at 2022-06-14 02:39:49.724954
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    ast.Try, ast.If, ast.While, ast.For, ast.FunctionDef, ast.Module
    Union[ast.Expr, ast.Assign]

# Generated at 2022-06-14 02:39:57.953580
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    snip = snippet('''
        def foo():
            yield from 1
            yield from 2
            yield from 3
    ''')

    assert_ast_equals(snip, """
    def foo():
        iterable = iter(1)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                exc = exc
                break
        iterable = iter(2)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                exc = exc
                break
        iterable = iter(3)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                exc = exc
                break
    """)



# Generated at 2022-06-14 02:39:59.689749
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer
    t = YieldFromTransformer()


# Generated at 2022-06-14 02:40:01.126714
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  t = YieldFromTransformer()
  assert t is not None

# Generated at 2022-06-14 02:40:10.510797
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    def make_test_node(node_name: str, node_body: ast.AST) -> ast.AST:
        class TestNode(ast.AST):
            _fields = ('node_body',)

        test_node = TestNode()  # type: ignore
        setattr(test_node, node_name, node_body)
        return test_node

    cases = (
        ('function_def', ast.FunctionDef),
        ('for', ast.For),
        ('while', ast.While),
        ('if', ast.If),
        ('try', ast.Try),
    )

    for node_name, node_type in cases:
        node_body = make_test_node('body', ast.AST())
        test_node = make_test_node(node_name, node_body)

        yield_from_trans

# Generated at 2022-06-14 02:40:21.777078
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from js2py.pyjs import translate_function
    from js2py.base import PyJsException, PyJsUndefined
    from js2py.pyjs_shared.translator import PyJsTranslateError
    # (1) Arguments passing

# Generated at 2022-06-14 02:40:31.885750
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class node1(ast.AST):
        _fields = []
    node1.__name__ = 'Expr'
    class node2(ast.AST):
        _fields = ['value']
    node2.__name__ = 'Assign'
    class node3(ast.AST):
        _fields = ['value']
    node3.__name__ = 'YieldFrom'
    class node4(ast.AST):
        _fields = ['body']
    node4.__name__ = 'Module'
    class node5(ast.AST):
        _fields = ['body']
    node5.__name__ = 'If'
    class node6(ast.AST):
        _fields = ['body']
    node6.__name__ = 'While'
    class node7(ast.AST):
        _fields = ['body']

# Generated at 2022-06-14 02:40:37.791268
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor
    from textwrap import dedent
    from ..utils.helpers import tree_from_string
    tree = tree_from_string(dedent("""
    if True:
        yield from [1, 2, 3]
    """))
    assert not YieldFromTransformer().process(tree)
    assert astor.to_source(tree) == dedent("""
    if True:
        let(iterable)
        iterable = iter([1, 2, 3])
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    exc = exc.value
                break
    """)


# Generated at 2022-06-14 02:40:46.534786
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("""def func():\n    x = yield from f()""")
    YieldFromTransformer().visit(tree)
    assert ast.dump(tree) == """Module(body=[FunctionDef(name='func', body=[Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Name(id='iter', ctx=Load()), args=[Call(func=Name(id='f', ctx=Load()), args=[], keywords=[])], keywords=[]))], args=[], decorator_list=[], returns=None)])"""

# Generated at 2022-06-14 02:40:50.546277
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class_method, _ = get_class_method(YieldFromTransformer,
                                       "__init__",
                                       "YieldFromTransformer")
    assert class_method.__doc__ == ("Compiles yield from to special while statement.")



# Generated at 2022-06-14 02:41:02.564244
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().target == (3, 2)


# Generated at 2022-06-14 02:41:04.424102
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from = YieldFromTransformer()
    assert isinstance(yield_from, YieldFromTransformer)

# Generated at 2022-06-14 02:41:11.224154
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor
    with open('./test/test_funcs/yield_from_test.py') as module_file:
        tree = ast.parse(module_file.read())
    YieldFromTransformer(debug=False).visit(tree)
    tree2 = astor.dump(tree)
    with open('./test/test_funcs/compiled_yield_from_test.py') as module_compiled:
        tree3 = module_compiled.read()
    assert tree2 == tree3

# Generated at 2022-06-14 02:41:14.529002
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'
    assert YieldFromTransformer.__doc__ == "Compiles yield from to special while statement."
    assert YieldFromTransformer.target == (3, 2)


# Generated at 2022-06-14 02:41:16.466498
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:17.331517
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:18.526096
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    obj = YieldFromTransformer()
    assert obj.target == (3, 2)

# Generated at 2022-06-14 02:41:20.044414
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


# Generated at 2022-06-14 02:41:22.268478
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    _ = YieldFromTransformer(None)

# Generated at 2022-06-14 02:41:26.033253
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert issubclass(YieldFromTransformer, BaseNodeTransformer)
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'
    YieldFromTransformer()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 02:41:47.167731
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:41:49.906402
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Unit tests for function _get_yield_from_index

# Generated at 2022-06-14 02:41:50.885830
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:02.459998
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import generate_var
    from ..utils.node import pformat
    from ..utils.meta import copy_meta
    generator = generate_var('generator')
    try_ = ast.Try(body=[
        ast.Expr(value=ast.YieldFrom(value=generator)),
    ],
    finalbody=[
        ast.Expr(value=ast.YieldFrom(value=generator)),
    ],
    handlers=[ast.ExceptHandler(body=[
        ast.Expr(value=ast.YieldFrom(value=generator)),
    ])])
    module = ast.parse('""')
    module.body = [try_]
    tree = YieldFromTransformer().visit(module)

# Generated at 2022-06-14 02:42:03.354951
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # No need to test
    pass


# Generated at 2022-06-14 02:42:05.572201
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from_transformer = YieldFromTransformer()
    assert yield_from_transformer

# Generated at 2022-06-14 02:42:16.043756
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    snippet.sneak_in(True)
    res = YieldFromTransformer().visit(
        ast.parse('x = yield from "abd"; y = yield from "abd"')
    )

# Generated at 2022-06-14 02:42:26.261494
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # create a class object
    yf = YieldFromTransformer()
    # a function definition
    func = ast.FunctionDef(name='func', body=[], decorator_list=[])
    # a yield from statement
    yieldf = ast.YieldFrom(value=ast.Name(id='a', ctx=ast.Load()))
    # an assign statement with yield from
    assign_stmt = ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())], value=yieldf)
    # call visit method
    yf.visit(assign_stmt)
    # verify
    assert assign_stmt.value.value.id == 'iter'
    assert assign_stmt.value.value.args[0].id == 'a'
    # a assert statement with yield from

# Generated at 2022-06-14 02:42:27.903965
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:42:32.492939
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.source import source
    from ..transformers import TransformerSequence

    t = TransformerSequence(YieldFromTransformer())
    t.visit(source('def f():\n    yield from range(5)'))

# Generated at 2022-06-14 02:43:16.930643
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__doc__ is not None

# Generated at 2022-06-14 02:43:18.671481
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:43:30.531363
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:43:33.325293
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = 5
    y = 6
    z = YieldFromTransformer([x,y])
    assert z.visit() == [5,6]

# Generated at 2022-06-14 02:43:35.605146
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast

    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:43:37.637359
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_utils import parse, compare_source
    from . import YieldFromTransformer


# Generated at 2022-06-14 02:43:38.834983
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    obj = YieldFromTransformer()
    assert(isinstance(obj, BaseNodeTransformer))


# Generated at 2022-06-14 02:43:40.256948
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()
    assert t is not None

# Generated at 2022-06-14 02:43:48.981936
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Class variable
    assert YieldFromTransformer.target == (3, 2)
    # Private variable
    assert YieldFromTransformer._tree_changed == False
    # Private method
    # _get_yield_from_index()
    yield_from_statement = ast.YieldFrom(value=None)
    index_expression = ast.Expr(value=yield_from_statement)
    index_assignment = ast.Assign(targets=[None], value=yield_from_statement)
    body_list = [index_expression, index_assignment]
    test_node_with_body = ast.FunctionDef(body=body_list, name="TestNode")
    assert YieldFromTransformer._get_yield_from_index(test_node_with_body, ast.Expr) == 0
   

# Generated at 2022-06-14 02:43:49.859666
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert(True)



# Generated at 2022-06-14 02:45:47.049655
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = ast.parse('result = yield from foo()')
    YieldFromTransformer().visit(a)
    assert str(a) == "result = yield from foo()"

# Generated at 2022-06-14 02:45:48.471843
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:45:59.299995
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .context import Context
    from .mock_node import MockNode
    from ..utils.tree import get_node
    node = MockNode(
        body=[
            MockNode(
                body=[
                    MockNode(body=MockNode()),
                    MockNode(body=MockNode()),
                ]
            )
        ]
    )
    context = Context(YieldFromTransformer(), node)
    new_node = context.run()
    node = get_node(new_node, ast.While)
    assert node is not None

# Generated at 2022-06-14 02:46:01.409677
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from random import choice
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:46:15.073609
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.unparse import Unparser
    from ..utils.helpers import get_ast, print_tree
    from ..utils.test_utils import assert_equal


# Generated at 2022-06-14 02:46:16.792143
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:46:22.472865
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.test_helper import AssertTree
    from ..visitors.printer import print_tree
    from .fold_if import IfStatementFoldingTransformer

    tree = AssertTree(
        YieldFromTransformer,
        IfStatementFoldingTransformer,
        __file__,
        'yield_from_transformer',
        'YieldFromTransformer',
        'test_case',
    )
    print(print_tree(tree.module))
    tree.assert_equal()

# Generated at 2022-06-14 02:46:31.325228
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.testing import assert_transform
    # try:
    #     yield from ...
    # catch StopIteration as e:
    #     ...
    @assert_transform(YieldFromTransformer,
                      'try:\n    yield from i\nexcept StopIteration as e:\n    pass',
                      """\
try:
    let(iterable)
    iterable = iter(i)
    while True:
        try:
            yield next(iterable)
        except StopIteration as exc:
            break
except StopIteration as e:
    pass""")
    def test_yield_from_in_try_catch(i):
        try:
            yield from i
        except StopIteration as e:
            pass

    # try:
    #     yield from ...
    # catch StopIteration:
   

# Generated at 2022-06-14 02:46:35.029601
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Unit test for constructor of class YieldFromTransformer"""
    assert YieldFromTransformer().target == (3, 2)


# Generated at 2022-06-14 02:46:36.988416
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse('a = yield from []')
    node = YieldFromTransformer().visit(node)
