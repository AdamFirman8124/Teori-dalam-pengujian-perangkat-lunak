

# Generated at 2022-06-14 02:06:04.844564
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from astor.code_gen import to_source

    source = """
        def fn():
            yield 1
            return 10
    """

    tree = ast.parse(source)  # type: ignore
    Transformer = ReturnFromGeneratorTransformer()
    new_tree = Transformer.visit(tree)  # type: ignore
    # The visitor shouldn't change the tree if there's no return in generators
    assert to_source(new_tree) == to_source(tree)

    source = """
        def fn2():
            yield 1
            return
    """

    tree = ast.parse(source)  # type: ignore
    Transformer = ReturnFromGeneratorTransformer()
    new_tree = Transformer.visit(tree)  # type: ignore
    # The visitor shouldn't change the tree if the return value is None
   

# Generated at 2022-06-14 02:06:10.619658
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse('def fn():\n    yield 1\n    return 5')
    node = tree.body[0]
    expected = 'def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc'
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)
    assert to_source(node) == expected

# Generated at 2022-06-14 02:06:12.335876
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:22.964662
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source_code_transformer import SourceCodeTransformer
    from ..utils.source_code_visitor import SourceCodeVisitor
    from ..utils.source_code_parser import parse

    class TestVisitor(SourceCodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            self.source_code.update(node, ReturnFromGeneratorTransformer().visit(node))
            return self.generic_visit(node)

    source = '''
        def generator_with_return():
            yield 1
            return 4
    '''
    expected = '''
        def generator_with_return():
            yield 1
            exc = StopIteration()
            exc.value = 4
            raise exc
    '''

# Generated at 2022-06-14 02:06:26.579510
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import ast as pyast
    from ..utils.source import source
    from ..transpile import transpile
    from .base import BaseNodeTransformer

    class _Mock(BaseNodeTransformer):
        def visit_FunctionDef(self, node):
            return node


# Generated at 2022-06-14 02:06:41.594899
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # method test_ReturnFromGeneratorTransformer_visit_FunctionDef of class ReturnFromGeneratorTransformer
    transformer = ReturnFromGeneratorTransformer()
    program_tree = ast.parse('def foo(a, b):\n    yield a\n    return b')
    returned_tree = transformer.visit(program_tree)

# Generated at 2022-06-14 02:06:50.067178
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class TestReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer):
        def __init__(self):
            ReturnFromGeneratorTransformer.__init__(self)
            self.function_names: List[str] = []
            self.return_values: List[Any] = []

        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            self.function_names.append(node.name)
            self.return_values = []
            for generator_return in self._find_generator_returns(node):
                _, return_ = generator_return
                self.return_values.append(return_.value)
            return ReturnFromGeneratorTransformer.visit_FunctionDef(self, node)

    import astor

# Generated at 2022-06-14 02:06:56.363401
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import typed_ast.ast3 as ast

    code = """def f(): yield 0; return 0"""
    expected_result = """def f(): yield 0
exc = StopIteration()
exc.value = 0
raise exc"""

    node = ast.parse(code, mode="exec")
    ReturnFromGeneratorTransformer.run_visitor(node, code)
    assert ast.unparse(node) == expected_result

# Generated at 2022-06-14 02:07:04.902282
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_helpers import get_ast, assert_code_equal
    source = '''
    def fn():
        yield 1
        return 5
    '''
    expected = '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''
    old_ast = get_ast(source)
    new_ast = ReturnFromGeneratorTransformer().visit(old_ast)
    assert_code_equal(new_ast, expected)


# Generated at 2022-06-14 02:07:12.601380
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def return_from_generator(return_value):
        exc = StopIteration()
        exc.value = return_value
        raise exc


# Generated at 2022-06-14 02:07:17.235510
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:19.446417
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..backport_ast import parse


# Generated at 2022-06-14 02:07:21.581891
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:07:31.970339
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('def fn(): yield 1; return 5')
    node2 = ast.parse('def fn(x): yield x; return x')
    ret_tr = ReturnFromGeneratorTransformer()
    expected = ast.parse('def fn(): yield 1; exc = StopIteration(); exc.value = 5; raise exc')
    expected2 = ast.parse('def fn(x): yield x; exc = StopIteration(); exc.value = x; raise exc')

    assert ast.dump(ret_tr.visit(node)) == ast.dump(expected)
    assert ast.dump(ret_tr.visit(node2)) == ast.dump(expected2)

# Generated at 2022-06-14 02:07:36.394273
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def generator(a):
        yield a
        return a

    def test():
        def test():
            def foo():
                yield 1
                return 5
        return foo


# Generated at 2022-06-14 02:07:43.468024
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    func_def = """
        def gen():
            yield 1
            return 5
            """
    expected = """
        def gen():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
            """
    expected = ast.parse(expected)
    func_def = ast.parse(func_def)
    result = ReturnFromGeneratorTransformer().visit(func_def)
    assert_code_equal(result, expected)



# Generated at 2022-06-14 02:07:53.331364
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    with patch('typed_astunparse.unparse') as unpatch:
        unpatch.side_effect = ['function_name = 5']

        import ast
        from flake8_typing_imports.transformers.return_from_generator import ReturnFromGeneratorTransformer
        transformer = ReturnFromGeneratorTransformer()
        new_node = transformer.visit(ast.parse('def function_name():\n\tyield 1\n\treturn 5\n'))
        assert str(new_node) == 'def function_name():\n\tyield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc\n'

# Generated at 2022-06-14 02:07:54.718859
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 02:07:56.379790
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor  # type: ignore


# Generated at 2022-06-14 02:08:03.703900
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_function_generator():
        yield 1
        yield 2
        return 1

    gen = test_function_generator()

    assert next(gen) == 1
    assert next(gen) == 2
    with pytest.raises(StopIteration) as exc_info:
        next(gen)
    assert exc_info.value.value == 1



# Generated at 2022-06-14 02:08:14.460532
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """
        def x():
            if 1:
                yield 1
                return 2
    """
    expected = """
        def x():
            if 1:
                yield 1
                exc = StopIteration()
                exc.value = 2
                raise exc
    """
    tree = ast.parse(source)  # type: ignore
    new_tree = ReturnFromGeneratorTransformer().visit(tree)  # type: ignore
    assert ast.dump(new_tree) == expected

# Generated at 2022-06-14 02:08:28.491995
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Regions
    from_ = 'from future import generators'
    code = '''
    import numbers
    import math
    import typing

    @decorator
    def fn() -> numbers.Number:
        '''

    yield_ = '  yield 1'
    blank = '  '
    return_ = '  return 5'

    to_ = '''
    import numbers
    import math
    import typing

    @decorator
    def fn() -> numbers.Number:
        '''

    yield_ = '  yield 1'
    blank = '  '
    exc_ = '  exc = StopIteration()'
    exc_value = '  exc.value = 5'
    raise_ = '  raise exc'
    # /Regions

    # Test 1

# Generated at 2022-06-14 02:08:38.787598
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test1():
        def fn():
            yield 1
            return 5
        return fn

    def test2():
        def fn():
            yield 1
        return fn

    def test3():
        def fn():
            def nested():
                yield 1
                return 5
            return nested
        return fn

    def test4():
        def fn():
            yield 1
            for x in range(5):
                yield x
            return 5
        return fn

    t1 = test1()
    for x in t1():
        assert x == 1
    with pytest.raises(StopIteration) as e:
        t1()
    assert e.value.value == 5

    t2 = test2()
    assert list(t2()) == [1]

    t3 = test3()

# Generated at 2022-06-14 02:08:49.037266
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import inspect
    import textwrap
    from ..utils.source import Source

    def get_source(func: ast.FunctionDef) -> Source:
        return Source(inspect.getsource(func))

    def get_func_body(func: ast.FunctionDef) -> Source:
        src = get_source(func)
        return Source(src.code[src.line + 1:src.endline - 1])

    def test_return_from_generator(fn):
        transformer = ReturnFromGeneratorTransformer()
        new_tree = transformer.visit(ast.parse(textwrap.dedent(fn)))

        new_func: ast.FunctionDef = next(
            node for node in ast.walk(new_tree) if isinstance(node, ast.FunctionDef)
        )


# Generated at 2022-06-14 02:09:02.081056
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import ast as stdlib_ast
    import textwrap

    # Example1:
    node = stdlib_ast.parse(textwrap.dedent('''
        def fn():
            yield 1
            return 5
    ''')).body[0]

    tree = ast.parse(
        textwrap.dedent('''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    ''')
    )
    expected = tree.body[0]  # type: ignore

    rft = ReturnFromGeneratorTransformer()
    result = rft.visit(node)

    assert result == expected

    # Example2:

# Generated at 2022-06-14 02:09:08.454441
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .setup_test import setup_test
    local_dict = setup_test()

    from typed_python._types import Function
    assert not isinstance(local_dict['generator_with_normal_return'], Function)
    assert isinstance(local_dict['generator_with_return'], Function)

# Generated at 2022-06-14 02:09:20.537069
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Node: pass
    # Case 1: no 'return' in function
    node = Node()
    node.body = []
    tree = ReturnFromGeneratorTransformer()
    tree._find_generator_returns(node)
    assert len(node.body) == 0

    # Case 2: one 'return' in function
    node = Node()
    node.body = []
    return_ = Node()
    return_.value = 4
    node.body.append(return_)
    tree = ReturnFromGeneratorTransformer()
    tree._find_generator_returns(node)
    assert len(node.body) == 0

    # Case 3: one 'return' in function and one 'yield' in function
    node = Node()
    node.body = []
    return_ = Node()
    return_.value = 4

# Generated at 2022-06-14 02:09:30.746456
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    input_code = """
    def fn():
        yield 1
        return 5
    """
    expected_output = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    tree = ast.parse(input_code)  # type: ignore
    ReturnFromGeneratorTransformer().visit(tree)  # type: ignore
    tree = ast.fix_missing_locations(tree)  # type: ignore
    output_code = astor.to_source(tree)

    assert output_code == expected_output

# Generated at 2022-06-14 02:09:38.788321
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse

    source = """
        def fn():
            yield 1
            return 5
    """
    expected_source = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    node = parse(source)
    ReturnFromGeneratorTransformer().visit(node)
    assert compile(node, '<unknown>', 'single')
    assert expected_source == ast.unparse(node)

# Generated at 2022-06-14 02:09:40.709138
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor

# Generated at 2022-06-14 02:10:01.061723
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.test_visitor import TestVisitor
    source = '''
        def fn():
            yield 1
            return 5
        def fn2():
            yield 1
            return 5
            yield 7
        def fn3():
            yield 1
            return
    '''

# Generated at 2022-06-14 02:10:08.953319
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    expected = ast.parse("""
    def test_fn(a, b):
        yield a
        exc = StopIteration()
        exc.value = b
        raise exc
    """)
    node = ast.parse("""
    def test_fn(a, b):
        yield a
        return b
    """)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)
    assert_equals(expected, node)

# Generated at 2022-06-14 02:10:17.923472
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def foo():
        yield 1
        yield 2
        return 3

    node = parso.parse(inspect.getsource(foo))
    transformer = ReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)
    assert new_node.get_code() == \
           "def foo():\n" \
           "    yield 1\n" \
           "    yield 2\n" \
           "    exc = StopIteration()\n" \
           "    exc.value = 3\n" \
           "    raise exc"



# Generated at 2022-06-14 02:10:22.687464
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .utils import get_node

    node = get_node("""
    def f():
        yield 1
        return 2

    def g():
        yield 1
        yield 2
        return 3

    def h():
        yield 1
        return
    """)
    transformer = ReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)

    assert new_node.body[0] == get_node("""
    def f():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """)
    assert new_node.body[1] == get_node("""
    def g():
        yield 1
        yield 2
        exc = StopIteration()
        exc.value = 3
        raise exc
    """)

# Generated at 2022-06-14 02:10:28.569323
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import ast_eq

    @snippet
    def fn():
        yield 1
        return 2

    @snippet
    def fn_res():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc

    tree = ast.parse(fn)
    tree_res = ast.parse(fn_res)
    transformer = ReturnFromGeneratorTransformer()

    assert ast_eq(transformer.visit(tree), tree_res)



# Generated at 2022-06-14 02:10:42.188538
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_node_equal

    def check(node: ast.FunctionDef, expected: ast.FunctionDef) -> None:
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(node)
        assert_node_equal(node, expected)

    def foo():
        yield 1
        return 'x'

    foo_expected = foo()
    foo_expected.body[-1].value = StopIteration()
    foo_expected.body.append(ast.Raise(value=foo_expected.body[-1].value,
                                  exc=ast.Name(id='exc', ctx=ast.Load()),
                                  traceback=None))
    check(foo(), foo_expected)

    def foo():
        yield 1
        return
        def fn():
            return 'x'



# Generated at 2022-06-14 02:10:50.261599
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # snippet fn
    def fn():
        yield 1
        if 5:
            yield 2
        return 3
    # /snippet
    fn_node = ast.parse(fn.source).body[0]
    fn_node = ReturnFromGeneratorTransformer.transform(fn_node)
    assert ast.dump(fn_node) == """
    def fn():
        yield
        1
        exc = StopIteration()
        exc.value = 3
        raise exc
    """

# Generated at 2022-06-14 02:10:56.045221
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    class NodeTransformerImpl(ReturnFromGeneratorTransformer):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            return super().visit_FunctionDef(node)


# Generated at 2022-06-14 02:10:59.573566
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_equal_ast, make_function

    def fn():
        yield 1
        yield 2
        return 5


# Generated at 2022-06-14 02:11:08.042049
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import ast_from_snippet, ast_to_source, ast_equal
    from ..utils.fixtures import snippet_return_from_generator
    from ..utils.visitor import print_ast

    tree = ast_from_snippet(snippet_return_from_generator.get_body())

    expected_tree = ast_from_snippet(snippet_return_from_generator.get_expected_body())

    transformer = ReturnFromGeneratorTransformer()
    transformed_tree = transformer.visit(tree)

    assert ast_equal(expected_tree, transformed_tree)



# Generated at 2022-06-14 02:11:51.407632
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3
    from ..utils.fake import fake_funcdef

    transformer = ReturnFromGeneratorTransformer()

    def test(body):
        func = fake_funcdef()
        func.body = body

        value = transformer.visit_FunctionDef(func)

        return value.body

    # case 1: no change
    assert test([]) == []

    # case 2: no change
    assert test([ast3.Return()]) == [ast3.Return()]

    # case 3: no change
    assert test([ast3.Return(None)]) == [ast3.Return(None)]

    # case 4: no change
    assert test([ast3.Return(ast3.Num(0)), ast3.Return()]) == [ast3.Return(ast3.Num(0)), ast3.Return()]



# Generated at 2022-06-14 02:11:58.354328
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

    def test(code, expected):
        tree = ast.parse(textwrap.dedent(code))

        transformer.visit(tree)

        assert textwrap.dedent(expected) == astor.to_source(tree)

    test('''
        def fn():
            yield 1
            return 5
    ''', '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    ''')

    test('''
        def fn():
            yield 1
            if True:
                return 5
    ''', '''
        def fn():
            yield 1
            if True:
                exc = StopIteration()
                exc.value = 5
                raise exc
    ''')


# Generated at 2022-06-14 02:12:10.697978
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse('''
    def g(x):
        if x == 0:
            yield None
            return 1
        else:
            x -= 1
            y = yield from g(x)
            return y + 1
    ''')
    tree = ReturnFromGeneratorTransformer().visit(tree)
    print(ast.dump(tree))

# Generated at 2022-06-14 02:12:19.951919
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_python.compiler.type_wrappers.int32_wrapper import Int32
    from typed_python.compiler.type_wrappers.none_type_wrapper import NoneTypeWrapper
    from typed_python.compiler.type_wrappers.wrapper import Wrapper
    from typed_python.compiler.conversion_level import ConversionLevel

    m = ast.Module()
    f = ast.FunctionDef(name="f1", args=ast.arguments(args=[], kwonlyargs=[], vararg=None, kwarg=None, defaults=[], kw_defaults=[]), body=[ast.Return(value=ast.Constant(value=1))])

# Generated at 2022-06-14 02:12:26.911007
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseTestTransformer, get_code
    import ast
    import unittest
    import inspect

    class Test(unittest.TestCase):
        def setUp(self):
            self.transformer = ReturnFromGeneratorTransformer()
            self.transform_function_body = BaseTestTransformer.make_visit_function_body(self.transformer)

        def test_1(self):
            code = get_code(inspect.getsource(test_ReturnFromGeneratorTransformer_visit_FunctionDef))
            node = ast.parse(code)
            self.transform_function_body(node.body[0].body)
            assert self.transformer._tree_changed == False


# Generated at 2022-06-14 02:12:39.816667
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    @snippet
    def test_case():
        let(fn)
        fn = lambda: x

# Generated at 2022-06-14 02:12:45.324353
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformerTestCase
    from ..transformers import ReturnFromGeneratorTransformer

    class Test(BaseNodeTransformerTestCase):
        def __init__(self, *args, **kwargs):
            super(Test, self).__init__(*args, **kwargs)
            self.transformer = ReturnFromGeneratorTransformer(self.tree)


# Generated at 2022-06-14 02:12:56.914789
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    input_ = """
    def fn1():
        yield 1
        return 5
    def fn2():
        yield 1
        return
    def fn3():
        yield 1
        return True
    def fn4():
        yield 1
        return 5 + 3
    def fn5():
        return 5
        yield 1
    """

# Generated at 2022-06-14 02:12:58.218577
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:11.732546
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import transform, ast_to_str

    source1 = """
    def fn():
        yield 1
        return 5
    """
    expected_ast1 = """
    def fn():
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    source2 = """
    def fn():
        for i in [1, 2, 3]:
            yield i
            return 5
    """
    expected_ast2 = """
    def fn():
        for i in [1, 2, 3]:
            exc = StopIteration()
            exc.value = 5
            raise exc
    """

    source3 = """
    def f1():
        yield 1
        def f2():
            yield 2
            return 5
    """

# Generated at 2022-06-14 02:14:51.784685
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:15:04.886688
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Node:
        pass

    fn = Node()
    fn.body = [Node(), Node(), Node(), Node(), Node()]
    node = Node()
    node.body = [fn, Node(), Node()]

    # Node in fn.body, which is not generator return
    fn.body[0].__class__ = ast.Yield
    with pytest.raises(StopIteration):
        returns = ReturnFromGeneratorTransformer()._find_generator_returns(node)
        assert returns == []

    # Node in fn.body, which is not generator return
    fn.body[0].__class__ = ast.YieldFrom
    with pytest.raises(StopIteration):
        returns = ReturnFromGeneratorTransformer()._find_generator_returns(node)
        assert returns == []

    # Node in

# Generated at 2022-06-14 02:15:08.609760
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3
    from ast_converter import convert_ast
    from ..utils.parse import parse_function
    from nose.tools import assert_equal
    

# Generated at 2022-06-14 02:15:19.127375
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(node, expected):
        t = ReturnFromGeneratorTransformer()
        t.visit(node)
        assert expected == node

    test(ast.parse('''
        def fn():
            yield
            return
        '''), ast.parse('''
        def fn():
            yield
        '''))
    test(ast.parse('''
        def fn():
            yield
            return 1
        '''), ast.parse('''
        def fn():
            yield
            exc = StopIteration()
            exc.value = 1
            raise exc
        '''))


__all__ = ['ReturnFromGeneratorTransformer']

# Generated at 2022-06-14 02:15:29.567920
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_visit_function_without_yield():
        class_ = """
        class A:
            def fn(self):
                return 1
        """
        expected = """
        class A:
            def fn(self):
                return 1
        """
        node = parse(class_, mode='exec')
        node = ReturnFromGeneratorTransformer().visit(node)
        assert str(node) == expected

    def test_visit_function_without_return():
        class_ = """
        class A:
            def fn(self):
                yield 1
        """
        expected = """
        class A:
            def fn(self):
                yield 1
        """
        node = parse(class_, mode='exec')
        node = ReturnFromGeneratorTransformer().visit(node)

# Generated at 2022-06-14 02:15:34.247305
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import bytes_from_list
    from ..utils.generic_visitor import GenericVisitor
    from ..utils.snippet import snippet
    from ..utils.typed_ast_pprint import TAP
    

# Generated at 2022-06-14 02:15:35.961738
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def gen_fn():
        yield 1
        return 5


# Generated at 2022-06-14 02:15:43.250289
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    FunctionDef_input = ast.parse('def fn(x):\n yield x\n return x')
    ReturnFromGeneratorTransformer().visit(FunctionDef_input)
    FunctionDef_expected = ast.parse('def fn(x):\n yield x\n exc = StopIteration()\n exc.value = x\n raise exc')
    assert ast.dump(FunctionDef_expected) == ast.dump(FunctionDef_input)

# Generated at 2022-06-14 02:15:48.002833
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:15:58.630422
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer