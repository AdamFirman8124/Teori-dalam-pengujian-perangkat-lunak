

# Generated at 2022-06-14 01:44:17.252708
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ...tests import test_utils
    from ...tests.context_mock import context_mock

    class Dummy(object):
        pass

    from ...utils import logging
    logging.setup()
    logger = logging.getLogger(__name__)

    args = Dummy()
    args.node_transformer_classes = []

    tree = test_utils.parse_string("""\
        d = {1: 2, **a, 3: 4, **b, 5: 6, **c, 7: 8, **d, 9: 10}""")
    ctx = context_mock(args=args, logger=logger)
    DictUnpackingTransformer(ctx).visit(tree)


# Generated at 2022-06-14 01:44:24.761357
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from ..utils.testing import check_transform, AST_3_if


# Generated at 2022-06-14 01:44:33.399852
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # test_1
    # before
    # {1: 1, **dict_a}
    # after
    # _py_backwards_merge_dicts([dict({1: 1})], dict_a)
    before = ast.parse("{1: 1, **dict_a}", '<test>')
    after = ast.parse("_py_backwards_merge_dicts([dict({1: 1})], dict_a)", '<test>')
    trans = DictUnpackingTransformer()
    new = trans.visit(before)
    assert ast.dump(after) == ast.dump(new)
    # test_2
    # before
    # {1: 1, **dict_a, 2: 2}
    # after
    # _py_backwards_merge_dicts([{1:

# Generated at 2022-06-14 01:44:42.623002
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.tree import parse
    from ..utils.astcompare import ast_equal

    def test(code, expected):
        expected = parse(expected)
        node = parse(code)
        transformer = DictUnpackingTransformer()
        result = transformer.visit(node)
        assert ast_equal(expected, result)

    test(
        code='{1: 1, **dict_a}',
        expected='_py_backwards_merge_dicts([dict({1: 1})], dict_a)')

    test(
        code='{**dict_a, 1: 2}',
        expected='_py_backwards_merge_dicts([dict_a, dict({1: 2})])')


# Generated at 2022-06-14 01:44:50.956813
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '{1: "a", 2: "b", 3: "c", **dict_a, **dict_b}'
    expected = '_py_backwards_merge_dicts([{"a": 1, "b": 2, "c": 3}], dict_a, dict_b)'
    module = ast.parse(source)
    tree_transformer = DictUnpackingTransformer()
    tree_transformer.visit(module)
    assert codegen.to_source(module) == merge_dicts() + expected

# Generated at 2022-06-14 01:45:01.991341
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    def do_test(code, expected):
        result = transformer.visit(ast.parse(code))
        assert ast.dump(result) == expected

    yield do_test, \
        "{1:1, **dict_a}", \
        "Module(body=[Expr(value=Call(func=Name(id='_py_backwards_merge_dicts', ctx=Load()), args=[List(elts=[Dict(keys=[Num(n=1)], values=[Num(n=1)]), Name(id='dict_a', ctx=Load())])], keywords=[]))])"


# Generated at 2022-06-14 01:45:12.329739
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    source = '''
    dict_a = {1: 2}
    {1: 1, **dict_a, **{3: 4}, 2: 2, **{5: 6}}
    '''
    expected_source = '''
    _py_backwards_merge_dicts([dict({1: 1}), dict_a], {3: 4}, dict({5: 6}))
    '''
    tree = ast.parse(source)
    expected_tree = astor.code_to_ast.parse(expected_source)
    DictUnpackingTransformer().visit(tree)
    assert astor.to_source(tree) == astor.to_source(expected_tree)

# Generated at 2022-06-14 01:45:22.876208
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformerTestCase
    from ..utils.tree import dump
    from ..utils.compare_ast import compare_ast

    class TestCase(BaseNodeTransformerTestCase):
        TRANSFORMER = DictUnpackingTransformer
        EXAMPLE = """\
            {
                1: 2,
                **{3: 4, 5: 6}
            }
            """
        EXPECTED = """\
            dict(_py_backwards_merge_dicts([dict([(1, 2)])], dict([(3, 4), (5, 6)])))
            """

    example = TestCase.EXAMPLE
    expected = TestCase.EXPECTED

    tree = ast.parse(example)
    transformer = TestCase.TRANSFORMER()
    new_

# Generated at 2022-06-14 01:45:28.112872
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.fixtures import unpack_dict
    snippet = unpack_dict.get_snippet()
    expected_ast = unpack_dict.get_ast()
    node = ast.parse(snippet)
    _node = DictUnpackingTransformer().visit(node)
    assert ast.dump(_node) == ast.dump(expected_ast)


# Generated at 2022-06-14 01:45:38.175951
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse_fixed import unparse
    from astpretty import pprint

    tree = ast.parse('''{**{}, 2: 1, []: [], 1: 2, 'c': 'd'}''')

    transformer = DictUnpackingTransformer()
    new_tree = transformer.visit(tree)

    assert transformer._tree_changed is True
    assert isinstance(new_tree, ast.Module)
    assert new_tree.body[0].body[0].name == '_py_backwards_merge_dicts'
    assert isinstance(new_tree.body[0].body[0].decorator_list, list)

# Generated at 2022-06-14 01:45:46.904161
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    source = ast.parse("{1: 1, **dict_a}")
    expected = ast.parse("_py_backwards_merge_dicts([{1: 1}], dict_a)")
    assert transformer.visit(source) == expected

# Generated at 2022-06-14 01:46:00.946640
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '''
        {1: 1, **{2: 2}}
    '''

    expected = '''
        _py_backwards_merge_dicts([{1: 1}], {2: 2})
    '''

    module = compile(source, '<unknown>', 'exec', flags=ast.PyCF_ONLY_AST)
    transformer = DictUnpackingTransformer()
    actual = transformer.visit(module)
    assert ast.dump(actual) == ast.dump(expected)

    source = '''
        {1: 1, b: 2, **{2: 2}}
    '''

    expected = '''
        _py_backwards_merge_dicts([{1: 1, 'b': 2}], {2: 2})
    '''


# Generated at 2022-06-14 01:46:09.186632
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_astunparse import unparse
    from .fixtures import DICT_UNPACKING_TRANSFORMER_TEST_CASES
    for test_case in DICT_UNPACKING_TRANSFORMER_TEST_CASES:
        tree = test_case.given.parse()
        DictUnpackingTransformer().visit(tree)
        assert unparse(tree) == test_case.expected

# Generated at 2022-06-14 01:46:19.494682
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:46:31.125583
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import transform, assert_equal
    from ..utils.testing import assert_symmetrical_transformation
    from ..utils.source import Source
    from ..utils.tree import dump

    s = Source(
        """
        a = {1: 1, **{2: 2}, **{3: 3}}
        """)
    expected = Source("""
    _py_backwards_merge_dicts([{1: 1, 2: 2}, {3: 3}])""")

    ast_tree = s.parse()
    new_ast_tree = transform(DictUnpackingTransformer(), ast_tree)
    assert_equal(dump(new_ast_tree), expected)

    assert_symmetrical_transformation(
        DictUnpackingTransformer(),
        Source("{1: 1}"))
    assert_

# Generated at 2022-06-14 01:46:45.443368
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    def check(source: str, expected: str) -> None:
        node = ast.parse(source)
        node = transformer.visit(node)
        result = compile(node, '', mode='exec')
        exec(result)

        d = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6
        }
        expected_result = eval(expected)
        result_dict = _py_backwards_merge_dicts(
            [{'a': 1, 'b': 2}, {'c': 3}, {'d': 4}, {'e': 5}, {'f': 6}])
        assert result_dict == expected_result


# Generated at 2022-06-14 01:46:55.403796
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor

    tree = ast.parse(
        '{\n'
        '    key_a: value_a,\n'
        '    key_b: value_b,\n'
        '    None: dict_c,\n'
        '    None: dict_d,\n'
        '    key_c: value_c,\n'
        '    None: dict_e,\n'
        '    key_d: value_d,\n'
        '}')


# Generated at 2022-06-14 01:47:03.465250
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    dut = DictUnpackingTransformer()
    code = '{**a, 1: 2, 3: 4, **b}'
    expected = '_py_backwards_merge_dicts([{1: 2, 3: 4}], a, b)'
    assert dut.visit(ast.parse(code)) == ast.parse(expected)



# Generated at 2022-06-14 01:47:13.628024
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    from .common import get_transformer
    module = ast.parse('{1: 1, 2: 2, 3: 3, **dict(), **dict4, 5: 5}')
    transformer = get_transformer(DictUnpackingTransformer)
    transformer.visit(module)
    assert transformer._tree_changed
    assert transformer._snippets == ['_py_backwards_merge_dicts']

# Generated at 2022-06-14 01:47:22.324277
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from ..utils.source import source
    from .. import ast_converter
    import astor


# Generated at 2022-06-14 01:47:38.887306
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from ..utils.unparse import Unparser
    ast_3_4 = ast.parse(
        """
{1: 2, **dict_1, 3: 4, **dict_2, 5: 6, **dict_3}
""",
        'test', 'exec')
    DictUnpackingTransformer().visit(ast_3_4)
    Unparser(ast_3_4)
    assert astor.to_source(ast_3_4) == """
_py_backwards_merge_dicts([{1: 2}, dict_1, {3: 4}, dict_2, {5: 6}], dict_3)
"""

# Generated at 2022-06-14 01:47:46.021591
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # pylint: disable=C0111
    from ..utils.testing import assert_transformed_ast
    assert_transformed_ast("""
        {1: 1, **dict_a}
    """, """
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """, """
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
    """)

# Generated at 2022-06-14 01:47:55.833919
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse(
        """
        {
            1: 2,
            **{1: 2},
            2: 3,
            **{3: 4}
        }
        """)
    transformed_tree = DictUnpackingTransformer().visit(tree)
    assert isinstance(transformed_tree, ast.Module)
    assert len(transformed_tree.body) == 1
    assign = transformed_tree.body[0]
    assert isinstance(assign, ast.Assign)
    assert len(assign.targets) == 1
    assert isinstance(assign.targets[0], ast.Name)
    assert assign.targets[0].id == '__ans'
    assert isinstance(assign.value, ast.Call)

# Generated at 2022-06-14 01:48:05.958535
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert DictUnpackingTransformer('{1: 1, **a, 2: 2, **b}').result == \
            '_py_backwards_merge_dicts([{1: 1, 2: 2}], a, b)'
    assert DictUnpackingTransformer('{1: 1, 2: 2, **a}').result == \
            '_py_backwards_merge_dicts([{1: 1, 2: 2}], a)'
    assert DictUnpackingTransformer('{1: 1, **a, 2: 2}').result == \
            '_py_backwards_merge_dicts([{1: 1, 2: 2}], a)'

# Generated at 2022-06-14 01:48:09.369656
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = """
        foo({1: 1, **dict_a})
        """
    node = ast.parse(code)
    # noinspection PyTypeChecker
    transformer = DictUnpackingTransformer()
    result = transformer.visit(node)
    result_code = compile(result, '<test>', 'exec')
    exec(result_code)

# Generated at 2022-06-14 01:48:14.446934
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source
    from ..utils.ast import get_ast
    from ..utils.compat import get_code

    source = source("{1: 1, 2: 2, **{3: 3, 4: 4}}")
    ast_module = get_ast(source)

    trans = DictUnpackingTransformer()
    trans.visit(ast_module)

    # Check that module was changed
    assert trans.tree_changed is True

    # Check that dict was converted to calls
    assert get_code(ast_module) == source_merge


# Generated at 2022-06-14 01:48:25.524201
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Dict, Name, Call
    from ..types import dict_, dict_value
    from ..utils import T
    from ..utils.typechecker import TypeChecker

    import pytest

    class TransformerTest(BaseNodeTransformer):
        def __init__(self, ast_: ast.AST) -> None:
            self._ast = ast_

        def visit(self, node: ast.AST) -> None:
            pass

    with pytest.warns(None) as warnings:
        transformer = TransformerTest(None)

        dict_unpacking = DictUnpackingTransformer()

        assert dict_unpacking.target == (3, 4)

        # Test on Dict without unpacking

# Generated at 2022-06-14 01:48:36.402813
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from unittest import TestCase, main

    from typed_ast.ast3 import parse

    from .base import BaseNodeTransformerTestCase

    def to_ast(code: str) -> ast.Dict:
        return parse(code).body[0].value

    class DictUnpackingTransformerTestCase(BaseNodeTransformerTestCase):
        transformer = DictUnpackingTransformer
        default_kwargs = dict(return_changed_tree=False)

        def test_basic(self):
            source = '{1: 1, 2: 2, **{3: 3}, **{4: 4}}'
            expected = '_py_backwards_merge_dicts([{1: 1, 2: 2}], {3: 3}, {4: 4})'
            node = to_ast(source)
            result = self.transform

# Generated at 2022-06-14 01:48:46.882839
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..type_inference.syntax import parse

    def check(before: str, after: str) -> None:
        tr = DictUnpackingTransformer()
        tr.visit(parse(before))
        result = before.split('\n')
        assert ''.join(result) == after

    check(
        """
        {1: 1, **x}
        """,
        """
        _py_backwards_merge_dicts([{1: 1}], x)
        """)

    check(
        """
        {1: 1, **x, 2: 2, **y, 3: 3}
        """,
        """
        _py_backwards_merge_dicts([{1: 1}, {2: 2}, {3: 3}], x, y)
        """)

# Generated at 2022-06-14 01:48:53.086956
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    before = ast.parse("""{1: 1, **{2: 2}, **{3: 3}, 4: 4, **{5: 5}}""")
    DictUnpackingTransformer().visit(before)
    after = ast.parse("""
_py_backwards_merge_dicts([{1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}])""")
    assert before == after



# Generated at 2022-06-14 01:49:21.543408
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    transformer = DictUnpackingTransformer()  # type: ignore

    def check(input: ast.Dict, expected: ast.AST) -> None:
        actual = transformer.visit(input)  # type: ignore
        assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 01:49:27.155792
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = dedent('''\
    {1: 1, 2: 2, 3: 3, **x}
    ''')
    expected = dedent('''\
    _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], x)
    ''')
    mod = ast.parse(source)
    DictUnpackingTransformer(expected=expected).visit(mod)

# Generated at 2022-06-14 01:49:38.704034
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from ast_tools.visitor import AstRewriteVisitor

    # Given
    class Finder(ast.NodeVisitor):
        def __init__(self):
            self.result = []

        def visit_Dict(self, node: ast.Dict) -> None:
            if None in node.keys:
                self.result.append(node)

    source = """
    import a

    def f(**kwargs):
        return {1: 1, **kwargs}

    def g():
        return {1: 1, **a.b}
    """
    node = ast.parse(source)
    visitor = Finder()
    visitor.visit(node)
    target_nodes = visitor.result

    # When
    visitor = AstRewriteVisitor(DictUnpackingTransformer)
    visitor

# Generated at 2022-06-14 01:49:46.698808
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Examples:
    # {1: 2}
    # {1: 2, **x}
    # {1: 2, **x, 3: 4}
    # {1: 2, **x, **y}
    # {1: 2, **x, 3: 4, **y, 5: 6}
    # {1: 2, **x, 3: 4, **y, **z}
    # {1: 2, **x, 3: 4, **y, 5: 6, **z, **t}

    def get_expectation(source: str, target: str) -> ast.Module:
        expectation = ast.parse(
            dedent(target).strip(),
            filename='<unknown>',
            mode='exec')

        expectation.body.insert(0,
                                merge_dicts.get_body()) 

# Generated at 2022-06-14 01:49:57.200947
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Tests compilation of:
    
        {1: 1, None: {...}, 2: 2, None: {...}}
        
    To:
    
        _py_backwards_merge_dicts([{1: 1, 2: 2}], {...})
    """
    transformer = DictUnpackingTransformer()
    node = ast.Dict(keys=[ast.Num(1), None, ast.Num(2), None],
                    values=[ast.Num(1),
                            ast.Dict(keys=[ast.Num(3)],
                                     values=[ast.Num(4)]),
                            ast.Num(2),
                            ast.Dict(keys=[ast.Num(5)],
                                     values=[ast.Num(6)])])
    # TODO: add assert

# Generated at 2022-06-14 01:50:04.475853
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def check(before, after):
        checker = Checker()
        checker.visit(before)
        assert checker.tree_changed is True
        assert before is not checker.visit(before)
        assert after == after

    class Checker(DictUnpackingTransformer):
        def __init__(self):
            self.tree_changed = False

        def visit_Dict(self, node: ast.Dict) -> ast.Dict:
            self.tree_changed = True
            return self.generic_visit(node)  # type: ignore

        def _merge_dicts(self, *args):
            pass

    yield check

# Generated at 2022-06-14 01:50:11.640524
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from test.utils import round_trip

    assert round_trip('''{'a': 1, 2: 3, **{'b': 'c', 'd': 4}}''') == \
    '''_py_backwards_merge_dicts([{'a': 1, 2: 3}], {'b': 'c', 'd': 4})'''

    assert round_trip('''{**{}}''') == \
    '''{}'''



# Generated at 2022-06-14 01:50:18.776693
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():  # type: ignore
    assert ast.parse("""
        {
            1: 2,
            **{3: 4},
            5: 6,
            **{7: 8},
            9: 10,
        }
        """).body[0].value == \
        DictUnpackingTransformer().visit(ast.parse("""
            {
                1: 2,
                **{3: 4},
                5: 6,
                **{7: 8},
                9: 10,
            }
            """).body[0].value)

# Generated at 2022-06-14 01:50:26.016974
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class T(ast.NodeVisitor):
        def visit_Call(self, node):
            assert node.func.id == '_py_backwards_merge_dicts'
            return node.args[0].elts[0]
    dict_ = ast.parse("dict({1: 1, **dict_a})", mode='eval').body
    actual = T().visit(dict_)
    expected = ast.parse("{1: 1}", mode='eval').body
    assert ast.dump(actual, annotate_fields=False) == ast.dump(expected, annotate_fields=False)

# Generated at 2022-06-14 01:50:36.881874
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert ast.dump(
        DictUnpackingTransformer().visit(ast.parse("{1: 1, 2: 2, **{3: 4}} ")),
        include_attributes=True,
        ) == \
        ast.dump(ast.parse(
            """
            _py_backwards_merge_dicts([{1: 1, 2: 2}], {3: 4})
            """),
        include_attributes=True)

# Generated at 2022-06-14 01:51:50.445771
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from .utils import roundtrip
    from ..utils.examples import examples_dicts
    for code, nodes in examples_dicts():
        code = \
            """
            dict_a = {0: 0, 1: 1}
            dict_b = {0: 0}
            {}
            """.format(code)
        _, crnt_nodes = roundtrip(ast.parse(code), DictUnpackingTransformer)
        assert len(nodes) == len(crnt_nodes)

# Generated at 2022-06-14 01:51:59.596354
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    input = '''{1: 1, **d}'''
    expected = '''_py_backwards_merge_dicts([{1: 1}], d)'''

    node = ast.parse(input).body[0].value
    transformer = DictUnpackingTransformer()
    result = transformer.visit(node)
    result_code = compile(ast.fix_missing_locations(ast.Module(body=[ast.Expr(value=result)])), '', 'exec')
    result_namespace = {}
    exec(result_code, result_namespace)
    assert result_namespace['_py_backwards_merge_dicts'] == _py_backwards_merge_dicts

# Generated at 2022-06-14 01:52:02.572485
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    return """
    from math import *

    def f():
        pass
    """


# Generated at 2022-06-14 01:52:08.649550
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse('{1: 1, None: 2, {3: 3}, 4: 5, None: 6}')
    expected = '_py_backwards_merge_dicts([dict({1: 1, None: 2}), dict({3: 3}), dict({4: 5}), 6])'
    result = DictUnpackingTransformer().visit(node)
    assert expected == ast.unparse(result).strip()

# Generated at 2022-06-14 01:52:19.445023
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_astunparse import unparse
    from .test_transformer import transform_snippets
    from .test_transformer import find_functions
    from .test_transformer import visit_nodes
    import ast as std_ast

    transformer = DictUnpackingTransformer()
    func = find_functions(transform_snippets(merge_dicts.get_body()),
                          '_py_backwards_merge_dicts')[0]
    assert func.args.kwonlyargs == []
    assert func.args.vararg == 'dicts'
    assert func.args.kwarg == None
    assert func.args.defaults == []

    module = transform_snippets('''
    result = {1: 1, **dict_a}
    ''')
    module = visit_

# Generated at 2022-06-14 01:52:25.091698
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from .test_base import BaseTestTransformer
    from .test_base import BaseTestAnalyzer
    from .test_base import BaseTestFixer

    class TestFixer(BaseTestFixer):
        transformer_class = DictUnpackingTransformer

    class TestAnalyzer(BaseTestAnalyzer):
        transformer_class = DictUnpackingTransformer

    class TestTransformer(BaseTestTransformer):
        transformer_class = DictUnpackingTransformer

    (TestFixer, TestAnalyzer, TestTransformer)  # Silence linter

# Generated at 2022-06-14 01:52:26.810890
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:52:40.796577
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer(): # type: () -> None
    transformer = DictUnpackingTransformer()

    assert transformer._split_by_None([]) == [[]]
    assert transformer._split_by_None([(1, 2)]) == [[(1, 2)]]
    assert transformer._split_by_None([(1, 2), (None, 3), (4, 5)]) == [
        [(1, 2)], 3, [(4, 5)]]
    assert transformer._split_by_None([(None, 1), (None, 2)]) == [1, 2]

    assert transformer._prepare_splitted([]) == []
    assert transformer._prepare_splitted([[]]) == []

# Generated at 2022-06-14 01:52:50.309125
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .base import UnitTestTransformer

    tree = ast.parse("{1: 1, **dict_a}")
    expected = """
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result


    {1: 1, **dict_a}
    """
    trans = UnitTestTransformer(DictUnpackingTransformer, tree, expected)
    trans.test()


# Generated at 2022-06-14 01:53:01.316657
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transforms.convert import convert_from_module
    from ..utils.ast import dump_ast

    result = DictUnpackingTransformer().visit_Dict(
        ast.parse('''
        {1: 2, **{3: 4}, 5: 6, **{7: 8}, **{9: 10}}
        ''').body[0])

# Generated at 2022-06-14 01:53:27.957507
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:53:39.603241
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .base import CompilerTestCase
    from ..utils.tree import node_equal
    from ..utils.tree import build_module



# Generated at 2022-06-14 01:53:49.949284
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    # type: () -> None
    import sys
    import astor
    from .fixture import transform

    code = "{1: 1, 2: 2, **dict_a, **dict_b, 3: 3, **dict_c, 4: 4}"
    tree = ast.parse(code)
    transform(tree, DictUnpackingTransformer)
    print(astor.to_source(tree))


# Generated at 2022-06-14 01:54:00.230692
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import glob
    import pathlib
    from ..utils.ast_builder import build_ast
    from ..utils.ast_list import ast_list
