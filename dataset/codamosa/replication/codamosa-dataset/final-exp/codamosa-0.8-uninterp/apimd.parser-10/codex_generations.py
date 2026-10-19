

# Generated at 2022-06-13 17:46:19.870179
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == \
           '| a | b |\n' \
           '|:---:|:---:|\n' \
           '| c | d |\n' \
           '| e | f |\n\n'



# Generated at 2022-06-13 17:46:27.734281
# Unit test for method api of class Parser
def test_Parser_api():
    from .utils import _parse
    from . import resolver

    # case 1
    parser = Parser()
    parser.api('', _parse('def f(): ...'))
    assert resolver.unparse(parser.doc[''].format('f')) == (
        '# f()\n\n'
        '*Full name:* `f`\n\n'
        '```eval_rst\n'
        '.. csv-table::\n'
        '   :header: "Arguments", "Type"\n'
        '   :widths: 15, 10\n\n'
        '   "return", "`None`"\n'
        '```')

    # case 2
    parser = Parser()

# Generated at 2022-06-13 17:46:36.012983
# Unit test for method compile of class Parser
def test_Parser_compile():
    p = Parser([])
    p.doc[''] = '[](#)'
    p.doc['.a'] = '{}\n\n'
    p.doc['.a.b'] = '{}'
    p.doc['.b'] = '{}\n'
    p.doc['.c'] = '{}\n\n\n'
    p.docstring['.a'] = "A"
    p.docstring['.a.b'] = "B"
    p.docstring['.b'] = "C"
    p.root['.a'] = '.a'
    p.root['.a.b'] = '.a'
    p.root['.b'] = '.b'
    p.root['.c'] = '.c'
    p.level['.a'] = 0
    p

# Generated at 2022-06-13 17:46:44.438711
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    from inspect import Parameter
    from typing import List, Optional, Tuple, Union
    from types import ModuleType
    from asttokens import ASTTokens
    from doc_extract.base import Parser, FunctionDef, arguments, arg, Name
    from doc_extract.base import Return, Constant
    # arguments
    parser = Parser()
    parser.alias['b.arg'] = 'arg'
    kwonlyargs = [arg('x', None), arg('y', None)]
    args = arguments(
        args=[arg('a', None)],
        kwonlyargs=kwonlyargs,
        defaults=[Constant(value=1)],
        kw_defaults=[Constant(value=None), Constant(value=True)]
    )
    # test
    p = parser.func_ann('b', args)
   

# Generated at 2022-06-13 17:46:53.511377
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    p = Parser(False, False, False)
    p.func_ann("root", [(arg("a", None), arg("b", None), arg("c", None))])
    p.func_ann("root", [arg("a", None), arg("b", None), arg("c", None)])
    p.func_ann("root", [arg("a", None), arg("b", None), arg("c", None)],
                has_self=False, cls_method=False)
    args = [arg("a", None), arg("b", None), arg("c", None)]
    p.func_ann("root", args, has_self=True, cls_method=True)
    p.func_ann("root", args, has_self=True, cls_method=False)

test_Parser_func_ann

# Generated at 2022-06-13 17:46:57.777377
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    def f(x: int, a: str = "") -> int: ...
    p = Parser(root='')
    p.func_api('', '', f.__annotations__['return'], 
               f.__annotations__['a'], has_self=False, cls_method=False)
    assert p.doc[''] == 'Argument | Type | Default\n--- | --- | ---\n' \
                        'x | int | \n' \
                        'a | str | ""\n' \
                        'return | int | \n'

# Generated at 2022-06-13 17:47:08.040338
# Unit test for method func_ann of class Parser

# Generated at 2022-06-13 17:47:11.210115
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == '''\
| a | b |
|:---:|:---:|
| c | d |
| e | f |

'''



# Generated at 2022-06-13 17:47:17.182579
# Unit test for function doctest
def test_doctest():
    assert doctest('>>> print("a")') == '```python\n>>> print("a")\n```'
    assert doctest('>>> print("a")\nok') == '```python\n>>> print("a")\n```\nok'
    assert doctest('>>> print("a")\n>>> print("b")') == '```python\n>>> print("a")\n>>> print("b")\n```'
    assert doctest('>>> print("a")\nok\n>>> print("b")') == '```python\n>>> print("a")\n```\nok\n```python\n>>> print("b")\n```'



# Generated at 2022-06-13 17:47:20.352330
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    node = Subscript(Name('typing.Union', Load),
                     Tuple(elts=[Name('A', Load), Name('B', Load)], ctx=Load()),
                     ctx=Load())
    assert unparse(Resolver('root', {}).visit(node)) == 'A | B'

# Generated at 2022-06-13 17:48:35.998206
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    # class Parser

    def check(name: str, ast: Module, *, toc: bool = False, link: bool = False):
        # Test case for class_api

        m: ModuleType = type('m', (), {'__file__': 'm.py'})
        Parser(toc=toc, link=link).load(m, ast)
        assert Parser(toc=toc, link=link).compile() == name

# Generated at 2022-06-13 17:48:41.854688
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == '''\
| a | b |
|:---:|:---:|
| c | d |
| e | f |

'''
    assert table('a') == '''\
| a |
|:---:|

'''
    assert table() == '''\

'''

# Generated at 2022-06-13 17:48:51.209459
# Unit test for function const_type
def test_const_type():
    from .test.test_const_type import _expr

# Generated at 2022-06-13 17:48:58.728841
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    p = Parser()
    node = FunctionDef(name="test", args=arguments(), returns=None)
    name = "test"
    p.func_api(name, node.args, node.returns, has_self=True, cls_method=False)
    assert p.doc[name] == '\n'.join([
        '# test()',
        '',
        '*Full name:* `test`',
        '',
        '**Arguments**',
        '',
        '| Name | Type |',
        '|:----:|:----:|',
        '| type[Self] |  |',
        '',
    ])
    node = ClassDef(name="", bases=[], keywords=[],
                    body=[], decorator_list=[])
    name = "test"