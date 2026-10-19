

# Generated at 2022-06-14 01:44:03.507804
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse("{1: 1, **dict_a}")
    DictUnpackingTransformer().visit(module)
    assert merge_dicts.strip() in ast.dump(module)



# Generated at 2022-06-14 01:44:15.404128
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import os.path
    import sys
    import unittest

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from typed_ast.ast3 import parse
    from typed_ast.ast3 import dump
    from typed_ast.transforms import DictUnpackingTransformer

    class TestDictUnpackingTransformer(unittest.TestCase):
        def assertTransformedEquals(self,
                                    before: str,
                                    after: str) -> None:
            node_before = parse(before)
            node_after = parse(after)
            modified_node = DictUnpackingTransformer().visit(node_before)
            self.assertEqual(dump(node_after), dump(modified_node))


# Generated at 2022-06-14 01:44:23.957152
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    input1 = ast.parse('{1: 1, **dict_a}')
    output1 = ast.parse(
        """_py_backwards_merge_dicts([dict({1: 1})], dict_a)""")
    input2 = ast.parse('{1: 1, 2: 2, **dict_a}')
    output2 = ast.parse(
        """_py_backwards_merge_dicts([dict({1: 1, 2: 2})], dict_a)""")
    input3 = ast.parse('{1: 1, 2: 2, **dict_a, **dict_b}')
    output3 = ast.parse(
        """_py_backwards_merge_dicts([dict({1: 1, 2: 2})], dict_a, dict_b)""")
    input4

# Generated at 2022-06-14 01:44:34.991819
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    src = "a = {}"
    expected = ast.parse(src).body[0]
    actual = transformer.visit(ast.parse(src))

    assert actual == expected

    src = "a = {1: 1, **dict_a}"
    expected = ast.parse(src).body[0]
    actual = transformer.visit(ast.parse(src))

    assert ast.dump(actual) == ast.dump(expected)

    src = "a = {1: 1, **dict_a, 2: 2}"
    expected = ast.parse(src).body[0]
    actual = transformer.visit(ast.parse(src))

    assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 01:44:42.601773
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse('d = {1: 2, 2: 3, **d1, 4: 5, 6: 7, **d2}')
    expected = ast.parse("""
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result

        d = _py_backwards_merge_dicts([{1: 2, 2: 3}, d1, {4: 5, 6: 7}], d2)
    """)
    DictUnpackingTransformer().visit(module)  # Should be no-op
    assert module == expected

# Generated at 2022-06-14 01:44:50.956788
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_node_equal, assert_tree_changed
    snippet = """
        {1, 2, 3, **dict1}
    """
    tree = snippet.ast
    tree = DictUnpackingTransformer().visit(tree)
    assert_tree_changed(tree)
    expected = """
        _py_backwards_merge_dicts([{1, 2, 3}], dict1)
    """
    expected = expected.ast
    assert_node_equal(tree, expected)



# Generated at 2022-06-14 01:44:59.607213
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    t = DictUnpackingTransformer()

    # simple dictionary merging
    node = ast.parse("{1: 1, **dict_a}").body[0].value
    assert isinstance(node, ast.Dict)
    new_node = t.visit(node)
    assert isinstance(new_node, ast.Call)
    assert t._tree_changed == True
    assert ast.dump(new_node) == ast.dump(ast.parse("_py_backwards_merge_dicts((dict({1: 1}),), dict_a)"))
    t._tree_changed = False

    # unchanged case
    node = ast.parse("{1: 1, 2: 2}").body[0].value
    assert isinstance(node, ast.Dict)
    new_node = t.visit(node)


# Generated at 2022-06-14 01:45:07.156496
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    transformer = DictUnpackingTransformer()
    tree = ast.parse('{1: 1, **dict_a}')
    assert transformer.visit(tree) == ast.parse(
        """
        _py_backwards_merge_dicts([{1: 1}], dict_a)
        """)

# Generated at 2022-06-14 01:45:16.399809
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor  # type: ignore

    code = """\
{1: 1, **{2: 2}, 3: 3, **{4: 4}}
{1: 1, **{2: 2, **{3: 3, **{4: 4}}}}
{1: 1, **{2: 2, **{3: 3, **{4: 4, **{5: 5}}}}, **{6: 6}, 7: 7}
{1: 1, **{2: 2, **{3: 3, **{4: 4, **{5: 5}}}}}\
""".lstrip()

# Generated at 2022-06-14 01:45:24.366413
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = """
    a = {
        **a,
        b = 1,
        'c': 2,
        d: 3,
    }    
    """
    module = ast.parse(code)
    transformer = DictUnpackingTransformer()
    transformer.visit(module)
    assert transformer._tree_changed

    expected = """
    a = _py_backwards_merge_dicts([{'b': 1, 'c': 2, d: 3}], a)
    """
    assert module_to_str(module) == trim(expected)


# Generated at 2022-06-14 01:45:37.576903
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse('{1: 1, **dict_a, 2: 2, **dict_b}')
    transformer = DictUnpackingTransformer()
    result = transformer.visit(tree)
    assert result.body[0].value.func.id == '_py_backwards_merge_dicts'
    assert result.body[0].value.args[0].elts == [
        ast.Dict(keys=[ast.Num(n=1), ast.Num(n=2)],
                 values=[ast.Num(n=1), ast.Num(n=2)]),
        ast.Name(id='dict_a'),
        ast.Name(id='dict_b'),
    ]

# Generated at 2022-06-14 01:45:44.268729
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse('d = {**{}}')
    transformer = DictUnpackingTransformer()
    transformer.visit(tree)
    expected = ast.parse(merge_dicts + '\n\nd = _py_backwards_merge_dicts([], {})')
    assert tree == expected


# Generated at 2022-06-14 01:46:00.178368
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from . import TransformerTestCase
    from .transforms.unpacking import UnpackingTransformer
    
    class DictUnpackingTransformerTestCase(TransformerTestCase):
        transform = DictUnpackingTransformer
        target = (3, 4)
        input = """
        {1: 2, None: {3: 4, 5: 6}, 7: 8}
        {1: 2, **{3: 4, 5: 6}, 7: 8}
        """
        expected_output = """
        _py_backwards_merge_dicts([{1: 2}, {3: 4, 5: 6}], {7: 8})
        _py_backwards_merge_dicts([{1: 2}, {3: 4, 5: 6}], {7: 8})
        """

# Generated at 2022-06-14 01:46:10.719504
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Original dict
    d = {'a': 1, **{'b': 2, 'c': 3}, 'd': 4}
    # Expected dict
    e = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # Compiled dict
    c = _py_backwards_merge_dicts([{'a': 1}, {'d': 4}], {'b': 2, 'c': 3})
    assert e == d  # dicts is equal
    assert e == c  # dicts is equal

    # Test for dict without unpacking
    d = {1: 2, 3: 4}
    e = d
    c = DictUnpackingTransformer().visit(ast.parse(repr(d))).body[0].value
    assert e == d  # dicts is

# Generated at 2022-06-14 01:46:18.615769
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from ..utils.test_utils import node_test

    merge_dicts_tree = merge_dicts.get_tree()
    DictUnpackingTransformer().visit(merge_dicts_tree)

    tree = ast.parse("""
    foo = {1: 1, **{2: 2}, 3: 3, **{4: 4}}
    """)
    node_test(tree,
              """
        foo = _py_backwards_merge_dicts([{1: 1}, {2: 2}, {3: 3}], {4: 4})""")

# Generated at 2022-06-14 01:46:23.947790
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse("""
    x = {1: 1, **dict_a}
    """)
    DictUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == (
    """Module(body=[
    Assign(targets=[Name(id='x', ctx=Store())],
        value=Call(func=Name(id='_py_backwards_merge_dicts', ctx=Load()),
            args=[List(elts=[Dict(keys=[Num(n=1)], values=[Num(n=1)]),
            Name(id='dict_a', ctx=Load())])], keywords=[])),
    ])""")


# Generated at 2022-06-14 01:46:30.220945
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse('{1: 1, 2: 2, 3: 3, **some_dict, 4: 4, **some_other_dict}')
    result = DictUnpackingTransformer().visit(tree)
    assert str(result) == '_py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}, ' \
                          'some_dict, {4: 4}], some_other_dict)'

# Generated at 2022-06-14 01:46:39.830433
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    import unittest

    dict_unpacking_transform = DictUnpackingTransformer()

    class TestDictUnpacking(unittest.TestCase):
        @staticmethod
        def _test(before, after):
            tree = ast.parse(before)
            dict_unpacking_transform.visit(tree)
            self.assertEqual(astor.to_source(tree), after)

        def test_Dict(self):
            before = """
        {1: 1, **dict_a}
        """
            after = """
        _py_backwards_merge_dicts([{1: 1}], dict_a)
        """
            self._test(before, after)


# Generated at 2022-06-14 01:46:44.469059
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import ast
    import astor
    node = ast.parse(
        """{\n    1: 2,\n    3: 4,\n}\n""")
    assert isinstance(node, ast.Module)
    transformed = DictUnpackingTransformer().visit(node)

# Generated at 2022-06-14 01:46:50.341928
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    sample_code = '''\
{'a': 1, **b, 'c': 2, **d}
'''
    expected_code = '''\
_py_backwards_merge_dicts([{'a': 1}, 'c': 2], b, d)
'''
    assert DictUnpackingTransformer(sample_code).run() == expected_code

# Generated at 2022-06-14 01:47:07.277701
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    x = ast.parse("""
    {1: 2, **{1: 0}, 2: 5, **{1: 4}, **{1: 6}}
    """)
    DictUnpackingTransformer().visit(x)

# Generated at 2022-06-14 01:47:15.928783
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ty_ast.ast3 as ast
    node = ast.Dict(keys=[None, ast.Str(s='4'), None],
                    values=[ast.Dict(keys=[ast.Str(s='a'), ast.Str(s='b')],
                                     values=[ast.Num(n=42), ast.Num(n=3.14)]),
                            ast.Dict(keys=[ast.Str(s='a')],
                                     values=[ast.Num(n=42)]),
                            ast.Dict(keys=[ast.Str(s='a'), ast.Str(s='b')],
                                     values=[ast.Num(n=42), ast.Num(n=3.14)])])

# Generated at 2022-06-14 01:47:24.529749
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from asttokens import ASTTokens
    from ..utils.tokens import insert_at as tokens_insert_at
    from textwrap import dedent

    test_code = dedent('''
        x = {1: 1, 2: 2}
        y = {1: 2, **x}
        z = {1: 2, 3: 3, **x}
        w = {1: 2, 3: 3, **x, **y}
    ''')
    atok = ASTTokens(test_code, parse=True)
    node = atok.tree

# Generated at 2022-06-14 01:47:25.031632
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert False

# Generated at 2022-06-14 01:47:32.798801
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import os.path
    import astor
    from test_module import test_module
    from ..utils.tree import get_tree
    from ..utils.snippet import PythonCodeSnippet
    from ..utils.misc import assert_ast_tree_equal

    code = PythonCodeSnippet.from_file(os.path.join(test_module, 'dict_unpacking.py'))
    node = get_tree(code)
    DictUnpackingTransformer().generic_visit(node)


# Generated at 2022-06-14 01:47:39.392966
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..testing.utils import get_ast
    source = """
{1: None, 2: None, **{1: 2, 3: 4}, 3: None, 4: 5, **{2: 3}}
"""
    expected = """
_py_backwards_merge_dicts([{1: None, 2: None}, dict({1: 2, 3: 4}), {3: None, 4: 5}], {2: 3})
"""
    node = get_ast(source)
    node = DictUnpackingTransformer().visit(node)
    assert get_ast(expected) == node

# Generated at 2022-06-14 01:47:48.702169
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import cmp_node
    from .base import BaseNodeTransformerTestCase
    from .dict_unpacking import DictUnpackingTransformer

    class Test(BaseNodeTransformerTestCase):
        def test(self):
            dict_ = ast.Dict(
                keys=[ast.Constant(1), None, ast.Constant(2)],
                values=[ast.Constant(1), ast.Call(
                    func=ast.Constant(3),
                    args=[],
                    keywords=[])]
            )


# Generated at 2022-06-14 01:47:53.953434
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    assert transformer.visit(ast.parse('''
        {1:1, **d, 2:2}
    ''')) == ast.parse('''
        d = {}
        _py_backwards_merge_dicts([{1:1}, d, {2:2}])
    ''')

# Generated at 2022-06-14 01:48:00.135922
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from . import parse_ast, dump_ast
    from textwrap import dedent

    expected = dedent('''
    _py_backwards_merge_dicts([{1: 1, 2: 2}, {3: 3, 4: 4}, {5: 5}])
    ''').strip()

    tree = parse_ast(
        node_transformer_classes=[DictUnpackingTransformer],
        code=dedent('''\
        {1: 1, 2: 2, **{3: 3, 4: 4, **{5: 5}}}
        ''')
    )
    assert dump_ast(tree) == expected

# Generated at 2022-06-14 01:48:10.669289
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.testing import assert_ast_equal
    from .codegen import to_source

    ast_node = ast.parse('''
    {1: 2, "a": "b", **{}, **{"c": "d"}, 4: 5, **{7: 8}}
    ''')
    result = to_source(DictUnpackingTransformer().visit(ast_node))
    expected = '''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    _py_backwards_merge_dicts([{1: 2, "a": "b", 4: 5}, {}, {"c": "d"}, {7: 8}])
    '''
    assert_ast_equal

# Generated at 2022-06-14 01:48:26.080865
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import sys
    import textwrap
    import types
    import unittest

    import astunparse

    class DictUnpackingTransformerTest(unittest.TestCase):
        def setUp(self):
            self.transformer = DictUnpackingTransformer()
            self.maxDiff = None

        def test_trivial(self):
            code = "{'a': 1}"
            target_code = '_py_backwards_merge_dicts([{"a": 1},])'
            ast_ = ast.parse(code)
            new_ast = self.transformer.visit(ast_)
            new_code = astunparse.unparse(new_ast).strip()
            self.assertEqual(target_code, new_code)


# Generated at 2022-06-14 01:48:34.199815
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..parsers import python_to_ast
    from ..utils.tree import to_code

    code = """
    {
        1: 1,
        **dict_a
    }
    """

    expected = """
    _py_backwards_merge_dicts([{1: 1}], dict_a)
    """

    tree = python_to_ast(code, parser='python3')
    tree = DictUnpackingTransformer(tree).transformed

    result = to_code(tree)
    assert result == expected

# Generated at 2022-06-14 01:48:45.207721
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    Marker = Union[ast.Call, ast.Dict]

    def assert_result(text, expected_text, func=assert_not_equal):
        new_ast = DictUnpackingTransformer().visit(ast.parse(text))
        new_text = ast.unparse(new_ast).strip()
        func(text, new_text)
        func(expected_text.strip(), new_text)

    assert_result('{}', '')
    assert_result('{1:2}', '')

    assert_result('{**{}}', '{}')
    assert_result('{**{1:2}}', '{1:2}')
    assert_result('{**{1:2,3:4}}', '{1:2,3:4}')

# Generated at 2022-06-14 01:48:49.264535
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.python_source import Source
    source = Source("""
    d = {1: 1, **dict_a}
    """)
    transformer = DictUnpackingTransformer()
    result = source.get_ast().accept(transformer)
    assert source.dump_ast() != result

# Generated at 2022-06-14 01:48:56.644943
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    transformer = DictUnpackingTransformer()
    source = """{'a': 1, 'b': 2, **dict_c}"""
    expected = """_py_backwards_merge_dicts([{'a': 1, 'b': 2}, dict_c])"""
    node = ast.parse(source)
    node = transformer.visit(node)
    node = ast.fix_missing_locations(node)
    generated = compile(node, '', 'exec')
    actual = str(node.body[0].value)
    assert actual == expected

# Generated at 2022-06-14 01:49:05.413917
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Arrange
    class DummyTransformer(BaseNodeTransformer):
        pass

    transformer = DummyTransformer()
    tree = ast.Module(body=[ast.Dict(keys=[None, ast.Str(s='a'), None, None,
                                          ast.Str(s='b')],
                                    values=[ast.Num(n=1), ast.Num(n=2),
                                            ast.Num(n=3), ast.Num(n=4),
                                            ast.Num(n=5)])])

    # Act
    DictUnpackingTransformer(transformer).visit(tree)

    # Assert
    assert transformer.tree_changed is True
    assert isinstance(tree.body[1], ast.Call)

# Generated at 2022-06-14 01:49:15.287020
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from astunparse import unparse

    class Dummy(object):
        def __init__(self, tree_changed: bool = False):
            self._tree_changed = tree_changed

        @property
        def tree_changed(self) -> bool:
            return self._tree_changed

    module = ast.parse('{1: 1, **dict_a}')
    node = Dummy()
    DictUnpackingTransformer.visit_Module(node, module)
    assert unparse(module) == '_py_backwards_merge_dicts([{1: 1}], dict_a)\n'
    assert node.tree_changed



# Generated at 2022-06-14 01:49:26.095328
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node1 = ast.Dict(keys=[ast.Num(n=1), None], values=[ast.Num(n=1), ast.Dict(keys=[ast.Num(n=2)], values=[ast.Num(n=2)])])
    node2 = ast.Dict(keys=[ast.Num(n=1), ast.Num(n=2)], values=[ast.Num(n=1), ast.Num(n=2)])
    result1 = DictUnpackingTransformer().visit(node1)
    result2 = DictUnpackingTransformer().visit(node2)


# Generated at 2022-06-14 01:49:37.606221
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_code_equal
    from ..utils.tree import ast_parse

    code = '''
        {1: 1, 2: 2, 3: 3, **dict_}
    '''
    expected = '''
        _py_backwards_merge_dicts(
            [{1: 1, 2: 2, 3: 3}],
            dict_)
    '''
    expected = expected.lstrip()
    expected = ast_parse(expected)

    input = ast_parse(code)
    ast.fix_missing_locations(input)

    result = DictUnpackingTransformer().visit(input)
    ast.fix_missing_locations(result)

    assert_code_equal(expected, result)



# Generated at 2022-06-14 01:49:46.324637
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    source = '''
        {'a': 1, 'b': 2}
        {'a': 1, **{'b': 2}}
        {'a': 1, **{'b': 2}, **{'c': 3}}
    '''


# Generated at 2022-06-14 01:50:03.490035
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .utils import parse, dump

    class DictFoo(DictUnpackingTransformer):
        def visit_Dict(self, node: ast.Dict) -> ast.Dict:
            node = DictUnpackingTransformer.visit_Dict(self, node)
            node.keys.append(ast.Str(s='foo'))
            node.values.append(ast.Num(i=42))
            return node

    # No unpacking
    tree = parse('{1: 1}')
    tree = DictFoo().visit(tree)
    assert dump(tree) == '{1: 1, "foo": 42}'

    # Unpacking
    tree = parse('{1: 1, **foo}')
    tree = DictFoo().visit(tree)

# Generated at 2022-06-14 01:50:13.976310
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ast as py_ast
    import astunparse

    def parse(source: str) -> py_ast.AST:
        # noinspection PyTypeChecker
        return py_ast.parse(source)

    def pyast_to_ast_ast(pyast: py_ast.AST, target: Tuple[int, int]) \
            -> ast.AST:
        from ..converter import Converter
        return Converter(target).convert(pyast)

    def compile_to_pyast(ast_ast: ast.AST) -> py_ast.AST:
        from ..converter import Converter
        return Converter().visit(ast_ast)


# Generated at 2022-06-14 01:50:24.527522
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astunparse
    import textwrap

    x = ast.parse(textwrap.dedent('''
        {1: 1, 2: 2, 3: 3, None: 4, 5: 5}
        {1: 1, 2: 2, None: 3, None: 4, 5: 5}
        {None: 1, None: 2, None: 3, None: 4}
        {1: 1, None: None, None: None, None: None}
        {1: 1, 2: 2, None: [3, 4, 5]}
    '''))
    DictUnpackingTransformer().visit(x)
    print(astunparse.unparse(x))

# Generated at 2022-06-14 01:50:31.761953
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '''{1: 2, 1: 3, **{1: 4}}'''
    expected = '''_py_backwards_merge_dicts([{1: 2, 1: 3}], {1: 4})'''
    tree = ast.parse(source)
    tree = DictUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 01:50:40.270544
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .testutils import make_local_node, transform
    from .testutils import assert_same_source

    ex = make_local_node('{1: 2, **{}}')
    DictUnpackingTransformer(ex).visit(ex)
    assert_same_source(ex, '_py_backwards_merge_dicts([{1: 2}], {})')

    ex = make_local_node('{1: 2, **{3: 4}, **{5: 6}}')
    DictUnpackingTransformer(ex).visit(ex)
    assert_same_source(ex, '_py_backwards_merge_dicts([{1: 2}], {3: 4}, {5: 6})')

# Generated at 2022-06-14 01:50:51.458974
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse
    from .base import BaseNodeTest
    from .all import transform_all

    class Test(BaseNodeTest):
        target = DictUnpackingTransformer

        def test_one(self):
            input_ = '{1: 1, **{2: 2}}'
            expected = '_py_backwards_merge_dicts([{1: 1}], {2: 2})'
            assert self.transformed(input_) == expected

        def test_two(self):
            input_ = '{1: 1, 2: 2, **{3: 3}}'
            expected = '_py_backwards_merge_dicts([{1: 1, 2: 2}], {3: 3})'
            assert self.transformed(input_) == expected


# Generated at 2022-06-14 01:50:54.813240
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert DictUnpackingTransformer().visit(ast.parse("{1: 2, **{3: 4}}")) == ast.parse("_py_backwards_merge_dicts([{1: 2}], {3: 4})")

# Generated at 2022-06-14 01:51:06.099460
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    pairs1 = (
        (None, ast.Call(
            func=ast.Name(id='dict'),
            args=[ast.List(elts=[])],
            keywords=[])),
        (ast.Constant(value=1), ast.Constant(value=1)),
        (None, ast.Name(id='arg')),
        (ast.Constant(value=2), ast.Constant(value=2)),
        (None, ast.Name(id='kwarg')),
    )


# Generated at 2022-06-14 01:51:11.976579
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.unparse import unparse
    from .test_utils import transform

    source = '''
    {
        **{1: 1},
        **{2: 2},
        1: 1,
        **{3: 3}
    }
    '''

    expected = '''
    _py_backwards_merge_dicts([{}, {1: 1}, {2: 2}, {3: 3}])
    '''

    assert unparse(transform(DictUnpackingTransformer, source)) == expected

# Generated at 2022-06-14 01:51:23.131973
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.Dict(keys=[ast.Num(1), None, None, ast.Num(3)],
                    values=[ast.Name(id='a'),
                            ast.Call(func=ast.Name(id='dict'), args=[], keywords=[]),
                            ast.Dict(keys=[], values=[]),
                            ast.Num(4)])
    transformer = DictUnpackingTransformer()
    transformer.visit(node)
    assert transformer._tree_changed

# Generated at 2022-06-14 01:51:35.301326
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    input = """
my_dict = {1: 1, **dict_a, 2: 2}
my_dict2 = {1: 1, **dict_a, 2: 2, **dict_b}
"""

# Generated at 2022-06-14 01:51:45.350661
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = """
        def a(x):
            return {1: 2, **x, **y, 3: 4}
        """
    t = DictUnpackingTransformer()
    expected = """
        def a(x):
            return _py_backwards_merge_dicts(
                [{1: 2, **x, 3: 4}], y)
        """

    node = ast.parse(code)
    new_node = t.visit(node)
    assert expected == astunparse.unparse(new_node)

# Generated at 2022-06-14 01:51:54.434164
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from ast_toolbox import ast_visit


# Generated at 2022-06-14 01:52:04.857970
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    node = ast.parse('{1: 1, **{2: 2}, **{3: 3}, 4: 4}')
    result = transformer.visit(node)

# Generated at 2022-06-14 01:52:16.001508
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse

    node = merge_dicts.get_ast()
    node = ast.fix_missing_locations(node)
    # Dict([(Number(n=1), Number(n=1)), (Name(id='dict_a', ctx=Load()), Name(id='dict_a', ctx=Load()))])
    node = ast.fix_missing_locations(ast.Dict(
        keys=[ast.Num(n=1), ast.Name(id='dict_a', ctx=ast.Load())],
        values=[ast.Num(n=1), ast.Name(id='dict_a', ctx=ast.Load())]
    ))

    node = DictUnpackingTransformer().visit(node)
    print(unparse(node))
    # _py_backwards

# Generated at 2022-06-14 01:52:24.835216
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Tests if dict unpacking is converted correctly."""
    code = """
    {1: 1, **dict_a, 2: 3, **dict_b, 3: 4}
    """
    node = ast.parse(code)
    node_new = DictUnpackingTransformer().visit(node)

# Generated at 2022-06-14 01:52:40.183184
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    import ast
    import astor
    from prompt_toolkit.completion import Completion
    from .transformer import Transformer

    source = dedent('''
    foo = {1: 1, 2: 2, 3: 3, **bar, 4: 4, 5: 5, 6: 6}
    ''')

    tree = ast.parse(source)  # type: ignore
    transformer = Transformer()

    result = transformer(tree, max_suggestions=3)

    assert len(result) == 1
    assert result[0].new_source == dedent('''
        foo = _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}, {4: 4, 5: 5, 6: 6}], bar)
        ''')

# Generated at 2022-06-14 01:52:54.045140
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    module = ast.parse('{1: 1, 2: 2, **{"a": 1}, 3: 3, **{"b": 2}, 4: 4}')
    ast.fix_missing_locations(module)
    expected_module = ast.parse('''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    _py_backwards_merge_dicts([{1: 1, 2: 2}, {"a": 1}, {3: 3}, {"b": 2}, {4: 4}])
    ''')
    ast.fix_missing_locations(expected_module)
    transformer = DictUnpackingTransformer()
    transformed_module = transformer.visit(module)  # type:

# Generated at 2022-06-14 01:53:03.347126
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """
    Tests DictUnpackingTransformer.visit_Dict method.
    """
    from ..utils.test_utils import check_transformer_output


# Generated at 2022-06-14 01:53:14.144927
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from ..utils.testing import get_example_ast

    with get_example_ast('data/examples/dict_unpacking/example_1.py') as root:
        transformer = DictUnpackingTransformer()
        transformer.visit(root)
        result = astor.to_source(root)

    with get_example_ast('data/examples/dict_unpacking/example_1_fixed.py') as root:
        expected = astor.to_source(root)

    assert result == expected

# Generated at 2022-06-14 01:53:41.689025
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.fake import fake

    def check(code: str, expected: str) -> None:
        node = ast.parse(code)  # type: ignore
        transformer = DictUnpackingTransformer()
        actual = ast.dump(transformer.visit(node))
        assert actual == expected

    # - straight forward
    code = '{1: 1, 2: 2, **{3: 3}, **{4: 4}}'
    expected = '_py_backwards_merge_dicts([dict({1: 1, 2: 2}, **{3: 3}), dict({1: 1, 2: 2}, **{4: 4})])'
    check(code, expected)

    # - no keys
    code = '{**dict_a}'

# Generated at 2022-06-14 01:53:50.577642
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .testing_utils import assert_converted

    node = ast.parse("{a: 1, b: 2, **c}")

    transformer = DictUnpackingTransformer(node)
    node = transformer.visit(node)

    assert_converted(node, """
    import builtins as _builtins
    def _py_backwards_merge_dicts(dicts):
        result = _builtins.dict()
        for dict_ in dicts:
            result.update(dict_)
        return result
    _py_backwards_merge_dicts((_builtins.dict({a: 1, b: 2}), c))
    """)