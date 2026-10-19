

# Generated at 2022-06-14 01:44:15.636295
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()
    assert transformer.visit(ast.parse('''
        {1: 1, 2: 2, **dict_a, 3: 3, **dict_b}
    ''')) == ast.parse('''
        (
            (
                _py_backwards_merge_dicts(
                    [(
                        (
                            (
                                (
                                    dict(
                                        [(1), (1)]
                                    )
                                ),
                                (
                                    dict(
                                        [(2), (2)]
                                    )
                                )
                            )
                        )
                    ],
                    dict_a
                )
            ),
            dict_b
        )
    ''')

# Generated at 2022-06-14 01:44:18.707311
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    code = '''{1: 1, 2: 2}'''
    transformed_code = '''_py_backwards_merge_dicts([], {})'''
    assert transform(code, 3, 4, DictUnpackingTransformer) == transformed_code

# Generated at 2022-06-14 01:44:22.172915
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    assert isinstance(compile(
        "a = {**b, **{'c': 1}, 2: 'd', **e}",
        "<string>",
        "exec",
    ), ast.Module)

# Generated at 2022-06-14 01:44:31.457951
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import source
    from ..utils.ast import parse
    from ..utils.visitor import NodeVisitor
    
    class CallPrinter(NodeVisitor):
        def __init__(self):
            self.calls = []
        
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name) and node.func.id == '_py_backwards_merge_dicts':
                self.calls.append(node)
    
    ctx = {
        'data': {1: 2},
        'another_data': {2: 3},
        'yet_another_data': {3: 4},
    }
    
    def run():
        return {1: 2, **data, **another_data, **yet_another_data}
    
    source

# Generated at 2022-06-14 01:44:39.029644
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils import parse
    from ..utils.fixtures import (dict_nested_with_unpacking,
                                  dict_nested_without_unpacking)

    # Assert that unpacking is present in original annotated dict
    assert '**' in dict_nested_with_unpacking
    assert '**' not in dict_nested_without_unpacking

    # Assert that unpacking is gone in transformed dict
    with_unpacking = parse(dict_nested_with_unpacking)
    without_unpacking = parse(dict_nested_without_unpacking)

    transformer = DictUnpackingTransformer()
    transformer.visit(with_unpacking)
    assert transformer._tree_changed and transformer.target in transformer.versions  # noqa

    transformer = DictUnpackingTransformer()

# Generated at 2022-06-14 01:44:48.991747
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    code = '''
        {None: foo, 'bar': baz, 1: qux, None: None, '123': 123, None: {}}'''

    module = ast.parse(code)
    DictUnpackingTransformer().visit(module)

    results = ('{1: qux}', '{123: 123}', '{}')
    assert module.body[0].body[1].value.args[0].elts == [
        ast.Dict(keys=ast.Num(n=1), values=ast.Name(id='qux')),
        ast.Dict(keys=ast.Str(s='123'), values=ast.Num(n=123)),
        ast.Dict(keys=[], values=[])
    ]

# Generated at 2022-06-14 01:44:59.539380
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    ns = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    # noinspection PyTypeChecker
    def check(code: str, result: Union[str, ast.AST]):
        prepare_code = ast.parse(code)
        # noinspection PyTypeChecker
        expected = ast.parse(result).body[0] if isinstance(result, str) else result
        transformer = DictUnpackingTransformer()
        result = transformer.visit_Module(prepare_code)  # type: ignore
        resulting_code = compile(result, '<test>', 'exec')
        exec(resulting_code, ns)
        assert ns['_py_backwards_merge_dicts'] is not None
        assert result.body[-1] == expected



# Generated at 2022-06-14 01:45:11.315811
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:45:22.215441
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse, Dict, Call, Name, List, BinOp
    from .multiply import MultiplyOperatorTransformer

    source = """
    x = {1: 2, 3: 4}
    x = {1: 2, 3: 4, **a}
    x = {1: 2, 3: 4, **a, 5: 6, **b}
    x = {k: v for k, v in x}
    x = {**a, 'b': 2}
    x = {**a, 'b': 2, **b, **c}
    x = {**a, 'b': 2, **b, **c} + {**a, 'b': 2, **b, **c}
    """


# Generated at 2022-06-14 01:45:28.579022
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    src = """
from typing import Union
from typed_ast import ast3 as ast
from ...utils.tree import insert_at
from ...utils.snippet import snippet
from ...transformers.base import BaseNodeTransformer
from ...utils import find_nodes
from ...utils.visitor import NodeVisitor
from ...utils.snippet import snippet
from ..utils.tree import insert_at
from ..utils.snippet import snippet
from .base import BaseNodeTransformer"""

# Generated at 2022-06-14 01:45:42.681339
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse
    code = '''\
{1: 2, 3: 4, **kwargs}
'''
    expected = '''\
_py_backwards_merge_dicts([{1: 2, 3: 4}], kwargs)
'''
    actual = DictUnpackingTransformer().visit(parse(code))
    assert compile(actual, '<ast>', 'exec').co_consts[0] == compile(expected,
                                                                    '<ast>',
                                                                    'exec').co_consts[0]

# Generated at 2022-06-14 01:45:48.133104
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    src = """{1: 1, **dict_a, 3: 3, **dict_b}"""
    module = ast.parse(src)
    DictUnpackingTransformer().visit(module)
    expected = """_py_backwards_merge_dicts([{1: 1, 3: 3}], dict_a, dict_b)"""
    assert ast.dump(module, include_attributes=False) == expected


# Generated at 2022-06-14 01:46:01.148494
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # set up nodes
    _1, _2, _3, _4, _5 = [ast.Num(n=n) for n in range(1, 6)]
    _a, _b, _c, _d = [ast.Name(id=x) for x in ['a', 'b', 'c', 'd']]
    _e = ast.Dict(keys=[ast.Name(id='e')], values=[_5])
    _f = ast.Dict(keys=[ast.Name(id='f')], values=[_4])
    _g = ast.Dict(keys=[ast.Name(id='g')], values=[_3])
    _h = ast.Dict(keys=[ast.Name(id='h')], values=[_2])

# Generated at 2022-06-14 01:46:10.189355
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .utils import transform_and_compare, load
    from ..utils.nodes import from_dict
    from ..utils.source import source_to_string

    result = transform_and_compare(
        DictUnpackingTransformer, # type: ignore
        load('dict-unpacking'), # type: ignore
        expected_ast=from_dict(load('dict-unpacking.desugared')), # type: ignore
        expected_source=source_to_string(load('dict-unpacking.desugared'))) # type: ignore

# Generated at 2022-06-14 01:46:19.389965
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.source import Source
    from .base import BaseNodeTransformer
    from .dead_code_elimination import DeadCodeEliminationTransformer

    source = Source("""
        {
            1: 1,
            **dict_a,
            2: 2,
            **dict_b
        }
    """)

    node = source.as_module()
    node = DictUnpackingTransformer().visit(node)
    node = BaseNodeTransformer().visit(node)
    node = DeadCodeEliminationTransformer().visit(node)
    source.set(node)

    assert source == '_py_backwards_merge_dicts([{1: 1, 2: 2}], dict_a, dict_b)'

# Generated at 2022-06-14 01:46:28.084231
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.test import assert_equal_ast
    from ..utils.tree import to_module

    src = '''
    {1: 1, 2: 2, 3: 3, **{4: {4: 4}}}
    '''
    expect = '''
    _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}, {4: {4: 4}}])
    '''
    actual = DictUnpackingTransformer().visit(to_module(src))
    assert_equal_ast(actual, expect)

# Generated at 2022-06-14 01:46:33.801128
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    transformer = DictUnpackingTransformer()
    node = ast.Module([])
    transformed = transformer.visit(node)

    assert transformer.tree_changed
    assert ast.dump(transformed) == \
        'Module(body=[_py_backwards_merge_dicts(' \
        '[], __dict__, __annotations__, __builtins__, __doc__, __file__, ' \
        '__name__, __package__, __cached__, __loader__)])'


# Generated at 2022-06-14 01:46:48.358954
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    snippet = [
        ast.Dict(keys=[None, ast.Str(s='bar'), None, None], 
                 values=[ast.Dict(keys=[], values=[]), 
                         ast.Dict(keys=[], values=[]),
                         ast.Dict(keys=[], values=[]),
                         ast.Dict(keys=[], values=[]),
                         ])
    ]

# Generated at 2022-06-14 01:46:56.575892
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # arrange
    transformer = DictUnpackingTransformer()
    node = ast.Dict(keys=[None, None, ast.Num(1)],
                    values=[
                        ast.Call(
                            func=ast.Name(id='dict'),
                            args=[ast.Dict(
                                keys=[ast.Num(1), ast.Num(2)],
                                values=[ast.Num(1), ast.Num(2)])],
                            keywords=[]),
                        ast.Name(id='dict_a'),
                        ast.Num(1)
                    ])


# Generated at 2022-06-14 01:46:58.567916
# Unit test for method visit_Module of class DictUnpackingTransformer

# Generated at 2022-06-14 01:47:16.446053
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from astunparse import unparse

    dict_ = ast.Dict(
        keys=[ast.Num(n=1),
              None,
              ast.Num(n=2),
              None,
              ast.Num(n=3)],
        values=[ast.Num(n=1),
                ast.Call(
                    func=ast.Name(id='dict_a'),
                    args=[],
                    keywords=[]),
                ast.Num(n=2),
                ast.Call(
                    func=ast.Name(id='dict_b'),
                    args=[],
                    keywords=[]),
                ast.Num(n=3)])

# Generated at 2022-06-14 01:47:22.486192
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_astunparse import unparse

    tree = ast.parse("""\
{
    **{'a': 2},
    **{'a': 3},
    'b': 3
}
    """)  # type: ignore
    DictUnpackingTransformer().visit(tree)
    result = unparse(tree)
    expected = """\
_py_backwards_merge_dicts([], {'a': 2}, {'a': 3}, {'b': 3})
"""
    assert result == expected



# Generated at 2022-06-14 01:47:27.149727
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    node = ast.parse("""{
            1: 1,
            2: 2,
            **{3: 3},
            4: 4,
            **{5: 5}
        }""")

    assert DictUnpackingTransformer().visit(node) == ast.parse("""_py_backwards_merge_dicts([dict({1: 1, 2: 2}), {3: 3}, dict({4: 4})], {5: 5})""")


# Generated at 2022-06-14 01:47:28.160832
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    import astunparse


# Generated at 2022-06-14 01:47:38.102799
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.source import assign_and_flow_to_return, source_dump
    from ..utils.parser import parse_string
    from ..utils.compare import compare_ast
    from ..utils.parsing import parse_function_eventually, parse_main_eventually
    from .transformers import Transformer
    from .ast_conversion import get_top_modules
    
    # DictUnpackingTransformer.visit_Module  IS NOT IMPLEMENTED PROPERLY
    # IT SEGFAULTS WHEN:
    #   __file__ IS IN MODULE
    #   MERGED_DICTS IS DEFINED AFTER MODULE, I.E. IN MAIN
    source = '''
a = {1: 1, 2: 2, 3: 3}
b = {**a}
'''
    
    # result_

# Generated at 2022-06-14 01:47:43.769075
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astpretty
    tree_source = """\
{1: 1,
 **dict_a}
"""
    tree = ast.parse(tree_source)
    tree = DictUnpackingTransformer().visit(tree)
    assert astpretty.dump(tree).strip() == """\
_py_backwards_merge_dicts([{1: 1}], dict_a)
"""

# Generated at 2022-06-14 01:47:49.868973
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.fake import Dummy

    transformer = DictUnpackingTransformer()
    code = "{1: 1, **{2: 2}, 3: 3}"
    result = transformer.visit(ast.parse(code))
    expected = ast.parse(
        """_py_backwards_merge_dicts([{1: 1}], {2: 2}, {3: 3})""").body[0]
    assert result == expected



# Generated at 2022-06-14 01:47:58.311494
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3
    transformer = DictUnpackingTransformer()
    input_dict = ast3.parse('{1: 1, 2: 2, 3: 3, **{4: 4, **{5: 5}, 6: 6}}')
    output_dict = transformer.visit(input_dict)  # type: ignore

    expected_dict = ast3.parse('''
        _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], {4: 4, **{5: 5}, 6: 6})
    ''')
    assert ast3.dump(output_dict) == ast3.dump(expected_dict)


# Generated at 2022-06-14 01:48:08.814004
# Unit test for method visit_Dict of class DictUnpackingTransformer

# Generated at 2022-06-14 01:48:18.398900
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    transformer = DictUnpackingTransformer()  # type: ignore
    transformer._tree_changed = False

    input = ast.parse("""{
        1: 1,
        **dict_a,
        2: 2,
        **dict_b,
        3: 3
    }""").body[0]
    output = transformer.visit_Dict(input)

    assert transformer._tree_changed
    assert output.__repr__() == """
    _py_backwards_merge_dicts(
        [dict({
            1: 1,
            2: 2,
            3: 3
        }),
        dict_a,
        dict({
            2: 2,
            3: 3
        }),
        dict_b,
        dict({
            3: 3
        })]
    )""".lstrip

# Generated at 2022-06-14 01:48:33.350628
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast.ast3 import parse, dump

    result = compile(DictUnpackingTransformer().visit(
        parse(
            """
            {1: 1, 2: 2, 3: 3, **dict_a, 4: 4, **dict_b}
            """
        )
    ), '<string>', mode='eval')
    assert eval(result) == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}

# Generated at 2022-06-14 01:48:44.175009
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    tree = ast.parse('var = {1: 1, **dict_a}')

    transformer = DictUnpackingTransformer(tree)
    transformer.visit(tree)

    # pprint.pprint(ast.dump(tree))


# Generated at 2022-06-14 01:48:50.595083
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..utils.testing import assert_equal_source
    from ..utils.source import dedent

    source = '''
        dict(a=b, **a)
        dict(a=b, c=d, **a, d=c)
    '''
    expected_source = '''
        _py_backwards_merge_dicts([{'a': b}], a)
        _py_backwards_merge_dicts([{'a': b, 'c': d}, {'d': c}])
    '''
    assert_equal_source(
        DictUnpackingTransformer,
        source,
        expected_source
    )
    # Test that dict is created when only unpacking is used

# Generated at 2022-06-14 01:48:57.108396
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    expr = '{1: 1, 2: 2, **{3: 3}, 4: 4, **{5: 5}, 6: 6}'
    expected = '_py_backwards_merge_dicts([{1: 1, 2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}])'

    ast_ = ast.parse(expr)
    DictUnpackingTransformer().visit(ast_)  # type: ignore
    
    assert ast_dump(ast_) == expected



# Generated at 2022-06-14 01:49:06.093800
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
  from typed_ast import ast3
  from typed_ast import convert
  from snippet import snippet

  @snippet
  def code():
    for i in range(10):
      print(f"{i} == {i**2}")
    
  module = convert(code.get_ast())
  dict_unpacking_transformer = DictUnpackingTransformer()
  module = dict_unpacking_transformer.visit(module)
  exec(compile(module, filename="<ast>", mode="exec"), {}, None)


# Generated at 2022-06-14 01:49:16.504583
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from typed_ast import ast3 as ast

    class _(DictUnpackingTransformer):
        def visit_Name(self, node):
            return ast.Num(1)
    assert _().visit(ast.parse('{1: 2}')) == ast.parse('{1: 2}')
    assert _().visit(ast.parse('{1: 2, **x}')) == ast.parse('_py_backwards_merge_dicts([{1: 1}], x)')
    assert _().visit(ast.parse('{1: 2, **x, **y}')) == ast.parse('_py_backwards_merge_dicts([{1: 1}, {}], x, y)')

# Generated at 2022-06-14 01:49:24.127992
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    __tracebackhide__ = True
    from typed_ast import ast3
    from .test_BaseNodeTransformer import BaseNodeTransformerTest

    class DUT(DictUnpackingTransformer, BaseNodeTransformerTest):
        pass
    DUT.test('''
    {1: 1, None: x, 2: 2, None: y, 3: 3}
    ''', '''
    _py_backwards_merge_dicts([{1: 1, 2: 2, 3: 3}], x, y)
    ''')

# Generated at 2022-06-14 01:49:31.393503
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    def transpile_func(**kwargs):
        snippet = """
        def func(x, y):
            return {x: y, **kwargs}
        """
        tree = ast.parse(snippet)  # type: ignore
        DictUnpackingTransformer(**kwargs).visit(tree)
        generated_code = compile(tree, filename='<ast>', mode='exec')
        namespace = dict(kwargs=kwargs)
        exec(generated_code, namespace)
        return namespace['func']

    func = transpile_func()
    assert func(1, 2) == {1: 2}
    assert func(1, 2) == {1: 2}

    func = transpile_func(x=2, y=3)

# Generated at 2022-06-14 01:49:38.705916
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.testing import assert_source

    source = """
        {1: 1, **dict_a}
    """

    result = """
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
        
        _py_backwards_merge_dicts([{1: 1}], dict_a)
    """

    assert_source(DictUnpackingTransformer, result, source)



# Generated at 2022-06-14 01:49:51.088242
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    def test(s):
        module = compile(s, "<test_DictUnpackingTransformer_visit_Module>",
                         "exec", ast.PyCF_ONLY_AST)
        DictUnpackingTransformer().visit(module)

# Generated at 2022-06-14 01:50:04.400569
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..testing import assert_replaced_ast
    from ..testing import assert_unchanged_ast

    # without unpacking
    assert_replaced_ast(
        DictUnpackingTransformer,
        """
        {0: 2, 1: 2}
        """,
        """
        {0: 2, 1: 2}
        """
    )

    # with unpacking
    assert_replaced_ast(
        DictUnpackingTransformer,
        """
        {0: 2, 1: 2, **{2: 3}}
        """,
        """
        _py_backwards_merge_dicts([{0: 2, 1: 2}], {2: 3})
        """
    )

    # with unpacking after

# Generated at 2022-06-14 01:50:06.231301
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    node = ast.parse("""
{1: 2, 3: 4, **dict1}
    """)

# Generated at 2022-06-14 01:50:13.209458
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from ..node_visitor import NodeVisitor
    from ..utils.python import parse_source
    
    source = """
    {1: 1, **{2: 2}, 3: 3, **{4: 4}}
    """
    
    result = parse_source(source, node_visitor=NodeVisitor(DictUnpackingTransformer()))
    expected = """\
_py_backwards_merge_dicts([{1: 1}, 3: 3], {2: 2}, {4: 4})
"""
    assert expected == result

# Generated at 2022-06-14 01:50:23.805275
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():

    from ..utils.example import compile_command
    from ..utils.parsing import unparse
    from .module_test import pprint_ast

    # This should be added:
    # def _py_backwards_merge_dicts(dicts):
    #   result = {}
    #   for dict_ in dicts:
    #       result.update(dict_)
    #   return result
    # This should be modified:
    # {1: 1, **{2: 2}, 3: 3, **{4: 4}, 5: 5, **{6: 6}}
    # To:
    # _py_backwards_merge_dicts([{1: 1}, {2: 2}, {3: 3}], {4: 4}, {5: 5},
    #                           {6: 6}])

    source_

# Generated at 2022-06-14 01:50:35.749554
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    # Compiles to a sequence of _py_backwards_merge_dicts calls
    tree = ast.parse("""
{1: 1, 2: 0, None: {3: 2}, 4: 4, **{'a': 2}}
    """)
    result = DictUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 01:50:41.849653
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.testing import Source
    from .node_transformer import transform

    x = merge_dicts.get_ast()
    for source in Source.iter_examples(pattern='dict-unpacking', type='snippet'):
        module = transform(x, [DictUnpackingTransformer])

        assert source.has_equal_ast(module)

# Generated at 2022-06-14 01:50:51.816784
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.source import source
    from .. import fixer_names

    expected_source = source('''
        def _py_backwards_merge_dicts(dicts):
            result = {}
            for dict_ in dicts:
                result.update(dict_)
            return result
    ''')

    class FakeNodeTransformer(BaseNodeTransformer):
        def visit_Dict(self, node):
            return ast.Dict()

    transformer = FakeNodeTransformer(fixer_names)
    instance = DictUnpackingTransformer(transformer)
    result = instance.visit_Module(ast.parse(''))
    assert result.body[0] == ast.parse(expected_source).body[0]



# Generated at 2022-06-14 01:51:02.976040
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from .. import compile
    from ..ast_transforms import DictUnpackingTransformer
    from .utils import assert_equal, assert_raises_with_msg

    assert_equal(['_py_backwards_merge_dicts'],
                 compile('{}', ast_transforms=[DictUnpackingTransformer]).co_names)

    assert_equal(['_py_backwards_merge_dicts'],
                 compile('a = {1:1}', ast_transforms=[DictUnpackingTransformer]).co_names)

    assert_equal(['_py_backwards_merge_dicts'],
                 compile('a = {1:1, **{}}', ast_transforms=[DictUnpackingTransformer]).co_names)


# Generated at 2022-06-14 01:51:06.685298
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    assert ast.parse(
        '{1: 1, **dict_a}'
    ).body[0].value == ast.parse(
        '_py_backwards_merge_dicts([{1: 1}], dict_a})'
    ).body[0].value

# Generated at 2022-06-14 01:51:09.353257
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.test import transform, assert_equal

    @transform(DictUnpackingTransformer)
    def test():
        return {1: 1, **dict_a}



# Generated at 2022-06-14 01:51:26.221902
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..config import Config
    from ..utils.source import source_to_unicode
    from ..utils.ast_helpers import dump_ast
    node = ast.parse(source_to_unicode('''
    def foo(x):
        return {1: 1, 2: 2, **x}
    '''))
    node = DictUnpackingTransformer(Config()).visit(node)

# Generated at 2022-06-14 01:51:28.462533
# Unit test for method visit_Module of class DictUnpackingTransformer

# Generated at 2022-06-14 01:51:34.657031
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ... import compile_snippet
    from ...testing.codegen import code_gen

    source = compile_snippet(merge_dicts.get_source())
    expected = compile_snippet(code_gen(source), mode='eval')
    test = DictUnpackingTransformer()
    result = test.visit_Module(source)
    assert code_gen(result, mode='eval') == expected



# Generated at 2022-06-14 01:51:38.823520
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from . import remove_type_comments, assert_equal_code
    from typed_astunparse import unparse
    import astunparse
    import ast


# Generated at 2022-06-14 01:51:43.422420
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    x = DictUnpackingTransformer()
    assert x.tree_changed == False
    assert x.target == (3,4)
    assert x.stack == []
    assert x.environment == {}
    assert x.parent == None

# Generated at 2022-06-14 01:51:53.589782
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    """Unit test for method visit_Dict of class DictUnpackingTransformer."""
    # pylint: disable=unused-variable,exec-used
    
    # Test for:
    #    {1: 1, **dict_a}
    dict_ = ast.Dict(keys=[ast.Num(n=1), None],
                     values=[ast.Num(n=1), ast.Name(id='dict_a')])
    result = DictUnpackingTransformer().visit(dict_)  # type: ignore

# Generated at 2022-06-14 01:52:03.327122
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.python_source import Source

    src = """
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
    mod = ast.parse(src)
    result = DictUnpackingTransformer().visit(mod)
    expected_mod = ast.parse(expected)
    assert ast.dump(result) == ast.dump(expected_mod)



# Generated at 2022-06-14 01:52:06.890552
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    actual = DictUnpackingTransformer().transform(
        """
        {1: 1, **dict_a}
        """
    )
    assert actual == merge_dicts() + """
        {1: 1, 2: 2}
        """

# Generated at 2022-06-14 01:52:18.008792
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    a = ast.Name(id='a')
    b = ast.Name(id='b')
    statement1 = ast.Expr(value=ast.Dict(keys=[a, None], values=[b, a]))
    statement2 = ast.Expr(value=ast.Dict(keys=[a, None], values=[b, a]))
    statement3 = ast.Expr(value=ast.Dict(keys=[None, a], values=[a, b]))
    statements = [statement1, statement2, statement3]
    module = ast.Module(body=statements)
    DictUnpackingTransformer().visit(module)

# Generated at 2022-06-14 01:52:25.875919
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ast import literal_eval

    def to_ast(text):
        return literal_eval(text)


# Generated at 2022-06-14 01:52:46.798502
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from ..utils.node import Node
    assert Node('_py_backwards_merge_dicts = merge_dicts()') == \
           DictUnpackingTransformer().visit(Node('pass'))



# Generated at 2022-06-14 01:52:53.627324
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    x = ast.parse("""
    def f():
        a = {1: 2}
    """)

    res = ast.parse("""
    def f():
        a = _py_backwards_merge_dicts([{1: 2}])
    """)

    assert ast.dump(DictUnpackingTransformer().visit(x)) == ast.dump(res)


# Generated at 2022-06-14 01:53:03.131453
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    from ..parser import parse
    from ..utils.simplification import simplify_syntax
    from ..transformer.utils import apply_transforms

    transformer = DictUnpackingTransformer()

    code = '''
        a = {1: 2, **d}
        {1: 2, **d}
        {1: 2}
        {1: 2, 3: 4, **d}
        {k1: v1, **d, k2: v2}
        {k1: v1, k2: v2, **d, k3: v3}
        {**d, **f}
    '''
    ctx = dict(a=1, b=2, c=3, d=4, e=5)

# Generated at 2022-06-14 01:53:09.539102
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    python_code = '''a = {None: 1, 2: 2, None: 3}'''
    tree = ast.parse(python_code)

    transformer = DictUnpackingTransformer()
    transformer.visit(tree)

    assert transformer._tree_changed

# Generated at 2022-06-14 01:53:12.259811
# Unit test for constructor of class DictUnpackingTransformer
def test_DictUnpackingTransformer():
    print('Testing constructor of ' + str(DictUnpackingTransformer))
    DictUnpackingTransformer()

# Generated at 2022-06-14 01:53:20.475678
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    class TestVisitor(ast.NodeVisitor):
        def __init__(self):
            self.imports = []

        def generic_visit(self, node):
            pass

        def visit_Import(self, node: ast.Import):
            self.imports.extend([alias.name for alias in node.names])
            super().generic_visit(node)


# Generated at 2022-06-14 01:53:28.000381
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from ..transformer import Transformer
    
    code = '''
    {1:2, 3:4, 5:6, **a, **b, 7:8, **c, 9:10}
    '''
    result = Transformer().transform_source(code, target=(3, 4), 
                                            backend='ast')
    expected = '''
    _py_backwards_merge_dicts([{'1': 2, '3': 4, '5': 6, '7': 8, '9': 10}], a, 
    b, c)'''
    assert result == expected


# Generated at 2022-06-14 01:53:35.724579
# Unit test for method visit_Module of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from textwrap import dedent

    t = DictUnpackingTransformer()
    m = ast.parse(dedent('''\
    {1:1, 2:2, **kwargs}
    '''))

    t.visit(m)

    assert dedent('''\
    _py_backwards_merge_dicts([{1:1, 2:2}], kwargs)
    ''') == astor.to_source(m)

# Generated at 2022-06-14 01:53:46.873735
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    import astor

    def expect(source, expected):
        actual = astor.to_source(DictUnpackingTransformer().visit(ast.parse(source)))
        assert actual == expected

    # more complicated test
    expect("""{1: 1, 2: 1, **dict_a, 3: 1, **dict_b, 4: 1, **dict_c}""",
           """_py_backwards_merge_dicts([{1: 1, 2: 1}, dict_a, {3: 1},
                                         dict_b, {4: 1}, dict_c])""")

    # simple test

# Generated at 2022-06-14 01:53:56.363291
# Unit test for method visit_Dict of class DictUnpackingTransformer
def test_DictUnpackingTransformer_visit_Dict():
    from .. import compile_pipeline

    code = '''
        x = {'a': 1, 2: 3, None: f()}
        y = {2: 3, **g()}
        z = {'a': 1, 2: 3, **g(), None: f()}
    '''