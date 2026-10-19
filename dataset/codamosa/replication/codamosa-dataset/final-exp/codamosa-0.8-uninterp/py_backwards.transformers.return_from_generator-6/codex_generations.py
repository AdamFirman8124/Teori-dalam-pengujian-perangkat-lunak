

# Generated at 2022-06-14 02:06:06.592546
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""

    # TODO: implement
    assert False



# Generated at 2022-06-14 02:06:13.671304
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    return_value = ast.parse("42").body[0].value
    source = f"""\
        def fn():
            yield 1
            return {return_value}
    """
    tree = ast.parse(source)
    transformer = ReturnFromGeneratorTransformer()
    tree = transformer.visit(tree)

    expected = f"""\
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = {return_value}
            raise exc
    """
    expected = ast.parse(expected)
    assert tree == expected

# Generated at 2022-06-14 02:06:24.202915
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testutils import source

    def test_case(src: str, expected: str) -> None:
        src = f'{source("")}\n{src}'
        expected = f'{source("")}\n{expected}'
        node = ast.parse(src)
        node = ReturnFromGeneratorTransformer().visit(node)
        assert ast.dump(node) == expected

    # return in generator
    test_case("""
        def fn():
            yield 1
            return 5
        """, """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """)

    # return in generator inside if

# Generated at 2022-06-14 02:06:31.864682
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from mypy_extensions import TypedDict
    import ast as _ast
    from ast_transformer.test_utils import assert_equal_ast

    def transformer(tree: _ast.AST) -> _ast.AST:
        transformer = ReturnFromGeneratorTransformer()
        return transformer.visit(tree)

    code = '''
    def fn():
        yield 1
        return "xyz"
    '''
    expected = '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = "xyz"
        raise exc
    '''
    tree = transformer(ast.parse(code))
    assert_equal_ast(tree, expected)

# Generated at 2022-06-14 02:06:39.824255
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class DummyFunctionDef(ast.FunctionDef):
        fields = ['body']

    class DummyYield(ast.Yield):
        fields = ['value']

    class DummyExpr(ast.Expr):
        fields = ['value']

    class DummyName(ast.Name):
        fields = ['id', 'ctx']

    class DummyLoad(ast.Load):
        fields = []

    class DummyNum(ast.Num):
        fields = ['n']

    class DummyReturn(ast.Return):
        fields = ['value']

    class DummyAssign(ast.Assign):
        fields = ['targets', 'value']

    class DummyAugAssign(ast.AugAssign):
        fields = ['op', 'value']


# Generated at 2022-06-14 02:06:49.777463
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_asts_equal, assert_code_equal
    from ..ast_compare import ast_compare
    from ..utils.source import source

    transformer = ReturnFromGeneratorTransformer()
    func_ast = ast.parse(source('''
        def foo():
            r = 5
            yield r
            return 5
        '''))
    assert_asts_equal(func_ast.body[0], func_ast)
    
    gen = transformer.visit(func_ast)

# Generated at 2022-06-14 02:06:50.408072
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:01.557394
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    ast_module = ast.parse(
        """
        @some_decorator
        def foo():
            def fn():
                yield 1
                return 2

            def fn2():
                return 3

            def fn3():
                return 4
                yield 3

            yield 5

        @some_decorator
        def bar():
            return 6
        """)
    expected_ast_module = ast.parse(
        """
        @some_decorator
        def foo():
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 2
                raise exc

            def fn2():
                return 3

            def fn3():
                return 4
                yield 3

            yield 5

        @some_decorator
        def bar():
            return 6
        """
    )
    expected_source

# Generated at 2022-06-14 02:07:10.432883
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(input_code):
        module_node = ast.parse(input_code)
        transformed_module = ReturnFromGeneratorTransformer().visit(module_code)  # type: ignore
        transformed_code = compile(transformed_module, '<test>', 'exec')
        glob = {}
        exec(transformed_code, glob)
        assert 'fn' in glob
        glob['fn']()

    def test_no_yield(input_code):
        module_node = ast.parse(input_code)
        transformed_module = ReturnFromGeneratorTransformer().visit(module_code)  # type: ignore
        assert ast.dump(transformed_module) == ast.dump(module_node)

    snippet.set_globals('fn', 'generator_fn')

# Generated at 2022-06-14 02:07:12.911485
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    gens = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:07:26.135688
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class TestReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer):
        def __init__(self):
            self._tree_changed = False

    def _create_node(src: str) -> ast.FunctionDef:
        parsed = ast.parse(src)
        fn = parsed.body[0]
        return fn

    # Should not replace return statement
    node = _create_node("""def fn():
        return 1""")
    TestReturnFromGeneratorTransformer().visit(node)
    assert not node.body[0].body

    # Should not replace return statements
    node = _create_node("""def fn():
        return 1
        return 2""")
    TestReturnFromGeneratorTransformer().visit(node)
    assert len(node.body[0].body) == 2

    # Should replace return statement


# Generated at 2022-06-14 02:07:28.636058
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..unittest_tools import assert_code_equal
    from .transforms import StringTransformer


# Generated at 2022-06-14 02:07:41.513438
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..compiler import Compiler

    code = """
    def fn0():
        yield 1
        return 5

    def fn1():
        yield 1
        x = 10
        return x

    def fn2():
        yield 1
        return x

    def fn3():
        yield 1
        if i == 10:
            return x

    def fn4():
        if i == 10:
            return x
        yield 1

    def fn5():
        return x

    def fn6():
        yield 1
        yield 2
    """

    root = ast.parse(code)
    c = Compiler()
    c.visit(root)

    assert root.body[0].body == ["yield 1", "exc = StopIteration()", "exc.value = 5", "raise exc"]

# Generated at 2022-06-14 02:07:55.035862
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformerTests
    suite = BaseNodeTransformerTests
    tester = suite.make_visitor_test(ReturnFromGeneratorTransformer)
    tester.test(
        code='''
        def generator():
            if True:
                return 1
            yield 5
        ''',
        expected='''
        def generator():
            if True:
                _L = StopIteration()
                _L.value = 1
                raise _L
            yield 5
        '''
    )

    tester.test(
        code='''
        def generator():
            yield 1
        ''',
        expected='''
        def generator():
            yield 1
        '''
    )


# Generated at 2022-06-14 02:08:04.786389
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    def test_it_replaces_return_with_exception():
        source = inspect.cleandoc("""
        def fn():
            if True:
                return
        """)
        tree = ast.parse(source)

        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(tree)

        # checks if StopIteration exception is raised
        assert isinstance(tree.body[0].body[0].body[0].body[0].body[0], ast.Raise)
        exc = tree.body[0].body[0].body[0].body[0].body[0].exc
        assert isinstance(exc, ast.Call)
        func = exc.func
        assert isinstance(func, ast.Name)
        assert func.id == 'StopIteration'
        value = tree.body[0].body

# Generated at 2022-06-14 02:08:13.620344
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    module = ast.parse(
        """
        def fn():
            yield 1
            return 5

        def fn2():
            yield 1
            yield 2
            return 5

        def fn3():
            for i in range(10):
                yield i
            return 10

        def fn4():
            yield from []
            return 10

        def fn5():
            if 1:
                return 5
            yield 1


        def fn6():
            return 5

        """
    )
    fn = module.body[0]
    fn2 = module.body[1]
    fn3 = module.body[2]
    fn4 = module.body[3]
    fn5 = module.body[4]
    fn6 = module.body[5]
    fn.body = node_to_str_list(fn.body)


# Generated at 2022-06-14 02:08:18.210247
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from . import ast3 as ast3module


# Generated at 2022-06-14 02:08:30.417982
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse
    from unittest.mock import Mock

    class Test:
        pass

    # Test function with yields
    node_1 = parse("""
    def fn():
        yield 1
        return 5
    """)
    node_1.body[0].args = []
    transformer = ReturnFromGeneratorTransformer()
    transformer._tree_changed = False
    node_1_transformed = transformer.visit(node_1)
    assert node_1_transformed is None
    assert transformer._tree_changed is True
    assert node_1_transformed is None
    assert [x.__class__ for x in node_1.body] == [ast.Expr, ast.Assign, ast.Assign, ast.Raise]

# Generated at 2022-06-14 02:08:36.597910
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    src = '''
        def a():
            yield 1
            return 5
    '''

    t = ReturnFromGeneratorTransformer(src)
    transformed_tree = t.visit(t.tree)

    expected_result = '''
        def a():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''

    assert expected_result == astor.to_source(transformed_tree).strip()



# Generated at 2022-06-14 02:08:37.987352
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..testing import run_local_tests
    run_local_tests()

# Generated at 2022-06-14 02:08:54.703095
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # This is an example of a function that returns in a generator function
    def fn():
        yield 1
        return 5

    function_def_node = ast.parse(inspect.getsource(fn)).body[0]  # type: ignore

    rfgt = ReturnFromGeneratorTransformer()
    rfgt.visit(function_def_node)

    assert(str(function_def_node) == (
        "def fn():\n"
        "    yield 1\n"
        "    exc = StopIteration()\n"
        "    exc.value = 5\n"
        "    raise exc\n"
    ))

    # This is an example of a function that returns in a non-generator function
    def fn():
        return 5


# Generated at 2022-06-14 02:09:01.793204
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

    @snippet
    def test_fn():
        yield 1
        return 5

    result = transformer.run_pipeline(test_fn.get_tree())

    @snippet
    def expected_fn():
        yield 1
        let(exc)
        exc = StopIteration()
        exc.value = 5
        raise exc

    assert result == expected_fn.get_tree()

# Generated at 2022-06-14 02:09:08.448645
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import typed_ast.ast3 as ast
    import astor
    new_code = ReturnFromGeneratorTransformer().visit(
        ast.parse("""
        def fn():
            yield 1
            return 5
    """)
    )
    assert astor.to_source(new_code) == """\
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """

# Generated at 2022-06-14 02:09:20.537778
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Testcase 1: Non-empty generator
    test_codenode1 = ast.FunctionDef(
        name='fn',
        body=[
            ast.Yield(
                value=ast.Num(n=1)
            ),
            ast.Return(
                value=ast.Num(n=5)
            )
        ]
    )
    test_node1 = ReturnFromGeneratorTransformer()
    test_codenode1 = test_node1.visit(test_codenode1)

# Generated at 2022-06-14 02:09:22.448785
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:32.233395
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.snippet import source
    from ..unittest_tools import assert_curr_op_equal

    node = ast.parse(source(
        '''
        def fn():
            yield 1
            return 5
        '''
    ))
    transformer = ReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)
    expected_node = ast.parse(source(
        '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        '''
    ))
    assert_curr_op_equal(new_node, expected_node)

# Generated at 2022-06-14 02:09:44.069276
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def start_end_lineno(node: ast.AST) -> Tuple[int, int]:
        """Compute starting and ending line number."""
        lineno = node.lineno
        if isinstance(node, ast.FunctionDef):
            lineno = node.body[-1].lineno
        elif isinstance(node, ast.If):
            lineno = node.orelse[-1].lineno
        return lineno, node.end_lineno

    import astor  # type: ignore
    from itertools import count


# Generated at 2022-06-14 02:09:46.560500
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""

# Generated at 2022-06-14 02:09:57.037563
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .helper_visitor import _test_visit
    class TestVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            node.body = []

    test_code = """
    def fn():
        yield 1
        return 5
    """

    expected_code = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    _test_visit(test_code, expected_code, ReturnFromGeneratorTransformer, TestVisitor)


# Generated at 2022-06-14 02:10:06.500663
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..refactor import RefactoringTool
    from .base import get_refactored_code

    tool = RefactoringTool(['-w', '-'])
    transformer = ReturnFromGeneratorTransformer()

    for input, output in get_refactored_code(transformer, 'transformers.return_from_generator'):
        tree = tool.refactor_string(input, transformer.__class__.__name__)
        output = tool.refactor_string(output, transformer.__class__.__name__)

        assert tree == output



# Generated at 2022-06-14 02:10:17.933824
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Setup
    code_str = "def fn():\n    yield 1\n    return 5"
    node = ast.parse(code_str).body[0]
    node = node.body[1]
    t = ReturnFromGeneratorTransformer()

    # Exercise
    node = t.visit_FunctionDef(node)

    # Verify
    expected_code_str = "def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc"
    assert ast.dump(node) == expected_code_str


# Generated at 2022-06-14 02:10:20.555824
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def get_test_ast(code):
        print(code)
        return ast.parse(code)

    def check_return_from_generator(code, expected_code):
        transform = ReturnFromGeneratorTransformer()
        node = transform.visit(get_test_ast(code))
        print(code, expected_code)
        print(ast.dump(node))
        assert ast.dump(node) == expected_code


# Generated at 2022-06-14 02:10:25.487676
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
    def foo():
        def bar():
            yield 'a'
            return 42
        return bar()
    """
    tree = ast.parse(code)
    t = ReturnFromGeneratorTransformer()
    tree = t.visit(tree)

# Generated at 2022-06-14 02:10:30.295578
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert ReturnFromGeneratorTransformer().visit(ast.parse("def fn():\n    yield 1\n    return 5\n")) == ast.parse("def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc\n")

# Generated at 2022-06-14 02:10:42.134298
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # this test can fail if you change the code under tests
    source_code = '''
        def fn():
            yield 1
            return 5

        def fn2():
            yield 1
            return

        def fn3():
            return 5

        def fn4():
            return
    '''

    target_code = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        def fn2():
            yield 1
            return
        def fn3():
            return 5
        def fn4():
            return
    '''
    module = ast.parse(source_code)
    ReturnFromGeneratorTransformer().visit(module)
    assert ast.dump(module) == target_code

# Generated at 2022-06-14 02:10:52.391194
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.ast import ast_to_src

    def make_module(src):
        return ast.parse(src)

    src = """
    def fn():
        yield 11
        return 13
    """
    expected = """
    def fn():
        yield 11
        exc = StopIteration()
        exc.value = 13
        raise exc
    """
    node = make_module(src)
    ReturnFromGeneratorTransformer().visit(node)
    result = ast_to_src(node)
    print(result)
    assert result == expected

    src = """
    def fn():
        yield 11
        for i in range(10):
            yield i
        return 13
    """

# Generated at 2022-06-14 02:10:53.669774
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:00.344716
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    input_code = """
        def fn():
            yield 1
            return 5
    """

    expected_code = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """

    tree = ast.parse(input_code)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    output_code = astor.to_source(tree)

    assert output_code == expected_code



# Generated at 2022-06-14 02:11:08.335459
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import test_utils
    from typed_ast import ast3 as ast

    source = "def fn():\n\tyield 1\n\treturn 2"
    expected_source = "def fn():\n\tyield 1\nexc = StopIteration()\nexc.value = 2\nraise exc"

    expected_ast = test_utils.build_ast(expected_source)
    actual_ast = test_utils.build_ast(source, transformers=ReturnFromGeneratorTransformer)

    assert ast.dump(expected_ast) == ast.dump(actual_ast)


# Generated at 2022-06-14 02:11:15.556915
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
        def fn():
            yield 5
            return 4
    """
    expected_code = """
        def fn():
            yield 5
            exc = StopIteration()
            exc.value = 4
            raise exc
    """
    tree = ast.parse(code)
    ReturnFromGeneratorTransformer().visit(tree)
    assert astor.to_source(tree) == expected_code



# Generated at 2022-06-14 02:11:37.537485
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import compile
    code = """
    def fn():
        yield 1
        yield 2
        return 5
    def not_generator():
        return 5
    """

    expected = """
    def fn():
        yield 1
        yield 2
        exc = StopIteration()
        exc.value = 5
        raise exc
    def not_generator():
        return 5
    """

    ast_ = compile(code, '<stdin>', 'exec')
    assert str(ast_) == expected

# Generated at 2022-06-14 02:11:51.578921
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert_equal = partial(assert_equals,
                           node1_transformer=ReturnFromGeneratorTransformer)

    assert_equal('''
        def fn(x): pass
    ''', '''
        def fn(x): pass
    ''')

    assert_equal('''
        def fn(x):
            return x
    ''', '''
        def fn(x):
            return x
    ''')

    assert_equal('''
        def fn():
            x = 5
            return x
    ''', '''
        def fn():
            x = 5
            exc = StopIteration()
            exc.value = x
            raise exc
    ''')


# Generated at 2022-06-14 02:11:55.382078
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    ast.parse = lambda code: ast.parse(code).body[0]
    test_transformer = ReturnFromGeneratorTransformer()
    def test(code, expected):
        node = ast.parse(code)
        test_transformer.visit(node)
        assert ast.dump(node, 'exec') == expected


# Generated at 2022-06-14 02:11:56.098518
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:01.402537
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    x = f"""
        def fn():
            yield 1
            return 5
    """
    # Load the code and expect to find a return statement
    loader = Loader(x)
    module = loader.load_module(x)
    fn = getattr(module, 'fn')
    assert isinstance(fn, types.FunctionType)

    # Transform with ReturnFromGeneratorTransformer, expect to find yield
    transformer = ReturnFromGeneratorTransformer()
    module = transformer.visit(module)
    fn = getattr(module, 'fn')
    assert isinstance(fn, types.GeneratorType)

    # Run the generator, it should raise StopIteration exception
    with pytest.raises(StopIteration):
        fn()

    # Now test a function that doesn't yield, so should not be modified

# Generated at 2022-06-14 02:12:12.851596
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer"""
    transformer = ReturnFromGeneratorTransformer()
    assert isinstance(transformer, ReturnFromGeneratorTransformer)

    code = """
        def foo():
            yield 1
            return 0
    """
    tree = ast.parse(code)
    expected_code = """
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 0
            raise exc
    """
    assert transformer.visit(tree) == ast.parse(expected_code)

    code = """
        def foo():
            return 0
    """
    tree = ast.parse(code)
    assert transformer.visit(tree) == tree

    code = """
        def foo(bar):
            yield bar
            return bar
    """
    tree

# Generated at 2022-06-14 02:12:15.959121
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def run(source: str) -> None:
        tree = ast.parse(source)
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(tree)
        print(ast.unparse(tree))


# Generated at 2022-06-14 02:12:23.747840
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    no_changes = ast.FunctionDef(
        name='fn',
        args=ast.arguments(
            args=[],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[
            ast.Expr(
                value=ast.Yield(
                    value=ast.Num(n=1)
                )
            ),
            ast.Return(
                value=None
            )
        ],
        decorator_list=[],
        returns=None
    )


# Generated at 2022-06-14 02:12:34.526097
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import unittest
    from ..utils.helpers import get_node

    class ReturnFromGeneratorTransformerTestCase(unittest.TestCase):
        def _test_case(self, before: str, after: str) -> None:
            result = get_node(after)
            ReturnFromGeneratorTransformer().visit(get_node(before))
            self.assertEqual(result, get_node(before))

        def test_return_from_generator__return_none(self):
            self._test_case(
                """
                def fn():
                    yield 1
                    return
                """,
                """
                def fn():
                    yield 1
                    return
                """
            )


# Generated at 2022-06-14 02:12:37.052874
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:13.189178
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        yield 1
        return 5

    cls = ReturnFromGeneratorTransformer()
    ret = cls.visit_FunctionDef(ast.parse(inspect.getsource(fn)).body[0])
    assert ret.body[1].value.func.value.id == 'StopIteration'

# Generated at 2022-06-14 02:13:20.305118
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:31.917987
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..parse_tree import parse
    from ..byte_code import compile_ast_to_code

    def check(before, after):
        before = parse(before)
        after = parse(after)
        assert compile_ast_to_code(ReturnFromGeneratorTransformer.run(before)) == \
            compile_ast_to_code(after)

    check('def a(): return', 'def a(): pass')
    check('def a(): yield; return', 'def a(): pass')
    check('def a(): yield; return 1', 'def a(): pass')
    check('def a(): yield 1; return 1', '''def a():
    yield 1
    exc = StopIteration()
    exc.value = 1
    raise exc''')

# Generated at 2022-06-14 02:13:38.313468
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3
    from .. import transforms

    tree = ast3.parse('def fn(): yield 1; return 5')
    transform = transforms.ReturnFromGeneratorTransformer()
    exp_tree = ast3.parse('''
    def fn():
        yield 1
        let(exc)
        exc = StopIteration()
        exc.value = 5
        raise exc
    ''')

    tree = transform.visit(tree)
    assert ast3.dump(tree) == ast3.dump(exp_tree)

# Generated at 2022-06-14 02:13:42.024759
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import auto_test_pickles

    auto_test_pickles(ReturnFromGeneratorTransformer(), """
        def fn():
            yield 1
            return 5

        def fn2():
            yield from range(5)
            x = 5; return x

        def fn3():
            for i in range(5):
                yield i
            return
        """)

# Generated at 2022-06-14 02:13:52.943531
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    from .base import BaseNodeTransformerTestCase
    from .noop_transformer import NoopTransformer
    from .for_in_transformer import ForInTransformer
    from .function_call_transformer import FunctionCallTransformer

    class ReturnFromGeneratorTransformerTestCase(
        BaseNodeTransformerTestCase[ReturnFromGeneratorTransformer]
    ):
        transformer = ReturnFromGeneratorTransformer


# Generated at 2022-06-14 02:14:02.553729
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testing import check_in, check_not_in
    from ..utils.source import source_to_tree, tree_to_source
    source = '''
    def fn():
        yield 1
        return 4
    '''
    node1 = source_to_tree(source, version='3.2')
    node2 = ReturnFromGeneratorTransformer().visit(node1)
    source_after = tree_to_source(node2)

    check_in('''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 4
        raise exc
    ''', source_after)
    check_not_in('return 4', source_after)



# Generated at 2022-06-14 02:14:06.885167
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse
    from test_transformer import dump
    from .compiler import EmitContext, Compiler


# Generated at 2022-06-14 02:14:13.681577
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import typed_python._types as _types
    import typed_astunparse
    code = '''
            def fn():
                yield 1
                return 5
    '''
    tree = ast.parse(code)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    assert typed_astunparse.unparse(tree) == "def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc\n"
    assert tree.body[0].body[1].value.func.id == 'StopIteration'
    assert tree.body[0].body[2].value.elts[0].id == 'exc'
    assert _types.Function(_types.NoneType).getTypeOf(tree) == _types.NoneType

# Generated at 2022-06-14 02:14:24.564784
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    transformer = ReturnFromGeneratorTransformer()
    def f():
        yield 1
        return 5
    node = ast.parse(f)[0]
    transformer.visit(node)

# Generated at 2022-06-14 02:15:40.489302
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
    def fn():
        yield 1
        return 5
    """
    expected_code = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    tree = ast.parse(code)
    expected_tree = ast.parse(expected_code)
    transformer = ReturnFromGeneratorTransformer()
    tree = transformer.visit(tree)
    # check if transformer changed code at all
    assert transformer._tree_changed
    assert ast.dump(tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:15:42.971107
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import inspect
    from ..compiler import thrifty

    def fn():
        yield 1
        return 5


# Generated at 2022-06-14 02:15:53.339296
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Case 1: default
    node = ast.parse("""
        def fn():
            yield 1
            return 5
    """).body[0]  # type: ignore
    expected = ast.parse("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """).body[0]  # type: ignore
    actual = ReturnFromGeneratorTransformer().visit(node)
    assert actual == expected

    # Case 2: with other statements in body
    node = ast.parse("""
        def fn():
            yield 1
            print(1)
            return 5
    """).body[0]  # type: ignore

# Generated at 2022-06-14 02:16:00.591773
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse
    import tempfile
    import os

    test = '''
    def foo():
        yield 1
        return 8
    '''
    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(os.path.join(tmpdirname, 'test.py'), 'wt') as tmp:
            tmp.write(test)
        tree = ast.parse(test)
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(tree)
        assert astunparse.dump(tree) == astunparse.dump(ast.parse(str(
            return_from_generator.snippet)))

