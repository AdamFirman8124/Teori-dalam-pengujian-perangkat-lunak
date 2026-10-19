

# Generated at 2022-06-13 17:45:00.984116
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    """Test class parser."""
    doc = {'abc.abc': '', 'abc.abc.abc': ''}
    alias = {}
    parser = Parser(doc, alias, {}, {}, False)

# Generated at 2022-06-13 17:45:06.608923
# Unit test for method imports of class Parser
def test_Parser_imports():
    root = 'media_download'
    node = Import([alias("img_load", "MediaDownload"), alias("_img_load", "_MediaDownload")])
    parser = Parser()
    parser.imports(root, node)
    assert parser.alias == {
        f'{root}.img_load': 'MediaDownload',
        f'{root}._img_load': '_MediaDownload'
    }
    assert parser.imp == {}

# Generated at 2022-06-13 17:45:15.132376
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():
    m = module_from_spec(spec('dummy'))
    m.__spec__.origin = '<dummy>'
    m.__doc__ = """Docstring of dummy module."""
    p = Parser(link=False, toc=False)
    p.load_docstring('dummy', m)
    p.docstring['dummy']
    p.docstring['dummy.__dict__']
    p.docstring['dummy.__init__']
    p.docstring['dummy.__name__']
    p.docstring['dummy.__package__']
    p.docstring['dummy.__spec__']
    p.docstring['dummy.__loader__']
    p.docstring['dummy.__file__']

# Generated at 2022-06-13 17:45:26.095783
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    # Union
    e = parse('typing.Union[int, str]').body[0]
    assert unparse(Resolver('a', {}).visit(e)) == '(int | str)'
    # Optional
    e = parse('typing.Optional[str]').body[0]
    assert unparse(Resolver('a', {}).visit(e)) == '(str | None)'
    # PEP585
    e = parse('typing.Sequence[str]').body[0]
    assert unparse(Resolver('a', {}).visit(e)) == 'list[str]'
    # PEP604
    e = parse('typing.AsyncGenerator[str, int]').body[0]

# Generated at 2022-06-13 17:45:32.541887
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    """Unit test for Parser.class_api"""
    import ast
    import inspect
    def parse(a_class):
        """Helper function to parse class AST"""
        return Parser().class_api('', ClassDef(
            name=a_class.__name__,
            bases=[Name(id=b.__name__, ctx=Load()) for b in a_class.__bases__],
            body=[Assign(targets=[Name(id=k, ctx=Store())], value=Constant(
                value=v)) for k, v in a_class.__dict__.items()]))
    class A:
        """A docstring"""
        pass
    class B(A):
        """B docstring"""
        pass
    class C(A):
        """C docstring"""

# Generated at 2022-06-13 17:45:37.285378
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    """Unit test for Resolver.visit_Name"""
    doc = """
    x = 0
    a = x
    assert a == 0
    """
    r = Resolver(None, {})
    assert r.visit_Name(ast.parse(doc).body[1].value) == ast.parse("x").body[0].value



# Generated at 2022-06-13 17:45:41.252232
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == \
        '| a | b |\n|:---:|:---:|\n| c | d |\n| e | f |\n\n'



# Generated at 2022-06-13 17:45:52.422111
# Unit test for method imports of class Parser
def test_Parser_imports():
    p = Parser(None, None, None, False)
    p.alias = {
        "os.path": "os_path",
        "collections.abc": "collections_abc",
        "collections.abc.SS": "SS",
        "abc": "abc",
        "abc.A": "A",
        "abc.A.B": "B",
        "abc.A.B.C": "C",
    }
    p.root = {
        "SS": "collections.abc.SS",
        "A": "abc.A",
        "B": "abc.A.B",
        "C": "abc.A.B.C",
    }
    p.imports("abc", Import([alias("sys", "sys"), alias("os", "os")]))

# Generated at 2022-06-13 17:46:01.002466
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    try:
        from types import ModuleType
    except ImportError:
        return
    alias = {
        'typing': 'typing',
        'typing.Optional': 'typing.Optional',
        'typing.Union': 'typing.Union',
        'typing.Tuple': 'typing.Tuple',
    }
    assert Resolver('typing', alias).visit_Subscript(
        Subscript(Name('Tuple', Load), Tuple([Constant(1), Constant(2)], Load),
                  Load())
    ) == Tuple([Constant(1), Constant(2)], Load())

# Generated at 2022-06-13 17:46:05.953254
# Unit test for method compile of class Parser
def test_Parser_compile():
    # method compile
    p = Parser(link=False)
    p.feed_from_file(TEST_DATA_PATH / "test_module.py")
    doc = p.compile()

# Generated at 2022-06-13 17:48:09.749601
# Unit test for function doctest
def test_doctest():
    assert doctest('\n>>> print("Hello world.")\nHello world.\n') == (
        '\n```python\n>>> print("Hello world.")\nHello world.\n```\n'
    )
    assert doctest('\n>>> print("Hello world.")\nHello world.\nNo sign.') == (
        '\n```python\n>>> print("Hello world.")\nHello world.\n```\nNo sign.'
    )
    assert doctest('No sign.\n>>> print("Hello world.")\nHello world.\n') == (
        'No sign.\n```python\n>>> print("Hello world.")\nHello world.\n```\n'
    )

# Generated at 2022-06-13 17:48:19.125444
# Unit test for function const_type
def test_const_type():
    # Test for boolean
    t = parse("True")
    assert const_type(t.body[0]) == "bool"
    t = parse("False")
    assert const_type(t.body[0]) == "bool"
    # Test for int
    t = parse("1234")
    assert const_type(t.body[0]) == "int"
    t = parse("0x1234")
    assert const_type(t.body[0]) == "int"
    t = parse("0o1234")
    assert const_type(t.body[0]) == "int"
    t = parse("0b1001100010")
    assert const_type(t.body[0]) == "int"
    # Test for float
    t = parse("1234.5678")

# Generated at 2022-06-13 17:48:26.127954
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    from astroid import extract_node
    from astroid.builder import ASTNGBuilder
    from pyls_ms_pytype.logger import Logger
    logger = Logger()
    parser = Parser(logger)
    module = 'class Parent: ...\n\n' \
             'class Child(Parent):\n' \
             '    pass\n'
    module = ASTNGBuilder(logger=logger).string_build(module)
    body = module.body
    assert len(body) == 2
    classdef = extract_node('''
    class Child(Parent):
        pass
    ''')
    parser.class_api('', classdef, [], body[1].body)

# Generated at 2022-06-13 17:48:36.151700
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    # Simple test
    p = Parser()
    args = (
        arg('self', None),
        arg('a', Name('int')),
        arg('*_', None),
        arg('return', None),
    )
    ans = ['Self', 'int', '...', 'Any']
    for a, b in zip(ans, p.func_ann('', args, has_self=True)):
        assert a == b
    # Advanced test
    p = Parser()

# Generated at 2022-06-13 17:48:45.802859
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    p = Parser()
    assert list(p.func_ann('a', [], has_self=True, cls_method=False)) == ['type[Self]']
    assert list(p.func_ann('a', [], has_self=True, cls_method=True)) == ['type[Self]']
    assert list(p.func_ann('a', [], has_self=False, cls_method=False)) == []
    assert list(p.func_ann('a', [], has_self=False, cls_method=True)) == []
    assert list(p.func_ann('a', [arg('', None)],
                           has_self=True, cls_method=False)) == ['type[Self]', ANY]

# Generated at 2022-06-13 17:48:54.432089
# Unit test for function const_type
def test_const_type():
    """Unit test for function const_type."""
    assert const_type(parse('"Test"', mode='eval')) == 'str'
    assert const_type(parse('1j', mode='eval')) == 'complex'
    assert const_type(parse('1', mode='eval')) == 'int'
    assert const_type(parse('1.0', mode='eval')) == 'float'
    assert const_type(parse('True', mode='eval')) == 'bool'
    assert const_type(parse('[1, 1.0]', mode='eval')) == 'list[int, float]'
    assert const_type(parse('{1, 1.0}', mode='eval')) == 'set[float, int]'

# Generated at 2022-06-13 17:48:59.037237
# Unit test for function is_public_family
def test_is_public_family():
    assert not is_public_family(__name__)
    assert is_public_family('a')
    assert not is_public_family('a.__b')
    assert not is_public_family('a._b')
    assert is_public_family('a.b')
    assert is_public_family('a.b.__c')
    assert not is_public_family('a.b._c')
    assert is_public_family('a.b.c')



# Generated at 2022-06-13 17:49:08.702455
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    from python_todo.python_todo.parser import Parser
    from python_todo.python_todo import ast
    from python_todo.python_todo import ast_ext
    from python_todo.python_todo.lexer import Lexer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    p = Parser()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    