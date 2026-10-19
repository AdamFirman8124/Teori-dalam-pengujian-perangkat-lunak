

# Generated at 2022-06-14 01:44:13.797728
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse(
        """
        {'a': 'b', 'c': 'd', **{'e': 'f'}}
        """)

    class FakeMigrator(DictUnpackingTransformer):
        _tree_changed = False

    FakeMigrator().visit(tree)
    assert FakeMigrator._tree_changed is True


# Generated at 2022-06-14 01:44:19.202003
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class _NodeTransformer(DictUnpackingTransformer):
        def __init__(self, tree):
            self.tree = tree
            self.tree_changed = False
            self._tree_changed = False

    transformer = _NodeTransformer(ast.parse('{1:1, **{2:2, **{3:3}}}'))
    result = transformer.visit(transformer.tree)
    assert transformer.tree_changed == True
    assert isinstance(result, ast.Call)

# Generated at 2022-06-14 01:44:25.483575
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astunparse

    code = '''
    def f():
        a = {
            'a': 1,
            **b,
            'c': 6,
            **d,
            'e': 5,
            'f': 6,
            **g,
            'h': 3,
            **j
        }
    '''
    lineno = 3
    col_offset = 4

# Generated at 2022-06-14 01:44:32.882743
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from .test_helpers import assert_converted
    

# Generated at 2022-06-14 01:44:42.347602
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 01:44:53.872971
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse('{1: 1, **{2: 2}}')
    DictUnpackingTransformer().visit(tree)
    assert len(tree.body) == 2

# Generated at 2022-06-14 01:44:58.560442
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse("{1: 1, **dict_a}")
    transformer = DictUnpackingTransformer()
    transformer.visit(tree)
    name_call_a = ast.Name(id="dict_a")
    dct_1 = ast.Dict(keys=[ast.Num(1)], values=[ast.Num(1)])
    list_ = ast.List(elts=[dct_1, name_call_a])
    call = ast.Call(
        func=ast.Name(id="_py_backwards_merge_dicts"),
        args=[list_],
        keywords=[])
    assert ast.dump(tree) == ast.dump(call)

# Generated at 2022-06-14 01:45:06.423514
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    source = """\
    {1: 1, 2: 2, **{3: 3, **{4: 4}}}
    """
    module = ast.parse(source)
    expected = """\
    def _py_backwards_merge_dicts(dicts): return _py_backwards_merge_dicts([dict(zip((1, 2), (1, 2)))], {3: 3}, {4: 4})
    """
    assert expected == ast.unparse(DictUnpackingTransformer().visit(module))


# Generated at 2022-06-14 01:45:13.203043
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..ast_utils import get_ast
    from .base import BaseNodeTransformerTestCase

    class TestCase(BaseNodeTransformerTestCase):
        def test_for_dict_with_no_unpacking(self):
            node = get_ast("{1: 1}")
            self.check(node, node)

        def test_for_dict_with_unpacking(self):
            node = get_ast("{1: 1, **a}")
            self.check(node, "dict({1: 1}, **a)")

        def test_for_dict_with_multiple_unpacking(self):
            node = get_ast("{1: 1, **a, 2: 2, **b}")

# Generated at 2022-06-14 01:45:22.230480
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    transformer = DictUnpackingTransformer()
    code = compile(dedent("""
        def foo():
            return {1: 1, **{2: 2}}
    """), '<test>', 'exec')
    node = ast.parse(code)
    assert transformer.visit(node) == compile(dedent("""
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result


        def foo():
            return _py_backwards_merge_dicts([{1: 1}], {2: 2})
    """), '<test>', 'exec')


# Generated at 2022-06-14 01:45:35.063523
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import as_ast_node
    from typed_ast import ast3
    from ..transforms import DictUnpackingTransformer
    from ..transforms.class_decorator import ClassDecoratorTransformer

    DICT_TEMPLATE = '''
        def f(a, b, c, d):
            return {a: a, b: b, c: c,
                    d: d,
                    **{a: a, b: b, c: c},
                    **{d: d},
                    **e, **f, **g
                    }
    '''

    AST = as_ast_node(CLASS_DECORATOR_TEMPLATE.format(DICT_TEMPLATE))
    assert isinstance(AST, ast3.ClassDef)

    ClassDecoratorTransformer().visit(AST)


# Generated at 2022-06-14 01:45:45.475736
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    expected = ast.parse('def _py_backwards_merge_dicts(dicts):\n    result = {}\n    for dict_ in dicts:\n        result.update(dict_)\n    return result\n_py_backwards_merge_dicts([{1: 1}], dict_a)')
    expected = expected.body[-1]

    actual = ast.parse('{1: 1, **dict_a}')
    actual = actual.body[0]

    transformer = DictUnpackingTransformer()
    actual = transformer.visit(actual)

    assert isinstance(actual, ast.Call)
    assert actual.func.id == expected.func.id
    assert len(actual.args) == len(expected.args)
    assert len(actual.keywords) == len(expected.keywords)

# Generated at 2022-06-14 01:46:00.608869
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse

    test_cases = """
        {1: 1, **dict_a, 2: 2}
        {1: 1, **dict_a, 2: 2, **dict_b}
        {**dict_a, **dict_b}
        {1: 1, **dict_a}
        {1: 1, **dict_a, **dict_b}
    """.split("\n")


# Generated at 2022-06-14 01:46:10.747223
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    transformer = DictUnpackingTransformer()
    tree = ast.parse("""\
{1: 2, None: 4, 5: 6, None: 8, None: 10}
{None: 4, 5: 6, None: 8, None: 10}
{1: 2, 5: 6}
{1: 2, None: None, 5: 6}
{1: 2, None: None}
""")

# Generated at 2022-06-14 01:46:20.033441
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tf = DictUnpackingTransformer()
    tree = ast.parse(
        '{\n'
        '    a: 1,\n'
        '    None: [],\n'
        '    b: 2,\n'
        '    None: 1,\n'
        '    c: 3\n'
        '}')
    tf.visit(tree)
    assert str(tree) == (
        '_py_backwards_merge_dicts([\n'
        'dict({\n'
        'a: 1,\n'
        'b: 2,\n'
        'c: 3\n'
        '}), ], [\n'
        '])'
    )

# Generated at 2022-06-14 01:46:31.423528
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse, dump
    from .test_utils import assert_equal_code


# Generated at 2022-06-14 01:46:42.646605
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .unpacking_transformer import UnpackingTransformer
    from ..utils import to_str
    code = '''
{'a': 1, **dict_a, 'b': 2, **dict_b}
'''
    expected = '''
_py_backwards_merge_dicts(
    [dict(['a', 'b'], [1, 2]), dict_a, dict_b])
'''
    tree = ast.parse(code)
    UnpackingTransformer().visit(tree)
    DictUnpackingTransformer().visit(tree)
    assert to_str(tree) == expected

# Generated at 2022-06-14 01:46:51.147584
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    dict_unpacking_transformer = DictUnpackingTransformer()
    assert ast.dump(
        dict_unpacking_transformer.visit(  # type: ignore
            ast.parse(
                '{1: 3, None: {}, 5: 3, None: {}, 6: 9}'))) == \
        ast.dump(
            ast.parse(
                '_py_backwards_merge_dicts([{1: 3, 5: 3}], {}, '
                '_py_backwards_merge_dicts([{}], {6: 9}))'))



# Generated at 2022-06-14 01:47:04.620443
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import ast
    import astor

    class CustomNode(object):
        def get_body(self):
            return ast.Module([], [], [])

    module = CustomNode()

    class DictUnpackingTransformer(object):
        def _insert_at(self, x, y, z):
            return None

        def visit_Module(self, node):
            self._insert_at(0, node, module.get_body())
            return ast.Module()



    d = DictUnpackingTransformer()
    d.visit_Module(None)
    print(astor.to_source(module.get_body()))
    assert False

if __name__ == '__main__':
    test_DictUnpackingTransformer_visit_Module()

# Generated at 2022-06-14 01:47:13.143231
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    a = ast3.parse('{1: 2, 3: 4, **{5: 6}, **{7: 8}}')
    assert dump_ast(a) == 'Module(body=[Dict(keys=[Num(n=1), Num(n=3), None, None], values=[Num(n=2), Num(n=4), Dict(keys=[Num(n=5)], values=[Num(n=6)]), Dict(keys=[Num(n=7)], values=[Num(n=8))])])'

    DictUnpackingTransformer().visit(a)

# Generated at 2022-06-14 01:47:23.844699
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    program = ast.Module([merge_dicts.get_body()])
    assert ast.Module(body=[]) == DictUnpackingTransformer().visit(program)



# Generated at 2022-06-14 01:47:34.505752
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from test_utils import dedent
    code = dedent('''
    class myclass:
        def mymethod(self, a, **kwargs):
            pass

        def __init__(self, **kwargs):
            pass
    ''')
    expected_code = dedent('''
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    class myclass:
        def mymethod(self, a, **kwargs):
            pass

        def __init__(self, **kwargs):
            pass
    ''')
    expected_tree = ast.fix_missing_locations(ast.parse(expected_code))
    expected_code = expected_code.strip()
    tree

# Generated at 2022-06-14 01:47:41.561328
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    mod = ast.parse('{1: 1, 2: 2, 3: 3}')  # type: ignore
    refactored = DictUnpackingTransformer().visit(mod)  # type: ignore

    assert len(refactored.body) == 3
    assert isinstance(refactored.body[0], ast.FunctionDef)
    assert isinstance(refactored.body[1], ast.Expr)
    assert isinstance(refactored.body[2], ast.Dict)


# Generated at 2022-06-14 01:47:50.173605
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transform import ast_to_src

    class Dummy(ast.AST):
        pass

    t = DictUnpackingTransformer()

    kwargs = {
        'arg1': 1,
        **Dummy(),
        'arg2': 2,
        **Dummy(),
        'arg3': [3, 3],
        **Dummy(),
        'arg4': {4, 4},
        **Dummy(),
    }

    node = t.visit(ast.Call(func=ast.Name(id='foo'),
                            args=[],
                            keywords=[ast.keyword(arg=None,
                                                   value=kwargs)]))
    src = ast_to_src(node)

# Generated at 2022-06-14 01:47:59.417756
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .. import run
    from ..factories import make_snippet
    from .base import NodeTransformer


# Generated at 2022-06-14 01:48:10.045223
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def test(source: str, expected: str) -> None:
        node = ast.parse(source)
        result = DictUnpackingTransformer().visit(node)
        assert ast.dump(ast.fix_missing_locations(result)) == expected
        
    test('{**{1: 2}, **{1: 1}, 2: None, 3: 3}',
         '_py_backwards_merge_dicts([{3: 3, 2: None}], {1: 2}, {1: 1})')
    test('{**dict_a, **dict_b, **dict_c, **{1: 1, 2:  2}}',
         '_py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a, dict_b, dict_c)')

# Generated at 2022-06-14 01:48:17.669460
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = """
    a = {1: 1, **dict_a, 2: 2, **{3: 3}}
    """
    target = """
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    a = _py_backwards_merge_dicts([{1: 1, 2: 2}, dict_a, {3: 3}])
    """
    tr = DictUnpackingTransformer()
    assert tr.run(source) == target

# Generated at 2022-06-14 01:48:23.052517
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = '{1: 1, None: 2, 3: 4}'
    expected = '_py_backwards_merge_dicts([{1: 1, 3: 4}], 2)'
    
    from ..tests.test_transformer import _assert_conversion
    _assert_conversion(DictUnpackingTransformer, source, expected)

# Generated at 2022-06-14 01:48:32.624142
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    # None in keys
    node = ast.Dict(keys=[ast.Num(n=1), None, ast.Name(id='dict_a', ctx=ast.Load())],
                    values=[ast.Num(n=1), ast.Dict(keys=[], values=[]), ast.Name(id='dict_b', ctx=ast.Load())])

# Generated at 2022-06-14 01:48:43.275932
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from ..utils.transformer import module_from_str
    from ..utils.ast import ast_equal, dump_ast
    source_code = """\
    x = {1: 1, 2: 2, 3: 3, **{True: 4, 5: 5}}
    """
    expected_code = """\
    x = _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], {True: 4, 5: 5})
    """
    ast_module = module_from_str(source_code, __name__)
    expected_module = module_from_str(expected_code, __name__)
    transformer = DictUnpackingTransformer()
    transformer.visit(ast_module)

# Generated at 2022-06-14 01:49:11.169793
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.typing import Dict, List

    import ast
    import logging
    import unittest

    from typed_astunparse import unparse as unparse_typed

    from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer

    logger = logging.getLogger(__name__)

    class TestCase(unittest.TestCase):
        def _test_case(self, before, after):
            before_typed = ast.parse(before)
            after_typed = ast.parse(after)

            transformer = DictUnpackingTransformer()
            result = transformer.visit(before_typed)
            self.assertEqual(unparse_typed(result), unparse_typed(after_typed))

# Generated at 2022-06-14 01:49:20.695153
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from . import analyze

    source = """
{a: 1, **d1}
{a: 1, b: 2, **d1, **d2}
{}
{**d1}
    """

    tests = [
        "({a: 1}).update(d1)",
        "({a: 1, b: 2}).update(d1).update(d2)",
        "{}",
        "dict(d1)",
    ]

    for src, expected in zip(source.splitlines()[1:], tests):
        tree = analyze(src)
        t = DictUnpackingTransformer()
        t.visit(tree)
        _, r = t.as_string()
        assert r.strip() == expected.strip()

# Generated at 2022-06-14 01:49:30.193919
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from textwrap import dedent
    from astunparse import unparse
    from ..testing.utils import get_ast

    assert_transform(
        DictUnpackingTransformer,
        {
            'before': dedent('''
            {
                1: 2, 3: 4
            };
            '''),
            'after': dedent('''
            _py_backwards_merge_dicts([{1: 2, 3: 4}]);
            '''),
        },
        with_format=True)


# Generated at 2022-06-14 01:49:37.413770
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .test_utils import roundtrip
    from ..utils.ast_helpers import dump
    before = ast.parse('''
    {1: 1, 2: 2, **x, **y}  # comment
    ''')
    after = ast.parse('''
    _py_backwards_merge_dicts([{1: 1, 2: 2}], x, y)  # comment
    ''')

    assert dump(after) == dump(roundtrip(before))



# Generated at 2022-06-14 01:49:44.705921
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor

    tree = ast.parse("""{1: 1, **dict_a}""")
    expected_tree = ast.parse("""_py_backwards_merge_dicts([{1: 1}], dict_a)""")
    transformer = DictUnpackingTransformer()
    transformer.visit(tree)
    assert astor.to_source(tree) == astor.to_source(expected_tree)

# Generated at 2022-06-14 01:49:50.328667
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    
    inp = """
        {1: 1, **dict_a}
    """
    res = """
        _py_backwards_merge_dicts([{1: 1}], dict_a})
    """
    
    assert astor.to_source(DictUnpackingTransformer().visit(ast.parse(inp))) \
           == res


# Generated at 2022-06-14 01:50:03.454839
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from .test_utils import roundtrip


# Generated at 2022-06-14 01:50:09.905717
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node = ast.parse('def foo(bar):')
    DictUnpackingTransformer().visit(node)
    assert str(node) == dedent('''\
    def foo(bar):
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
    ''')



# Generated at 2022-06-14 01:50:18.903013
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.tree_compare import tree_compare
    from typed_ast.ast3 import Dict, Name
    transformer = DictUnpackingTransformer()

    inp = Dict(keys=[None, None, 1, None, Name(id='a')],
               values=[Name(id='dict_a'),
                       Name(id='dict_b'),
                       2,
                       Name(id='dict_c'),
                       Name(id='b')])

    exp = Dict(keys=[1, Name(id='a')],
               values=[2, Name(id='b')])

    # merge_dicts module
    exp.body.insert(0, merge_dicts.get_body()[0])

    # call to _py_backwards_merge_dicts

# Generated at 2022-06-14 01:50:26.424758
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from unittest.mock import patch
    from ..utils.tree_compare import ast_equals

    from typed_ast import ast3 as ast
    
    from .dict_unpacking import DictUnpackingTransformer

    with patch('typed_astunparse.unparse', return_value='unparsed'):
        assert ast_equals(
            {'a': 1, 'b': 2, **{'c': 3}},
            DictUnpackingTransformer().visit(
                ast.parse('''
                {'a': 1, 'b': 2, **{'c': 3}}
                ''')))

# Generated at 2022-06-14 01:51:10.212479
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def test_method(self, node):
        return self.visit_Dict(node)

    transformer = DictUnpackingTransformer()
    assert transformer.visit_Dict(ast.Dict(keys=[None], values=[ast.Name(id='None')])) == ast.Call(
        func=ast.Name(id='_py_backwards_merge_dicts'),
        args=[ast.List(elts=[ast.Dict(keys=[], values=[])])],
        keywords=[])


# Generated at 2022-06-14 01:51:22.478326
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    from typed_ast.ast3 import Dict, Tuple, Name, Load, Constant
    node = Dict(keys=[
        Name(id='arg_b', ctx=Load()),
        Name(id='arg_c', ctx=Load()),
        Constant(value=None),
        Name(id='arg_a', ctx=Load())
    ], values=[
        Name(id='val_b', ctx=Load()),
        Name(id='val_c', ctx=Load()),
        Name(id='arg_d', ctx=Load()),
        Name(id='val_a', ctx=Load())
    ])


# Generated at 2022-06-14 01:51:29.980403
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree1 = ast.parse(
        'def foo(dict_a):\n    _1 = {1: 1, **dict_a}')  # type: ast.Module
    tree2 = ast.parse(
        'def foo(dict_a):\n    _1 = _py_backwards_merge_dicts('
        '[{1: 1}], dict_a)\n')  # type: ast.Module
    transformer = DictUnpackingTransformer()
    transformer.visit(tree1)
    assert str(tree1) == str(tree2)
    print(ast.dump(tree1))

# Generated at 2022-06-14 01:51:33.272915
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    tree = ast.parse('{1: 1, **dict_a}')
    transformer = DictUnpackingTransformer()
    transformer.visit(tree)

# Generated at 2022-06-14 01:51:43.734120
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse, dump
    node = parse("{1: 1, 2: 2, **{3: 3, 4: 4}, 5: 5, **{6: 6, 7: 7}}")
    transformer = DictUnpackingTransformer()

    result = transformer.visit(node)
    assert dump(result) == dump(parse(textwrap.dedent("""
    _py_backwards_merge_dicts([dict({1: 1, 2: 2, 5: 5}), {3: 3, 4: 4}, {6: 6, 7: 7}])
    """)))

# Generated at 2022-06-14 01:51:51.008264
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    node = ast.parse("{1: 1, 2: 2, **dict_a}")
    expected = ast.parse("_py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a)")
    generated = transformer.visit(node)
    assert ast.dump(expected, include_attributes=False) == \
           ast.dump(generated, include_attributes=False)



# Generated at 2022-06-14 01:52:01.512049
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert_transform(
        r'''
        {1: 1, **dict_a}
        ''',
        r'''
        _py_backwards_merge_dicts([{1: 1}], dict_a)
        ''',
        DictUnpackingTransformer
    )

    assert_transform(
        r'''
        {**dict_a, 1: 1}
        ''',
        r'''
        _py_backwards_merge_dicts([{1: 1}], dict_a)
        ''',
        DictUnpackingTransformer
    )


# Generated at 2022-06-14 01:52:07.103412
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    code = 'd = {1: 1, **{2: 2}, **{3: 3}}'
    expected_code = (
        'd = _py_backwards_merge_dicts([dict({1: 1})], {2: 2}, {3: 3})')
    actual_code = transformer.visit_code(code)
    assert actual_code == expected_code

# Generated at 2022-06-14 01:52:18.160401
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import random
    
    class DummyNode(ast.AST):
        pass
    

# Generated at 2022-06-14 01:52:23.408211
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import typed_astunparse
    import astunparse

    code = '{1: 1, **dict_a, 2: 2, **dict_b}'
    tree = ast.parse(code)
    tree = DictUnpackingTransformer().visit(tree)
    assert typed_astunparse.unparse(tree) == \
           '_py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a, dict_b)'

# Generated at 2022-06-14 01:53:41.011633
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast
    from transformers import DictUnpackingTransformer
    from utils.examples import expr_examples


# Generated at 2022-06-14 01:53:51.393802
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    x = ast.Expr(
        value=ast.Dict(
            keys=[None, ast.Str(s='a')],
            values=[ast.Dict(
                keys=[None, ast.Str(s='b')],
                values=[ast.Num(n=1), ast.Num(n=3)]
            ), ast.Dict(
                keys=[ast.Str(s='b'), ast.Str(s='c')],
                values=[ast.Num(n=2), ast.Num(n=4)]
            )]
        )
    )
    code = "x  # type: ignore"


# Generated at 2022-06-14 01:53:57.541443
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from .fixtures import DictUnpackingFixture
    from .helpers import assert_source_equal
    from .test_base import run_node_transformer_test
    test = DictUnpackingFixture()
    result = run_node_transformer_test(DictUnpackingTransformer, test)
    assert_source_equal(astor.to_source(result), test.result_source)