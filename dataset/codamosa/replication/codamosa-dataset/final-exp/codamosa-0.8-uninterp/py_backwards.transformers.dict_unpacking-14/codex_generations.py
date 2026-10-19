

# Generated at 2022-06-14 01:44:16.275329
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import parse

    module = parse(
        '{x: "a", y: "b", **a, **b, k: "k", 1: "1", **func()}')  # type: ignore
    assert str(module) == \
        '{x: "a", y: "b", **a, **b, k: "k", 1: "1", **func()}'

    transformer = DictUnpackingTransformer()
    module = transformer.visit(module)
    assert str(module) == \
        '_py_backwards_merge_dicts([{x: "a", y: "b"}, {k: "k", 1: "1"}], a, b, func())'


# Generated at 2022-06-14 01:44:24.240375
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    b = DictUnpackingTransformer()
    tree = ast.parse("""
        import *
        from *
    
        {**x}
    """)

    b.visit(tree)
    # TODO: check, that merged dicts function is not added to module twice
    # TODO: create complex tree with three layered dicts and assert that
    # _py_backwards_merge_dicts is called twice

# Generated at 2022-06-14 01:44:27.194484
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astor
    code = """{1: 1, **a, 2: 2, **b, 3: 3, **c}"""

# Generated at 2022-06-14 01:44:34.056481
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import copy
    import astor.source

    source = r"""
    {1: 2, **dict_a, **dict_b, 3: 4, **dict_c}
    
    {1: 2, **dict_a, **dict_b, 3: 4, **dict_c, **dict_d}
    
    {1: 2, **dict_a}
    
    {1: 2}
    
    {}
    
    {**dict_a}
    
    {**dict_a, **dict_b}
    """

    nodes = ast.parse(source)

# Generated at 2022-06-14 01:44:40.617751
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_ast.ast3 as ast
    transformer = DictUnpackingTransformer()
    source = '''{1: 1, **dict_a}'''
    expected = '''_py_backwards_merge_dicts([{1: 1}], dict_a)'''
    tree = ast.parse(source)
    transformer.visit(tree)
    code = compile(tree, '', 'exec')

    result = ''
    exec(code, globals())
    assert result == expected

# Generated at 2022-06-14 01:44:49.239157
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    ts = DictUnpackingTransformer()
    d = ast.parse('{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}')
    d.body[0].value.keys[0] = None
    d.body[0].value.keys[4] = None
    d.body[0].value.keys[5] = None
    d.body[0].value.keys[-1] = None
    result = ts.visit(d)
    assert isinstance(result.body[0].value, ast.Call)
    assert isinstance(result.body[0].value.args[0], ast.List)
    assert result.body[0].value.func.id == '_py_backwards_merge_dicts'

# Generated at 2022-06-14 01:44:53.509859
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    transformer = DictUnpackingTransformer()
    code = """
        def function(self):
            a = {"a": 1, **{}, "b": 2}
            b = {}
            b.update(a)
    """
    tree = ast.parse(code)
    result = transformer.visit(tree)
    expected = """
        _py_backwards_merge_dicts = _py_backwards_merge_dicts
        def function(self):
            a = _py_backwards_merge_dicts(dict(a=1), dict())
            b = dict()
            b.update(a)
    """
    assert ast.dump(result) == expected


# Generated at 2022-06-14 01:45:03.378257
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse('''{1: 1, 2: 2, **{'a': 'b', 'b': 'c', }, 3: 3, **x}''')
    assert node.body[0].value == ast.Dict(keys=[
        ast.Num(n=1), ast.Num(n=2), None, ast.Num(n=3), None],
        values=[ast.Num(n=1), ast.Num(n=2), ast.Dict(keys=[ast.Str(s='a'),
                                                           ast.Str(s='b')],
                                                    values=[ast.Str(s='b'),
                                                            ast.Str(s='c')]),
                ast.Num(n=3), ast.Name(id='x')])
    transformed = DictUnpackingTransformer().visit

# Generated at 2022-06-14 01:45:11.604899
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse

    source = '''
    {1: 1, **dict_a}
    '''

    node = ast.parse(source)
    DictUnpackingTransformer().visit(node)

    expected = '''
    (lambda _py_backwards_merge_dicts: _py_backwards_merge_dicts([{1: 1}], dict_a))(
        lambda dicts: dict(_py_backwards_merge_dicts(dicts))
    )
    '''

    assert astunparse.unparse(node) == dedent(expected).strip()

# Generated at 2022-06-14 01:45:21.697107
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = """
    a = {1: 1, **dict_a, **dict_b, 2: 2, **dict_c}
    """
    node = ast.parse(tree)
    xformer = DictUnpackingTransformer()
    result = xformer.visit(node)  # type: ignore
    ref = """
    _py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a, dict_b, dict_c)
    """
    ref = ast.parse(ref)
    assert ast.dump(result, include_attributes=True) == ast.dump(ref, include_attributes=True)

# Generated at 2022-06-14 01:45:39.539183
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import shippo
    source = '''\
        {1: 1, **dict_a}
    '''
    result = shippo.transform(source, 'snippets_dict_unpacking')
    assert '_py_backwards_merge_dicts([{1: 1}], dict_a)' in result

# Generated at 2022-06-14 01:45:41.199552
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.tree import parse
    from ..utils.dump import dump


# Generated at 2022-06-14 01:45:50.521149
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..testing_utils import transform_to_code
    assert transform_to_code(
        DictUnpackingTransformer,
        '{1: 1}') == '{1: 1}'
    assert transform_to_code(
        DictUnpackingTransformer,
        '{**a}') == '_py_backwards_merge_dicts([dict()], a)'
    assert transform_to_code(
        DictUnpackingTransformer,
        '{1: 1, *args, 5: \'d\', **kwargs}') == '_py_backwards_merge_dicts([{1:1, 5:\'d\'}, args, kwargs])'

# Generated at 2022-06-14 01:46:00.258061
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.ast_builder import build_ast

    node = build_ast('''
        {**dict_a}
    ''')
    assert DictUnpackingTransformer().visit(node) == build_ast('''
        _py_backwards_merge_dicts([], dict_a)
    ''')

    node = build_ast('''
        {'a': 1, **dict_a}
    ''')
    assert DictUnpackingTransformer().visit(node) == build_ast('''
        _py_backwards_merge_dicts([{'a': 1}], dict_a)
    ''')

    node = build_ast('''
        {1: 1, 'a': 1, **dict_a}
    ''')
    assert DictUn

# Generated at 2022-06-14 01:46:06.114598
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import CodegenState
    from .meta import transformer_from

    state = CodegenState()
    transformer = transformer_from(DictUnpackingTransformer, state)

    compiled = transformer.visit(ast.parse("""
        {
            **a, 
            'b': c,
            None: d, 
            **e,
            'f': g,
            **h,
            'i': j,
            None: k,
            'l': m
        }"""))


# Generated at 2022-06-14 01:46:11.522933
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..ast_converter import convert
    from ..utils.tree import ast_to_string

    source = '{1: 1, 2: "two"}'
    root = convert(source)
    DictUnpackingTransformer().visit(root)
    actual = ast_to_string(root)
    expected = '''{
    1: 1,
    2: 'two'
}'''
    assert actual == expected



# Generated at 2022-06-14 01:46:19.312229
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .context import Context
    from .source_replacer import SourceReplacer
    from .tools import ast_equal

    ctx = Context()
    ctx.update(merge_dicts.args)
    source = ast.parse('{1:1, **a, 2:2}', '', 'exec')
    expected = ast.parse('_py_backwards_merge_dicts([{1: 1, 2: 2}], a)', '', 'exec')
    result = SourceReplacer(
        DictUnpackingTransformer(ctx)).visit(source)

    assert ast_equal(expected, result)

# Generated at 2022-06-14 01:46:30.735593
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source, source_debug
    from ..utils.visitor import print_ast

    code = """
    from typing import Dict, Any

    def f(a: Dict[str, Any], b: Dict[str, str], c: Dict[int, Any]) -> Dict[str, str]:
        d = {
            'a': a,
            'b': b,
            **c,
        }
        return d
    """
    tree1 = source_debug(code)
    tree2 = source_debug(code)
    transformer = DictUnpackingTransformer()
    transformer.visit(tree1)
    print_ast(tree1)  # should contain _py_backwards_merge_dicts function
    tree2 = source(code)

# Generated at 2022-06-14 01:46:45.083481
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ...utils import _DictUnpackingTransformer as _DUT
    class _DictUnpackingTransformer(_DUT):
        def _split_by_None(self, pairs):
            return super()._split_by_None(pairs)

        def _prepare_splitted(self, splitted):
            return super()._prepare_splitted(splitted)

        def _merge_dicts(self, xs):
            from ..utils.tree import ast_equal
            self.assertTrue(
                ast_equal(
                    self._merge_dicts(xs),
                    ast.Call(func=ast.Name(id='_py_backwards_merge_dicts'),
                             args=[ast.List(elts=list(xs))],
                             keywords=[])))
            return

    ut = _D

# Generated at 2022-06-14 01:46:51.046989
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = """\
        {1:1, 2:2, **{3:3, 4:4}}
    """
    expect = """\
        _py_backwards_merge_dicts([{1: 1, 2: 2}], {3: 3, 4: 4})
    """
    result = DictUnpackingTransformer().visit(ast.parse(source))
    assert expect == astunparse.unparse(result)

# Generated at 2022-06-14 01:46:56.847833
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:47:09.256965
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from .base import TreeTransformerTestCase

    class DUT(DictUnpackingTransformer):
        pass


    class DUTTestCase(TreeTransformerTestCase):
        transformer_class = DUT

        def test_no_unpacking(self):
            case = ast.Dict(keys=[], values=[])
            expected = case

            self.assert_transformed_ast(case, expected)

        def test_simple(self):
            case = ast.Dict(keys=[ast.Num(1), ast.Num(2)],
                            values=[ast.Num(1), ast.Num(2)])
            expected = case

            self.assert_transformed_ast(case, expected)


# Generated at 2022-06-14 01:47:17.160164
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse('''{'foo': 'bar', 'bar': 'baz', **dict_a}''')
    tree = DictUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == dedent('''
        _py_backwards_merge_dicts([{'foo': 'bar', 'bar': 'baz'}], dict_a)
        ''').strip()

# Generated at 2022-06-14 01:47:22.986215
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transformer import Transformer
    from ..utils.codegen import to_source
    from ..utils.source import dedent

    class TestTransformer(Transformer):
        def visit_Dict(self, node):
            return node
    
    source = dedent('''
        {1: 1, **dict_a, **dict_b}
    ''')
    module = Transformer.run(source)
    test_module = TestTransformer.run(source)
    assert to_source(module) == to_source(test_module)

# Generated at 2022-06-14 01:47:30.048845
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .transformers_util import run_visitor


    in_module = '''
{1: 1, 2: 2, 3: 3, **a, **b, 4: 4, 5: 5, **c}
'''
    out_module = '''
_py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}, dict(4=4, 5=5)], a, b, c)
'''
    assert run_visitor(in_module, DictUnpackingTransformer).strip() == out_module

# Generated at 2022-06-14 01:47:39.393406
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from _ast import parse, Dict

    tree = parse('''
        {1: 2,
         3: 4,
         'qwerty': 'qwerty',
         1: 2,
         **{'big': 'small'},
         'asdf': 'asdf',
         **{'key': 'value'},
         1: 2}
    ''')

    expected_tree = parse('''
        _py_backwards_merge_dicts([{1: 2, 3: 4, 'qwerty': 'qwerty', 1: 2}, {'big': 'small'}, {'asdf': 'asdf'}, {'key': 'value'}, {1: 2}])
    ''')

    DictUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 01:47:47.476784
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ast
    import tests.utils.compile

    node = ast.parse("""
{
    'x': 10,
    **y,
    **z,
    'y': 20,
    **k,
    'z': 30,
}
""")
    transformer = DictUnpackingTransformer()
    result = transformer.visit(node)
    expected = """
_py_backwards_merge_dicts([
    {
        'x': 10,
        'y': 20,
        'z': 30,
    }
], y, z, k)
""".strip()
    assert tests.utils.compile.to_source(result) == expected



# Generated at 2022-06-14 01:47:51.258164
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_transformer import assert_transform

    assert_transform(
        DictUnpackingTransformer,
        '{1: 1, 2: 2, 3: 3, **var_a, **var_b, **var_c}',
        '{1: 1, 2: 2, 3: 3}.update(*[{}, var_a, var_b, var_c])'
    )



# Generated at 2022-06-14 01:47:59.653348
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import BaseNodeTransformer
    from .base import BaseNodeTransformerTester

    class Tester(BaseNodeTransformerTester):
        transformer = DictUnpackingTransformer
        code = """
            d = {'a': 1}
            d2 = {'b': 2, **d}
            d3 = {'c': 3, **d2}
            d4 = {'d': 4, 'e': 5, **d3}
            d5 = {'f': 6, **d4}
        """

# Generated at 2022-06-14 01:48:02.552741
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import to_source
    from ..utils.testing import rewrite

    kwargs = {'backwards': False}

# Generated at 2022-06-14 01:48:27.115953
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from ..utils.tree import parse

    transformer = DictUnpackingTransformer()
    src = '''
    def f(x: int, **kwargs: int) -> int:
        return {}
    '''
    node = parse(src)
    transformer.visit(node)
    assert astor.to_source(node) == '''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result


    def f(x: int, **kwargs: int) -> int:
        return _py_backwards_merge_dicts([], kwargs)
    '''

# Generated at 2022-06-14 01:48:37.984514
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    src = """
    x= {1: 1, **a}
    x= {**a, 2: 2}
    x= {1: 1, **a, 2: 2}
    x= {**a, 2: 2, 3: 3}
    x= {1: 1, **a, 2: 2, 3: 3}
    x= {1: 1, 2: 2, 3: 3, **a, 4: 4, 5: 5}
    x= {1: 1, 2: 2, 3: 3, **a, 4: 4, 5: 5, **b, 6: 6}
    x= {1: 1, 2: 2, 3: 3, **a, 4: 4, 5: 5, **b, 6: 6, **c, 7: 7}
    """
    

# Generated at 2022-06-14 01:48:44.366128
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transformer import Transformer
    from ..utils.source import source

    code = '''
        {1: 1, **dict_a}
    '''
    tree = ast.parse(source(code))
    flattened, _ = Transformer(tree).transform()
    assert source(flattened) == source('''
        __tmp__ = {}
        __tmp__.update(dict_a)
        __tmp__.update({1: 1})
    ''')

# Generated at 2022-06-14 01:48:54.271756
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .oracle_test import ast_test_equal

    tree = ast.parse("{1: 1, **{2: 2}, 3: 3, **{4: 4, 5: 5}, 6: 6}")
    ast_test_equal(tree, '''
        {1: 1, **_py_backwards_merge_dicts([{3: 3, 6: 6}], {2: 2, 4: 4, 5: 5})}
    ''')

    tree = ast.parse("{1: 1, **{2: 2}, 3: 3, **{4: 4, 5: 5}, **{6: 6}}")

# Generated at 2022-06-14 01:49:03.640122
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import BaseNodeTransformerTestCase

    class DictUnpackingTransformerTestCase(BaseNodeTransformerTestCase):
        transformer = DictUnpackingTransformer
        expected_result = {'a': 1, 'b': 2}

        def test_unpacking(self):
            source = 'a = {1: 1, **{2: 2, 3: 3}}'
            self.expected_code = """
                _py_backwards_merge_dicts([{1: 1}], {2: 2, 3: 3})
            """
            self.source = source

        def test_nested_unpacking(self):
            source = 'a = {1: 1, **{2: 2, **{3: 3}}}'

# Generated at 2022-06-14 01:49:05.893436
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from mm_compilers.compilers import compile_to_executable

# Generated at 2022-06-14 01:49:09.730249
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import parse
    from ..utils.ast_helpers import to_source
    from ..utils.misc import get_calls_names


# Generated at 2022-06-14 01:49:20.086529
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse
    from ..transforms import DictUnpackingTransformer

    code = r'''
a = {**a, **b}
c = {'a': 3, **c}
d = {1: 2, **d, 'a': 2}
    '''
    expected = r'''
a = _py_backwards_merge_dicts([], a, b)
c = _py_backwards_merge_dicts([{"a": 3}], c)
d = _py_backwards_merge_dicts([{1: 2}, {"a": 2}], d)
    '''
    tree = ast.parse(code)
    tree = DictUnpackingTransformer().visit(tree)
    assert astunparse.unparse(tree) == expected



# Generated at 2022-06-14 01:49:26.677731
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import dump
    node = ast.parse('''
        {a: 1, b: 2, **c, d: 3}
    ''')

    transformer = DictUnpackingTransformer()
    result = transformer.visit(node)
    assert dump(result) == '''
        _py_backwards_merge_dicts((
          {a: 1, b: 2},
          c,
          dict([(d, 3)])
        ))
    '''

# Generated at 2022-06-14 01:49:38.420056
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import _transform
    from ..ast_utils import dump
    from ..utils.python import is_python_2
    import textwrap
    import astor

    if is_python_2():
        return

    code = """
    {None, None, None, None, None, None, None, None, None, None}
    {None, None, 1, 2, None, None, None, None, None, None}
    {None, None, {None, None, 1, 2, None, None}, None, 1, 2, None}
    {1, 2, {None, None, 1, 2, None, None}, None, 1, 2, None}
    """


# Generated at 2022-06-14 01:50:11.982262
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse
    import ast

    # Code and expected result:
    code = """\
a = {1: 2, **b}"""
    expected = """\
a = _py_backwards_merge_dicts([{'1': '2'}], b)"""

    # Transforms tree:
    tree = ast.parse(code)
    transformer = DictUnpackingTransformer()
    transformed = transformer.visit(tree)  # type: ignore
    result = unparse(transformed)

    assert result == expected



# Generated at 2022-06-14 01:50:22.068671
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from ..compiler import PyCompiler

    code = r'''{1: 1, **dict_a}'''
    expected = r'''def _compile_time_function_0():
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    _py_backwards_merge_dicts([{1: 1}], dict_a)'''

    tree = ast3.parse(code)
    tree = PyCompiler.compile(tree)

    expected_tree = ast3.parse(expected)

    assert ast3.dump(tree) == ast3.dump(expected_tree)

# Generated at 2022-06-14 01:50:29.376169
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert str(DictUnpackingTransformer().visit(ast.parse(
        """
        {1: 1, **{2: 2}}
        """))) == \
        cleanup("""
        {1: 1, **{2: 2}}
        """)

    assert str(DictUnpackingTransformer().visit(ast.parse(
        """
        {1: 1, **{2: 2}, 2: 1, **{3: 2}}
        """))) == \
        cleanup("""
        _py_backwards_merge_dicts([{1: 1, 2: 1}], {2: 2}, {3: 2})
        """)

    assert str(DictUnpackingTransformer().visit(ast.parse(
        """
        {1: 1, **{2: 2}, 3: 3}
        """)))

# Generated at 2022-06-14 01:50:35.990346
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = textwrap.dedent(
        """\
        {
            'a': a,
            **d,
            'b': b,
        }""")
    target = textwrap.dedent(
        """\
        _py_backwards_merge_dicts(
            [
                {
                    'a': a,
                }
            ],
            d
        )""")

    assert DictUnpackingTransformer.run_single(source) == target

# Generated at 2022-06-14 01:50:47.648044
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import BaseNodeTransformerTestCase
    from ..utils.testing import get_comparison_ast

    class TestCase(BaseNodeTransformerTestCase):
        transform = DictUnpackingTransformer.visit_Dict

        def test_merge_dicts_1(self):
            src = """
                {1: 1, **dict_a}
                """
            exp = """
                _py_backwards_merge_dicts([{1: 1}], dict_a)
                """
            self.compare(src, exp)

        def test_merge_dicts_2(self):
            src = """
                {1: 1, **dict_a, 2: 2, **dict_b}
                """

# Generated at 2022-06-14 01:50:55.261620
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert "print({**{'a': 1}, **{}})" == \
           DictUnpackingTransformer.run_simple(
               "print({**{'a': 1}, **{}})")
    assert "print({'b': 2, **{}})" == \
           DictUnpackingTransformer.run_simple(
               "print({'b': 2, **{}})")
    assert "_py_backwards_merge_dicts([{'a': 1}], {})" == \
           DictUnpackingTransformer.run_simple(
               "print({'a': 1, **{}})")

# Generated at 2022-06-14 01:51:00.299022
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    x = ast.parse(
        """
        {'a': x, 'b': y, None: z, 'c': w}
        """)
    transformer = DictUnpackingTransformer()
    assert isinstance(transformer.visit(x), ast.Call)


# Generated at 2022-06-14 01:51:07.614328
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor  # type: ignore
    from ast import parse

    code = '{1: 1, **dict_a, **dict_b, 2: 2, **dict_c}'
    expected = '_py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a, dict_b, dict_c)'

    transformer = DictUnpackingTransformer()
    result = transformer.visit_Module(parse(code))

    assert astor.to_source(result) == expected

# Generated at 2022-06-14 01:51:19.648021
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .helpers import get_test_case_dict
    from .helpers import assert_source


# Generated at 2022-06-14 01:51:27.515176
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import Module, Dict, Name, Num, Call, Str

    code = """{1: 1, **{2: 2}, 3: 3, **{4: 4}, 5: 5}"""

    expected_code = """_py_backwards_merge_dicts([{1: 1}, 3: 3, 5: 5], {2: 2}, {4: 4})"""
    expected_ast = Module(body=[Call(func=Name(id='_py_backwards_merge_dicts'), args=[List(elts=[Dict(keys=[Num(n=1)], values=[Num(n=1)]), Num(n=3), Num(n=5)])], keywords=[])], type_ignores=[])

    tree = ast.parse(code)
    node_transformer = DictUnpackingTrans

# Generated at 2022-06-14 01:52:22.230620
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert DictUnpackingTransformer().visit(
        ast.parse("{1: 1, **dict_a}")) == ast.parse(
        """
        _py_backwards_merge_dicts([{1: 1}], dict_a})
        """)

# Generated at 2022-06-14 01:52:30.098528
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ...tests.testing import assert_tree
    from ...tests.testing import assert_tree_unchanged
    from ...tests.utils import parse


# Generated at 2022-06-14 01:52:38.943149
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_source_equal
    from .testing import wrap_in_module

    source = '''
        {1: 2, **a}
        '''
    expected = '''
        _py_backwards_merge_dicts([{1: 2}], a)
        '''
    assert_source_equal(wrap_in_module(source), expected)


# Generated at 2022-06-14 01:52:45.424454
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test_utils import assert_source
    from ..utils.format import multiline_repr

    source = multiline_repr(
        '',
        '{1: 1, **_a}',
        '',
    )

    expected = multiline_repr(
        '',
        '_py_backwards_merge_dicts([{1: 1}], _a)',
        '',
    )

    tree = ast.parse(source)

    transformer = DictUnpackingTransformer()
    tree = transformer.visit(tree)  # type: ignore
    assert_source(expected, tree)

# Generated at 2022-06-14 01:52:58.189073
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_transform, assert_transform_as, \
        assert_not_transformed, assert_not_transformed_as
    import typed_astunparse
    import ast
    import astunparse

    ast_src = r"""
        {1: 1, **dict_a}
        {1: 1, **dict_a, 2: 2, **dict_b}
        {1: 1, **dict_a, 2: 2}
        {**dict_a, 2: 2}
        {1: 1, **dict_a, 2: 2, **dict_b, 3: 3, **dict_c}
    """

# Generated at 2022-06-14 01:53:09.599735
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # TODO:
    # - comments
    # - line numbers

    compound = '''
        {1: 1, 2: 2, 3: 3, 5: 5, None: 100, 6: 6, None: 200, 6: 7}
    '''
    expected = '''
        _py_backwards_merge_dicts({1: 1, 2: 2, 3: 3, 5: 5},
                                  {1: 100, 2: 200, 6: 7},
                                  {1: 6})
    '''
    expected_node = ast.parse(expected).body[0].value
    node = ast.parse(compound)
    result = DictUnpackingTransformer().visit(node)
    assert result.body[0].value == expected_node

# Generated at 2022-06-14 01:53:19.738530
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    ast_ = ast.parse('''
{1: 1, 2: 2, **dict(), **x, **{42: 42}, **y, 3: 3, **dict(), 4: 4}
    ''')
    expected_ast_ = ast.parse('''
_py_backwards_merge_dicts(
    [{1: 1, 2: 2, 3: 3, 4: 4}], dict(), x, {42: 42}, y, dict()
)
    ''')

    code = compile(ast_, filename='<ast>', mode='exec')
    expected_code = compile(expected_ast_, filename='<ast>', mode='exec')

    namespace = {}
    exec(code, namespace)
    expected_namespace = {}
    exec(expected_code, expected_namespace)


# Generated at 2022-06-14 01:53:29.288932
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from ..utils.fixtures import ast_call, ast_dicts
    from ..utils.fixtures import standard_test
    
    source = """
    {None: None, 1: 1, None: None, **a, 2: 2, None: None, **b, 3: 3}
    """
    
    expected = _py_backwards_merge_dicts(
        [{2: 2, 3: 3}], a, b, {1: 1}
    )
    expected = ast_call(expected)
    
    transformer = DictUnpackingTransformer()
    result = standard_test(transformer, source, expected)
    pairs = zip(ast.iter_fields(result), ast.iter_fields(expected))

# Generated at 2022-06-14 01:53:40.687322
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    dict_ = ast.Dict(keys=[
        ast.Num(1),
        None,
        ast.Num(3),
        None,
        ast.Num(5)],
                      values=[
        ast.Num(1),
        ast.Dict(keys=[ast.Num(2)], values=[ast.Dict(keys=[ast.Num(2)],
                                                      values=[ast.Num(2)])]),
        ast.Num(3),
        ast.Dict(keys=[ast.Num(4)], values=[ast.Num(4)]),
        ast.Num(5)])

    call = DictUnpackingTransformer().visit(dict_)
    assert isinstance(call, ast.Call)
    assert isinstance(call.func, ast.Name)

# Generated at 2022-06-14 01:53:51.060392
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse as unp
    from .. import ast3 as ast3

    def check_transform(expr, expected):
        transformer = DictUnpackingTransformer()
        node = ast3.parse(expr)
        transformer.visit(node)
        transformed = unp(node)
        assert transformed == expected, (transformed, expected)

    expr = '{1: 1, 2: 2, **dict_a}'
    expected = ('_py_backwards_merge_dicts([dict(zip([1, 2], [1, 2]))], dict_a)'
                )
    check_transform(expr, expected)

    expr = '{1: 1, **dict_a, **dict_b}'