

# Generated at 2022-06-14 02:06:17.008794
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # type: () -> None
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer"""

    node = ast.parse('def my_fn(): yield 1; return 5')
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)
    assert_source_equal(node, 'def my_fn(): yield 1; exc = StopIteration(); exc.value = 5; raise exc')

    node = ast.parse('def my_fn(): yield from range(10); return 5')
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)
    assert_source_equal(node, 'def my_fn(): yield from range(10); exc = StopIteration(); exc.value = 5; raise exc')


# Generated at 2022-06-14 02:06:18.097209
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:25.668772
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    src = """
    def fn():
        yield 1
        return 5
    """

    for line in src.splitlines():
        print(line)

    tree = ast.parse(src)
    ReturnFromGeneratorTransformer().visit(tree)

    expected = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    for line in expected.splitlines():
        print(line)

    expected_tree = ast.parse(expected)

    assert ast.dump(tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:06:30.178108
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:38.752285
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse

    def get_tree(code, *args, **kwargs):
        tree = parse(code, *args, **kwargs)
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(tree)
        return tree

    assert get_tree('1').body[0].n == 1

    expr1 = get_tree('return 1')
    assert isinstance(expr1.body[0], ast.Expr)
    assert isinstance(expr1.body[0].value, ast.Call)
    assert isinstance(expr1.body[0].value.func, ast.Name)
    assert expr1.body[0].value.func.id == 'StopIteration'


# Generated at 2022-06-14 02:06:49.344975
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # import ast
    from typed_ast import ast3 as ast
    from textwrap import dedent
    from . import BaseNodeTransformer
    from .return_from_generator import ReturnFromGeneratorTransformer
    # Test for no return statements
    def test_no_return():
        class Test1(BaseNodeTransformer):
            def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
                return ReturnFromGeneratorTransformer().visit_FunctionDef(node)

        node = ast.parse(dedent('''
            def fn():
                yield 1
                yield 2
        '''))
        node = Test1().visit(node)


# Generated at 2022-06-14 02:06:52.537688
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..compile_to_ast import compile_to_ast
    from ..module_visitor import ModuleTransformer, get_code
    from ..config import Config


# Generated at 2022-06-14 02:07:06.120691
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:16.028955
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('def fn(): yield 1; return 5')
    fn = node.body[0]
    assert isinstance(fn, ast.FunctionDef)

    rfg = ReturnFromGeneratorTransformer()
    new_fn = rfg.visit(fn)

    expected = """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc"""
    assert new_fn is not fn
    assert ast.dump(ast.Module([new_fn])) == expected

# Generated at 2022-06-14 02:07:31.263358
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """g = (x for x in range(1, 10))"""
    ast_code = ast.parse(code)
    node_transformer = ReturnFromGeneratorTransformer()
    node_transformer.visit(ast_code)
    assert ast.dump(ast_code) == "Module(body=[Assign(targets=[Name(id='g', ctx=Store())], value=GeneratorExp(elt=Name(id='x', ctx=Load()), generators=[comprehension(target=Name(id='x', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Num(n=1), Num(n=10)], keywords=[]), ifs=[], is_async=0)]))])"


# Generated at 2022-06-14 02:07:38.081447
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:45.638634
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def check(s: str, expected: str) -> None:
        node = ast.parse(s)
        node = ReturnFromGeneratorTransformer().visit(node)
        print(node)
        assert ast.dump(node, include_attributes=False) == ast.dump(ast.parse(expected), include_attributes=False)

    check(
        'def fn():\n    yield 1\n    return 5',
        'def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc'
    )

# Generated at 2022-06-14 02:07:57.467140
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    #
    # def fn():
    #     yield 1
    #     return 5
    #
    # to:
    #
    # def fn():
    #     yield 1
    #     exc = StopIteration()
    #     exc.value = 5
    #     raise exc
    #
    def fn():
        yield 1
        return 5

    node = ast.parse(fn.__code__)  # type: ignore
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)
    exec(compile(node, filename="<ast>", mode='exec'), globals())

    assert fn().send(None) == 1
    with pytest.raises(StopIteration) as excinfo:
        fn().send(None)

    assert excinfo.value.value == 5

# Generated at 2022-06-14 02:08:06.067140
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('''
    def childFunction():
        return 1

    def parentFunction():
        if x:
            y = childFunction()
        else:
            return 3
    ''')

    expected = ast.parse('''
    def childFunction():
        exc = StopIteration()
        exc.value = 1
        raise exc    

    def parentFunction():
        if x:
            y = childFunction()
        else:
            exc = StopIteration()
            exc.value = 3
            raise exc
    ''')
    transformer = ReturnFromGeneratorTransformer()
    result = transformer.visit(node)
    assert ast.dump(result) == ast.dump(expected)

# Generated at 2022-06-14 02:08:13.161084
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert ReturnFromGeneratorTransformer().visit_FunctionDef(
        ast.parse("""
            def fn():
                yield 1
                if True:
                    yield 2
                    return 5
                return 6
        """).body[0]
    ).body[-1].body == [
            let(exc),
            exc.assign(ast.Call(func=ast.Name(id='StopIteration', ctx=ast.Load()), args=[], keywords=[])),
            exc.attr('value').assign(ast.Num(n=5)),
            ast.Raise(exc=exc, cause=None)
    ]



# Generated at 2022-06-14 02:08:23.257434
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test 1
    node = ast.parse("""
    def fn():
        yield 1
        return 5
    """).body[0]
    expected = ast.parse("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """).body[0]

    gen_transformer = ReturnFromGeneratorTransformer()
    new_node = gen_transformer.visit(node)

    assert ast.dump(new_node) == ast.dump(expected)



# Generated at 2022-06-14 02:08:32.209876
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.test import assert_code_equal

    node = ast.parse('''
        def fn(a):
            yield 1
            return a
    ''')

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)

    assert_code_equal('''
        def fn(a):
            yield 1
            exc = StopIteration()
            exc.value = a
            raise exc
    ''', transformer.dump_tree(node))


# Generated at 2022-06-14 02:08:39.897718
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.fixtures import basic_generator_with_return

    transformer = ReturnFromGeneratorTransformer()
    new_tree = transformer.visit(basic_generator_with_return)

    assert transformer._tree_changed is True
    assert transformer._num_of_nodes_visited > 0

    import astor

    print(astor.to_source(new_tree))

# Generated at 2022-06-14 02:08:54.218671
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tr = ReturnFromGeneratorTransformer()

    func_def_node = ast.parse('def fn():\n    return 1')
    fn_node = func_def_node.body[0]
    assert fn_node.name == 'fn'
    assert isinstance(fn_node.body[0], ast.Return)
    assert fn_node.body[0].value.n == 1
    assert fn_node.body[0].value.lineno == 2
    assert fn_node.body[0].value.col_offset == 4

    tr.visit(func_def_node)
    assert fn_node.name == 'fn'
    assert isinstance(fn_node.body[0], ast.Assign)
    assert fn_node.body[0].targets[0].id == 'exc'
    assert fn_

# Generated at 2022-06-14 02:09:03.454191
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformerTest
    from .to_py34 import ToPy34Transformer
    from .to_py38 import ToPy38Transformer
    from .remove_arguments import RemoveArgumentsTransformer

    class Test(BaseNodeTransformerTest):
        target = (3, 8)
        transformers = ToPy34Transformer, ToPy38Transformer, RemoveArgumentsTransformer, ReturnFromGeneratorTransformer
        code = '''
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

    Test.run()

# Generated at 2022-06-14 02:09:20.606562
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
    def fn():
        yield 1
        return 5
    """
    tree = ast.parse(code)
    ret_transformer = ReturnFromGeneratorTransformer()
    new_tree = ret_transformer.visit(tree)
    compiled_code = ret_transformer.compile(new_tree)

    assert 'def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc' == compiled_code, compiled_code


# Generated at 2022-06-14 02:09:33.539365
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    tree = ast.parse("""
        def fn(x):
            def inner():
                yield 1
                yield x
                return 'z'

            return inner()

        def fn2(x):
            yield 1
            return 5
    """)
    new_tree = transformer.visit(tree)

    assert transformer._tree_changed

# Generated at 2022-06-14 02:09:45.281866
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source_code = '''
        def fn():
            yield 1
            return 5
    '''
    source_ast = ast.parse(source_code)
    source_ast.body[0].body[1].value.n = 5
    result_ast = ReturnFromGeneratorTransformer().visit_FunctionDef(source_ast.body[0])

# Generated at 2022-06-14 02:09:49.017795
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def check_result(body, expected_lines):
        transformer = ReturnFromGeneratorTransformer()
        node = ast.parse(body)
        transformer.visit(node)
        lines = [line.strip() for line in ast.dump(node).splitlines()]
        assert lines[2:] == expected_lines


# Generated at 2022-06-14 02:09:53.013470
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import TreeChecker
    from ..utils.ast_builder import ast_from, build

    # Given

# Generated at 2022-06-14 02:09:59.877409
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('def foo():\n    yield 1\n    yield 2\n    return 3')
    assert str(node) == 'def foo():\n    yield 1\n    yield 2\n    return 3'
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)
    assert str(node) == 'def foo():\n    yield 1\n    yield 2\n    exc = StopIteration()\n    exc.value = 3\n    raise exc'
    print('test_ReturnFromGeneratorTransformer_visit_FunctionDef PASSED')

# Generated at 2022-06-14 02:10:11.778479
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import pytest
    from ..utils.source import source_to_func
    from ..visitors.walker import Walker

    source = """
    def fn():
        if a:
            return 5

        yield from b()
        return 7
    """
    expect = """
    def fn():
        if a:
            exc = StopIteration()
            exc.value = 5
            raise exc

        yield from b()
        exc = StopIteration()
        exc.value = 7
        raise exc
    """
    node = source_to_func(source)
    result = Walker(node, [ReturnFromGeneratorTransformer]).result
    assert ast.dump(result) == ast.dump(source_to_func(expect))

    source = """
    def fn():
        return 5
    """

# Generated at 2022-06-14 02:10:23.538929
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    code = """
    def test():
        yield 1
        return 5
    """

    desired_code = """
    def test():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    node = ast.parse(code)
    my_transformer = ReturnFromGeneratorTransformer()
    new_node = my_transformer.visit(node)

    # The tree should be modified
    assert my_transformer.tree_changed() == True
    # The new code should be the expected one
    assert astunparse.unparse(new_node) == desired_code

# Generated at 2022-06-14 02:10:26.876718
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ...utils.ast_format import generic_ast_node_to_str
    from ..utils import build_ast

# Generated at 2022-06-14 02:10:36.178412
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from darglint.transformer_utils import get_node_as_string
    from darglint.config import load_config
    config = load_config()

    block = """\
        def fn():
            yield 1
            return 5
        """
    expected = """\
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """
    transformer = ReturnFromGeneratorTransformer(config)
    node = transformer.visit(ast.parse(block))
    result = get_node_as_string(node)
    assert result == expected

    block = """\
        def fn():
            yield 1
            if 3:
                return 5
        """

# Generated at 2022-06-14 02:11:00.293944
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.tester import AssertEqualMixin
    from ..utils.tester import make_fixtures

    class Tester(AssertEqualMixin):
        transformer = ReturnFromGeneratorTransformer()
        fixtures = make_fixtures('fn')

        def _test(self, node: ast.FunctionDef) -> None:
            self.transformer.visit(node)
            self.assertEqual(node, self.fixtures.fn('expected'))
    Tester().run()

# Generated at 2022-06-14 02:11:11.065556
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class MockAST(ast.AST):
        def __init__(self, parent, value=None):
            self.parent = parent
            self.body = []
            self.value = value
            self.index = 0
            self.level = 0 if isinstance(parent, MockAST) else 1
            self.return_value = parent.return_value if isinstance(parent, MockAST) else value

            if isinstance(parent, MockAST):
                parent.body.append(self)

        def __repr__(self):
            return '<%s %d - %d>' % (self.__class__.__name__, self.level, self.index)

    class MockExpr(ast.AST):
        pass

    class MockExprContext(ast.AST):
        pass


# Generated at 2022-06-14 02:11:22.078674
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    for v in range(2, 6):
        code = '''
        def fn():
            yield 1
            return 5
        '''

        tree = ast.parse(code)
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(tree)

        expected = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        '''

        got = astor.to_source(transformer.tree)
        print('\n')
        print(f'Version: {v}' + '\n' + '_' * 10)
        print('expected:')
        print(astor.to_source(ast.parse(expected)))
        print('\n')
        print('got:')
        print(got)

# Generated at 2022-06-14 02:11:33.286800
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Test(unittest.TestCase):
        def test(self):
            fn = ast.parse("""
                def fn():
                    for x in [1, 2, 3]:
                        yield 1
                    return 5
            """)
            expected = ast.parse("""
                def fn():
                    for x in [1, 2, 3]:
                        yield 1
                    exc = StopIteration()
                    exc.value = 5
                    raise exc
            """)
            node = fn.body[0]
            node = ReturnFromGeneratorTransformer().visit(node)
            self.assertEqual(expected.body[0], node)

    test = Test()
    test.test()

# Generated at 2022-06-14 02:11:43.761689
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class TestReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer):
        def __init__(self):
            self.__is_method_visit_FunctionDef_called = False

        def visit_FunctionDef(self, node):
            self.__is_method_visit_FunctionDef_called = True
            return node

        def is_method_visit_FunctionDef_called(self):
            return self.__is_method_visit_FunctionDef_called

    coding = 'def fn():\n    yield 1\n    return 5\n'
    expected_coding = 'def fn():\n    yield 1\n    exc = StopIteration()\n    '\
                      'exc.value = 5\n    raise exc\n'
    tree = ast.parse(coding)

    tester = TestReturnFromGener

# Generated at 2022-06-14 02:11:54.996150
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse
    module = parse('''
    def fn(x):
        if x:
            return 1
        while True:
            yield 2
            if x:
                return 3
        yield 4
        return 5
    ''')

    class FakeModule(ast.Module):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.body = [module]

    transformer = ReturnFromGeneratorTransformer()
    module = transformer.visit(FakeModule())

    fn = module.body[0]
    assert fn.name == 'fn'

    assert isinstance(fn.body[0], ast.If)
    assert isinstance(fn.body[1], ast.While)

# Generated at 2022-06-14 02:12:03.755808
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # type: () -> None
    from .test_base import compile_to_ast
    from ..utils.asserts import assert_code_equal

    source = """
    def foo():
        yield 1
        return 2
    """
    expected = """
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """

    node = compile_to_ast(source)
    ReturnFromGeneratorTransformer().visit(node)

    assert_code_equal(node, expected)

# Generated at 2022-06-14 02:12:08.966832
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    f = ast.parse('def fn(): yield 1; return 5').body[0]  # type: ignore
    expected = ast.parse('def fn(): yield 1; exc = StopIteration(); exc.value = 5; raise exc').body[0]  # type: ignore
    assert ReturnFromGeneratorTransformer().visit(f) == expected


# Generated at 2022-06-14 02:12:18.348119
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:19.961557
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:12:52.794586
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    # Generating input parameters

    # module_ast_node = Module(body=[])
    module_ast_node = ast.parse("\n")
    module_ast_node = module_ast_node.body[0]

    # class_def_node = ClassDef(name='Class', bases=[], keywords=[],
    #                           body=[], decorator_list=[])
    class_def_node = ast.parse("\n")
    class_def_node = class_def_node.body[0]

    # func_def_node = FunctionDef(name='func', args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[],
    #                                                         kwarg=None, defaults=[]), body=[Expr(value=Str(s='\n    ')),
    #

# Generated at 2022-06-14 02:13:00.598670
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    module, _ = parse("""def foo(x):
        yield x
        return 1""")

    assert len(module.body) == 1
    fn = module.body[0]
    assert isinstance(fn, ast.FunctionDef)
    assert fn.name == "foo"
    assert len(fn.body) == 3
    assert isinstance(fn.body[1], ast.Yield)
    assert isinstance(fn.body[2], ast.Return)
    assert fn.body[2].value.n == 1

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(module)

    assert transformer._tree_changed
    assert len(transformer._errors) == 0

    assert len(fn.body) == 5
    assert isinstance(fn.body[1], ast.Yield)

# Generated at 2022-06-14 02:13:13.189961
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # return in generator
    class TestReturnFromGeneratorTransformerVisitFunctionDef:
        def foo():
            yield 1
            return 5

    source = ast.dump(ast.parse(dedent(
        TestReturnFromGeneratorTransformerVisitFunctionDef.foo.__doc__
    )), annotate_fields=False, include_attributes=True)
    expected = ast.dump(ast.parse(dedent(
        """
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """
    )), annotate_fields=False, include_attributes=True)

    transformer = ReturnFromGeneratorTransformer()
    new_tree = transformer.visit(ast.parse(source))

# Generated at 2022-06-14 02:13:26.014797
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Original return
    node = ast.FunctionDef(name='fn', args=ast.arguments(
        args=[],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[],
    ), body=[
        ast.Yield(value=ast.Num(n=1)),
        ast.Return(value=ast.Name(id='a', ctx=ast.Load()))
    ], decorator_list=[], returns=None)

    # Transformed return

# Generated at 2022-06-14 02:13:35.013550
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    # Test case with no return nodes
    f = ast.parse(textwrap.dedent("""\
        def f():
            pass
        """))
    assert ReturnFromGeneratorTransformer().visit(f).body[0].name == 'f'

    # Test case with no return nodes in a generator
    f = ast.parse(textwrap.dedent("""\
        def f():
            yield 1
        """))
    assert ReturnFromGeneratorTransformer().visit(f).body[0].name == 'f'

    # Test case with no return nodes in a function
    f = ast.parse(textwrap.dedent("""\
        def f():
            return
        """))
    assert ReturnFromGeneratorTransformer().visit(f).body[0].name == 'f'

    # Test case with no return nodes in

# Generated at 2022-06-14 02:13:41.765884
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor

    input = "def fn():\n\tyield 1\n\treturn 5"
    expected = "def fn():\n\tyield 1\n\texc = StopIteration()\n\texc.value = 5\n\traise exc"

    tree = ast.parse(input)  # type: ignore
    transformer = ReturnFromGeneratorTransformer()
    new_tree = transformer.visit(tree)  # type: ignore

    result = astor.to_source(new_tree)
    assert expected == result
    assert transformer._tree_changed



# Generated at 2022-06-14 02:13:51.835571
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import parse_to_ast_node

    class_obj = ReturnFromGeneratorTransformer()
    input_ast_node = parse_to_ast_node('''
        def generator():
            yield 1
            return 3
    ''')
    expected_ast_node = parse_to_ast_node('''
        def generator():
            yield 1
            exc = StopIteration()
            exc.value = 3
            raise exc
    ''')
    actual_ast_node = class_obj.visit(input_ast_node)
    assert ast.dump(actual_ast_node) == ast.dump(expected_ast_node)
    assert class_obj._tree_changed is True

# Generated at 2022-06-14 02:13:52.938083
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:14:03.576062
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Test(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
            return node

    fn = ast.parse(
        textwrap.dedent("""\
        def fn():
            yield 1
            return 5
        """)
    )

    fd = Test().visit(fn)  # type: ignore

    assert isinstance(fd, ast.Module)

    fd = fd.body[0]

    assert isinstance(fd, ast.FunctionDef)
    assert fd.name == 'fn'

    assert len(fd.body) == 3
    assert isinstance(fd.body[0], ast.Expr)

    yield_node = fd.body[0]  # type: ast.Yield

# Generated at 2022-06-14 02:14:04.431086
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:15:25.845275
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    stmt = ast.parse("""
        def f():
            a = 1
            while True:
                if a:
                    yield 1
                else:
                    return 3
    """)
    expected_stmt = ast.parse("""
        def f():
            a = 1
            while True:
                if a:
                    yield 1
                else:
                    exc = StopIteration()
                    exc.value = 3
                    raise exc
    """)
    assert Compile(ReturnFromGeneratorTransformer()).visit(stmt) == expected_stmt



# Generated at 2022-06-14 02:15:27.993256
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()


# Generated at 2022-06-14 02:15:36.169164
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse
    code = """
    def fn():
        yield 1
        return 5
    """
    ast_tree = ast.parse(code)
    ast_tree_modified = ReturnFromGeneratorTransformer().visit(ast_tree)
    code_modified = astunparse.unparse(ast_tree_modified)
    assert code_modified == '\ndef fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc'

# Generated at 2022-06-14 02:15:36.767517
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:15:47.335442
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class TestTransformer(ReturnFromGeneratorTransformer):
        def visit(self, node):
            self._visited_nodes.append(node)
            return super().visit(node)

        def _clear_results(self):
            self._visited_nodes = []

        def get_results(self):
            return self._visited_nodes

    def test_code(x, y):
        if x:
            yield 1
        yield 2
        return 3

    def test_code2(x, y):
        yield 1
        yield y
        return y

    def test_code3():
        yield 1
        return 1
        yield 2

    source = inspect.getsource(test_code)
    source2 = inspect.getsource(test_code2)

# Generated at 2022-06-14 02:15:49.823085
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testing import run_individual_test
    

# Generated at 2022-06-14 02:15:51.268376
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:16:06.484737
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    tree = ast.parse("""
    def fn():
        yield 1

        if True:
            return 3
        else:
            return 5
    """)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    expected = ast.parse("""
    def fn():
        yield 1

        if True:
            try:
                exc = StopIteration()
                exc.value = 3
                raise exc
            except StopIteration as exc:
                return exc.value
            
        else:
            try:
                exc = StopIteration()
                exc.value = 5
                raise exc
            except StopIteration as exc:
                return exc.value
    """)
    assert ast.dump(tree) == ast.dump(expected)
