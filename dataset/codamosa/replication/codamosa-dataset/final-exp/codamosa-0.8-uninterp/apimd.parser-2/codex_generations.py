

# Generated at 2022-06-13 17:47:05.486322
# Unit test for method api of class Parser
def test_Parser_api():
    assert False

# Generated at 2022-06-13 17:47:13.690891
# Unit test for method api of class Parser
def test_Parser_api():
    p = Parser()
    p.api('a', FunctionDef(None, "foo", arguments(args=[]), None, []))
    assert p.doc["a.foo"].strip() == """\
# foo()

*Full name:* `a.foo`

|Argument|Annotation|
|:-------|:---------|
|return  |          |
"""
    p.doc = {}
    p.api('b', FunctionDef(None, "baz",
                           arguments(args=[arg('a', None), arg('b', None)]),
                           None, []))

# Generated at 2022-06-13 17:47:17.645054
# Unit test for function doctest
def test_doctest():
    assert doctest("") == ""
    assert doctest(">>> foo") == "```python\n>>> foo\n```"
    assert doctest(">>> foo\n\n>>> foo") == "```python\n>>> foo\n\n>>> foo\n```"
    assert doctest(">>> foo\n\n>>> bar") == "```python\n>>> foo\n```\n\n>>> bar"



# Generated at 2022-06-13 17:47:27.691833
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():
    def _test(m, m_file):
        p = Parser(m_file)
        vars = inspect.currentframe().f_back.f_locals.copy()
        for k in globals().keys():
            vars.pop(k)
        p.load_docstring('', m)
        actual_result = {}
        for k, v in p.docstring.items():
            actual_result[k] = vars.setdefault(k, v)
        return actual_result
    m_arg = ""
    m_file = join('my_path', 'my_file.py')
    m = ModuleType(m_file)
    assert _test(m, m_file) == {}
    assert m.__doc__ is None
    m.__doc__ = ''

# Generated at 2022-06-13 17:47:31.208999
# Unit test for function is_public_family
def test_is_public_family():
    if is_public_family("test.test"):
        raise ValueError("error")
    if is_public_family("test"):
        raise ValueError("error")
    if is_public_family("test.test2"):
        raise ValueError("error")
    if not is_public_family("test.__test2"):
        raise ValueError("error")
    if not is_public_family("test.__test2.__test"):
        raise ValueError("error")
test_is_public_family.__doc__ = """Test function is_public_family"""

# Generated at 2022-06-13 17:47:44.057753
# Unit test for method api of class Parser
def test_Parser_api():
    """Test Parser.api."""
    class Test(Parser):
        """Test class."""
        def __init__(self):
            """Initialize."""
            self.doc: Dict[str, str] = {}
            self.docstring: Dict[str, str] = {}

        def api(self, root: str, node: _API, *, prefix: str = '') -> None:
            """Override."""
            Parser.api(self, root, node, prefix=prefix)

    test = Test()

# Generated at 2022-06-13 17:47:52.934118
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    p = Parser()
    p.imp['foo'] = {'foo', 'foo.bar', 'foo.baz'}
    assert not p.is_public('foo.qux')
    p.imp['foo.baz'] = {'foo.baz.qux', 'foo.baz.quux'}
    assert not p.is_public('foo.baz.quux')
    p.imp['foo.baz'] = set()
    assert not p.is_public('foo.baz.quux')
    p.imp['foo'] = set()
    assert p.is_public('foo.baz.quux')
    assert not p.is_public('foo.qux')
    p.imp['foo'] = {'foo.qux'}

# Generated at 2022-06-13 17:47:58.662066
# Unit test for function doctest
def test_doctest():
    # Test comment lines
    doc = '''abc
    >>> a
    123
    '''
    assert doctest(doc) == '''abc
    >>> a
    123
    '''
    # Test lines with comment
    doc = '''# abc
    >>> a
    # 123
    '''
    assert doctest(doc) == '''# abc
    >>> a
    # 123
    '''
    # Test wrapped lines
    doc = '''>>> a = 123
    ... b = 456
    '''
    assert doctest(doc) == '''```python
    >>> a = 123
    ... b = 456
    ```
    '''
    # Test empty doctest
    doc = ''
    assert doctest(doc) == ''
    # Test doctest with suffix

# Generated at 2022-06-13 17:48:08.098658
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    import ast
    from . import annotations as py
    parser = Parser(None)
    pars = parser.func_ann('', [
        arg('param', py.parse(ast.parse('int'))),
        arg('param', py.parse(ast.parse('str'))),
        arg('return', py.parse(ast.parse('None'))),
    ], has_self=False, cls_method=False)
    assert list(pars) == ['int', 'str', 'None']
    pars = parser.func_ann('', [
        arg('param', py.parse(ast.parse('int'))),
        arg('return', py.parse(ast.parse('None'))),
    ], has_self=True, cls_method=False)

# Generated at 2022-06-13 17:48:17.893529
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    t = Parser()
    t.func_api('min', 'min.min', arguments(args=[], defaults=[]), None,
               has_self=False, cls_method=False)
    assert t.doc['min.min'] == '# min()\n\n*Full name:* `min`\n\n' + table(
        "Arguments", 'Type', items=[('return', 'typing.Any')])
    t.func_api('x', 'x.a.f', arguments(args=[], defaults=[]), None,
               has_self=False, cls_method=False)