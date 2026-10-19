

# Generated at 2022-06-14 02:06:11.227153
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_function_def
    from .base import BaseNodeTest

    method = BaseNodeTest.get_method(ReturnFromGeneratorTransformer, 'visit_FunctionDef')

    function_def = ast.parse("""
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

    assert_function_def(method, function_def, expected)


# Generated at 2022-06-14 02:06:12.461305
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:21.929967
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    original_code = """
    def funct():
        for i in range(1, 10):
            yield i
        return i # this is a problem
        """
    expected_code = """
    def funct():
        for i in range(1, 10):
            yield i
        exc = StopIteration()
        exc.value = i
        raise exc
        """

    # create nodes from code
    module = ast.parse(original_code)

    # optimize code
    ReturnFromGeneratorTransformer().visit(module)

    # convert optimized code to source code
    optimized_code = astor.to_source(module).strip()

    # compare codes
    assert expected_code == optimized_code

# Generated at 2022-06-14 02:06:27.307020
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transform = ReturnFromGeneratorTransformer()
    tree = ast.parse("""
        def foo():
            yield 1
            return 5
    """)
    NodeTransformer.generic_visit(transform, tree)
    assert str(tree) == """
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """



# Generated at 2022-06-14 02:06:37.695928
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import sys
    import unittest
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformerTest
    from .base import transform
    from .base.testing_utils import get_arguments_from_function_def
    from .base.testing_utils import mock_ast_node_subclasses


    class TestCase(unittest.TestCase, BaseNodeTransformerTest):
        transformer = ReturnFromGeneratorTransformer
        target = (3, 2)

        def test_function_without_return(self):
            node = ast.FunctionDef(
                name='fn',
                args=ast.arguments(),
                body=[
                    ast.Expr(ast.Name(id='print', ctx=ast.Load())),
                ],
            )


# Generated at 2022-06-14 02:06:39.260046
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:48.992479
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import textwrap
    from ..utils.source import Source
    source = Source.from_code(textwrap.dedent('''
        def fn():
            yield 1
            return 5
    '''))

    new_source = source.apply_ast(ReturnFromGeneratorTransformer)

    assert str(new_source) == textwrap.dedent('''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    ''')

    new_ast = new_source.ast()
    assert_msgs = []

    for return_node in new_source.find_all(ast.Return):
        assert_msgs.append(f'{return_node} should be replaced with StopIteration raising')


# Generated at 2022-06-14 02:06:50.509565
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:01.651440
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import textwrap
    from ..utils import get_func

    def get_source(func):
        return textwrap.dedent(inspect.getsource(func))

    def check(func):
        source = get_source(func)
        res_func = get_func(source, ReturnFromGeneratorTransformer)
        assert get_source(res_func) == get_source(func_res)

    def func():
        yield 1
        return 2

    def func_res():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc

    check(func)

    func = func_res
    check(func)

    func_res = func
    check(func)

    def func_res():
        yield 1
        raise StopIteration(2)

    def func():
        yield 1

# Generated at 2022-06-14 02:07:07.772440
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    module = ast.parse('def fn():\n'
                       '    yield 1\n'
                       '    return 5', '<test>', 'exec')
    node = module.body[0]
    tree = ReturnFromGeneratorTransformer().visit(module)
    expected = ast.parse('def fn():\n'
                         '    yield 1\n'
                         '    exc = StopIteration()\n'
                         '    exc.value = 5\n'
                         '    raise exc', '<test>', 'exec')
    assert ast.dump(tree) == ast.dump(expected)

# Generated at 2022-06-14 02:07:23.162215
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer('target')

    function_def = ast.FunctionDef(
        name='fn',
        body=[ast.Return(value=ast.Num(n=5))],
        decorator_list=[],
        args=ast.arguments(
            args=[],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        )
    )

    assert transformer.visit(function_def) == function_def


# Generated at 2022-06-14 02:07:33.300006
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class GeneratorVisitor(ast.NodeVisitor):
        def __init__(self):
            self.func_defs = []

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            self.func_defs.append(node)

    generator_visitor = GeneratorVisitor()

    for gen in glob.iglob('tests/example_generators/*.py'):
        mod = ast.parse(open(gen).read())
        transformer = ReturnFromGeneratorTransformer()
        mod = transformer.visit(mod)  # type: ignore
        generator_visitor.visit(mod)
        assert transformer._tree_changed

    for func_def in generator_visitor.func_defs:
        # All return statements should be replaced with
        # StopIteration exception
        assert not _returns_

# Generated at 2022-06-14 02:07:40.640940
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .sample_asts import ReturnFromGeneratorTransformer_FOR_TESTING

    source = ReturnFromGeneratorTransformer_FOR_TESTING.code
    expected = ReturnFromGeneratorTransformer_FOR_TESTING.expected
    tree = ast.parse(source)
    result = ReturnFromGeneratorTransformer().visit(tree)
    assert ast.dump(result) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 02:07:45.068770
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class_ = ReturnFromGeneratorTransformer()
    result = class_.visit_FunctionDef(ast.parse('def fn():\n    yield 1\n    return 10\n').body[0])

# Generated at 2022-06-14 02:07:53.103566
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    expected_result_code = ("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """)

    input_code = ("""
    def fn():
        yield 1
        return 5
    """)

    expected_result_ast = parse(expected_result_code)
    input_ast = parse(input_code)

    transformer = ReturnFromGeneratorTransformer()
    actual_result_ast = transformer.visit(input_ast)

    assert_equals(expected_result_ast, actual_result_ast)

# Generated at 2022-06-14 02:08:02.413781
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..includes import patch_includes
    from ..utils.ast import dump, module_best_effort, node_to_str
    from ..utils.visitor import Visitor

    patch_includes()

    class Vis(Visitor):
        GENERATORS = {}  # type: ignore

        def visit_FunctionDef(self, node: ast.FunctionDef):
            if not node.name.startswith('test_'):
                return

            self.GENERATORS[node.name] = node

    patcher_module = module_best_effort('tests/fixtures/generator.py')
    Vis().visit(patcher_module)

    gen_names = ['test_basic_generator',
                 'test_async_gen',
                 'test_async_for',
                 'test_async_with']

# Generated at 2022-06-14 02:08:04.907581
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_transformer import compile_function
    from ..utils.source import source


# Generated at 2022-06-14 02:08:13.376405
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import as_ast

    content = '''
    def fn():
        yield 1
        return 5
    def generator_with_no_return():
        yield 1
        yield 2
    def no_yield():
        return 5
    '''

    expected = '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc

    def generator_with_no_return():
        yield 1
        yield 2


    def no_yield():
        return 5
    '''

    node = as_ast(content)
    transformer = ReturnFromGeneratorTransformer()
    node = transformer.visit(node)
    diff = DeepDiff(as_ast(expected), node)
    assert not diff

# Generated at 2022-06-14 02:08:27.466642
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # This is the generated AST for the following python code
    # def fn():
    #     yield 1
    #     return 5
    fn = ast.FunctionDef(name='fn',
                         args=ast.arguments(
                             args=[],
                             vararg=None,
                             kwonlyargs=[],
                             kw_defaults=[],
                             kwarg=None,
                             defaults=[]),
                         body=[
                             ast.Expr(value=ast.Yield(value=ast.Constant(value=1,
                                                                        kind=None),
                                                      kind=None),
                                      kind=None),
                             ast.Return(value=ast.Constant(value=5, kind=None))],
                         decorator_list=[],
                         returns=None,
                         keywords=[])




# Generated at 2022-06-14 02:08:33.846474
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('def foo():\n\tyield 1\n\treturn 5\n')
    actual = ReturnFromGeneratorTransformer().visit(node)  # type: ignore
    expected = ast.parse('def foo():\n\tyield 1\n\texc = StopIteration()\n\texc.value = 5\n\traise exc\n')
    assert ast.dump(actual) == ast.dump(expected)

# Generated at 2022-06-14 02:08:45.434734
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .util import source_to_ast as ast
    from ..utils.source_for_tests import RETURN_FROM_GENERATOR_SOURCE
    
    node = ast(RETURN_FROM_GENERATOR_SOURCE)

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)

    assert transformer.has_changed() is True

    assert transformer.target == (3, 2)



# Generated at 2022-06-14 02:08:52.488460
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..testing import assert_snippet
    source = """
        def fn():
            yield 1
            return 5
    """
    expected = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    assert_snippet(ReturnFromGeneratorTransformer, source, expected)



# Generated at 2022-06-14 02:08:53.828349
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:58.847676
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.build_ast import build_ast

    #print(build_ast("def foo(): yield 1; return 5", ast_version=3.8))
    class_ = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:09:04.871103
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    assert transformer.visit_FunctionDef(ast.parse("""
    def fn():
        yield 1
        return 5""").body[0]) == ast.parse("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc""").body[0]



# Generated at 2022-06-14 02:09:07.162638
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:14.261765
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    test_input = """
        def test():
            yield 1
            return 2
            """
    expected = """
        def test():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
            """

    node = ast.parse(test_input)
    ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(node) == expected

# Generated at 2022-06-14 02:09:22.635338
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class EmptyNodeTransformer(BaseNodeTransformer):
        target = (3, 0)
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            return ast.parse('def foo(): return 1').body[0]

    # ensure that class doesn't have own method
    assert not hasattr(EmptyNodeTransformer, 'visit_Return')

    # check return from simple generator
    original = ast.parse('def foo():\n'
                         '    yield 1\n'
                         '    return 5')
    target = ast.parse('def foo():\n'
                       '    yield 1\n'
                       '    exc = StopIteration()\n'
                       '    exc.value = 5\n'
                       '    raise exc')

    compiler = EmptyNodeTransformer()
    transformer = ReturnFromGener

# Generated at 2022-06-14 02:09:34.629297
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.test_utils import transform, assert_equal
    from ..utils.snippet import snippet, let
    from .utils import place_function

    let(return_from_generator)

    @place_function(function_name="return_from_generator",
                    arg_names=["return_value"],
                    return_type=None,
                    body_type=ast.Expr,
                    body=return_from_generator)

    def test_function(function):
        function = function()
        function = transform(ReturnFromGeneratorTransformer, function)


# Generated at 2022-06-14 02:09:38.484163
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class ReturnFromGeneratorTransformerSubclass(ReturnFromGeneratorTransformer):
        def _replace_return(self, parent: Any, return_: ast.Return) -> None:
            pass


# Generated at 2022-06-14 02:09:48.908766
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    c = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:09:54.923715
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    checker = TypeChecker()
    tree = ast.parse("""
        def fn():
            yield 1
            return 5
    """)
    node = tree.body[0]
    transformer = ReturnFromGeneratorTransformer(tree)
    result = transformer.visit_FunctionDef(node)
    assert checker.check(result) == []

# Generated at 2022-06-14 02:09:59.289485
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Create AST
    node = ast.parse(
        """
            def fn1():
                yield 1
                return 5

            def fn2():
                yield 1
                r = 6
                return r

            def fn3():
                yield 1
                return
        """
    )

    # Run transformer
    run_transformer(ReturnFromGeneratorTransformer, node)

    # Check results
    assert_equal_ast(
        node,
        """
            def fn1():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc

            def fn2():
                yield 1
                r = 6
                exc = StopIteration()
                exc.value = r
                raise exc

            def fn3():
                yield 1
                return

        """
    )

# Generated at 2022-06-14 02:10:00.557014
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:05.986795
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    src = """
    def fn():
        yield 1
        return 5
    """
    expected = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    assert transform(ReturnFromGeneratorTransformer, src) == expected

# Generated at 2022-06-14 02:10:15.031733
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    from astunparse import unparse

    from .syntax_tree_visitors import print_debug_info

    code = '''
    def fn1():
        yield 1
        return 5 + 1

    def fn2():
        yield 1
        return 5
    '''

    parsed_ast = ast.parse(code)
    print_debug_info(parsed_ast)

    transformed_ast = ReturnFromGeneratorTransformer().visit(parsed_ast)
    print_debug_info(transformed_ast)


# Generated at 2022-06-14 02:10:16.187222
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:23.902886
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("""
    def fn():
        yield 1
        return 5
    """).body[0]
    node = ReturnFromGeneratorTransformer().visit(node)

    body = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    expected = ast.parse(body).body[0]

    assert ast.dump(node) == ast.dump(expected)

# Generated at 2022-06-14 02:10:34.489964
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    fn = ast.FunctionDef(name='fn',
                      args=ast.arguments(
                        args=[ast.Name(id='self', ctx=ast.Param())],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[]),
                      body=[ast.Yield(value=ast.Num(n=1)),
                            ast.Return(value=ast.Num(n=5))],
                      decorator_list=[],
                      returns=None,
                      type_comment=None)

# Generated at 2022-06-14 02:10:45.233456
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    from .test_utils.test_visitor import compare_ast

    code = """
    def foo():
        x = 5
        if x == 5:
            yield x
            return 3
        elif x == 6:
            yield x + 1
            return 4
        else:
            yield x + 2


    def bar():
        x = 5
        if x == 5:
            yield x
        elif x == 6:
            yield x + 1
        else:
            yield x + 2
    """

# Generated at 2022-06-14 02:11:11.650968
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """
        def fn():
            def fn2():
                for i in range(3):
                    yield i
                return i
            return 1
        def fn3():
            yield 2
            return 2
        def fn4():
            return 1
    """
    expected = """
        def fn():
            def fn2():
                for i in range(3):
                    yield i
                exc = StopIteration()
                exc.value = i
                raise exc
            return 1
        def fn3():
            yield 2
            exc = StopIteration()
            exc.value = 2
            raise exc
        def fn4():
            return 1
    """
    root = ast.parse(source)
    node = root.body[1]

    ReturnFromGeneratorTransformer().visit(root)


# Generated at 2022-06-14 02:11:22.485501
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.fake import FakeNode
    from .base import NodeTransformer, NodeVisitor

    class TestTransformer(NodeTransformer):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
            for line in return_from_generator.get_body(return_value='5'):
                node.body.append(line)
            return self.generic_visit(node)

    class TestVisitor(NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
            return len(node.body)

    visitor = TestVisitor()
    transformer = TestTransformer()

    node = FakeNode()
    node.body = [ast.Yield(None)]
    node.body.append(ast.Return(None))

# Generated at 2022-06-14 02:11:25.294048
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from idiom import Idiom
    import typed_ast.ast3 as ast
    import astor


# Generated at 2022-06-14 02:11:27.624414
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_compiler(codestr: str) -> str:
        tree = ast.parse(codestr)
        ReturnFromGeneratorTransformer.run_on_tree(tree)
        return tree.body[0]


# Generated at 2022-06-14 02:11:28.936269
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor

# Generated at 2022-06-14 02:11:39.625477
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("""
    def fn():
        yield 1
        return
    """)
    nt = ReturnFromGeneratorTransformer()
    nt.visit(node)

# Generated at 2022-06-14 02:11:48.062520
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    f = inspect.currentframe()
    outerframes = inspect.getouterframes(f)
    path = outerframes[len(outerframes)-1][1]
    directory = os.path.dirname(os.path.abspath(path)) + "/../"

    file_path = directory + "tests/samples/generator.py"

    with open(file_path, "r") as source:
        tree = ast.parse(source.read())

    t = ReturnFromGeneratorTransformer()
    res = t.visit(tree)

    assert res.body[0].name == "NoReturn"
    assert res.body[1].name == "ReturnFromGenerator"
    assert res.body[2].body[0].body[0].value.id == "StopIteration"

# Generated at 2022-06-14 02:11:49.038035
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:49.885700
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:56.080153
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.transform_test import assert_transform

    def function():
        for x in range(1, 3):
            a = yield x
            return a
        return

    assert_transform(
        ReturnFromGeneratorTransformer,
        function,
        '''
        def function():
            for x in range(1, 3):
                a = yield x
                exc = StopIteration()
                exc.value = a
                raise exc
            return
        '''
    )

# Generated at 2022-06-14 02:12:41.568483
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def _make_code(fn):
        return ast.parse(fn).body[0]

    def _test(code, result_code):
        # type: (str, str) -> None
        transformer = ReturnFromGeneratorTransformer()
        result = transformer.visit(_make_code(code))
        assert result_code == ast.unparse(result)

    # Test case with multiple returns
    code = """
        def f():
            yield 1
            return a
            yield 2
            return b
    """
    result_code = """
        def f():
            yield 1
            exc = StopIteration()
            exc.value = a
            raise exc
            yield 2
            exc = StopIteration()
            exc.value = b
            raise exc
    """
    _test(code, result_code)

    # Test

# Generated at 2022-06-14 02:12:53.559135
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor

    def fn():
        yield 1
        return 2

    assert fn.__name__ == 'fn'
    assert list(fn()) == [1]

    source = astor.to_source(ast.parse(fn.__code__.co_consts[1]))
    assert source == 'def fn():\n    yield 1\n    return 2\n'

    code = fn.__code__.co_consts[1]

    transformed = ReturnFromGeneratorTransformer().visit(code)
    assert transformed != code

    source = astor.to_source(transformed)
    assert source == 'def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 2\n    raise exc\n'

    # Create compiled with new code object

# Generated at 2022-06-14 02:12:54.782229
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:02.144699
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source import source_to_node

    source = """
    
        def fn():
            yield 1
            return 5

        def fn2():
            yield 1
            if 1:
                return 5
            return 6

        def fn3():
            yield 1
            if 1:
                return 5
            yield 6
            return 7

        def fn4():
            yield 1
            if 1:
                if 2:
                    yield 2
                    if 3:
                        yield 3
                        return 4
                    return 5
                return 6
            return 7
    
    """
    node = source_to_node(source)
    ReturnFromGeneratorTransformer().visit(node)

# Generated at 2022-06-14 02:13:10.040026
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """
        def g():
            yield 1
            return 5
    """
    expected = """
        def g():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    tree = ast.parse(source)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)
    result = ast.unparse(tree)
    assert result == expected



# Generated at 2022-06-14 02:13:20.204134
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # arrange
    class TestTransformer(ast.NodeTransformer):
        def __init__(self, module: ast.AST, return_from_generator_transform=ReturnFromGeneratorTransformer()):
            self.return_from_generator_transform = return_from_generator_transform
            self.module = module

        def visit_Module(self, node: ast.Module) -> ast.Module:
            node.body = [self.return_from_generator_transform.visit(node) for node in node.body]
            return node

    test_input = '''
        def f1():
            yield 1
            return 2
        '''
    test_expected = '''
        def f1():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
        '''
   

# Generated at 2022-06-14 02:13:31.842230
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.parso.python.tree import PythonNode
    from ..utils.parso.python.parser import ParserSyntaxError
    from ..utils.snippet import snippet

    code = snippet(fn)
    root = ast.parse(code, '<test>')
    node = ast.fix_missing_locations(root)

    def get_fns(node: ast.AST) -> List[PythonNode]:
        if isinstance(node, ast.AST):
            for field, value in ast.iter_fields(node):
                if isinstance(value, list):
                    for item in value:
                        yield from get_fns(item)
                else:
                    yield from get_fns(value)
        elif isinstance(node, PythonNode):
            yield node


# Generated at 2022-06-14 02:13:37.521528
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_function():
        yield 1
        return 5

    tree = ast.parse(inspect.getsource(test_function))

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)

    def check_function():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc

    assert ast.dump(tree) == ast.dump(ast.parse(inspect.getsource(check_function)))



# Generated at 2022-06-14 02:13:47.486374
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # CASE: empty function
    assert ReturnFromGeneratorTransformer().visit(ast.parse('def fn():pass')) == ast.parse('def fn():pass')

    # CASE: empty generator
    assert ReturnFromGeneratorTransformer().visit(ast.parse('def fn():yield 1')) == ast.parse('def fn():yield 1')

    # CASE: generator with return
    assert ReturnFromGeneratorTransformer().visit(ast.parse('def fn():yield 1; return 1')) == ast.parse(
        'def fn():\n'
        '    yield 1\n'
        '    exc = StopIteration()\n'
        '    exc.value = 1\n'
        '    raise exc')

    # CASE: generator with return in for loop

# Generated at 2022-06-14 02:13:55.194204
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse('\n'.join([
        'def foo():',
        '    yield 1',
        '    return 5'
    ]))
    node = tree.body[0]
    result = ReturnFromGeneratorTransformer().visit(node)
    expected = ast.parse('\n'.join([
        'def foo():',
        '    yield 1',
        '    exc = StopIteration()',
        '    exc.value = 5',
        '    raise exc',
    ]))
    assert ast.dump(result, annotate_fields=False) == ast.dump(expected, annotate_fields=False)


# Generated at 2022-06-14 02:15:15.648839
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Arrange
    expected_code1 = """def count(n):
    x = 0
    while x < n:
        yield x
        exc = StopIteration()
        exc.value = x
        raise exc
        x += 1"""
    expected_code2 = """def count(n):
    x = 0
    while x < n:
        yield x
        x += 1"""
    expected_code3 = """def count(n):
    x = 0
    while x < n:
        yield x
        exc = StopIteration()
        exc.value = x
        raise exc
        x += 1
    exc = StopIteration()
    exc.value = x
    raise exc"""

# Generated at 2022-06-14 02:15:26.864698
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """fun(a):
    try:
        yield a
    except StopIteration:
        yield b
    finally:
        return 5"""
    expected = """fun(a):
    try:
        yield a
    except StopIteration:
        yield b
    finally:
        exc = StopIteration()
        exc.value = 5
        raise exc"""

    node = ast.parse(source)
    node = ast.fix_missing_locations(node)
    transformer = ReturnFromGeneratorTransformer()
    node = transformer.visit(node)
    assert transformer._tree_changed
    assert ast.dump(node, annotate_fields=False) == expected

    source = """fun(a):
    try:
        yield a
    except StopIteration:
        yield b
    finally:
        return c"""


# Generated at 2022-06-14 02:15:38.936559
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import unittest
    import typed_ast.ast3 as ast
    from .conftest import get_node_of_class, func_body_from_str

    class ReturnFromGeneratorTransformerTest(unittest.TestCase):
        def test_it_should_replace_return_from_generator_to_exception_raising(self):
            node = get_node_of_class(ast.FunctionDef, '''
                def fn():
                    yield
                    return 1
                ''')
            transformer = ReturnFromGeneratorTransformer()
            transformer.visit(node)
            self.assertSequenceEqual(func_body_from_str('''
                yield
                exc = StopIteration()
                exc.value = 1
                raise exc
                '''), node.body)


# Generated at 2022-06-14 02:15:39.968692
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:15:47.775154
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from astunparse import unparse
    tree = ast.parse(TEST_CODE_INPUT)
    transformer = ReturnFromGeneratorTransformer(tree)

    result = transformer.visit(tree)
    assert transformer._tree_changed

    parsed_result = ast.parse(unparse(result))
    expected_result = ast.parse(TEST_CODE_OUTPUT)

    assert ast.dump(parsed_result) == ast.dump(expected_result)



# Generated at 2022-06-14 02:15:49.472830
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:16:04.254649
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(string: str, expected: str, version: Tuple[int, int] = (3, 8)):
        code = ast.parse(string)
        ReturnFromGeneratorTransformer(version=version).visit(code)
        assert ast.unparse(code) == expected

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
            return 5
            yield 6
    ''', '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
            yield 6
    ''')
