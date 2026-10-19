

# Generated at 2022-06-14 02:06:03.425114
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    generator_returns = ReturnFromGeneratorTransformer()._find_generator_returns(
        ast.parse(
            """
            def fn():
                yield 1
                return 5
            """
        ).body[0]
    )
    assert generator_returns
    parent, return_ = generator_returns[0]
    assert isinstance(parent, ast.FunctionDef)
    assert isinstance(return_, ast.Return)
    assert return_.value.n == 5

    ReturnFromGeneratorTransformer()._replace_return(parent, return_)

# Generated at 2022-06-14 02:06:10.446088
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    transformer = ReturnFromGeneratorTransformer()
    tree = ast.parse(
        """
        def generator():
            yield 1
            return 2
        """
    )
    tree = transformer.visit(tree)
    expected_tree = ast.parse(
        """
        def generator():
            yield 1
            exc = StopIteration()
            exc.value = 2
            raise exc
        """
    )

    assert ast.dump(tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:06:21.634017
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from typed_ast.exceptions import *
    from typed_ast.transforms import *
    from typed_ast.transforms.ReturnFromGeneratorTransformer import *
    from typed_ast.transforms.BaseNodeTransformer import *

    class TestReturnFromGeneratorTransformer(BaseNodeTransformer):
        def __init__(self, tree):
            super().__init__(tree)
            self._tree_changed = False

        def visit_FunctionDef(self, node):
            node = node
            return node
    #

# Generated at 2022-06-14 02:06:28.041337
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    code = """
        def return_from_generator_transformer_visit_FunctionDef():
            yield 1
            return 5
    """
    expected = """
        def return_from_generator_transformer_visit_FunctionDef():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
    """
    tree = ast.parse(code).body[0]
    tree = ReturnFromGeneratorTransformer.run_pipeline(tree)
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:06:37.755513
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    func_def = ast.FunctionDef(name='foo', args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[ast.Expr(value=ast.Yield(value=ast.Num(n=1))), ast.Return(value=ast.Num(n=2))], decorator_list=[], returns=None)


# Generated at 2022-06-14 02:06:45.938646
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node_to_test = ast.parse("""def fn():
    yield 1
    return 4
  """)

    expected_result = ast.parse("""def fn():
    yield 1
    exc = StopIteration()
    exc.value = 4
    raise exc
  """)

    actual_result = ReturnFromGeneratorTransformer().visit(node_to_test)
    print(ast.dump(actual_result))
    assert ast.dump(actual_result) == ast.dump(expected_result)


# Generated at 2022-06-14 02:06:57.866051
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astunparse
    from .base import BaseNodeTransformerTest
    from ..utils.ast_helper import print_node, parse_ast, ast_equals

    base_node_transformer_test = BaseNodeTransformerTest(
        transformer_class=ReturnFromGeneratorTransformer,
        method_name='visit_FunctionDef',
    )

    simple_generator = """\
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
    assert ast_equals(expected, base_node_transformer_test.test_single_snippet(simple_generator))


# Generated at 2022-06-14 02:07:07.420372
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    ast1 = ast.parse('def fn(): yield 1')
    ast2 = ast.parse('def fn(): return 1')
    ast3 = ast.parse('def fn(): yield 1; return 1')
    ast4 = ast.parse('def fn(): for i in [1, 2, 3]: return i')
    ast5 = ast.parse('def fn(): yield from [1, 2, 3]')
    ast6 = ast.parse('def fn(): 1; yield 2')
    ast7 = ast.parse('def fn(): return 1; yield 2')
    ast8 = ast.parse('def fn(): print(1); return 1')

    transformer = ReturnFromGeneratorTransformer()
    c_ast1 = transformer.visit(ast1)
    c_ast2 = transformer.visit(ast2)
    c_ast3 = transformer.vis

# Generated at 2022-06-14 02:07:20.623433
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ...imports import ImportTransformer
    from ...docstring import DocstringTransformer
    from ...lambda_ import LambdaTransformer
    from ...name import NameTransformer
    from ...print_ import PrintTransformer
    from ...assert_ import AssertTransformer
    from ...import_ import ImportStringTransformer
    from ...raise_ import RaiseTransformer

    source = """
        import a

        def fn():
            yield 1
            return 5


        class A:
            if True:
                yield 1
                return 5


        class B:
            @a
            def fn(self):
                yield 1
                return 5
    """


# Generated at 2022-06-14 02:07:33.023911
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse("""
    def fn():
        yield 1
        return 2
    """)
    tree = ReturnFromGeneratorTransformer().visit(tree)

# Generated at 2022-06-14 02:07:43.027780
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_helpers import assert_node_tree, get_ast


# Generated at 2022-06-14 02:07:54.049348
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from textwrap import dedent
    from ..utils import fix
    from .asdl import Python3_6ASDL

    code = dedent('''\
    def generator():
        for i in range(10):
            yield i
        return 5
    ''')
    expected = dedent('''\
    def generator():
        for i in range(10):
            yield i
        exc = StopIteration()
        exc.value = 5
        raise exc
    ''')

    tree, module = Python3_6ASDL.cast(ast.parse(code, mode='exec'))
    fixed = fix(module, [ReturnFromGeneratorTransformer])
    result = ast.unparse(fixed).strip()
    assert result == expected

# Generated at 2022-06-14 02:08:03.743232
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source import source_to_unicode
    from ..utils.ast import print_ast

    code = source_to_unicode('''
        def fn():
            yield 1
            return 2
            return 3

        def fn2():
            yield from (1, 2, 3)
            return 2
            return 3

        def fn3():
            yield 1
            return 2
            yield 3

        def fn4():
            yield 1
            yield 2
            yield 3
    ''')

    tree = ast.parse(code)
    ReturnFromGeneratorTransformer().visit(tree)


# Generated at 2022-06-14 02:08:13.882645
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast.ast3 import Module
    from ..utils.sourcecode import to_source
    from .fake_typed_ast import FakeTypedAst
    fake_typed_ast = FakeTypedAst(3, 2)
    module = Module([fake_typed_ast.function(
        name="simple",
        return_type=fake_typed_ast.Yield(fake_typed_ast.Num(1)),
        body=[fake_typed_ast.Return(fake_typed_ast.Num(5))],
    )])
    assert to_source(module) == "def simple():\n    yield 1\n    return 5\n"
    ReturnFromGeneratorTransformer().visit(module)

# Generated at 2022-06-14 02:08:15.638470
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:26.183094
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..testing.utils import build_and_run_unittest
    code = """
    def fn():
        yield 1
        return 5
    """
    cleaned_code = """
    def fn():
        yield 1
        exc = StopIteration()
        exc.value = 5
        raise exc
    """
    self_obj = build_and_run_unittest(ReturnFromGeneratorTransformer, code, cleaned_code)
    assert self_obj._find_generator_returns(self_obj.node) == [(self_obj.node, self_obj.node.body[1])]

# Generated at 2022-06-14 02:08:37.135776
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:08:38.497202
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.fixtures import get_example_ast

# Generated at 2022-06-14 02:08:48.887334
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """
    Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
    """
    from ..utils.test_utils import generate_source_code
    from ..utils.test_utils import function_definition_1
    i = ReturnFromGeneratorTransformer()
    ast_module = function_definition_1()
    x = i.visit(ast_module)

    print(generate_source_code(ast_module))

# Generated at 2022-06-14 02:09:02.014579
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """Unit test for method visit_FunctionDef of class
    ReturnFromGeneratorTransformer"""
    import astor
    generator_function_def = ast.parse(
        "def generator_function():\n"
        "    yield 1\n"
        "    return 5").body[0]

    old_body = generator_function_def.body[:]
    new_function_def = ReturnFromGeneratorTransformer().visit(generator_function_def)
    assert astor.to_source(new_function_def) == (
        "def generator_function():\n"
        "    yield 1\n"
        "    exc = StopIteration()\n"
        "    exc.value = 5\n"
        "    raise exc")
    assert new_function_def.body == old_body

# Generated at 2022-06-14 02:09:08.265367
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():

    from ..utils import get_node
    from ..utils import compare_ast


# Generated at 2022-06-14 02:09:16.308874
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import compile_to_ast, parse_ast

    code = '''def fn():
    yield x
    return y
'''
    expected = '''def fn():
    yield x
    exc = StopIteration()
    exc.value = y
    raise exc
'''

    tree = parse_ast(code)
    ReturnFromGeneratorTransformer().visit(tree)
    ast_code = compile_to_ast(tree)
    assert ast_code == expected

# Generated at 2022-06-14 02:09:17.859313
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    t = ReturnFromGeneratorTransformer()

# Generated at 2022-06-14 02:09:28.298589
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import BaseNodeTransformer
    from .line_offset_to_lineno_transformer import LineOffsetToLinenoTransformer
    from typed_ast import ast3 as ast

    code_str = '''
if a():
    def f():
        yield 1
        return 2
    print(f())
'''
    expected_code_str = '''
if a():
    def f():
        yield 1
        exc = StopIteration()
        exc.value = 2
        raise exc

    print(f())
'''
    expected_code = ast.parse(expected_code_str)
    code = ast.parse(code_str)
    LineOffsetToLinenoTransformer().visit(code)
    ReturnFromGeneratorTransformer().visit(code)

# Generated at 2022-06-14 02:09:39.937137
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    source = """
    def fn():
        1
        yield 3
        if True:
            return 5
        if False:
            return 6
        5
    """

    expected = """
    def fn():
        1
        yield 3
        if True:
            exc = StopIteration()
            exc.value = 5
            raise exc
        if False:
            exc = StopIteration()
            exc.value = 6
            raise exc
        5
    """
    module = ast.parse(source)  # type: ignore
    expected = ast.parse(expected).body[0]  # type: ignore
    fn = module.body[0]
    ReturnFromGeneratorTransformer().visit(fn)
    assert str(fn) == str(expected)


# Generated at 2022-06-14 02:09:47.419544
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import assert_function_def_equal, ast_parse
    from .identity import IdentityTransformer

    transformer = IdentityTransformer()
    transformer.register_transformer(ReturnFromGeneratorTransformer)

    # test: def fn():
    #         yield 1
    #         return 5
    #     ->
    #     def fn():
    #         yield 1
    #         exc = StopIteration()
    #         exc.value = 5
    #         raise exc


# Generated at 2022-06-14 02:10:02.326307
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def run_test(snippet):
        # type: (str) -> str
        module_node = ast.parse(snippet)  # type: ignore
        transformer = ReturnFromGeneratorTransformer()
        transformer.visit(module_node)
        return module_node

    def check(snippet):
        # type: (str) -> str
        expected = snippet.replace(
            "return 5",
            "exc = StopIteration()\n"
            "exc.value = 5\n"
            "raise exc",
        )
        assert str(run_test(snippet)) == expected
        return expected

    snippet1 = """
        def fn():
            def inner_fn():
                return 5
    """

# Generated at 2022-06-14 02:10:13.047264
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class Dummy(ast.AST):
        def __init__(self):
            self.body = []

    source = 'def x():\n' \
             '    yield 1\n' \
             '    return 5'

    tree = ast.parse(source)
    assert type(tree.body[0]) is ast.FunctionDef

    fn = tree.body[0]
    fn.returns = ast.Name('', ast.Load())
    fn.body = ast.Module(body=tree.body[0].body).body

    transformer = ReturnFromGeneratorTransformer()
    transformer.visit(tree)
    output = ast.fix_missing_locations(tree)

    assert output.body[0].body[1].value.func.id == 'StopIteration'

# Generated at 2022-06-14 02:10:25.357023
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from .testutils import make_function_def
    def_node = make_function_def(
        "fn",
        ["a"],
        [
            ast.Yield(ast.Num(42)),
            ast.Return(ast.Num(5))
        ])
    

# Generated at 2022-06-14 02:10:34.683915
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import typed_astunparse
    from flake8_typing_imports.visitors.typing_fixer import TypingImportsTransformer
    node = ast.parse("""
    def fn():
        yield 1
        return 5""")

    node = TypingImportsTransformer.run_visitor(node)
    node = ReturnFromGeneratorTransformer.run_visitor(node)
    result = typed_astunparse.unparse(node)

    assert result == '\n' \
        'def fn():\n' \
        '    yield 1\n' \
        '    exc = StopIteration()\n' \
        '    exc.value = 5\n' \
        '    raise exc\n'

# Generated at 2022-06-14 02:10:47.953593
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('''
        def fn():
            yield 1
            return 1
    ''')

    expected_node = ast.parse('''
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 1
            raise exc
    ''')

    node = ReturnFromGeneratorTransformer().visit(node)
    assert ast.dump(node) == ast.dump(expected_node)



# Generated at 2022-06-14 02:10:56.431338
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_equal_source
    from ..utils.ast_utils import dump_ast

    assert_equal_source(
        dump_ast(ReturnFromGeneratorTransformer().visit(ast.parse('''
            def fn():
                yield 1
                return 5
        '''))), '''
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
        ''')

# Generated at 2022-06-14 02:11:07.188665
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    node = ast.parse('def fn(): yield 1; return 5; return 2;')
    transformer = ReturnFromGeneratorTransformer()
    new_node = transformer.visit(node)

# Generated at 2022-06-14 02:11:15.317424
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from .base import BaseNodeTestCase
    from .base import NodeTransformerTestCase

    class ReturnFromGeneratorTransformer(BaseNodeTransformer):
        """Compiles return in generators like:
            def fn():
                yield 1
                return 5
        To:
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
        """
        target = (3, 2)

        def _find_generator_returns(self, node):
            """Using bfs find all `return` statements in function."""
            to_check = [(node, x) for x in node.body]  # type: ignore
            returns = []
            has_yield = False

# Generated at 2022-06-14 02:11:24.644322
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    import astor
    from .base import BaseNodeTransformer

    class TestReturnFromGeneratorTransformer(BaseNodeTransformer):
        target = (3, 2)

        def _find_generator_returns(self, node: ast.FunctionDef) \
                -> List[Tuple[ast.stmt, ast.Return]]:
            """Using bfs find all `return` statements in function."""
            to_check = [(node, x) for x in node.body]
            returns = []
            has_yield = False
            while to_check:
                parent, current = to_check.pop()

                if isinstance(current, ast.FunctionDef):
                    continue
                elif hasattr(current, 'value'):
                    to_check.append((current, current.value))

# Generated at 2022-06-14 02:11:37.349823
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn1():
        yield 1
        return 5
    def fn2():
        yield 5
    def fn3():
        return 5
    def fn4():
        yield
    def fn5():
        yield
        return 5
    def fn6():
        yield
        for x in [1,2,3]:
            yield x
            return 5
    def fn7():
        yield
        try:
            yield
        finally:
            print('finally')
            return 5

    from .base import UnitTestTransformer, get_transformed_source
    class ReturnFromGeneratorTransformerTest(UnitTestTransformer):
        NODE_TRANSFORMER = ReturnFromGeneratorTransformer
        EXCLUDE_SOURCE_HASH = ['SourceHashVisitor']

    assert get_transformed_source(fn1) == get_trans

# Generated at 2022-06-14 02:11:39.640427
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:11:51.236013
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils import parse, dump, compare_asts
    from .test_base import transform_test_data
    from .test_annotations import AnnotationSyntaxTestCase
    for test in transform_test_data():
        for parent_node, target, result in AnnotationSyntaxTestCase.yield_cases(test):
            for case in [target, result]:
                code, _ = case
                if code is None:
                    continue
                tree = parse(code, version="3.6")
                out = ReturnFromGeneratorTransformer().visit(tree)
                dump_out = dump(out)
                dump_result = dump(result)
                compare_asts(dump_out, dump_result, test.filename)

# Generated at 2022-06-14 02:11:58.280330
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    tree = ast.parse('''
        def f():
            print(2)
            return 5
        def g():
            yield 1
            return 5
        def h():
            yield 1
            yield 2
            return 5
        def i():
            yield 1
            raise Exception()

        def j():
            try:
                return 5
            except:
                pass
        def k():
            for i in range(2):
                yield i
            return 5
        def l():
            for i in range(2):
                return 5
            return 4
        def m():
            for i in range(2):
                print(i)
                return 5
            return 4
        def n():
            yield from range(2)
            return 5
        def o():
            return 0
    ''')

# Generated at 2022-06-14 02:12:07.604718
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    funcdef = ast.parse('def fn():\n    yield 1\n    return 5')  # type: ignore
    target = ast.parse('def fn():\n    yield 1\n    exc = StopIteration()\n    exc.value = 5\n    raise exc')  # type: ignore
    t = ReturnFromGeneratorTransformer()
    t.visit(funcdef)
    assert ast.dump(funcdef, annotate_fields=False, include_attributes=False) == ast.dump(target, annotate_fields=False, include_attributes=False)  # type: ignore

# Generated at 2022-06-14 02:12:16.232519
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:12:26.533141
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    """
    Test that ReturnFromGeneratorTransformer replaces all return statements in generator with StopIteration raise.
    """
    class TestNode(ast.AST):
        _fields = ('body', 'return_val')

    return_node = ast.Return(value=ast.Num(n=1))
    yield_node = ast.Expr(value=ast.Yield(value=ast.Num(n=2)))
    test_node = TestNode(body=[return_node, yield_node], return_val=3)


# Generated at 2022-06-14 02:12:28.106561
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.test_utils import assert_equal_ast

# Generated at 2022-06-14 02:12:40.990996
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_env_transformers import to_source
    from ..backend.add_from_import_transformer import AddFromImportTransformer
    from ..backend.fix_missing_locations_transformer import FixMissingLocationsTransformer
    from ..backend.ast_to_code_transformer import ASTToCodeTransformer

    source = """
        def fn():
            yield 1
            return 5
    """
    compiler = ASTToCodeTransformer()
    compiler.add_transformer(AddFromImportTransformer)
    compiler.add_transformer(ReturnFromGeneratorTransformer)
    compiler.add_transformer(FixMissingLocationsTransformer)
    compiler.compile(source, '<test>')
    # We need to use to_source here because nodes are in different order.
    res = compiler.ast_to_code

# Generated at 2022-06-14 02:12:49.696976
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast

    code = '''
        def fn(i):
            if i < 2:
                yield i
                return

            try:
                yield i
            except Exception:
                return i
            
            while True:
                yield i
                if i > 5:
                    return i
                i += 1
    '''

    parsed_code = ast.parse(code)

    transformed = ReturnFromGeneratorTransformer().visit(parsed_code)

    # ast.fix_missing_locations(transformed)
    # final_code = astor.to_source(transformed)

    # assert final_code == expected

# Generated at 2022-06-14 02:12:59.444614
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .base import NodeTest
    from .. import transformer

    # Transform the snippet
    code = "def fn():\n" + \
           "    yield 1\n" + \
           "    return 5\n"
    tree = transformer.parse(code)
    transformer.transform(tree, [ReturnFromGeneratorTransformer])

    # Get the first function def
    fn = tree.body[0]

    # Check that the function def changed

# Generated at 2022-06-14 02:13:12.356275
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        yield 1
        return 5

    def fn2():
        yield 1
        for x in range(5):
            yield x
        return 5

    def fn3():
        yield 1
        return

    def fn4():
        return 5

    assert ReturnFromGeneratorTransformer().visit(ast.parse(snippet(fn))) == \
        ReturnFromGeneratorTransformer().visit(
                ast.parse(snippet(return_from_generator(5))))

    assert ReturnFromGeneratorTransformer().visit(ast.parse(snippet(fn2))) == \
        ReturnFromGeneratorTransformer().visit(
                ast.parse(snippet(return_from_generator(5))))

    assert ReturnFromGeneratorTransformer().visit(ast.parse(snippet(fn3)))

# Generated at 2022-06-14 02:13:24.917288
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():    
    from typed_ast import ast3 as ast
    from ..utils.snippet import snippet
    from .base import BaseNodeTransformer
    class ReturnFromGeneratorTransformer(BaseNodeTransformer):
        """Compiles return in generators like:
            def fn():
                yield 1
                return 5
        To:
            def fn():
                yield 1
                exc = StopIteration()
                exc.value = 5
                raise exc
        """
        target = (3, 2)
        def _find_generator_returns(self, node: ast.FunctionDef) \
                -> List[Tuple[ast.stmt, ast.Return]]:
            """Using bfs find all `return` statements in function."""
            to_check = [(node, x) for x in node.body]  # type: ignore
            returns = []


# Generated at 2022-06-14 02:13:33.109569
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from .test_utils import NodeTransformerTest
    import inspect
    import os
    import sys

    class TestTransformer(NodeTransformerTest):
        # pylint: disable=abstract-method
        transformer = ReturnFromGeneratorTransformer
        dir = os.path.dirname(__file__)
        base_path = os.path.join(dir, 'transformers', 'tests', 'return_from_generator')
        target_versions = (3, 2)

        def _get_code_variables(self, input_code: str, **kwargs) -> Tuple[str, str]:
            old_code = input_code

            # hack: the return codes are enough.
            if 'yields' in input_code:
                input_code = input_code.replace('yields', 'return')


# Generated at 2022-06-14 02:13:34.224463
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:14:04.459200
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    def fn():
        if True:
            yield 1
            return 5

    transformed = ast.parse(ReturnFromGeneratorTransformer().visit(fn))
    fn_def = transformed.body[0]

    assert_true(isinstance(fn_def, ast.FunctionDef))
    assert_equal(fn_def.name, 'fn')

    assert_equal(len(fn_def.body), 5)

    if_stmt = fn_def.body[0]

    assert_true(isinstance(if_stmt, ast.If))
    assert_true(isinstance(if_stmt.body[0], ast.Expr))

    yield_stmt = if_stmt.body[0].value

    assert_true(isinstance(yield_stmt, ast.Yield))

# Generated at 2022-06-14 02:14:11.043632
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    input_code = """\
        def fn():
            yield 1
            return 5
        """
    expected_code = """\
        def fn():
            yield 1
            exc = StopIteration()
            exc.value = 5
            raise exc
        """

    actual = apply_transformer(ReturnFromGeneratorTransformer, input_code)
    assert actual == expected_code

# Generated at 2022-06-14 02:14:20.270254
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class MockNode:
        @staticmethod
        def index(x):
            return 1
        @staticmethod
        def generic_visit(x, y):
            return x, y
        @staticmethod
        def get_body(return_value=MockNode()):
            return [MockNode() for i in range(4)]
        @staticmethod
        def pop(x):
            pass
        def insert(self, index, line):
            pass

    class MockReturnNode:
        def __init__(self, x):
            self.value = x

    mock_tree = MockNode()
    mock_tree.body = [MockReturnNode(5), MockReturnNode(6)]

    mock_function_def = MockNode()

# Generated at 2022-06-14 02:14:34.139992
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from ..type_inference_programs.forward_analysis import ForwardAnalysis
    from ..pythran_changes.break_continue_transformer import BreakContinueTransformer
    from ..utils import change_ast

    def build_ast(func):
        code = func.__code__
        tree = ast.parse(code.co_consts[0])
        parent = ast.AST()
        tree._parent = parent
        tree._ctx = ast.Load
        return tree


# Generated at 2022-06-14 02:14:44.982444
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from copy import deepcopy
    from hstest.exceptions import WrongAnswer
    from .replacement import Replacement
    from .transformers import Python3Transformer

    r = Replacement("a", "return a")

    with pytest.raises(WrongAnswer) as e:
        Python3Transformer(r).visit(deepcopy(r.node))
    assert "Yield, yield from, and return are invalid inside generator" in str(e)

    with pytest.raises(WrongAnswer) as e:
        Python3Transformer(r).visit(deepcopy(r.node))
    assert "Yield, yield from, and return are invalid inside generator" in str(e)

# Generated at 2022-06-14 02:14:46.447082
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer

# Generated at 2022-06-14 02:14:56.730356
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    assert "pass" == transform(
        """
        def fn():
            pass
        """,
        [ReturnFromGeneratorTransformer],
    )
    assert "def fn():\n    yield 1" == transform(
        """
        def fn():
            yield 1
        """,
        [ReturnFromGeneratorTransformer],
    )
    assert "def fn():\n    yield 1" == transform(
        """
        def fn():
            yield 1
            return
        """,
        [ReturnFromGeneratorTransformer],
    )
    assert "def fn():\n    yield 1" == transform(
        """
        def fn():
            yield 1
            return 0
        """,
        [ReturnFromGeneratorTransformer],
    )

# Generated at 2022-06-14 02:15:07.512673
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from typed_ast import ast3 as ast
    from textwrap import dedent
    from .base import BaseNodeTransformerTest
    from .base import BaseNodeTransformerTest
    from ..as_py import as_py
    from ..as_ast import as_ast

    source = dedent('''
        def fn(a: int) -> None:
            yield 5
            return a
    ''')
    expected_source = dedent('''
        def fn(a: int) -> None:
            yield 5
            exc = StopIteration()
            exc.value = a
            raise exc
    ''')

    class TestTransformer(BaseNodeTransformer):
        PROCESSORS = [ReturnFromGeneratorTransformer]

    test_transformer = TestTransformer()
    node = as_ast(source)
    node = test

# Generated at 2022-06-14 02:15:21.021481
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    class AssertVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            
            # expected node.body before the transformation
            expected_node_body = [
                ast.Expr(value=ast.Yield(value=ast.Num(n=1))),
                ast.Return(value=ast.Num(n=5))
            ]
            
            # expected node.body after the transformation

# Generated at 2022-06-14 02:15:30.456991
# Unit test for method visit_FunctionDef of class ReturnFromGeneratorTransformer
def test_ReturnFromGeneratorTransformer_visit_FunctionDef():
    from ..utils.source import source_to_funcdef
    from ..utils.ast import dump
    import astor  # type: ignore

    code = """
    def fn():
        yield 1
        yield 2
        return 5
    """
    expected = """
    def fn():
        yield 1
        yield 2
        exc = StopIteration()
        exc.value = 5
        raise exc
    """

    tree = source_to_funcdef(code)
    tree = ast.fix_missing_locations(tree)
    tree = ReturnFromGeneratorTransformer().visit(tree)
    tree = ast.fix_missing_locations(tree)

    dump(tree)
    actual = astor.to_source(tree)

    assert actual.strip() == expected.strip()