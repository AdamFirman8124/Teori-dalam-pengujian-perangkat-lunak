

# Generated at 2022-06-14 02:16:59.317838
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test the constructor.

    """
    assert StringTypesTransformer.name == 'StringTypesTransformer'
    assert StringTypesTransformer.target == (2, 7)

# Generated at 2022-06-14 02:17:05.663287
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    data = (
        ('class foo():\n    pass', 'class foo():\n    pass', False),
        (
            'x = str',
            'x = unicode',
            True,
        ),
    )

    for code, result, changed in data:
        tree = ast.parse(code)
        result = ast.parse(result)
        result = StringTypesTransformer.transform(tree)
        assert result.tree == result, 'Transformation did not match result'
        assert result.tree_changed == changed, 'Transformation change flag did not match'

# Generated at 2022-06-14 02:17:12.166983
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_code = "def foo(bar): return str(bar)"
    expected_tree = ast.parse("def foo(bar): return unicode(bar)")

    transformer = StringTypesTransformer()
    actual_tree = transformer.transform(ast.parse(input_code))

    assert actual_tree.changes
    assert ast.dump(actual_tree.tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:17:20.677708
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from . import test
    from ..utils.source import Source
    from ..utils.tree import dump

    source = Source("""
        import io
        import os
        import sys

        def f():
            return str('hello')
    """)

    tree = test.apply_transform_to_single_file(source, StringTypesTransformer)
    assert dump(tree) == """
        import io
        import os
        import sys

        def f():
            return unicode('hello')
    """
    print("Unit test for StringTypesTransformer has passed.")
    return

# Invoke unit test
if __name__ == '__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:17:24.926101
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('a = str(1)')) == TransformationResult(tree=ast.parse('a = unicode(1)'), tree_changed=True, dependencies=[] )

# Generated at 2022-06-14 02:17:34.945452
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3
    from .string import StringTransformer
    from .utils import backport_function_def, backport_simple_stmt, backport_name_for_expr, backport_binary_operator_to_function_call
    from . import utils

    tree = ast3.parse('a = str(b)', mode='exec')
    tree = backport_function_def(tree, tree.body[0])
    tree = backport_simple_stmt(tree, tree.body[0].value)
    tree = backport_name_for_expr(tree, tree.body[0].value.value)
    tree = backport_binary_operator_to_function_call(tree, tree.body[0].value.value.args[0])
    tree = StringTransformer.transform(tree)
   

# Generated at 2022-06-14 02:17:44.197387
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests the StringTypesTransformer class.
    
    """
    BaseTransformer.test_type_hint('str', 'unicode', StringTypesTransformer)
    BaseTransformer.test_type_hint('typing.Iterable[str]', 'typing.Iterable[unicode]', StringTypesTransformer)
    BaseTransformer.test_type_hint('typing.List[str]', 'typing.List[unicode]', StringTypesTransformer)
    BaseTransformer.test_type_hint('typing.List[typing.List[str]]', 'typing.List[typing.List[unicode]]', StringTypesTransformer)

# Generated at 2022-06-14 02:17:45.547344
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_ast


# Generated at 2022-06-14 02:17:52.185201
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast

    code = '''
    s = str(x)
    print(s)
    '''

    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)

    code_after_transform = '''
    s = unicode(x)
    print(s)
    '''

    tree_after_transform = ast.parse(code_after_transform)

    assert ast.dump(tree, annotate_fields=False) == ast.dump(tree_after_transform, annotate_fields=False)

# Generated at 2022-06-14 02:17:54.108543
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    import tempfile


# Generated at 2022-06-14 02:17:56.819436
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor

# Generated at 2022-06-14 02:18:08.357005
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..transformer import Transformer

    code = '''def f(x: str, y: int) -> str:
        x = y
        print('Hello World!')
        return "abcd"
        '''
    expected_code = '''def f(x: unicode, y: int) -> unicode:
        x = y
        print('Hello World!')
        return "abcd"
        '''

    tree = ast.parse(code)
    transformer = Transformer(tree)
    transformer.add_transformer(StringTypesTransformer)

    tree = transformer.transform()
    assert ast.dump(tree) == expected_code

# Generated at 2022-06-14 02:18:14.939627
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for constructor of class StringTypesTransformer"""

    # Create AST
    ast_tree = ast.parse(
        'if True:\n'
        '    a, b = 1, str(1)'
    )

    # Transform
    transformer = StringTypesTransformer()
    new_ast_tree = transformer.transform(ast_tree)


# Generated at 2022-06-14 02:18:15.734916
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:18:21.542203
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse(
        "spam = str('eggs')"
        , mode='exec')
    print(ast.dump(tree))
    print(ast.dump(StringTypesTransformer.transform(tree).tree))

    assert ast.dump(StringTypesTransformer.transform(tree).tree) == \
        "Module(body=[Assign(targets=[Name(id='spam', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Str(s='eggs')], keywords=[]))])"

    tree = ast.parse(
        "import collections\nspam = collections.namedtuple('eggs', 'bacon')"
        , mode='exec')
    print(ast.dump(tree))
   

# Generated at 2022-06-14 02:18:22.088185
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:18:25.928455
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str_wrap("str")')
    result = StringTypesTransformer.transform(tree)

    assert str(result) == 'unicode_wrap("str")'

# Generated at 2022-06-14 02:18:37.051319
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    with open("test/fixtures/StringTypesTransformer.py") as f:
        tree = ast.parse(f.read())
        tree = StringTypesTransformer.transform(tree)

# Generated at 2022-06-14 02:18:40.843501
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assertion = 'def f(txt: unicode): pass'
    tree = ast.parse(assertion)
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed == True

# Generated at 2022-06-14 02:18:45.849790
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("a: str = 'Hello'")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed
    assert ast.dump(result.tree) == \
        "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Str(s='Hello'))])"

# Generated at 2022-06-14 02:18:54.092423
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
        def func():
            str_type = str
            str_name = str()
    """)

    transformed_source, tree_changed = StringTypesTransformer.transform(tree)
    assert tree_changed
    assert "str_type = unicode" in transformed_source
    assert "str_name = unicode()" in transformed_source



# Generated at 2022-06-14 02:18:57.188965
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    stringTypeTransformer = StringTypesTransformer()
    expected = ast.Name(id='unicode', ctx=ast.Load())
    actual = stringTypeTransformer.transform(ast.Name(id='str',ctx=ast.Load()))
    assert actual == expected


# Integration test for ColorFiltersTransformer

# Generated at 2022-06-14 02:19:04.585371
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer()
    node = ast.parse("s = str(2)")
    t.visit(node)
    assert ast.dump(node) == "Module(body=[Assign(targets=[Name(id='s', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Num(n=2)], keywords=[], starargs=None, kwargs=None))])"
    print("Test passed")


# Generated at 2022-06-14 02:19:12.677815
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    expected_tree = ast.Module(body=[ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Call(
            func=ast.Name(id='unicode', ctx=ast.Load()),
            args=[ast.Str(s='hello')],
            keywords=[])
    )])

    tree = ast.parse('x = str("hello")')
    tree = StringTypesTransformer.transform(tree)
    assert tree.tree == expected_tree

# Generated at 2022-06-14 02:19:19.284198
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # pylint: disable=protected-access
    my_transformer = StringTypesTransformer("2.7", "3.0")
    my_transformer.target = (2, 7)

    # Get a string and assert that it is a ast.Name, and that its id ("str") is a string
    assert not isinstance(my_transformer._BaseTransformer__target, ast.Str)
    assert isinstance(my_transformer._BaseTransformer__target, ast.Name)
    assert isinstance(my_transformer._BaseTransformer__target.id, str)
    # pylint: enable=protected-access

# Generated at 2022-06-14 02:19:29.991852
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # type: () -> None
    tree = ast.parse('''
      if True:
         var = str
         var2 = str(var)
    ''')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed


# Generated at 2022-06-14 02:19:30.854356
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:19:38.330579
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
#!/usr/bin/python
x = "hello"
print (x)
'''
    tree = ast.parse(code)
    expected_tree = ast.parse('''
#!/usr/bin/python
x = u"hello"
print (x)
    ''')
    tree2 = StringTypesTransformer.transform(tree)
    assert ast.dump(tree2, include_attributes=True) == ast.dump(expected_tree, include_attributes=True)
    assert tree2.tree_changed == True

# Generated at 2022-06-14 02:19:45.212344
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = 'str("Hello, World!")'
    expected = 'unicode("Hello, World!")'
    tree = ast.parse(source)

    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed
    assert ast.dump(result.tree) == ast.dump(ast.parse(expected))
    assert result.warnings == []

# Generated at 2022-06-14 02:19:48.669051
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:20:01.077248
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code_str = """
a = str()
if(str == str):
    return str
    """
    tree = ast.parse(code_str)
    res = StringTypesTransformer.transform(tree)
    new_code = astor.to_source(res.tree)
    expected_code = """
a = unicode()
if(unicode == unicode):
    return unicode
    """
    assert new_code == expected_code

# Generated at 2022-06-14 02:20:02.747359
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse
    # Before

# Generated at 2022-06-14 02:20:09.660188
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for StringTypesTransformer. 

    """
    from ..unparse import Unparser
    from .. import parse
    from .. import transform
    from ..utils.tree import print_tree

    code = "str('abc')"
    tree = parse(code)
    #print_tree(tree)
    tree, changed, _ = transform(tree, StringTypesTransformer)
    #print_tree(tree)
    code_out = Unparser(tree)
    assert code_out == "unicode('abc')"
    assert changed

# Generated at 2022-06-14 02:20:14.475248
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("foo = str(bar)")
    transformer = StringTypesTransformer()
    transformed, _ = transformer.transform(tree)
    assert transformed == ast.parse("foo = unicode(bar)")
    assert str(transformed) == "foo = unicode(bar)"



# Generated at 2022-06-14 02:20:17.508577
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    module = ast.parse('str ("abc")')
    StringTypesTransformer.transform(module)
    assert module != None
    """Unit test for constructor of class StringTypesTransformer"""
    

# Generated at 2022-06-14 02:20:24.534371
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    from typed_ast import ast3 as typed_ast
    from ..utils.source import source_to_unicode
    from .base import DefaultTransformer

    source = source_to_unicode('''
hello = 'world'
print(str(hello))
''')
    expected_source = source_to_unicode('''
hello = u'world'
print(unicode(hello))
''')
    expected_tree = ast.parse(source)
    expected_tree = DefaultTransformer().visit(expected_tree)
    result_tree = ast.parse(source)
    result_tree = StringTypesTransformer().visit(result_tree)

    assert typed_ast.dump(expected_tree) == typed_ast.dump(result_tree)

# Generated at 2022-06-14 02:20:27.385647
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    test_tree = ast.parse("str('cod3r')")

    result = StringTypesTransformer.transform(test_tree)
    
    assert result.tree_changed
    assert result.tree == ast.parse("unicode('cod3r')")

# Generated at 2022-06-14 02:20:36.205673
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Create AST
    string = ast.Str(s='x')
    type_ = ast.Name(__type=string,
                    id='str',
                    ctx=ast.Load())
    call = ast.Call(__type=ast.Str(s='x'),
                    func=type_,
                    args=[string],
                    keywords=[],
                    starargs=None,
                    kwargs=None)
    expr = ast.Expr(__type=ast.Str(s='x'),
                    value=call)
    body = [expr]
    statements = ast.Suite(__type=ast.Str(s='x'),
                            body=body)
    module = ast.Module(__type=ast.Str(s='x'),
                        body=statements)

    # Test transformation
    transformer = StringTypesTransformer()
   

# Generated at 2022-06-14 02:20:40.130619
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test for constructor of class StringTypesTransformer.

    """
    string_types_transformer = StringTypesTransformer()
    assert_equal(string_types_transformer.target, (2, 7))


# Generated at 2022-06-14 02:20:42.307281
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.__name__ == 'StringTypesTransformer'
    assert StringTypesTransformer.target == (2, 7)

# Generated at 2022-06-14 02:20:55.941063
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test the constructor
    StringTypesTransformer()
    # Nothing to test as only static methods are present
    return

# Generated at 2022-06-14 02:21:09.350682
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from .shared import get_ast
    parser = ast.Python27Parser()
    tree = parser.parse('a = str(b)')
    tree = StringTypesTransformer.transform(tree)
    tree = astor.to_source(tree)
    assert tree == 'a = unicode(b)\n', tree
    #
    tree = parser.parse('a = b.str')
    tree = StringTypesTransformer.transform(tree)
    tree = astor.to_source(tree)
    assert tree == 'a = b.unicode\n', tree
    #
    tree = parser.parse('from b import str')
    tree = StringTypesTransformer.transform(tree)
    tree = astor.to_source(tree)
    assert tree == 'from b import str\n', tree
    #


# Generated at 2022-06-14 02:21:16.860443
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    from typed_ast import ast3 as ast

    tree = ast.parse("""x = str('hello')""", mode='exec')

    result = StringTypesTransformer.transform(tree)
    assert isinstance(result.transformed, ast.Module)
    assert result.changed

    assert result.transformed.body[0].value.func.id == "unicode"

# Generated at 2022-06-14 02:21:20.682041
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(
        ast.parse('a = str(x)')
    ).new_tree == ast.parse('a = unicode(x)')

# Generated at 2022-06-14 02:21:22.054916
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:21:26.335270
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class_ = StringTypesTransformer()
    assert class_.target == (2, 7)
    assert isinstance(class_.transform('foo'), TransformationResult)

# Generated at 2022-06-14 02:21:27.633298
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer()

# Generated at 2022-06-14 02:21:32.516598
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('"Hello World"')
    t, _ = StringTypesTransformer.transform(tree)
    assert [n.id for n in find(t, ast.Name)] == ['unicode']
    assert [n.s for n in find(t, ast.Str)] == ['Hello World']

# Generated at 2022-06-14 02:21:35.450242
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    strings = ("foo bar baz")

    assert StringTypesTransformer().transform(strings) == ("foo bar baz")

# Generated at 2022-06-14 02:21:42.575290
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    # Build AST
    tree = ast.parse('''
a = str(b)
str(c)
isinstance(d, str)
e = str()
''')

    expected = ast.parse('''
a = unicode(b)
unicode(c)
isinstance(d, unicode)
e = unicode()
''')
    t = StringTypesTransformer()
    new_tree = t.transform(tree)
    assert astor.to_source(new_tree[0]) == astor.to_source(expected)

# Generated at 2022-06-14 02:22:09.890359
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        str
        s = 'now'
        """
    tree = ast.parse(code)
    out = StringTypesTransformer.transform(tree)
    assert out.code == """\
unicode
s = 'now'
"""

# Generated at 2022-06-14 02:22:16.028646
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('''
        str(1)
        1 + str(1) + 1
        "string"
        ''')
    expected_tree = ast.parse('''
        unicode(1)
        1 + unicode(1) + 1
        "string"
        ''')

    assert StringTypesTransformer.transform(tree).tree == expected_tree

# Generated at 2022-06-14 02:22:25.804079
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..types import TestCase as TestCase
    from ..utils.source import Source
    from ..utils.tree import file_to_ast


# Generated at 2022-06-14 02:22:27.421640
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:22:31.057372
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    a = 'def f(): str'
    b = 'def f(): unicode'
    assert StringTypesTransformer.transform(ast.parse(a)).code == b

# Generated at 2022-06-14 02:22:36.424143
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse
    my_ast = ast.parse("""
    a = str()
    b = 'abc'
    c = 'ab' + 'c'
    """)
    StringTypesTransformer.transform(my_ast)
    expected = """
    a = unicode()
    b = 'abc'
    c = 'ab' + 'c'
    """
    assert astunparse.unparse(my_ast) == expected

# Generated at 2022-06-14 02:22:43.668158
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    data = ast.parse("x = str(y) + ' ' + str(z)")
    tree = StringTypesTransformer.transform(data).tree
    assert ast.dump(tree, annotate_fields=False) == ast.dump(data, annotate_fields=False).replace("'str'", "'unicode'")

# Generated at 2022-06-14 02:22:52.672780
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3
    from .utils import roundtrip, compare_ast

    compare_ast(StringTypesTransformer.run("a = str(b)"), "a = unicode(b)")
    compare_ast(StringTypesTransformer.run("a = isinstance(b, str)"), "a = isinstance(b, unicode)")
    compare_ast(StringTypesTransformer.run("a = type(b) == str"), "a = type(b) == unicode")

# Generated at 2022-06-14 02:22:59.678405
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_tree
    from . import traverse

    source = '''
    # a python file
    from typing import Optional

    def foo(bar: str) -> Optional[str]:
        pass
    '''
    tree = source_to_tree(source)
    new_tree = StringTypesTransformer.run_on_tree(tree)
    traverse(new_tree)

    assert isinstance(new_tree, ast.AST)  # type: ignore



# Generated at 2022-06-14 02:23:08.656921
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_tree

    input_source = '''
x = "abc"
y = unicode
z = str
'''
    expected_source = '''
x = u"abc"
y = unicode
z = unicode
'''

    input_tree = source_to_tree(input_source)
    expected_tree = source_to_tree(expected_source)

    actual_tree, transformed = StringTypesTransformer.transform(input_tree)

    assert transformed
    assert expected_tree == actual_tree



# Generated at 2022-06-14 02:23:59.300390
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert True

# Generated at 2022-06-14 02:23:59.908973
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
   pass

# Generated at 2022-06-14 02:24:05.720876
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Creating the AST
    tree = ast.parse('def dummy_func(a):\n    return str(a)')
    # Creating transformer instance
    transformer = StringTypesTransformer()
    # Applying transformations
    new_tree = transformer.visit(tree)
    # Asserting new tree is as expected
    assert str(new_tree) == 'def dummy_func(a):\n    return unicode(a)\n'

# Generated at 2022-06-14 02:24:19.325491
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .base import create_module
    from .base import create_normalized_ast
    from .base import generate_source_code

    # Create a module
    tree = create_module()

    # Add the class declaration
    cls = ast.ClassDef(name='TestStringTypesTransformer',
                       bases=[],
                       keywords=[],
                       body=[],
                       decorator_list=[])
    tree.body.append(cls)

    # Add a function

# Generated at 2022-06-14 02:24:21.178600
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests the functionality of the StringTypesTransformer on a sample source file.

    """


# Generated at 2022-06-14 02:24:26.015768
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Single str
    code = "x = str(y)"
    tree = ast.parse(code)
    new_tree = StringTypesTransformer.transform(tree).tree
    assert ast.dump(new_tree) == ast.dump(ast.parse("x = unicode(y)"))

    # Multiple str
    code = "x = str(y)\nprint(str(x))"
    tree = ast.parse(code)
    new_tree = StringTypesTransformer.transform(tree).tree
    assert ast.dump(new_tree) == ast.dump(ast.parse("x = unicode(y)\nprint(unicode(x))"))

# Generated at 2022-06-14 02:24:29.164543
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from astor.source_repr import dump_python_source
    from .. import transform


# Generated at 2022-06-14 02:24:39.059466
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .helpers import assert_transform
    from typed_ast import ast3 as ast
    string_types_transformer = StringTypesTransformer()
    tree_changed = string_types_transformer.transform(ast.parse('''
    class Test(object):
        def __init__(self, arg: str):
            self.arg = arg
    '''))
    assert_transform(tree_changed, '''
    class Test(object):
        def __init__(self, arg: unicode):
            self.arg = arg
    ''')
    tree_changed = string_types_transformer.transform(ast.parse('''
    class Test(object):
        def __init__(self, arg: str):
            self.arg = arg
        def test(self):
            pass
    '''))
    assert_

# Generated at 2022-06-14 02:24:40.844521
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    StringTypesTransformer.transform(ast.parse('a = str(1)'))

# Generated at 2022-06-14 02:24:46.521512
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
v = str(1)
    """
    expected_result = """
v = unicode(1)
    """
    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed
    assert ast.dump(result.new_tree) == ast.dump(ast.parse(expected_result))

# Generated at 2022-06-14 02:26:42.505600
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:26:47.382929
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    print('Test StringTypesTransformer')
    tree = ast.parse('str()')
    res = StringTypesTransformer.transform(tree)
    assert ast.dump(res.tree) == ast.dump(ast.parse('unicode()'))

# Generated at 2022-06-14 02:26:51.376536
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # assertEqual is in unittest
    assert (StringTypesTransformer(2, 7).tree is None)
    assert (StringTypesTransformer(2, 7).tree_changed is False)
    assert (StringTypesTransformer(2, 7).warnings is None)

# Generated at 2022-06-14 02:26:57.692479
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Str

    #make a tree
    tree = ast.Str("abc")
    assert tree.s == "abc"

    # make a transformer
    transformer = StringTypesTransformer()

    # test transformation
    transformed_tree, changed_tree = transformer.transform(tree)

    assert isinstance(transformed_tree, ast.Str)
    assert not changed_tree
    assert tree.s == "abc"
    assert transformed_tree.s == "abc"