

# Generated at 2022-06-14 01:44:16.950240
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_ast.ast3 as ast
    import astor
    transformer = DictUnpackingTransformer()
    node = ast.Dict(
        keys=[ast.Num(n=1), None, ast.Num(n=2)],
        values=[ast.Num(n=1), ast.Dict(keys=[], values=[]), ast.Num(n=2)])
    new_node = transformer.visit_Dict(node)
    assert isinstance(new_node, ast.Call)

# Generated at 2022-06-14 01:44:21.577116
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    ast_module = ast.parse("{1: 1, **dict_a}")
    transformer.visit(ast_module)
    assert astor.to_source(ast_module) == (
        "_py_backwards_merge_dicts([{1: 1}], dict_a)")

# Generated at 2022-06-14 01:44:30.947307
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    
    def _test(x: dict, expected: dict):
        node = ast.parse(f'{{{", ".join(f"{k}: {v}" for k, v in x.items())}}}')  # type: ignore
        res = DictUnpackingTransformer().visit(node)  # type: ignore
        print(res)
        assert isinstance(res, ast.Module)
        ast.fix_missing_locations(res)
        res = compile(res, '', 'single')
        res = res.__dict__['co_consts'][0]
        assert res == expected
    
    _test({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3})

# Generated at 2022-06-14 01:44:37.280885
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Given
    t = DictUnpackingTransformer()
    sample = """
        d = {1: 2, **a, 3: 4, 5: **b, 6: 7}"""
    expected = """_py_backwards_merge_dicts([{1: 2, 3: 4}, a, {5: dict()}, b, {6: 7}])"""

    # When
    actual = t.visit(ast.parse(sample))

    # Then
    assert expected in ast.dump(actual)

# Generated at 2022-06-14 01:44:45.167260
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '''
        x = {a: 42, 42: b, **c}
        '''
    tree = parse(source)
    DictUnpackingTransformer().visit(tree)
    result = dump(tree)
    assert result == '''
        _py_backwards_merge_dicts([{a: 42, 42: b}], c)
        x = None
        '''



# Generated at 2022-06-14 01:44:54.351842
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from ..utils.parse import parse, to_source
    from ..utils.unparse import Unparser

    unparser = Unparser()
    ast_tree = parse(dedent("""\
        {1: 1, 2: 2, **a}
    """))
    result = DictUnpackingTransformer().visit(ast_tree.body[0])

    # We don't have complete implementation of py34 AST node dump
    # so we just compare strings
    expected = dedent("""\
        _py_backwards_merge_dicts([{1: 1, 2: 2}], a)
    """)
    actual = to_source(result).strip()
    assert expected == actual

# Generated at 2022-06-14 01:44:58.637516
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    module = ast.parse("{1: 1, 2: 2, 3: 3, **foo}")
    DictUnpackingTransformer().visit(module)
    assert ast.dump(module) == "from __future__ import annotations; " \
        "___1 = {1: 1, 2: 2, 3: 3}; _py_backwards_merge_dicts([___1], foo)"



# Generated at 2022-06-14 01:45:05.876522
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Given
    node = ast.parse('{1: 1, **{2: 2}, 3: 3, **{4: 4}}')

    # When
    transformer = DictUnpackingTransformer()
    new_node = transformer.visit(node)

    # Then

# Generated at 2022-06-14 01:45:14.130872
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_code_equal

    code = """
a=1
b=2
c=3
d={a: 1, None: d, b: 2, c: 3}
"""
    expected = """
a=1
b=2
c=3
d=_py_backwards_merge_dicts([{a: 1, b: 2, c: 3}], d)
"""
    assert_code_equal(expected, DictUnpackingTransformer().visit_str(code))

# Generated at 2022-06-14 01:45:21.179996
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    # Note: Dictionary unpacking is a new Python feature, declared in PEP 448
    tree = ast.parse('''
    x = {1:1, **a}
    ''')
    transformer.visit(tree)
    expected = ast.parse('''
    _py_backwards_merge_dicts([{1: 1}], a)
    ''')
    assert compare_ast(tree, expected)


# Generated at 2022-06-14 01:45:36.661079
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Assert that unpacking works in many places
    assert ast.dump(
        DictUnpackingTransformer().visit(
            ast.parse('print({1: 1, **{2: 2}, 3: 4, **{5: 6}})'))) \
        == ast.dump(
            ast.parse('''
            print(_py_backwards_merge_dicts([{1: 1, 3: 4}],
                                            {2: 2}, {5: 6}))'''))

    # Assert that empty dicts are ignored
    assert ast.dump(
        DictUnpackingTransformer().visit(
            ast.parse('print({1: 1, **{}})'))) \
        == ast.dump(
            ast.parse('''
                print({1: 1})'''))

# Generated at 2022-06-14 01:45:39.705369
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import parse
    parse("""{x: "one", y: "two", **{"one": 1}}""")



# Generated at 2022-06-14 01:45:46.098447
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:46:00.762648
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typing import Any, Dict, List
    from ..typed_astunparse import unparse
    from typed_ast import ast3 as ast

    @snippet
    def test_dict_literals(a: int, b: int, c: int, d: int, e: int) -> None:
        {
            1: a,
            **{
                2: b,
                4: c,
               **{
                    3: d,
                    5: e
                }
            }
        }

    tree = ast.parse(inspect.getsource(test_dict_literals))
    tr = DictUnpackingTransformer()
    tr.visit(tree)

# Generated at 2022-06-14 01:46:10.467359
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import load_ast_tree

    code = r"""
    {1: 2, **a, 3: 4, **b, 5: 6, **c}
    """
    new_code = r"""
    _py_backwards_merge_dicts([{1: 2, 3: 4, 5: 6}], a, b, c)
    """

    tree = load_ast_tree(code)
    new_tree = DictUnpackingTransformer().visit(tree)
    assert load_ast_tree(new_code) == new_tree

# Generated at 2022-06-14 01:46:20.179859
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ast3 as ast

# Generated at 2022-06-14 01:46:24.896461
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert transform(
        """
        {'a': 1, **d, **e}
        """,
        DictUnpackingTransformer) == """
        _py_backwards_merge_dicts([{'a': 1}], d, e)
        """



# Generated at 2022-06-14 01:46:33.837916
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .utils import parse
    from .utils import dump
    from .utils import compare_ast

    module = '''"dict with dict unpacking"; {1: 1, **dict_a, 2: 2, **dict_b}'''
    expected_module = '''"dict with dict unpacking"; _py_backwards_merge_dicts([{1: 1}, dict_a, {2: 2}], dict_b})'''

    ast_node = parse(module)
    expected_ast = parse(expected_module)
    new_ast = DictUnpackingTransformer().visit(ast_node)

    assert compare_ast(expected_ast, new_ast)
    assert dump(expected_ast) == dump(new_ast)


# Generated at 2022-06-14 01:46:48.417123
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typing import Dict
    from typed_ast import ast3 as ast

    transformer = DictUnpackingTransformer()
    input_dict = ast.Dict(
        keys=[ast.Num(n=1), ast.Num(n=2), None, ast.Num(n=3)],
        values=[ast.Num(n=1), ast.Num(n=2), ast.Dict(keys=[ast.Num(n=1)],
                                                     values=[ast.Num(n=2)]),
                ast.Num(n=3)])
    result = transformer.visit(input_dict)  # type: ignore

# Generated at 2022-06-14 01:46:56.613144
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import parse
    from .ast_compat import ast_to_source
    program_before_transform = '''
    {
        1: 1,
        'a': 'a',
        **{
            'c': 'c',
            **{
                'd': 'd',
            },
        },
        2: 2
    }
    '''

    node = parse(program_before_transform)
    result = DictUnpackingTransformer().visit(node)
    program_after_transform = ast_to_source(result)


# Generated at 2022-06-14 01:47:11.625263
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse('D = {1:1, **D}')
    expected = ast.parse('D = _py_backwards_merge_dicts([{1: 1}], D)')
    actual = DictUnpackingTransformer().visit(node)
    assert ast.dump(expected) == ast.dump(actual)

# Generated at 2022-06-14 01:47:20.526121
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import as_source
    from .expr_factory import expr_factory
    from ..utils.dump import dump_ast
    from astunparse import unparse
    from ..utils.test import expect
    import astor
    import typing
    def _test_DictUnpackingTransformer_visit_Dict(
            target: ast.Dict,
            expected: typing.Optional[ast.AST] = None,
            *,
            messages: typing.List[typing.Any] = None,
            **module_kwargs):
        result = DictUnpackingTransformer(**module_kwargs).visit(target)

# Generated at 2022-06-14 01:47:28.124720
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_astunparse import unparse
    from cst.to_typed_ast import to_typed_ast
    import astunparse
    source = """
    {1: 1, **dict_a}
    """
    tree = to_typed_ast(ast.parse(source))
    node = tree.body[0].value
    assert isinstance(node, ast.Dict)

    result = DictUnpackingTransformer().visit(node)
    assert unparse(result) == '_py_backwards_merge_dicts([{1: 1}], dict_a)'

    tree = to_typed_ast(ast.parse(source))
    node = tree.body[0].value
    assert isinstance(node, ast.Dict)


# Generated at 2022-06-14 01:47:28.720698
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    pass

# Generated at 2022-06-14 01:47:38.099716
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # pylint: disable=too-many-locals
    from ..utils.testing import transformation_test
    from ..utils import msg
    from . import ast_compare

    class DictUnpackingTransformerTest(transformation_test.TransformTestCase):
        transformer = DictUnpackingTransformer()
        filename = 'file.py'
        

# Generated at 2022-06-14 01:47:40.990421
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test_visitor import _test_visit_Dict
    _test_visit_Dict(DictUnpackingTransformer)

# Generated at 2022-06-14 01:47:49.800612
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    class TestTransformer(BaseNodeTransformer):

        def __init__(self, transformer: DictUnpackingTransformer):
            self.transformer = transformer

        def visit_Dict(self, node: ast.Dict) -> ast.Dict:
            return self.transformer.visit_Dict(node)  # type: ignore

    tt = TestTransformer(DictUnpackingTransformer())
    assert tt.visit(parse_expr('{1: 2}')) == parse_expr('{1: 2}')
    assert tt.visit(parse_expr('{1: 2, **{}}')) == parse_expr(
        '_py_backwards_merge_dicts([{1: 2}], {})')

# Generated at 2022-06-14 01:47:51.027686
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_utils.test_unpacking_transformer import test_transformer
    return test_transformer(DictUnpackingTransformer)

# Generated at 2022-06-14 01:47:59.628509
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.ast_builder import AstBuilder
    ab = AstBuilder()

# Generated at 2022-06-14 01:48:10.291860
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tr = DictUnpackingTransformer()

    node = ast.Dict(keys=[None, ast.Name(id='a'), None], values=[
        ast.Dict(keys=[ast.Str(s='1'), ast.Str(s='2')],
                 values=[ast.Num(n=1), ast.Num(n=2)]),
        ast.Name(id='d'),
        ast.Dict(keys=[ast.Str(s='3')], values=[ast.Num(n=3)])
    ])

# Generated at 2022-06-14 01:48:35.750845
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse
    from .tests.utils import round_trip

    code = '''
    {1: 3, 2: 4, **dict1, 3: 5, **dict2}
    '''

    expected = '''
    _py_backwards_merge_dicts([{1: 3, 2: 4}, dict1, {3: 5}, dict2])
    '''

    tree = parse(code)
    tree = DictUnpackingTransformer().visit(tree)
    assert round_trip(tree) == expected

# Generated at 2022-06-14 01:48:36.297874
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert True

# Generated at 2022-06-14 01:48:44.887990
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Unit test for DictUnpackingTransformer.visit_Dict."""
    from astor.code_gen import to_source
    from ..transformers.dict_unpacking import DictUnpackingTransformer
    x = ast.parse("{'a': 0, **a, 'b': 1, **b, 'c': 2, **c}")
    x = DictUnpackingTransformer().visit(x)
    expected_result = '_py_backwards_merge_dicts([{\'a\': 0, \'b\': 1, \'c\': 2}], a, b, c)'
    assert to_source(x) == expected_result

# Generated at 2022-06-14 01:48:50.326316
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '''
    {None: 1, 1: 2, None: 2, None: None, None: {}}
    '''
    tree = ast.parse(code)  # type: ignore
    DictUnpackingTransformer().visit(tree)
    # TODO: Should be restored
    # assert code_equal(tree, """
    # _py_backwards_merge_dicts([{}, {}, {}, {}])
    # """)

# Generated at 2022-06-14 01:49:00.877256
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import test

    @test.case
    def simple_nested_dict():
        code = '''{1: 1, 2: 2, **{"a": "foo", **{3: 3, 4: 4}}}'''
        expected = '''_py_backwards_merge_dicts([{1: 1, 2: 2}, {"a": "foo"}, {3: 3, 4: 4}])'''
        test.assert_equals(expected, code, DictUnpackingTransformer)

    @test.case
    def empty_nested_dict():
        code = '''{1: 1, **{}}'''
        expected = '''_py_backwards_merge_dicts([{1: 1}])'''
        test.assert_equals(expected, code, DictUnpackingTransformer)

# Generated at 2022-06-14 01:49:12.296579
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_ast.ast3 as ast
    transformer = DictUnpackingTransformer()
    assert transformer.visit(ast.Dict(keys=[None, ast.Num(1)],
                                values=[ast.Num(1)],
                                ctx=ast.Load())) == ast.Call(
                                    func=ast.Name(id='_py_backwards_merge_dicts'),
                                    args=[ast.List(elts=[ast.Call(
                                                        func=ast.Name(id='dict'),
                                                        args=[ast.Dict(
                                                            keys=[],
                                                            values=[ast.Num(1)],
                                                            ctx=ast.Load())],
                                                        keywords=[])],
                                                   ctx=ast.Load())],
                                    keywords=[])

# Generated at 2022-06-14 01:49:23.198200
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def check(before: str, after: str) -> None:
        root = ast.parse(before)
        element = root.body[0].value  # type: ast.Dict
        assert isinstance(element, ast.Dict)

        transformer = DictUnpackingTransformer()
        new_dict = transformer.visit(element)
        assert transformer._tree_changed

        root.body[0].value = new_dict
        assert astor.to_source(root).strip() == after

    check(
        """{1: 1}""",
        """{1: 1}"""
    )

    check(
        """{1: 1, **{}}""",
        """_py_backwards_merge_dicts([{1: 1}], {})"""
    )


# Generated at 2022-06-14 01:49:24.230375
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:49:30.982009
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert DictUnpackingTransformer._split_by_None([
        (ast.Num(n=1), ast.Num(n=2)),
        (ast.Num(n=3), ast.Num(n=4)),
        (None, ast.Name(id='a')),
        (None, ast.Name(id='b')),
    ]) == [
        [  # type: ignore
            (ast.Num(n=1), ast.Num(n=2)),
            (ast.Num(n=3), ast.Num(n=4))],
        ast.Name(id='a'),  # type: ignore
        [],
        ast.Name(id='b')
    ]

# Generated at 2022-06-14 01:49:41.129548
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..compiler import Compiler
    from ..utils.testing import assert_code_equal

    c = Compiler()

    assert_code_equal(
        c.compile_ast(ast.parse('''
            a = {1: 1, **a}
        ''')),
        'a = _py_backwards_merge_dicts([{1: 1}], a)')

    assert_code_equal(
        c.compile_ast(ast.parse('''
            a = {1: 1, **a, **b}
        ''')),
        'a = _py_backwards_merge_dicts([{1: 1}], a, b)')


# Generated at 2022-06-14 01:50:20.803915
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class DictUnpackingTransformerSubclass(DictUnpackingTransformer):
        def __init__(self):
            self._tree_changed = False

    unpacking_transformer = DictUnpackingTransformerSubclass()
    parsed = ast.parse('1')
    assert not unpacking_transformer._tree_changed
    assert unpacking_transformer.visit(parsed) == parsed
    assert not unpacking_transformer._tree_changed



# Generated at 2022-06-14 01:50:28.728088
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import logging
    import inspect
    import astunparse
    from textwrap import dedent
    transformer = DictUnpackingTransformer()
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    logger.addHandler(logging.StreamHandler())

    def test(code: str, expected: str) -> str:
        node = ast.parse(dedent(code))
        transformer.visit(node)
        transformed = astunparse.unparse(node).strip()
        assert transformed == dedent(expected)
        return transformed

    test(
        code='''\
        dict(1=1, **dict_a)
        ''',
        expected='''\
        _py_backwards_merge_dicts((dict(1=1), dict_a))
        '''
    )

   

# Generated at 2022-06-14 01:50:39.269801
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    @compile_to_ast(DictUnpackingTransformer)
    def __py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    @compile_to_ast(DictUnpackingTransformer)
    def foo(a):
        return {1: 1, **a}

    foo.compare_ast('''
        def foo(a):
            return _py_backwards_merge_dicts([{1: 1}], a)
    ''')

# Generated at 2022-06-14 01:50:49.399588
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    @snippet
    def vartest():
        """
        x = {1: 1, 2: 2, **{3: 3, 4: 4}}
        y = {1: 1, 2: 2, 1: 10, **{3: 3, 4: 4}}
        z = {1: 1, 2: 2, **{2: 3, 4: 4}}
        z = {1: 1, **{1: 1, 2: 2, **{2: 3, 4: 4}}, 4: 4}
        """

    assert DictUnpackingTransformer.run_tree(vartest.get_tree()) == DictUnpackingTransformer.run_source(vartest.get_source())


# Generated at 2022-06-14 01:51:00.307972
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    data = """
{a: b, **x, **y, 'c': d}
{a: b, **x, 'c': d, **y}
{a: b, 'c': d, **x, **y}
{a: b, **x, 'c': d, **y, e: f}
{a: b, **x, **y, 'c': d, **z, e: f, **g}
{a: b, **x, **y, 'c': d, **z, e: f, g: h, **i}
{a: b, **x, **y, **z, 'c': d, **g, e: f, h: h, **i}
    """

# Generated at 2022-06-14 01:51:09.973849
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import code_gen
    from ..utils.source import Source
    from .base import BaseNodeTransformerTest

    # pylint: disable=invalid-name,missing-docstring,too-few-public-methods,unnecessary-pass
    class TestDictUnpackingTransformer(BaseNodeTransformerTest):
        transformer = DictUnpackingTransformer
        before = Source(
            """
            def f():
                return {'a': 1, **{'b': 2}}
            """)
        after = Source(
            """
            def f():
                return _py_backwards_merge_dicts([{'a': 1}], {'b': 2})
            """)

    code_gen.assert_transformation(TestDictUnpackingTransformer)

# Generated at 2022-06-14 01:51:22.427689
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:51:28.600937
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    src = """\
d = {1: 2, 3: 4, **{5: 6, **tiv}, **{7: 8, 9: 10}}
    """
    result = transform(src, DictUnpackingTransformer)
    expected = """\
d = _py_backwards_merge_dicts([{1: 2, 3: 4}, {5: 6, **tiv}, {7: 8, 9: 10}])
    """
    assert result.strip() == expected.strip()



# Generated at 2022-06-14 01:51:35.944626
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.codegen import to_source
    from ..utils.ast import parse

    source = '''
{
    1: 1,
    **dict_1
}
'''
    expr = parse(source).body[0]
    result = DictUnpackingTransformer.run_top_down(expr)
    print(to_source(result))
    assert to_source(result) == '''
_py_backwards_merge_dicts([{1: 1}], dict_1)
'''


# Generated at 2022-06-14 01:51:37.159399
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor

# Generated at 2022-06-14 01:52:57.713680
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_ast.ast3 as typed_ast
    import ast
    import unittest
    from typed_ast.test_utils import convert
    from .transforms.unpack import DictUnpackingTransformer

    class Test(unittest.TestCase):
        def test(self):
            class DictUnpackingTransformer(BaseNodeTransformer):
                """Compiles:

                    {1: 1, **dict_a}

                To:

                    _py_backwards_merge_dicts([{1: 1}], dict_a})

                """
                target = (3, 4)

                def _split_by_None(self, pairs: Iterable[Pair]) -> Splitted:
                    """Splits pairs to lists separated by dict unpacking statements."""
                    result = [[]]  # type: Splitted

# Generated at 2022-06-14 01:53:05.304700
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_base import BaseNodeTransformerTestCase
    from .test_base import Code

    class TestCase(BaseNodeTransformerTestCase):
        transformer = DictUnpackingTransformer

        # FIXME: Add some tests for DictUnpackingTransformer.visit_Dict

    test_cases = [
        # FIXME: add some test_cases
    ]

    for test_case in test_cases:
        test_case.run(TestCase)

# Generated at 2022-06-14 01:53:16.228580
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # type: () -> None
    """Make sure that the test covers all branches."""
    source = """
    {1: "a", 2: "b", None: True, 1.0: float("1"), None: None}
    """
    expected = """
    _py_backwards_merge_dicts([{1: "a", 2: "b"}, 1.0: float("1")], True, None)
    """

    node = ast.parse(source)
    DictUnpackingTransformer(node).run()
    node = ast.fix_missing_locations(node)
    expected = ast.parse(expected)
    expected = ast.fix_missing_locations(expected)
    assert ast.dump(node) == ast.dump(expected)


# Generated at 2022-06-14 01:53:23.787019
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from . import transform
    from . import visit_and_get_tree_changed
    from ..utils.ast_diff import check_ast_diff

    def check(code, expected_code):
        tree_changed = visit_and_get_tree_changed(code, DictUnpackingTransformer)
        result_code = transform(code, DictUnpackingTransformer)
        check_ast_diff(expected_code, result_code)
        return tree_changed

    assert True is check('{1: 1, **dict_a}', '_py_backwards_merge_dicts([{1: 1}], dict_a)')
    assert True is check('{**dict_a, 1: 1}', '_py_backwards_merge_dicts([{1: 1}], dict_a)')
    assert True is check

# Generated at 2022-06-14 01:53:31.851278
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source
    from ..utils.ast import dump_ast

    source1 = "d = {'a': 1, 'b': 2, **{'c': 3}}"
    source2 = "d = {'a': 1, **{'c': 3}, 'b': 2, **{'d': 4}}"
    source3 = "d = {'a': 1, **{'c': 3}, **{'d': 4}}"
    source4 = "d = {**{'c': 3}, **{'d': 4}}"
    source5 = "{**{'c': 3}, 'a': 1, **{'d': 4}}"
    for source in (source1, source2, source3, source4, source5):
        tree = ast.parse(source)

# Generated at 2022-06-14 01:53:39.603291
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class TestTransformer(BaseNodeTransformer):
        def visit_Dict(self, node):
            return 1
    module_node = ast.parse('{1: 1, **{}}')
    transformer = TestTransformer()
    result = transformer.visit(module_node)
    node = ast.parse(
        """
if False:
    _py_backwards_merge_dicts([{1: 1}], {})
1
"""
    ).body[1]
    assert_equal(result, node)



# Generated at 2022-06-14 01:53:46.473022
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.parser import parse
    from ..utils.visitor import print_visit

    # Check unpacking with key
    node = parse("{1: 1, **{'a': 1}}")
    assert isinstance(node, ast.Module)
    DictUnpackingTransformer().visit(node)
    assert print_visit(node) == "from __future__ import print_function\n" \
                                 "_py_backwards_merge_dicts([{1: 1}], {'a': 1})\n"

    # Check unpacking without key
    node = parse("{**{'a': 1}}")
    assert isinstance(node, ast.Module)
    DictUnpackingTransformer().visit(node)

# Generated at 2022-06-14 01:53:53.649494
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Unit test for method visit_Dict of class DictUnpackingTransformer."""
    from .test_base import BaseNodeTransformerTestCase
    from .test_base import overloaded_compile_function

    class TestCase(BaseNodeTransformerTestCase):
        transformer = DictUnpackingTransformer()
        compile_function = staticmethod(overloaded_compile_function(
            transformer, {'_py_backwards_merge_dicts': merge_dicts}))

    TestCase.run_tests(__file__, 'test_DictUnpackingTransformer_visit_Dict')



# Generated at 2022-06-14 01:54:02.228218
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import (
        source_to_unicode, source_to_ast, ast_to_source,
        ast_to_source_unicode)
    from ..utils.source import transform
    from ..utils.py33_test_support import assertRegex

    source = """
        {1: 1, **dict_a}
        """
    expected = """
        _py_backwards_merge_dicts([{1: 1}], dict_a)
        """
    test_transform = transform(DictUnpackingTransformer)
    ast_obj = source_to_ast(source)
    new_source = ast_to_source(test_transform(ast_obj))

    # source -> ast
    assert source == source_to_unicode(ast_obj)

    # ast -> source
    assert new_