

# Generated at 2022-06-14 02:39:04.989297
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer  # hints YieldFromTransformer to flake8

# Generated at 2022-06-14 02:39:06.316845
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().__class__ == YieldFromTransformer

# Generated at 2022-06-14 02:39:07.328685
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:39:14.925140
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor
    from astor.codegen import to_source
    from fissix.pygram import python_symbols as syms
    from fissix.pytree import Leaf


# Generated at 2022-06-14 02:39:24.949433
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typing import List, Generator
    from ..utils.helpers import node_to_function
    from ..utils.tree import extract_node_at
    from ..utils.meta import change_meta
    from ..utils.snippet import get_entry_point

    # Unit test for method YieldFromTransformer._get_yield_from_index
    def test_get_yield_from_index():
        from ..utils.tree import get_closest_parent
        from ..rewrite.assignment_to_function import AssignmentToFunction
        from ..rewrite.correct_ast import CorrectAst

        def test(code: str, type_: Type[Holder], line: int):
            node = node_to_function(code)

            a2f = AssignmentToFunction()
            node = a2f.visit(node)  # type

# Generated at 2022-06-14 02:39:34.538569
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # 1. Create a YieldFromTransformer object
    Y = YieldFromTransformer()
    # 2. Create a node
    node = ast.While()
    # 3. Set the _tree_changed attribute
    Y._tree_changed = True
    # 4. Return node
    assert Y.visit(node) == node
    # Testing the _get_yield_from_index() method
    class Node():
        def __init__(self):
            self.body = [ast.While()]
    node = Node()
    assert Y._get_yield_from_index(node, ast.While) == 0
    assert Y._get_yield_from_index(node, ast.Module) == None
    # Testing the _emulate_yield_from() method
    node = ast.YieldFrom()
    assert Y

# Generated at 2022-06-14 02:39:35.721130
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()



# Generated at 2022-06-14 02:39:43.125951
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    trans = YieldFromTransformer('t.py', 'body')
    assert trans._get_yield_from_index(ast.parse('def f():\n    pass'), ast.Assign) is None
    assert trans._get_yield_from_index(ast.parse('def f():\n    a = yield from b'), ast.Assign) == 0
    assert trans._get_yield_from_index(ast.parse('def f():\n    a = yield from b'), ast.Expr) == None
    assert trans._get_yield_from_index(ast.parse('def f():\n    yield from b'), ast.Expr) == 0



# Generated at 2022-06-14 02:39:43.993427
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    raise NotImplementedError


# Generated at 2022-06-14 02:39:49.085439
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # We can't just check the type here since the function
    # YieldFromTransformer() has no meaningful return value
    assert callable(YieldFromTransformer)

# Unit tests for method _get_yield_from_index(self, node: ast.AST, type_: Type[Holder]) -> Optional[int]:

# Generated at 2022-06-14 02:39:56.274828
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None

# test_YieldFromTransformer()

# Generated at 2022-06-14 02:39:58.435083
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print('Creating new object of YieldFromTransformer')
    trans = YieldFromTransformer()
    assert trans is not None

# Generated at 2022-06-14 02:39:59.786212
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:40:02.022649
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.fake import FakeTreeGenerator
    YieldFromTransformer(FakeTreeGenerator()).transform(FakeTreeGenerator().ast)

# Generated at 2022-06-14 02:40:10.303625
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse("""
    class Foo:
        def __init__(self, a):
            self.a = a
        def bar(self, b):
            return yield from b""")
    YieldFromTransformer().visit(tree)
    expected = """class Foo:
    def __init__(self, a):
        self.a = a
    def bar(self, b):
        let(iterable)
        iterable = iter(b)
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    return exc.value
                break"""
    assert format(tree, 'setuptools') == expected

# Generated at 2022-06-14 02:40:12.801802
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer!=None

if __name__ == "__main__":
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:40:13.938064
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:40:14.856853
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:40:15.811726
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:23.345272
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse('''from asyncio import CancelledError
try:
    pass
except CancelledError as e:
    pass
''')
    expected_node = ast.parse('''from asyncio import CancelledError
try:
    pass
except CancelledError as e:
    pass
''')
    obj = YieldFromTransformer()
    assert obj.visit(node) == expected_node

# Generated at 2022-06-14 02:40:45.924583
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from io import StringIO
    from typed_ast import ast3
    from ..utils.compiler import compile_snippet_to_module
    from ..utils.helpers import VariablesGenerator
    from .base import BaseNodeTransformer

    code = '''
async def fn():
    i = (x async for x in [1, 2, 3, 4, 5])
    await do_stuff()
    return i
'''
    # Get the AST tree
    tree = ast3.parse(code)

    # Init class
    transformer = YieldFromTransformer()

    # Get the transformed tree
    tree = transformer.visit(tree)
    assert transformer.tree_changed

    # Get all the code
    buff = StringIO()
    ast3.unparse(tree, buff)

    # Replace all the generated variables (e.

# Generated at 2022-06-14 02:40:47.980127
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Pass
    YieldFromTransformer()
    assert True

# Generated at 2022-06-14 02:40:49.862766
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Prepare data for test_YieldFromTransformer
    # Variables for test_YieldFromTransformer
    yf = YieldFromTransformer()
    assert yf is not None

# Generated at 2022-06-14 02:41:00.217440
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from pythran.tests import TestEnv
    from pythran.passmanager import PassManager
    from pythran.analyses import PythranAnalysis
    from pythran.tables import MODULE_TRANSFORMS
    from os.path import join, dirname, realpath
    import sys
    import ast

    module = ast.parse("def foo(): yield from foo()")
    module.name = "__main__"

    env = TestEnv()
    pm = PassManager("test")
    generated = pm.gather(PythranAnalysis, [module], env)
    generated = pm.apply(YieldFromTransformer, generated, env)
    env.finalize()
    assert env.passmanager.dump(generated, "test", "YieldFromTransformer")
    #import astor
    #print(astor.to

# Generated at 2022-06-14 02:41:03.369916
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """ Unit test for constructor of class YieldFromTransformer."""
    # Arrange
    # Act
    obj = YieldFromTransformer
    # Assert
    assert obj is not None


# Generated at 2022-06-14 02:41:12.207699
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = 'a = yield from list(b)'
    expected_code = '''\
a = None
while True:
    try:
        iterable = iter(list(b))
        while True:
            try:
                a = next(iterable)
                yield a
            except StopIteration as exc:
                if hasattr(exc, 'value'):
                    a = exc.value
                break
    except StopIteration as exc:
        pass'''

    module = ast.parse(code)
    YieldFromTransformer().visit(module)
    assert ast.dump(module) == expected_code


code = '''\
a = yield from list(range(10))   # a = None
b = yield from list(range(20))   # b = None
yield from range(30)'''

expected

# Generated at 2022-06-14 02:41:12.724712
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:41:13.495639
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:41:14.573248
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


# Generated at 2022-06-14 02:41:20.783044
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from = ast.YieldFrom()
    target = ast.Name()
    yield_from.value = target
    target_assignment = ast.Assign()
    target_assignment.targets = [target]
    target_assignment.value = yield_from

    expr = ast.Expr()
    expr.value = yield_from

    body = [target_assignment, expr]

    try_ = ast.Try()
    try_.body = body
    try_.body = body
    m = ast.Module()
    m.body = [try_]

    t = YieldFromTransformer()
    t.visit(m)

    assert isinstance(try_.body[0], ast.Assign)
    assert isinstance(try_.body[1], ast.While)



# Generated at 2022-06-14 02:41:42.890956
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:44.580634
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    o = YieldFromTransformer()
    assert o.target == (3, 2)


# Unit tests for methods of class YieldFromTransformer

# Generated at 2022-06-14 02:41:48.539944
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class _YieldFromTransformerTester(unittest.TestCase):
        def setUp(self):
            self.assertTrue(YieldFromTransformer(None).__doc__)
            self.assertTrue(YieldFromTransformer(None).visit.__doc__)

    _YieldFromTransformerTester().setUp()


# Generated at 2022-06-14 02:41:49.762322
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None


# Generated at 2022-06-14 02:42:01.624138
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.source import Source
    from ..utils.helpers import unparse
    from .function_arguments import FunctionArgumentsTransformer

    code = '''
    def foo():
        yield from bar()
    '''
    source = Source(code, 'data')
    root = source.ast
    transformer = FunctionArgumentsTransformer()
    transformer.visit(root)
    transformer = YieldFromTransformer()
    transformer.visit(root)
    result = unparse(root)
    print(result)


# Generated at 2022-06-14 02:42:03.658056
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.transformer import Transformer
    from ..utils.source import Source


# Generated at 2022-06-14 02:42:11.075491
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import print_python_ast
    from .meta_transformer import MetaTransformer

    src = """
    def gen():
        yield 1
        yield 2

    def f():
        a = yield from gen()

    def g():
        yield from gen()

    def h():
        yield from gen()
        b = 1
    """

# Generated at 2022-06-14 02:42:12.059388
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:21.213357
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from . import ast_unparse
    from .replacement_transformer import ReplacementTransformer
    from compiler.consts import VERSION as PYTHON_VERSION
    import ast

    # Empty module
    module_str = 'pass'
    module_tree = ast.parse(module_str)

    # Test if the tree doesn't change
    if PYTHON_VERSION >= (3, 8):
        # A module is not modified
        assert str(module_tree) == module_str
        assert ast_unparse.unparse(module_tree) == module_str

    # Transform assign
    module_str = 'def foo(a): yield from a'

    module_tree = ast.parse(module_str)
    module_tree = ReplacementTransformer().visit(module_tree)

# Generated at 2022-06-14 02:42:22.774657
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:25.367617
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  i = YieldFromTransformer()
  assert i is not None


# Generated at 2022-06-14 02:43:27.522393
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .pep8_to_py3 import PEP8ToPy3Transformer


# Generated at 2022-06-14 02:43:28.865757
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # __init__(self) -> None
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:43:31.006470
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    g = YieldFromTransformer()
    assert(g is not None)

# Unit tests for method _get_yield_from_index of class YieldFromTransformer

# Generated at 2022-06-14 02:43:32.214380
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:43:34.400905
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()
    assert YieldFromTransformer


# Generated at 2022-06-14 02:43:35.503354
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:45.850253
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    trans = YieldFromTransformer()
    fn = ast.FunctionDef(body=[ast.Expr(value=ast.YieldFrom(value=ast.Name(id='generator')))])
    trans.visit(fn)
    assert [item.id for item in fn.body[0].body[0].targets] == ['yield_from']
    assert [item.value.id for item in fn.body[0].body if isinstance(item, ast.Assign)] == ['yield_from']

    fn = ast.FunctionDef(body=[ast.Expr(value=ast.YieldFrom(value=ast.Name(id='generator')))])
    trans.visit(fn)

# Generated at 2022-06-14 02:43:53.530428
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3
    # compile string to ast.Module
    node1 = ast3.parse('a = yield from list(range(4))')
    node2 = ast3.parse('yield from list(range(4))')
    node3 = ast3.parse('yield from list(range(4))\n yield from list(range(4))')
    node4 = ast3.parse('\n a = yield from list(range(4))\n b = yield from list(range(4))\n')
    print(node1)
    print(node2)
    print(node3)
    print(node4)
    # create an instance YieldFromTransformer
    t1 = YieldFromTransformer()
    # call visit method and transfrom ast.Module
    t1.visit(node1)


# Generated at 2022-06-14 02:44:04.758254
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.ast_builder import build

    class TestTransformer(YieldFromTransformer):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._tree_changed = False

    # Simple case
    ast_one = build("""
    a = range(2)
    yield from a
    """)
    trans = TestTransformer()
    trans.visit(ast_one)
    assert trans._tree_changed
    ast_two = build("""
    a = range(2)
    while True:
        try:
            yield next(iter(a))
        except StopIteration as exc:
            a = exc.value
            break
    """)
    assert ast_one == ast_two

    # Try test

# Generated at 2022-06-14 02:46:49.557503
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    if True:
        pass
    if True:
        pass
    if True:
        pass
    if True:
        pass
    if True:
        pass

# Generated at 2022-06-14 02:46:50.185608
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    raise Exception

# Generated at 2022-06-14 02:46:53.923293
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    for var_num in range(10):
        for target in [(3, 2), (3, 3)]:
            x = YieldFromTransformer(target)
            x = YieldFromTransformer(target)
            assert isinstance(x, YieldFromTransformer)

# Generated at 2022-06-14 02:46:55.247815
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:47:03.908136
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.ast3 import Try, Expr, FunctionDef, Name, Load, YieldFrom, Module
    from typed_ast.ast3 import AST
    from typed_ast.ast3 import Store, Arguments

    funcbody = [Try(body=[Expr(value=YieldFrom(value=Name(id='yf_gen', ctx=Load())))],
                    handlers=[Expr(value=YieldFrom(value=Name(id='yf_gen', ctx=Load())))],
                    orelse=[Expr(value=YieldFrom(value=Name(id='yf_gen', ctx=Load())))],
                    finalbody=[Expr(value=YieldFrom(value=Name(id='yf_gen', ctx=Load())))])]


# Generated at 2022-06-14 02:47:04.709067
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:47:05.436812
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    Transformer = YieldFromTransformer()
    Transformer

# Generated at 2022-06-14 02:47:10.547186
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import parse
    tree = parse(
        'yield from range(10)')
    print(tree)
print(YieldFromTransformer(tree, {}))



transformer = YieldFromTransformer()
assert transformer.generic_visit(tree)

print(ast.dump(transformer.generic_visit(tree)))

# tree = ast.parse(
#     'yield from range(10)')

# print(tree)

# Generated at 2022-06-14 02:47:12.059958
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer

# Generated at 2022-06-14 02:47:12.796913
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer