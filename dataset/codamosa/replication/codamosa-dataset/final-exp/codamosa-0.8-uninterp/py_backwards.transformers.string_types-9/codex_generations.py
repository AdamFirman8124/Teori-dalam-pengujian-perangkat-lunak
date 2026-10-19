

# Generated at 2022-06-14 02:16:59.721078
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    test_tree = ast.parse('b = True')
    actual_tree, changed, messages = StringTypesTransformer.transform(test_tree)
    expected_tree = ast.parse('b = True')
    assert ast.dump(actual_tree) == ast.dump(expected_tree)

    test_tree = ast.parse('foo = str()')
    actual_tree, changed, messages = StringTypesTransformer.transform(test_tree)
    expected_tree = ast.parse('foo = unicode()')
    assert ast.dump(actual_tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:17:12.379898
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    foo = ast.Name(id='foo', ctx=ast.Load())
    bar = ast.Name(id='bar', ctx=ast.Load())

# Generated at 2022-06-14 02:17:13.507839
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:16.402640
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typing import List, Tuple
    # Test for transforming a simple example
    def simple_example():
        return 'Hello world'

# Generated at 2022-06-14 02:17:17.894511
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:17:22.590988
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("str('test')")).tree == ast.parse("unicode('test')")
    assert StringTypesTransformer.transform(ast.parse("test_str")).tree == ast.parse("test_str")

# Generated at 2022-06-14 02:17:28.459615
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    from typed_ast.transforms.string_types import StringTypesTransformer
    result = StringTypesTransformer.transform(ast.parse('str(3)', mode="eval"))
    assert result.code == 'unicode(3)'
    assert result.tree_changed is True

# Generated at 2022-06-14 02:17:32.199071
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
a = str(2)
"""

    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)
    exec(compile(tree, '', 'exec'), globals())

    assert a == '2'

# Generated at 2022-06-14 02:17:42.339441
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import os
    import sys
    module_path = os.path.dirname(__file__)
    module_path = os.path.join(module_path, '../../test_files/test_string_types.py')
    spec = importlib.util.spec_from_file_location('test_string_types', module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    tree = ast.parse(open(module_path, 'r').read())
    tree = StringTypesTransformer.transform(tree).tree

    # Check that the correct nodes were replaced
    assert 'unicode' in ast.dump(tree)
    assert 'str' not in ast.dump(tree)


# Generated at 2022-06-14 02:17:51.765054
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    x = str(1)
    y = unicode(2)
    """
    tree = ast.parse(code)
    res = StringTypesTransformer.transform(tree)
    assert res.tree == ast.parse(code)

    code = """
    x = str(1)
    y = str(2)
    """
    tree = ast.parse(code)
    res = StringTypesTransformer.transform(tree)
    assert res.tree == ast.parse("""
    x = unicode(1)
    y = unicode(2)
    """)

    code = """
    x = str(1)
    y = str(2)
    """
    tree = ast.parse(code)
    res = StringTypesTransformer.transform(tree)

# Generated at 2022-06-14 02:17:55.020235
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 02:18:01.601434
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Transforming single string
    tree1 = ast.parse('str("Hello World")')
    assert StringTypesTransformer.transform(tree1).tree == ast.parse('unicode("Hello World")')

    # Transforming multiple strings
    tree2 = ast.parse('str("1") + str("2")')
    assert StringTypesTransformer.transform(tree2).tree == ast.parse('unicode("1") + unicode("2")')

# Generated at 2022-06-14 02:18:03.139225
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    from ..utils import test_util

    test_util.assert_two_to_three_transformer(StringTypesTransformer)

# Generated at 2022-06-14 02:18:11.385440
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from .transformers import ast_transformer_factory, CODE_BOOL_REPR
    test_input = "print(b'0')"
    tree = ast.parse(test_input, mode='exec')
    expected_code = "print(b'0')"
    transformed_code = astor.to_source(tree)
    assert(expected_code == transformed_code)
    transformer = ast_transformer_factory(2, 7, CODE_BOOL_REPR)
    tree = transformer.transform(tree)
    transformed_code = astor.to_source(tree)
    assert(expected_code == transformed_code)



# Generated at 2022-06-14 02:18:22.133614
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for StringTypesTransformer
    """
    import sys
    import io

    tree = ast.parse('''
if True:
    print(str())
    x = str()
    y = foo(str="bar")
    z = foo(str="bar", str="baz")
    w = foo(bar, baz="baz", str="bar", str="baz")
    ''')

    expected = ast.parse('''
if True:
    print(unicode())
    x = unicode()
    y = foo(unicode="bar")
    z = foo(unicode="bar", unicode="baz")
    w = foo(bar, baz="baz", unicode="bar", unicode="baz")
    ''')

    refactored_tree = StringTypesTransformer.transform

# Generated at 2022-06-14 02:18:27.818727
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    x = str(1)
    """
    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)
    assert ast.dump(tree) == "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Num(n=1)], keywords=[], starargs=None, kwargs=None))])"

# Generated at 2022-06-14 02:18:38.775583
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..tests.utils import make_call, make_name
    root = ast.Module([
        ast.Assign([ast.Name(id='v1', ctx=ast.Store())], make_call(make_name('str'), []))
    ])

    t = StringTypesTransformer()
    new_tree = t.visit(root)

    assert isinstance(new_tree, ast.Module)
    assert isinstance(new_tree.body[0], ast.Assign)
    assert isinstance(new_tree.body[0].targets[0], ast.Name)
    assert new_tree.body[0].targets[0].id == 'v1'
    assert isinstance(new_tree.body[0].value, ast.Call)

# Generated at 2022-06-14 02:18:44.475389
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """my_string = str('string_value') """
    expected_code = """my_string = unicode('string_value') """
    tree = ast.parse(code)
    transformed_tree = StringTypesTransformer.transform(tree).tree
    transformed_code = astor.to_source(transformed_tree)
    assert transformed_code == expected_code



# Generated at 2022-06-14 02:18:48.832814
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    result = StringTypesTransformer.transform(ast.parse('str(2)'))
    assert result.changed
    result = StringTypesTransformer.transform(ast.parse('unicode(2)'))
    assert not result.changed



# Generated at 2022-06-14 02:18:49.844627
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:56.114055
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Given
    code = '''
        a = str('foo')
    '''
    expected_code = '''
        a = unicode('foo')
    '''

    # When
    tree = ast.parse(code)
    tree = StringTypesTransformer.transform(tree)

    # Then
    assert(expected_code == ast.unparse(tree))

# Generated at 2022-06-14 02:19:00.456408
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..codegen import to_source
    module_ast = ast.parse("str()")
    transformer = StringTypesTransformer()
    new_ast = transformer.visit(module_ast)
    assert to_source(new_ast) == "unicode()"

# Generated at 2022-06-14 02:19:08.954708
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    import astunparse
    import sys

    source = """\
x = 'str'
y = str
"""
    tree = ast.parse(source)
    print('Original tree:')
    print(astunparse.unparse(tree))
    trans = StringTypesTransformer()
    assert trans.target == (2, 7)
    new_tree = trans.transform(tree)
    print('Transformed tree:')
    print(astunparse.unparse(new_tree))
    assert new_tree == (ast.parse("""\
x = 'str'
y = unicode
"""))
    #assert trans.transform(tree) == ast.parse("""\
    #x = 'str'
    #y = unicode
    #""")


# Generated at 2022-06-14 02:19:17.072735
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class TestTransformer(BaseTransformer):
        """Test class containing correct and incorrect transformations.
        """

        @classmethod
        def transform(cls, tree: ast.AST) -> TransformationResult:
            tree_changed = False
            error_messages = []

            # Test correct transformation
            node = ast.Name(id='str', ctx=ast.Load())
            changed = StringTypesTransformer.transform(node)
            if node.id != 'unicode':
                error_messages.append('Strings in constructor does not change.')
            else:
                tree_changed = True

            changed = StringTypesTransformer.transform(tree)
            return TransformationResult(tree, tree_changed, error_messages)

    tree = ast.Module([])
    assert TestTransformer.transform(tree)

# Generated at 2022-06-14 02:19:20.751901
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    simple_test_string = "assert str is not unicode"

    print('Testing StringTypesTransformer')
    t = StringTypesTransformer()
    tree = ast.parse(simple_test_string)

    new_tree = t.transform(tree)

    assert new_tree.tree.body[0].test.left.id == "unicode"

# Generated at 2022-06-14 02:19:22.407105
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:19:31.000675
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_unicode
    from .base import apply_transformers
    source = source_to_unicode("""
        def foo(x):
            return str(x) + "bar"
    """)
    tree = ast.parse(source)
    transformer = StringTypesTransformer()
    new_tree = apply_transformers(tree, [transformer])
    assert new_tree.body[0].body.value.left.id == "unicode"
    assert new_tree.body[0].body.value.right.s == "bar"

# Generated at 2022-06-14 02:19:32.697006
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # The class is a singleton so we can just instantiate it
    transformer = StringTypesTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:19:39.455785
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    import typed_astunparse
    test_input = """
a = str('test')

print(a)
    """
    expected = """
a = unicode('test')

print(a)
    """
    t = ast.parse(test_input)
    res = StringTypesTransformer.transform(t)

    print(typed_astunparse.dump_ast(res.tree))
    assert typed_astunparse.dump_ast(res.tree).strip() == expected.strip()

# Generated at 2022-06-14 02:19:47.839139
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from textwrap import dedent
    from typed_ast import ast3, parse
    from typed_ast.py27 import c_ast27 as c_ast
    TT = StringTypesTransformer

    s = "str(1)"
    tree = parse(s)

    new_tree, changed, messages = TT.transform(tree)
    assert not changed
    print(ast.dump(new_tree))

    s = "unicode(1)"
    tree = parse(s)

    new_tree, changed, messages = TT.transform(tree)
    assert not changed
    print(ast.dump(new_tree))

    s = "a = str(1)"
    tree = parse(s)

    new_tree, changed, messages = TT.transform(tree)
    assert changed
    print(ast.dump(new_tree))

# Generated at 2022-06-14 02:19:58.731000
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test code
    test_code = "print(str(1))"
    # Expected result
    expected_code = "print(unicode(1))"
    # Run transformer
    result = StringTypesTransformer.transform(test_code)
    # Assert result is equal to expected code
    assert result.code == expected_code

# Generated at 2022-06-14 02:20:02.951183
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast.ast3 import Name

    tree = Name(id = 'str', ctx = Load())

    tree = StringTypesTransformer.transform(tree).new_tree

    assert(isinstance(tree, Name))
    assert(tree.id == 'unicode')

# Generated at 2022-06-14 02:20:04.636441
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:20:10.947487
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree_original = ast.parse('''
x = str()
    ''')

    tree_expected = ast.parse('''
x = unicode()
    ''')

    tree_transformed = StringTypesTransformer.transform(tree_original).tree

    assert ast.dump(tree_expected) == ast.dump(tree_transformed)

# Generated at 2022-06-14 02:20:23.286900
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Testing for class `StringTypesTransformer`."""

    # Test that `str` is replaced by `unicode`:
    assert StringTypesTransformer.transform(
        ast.parse('x = str("foo")')) == TransformationResult(
            ast.parse('x = unicode("foo")'), tree_changed=True, errors=[])

    # Test that `str` is also replaced in function calls:
    assert StringTypesTransformer.transform(
        ast.parse('x = str("foo").strip()')) == TransformationResult(
            ast.parse('x = unicode("foo").strip()'), tree_changed=True, errors=[])

    # Test that `str` is not replaced by `unicode` if it is not a variable:

# Generated at 2022-06-14 02:20:26.855227
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .tests.fixtures.string_types import before, after

    t = StringTypesTransformer.transform(before)
    assert ast.dump(t.tree) == ast.dump(after)

# Generated at 2022-06-14 02:20:28.949406
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:20:34.365896
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer()
    code = "name = 'string'"
    tree = ast.parse(code)
    new_tree = t.transform(tree)

    assert(new_tree.tree_changed == True)
    assert(ast.dump(new_tree.tree) == ast.dump(ast.parse("name = u'string'")))

# Generated at 2022-06-14 02:20:35.341241
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:20:37.240827
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    sample1 = """str"""
    sample2 = """str(variable)"""

# Generated at 2022-06-14 02:20:50.636092
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform([]) == TransformationResult([], False, [])

# Generated at 2022-06-14 02:20:55.745075
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer(): 
    tree = ast.parse('''
str('foo')
    ''')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed
    # There are better tests, but it's still a start
    assert ast.dump(result.tree) == ast.dump(ast.parse('''
unicode('foo')
    '''))

# Generated at 2022-06-14 02:21:09.211548
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # test string with unicode
    tree = ast.parse("""def g(a):
    b = a + u"abcd"
    
    if type(b) == str:
        pass
    """, mode='exec')
    new = StringTypesTransformer().visit(tree)
    assert ast.dump(new) == ast.dump(tree)

    # test string with unicode
    tree = ast.parse("""def g(a):
    b = a + "abcd"
    
    if type(b) == str:
        pass
    """, mode='exec')
    new = StringTypesTransformer().visit(tree)
    expected = "def g(a):\n    b = a + u\"abcd\"\n\n    if type(b) == unicode:\n        pass"

# Generated at 2022-06-14 02:21:15.989302
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_base import CodeMapTest
    import typed_ast.ast3 as ast

    tree = ast.parse("""\
import sys
print(str(123))
""")
    expected = ast.parse("""\
import sys
print(unicode(123))
""")

    CodeMapTest.test(StringTypesTransformer, tree, expected)

# Generated at 2022-06-14 02:21:24.475717
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    str_node = ast.Name(id='str', ctx=ast.Load())
    func = ast.FunctionDef(name='test', args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[ast.Return(value=str_node)], decorator_list=[], returns=None)
    tree = ast.Module(body=[func])
    res = StringTypesTransformer.transform(tree)
    assert isinstance(res.transform_result.body[0].body[0].value, ast.Name)
    assert res.transform_result.body[0].body[0].value.id == 'unicode'

# Generated at 2022-06-14 02:21:31.689247
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse

    code = """
        def test():
            t = str()
    """

    tree = ast.parse(code)
    ref_tree = ast.parse(code.replace('str', 'unicode'))

    trans = StringTypesTransformer()
    new_tree = trans.transform(tree)

    assert astunparse.unparse(new_tree.tree) == astunparse.unparse(ref_tree)

# Generated at 2022-06-14 02:21:36.684794
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # type: () -> None
    from ..transforms import TransformResult

    transformer = StringTypesTransformer()
    source = "str('Hello')"

    tree = ast.parse(source)
    transformer.transform(tree)

    result = TransformResult(tree, True, [])
    assert result.transformed



# Generated at 2022-06-14 02:21:42.262406
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    s = "b = str('test')\nprint(b)"
    expected = "b = unicode('test')\nprint(b)"

    t = ast.parse(s)
    t, modified, _ = StringTypesTransformer.transform(t)

    if modified:
        file_ast, _, _ = StringTypesTransformer.transform(file_ast)
        assert expected == compile(t, "<test>", "exec")



# Generated at 2022-06-14 02:21:51.591791
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        class MyClass:
            def __init__(self):
                self.str = str('Hello, World!')
                """
    correct_code = """
        class MyClass:
            def __init__(self):
                self.str = unicode('Hello, World!')
        """
    tree = ast.parse(code)
    transformed_tree = ast.parse(correct_code)

    tt = StringTypesTransformer()
    result = tt.transform(tree)

    assert(result.success == True)
    assert(result.tree == transformed_tree)

# Generated at 2022-06-14 02:21:55.711496
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
x = "abc"
s = str(x)
""")

    tt = StringTypesTransformer.transform(tree)
    assert tt.tree_changed
    assert tt.meta_data == []
    assert not tt.tree_changed
    assert tt.meta_data == []

# Generated at 2022-06-14 02:22:23.078509
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    r'''Unit test for constructor of class StringTypesTransformer.
    '''
    # pylint: disable=line-too-long

# Generated at 2022-06-14 02:22:24.383583
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = ast.parse('str')
    StringTypesTransformer.transform(t)

# Generated at 2022-06-14 02:22:28.798552
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    original_code: str = """
variable: str
"""
    expected_code: str = """
variable: unicode
"""

    t = StringTypesTransformer()
    t.transform_source(original_code)
    assert expected_code == t.output

# Generated at 2022-06-14 02:22:32.132862
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Given
    string1 = '''
        class MyTestClass( object ):
            def __init__( self ):
                print(str("Hello"))
    '''

    string2 = '''
    class MyTestClass( object ):
        def __init__( self ):
            print("Hello")
    '''


# Generated at 2022-06-14 02:22:36.986255
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Unit test for constructor of class StringTypesTransformer
    source = """
    # example
    x = 'hello'
    """
    expected = """
    # example
    x = u'hello'
    """
    tree = ast.parse(source)
    tree = StringTypesTransformer.transform(tree)
    actual = astor.to_source(tree.node)
    assert actual == expected

# Generated at 2022-06-14 02:22:40.051695
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # TODO: Add tests here.
    assert True

# ------------------------


# Generated at 2022-06-14 02:22:46.986634
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    program = ast.parse("x = str(2)")
    result = StringTypesTransformer.transform(program)
    assert result.tree_changed
    assert result.messages == []

    assert ast.dump(result.tree) == ast.dump(ast.parse("x = unicode(2)"))


# Generated at 2022-06-14 02:22:48.557062
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:22:57.881019
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('''
        def foo():
            name = str(1)
        ''')) == TransformationResult(ast.parse('''
        def foo():
            name = unicode(1)
        '''), tree_changed=True,
            static_errors=[])

    assert StringTypesTransformer.transform(ast.parse('''
        def foo():
            name = str
        ''')) == TransformationResult(ast.parse('''
        def foo():
            name = unicode
        '''), tree_changed=True,
            static_errors=[])

if __name__=='__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:23:10.388852
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    from typed_ast import (NodeTransformer, fix_missing_locations)

    example = """
    def f(x: str, y: str) -> str:
        return x + y

    print(f('hello ', 'world'))
    """

    result = """
    def f(x: unicode, y: unicode) -> unicode:
        return x + y

    print(f('hello ', 'world'))
    """

    tree = ast.parse(example)
    tree = fix_missing_locations(tree)
    transformer = NodeTransformer()
    transformer.visit(tree)

    tree2 = ast.parse(result)
    tree2 = fix_missing_locations(tree2)

    assert ast.dump(tree) == ast.dump(tree2)

# Generated at 2022-06-14 02:24:02.712906
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from typed_ast import parse as typed_ast_parse
    import sys

# Generated at 2022-06-14 02:24:15.451093
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast


    class Node(ast.AST):
        def __init__(self, str):
            self.str = str


    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node):
            return node


    class Transformer(ast.NodeTransformer):
        def visit_Name(self, node):
            return self.generic_visit(node)


    binop = ast.BinOp()
    binop.left = ast.Name('str')
    binop.op = ast.Add()
    binop.right = ast.Name('str')

    visitor = Visitor()
    name = visitor.visit(binop)
    print(name.id)  # str

    transformer = Transformer()

# Generated at 2022-06-14 02:24:19.253552
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for constructor of class StringTypesTransformer.

    """
    class_ = StringTypesTransformer
    assert isinstance(class_, type)
    assert issubclass(class_, BaseTransformer)



# Generated at 2022-06-14 02:24:27.504392
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests for the constructor of class StringTypesTransformer.
    
    """
    # Set up a dummy source code
    source = """
foo = str()
"""
    # Compile the source code into an AST
    tree = ast.parse(source)

    # Create an instance of StringTypesTransformer
    transformer = StringTypesTransformer()

    # Invoke the visit method
    transformed_tree, tree_changed, messages = transformer.transform(tree)

    # Verify the result
    assert tree_changed is True
    assert len(messages) == 0
    assert isinstance(transformed_tree, ast.AST)

# Generated at 2022-06-14 02:24:29.102865
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()


# Generated at 2022-06-14 02:24:30.719444
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    print("Unit test for constructor of class StringTypesTransformer")


# Generated at 2022-06-14 02:24:31.655021
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:24:35.369732
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str(0)')
    new_tree = StringTypesTransformer.transform(tree)
    node = new_tree.tree.body[0].value
    assert isinstance(node, ast.Call)
    assert (node.func.id) == 'unicode'

# Generated at 2022-06-14 02:24:47.984300
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
    def f(x):
        return str(x)
    """)

    transformer = StringTypesTransformer()
    transformed_tree = transformer.transform(tree)
    eval(compile(transformed_tree, filename="", mode="exec"))
    print('\n'.join(map(str, transformer.log)))


# unit test for class StringUnicodeTransformer
F = StringTypesTransformer()
assert F.transform(ast.parse("x")).tree == ast.parse("x")
assert F.transform(ast.parse("str")).tree == ast.parse("unicode")

assert F.transform(ast.parse("str(x)")).tree == ast.parse("unicode(x)")
assert F.transform(ast.parse("str(str(x))")).tree == ast.parse

# Generated at 2022-06-14 02:24:50.535074
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.fake import FakeTestingTreeBuilder

    FakeTestingTreeBuilder.test_transformer(StringTypesTransformer)

# Generated at 2022-06-14 02:26:44.266080
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:26:51.061000
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from pprint import pprint
    import ast, typed_ast.ast3
    from ..utils.tree import print_tree

    tree = ast.parse('str(1)')
    tree = typed_ast.ast3.fix_missing_locations(tree)
    print_tree(tree)
    pprint(StringTypesTransformer.transform(tree))


if __name__ == '__main__':
    test_StringTypesTransformer()