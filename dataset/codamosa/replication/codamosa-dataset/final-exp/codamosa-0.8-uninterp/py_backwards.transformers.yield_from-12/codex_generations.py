

# Generated at 2022-06-14 02:39:06.714184
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import pickle
    from typed_ast import ast3
    from typed_ast.transforms import YieldFromTransformer
    t = YieldFromTransformer()
    assert t is not None
    assert isinstance(t, YieldFromTransformer)        
    pickle.dumps(t)

# Generated at 2022-06-14 02:39:08.748851
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transform = YieldFromTransformer()
    assert transform is not None

# Generated at 2022-06-14 02:39:10.058247
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None

# Generated at 2022-06-14 02:39:10.938495
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:39:15.591751
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse('def foo(): yield from foo()')
    assert YieldFromTransformer().visit(node) == ast.parse('def foo(): iterable = iter(foo()); while True: try: yield next(iterable) except StopIteration as e: if hasattr(e, \'value\'): pass; break')


# Generated at 2022-06-14 02:39:18.302350
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    _ = YieldFromTransformer()

# Generated at 2022-06-14 02:39:25.940976
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astunparse
    from typed_ast import ast3 as ast
    a = ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                    value=ast.YieldFrom(value=ast.Call(func=ast.Name(id='c', ctx=ast.Load()),
                                                       args=[ast.Num(n=10)],
                                                       keywords=[])))
    m = ast.Module(body=[a])
    YieldFromTransformer().visit(m)
    assert astunparse.unparse(m) == '\nresult_assignment(exc, a)\n'


# Generated at 2022-06-14 02:39:30.355407
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    from ..utils.ast_helpers import to_source
    from ..typed_ast import ast3 as typed_ast

    inp = """
x = f()
y = g(x)
    """

    def func():
        a = f()
        b = g(a)


# Generated at 2022-06-14 02:39:30.924396
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:32.316780
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(3, 2) != None


# Generated at 2022-06-14 02:39:38.671161
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:39:40.594963
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tryTransformer = YieldFromTransformer()
    testNode = ast.parse('a = yield from b')
    tryTransformer.visit(testNode)

# Generated at 2022-06-14 02:39:41.390883
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = YieldFromTransformer()


# Generated at 2022-06-14 02:39:47.307771
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from unittest import TestCase

    from ..utils.testing import source

    class YieldFromTransformerTest(TestCase):
        def _test(self, code: str, expected: str) -> None:
            new_tree = YieldFromTransformer().visit(
                source(code).tree
            )  # type: ignore

            self.assertEqual(source(expected).code,
                             source.from_ast(new_tree).code)

        def test_simple(self) -> None:
            code = """
                def func1(n):
                    yield from range(10)
                """

# Generated at 2022-06-14 02:39:48.420336
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None) is not None

# Generated at 2022-06-14 02:39:50.016987
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tf = YieldFromTransformer([])
    assert isinstance(tf, YieldFromTransformer)

# Generated at 2022-06-14 02:39:50.895127
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:39:52.427236
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None).__class__ == YieldFromTransformer


# Generated at 2022-06-14 02:39:53.623722
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = YieldFromTransformer()
    assert node is not None

# Generated at 2022-06-14 02:39:55.309567
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor


# Generated at 2022-06-14 02:40:08.753894
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer(None)
    try:
        t.visit(None)
    except Exception as e:
        print (e)
    # assert False
    return True
assert test_YieldFromTransformer()

# Generated at 2022-06-14 02:40:19.563438
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    def transform(code):
        """
        Transform yield from to while cycle with try statement
        """
        module = ast.parse(code)
        transformer = YieldFromTransformer()
        transformer.visit(module)
        module = ast.fix_missing_locations(module)
        return module, transformer._tree_changed

    code = """
    def fun():
        yield from gen()
    """
    assert transform(code)[1]

    code = """
    def fun():
        yield from gen()
        yield from gen()
    """
    assert transform(code)[1]

    code = """
    def fun():
        yield from gen()
        yield from gen()
        x = 5
    """
    assert transform(code)[1]


# Generated at 2022-06-14 02:40:21.440156
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert(isinstance(YieldFromTransformer(), YieldFromTransformer))

# Generated at 2022-06-14 02:40:22.809431
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:30.539161
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.source import source
    import astor

    source_code = source('''
        def f(x):
            a, b = yield from (g() for _ in range(x))
            yield from (c + d for _ in range(x))
            yield from range(x)
            return yield from e(x)
        ''')
    code = source_code.get_ast()
    result = YieldFromTransformer().visit(code)
    print(astor.to_source(result))
    assert astor.to_source(code) == astor.to_source(result)

# Generated at 2022-06-14 02:40:31.233687
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:40:35.591341
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast.ast3 import parse
    from ..utils.tree import dump
    from ..rewriter import Rewriter
    source = '''
        x = yield from f()
        g()
        '''
    ast_tree = parse(source)
    rewriter = Rewriter(ast_tree)
    rewriter.apply_transformers([YieldFromTransformer])
    dump(rewriter.tree)

# Generated at 2022-06-14 02:40:47.978946
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_base import get_test_Astroid
    from ..patcher.source.util import get_patched_ast_tree
    from ..patcher.node_transformer.utils import dump_ast
    from ..patcher.node_transformer.utils import compare_ast_trees
    from ..patcher.source.iter_replacer import IterReplacer
    from ..patcher.mod import PythonMod
    from ..utils.transform import _transform
    
    # test 1: test YieldFromTransformer constructor

# Generated at 2022-06-14 02:40:52.710944
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from = ast.YieldFrom(value = ast.Name(id='None', ctx=ast.Load()))
    exp = ast.Expr(value = yield_from)
    body = [exp]
    node = ast.Module(body = body)

    yield_from_transformer = YieldFromTransformer()
    yield_from_transformer.visit(node)
    # Compare the compiler version
    assert(yield_from_transformer.target == (3, 2))

# Generated at 2022-06-14 02:40:53.556379
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer is not None

# Generated at 2022-06-14 02:41:22.570242
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. codegen import to_source
    tree = ast.parse("def f(): yield from [1, 2, 3, 4]")
    module = YieldFromTransformer().visit(tree)
    assert module is not tree
    source = to_source(module)
    print(source)
    assert source == 'def f():\n    exc = VariablesGenerator.generate(\'exc\')\n    iterable = iter([1, 2, 3, 4])\n    while True:\n        try:\n            yield next(iterable)\n        except StopIteration as exc:\n            if hasattr(exc, \'value\'):\n                exc = exc.value\n            break\n'


# Generated at 2022-06-14 02:41:23.766660
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:41:38.519488
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_helpers import Context
    from .test_helpers import assert_ok
    from typed_ast.test_utils import assert_parse_dump
    from typed_ast import ast3 as ast

    # It should remove yield from from the assignments.
    with Context(YieldFromTransformer):
        node = ast.parse("""
            def foo():
                a = yield from bar()
                a = yield from baz()
                b = yield from qux()
                c = yield from quux()
            """
        )
        assert_ok(node, lambda n: n.body[0].body)


# Generated at 2022-06-14 02:41:45.589886
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    ast_tree = ast.parse("""
    def f():
        yield from range(5)
    """)

    tr = YieldFromTransformer()
    tr.visit(ast_tree)
    transformed_tree = ast.parse("""
    def f():
        let(iterable)
        iterable = iter(range(5))
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                break
    """)

    assert ast.dump(transformed_tree) == ast.dump(ast_tree)

# Generated at 2022-06-14 02:41:48.352573
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    tree = ast.parse('''
try:
    result = yield from async_func()
except Exception as e:
    pass
''')
    YieldFromTransformer().visit(tree)
    assert compile(tree, '', 'exec')

# Generated at 2022-06-14 02:41:55.569993
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    body = ast.Expr(ast.YieldFrom('fixture'))
    module = ast.Module([body], type_ignores=[])
    assert module.body[0].value.value == 'fixture'
    module = YieldFromTransformer().run(module)
    assert module.body[0].value.value.value == 'fixture'
    assert module.body[1].value.value == 'fixture'

# Generated at 2022-06-14 02:42:02.594707
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import typeddfs
    from typed_ast.ast3 import parse, TryExcept
    source2 = '''
        def foo():
            try:
                yield from bar()
            except Exception as e:
                pass
    '''
    tree = parse(source2)
    for node in tree.body:
        if isinstance(node, TryExcept):
            func_repr = repr(YieldFromTransformer().visit(node))
        else:
            func_repr = 'foo'
    assert func_repr == 'foo'

# Generated at 2022-06-14 02:42:04.436697
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()
    assert t


# Generated at 2022-06-14 02:42:05.414966
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:42:06.661337
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():  
    YieldFromTransformer()

# Generated at 2022-06-14 02:42:50.630921
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == "YieldFromTransformer"

# Generated at 2022-06-14 02:42:51.208826
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass # TODO

# Generated at 2022-06-14 02:43:01.460610
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  from ..utils.helpers import load_example_ast, save_ast
  import ast
  from .base import BaseNodeTransformer
  from .yield_from import YieldFromTransformer

  ast_dict = load_example_ast('yield_from')
  assert isinstance(ast_dict, dict)

  assert "ast" in ast_dict.keys()
  assert "code" in ast_dict.keys()

  result_ast = ast_dict["ast"]
  assert isinstance(result_ast, ast.Module)

  code_str = ast_dict["code"]
  assert isinstance(code_str, str)

  example_tree = YieldFromTransformer().visit(result_ast)
  assert isinstance(example_tree, ast.Module)


# Generated at 2022-06-14 02:43:04.761383
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # assert YieldFromTransformer() != YieldFromTransformer()
    assert YieldFromTransformer(3, 2) != YieldFromTransformer(3, 3)


# Generated at 2022-06-14 02:43:06.078785
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:43:07.090257
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()

# Generated at 2022-06-14 02:43:16.288670
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import code

    assert code('def foo():\n    yield from bar(1)') == code(
        'def foo():\n  iterable = iter(bar(1))\n  while True:\n    try:\n      yield next(iterable)\n    except StopIteration as exc:\n      break\n'
    )
    assert code('some = 3\ndef foo():\n    some = yield from bar(1)') == code(
        'some = 3\ndef foo():\n  iterable = iter(bar(1))\n  while True:\n    try:\n      yield next(iterable)\n    except StopIteration as exc:\n      some = exc.value\n      break\n'
    )

# Generated at 2022-06-14 02:43:18.544483
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor
    from .base import BaseNodeTransformer


# Generated at 2022-06-14 02:43:30.042390
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Setup
    from ..utils.environment import Environment
    from ..utils.helpers import parse
    from .main import MainTransformer

    env = Environment(YieldFromTransformer, MainTransformer)
    with open('../tests/transformer/yield_from/test.py') as f:
        tree = parse(f.read(-1))
    transformer = YieldFromTransformer(env)

    # Exercise
    transformer.visit(tree)
    # Verify
    assert transformer._tree_changed
    expected_file = '../tests/transformer/yield_from/expected.py'
    with open(expected_file) as f:
        expected = f.read(-1)
    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 02:43:30.975756
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer



# Generated at 2022-06-14 02:45:29.071177
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import load_example_ast
    name = "YieldFromTransformer"
    path = f"{name}.py"
    with open(path, "w") as f:
        f.write(load_example_ast(name, "YieldFromTransformer"))
    __import__(f"{name}")
    as_str = open(path).read()
    assert as_str == load_example_ast(name, "YieldFromTransformer", False)

# Generated at 2022-06-14 02:45:36.326041
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from . import default_fixture

    fixt = default_fixture

    match = fixt('''
    a = yield from gen()
    ''')
    want = fixt('''
    let(exc)
    let(iterable)
    iterable = iter(gen())
    try:
        a = next(iterable)
    except StopIteration as exc:
        pass
    ''')

    match ^ YieldFromTransformer

    match == want

# Generated at 2022-06-14 02:45:42.398021
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..transformers.tests.utils import transform
    from ..transformers.yield_from import YieldFromTransformer
    from ..utils.helpers import get_ast
    from ..utils.source import Source

    src = """
    result = yield from generator
    """
    expected = """
    let(iterable)
    iterable = iter(generator)
    while True:
        try:
            yield next(iterable)
        except StopIteration as exc:
            result = exc.value
            break
    """
    # src = """
    # result = yield from f() + g()*(yield from [1, 2, 3])
    # result = yield from h() or yield from i()
    # result = yield from k() and yield from g()
    # result = yield from l()
    # """
    #

# Generated at 2022-06-14 02:45:57.967872
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from compiler import compile
    from compiler.ast import CallFunc, Name, Assign, AssName, \
        Getattr, AssAttr, Yield, YieldFrom, Function, GenExprFor, GenExprIf, \
        Module, Printnl, Discard, Lambda, Return, TryExcept, List, \
        If, While, For, Raise, TryFinally, Tuple, Stmt, Const, IfExp, Or, And, \
        Backquote, Add, Sub, Mul, Div, Mod, UnaryAdd, UnarySub, Power, Invert, \
        LeftShift, RightShift, Bitand, Bitor, Bitxor, FloorDiv, Not, Compare, \
        Subscript, In, NotIn, Is, IsNot, ListComp, Continue, Break, Class


# Generated at 2022-06-14 02:46:05.338983
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ast import parse
    from .test_nodes import CNodeTransformer
    from .test_nodes import assert_source_equal

    YieldFromTransformer.register_transformed_nodes(CNodeTransformer)

    source = '''
        def foo():
            for i in [1, 2]:
                yield from i
                yield from i
    '''
    tree = parse(source)
    YieldFromTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:46:06.850985
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:46:08.135919
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()

# Generated at 2022-06-14 02:46:10.210646
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    c = YieldFromTransformer()
    assert c is not None

# Generated at 2022-06-14 02:46:21.304960
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from compiler.ast import Assign, Function, Module, Name, Node, Print, Subscript, YieldFrom
    
    source = 'def foo():\n' +\
             '    yield from bar()'
    expected = Module(None, Stmt([Function(None, 'foo', [], [], 0, None, Stmt([While(CallFunc(Name('next'), [CallFunc(Name('iter'), [CallFunc(Name('bar'), [])])], None, None), [Excepthandler([Name('StopIteration')], None, [Pass()])], Pass(), None)]), None)]))
    c = YieldFromTransformer()
    actual = c.visit(parse(source))
    assert ast_eq(actual, expected)


# Generated at 2022-06-14 02:46:23.805720
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    trans = YieldFromTransformer()
    assert repr(trans) == 'YieldFromTransformer()'
