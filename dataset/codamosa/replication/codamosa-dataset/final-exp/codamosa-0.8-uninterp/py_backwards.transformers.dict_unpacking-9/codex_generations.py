

# Generated at 2022-06-14 01:44:13.797938
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..compiler import NodeTransformerCompiler
    from ..testutils.codegen import assert_one_liner_equal

    code = """\
x = {1: 2, 3: 4, **{"foo": "bar"}}
y = {1: 2, 3: 4, **{"foo": "bar"}}
z = {"foo": "bar"}
"""
    expected = """\
x = _py_backwards_merge_dicts([{1: 2, 3: 4}], {"foo": "bar"})
y = _py_backwards_merge_dicts([{1: 2, 3: 4}], {"foo": "bar"})
z = {"foo": "bar"}
"""
    compiled = NodeTransformerCompiler(DictUnpackingTransformer).compile_code(code)
    assert_one_liner_equal

# Generated at 2022-06-14 01:44:18.977815
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class Test(DictUnpackingTransformer):
        _tree_changed: bool

    source = ast.parse('{x: y, **z, a: b}')
    result = ast.parse('_py_backwards_merge_dicts([{x: y, a: b}], z)')
    expected = ast.Module(body=[result.body[0]])

    transformer = Test()
    assert transformer.visit(source) == expected

# Generated at 2022-06-14 01:44:29.322098
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:44:38.946414
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    class DictUnpackingTransformer(DictUnpackingTransformer):
        def _split_by_None(self, pairs: Iterable[Pair]) -> Splitted:
            return super()._split_by_None(pairs)

        def _prepare_splitted(self, splitted: Splitted) \
                -> Iterable[Union[ast.Call, ast.Dict]]:
            return super()._prepare_splitted(splitted)

        def _merge_dicts(self, xs: Iterable[Union[ast.Call, ast.Dict]]) \
                -> ast.Call:
            return super()._merge_dicts(xs)


# Generated at 2022-06-14 01:44:47.435287
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import parse
    from ..utils.tree import CodeTreeWalker, tree


# Generated at 2022-06-14 01:44:54.473236
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class TestTransformer(DictUnpackingTransformer):
        def __init__(self):
            self._tree_changed = False

        def is_tree_changed(self):
            return self._tree_changed

    node = ast.parse('{1: 1, 2: 2, [i, 1]: [1, 2], **a, 4: 4}')
    node = TestTransformer().visit(node)
    assert TestTransformer().is_tree_changed()

# Generated at 2022-06-14 01:44:57.415315
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse
    DictUnpackingTransformer().visit(parse("{**a, 1:2, 3:4, **b, 5:6, **c}"))

# Generated at 2022-06-14 01:45:07.975006
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.snippet import transform
    from enum import Enum
    import unittest
    import typing as t
    
    T = t.TypeVar('T')
    
    class Py3(t.Generic[T], Enum):
        X1 = 1
        X2 = 2
    
    def f(x: t.Dict[int, int], y1: t.Dict[int, int], y2: t.Dict[int, int]):
        return {1: Py3.X1, **x}
    
    result = transform(f, DictUnpackingTransformer)

# Generated at 2022-06-14 01:45:15.372834
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from astmonkey import transformers
    transformer = transformers.DictUnpackingTransformer()
    node = ast.parse(
        '{1: 1, 2: 2, None: 1, 3: 4, 4: 5, None: 2, 6: 7}')
    transformer.visit(node)
    result = astor.to_source(node)
    expected = ("_py_backwards_merge_dicts([{1: 1, 2: 2}, 1, {3: 4, 4: 5}, "
                "2, {6: 7}])")
    assert result == expected



# Generated at 2022-06-14 01:45:26.648260
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from ..utils.fake import FakeAST
    from ..utils.checker import assert_equal

    transformer = DictUnpackingTransformer()

    input_dict = ast3.Dict(keys=[], values=[])
    result_dict = transformer.visit(input_dict)
    assert_equal(input_dict, result_dict)

    input_dict = ast3.Dict(keys=[ast3.Str(s='a')], values=[ast3.Str(s='a')])
    result_dict = transformer.visit(input_dict)
    assert_equal(input_dict, result_dict)

    fake_a = FakeAST(input_dict)


# Generated at 2022-06-14 01:45:44.301825
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import UnitTestTransformer
    from ..utils.testing import roundtrip

    class T(UnitTestTransformer):
        def visit_Dict(self, node):
            return ast.Call(
                func=ast.Name(id='_py_backwards_merge_dicts'),
                args=[
                    ast.List(elts=node.values + [
                        ast.Call(func=ast.Name(id='dict'),
                                 args=[],
                                 keywords=[])]),
                    ast.Dict(keys=[
                        ast.Name(id='a'),
                        ast.Name(id='b')],
                        values=[
                            ast.List(elts=[]),
                            ast.List(elts=[])])],
                keywords=[])

    t = T(3)

# Generated at 2022-06-14 01:45:55.504707
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = """
    d = {'one': 1, **d, 'two': 2, **e} 
    """
    expected = """
    _py_backwards_merge_dicts([{'one': 1, 'two': 2}], d, e)
    """

    tree = ast.parse(code)
    DictUnpackingTransformer().visit(tree)
    generated = ast.fix_missing_locations(tree)
    assert ast.dump(generated) == expected

# Generated at 2022-06-14 01:46:02.340656
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    dut = DictUnpackingTransformer()
    input_ = ast.parse('{1: 1, **dict_a}')
    expected_output = ast.parse('''
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    ''')
    output = dut.visit(input_)
    assert ast.dump(expected_output, annotate_fields=False) == \
        ast.dump(output, annotate_fields=False)

# Generated at 2022-06-14 01:46:12.468410
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..ast import python_to_ast, replace_fields
    input_ = python_to_ast("""
        {1: 2, None: {3: 4}, 'test': 42, None: {5: 6},
            **dict_a, **dict_b}
    """)
    expected = python_to_ast("""
        _py_backwards_merge_dicts([{1: 2,
            'test': 42}, {3: 4}, {5: 6}], dict_a, dict_b)
    """)
    # Replace module name in LHS and RHS
    replace_fields(expected, module='__main__')
    # Run transformer
    transformer = DictUnpackingTransformer()
    output = transformer.visit(input_)
    assert output == expected

# Generated at 2022-06-14 01:46:18.969384
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    transformer = DictUnpackingTransformer()
    dict_ = ast.parse('{1:2, 3:4, **{5:6, 7:8}, 9:10}').body[0].value
    expected = ast.parse('_py_backwards_merge_dicts([{1:2, 3:4, 9:10}], {5:6, 7:8})').body[0].value

    actual = transformer.visit(dict_)

    assert expected == actual

# Generated at 2022-06-14 01:46:24.506707
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    visitor = DictUnpackingTransformer()
    source = '{1: 1, 2: 2, 3: 3, **dict_a}'
    source = ast.parse(source)
    parents = [None] * (len(source.body[0].body[0].body[0].value.values) + 1)
    parents[-1] = source.body[0].body[0]
    visitor.visit(source, parents)
    assert visitor._tree_changed is True

# Generated at 2022-06-14 01:46:34.155472
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:46:48.571498
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.fixtures import get_test_case_ast
    
    transformer = DictUnpackingTransformer()
    node = get_test_case_ast(__file__, 'DictUnpackingTransformer')
    transformer.visit(node)
    assert transformer._tree_changed
    assert isinstance(node.body[0], ast.Expr)
    assert isinstance(node.body[0].value, ast.Call)
    assert node.body[0].value.func.id == '_py_backwards_merge_dicts'
    assert isinstance(node.body[1], ast.Assign)
    assert isinstance(node.body[1].value, ast.Call)
    assert node.body[1].value.func.id == '_py_backwards_merge_dicts'

# Generated at 2022-06-14 01:46:56.782648
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse

    _code = astunparse.unparse(DictUnpackingTransformer().visit(
        ast.parse("""{1: 1, 2: 2, **{3: 3, 4: 4}, 5: 5}""")))
    assert _code == "_py_backwards_merge_dicts([dict({1: 1, 2: 2}), {3: 3, 4: 4}], {5: 5})"



# Generated at 2022-06-14 01:47:07.446249
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    node = ast.parse('a = {1: 1, **dict_a}')
    expected = ast.parse(dedent('''
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
        
        a = _py_backwards_merge_dicts([{1: 1}], dict_a)
        '''))
    assert transformer.visit(node) == expected

# Generated at 2022-06-14 01:47:18.248925
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:47:26.349484
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse('{1: 1, 2: 2, **x, 3: 3, **y}')
    tree = DictUnpackingTransformer().visit(tree)

    expected = ast.parse('''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    _py_backwards_merge_dicts([dict([(1, 1), (2, 2)]), x, dict([(3, 3)]), y])
    ''')

    assert ast.dump(tree, annotate_fields=False, include_attributes=False) == \
        ast.dump(expected, annotate_fields=False, include_attributes=False)



# Generated at 2022-06-14 01:47:36.761957
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import compare_ast, copy_ast, parse

    source = '''
    {1: 2, 3: 4, 5: 6, **dict_a, 7: 8, **dict_b, 9: 10, **dict_c}
    '''
    expected = '''
    _py_backwards_merge_dicts([{'1': 2, '3': 4, '5': 6}, 7, 8, _py_backwards_merge_dicts([{'9': 10}], dict_c)], _py_backwards_merge_dicts([], dict_b), dict_a)
    '''
    tree = parse(source)
    transformer = DictUnpackingTransformer()
    new_tree = transformer.visit(tree)
    assert compare_ast(new_tree, expected)

# Generated at 2022-06-14 01:47:41.797437
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .parser import parse
    from ..utils.dump import dump
    from ..compiler import Compiler

    code = "print({1: 2, **{}, **{3: 4}, 5: 6, **{}})"
    tree = parse(code)
    Compiler(tree).compile_to_java()
    assert dump(tree) == dump(parse("""\
print(_py_backwards_merge_dicts([{1: 2, 5: 6}], _py_backwards_merge_dicts([{}], _py_backwards_merge_dicts([{3: 4}], dict()))))
"""))

# Generated at 2022-06-14 01:47:49.800006
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_node_equal

    in_text = '''
{1: 1, **{2: 2}, 3: 3, **{4: 4}, 5: 5, **{6: 6}}
'''
    out_text = '''
_py_backwards_merge_dicts([{1: 1, 3: 3, 5: 5}, {2: 2}, {4: 4}, {6: 6}])
'''
    in_node = ast.parse(in_text)
    out_node = ast.parse(out_text)
    transformer = DictUnpackingTransformer()
    result = transformer.visit(in_node)
    assert_node_equal(result, out_node)  # type: ignore

# Generated at 2022-06-14 01:47:59.087110
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert_equal(ast.dump(ast.parse('{1: 1, **dict_a}')),
                 'Module(body=[Expr(value=Dict(keys=[Num(n=1), None], '
                 'values=[Num(n=1), Name(id="dict_a", ctx=Load())]))])')

# Generated at 2022-06-14 01:48:09.756104
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    node = ast.parse('{}')
    assert transformer.visit(node) == node

    node = ast.parse('{None: 10}')
    assert transformer.visit(node) == ast.parse('{None: 10}')

    node = ast.parse('{None: 10, None: 15}')
    assert transformer.visit(node) == ast.parse('{None: 10, None: 15}')

    node = ast.parse('{1: 10}')
    assert transformer.visit(node) == ast.parse('{1: 10}')

    node = ast.parse('{1: 10, None: 15}')

# Generated at 2022-06-14 01:48:16.211563
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse("""{x: value, y: 'value', z: z, **a, **b, **c, **d, **e}""")
    expected = ast.parse(
        """_py_backwards_merge_dicts([{x: value}, {y: 'value'}, {z: z}], a, b, c, d, e)""")
    assert expected.body[0].value.args == DictUnpackingTransformer().visit(node).body[0].value.args

# Generated at 2022-06-14 01:48:21.533580
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert DictUnpackingTransformer().visit(ast.parse('''
        a = {1: 1, 2: 2, **d}
    ''')) == ast.parse('''
        _py_backwards_merge_dicts([{1: 1, 2: 2}], d)
    ''')

# Generated at 2022-06-14 01:48:31.203880
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    node = ast.parse(
        '{"a": 1, 1: 1, None: {1: 1}, **a, **b, **c, "c": 2}')
    node = node.body[0].value
    assert isinstance(node, ast.Dict)
    assert len(node.keys) == 9
    assert node.keys[3] is None, node.keys[3]
    assert node.keys[5] is None, node.keys[5]
    assert node.keys[7] is None, node.keys[7]

    transformer = DictUnpackingTransformer()
    actual = transformer.visit(node)


# Generated at 2022-06-14 01:49:02.328008
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from .misc import parse, dump
    

# Generated at 2022-06-14 01:49:11.596390
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = """
        {
            1: 1,
            **dict1, 
            2: 2,
            3: 3,
            **dict2,
            4: 4
        }
    """
    expected = """
        _py_backwards_merge_dicts(
            [{1: 1, 2: 2, 3: 3}], dict1, dict2, {4: 4})
    """
    
    tree = ast.parse(source)
    ast.fix_missing_locations(tree)
    new_tree = DictUnpackingTransformer().visit(tree)
    new_source = astor.to_source(new_tree)
    assert new_source.strip() == expected.strip()


# Generated at 2022-06-14 01:49:15.384514
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    x = ast.parse("{1: 2, **{3: 4}}")
    assert DictUnpackingTransformer().visit(x) == ast.parse("""
        _py_backwards_merge_dicts([{1: 2}], {3: 4})
    """)

# Generated at 2022-06-14 01:49:25.877013
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = textwrap.dedent("""\
    def func():
        return {1: 1, 2: 2, 3: 3, **dict_a, **dict_b, 4: 4, 5: 5}
    """)

    result = textwrap.dedent("""\
    def func():
        return _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}, dict_a], dict_b, {4: 4, 5: 5})
    """)

    result_ast = ast.parse(result)
    transformer = DictUnpackingTransformer()
    transformed_ast = transformer.visit(ast.parse(code))
    assert ast.dump(result_ast) == ast.dump(transformed_ast)



# Generated at 2022-06-14 01:49:28.849889
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    code = '''
    {1: 2, **dict_a}
    '''

# Generated at 2022-06-14 01:49:37.576267
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    src = dedent("""
    x = {1: 2, **dict_a, **dict_b, **dict_c, 3: 4}
    """)
    expected = dedent("""
    _py_backwards_merge_dicts([{1: 2}, 3: 4], dict_a, dict_b, dict_c)
    """)
    node = ast.parse(src)
    DictUnpackingTransformer.run_visitor(node)
    assert expected == astor.to_source(node)

# Generated at 2022-06-14 01:49:41.206845
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert str(DictUnpackingTransformer().visit(ast.parse(''' 
{1: 1, 2: 2, **{3: 3}}
'''))) == ''' 
_py_backwards_merge_dicts([dict({1: 1, 2: 2}), {3: 3}])
'''

# Generated at 2022-06-14 01:49:52.692360
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    data = {
        'dict_a': ast.Dict(keys=[ast.Num(1), ast.Num(2)],
                           values=[ast.Num(3), ast.Num(4)]),
        'res': ast.Dict(keys=[ast.Num(1), ast.Num(2), None],
                        values=[ast.Num(1), ast.Num(2), ast.Dict(keys=[ast.Name(id='a')],
                                                                values=[ast.Num(2)])]),
    }

    before = ast.Module(body=[ast.Expr(value=data['res'])])

# Generated at 2022-06-14 01:50:04.678253
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:50:05.276828
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    pass

# Generated at 2022-06-14 01:50:39.230400
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor


# Generated at 2022-06-14 01:50:48.674433
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test_helpers import get_ast
    from ..utils.test_helpers import compare_trees

    source = """
{1: 1, **dict_a}
    """

    # This is the desired AST
    expected = """
_py_backwards_merge_dicts([{1: 1}], dict_a)
    """
    expected = get_ast(expected)

    # Transform the source AST
    source = get_ast(source)
    transformer = DictUnpackingTransformer()
    actual = transformer.visit(source)

    # Compare the two ASTs
    compare_trees(expected, actual)



# Generated at 2022-06-14 01:50:55.382779
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse
    import ast
    import io
    import sys

    buf = io.StringIO()
    sys.stdout = buf

    source = '''
        {1: 1, 2: 2, **a}'''
    source_ast = ast.parse(source)
    transformed_ast = DictUnpackingTransformer().visit(source_ast)
    print(astunparse.dump_tree(transformed_ast))

    sys.stdout = sys.__stdout__

# Generated at 2022-06-14 01:51:04.152100
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    some_dict, dict_a, dict_b, dict_c, dict_d = 'some_dict', 'dict_a', 'dict_b', 'dict_c', 'dict_d'
    t = DictUnpackingTransformer()
    assert t.visit(ast.parse(f'{{1: {some_dict}, **{dict_a}}}')) == ast.parse(f'_py_backwards_merge_dicts([{{1: {some_dict}}}], {dict_a})')  # noqa

# Generated at 2022-06-14 01:51:10.374721
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .. import compile_to_ast
    transform = DictUnpackingTransformer(target=DictUnpackingTransformer.target)
    compiled = compile_to_ast("""
    {1: 1, **dict_a}
    """, target=DictUnpackingTransformer.target)
    transform.visit(compiled)
    assert compile_to_ast(str(compiled),
                          target=DictUnpackingTransformer.target) == compiled

# Generated at 2022-06-14 01:51:22.528603
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from textwrap import dedent
    from ..utils.helpers import compare_source_code

    source_code = dedent("""
    d = {1: 2, **{'a': 'b'}, 2: 3, **{'a': 'c'}, **{'a': 'd'}, 3: 4}
    """)
    source_code_expected = dedent("""
    _py_backwards_merge_dicts([{1: 2, 2: 3, 3: 4}], {'a': 'b'}, {'a': 'c'}, {'a': 'd'})
    """)

    tree = ast.parse(source_code)
    DictUnpackingTransformer().visit(tree)
    source_code_actual = astor.to_source(tree)
    compare_

# Generated at 2022-06-14 01:51:31.915307
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import transform
    from . import ForwardAnnotator


# Generated at 2022-06-14 01:51:38.881483
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    src = '''
    {1: 1, 2: 2, **dict_a, **dict_b, **dict_c}
    '''
    node = ast.parse(src)
    expected = '''
    _py_backwards_merge_dicts([{1: 1, 2: 2}, dict_a, dict_b, dict_c])
    '''
    code = compile(transformer.visit(node), filename='<test>', mode='eval')
    assert expected == code.co_consts[0]

# Generated at 2022-06-14 01:51:46.040880
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transpile import transpile
    from ..visitor import get_ast

    def dict_unpacking():
        return {1: 1, **{2: 2}, 3: 3, **{4: 4}}

    tree = get_ast(dict_unpacking)
    tree = DictUnpackingTransformer().visit(tree)
    assert transpile(tree) == dict_unpacking()

# Generated at 2022-06-14 01:51:52.651334
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_base import BaseNodeTransformerTestCase

    class TestCase(BaseNodeTransformerTestCase):
        node_transformer = DictUnpackingTransformer

        def test_case_1(self):
            # type: () -> None
            source = """
            {1: 1, **a}
            """
            expected = """
            _py_backwards_merge_dicts([{1: 1}], a)
            """
            result = self.transform(source)
            self.assertMultiLineEqual(result, expected)

        def test_case_2(self):
            # type: () -> None
            source = """
            {1: 1, **a, 3: 3, **b}
            """

# Generated at 2022-06-14 01:52:54.239766
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transform_dict = DictUnpackingTransformer().visit_Dict

    def test_transform_dict(*args):
        tree, = args
        assert isinstance(tree, ast.Dict)
        return transform_dict(tree)

    tree = ast.parse('{1: 1, 2: 2, **dict_a, **dict_b}')
    expected = ast.parse('''
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result

        _py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a, dict_b)
    ''')
    new = transform_dict(tree.body[0])
    assert ast.dump(new)

# Generated at 2022-06-14 01:53:00.155115
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor  # type: ignore

    code = """
    {1: 1, **dict_a}
    """
    module = ast.parse(code)
    DictUnpackingTransformer().visit(module)
    result = astor.to_source(module)  # type: ignore
    assert result == """_py_backwards_merge_dicts([({1: 1})], dict_a)"""

# Generated at 2022-06-14 01:53:15.672444
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse
    from .. import transform

    snippet = """
    x = {1: 2}
    x = {1: 2, **{3: 4}}
    x = {1: 2, **{3: 4}, **{5: 6}}
    x = {1: 2, **{3: 4}, 4: 5, **{5: 6}}
    x = {
      1: 2,
      2: 3,
      **{3: 4},
      4: 5,
      5: 6
    }
    """

# Generated at 2022-06-14 01:53:23.529103
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor

    class DictUnpackingTransformer_visit_Dict(DictUnpackingTransformer):
        """Temporary class for checking code of method visit_Dict."""
        def __init__(self):
            super().__init__(level=1)

        def _split_by_None(self, pairs):
            return super()._split_by_None(pairs)

        def _prepare_splitted(self, splitted):
            return super()._prepare_splitted(splitted)

        def _merge_dicts(self, xs):
            return super()._merge_dicts(xs)

    # Checking for situation when dict doesn't contain unpacking.

    transformer = DictUnpackingTransformer_visit_Dict()

# Generated at 2022-06-14 01:53:31.696688
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .tester import run_module
    from typed_ast import ast3 as ast

    @run_module
    def test_transformer():
        node = ast.Dict(
            keys=[ast.Num(n=1), None, None, None, None, ast.Num(n=2)],
            values=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3), ast.Num(n=4),
                    ast.Dict(keys=[ast.Num(n=0)], values=[ast.Num(n=0)]),
                    ast.Num(n=3)])
        transformed = DictUnpackingTransformer().visit(node)  # type: ignore

# Generated at 2022-06-14 01:53:41.939223
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '''
    {
        'good': a,
        **b,
        **c,
        'bad': a,
        **d,
        'ugly': a,
        1: 1,
        **e,
        'good': a,
        **f,
        **g,
        'bad': a,
        **h
    }
    '''
    expected = '''
    _py_backwards_merge_dicts([{'good': a,
                                'bad': a,
                                1: 1,
                                'ugly': a,
                                'good': a,
                                'bad': a}],
                              b, c, d, e, f, g, h)
    '''

# Generated at 2022-06-14 01:53:52.225963
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..tests.utils import make_snippet

    transformer = DictUnpackingTransformer()

    code = make_snippet(dict_unpacking=
                        '''
                        {
                            1: 1,
                            **{2: 2},
                            3: 3,
                            **{4: 4}
                        }
                        ''')
    expected = make_snippet(dict_unpacking=
                            '''
                            _py_backwards_merge_dicts(
                                [
                                    {1: 1},
                                    dict({2: 2}),
                                    {3: 3},
                                    dict({4: 4})
                                ]
                            )
                            ''')
    
    transformer.visit(ast.parse(code))  # type: ignore
    value = astor