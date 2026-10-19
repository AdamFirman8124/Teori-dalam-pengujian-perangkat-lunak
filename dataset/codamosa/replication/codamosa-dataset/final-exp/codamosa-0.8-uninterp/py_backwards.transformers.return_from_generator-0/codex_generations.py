

# Generated at 2022-06-14 02:06:01.381237
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:13.635230
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()

    def test(fn_source: str, expected_fn_source: str) -> None:
        node = ast.parse(fn_source)
        code = compile(node, '<test>', 'exec')
        exec(code)
        fn_name = fn_source.split(' ')[1].split('(')[0]
        node.body[0].body = transformer.visit(node.body[0].body)

        assert ast.dump(node) == ast.dump(
            ast.parse(expected_fn_source))

        code = compile(node, '<test>', 'exec')
        exec(code)

        assert locals()[fn_name]() == fn()


# Generated at 2022-06-14 02:06:23.810251
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import compile_source, source_to_ast, source_to_node, ast_to_source
    def test_func(source, expected):
        source_ast = source_to_ast(source)
        node = source_to_node(source_ast)
        assert(isinstance(node, ast.FunctionDef))
        ReturnFromGeneratorTransformer().visit(node)
        result_ast = source_to_ast(ast_to_source(ast.fix_missing_locations(node)))
        expected_ast = source_to_ast(expected)
        assert(compile_source(result_ast, '<test>', 'exec') ==
               compile_source(expected_ast, '<test>', 'exec'))

# Generated at 2022-06-14 02:06:32.606120
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    # Przygotowanie danych
    from ..utils.source import set_source
    from .type_check_remover import TypeCheckRemover

    code = """
        def fn(a):
            if isinstance(a, int):
                return True
            return False
        def generator():
            if True:
                yield 1
                return True
            return False
    """
    expected = """
        def fn(a):
            if isinstance(a, int):
                return True
            return False
        def generator():
            if True:
                yield 1
                exc = StopIteration()
                exc.value = True
                raise exc
            exc = StopIteration()
            exc.value = False
            raise exc
    """
    tree = ast.parse(code)
    set_source(tree, code)
    Type

# Generated at 2022-06-14 02:06:41.283527
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    fn = ast.parse("""
        def foo():
            yield 42
            return 42
        def bar():
            yield 1
            return 42
            yield 2
    """).body[1]

    visitor = ReturnFromGeneratorTransformer()
    result = visitor.visit(fn)
    assert result == ast.parse("""
        def bar():
            yield 1
            exc = StopIteration()
            exc.value = 42
            raise exc
            yield 2
    """)

# Generated at 2022-06-14 02:06:44.042427
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from .fake_nodes import fake_node
    from .transformers import ReturnFromGeneratorTransformer


# Generated at 2022-06-14 02:06:49.700719
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typing import Any
    from typed_ast import ast3 as ast
    from .common import apply_transformer
    from .common import transform_and_decode
    from .common import assert_transformer

    class x:
        def fn():
            yield 1
            return 5

    tree = ast.parse('def fn(): yield 1; return 5')
    new_tree = apply_transformer(ReturnFromGeneratorTransformer, tree)


# Generated at 2022-06-14 02:06:56.404804
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
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

    tree = ast.parse(code)
    ReturnFromGeneratorTransformer().visit(tree)
    actual = astor.to_source(tree)

    assert actual.strip() == expected.strip()



# Generated at 2022-06-14 02:07:04.521398
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
        def test_generator():
            yield 1
            return 1
        """
    module = ast.parse(code)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(module)
    expected_code = """
        def test_generator():
            yield 1
            exc = StopIteration()
            exc.value = 1
            raise exc
        """

    expected_module = ast.parse(expected_code)
    assert ast.dump(module) == ast.dump(expected_module)

# Generated at 2022-06-14 02:07:11.037496
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    module = ast.parse("""
    def f():
        yield
        return
    def g():
        return 100
    def h():
        yield 1
        return 200
    def i():
        yield 2
        return 300
        return 400
    def j():
        return
        yield 3
        return 500
    """)

# Generated at 2022-06-14 02:07:23.187213
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils import python_to_python_ast, dump_python_source
    from .base import NodeTransformerTestCase

    class Test(NodeTransformerTestCase):
        target_class = ReturnFromGeneratorTransformer
        target_version = (3, 2)


# Generated at 2022-06-14 02:07:34.615467
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Test method visit_FunctionDef of class ReturnFromGeneratorTransformer"""
    transformer = ReturnFromGeneratorTransformer()

    parsed = ast.parse('''
        def fn():
            yield 1
            return 5
    ''')
    node = parsed.body[0]
    assert isinstance(node, ast.FunctionDef)
    result = transformer.visit(node)

    assert transformer._tree_changed is True
    assert node.body
    assert isinstance(result.body[-1], ast.Assign)
    assert isinstance(result.body[-2], ast.Raise)
    assert isinstance(result.body[-3], ast.Assign)
    assert isinstance(result.body[-4], ast.Raise)

# Generated at 2022-06-14 02:07:35.995909
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:37.248230
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:38.126348
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert True

# Generated at 2022-06-14 02:07:47.951128
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_func1():
        yield 1
        return

    def test_func2():
        yield 2
        return 2

    def test_func3():
        yield 3
        return 2, 3

    def test_func_no_changes():  # noqa
        return 1

    def test_func_no_changes2():  # noqa
        yield 1
        return

    def test_func_no_changes3():  # noqa
        yield 1
        yield 2

    def test_func_no_changes4():  # noqa
        yield 1
        return 2

    def test_func_no_changes5():  # noqa
        yield 1
        return 2, 3

    def test_func_no_changes6():  # noqa
        yield 1
        return None

    assert ReturnFromGeneratorTransformer.run

# Generated at 2022-06-14 02:07:58.433061
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_returns(code: str, expected_result: str) -> None:
        function_def = ast.parse(code).body[0]
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(function_def)
        assert ast.dump(function_def) == expected_result

    test_returns('def fn(): return 1', 'def fn(): return 1')
    test_returns('def fn(): yield 1', 'def fn(): yield 1')
    test_returns('def fn(): yield 1; return 1', 'def fn():\n    yield 1\n    let(exc)\n    exc = StopIteration()\n    exc.value = 1\n    raise exc')

# Generated at 2022-06-14 02:08:07.880666
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    input_code = "\n".join([
        "def fn():",
        "    a = 0",
        "    for i in range(5):",
        "        yield i",
        "    return 42"
    ])

    expected_code = "\n".join([
        "def fn():",
        "    a = 0",
        "    for i in range(5):",
        "        yield i",
        "    exc = StopIteration()",
        "    exc.value = 42",
        "    raise exc"
    ])

    # Parse string to AST
    tree = ast.parse(input_code)

    # Compile the transformer, then apply it to the input AST
    transformer = ReturnFromGeneratorTransformer()
    output_tree = transformer.visit(tree)

    # Use the same dumper to convert

# Generated at 2022-06-14 02:08:16.068623
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse
    from .base import BaseNodeTransformerTestCase

    class Test(BaseNodeTransformerTestCase):
        def create_transformer(self):
            return ReturnFromGeneratorTransformer()

        def test_return_from_generator(self):
            code = """
                def foo():
                    yield 1

                    return 1
            """
            expected = """
                def foo():
                    yield 1
                    exc = StopIteration()
                    exc.value = 1
                    raise exc
            """
            self.assertCodeTransformation(code, expected)

        def test_return_from_generator_multi_line(self):
            code = """
                def foo():
                    yield 1

                    return 1 * 2 * \
                           3 * 4 * 5
            """

# Generated at 2022-06-14 02:08:29.408087
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from..utils.visitor import get_ast_from_scratch
    from..utils.visitor import dump_ast
    from_code = """
    def fn():
        yield 1
        return 5
    """
    tree = get_ast_from_scratch(from_code)
    assert isinstance(tree, ast.Module), 'tree should be ast.Module in order to pass this test'
    tree.body[0].body[1].value.n = 5
    transformer = ReturnFromGeneratorTransformer()
    tree_changed = transformer.visit(tree)
    assert tree_changed == True, 'tree_changed should be True in order to pass this test'
    expected_code = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    expected

# Generated at 2022-06-14 02:08:44.688287
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class MockBaseNodeTransformer(BaseNodeTransformer):
        def __init__(self, tree_changed = False):
            self._tree_changed = tree_changed

        def _find_generator_returns(self, node: ast.FunctionDef) -> List[Tuple[ast.stmt, ast.Return]]:
            pass

        def _replace_return(self, parent: Any, return_: ast.Return):
            pass

    transformer = MockBaseNodeTransformer(tree_changed = False)
    transformer.visit_FunctionDef(ast.parse('def fn(): return 0'))
    assert transformer._tree_changed == False

    transformer = MockBaseNodeTransformer(tree_changed = True)
    transformer.visit_FunctionDef(ast.parse('def fn(): return 0'))
    assert transformer._tree_changed == True



# Generated at 2022-06-14 02:08:53.366561
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse
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
    tree = ast.parse(code)
    actual = astunparse.unparse(ReturnFromGeneratorTransformer().visit(tree))
    assert actual == expected

# Generated at 2022-06-14 02:08:54.159803
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:03.958578
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typing import List

    from typed_ast import ast3 as ast

    from .base import GeneratorInfo, BaseNodeTransformer

    def _add_generator_info(node: ast.FunctionDef) -> ast.FunctionDef:
        node.generator_info = GeneratorInfo()
        return node

    def _get_body_text(node: ast.FunctionDef) -> List[str]:
        return [x.body[0] for x in node.body if isinstance(x, ast.Expr)]

    node = ast.parse('def f(): return "1"')
    _add_generator_info(node.body[0])

    transformer = ReturnFromGeneratorTransformer()
    actual = transformer.visit(node)

    expected = _add_generator_info(ast.parse('def f(): raise StopIteration(1)'))

# Generated at 2022-06-14 02:09:14.933785
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from random import randint

    from ..utils.python_source import PythonSource

    org_str = """
    def fn():
        yield 1
        return 5
    """
    expected_str = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    for version in (3, 2):
        tree = ast.parse(org_str)

        transformer = ReturnFromGeneratorTransformer({})

        tree = transformer.visit(tree)

        source = PythonSource(tree, version)
        assert source.dumps() == expected_str

# Generated at 2022-06-14 02:09:21.341301
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    target = '''def fn():
        yield 1
        return 5
    '''
    transformer = ReturnFromGeneratorTransformer()
    out = transformer.visit_FunctionDef(ast.parse(target).body[0])

    expected = '''def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc
    '''
    assert transformer._tree_changed is True
    assert ast.dump(out) == ast.dump(ast.parse(expected).body[0])

# Generated at 2022-06-14 02:09:30.925404
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code_snippet = """
    def fn():
        yield 1
        return 2
    """
    expected_result = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """
    tree = ast.parse(code_snippet)
    ReturnFromGeneratorTransformer().visit(tree)
    compiled_obj = compile(tree, '<string>', 'exec')
    exec(compiled_obj)
    assert fn().__next__() == 1
    assert fn().__next__() == 2
    assert code_snippet != expected_result


    code_snippet = """
    def fn():
        return 2
    """
    tree = ast.parse(code_snippet)

# Generated at 2022-06-14 02:09:42.677984
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..testing.utils import build_anonymous_function, build_function_def, build_return_statement, build_yield_statement
    from ..testing.visitor import SourceVisitor
    from ..testing.visitor import expect_single_node

    tree = build_function_def(
        body=[
            build_return_statement(value=None),
            build_yield_statement(value=None),
            build_return_statement(value=None),
            build_return_statement(value=build_anonymous_function()),
            build_return_statement(value=None),
        ]
    )

    result = tree.visit(SourceVisitor)
    assert result == tree

    result = tree.visit(ReturnFromGeneratorTransformer)
    assert result is not tree

# Generated at 2022-06-14 02:09:52.334379
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..utils.testing import rewrite
    from ..modules.typed_ast.ast3 import fix_missing_locations
    from .type_comment_transformer import TypeCommentTransformer

    from textwrap import dedent
    import astunparse

    ast_input = ast.parse(dedent('''\
        def gen():
            if True:
                return 5

        def gen_1():
            if True:
                yield 5
            return 5

        def gen_2():
            if True:
                yield 5
            yield 5
            return 5

        def fn_1():
            if True:
                return 5

        def fn_2():
            return 5
    '''))


# Generated at 2022-06-14 02:09:53.123885
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:14.928678
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import transform
    from .test_utils import AssertNodeEqualVisitor

    code = """
        def fn():
            yield 1
            return 5
    """

    result_code = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """

    expected = ast.parse(result_code)
    result = transform(code, ReturnFromGeneratorTransformer)
    assert isinstance(result, ast.Module)
    AssertNodeEqualVisitor().visit(result.body[0], expected.body[0])


# Generated at 2022-06-14 02:10:26.624944
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import ast_unparse
    from ..utils import unindent
    from .base import UnitTestCase

    class Test(UnitTestCase):
        def test_return_from_generator(self):
            to_transpile = unindent("""
                def fn():
                    yield 1
                    return 5""")
            expected_output = unindent("""
                def fn():
                    yield 1
                    exc = StopIteration()
                    exc.value = 5
                    raise exc
                """)
            self._test_transformer(to_transpile, expected_output, ReturnFromGeneratorTransformer)
        def test_non_generator_function(self):
            to_transpile = unindent("""
                def fn():
                    return 5""")

# Generated at 2022-06-14 02:10:36.049647
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from nose.tools import assert_equals
    from typed_ast import ast3
    import re

    if 3 <= ast3.__version__ < 3.5:
        return

    code = """\
    def fn():
        yield 1
        return 5
    """
    expected_code = re.sub(r'\s{2,}', '', """\
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """)

    AST = ast3.parse(code)  # type: ast3.AST
    transformer = ReturnFromGeneratorTransformer()
    AST = transformer.visit(AST)  # type: ast3.AST
    AST.body[0].body.pop(0)
    generated_code = ast3.unparse(AST)  # type

# Generated at 2022-06-14 02:10:50.486816
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse

    test_code = '''
    def gen(a):
        if a > 1:
            return 6
        else:
            if a < 1:
                yield 1
                return 5
            else:
                yield 1
                yield 3
                return 0
    '''

    expected_code = '''
    def gen(a):
        if a > 1:
            exc = StopIteration()
            exc.value = 6
            raise exc
        else:
            if a < 1:
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
            else:
                yield 1
                yield 3
                exc = StopIteration()
                exc.value = 0
                raise exc
    '''

    test_ast = ast.parse(test_code)
    expected_ast

# Generated at 2022-06-14 02:10:51.082554
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:03.003763
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from unittest import TestCase
    from py2stub.compilers.syntax import ReturnFromGeneratorTransformer
    from ..utils.source_gen import generate_source_from_transformer
    from ..utils.source_gen import get_compiled_code_from_source
    from ..utils.source_gen import get_ast_from_code

    class Test_visit_FunctionDef(TestCase):
        def test_does_nothing_when_function_does_not_have_yield(self):
            source = dedent("""
            def fn():
                return 0
            """)
            ast_after = get_ast_from_code(
                get_compiled_code_from_source('', source),
                ReturnFromGeneratorTransformer)
            ast_before = get_ast_from_code('', source)


# Generated at 2022-06-14 02:11:15.962456
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..visitor import transform

    code = """
    def fn(x):
        if x:
            yield 1
            return 5
        else:
            yield 1
            return 6
    """
    expected = """
    def fn(x):
        if x:
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        else:
            yield 1
            exc = StopIteration()
            exc.value = 6
            raise exc
    """
    tree = ast.parse(code)
    transform(tree, ReturnFromGeneratorTransformer)
    tree_expected = ast.parse(expected)
    assert ast.dump(tree) == ast.dump(tree_expected)


# Generated at 2022-06-14 02:11:17.099447
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:18.060251
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        def inner():
            yield 4
            return 5
        return inner()


# Generated at 2022-06-14 02:11:20.163346
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import _fixtures.generators as src
    from typed_astunparse import unparse


# Generated at 2022-06-14 02:11:48.459741
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    fn = ast.parse('def fn():\n yield 1\n return 5').body[0]
    expected = 'def fn():\n yield 1\nexc = StopIteration()\nexc.value = 5\nraise exc\n'
    result = ReturnFromGeneratorTransformer(fn).visit_FunctionDef()

    assert ast.dump(result) == expected



# Generated at 2022-06-14 02:11:58.035677
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(code):
        node = ast.parse(dedent(code))
        transformer = ReturnFromGeneratorTransformer()
        node = transformer.visit(node)
        return transformer.is_changed(), node, transformer._tree_changed

    code = """
    def gen():
        yield 1
        return 5
    """
    is_changed, node, tree_changed = test(code)
    assert is_changed is True
    assert tree_changed is True
    code2 = """
    def gen():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    node2 = ast.parse(dedent(code2))
    assert ast.dump(node.body[0]) == ast.dump(node2.body[0])


# Generated at 2022-06-14 02:12:10.482568
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    t = ReturnFromGeneratorTransformer()
    assert t.visit(ast.parse('def foo():\n    return 5')) == \
        ast.parse('def foo():\n    return 5')
    assert t.visit(ast.parse('def foo():\n    return "foo"')) == \
        ast.parse('def foo():\n    return "foo"')
    assert t.visit(ast.parse('def foo():\n    yield 5\n    return "foo"')) == \
        ast.parse('def foo():\n    yield 5\n    exc = StopIteration()\n'
                  '    exc.value = "foo"\n    raise exc')

# Generated at 2022-06-14 02:12:19.870378
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(fn, expected):
        transformer = ReturnFromGeneratorTransformer()
        assert transformer.visit(ast.parse(fn)) == ast.parse(expected)

    def gen():
        yield 1
        return 2
    test(gen, """
        def gen():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
        """)

    def gen2():
        yield 1
        yield 2
        return 3
    test(gen2, """
        def gen2():
            yield 1
            yield 2
            exc = StopIteration()
            exc.value = 3
            raise exc
        """)

    def gen3():
        yield 1
        yield 2
        yield 3
        return 4
        return 5
        return 6

# Generated at 2022-06-14 02:12:24.982275
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""
        def fn():
            yield 1
            return 5
    """)
    expected_tree = ast.parse("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)
    transformer = ReturnFromGeneratorTransformer()
    tree = transformer.visit(tree)
    assert ast.dump(tree) == ast.dump(expected_tree)


# Generated at 2022-06-14 02:12:27.950224
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:30.096817
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer"""

# Generated at 2022-06-14 02:12:33.635761
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # It should replace return in generators with exception raising
    node = ast.parse('def fn(): yield 1; return 5')

    node = ReturnFromGeneratorTransformer.run(node)


# Generated at 2022-06-14 02:12:44.635099
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from compileall import compile_dir

    def _get_example_body(func: str, returns: List[str]) -> str:
        return "def {}():\n{}\n{}\n{}".format(func,
            "\n".join(["yield i"] * len(returns)),
            "\n".join(["return {}".format(x) for x in returns]),
            "print(1)"
        )

    def _check_source_equal(src: str, want: str) -> bool:
        return ast.dump(ast.parse(src), include_attributes=True) == ast.dump(ast.parse(want), include_attributes=True)

    src_dir = "test/transformer/return_from_generator"
    compile_dir(src_dir, quiet=True)


# Generated at 2022-06-14 02:12:54.534702
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import generate
    from .transformers_test import assert_transformed

    source = """\
    def fn():
        yield 1
        return 5
    """
    expected_output = """\
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    assert_transformed(ReturnFromGeneratorTransformer, source, expected_output)

    source = """\
    def fn():
        yield 1
        return 5

    def fn2():
        yield 2
        return 6
    """

# Generated at 2022-06-14 02:13:47.850789
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse("""
        def foo():
            yield 1
            return 2
    """, mode='exec')

    assert node.body[0].body[-1].value.n == 2

    transformer = ReturnFromGeneratorTransformer()
    transformed = transformer.visit(node)

    assert len(transformed.body[0].body) == 4
    exc_value = transformed.body[0].body[-2].targets[0].id
    assert transformed.body[0].body[-1].value.value.id == exc_value

# Generated at 2022-06-14 02:13:49.798039
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typing import Any, List, Iterator
    import astor
    from ..utils.fake import FakeCodegen


# Generated at 2022-06-14 02:13:50.750545
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:14:03.170311
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Test visit_FunctionDef method of class ReturnFromGeneratorTransformer."""
    module = ast.parse('def fn(a, b):\n    yield a\n    return b')
    node = module.body[0]
    R = ReturnFromGeneratorTransformer()
    R.visit(node)
    assert R.changed is True
    assert ast.dump(node) == 'def fn(a, b):\n    yield a\n    exc = StopIteration()\n    exc.value = b\n    raise exc'

    # Test that transformer fails if there is no yield statement
    module = ast.parse('def fn(a, b):\n    return b\n')
    node = module.body[0]
    R = ReturnFromGeneratorTransformer()
    R.visit(node)

# Generated at 2022-06-14 02:14:06.163840
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        yield 1
        return 5


# Generated at 2022-06-14 02:14:12.887828
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse, dump

    code = """\
    def fn():
        yield 1
        return 5
    """

    tree = parse(code)
    ReturnFromGeneratorTransformer().visit(tree)
    assert dump(tree) == """\
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

# Generated at 2022-06-14 02:14:22.113880
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

    tree = ast.parse(dedent(code))
    ReturnFromGeneratorTransformer().visit(tree)
    actual_code = ""
    for line in ast.unparse(tree).split('\n')[1:]:
        actual_code += "    " + line + "\n"
    assert dedent(expected_code) == actual_code

# Generated at 2022-06-14 02:14:37.074559
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import parse_to_ast


# Generated at 2022-06-14 02:14:40.208653
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import transforms
    from typed_ast import ast3
    from ..transforms._test_utils import assert_source_equal


# Generated at 2022-06-14 02:14:41.535571
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer