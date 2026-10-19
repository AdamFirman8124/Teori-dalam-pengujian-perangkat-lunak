

# Generated at 2022-06-14 02:06:04.195388
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:06:14.418805
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    source = """
    def foo():
        yield 1
        return 1
    def bar():
        return 1
    def baz():
        yield 1
        yield 2
        return 1
    def quz():
        yield 1
        for x in range(5):
            print(x)
        return 1
    """

    expected = """
    def foo():
        yield 1
        exc = StopIteration()
        exc.value = 1
        raise exc
    def bar():
        return 1
    def baz():
        yield 1
        yield 2
        exc = StopIteration()
        exc.value = 1
        raise exc
    def quz():
        yield 1
        for x in range(5):
            print(x)
        exc = StopIteration()
        exc.value = 1
        raise exc
    """



# Generated at 2022-06-14 02:06:25.220442
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ...tests.mixins import CodegenTestCaseMixin
    from ...utils.testing import assert_equal_code

    class ReturnFromGeneratorTestCase(CodegenTestCaseMixin, unittest.TestCase):

        @staticmethod
        def _make_generator():
            yield 1  # noqa

        @staticmethod
        def _make_generator_with_return(value):
            yield 1  # noqa
            return value  # noqa

    ReturnFromGeneratorTestCase.do_test_code_vs_tree(
        lambda: ReturnFromGeneratorTestCase._make_generator(),
        'def _make_generator():\n'
        '    yield 1\n'
    )


# Generated at 2022-06-14 02:06:29.173366
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import check
    from .test_utils import transform

    def test(input_code, expected_code):
        check(input_code, expected_code, transform(ReturnFromGeneratorTransformer))

    test(
        """
        def fn():
            yield 5
            return 6
        """,
        """
        def fn():
            yield 5
            exc = StopIteration()
            exc.value = 6
            raise exc
        """
    )


# Generated at 2022-06-14 02:06:31.637657
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import parse
    from .test_helpers import roundtrip_unparse, roundtrip_visit

# Generated at 2022-06-14 02:06:39.678894
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from collections import defaultdict
    from .base import BaseNodeTransformer
    from .return_from_generator import ReturnFromGeneratorTransformer
    from ..utils.source import Source, normalize
    from ..utils.sourcetree import ast_to_sourcetree, sourcetree_to_ast, sourcetree_to_source

    def assert_transformation(source_code_in, source_code_out):
        source_tree_in = ast_to_sourcetree(ast.parse(normalize(source_code_in)))

        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(sourcetree_to_ast(source_tree_in))
        assert transformer._tree_changed is True
        assert_tree = sourcet

# Generated at 2022-06-14 02:06:49.662141
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test case 1
    # Code
    code1 = """
    def fn():
        yield 1
        return 5
    """
    # Expected AST
    ast1_expected = ast.parse(
        """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    )
    # Transform code1
    ast1 = ast.parse(code1)
    ast1_transformed = ReturnFromGeneratorTransformer().visit(ast1)
    # Assert
    assert astor.to_source(ast1_transformed) == astor.to_source(ast1_expected)

    # Test case 2
    # Code
    code2 = """
    def fn():
        return 5
    """
    # Expected AST

# Generated at 2022-06-14 02:06:51.875757
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_fn():
        yield 1
        return 5


# Generated at 2022-06-14 02:07:02.581583
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from .base import BaseNodeTransformer
    from .base import BaseCodeGenerator
    from .base import BaseNodeVisitor
    from .base import NodeTransformerError
    from .base import NodeVisitorError
    from .base import CodeGeneratorError
    from ..utils.snippet import snippet, let
    from ..utils.combinators import OnSuccess
    from ..utils.combinators import OneOrMore
    from ..utils.combinators import ZeroOrMore
    from ..utils.combinators import Optional
    from ..utils.combinators import Or
    from ..utils.combinators import Forward
    from ..utils.combinators import Apply

# Generated at 2022-06-14 02:07:04.244247
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .. import compiler
    from ..transformer import TransformerSequence


# Generated at 2022-06-14 02:07:13.037203
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_code(code):
        node = ast.parse(code)
        ReturnFromGeneratorTransformer().visit(node)
        exec(compile(node, "<string>", "exec"))


# Generated at 2022-06-14 02:07:14.277089
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    t = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:07:30.025805
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import ast as pyast

    t = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:07:37.190510
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
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
    tree = ast.parse(source)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    tree = ast.fix_missing_locations(tree)
    asse

# Generated at 2022-06-14 02:07:41.246861
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        yield 1
        return 5

    tree = ast.parse(inspect.getsource(fn))
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)


# Generated at 2022-06-14 02:07:54.811915
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_node_data import test_node_data_visit


# Generated at 2022-06-14 02:08:04.486913
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_fn(a):
        yield b
        return a
    test_fn = ast.parse(dedent(test_fn.__doc__)).body[0]
    trans = ReturnFromGeneratorTransformer()
    res = trans.visit(test_fn)
    assert isinstance(res, ast.FunctionDef)

# Generated at 2022-06-14 02:08:05.405135
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
  assert False

# Generated at 2022-06-14 02:08:14.168935
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class ReturnFromGeneratorTransformerSubclass(ReturnFromGeneratorTransformer):
        def __init__(self):
            self.visit_FunctionDef_called = False
            self.generic_visit_called = False
            self._tree_changed = False

        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            self.visit_FunctionDef_called = True
            return super(ReturnFromGeneratorTransformerSubclass, self).visit_FunctionDef(node)

        def generic_visit(self, node: ast.AST) -> ast.AST:
            self.generic_visit_called = True
            return node

    obj = ReturnFromGeneratorTransformerSubclass()
    obj.visit(ast.parse('''def fn():
        yield 1
        return 5'''))


# Generated at 2022-06-14 02:08:27.754897
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .support import get_ast_of_string
    from ..utils.snippet import snippets
    from typed_ast import ast3 as ast
    # Define a source code snippet
    code_to_test = snippets["decorator_on_def"]
    # Get the corresponding AST
    root = get_ast_of_string(code_to_test)
    root.body[0].body = [ast.Return(value=ast.Constant(value=None), lineno=1, col_offset=0)]
    # Create a transformer object
    transformer = ReturnFromGeneratorTransformer()
    # Apply the transformation
    transformer.visit(root)
    # Check that the result is what you expect

# Generated at 2022-06-14 02:08:41.518346
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ...ast_utils import get_ast
    from ... import transforms

    source = """
        def fn():
            yield 1
            return 5
    """
    node = get_ast(source)

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(node)

    result = transforms.unparse(node)
    expected = """
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    assert result == expected


# Generated at 2022-06-14 02:08:54.822025
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    text = """
    def foo():
        yield 1
        return 5

    def bar():
        yield 1
        if True:
            return 5
        else:
            return 6
    """

    ast_tree = ast.parse(text)
    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(ast_tree)
    lines = ast.unparse(ast_tree).split('\n')

    def strip_leading_spaces(line):
        return line[4:]

    strip_lines = [strip_leading_spaces(line) for line in lines]


# Generated at 2022-06-14 02:09:01.893846
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = textwrap.dedent('''
    def fn():
        yield 1
        return 2
    ''')

    expected = textwrap.dedent('''
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    ''')

    tree = ast.parse(source)
    transformer = ReturnFromGeneratorTransformer()
    new_tree = transformer.visit(tree)

    compare_ast(expected, new_tree)

# Generated at 2022-06-14 02:09:12.557910
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class ReturnFromGeneratorTransformerSubclass(ReturnFromGeneratorTransformer):
        def __init__(self):
            self.generator_returns = []
            self._tree_changed = False

        def _find_generator_returns(self, node):
            return self.generator_returns

    node = ast.parse("""
        def fn():
            yield 1
            for i in range(10):
                return 5
    """)
    function_def = node.body[0]
    return_ = function_def.body[1].body[0].body[0]
    transformer = ReturnFromGeneratorTransformerSubclass()
    transformer.generator_returns.append((function_def, return_))
    new_ast = transformer.visit(node)

# Generated at 2022-06-14 02:09:21.450989
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .return_from_generator import ReturnFromGeneratorTransformer

    inherit_docstring = ast.parse("""
    def sequencer_without_return(n):
        for item in range(n):
            yield item
            if item == 2:
                return
    """).body[0]

    sequencer_with_return = ast.parse("""
    def sequencer_with_return(n):
        for item in range(n):
            yield item
            if item == 2:
                return 5
    """).body[0]

    sequencer_with_return_multiple = ast.parse("""
    def sequencer_with_return(n):
        for item in range(n):
            if item == 2:
                return 5
            yield item
    """).body[0]

    sequencer_with_inner_return

# Generated at 2022-06-14 02:09:23.264669
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:09:31.090938
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import parse
    tree = parse("""
    def fn():
        yield 1
        return 2
    """)
    fixed_tree = parse("""
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """)
    transformer = ReturnFromGeneratorTransformer()
    assert transformer.visit(tree) == fixed_tree

# Generated at 2022-06-14 02:09:44.585881
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test(body):
        node = ast.parse(body).body[0]
        return ReturnFromGeneratorTransformer().visit(node)
    # Generator without return should not be changed
    node = ast.parse('def fn(): yield 1; yield 2')
    node = ReturnFromGeneratorTransformer().visit(node)
    assert node.body[0].body[0].value.value == 1
    assert node.body[0].body[1].value.value == 2

    # Return without value should not be changed
    node = test('def fn(): yield 1; return')
    assert node.body[0].body[0].value.value == 1
    assert isinstance(node.body[0].body[1], ast.Return)

    # Return with value should be changed

# Generated at 2022-06-14 02:09:46.393927
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from pprint import pprint
    from typed_ast._ast3 import parse as parsed

# Generated at 2022-06-14 02:09:57.862508
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Setup
    node = ast.parse(
        'def fn():\n'
        '    yield 1\n'
        '    return 5'
    ).body[0]  # type: ignore
    expected = ast.parse(
        'def fn():\n'
        '    yield 1\n'
        '    exc = StopIteration()\n'
        '    exc.value = 5\n'
        '    raise exc'
    ).body[0]  # type: ignore

    # Exercise
    transformer = ReturnFromGeneratorTransformer()
    actual = transformer.visit(node)  # type: ignore

    # Verify
    assert ast.dump(actual) == ast.dump(expected)



# Generated at 2022-06-14 02:10:19.533314
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    function_definition = ast.parse(
        """def fn():
            yield 1
            return 5"""
    ).body[0]
    expected = ast.parse(
        """def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc"""
    ).body[0]
    actual = ReturnFromGeneratorTransformer().visit(function_definition)
    assert ast.dump(expected) == ast.dump(actual)


# Generated at 2022-06-14 02:10:29.539009
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def gen_with_return():
        yield 1
        yield 2
        yield 3
        return 4

    def gen_without_return():
        yield 1
        yield 2
        yield 3

    tree_with_return = ast.parse(inspect.getsource(gen_with_return))
    tree_without_return = ast.parse(inspect.getsource(gen_without_return))

    transformer = ReturnFromGeneratorTransformer(tree_with_return)
    assert transformer._tree_changed is True
    transformer.visit(tree_with_return)

    transformer = ReturnFromGeneratorTransformer(tree_without_return)
    assert transformer._tree_changed is False
    transformer.visit(tree_without_return)

    node_with_return = tree_with_return.body[0]  # type: ignore
    node

# Generated at 2022-06-14 02:10:40.243668
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    source = '''
    # This is a comment
    def fn():
        yield 1  # Comment
        return 5'''

    def actual():
        module = ast.parse(source)
        checker = ReturnFromGeneratorTransformer()
        checker.visit(module)
        module_out = ast.fix_missing_locations(module)
        return ast.unparse(module_out)

    expected = '''
    # This is a comment
    def fn():
        yield 1  # Comment
        exc = StopIteration()
        exc.value = 5
        raise exc'''
    assert actual() == expected



# Generated at 2022-06-14 02:10:42.052819
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:52.186339
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # assert_equal is used instead of assert_same_ast to ignore line numbers
    # generated by typed_ast.
    assert_equal(
        ReturnFromGeneratorTransformer().visit(
            ast.parse("""def fn():
    yield 1
    return 5""")
        ),
        ast.parse("""def fn():
    yield 1
    exc = StopIteration()
    exc.value = 5
    raise exc""")
    )

    assert_equal(
        ReturnFromGeneratorTransformer().visit(
            ast.parse("""def fn():
    return 5""")
        ),
        ast.parse("""def fn():
    return 5""")
    )


# Unit tests for method _find_generator_returns of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:10:53.474142
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:04.284662
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformer
    from .base import BaseNodeTransformerTests
    from .base import node_factory
    from .. import Tree
    import unittest
    import ast

    # test data
    #################
    class TestData(object):
        class TestUnit(object):
            def __init__(self, input_ast, expect_ast, expect_changed):
                self.input_ast = input_ast
                self.expect_ast = expect_ast
                self.expect_changed = expect_changed

    class TestUnitBasic(TestData.TestUnit):
        def __init__(self, input_ast_str, expect_ast_str, expect_changed=True):
            self.input_ast = node_factory(input_ast_str)
            self.expect_ast = node_f

# Generated at 2022-06-14 02:11:18.144209
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    # Test case where return is not in a generator
    node = ast.parse(
        """
        def f():
            return 1
        """
    )
    transformer = ReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)
    assert transformer._tree_changed == False
    assert ast.dump(new_node) == ast.dump(node)

    # Test case where return is in a generator without other return statements
    node = ast.parse(
        """
        def f():
            yield 1
            return 1
        """
    )
    transformer = ReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)
    assert transformer._tree_changed == True

# Generated at 2022-06-14 02:11:25.229474
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    t = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:11:33.351123
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for ReturnFromGeneratorTransformer.visit_FunctionDef"""
    node = ast.parse("""
        def generator():
            yield 1
            return 'a'
    """).body[0]

    expected = ast.parse("""
        def generator():
            yield 1
            exc = StopIteration()
            exc.value = 'a'
            raise exc
    """).body[0]

    ReturnFromGeneratorTransformer()(node)

    assert node == expected

# Generated at 2022-06-14 02:12:08.811109
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert_code_equal(
        """
        def a():
            yield 1
            return 5
        """,
        """
        def a():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """
    )



# Generated at 2022-06-14 02:12:12.822221
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def check(before, after):
        node = ast.parse(before)
        new_node = ReturnFromGeneratorTransformer().visit(node)
        assert ast.dump(new_node) == ast.dump(ast.parse(after))


# Generated at 2022-06-14 02:12:14.008440
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:14.741296
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:25.787921
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import assert_source

    source = '''
    def fn():
        yield 1
        if a:
            return 5

    def fn2():
        yield 1
        try:
            return 6
        except:
            pass

    def fn3():
        yield 1
        if a:
            return 5
        else:
            return 6

    def fn4():
        yield 1
        if a:
            return 5
        elif b:
            return 6
        else:
            return 7

    def fn5():
        yield 1
        while True:
            if a:
                return 5
            elif b:
                return 6
            else:
                return 7
    '''

# Generated at 2022-06-14 02:12:26.406624
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:27.996776
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:38.275293
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.typed_ast import ast3 as ast
    func_1 = ast.parse("""
        def some_function(a,b,c):
            yield a
            yield b
            return c
        """, mode='exec').body[0]
    func_2 = ast.parse("""
        def some_function(a,b,c):
            exc = StopIteration()
            exc.value = c
            raise exc""", mode='exec').body[0]
    func_to_check = ReturnFromGeneratorTransformer().visit(func_1)
    assert func_to_check == func_2

# Generated at 2022-06-14 02:12:39.946900
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()


# Generated at 2022-06-14 02:12:51.238878
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    _ct = ReturnFromGeneratorTransformer()
    assert _ct.target == (3, 2)

    _tree = ast.parse("""\
    def fn():
        yield 1
        return 5
        """)

    _ct.visit(_tree)

    assert ast.dump(_tree) == "Module(body=[FunctionDef(name='fn', args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Yield(value=Num(n=1))), Expr(value=Call(func=Name(id='return_from_generator', ctx=Load()), args=[Num(n=5)], keywords=[])), Return(value=None)], decorator_list=[], returns=None)])"
   

# Generated at 2022-06-14 02:14:06.585433
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert_equal(
        ast.fix_missing_locations(ReturnFromGeneratorTransformer().visit(
            ast.parse(textwrap.dedent(
                """\
                def fn():
                    yield 1
                    return 5
                """
            ))
        )),
        ast.fix_missing_locations(ast.parse(textwrap.dedent(
            """\
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
            """
        )))
    )


# Generated at 2022-06-14 02:14:14.594915
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    s = """
    def k(a):
        yield a
        return a
    """

    expected = """
    def k(a):
        yield a
        exc = StopIteration()
        exc.value = a
        raise exc
    """

    node = ast.parse(s)
    node = ReturnFromGeneratorTransformer().visit(node)  # type: ignore
    actual = ast.fix_missing_locations(node)
    actual = ast.unparse(actual)
    assert actual == expected

# Generated at 2022-06-14 02:14:24.793274
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def test_function():
        yield 1
        return 2
    expected = "def test_function(): yield 1; exc = StopIteration(); exc.value = 2; raise exc;"
    compiled = compile(ast.parse(expected), '<test>', 'exec')
    module = types.ModuleType(__name__)
    eval(compiled, module.__dict__)

    self = ReturnFromGeneratorTransformer()
    fn = test_function
    node = ast.parse(inspect.getsource(fn))
    transformed = self.visit(node)
    code = compile(transformed, '<test>', 'exec')
    module = types.ModuleType(__name__)
    eval(code, module.__dict__)
    assert fn() == module.test_function()

# Generated at 2022-06-14 02:14:27.353733
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    """
    Consider the following code snippet:
    def fn():
        yield 1
        return 5
    """

# Generated at 2022-06-14 02:14:36.061583
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent
    from ..transformer.return_from_generator import ReturnFromGeneratorTransformer
    from ..utils.snippet import snippet
    from ..utils.ast_writer import ast_writer

    # Test without yield (no changes are expected)
    with snippet:
        def fn():
            return 1

    input_ast = ast_writer.dumps_ast(fn)
    expected_ast = ast_writer.dumps_ast(fn)
    transformer = ReturnFromGeneratorTransformer()
    got_ast = transformer.visit(input_ast)
    assert got_ast == expected_ast

    # Test with yield, return should be replaced
    with snippet:
        def fn():
            yield 1
            return 2

    input_ast = ast_writer.dumps_ast(fn)

# Generated at 2022-06-14 02:14:48.393478
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import generate_ast_code
    for fn_name, args, kwargs in [
        ('foo', (), dict(a=1, b=2, c=3)),
        ('bar', (1,), dict(b=2)),
    ]:
        fn = f'''def {fn_name}({', '.join(args)}):
            yield 1
            return 5
        '''
        ast_fn = generate_ast_code(fn)
        expected_fn = f'''def {fn_name}({', '.join(args)}):
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        '''
        expected_ast_fn = generate_ast_code(expected_fn)

# Generated at 2022-06-14 02:15:01.230166
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse
    snippet = """
                def make_counter():
                    n = 0
                    while True:
                        if n == 5:
                            return n
                        else:
                            yield n
                            n += 1
                """
    tree = ast.parse(snippet)
    result_tree = ReturnFromGeneratorTransformer().visit(tree)
    result_tree_code = astunparse.unparse(result_tree)
    expected_code = """
                def make_counter():
                    n = 0
                    while True:
                        if n == 5:
                            exc = StopIteration()
                            exc.value = n
                            raise exc
                        else:
                            yield n
                            n += 1
                """
    assert result_tree_code == expected_code

# Generated at 2022-06-14 02:15:15.791488
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """
    Test ReturnFromGeneratorTransformer._find_generator_returns method
    """
    function_body_list_with_yield_and_return = [
            ast.Expr(
                value=ast.Yield(
                    value=ast.Constant(value=1, kind=None),
                    kind=None
                    )
                ),
            ast.Return(
                value=ast.Constant(value=5, kind=None)
                )
            ]


# Generated at 2022-06-14 02:15:17.906603
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .basic_transformations import DummyTransformer
    import astor


# Generated at 2022-06-14 02:15:28.529790
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    source = """
    def f1():
        return 1
    def f2():
        yield 1
        return 2
    """
    tree = ast.parse(source)
    transformer.visit(tree)
    expected = """
    def f1():
        return 1
    def f2():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc
    """
    assert ast.dump(tree) == expected

if __name__ == "__main__":
    import sys
    import os
    import unittest
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from tests.test_all_transformers import TestAllTransformers
   