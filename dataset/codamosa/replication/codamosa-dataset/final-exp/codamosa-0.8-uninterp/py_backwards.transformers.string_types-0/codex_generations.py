

# Generated at 2022-06-14 02:17:00.430799
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('''
        "abcd"
        "efg"
    ''')

    expected = ast.parse('''
        "abcd"
        "efg"
    ''')

    result = StringTypesTransformer.transform(tree)

    print(result)

    assert result.tree == expected
    assert result.tree_changed == False

# Generated at 2022-06-14 02:17:01.261855
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert hasattr(ast, 'Name')

# Generated at 2022-06-14 02:17:09.442267
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3
    x = ast3.Name(id='str', ctx=ast3.Load())
    y = ast3.Name(id='str', ctx=ast3.Load())

# Generated at 2022-06-14 02:17:16.514040
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    from ..utils.tree import to_src
    result = StringTypesTransformer.transform(ast.parse(u"def foo():\n    x = str('foo')\n    print(x)\n"))
    print(result.tree)
    print(to_src(result.tree))
    assert result.tree_changed is True
    assert to_src(result.tree) == "def foo():\n    x = unicode('foo')\n    print(x)\n"

# Generated at 2022-06-14 02:17:21.680440
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
nodes: double
  node_id: str
  """)
    actual_tree, _, _ = StringTypesTransformer.transform(tree)
    expected_tree = ast.parse("""
nodes: double
  node_id: unicode
  """)
    actual_tree == expected_tree

if __name__ == "__main__":
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:17:32.041177
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class AssertChecker(ast.NodeVisitor):
        def __init__(self):
            self.assert_called = False

        def visit_Assert(self, node):
            self.assert_called = True
            if not isinstance(node.test.left, ast.Name) and \
                    node.test.left.id == 'foo':
                raise Exception("assertion error")

    test_node = ast.parse("""assert foo == "bar"\n""")
    checker = AssertChecker()
    test_node = StringTypesTransformer.transform(test_node)
    checker.visit(test_node)
    assert checker.assert_called

# Generated at 2022-06-14 02:17:38.348491
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    stt = StringTypesTransformer()
    assert ast.dump(stt.transform('a = str(b)').tree) == \
        "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Name(id='b', ctx=Load())], keywords=[], starargs=None, kwargs=None))])"

# Generated at 2022-06-14 02:17:48.528572
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import sys
    import os
    import tempfile
    import unittest
    from contextlib import contextmanager
    from typed_ast import ast3 as ast

    from typed_astunparse import unparse

    from typed_astunparse.unparser import Unparser

    from .base import BaseTransformerTest

    class TestStringTypesTransformer(BaseTransformerTest):

        TRANSFORMER = StringTypesTransformer

        def test_str(self):
            code = 'str("a")'
            node = ast.parse(code)
            new_node = self.transform(node)
            Unparser(new_node, sys.stdout)
            self.assertEqual(unparse(new_node), 'unicode("a")')

    return TestStringTypesTransformer


# Generated at 2022-06-14 02:17:54.390414
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse
    import textwrap
    
    code = textwrap.dedent("""
        def foo(a):
            return str(a)
    """)

    tree = ast.parse(code)
    tree = StringTypesTransformer.transform(tree)
    print(astunparse.unparse(tree))

# Generated at 2022-06-14 02:17:58.407800
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    s = "a = str('aa')"
    expected = """a = unicode('aa')"""
    tr = StringTypesTransformer()
    assert tr.transform_single_file(s) == expected

# Generated at 2022-06-14 02:18:02.627740
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:06.901525
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = 'a = str(1)'
    expected = 'a = unicode(1)'
    tree = ast.parse(code)
    new_tree, _ = StringTypesTransformer.transform(tree)
    assert astor.to_source(new_tree).strip() == expected.strip()

# Generated at 2022-06-14 02:18:14.402217
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # these lines should be the same
    source = '''
a = str(2)
b = unicode(2)
'''
    expected_source = '''
a = unicode(2)
b = unicode(2)
'''
    t = StringTypesTransformer()
    tree = ast.parse(source)
    result = t.transform(tree)
    print(ast.dump(result.tree))
    assert ast.dump(result.tree) == ast.dump(ast.parse(expected_source))

# Generated at 2022-06-14 02:18:17.156531
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    s = "s = str('a')"
    t = astor.parse_file(s)
    tree = StringTypesTransformer().transform(t)
    pass

# Generated at 2022-06-14 02:18:21.204957
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
        s = str("Hello world")
    """)
    tree_transformed = StringTypesTransformer.transform(tree)
    tree_expected = ast.parse("""
        s = unicode("Hello world")
    """)
    assert tree_transformed.tree == tree_expected

# Generated at 2022-06-14 02:18:26.807661
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    node = ast.Name(id='str', ctx=ast.Load())
    result = StringTypesTransformer.transform(node)
    assert result.changed
    assert isinstance(result.tree, ast.Name)
    assert result.tree.id == 'unicode'

# Generated at 2022-06-14 02:18:30.535549
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_base import TestTransformerBase
    from . import example

    class TestStringTypesTransformer(TestTransformerBase):
        transformer = StringTypesTransformer

    TestStringTypesTransformer.run_tests(example)

# Generated at 2022-06-14 02:18:33.905601
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = ast.parse("a = str(b)")
    mt = ast.parse("a = unicode(b)")
    
    t = StringTypesTransformer.transform(t).tree
    compare_ast(t, mt)

# Generated at 2022-06-14 02:18:37.196643
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str')
    transformer = StringTypesTransformer.get_transformer()
    new_tree = transformer.transform(tree)
    assert ast.dump(new_tree) == ast.dump(ast.parse('unicode'))

# Generated at 2022-06-14 02:18:45.052658
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse

    test_code = """
s1 = str(my_var)
s2 = str(my_var)
    """

    tree = ast.parse(test_code)
    tree = StringTypesTransformer.transform(tree)[0]
    assert astunparse.unparse(tree) == """
s1 = unicode(my_var)
s2 = unicode(my_var)
    """.lstrip()

if __name__ == '__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:18:49.135349
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:50.587889
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class X(StringTypesTransformer):
        pass
    obj = X()

# Generated at 2022-06-14 02:18:51.565842
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:59.204004
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class TestVisitor(StringTypesTransformer):
        pass

    code = """
a = str(1)
"""
    tree = ast.parse(code)
    TestVisitor.run(tree)
    assert ast.dump(tree) == dedent("""
    (Module
      (Assign
        (targets=[Name(id='a', ctx=Store())])
        (value=Call(func=Name(id='unicode', ctx=Load()), args=[Num(n=1)], keywords=[]))))
    """).strip()

# Generated at 2022-06-14 02:19:08.456989
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # a = 'str'
    # print a
    test_code = """
a = 'str'
print a
    """
    expected_code = """
a = u'str'
print a
    """
    tree = ast.parse(test_code)
    tree = StringTypesTransformer.transform(tree).tree

    assert ast.unparse(tree) == expected_code

    # a = '%d' % 10
    # print a
    test_code = """
a = '%d' % 10
print a
    """
    expected_code = """
a = u'%d' % 10
print a
    """
    tree = ast.parse(test_code)
    tree = StringTypesTransformer.transform(tree).tree

    assert ast.unparse(tree) == expected_code

    # a = '%

# Generated at 2022-06-14 02:19:14.288988
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
a = str(2)
b = str(b)
c = 2
"""
    expected_code = """
a = unicode(2)
b = unicode(b)
c = 2
"""
    tree = ast.parse(code)
    tree_changed, errors, changed_trees = StringTypesTransformer.transform(tree)
    assert changed_trees[0].get_code() == expected_code
    assert tree_changed
    assert errors == []

# Unit test against class StringTypesTransformer

# Generated at 2022-06-14 02:19:22.038486
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast as py_ast
    import typing

    class TestTransformer(StringTypesTransformer):
        def visit_Name(self, node: py_ast.Name) -> typing.Any:
            if node.id == 'unicode':
                new_name = py_ast.Name('str', py_ast.Load())
                return new_name
            else:
                return node


    code = """
    a = 'test'
    b = str('test')
    c = 123123
    """

    tree = py_ast.parse(code)
    test_transformer = TestTransformer(py_ast.parse(code))
    result = test_transformer.transform(tree)

    # Make some target changes

# Generated at 2022-06-14 02:19:25.100387
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    print ('Testing constructor of class StringTypesTransformer')
    transformer = StringTypesTransformer()
    assert transformer is not None
    assert callable(transformer)


# Generated at 2022-06-14 02:19:25.794537
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:19:28.800690
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_utils import make_test_transformer

    test = make_test_transformer(StringTypesTransformer)
    test("""
        str
        """)

# Generated at 2022-06-14 02:19:33.912268
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    trans = StringTypesTransformer()
    assert trans.target == (2, 7)


# Generated at 2022-06-14 02:19:35.037189
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # not implemented
    pass

# Generated at 2022-06-14 02:19:38.853741
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
a = str()
"""
    expected = """
a = unicode()
"""

    tree = ast.parse(code)
    tree = StringTypesTransformer.transform(tree)
    assert expected == py_ast.dump_python_source(tree)

# Generated at 2022-06-14 02:19:44.061146
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .. import transform

    code = '''
        def f(s):
            return str(s)
    '''

    tree = ast.parse(code)
    transform(tree, StringTypesTransformer)
    fixed_code = '''
        def f(s):
            return unicode(s)
    '''
    assert ast.dump(tree) == ast.dump(ast.parse(fixed_code))

# Generated at 2022-06-14 02:19:56.213538
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
	# Check str -> unicode
	assert ast.dump(StringTypesTransformer.run('a = str("hello")')) == 'Module(body=[Assign(targets=[Name(id="a", ctx=Store())], value=Call(func=Name(id="unicode", ctx=Load()), args=[Str(s="hello")], keywords=[], starargs=None, kwargs=None))])'
	# Check that nothing happens if there is no str() function
	assert ast.dump(StringTypesTransformer.run('a = "hello"')) == 'Module(body=[Assign(targets=[Name(id="a", ctx=Store())], value=Str(s="hello"))])'
	# Check that nothing happens if there is something other than str()

# Generated at 2022-06-14 02:20:06.586269
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test Data
    input_file_name = 'test_data/string_types_test_data/input_test_string.py'

    input_file = open(input_file_name, 'r')
    input_data = input_file.read()
    input_file.close()

    expected_output_file_name = 'test_data/string_types_test_data/expected_output_test_string.py'

    expected_output_file = open(expected_output_file_name, 'r')
    expected_output_data = expected_output_file.read()
    expected_output_file.close()

    # Actual Output
    transformation_result = StringTypesTransformer.transform(input_data)
    actual_ouput_data = transformation_result.transformed_tree

    # Assert
    assert actual_

# Generated at 2022-06-14 02:20:19.464703
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class User:
        def __init__(self, fname: str, lname: str) -> None:
            self.fname = fname
            self.lname = lname

        def say_hello(self) -> None:
            print(f'Hello, {self.fname} {self.lname}')

    SOURCE = dedent('''
    class User:
        def __init__(self, fname: str, lname: str):
            self.fname = fname
            self.lname = lname

        def say_hello(self):
            print('Hello, ' + self.fname + ' ' + self.lname)

    ''')

    tree = ast.parse(SOURCE)
    new_tree = StringTypesTransformer.transform(tree)

# Generated at 2022-06-14 02:20:27.052395
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse(
        '''
        class Example:
            def __init__(self, name: str):
                self.name = name
        '''
    )
    
    tree_changed, _ = StringTypesTransformer().transform(tree)
    assert tree_changed
    
    target = ast.parse(
        '''
        class Example:
            def __init__(self, name: unicode):
                self.name = name
        '''
    )
    
    assert ast.dump(tree) == ast.dump(target)

# Generated at 2022-06-14 02:20:31.626931
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        x = 'test'
        y = str(x)
        y = unicode()
    """
    expected = """
        x = 'test'
        y = unicode(x)
        y = unicode()
    """

    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)

    assert result.code == expected

# Generated at 2022-06-14 02:20:34.280824
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("str")
    t = StringTypesTransformer()
    assert t.transform(tree)
    assert str(tree) == "unicode"

# Generated at 2022-06-14 02:20:40.499802
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    print(StringTypesTransformer.transform('import unicode'))
    print(StringTypesTransformer.transform('from typed_ast import a2'))

# Generated at 2022-06-14 02:20:51.253422
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import builtins
    tree = ast.parse('a = str; b = unicode')

    class DummyModule(object):
        @property
        def name(self):
            return 'six'

        @property
        def __file__(self):
            return '/path/to/six.py'

    class_def = ast.ClassDef(bases=[ast.Attribute(value=ast.Name(id='builtins', ctx=ast.Load()), attr='object', ctx=ast.Load())],
                             name='DummyClass',
                             keywords=[],
                             body=[ast.Expr(value=ast.Str(s='class docstring'))],
                             decorator_list=[])


# Generated at 2022-06-14 02:20:55.711597
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    src = """
        import os
        import sys

        def foo(x: str) -> str:
            return x + str('hello')
    """

    res = """
        import os
        import sys

        def foo(x: unicode) -> unicode:
            return x + unicode('hello')
    """

    trf = StringTypesTransformer()
    trf.transform_source(src) == res

# Generated at 2022-06-14 02:20:58.136171
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    print("test_StringTypesTransformer...")
    assert True
    


# Generated at 2022-06-14 02:21:06.531561
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .. import transform
    import textwrap
    source = textwrap.dedent('''
    class Test:
        def func(self):
            return str
    ''')
    tree = ast.parse(source)
    tree = transform(tree, StringTypesTransformer)
    new_source = compile(tree, '<test>', 'exec')
    ns = {}
    exec(new_source, ns)
    assert ns['Test'].func() is unicode

# Generated at 2022-06-14 02:21:10.706185
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse
    input = 'x = str'
    expected_output = 'x = unicode'
    tree = ast.parse(input)
    new_tree, tree_changed, messages = StringTypesTransformer.transform(tree)
    assert tree_changed
    assert astunparse.unparse(new_tree) == expected_output
    assert messages == []

# Generated at 2022-06-14 02:21:13.805766
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:21:18.658945
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_base import CodeTreeTester
    tester = CodeTreeTester(StringTypesTransformer)

    tester.test_transform('str()', 'unicode()')
    tester.test_transform('type(str())', 'type(unicode())')
    tester.test_transform('type(foo) == str', 'type(foo) == unicode')

# Generated at 2022-06-14 02:21:23.135394
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """
    x = str()
    y = 'abc'
    """

    tree = ast.parse(source)
    result = StringTypesTransformer.transform(tree)
    expected = """
    x = unicode()
    y = "abc"
    """

    assert astor.to_source(result.tree) == expected

# Generated at 2022-06-14 02:21:31.417521
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    code = """\
    class Foo(object):

        def foo(self, x):
            if isinstance(x, str):
                print('x is of type str')
            else:
                print('x is not of type str')

    """
    exp_code = """\
    class Foo(object):

        def foo(self, x):
            if isinstance(x, unicode):
                print('x is of type str')
            else:
                print('x is not of type str')

    """
    tree = ast.parse(code)
    transformer = StringTypesTransformer()
    new_tree = transformer.transform(tree)
    assert ast.dump(new_tree) == ast.dump(ast.parse(exp_code))

# Generated at 2022-06-14 02:21:44.572257
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    import textwrap

    source = textwrap.dedent('''\
        result = str('hello world!')
        ''')
    expected_source = textwrap.dedent('''\
        result = unicode('hello world!')
        ''')

    tree = ast.parse(source)
    result_tree, tree_changed, errors = StringTypesTransformer.transform(tree)
    assert tree_changed == True
    assert errors == []
    assert ast.dump(result_tree) == ast.dump(ast.parse(expected_source))


# Generated at 2022-06-14 02:21:45.195767
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:21:56.475765
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..runner import to_source
    source = '''
    def foo(bar):
        pass
    class A(object):
        def __init__(self, a):
            self.a = a
    if __name__ == '__main__':
        main()
    '''
    source_bytes = source.encode('utf-8')
    expected_source = '''
    def foo(bar):
        pass
    class A(object):
        def __init__(self, a):
            self.a = a
    if __name__ == '__main__':
        main()
    '''

    tree = ast.parse(source)
    transformed_tree, _, _ = StringTypesTransformer.transform(tree)

    assert (to_source(transformed_tree) == expected_source)

# Generated at 2022-06-14 02:22:00.442917
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    node = ast.Name(id = "str", ctx = ast.Load())
    test = StringTypesTransformer.transform(node)
    assert isinstance(test.tree, ast.Name)
    assert test.tree.id == "unicode"
    assert test.tree_changed == True

# Generated at 2022-06-14 02:22:11.253014
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str(x) + unicode(y)')
    transformer = StringTypesTransformer()

    assert transformer.transform(tree) == (None, True, [])

# Generated at 2022-06-14 02:22:16.069634
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Creating ast tree for testing
    tree = ast.parse("print('Hello, world!')")
    tree_before_transformation = copy.deepcopy(tree)
    StringTypesTransformer.transform(tree)
    assert not ast.dump(tree) == ast.dump(tree_before_transformation)
    print("Unit test for StringTypesTransformer: PASSED")


# Generated at 2022-06-14 02:22:18.805397
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("a = 1 + str(x)")) == TransformationResult(ast.parse("a = 1 + unicode(x)"), True, [])

# Generated at 2022-06-14 02:22:21.610862
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse
    from textwrap import dedent

    tree = ast.parse("""\
        s = str()
    """)

    result = StringTypesTransformer.transform(tree)

    assert astunparse.unparse(result.tree).strip() == dedent("""\
        s = unicode()
    """).strip()

# Generated at 2022-06-14 02:22:23.730346
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert isinstance(StringTypesTransformer(), BaseTransformer)

# Test that it will be inserted when specified in LIST_OF_TRANSFORMERS

# Generated at 2022-06-14 02:22:28.373349
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Define sample code
    parrot = ast.parse("str")

    # Define expected result 1
    expected1 = ast.parse("unicode")

    # Perform the test
    actual = StringTypesTransformer.transform(parrot)

    # Verify the result
    assert ast.dump(actual.tree) == ast.dump(expected1)
    assert actual.tree_changed == True
    assert actual.is_supported == True

# Generated at 2022-06-14 02:22:49.654600
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.testing import run_test_transformer
    from ..utils.transformations import TransformationRunner

    # Create a transformer list, then create a new transformer object for each transformation in the list.
    transformer_list = [StringTypesTransformer]
    runner = TransformationRunner(transformer_list)

    # Pass a minimal AST through the transformation runner.
    tree = ast.parse("str_test = 'this is a string'")
    run_test_transformer(tree, runner)

    # Assert that the output is correct.
    # Specifically, ensure that the new node that is constructed by the transformer has the expected values.
    # In this specific case the expected output is "unicode_test = 'this is a string'" because the transformer
    #  replaces 'str' with 'unicode'.
    assert "unicode_test" in str(tree)

# Generated at 2022-06-14 02:23:00.332649
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .base import BaseTransformerTest
    from ..utils.source import Source

    class Test(BaseTransformerTest):
        target_class = StringTypesTransformer
        code_block = """
        my_str = str()
        """
        expected_code_block = """
        my_str = unicode()
        """

    class Test3(Test):
        target_version = (3, 0)
        code_block = """
        my_str = str()
        my_bytes = bytes()
        """
        expected_code_block = """
        my_str = unicode()
        my_bytes = bytes()
        """

    class Test3p8(Test):
        target_version = (3, 8)

# Generated at 2022-06-14 02:23:06.860011
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_nodes

    source = """
        for i in range(10):
            a = str(i)
            b = str(i+1)
        """
    tree = source_to_nodes(source)

    t = StringTypesTransformer()
    result = t.transform(tree)
    assert result.tree_changed

    # TODO: "assert_source()"

# Generated at 2022-06-14 02:23:11.434176
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    src = "str('a')"
    expected_dst = "unicode('a')"
    dst = StringTypesTransformer.transform(ast.parse(src))
    assert dst.changed == True
    assert astunparse(dst.tree) == expected_dst

# Generated at 2022-06-14 02:23:14.014896
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:27.923073
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    import textwrap
    
    code = textwrap.dedent('''
    class C:
        def __init__(self, name=str):
            self.name = name

        def get_name(self):
            return str(self.name)
    ''')

    tree = ast.parse(code)
    tree_transformed = StringTypesTransformer.transform(tree)

    import unittest
    class TestStringTypesTransformer(unittest.TestCase):
        def test_StringTypesTransformer(self):
            # Ensure that transformer has not broken the parser
            self.assertIsInstance(tree_transformed.tree, ast.AST)

            import inspect
            code_from_ast = inspect.getsource(tree_transformed.tree)

# Generated at 2022-06-14 02:23:31.263070
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test to check constructor of class StringTypesTransformer.
    """
    transformer = StringTypesTransformer()
    assert transformer.target == (2, 7)



# Generated at 2022-06-14 02:23:44.439191
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    stringTypesTransformer = StringTypesTransformer()
    # Basic test
    assert stringTypesTransformer.transform("greet = 'hello world'") == ("greet = unicode('hello world')", True, [])
    assert stringTypesTransformer.transform("greet = \"hello world\"") == ("greet = unicode(\"hello world\")", True, [])
    # Using a variable in the string
    assert stringTypesTransformer.transform("greet = \"hello\" + name") == ("greet = unicode(\"hello\") + name", True, [])
    assert stringTypesTransformer.transform("greet = 'hello' + name") == ("greet = unicode('hello') + name", True, [])
    # With string format

# Generated at 2022-06-14 02:23:45.437327
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()

# Generated at 2022-06-14 02:23:54.741816
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Testing case when AST contains no `str` to be replaced
    test_ast = ast.parse("def f(x):\n    return g(str(x))")
    result = StringTypesTransformer.transform(test_ast)
    assert result.tree_changed == False

    # Testing case when AST contains a single `str` to be replaced
    test_ast = ast.parse("def f(x):\n    return str(x)")
    result = StringTypesTransformer.transform(test_ast)
    assert result.tree_changed == True
    assert result.errors == []

    # Testing case when AST contains multiple `str` to be replaced
    test_ast = ast.parse("def f(x):\n    return str(x) + str(x) + str(x)")

# Generated at 2022-06-14 02:24:22.329499
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import sys

    sys.stderr.write('Testing class StringTypesTransformer...\n')

    import astor
    from astmonkey import transformations
    from typing import List


# Generated at 2022-06-14 02:24:23.683934
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:24:37.906364
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from typed_ast import ast3 as ast
    from ..utils.fixtures import parametrize
    from .base import BaseTestTransformer

    _, tree = parametrize('class A: def f(self, x: str()): ...')

    class TestStringTypesTransformer(BaseTestTransformer):
        transformer = StringTypesTransformer

# Generated at 2022-06-14 02:24:44.259706
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer(): 
    # TransformationResult is a namedtuple
    result = StringTypesTransformer.transform(ast.parse('str')) 
    assert isinstance(result, TransformationResult)

    # Test expected values for each namedtuple field
    assert result[0] == ast.parse('unicode')
    assert result[1] == True
    assert result[2] == []

# Generated at 2022-06-14 02:24:46.843447
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    StringTypesTransformer().transform(ast.parse("""
        str(123)
    """))

# Generated at 2022-06-14 02:24:47.541727
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:24:50.429874
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    a = StringTypesTransformer()
    assert isinstance(a, StringTypesTransformer)

# Test string type to unicode

# Generated at 2022-06-14 02:25:03.002509
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    import unittest
    import sys
    sys.path.append("..")
    from ..utils import ast_compare
    from ..utils.ast_plumbing import insert_imports

    source = ast.parse("from typing import Dict, List, Tuple, Union\n\n"
                       "def f(x: unicode, y: Tuple[unicode, ...]):\n"
                       "    return x + y\n")
    correct = ast.parse("from typing import Dict, List, Tuple, Union\n\n"
                        "def f(x: str, y: Tuple[unicode, ...]):\n"
                        "    return x + y\n")

    inserted = insert_imports(source)

# Generated at 2022-06-14 02:25:04.038314
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:25:06.184519
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert 'unicode' == StringTypesTransformer.transform(5)

# Generated at 2022-06-14 02:26:06.726842
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast

    # Build AST

# Generated at 2022-06-14 02:26:15.527090
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    import cStringIO
    import sys

    from typed_ast import ast3
    from .base import BaseTransformer

    from ..utils import tree

    class Test_StringTypesTransformer(BaseTransformer):
        python_version = (2, 7) # type: Tuple[int, ...]

        def visit_Name(self, node: ast.Name):
            if node.id == 'str':
                node.id = 'unicode'
                return node


    # test_simple_program_with_string.py
    source = '''
    var = "test"
    print(var)
    '''

    # Construct an AST
    expected_ast = ast3.parse(source)

    # Apply the transformation
    Test_StringTypesTransformer.transform(expected_ast)

    # Check that the tree is equal

# Generated at 2022-06-14 02:26:22.612077
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_code = """
        x = "Hello"
        if isinstance(x, str):
            print("hello")
    """
    expected_output = """
        x = "Hello"
        if isinstance(x, unicode):
            print("hello")
    """
    tree = ast.parse(input_code)
    tree_changed, new_tree = StringTypesTransformer.transform(tree)
    assert comparator.compare(ast.dump(new_tree), expected_output)

# Generated at 2022-06-14 02:26:30.245424
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    tree = ast.parse("""
'''DocString'''
s = str(s)
a = str(x) + str(y) + str(z)
b = str(x) + str(y) + str(z)
    """)
    t = StringTypesTransformer()
    t.transform(tree)

    assert t.log == []
    assert t.tree_changed == True
    assert ast.dump(t.tree) == ast.dump(ast.parse("""
'''DocString'''
s = unicode(s)
a = unicode(x) + unicode(y) + unicode(z)
b = unicode(x) + unicode(y) + unicode(z)
    """))

# Generated at 2022-06-14 02:26:33.357460
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform('str("hello")') == 'unicode("hello")'
    assert StringTypesTransformer.transform('str("hello")') == 'unicode("hello")'

# Generated at 2022-06-14 02:26:38.873814
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = \
    """
    A = str()
    """
    expected_code = \
    """
    A = unicode()
    """
    tree = ast.parse(code)
    new_tree = StringTypesTransformer.transform(tree)
    assert ast.unparse(new_tree.tree) == expected_code

# Generated at 2022-06-14 02:26:40.348748
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert isinstance(StringTypesTransformer(), StringTypesTransformer)


# Generated at 2022-06-14 02:26:41.501565
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .. import transform

# Generated at 2022-06-14 02:26:47.166627
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    import typed_ast.ast3
    from typed_ast import ast3 as ast
    from typed_ast.py37 import Py37Transformer
    from ..utils.tree import ast_to_text
    from ..utils.compare import compare_ast


# Generated at 2022-06-14 02:26:55.050769
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_base import generate_test_ast
    from .test_base import assert_matching_ast

    # tree_before
    tree = ast.parse('str()')

    # tree_after
    expected_tree = ast.parse('unicode()')
    expected_err_msg_list = []

    transformer = StringTypesTransformer()
    actual_result = transformer.transform(tree)

    assert_matching_ast(expected_tree, actual_result.transformed_tree)
    assert expected_err_msg_list == actual_result.error_messages