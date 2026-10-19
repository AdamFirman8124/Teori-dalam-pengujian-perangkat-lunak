

# Generated at 2022-06-14 02:06:05.489272
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent
    code = dedent('''\
        def gen(x):
            yield x
            return 10
        ''')
    expected_code = dedent('''\
        def gen(x):
            yield x
            exc = StopIteration()
            exc.value = 10
            raise exc
        ''')
    transformer = ReturnFromGeneratorTransformer()
    new_ast = transformer.visit(ast.parse(code))
    generator = new_ast.body[0]
    assert 'raise' in generator.body[2].value.func.id
    assert transformer.tree_changed == True
    assert ast.dump(new_ast) == ast.dump(ast.parse(expected_code))



# Generated at 2022-06-14 02:06:15.528126
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import get_CST_from_func
    from ..utils.test_utils import check_CST_against_AST
    from ..utils.test_utils import get_ast_from_func

    func = """
        def fn(x: int):
            def fn1(y: int) -> int:
                return x + y

            if x > 5:
                return x + 5

            return fn1(x)
    """


# Generated at 2022-06-14 02:06:22.668265
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""def fn():
            yield 1
            return 5
    """)

    node = tree.body[0]

    transformer = ReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)
    assert new_node is not None

    expected = """def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc"""

    assert ast.dump(new_node) == ast.dump(ast.parse(expected))



# Generated at 2022-06-14 02:06:23.972214
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:29.388638
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    import builtins

    # Case 1:
    test_case_1_code = '''
    def fn():
        yield 1
        return 2
    '''

    module_1 = ast.parse(test_case_1_code)
    transformer_1 = ReturnFromGeneratorTransformer()
    module_1_transformed = transformer_1.visit(module_1)

# Generated at 2022-06-14 02:06:36.123154
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    source = """
    def fn():
        yield 1
        if True:
            return 5
        else:
            return 6
    """

    expected = """
    def fn():
        yield 1
        if True:
            exc = StopIteration()
            exc.value = 5
            raise exc
        else:
            exc = StopIteration()
            exc.value = 6
            raise exc
    """

    root = ast.parse(source)
    ReturnFromGeneratorTransformer().visit(root)

    assert str(root) == expected

# Generated at 2022-06-14 02:06:44.234624
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """
    def foo():
      yield 1
      return 2

    def bar():
      yield 1
      return 2
      yield 3
    """
    expected = """
    def foo():
      yield 1
      exc = StopIteration()
      exc.value = 2
      raise exc

    def bar():
      yield 1
      yield 3
    """

    tree = ast.parse(source)
    ReturnFromGeneratorTransformer().visit(tree)
    assert ast.dump(tree) == expected


# Generated at 2022-06-14 02:06:45.588997
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:47.281637
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    

# Generated at 2022-06-14 02:06:58.967048
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import round_trip, assert_type_and_value, round_trip_and_compare
    from ..utils.ast import parse


# Generated at 2022-06-14 02:07:10.903707
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer(None)

    def fn_simple_return():
        yield 'one'
        return 'two'

    def fn_yield_call_return():
        yield 'one'
        try:
            two()
        except:
            pass
        else:
            return 'two'

    def fn_two_returns():
        yield 'one'
        if True:
            return 'two'
        else:
            return 'three'

    def fn_if_return():
        yield 'one'
        if True:
            return 'two'
        else:
            return

    def fn_if_if_return():
        yield 'one'
        if True:
            if True:
                return 'two'
            else:
                return 'three'
        else:
            return


# Generated at 2022-06-14 02:07:18.172547
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """
    def foo():
        yield 2
        for a in range(5):
            yield a
        return 5
    """
    expected = """
    def foo():
        yield 2
        for a in range(5):
            yield a
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    result = transform(source, ReturnFromGeneratorTransformer)
    assert expected == result



# Generated at 2022-06-14 02:07:26.812565
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Checker(BaseNodeTransformer):
        def __init__(self):
            self.targets = [
                'return_from_generator',
                'exc = StopIteration()',
                'exc.value = ',
                'raise exc'
            ]

        def generic_visit(self, node):
            if isinstance(node, ast.Expr):
                if any(x in node.value.s for x in self.targets):
                    assert True
            if hasattr(node, 'body'):
                for child in ast.iter_child_nodes(node):
                    self.generic_visit(child)
            return node

    test_fn = """
    def test():
        yield 1
        return 1
    """
    node = ast.parse(test_fn, 'test')

# Generated at 2022-06-14 02:07:39.742640
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

    # empty function
    node = ast.parse('def fn(): pass')
    transformer.visit(node)
    assert transformer._tree_changed == False
    assert ast.dump(node, include_attributes=True) == \
    'Module([FunctionDef(name=fn, args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Pass()], decorator_list=[], returns=None)], type_ignores=[])'

    # function with non generators returns
    # return 1
    node = ast.parse('def fn():\n    return 1')
    transformer.visit(node)
    assert transformer._tree_changed == False

# Generated at 2022-06-14 02:07:52.827926
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import ast_factory


# Generated at 2022-06-14 02:08:00.889162
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import typed_astunparse
    source = '''
    def f(b):
        yield b
        return False
    '''
    tree = ast.parse(source)
    transformer = ReturnFromGeneratorTransformer()
    transformed_tree = ast.fix_missing_locations(transformer.visit(tree))
    assert typed_astunparse.unparse(transformed_tree) == '''
    def f(b):
        yield b
        exc = StopIteration()
        exc.value = False
        raise exc
    '''

# Generated at 2022-06-14 02:08:01.595063
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:02.324519
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:11.177081
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
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

    before_ast = ast.parse(before)
    after_ast = ast.parse(after)

    transformer = ReturnFromGeneratorTransformer(before_ast)
    transformer.visit(before_ast)
    assert before_ast.body[0].body == after_ast.body[0].body


# Generated at 2022-06-14 02:08:19.004626
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert_transform(
        ReturnFromGeneratorTransformer,
        'def fn():\n    return 1',
        'def fn():\n    return 1',
    )
    assert_transform(
        ReturnFromGeneratorTransformer,
        'def fn():\n    yield 1\n    return 1',
        'def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 1\n    raise exc'
    )
    assert_transform(
        ReturnFromGeneratorTransformer,
        'def fn():\n    yield from range(10)\n    return 1',
        'def fn():\n    yield from range(10)\n    exc = StopIteration()\n    exc.value = 1\n    raise exc'
    )

# Generated at 2022-06-14 02:08:39.928536
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse

    class TestNodeTransformer(BaseNodeTransformer):
        target = (3, 4)

        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            return self.generic_visit(node)  # pragma: no cover

    code = '''
        def test_generator():
            yield 1
            return 5
        def test_return():
            return 5
        def test_func():
            return
    '''

    node = ast.parse(code)
    transformer = TestNodeTransformer()
    node = transformer.visit(node)

    assert unparse(node) == code

    transformer = ReturnFromGeneratorTransformer()
    node = transformer.visit(node)


# Generated at 2022-06-14 02:08:49.604035
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

    def get_body(body):
        body = [
            current_stmt
            for current_stmt in ast.parse(body).body
            if isinstance(current_stmt, ast.FunctionDef)
        ][0].body

        return [str(current_stmt) for current_stmt in body]

    assert get_body('''
        def fn():
            pass
    ''') == [
        'pass',
    ]

    assert get_body('''
        def fn():
            yield 1
    ''') == [
        'yield 1',
    ]


# Generated at 2022-06-14 02:08:51.151285
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:02.884189
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:13.077163
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    f = ast.parse('def fn():\n    yield 1\n    return 5').body[0]
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(f)


# Generated at 2022-06-14 02:09:18.245497
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse
    source = '''def f():
    yield 1
    return 2'''
    expected = '''def f():
    yield 1
    exc = StopIteration()
    exc.value = 2
    raise exc'''
    tree = ast.parse(source)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)
    actual = astunparse.unparse(tree)
    assert actual == expected

# Generated at 2022-06-14 02:09:19.245346
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:28.716541
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
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
    node = ast.parse(source)  # type: ignore
    t = ReturnFromGeneratorTransformer()
    node = t.visit(node)  # type: ignore
    assert t._tree_changed == True
    assert ast.dump(node) == expected


# Generated at 2022-06-14 02:09:30.099528
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from ..utils import test_utils

# Generated at 2022-06-14 02:09:42.349919
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_transformer import \
        make_test, get_test_string, get_test_ast, compare_asts

    class TestClass:
        def test_1(self):
            @make_test(ReturnFromGeneratorTransformer)
            def test():
                def gen():
                    yield 1
                    return 2

                return gen

        def test_2(self):
            @make_test(ReturnFromGeneratorTransformer)
            def test():
                def gen():
                    yield 1

                return gen

        def test_3(self):
            @make_test(ReturnFromGeneratorTransformer)
            def test():
                def f():
                    return 1

                return f


# Generated at 2022-06-14 02:10:09.945939
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert_equal(ReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer.target).visit_FunctionDef(
        ast.parse("""def fn():
    yield 1
    return 5""").body[0]
    ),
        ast.parse("""def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc""").body[0]
    )
    assert_equal(ReturnFromGeneratorTransformer(ReturnFromGeneratorTransformer.target).visit_FunctionDef(
        ast.parse("""def fn():
    return 1""").body[0]
    ),
        ast.parse("""def fn():
    return 1""").body[0]
    )

# Generated at 2022-06-14 02:10:10.960413
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:23.815381
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_method(self):
        method = ReturnFromGeneratorTransformer().visit_FunctionDef

        node_no_returns = ast.parse("""
            def fn():
                yield 1
                yield 2
            """)

        node_return = ast.parse("""
            def fn():
                yield 1
                return 3
            """)

        node_return_in_if = ast.parse("""
            def fn():
                yield 1
                if True:
                    return 3
                else:
                    return 4
            """)

        node_return_in_lambda = ast.parse("""
            def fn():
                yield 1
                lambda x: x
                return 3
            """)

        result_no_returns = method(self, node_no_returns.body[0])

# Generated at 2022-06-14 02:10:33.508361
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """
    def test():
        yield 1
        return 5

    def test_two():
        return 5
    """
    expected = """
    def test():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc

    def test_two():
        return 5
    """

    suite = ast.parse(source)
    transformer = ReturnFromGeneratorTransformer()
    expected_suite = ast.parse(expected)
    transformer.visit(suite)
    assert transformer._tree_changed is True
    assert expected_suite.body[0] == suite.body[0]
    assert expected_suite.body[1] == suite.body[1]



# Generated at 2022-06-14 02:10:43.214085
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    # Arrange
    from ...testing.utils import build_node
    from .. import PythonVersion

    node = build_node('def fn():\n\tyield 1\n\treturn 5', 3, 2)
    transformer = ReturnFromGeneratorTransformer(target_version=PythonVersion(3, 8))

    # Act
    transformer.visit(node)

    # Assert
    assert transformer.tree_changed

    # Assert
    expected = 'def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc'
    actual = dump(node)
    assert actual == expected

# Generated at 2022-06-14 02:10:50.044784
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
        def foo():
            yield 1
            return 2
    """
    tree = ast.parse(code)
    xformer = ReturnFromGeneratorTransformer()
    tree = xformer.visit(tree)
    assert code_gen.to_source(tree) == """
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
    """

# Generated at 2022-06-14 02:11:02.973027
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..rewrite_unpythonic import unpythonic_ast as ua

    # Helper method to check if given ast consists of stopiteration exception
    def check_generator_return_ast(body_ast, return_value_ast):
        assert len(body_ast) == 4
        assert isinstance(body_ast[0], ast.Assign)
        assert isinstance(body_ast[0].value, ast.Call)
        assert isinstance(body_ast[0].value.func, ast.Name)
        assert body_ast[0].value.func.id == 'StopIteration'
        assert len(body_ast[0].targets) == 1
        assert isinstance(body_ast[0].targets[0], ast.Name)

# Generated at 2022-06-14 02:11:13.069590
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import dedent
    from ..utils import ast_transform_test
    code = dedent("""
    def fn():
        yield 1
        return 5
    """)
    expected_code = dedent("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """)
    @ast_transform_test(ReturnFromGeneratorTransformer)
    def transform(tree):
        pass
    transform(code, expected_code)
# End of unit test

# Generated at 2022-06-14 02:11:15.265427
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:11:24.645215
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import run_on_lines
    from sys import version_info

    lines = [
        'def fn():',
        '    yield 1',
        '    return 2',
        '    yield 3',
        '    return 4',
    ]

    expected_lines = [
        'def fn():',
        '    yield 1',
        "    exc = StopIteration()",
        "    exc.value = 2",
        "    raise exc",
        '    yield 3',
        "    exc = StopIteration()",
        "    exc.value = 4",
        "    raise exc",
    ]

    @run_on_lines
    def run(lines):
        from typed_ast import parse
        from ..transformers import ReturnFromGeneratorTransformer


# Generated at 2022-06-14 02:11:53.356733
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testutils import check_transformer_class
    check_transformer_class(ReturnFromGeneratorTransformer)

# Generated at 2022-06-14 02:11:54.720772
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:59.888596
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..test_utils import parse, transform
    from ..utils.fixtures import simple_generator

    try:
        tree = parse(simple_generator)
        transform(tree, [ReturnFromGeneratorTransformer])
    except Exception as e:
        assert False, e
    else:
        assert True



# Generated at 2022-06-14 02:12:03.178217
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import create_function_node
    from .base import make_code_from_node


# Generated at 2022-06-14 02:12:10.499442
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    '''
    Test case for ReturnFromGeneratorTransformer.visit_FunctionDef.
    '''
    src = dedent("""\
        def fn():
            yield 1
            return 5
        """)

    expected = dedent("""\
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """)

    code = ast.parse(src)
    ReturnFromGeneratorTransformer().visit(code)
    assert roundtrip(code) == expected

# Generated at 2022-06-14 02:12:11.014042
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:18.813564
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformerTestCase
    from textwrap import dedent

    class TestCase(BaseNodeTransformerTestCase):
        def test_return_from_generator(self):
            src = dedent('''
                def fn():
                    yield 5
                    return 6
            ''')
            expected = dedent('''
                def fn():
                    yield 5
                    exc = StopIteration()
                    exc.value = 6
                    raise exc
            ''')
            self.assertCodeTransformation(src, expected, [ReturnFromGeneratorTransformer])

# Generated at 2022-06-14 02:12:24.376324
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse(
        """
        def generator():
            yield 1
            return 2
        """
    )
    expected = ast.parse(
        """
        def generator():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
        """
    ).body[0]

    result = ReturnFromGeneratorTransformer().visit(node)

    assert_equivalent_node(expected, result)


# Generated at 2022-06-14 02:12:33.939868
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import print_parso_node, print_compiled_node

    code_snippet = """
        def fn():
            yield 1
            return 5
        """

    root = ast.parse(code_snippet)
    expected = ast.parse("def fn(): yield 1; exc = StopIteration(); exc.value = 5; raise exc")
    node = root.children[0]

    transformer = ReturnFromGeneratorTransformer(root)

    new_node = transformer.visit(node)

    print_parso_node(new_node)

    print_compiled_node(expected)

    assert new_node == expected



# Generated at 2022-06-14 02:12:35.149398
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:35.752900
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assertAST
    from .utils import transform, dump
    source = """
    def fn():
        yield 1
        return 2
    def fn2():
        return 3
    def fn3():
        yield 1
        if True:
            return 5
    def fn4():
        for x in range(3):
            yield x
            return x
    def fn5():
        try:
            return 0
        except Exception:
            return 1
    """

# Generated at 2022-06-14 02:13:46.878511
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test():
        def test():
            yield 1
            return 5
        x = test()
        x.__next__(); x.__next__(); x.__next__(); x.__next__()

    class _Test(BaseNodeTransformer):
        def visit_Assign(self, node: ast.Assign) -> ast.Assign:
            if isinstance(node.value, ast.Call) and \
                    isinstance(node.value.func, ast.Name) and \
                    node.value.func.id == 'test':
                test_node = node.value.func
                function = self._functions_pool[test_node]
                transformer = ReturnFromGeneratorTransformer()
                result = transformer.visit(function)
                return node


# Generated at 2022-06-14 02:13:50.911236
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import unittest
    from .test_utils import generate_test
    from typed_ast import ast3


# Generated at 2022-06-14 02:14:02.037666
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from pytest import raises
    from .test_utils import transform, function_with_body

    # Using bfs find all `return` statements in function
    def test_find_generator_returns():
        t = transform(ReturnFromGeneratorTransformer)
        tree = ast.parse(function_with_body(
            'yield 1\n'
            'return 5\n'
        ))
        t.visit(tree)
        assert len(t._find_generator_returns(tree.body[0])) == 1

        tree = ast.parse(function_with_body(
            'yield 1\n'
            'return 1\n'
            'return 2\n'
        ))
        t.visit(tree)

# Generated at 2022-06-14 02:14:15.616130
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformer
    import typed_astunparse

    def _do_test(text, expected):
        module = ast.parse(text)
        transformer = ReturnFromGeneratorTransformer()
        BaseNodeTransformer.apply_transformer(transformer, module)
        assert typed_astunparse.unparse(module) == expected

    text = """if u:
    def fn():
        yield 1
        return 5
"""
    expected = """if u:
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
"""
    _do_test(text, expected)

    text = """if u:
    def fn():
        yield from range(10)
        return 5
"""

# Generated at 2022-06-14 02:14:25.304260
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Given
    first_snippet_body_list = list(first_snippet.get_body())

    first_target_node_list = list(first_target_node.get_child_nodes())

    second_snippet_body_list = list(second_snippet.get_body())

    second_target_node_list = list(second_target_node.get_child_nodes())

    function_def_node_list = list(function_def.get_child_nodes())


# Generated at 2022-06-14 02:14:37.263109
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source_code import SourceCode
    from .function_def_transformer import FunctionDefTransformer
    from ..utils.test_fixtures import build_parse_tree
    from ..test_utils import assert_transformation

    # Sample code
    def fn(self):
        yield 1
        return 5

    # Parse code
    module = build_parse_tree(fn, build_ast=True)
    function = module.body[0]

    # Generated code
    def expected_fn(self):
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc

    # Compare produced ast

# Generated at 2022-06-14 02:14:49.105183
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        yield 1
        return 5

    # Check code of fn
    code = compile(fn.__code__, "", "exec")
    print(str(code))
    # Code structure
    # code = types.CodeType(
    #     argcount=1,
    #     kwonlyargcount=0,
    #     nlocals=3,
    #     stacksize=2,
    #     flags=67,
    #     codestring,
    #     constants,
    #     names,
    #     varnames,
    #     filename,
    #     name,
    #     firstlineno,
    #     lnotab,
    #     freevars,
    #     cellvars
    # )

    code_ = test_ReturnFromGeneratorTransformer_visit_Function

# Generated at 2022-06-14 02:15:01.553728
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    def fn():
        yield 1
        return 5
    code = compile(fn.__code__, fn.__name__, 'exec')
    code = ast.parse(code)
    node = code.body[0]
    assert isinstance(node, ast.FunctionDef)
    assert len(ast.walk(node)) == 6, 'node must have 6 childs'
    assert isinstance(node.body[1], ast.Return)

    module = ast.Module(body=[node])
    transformer = ReturnFromGeneratorTransformer()
    node = transformer.visit(module)

    assert isinstance(node, ast.Module)
    node = node.body[0]
    assert isinstance(node, ast.FunctionDef)

# Generated at 2022-06-14 02:15:13.445388
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    rfgt = ReturnFromGeneratorTransformer()

    # Test that transformer does nothing if function contains only normal return
    func_def = ast.FunctionDef(
        name='fn',
        args=ast.arguments(args=[]),
        body=[ast.Return(None)])
    assert rfgt.visit(func_def) == func_def

    # Test that transformer removes normal return
    func_def = ast.FunctionDef(
        name='fn',
        args=ast.arguments(args=[]),
        body=[ast.Yield(None), ast.Return(None)])