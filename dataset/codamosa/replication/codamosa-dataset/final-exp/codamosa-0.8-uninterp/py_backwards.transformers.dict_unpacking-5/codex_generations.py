

# Generated at 2022-06-14 01:44:05.803777
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from .test_transformers import run_transformer
    from .test_transformers import assert_source_matches

    dict_unpacking_transformer = DictUnpackingTransformer()
    code = '''
        a = {1: 1, 2: 3+2, **{3: 4}, 6: 5}
        b = {1: 2, 3: 3, **{}, 5: 6}
    '''

# Generated at 2022-06-14 01:44:16.005323
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import textwrap
    from typed_ast import ast3, parse, parse3
    module = ast3.parse(textwrap.dedent('''\
        def func(a, b, c):
            d = {1: 1, 2: 2, 3: 3, **a, **b, 4: 4, **c}
            return d'''))
    root = DictUnpackingTransformer().visit(module)

# Generated at 2022-06-14 01:44:24.080994
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import parse


# Generated at 2022-06-14 01:44:31.246457
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert (ast.dump(
        DictUnpackingTransformer().visit(ast.parse(
            """
            {1: 1, 2: 2, "3": 3, **{4: 4}}
            """
        ))) == ast.dump(
        ast.parse(
            """
            _py_backwards_merge_dicts([{1: 1, 2: 2, '3': 3}], {4: 4})
            """
        ),
    ))



# Generated at 2022-06-14 01:44:42.225472
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import run_local_tests
    from ..utils import unparse


# Generated at 2022-06-14 01:44:50.907511
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from ..utils.ast_compare import assert_equal, to_source

    def f(a, b):
        return {a: None, **b}

    expected = \
        """def f(a, b):
    return _py_backwards_merge_dicts([{a: None}], b)
"""

    dut = DictUnpackingTransformer()
    result = dut.visit(ast.parse(to_source(f)))  # type: ignore
    assert_equal(result, ast.parse(expected))

# Generated at 2022-06-14 01:44:59.565756
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class T(DictUnpackingTransformer):
        def __init__(self):
            self.visit_Dict = self._visit_Dict
            self._tree_changed = False
            self._transformed = None

    def check(pairs, expected_code, expected_changed=True):
        node = ast.Dict(keys=[key for key, _ in pairs],
                        values=[value for _, value in pairs])
        t = T()
        t.visit(node)
        assert t._transformed == expected_code
        assert t._tree_changed == expected_changed


# Generated at 2022-06-14 01:45:11.303969
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..testing import assert_transform


# Generated at 2022-06-14 01:45:21.034769
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node = ast.parse('{1: 1, 2: 2, None: {3: 3}, 4: 4}')
    actual = DictUnpackingTransformer().visit(node)
    expected = ast.parse('''
        def _py_backwards_merge_dicts(xs):
            result = {}
            for x in xs:
                result.update(x)
            return result


        _py_backwards_merge_dicts([{1: 1, 2: 2}, dict({3: 3}), {4: 4}])
    ''')
    assert ast.dump(actual, include_attributes=False) \
        == ast.dump(expected, include_attributes=False)

# Generated at 2022-06-14 01:45:26.694068
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    return """
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result

        x = {**dict_a}
        y = {1: 1, 2: 2}
        z = {1: 1, **dict_b, 2: 2, **dict_c}
    """



# Generated at 2022-06-14 01:45:43.035806
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from test.parser_test import get_ast

    node = get_ast("""
    {1: 1}
    """)  # type: ast.Module

    transformer = DictUnpackingTransformer()
    transformer.visit(node)
    expected_node = get_ast("""
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    {1: 1}
    """)  # type: ast.Module
    assert node.body == expected_node.body



# Generated at 2022-06-14 01:45:52.232286
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.syntaxtree import parse

    src = '''
    {**dict_a, **dict_b, 'b': 20}
    '''
    expected = '''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    
    
    _py_backwards_merge_dicts([dict_a, dict_b, {'b': 20}])
    '''
    tree = parse(src)
    transformer = DictUnpackingTransformer()
    tree = transformer.visit(tree)
    code = compile(tree, '<test>', 'exec')
    ns = {}
    exec(code, ns)
    assert transformer._tree_changed
    assert code

# Generated at 2022-06-14 01:46:00.237269
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    o = DictUnpackingTransformer()
    normal = ast.parse("z = {'a': 3, 'b': 4, 'c': 5, 'd': 6}; z['c'] + z['d']")
    unpacking = ast.parse("z = {'a': 3, 'b': 4, **{'c': 5, 'd': 6}}; z['c'] + z['d']")

    normal = o.visit(normal)
    unpacking = o.visit(unpacking)

    assert ast.dump(normal) == ast.dump(unpacking)

# Generated at 2022-06-14 01:46:06.176018
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ast import parse, dump

    code = """
    {1: 1, **dict_a}
    """
    expected = """
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result


    _py_backwards_merge_dicts([{1: 1}], dict_a)
    """
    module = parse(code)
    result = DictUnpackingTransformer().visit(module)
    assert dump(result) == expected


# Generated at 2022-06-14 01:46:07.495768
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    pass


# Generated at 2022-06-14 01:46:13.847777
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    source = """
    def func():
        a = {1: 1, **{2: 2}}
    """
    expected = """
    def func():
        a = _py_backwards_merge_dicts([{1: 1}], {2: 2})
    """

    module = ast.parse(source)
    DictUnpackingTransformer().visit(module)  # type: ignore
    assert (expected == astunparse.unparse(module))

# Generated at 2022-06-14 01:46:21.081635
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.imports import import_name_following_call
    import astor
    ast_ = ast.parse("a = {1: 1, **dict_a}")
    DictUnpackingTransformer().visit(ast_)
    code = astor.to_source(ast_)
    code = import_name_following_call(code)
    print(code)

# Generated at 2022-06-14 01:46:27.511775
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..compile import compile_snippet

    assert compile_snippet('{**a, **b, **c}') == {'a': {},
                                                 'b': {},
                                                 'c': {}}



# Generated at 2022-06-14 01:46:32.808690
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astor
    from ..utils.misc import assert_roundtrip

    node = ast.Module(body=[
        ast.Expr(value=ast.Dict(keys=[None, None], values=[])),
    ])
    assert_roundtrip(DictUnpackingTransformer, node,
                     expected=merge_dicts.get_body() + ['_py_backwards_merge_dicts(dict(), dict())'])



# Generated at 2022-06-14 01:46:35.296607
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astor
    from .testing_utils import assert_source_equal


# Generated at 2022-06-14 01:46:41.869424
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import typed_astunparse
    import astunparse

# Generated at 2022-06-14 01:46:49.075181
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    expected = merge_dicts.get_body()
    actual = ast.parse('')
    actual = DictUnpackingTransformer().visit(actual)
    actual = ast.fix_missing_locations(actual)
    assert ast.dump(expected) == ast.dump(actual)



# Generated at 2022-06-14 01:46:55.587907
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    # type: () -> None
    code = '{1: 1, **d, 3: 3, **e, 4: 4, 5: 5}'
    tree = ast.parse(code)
    tree = DictUnpackingTransformer().visit(tree)
    assert code == tree_to_code(tree)



# Generated at 2022-06-14 01:47:08.099226
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..testing import TestCase, test_ast
    from ..testing import make_testcase, transform_testcase
    

# Generated at 2022-06-14 01:47:15.238949
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.testing import assert_transform

    assert_transform(DictUnpackingTransformer,
                     """
        {}
                     """,
                     """
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
        {}
                     """)



# Generated at 2022-06-14 01:47:20.641626
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.testing import get_ast, round_trip

    def func():
        {1: 1, **dict_a}

    node = get_ast(func)
    node = DictUnpackingTransformer().visit(node)
    source = round_trip(node)
    assert source == "def func():\n" \
                     "    _py_backwards_merge_dicts([{1: 1}], dict_a)"



# Generated at 2022-06-14 01:47:26.423852
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    input = '''\
{1: 1, 2: 2, 3: 3, **a}
'''

    expected = '''\
_py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], a)
'''

    from ..utils.parse_ast import parse_ast
    from .testing import transform_testing

    module = parse_ast(input)
    target = DictUnpackingTransformer()
    result = target.visit(module)
    assert transform_testing(result) == expected



# Generated at 2022-06-14 01:47:32.183439
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    """Tests cases for method visit_Module of class DictUnpackingTransformer"""
    def test(code):
        """Transforms code and tests it"""
        module = ast.parse(code)
        new_module = DictUnpackingTransformer().visit(module)
        assert isinstance(new_module, ast.Module)
        assert isinstance(new_module.body[0], ast.Expr)
        assert isinstance(new_module.body[0].value, ast.Str)
        assert new_module.body[0].value.s == '\n'.join(merge_dicts.get_body())

    test('''
        from typed_ast import ast3 as ast  # type: ignore

        def test():
            {1: 2, 3: 4}
    ''')


# Generated at 2022-06-14 01:47:38.139056
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astunparse

    t = DictUnpackingTransformer()
    result = t.visit(ast.parse("{'a': 1}"))


# Generated at 2022-06-14 01:47:48.329725
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .test_utils import compile_function
    from .utils import UnversionedPythonNodeTransformer
    from . import untested
    untested()

    test_func = compile_function(
        ['_py_backwards_merge_dicts'],
        '''# BEGIN TEST
            {1: 2}
        # END TEST''')[0]

    expected_func = compile_function(
        [],
        '''# BEGIN TEST
            def _py_backwards_merge_dicts(dicts):
                result = {}
                for dict_ in dicts:
                    result.update(dict_)
                return result
        # END TEST''' +
        '''# BEGIN TEST
            {1: 2}
        # END TEST''')[0]

    assert test_func == expected_func


# Generated at 2022-06-14 01:48:06.220355
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..typed_astunparse import unparse
    from .test_base import ast_test_case
    import textwrap
    import typing
    node = ast_test_case(textwrap.dedent('''\
        a = {0: 1, **i}
        '''))
    node = DictUnpackingTransformer().visit(node)
    assert node is not None
    res = unparse(node, include_encoding_declaration=False, sort_names=False)

# Generated at 2022-06-14 01:48:16.158971
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .unparse import unparse

    module = ast.parse('''
        def func():
            {1: 2, **a}
            {1: 2, **a, 3: 4, **b}
            {1: 2, **a, 3: 4, **b, 5: 6}
        ''')


# Generated at 2022-06-14 01:48:27.585470
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    SCRIPT = """
a = {'a': 1, 2: 3, **d}
    """

    transformer = DictUnpackingTransformer()
    module = ast.parse(SCRIPT)
    assert len(module.body) == 2
    assert isinstance(module.body[0], ast.Expr)
    assert isinstance(module.body[0].value, ast.Call)
    assert len(module.body[0].value.args) == 1
    assert isinstance(module.body[0].value.args[0], ast.Str)
    assert module.body[0].value.args[0].s == 'a = {\'a\': 1, 2: 3, **d}\n'
    new_module = transformer.visit(module)
    assert len(new_module.body) == 3

# Generated at 2022-06-14 01:48:30.847071
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    source = """        {1: 1, **dict_a}"""

# Generated at 2022-06-14 01:48:39.915035
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.testing import make_fixture, run_test
    from ..utils.env import Env
    from ..utils.tree import dump
    source = '''
            {1: 1, **dict_a}
            '''
    result = '''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    _py_backwards_merge_dicts([{1: 1}], dict_a)
    '''
    tree = make_fixture(source, result)
    expected_tree = make_fixture(source, result)

    class TransformerEnv(Env):
        pass


# Generated at 2022-06-14 01:48:47.106707
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    # TEST 1
    code = """
        def f():
            pass
    """
    expected = """
        def f():
            pass
    """
    transformer = DictUnpackingTransformer()
    tree = ast.parse(code)
    tree = transformer.visit(tree)
    tree = ast.fix_missing_locations(tree)
    assert expected == astor.to_source(tree)

    # TEST 2
    code = """
        def f():
            pass
        def f():
            pass
    """

# Generated at 2022-06-14 01:48:53.625759
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .transformations import DictUnpackingTransformer
    module_node = ast.parse("def func():\n    {1:1, **a}\n")
    transformed_module_node = DictUnpackingTransformer().visit(module_node)
    module_source = astor.to_source(transformed_module_node)
    assert (
        module_source ==
        'def func():\n    _py_backwards_merge_dicts((dict(1), a,))\n')



# Generated at 2022-06-14 01:49:00.852675
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..testing.utils import check_snapshot
    from ..testing.utils import get_ast_tree
    from ..testing.utils import tokenize_with_snippets

    source = '''
    {1: 1, **dict_a, **dict_b}
    '''.strip()
    tree = get_ast_tree(tokenize_with_snippets(source))
    tr = DictUnpackingTransformer()
    result = tr.visit(tree)
    check_snapshot(result, 'test_DictUnpackingTransformer_visit_Module')

# Generated at 2022-06-14 01:49:04.637620
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse(
        """
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11,
12: 12, 13: 13, 14: 14, **a}
"""
    )
    transformer = DictUnpackingTransformer()
    transformer.visit(module)
    target = ast.parse(
        """
_py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14}], a)
"""
    )
    assert module.body == target.body

# Generated at 2022-06-14 01:49:14.791391
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import typed_ast.ast3 as ast

    class Dummy(ast.NodeTransformer):
        def __init__(self):
            self.mutation_called = False

        def visit_Dict(self, node):
            self.mutation_called = True
            return node

    dummy = Dummy()
    merged = DictUnpackingTransformer()
    module = ast.parse('{1: 1, **a}')
    merged.visit(module)
    dummy.visit(module)

    assert merged.mutation_called == False
    assert dummy.mutation_called == True

    assert module.body[1].value.func.id == '_py_backwards_merge_dicts'

# Generated at 2022-06-14 01:49:34.525200
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:49:36.397761
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astor  # type: ignore


# Generated at 2022-06-14 01:49:37.413148
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer() is not None

# Generated at 2022-06-14 01:49:38.703894
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer((1, 2)) is not None

# Generated at 2022-06-14 01:49:51.086988
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import numpy as np
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Dict

    t = DictUnpackingTransformer()
    assert t.visit(ast.parse('{1: 1, 1: 1}')) == ast.parse('{1: 1, 1: 1}')  # type: ignore
    assert t.visit(ast.parse('{1: 1, None: {1: 1}}')) == ast.parse('_py_backwards_merge_dicts([{1: 1}], dict({1: 1}))')  # type: ignore

# Generated at 2022-06-14 01:49:52.729667
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer() is not None


# Generated at 2022-06-14 01:50:04.711747
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import pytest

    from .test_setup import format_code, parse_to_node

    expect = format_code(merge_dicts.get_body()) + format_code("""
_py_backwards_merge_dicts([{1: 1, 2: 2}], a)
    """)
    actual = format_code(DictUnpackingTransformer().visit(
        parse_to_node("""
{1: 1, 2: 2, **a}
        """)))
    assert expect == actual

    # with multiple None-value keys

# Generated at 2022-06-14 01:50:05.428887
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert isinstance(DictUnpackingTransformer, type)

# Generated at 2022-06-14 01:50:08.620556
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    assert [ast.parse(x).body[0] for x in merge_dicts.as_list()] == \
        DictUnpackingTransformer(None).visit_Module(ast.Module(body=[])).body



# Generated at 2022-06-14 01:50:11.497207
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    print("Testing constructor for class DictUnpackingTransformer")
    DictUnpackingTransformer()
    print("PASSED")


# Generated at 2022-06-14 01:50:52.806495
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '''
        {1: 1, 2: 2, **dict_a, 3: 3, **dict_b, 4: 4, **dict_c}
    '''
    result = '''
        _py_backwards_merge_dicts([{1: 1, 2: 2}, dict_a, {3: 3}, dict_b, {4: 4}], dict_c)
    '''
    node = ast.parse(code)
    expected = ast.parse(result, mode='eval')
    DictUnpackingTransformer().run(node)
    assert ast.dump(node, mode='eval') == ast.dump(expected, mode='eval')

# Generated at 2022-06-14 01:51:04.084828
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert '''
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    ''' == astor.to_source(
        DictUnpackingTransformer().visit(
            ast.parse('''
                {1: 1, **dict_a}
            ''')))

    assert '''
        _py_backwards_merge_dicts([{}, dict_a], dict_b)
    ''' == astor.to_source(
        DictUnpackingTransformer().visit(
            ast.parse('''
                {**dict_a, **dict_b}
            ''')))

    assert '''
        _py_backwards_merge_dicts([{1: 2, 3: 4}], dict_a)
    ''' == astor.to_

# Generated at 2022-06-14 01:51:14.174661
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    x = '''
{1: 1}
{**dict_a}
{1: 1, **dict_a}
{1: 1, 'a': 2, **dict_a}
{1: 1, 'a': 2, **dict_a, **dict_b}
{1: 1, 'a': 2, **dict_a, 'b': 3}
{**dict_a, **dict_b}
{**dict_a, **dict_b, **dict_c}
{**dict_a, **dict_b, 'c': 3}
    '''

# Generated at 2022-06-14 01:51:21.469221
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse('''\
            {'a': 'b', **{'c': 'd'}}
            ''')
    expected = ast.parse('''\
            _py_backwards_merge_dicts([{'a': 'b'}], {'c': 'd'})
            ''')
    transformer = DictUnpackingTransformer()
    result = transformer.visit(tree)
    assert ast.dump(result) == ast.dump(expected)
    assert transformer._tree_changed

# Generated at 2022-06-14 01:51:31.615891
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse('dict({1: 1, 2: 2}, **dict_a)')
    DictUnpackingTransformer().visit(module)
    assert ast.dump(module) == \
           "import ast3\n" \
           "\n" \
           "\n" \
           "# --- Snippet begins here ---\n" \
           "\n" \
           "def _py_backwards_merge_dicts(dicts):\n" \
           "    result = {}\n" \
           "    for dict_ in dicts:\n" \
           "        result.update(dict_)\n" \
           "    return result\n" \
           "\n" \
           "\n" \
           "# --- Snippet ends here ---\n" \
           "\n" \
           "\n"

# Generated at 2022-06-14 01:51:32.666847
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    return



# Generated at 2022-06-14 01:51:42.239822
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astor
    from ast import Module
    from .testutils import round_trip
    
    x = Module(body=[])
    
    rt = round_trip(x, DictUnpackingTransformer())
    
    # print(astor.to_source(rt))
    assert astor.to_source(rt) == 'from typing import Any\n\n\n_py_backwards_merge_dicts = (lambda dicts: (result := {}) and (result.update(*dicts) or result))\n'

# Generated at 2022-06-14 01:51:47.693816
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    t = DictUnpackingTransformer()
    tree = ast.parse('{1: 2, 3: 4}')
    t.visit(tree)
    assert '_py_backwards_merge_dicts' in ast.dump(tree)



# Generated at 2022-06-14 01:51:56.928818
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    imports = (
        "from __future__ import annotations\n"
        "from typing import List\n"
        "from mypy_extensions import TypedDict\n"
    )

    src = dedent(
        f"""\
        {imports}

        d: Dict = {{
            1: 2,
            3: 4,
            5: 6,
            **{{7: 8}}
        }}
        """
    )


# Generated at 2022-06-14 01:52:01.102163
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import typed_ast.ast3 as ast
    from . import transform


# Generated at 2022-06-14 01:53:19.128997
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import typed_ast.ast3 as ast
    from .base import BaseNodeTransformerTestCase

    class Test(BaseNodeTransformerTestCase):
        def create_transformer(self):
            return DictUnpackingTransformer()


# Generated at 2022-06-14 01:53:26.127249
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from ..utils.testing import assert_equal_code

    nodes = ast3.parse('{1: 1, **dict_a, 2: 2, **dict_b}')
    result = DictUnpackingTransformer().visit(nodes)

    expected = ast3.parse('_py_backwards_merge_dicts((dict({1: 1}), dict_a, dict({2: 2}), dict_b))')
    assert_equal_code(result, expected)

# Generated at 2022-06-14 01:53:37.618794
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    a = {1: 1, 2: 2}
    b = {3: 3, 4: 4}

    src = """{1: 1, None, **a, 2: 2, None, **b}"""
    expected = "_py_backwards_merge_dicts([" \
               "{1: 1, 2: 2}, a, {3: 3, 4: 4}])"

    mod = ast.parse(src)
    DictUnpackingTransformer().visit(mod)
    mod_ast = ast.fix_missing_locations(mod)
    mod_src = compile(mod_ast, '', 'exec')
    exec(mod_src)

    assert eval(expected) == eval(src)



# Generated at 2022-06-14 01:53:40.204970
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    instance = DictUnpackingTransformer()
    assert isinstance(instance, BaseNodeTransformer)

# Test case for method visit_Dict and constructor of class DictUnpackingTransformer

# Generated at 2022-06-14 01:53:50.528427
# Unit test for method visit_Module of class DictUnpackingTransformer