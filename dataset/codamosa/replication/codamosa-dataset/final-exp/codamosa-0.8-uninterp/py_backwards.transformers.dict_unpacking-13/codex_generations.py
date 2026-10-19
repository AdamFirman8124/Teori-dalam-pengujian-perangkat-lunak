

# Generated at 2022-06-14 01:44:13.797730
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    def check(code: str, expected: str) -> None:
        node = ast.parse(code)
        node = transformer.visit(node)
        node = ast.fix_missing_locations(node)
        new_code = astor.to_source(node)
        assert new_code == expected, new_code

    check(
        '''{1: 2, 3: 4, **dict_a, 5: 6, **dict_b, 7: 8}''',
        '''_py_backwards_merge_dicts([{1: 2, 3: 4}, dict_a, {5: 6}, dict_b, {7: 8}])''',
    )


# Generated at 2022-06-14 01:44:21.160999
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse("""\
{1: 1, **{2: 2}}
{1: 1, **dict_a, 2: 2, **dict_b}
{1: 1, **dict_a, 2: 2, **dict_b, 3: 3, **dict_c}
{1: 1, **dict_a, 2: 2, 3: 3, **dict_c}
{**dict_a, 2: 2, 3: 3, **dict_c}
{1: 1, **dict_a, 2: 2, 3: 3}
""")

# Generated at 2022-06-14 01:44:30.503161
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert ast.dump(
        DictUnpackingTransformer().visit(ast.parse('{1: 1, **{2: 2}}'))) == \
        'Module(body=[_py_backwards_merge_dicts([Dict(keys=[Num(n=1)], values=[Num(n=1)]), Dict(keys=[], values=[Dict(keys=[Num(n=2)], values=[Num(n=2)])])])])'


# Generated at 2022-06-14 01:44:38.989114
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from mypy_extensions import TypedDict
    import ast
    import astor

    class TestCase(TypedDict):
        name: str
        code: str
        expected: str


# Generated at 2022-06-14 01:44:48.719796
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_astunparse import unparse
    from .. import fix_code
    from .utils_for_tests import assert_equal_source

    code = '{\n' \
           ' 1: 2,\n' \
           ' 3: 4,\n' \
           ' None: None,\n' \
           ' 5: 6,\n' \
           ' 7: 8,\n' \
           ' 9: 10,\n' \
           '}\n'

    assert_equal_source(
        unparse(fix_code(code)),
        '_py_backwards_merge_dicts([{1: 2, 3: 4}], None, {5: 6, 7: 8, 9: 10})\n'
    )

# Generated at 2022-06-14 01:44:57.975083
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def test(kv: List[Pair]) -> ast.AST:
        node = ast.Dict(keys=[key for key, _ in kv],
                        values=[value for _, value in kv])
        return DictUnpackingTransformer().visit(node)

    f = ast.Name(id='f')
    a = ast.Name(id='a')
    b = ast.Name(id='b')
    c = ast.Name(id='c')


# Generated at 2022-06-14 01:45:07.996736
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transpile import transpile

    source = '''
        {1: 1, **dict_a, 2: 2}
        {**dict_a, 2: 2}
        {1: 1, **dict_a}
        {1: 1, **dict_a, **dict_b}
        {1: 1, **dict_a, 2: 2, **dict_b}
        {1: 1, **dict_a, **dict_b, 2: 2}
        {1: 1, **dict_a, **dict_b, 2: 2, 3: 3}
        {1: 1, **dict_a, 2: 2, **dict_b, 3: 3}
        {1: 1, **dict_a, 2: 2, 3: 3, **dict_b}
    '''

# Generated at 2022-06-14 01:45:14.744804
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_setup import setup

    source = '''\
{1: 1, **{2: 2, **{3: 3, **{4: 4}}}, 5: 5, **{6: 6}}'''
    expected = '''\
_py_backwards_merge_dicts([{1: 1, 5: 5}], {2: 2, **{3: 3, **{4: 4}}}, {6: 6})'''
    actual = setup(DictUnpackingTransformer, source)
    assert actual == expected



# Generated at 2022-06-14 01:45:26.071240
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # pylint: disable=missing-function-docstring
    # pylint: disable=missing-class-docstring
    # pylint: disable=pointless-string-statement
    # pylint: disable=unexpected-keyword-arg
    # pylint: disable=no-member
    # pylint: disable=no-value-for-parameter

    from typing import Any

    from typed_ast import ast3 as ast


# Generated at 2022-06-14 01:45:33.153142
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import compile_function
    exec(compile_function(DictUnpackingTransformer, """
        def function(a, b):
            return {1: a, 2: b, **c, **d}
    """), locals(), globals())

    assert function(1, 2, c={3: 3}, d={4: 4}) == {1: 1, 2: 2, 3: 3, 4: 4}

# Generated at 2022-06-14 01:45:44.739753
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ast
    import astor
    source = """{1: 2, **{3: 4}}"""
    tree = ast.parse(source)
    expected_tree = ast.parse('_py_backwards_merge_dicts([{1: 2}], {3: 4})')
    new_tree = DictUnpackingTransformer().visit(tree)
    assert astor.to_source(new_tree) == astor.to_source(expected_tree)


# Generated at 2022-06-14 01:45:59.072958
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.parse_source import generate_ast
    from ..utils.ast_helpers import dump_ast
    from ..utils.compare_ast import compare_ast
    from ..utils.transform import transform

    
    source = '{1: 1, **dict_a}'
    expected = '_py_backwards_merge_dicts([{1: 1}], dict_a})'

    ast_tree = generate_ast(source)
    new_ast = transform(ast_tree, [DictUnpackingTransformer])
    actual = dump_ast(new_ast)
    compare_ast(expected, actual)

# Generated at 2022-06-14 01:46:02.986594
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '{1: 1, **dict_a, 3: 3, 4: 4, **dict_b}'
    expected = "_py_backwards_merge_dicts([{1: 1, 3: 3, 4: 4}], dict_a, dict_b)"
    tree = ast.parse(source)
    DictUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == f'Module(body=[{merge_dicts}, Expr(value={expected})])'

# Generated at 2022-06-14 01:46:12.970776
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from compiler.ast import Dict
    from compiler.visitor import walk
    from typed_ast import ast3 as ast

    no_dict_unpacking = ast.Dict(
        keys=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3)],
        values=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3)])
    transformer = DictUnpackingTransformer(ast.parse(merge_dicts()))
    walk(no_dict_unpacking, transformer)
    assert isinstance(no_dict_unpacking, ast.Dict)


# Generated at 2022-06-14 01:46:19.387591
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    sample = ast.parse("{1: 1, 2: 2, 3: 3, **{4: 4, 5: 5}}")
    transformer = DictUnpackingTransformer()
    sample = transformer.visit(sample)

# Generated at 2022-06-14 01:46:28.471407
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '''
    n = {
        1: 1,
        **a,
        2: 2
    }
    '''
    expected = '''
    n = (
        _py_backwards_merge_dicts([{1: 1}, {2: 2}], a)
    )

    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    '''
    result = DictUnpackingTransformer.run(code)
    assert result == expected

# Generated at 2022-06-14 01:46:32.922878
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    def check(fn, expected):
        tree = ast3.parse(fn)
        DictUnpackingTransformer().visit(tree)
        assert ast3.dump(tree) == ast3.dump(expected)

    check("""
        {**a, **b}
        """,
        """
        _py_backwards_merge_dicts([a], b)
        """)

# Generated at 2022-06-14 01:46:46.084968
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer(None)

# Generated at 2022-06-14 01:46:55.658278
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor

    class DictUnpackingTestTransformer(DictUnpackingTransformer):  # noqa
        def _split_by_None(self, pairs):
            return [(k, v) for k, v in pairs if k is not None]  # type: ignore

        def _prepare_splitted(self, splitted):  # noqa
            yield splitted

        def _merge_dicts(self, xs):  # noqa
            return xs

    node = ast.parse(u"""{'a': 1, **d, 'b': 2, **e}""", mode='eval')
    expected_result = [(u'a', 1), (u'b', 2)]
    result = DictUnpackingTestTransformer().visit_Dict(node.body)
    assert result == expected_result, astor

# Generated at 2022-06-14 01:47:07.624822
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from ..utils.source import get_source
    from .base import NodeTransformerTestCase

    source = get_source(ast3.parse('''
    {1: 1, 2: 2, **dict_a}
    '''))
    expected = get_source(ast3.parse('''
    _py_backwards_merge_dicts([dict({1: 1, 2: 2})], dict_a)
    '''))

    class Test(NodeTransformerTestCase):
        transformer = DictUnpackingTransformer
        target = source
        result = expected

    Test().test()

# Generated at 2022-06-14 01:47:23.498519
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_transformer import (
        run_test_for_one_node_transformer,
        source_to_ast_node,
    )

    source = source_to_ast_node("""
        a = {1: 2, **{3: 4}}
    """, mode='eval')

    transformer = DictUnpackingTransformer()
    expected = source_to_ast_node("""
        a = _py_backwards_merge_dicts([{1: 2}], {3: 4})
    """, mode='eval')

    run_test_for_one_node_transformer(transformer, source, expected)

# Generated at 2022-06-14 01:47:34.458779
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:47:41.951031
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    ast_dict_unpacking = ast.parse("{1: 2, **{3: 4, **{5: 6}}}")
    ast_dict_unpacking_expected = ast.parse("""
_py_backwards_merge_dicts([{1: 2, 3: 4}], {5: 6})
    """)
    DictUnpackingTransformer().visit(ast_dict_unpacking)
    assert ast_dict_unpacking.body[0].value == \
        ast_dict_unpacking_expected.body[0].value

# Generated at 2022-06-14 01:47:48.557343
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    
    node = ast.parse('''\
        a = {1: 2, 3: 4, **d, None: 8, **e}
        ''')
    
    expected = ast.parse('''\
        a = _py_backwards_merge_dicts([{1: 2, 3: 4}], d, {8}, e)
        ''')
    
    t = DictUnpackingTransformer()
    assert ast.dump(t.visit(node)) == ast.dump(expected)

# Generated at 2022-06-14 01:47:58.125387
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer(None)

    assert transformer.visit(ast.parse('''
{}
''')) == ast.parse('''
_py_backwards_merge_dicts([{}, {}])
''')
    assert transformer.visit(ast.parse('''
{1: 1}
''')) == ast.parse('''
_py_backwards_merge_dicts([{1: 1}, {}])
''')
    assert transformer.visit(ast.parse('''
{None: None, **{1: 1}}
''')) == ast.parse('''
_py_backwards_merge_dicts([{None: None}, {1: 1}, {}])
''')

# Generated at 2022-06-14 01:48:08.564362
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent

    def test(source, expected):
        node = ast.parse(dedent(source))
        result = DictUnpackingTransformer.run(node, ())
        print(ast.dump(result, include_attributes=False))
        print(expected)


# Generated at 2022-06-14 01:48:18.199102
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import BaseNodeTestTransformer
    from ..utils.snippet import transform

    @BaseNodeTestTransformer.register_transformer(DictUnpackingTransformer)
    def transform(transformer, node):
        return transformer.visit(node)

    # test with single unpacking
    input = '{1: 1, **a, 2: 2}'
    expected = '_py_backwards_merge_dicts([{2: 2}], _py_backwards_merge_dicts([{1: 1}], a))'
    assert transform(DictUnpackingTransformer(), input) == expected

    # test with multiple unpacking
    input = '{1: 1, **a, 2: 2, **b}'

# Generated at 2022-06-14 01:48:28.999480
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse, Assign, Dict, Name, Module, Expr, Call

    transformer = DictUnpackingTransformer()
    input_ = Dict(keys=[None, 1, None, 2], values=[
                  Name(id='a', ctx=Load()), Name(id='b', ctx=Load()),
                  Name(id='c', ctx=Load()), Name(id='d', ctx=Load())])

# Generated at 2022-06-14 01:48:38.239468
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import generate_code
    from .module_level_annotation import \
        ModuleLevelAnnotationTransformer
    from ..utils.tree import ast_equals

    transformers = (
        DictUnpackingTransformer,
        ModuleLevelAnnotationTransformer,
    )

    code = """
        def foo(x: int) -> str:
            return {None: x, **locals()}
    """
    expected = """
        def foo(x: int) -> str:
            return _py_backwards_merge_dicts([{None: x}], locals())
    """
    module = generate_code(code, transformers)
    expected_module = generate_code(expected, transformers)
    assert ast_equals(module, expected_module)

# Generated at 2022-06-14 01:48:44.366100
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..unparse import Unparser
    from ..parse import parse
    from .base import BaseTestCase
    from textwrap import dedent

    source = dedent('''
    def f():
        a = {1:1, **{2:2}, 3:3, **{4:4}}
    ''')
    expected = dedent('''
    def f():
        a = _py_backwards_merge_dicts([{1: 1, 3: 3}], {2: 2}, {4: 4})
    ''')
    unparser = Unparser(source=source)
    assert unparser.unparse() == expected

# Generated at 2022-06-14 01:48:50.707376
# Unit test for method visit_Module of class DictUnpackingTransformer

# Generated at 2022-06-14 01:48:53.181859
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import round_trip
    code = '''{1: 1, **dict_a}'''

# Generated at 2022-06-14 01:48:57.732960
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import sys
    import ast
    import astor
    from astropy import mod
    from astropy.tests.helper import assert_source_equal

    code = '''{1, **x}'''


# Generated at 2022-06-14 01:48:58.627269
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:49:04.681296
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast.ast3 import parse
    from ..utils.helpers import node_to_str

    node = parse('{1: 1, **{2: 2}, 3: 3, **{4: 4}, 5: 5, **{6: 6}}')
    DictUnpackingTransformer().visit(node)
    assert node_to_str(node) == '_py_backwards_merge_dicts([dict({1: 1}), dict({3: 3}), dict({5: 5})], {2: 2}, {4: 4}, {6: 6})'

# Generated at 2022-06-14 01:49:05.632341
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:49:09.367278
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.tree import parse
    from ..utils.python import to_python

    INPUT = '''{1: 2, **{}}'''

# Generated at 2022-06-14 01:49:19.767607
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    class MyDictUnpackingTransformer(DictUnpackingTransformer):
        def __init__(self):
            self._tree_changed = False

        def _visit_change(self, node: ast.AST) -> bool:
            self._tree_changed = True
            return self.generic_visit(node)

        def _visit_unchange(self, node: ast.AST) -> ast.AST:
            return node

        def visit_Num(self, node: ast.Num) -> Union[ast.AST, bool]:
            return self._visit_unchange(node)

        def visit_Str(self, node: ast.Str) -> Union[ast.AST, bool]:
            return self._visit_unchange(node)


# Generated at 2022-06-14 01:49:29.653293
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ast import parse
    from .base import BaseNodeTransformerTestCase
    from .string_format_function import StringFormatFunctionTransformer

    transformer = StringFormatFunctionTransformer()
    DictUnpackingTransformer.__bases__ += (BaseNodeTransformerTestCase,)
    DictUnpackingTransformer._transform = transformer.transform

# Generated at 2022-06-14 01:49:35.450662
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    '''Checks whether ast is returned properly in constructor of class DictUnpackingTransformer'''
    
    # Tests if ast is returned properly without splitted
    def test_visit_Dict_without_splitted(self, node):
        if None not in node.keys:
            return self.generic_visit(node)  # type: ignore


# Generated at 2022-06-14 01:49:53.046649
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import BaseNodeTransformerTest
    from ..utils.dump import dump

    @snippet
    def before():
        {1: 2, **a, 5: 6, **b, **c, **d, 9: 10}

    @snippet
    def after():
        _py_backwards_merge_dicts([{1: 2, 5: 6}], a, b, c, d, {9: 10})

    BaseNodeTransformerTest(DictUnpackingTransformer, before, after)


# Generated at 2022-06-14 01:49:54.798044
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    transformer = DictUnpackingTransformer()

    assert transformer is not None

# Generated at 2022-06-14 01:49:56.500166
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:49:59.065210
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from .test_utils import make_cst_from_snippet
    make_cst_from_snippet(DictUnpackingTransformer, 'DictUnpackingTransformer')

# Generated at 2022-06-14 01:50:10.339102
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing.transformer import make_test


# Generated at 2022-06-14 01:50:11.345231
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer()


# Generated at 2022-06-14 01:50:12.308685
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer()

# Generated at 2022-06-14 01:50:22.912406
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast  # type: ignore

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node: ast.Name) -> Optional[bool]:
            if isinstance(node.ctx, ast.Load):
                return False
            return None


# Generated at 2022-06-14 01:50:29.844946
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..testing.utils import assert_block_equals
    from ..testing.visitor import ASTNode

    tree = ASTNode().module(
        ASTNode().dict(
            ASTNode().number('1'),
            ASTNode().number('2'),
            None,
            ASTNode().name('a'),
            ASTNode().none()))

    expected = ASTNode().module(
        ASTNode().call(
            ASTNode().name('_py_backwards_merge_dicts'),
            [ASTNode().list(
                ASTNode().dict(
                    ASTNode().number('1'),
                    ASTNode().number('2')),
                ASTNode().name('a'),
                ASTNode().call(
                    ASTNode().name('dict'),
                    [ASTNode().none()]))]))


# Generated at 2022-06-14 01:50:35.197182
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from astunparse import unparse
    from .utils import assert_and_parse

    expected = merge_dicts.get_body() + ['\n', 'a = 1']
    snippet = """
    a = 1
    """
    expected = ''.join(expected).strip()
    assert_and_parse(DictUnpackingTransformer, snippet, expected)


# Generated at 2022-06-14 01:50:57.753970
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()



# Generated at 2022-06-14 01:51:00.260939
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astunparse

    source = '''{1: 1, **dict_a}'''

# Generated at 2022-06-14 01:51:10.211386
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse("")
    assert isinstance(module, ast.Module)
    assert [] == module.body
    assert 0 == len(module.body)

    new_module = DictUnpackingTransformer().visit_Module(module)
    assert isinstance(new_module, ast.Module)
    assert isinstance(new_module.body[0], ast.Expr)
    assert isinstance(new_module.body[0].value, ast.Call)
    assert isinstance(new_module.body[0].value.func, ast.Name)
    assert 'dict' == new_module.body[0].value.func.id
    assert [] == new_module.body[0].value.args
    assert [] == new_module.body[0].value.keywords


# Generated at 2022-06-14 01:51:13.323983
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    t = DictUnpackingTransformer()
    assert isinstance(t, DictUnpackingTransformer)

# Generated at 2022-06-14 01:51:23.321589
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from . import from_source
    
    x = from_source(
        """
        {
            1 : 1,
            2 : 2,
            **{"a": "b"},
            **dict_a,
            3 : 3,
        }
        """)
    
    y = from_source(
    
        """
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result

        _py_backwards_merge_dicts([{1: 1, 2: 2}, {"a": "b"}, dict_a, {3: 3}])
        """)
    
    assert x == y



# Generated at 2022-06-14 01:51:33.944756
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse("{1: 1, **dict_a}")
    result = DictUnpackingTransformer().visit_Module(module)
    expected = ast.Module([
        merge_dicts.get_body()[0],
        ast.Expr(value=ast.Call(func=ast.Name(id='_py_backwards_merge_dicts'),
                                args=[ast.List(elts=[ast.Dict(keys=[ast.Constant(1)],
                                                               values=[ast.Constant(1)])]),
                                      ast.Name(id='dict_a')],
                                keywords=[]))])
    assert result == expected


# Generated at 2022-06-14 01:51:47.556691
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node = ast.Module(
        body=[
            ast.Expr(
                value=ast.Dict(
                    keys=[
                        ast.Str(s='key1'),
                        None,
                        ast.Str(s='key2')],
                    values=[
                        ast.Str(s='value1'),
                        ast.Name(id='variable'),
                        ast.Str(s='value2')])),
            ast.Expr(
                value=ast.Dict(
                    keys=[None],
                    values=[
                        ast.Name(id='variable2')]))])

# Generated at 2022-06-14 01:51:56.879189
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import load_module, dump_module
    from ..main import compile_ast
    from .test_utils import get_test_cases

    module = load_module(None, """
        {1: 2}
        {1: 2, **{3: 4, **dict_a}}
        {1: 2, **{3: 4, **dict_a}, **{5: 6}}
    """)

    module = compile_ast(module, [DictUnpackingTransformer])
    dump_module(module)


# Generated at 2022-06-14 01:51:57.939510
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:52:06.740137
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse
    import textwrap
    source = textwrap.dedent('''
    {
        1: 1,
        **dict_a,
        2: 2,
        **dict_b
    }
    ''')
    tree = ast.parse(source)
    transformer = DictUnpackingTransformer()
    result = transformer.visit(tree)
    got = astunparse.unparse(result).strip()
    want = textwrap.dedent('''
    _py_backwards_merge_dicts([{1: 1}, {2: 2}], dict_a, dict_b)
    ''').strip()
    assert got == want
    assert transformer._tree_changed



# Generated at 2022-06-14 01:53:01.547590
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    # Spaced
    source = """
        {
            1: 2,
            **{
                2: 3,
            },
            **{
                3: 4,
            },
            4: 5,
        }
    """
    parsed = ast.parse(source)
    transformed = transformer.visit(parsed)
    assert str(transformed) == """
        _py_backwards_merge_dicts(
            [
                {
                    1: 2,
                    4: 5,
                },
                {
                    2: 3,
                },
                {
                    3: 4,
                },
            ],
        )
    """

    # Dict as value

# Generated at 2022-06-14 01:53:10.400269
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse

    tree = ast.parse('{x: 0, y: 1, **z}')
    visitor = DictUnpackingTransformer()
    result = visitor.visit(tree)  # type: ignore
    assert isinstance(result, ast.Module)

    assert astunparse.unparse(result) == """\
_py_backwards_merge_dicts([{'x': 0, 'y': 1}], z)
"""

# Generated at 2022-06-14 01:53:13.784401
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse("""{1: 1, **dict_a}""")

    # This should work without this line but mypy does not agree
    DictUnpackingTransformer().visit(module)  # type: ignore

# Generated at 2022-06-14 01:53:22.597457
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from unittest import TestCase, main
    from typed_ast import ast3 as ast

    class _T(TestCase):
        def _TR(self, code, expected) -> None:
            tree = ast.parse(code)
            DictUnpackingTransformer().visit(tree)
            self.assertEqual(ast.dump(tree), expected)

        def test_Dict_without_unpacking(self) -> None:
            self._TR('{1: 1}',
                     "Module(body=[Expr(value=Dict(keys=[Num(n=1)], values=[Num(n=1)]))])")


# Generated at 2022-06-14 01:53:23.600026
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer().__class__ == DictUnpackingTransformer



# Generated at 2022-06-14 01:53:24.638115
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    return DictUnpackingTransformer()

# Generated at 2022-06-14 01:53:35.669869
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = """
        x = {1: 1}
        y = {1: 1, **x}
    """
    tree = ast.parse(code)
    expected = """
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    
    
    x = {1: 1}
    y = _py_backwards_merge_dicts([{1: 1}], x)
    """
    DictUnpackingTransformer().visit(tree)
    result = compile(tree, '', 'exec')
    assert expected == inspect.getsource(result)

# Generated at 2022-06-14 01:53:46.823496
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from ..unparser import Unparser
    from ..utils.fake_libs import fake_typing_module

    @snippet
    def s():
        def f(a: int, *, b: int):
            print({
                "a": a,
                "b": b,
                **kwargs,
            })

    source = s.get_body()
    source_code = source.body[0].body[0]
    assert isinstance(source_code, ast.Print)
    assert isinstance(source_code.dest, ast.Name)
    assert source_code.dest.id == 'print'
    assert len(source_code.values) == 1
    assert isinstance(source_code.values[0], ast.Dict)
    # First elements of the dict is key-value pair.

# Generated at 2022-06-14 01:53:56.321635
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def assert_parse(src, expected):
        transformer = DictUnpackingTransformer()
        transformed = transformer.visit(ast.parse(src, '<test>'))
        assert ast.dump(transformed) == ast.dump(ast.parse(expected, '<test>'))

    # Case when nothing is transformed
    assert_parse(
        src='{}',
        expected='{}')

    assert_parse(
        src='{1: 1}',
        expected='{1: 1}')

    assert_parse(
        src='{1: 1, 2: 2}',
        expected='{1: 1, 2: 2}')

    assert_parse(
        src='{1: 1, **{}}',
        expected='{1: 1}')

    # Case when transformation is applied
    assert_parse