

# Generated at 2022-06-13 17:45:19.499312
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == '''
| a | b |
|:---:|:---:|
| c | d |
| e | f |

'''



# Generated at 2022-06-13 17:45:27.202682
# Unit test for function walk_body
def test_walk_body():
    tester = [
        'if True:\n    try:\n        do()\n    except:\n        do()\n    else:\n        do()\n    finally:\n        do()\n',
        'if True:\n    a = 1\n    if True:\n        a = 2\n'
    ]
    answer = ['do()\n', 'a = 1\na = 2\n', 'do()\n', 'do()\n', 'do()\n', 'a = 1\na = 2\n']
    for test in tester:
        assert list(walk_body(parse(test).body)) == answer[:len(answer) // 2]



# Generated at 2022-06-13 17:45:37.793476
# Unit test for function doctest
def test_doctest():
    test = '''
>>> a = 1
>>> a
1
'''
    assert doctest(test) == '''
```python
>>> a = 1
>>> a
1
```
'''
    test = '''
>>> a = 1
>>> a
1
>>> a = 1
>>> a
1
>>> a = 1
>>> a
1
>>> a = 1
>>> a
1
'''
    assert doctest(test) == '''
```python
>>> a = 1
>>> a
1
```
>>> a = 1
>>> a
1
```python
>>> a = 1
>>> a
1
```
'''



# Generated at 2022-06-13 17:45:47.231343
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    doc = {}
    Parser(doc).func_api('root', 'func', arguments(
        [arg('a', Name(id='int', ctx=Load()))], None, None, [], [], None,
        [arg('b', Name(id='list', ctx=Load()))], None),
                          None, has_self=False, cls_method=False)

# Generated at 2022-06-13 17:45:57.034278
# Unit test for method api of class Parser

# Generated at 2022-06-13 17:46:03.719462
# Unit test for function doctest
def test_doctest():
    assert doctest("Hello world.") == "Hello world."
    assert doctest(">>> print('Hello world.')") == "```python\n>>> print('Hello world.')\n```"
    assert doctest(">>> print('Hello world.')\nHello world.") == "```python\n>>> print('Hello world.')\n```\nHello world."
    assert doctest("Hello world.\n>>> print('Hello world.')") == "Hello world.\n```python\n>>> print('Hello world.')\n```"
    assert doctest("Hello world.\n>>> print('Hello world.')\nHello world.") == "Hello world.\n```python\n>>> print('Hello world.')\n```\nHello world."

# Generated at 2022-06-13 17:46:14.232530
# Unit test for method api of class Parser

# Generated at 2022-06-13 17:46:24.702557
# Unit test for method globals of class Parser
def test_Parser_globals():
    parser = Parser(link=False, toc=False)
    root = 'test'
    parser.globals(root, parse('__all__ = [1, 2]')[0])
    parser.globals(root, parse('__all__ = (1, 2)')[0])
    parser.globals(root, parse('__all__ = ("a", "b")')[0])
    assert parser.imp[root] == {'test.1', 'test.2', 'test.a', 'test.b'}
    parser.imp = {root: {}}
    parser.globals(root, parse('__all__ = [1, "a"]')[0])
    assert parser.imp[root] == {'test.1', 'test.a'}

# Generated at 2022-06-13 17:46:34.763949
# Unit test for function const_type
def test_const_type(): # noqa
    assert const_type(parse('True').body[0].value) == 'bool'
    assert const_type(parse('False').body[0].value) == 'bool'
    assert const_type(parse('None').body[0].value) == 'NoneType'
    assert const_type(parse('1').body[0].value) == 'int'
    assert const_type(parse('3.14').body[0].value) == 'float'
    assert const_type(parse('3.14+2j').body[0].value) == 'complex'
    assert const_type(parse('"string"').body[0].value) == 'str'
    assert const_type(parse('"".join()').body[0].value) == 'str'

# Generated at 2022-06-13 17:46:43.895484
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    import pkgutil
    import doct
    std_lib = doct.import_('doct.std_lib')
    std_lib.add_hook(doct.doct_import)
    std_lib.doct_import()
    pkgs = [
        std_lib,
        doct.import_('typing'),
        doct.import_('functools'),
        doct.import_('unittest'),
        pkgutil.import_module('doct._parser'),
    ]
    parser = Parser(True, True)
    for p in pkgs:
        for imp in pkgutil.walk_packages(p.__path__):
            m = doct.import_(f"{p.__name__}.{imp.name}")
            parser.parse_package(m)

# Generated at 2022-06-13 17:48:51.245626
# Unit test for method globals of class Parser
def test_Parser_globals():
    """Unit test for method globals of class Parser."""
    p = Parser()
    p.globals("", Assign([Name("a", Load())], Constant("b")))
    assert p.alias["a"] == "b"

# Generated at 2022-06-13 17:48:58.522259
# Unit test for method globals of class Parser
def test_Parser_globals():
    """Test globals."""
    p = Parser(toc=False)
    p.globals('a', ast.parse('CLASS: str\n').body[0])
    p.globals('a', ast.parse('CONST: int\n').body[0])
    p.globals('a', ast.parse('__all__ = [1, 2]\n').body[0])
    assert p.alias == {'a.CLASS': 'str', 'a.CONST': 'int'}
    assert p.root == {'a.CONST': 'a'}
    assert p.const == {'a.CONST': 'int'}
    assert p.imp == {'a': {'a.1', 'a.2'}}
