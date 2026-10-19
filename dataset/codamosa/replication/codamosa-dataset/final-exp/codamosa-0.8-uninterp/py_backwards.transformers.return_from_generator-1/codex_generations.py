

# Generated at 2022-06-14 02:06:03.453617
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class ReturnFromGeneratorTransformerMock(ReturnFromGeneratorTransformer):
        def __init__(self):
            self.generic_visit_node_calls = 0
        def generic_visit(self, node):
            self.generic_visit_node_calls += 1
            return node

    ast_tree = ast.parse("""
    def fn(a):
        yield 1
        yield a
        yield from range(a)
        return a
    """)
    transformer = ReturnFromGeneratorTransformerMock()
    transformer.visit(ast_tree)
    # outputs "[<_ast.ExceptHandler object at 0x000002078F33F5F8>]",
    # or "[]" (depending on Python version)
    print(transformer.generic_visit_node_calls)

    # This is

# Generated at 2022-06-14 02:06:12.669422
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # get correct source and correct target
    source = """
    def foo():
        yield 1
        return 5
    """
    target = """
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    node = ast.parse(source)
    # replace
    transformer = ReturnFromGeneratorTransformer()
    node_replaced = transformer.visit(node)
    assert transformer._tree_changed is True
    # get replaced source
    source_replaced = ast.unparse(node_replaced)

    # compare
    assert source_replaced == target



# Generated at 2022-06-14 02:06:13.319058
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:23.900735
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert ReturnFromGeneratorTransformer(version=3).visit(
        ast.parse("def fn():\n    yield 1\n    return 5\n")) == \
        ast.parse("""def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc""")

    assert ReturnFromGeneratorTransformer(version=3).visit(
        ast.parse("def fn():\n    yield 1\n    return\n")) == \
        ast.parse("def fn():\n    yield 1\n    return")


# Generated at 2022-06-14 02:06:27.056090
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    actual = ReturnFromGeneratorTransformer().visit(TestFixture.generator_return_node)
    expected = TestFixture.generator_return_replaced_node

    assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 02:06:34.561930
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    test_code = """
        def fn1(a):
            yield 0
            return a

        def fn2():
            b = 10
            yield b
            return b

        def fn3(a):
            yield 0
            return a
            return b

        def fn4():
            return a
    """

    expected_code = """
        def fn1(a):
            yield 0
            exc = StopIteration()
            exc.value = a
            raise exc

        def fn2():
            b = 10
            yield b
            exc = StopIteration()
            exc.value = b
            raise exc

        def fn3(a):
            yield 0
            exc = StopIteration()
            exc.value = a
            raise exc
            return b

        def fn4():
            return a
    """
    assert ReturnFrom

# Generated at 2022-06-14 02:06:41.652182
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # setup
    class Node(ast.AST):
        pass
    class Node2(ast.AST):
        pass
    class Attribute(ast.AST):
        value: Node
        attr: str
        ctx: ast.Load
    class Call(ast.AST):
        func: Node
        args: List[Node]
        keywords: List[Any]
    class BinOp(ast.AST):
        left: Node
        op: ast.Add
        right: Node
    class Return(ast.AST):
        value: Node
    class FunctionDef(ast.AST):
        name: str
        body: List[Node]
        decorator_list: List[Node]
        returns: Node
    class Name(ast.AST):
        id: str
        ctx: ast.Load

# Generated at 2022-06-14 02:06:50.054569
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ... import transform
    from ..for_return import ReturnTransformer

    # Before.
    src = """
        import typing

        def fn():
            yield from iter([1, 2])
            return 5
    """
    module, _ = transform(ReturnFromGeneratorTransformer, ReturnTransformer, src)
    assert module is not None

    # After.
    fn = module.body[1]
    assert len(fn.body) == 3
    yield_ = fn.body[0]
    assert isinstance(yield_, ast.Expr)
    assert isinstance(yield_.value, ast.YieldFrom)
    expr = fn.body[1]
    assert isinstance(expr, ast.Expr)
    exc = expr.value
    assert isinstance(exc, ast.Assign)
    value = exc.value

# Generated at 2022-06-14 02:07:01.267519
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Test the method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    @snippet
    def original():
        def fn():
            yield 0
            return None
        def generator():
            yield 1
            if some_condition:
                return 2
            yield 3
        def another_generator():
            return 4

    @snippet
    def expected():
        def fn():
            yield 0
            exc = StopIteration()
            exc.value = None
            raise exc
        def generator():
            yield 1
            if some_condition:
                exc = StopIteration()
                exc.value = 2
                raise exc
            yield 3
        def another_generator():
            return 4

    tree = ast.parse(original.get_body())
    ReturnFromGeneratorTransformer().visit(tree)
   

# Generated at 2022-06-14 02:07:10.151938
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_programs_equal
    from .test_fixes import BaseNodeTransformerTest


# Generated at 2022-06-14 02:07:17.157629
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_source_equal

# Generated at 2022-06-14 02:07:20.008686
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from copy import deepcopy

    # TEST 1

# Generated at 2022-06-14 02:07:32.414754
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    t = ReturnFromGeneratorTransformer()
    def fn1():
        yield 1
        return 3
    def fn2(a):
        yield a
        yield 2
        return 3
    def fn3():
        while True:
            yield 1
            yield 2
            return 3
    def fn4():
        yield 1
        return
    def fn5():
        yield None
        return 3
    def fn6():
        yield 1
        return None
    def fn7():
        yield 1
        return self.a
    def fn8():
        return 3
    def fn9():
        yield 1
        while True:
            yield 2
            return 3
    def fn10():
        yield 1
        try:
            return 3
        except:
            pass
    def fn11():
        yield 1
        return 3
        yield

# Generated at 2022-06-14 02:07:42.402411
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import check
    from ..utils.source_recorder import SourceRecorder

    transformer = ReturnFromGeneratorTransformer()

    s, node = check("""
        def foo():
            yield 1
            return 5
    """)
    node = transformer.visit(node)
    assert transformer._tree_changed is True
    s2, _ = check("""
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)
    assert SourceRecorder.to_source(node) == s2

    transformer = ReturnFromGeneratorTransformer()
    s, node = check("""
        def foo():
            return
    """)
    node = transformer.visit(node)
    assert transformer._tree_changed is False
    assert SourceRecorder

# Generated at 2022-06-14 02:07:54.537328
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:02.271020
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    current_function_name = inspect.currentframe().f_code.co_name
    if current_function_name not in globals():
        pytest.skip("function {} is not defined in test module".format(current_function_name))
    elif not hasattr(globals()[current_function_name], '__annotations__'):
        pytest.skip("function {} has no type annotations".format(current_function_name))
    else:
        function = globals()[current_function_name]
        signature = get_type_hints(function)
        assert signature['return'] == ast.FunctionDef

# Generated at 2022-06-14 02:08:10.741019
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..build import build_ast
    from ..utils.debug import assert_node

    source = '''
    def bar():
        if 1:
            return 1
    '''
    expected = '''
    def bar():
        if 1:
            exc = StopIteration()
            exc.value = 1
            raise exc
    '''
    node = build_ast(source).body[0]
    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(node)

    assert_node(result, expected)

# Generated at 2022-06-14 02:08:17.596513
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    func_def_node = ast.parse("""
        def fn():
            yield 1
            return 5  # this is the only return in any function, nested or not
    """)
    expected = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """

    assert not ReturnFromGeneratorTransformer()._tree_changed
    ReturnFromGeneratorTransformer().visit(func_def_node)

    assert ReturnFromGeneratorTransformer()._tree_changed
    assert ast.dump(func_def_node) == expected  # type: ignore


# Generated at 2022-06-14 02:08:22.784464
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = textwrap.dedent(
        '''
        def fn():
            yield 1
            return 5
        ''')
    expected = textwrap.dedent(
        '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        ''')
    tree = ast.parse(source)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    actual = ast.unparse(tree)

    assert actual == expected



# Generated at 2022-06-14 02:08:29.486749
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    node = ast.parse(
        """def fn():
            yield 1
            return 5""")
    transformer = ReturnFromGeneratorTransformer()
    res = transformer.visit(node)
    assert(astor.to_source(res) == """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc""")

# Generated at 2022-06-14 02:08:42.562914
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(input_code, expected_code):
        src = ast.parse(input_code)
        transformed = ReturnFromGeneratorTransformer().visit(src)
        assert str(transformed) == expected_code

    test('def fn():\n    yield\n    return 1',
         'def fn():\n    yield\n    exc = StopIteration()\n    exc.value = 1\n    raise exc')
    test('def fn():\n    pass', 'def fn():\n    pass')


# Generated at 2022-06-14 02:08:44.184004
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:53.262632
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_case():
        def fn():
            yield 1
            x = yield 2
            return 3

        return fn()

    # test that method visit_FunctionDef transform return in generator to exception raising
    assert next(test_case()) == 1
    assert next(test_case()) == 2
    with pytest.raises(StopIteration) as exc_info:
        next(test_case())
    assert exc_info.value.value == 3



# Generated at 2022-06-14 02:09:03.662185
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Given
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
    # When
    actual_node = ast.parse(source)
    expected_node = ast.parse(expected_source)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(actual_node)
    # Then
    assert transformer._tree_changed is True, \
        "Expected that _tree_changed would be True"
    assert ast.dump(actual_node, include_attributes=True) == ast.dump(expected_node, include_attributes=True), \
        "The nodes differ"


# Generated at 2022-06-14 02:09:05.629783
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:14.994049
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = '''
        def fn():
            yield 1
            return 5
    '''
    expected_code = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''
    tree = ast.parse(code)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    compiled = compile(tree, '', 'exec')

    ns = {}
    exec(compiled, ns)

    assert ns['fn']() == 5



# Generated at 2022-06-14 02:09:22.304214
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.snippet import snippet
    import astor

    @snippet
    def return_in_generator_function(a, b):
        yield a
        return b

    @snippet
    def generator_function():
        yield 1
        yield 2
        yield 3

    @snippet
    def return_in_generator_function_2(a):
        for i in range(10):
            yield i
        return a

    @snippet
    def return_in_generator_function_3(a):
        return a

    @snippet
    def return_in_generator_function_4(a):
        x = 'a'
        yield x

    @snippet
    def return_in_generator_function_5(a):
        yield 'a'
        return

# Generated at 2022-06-14 02:09:23.526391
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:38.531192
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import CompilerError
    from .base import BaseTestTransformer
    
    class Test(BaseTestTransformer):
        transformer = ReturnFromGeneratorTransformer
        filename = __file__
    
        def test_generator_with_return(self, tmpdir):
            self.assert_compilation(
                src='''
                    def generate(iterable):
                        for item in iterable:
                            yield item
                        return 'value'
                ''',
                expected = '''
                    def generate(iterable):
                        for item in iterable:
                            yield item
                        exc = StopIteration()
                        exc.value = 'value'
                        raise exc
                '''
            )
    

# Generated at 2022-06-14 02:09:47.496819
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.ast_toolbox import node_to_str
    from ..utils.snippet import make_snippet
    from .base import BaseNodeTransformer
    from .for_range_to_for_in import ForRangeToForInTransformer
    from .function_arguments import FunctionArgumentsTransformer
    code = """\
    def fn():
        yield 1
        return 5
    def fn2():
        yield 1
        return 5
        return 6
        yield 5
    def fn3():
        if True:
            return 5
        return 6
        yield 5
    """
    tree = ast.parse(code)

# Generated at 2022-06-14 02:10:09.157951
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""
        def fn():
            yield 1
            return 5
    """)
    ReturnFromGeneratorTransformer().visit(tree)
    assert str(tree) == """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """

# Generated at 2022-06-14 02:10:10.147281
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:19.950854
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    sample_python_code = '''
    def foo():
        yield 1
        return 2
    '''
    expected_python_code = '''
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    '''

    input_ast = ast.parse(sample_python_code)
    expected_ast = ast.parse(expected_python_code)

    actual_ast = ReturnFromGeneratorTransformer().visit(input_ast)

    assert ast.dump(actual_ast) == ast.dump(expected_ast)


# Generated at 2022-06-14 02:10:27.145659
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..tests.test_transformer import test_transformer
    from ..utils.get_ast import get_ast
    from ..utils.snippet import snippet

    @snippet
    def before():
        def fn():
            yield 1
            return 5

    @snippet
    def after():
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc

    test_transformer(before, after, [ReturnFromGeneratorTransformer])


# Generated at 2022-06-14 02:10:28.394294
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:31.000671
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:37.444769
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert snippet.test_snippet(
        snippet.compile_snippets(ReturnFromGeneratorTransformer().visit_FunctionDef),
        """
        def fn():
            yield 1
            return 5
        """
    ) == """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """

# Generated at 2022-06-14 02:10:51.003600
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.FunctionDef(name='test', args=ast.arguments(args=[], vararg=[], kwarg=[], defaults=[], kw_defaults=[]),
                           body=ast.stmt([ast.Return(value=ast.Num(n=2))]), decorator_list=[],
                           returns=None)
    transformer = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:11:02.902946
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    function_definition = ast.parse('''
    def fn():
        yield 1
        return 5
    ''')
    expected_return_from_generator = ast.parse('''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    ''')
    expected_non_return_from_generator = ast.parse('''
    def fn():
        return 1
    ''')
    function_definition_no_return_from_generator = ast.parse('''
    def fn():
        return 5
    ''')
    # Test when a generator return a value
    assert ReturnFromGeneratorTransformer().visit(function_definition) == expected_return_from_generator
    # Test when a generator does not returns a value
    assert Return

# Generated at 2022-06-14 02:11:05.003836
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    pass



# Generated at 2022-06-14 02:11:43.243011
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    from ..utils.fakeutils import FakeFileLike
    import typed_ast.ast3 as ast
    from .example_transformer import ExampleTransformer
    import astunparse

    # given

# Generated at 2022-06-14 02:11:54.745810
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:55.865557
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tests = []

# Generated at 2022-06-14 02:11:57.182724
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:09.876762
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        yield 1
        return 5

    tree = ast.parse(inspect.getsource(fn))
    assert tree.body[0].body[1].value.n == 5
    tree = ReturnFromGeneratorTransformer().visit(tree)
    assert len(tree.body[0].body) == 3
    assert isinstance(tree.body[0].body[1], ast.Expr)
    assert isinstance(tree.body[0].body[1].value, ast.Call)
    assert isinstance(tree.body[0].body[1].value.func, ast.Attribute)
    assert tree.body[0].body[1].value.func.attr == 'value'
    assert isinstance(tree.body[0].body[1].value.args[0], ast.Num)

# Generated at 2022-06-14 02:12:11.514084
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:23.564228
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ...tests.testing_utils import run_test_ast_transformer

    code_1 = """def fn():
    yield 1
    return 5
    """

    expected_code_1 = """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc
    """

    code_2 = """def fn():
    yield 1
    yield 4
    return 5
    """

    expected_code_2 = """def fn():
    yield 1
    yield 4
    exc = StopIteration()
    exc.value = 5
    raise exc
    """

    code_3 = """def fn(a):
    yield 1
    for i in a:
        yield 5
        return 6
    """

# Generated at 2022-06-14 02:12:32.433720
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent
    from ..utils.source import source_to_ast

    code = dedent("""\
        def fn():
            yield 1
            yield 3
            yield 4
            return 5
    """)

    expected = dedent("""\
        def fn():
            yield 1
            yield 3
            yield 4
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)

    transformer = ReturnFromGeneratorTransformer()
    assert transformer.transform(source_to_ast(code)) == expected


# Generated at 2022-06-14 02:12:43.530578
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    from ..utils.fake_ast import fake_ast

    class Generator:
        def __init__(self, value):
            self.value = value

        def generator_function(self) -> int:
            yield self.generator_method(1)
            return self.value

        def generator_method(self, x: int) -> int:
            yield self.non_generator(x)
            return self.generator_function()

        def non_generator(self, x: int) -> int:
            return x + 1

    class GaurdedClass:
        def __init__(self, value: int):
            self.value = value

        def is_positive(self) -> bool:
            return self.value > 0


# Generated at 2022-06-14 02:12:45.532345
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import Py2Walker
    from .base import Py2Fixer


# Generated at 2022-06-14 02:14:04.130827
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from ast_helpers import parse_to_funcdef
    # Init
    node_a = parse_to_funcdef("""
    def fn():
        yield 1
        return 5
    """)
    node_b = parse_to_funcdef(astor.to_source(node_a))
    # Run
    node_a = ReturnFromGeneratorTransformer().visit(node_a)
    # Asserts
    assert astor.to_source(node_a) == astor.to_source(node_b)

# Generated at 2022-06-14 02:14:16.765777
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def run_test(test_input, expected_output):
        """
        Helper function to run a single test.
        """
        module_node = ast.parse(test_input)  # type: ignore
        transformer = ReturnFromGeneratorTransformer()
        new_module_node = transformer.visit(module_node)  # type: ignore
        actual_output = ast.unparse(new_module_node)
        assert actual_output.strip() == expected_output.strip()

    def test_generator():
        test_input = """
            def test_generator():
                yield 1
                return 5
        """
        expected_output = """
            def test_generator():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
        """

# Generated at 2022-06-14 02:14:25.757382
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class TestTransformer(ReturnFromGeneratorTransformer):
        pass

    # Generator with return
    node = ast.parse(
        """
        def fn():
            yield 1
            return 5
        """
    ).body[0]
    transformer = TestTransformer()
    transformer.visit(node)
    assert(ast.dump(node) == textwrap.dedent(
        """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """
    ).strip())

    # Generator without return
    node = ast.parse(
        """
        def fn():
            yield 1
        """
    ).body[0]
    transformer = TestTransformer()
    transformer.visit(node)

# Generated at 2022-06-14 02:14:35.504802
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    from .. import transformers  # noqa: F401
    from ..utils.source import Source
    from ..utils.ast_builder import ast_from_string, ast_to_source

    source = Source("""
        def fn():
            1
            def fn2():
                return 6
            2
    """)

    module = ast_from_string(source)

    assert ast_to_source(module) == "def fn():\n    1\n    def fn2():\n        return 6\n    2\n"

    module = ReturnFromGeneratorTransformer().visit(module)
    module = ast.fix_missing_locations(module)


# Generated at 2022-06-14 02:14:42.400578
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('def foo(x):\n    yield x\n    return 5')
    res = ast.dump(ReturnFromGeneratorTransformer().visit(node))
    expected = b'def foo(x):\n    yield x\n    exc = StopIteration()\n    exc.value = 5\n    raise exc'
    assert res == expected


# Generated at 2022-06-14 02:14:58.338482
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTest
    from .remove_parentheses_transformer import RemoveParenthesesTransformer
    from .return_if_comprehension_transformer import ReturnIfComprehensionTransformer
    from .parentheses_to_tuples_transformer import ParenthesesToTuplesTransformer
    from .generators_to_list_comprehensions_transformer import GeneratorsToListComprehensionsTransformer

    class ReturnFromGeneratorTransformerTest(BaseNodeTest):
        target_transformer = ReturnFromGeneratorTransformer(
            targets=[RemoveParenthesesTransformer,
                     ReturnIfComprehensionTransformer,
                     ParenthesesToTuplesTransformer,
                     GeneratorsToListComprehensionsTransformer])
        target_node = ast.FunctionDef
        target_node_class = ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:15:07.124516
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_base import get_test_ast, compare_nodes

    code = """
    def a(x:int):
        def b():
            print("a")
            return 5

        yield 1
        b()
    """
    expected = """
    def a(x : int):
        def b():
            print("a")
            exc = StopIteration()
            exc.value = 5
            raise exc

        yield 1
        b()
    """

    root = get_test_ast(code)
    ReturnFromGeneratorTransformer().visit(root)
    compare_nodes(root, expected)

# Generated at 2022-06-14 02:15:16.908730
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformer
    import unittest
    import sys

    class MyTestCase(unittest.TestCase):
        def assert_transformation_result(self, input_, expected_output):
            actual_output = BaseNodeTransformer._run_transformer(input_, ReturnFromGeneratorTransformer)
            self.assertEqual(actual_output, expected_output)


# Generated at 2022-06-14 02:15:27.820272
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.helper import compare_node, node_to_str

    def gen_test_data(given_code, expect_code):
        # create test data
        root = ast.parse(given_code)
        node = root.body[0]
        expected = ast.parse(expect_code).body[0]
        return root, node, expected

    def test_transform(given_code, expect_code):
        root, node, expected = gen_test_data(given_code, expect_code)
        transformer = ReturnFromGeneratorTransformer()
        new_node = transformer.visit(node)
        compare_node(expected, new_node)
        assert transformer.tree_changed == True


# Generated at 2022-06-14 02:15:39.746812
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..transpile import Transpiler
    from .test_transpiler import get_ast
    from .test_transpiler import make_MockFile
    from .test_transpiler import assert_types

    mock_file = make_MockFile()

    def check(code, expected):
        assert code
        t = Transpiler()
        t.register_transformer(ReturnFromGeneratorTransformer())
        t.register_transformer(assert_types)
        source = get_ast(code)
        new_ast = t.transpile_file(mock_file, source)
        assert expected == new_ast
