

# Generated at 2022-06-14 02:06:04.732135
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
    def foo():
        yield 1
        return 0
    """
    expected = """
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 0
        raise exc
    """
    node = ast.parse(code)
    ReturnFromGeneratorTransformer().visit(node)
    Checker().visit(node)
    Checker().visit(ast.parse(expected))
    assert to_source(node) == expected



# Generated at 2022-06-14 02:06:06.319619
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..transpile import transpile

# Generated at 2022-06-14 02:06:13.204416
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Test case for ReturnFromGeneratorTransformer.visit_FunctionDef method."""
    def check(code):
        node = ast.parse(code)
        ReturnFromGeneratorTransformer().visit(node)
        compiled = compile(node, '<test>', 'exec')
        exec(compiled)  # pylint: disable=exec-used
        fn()

    for code in ['def fn(): yield 1\n' + x for x in return_from_generator.get_body()]:
        yield check, code

# Generated at 2022-06-14 02:06:23.765373
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import parse
    from .base import BaseNodeTransformer
    from .if_constexpr import IfConstexprTransformer
    from .enum_rewriter import EnumRewriter
    from .optional_rewriter import OptionalRewriter
    from .typed_ast.ast3 import parse

    code = """\
    from typing import Optional

    def test(n: int) -> Optional[int]:
        if n == 0:
            return 42
        else:
            return None

    def test2(n: int) -> int:
        return 42

    def test3() -> int:
        yield 1
        return 5

    def test4() -> int:
        yield 1
        yield 2
        for _ in range(4):
            yield 3
        return 5

    """

# Generated at 2022-06-14 02:06:24.500771
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor  # type: ignore


# Generated at 2022-06-14 02:06:33.056198
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .contextual_transform import ContextualTransformer
    from ..utils.codegen import to_source
    from ..utils.source_repr import code_repr

    lines = """\
        def fn():
            yield 1
            return 5
        def fn2():
            def a():
                return 6
            yield 5
        def fn3():
            yield 1
            def a():
                return 6
            yield 2
        def fn4():
            yield 1
            return
        def fn5(x):
            yield x
            return x"""

    code = compile(lines, '<test>', 'exec')  # type: ignore
    ctx = ContextualTransformer()
    tree = ctx.visit(ast.parse(code))  # type: ignore
    transformer = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:06:40.864856
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

    node = ast.parse(source)
    ReturnFromGeneratorTransformer().visit(node)
    result = ast.unparse(node)
    print(result)
    assert expected == result

# Generated at 2022-06-14 02:06:46.724855
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
    module = ast.parse(src)
    ReturnFromGeneratorTransformer().visit(module)
    actual = ast.unparse(module)

    assert actual == expected

# Generated at 2022-06-14 02:06:58.570135
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # type: () -> None
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Assign, FunctionDef, Load, Name, Num, Return, Store, Yield, If, Compare, Eq, While
    from ..transpiler import Transpiler
    from ..utils.ast import compare_ast, find_all_of_type

    # Without Yield
    in_ast = ast.parse('''
        def fn():
            if True:
                return 5
    ''')

    expected_ast = ast.parse('''
        def fn():
            if True:
                return 5
    ''')  # ast.parse returns all nodes as ast.stmt, so it always needs to be casted.


# Generated at 2022-06-14 02:07:01.128007
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test case 1
    # Function definition with return statement and yield statement
    return_val = '5'

# Generated at 2022-06-14 02:07:13.011415
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source import source
    from ..utils.compare_ast import compare_ast
    from ..utils.fix_python_source import fix_python_source
    from ..utils.parsing import parse_function
    from ..utils.visitor import get_body_as_nodes

    module_node = parse_function(source("""
        def fn():
            yield 1
            return 5
    """))
    function_node = get_body_as_nodes(module_node)[0]

    result = ReturnFromGeneratorTransformer().visit(function_node)
    expected = parse_function(source("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """))

    assert compare_ast(result, expected)
    assert fix_python_

# Generated at 2022-06-14 02:07:28.879398
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:07:36.460408
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('''\
        def foo():
            yield 1
            return 5
    ''')

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)

    assert transformer._tree_changed
    assert transformer.modified_tree == ast.parse('''\
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    ''')

# Generated at 2022-06-14 02:07:45.975434
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    @snippet
    def snippet(a):
        yield a
        if a:
            return 5
        else:
            return 6

    class TestTransformer(BaseNodeTransformer):
        def visit_FunctionDef(self, node):
            self.generic_visit(node)  # type: ignore
            return node

    class Test(metaclass=PrepareMetaclass):
        @snippet
        def test(a):
            yield a
            exc = StopIteration()
            exc.value = 5 if a else 6
            raise exc

    transformed = snippet.transformed()
    visitor = TestTransformer()
    visitor.visit(transformed)
    assert Test.test.matches(transformed)

# Generated at 2022-06-14 02:07:53.390450
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    res = ast.parse("""
    def fn():
        yield 1
        return 42
    """)

    expected = ast.parse("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 42
        raise exc
    """)

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(res)

    assert ast.dump(res) == ast.dump(expected)



# Generated at 2022-06-14 02:08:00.765784
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # do_return()
    def do_return():
        yield 1
        return 5

    # do_return_()
    def do_return_():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc

    tree = ast.parse(inspect.getsource(do_return))
    new_tree = ReturnFromGeneratorTransformer.run_pipeline(tree)
    compiled = compile(new_tree, filename="<ast>", mode="exec")
    namespace = {}
    exec(compiled, namespace)
    assert list(namespace["do_return"]()) == list(do_return_())

# Generated at 2022-06-14 02:08:12.639864
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import build_ast, compare_ast

    # Case 1: only one return statement in a function
    input_string = """def fn():
    yield 1
    return 2"""
    expected_output = """def fn():
    yield 1
    exc = StopIteration()
    exc.value = 2
    raise exc"""
    tree = build_ast(input_string)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)
    output = compare_ast(tree, expected_output)
    assert output is True

    # Case 2: no return statements in a function
    input_string = """def fn():
    yield 1"""
    expected_output = """def fn():
    yield 1"""
    tree = build_ast(input_string)
    transformer = ReturnFromGeneratorTransformer()
   

# Generated at 2022-06-14 02:08:14.975388
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse
    from typed_astunparse import unparse

# Generated at 2022-06-14 02:08:28.550679
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(code):
        node = ast.parse(code)
        tran = ReturnFromGeneratorTransformer()
        tran.visit(node)
        return node

    node = test('''
        def fn():
            yield 1
            return 5
            yield 6

        def fn2():
            yield 2
            for i in range(10):
                if i == 5:
                    return 7
                yield 3

        def fn3():
            yield 4
            def fn():
                return 5
            return fn

        def fn4():
            yield 5
            if True:
                return 5

        def fn5():
            yield 6
            return
    ''')


# Generated at 2022-06-14 02:08:30.926425
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:45.709176
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = 'def function(): yield 1 ; return 5'
    tree = ast.parse(code)
    transformer = ReturnFromGeneratorTransformer()
    tree = transformer.visit(tree)
    generated_code = tree_to_str(tree)
    expected_code = 'def function(): yield 1 ; exc = StopIteration() ; exc.value = 5 ; raise exc'
    assert generated_code == expected_code

# Generated at 2022-06-14 02:08:58.553965
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def generator_function():
        yield 1
        return 5

    expected = """def generator_function():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc"""
    source = inspect.getsource(generator_function)
    new_code = compile_from_string(expected, '<foo>', 'exec').co_consts[0]
    original_code = compile_from_string(source, '<foo>', 'exec').co_consts[0]
    visitor = ReturnFromGeneratorTransformer()
    visitor.visit(original_code)
    assert visitor._tree_changed

    assert astor.to_source(original_code) == astor.to_source(new_code)

# Generated at 2022-06-14 02:09:07.284118
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import re
    from textwrap import dedent

    from ..utils.testing import run_node_transform_test
    from ..utils.testing import assertAstEqual, parseAst

    def test_code(code: str) -> None:
        assertAstEqual(
            parseAst(code),
            parseAst(dedent(code))
        )

    def do_test(code):
        run_node_transform_test(ReturnFromGeneratorTransformer, code, test_code)

    do_test("""
        def fn():
            yield 1
            return 5
    """)

    do_test("""
        def fn():
            def inner():
                yield 2
                return 5

            yield 1
            return 5
    """)


# Generated at 2022-06-14 02:09:12.901189
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def check(src_code, expected_result_code):
        src = ast.parse(src_code)
        expected_result = ast.parse(expected_result_code)
        result = ReturnFromGeneratorTransformer().visit(src)
        assert result == expected_result


# Generated at 2022-06-14 02:09:20.579399
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ast_compat import parse, dump_ast
    from ..utils.test import TestGeneratorRunner

    runner = TestGeneratorRunner()
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
    node = parse(source)
    transformed = ReturnFromGeneratorTransformer().visit(node)
    runner.run([dump_ast(transformed)], expected)

# Generated at 2022-06-14 02:09:33.485454
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import FunctionDef, Return, Name, Load, Str

    source = """
        def fn():
            yield 1
            return "str"
    """
    tree = ast.parse(source)

    transformer = ReturnFromGeneratorTransformer()
    new_tree = transformer.visit(tree)

    exc = Name(id='exc', ctx=Load())
    call4 = Call(func=Attribute(value=Name(id='StopIteration', ctx=Load()), attr='value', ctx=Load()), args=[Str(s='str')], keywords=[])
    exc_value = Assign(targets=[Attribute(value=exc, attr='value', ctx=Store())], value=call4)
    raise_exc = Raise(exc=exc, cause=None)
    new_fn_body

# Generated at 2022-06-14 02:09:46.575304
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Create instance of ReturnFromGeneratorTransformer
    transformer = ReturnFromGeneratorTransformer()
    # Create node ReturnFromGeneratorTransformer
    node = FunctionDef(body = [
        Yield(value = Num(n = 1)),
        Return(value = Num(n = 5))
    ])
    # Call visit_FunctionDef
    method_result = transformer.visit_FunctionDef(node)
    # Check results
    assert isinstance(method_result, FunctionDef)
    assert isinstance(method_result.body[0], Yield)
    assert isinstance(method_result.body[0].value, Num)
    assert method_result.body[0].value.n == 1
    assert isinstance(method_result.body[1], Assign)

# Generated at 2022-06-14 02:09:59.003451
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import unittest
    from typed_ast import ast3 as ast
    import itertools
    import sys
    import io

    def dump_to_buffer(node):
        out = io.StringIO()
        sys.stdout = out

        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(node)

        sys.stdout = sys.__stdout__

        lines = out.getvalue().splitlines()
        assert lines[0].strip() == 'def fn(a: int, b: str) -> int:'
        assert lines[1].strip() == '    exc = StopIteration()'
        assert lines[2].strip() == '    exc.value = return_value'
        assert lines[3].strip() == '    raise exc'
        assert lines[4].strip() == '    return 1'

   

# Generated at 2022-06-14 02:10:00.240584
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:01.991817
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:27.457679
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent
    from ..utils.ast import ast_equal_ignore_line_number
    from ..utils.misc import indent_code

    # Case 1: Normal Case
    fn_1 = dedent('''
        def fn_1():
            yield 1
            return 5
    ''')
    fn_1_expected = dedent('''
        def fn_1():
            yield 1

            exc = StopIteration()
            exc.value = 5
            raise exc
    ''')

    # Case 2: Generator without yield
    fn_2 = dedent('''
        def fn_2():
            return 5
    ''')
    fn_2_expected = dedent('''
        def fn_2():
            return 5
    ''')

    # Case 3: Generator with multiple returns
   

# Generated at 2022-06-14 02:10:36.522380
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import unittest as ut

    class ReturnFromGeneratorTransformerTest(ut.TestCase):
        def setUp(self):
            self.maxDiff = None

        def check(self, snippet_: str, expected: str) -> None:
            transformer = ReturnFromGeneratorTransformer()
            node = ast.parse(snippet_, mode="exec")
            new_node = transformer.visit(node)
            self.assertEqual(expected, ast.dump(new_node))


# Generated at 2022-06-14 02:10:50.589289
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    t = ReturnFromGeneratorTransformer()
    fn = ast.FunctionDef(name='fn',
                         body=[ast.Yield(value=ast.Num(1)),
                               ast.Return(value=ast.Num(5))],
                         args=ast.arguments(args=[], vararg=None, kwonlyargs=[],
                                            kw_defaults=[], kwarg=None, defaults=[]))


# Generated at 2022-06-14 02:11:02.441952
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    class TestTransformer(ast.NodeTransformer):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            return node

    from .base import BaseNodeTransformer
    transformer = BaseNodeTransformer.mixin(TestTransformer, [ReturnFromGeneratorTransformer])
    transformer = transformer()

    fn = '''
        @contextmanager
        def ctx():
            yield 'a'
            return 'b'

        def fn():
            yield 1
            return 3
    '''

# Generated at 2022-06-14 02:11:16.494751
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.testing import make_snippet, transform
    from ..utils.testing import assert_node_equal

    # Method test 1: Simple case
    source = make_snippet("""
        def fn():
            yield 1
            return 5
    """)
    expected = make_snippet("""
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """)
    assert_node_equal(transform(source, 3, 2), expected)

    # Method test 2: Function with yield, but without return
    source = make_snippet("""
        def fn():
            yield 1
    """)
    expected = make_snippet("""
        def fn():
            yield 1
    """)

# Generated at 2022-06-14 02:11:24.908310
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = '''
    import math

    def fn(a, b):
        for i, j in zip(a, b):
            yield i, j
        return math.gcd(a, b)

    def gen():
        if True:
            yield 1
            return 2
        elif False:
            yield 3
        else:
            return 4
    '''
    tree = ast.parse(source)
    tf = ReturnFromGeneratorTransformer()
    tree = tf.visit(tree)

# Generated at 2022-06-14 02:11:26.236840
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:34.788213
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Given
    node = ast.parse("""
    def f():
        a = 5
        return a
    """)
    expected_node = ast.parse("""
    def f():
        a = 5
        exc = StopIteration()
        exc.value = a
        raise exc
    """)

    # When
    actual_node = ReturnFromGeneratorTransformer().visit(node)

    # Then
    assert ast.dump(actual_node) == ast.dump(expected_node)


# Generated at 2022-06-14 02:11:37.938015
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:51.636090
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('''
    def fn():
        yield 1
        return 5

    def fn():
        yield 1
        def fn2():
            yield 2
            return 6
        fn2()
        yield 3
        return 5

    ''')
    new_node = ReturnFromGeneratorTransformer().visit(node)

# Generated at 2022-06-14 02:12:30.088309
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = '''
        def fn():
            yield 1
            return 5
    '''
    tree = ast.parse(source)
    ast.fix_missing_locations(tree)

    transformer = ReturnFromGeneratorTransformer(tree)
    transformer.visit(tree)

    expected = '''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    '''
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:12:36.951403
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import textwrap
    from typed_ast import ast3 as ast
    from ..utils.source_code import SourceCode
    from .transformer_test import TransformerTest
    from .remove_no_effect_stmt import RemoveNoEffectStmtTransformer
    from .remove_annotations import RemoveAnnotationsTransformer
    from .remove_metaclass import RemoveMetaclassTransformer

    class FindGeneratorReturnsTest(TransformerTest):
        TRANSFORMER = ReturnFromGeneratorTransformer
        CODE = textwrap.dedent('''
        def generator():
            yield 1
            return 5
            
        def generator_no_yield():
            return 5

        def generator_no_return():
            yield 1
            
        def generator_no_change():
            yield 1
            return 5
            yield 6
        ''')


# Generated at 2022-06-14 02:12:47.522768
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    # Simple test
    body = [ast.Yield(ast.Constant("x")), ast.Return(ast.Constant("y"))]
    final_body = [
        ast.Yield(ast.Constant("x")),
        ast.Assign([ast.Name("exc")], ast.Call(func=ast.Name("StopIteration"),args=[], keywords=[])),
        ast.AugAssign(target=ast.Attribute(value=ast.Name("exc"), attr="value"), op=ast.AugLoad(), value=ast.Constant("y")),
        ast.Raise(exc=ast.Name("exc"), cause=None)
    ]


    # Create a leaf node

# Generated at 2022-06-14 02:12:54.745757
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_astunparse import unparse
    from ..utils.test_utils import get_test_data
    data = get_test_data('generator_return.func_body', 'generator_return.func_body.after')
    func_body = ast.parse(data.before).body[0]
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(func_body)
    expected = unparse(func_body)
    assert expected == data.after

# Generated at 2022-06-14 02:13:02.148873
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from . import test_func as t
    from . import utils as u
    from ..utils.source import source

    transformer = ReturnFromGeneratorTransformer()  # type: ignore
    transformer.visit(t.func_with_return_in_generator)
    assert u.format_ast(t.func_with_return_in_generator) == u.format_ast(source(
    '''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''
    ))

    transformer.visit(t.function_with_try)

# Generated at 2022-06-14 02:13:10.034845
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # -------------- snippet start --------------
    # Function
    def a():
        yield 1
        return 2
    # -------------- snippet end --------------
    # -------------- snippet start --------------
    # Function
    def a():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    # -------------- snippet end --------------
    ReturnFromGeneratorTransformer.verify(a, globals())



# Generated at 2022-06-14 02:13:20.104894
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transform = ReturnFromGeneratorTransformer()
    source = """
        def fn1():
            return 1
        def fn2():
            yield 1
            return 2
        def fn3(v):
            if v:
                yield 1
            return 3
        def fn4():
            for n in [1, 2, 4]:
                yield n
            return 5
        def fn5():
            return
    """

    tree = ast.parse(source)
    transform.visit(tree)

    def return_2_gen():
        for n in [1, 2, 4]:
            yield n
        exc = StopIteration()
        exc.value = 5
        raise exc

    def fn3(v):
        if v:
            yield 1
        exc = StopIteration()
        exc.value = 3
        raise exc

   

# Generated at 2022-06-14 02:13:31.803845
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:13:33.062030
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3
    import copy


# Generated at 2022-06-14 02:13:37.384999
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from . import transform

    code = """
        def foo():
            yield 1
            return 10
    """
    assert transform(code, ReturnFromGeneratorTransformer) == """
        def foo():
            yield 1
            exc = StopIteration()
            exc.value = 10
            raise exc
    """

# Generated at 2022-06-14 02:14:56.155296
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Tests method visit_FunctionDef of class ReturnFromGeneratorTransformer."""
    from .generator_return_input import generator_input_source
    from .generator_return_output import generator_output_source

    tree = ast.parse(generator_input_source)
    expected_tree = ast.parse(generator_output_source)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)

    assert ast.dump(tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:15:07.087821
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.visitor import NodeVisitor
    from ..utils.source_to_ast import source_to_ast
    from ..utils.code_transformer import CodeTransformer
    source = """
        def fn():
            yield 1
            return 2
    """
    code = compile(source_to_ast(source), '<string>', 'exec')
    assert any(isinstance(child, ast.FunctionDef)
               for child in NodeVisitor().visit(code).body)

    new_code = CodeTransformer().visit(code)
    new_source = ast.unparse(new_code)
    expected = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
    """
    assert new_source == expected

# Generated at 2022-06-14 02:15:15.597579
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    tree = ast.parse('''
    def generator1():
        yield 1
        return 5
    ''')
    transformer.visit(tree)
    expected = '''
    def generator1():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    '''
    assert ast.dump(tree) == expected



# Generated at 2022-06-14 02:15:26.823849
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import parse
    node = parse('def fn():\n    yield 1\n    return 5').body[0]
    assert node.body[0].value == 1
    assert node.body[1].value == 5
    transformer = ReturnFromGeneratorTransformer()
    node = transformer.visit(node)

    # tree is changed
    assert transformer.tree_changed

    # nothing to yield
    assert node.body[0].value == 1
    # return changed
    assert isinstance(node.body[1], ast.Expr)
    assert isinstance(node.body[1].value, ast.Raise)
    assert isinstance(node.body[1].value.exc, ast.Call)
    assert isinstance(node.body[1].value.exc.func, ast.Name)

# Generated at 2022-06-14 02:15:34.567510
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import parse, get_ast
    from ..visitor import Visitor
    from ..parser import parse_block

    class VisitorForTest(Visitor):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            """Does not change function."""
            return node

    def _get_tree(src: str, version: Tuple[int, int]) -> ast.Module:
        source = parse(src)
        tree = get_ast(source, version=version)
        visitor = VisitorForTest()
        visitor.visit(tree)
        return tree

    def _get_fn_name(src: str) -> str:
        tree = _get_tree(src, (3, 6))
        assert len(tree.body) == 1

# Generated at 2022-06-14 02:15:45.136941
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import to_source
    from .exceptions import UnsupportedError

    from .docstrings import DocstringTransformer
    from .literals import LiteralsTransformer
    from .functions import FunctionTransformer
    from .assignments import AssignmentsTransformer
    from .imports import ImportsTransformer
    from .control_structures import ControlStructuresTransformer
    from .exceptions import ExceptionsTransformer
    from .comprehensions import ComprehensionsTransformer
    from .classes import ClassesTransformer
    from .decorators import DecoratorsTransformer
    from .arguments import ArgumentsTransformer
    from .logic import LogicTransformer
    from .expressions import ExpressionsTransformer


# Generated at 2022-06-14 02:15:46.669586
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:15:53.777993
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..astunparse import unparse

    original_code = """
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

    tree = ast.parse(original_code)
    ReturnFromGeneratorTransformer().visit(tree)
    assert unparse(tree) == expected_code

