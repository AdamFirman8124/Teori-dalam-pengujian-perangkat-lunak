

# Generated at 2022-06-14 01:44:12.238354
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor

    class TestableDictUnpackingTransformer(DictUnpackingTransformer):
        def _split_by_None(self, pairs: Iterable[Pair]) -> Splitted:
            return super()._split_by_None(pairs)

        def _prepare_splitted(self, splitted: Splitted) -> Splitted:
            return splitted

        def _merge_dicts(self, xs: Iterable[Union[ast.Call, ast.Dict]]) \
                -> ast.Call:
            return ast.Call(
                func=ast.Name(id='merge_dicts'),
                args=[ast.List(elts=list(xs))],
                keywords=[])


    t = TestableDictUnpackingTransformer()

# Generated at 2022-06-14 01:44:16.100350
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse('{{1: 1, **dict_a}: 1}')
    DictUnpackingTransformer().visit(node)
    assert '{1: 1, **dict_a}: 1' not in ast.dump(node)

# Generated at 2022-06-14 01:44:24.163283
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source_to_ast, ast_to_source

    def test_transform(before, after):
        transformer = DictUnpackingTransformer()
        root = source_to_ast(before)
        transformer.visit(root)
        after = ast_to_source(root)

        assert after == after, "Invalid transformation"

    test_transform("{*a, **b}", "_py_backwards_merge_dicts([a], b)")
    test_transform("{a: b, **c}", "_py_backwards_merge_dicts([{a: b}], c)")
    test_transform("{a: b, *c, **d}",
                   "_py_backwards_merge_dicts([{a: b}, c], d)")

# Generated at 2022-06-14 01:44:35.332694
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import check_transform

    # None key in dict:
    check_transform(DictUnpackingTransformer,
        """
        {'a': 1, 'b': 2, **d, 'c': 3}
        """,
        """
        _py_backwards_merge_dicts([{'a': 1, 'b': 2, 'c': 3}], d)
        """
    )

    # None key in dict and anonymous dicts:

# Generated at 2022-06-14 01:44:43.269939
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse("{'key': 1, **a}")
    DictUnpackingTransformer().visit(module)
    assert str(module) == \
        "from typing import List\n" \
        "\n" \
        "\n" \
        "def _py_backwards_merge_dicts(dicts: List[Dict]) -> Dict:\n" \
        "    result = {}\n" \
        "    for dict_ in dicts:\n" \
        "        result.update(dict_)\n" \
        "    return result\n\n" \
        "{'key': 1, **_py_backwards_merge_dicts([dict(key=1)], a)}\n" \
        "\n"

# Generated at 2022-06-14 01:44:52.371984
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    ast_ = ast3
    transformer = DictUnpackingTransformer()
    module = ast3.parse("""{1: 2, 3: 4, **{5: 6, 7: 8}}""")
    prepared = transformer.visit(module)
    desired_result = ast3.parse("""
    _py_backwards_merge_dicts([dict(1, 2, 3, 4)], {5: 6, 7: 8})
    """)
    assert ast3.dump(prepared) == ast3.dump(desired_result)


# Generated at 2022-06-14 01:44:57.715626
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node = ast.parse('''{1: 1}''', mode='eval')
    assert node
    dec = DictUnpackingTransformer()
    dec.visit(node)
    result = ast.dump(node, include_attributes=True)
    assert result == 'Module(body=[ImportFrom(module=\'builtins\', names=[alias(name=\'dict\', asname=None)], level=0, relative=False)], type_ignores=[])'

# Generated at 2022-06-14 01:45:06.172147
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_equivalent_code
    code = '''
        a = {1: 1, 2: 2, **dict_a, **{}, **dict_c, **dict_b, **dict_f, 5: 5}
    '''
    expected = '''
        _py_backwards_merge_dicts([{1: 1, 2: 2}, dict_a, {}, dict_c, dict_b, dict_f, {5: 5}])
    '''
    expected = '\n'.join(line.strip() for line in expected.split('\n'))
    code, _ = DictUnpackingTransformer(target=(3, 4)).transform(code)
    assert_equivalent_code(code, expected)

# Generated at 2022-06-14 01:45:16.109012
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse('''\

{1: 1, 2: 2, **dict_a}

{1: 1, 2: 2, **dict_a, **dict_b}

{1: 1, **{2: 2, **dict_a}}

{1: 1, **{2: 2, **dict_a, **dict_b}}

''')


# Generated at 2022-06-14 01:45:23.563433
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node = ast.parse("{**dict_a}")
    output = ast.dump(DictUnpackingTransformer().visit(node))
    expected = ast.dump(ast.Module([
        merge_dicts.get_body(),
        ast.Expr(value=ast.Call(
            func=ast.Name(id='_py_backwards_merge_dicts'),
            args=[ast.List(elts=[
                ast.Call(
                    func=ast.Name(id='dict'),
                    args=[ast.Name(id='dict_a')],
                    keywords=[])
            ])],
            keywords=[])),
    ]))

    assert output == expected


# Generated at 2022-06-14 01:45:37.223394
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.sample import common_dicts_samples
    from ..utils.iter import flatten
    from ..utils import test
    source = common_dicts_samples[9]['source']
    expected = common_dicts_samples[9]['expected']

    class Probe:
        x = 0

        def visit(self, func):
            self.x += 1
    probe = Probe()

    node = ast.parse(source)
    transformer = DictUnpackingTransformer()
    assert transformer._tree_changed is False
    result = transformer.visit(node)
    assert transformer._tree_changed is True
    probe.visit(transformer.visit_Dict)
    assert transformer._tree_changed is False
    assert probe.x == 1
    assert test.dump_code(result) == expected

# Generated at 2022-06-14 01:45:44.779212
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    sample_dict = ast.Dict(keys=[ast.Num(1), None],
                           values=[ast.Num(1), ast.Num(2)])
    actual = DictUnpackingTransformer().visit(sample_dict)
    expected = ast.Call(
        func=ast.Name(id='_py_backwards_merge_dicts'),
        args=[ast.List(elts=[
            ast.Dict(keys=[ast.Num(1)], values=[ast.Num(1)]),
            ast.Num(2)])],
        keywords=[])
    assert astor.to_source(actual).strip() == astor.to_source(expected).strip()



# Generated at 2022-06-14 01:45:45.760257
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    pass

# Generated at 2022-06-14 01:46:00.688890
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse
    func_def = parse("""
        def func(arg):
            return {1: 1, **arg}
        """)

    transformer = DictUnpackingTransformer()
    new_tree = transformer.visit(func_def)
    assert transformer._tree_changed is True

    # Check that the tree changed
    assert func_def is not new_tree
    assert len(new_tree.body) == 1

    # Check that function body changed
    func_def_body = func_def.body[0].body
    new_func_def_body = new_tree.body[0].body
    assert len(func_def_body) == 1
    assert len(new_func_def_body) == 2

    # Check that function docstring was added
    assert new_tree.body

# Generated at 2022-06-14 01:46:12.499192
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # We want to transform this code:
    # {k1: v1, **dict1, k2: v2, **dict2}
    # to this code:
    # _py_backwards_merge_dicts([{k1: v1, k2: v2}], dict1, dict2)

    # _py_backwards_merge_dicts is defined in snippet
    # (we don't want to test snippet)
    source = '\n'.join([
        'import typing',
        '',
        'def f(x: typing.Any) -> typing.Any:',
        '    return {1: 1, **{}, 2: x}',
    ])

# Generated at 2022-06-14 01:46:21.735439
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    input_code = '''
        {1: 1, 2: 2, 3: 3}
        {1: 1, None: 2, 3: 3}
        {1: 1, None: {2: 2}, 3: 3}
        {1: 1, 2: 2, None: {3: 3}}
        {1: 1, 2: 2, None: {3: 3, None: {4: 4}}, 5: 5}
        {None: {1: 1, None: {2: 2}}, 3: 3, None: [1, 2]}
        '''


# Generated at 2022-06-14 01:46:32.185281
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from ..utils.test import (
        assert_node_equal,
        get_visitor_output,
    )
    from .base import BaseNodeTransformer

    source = """
    @disable_dict_unpacking
    def foo(x: int, y: int, **kwargs: int) -> int:
        bar = {x: y, **kwargs}
        return 2
    """
    result = b"""
    @disable_dict_unpacking
    def foo(x: int, y: int, **kwargs: int) -> int:
        bar = {x: y, **kwargs}
        return 2
    """
    tree_before = ast.parse(source)

# Generated at 2022-06-14 01:46:44.262215
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from ..registry import registry

    class TestDictUnpackingTransformer(DictUnpackingTransformer):
        target = registry.python_versions_supported

    source = dedent('''\
        {1, **{2: 2, **{3: 3}, 4: 4}}
        ''')

    result = dedent('''\
        def _py_backwards_merge_dicts(dicts): pass
        _py_backwards_merge_dicts([{1}, {2: 2}, {3: 3, 4: 4}])
        ''')

    assert TestDictUnpackingTransformer(source).result == result

# Generated at 2022-06-14 01:46:52.197263
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ast
    import astunparse
    code = "foo = {1: 'a', **dict_a, 2: 'b', 3: 'c', **dict_b, 4: 'd', 5: 'e'}"
    ast_ = ast.parse(code)
    target = ast.Dict(keys=[ast.Num(1), None, ast.Num(2), ast.Num(3), None,
                            ast.Num(4), ast.Num(5)],
                      values=[ast.Str('a'), ast.Name(id='dict_a', ctx=ast.Load()), ast.Str('b'),
                              ast.Str('c'), ast.Name(id='dict_b', ctx=ast.Load()), ast.Str('d'),
                              ast.Str('e')],
                      )

# Generated at 2022-06-14 01:47:05.849787
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent

    from typed_ast import ast3 as ast

    from ..utils.source import Source
    from . import ast_transformer

    source = Source('py')

    source.put_text(r"""
        a = {1: 2, **a, 3: 4, }
    """)

    expected_output = dedent(r"""
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result


        a = _py_backwards_merge_dicts([{1: 2}], a, {3: 4})
    """)

    expected_ast = ast.parse(expected_output)  # type: ignore

# Generated at 2022-06-14 01:47:24.830328
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .. import compile_isolated
    from ..utils.fake import FakeTraced

    def test():
        d0 = {1: 2, 3: 4}
        d1 = {}
        d2 = {5: 6}
        d3 = {1: 100}
        x = {1: 1, **d0}
        y = {**d0, **d1, **d2}
        z = {1: 1, **d0, **d2, **d3}
        return x, y, z

    compiled = compile_isolated(test, [])

    assert compiled.func_ir.arg_counts == (0, 0)
    compiled_lines, _ = compiled.func_ir.lines, compiled.func_ir.arg_names

    fake = FakeTraced()  # type: ignore
    retval = compiled

# Generated at 2022-06-14 01:47:35.190359
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class DictUnpackingTransformerMock(object):
        def _split_by_None(self, pairs):
            pairs_list = list(pairs)
            len_pairs = len(pairs_list)
            return [pairs_list[:2], pairs_list[2:len_pairs-2], pairs_list[len_pairs-2:]]

        def _prepare_splitted(self, splitted):
            return splitted

        def _merge_dicts(self, xs):
            xs_list = list(xs)
            return ast.Call(func=ast.Name(id='merge_dicts'), args=[xs_list[0], xs_list[1], xs_list[2]], keywords=[])
        

# Generated at 2022-06-14 01:47:43.470293
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent

    from ..utils.python_transformer import Python3Transformer

    class TestTransformer(Python3Transformer):
        METHOD_TO_TEST = 'visit_Dict'

        @classmethod
        def get_body(cls):
            return dedent(inspect.getsource(DictUnpackingTransformer))


# Generated at 2022-06-14 01:47:51.412635
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert ast.dump(DictUnpackingTransformer().visit(ast.parse("{1: 1}"))) \
        == "Module(body=[Expr(value=Dict(keys=[Num(n=1)], values=[Num(n=1)]))])"

# Generated at 2022-06-14 01:47:58.163174
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = ast.parse(
        """{1: 2, **{3: 4}}"""
    )

    expected = ast.parse(
        """
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
        _py_backwards_merge_dicts([{1: 2}], {3: 4})
        """
    )

    transformer = DictUnpackingTransformer()
    result = transformer.visit(source)
    compare_ast(result, expected)

# Generated at 2022-06-14 01:48:02.057496
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    node = ast.parse('''{1: 1, 2: 2}''')
    new_node = transformer.visit(node)
    assert ast.dump(node) == ast.dump(new_node)



# Generated at 2022-06-14 01:48:09.656633
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_transformer import compile_and_run
    from .test_transformer import assert_tree_equals

    script = '''
{**dict_a, 1: 1, **dict_b}
    '''
    res_script = '''
_py_backwards_merge_dicts([dict(1=1)], dict_a, dict_b)
    '''
    tree = compile_and_run(script)
    expected_tree = compile_and_run(res_script)
    assert_tree_equals(tree, expected_tree)

# Generated at 2022-06-14 01:48:20.644454
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    pairs = [
        (ast.Num(n=1), ast.Str(s='1')),
        (None, ast.Call(
            func=ast.Name(id='dict'),
            args=[ast.List(elts=[])],
            keywords=[])),
        (ast.Num(n=2), ast.Str(s='2')),
        (None, ast.Name(id='dict_b')),
        (None, ast.Call(
            func=ast.Name(id='dict'),
            args=[ast.List(elts=[])],
            keywords=[])),
        (ast.Num(n=3), ast.Str(s='3')),
    ]

# Generated at 2022-06-14 01:48:30.552343
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    source = """\
{1: 1, **{1: 1}, 2: 2}
{**{1: 1}, 2: 2}
{1: 1, **{1: 1}, **{1: 1}, **{1: 1}}
"""
    expected = """\
_py_backwards_merge_dicts([dict({1: 1}), {2: 2}], {1: 1})
_py_backwards_merge_dicts([{2: 2}], {1: 1})
_py_backwards_merge_dicts([_py_backwards_merge_dicts([dict({1: 1})], {1: 1}), {1: 1}], {1: 1})
"""

    tree = ast.parse(source)

# Generated at 2022-06-14 01:48:35.381663
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse(
        '{1: 1, 2: 2, **a, 3: 3, 4: 4, **b}', mode='exec').body[0].value
    assert isinstance(node, ast.Dict)
    result = DictUnpackingTransformer().visit(node)
    assert isinstance(result, ast.Call)



# Generated at 2022-06-14 01:48:50.324574
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import dump
    from .utils import roundtrip
    from .test_BaseNodeTransformer import BaseNodeTransformerImpl

    code = '{a: 0, b: 1, **x, **y, c: 2}'
    ast_tree = roundtrip(code)

    class DUT(BaseNodeTransformerImpl, DictUnpackingTransformer):
        pass

    transformer = DUT()
    new_ast_tree = transformer.visit(ast_tree)
    new_code = dump(new_ast_tree)

    print(new_code)
    print(code)


# Generated at 2022-06-14 01:48:58.499407
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    expected_source = '''\
_py_backwards_merge_dicts([{}, {1: 1}], {1: 2, **dict_a})
'''
    source = '''\
_py_backwards_merge_dicts([{}, {1: 1}], {1: 2, **dict_a})
'''
    ast_ = ast.parse(source)
    DictUnpackingTransformer().visit(ast_)
    assert expected_source == ast_.body[0].body[0].value.args[1].value.args[1].value.args[1].value.args[0].value.value.func.id  # type ignore



# Generated at 2022-06-14 01:49:06.328059
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..parser import PythonParser
    from ..unparser import PythonUnparser

    source1 = "{1: 1, **dict_a}"
    source2 = "{1: 1, 2: 2, **dict_a, **dict_b, 3: 3}"
    source3 = "{1: 1, 2: 2, 3: 3, 4: 4 if True else 5, 6: 6 if False else 7}"
    source4 = "{1: 1, **dict_a, 2: 2, **dict_b, 3: 3}"
    source5 = "{**dict_a, 1: 1}"
    source6 = "{1: 1, 2: 2, 3: 3, }"
    source7 = "{1: 1, 2: 2, 3: {}.attribute, }"

# Generated at 2022-06-14 01:49:17.888801
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .main import compile_to_ast as c
    from ..utils.dump_utils import dump_ast_to_lines
    from ..utils.tree import print_tree_as_lines

    assert dump_ast_to_lines(c('{1: 1}', transformers=[DictUnpackingTransformer])) == \
           dump_ast_to_lines(c('{1: 1}'))
    assert dump_ast_to_lines(c('{1: 1, **dict_a}', transformers=[DictUnpackingTransformer])) == \
           dump_ast_to_lines(c('_py_backwards_merge_dicts([{1: 1}], dict_a)'))

# Generated at 2022-06-14 01:49:21.265353
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    d = ast.Dict(keys=[None, ast.Str(s=""), None])
    result = DictUnpackingTransformer().visit_Dict(d)
    assert isinstance(result, ast.Call)

# Generated at 2022-06-14 01:49:30.302692
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_parser import parse_ast
    from .base import NodeTransformerTestCase

    class Test(NodeTransformerTestCase):

        transformer = DictUnpackingTransformer()
        filename = __file__

# Generated at 2022-06-14 01:49:40.655842
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from ..utils.source import source_to_ast

    template = dedent("""
        {
            {
                {}, {}
            }, 
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {}
        }
    """)
    n = 10


# Generated at 2022-06-14 01:49:49.961552
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .base import PythonNodeTransformer
    from ..utils.source import source_to_ast

    source = '{1: 1, **dict_a}'
    test_node = source_to_ast(source)
    assert isinstance(test_node, ast.Dict)

    expected = '_py_backwards_merge_dicts(dicts=[dict([(1, 1)]), dict_a])'
    PythonNodeTransformer.run_test(
        transformer_class=DictUnpackingTransformer,
        source=source,
        expected=expected,
        test_node_class=ast.Dict)



# Generated at 2022-06-14 01:50:03.415541
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ...utils.python_ast import parse
    module = parse('{1: 1, **dict_a}')
    DictUnpackingTransformer().visit_Module(module)
    assert module.body[0] == merge_dicts.get_body()
    assert module.body[1] == ast.Expr(
        value=ast.Call(
            func=ast.Name(id='_py_backwards_merge_dicts'),
            args=[ast.List(elts=[
                ast.Call(
                    func=ast.Name(id='dict'),
                    args=[ast.Dict(
                        keys=[ast.Num(n=1)],
                        values=[ast.Num(n=1)])],
                    keywords=[]),
                ast.Name(id='dict_a')])],
            keywords=[]))

# Generated at 2022-06-14 01:50:13.321993
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.mock_node import MockNode

    dict_a = MockNode()
    dict_b = MockNode()
    dict_c = MockNode()
    dict_d = MockNode()
    dict_e = MockNode()
    dict_f = MockNode()


# Generated at 2022-06-14 01:50:39.151287
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:50:49.682218
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from typed_ast import ast3 as ast

    expected = dedent('''\
        def f():
            return _py_backwards_merge_dicts([{'a': 1}], {'b': 2}, {'c': 3})
    ''')
    node = ast.parse(dedent('''\
        def f():
            return {'a': 1, 'b': 2, **{'c': 3}}
    '''))

    DictUnpackingTransformer().visit(node)
    expected = ast.parse(expected)
    assert ast.dump(expected, include_attributes=False) == \
        ast.dump(node, include_attributes=False)


# Generated at 2022-06-14 01:50:58.293736
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    module = ast.parse("{1: 1, **dict_a}")
    DictUnpackingTransformer().generic_visit(module)
    to_string = ast.dump(module)

# Generated at 2022-06-14 01:51:06.889372
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def test_case(input, expected):
        input = ast.parse(input)
        expected = ast.parse(expected)
        actual = DictUnpackingTransformer().visit(input)
        assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 01:51:15.481453
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:51:22.710268
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transpiler import Transpiler
    from ..utils.dump import dump

    node = ast.parse(
"""
{1, 2, 3, **{4, 5, 6}}
""")
    transpiler = Transpiler(transformer_classes=[DictUnpackingTransformer])
    transpiler.visit(node)

    assert dump(node) == \
"""_py_backwards_merge_dicts([{1, 2, 3}], {4, 5, 6})
"""

# Generated at 2022-06-14 01:51:32.042191
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_ast.ast3 as ast
    from typed_ast.ast3 import Dict, Name, Load, Call, List, Num

    pairs = [(Num(1), Num(1)), (None, Name(id='dict_a')), (Num(2), Num(2))]
    node = Dict(keys=[key for key, _ in pairs],
                values=[value for _, value in pairs],
                ctx=Load())

# Generated at 2022-06-14 01:51:36.901705
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import logging
    import astor  # type: ignore
    from ..utils.logger import Level

    logging.basicConfig(level=Level.ERROR)

    class MyNodeTransformer(ast.NodeTransformer):  # type: ignore
        def __init__(self):
            self._public_tree_changed = False

        @property
        def tree_changed(self):
            return self._public_tree_changed

        def generic_visit(self, node):
            if isinstance(node, ast.Dict):
                self._public_tree_changed = True
                if isinstance(node.keys[0], ast.Name):
                    return ast.Dict(keys=node.keys[::-1], values=node.values)
                else:
                    return [node.keys, node.values]
            return super().generic_visit

# Generated at 2022-06-14 01:51:44.391109
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from .snippets import expr_to_ast

    in_ = dedent("""\
        {1: 1, **dict_a}
        """)

    out = dedent("""\
        _py_backwards_merge_dicts([{1: 1}], dict_a})
        """)

    assert expr_to_ast(in_) == expr_to_ast(out)

# Generated at 2022-06-14 01:51:52.137355
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.tests import check_visitor
    from ..utils.tree import parse
    from ..utils.codegen import to_source
    from past.builtins import exec
    from pprint import pprint
    from ..utils.tests import assert_equal

    result = check_visitor(DictUnpackingTransformer, dict(a=1, **{'b':2}))
    assert_equal(to_source(result).strip(), '_py_backwards_merge_dicts([dict(a=1)], {\'b\': 2})')


# Generated at 2022-06-14 01:52:39.895464
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astpretty import pprint
    from ..utils.ast3 import parse

    source = """
    {1: 1, 2: 2, None: dict_a, 'a': 'a'} 
    """
    expected = """
    _py_backwards_merge_dicts([{1: 1, 2: 2}, dict_a, {'a': 'a'}])
    """
    result = DictUnpackingTransformer().visit(parse(source))  # type: ignore
    _expected_ast = parse(expected)  # type: ignore
    try:
        assert ast.dump(result) == ast.dump(_expected_ast)
    except AssertionError:
        print('In:')
        pprint(parse(source))
        print('Expected:')
        pprint(_expected_ast)
        print

# Generated at 2022-06-14 01:52:46.159851
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source

    transformed = source(DictUnpackingTransformer, """
        {1: 1, **dict_a}
    """)

    assert transformed == """
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """



# Generated at 2022-06-14 01:52:58.539377
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse as _parse
    from ..utils.tree import print_tree as _print
    from ..utils.transform import transform as _transform
    from ..utils.hash import hash as _hash
    from .test_case import TestCase as _TestCase
    from .test_case import _TestCaseSuit

    cases = _TestCaseSuit()

    @cases.add
    class _(cases._TestCase):
        code = """
            {1: 1, **dict_a}
        """
        result_code = """
            _py_backwards_merge_dicts([dict({1: 1})], dict_a)
        """


# Generated at 2022-06-14 01:53:10.395110
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source
    from ..treetransformer import TreeTransformer
    
    inputs = (
        {"**x": "dict(x)"},
        {"1: 2, **x": """dict(_py_backwards_merge_dicts([{1: 2}], x))"""},
        {"1: 2, **x, 3: 4": """dict(_py_backwards_merge_dicts([{1: 2}], x, {3: 4}))"""},
        {"1: 2, **x, 3: 4, **x": """dict(_py_backwards_merge_dicts([{1: 2}], x, {3: 4}, x))"""},
    )

# Generated at 2022-06-14 01:53:17.065343
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    input = ast.parse('{1: 1, **dict_a, 2: 2, **dict_b}')
    expected = ast.parse('''\
_py_backwards_merge_dicts(
    [{1: 1}, dict_a, {2: 2}],
    dict_b)''')

    transformer = DictUnpackingTransformer()
    actual = transformer.visit(input)
    assert ast.dump(actual) == ast.dump(expected)

# Generated at 2022-06-14 01:53:21.795503
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '{1: 2, **{3: 4}}'
    expected = '_py_backwards_merge_dicts([{1: 2}], {3: 4})'
    tree = ast.parse(code)
    transformer = DictUnpackingTransformer()
    new_tree = transformer.visit(tree)
    assert ast.dump(new_tree, include_attributes=False,
                    annotate_fields=False) == expected

# Generated at 2022-06-14 01:53:27.148530
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    t = DictUnpackingTransformer()
    assert_compile_success(t, '{1: 1, **dict_a}')
    assert_compile_success(t, '{1: 1, **dict_a, 3: 3, **dict_b}')
    assert_compile_success(t, '{1: 1, **dict_a, 3: 3, **dict_b, 5: 5}')

# Generated at 2022-06-14 01:53:38.909348
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typing import Any
    from ..testing import assert_unchanged
    from ..testing import assert_changed_ast
    from ..testing import assert_changed_with
    from ..testing import make_callable
    from ..testing import assert_equal_code

    call_dict = make_callable(DictUnpackingTransformer)  # type: ignore

    assert_unchanged(call_dict, '''
        a = {}
    ''')

    assert_changed_ast(call_dict, '''
        a = {1: 2, **{3: 4}}
    ''', '''
        a = {1: 2, **_py_backwards_merge_dicts([], {3: 4})}
    ''')


# Generated at 2022-06-14 01:53:44.860884
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from .. import typed_astunparse
    from .unpacking import transform
    input = '''
    {a: b, None: 1, c: d}
    '''
    expected = '''
    _py_backwards_merge_dicts([
    {a: b,
     c: d
    }], 1)
    '''
    tree = ast3.parse(input)
    tree = transform(tree, [DictUnpackingTransformer()], {}, 'file.py')
    output = typed_astunparse.unparse(tree).strip()
    assert output == expected.strip()

# Generated at 2022-06-14 01:53:52.142700
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse

    code = '''
{1: 1, 2: 2, **a, 3: 3, **b, 4: 4, 5: 5}
'''

    expected = '''
_py_backwards_merge_dicts([{1: 1, 2: 2}, a, {3: 3}, b, {4: 4, 5: 5}])
'''

    module = ast.parse(code)
    transformer = DictUnpackingTransformer()
    result = transformer.visit(module)
    assert unparse(result) == expected