

# Generated at 2022-06-14 01:44:15.282715
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import Module, Call, Name, List
    from ..utils import get_ast

    code = "a = {'a': 1, **{'b': 2}}"
    mod = get_ast(code)
    assert isinstance(mod, Module)
    assert isinstance(mod.body[0].value, Call)
    assert isinstance(mod.body[0].value.func, Name)
    assert mod.body[0].value.func.id == '_py_backwards_merge_dicts'
    assert isinstance(mod.body[0].value.args[0], List)
    assert len(mod.body[0].value.args[0].elts) == 2



# Generated at 2022-06-14 01:44:24.863257
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    transformer = DictUnpackingTransformer()

    module = ast.Module(body=[
        ast.Dict(keys=[ast.Str(s='key_A'), ast.Str(s='key_b')],
                 values=[ast.List(elts=[]), ast.List(elts=[])])
    ])

    expected_module = ast.Module(body=[
        merge_dicts, 
        ast.Dict(keys=[ast.Str(s='key_A'), ast.Str(s='key_b')],
                 values=[ast.List(elts=[]), ast.List(elts=[])])
    ])

    actual_module = transformer.visit(module)

    assert ast.dump(actual_module) == ast.dump(expected_module)


# Generated at 2022-06-14 01:44:32.428279
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    kwargs = {'leaf': 'leaf', 'node': 'node'}
    expr = ast.parse("""
        {1: 1, **{**kwargs}, 2: 2}
    """).body[0].value

    module = ast.parse("""
        def test_func(a, **kwargs):
            return {1: 1, **{**kwargs}, 2: 2}
    """)
    expected = """
        def test_func(a, **kwargs):
            return _py_backwards_merge_dicts([{1: 1}, _py_backwards_merge_dicts([kwargs], )], {2: 2})
    """

    transformer = DictUnpackingTransformer()
    new_module = transformer.visit(module)
    assert transformer._tree_changed
    tree_changed_

# Generated at 2022-06-14 01:44:42.291296
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    splitted = [
        [('a', ast.Num(1))],
        ast.Name(id='b'),
        [('c', ast.Num(2))]]

    expected_tr_result = ast.Call(
        func=ast.Name(id='_py_backwards_merge_dicts'),
        args=[ast.List(elts=[
            ast.Dict(keys=['a'], values=[ast.Num(1)]),
            ast.Call(
                func=ast.Name(id='dict'),
                args=[ast.Name(id='b')],
                keywords=[]),
            ast.Dict(keys=['c'], values=[ast.Num(2)])])],
        keywords=[])

    tr = DictUnpackingTransformer()
    x

# Generated at 2022-06-14 01:44:53.827237
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transform = DictUnpackingTransformer()

    # case: no occurence of unpacking
    node = ast.parse("{1: 1}").body[0]
    assert transform.visit(node) == node

    # case: multiple unpacking
    node = ast.parse("{1: 1, **a, 2: 2, **b, 3: 3}").body[0]

# Generated at 2022-06-14 01:45:04.806978
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = """
    {1: 1, **a}
    {1: 1, **a, 2: 2}
    {1: 1, **a, **b, 2: 2}
    {1: 1, **a, **b, **c, 2: 2}
    """

# Generated at 2022-06-14 01:45:12.610953
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test import snippet_to_ast as sta
    from ..utils.test import ast_eq

    assert ast_eq(sta("{1: 2, 3: 4, **{5: 6, 7: 8}}"),
                  sta("""
    _py_backwards_merge_dicts([{1: 2, 3: 4}], {5: 6, 7: 8})
                  """)
                  )

# Generated at 2022-06-14 01:45:23.838347
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    node = ast.Dict(keys=[ast.Num(n=1), ast.Num(n=2), None, ast.Num(n=4)],
                    values=[ast.Num(n=1), ast.Num(n=2), ast.Dict(keys=[],
                                                                values=[]),
                            ast.Num(n=4)])
    t = DictUnpackingTransformer()
    x = t.visit(node)

# Generated at 2022-06-14 01:45:33.679194
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    def change_tree(code: str, assert_code: str, *, mode: int) -> None:
        """Tests transformer for given code."""
        tr = transformer.compile.visit(ast.parse(code, mode=mode))
        assert transformer._tree_changed
        assert transformer.compile.visit(tr) == assert_code

    code = """x = {1: 2, **a, 3: 4}"""
    assert_code = """x = _py_backwards_merge_dicts([{1: 2}, {3: 4}], a)"""
    change_tree(code, assert_code, mode='exec')
    change_tree(code, assert_code, mode='eval')


# Generated at 2022-06-14 01:45:43.356770
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = '''
    def func():
        return {"a":1}
    '''
    expected_code = '''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    def func():
        return {"a":1}
    '''
    result = DictUnpackingTransformer().visit_Module(ast.parse(code))
    result_code = ast.unparse(result)
    print(result_code)
    assert result_code == expected_code


# Generated at 2022-06-14 01:46:00.253336
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..node import print_node
    from textwrap import dedent
    sample = dedent("""\
        {a: 1, **b, c: 2, **d}
    """)
    tree = ast.parse(sample)
    expected = dedent("""\
        _py_backwards_merge_dicts([{'a': 1}, {'c': 2}], b, d)
    """)

    transformer = DictUnpackingTransformer()
    new_tree = transformer.visit(tree)
    assert print_node(new_tree) == expected

# Generated at 2022-06-14 01:46:05.625027
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import ast as _ast
    tree = _ast.parse(
        '{1: 1, **dict_a}',
        mode='eval')
    t = DictUnpackingTransformer()
    
    t._tree = tree
    tree = t.visit(tree)
    
    print(ast.dump(tree))

# Generated at 2022-06-14 01:46:13.740499
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .unpacking import UnpackingTransformer, DictUnpackingTransformer, Symbols
    from ..utils.tree import print_ast

    # Create a sample of a source file and compile it to AST
    source = '''
        {
            1: 1,
            **x,
            2: 2,
            **y
        }
    '''
    tree = ast.parse(source)

    # Prepare symbols and names to be available from the scope of the transformer
    symbols = Symbols()
    symbols.add_name('x', ast.Name(id='x'))
    symbols.add_name('y', ast.Name(id='y'))

    # Apply visit_Dict to the tree
    result = DictUnpackingTransformer(symbols=symbols).visit(tree)
    print_ast(result)

   

# Generated at 2022-06-14 01:46:18.734814
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..testing.utils import check_node_transformation
    check_node_transformation(
        """{a: b, **c, **d, None: None, e: f}""",
        """_py_backwards_merge_dicts([{a: b}, {e: f}], c, d)""",
        DictUnpackingTransformer)

# Generated at 2022-06-14 01:46:22.628503
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    m = ast.parse('{1: 1, **a, 2: 2, **b}')
    transformer = DictUnpackingTransformer()
    result = transformer.visit(m)
    expected = ast.parse('_py_backwards_merge_dicts([{1: 1, 2: 2}], a, b)')
    assert ast.dump(result) == ast.dump(expected)

# Generated at 2022-06-14 01:46:32.885760
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class DictUnpackingTransformer_visit_Dict(DictUnpackingTransformer):
        def _split_by_None(self, pairs):
            return super()._split_by_None(pairs)
        def _prepare_splitted(self, splitted):
            return super()._prepare_splitted(splitted)
        def _merge_dicts(self, xs):
            return super()._merge_dicts(xs)

    dict_a = ast.Dict(keys=[ast.Constant(value=3), ast.Constant(value=4)],
                      values=[ast.Constant(value=5), ast.Constant(value=6)])

# Generated at 2022-06-14 01:46:45.599329
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .bf import BlockingFuture
    from .importer import Importer
    from .py import PythonSource

    source = """
    {1: 2, **a, 2: 3, **b, 3: 4, **c}
    """
    node = ast.parse(source)
    module = Importer.Import(source, PythonSource()).create_module()
    BlockingFuture.wait_for_all_futures()
    transformer = DictUnpackingTransformer()
    result = transformer.visit(node)
    expected_result = """
    _py_backwards_merge_dicts([{1: 2, 2: 3, 3: 4}], a, b, c)
    """
    assert ast.dump(result) == ast.dump(ast.parse(expected_result))

# Generated at 2022-06-14 01:46:54.730692
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.py33_test_visitor import Py33TestTransformer
    from ..utils.source_code import SourceCode

    code = SourceCode.from_string("""
        _py_x = {1: 2, **{3: 4, **_py_y}, 5: 6, **{7: 8}}
    """)

    Py33TestTransformer(DictUnpackingTransformer, code).test()

    assert code.source == """
        _py_x = _py_backwards_merge_dicts([{1: 2}, {5: 6}],
        _py_backwards_merge_dicts([{3: 4}], _py_y), {7: 8})
    """

# Generated at 2022-06-14 01:47:05.808861
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse
    import astunparse

    source = '''
Foo(1, 2, {3: 4, **a, 5: 6, 7: 8})
2
    '''
    expected_output = '''
Foo(1, 2, _py_backwards_merge_dicts([{3: 4, 5: 6, 7: 8}], a))
2
    '''
    output = DictUnpackingTransformer().visit(parse(source))
    print(astunparse.unparse(output))
    assert astunparse.unparse(output).strip() == expected_output.strip()

# Generated at 2022-06-14 01:47:16.445586
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = """
        {1: 2, 3: 4, **{3: 5, **{6: 7, **{8: 9}}}}
        {1: 2, **{3: 4, **{5: 6, **{7: 8}}}, 5: 6}
        {1, 2, 3}
    """
    expected = """
        _py_backwards_merge_dicts(
            [dict({1: 2, 3: 4}), {3: 5}, {6: 7}, {8: 9}])
        _py_backwards_merge_dicts(
            [dict({1: 2}), {3: 4}, {5: 6}, {7: 8}], {5: 6})
        {1, 2, 3}
    """
    result = DictUnpackingTransformer(code).result

# Generated at 2022-06-14 01:47:35.041683
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import transform

    assert transform(
        DictUnpackingTransformer,
        '{1: 1}') == '{\n    1: 1\n}'

    assert transform(
        DictUnpackingTransformer,
        '{1: 1, 2: 2, **{3: 3}}') == (
            '_py_backwards_merge_dicts([{\n'
            '        1: 1,\n'
            '        2: 2\n'
            '    }], {3: 3})')


# Generated at 2022-06-14 01:47:43.426575
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import parse
    from .base import BaseNodeTransformerTests
    from .base import ModuleParseTestCase

    class TestDictUnpackingTransformer(ModuleParseTestCase,
                                        BaseNodeTransformerTests):
        transformer = DictUnpackingTransformer
        target_version = (3, 4)

        def test_DictUnpackingTransformer_visit_Dict_001(self):
            code = "{1: 1, **a}"
            expected_code = "_py_backwards_merge_dicts([{1: 1}], a)"
            tree = parse(code)
            transformer = self.transformer(self.target_version)
            new_tree = transformer.visit(tree)
            transformed_code = compile(new_tree, '<string>', 'exec')
            namespace = {}


# Generated at 2022-06-14 01:47:51.382663
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse

    test_cases = [
        "{'a': 1, **b, 'c': 2}",
        "{**a}",
        "{**a, **b}",
        "{'a': 1, **b, **c}",
        "{a: 1, **b, c: 2}",
    ]


# Generated at 2022-06-14 01:47:54.904767
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.fixtures import make_example_python_code_tree
    import astor

    tree = make_example_python_code_tree()
    DictUnpackingTransformer().visit(tree)
    print(astor.to_source(tree))

# Generated at 2022-06-14 01:48:01.508735
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent

    correct_source = dedent("""
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    def func():
        _py_backwards_merge_dicts([{1: 2, 3: 4}, {5: 6, 7: 8}])
    """)

    node = ast.parse("""
    def func():
        {1: 2, 3: 4, None: {5: 6, 7: 8}}
    """)

    result = DictUnpackingTransformer().visit(node)  # type: ignore

    assert ast.dump(result) == ast.dump(ast.parse(correct_source))


# Generated at 2022-06-14 01:48:02.609935
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor

# Generated at 2022-06-14 01:48:06.563251
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert ast.parse("{1: 1, None: {2: 3, 4: 5}}").body[0].value == \
        DictUnpackingTransformer().visit(
            ast.parse("{1: 1, None: {2: 3, 4: 5}}"))

# Generated at 2022-06-14 01:48:13.098505
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    expected = ast.parse("""
x = _py_backwards_merge_dicts(
    [dict({'a': 1}), dict({'b': 2})],
    **dict_var)
    """)

    code = """
x = {
    **dict_var,
    'a': 1,
    'b': 2,
}
    """
    transformer = DictUnpackingTransformer()
    res = transformer.visit(ast.parse(code))
    assert res == expected

# Generated at 2022-06-14 01:48:22.839282
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..toolchain import run_transforms
    from .stub_toolchain import StubToolchain
    from .stub_manager import StubModule

    toolchain = StubToolchain()
    result = run_transforms(toolchain, DictUnpackingTransformer,
                            StubModule('''
                            {1: 1, **{}, **{'a': 4}}
                            '''))
    expected = '''\
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    _py_backwards_merge_dicts([dict({1: 1}), {}, {'a': 4}])
    '''

    assert result == expected

# Generated at 2022-06-14 01:48:30.812610
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """
    Compiles:
        {1: 1, **dict_a}
        
    To:
        _py_backwards_merge_dicts([{1: 1}], dict_a})
    """
    DictUnpackingTransformer().visit(ast.parse("{1: 1, **dict_a}")) == ast.parse("""
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
            
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """)

# Generated at 2022-06-14 01:48:42.990000
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    transformer = DictUnpackingTransformer()
    assert transformer.visit(ast.parse('''
        {
            'a': 1, 
            **dict_a,
            2: 'b',
        }
    ''')) == ast.parse('''
        _py_backwards_merge_dicts([
            ({'a': 1},)
        ], dict_a, {2: 'b'})
    ''')

# Generated at 2022-06-14 01:48:52.898048
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    import typing
    node = ast.Dict(keys=[None, ast.Num(n=1), None, ast.Num(n=2)],
                    values=[ast.Num(n=0), ast.Num(n=1), ast.Num(n=2), ast.Num(n=3)])

# Generated at 2022-06-14 01:48:58.334686
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ast import parse, Dict
    from astunparse import dump
    from ..utils.example import example

    node = parse(example('test_DictUnpackingTransformer_visit_Dict.py'))
    DictUnpackingTransformer().transform(node)
    assert dump(node) == example('test_DictUnpackingTransformer_visit_Dict.py')

# Generated at 2022-06-14 01:49:06.187447
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    
    input_code = """{'1': 1, '2': 2, **d}"""
    expected_output_code = """_py_backwards_merge_dicts([{'1': 1, '2': 2}], d)"""

    actual_output_code = DictUnpackingTransformer().visit(input_code)
    assert expected_output_code == actual_output_code
    
    input_code = """{'1': 1, **{'2': 2}, **d}"""
    expected_output_code = """_py_backwards_merge_dicts([{'1': 1}, {'2': 2}], d)"""

    actual_output_code = DictUnpackingTransformer().visit(input_code)
    assert expected_output_code == actual_output_code
    
    input

# Generated at 2022-06-14 01:49:10.512603
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    test_code = '{1: 1, 2: 5, **{3: 6}, **{4: 4}, 5: 5, **{6: 6}}'

# Generated at 2022-06-14 01:49:11.543719
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .. import Transpiler

# Generated at 2022-06-14 01:49:18.299723
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test_utils import (
        assert_equal_ast,
        assert_equal_code,
        get_ast,
    )

    node = get_ast("""
        {1: 1, **dict_a}
        """)

    expected = get_ast("""
        _py_backwards_merge_dicts([{1: 1}], dict_a)
        """)

    assert_equal_ast(expected, DictUnpackingTransformer().visit(node))

# Generated at 2022-06-14 01:49:25.783324
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_astunparse import unparse

    code = """
    {x: y, z: z, **dsd}
    """
    tree = ast.parse(code)
    transformer = DictUnpackingTransformer()
    node = transformer.visit(tree)
    code_after = unparse(node)
    lines = code_after.splitlines()
    assert lines == [
        '_py_backwards_merge_dicts([{x: y, z: z}], dsd)'
    ]



# Generated at 2022-06-14 01:49:37.746531
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    source = """
x = {1: 2, 3: 4, **a, 5: 6}
    """
    tree = ast.parse(source)
    transformer.visit(tree)
    assert transformer._tree_changed

# Generated at 2022-06-14 01:49:50.010925
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    ctx = {
        '_py_backwards_merge_dicts': _py_backwards_merge_dicts
    }


# Generated at 2022-06-14 01:50:08.756347
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3, parse
    import astunparse
    # Given:
    before = """
{'a': 1, **dict_a, 'b': 2, **dict_b}
"""
    code = parse(before)
    assert isinstance(code, ast3.Module)
    # When
    DictUnpackingTransformer().visit(code)
    # Then:
    after = astunparse.unparse(code)
    expected = """
_py_backwards_merge_dicts([{'a': 1}, dict_a, {'b': 2}], dict_b)
"""
    assert after == expected

# Generated at 2022-06-14 01:50:19.852602
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typing import cast
    from . import compile
    from .base import BaseNodeTransformer
    from .utils import (
        UnexpectedASTNode,
        compare_with_expected,
        replace_name_in_mappings,
    )

    class DictUnpacker(BaseNodeTransformer):
        target = (3, 4)

        def visit_Dict(self, node):
            # type: (ast.Dict) -> ast.Dict
            return node

    # test merging dicts
    #{%
    #    {}
    #    {1: 1}
    #    {1: 1}
    #    {1: 1}
    #    {1: 1}
    #%}
    #{%
    #    {1: 1, **a}
    #    {1: 1, **a}

# Generated at 2022-06-14 01:50:28.160314
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.Dict(
        keys=[ast.Num(n=n) for n in range(3)],
        values=[ast.Tuple(elts=[ast.Num(n=n)], ctx=ast.Load()) for n in range(3)])

    transformer = DictUnpackingTransformer()
    result = transformer.visit(node)  # type: ignore
    assert isinstance(result, ast.Call)

# Generated at 2022-06-14 01:50:35.795112
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # given
    before = ast.parse(textwrap.dedent("""
        {
            1: 1,
            **{2: 2},
            3: 3,
            **{4: 4},
            **{
                5: 5
            },
            **{6: 6},
        }
    """)).body[0]

    transform = DictUnpackingTransformer()

    # when
    after = transform.visit(before)

    # then
    assert ast.dump(before) == ast.dump(after)

# Generated at 2022-06-14 01:50:47.600723
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..rendering import to_source as ts

    node = ast.parse("""
        my_dict = {'a': 1, 'b': 2, **dict_a}
    """)

    transformer = DictUnpackingTransformer()
    new_node = transformer.visit(node)
    output = ts(new_node)
    assert output == """
        from typed_ast import ast3 as ast

        _py_backwards_merge_dicts = lambda dicts: dict(d1, **d2) for d1 in dicts[:-1] for d2 in dicts[-1:-len(dicts):-1]

        my_dict = _py_backwards_merge_dicts([{'a': 1, 'b': 2}], dict_a)
    """.lstrip()

# Generated at 2022-06-14 01:50:57.071733
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import node_factory

    dict_ = node_factory.Dict([
        node_factory.Str('a'), node_factory.Num(1), None, node_factory.Dict([
            node_factory.Str('c'), node_factory.Num(2),
        ]),
        None, node_factory.Call(func=node_factory.Name('d')),
        node_factory.Str('b'), node_factory.Num(3),
    ])


# Generated at 2022-06-14 01:51:07.815540
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ...lib.typeshed.stdlib_partial.typing import \
        Dict as DictT, NewType, Generic, TypeVar

    Code = NewType('Code', str)
    A = TypeVar('A')
    B = TypeVar('B')
    C = TypeVar('C')

    class SomeClass(Generic[A, B]):
        def __init__(self, x: A, y: B) -> None:
            pass


# Generated at 2022-06-14 01:51:19.937298
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class CustomNodeTransformer(ast.NodeTransformer):
        def visit_List(self, node: ast.List) -> ast.List:
            return ast.List(elts=[ast.Num(n=1) for _ in range(len(node.elts))])

    source = """
        def f():
            x = {None: [i for i in range(10)], 'a': 1}
    """
    expected = """
        def f():
            x = _py_backwards_merge_dicts([{'a': 1}], {None: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})
    """
    tree = ast.parse(source)
    tree = CustomNodeTransformer().visit(tree)

# Generated at 2022-06-14 01:51:30.674655
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    def original():
        return {1: 1, 2: 3, 4: 5, **{'a': 1}, **None, **{'b': 2}}

    expected = (
        'def original():\n'
        '    return _py_backwards_merge_dicts([{1: 1, 2: 3, 4: 5}, {\'a\': 1}, {\'b\': 2}])\n')

    node = ast.parse(original.__code__).body[0]
    node_transformed = DictUnpackingTransformer().visit(node)
    assert astor.to_source(node_transformed) == expected

    import_path = 'dicts_unpacking.py'
    from .test_codegen import CodegenTest

# Generated at 2022-06-14 01:51:35.852733
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ast as st

    def check(before: st.AST, expected: st.AST) -> None:
        node = st.parse(source=before)
        node = DictUnpackingTransformer.run(node)
        node = st.dump(node)
        expected = st.dump(st.parse(source=expected))
        assert node == expected



# Generated at 2022-06-14 01:52:06.926446
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typing
    import ast
    import typed_ast.ast3 as typed_ast

    if typing.TYPE_CHECKING:
        from typing import get_type_hints
    value = ast.parse(
        'a = {'
        '    "a": 1, '
        '    2: 5, '
        '    **{'
        '        "b": 2, '
        '        3: 4'
        '    }, '
        '    "c": 3,'
        '    **{'
        '        4: 5'
        '    }'
        '}')
    value.body[0].value.keys  # type: ignore
    value.body[0].value.values  # type: ignore

    result = DictUnpackingTransformer().visit(value)

# Generated at 2022-06-14 01:52:18.037075
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    with transform(DictUnpackingTransformer) as tx:
        tree = tx.parse_tree('''
            def test(**kwargs) -> None:
                x = {1: 2, **kwargs}

            def test_not_updated(**kwargs) -> None:
                x = {1: 2, a: 's', **kwargs}
                y = {**kwargs}
        ''')
    assert tx.changed

    # check if tree was updated

# Generated at 2022-06-14 01:52:23.903936
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    node = ast.parse('{1: 1, 2: 2, **dict_a, 3: 3, **dict_b}')
    result = transformer.visit(node)
    expected = ast.parse(
        '_py_backwards_merge_dicts([{1: 1, 2: 2}, dict_a, {3: 3}], dict_b)')
    assert ast.dump(result, include_attributes=False) == ast.dump(expected, include_attributes=False)

# Generated at 2022-06-14 01:52:39.775374
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_nodes_equal
    from ..utils.testing import make_test_case


# Generated at 2022-06-14 01:52:53.566978
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Tests that visit_Dict works correctly."""
    # Test case 1
    # Input
    node = ast.Dict(
        keys=[None, None, ast.Str(s='key1')],
        values=[ast.Name(id='dict1'), ast.Name(id='dict2'), ast.Num(n=1)]
    )
    # Expected output

# Generated at 2022-06-14 01:52:58.686558
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    a = ast.parse('{1: 2, **a, 2: 3}')
    b = ast.parse('_py_backwards_merge_dicts([{1: 2}, 2: 3], a)')
    DictUnpackingTransformer().visit(a)
    assert ast.dump(a) == ast.dump(b)

# Generated at 2022-06-14 01:53:10.590661
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import Dict
    from ..codegen import to_source
    from .base import to_source as to_source_bytes

    expected = "{**{'a': 1}, **{'b': 2}, **{'c': 3}}"
    code = "{**{'a': 1, **{'b': 2}, 'c': 3}}"
    result = to_source(DictUnpackingTransformer().visit(ast.parse(code)))
    assert expected == result

    expected = b"_py_backwards_merge_dicts([{'a': 1, 'c': 3}], {})"
    result = to_source_bytes(DictUnpackingTransformer().visit(ast.parse(code)))
    assert expected == result


# Generated at 2022-06-14 01:53:17.248617
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse("{1: 2, **{3: 4, 5: 6}, 7: 8, **{9: 10}}")
    expected = "result = _py_backwards_merge_dicts([{1: 2}, {3: 4, 5: 6}, " \
               "{7: 8}], {9: 10})"
    actual = DictUnpackingTransformer().visit(node)
    assert ast.dump(actual) == expected  # type: ignore

# Generated at 2022-06-14 01:53:21.370765
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    input = ast.parse('{1: 1, 2: 2, **dict_a}')

    expected = ast.parse('_py_backwards_merge_dicts(['
                         'dict(1=1, 2=2), dict_a])')

    transformer = DictUnpackingTransformer()
    assert expected == transformer.visit(input)



# Generated at 2022-06-14 01:53:30.391180
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.tester import AssertAstUntransformed, AssertAstTransformed
    AssertAstUntransformed(
        unittest_path=__file__,
        transform=DictUnpackingTransformer,
        source={1: 2},
        expected={1: 2})

    AssertAstTransformed(
        transformer=DictUnpackingTransformer,
        source={1: 2, **{}},
        expected={"_py_backwards_merge_dicts": "_py_backwards_merge_dicts",
                  "{1: 2}": {1: 2}})
