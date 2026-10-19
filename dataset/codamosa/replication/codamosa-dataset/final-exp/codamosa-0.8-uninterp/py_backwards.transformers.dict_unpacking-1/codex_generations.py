

# Generated at 2022-06-14 01:44:13.797870
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source, to_source
    from .. import compile_snippet

    # Write unit test here
    snippet = """{1: 1, 2: 2, **x, 3: 3, **y}"""
    result = compile_snippet(source(snippet), DictUnpackingTransformer)
    assert to_source(result) == \
           '''_py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], x, y)'''

# Generated at 2022-06-14 01:44:21.159081
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def assert_transform(src, expected):
        tr = DictUnpackingTransformer()
        actual = tr.visit(ast.parse(src))
        assert ast.dump(actual) == ast.dump(ast.parse(expected))

    assert_transform('{**a}', '_py_backwards_merge_dicts([], a)')
    assert_transform('{1: 1, **a}', '_py_backwards_merge_dicts([{1: 1}], a)')
    assert_transform('{**a, **b, 2: 2}',
                     '_py_backwards_merge_dicts([], a, b, {2: 2})')

# Generated at 2022-06-14 01:44:30.535539
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import textwrap
    from pprint import pformat
    from ..utils.tree import print_tree

    assert not DictUnpackingTransformer.is_target_node(ast.Dict())


# Generated at 2022-06-14 01:44:33.221285
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:44:42.532429
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transforms import DictUnpackingTransformer
    from textwrap import dedent
    node = ast.parse(dedent("""\
        {
            1: 2,
            3: 4,
            **{5: 6}
        }
        """))

    expected = dedent("""\
        {
            1: 2,
            3: 4,
            **_py_backwards_merge_dicts([{1: 2, 3: 4}, {5: 6}])
        }
        """)

    transformer = DictUnpackingTransformer()
    result = transformer.visit(node)
    assert transformer._tree_changed
    assert expected == ast.unparse(result)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 01:44:54.092798
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import AbstractTransformerTestCase
    import typing

    class Test(AbstractTransformerTestCase):
        def _get_target(self):
            return DictUnpackingTransformer

        def test_dict(self):
            source = '''
                {1: "1", **{"2": 2}, 3: "3"}
                {1: "1", ("2", 3): 2, 3: "3"}
                {1: "1", None: 2, None: 3, 3: "3"}
                {1: "1", **{"2": 2}, **{"3": 3}}
                {1: "1", **{"2": 2}, None, **{"3": 3}}
            '''

# Generated at 2022-06-14 01:45:00.041271
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_ast.ast3 as ast3
    dict_unpacking_transformer = DictUnpackingTransformer()
    test_input = ast3.Dict(
        keys=[None, ast3.Constant(None), None, None, None, ast3.Constant(None)],
        values=[
            ast3.Constant('First dict'),
            ast3.Constant('First dict None'),
            ast3.Constant('Second dict'),
            ast3.Constant('Second dict None'),
            ast3.Constant('Third dict'),
            ast3.Constant('Third dict None'),
        ])

    result = dict_unpacking_transformer.visit(test_input)

    assert isinstance(result, ast3.Call)
    assert isinstance(result.func, ast3.Name)

# Generated at 2022-06-14 01:45:11.303965
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor  # type: ignore
    
    # Normal test
    assert DictUnpackingTransformer().visit(
        ast.parse(
            "def f():\n    {'a': 1, 2: 3, **consts, 'b': 42}; 42")) == \
        ast.parse(
            "def f():\n    _py_backwards_merge_dicts(\n"
            "        [{'a': 1, 2: 3}], consts); 42")

    # The case when dict is empty

# Generated at 2022-06-14 01:45:22.215763
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def run(expr: str, expected: str) -> None:
        node = ast.parse(expr)
        node = DictUnpackingTransformer().visit(node)
        assert ast.dump(node) == expected

    run('{1: 1, 2: 2}', '{1: 1, 2: 2}')
    run('{1: 1, **{2: 2}}',
        '_py_backwards_merge_dicts([{1: 1}], {2: 2})')
    run('{**{1: 1}, **{2: 2}}',
        '_py_backwards_merge_dicts([], {1: 1}, {2: 2})')

# Generated at 2022-06-14 01:45:30.154088
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    module = ast.parse('''
        {1: 1, None: {4: 4}, 2: 2, None: {7: 7}, 3: 3}
    ''')
    transformer = DictUnpackingTransformer()
    result = transformer.visit(module)
    assert transformer._tree_changed

# Generated at 2022-06-14 01:45:40.156450
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    expr = ast.parse('''
    {1: 2, **a}
    ''').body[0].value  # type: ignore

    result = transformer.visit(expr)

    expected = '_py_backwards_merge_dicts([{1: 2}], a)'

    assert ast.dump(result) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 01:45:46.249770
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.builder import build

    source  = "[*, {**x, 'a': 1, **y, time: time.time()}]"
    target1 = "list([time.time(), _py_backwards_merge_dicts([{'a': 1}], x, y)])"
    target2 = "list({None: time.time(), 'a': 1}.update(x).update(y))"

    # We need the following steps to run because merge_dicts is inserted at
    # the beginning of the transformations.
    transformer = DictUnpackingTransformer
    # These assertions are needed to check if the snippet merge_dicts is inserted properly
    assert transformer.transform_code('') == \
        merge_dicts.get_body() + '\n\n'

# Generated at 2022-06-14 01:46:00.809397
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.testing import assert_unchanged_ast, assert_changed_ast

    # DictUnpackingTransformer is activated for all Python versions below 3.5
    for version in (3, 4):
        assert_unchanged_ast("""
            a = 1
        """, version)

        assert_unchanged_ast("""
            a = 1
            
            def x():
                ...
        """, version)

        assert_unchanged_ast("""
            x = 1
            
            def __init__(**kwargs):
                super().__init__(**kwargs)
        """, version)


# Generated at 2022-06-14 01:46:12.500316
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    transformer = DictUnpackingTransformer()
    result = transformer.visit(ast.parse(
        """a = {1: 1, **{2: 2, 3: 3}, 4: 4, 5: 5, **{6: 6}}"""
    ))
    assert DictUnpackingTransformer._tree_changed == True  # type: ignore
    assert transformer.render(result) == 'a = _py_backwards_merge_dicts([{' \
                                          '1: 1, 4: 4, 5: 5}], {2: 2, 3: 3},' \
                                          ' {6: 6})'

    transformer = DictUnpackingTransformer()

# Generated at 2022-06-14 01:46:21.756035
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse
    from .helpers import assert_transforms_to, node

    dict_unpacking_transformer = DictUnpackingTransformer()

    assert_transforms_to(
        'dict_unpacking_transformer',
        dict_unpacking_transformer,
        parse('{1: 1, 2: 2, **dict_a}'),
        node(
            '_py_backwards_merge_dicts([dict({1: 1, 2: 2})], dict_a)'))

# Generated at 2022-06-14 01:46:25.348044
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # TODO: This test also tests visit_Call
    # TODO: This test also tests visit_Module
    # TODO: Tests for this function are in CompatTransformerTestCase
    assert False, "TODO: Implement"

# Generated at 2022-06-14 01:46:32.066198
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    assert DictUnpackingTransformer().visit_Module(ast3.parse("""
    def a_func(foo):
        return 1
    """).body[0]) == ast3.parse("""
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    def a_func(foo):
        return 1
    """).body[0]


# Generated at 2022-06-14 01:46:46.740406
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    def test_splitted(splitted, expected):
        result = DictUnpackingTransformer._prepare_splitted(splitted)
        assert list(map(ast.dump, result)) == list(map(ast.dump, expected))

    test_splitted([[(None, None)]], [ast.Call(
        func=ast.Name(id='dict'),
        args=[],
        keywords=[])])

    test_splitted([], [])  # type: ignore

    test_splitted([[(None, None), (None, None)]], [
        ast.Call(func=ast.Name(id='dict'), args=[], keywords=[]),
        ast.Call(func=ast.Name(id='dict'), args=[], keywords=[])])


# Generated at 2022-06-14 01:46:51.007503
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    program = """{1:1}"""
    expected = f"""{merge_dicts}
{program}"""

    node = ast.parse(program)
    DictUnpackingTransformer().visit(node)
    actual = ast.dump(node, include_attributes=False)

    assert actual == expected



# Generated at 2022-06-14 01:47:04.472099
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = """
    {1: 1, 2: 2, 3: 3, **dict_a, 4: 4, 5: 5, **dict_b, **dict_c}
    """
    expected = """
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    
    
    _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}, dict_a, {4: 4, 5: 5}, dict_b, dict_c])
    """
    etalon = ast.parse(expected)  # type: ignore
    assert DictUnpackingTransformer().visit(ast.parse(code)) == etalon

# Generated at 2022-06-14 01:47:18.884518
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    # Compile
    test = ast.parse('{1: 1, **dict_a}')
    transformer = DictUnpackingTransformer()
    transformed = transformer.visit(test)
    expected = ast.parse('_py_backwards_merge_dicts([{1: 1}], dict_a)')
    assert astor.to_source(transformed) == astor.to_source(expected)

    test = ast.parse('{1: 2, **{3: 4, 5: 6}, 7: 8}')
    transformer = DictUnpackingTransformer()
    transformed = transformer.visit(test)
    expected = ast.parse(
        '_py_backwards_merge_dicts([{1: 2}, {7: 8}], {3: 4, 5: 6})')


# Generated at 2022-06-14 01:47:26.848793
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    """Method visit_Module of class DictUnpackingTransformer
    should return the module which contains definition of function
    _py_backwards_merge_dicts and the same source code as input source code."""
    module = ast.parse("a = {1: 1, 2: 2, **c}")
    DictUnpackingTransformer().visit(module)

# Generated at 2022-06-14 01:47:31.828168
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .transformer import Transformer

    transformer = Transformer(DictUnpackingTransformer)
    src = '{1: 2, **dict_a, **dict_b}'
    expected = '_py_backwards_merge_dicts([{1: 2}], dict_a, dict_b)'

    assert transformer.transform(src) == expected

# Generated at 2022-06-14 01:47:42.894534
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from ..utils.ast_parser import parse
    from ..utils.test_utils import assert_equal_asts

    nodes = {
        'simple': ast.Dict,
        'no_unpacking': ast.Dict,
        'with_unpacking': ast.Call,
        'with_no_key': ast.Call,
        'with_two_unpacking': ast.Call,
    }
    source = """\
    {1: 1, **dict_a}
    {1: 1}
    {1: 1, **dict_a, **dict_b}
    {**dict_a}
    {1: 1, **dict_a, **dict_b}
    """
    scope = {'_py_backwards_merge_dicts': 'None'}



# Generated at 2022-06-14 01:47:51.070850
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    t = DictUnpackingTransformer()
    assert t._split_by_None([]) == [[]]
    assert t._split_by_None([(None, 1)]) == [[1]]
    assert t._split_by_None([(None, 1), (None, 2)]) == [[1], 2]
    assert t._split_by_None([(None, 1), (2, 3), (4, 5)]) == [[1], [], [2, 4], [3, 5]]
    
    assert ast.dump(t._prepare_splitted([])) == '[]'
    assert ast.dump(t._prepare_splitted([1])) == '[dict(1)]'
    assert ast.dump(t._prepare_splitted([[]])) == '[]'

# Generated at 2022-06-14 01:47:58.291896
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    # Given
    code = """
        {1}
    """
    expected = """
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
        
        {1}
    """
    # When
    result = DictUnpackingTransformer().visit_Module(
        ast.parse(code))  # type: ignore
    # Then
    assert ast.dump(result) == expected



# Generated at 2022-06-14 01:48:06.411072
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..test import test_utils
    from ..test.test_utils import transform

    test_utils.assert_equal_source(
        """
            {
                'a': 1,
                **dict_a,
                'b': 2,
                **dict_b,
                'c': 3,
            }
        """,
        """
            _py_backwards_merge_dicts(
                [{'a': 1, 'b': 2, 'c': 3}],
                dict_a,
                dict_b,
            )
        """,
        transform(DictUnpackingTransformer)
    )

# Generated at 2022-06-14 01:48:14.411094
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from ..utils.source import source, source_without_imports

    expected_source = dedent(r'''
    def some_func():
        return _py_backwards_merge_dicts([{'a': 20}], {'b': 21})

    ''')

    source_ = source(DictUnpackingTransformer, expected_source,
                     {'some_func': '''
    def some_func():
        return {'a': 20, **{'b': 21}}
    '''})
    source_without_imports(source_) == source_without_imports(expected_source)

# Generated at 2022-06-14 01:48:25.525158
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformerTestCase
    from .transformer_test_case import ast_equal
    from .transformer_test_case import run_transformer_test_case

    class TestCase(BaseNodeTransformerTestCase):
        transformer = DictUnpackingTransformer()

        def test_dict_unpacking(self):
            class Test(ast.AST):
                _fields = ('a', 'b', 'c', 'd', 'expr')


# Generated at 2022-06-14 01:48:35.795306
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    assert ast.dump(DictUnpackingTransformer().visit(
        ast.parse("{'a': 1, **{'b': 2}}", mode='eval'))) == \
        "Call(func=Name(id='_py_backwards_merge_dicts', ctx=Load()), " \
        "args=[List(elts=[Dict(keys=[Str(s='a')], values=[Num(n=1)]), " \
        "Call(func=Name(id='dict', ctx=Load()), " \
        "args=[Dict(keys=[Str(s='b')], values=[Num(n=2)])], " \
        "keywords=[])], ctx=Load())], keywords=[])"



# Generated at 2022-06-14 01:48:46.822810
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..testing_utils import assert_source_equal

# Generated at 2022-06-14 01:48:56.407585
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert ast.parse('{}').body[0].value == \
        DictUnpackingTransformer().visit(ast.parse('{}').body[0].value)  # type: ignore
    assert ast.parse('{1: 1}').body[0].value == \
        DictUnpackingTransformer().visit(ast.parse('{1: 1}').body[0].value)  # type: ignore
    assert ast.parse('{1: 1, **{2: 2}}').body[0].value == \
        DictUnpackingTransformer().visit(ast.parse('{1: 1, **{2: 2}}').body[0].value)  # type: ignore
    assert ast.parse('{1: 1, **{2: 2}, 3: 3}').body[0].value == \
        DictUn

# Generated at 2022-06-14 01:48:58.460189
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    pass  # implemented in test_DictUnpackingTransformer.py

# Generated at 2022-06-14 01:49:01.345649
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    """
    https://github.com/Python3Bonobo/bonobo-python3/issues/1
    """
    # type: () -> None
    transformer = DictUnpackingTransformer()

# Generated at 2022-06-14 01:49:08.232826
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    node = ast.parse('{1: 2, **a, **b}')
    transformer.visit(node)
    assert transformer._tree_changed
    tree = ast.parse('''
        _py_backwards_merge_dicts(
            [{1: 2}],
            a,
             b
        )
    ''')
    assert ast.dump(node) == ast.dump(tree)

# Generated at 2022-06-14 01:49:18.737113
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse
    from typing import Dict
    from ..utils.reader import read

    class Dummy:
        def __init__(self, x: int) -> None:
            self.x = x

    ast_dict = """{1: 2, **{3: 4}, 5: 6, None: {**None}, **{7: 8}}"""
    ast_tuple = """tuple({1: 2, **{3: 4}, 5: 6, None: {**None}, **{7: 8}})"""
    ast_dict_literal = """{1: 2, **{3: 4}, 5: 6, None: **{7: 8}}"""

# Generated at 2022-06-14 01:49:28.810123
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    pairs = [
        (ast.Num(1), ast.Num(1)),
        (None, ast.Name(id='a')),
        (ast.Num(2), ast.Num(2)),
        (None, ast.Name(id='b')),
        (ast.Num(3), ast.Num(3)),
    ]

    node = ast.Dict(keys=[key for key, _ in pairs], values=[value for _, value in pairs])
    real = DictUnpackingTransformer().visit(node)

# Generated at 2022-06-14 01:49:31.021706
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ast import parse
    from .transformers import register_transformers

# Generated at 2022-06-14 01:49:38.839335
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .base import do_transformation_test
    src = """
    def f():
        a = {1: 1, 2: 2}
        b = {3: 3, 4: 4, **a}
        return b
    """
    exp = """
    def f():
        a = {1: 1, 2: 2}
        b = _py_backwards_merge_dicts([{3: 3, 4: 4}], a)
        return b
    """
    do_transformation_test(DictUnpackingTransformer, src, exp)



# Generated at 2022-06-14 01:49:46.808468
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import make_call
    from ..unpack_unpacking import UnpackUnpackingTransformer

    make_call = UnpackUnpackingTransformer(3, 4).visit(make_call)
    DUT = DictUnpackingTransformer(3, 4)

    assert DUT.visit(make_call('{1: 1, 2: 2, 3: 3, **dict_a, 4: 4}')) == \
           make_call('_py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}, 4], '
                     'dict_a)')


# Generated at 2022-06-14 01:50:26.244249
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse
    from ..utils.unittest import TestCase, expectedFailure

    class DictUnpackingTransformerTestCase(TestCase):
        def test_basic(self):
            tree = ast.parse('{1: 2, 3: 4}')
            new_tree = DictUnpackingTransformer().visit(tree)
            self.assertEqual(ast.dump(new_tree),
                             ast.dump(tree))

        def test_unpacking(self):
            tree = ast.parse('{2: 3, 4: 5, **dict_}')
            new_tree = DictUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 01:50:35.384783
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test_visitor import TestVisitor

    ast_ = ast.parse('''{1: 2, 3: 4, **{1: 1, 2: 2}, None: None, **{3: 3}, 4: 5}''')
    ast_.body[0] = DictUnpackingTransformer().visit(ast_.body[0])
    TestVisitor(expected='''
_py_backwards_merge_dicts([dict({1: 5, 3: 4}), {1: 1, 2: 2}, {3: 3}], dict({4: 5}))''').visit(ast_.body[0])

# Generated at 2022-06-14 01:50:43.325676
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse('{1: 1, **{2: 2}, 3: 3, **{4: 4}, 5: 5}')
    visitor = DictUnpackingTransformer()
    visitor.visit(tree)
    assert astor.to_source(tree).strip() == \
        '_py_backwards_merge_dicts([{1: 1}, {3: 3}, {5: 5}], {2: 2}, {4: 4})'

# Generated at 2022-06-14 01:50:53.638550
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    dut = DictUnpackingTransformer()

    # Check simple case
    node = ast.Dict(keys=[None, None, ast.Num(n=3), None, None, ast.Num(n=6)],
                    values=[ast.Num(n=1),
                            ast.Num(n=2),
                            ast.Num(n=3),
                            ast.Num(n=4),
                            ast.Num(n=5),
                            ast.Num(n=6)])

# Generated at 2022-06-14 01:51:04.960790
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..imports import find_imports
    import_to_insert = list(find_imports('_py_backwards_merge_dicts'))

    source = '''
        {1: 2}
        {1: 2, 3: 4}
        {1: 2, 3: 4, **a}
        {1: 2, 3: 4, **a, 5: 6}
        {1: 2, 3: 4, **a, 5: 6, **b}
    '''

    merge_dicts.insert_at_end(import_to_insert)


# Generated at 2022-06-14 01:51:12.089838
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.ast import assert_ast_equal
    from ast import Dict
    from typed_ast import ast3
    # input
    input = ast3.parse('''{1: 1, **dict_a}''')
    # expected
    expected = ast3.parse(
        '''_py_backwards_merge_dicts([{1: 1}], dict_a)''')
    # actual
    actual = DictUnpackingTransformer().visit(input)
    # compare
    assert_ast_equal(expected, actual)



# Generated at 2022-06-14 01:51:23.210879
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    class DictUnpackingTransformer(BaseNodeTransformer):
        def visit_Dict(self, node: ast.Dict) -> ast.Call:
            if None not in node.keys:
                return self.generic_visit(node)  # type: ignore

            pairs = zip(node.keys, node.values)
            splitted = []
            for key, value in pairs:
                if key is None:
                    splitted.append(value)
                    splitted.append([])
                else:
                    assert isinstance(splitted[-1], list)
                    splitted[-1].append((key, value))


# Generated at 2022-06-14 01:51:35.059870
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = """{1: 2}"""
    expected = """{1: 2}"""
    assert expected == run_on_doc_string(source, DictUnpackingTransformer)

    source = """{None: 2}"""
    expected = """_py_backwards_merge_dicts([dict(), 2])"""
    assert expected == run_on_doc_string(source, DictUnpackingTransformer)

    source = """{1: 2, 3: 4}"""
    expected = """{1: 2, 3: 4}"""
    assert expected == run_on_doc_string(source, DictUnpackingTransformer)

    source = """{1: 2, None: 3, 4: 5}"""

# Generated at 2022-06-14 01:51:48.298712
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    pairs = [(1, 2), (3, 4), (None, ast.Name(id='name_a')), (5, 6)]
    # Backwards merge dicts: [{1: 2, 3: 4}, name_a, {5: 6}]

# Generated at 2022-06-14 01:51:53.411180
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    store = {}
    store["d"] = {1: 2}
    a = {3: 4, **store["d"]}
    a = {3: 4, **store["d"]}
    t = DictUnpackingTransformer()

    code = compile(t.transform(ast.parse("a = {3: 4, **store['d']}")),
                   "test.py",
                   mode="exec")
    exec(code, store)
    assert store['a'] == {3: 4, 1: 2}

# Generated at 2022-06-14 01:52:42.876653
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    
    def assert_transform(source, expected):
        source_tree = ast.parse(source)
        expected_tree = ast.parse(expected)
        transformer = DictUnpackingTransformer()
        result = transformer.visit(source_tree)
        assert result == expected_tree

    assert_transform('{1: 1}', '{1: 1}')
    assert_transform('{1: 1, **{2: 2}}', '_py_backwards_merge_dicts([{1: 1, 2: 2}])')
    assert_transform('{1: 1, **{2: 2}, **{3: 3}}', '_py_backwards_merge_dicts([{1: 1, 2: 2}, {3: 3}])')

# Generated at 2022-06-14 01:52:49.855405
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse("{1: 1, **{2: 2}}")
    transformer = DictUnpackingTransformer()
    expected = ast.parse("_py_backwards_merge_dicts([{1: 1}], {2: 2})")
    actual = transformer.visit(tree)
    assert (ast.dump(actual) == ast.dump(expected))


# Generated at 2022-06-14 01:52:54.814386
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    class DictUnpackingTransformerChecker(DictUnpackingTransformer):
        def __init__(self):
            self.visited = []

        def visit(self, node):
            self.visited.append(type(node))
            return super().visit(node)


# Generated at 2022-06-14 01:53:04.969355
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # DictUnpackingTransformer({**a, **b, **c}) ->
    # _py_backwards_merge_dicts([], a, b, c))
    #
    code = """\
        {**a, **b, **c}"""
    transformer = DictUnpackingTransformer()
    tranformed_code = transformer(code)
    expected_code = """\
        _py_backwards_merge_dicts([], a, b, c)"""
    assert expected_code == tranformed_code

    # DictUnpackingTransformer({**a, **b, **c}) ->
    # _py_backwards_merge_dicts([], a, b, c))
    #

# Generated at 2022-06-14 01:53:12.867921
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .context import Context
    from .fixtures import dict_unpacking
    from .matchers import match_ast

    # DictUnpackingTransformer.visit_Dict
    source = "{1: 1, **dict_a}"
    expected = "{1: 1, **_py_backwards_merge_dicts([{1: 1}], dict_a)}"
    tree = ast.parse(source)
    expected = ast.parse(expected)
    result = DictUnpackingTransformer(Context()).visit(tree)
    assert match_ast(result, expected)


if __name__ == '__main__':
    test_DictUnpackingTransformer_visit_Dict()

# Generated at 2022-06-14 01:53:18.886798
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source

    transformer = DictUnpackingTransformer()
    before = source('''
        {1: 1, **dict_a}
    ''')
    after = source('''
        _py_backwards_merge_dicts([{1: 1}], dict_a])
    ''')
    assert transformer.visit(ast.parse(before)) == ast.parse(after)
    assert transformer.will_change_tree is True

# Generated at 2022-06-14 01:53:22.916775
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    transformer = DictUnpackingTransformer()
    tree = transformer.visit(ast.parse('{1: 1, **dict_a}'))
    assert transformer._tree_changed
    assert ast.dump(tree) == (
        '_py_backwards_merge_dicts([{1: 1}], dict_a'
    )



# Generated at 2022-06-14 01:53:31.259574
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Unit test for method visit_Dict of class DictUnpackingTransformer."""
    from ..utils.testutils import _test_transform


# Generated at 2022-06-14 01:53:41.878676
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from py_backwards.transformations_3to4.transformations import DictUnpackingTransformer

    transformer = DictUnpackingTransformer()

    assert isinstance(transformer.visit(ast.parse('{1: 1, **dict_a}')), ast.Call)
    assert isinstance(transformer.visit(ast.parse('{1: 1, **dict_a, 2:2}')), ast.Call)
    assert isinstance(transformer.visit(ast.parse('{1: 1, **dict_a, 2:2, **dict_b, 3:3}')), ast.Call)

    assert isinstance(transformer.visit(ast.parse('{1: 1}')), ast.Dict)

# Generated at 2022-06-14 01:53:52.189336
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from itertools import repeat
    from ..utils.tree import parse_ast, print_ast

    x_prepared = ['{}', '{a: 1, b: 2}']

    xs = list(repeat((ast.Num(n=1), ast.Num(n=1)), 1000))
    xs.append((ast.Name(id='a'), ast.Num(n=1)))
    xs.append((ast.Name(id='b'), ast.Num(n=2)))
    xs.append((None, ast.Dict(keys=[], values=[])))
    x_splitted = [
        [],
        [xs[-2]],
        [xs[-1]],
        [],
    ]
