

# Generated at 2022-06-14 01:44:16.839305
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from .transformer_test import run_transformer_test

    code = dedent("""\
    d1 = {1:2}
    d2 = {**d1}
    d3 = {1:2, **{3:4}}
    d4 = {1:2, **{3:4}, 5:6}
    d5 = {1:2, **{3:4}, 5:6, 7:8}
    d6 = {1:2, **d1, 3:4}
    d7 = {1:2, **d1, 3:4, **d1}
    d8 = {1:2, **d1, 3:4, **{5:6}, 7:8}
    """)


# Generated at 2022-06-14 01:44:25.341331
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test_utils import assert_equal_ast
    from ..utils import parse_string_to_ast
    from .test_utils import clean_transformed_code, BaseNodeTransformerTest

    code = 'd = {a: b, **c, d: e}'
    expected = clean_transformed_code('''
        _py_backwards_merge_dicts([{a: b, d: e}], c)
    ''')
    tree = parse_string_to_ast(code, 3)
    transformer = BaseNodeTransformerTest(DictUnpackingTransformer, tree)
    result = transformer.result
    assert_equal_ast(result, expected)

# Generated at 2022-06-14 01:44:32.543822
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    module = ast.parse("""
{1: 2, **dict_a, 3: 4}
{1: 2, **{}, 3: 4}
{1: 2, **dict_a}
{1: 2}
{**dict_a}
""", '<test>', 'exec')

    DictUnpackingTransformer().visit(module)

    assert ast.dump(module) == """
__py_backwards_merge_dicts([dict(1=2), dict_a, dict(3=4)])
__py_backwards_merge_dicts([dict(1=2), dict(), dict(3=4)])
__py_backwards_merge_dicts([dict(1=2), dict_a])
{1: 2}
dict_a
"""

# Generated at 2022-06-14 01:44:42.320182
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse
    from astor.code_gen import to_source
    import astpretty

    code = '''{
        'foo': 'bar',
        **{'bar': 'baz'},
        123: 456,
        **{
            'baz': 'bazzer',
            **{
                'abc': 'abc'
            }
        },
        'abc': 'abc'
    }'''

    node = ast.parse(code)
    DictUnpackingTransformer().visit(node)
    result = to_source(node).strip()
    result = result.replace('_py_backwards_merge_dicts', 'dummy')

# Generated at 2022-06-14 01:44:53.829843
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_transformer import make_one
    import typed_astunparse

    transformer = make_one(DictUnpackingTransformer)
    result = transformer.visit(ast.parse("{1: 1, **{2: 2, 3: 3}}"))
    expected = ast.parse("__t_1 = dict({2: 2, 3: 3}, __placeholder__)")
    assert typed_astunparse.unparse(result) == typed_astunparse.unparse(expected)

    result = transformer.visit(ast.parse("{1: 1, 2: 2, **{2: 2, 3: 3}}"))
    expected = ast.parse("_py_backwards_merge_dicts([{1: 1, 2: 2}], {2: 2, 3: 3})")
    assert typed_astunparse

# Generated at 2022-06-14 01:45:04.806793
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.example import example
    from ..utils.testing_utils import assert_equivalent_nodes
    from ..utils.tree import to_source
    from ..utils.visitor import TreeVisitor

    def test(source):
        node = example(source)
        transformed = DictUnpackingTransformer().visit(node)
        print(to_source(transformed))

    source = """
    {1: 1, 2: 2, 3: 3, **dict_a}
    """
    expected = """
    _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], dict_a)
    """
    test(source)
    assert_equivalent_nodes(example(expected), example(source))


# Generated at 2022-06-14 01:45:12.910856
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '''
        {1: 2, 4: 5, **{3: 4}}
    '''
    expected_code = '''
        _py_backwards_merge_dicts([{1: 2, 4: 5}], {3: 4})
    '''
    node = ast.parse(code)
    DictUnpackingTransformer().visit(node)  # type: ignore
    assert ast.dump(node) == expected_code

# Generated at 2022-06-14 01:45:22.263978
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    source = """\
{1: 1, 2: 2, **dict_a, 3: 3, **dict_b, 4: 4, **dict_c}
"""
    expected = """\
_py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3, 4: 4}], dict_a, dict_b, dict_c)
"""

    node = ast.parse(source)
    transformer = DictUnpackingTransformer()
    new_node = transformer.visit(node)
    result = ast.unparse(new_node)

    assert result == expected

# Generated at 2022-06-14 01:45:31.058553
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = """{'a': 1, 'b': 2, **d}"""

    expected = """
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
new_dict = {'a': 1, 'b': 2}
_py_backward_merge_dicts([new_dict], d)"""

    node = ast.parse(source)
    DictUnpackingTransformer().visit(node)
    assert ast.dump(node) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 01:45:36.722763
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    pairs = [
        (ast.Num(1.0), ast.Num(2.0)),
        (None, ast.Name(id='a')),
        (ast.Str('s'), ast.Num(3.0))
    ]
    keys, values = zip(*pairs)
    d = ast.Dict(keys=keys, values=values)

    t = DictUnpackingTransformer()
    m = ast.Module([ast.Expr(value=d)])
    m = t.visit(m)
    assert isinstance(m, ast.Module)
    assert isinstance(m.body[0].value, ast.Call)
    assert isinstance(m.body[1].value, ast.Num)

# Generated at 2022-06-14 01:45:51.948696
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from .tester import node_test, assert_compile

    @node_test
    def test_compile(node, mode):
        transformer = DictUnpackingTransformer(mode)
        transformer.visit(node)
        return transformer._tree_changed

    test_compile(ast.Dict(keys=[ast.Num(n=1)], values=[ast.Num(n=1)]), True)
    test_compile(ast.Dict(keys=[None, ast.Num(n=1)], values=[ast.Num(n=1)]),
                 True)
    test_compile(ast.Dict(keys=[ast.Num(n=1), None], values=[ast.Num(n=1)]),
                 True)

# Generated at 2022-06-14 01:45:59.982343
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ast import parse
    from ..utils.tree import dump
    from ..utils.constants import TEST_CODE

    code = TEST_CODE['dict_unpacking']
    node_1 = parse(code)
    dump(node_1)
    node_2 = DictUnpackingTransformer.run_visit(node_1)
    dump(node_2)
    assert DictUnpackingTransformer.was_changed()


# Generated at 2022-06-14 01:46:00.530201
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    pass

# Generated at 2022-06-14 01:46:12.468366
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typing import List


# Generated at 2022-06-14 01:46:19.572373
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse
    from pathlib import Path
    import astor
    from ast_tools.transforms import DictUnpackingTransformer
    from ast_tools.utils import node_from_file, dump_tree

    original = node_from_file(
        Path(__file__).parent / 'data' / 'dict_unpacking.py')
    transformer = DictUnpackingTransformer()
    transformed = transformer.visit(original)
    dump_tree(transformed)
    assert unparse(transformed) == unparse(original)

# Generated at 2022-06-14 01:46:30.975201
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    assert ast.dump(transformer.visit(ast.parse('{1: 1, 2: 2}'))) == \
        ast.dump(ast.parse('{1: 1, 2: 2}'))
    assert ast.dump(transformer.visit(ast.parse('{1: 1, 2: 2, **dict_a}'))) == \
        ast.dump(ast.parse(
            '_py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a)'
        ))

# Generated at 2022-06-14 01:46:45.265979
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..visitor import DictUnpackingTransformer
    def test(program, expected):
        actual = DictUnpackingTransformer().visit(ast.parse(program))
        print(expected, '=', ast.dump(actual), sep='\n')
        assert ast.dump(actual) == expected

# Generated at 2022-06-14 01:46:53.420264
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:46:59.662060
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.snippet import assert_compile

    assert_compile(
        '''
        d = {1:1, **dict_a}
        ''',
        '''
        d = _py_backwards_merge_dicts([{1: 1}], dict_a)
        '''
    )



# Generated at 2022-06-14 01:47:10.572803
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import BaseNodeTransformerTestCase
    class Test(BaseNodeTransformerTestCase):
        target = DictUnpackingTransformer

    t = Test()

    # 1. {1: 1, **dict_a} => _py_backwards_merge_dicts([{1: 1}], dict_a})
    t.assert_transform(
        '{1: 1, **dict_a}',
        """
        _py_backwards_merge_dicts([
            {1: 1}],
            dict_a)
        """,
        'dict_a')

    # 2. {**dict_a} => dict_a
    t.assert_transform(
        '{**dict_a}',
        'dict_a',
        'dict_a')

    # 3. {} => {}
    t

# Generated at 2022-06-14 01:47:18.335476
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()



# Generated at 2022-06-14 01:47:19.185462
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    transformer = DictUnpackingTransformer()

# Generated at 2022-06-14 01:47:28.302339
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Given
    transformer = DictUnpackingTransformer()
    node = ast.parse("""
    {1: 2, 3: 4, **a}
    """)  # type: ast.Module

    # When
    new_root = transformer.visit(node)  # type: ignore

    # Then
    assert transformer._tree_changed
    assert transformer.stats['transforms'] == 1

# Generated at 2022-06-14 01:47:38.247865
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astor.source_repr import to_source
    from ..patterns import find_all

    code = """
d1 = {1: 2, 3: 4}
d2 = {5: 6, **d1}
d3 = {7: 8, **{9: 10}}
d4 = {11: 12, **d3, **d2}
    """
    compiled = compile(code, '<test>', 'exec',
                       ast.PyCF_ONLY_AST, optimize=0)
    assert all(isinstance(d, ast.Dict)
               for d in find_all(compiled, ast.Dict))

    DictUnpackingTransformer().visit(compiled)

    assert all(isinstance(d, ast.Call)
               for d in find_all(compiled, ast.Call))


# Generated at 2022-06-14 01:47:48.367675
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # {'a': 1}
    assert ast.dump(DictUnpackingTransformer().visit(ast.parse('{\'a\': 1}'))) == \
        "Dict(keys=[Str(s='a')], values=[Num(n=1)])"
    # {'a': 1, **{'b': 2}}

# Generated at 2022-06-14 01:47:53.637056
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse('{1: 1, **a, 2: 2, **b}, c = 3, d = 4')
    transformer = DictUnpackingTransformer()
    new_node = transformer.visit(node)
    assert str(new_node) == '_py_backwards_merge_dicts([{1: 1, 2: 2}], a, b)'

# Generated at 2022-06-14 01:48:00.906233
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import test_assert_equal, NodeTestCase, normalize, \
        assert_equal, run_test

    run_test(__file__, 'test_DictUnpackingTransformer_visit_Dict', 'dict_unpacking')

    class Test(NodeTestCase):
        target = (3, 4)
        transformer = DictUnpackingTransformer

        def test_call(self):
            code = '{1: 1, **dict_a}'
            expected = '_py_backwards_merge_dicts([{1: 1}], dict_a)'
            self.assert_transformation(code, expected)

        def test_dict_without_unpacking(self):
            code = '{1: 1, 2: 2}'
            expected = '{1: 1, 2: 2}'

# Generated at 2022-06-14 01:48:05.371283
# Unit test for method visit_Module of class DictUnpackingTransformer

# Generated at 2022-06-14 01:48:06.097557
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer()

# Generated at 2022-06-14 01:48:07.522286
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    unpacking = DictUnpackingTransformer()



# Generated at 2022-06-14 01:48:15.986847
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse("""
    def f(a):
        return {1: a, **a}
    def g():
        return {1: 1, **dict_b}
        """)
    expected = None
    DictUnpackingTransformer.run(tree)
    assert ast.dump(tree) == ast.dump(expected)


# Generated at 2022-06-14 01:48:17.574856
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer


# Generated at 2022-06-14 01:48:18.613015
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:48:29.273873
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from py_mini_racer.transforms.utils import get_tree

    def get_transformed(source: str):
        tree = get_tree(source)
        transformer = DictUnpackingTransformer()
        transformer.visit(tree)
        return tree

    assert ast3.dump(get_transformed('{1: 2}')) == 'Module(body=[{1: 2}])'


# Generated at 2022-06-14 01:48:30.283610
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    x = DictUnpackingTransformer()


# Generated at 2022-06-14 01:48:36.704442
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    from ..utils.testing import assert_program

    assert_program(
        DictUnpackingTransformer,
        """
        a = {
            'a': 1,
            'b': 2,
            **d,
            'c': 3,
            **e,
            'd': 4,
        }
        """,
        """
        a = _py_backwards_merge_dicts([{'a': 1, 'b': 2}, d, {'c': 3}, e, {'d': 4}])
        """
    )

# Generated at 2022-06-14 01:48:38.638261
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    x = DictUnpackingTransformer()
    assert x is not None

# Generated at 2022-06-14 01:48:48.495912
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .translate import translate
    from .transform_imports import ImportStmtTransformer
    from .remove_unnecessary_imports import RemoveUnnecessaryImports
    from ..utils import get_ast
    from textwrap import dedent

    src = dedent("""
    from typing import Dict
    
    d = {1: 2, 3: 4, **{'abc': 'abc', 'xyz': 'xyz'}}
    """)
    tree = get_ast(src)
    assert isinstance(tree, ast.Module)  # type: ignore

    node = tree.body[2]
    assert isinstance(node, ast.Assign)
    assert isinstance(node.value, ast.Dict)

    tree = ImportStmtTransformer(3, 'typing').visit(tree)
    tree = DictUn

# Generated at 2022-06-14 01:48:52.089977
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    class DictUnpackingTransformerTest(DictUnpackingTransformer):
        pass
    return DictUnpackingTransformerTest

transformer = DictUnpackingTransformer()  # type: Union[None, BaseNodeTransformer]

# Generated at 2022-06-14 01:48:53.929976
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:49:08.644122
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    transformer = DictUnpackingTransformer(target=(3, 5))
    assert transformer is not None

# Generated at 2022-06-14 01:49:19.106740
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import parse
    from ..utils.unparse import unparse

    source = '''
        dict_a = {1: 1, 3: 3}
        dict_b = {2: 2, **dict_a}
        dict_c = {1: 1, **dict_a, **dict_b}
        '''  # noqa: E501


# Generated at 2022-06-14 01:49:21.211402
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer.__name__ == 'DictUnpackingTransformer'

# Generated at 2022-06-14 01:49:30.279027
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tf = DictUnpackingTransformer()
    tf7 = DictUnpackingTransformer(target=(3, 7))
    assert tf.target == (3, 4)
    assert tf7.target == (3, 7)
    code = '{1: 1, 2: 2, 3: 3}'
    code_res = ast.parse(code)
    node = ast.parse('{1: 1, 2: 2, None: {} }')
    node_res = ast.parse('_py_backwards_merge_dicts([{1: 1, 2: 2}], {})')
    node2 = ast.parse('{None: {}, 1: 1, 2: 2}')

# Generated at 2022-06-14 01:49:35.740048
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_transform
    assert_transform(DictUnpackingTransformer,
                     """
                     {1: 1, **{2: 2}}
                     """,
                     """
                     _py_backwards_merge_dicts([dict({1: 1}), {2: 2}])
                     """)

# Generated at 2022-06-14 01:49:46.406951
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    import astunparse
    from .base import roundtrip


# Generated at 2022-06-14 01:49:48.712912
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert isinstance(DictUnpackingTransformer(), DictUnpackingTransformer)

# Unit tests for _split_by_None

# Generated at 2022-06-14 01:49:59.106465
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor


# Generated at 2022-06-14 01:50:02.378361
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    transpiler = DictUnpackingTransformer()
    assert transpiler.target == (3, 4)

# Generated at 2022-06-14 01:50:04.125511
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    dut = DictUnpackingTransformer()
    assert isinstance(dut, BaseNodeTransformer)

# Generated at 2022-06-14 01:50:23.799099
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    # type: () -> None
    _DictUnpackingTransformer = DictUnpackingTransformer()



# Generated at 2022-06-14 01:50:35.750608
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3

    schema = {
        '_py_backwards_merge_dicts': {
            'type': 'function',
            'returns': {'type': 'dict'}
        },
        'None': {
            'type': 'null',
        }
    }

    def run(code: str) -> ast3.Call:
        node = ast3.parse(code)
        node = DictUnpackingTransformer.run(node)
        node = astor.to_source(node)
        node = ast3.parse(node)
        return node.body[0].value  # type: ignore

    # Test that:
    # {**{1: 2, 3: 4}} => _py_backwards_merge_dicts([{1: 2, 3: 4}])
   

# Generated at 2022-06-14 01:50:47.230789
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ...test.test_transformer import test_transform
    
    src = '''
        class A:
            def __init__(self, dict_a, dict_b=None, dict_c=None):
                self.dict = {1: 1, **dict_a, **dict_b, 2: 2, **dict_c}
    '''

    expected = '''
        class A:
            def __init__(self, dict_a, dict_b=None, dict_c=None):
                self.dict = _py_backwards_merge_dicts([{1: 1}, dict_a, dict_b, {2: 2}], dict_c)
    '''

    test_transform(src, expected, DictUnpackingTransformer)



# Generated at 2022-06-14 01:50:50.071491
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    """Unit test for method visit_Module of class DictUnpackingTransformer."""
    import astor
    code = """\
{1:2}
"""

# Generated at 2022-06-14 01:51:00.446634
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # type: () -> None

    class V(DictUnpackingTransformer):

        def __init__(self, tree_changed: bool):
            super().__init__()
            self._tree_changed = tree_changed

        def generic_visit(self, node: ast.AST) -> ast.AST:
            return node

    def to_ast(s: str) -> ast.Dict:
        return ast.parse(s).body[0].value  # type: ignore

    def to_src(node: ast.AST) -> str:
        return compile(ast.fix_missing_locations(
                ast.Module(body=[ast.Expr(value=node)])),
            "<test>", "exec").co_consts[0].co_consts[0].co_consts[0]

    assert to_src

# Generated at 2022-06-14 01:51:10.374996
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class DummyClass(object):
        pass
    Dict = DummyClass()
    Call = DummyClass()
    Name = DummyClass()
    List = DummyClass()

# Generated at 2022-06-14 01:51:22.528871
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    FOO_BAR_BAZ = ast.Name(id='foo_bar_baz')
    FOO_BAR_BAR = ast.Name(id='foo_bar_bar')
    SOME_VALUE = ast.Name(id='some_value')

    code = """
        {1: 1, **foo_bar_baz, **foo_bar_bar}
    """
    expected_code = """
        _py_backwards_merge_dicts(
            [
                {1: 1},
                foo_bar_baz,
                foo_bar_bar,
            ])
    """

    class DummyNodeTransformer(ast.NodeTransformer):
        def visit_Name(self, node: ast.Name) -> ast.Name:
            return globals()[node.id]  # type: ignore

   

# Generated at 2022-06-14 01:51:30.385224
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '{**d, 0: 0}, {2: 2, **d, 1: 1}, {0: 0}, {**d, **d}'
    tree = ast.parse(source)
    DictUnpackingTransformer().visit(tree)
    expected = '_py_backwards_merge_dicts([{0: 0}], d) == dict(d) and _py_backwards_merge_dicts([{2: 2}, {1: 1}], d) == dict(d) and dict(d) and dict(d)'   # noqa: E501
    actual = astor.to_source(tree)
    assert expected == actual

# Generated at 2022-06-14 01:51:40.027276
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from astmonkey import transformers
    from textwrap import dedent
    from .test_base import BaseTestAnnotation
    from .test_base import BaseTestTransformer

    class ConstructorTest(BaseTestAnnotation):
        transformer = transformers.DictUnpackingTransformer

        def test_default_init(self):
            self.assertIsNotNone(self.transformer())  # type: ignore
            self.assertEqual(self.transformer().target, (3, 4))  # type: ignore
            self.assertEqual(self.transformer()._tree_changed, False)  # type: ignore

    class ModuleTest(BaseTestTransformer):
        transformer = transformers.DictUnpackingTransformer


# Generated at 2022-06-14 01:51:48.330523
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = dedent("""\
    {
        1: 1,
        **dict1,
        2: 2,
        **dict2
    }
    """)

    expected = dedent("""\
    _py_backwards_merge_dicts([{1: 1, 2: 2}], dict1, dict2)
    """)

    check_transformation(DictUnpackingTransformer, source, expected)



# Generated at 2022-06-14 01:52:27.366446
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node_orig = ast.parse("{1: 1, **dict_a}")

# Generated at 2022-06-14 01:52:38.057534
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = """
        foo = {1: 1, **a, **b, 3: 3, **c}
        """
    expected = """
        foo = _py_backwards_merge_dicts([{1: 1, 3: 3}, a, b, c])
        """

    old_tree = ast.parse(code)
    new_tree = DictUnpackingTransformer().visit(old_tree)
    assert ast.dump(new_tree, annotate_fields=False) == expected


# Generated at 2022-06-14 01:52:38.959121
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:52:44.052375
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .test_generator import from_str
    from ..utils.ast import (
        dump,
        remove_comments,
        is_equal,
    )
    from ..utils.source import (
        split,
        indent,
    )

    source = """
        foo = {1: 1, 2: 2, 3: 3, **dict_a}
    """
    expected_result = """
        _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], dict_a)
    """

# Generated at 2022-06-14 01:52:57.514033
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from pytest import raises
    from .helpers import assert_code_equal

    obj = DictUnpackingTransformer()
    result = obj.visit(ast.parse("{1: 1, **{}}"))  # type: ignore
    assert_code_equal("_py_backwards_merge_dicts([{1: 1}], {})", result)

    with raises(TypeError):
        obj.visit(ast.parse("{1: 1, **{}, 4: 5}"))  # type: igore

    result = obj.visit(ast.parse("{1: 1, **dict_a, 2: 2, **dict_b, 3: 3}"))  # type: ignore

# Generated at 2022-06-14 01:53:00.908170
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    # type: () -> None
    assert DictUnpackingTransformer().__class__.__name__ == 'DictUnpackingTransformer'

# Generated at 2022-06-14 01:53:02.236240
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:53:09.227456
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..unparser import Unparser
    source = '{"a": 1, **dict_a}'
    tree = ast.parse(source)
    tree = DictUnpackingTransformer().visit(tree)
    assert Unparser(tree).code == '_py_backwards_merge_dicts([{"a": 1}], dict_a)'

# Generated at 2022-06-14 01:53:15.012749
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from .base import TransformationTestCase

    class TestTransformer(TransformationTestCase):

        target = (3, 4)
        transform = DictUnpackingTransformer

        def test_transform_with_unpacking(self):
            snippet = """{1: 1, **{}}"""
            expected = """_py_backwards_merge_dicts([{1: 1}], {})"""
            self.check(snippet, expected)

        def test_transform_with_multiple_unpacking(self):
            snippet = """{1: 1, **{1: 1}, 2: 2, **{}}"""
            expected = """_py_backwards_merge_dicts([{1: 1}], {1: 1}, {2: 2}, {})"""
            self.check(snippet, expected)


# Generated at 2022-06-14 01:53:22.597177
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = parse_ast("""
    {1: 1, 2: 2, **{"a": 1}}
    """)

    expected = parse_ast(r"""
    import typed_ast.ast3
    def _py_backwards_merge_dicts():
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
    _py_backwards_merge_dicts([{1: 1, 2: 2}, {"a": 1}])
    """)  # noqa: E501

    DictUnpackingTransformer().visit(tree)

    assert compare_ast(tree, expected)