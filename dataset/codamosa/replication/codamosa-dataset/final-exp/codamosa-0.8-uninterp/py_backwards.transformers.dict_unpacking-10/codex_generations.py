

# Generated at 2022-06-14 01:44:13.797922
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    input = '''{1: 1}'''
    expected_output = '''
_py_backwards_merge_dicts = (lambda *dicts:
    {}.update(*dicts) or {})
{1: 1}
'''
    node = ast.parse(input)
    DictUnpackingTransformer().visit(node)
    output = astor.to_source(node)
    assert expected_output == output


# Generated at 2022-06-14 01:44:21.159404
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from typed_astunparse import unparse

    CODE = """
        {1: 1, 2: 2, **{3: 3}, 4: 4, **{5: 5}, **{6: 6}, 7: 7}
    """

    tree = ast.parse(CODE)
    transformer = DictUnpackingTransformer()
    transformed = transformer.visit(tree)

    assert isinstance(transformed, ast.Module)
    assert len(transformed.body) == 3
    assert isinstance(transformed.body[0], ast.Expr)
    assert isinstance(transformed.body[1], ast.Expr)
    assert isinstance(transformed.body[2], ast.Expr)
    assert isinstance(transformed.body[0].value, ast.Call)

# Generated at 2022-06-14 01:44:27.982660
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    from .codegenerator import to_source
    from .tree_compare import compare_ast

    node = ast.Dict(keys=[ast.Constant(value=1), None],
                    values=[ast.Constant(value=1), ast.Name(id='a')])

    with_none = ast.parse(to_source(node))
    without_none = ast.parse(to_source(DictUnpackingTransformer().visit(node)))

    compare_ast(with_none, without_none)

# Generated at 2022-06-14 01:44:32.249066
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transpile import Transpiler

    source = """
        instance = MyClass(
            **{'key1': 1, **{'key2': 2}},
            **{'key3': 3, **{'key4': 4}})
    """
    expected = """
        instance = _py_backwards_merge_dicts(
            [{'key1': 1, **{'key2': 2}}],
            {'key3': 3, **{'key4': 4}})
    """

    tree = ast.parse(source)
    Trasnpiler(tree).register_transformers(DictUnpackingTransformer).transpile()
    actual = compile(tree, filename="<ast>", mode="exec")
    expected = compile(expected, filename="<ast>", mode="exec")
    assert actual

# Generated at 2022-06-14 01:44:42.295032
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from unittest import TestCase, main
    import typed_astunparse
    import ast
    from ..utils.source import get_source
    from typing import Iterator, List, Tuple

    class Tester(TestCase):
        def _test(self, src: str, expected_src: str) -> None:
            src = get_source(src)
            expected_src = get_source(expected_src)
            module = typed_astunparse.ast3.parse(src)
            self.assertIsInstance(module, ast.Module)
            transformer = DictUnpackingTransformer()
            result = transformer.visit(module)
            self.assertIsInstance(result, ast.Module)
            expected = typed_astunparse.ast3.parse(expected_src)
            self.assertEqual(result, expected)

   

# Generated at 2022-06-14 01:44:53.827740
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:44:59.912989
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typeddf.compiler.ast as ast
    transformer = DictUnpackingTransformer()
    
    module = ast.Module(body=[
        ast.Assign(
            targets=[ast.Name(id='result', ctx=ast.Store())],
            value=ast.Dict(
                keys=[
                    ast.Num(n=1),
                    None,
                    ast.Str(s='hello')],
                values=[
                    ast.Str(s='foo'),
                    ast.Name(id='bar', ctx=ast.Load()),
                    ast.Num(n=3)]))])
    
    transformer.visit(module)
    assert transformer._tree_changed is True
    
    body = module.body
    assert isinstance(body[0], ast.Assign)
    
    assign = body[0]

# Generated at 2022-06-14 01:45:06.378873
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from . import compile
    import ast
    from . import _test_transform
    from .annotation_transformer import AnnotationTransformer
    from .type_comment_transformer import TypeCommentTransformer


# Generated at 2022-06-14 01:45:16.236641
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node = ast.parse("{1: 1, **dict_a}")
    node = DictUnpackingTransformer().visit(node)

# Generated at 2022-06-14 01:45:26.101824
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse('a = 10')
    tree = DictUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 01:45:37.896653
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse('''a = {1: 1, **arg}''')  # type: ast.Module
    module = DictUnpackingTransformer().visit(module)  # type: ignore

    assert module.body[0].value.args[0].elts[0].keys[0].n == 1
    assert module.body[0].value.args[0].elts[1].id == 'arg'



# Generated at 2022-06-14 01:45:40.522624
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    source = \
"""
d = {1: 1, **a}
"""

# Generated at 2022-06-14 01:45:51.281402
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import textwrap
    import unittest
    from ..utils.testing import assert_equal_ast, test_source
    from ..utils.unparser import Unparser

    class Tests(unittest.TestCase):
        def test_DictUnpackingTransformer_visit_Module(self):
            snippet_ = merge_dicts()
            source = textwrap.dedent(
                '''
                {1: 1, 2: 2, 3: 3, **{1: 2}, 4: 3, **{1: 1}}
                ''')
            tree = test_source(source)
            DictUnpackingTransformer().visit(tree)
            expected = snippet_ + source
            assert_equal_ast(expected, Unparser(tree))

    unittest.main()

# Generated at 2022-06-14 01:45:58.538925
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.tree import dump
    from .snippets import DictUnpackingTransformer_visit_Module

    module = DictUnpackingTransformer_visit_Module.get_ast()
    
    expected = DictUnpackingTransformer_visit_Module.expected
    expected = ast.parse(expected)

    actual = DictUnpackingTransformer().visit(module)
    actual = ast.fix_missing_locations(actual)

    assert dump(expected) == dump(actual)

# Generated at 2022-06-14 01:46:04.567720
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Tests compile of dicts with unpacking."""
    from ..utils.source import source

    # Compiles dict unpacking to normal dict
    assert DictUnpackingTransformer().visit(source('{**a}')) \
        == source('dict(a)')

    # Compiles dict unpacking with normal dict to function call
    assert DictUnpackingTransformer().visit(source('{1: 1, **a}')) \
        == source('_py_backwards_merge_dicts([{1: 1}], a)')

    # Compiles two dict unpacking with normal dict to function call

# Generated at 2022-06-14 01:46:11.807820
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_astunparse import unparse

    transformer = DictUnpackingTransformer()
    node = ast.parse("""
        {1: 1, **{'a': 'b', 'b': 'c'} }
        """)
    transformed = transformer.visit(node)
    transformed_code = unparse(transformed)
    expected_code = """
    _py_backwards_merge_dicts([{1: 1}], {'a': 'b', 'b': 'c'} )
    """
    assert transformed_code == expected_code

# Generated at 2022-06-14 01:46:21.213622
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    import sys

    class Compiler(ast.NodeVisitor):
        def __init__(self, version: Tuple[int, int]):
            self._version = version

        def compile(self, node: ast.AST) -> str:
            self.visit(node)
            return astor.to_source(node, add_line_information=False)

        def visit_Dict(self, node: ast.Dict):
            DictUnpackingTransformer(version=self._version).visit(node)

    sys.version_info = (3, 6)

    node = ast.parse('{1: 1, **{2: 2}}')
    result = Compiler((3, 6)).compile(node)

# Generated at 2022-06-14 01:46:30.061588
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse
    import textwrap
    # *** setup ***
    # setup code
    code = textwrap.dedent('''
        a = {1: 1, **dict_a}''')
    # setup expected
    expected = textwrap.dedent('''
        a = _py_backwards_merge_dicts([{1: 1}], dict_a)''')
    # setup visitor
    visitor = DictUnpackingTransformer()
    # *** run ***
    actual = visitor.visit(ast.parse(code))
    # *** assert ***
    assert astunparse.unparse(actual) == expected

# Generated at 2022-06-14 01:46:42.864402
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.transform import transform
    from .verifier import verify

    source = '''
        {1: 1, **dict_a}
        '''
    verify(
        transform(source, DictUnpackingTransformer),
        expect='_py_backwards_merge_dicts([{1: 1}], dict_a)',
    )

    source = '''
        {1: 1, **dict_a, **dict_b}
        '''
    verify(
        transform(source, DictUnpackingTransformer),
        expect='_py_backwards_merge_dicts([{1: 1}], dict_a, dict_b)',
    )

# Generated at 2022-06-14 01:46:55.230383
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse("_ = {a: b, **dict_a, **dict_b, c: d}")
    tree = DictUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 01:47:24.355975
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from collections import OrderedDict
    from ...utils.source_code import SourceCode

    test_cases = OrderedDict()
    test_cases['case #1'] = {
        'node': ast.parse('{1: 1, 2: 2, 3: 3}'),
        'expected': '{1: 1, 2: 2, 3: 3}',
    }
    test_cases['case #2'] = {
        'node': ast.parse('{1: 1, 2: 2, **a}'),
        'expected': '_py_backwards_merge_dicts([{1: 1, 2: 2}], a)',
    }

# Generated at 2022-06-14 01:47:34.693263
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class TestCode(ast.AST):
        _fields = ('kws',)

    def _visit_node(node, expected_result):
        transformer = DictUnpackingTransformer()
        result = transformer.visit_Dict(node)
        assert result == expected_result
        assert transformer._tree_changed == True

    # Empty dict
    node = ast.Dict(keys=[], values=[])
    expected_result = ast.Call(
        func=ast.Name(id='dict'),
        args=[], keywords=[])
    _visit_node(node, expected_result)

    # Simple dict
    node = ast.Dict(keys=[ast.Num(1)], values=[ast.Num(1)])

# Generated at 2022-06-14 01:47:45.372197
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.snippet import snippet
    from ast_toolbox import ast_compare
    from ast_toolbox.utils import ast_parse

    def transform(code: str) -> ast.AST:
        return DictUnpackingTransformer().visit(ast_parse(code))

    def get_dict(code: str) -> ast.AST:
        call = transform(code)
        assert isinstance(call, ast.Call)
        assert call.args[0].elts[0].keys == [ast.Name(id='x')]
        return call


# Generated at 2022-06-14 01:47:52.440730
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Unit test for method visit_Dict of class DictUnpackingTransformer."""
    class Custom(DictUnpackingTransformer):
        def visit_Dict(self, node: ast.Dict) -> Union[ast.Dict, ast.Call]:
            if None not in node.keys:
                return self.generic_visit(node)  # type: ignore
            return node

    node_1 = ast.Dict(keys=[None, None, None], values=[None, None, None])
    node_2 = ast.Dict(keys=[None, None, None], values=[None, None, None])
    node_3 = ast.Dict(keys=[None], values=[None])
    node_4 = ast.Dict(keys=[None, None], values=[None, None])

# Generated at 2022-06-14 01:47:59.361607
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import textwrap
    from typed_ast.ast3 import parse
    from numpydoc.docscrape import NumpyDocString
    from numpydoc.docscrape_sphinx import SphinxDocString

    src = textwrap.dedent("""
    def f(arg):
        docstring = arg
        """
    )
    root = parse(src)
    DictUnpackingTransformer({}).visit(root)

# Generated at 2022-06-14 01:48:09.995054
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # pylint: disable=unused-variable, too-many-locals, redefined-outer-name, too-many-branches, too-many-statements
    from pyredux_tools.compiler._ast3_impl.base import CompilerContext
    
    from typed_ast import ast3 as ast

    # noinspection PyShadowingNames
    def _test(src_code: str, exp_src_code: str) -> None:
        tree = ast.parse(src_code)
        DictUnpackingTransformer(CompilerContext()).\
            visit(tree)
        tree = ast.fix_missing_locations(tree)
        # todo: output formatted code
        assert exp_src_code == ast.dump(tree)

    # в начале модул

# Generated at 2022-06-14 01:48:15.348346
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.tester import assert_transform

    assert_transform(
        DictUnpackingTransformer,
        '''
        def foo():
            return {1: 2, **{3: 4}}
        ''',
        '''
        def foo():
            return _py_backwards_merge_dicts([{1: 2}], {3: 4})
        '''
    )



# Generated at 2022-06-14 01:48:26.685548
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.run import run_module
    from ..utils.load import load_module
    from .utils.compare import compare

    run_module(module=DictUnpackingTransformer, code="""
        # Before transformation
        assert {1: 2, **{3: 4}} == {1: 2, 3: 4}
        assert {**{}} == {}
        assert {1: 2, **{}} == {1: 2}
        assert {**{1: 2}} == {1: 2}
        assert {1: 2, **{3: 4}, **{5: 6}} == {1: 2, 3: 4, 5: 6}
        assert {1: 2, **{3: 4}, **{5: 6}, **{}} == {1: 2, 3: 4, 5: 6}
    """)


# Generated at 2022-06-14 01:48:37.036308
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from ..utils.transformer import transform_tree
    from ..tests.utils import assert_source

    code = '{1: 1, **dict_a, 2: 2, **dict_b, 3: 3}'
    expected = """
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    _py_backwards_merge_dicts([{
        1: 1,
        2: 2,
        3: 3
    }], dict_a, dict_b)
    """.strip()

    tree = transform_tree(code, DictUnpackingTransformer)
    assert_source(astor.to_source(tree), expected)

# Generated at 2022-06-14 01:48:47.550804
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source_to_nodes
    from ..utils.source import source_to_code
    from .ast_test import clear_locations

    source = """
    {
      **{'a': 2},
      1: 2,
      'a': 3,
      **{'a': 4, 'b': 5}
    }
    """
    module_node = source_to_nodes(source, 3)
    module_node = clear_locations(module_node)

    DictUnpackingTransformer().visit(module_node)


# Generated at 2022-06-14 01:49:24.367609
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer().__class__.__name__ == "DictUnpackingTransformer"

# Generated at 2022-06-14 01:49:26.068525
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    x = {'a': 1, **{'b': 2}}

# Generated at 2022-06-14 01:49:35.090197
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    def expected():
        def _py_backwards_merge_dicts():
            pass

    def actual_before():
        pass

    def actual_after():
        pass

    expected_ast = ast.parse(expected.__text__)
    actual_before_ast = ast.parse(actual_before.__text__)
    actual_after_ast = ast.parse(actual_after.__text__)
    assert DictUnpackingTransformer().visit(actual_before_ast) == actual_after_ast
    assert expected_ast == actual_after_ast

# Generated at 2022-06-14 01:49:40.193181
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from ..lint_ast import LintAst
    
    source = """
        {1: 1, **dict_a}
    """
    expected = merge_dicts.get_body() + """
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """
    tree = LintAst(source, DictUnpackingTransformer)
    assert expected == tree.source

# Generated at 2022-06-14 01:49:41.477003
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    x = DictUnpackingTransformer()
    assert repr(x) == '<DictUnpackingTransformer()>'

# Generated at 2022-06-14 01:49:42.923244
# Unit test for method visit_Module of class DictUnpackingTransformer

# Generated at 2022-06-14 01:49:53.812423
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_base import BaseNodeTransformerTest

# Generated at 2022-06-14 01:49:54.813563
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer()


# Generated at 2022-06-14 01:50:01.027909
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astor
    
    module = ast.parse('''{1: 1, **dict_a}''')
    module = DictUnpackingTransformer().visit(module)
    module = ast.Module([module])
    module = ast.fix_missing_locations(module)

# Generated at 2022-06-14 01:50:02.332088
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    transformer = DictUnpackingTransformer()

# Generated at 2022-06-14 01:50:32.324295
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ...testing import assert_transformed_code

    assert_transformed_code(
        DictUnpackingTransformer,
        """
        {
            1: 1,
            'a': 2,
            **dict_a
        }
        """,
        """
        _py_backwards_merge_dicts(
            [{1: 1, 'a': 2}],
            dict_a
        )
        """)

# Generated at 2022-06-14 01:50:39.010603
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .fixtures.dict_unpacking import DictUnpackingTransformer
    from .fixtures.dict_unpacking import ast_before, ast_after
    from .fixtures.dict_unpacking import code_before, code_after

    module = DictUnpackingTransformer().visit(ast_before)
    code = compile(module, filename="<ast>", mode="exec")
    exec(code, {})

    assert ast.dump(module) == ast.dump(ast_after)
    assert code == code_after

# Generated at 2022-06-14 01:50:41.899945
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    program = """
import sys
{1: 1, **dict_a}
    """

# Generated at 2022-06-14 01:50:46.722181
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = """
    a = {1: 2, **dict(x=3)}
    """
    expected = """
    _py_backwards_merge_dicts([{1: 2}], dict(x=3))
    """
    assert expected == repr(DictUnpackingTransformer().visit(
        ast.parse(dedent(code))))

# Generated at 2022-06-14 01:50:54.062295
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node = ast.parse(
        textwrap.dedent("""
        import typing
        {'a': 1}  # type: typing.Dict[str, int]
        """))
    DictUnpackingTransformer().visit(node)
    assert node.body[0].body[0].value.func.id == '_py_backwards_merge_dicts'
    assert '_py_backwards_merge_dicts = _py_backwards_merge_dicts' \
        in ast.dump(node.body[0])

# Generated at 2022-06-14 01:50:58.352476
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import parse
    from .test_base import get_used_imports

    module = parse(merge_dicts.get_body())
    module = DictUnpackingTransformer(module).visit(module)
    assert get_used_imports(module) == set()


# Generated at 2022-06-14 01:51:07.253698
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from .transformers.testing_utils import apply_transformer
    source = """
    {'a': x, **{'b': y}, **{'c': z}, 'd': w}
    """
    tree = ast.parse(source)
    apply_transformer(tree, DictUnpackingTransformer)
    expected_source = """
    _py_backwards_merge_dicts([{'a': x}], {'b': y}, {'c': z}, {'d': w})
    """
    assert astor.to_source(tree).strip() == expected_source


# Generated at 2022-06-14 01:51:19.053472
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse
    from ast import parse
    code = "a = {0: 1, '2': 2, **{}}"
    expected = """a = _py_backwards_merge_dicts([{0: 1, '2': 2}], {})"""
    node = DictUnpackingTransformer().visit(parse(code))  # type: ignore
    assert unparse(node).strip() == expected

    code = "a = {0: 1, **{'1': 1}}"
    expected = """a = _py_backwards_merge_dicts([{0: 1}], {'1': 1})"""
    node = DictUnpackingTransformer().visit(parse(code))  # type: ignore
    assert unparse(node).strip() == expected



# Generated at 2022-06-14 01:51:27.198556
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source_to_node
    import astor

    source = """a = {1: 2}"""
    node = source_to_node(source)  # type: ast.Module
    t = DictUnpackingTransformer()
    t.visit(node)
    assert astor.to_source(node) == 'a = {1: 2}'

    source = """a = {**{1: 2, 3: 4}}"""
    node = source_to_node(source)  # type: ast.Module
    t = DictUnpackingTransformer()
    t.visit(node)
    assert astor.to_source(node) == 'a = _py_backwards_merge_dicts([], {1: 2, 3: 4})'


# Generated at 2022-06-14 01:51:37.924988
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Tests visit_Dict method of class DictUnpackingTransformer."""

# Generated at 2022-06-14 01:52:30.123936
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ast
    import astunparse
    import textwrap

    def check(code, expected):
        code = textwrap.dedent(code)
        expected = textwrap.dedent(expected).lstrip()

        node = ast.parse(code)
        transpiled = DictUnpackingTransformer().visit(node)  # type: ignore
        result = astunparse.unparse(transpiled)
        assert result == expected

    check(
        '''
        {1: 1, **dict_a}''',

        '''
        _py_backwards_merge_dicts(
            [
                dict(1),
                dict_a
            ]
        )''')


# Generated at 2022-06-14 01:52:40.592570
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from ..unparse import Unparser
    from astunparse import unparse

    DictUnpackingTransformer().visit(
        ast.parse('''
            a = {1, 2}
            a = {**{1: 2}, **{3: 4}}
            a = {'a': 1, 'b': 2, **{'d', 'e'}}
            a = {**{}, **{}}
            a = {}
            '''))


# Generated at 2022-06-14 01:52:50.612825
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '''
{1: 1, None: a, 4: {None: b, 1: "a"}, None: None, None: c}
'''
    tree = ast.parse(source)
    expected = '''
_py_backwards_merge_dicts(
    [dict({1: 1}), a, dict({1: "a", 4: dict(b)}), dict({}), c])'''
    assert DictUnpackingTransformer().visit(tree) == expected  # type: ignore



# Generated at 2022-06-14 01:52:56.227807
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    cls = DictUnpackingTransformer
    tree = ast.parse('{1: 1, **a}', '<test>', 'exec')
    cls.run_visitor(tree)
    compare_source(tree, '_py_backwards_merge_dicts([{1: 1}], a)')

# Generated at 2022-06-14 01:52:57.408228
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:52:59.444657
# Unit test for method visit_Module of class DictUnpackingTransformer

# Generated at 2022-06-14 01:53:01.754401
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer()



# Generated at 2022-06-14 01:53:05.656743
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert isinstance(DictUnpackingTransformer(), DictUnpackingTransformer)
    assert isinstance(DictUnpackingTransformer(), BaseNodeTransformer)


# Generated at 2022-06-14 01:53:13.206274
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    """
    Test cases for visit_Module method.
    """

    # Test-case #1
    test_ast = ast.parse("""\
{}
""")

    # Test-case #2
    test_ast2 = ast.parse("""\
{1: 1, **dict_a}
""")

    assert DictUnpackingTransformer().visit(test_ast) == test_ast

    test_result = DictUnpackingTransformer().visit(test_ast2)
    assert type(test_result.body[0].value) == ast.Call
    assert test_result.body[0].value.func.id == '_py_backwards_merge_dicts'


# Generated at 2022-06-14 01:53:14.670073
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    transformer = DictUnpackingTransformer()
    assert transformer is not None