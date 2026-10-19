

# Generated at 2022-06-14 01:44:11.374947
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '''\
        {1: 1, **dict_a}
    '''
    expected = '''\
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    '''
    tree = ast.parse(code)  # type: ignore
    transformer = DictUnpackingTransformer()
    result = transformer.visit(tree)
    assert pretty_compare(expected, ast.unparse(result))



# Generated at 2022-06-14 01:44:18.636795
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    module = """
    {1: 2, **{}}
    """
    expected = """
    _py_backwards_merge_dicts([{1: 2}], {})
    """
    module_node = ast.parse(dedent(module))
    expected_node = ast.parse(dedent(expected))
    actual_node = DictUnpackingTransformer().visit(module_node)
    assert ast.dump(expected_node) == ast.dump(actual_node)


# Generated at 2022-06-14 01:44:28.943519
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from ..utils.context import Context
    from ..utils.visitor import Visitor

    # Setup
    _co = Context()
    _co.update({'_py_backwards_merge_dicts': merge_dicts})

    _visitor = Visitor(_co)

    # Given
    class _MyTransformer(DictUnpackingTransformer):
        pass

    _node = ast.parse(dedent("""
        {1: 1, **dict_a}
    """))

    # When
    _result = _MyTransformer.run(_node)
    _actual = _visitor.visit(_result)

    # Then
    _expected = dedent("""
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """).strip

# Generated at 2022-06-14 01:44:37.794609
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    class Dummy(ast.AST):
        _fields = ()

    transformer = DictUnpackingTransformer()
    assert isinstance(transformer.visit(ast.Dict(keys=[], values=[])), ast.Dict)
    result = transformer.visit(ast.Dict(keys=[None], values=[ast.List()]))
    assert isinstance(result, ast.Call)

    result = transformer.visit(ast.Dict(
        keys=[None, None, None], values=[Dummy(), Dummy(), Dummy()]
    ))
    assert isinstance(result, ast.Call)

# Generated at 2022-06-14 01:44:41.398077
# Unit test for method visit_Module of class DictUnpackingTransformer

# Generated at 2022-06-14 01:44:50.005417
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:45:02.865574
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    # Input data
    node = ast.parse('{1: 1, **{2: 2, 3: 3}, 4: 4, 5: 5}')
    # Expected result
    expected = ast.parse('_py_backwards_merge_dicts([{1: 1, 4: 4, 5: 5}], {2: 2, 3: 3})')

    # We actually want to test method `visit_Module`,
    # but it's easy to test method `visit_Dict`
    DictUnpackingTransformer(node, '+x').visit_Dict(node.body[0].value)

    assert ast.dump(expected) == ast.dump(node)

# Generated at 2022-06-14 01:45:09.102799
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse("""\
import dis
dis.dis(compile("{1: 1, **{'A': 2}, **{3: 4}}", "<string>", "eval"))""")
    DictUnpackingTransformer().visit(module)  # type: ignore
    print(ast.dump(module))
    # TODO: add asserts


# Generated at 2022-06-14 01:45:19.764272
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import run_tests, make_code
    from ..utils.codegen import c2py
    from ..utils.test_utils import assert_equal

    def transform_code(code: str) -> str:
        x = DictUnpackingTransformer(make_code(code)).visit(c2py(code))
        return ast.unparse(x)

    def test_01():
        code = '{a: 1, b: 2, **c}'
        res = '_py_backwards_merge_dicts([{a: 1, b: 2}], c)'
        assert_equal(transform_code(code), res)

    def test_02():
        code = '{a: 1, b: 2, **c, **d}'

# Generated at 2022-06-14 01:45:30.200725
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    tree = ast.parse("""
    a = {'a': 1, **b}
    """)

    result = DictUnpackingTransformer().visit(tree)


# Generated at 2022-06-14 01:45:45.096289
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    # pylint: disable=no-member, unused-variable
    import ast as _ast
    source = r'''
    {1: 1, **dict_a}
    '''
    actual = _ast.dump(_ast.parse(source),
                       annotate_fields=False)
    expected = r'''
    Module(body=[Expr(value=Call(func=Name(id='_py_backwards_merge_dicts', ctx=Load()), args=[List(elts=[Dict(keys=[], values=[Dict(keys=[Constant(value=1)], values=[Constant(value=1)])]), Name(id='dict_a', ctx=Load())], ctx=Load()), keywords=[]))])
    '''

    from ..utils.ast import are_asts_equal
    assert are_

# Generated at 2022-06-14 01:45:48.401134
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    transform = DictUnpackingTransformer()

# Generated at 2022-06-14 01:45:53.356793
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = '''\
{1: 1, **{'a': 'a'}, **dict_b}
'''

# Generated at 2022-06-14 01:46:02.166311
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_unchanged


# Generated at 2022-06-14 01:46:04.846515
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer(target=(3, 4)).target == (3, 4)


# Generated at 2022-06-14 01:46:06.165045
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():    
    pass


# Generated at 2022-06-14 01:46:12.127072
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse('a = 1')
    DictUnpackingTransformer().visit(module)
    assert ast.dump(module) == \
"""Module(body=[Expr(value=Call(func=Name(id='_py_backwards_merge_dicts', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=1))])"""


# Generated at 2022-06-14 01:46:17.051381
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    source = """{1: 1, **dict_a}"""
    expected = """{1: 1, **dict_a}"""
    node = ast.parse(source)

    DictUnpackingTransformer().visit(node)

    actual = astor.to_source(node)
    assert source == actual

# Generated at 2022-06-14 01:46:18.991090
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer().target == (3, 4)

# Generated at 2022-06-14 01:46:22.007412
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    class Test(DictUnpackingTransformer):
        _tree_changed = False
    module = ast.parse('a = 1')
    Test().visit(module)
    assert module.body[0].value.args[0].elts == merge_dicts.get_body()

# Generated at 2022-06-14 01:46:33.801287
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    x = dict(a=1, **dict(c=3))
    assert x == {'a': 1, 'c': 3}
    x = dict(a=1, **dict(b=2, **dict(c=3)))
    assert x == {'a': 1, 'b': 2, 'c': 3}
    x = dict(a=1, **dict(b=2, **dict(c=3, **dict(d=4, **dict(e=5)))))
    assert x == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    d = dict(b=2, **dict(c=3), d=4)
    assert d == {'b': 2, 'c': 3, 'd': 4}

# Generated at 2022-06-14 01:46:46.905194
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_pypy_ast_equal
    from typed_ast import ast3 as ast
    ast1 = ast.parse("{1: 1}")
    ast2 = ast.parse("{1: 1, **a}")
    ast3 = ast.parse("{1: 1, **a, 2: 2, **b}")
    ast4 = ast.parse("{1: 1, **a, **b}")
    ast5 = ast.parse("{}")
    ast6 = ast.parse("{**a, **b}")
    ast7 = ast.parse("{**a}")
    ast8 = ast.parse("{1: 2, **{}}")
    ast9 = ast.parse("{1: 1, 2: 2, **a}")

# Generated at 2022-06-14 01:46:56.019100
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.codegen import to_source
    from ..utils.tree import tree_to_str

    expr = '''
        {'a': 1, 2: 2, **{3: 3}, 'b': 1, **{4: 4}}
    '''
    node = ast.parse(expr)
    node = DictUnpackingTransformer().visit(node)  # type: ignore
    as_str = tree_to_str(node)

    expected = '''
    _py_backwards_merge_dicts([
        {'a': 1, 2: 2},
        {3: 3},
        {'b': 1},
        {4: 4}
    ])
    '''
    expected = expected.strip()

    assert as_str == expected, as_str

# Generated at 2022-06-14 01:47:00.226234
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_astunparse
    import astunparse
    node = ast.parse('{1: 1, **{2: 2}, 3: 3}')
    type_comment_module_transformer = DictUnpackingTransformer()
    output = typed_astunparse.unparse(type_comment_module_transformer.visit(node))
    expected = astunparse.unparse(ast.parse('_py_backwards_merge_dicts({1: 1, 3: 3}, {2: 2})'))
    assert output == expected

test_DictUnpackingTransformer_visit_Dict()

# Generated at 2022-06-14 01:47:06.127792
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse("{1: 1, **dict_a}")
    expected = ast.parse(merge_dicts() + "\n{1: 1, **dict_a}")
    node = DictUnpackingTransformer().visit(module)
    assert ast.dump(node) == ast.dump(expected)


# Generated at 2022-06-14 01:47:15.869426
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astor
    from dmoj.cptbox.handlers import CptboxSyscallFilterHandler
    from dmoj.executors.script_executor import ScriptExecutor
    from dmoj.transformer import Transformer

    with open('tests/eval_tests/test_dict_unpacking.py') as f:
        source = f.read()

    tree = ast.parse(source)
    formatted_source, _ = Transformer(
        DictUnpackingTransformer,
        ScriptExecutor(CptboxSyscallFilterHandler)
    ).transform_snippet(source, '<eval_test>')
    assert astor.to_source(tree) == formatted_source, \
        'Failed to apply the DictUnpackingTransformer.'

# Generated at 2022-06-14 01:47:17.603987
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer(None).__class__ == DictUnpackingTransformer



# Generated at 2022-06-14 01:47:23.511208
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.ast_factory import parse
    from ..transformer import Transformer
    from ..utils import NodeTransformerTestCase

    class TestTransformer(Transformer):
        node_transformer = DictUnpackingTransformer

    tr = NodeTransformerTestCase()
    tr.test_tree = parse(tr.test_tree)
    tr.expected_tree = parse(tr.expected_tree)
    tr.transformer = TestTransformer()
    tr.check_transformer()

# Generated at 2022-06-14 01:47:31.134437
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import textwrap

    node = ast.parse('{None: None, **dict_a}')
    expected = ast.parse(textwrap.dedent("""
    from functools import reduce

    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    _py_backwards_merge_dicts([{}], dict_a)
    """))
    assert DictUnpackingTransformer().visit(node) == expected

# Generated at 2022-06-14 01:47:35.834871
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import ast3 as ast

    module = ast.parse("{}")
    transformer = DictUnpackingTransformer()
    new_module = transformer.visit(module)
    assert new_module.body[0] == merge_dicts.get_body()[0]  # type: ignore


# Generated at 2022-06-14 01:47:40.351873
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    x = DictUnpackingTransformer()

# Generated at 2022-06-14 01:47:48.518964
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_astunparse import unparse

    source = """
    x = {1: 1, **a, 2: 2, **b, 3: 3}
    """

    expected = """
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    x = _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], a, b)
    """

    node = ast.parse(source)
    DictUnpackingTransformer().visit(node)  # type: ignore
    assert unparse(node) == expected

# Generated at 2022-06-14 01:47:49.825067
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    transformer = DictUnpackingTransformer()
    assert transformer

# Generated at 2022-06-14 01:47:59.121358
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .test_base import transform
    from typed_ast import ast3 as ast
    from textwrap import dedent

    src = dedent('''\
        def f(**kwargs):
            {1: 1, **kwargs}
        ''')
    src_expected = dedent('''\
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
        
        
        def f(**kwargs):
            _py_backwards_merge_dicts([{1: 1}], kwargs)
        ''')
    node_transformed = transform(ast.parse(src), DictUnpackingTransformer)

# Generated at 2022-06-14 01:48:09.757541
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..compiler import compile_snippet
    from ..utils.tree import convert_to_source

    snippet = '''{1: 2, **{3: 4}, 5: 6, **{7: 8}, **{9: 10, 11: 12}}'''
    module = compile_snippet(snippet)
    node = module.body[0].value
    assert isinstance(node, ast.Call)
    assert isinstance(node.args[0], ast.List)

# Generated at 2022-06-14 01:48:16.211544
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = """
        {1: 1, **dict_a}
    """
    expected = """
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """
    node = ast.parse(code)  # type: ignore
    transformer = DictUnpackingTransformer()
    new_node = transformer.visit(node)  # type: ignore
    transformer._tree_changed = False

    assert ast.dump(new_node) == expected  # type: ignore



# Generated at 2022-06-14 01:48:18.309532
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    # type: () -> None
    assert DictUnpackingTransformer() is not None

# Generated at 2022-06-14 01:48:23.548634
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .test_transformer import run_test

    source = """\
{1:2, 3:4, **{5:6}, {7:8}}"""

# Generated at 2022-06-14 01:48:32.985662
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    # type: () -> None
    in_code = '''
    x = {**{}}
    y = {'a': 1, **{'b'}}
    z = {'c': 2, **{'d': 3, 'e': 4}, 'f': 5, **{'g': 6}}
    '''

    out_code = '''
    x = _py_backwards_merge_dicts([{}])
    y = _py_backwards_merge_dicts([{'a': 1}], {'b'})
    z = _py_backwards_merge_dicts([{'c': 2}], {'d': 3, 'e': 4}, {'f': 5}, {'g': 6})
    '''

    checker = DictUnpackingTransformer()
    assert checker

# Generated at 2022-06-14 01:48:40.381724
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import ast3

    test_module = ast3.parse("""
        def f(x):
            return {1: 1, **x}
        """)

    assert test_module.body[0].body[0].value == ast3.parse('{1: 1, **x}')

    DictUnpackingTransformer().visit(test_module)

    assert test_module.body[0].body[0].value == ast3.parse('_py_backwards_merge_dicts([{1: 1}], x)')

# Generated at 2022-06-14 01:48:49.230425
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    module = ast.parse("{'a': 0, **b, **c}")
    DictUnpackingTransformer().visit(module)



# Generated at 2022-06-14 01:48:56.954889
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    _dict = (None, ast.Dict(keys=[], values=[]))
    pairs = [(_dict,), (_dict,), (_dict,)]
    split = DictUnpackingTransformer._split_by_None(None, pairs)
    assert split == [[], ast.Dict(keys=[], values=[]), [], ast.Dict(keys=[], values=[]), [], ast.Dict(keys=[], values=[])]
    assert split == [[], ast.Dict(keys=[], values=[]), [], ast.Dict(keys=[], values=[]), [], ast.Dict(keys=[], values=[])]

# Generated at 2022-06-14 01:49:04.140442
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from ..utils.testing import assert_ast_equal

    def process(code):
        from . import DictUnpackingTransformer
        return DictUnpackingTransformer(ast.parse(code)).visit(
            ast.parse(code))  # type: ignore

    code = '''
    {1: 1, **dict_a}
    '''
    expected_code = '''
    _py_backwards_merge_dicts([{1: 1}], dict_a)
    '''
    assert_ast_equal(process(code), ast.parse(expected_code))

# Generated at 2022-06-14 01:49:06.031120
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .test_fixtures import DictUnpackingTransformerTestCase
    DictUnpackingTransformerTestCase(DictUnpackingTransformer).run_tests()

# Generated at 2022-06-14 01:49:17.596378
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    pairs = [(None, ast.Dict(keys=[], values=[])),
             (None, ast.Dict(keys=[], values=[])),
             (ast.Num(n=1), ast.Num(n=2))]
    node = ast.Dict(keys=[key for key, _ in pairs],
                    values=[value for _, value in pairs])

    result = DictUnpackingTransformer().visit(node)
    assert isinstance(result, ast.Call)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args[0], ast.List)
    assert isinstance(result.args[0].elts[0], ast.Dict)
    assert isinstance(result.args[0].elts[1], ast.Call)

# Generated at 2022-06-14 01:49:23.198112
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from tests.util import create_ast
    from .common import apply_transformers

    tree = create_ast('{1: 1, **{1: 2}}')
    apply_transformers(DictUnpackingTransformer, tree)

    assert tree == create_ast('_py_backwards_merge_dicts([{1: 1}], {1: 2})')

# Generated at 2022-06-14 01:49:25.601475
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import ast3 as ast

    source = '''
{1: 2, 3: 4}
'''

# Generated at 2022-06-14 01:49:33.420443
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    expr = ast.parse('{1:1, **dict_a}')
    assert expr.body[0].value.keys == [ast.Num(1), None]
    transformer = DictUnpackingTransformer()
    result = transformer.visit(expr)
    assert result.body[0].value.func.id == '_py_backwards_merge_dicts'
    assert len(result.body[0].value.args[0].elts) == 2

# Generated at 2022-06-14 01:49:41.788829
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from ..utils.testing import transform
    from .test_conditional_expressions import test_DictUnpackingTransformer as \
        cond_test
    from .test_argument_unpacking import test_DictUnpackingTransformer as \
        unpack_test

    target = DictUnpackingTransformer.target

    tree = ast.parse("{1: 1, **{2: 2}}")
    transform(tree, DictUnpackingTransformer, target=target)
    assert cond_test()

    tree = ast.parse("{1: 1, **dict_a, **{2: 2}, 3: 3}")
    transform(tree, DictUnpackingTransformer, target=target)
    assert unpack_test()

# Generated at 2022-06-14 01:49:53.259466
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_transformer import run_visitor_test
    from ...utils.pyannotated_ast import transform

    nodes = [
        ast.Dict(keys=[
            ast.Constant(value=1),
            None,
            ast.Str(s='x'),
            ast.Constant(value=None)],
            values=[
            ast.Constant(value=1),
            ast.Name(id='dict_a'),
            ast.Constant(value=2),
            ast.Constant(value=3)])
    ]

# Generated at 2022-06-14 01:50:14.182427
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    source = textwrap.dedent("""
    a = {1: 1, **a}
    """)
    expected = textwrap.dedent("""
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result


    a = _py_backwards_merge_dicts([{1: 1}], a)
    """)
    assert expected == compile_snippet(source, DictUnpackingTransformer).strip()


# Generated at 2022-06-14 01:50:23.800701
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    string_src = '''{**a, 2: 3}'''
    expected_result = '''from typed_ast import ast3 as ast
from typing import Union, Iterable, Optional, List, Tuple
{
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    d = _py_backwards_merge_dicts([a, {2: 3}])
}'''
    tree = ast.parse(string_src)
    result = DictUnpackingTransformer().visit(tree)
    assert ast.dump(result) == expected_result


# Generated at 2022-06-14 01:50:26.477367
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    t = DictUnpackingTransformer()
    assert isinstance(t, DictUnpackingTransformer)

# Generated at 2022-06-14 01:50:34.041806
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source
    from ..utils.tests import assert_node

    code = source('''
        {a: 1, b: 2, **c, **d}
        ''')

    expected = source('''
        _py_backwards_merge_dicts([{'a': 1, 'b': 2}], c, d)
        ''')

    actual = DictUnpackingTransformer().visit(ast.parse(code))

    assert_node(expected, actual)

# Generated at 2022-06-14 01:50:39.579794
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse('''
    {1: 1, **dict1, **dict2, None, 3: 3, **dictn}
    ''')
    result = DictUnpackingTransformer().visit(tree)

    expected_tree = ast.parse('''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    _py_backwards_merge_dicts([{1: 1}, dict1, dict2, {3: 3}], dictn)
    ''')
    assert result == expected_tree

# Generated at 2022-06-14 01:50:50.945749
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_ast.ast3 as ast

    from .lib.context import Context

    ctx = Context()
    ctx.name = 'target'
    ctx.node = ast.Dict(keys=[ast.Constant(value=1), None, ast.Constant(value=3)],
                        values=[ast.Constant(value=1), ast.Constant(value=2), ast.Constant(value=3)])
    ctx.transformer_cls = DictUnpackingTransformer

# Generated at 2022-06-14 01:50:52.003558
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:51:03.118299
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import PrettifyNodeTransformer
    from ..utils.asserts import assert_tree_equal
    from .unpacking import UnpackingTransformer

    dut = DictUnpackingTransformer()

    source = 'def foo():\n    a = {1: 2, **{3: 4}}'
    actual = dut.transform(source)

    expect = (
        'def foo():\n'
        '    a = _py_backwards_merge_dicts([{1: 2}], {3: 4})'
    )

    print(PrettifyNodeTransformer().visit(actual))
    assert_tree_equal(actual, expect)

    source = 'def bar():\n    a = {1: 2, 3: 4, **{5: 6}}'
    actual = dut.transform(source)

# Generated at 2022-06-14 01:51:05.419413
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    # type: () -> None
    assert repr(DictUnpackingTransformer(None)) == \
        "DictUnpackingTransformer(None)"

# Generated at 2022-06-14 01:51:07.325185
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:51:45.989929
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.fake_ast import AST

    class TestCases(NamedTuple):
        tree: AST
        expected_tree: AST


# Generated at 2022-06-14 01:51:54.721336
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import textwrap
    from ..utils.source import Source
    from ..utils.dump import dump_tree

    m = merge_dicts()

    source = textwrap.dedent('''
    {1: 1, **dict_a, 2: 2}
    ''')

    expected = textwrap.dedent('''
    {1: 1, 2: 2}
    ''').strip()

    source = Source(source)
    tree = source.parse()
    tree = tree.body[0]
    transformer = DictUnpackingTransformer()
    tree = transformer.visit(tree)
    tree.lineno = 1
    tree.col_offset = 0

    assert transformer._tree_changed is True
    assert dump_tree(tree) == expected


# Generated at 2022-06-14 01:52:05.658595
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from .base import UnitTestTransformer
    from .utils import run_transformer

    class Test(UnitTestTransformer):
        transformer = DictUnpackingTransformer()

        @property
        def _merge_dicts_source(self) -> str:
            return merge_dicts.get_source()

        def test_noop_dict_unpacking(self) -> None:
            source = '{**{}}'
            expected = '{}'
            self._assert_codecompare(source, expected)

        def test_simple_dict_unpacking(self) -> None:
            source = '{**{1: 1}}'
            expected = self._merge_dicts_source + '{}'
            self._assert_codecompare(source, expected)


# Generated at 2022-06-14 01:52:15.122446
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..compiler import translate

    node = ast.parse('{1: 1, **dict_a}')
    DictUnpackingTransformer().visit(node)
    code = translate(node)
    assert code.strip() == \
        'def _py_backwards_merge_dicts(dicts):\n' \
        '    result = {}\n' \
        '    for dict_ in dicts:\n' \
        '        result.update(dict_)\n' \
        '    return result\n\n' \
        '_py_backwards_merge_dicts([{1: 1}], dict_a)'


# Generated at 2022-06-14 01:52:16.144782
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:52:24.908377
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_utils import round_trip, transform_from_func

    def merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result


# Generated at 2022-06-14 01:52:26.574043
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:52:34.526418
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert DictUnpackingTransformer(3, 4).visit(ast.parse('{1: 1, 2: 2, **dict_a}')) == \
           ast.parse(_merge_dicts('''\
         _py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a)'''))



# Generated at 2022-06-14 01:52:36.185337
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:52:37.730931
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer()

# Generated at 2022-06-14 01:53:08.629423
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    transformer = DictUnpackingTransformer()
    assert transformer is not None

# Generated at 2022-06-14 01:53:10.636863
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    o = DictUnpackingTransformer()
    assert o  # using just to shut up pylint

# Generated at 2022-06-14 01:53:11.671701
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer() is not None

# Generated at 2022-06-14 01:53:20.321222
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    import sys
    import io
    from ..utils.testing import assert_source

    src = '''
{1: 1, **dict_a}
{2: 2, **dict_b}
{**dict_a, **dict_b, **dict_c}
{}
{1:1, 2:2}
{**dict_a}
{**dict_b}
{}
{}
{1:1, **dict_a, 2:2}
'''

# Generated at 2022-06-14 01:53:28.746611
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from textwrap import dedent

    source = """\
        {1: 1, **dict_a}
    """
    expect = dedent("""\
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
        
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """)

    node = ast.parse(source)
    DictUnpackingTransformer().visit(node)
    result = compile(node, '', 'exec').co_consts[1]
    assert result == expect



# Generated at 2022-06-14 01:53:38.156624
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    code = """
    {a: 1, **dict_a}
    """
    tree = ast.parse(code)

    transformer = DictUnpackingTransformer()
    assert transformer.visit(tree).body[0] == \
        ast.Expr(ast.Call(
            func=ast.Name(id='_py_backwards_merge_dicts'),
            args=[ast.List(elts=[
                ast.Dict(keys=[ast.Name(id='a')], values=[ast.Num(1)]),
                ast.Name(id='dict_a')])],
            keywords=[]))



# Generated at 2022-06-14 01:53:43.178001
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    
    ast_orig  = ast.parse('x = {1: foo, 2: bar, **baz, 3: def}')
    ast_trans = DictUnpackingTransformer().visit(ast_orig)
    assert astor.to_source(ast_trans) == '_py_backwards_merge_dicts([{1: foo, 2: bar}, dict(baz)], 3: def)'



# Generated at 2022-06-14 01:53:51.588735
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source_to_ast, ast_to_source
    from ..utils.string import dedent
    sample = dedent("""
        a = {1: 1, **dict_a}
        """)
    sample_ast = source_to_ast(sample)
    expected = dedent("""
        _py_backwards_merge_dicts([{1: 1}], dict_a)
        """)

    sample_ast = DictUnpackingTransformer().visit(sample_ast)
    actual = ast_to_source(sample_ast).replace('\n', '')
    assert actual == expected

# Generated at 2022-06-14 01:53:57.582922
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    module = transformer.visit(ast.parse('''
{
    1: 2,
    **a,
    **b,
    3: 4,
    **c
}
'''))
    assert str(module) == '''
_py_backwards_merge_dicts([{1: 2}, {3: 4}], a, b, c)
'''