

# Generated at 2022-06-14 01:44:17.658844
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse, dump
    from .base import BaseNodeTransformer

    class TestNodeTransformer(BaseNodeTransformer):
        target = (3, 4)

        def visit_Str(self, node: ast.Str) -> ast.expr:
            return ast.Str(s=node.s + "_")

    class TestDictUnpackingTransformer(DictUnpackingTransformer):
        def visit_Str(self, node: ast.Str) -> ast.expr:
            return ast.Str(s=node.s + "_")

    node = parse("a = {str_: str_, None: str_}")
    actual = TestDictUnpackingTransformer().visit(node)

# Generated at 2022-06-14 01:44:23.931037
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = """
    {1: 1, **dict_a, 2: 2, **dict_b, 3:3}
    """
    node = ast.parse(source, '<test>', 'eval')
    node = DictUnpackingTransformer().visit(node)
    expected = """
    _py_backwards_merge_dicts([{1: 1, 2: 2}, dict_a, dict_b, {3: 3}])
    """
    expected = ast.parse(expected, '<test>', 'eval')
    assert ast.dump(node) == ast.dump(expected)



# Generated at 2022-06-14 01:44:31.687105
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Example
    # def f():
    #     return {1: 2, **{3: 4}, 5: 6, **{7: 8}}

    dict1 = ast.Dict(
        keys=[ast.Num(n=1), ast.Num(n=3), ast.Num(n=5), ast.Num(n=7)],
        values=[ast.Num(n=2), ast.Num(n=4), ast.Num(n=6), ast.Num(n=8)])
    dict2 = ast.Dict(
        keys=[ast.Num(n=1), ast.Num(n=3)],
        values=[ast.Num(n=2), ast.Num(n=4)])

# Generated at 2022-06-14 01:44:42.260364
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '{1: 1, **dict_a, 2: 2, **dict_b, 3: 3}'
    tree = ast.parse(code)
    DictUnpackingTransformer.run_if_is_valid_target(tree)
    result = ast.dump(tree)

# Generated at 2022-06-14 01:44:49.424473
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert_transformed_code_equals(
        code='''
        {1: 1, **dict_a, 2: 2, **dict_b}
        ''',
        transformer=DictUnpackingTransformer,
        expected_code='''
        _py_backwards_merge_dicts(
            [{1: 1, 2: 2}], dict_a, dict_b
        )
        '''
    )

# Generated at 2022-06-14 01:44:56.424211
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    DictUnpackingTransformer.target = (3, 8)
    source = """{1: 1, **dict_a}"""
    expected = """
_py_backwards_merge_dicts(
    [{1: 1}], dict_a)
    """
    result = DictUnpackingTransformer.run_single(source)
    assert expected == result



# Generated at 2022-06-14 01:45:01.339869
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.ast_helper import dump
    x = ast.parse("{1: 1, **dict_a}")
    DictUnpackingTransformer().visit(x)

# Generated at 2022-06-14 01:45:10.688279
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert ast.dump(DictUnpackingTransformer().visit(
        ast.parse('{1: 2, **d}').body[0])
    ) == 'Call(func=Name(id=\'_py_backwards_merge_dicts\', ctx=Load()), ' \
        'args=[List(elts=[Dict(keys=[Num(n=1)], values=[Num(n=2)]), ' \
        'Name(id=\'d\', ctx=Load())], ' \
        'ctx=Load())], keywords=[])'


# Generated at 2022-06-14 01:45:20.742100
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..parser import parse
    from .base import get_compiled_source

    source = '''\
d = {1: 1, 2: 2, **dict_a}
'''
    expected_code = '''\
d = _py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a)
'''
    expected_tree = parse(expected_code) # type: ignore

    tree = parse(source)
    transformer = DictUnpackingTransformer()
    tree = transformer.visit(tree)
    compiled_code = get_compiled_source(tree)

    assert compiled_code == expected_code
    assert ast.dump(tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 01:45:30.951528
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source_to_node
    from inspect import cleandoc

    node = source_to_node(cleandoc('''
    from typing import Dict, Any
    
    
    def foo(dict1: Dict[str, int], dict2: Dict[str, Any]) -> Dict[str, Any]:
        return {1: 1, 2: 2, **dict1, **dict2}
    
    def bar() -> Dict[str, int]:
        return {1: 1, 2: 2, **{3: 3}}
    
    def baz() -> Dict[str, Any]:
        return {1: 1, 2: 2, **{3: 3}}
    '''))
    transformer = DictUnpackingTransformer()
    transformer.visit(node)
    

# Generated at 2022-06-14 01:45:44.835630
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    # TODO: find better way for testing
    #       without modifying _context of ast.fix_missing_locations
    import astfixer.utils.tree
    astfixer.utils.tree._context = astfixer.utils.tree.Context()

    code = """
        d = {'a': 1, **{'b': 2}, 'c': 3, **{'d': 4}}
    """
    expected = """
        d = _py_backwards_merge_dicts(
            [{'a': 1, 'c': 3}],
            {'b': 2},
            {'d': 4}
        )
    """

    module = ast.parse(code)
    transformer = DictUnpackingTransformer()
    transformed = transformer.visit(module)

    assert astor.to_

# Generated at 2022-06-14 01:46:00.413688
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()

    class Node(ast.AST):
        def __init__(self, val):
            super().__init__()
            self.val = val

        def __eq__(self, other: object) -> bool:
            return isinstance(other, Node) and self.val == other.val

        def __repr__(self) -> str:
            return 'Node.{}'.format(self.val)

    expr_a = ast.Name(id='a', ctx=ast.Load())
    expr_b = ast.Name(id='b', ctx=ast.Load())
    expr_c = ast.Name(id='c', ctx=ast.Load())
    expr_A = Node('a')
    expr_B = Node('b')

# Generated at 2022-06-14 01:46:05.060882
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    module = ast.parse(
        dedent('''\
        {
            'a': [1, 2],
            **dict_a
        }''').strip())
    tr = DictUnpackingTransformer()
    tr.visit(module)
    res = dedent('''\
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result

          
        _py_backwards_merge_dicts([{'a': [1, 2]}], dict_a)''')
    assert ast.dump(module) == res

# Generated at 2022-06-14 01:46:13.612383
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import textwrap

    before = ast.parse(textwrap.dedent('''\
        {
            "a": 1,
            **dict_a,
            "b": 2,
            **dict_b,
            "c": 3
        }
    '''))

    after = ast.parse(textwrap.dedent('''\
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
        
        _py_backwards_merge_dicts([{'a': 1}, dict_a, {'b': 2}, dict_b, {'c': 3}])
    '''))

    expected = ast.fix_missing_locations(after)

    transformer = DictUnpacking

# Generated at 2022-06-14 01:46:22.119974
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Tests for _split_by_None method
    assert DictUnpackingTransformer()._split_by_None([(None, None)]) == [None]
    assert DictUnpackingTransformer()._split_by_None([(None, None),
                                                      (2, 3),
                                                      (None, None)]) == [None, [
            (2, 3)], None]
    # Tests for _prepare_splitted
    assert DictUnpackingTransformer()._prepare_splitted([[]]) == []
    assert DictUnpackingTransformer()._prepare_splitted([None]) == [
        ast.Call(
            func=ast.Name(id='dict'),
            args=[None],
            keywords=[])]

# Generated at 2022-06-14 01:46:32.510775
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    import typing as t

    sample = '''
        {None: 2, *{3: 4}, **{5: 6}}
        {**{5: 6}, *{3: 4}, None: 2}
        {1:2, **{3: 4}, *{5: 6}, 7: 8}
        {None}
        {None: None}
        {1: 2, None, None: 3, 4: 5}
    '''

# Generated at 2022-06-14 01:46:45.083442
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.tree import as_parsed_ast_string, as_string
    from typed_ast import ast3 as ast

    node = as_parsed_ast_string(r'''
        {1: 1, 2: 2, None: 1, 3: 3}
    ''')

    transformer = DictUnpackingTransformer(None)
    result = transformer.visit(node)

    expected_result = as_parsed_ast_string(r'''
        _py_backwards_merge_dicts([{1: 1, 2: 2}], 1, {3: 3})
    ''')

    assert as_string(result) == as_string(expected_result)



# Generated at 2022-06-14 01:46:55.375979
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    from ..utils.tree import dump_tree
    from ..utils.typing import String, StringIO
    import io
    import textwrap
    import os
    import sys

    path = os.path.dirname(os.path.abspath(__file__))
    path_to_test_dir = os.path.dirname(path)
    path_to_module = os.path.join(path_to_test_dir, 'backends', 'python')
    dummy_module_name = 'dummy'
    sys.path.append(path_to_module)
    module = __import__(dummy_module_name, fromlist=[''])

    source = '{{1: 1, **dict_a}}'

# Generated at 2022-06-14 01:47:01.206278
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    exp1 = ast.parse('{a: 1, b: 2, c: 3, None: d}')
    print(astor.to_source(exp1))
    x = DictUnpackingTransformer().visit(exp1)
    print(astor.to_source(x))

# Generated at 2022-06-14 01:47:11.370728
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    attrib = 'value'
    code_template = '{a.value: 1, 2, a.value: 3, None}'


# Generated at 2022-06-14 01:47:24.830337
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class DictUnpackingVisitor(ast.NodeVisitor):
        """ast.NodeVisitor which looks for object of type _py_backwards_merge_dicts."""
        def __init__(self):
            self.result = []

        def visit_Call(self, node: ast.Call) -> None:
            if isinstance(node.func, ast.Name) and node.func.id == '_py_backwards_merge_dicts':
                self.result.append(node)


# Generated at 2022-06-14 01:47:29.804057
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse

    source = """
    {
        1: 1,
        **{"a": 3},
        4: 5,
        **{
            "b": 2,
            "c": 4,
        },
        6: 7,
        None: None,
        8: 9,
        **{},
    }
    """

# Generated at 2022-06-14 01:47:39.230842
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    '''
    Check if DictUnpackingTransformer works properly on dicts with unpacking.
    '''

# Generated at 2022-06-14 01:47:48.595402
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    class DummyTransformer:
        target = (3, 4)

        def generic_visit(self, node: ast.Dict) -> ast.Dict:
            return node
    dummy_transform = DummyTransformer()

    assert DictUnpackingTransformer(dummy_transform).visit_Dict(  # type: ignore
        ast.parse('{1: 1}').body[0].value) == ast.parse('{1: 1}').body[0].value

# Generated at 2022-06-14 01:47:53.120069
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    assert transformer.visit(ast.parse('{1: 2, **{3: 4}}')) == \
           transformer.visit(ast.parse('_py_backwards_merge_dicts([{1: 2}], {3: 4})'))



# Generated at 2022-06-14 01:48:04.046458
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast, parse
    from ..utils import compiler
    def _test_DictUnpackingTransformer_visit_Dict(code):
        node = parse(code)
        DictUnpackingTransformer().visit(node)
        compiled = compiler.ast_to_func(node)
        return compiled

    assert _test_DictUnpackingTransformer_visit_Dict('{1: 1}')() == {1: 1}
    assert _test_DictUnpackingTransformer_visit_Dict('{1: 1, **dict_a}')(
        dict_a={2: 2, 3: 3}) == {1: 1, 2: 2, 3: 3}

# Generated at 2022-06-14 01:48:14.124756
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse('''
{
    1: 1,
    **{'a': 1},
    2: 2,
    **{'b': 2},
    **{'c': 3},
    3: 3
}
'''[1:])
    assert isinstance(DictUnpackingTransformer().visit(tree), ast.Call)
    assert isinstance(tree.body[0], ast.Assign)
    assert isinstance(tree.body[0].value, ast.Call)

    tree = ast.parse('''
{
    1: 1,
    **{'a': 1},
    **dict_b,
    2: 2
}
'''[1:])
    assert isinstance(DictUnpackingTransformer().visit(tree), ast.Call)

# Generated at 2022-06-14 01:48:22.668480
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor
    import textwrap

    code = textwrap.dedent("""
        {1: 1, **dict_a}
    """)
    tree = ast.parse(code)
    DictUnpackingTransformer().visit(tree)
    assert astor.to_source(tree) == textwrap.dedent("""
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result

        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """)


# Generated at 2022-06-14 01:48:28.800871
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..backport_util import format_code

    code = '{1: 1, **dict_a}'
    expected = '_py_backwards_merge_dicts([{1: 1}], dict_a}'

    module = ast.parse(code)
    transformer = DictUnpackingTransformer()
    new_module = transformer.visit(module)

    assert format_code(new_module) == format_code(expected)

# Generated at 2022-06-14 01:48:35.979043
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    tree = ast.parse("{1: 1, 2: 2, **dict_a, **dict_b, 3: 3}")
    transformer = DictUnpackingTransformer()
    transformer.visit(tree)
    expected = ast.Call(
        func=ast.Name(id='_py_backwards_merge_dicts'),
        args=[
            ast.List(
                elts=[ast.Dict(
                    keys=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3)],
                    values=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3)])]),
            ast.Name(id='dict_a'),
            ast.Name(id='dict_b')],
        keywords=[])

# Generated at 2022-06-14 01:48:50.747436
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from test.utils import roundtrip

    DictUnpackingTransformer.patch()
    tree = roundtrip(lambda: {1: 1, 'a': 2, 3: 3, **{'b': 4}, 'b': 5})
    merge_dicts.restore()
    assert tree.body[0].value.args[0].elts[0].keys[0].n == 1
    assert tree.body[0].value.args[0].elts[0].keys[1].s == 'a'
    assert tree.body[0].value.args[0].elts[0].keys[2].n == 3
    assert tree.body[0].value.args[0].elts[0].values[0].n == 1
    assert tree.body[0].value.args[0].elts[0].values[1].n

# Generated at 2022-06-14 01:49:02.074168
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test_utils import transform
    from ..utils.type_hint import TypeHintTransformer
    body = '''{}'''
    result = transform(body, DictUnpackingTransformer)
    assert result.strip() == body.strip()

    body = '''
    {1: 1}
    '''
    result = transform(body, DictUnpackingTransformer)
    assert result.strip() == body.strip()

    body = '''
    {1: 1, **a}
    '''
    result = transform(body, DictUnpackingTransformer)
    assert result.strip() == '''
    _py_backwards_merge_dicts([{1: 1}], a)
    '''


# Generated at 2022-06-14 01:49:09.510579
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert ast.dump(
        DictUnpackingTransformer().visit(
            ast.parse(
                """\
a = {1: 1, **a, 2: 2}

b = {**a}

c = {1: 1, **a, 2: 2, **b}
"""))) == """\
_py_backwards_merge_dicts([{1: 1}, a, {2: 2}])

a

_py_backwards_merge_dicts([{1: 1}, a, {2: 2}, b])
"""

# Generated at 2022-06-14 01:49:19.964851
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import dedent
    from ..utils.source import source_to_unicode

    example_dict = dedent("""
    {
        None: {'a': 1},
        'b': 2,
        None: {'c': 3},
        'd': 4,
    }
    """)
    code = 'result = %s' % source_to_unicode(example_dict)

    tree = ast.parse(code)
    transforme_tree = DictUnpackingTransformer().transform(tree)
    compiled = compile(transforme_tree, '<unknown>', 'exec')
    root = {}
    exec(compiled, {}, root)
    result = root['result']
    assert result == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Generated at 2022-06-14 01:49:29.802736
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    t = DictUnpackingTransformer()
    module = ast.parse("""
    {1: 1, 2: 2, **a}
    """)
    v = t.visit(module)
    assert v.body[0].value.args[0].elts[0].keys == [ast.Num(n=1)]
    assert v.body[0].value.args[0].elts[0].values == [ast.Num(n=1)]
    assert v.body[0].value.args[0].elts[1].keys == [ast.Num(n=2)]
    assert v.body[0].value.args[0].elts[1].values == [ast.Num(n=2)]
    assert v.body[0].value.args[1].id == 'a'

# Generated at 2022-06-14 01:49:39.055829
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer(0)
    tree = ast.parse('{1: 2, **dict_a(), **dict_b, 3: 4, **dict_c()}')
    tree = transformer.visit(tree)
    # noinspection PyUnresolvedReferences
    ast.fix_missing_locations(tree)
    assert ast.dump(tree) == \
        '_py_backwards_merge_dicts(["""Merge dicts backwards. This is ' \
        'necessary because the order of keys in Python determines its ' \
        'behavior.""", {"1": 2}, dict_a(), dict_b, {"3": 4}, dict_c())'



# Generated at 2022-06-14 01:49:46.983264
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..parser import ast_from_str


# Generated at 2022-06-14 01:49:53.424518
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # type: () -> None
    tree = ast.parse('{1: 2, 3: 4, **{5: 6, 7: 8, 9: 10}}', mode='eval')
    transformer = DictUnpackingTransformer()
    result = transformer.visit(tree)  # type: ignore
    assert ast.dump(result) == '_py_backwards_merge_dicts([dict({1: 2}, {3: 4})], {5: 6, 7: 8, 9: 10})'

# Generated at 2022-06-14 01:50:05.116634
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from xotl.tools.symbols import symbols

    tree = ast.parse('{"k1": 1, "k2": 2, **d, "k3": 3}')
    d = symbols('a.b.d', ast.Dict)
    D = DictUnpackingTransformer(symbols=symbols.bindings)
    result = D.run(tree)

# Generated at 2022-06-14 01:50:14.628251
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typing import Any

    def _make_Dict(keys: List[Any], values: List[Any]) -> ast.Dict:
        return ast.Dict(
            keys=keys,
            values=values)

    def _make_Call(func: ast.Callable, args: List[Any],
                   keywords: List[Any]) -> ast.Call:
        return ast.Call(
            func=func,
            args=args,
            keywords=keywords)

    def _make_name(id: str) -> ast.Name:
        return ast.Name(id=id)

    def _make_list(elts: List[Any]) -> ast.List:
        return ast.List(elts=elts)

    tester = DictUnpackingTransformer()


# Generated at 2022-06-14 01:50:26.317171
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    class TestCase:
        def __init__(self, code: str, expected_code: str, target: Optional[str]):
            self.code = code
            self.expected_code = expected_code
            self.target = target

        def test(self):
            result = DictUnpackingTransformer().visit(ast.parse(self.code))
            assert compile(result, '<string>', 'exec').co_names == (
                compile(self.expected_code, '<string>', 
                        'exec').co_names if self.target is None
                else compile(self.target, '<string>', 'exec').co_names)


# Generated at 2022-06-14 01:50:33.898204
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    module = ast.parse('{**{}}')
    module = DictUnpackingTransformer()(module)
    expected = ast.parse('\n'.join([
        'def _py_backwards_merge_dicts(dicts: list) -> dict:',
        '    result: dict = {}',
        '    for dict_ in dicts:',
        '        result.update(dict_)',
        '    return result',
        '{}'
    ]))
    assert module == expected



# Generated at 2022-06-14 01:50:35.292905
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert isinstance(DictUnpackingTransformer(), BaseNodeTransformer)

# Generated at 2022-06-14 01:50:47.231291
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    
    assert DictUnpackingTransformer().visit(ast.parse("{1: 1, **dict_a}")) == \
    ast.parse("""
    _py_backwards_merge_dicts([{1: 1}], dict_a)
    """).body[0]
    
    assert DictUnpackingTransformer().visit(ast.parse('{1: 1, 2: 2, **dict_a}')) == \
    ast.parse("""
    _py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a)
    """).body[0]
    

# Generated at 2022-06-14 01:50:53.164447
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    source = """
    d = {1: 1, **a}
    """
    expected = """
    d = _py_backwards_merge_dicts([{1: 1}], a)
    """
    node = ast.parse(source)
    result = DictUnpackingTransformer().visit(node)
    node_reduced = ast.parse(expected)
    assert ast.dump(result) == ast.dump(node_reduced)

# Generated at 2022-06-14 01:50:57.418421
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '{"a":1}'
    tree = ast.parse(code)
    transformer = DictUnpackingTransformer(tree)  # type: ignore
    transformer.visit(tree)
    expected = '''\
{'a': 1}'''
    assert code == expected


# Generated at 2022-06-14 01:50:58.402073
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    assert DictUnpackingTransformer()

# Generated at 2022-06-14 01:51:05.245735
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from astunparse import unparse
    mod = ast.parse("")
    result = DictUnpackingTransformer().visit_Module(mod)
    assert unparse(result).replace("\n", "").replace(" ", "") ==\
        "def_py_backwards_merge_dicts(dicts):result={}for_dict_indicts:result.update(dict_)returnresult".replace(
        "_", "")



# Generated at 2022-06-14 01:51:14.897938
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Tests method visit_Dict of DictUnpackingTransformer."""
    from astunparse import unparse
    from .base import run_for_tests
    from .generic import GenericNodeTransformer
    from .call import CallTransformer

    src = """{1: 1, **dict_a, **dict_b, 2: 2, 'three': 3, **dict_c}"""
    expected = """_py_backwards_merge_dicts(
    [{1: 1, 2: 2, 'three': 3}],
    dict_a, dict_b, dict_c)"""
    tree = run_for_tests([src], [DictUnpackingTransformer,
                                 GenericNodeTransformer,
                                 CallTransformer])
    got = unparse(tree)
    assert got == expected



# Generated at 2022-06-14 01:51:24.909408
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from node_transformers_test.util import run_test_nodes
    from node_transformers_test.util import run_test_node
    from node_transformers_test.util import run_test_blocks

    run_test_nodes(
        nodes=[
            ast.Dict(keys=[ast.Num(n=1), None, ast.Num(
                n=2)], values=[ast.Num(n=1), ast.Num(n=1), ast.Num(n=2)])
        ],
        node_transformer=DictUnpackingTransformer(),
        expected_code=[
            '_py_backwards_merge_dicts([{1: 1}, 1], {2: 2})'
        ]
    )


# Generated at 2022-06-14 01:51:36.521400
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    input_dict = ast.parse('dict({0:0, 1:1, 2:2, **{3:3, 4:4}})')
    expected = ast.parse(
        'dict({0:0, 1:1, 2:2, **_py_backwards_merge_dicts([dict({3:3}), {4:4})})'
    )
    result = transformer.visit(input_dict.body[0].value)
    assert ast.dump(expected) == ast.dump(result)

# Generated at 2022-06-14 01:51:37.809741
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:51:49.596754
# Unit test for constructor of class DictUnpackingTransformer

# Generated at 2022-06-14 01:51:56.444142
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .base import BaseNodeTransformerTestCase

    module = """
    {1: 1, **dict_a}
    """

    expected_module = """
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result
    _py_backwards_merge_dicts([{1: 1}], dict_a)
    """

    assert_transform(DictUnpackingTransformer, module, expected_module)


# Generated at 2022-06-14 01:52:00.262189
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = '''\
{1: 1, **dict_a}
'''
    node = ast.parse(code)
    tr = DictUnpackingTransformer()
    res = tr.visit(node)

# Generated at 2022-06-14 01:52:11.450302
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.helpers import copy_location
    from ..utils.visitor import NodeTransformer

    transformer = NodeTransformer()
    transformer.transformer_class = DictUnpackingTransformer

    def visit_Call(x):
        return copy_location(
            ast.Call(
                func=ast.Name(id='_py_backwards_merge_dicts'),
                args=[x],
                keywords=[]),
            x)

    code = transformer.visit(
        ast.parse('''
            dict(a=1, **dict(b=2), c=3, **dict(d=4))
        '''))

# Generated at 2022-06-14 01:52:18.133001
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    test_cases = [
        ("{}", "{}"),
        ("{1: 1}", "{1: 1}"),
        ("{1: 1, **{}}", "_py_backwards_merge_dicts([{1: 1}], {})"),
        ("{1: 1, **dict_a}", "_py_backwards_merge_dicts([{1: 1}], dict_a)"),
        (
            "{1: 1, **dict_a, 2: 2, **dict_b, 3: 3}",
            "_py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], dict_a, dict_b)"
        ),
    ]

# Generated at 2022-06-14 01:52:22.713578
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = """
    {1: 1, **dict_a}
    """
    assert DictUnpackingTransformer.run_and_dump(code) == code
    assert DictUnpackingTransformer.run_and_dump(code, target=(3, 6)) == """
    _py_backwards_merge_dicts([{1: 1}], dict_a)
    """



# Generated at 2022-06-14 01:52:28.137163
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .verify import verify

    # Test 1
    # input
    input_ = '''
    {**a, **b}
    '''
    # expected output
    expected = '''
    _py_backwards_merge_dicts([], a, b)
    '''
    # actual output
    actual = DictUnpackingTransformer().visit(
        ast.parse(input_))
    
    # verify
    verify(expected, actual)
    


# Generated at 2022-06-14 01:52:31.775722
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from astunparse import unparse
    from ast import parse

    transformer = DictUnpackingTransformer()
    module = ast.parse("""
        a = {1: 1, *b}
        """)
    result = transformer.visit(module)

# Generated at 2022-06-14 01:52:53.506696
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import unittest

    from typed_ast.ast3 import parse
    from typed_ast.pretty_printer import PrettyPrinter

    class TestDictUnpackingTransformer_visit_Dict(unittest.TestCase):
        def setUp(self):
            self.visitor = DictUnpackingTransformer()

        def test_normal_dict(self):
            code = '{1: 1}'
            expected = '{1: 1}'
            node = parse(code)
            result = self.visitor.visit(node)
            result.body[0].body[0].value.value.args.append(
                PrettyPrinter().visit(result))
            self.assertEqual(str(result), expected)


# Generated at 2022-06-14 01:52:57.953876
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    src = '{1: 1, **dict_a}'
    expected = '_py_backwards_merge_dicts([{1: 1}], dict_a}'
    support.assert_transform(DictUnpackingTransformer, src, expected)



# Generated at 2022-06-14 01:53:00.366026
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    class_ = globals()['DictUnpackingTransformer']
    assert class_ is not None


# Generated at 2022-06-14 01:53:16.009532
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse("def _py_backwards_merge_dicts(dicts):\n"
                     "    result = {}\n"
                     "    for dict_ in dicts:\n"
                     "        result.update(dict_)\n"
                     "    return result\n")

# Generated at 2022-06-14 01:53:20.657944
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    method_names_set = {method[0] for method in
                        inspect.getmembers(DictUnpackingTransformer,
                                           predicate=inspect.ismethod)}
    assert method_names_set == {'_split_by_None', '_prepare_splitted',
                                '_merge_dicts', 'visit_Module', 'visit_Dict',
                                'generic_visit'}

# Generated at 2022-06-14 01:53:29.920103
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import ast as _ast
    from ..utils.tester import NodeTestCase
    from ..utils.codegen import to_source
    from . import compile_isolated

    class _Test(NodeTestCase):
        target = DictUnpackingTransformer

        def _test(self, node: _ast.Dict, expected: str):
            self.generic_test(node, expected)

    _Test()._test(
        _ast.Dict(
            keys=[None, _ast.Num(1), None, _ast.Num(1)],
            values=[_ast.Str('a'), _ast.Str('b'), _ast.Str('c'), _ast.Str('d')]),
        '_py_backwards_merge_dicts([dict(b="a"), dict(d="c")], 1, 1)')

    _

# Generated at 2022-06-14 01:53:33.323821
# Unit test for method visit_Module of class DictUnpackingTransformer

# Generated at 2022-06-14 01:53:43.147376
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    keys = [ast.Num(1), ast.Str('x'), None]
    values = [ast.Num(2), ast.Num(3), ast.Str('z')]
    node = ast.Dict(keys, values)
    transformer = DictUnpackingTransformer()
    new_node = transformer.visit(node)
    assert isinstance(new_node, ast.Call)
    assert isinstance(new_node.func, ast.Name)
    assert new_node.func.id == '_py_backwards_merge_dicts'
    assert len(new_node.args) == 1
    assert len(new_node.args[0].elts) == 2
    assert isinstance(new_node.args[0].elts[0], ast.Dict)

# Generated at 2022-06-14 01:53:46.521023
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
  transformer = DictUnpackingTransformer()
  x = {
      'a': 1,
      **{'b': 2}
  }
  transformer.visit(ast.parse(str(x)))

# Generated at 2022-06-14 01:53:52.233217
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ...testing.utils import assert_transformed_ast

    input = '''
    {1: 1, **dict_a, None: 2, **dict_b}
    '''
    expected = '''
    {1: 1, 2: 3}
    '''

    dict_a = ast.Name(id='dict_a')
    dict_b = ast.Name(id='dict_b')
    t = DictUnpackingTransformer(dict_a, dict_b)
    assert_transformed_ast(t, input, expected)