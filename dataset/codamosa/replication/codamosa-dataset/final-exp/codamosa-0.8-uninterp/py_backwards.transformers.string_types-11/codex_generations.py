

# Generated at 2022-06-14 02:16:56.968641
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer(None, None).target == (2, 7)


# Generated at 2022-06-14 02:16:57.494914
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:00.941329
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import as_source

    code = 'import io; io.StringIO()'
    tree = ast.parse(code)
    trf = StringTypesTransformer().transform(tree)
    assert as_source(trf.tree) == 'import io; io.unicodeIO()'

# Generated at 2022-06-14 02:17:04.441524
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree_changed = False
    i = StringTypesTransformer(tree_changed)
    assert i.tree_changed == False

    tree_changed = True
    i = StringTypesTransformer(tree_changed)
    assert i.tree_changed == True



# Generated at 2022-06-14 02:17:07.104936
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for constructor of class StringTypesTransformer

    """
    assert issubclass(StringTypesTransformer, BaseTransformer)

# Generated at 2022-06-14 02:17:18.871381
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Creating AST
    tree = ast.parse("""
x = str(3)
y = str(3, 4)
z = str([3, 1])
    """)

    # Creating instance of StringTypesTransformer
    string_types_transformer = StringTypesTransformer(tree, StringTypesTransformer.target)

    # Transforming AST
    tree = string_types_transformer.transform()[0]

    # Checking that the first call's first argument is "unicode"
    assert(tree.body[0].value.func.id == 'unicode')
    # Checking that the second call's first argument is "unicode"
    assert(tree.body[1].value.func.id == 'unicode')
    # Checking that the third call's first argument is "unicode"

# Generated at 2022-06-14 02:17:23.538939
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3
    print(typed_ast.ast3.dump(StringTypesTransformer.transform(typed_ast.ast3.parse("x = str(y)"))[0]))

# Generated at 2022-06-14 02:17:31.776349
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3
    """
    # Test string input
    test_str_input = """

# Generated at 2022-06-14 02:17:37.772897
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    s = """a = "test" """
    tree = ast.parse(s)
    expected = ast.parse("a = u'test' ")
    transformed, changed, _ = StringTypesTransformer.transform(tree)
    assert not changed
    transformed, changed, _ = StringTypesTransformer.transform(transformed)
    assert changed
    assert ast.dump(transformed) == ast.dump(expected)



# Generated at 2022-06-14 02:17:46.604321
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import textwrap
    from ..utils.tree import find

    tree = ast.parse(textwrap.dedent('''
        print(str(1))
    '''))

    r = StringTypesTransformer.transform(tree)
    assert r.tree_changed
    assert r.messages == []

    # Ensure that `print(unicode(1))` is in the new tree
    assert len(find(r.tree, ast.Name)) == 1
    assert find(r.tree, ast.Name)[0].id == 'unicode'

# vim:ts=4:sw=4:softta

# Generated at 2022-06-14 02:17:53.881751
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .ast_transformer_tester import ASTTransformerTester
    from typed_ast import ast3 as ast
    from .string_type_tester import test_string_types

    test = ASTTransformerTester(StringTypesTransformer, string_type_tester)
    test_string_types(test)

# Generated at 2022-06-14 02:18:04.542762
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    type_list = [ast.Name(id=str('str'), 
                          ctx=ast.Load()),
                 ast.Name(id=str('unicode'),
                          ctx=ast.Load()),
                 ast.Name(id=str('int'),
                          ctx=ast.Load())]

    name_list = [ast.Name(id=str('str'), 
                          ctx=ast.Load()),
                 ast.Name(id=str('unicode'),
                          ctx=ast.Load()),
                 ast.Name(id=str('int'),
                          ctx=ast.Load())]


# Generated at 2022-06-14 02:18:09.595110
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        a = str(b)
    """
    expected = """
        a = unicode(b)
    """

    tree = ast.parse(code)
    result, _ = StringTypesTransformer.transform(tree)
    actual = ast.unparse(result).strip()

    assert actual == expected

# Generated at 2022-06-14 02:18:13.630252
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    node = ast.Name(id="str", ctx=ast.Load())
    new_node = StringTypesTransformer.transform(node).tree
    assert isinstance(new_node, ast.Name)
    assert new_node.id == "unicode"

# Generated at 2022-06-14 02:18:24.054617
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_astunparse

# Generated at 2022-06-14 02:18:26.724186
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t1 = ast.parse('str')
    t1_expected = ast.parse('unicode')
    assert StringTypesTransformer.transform(t1).tree == t1_expected

# -----------------------------------------------------------------------------


# Generated at 2022-06-14 02:18:33.256036
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # (1) Constructor test
    option = StringTypesTransformer()
    assert isinstance(option, BaseTransformer)
    assert option.target == (2, 7)
    assert option.priority == 1

    # (2) Transform test
    # (2.1) Tree with no string
    tree = ast.parse("def f():\n return 2")
    result = StringTypesTransformer().transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree == tree
    assert result.modified == False
    assert result.log == []

    # (2.2) Tree with string
    tree = ast.parse("def f():\n return 'hello'")
    result = StringTypesTransformer().transform(tree)
    assert isinstance(result, TransformationResult)

# Generated at 2022-06-14 02:18:41.408154
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str("abc")')
    assert len(tree.body) == 1

    result = StringTypesTransformer.transform(copy.deepcopy(tree))
    assert result.tree_changed

    tree = ast.parse('str("abc")')
    assert tree.body[0].value.id == 'str'
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed
    assert result.tree.body[0].value.id == 'unicode'

# Generated at 2022-06-14 02:18:48.411319
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Replacement with initialization
    assert StringTypesTransformer.transform(
        ast.parse("""
a = str("abc")""", 'test_string')).tree == ast.parse("""
a = unicode("abc")""", 'test_string')

    # Replacement without initialization
    assert StringTypesTransformer.transform(
        ast.parse("""
a = "abc"
b = str(a)""", 'test_string')).tree == ast.parse("""
a = "abc"
b = unicode(a)""", 'test_string')

# Generated at 2022-06-14 02:18:54.092018
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    before = ast.parse("""def expected(a):
        print(str(a))
        """)
    after = ast.parse("""def expected(a):
        print(unicode(a))
        """)
    t = StringTypesTransformer()
    # compare two trees
    trans, _ = t.transform(before)
    assert ast.dump(trans) == ast.dump(after)

# Generated at 2022-06-14 02:18:56.350074
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:19:05.899275
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import unittest
    from typed_ast import ast3 as ast
    from ..utils.tree import find

    class TestStringTypesTransformer(unittest.TestCase):
        """Test suite for StringTypesTransformer class."""

        def test_replace(self):
            node = ast.Name(id='str')
            StringTypesTransformer.transform(node)
            self.assertEqual(node.id, 'unicode')

        def test_no_replace(self):
            node = ast.Name(id='int')
            StringTypesTransformer.transform(node)
            self.assertEqual(node.id, 'int')

    # Run tests
    unittest.main(verbosity=2)

# Generated at 2022-06-14 02:19:07.537528
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer('str').constructor == StringTypesTransformer

# Generated at 2022-06-14 02:19:14.063170
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = 'a = str(42)'
    tree = ast.parse(source)
    assert isinstance(tree, ast.Module)
    assert len(list(ast.walk(tree))) == 9

    _, changed = StringTypesTransformer.transform(tree)
    assert_equal(changed, True)
    assert_equal(ast.dump(tree), ast.dump(ast.parse('a = unicode(42)')))

# Generated at 2022-06-14 02:19:16.486482
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests `StringTypesTransformer` constructor. 

    """
    assert StringTypesTransformer.target == (2, 7)


# Generated at 2022-06-14 02:19:21.330520
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils import compare_ast

    with open('tests/support/string_types.py') as test_file:
        tree = ast.parse(test_file.read())
    
    new_tree = StringTypesTransformer.transform(tree)

    with open('tests/support/string_types_transformed.py') as test_file:
        expected = ast.parse(test_file.read())

    assert compare_ast(new_tree.tree, expected)

# Generated at 2022-06-14 02:19:32.944070
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = "print(str(True))"

    from ..utils.source import source_to_code
    module = source_to_code(code, 'main', 2)
    new_module = StringTypesTransformer.transform(module)


# Generated at 2022-06-14 02:19:39.686067
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = '''foo = "str"'''
    tree = ast.parse(source)
    result, _ = StringTypesTransformer.transform(tree)
    assert ast.dump(result) == ast.dump(ast.parse('''foo = "unicode"'''))
    
    # Test if code stays the same if no changes are necessary
    result, _ = StringTypesTransformer.transform(result)
    assert ast.dump(result) == ast.dump(ast.parse('''foo = "unicode"'''))

# Generated at 2022-06-14 02:19:43.146890
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    test_code = 'a = str("Hello")'
    tree = ast.parse(test_code, mode='exec')
    StringTypesTransformer.transform(tree)
    exec(compile(tree, filename="<ast>", mode="exec"))
    assert a == u"Hello"

# Generated at 2022-06-14 02:19:44.604585
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .. import transform


# Generated at 2022-06-14 02:19:48.546774
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert True



# Generated at 2022-06-14 02:19:56.069599
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from ..rewrite_code import rewrite

    class AST:
        ...

    source_code = """
        print(str(123))

        class Foo:
            ...
    """
    source_tree = ast.parse(source_code, mode='exec')
    result = rewrite(source_tree, [StringTypesTransformer])
    print(result.tree)

# Generated at 2022-06-14 02:20:06.587184
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import sys
    import ast
    import inspect

    # Load the target method from its parent class
    parent_class = getattr(sys.modules[__name__], StringTypesTransformer.__bases__[0].__name__)
    method = getattr(parent_class, inspect.stack()[0][3])

    # Prepare in-memory file for code to be transformed
    old_code = '''def foo(a: str, b: str) -> str:
    return a + b

print(foo('x', 'y'))
    '''
    old_code_lines = old_code.splitlines()
    module = ast.parse(old_code)

    # Transform the AST
    new_module, changed = method(module)

    # Export to in-memory file again

# Generated at 2022-06-14 02:20:09.351822
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(string_tree) == string_tree_transformed

# Test data

# Generated at 2022-06-14 02:20:13.279480
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    root = ast.parse(u"isinstance(foo, str)")
    result = StringTypesTransformer.transform(root)

    assert u"isinstance(foo, unicode)" in astor.to_source(result.tree)

# Generated at 2022-06-14 02:20:20.950104
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = 'str("foo")'
    tree = ast.parse(code)
    actual_result = StringTypesTransformer.transform(tree)
    expected_result = TransformationResult(
        ast.parse('unicode("foo")'),
        True,
        [],
    )
    assert actual_result == expected_result

if __name__ == '__main__':
    import pytest
    pytest.main(['-xrf'])

# Generated at 2022-06-14 02:20:29.012883
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import textwrap

    source = textwrap.dedent("""
    def main():
        a: str
        def inner():
            a: str
    """)
    expect = textwrap.dedent("""
    def main():
        a: unicode
        def inner():
            a: unicode
    """)

    tree = ast.parse(source)
    tree = StringTypesTransformer.transform(tree)

    assert ast.dump(tree) == expect

# Generated at 2022-06-14 02:20:35.616844
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    oldstring = """
    def strFunc(st):
        str('test')
        """

    expected = """
    def strFunc(st):
        unicode('test')
        """
    oldtree = ast.parse(oldstring)
    expectedTree = ast.parse(expected)
    newTree = StringTypesTransformer.transform(oldtree)
    assert ast.dump(newTree.tree) == ast.dump(expectedTree)

# Generated at 2022-06-14 02:20:39.244399
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = ast.parse('a = "something"')
    t = StringTypesTransformer.transform(t)
    assert t.tree == ast.parse('a = u"something"')

# Generated at 2022-06-14 02:20:49.715603
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.result("str a = 'happy'") == "unicode a = 'happy'"
    assert StringTypesTransformer.result("def func(str a, str b): return a + b") == "def func(unicode a, unicode b): return a + b"
    assert StringTypesTransformer.result("print(str)") == "print(unicode)"
    assert StringTypesTransformer.result("print(type(str))") == "print(type(unicode))"
    assert StringTypesTransformer.result("print(type(a) is str)") == "print(type(a) is unicode)"
    assert StringTypesTransformer.result("def func(a): return a is str") == "def func(a): return a is unicode"

# Generated at 2022-06-14 02:21:03.666167
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import Source
    from ..utils.visitor import dump
    from ..utils.ast_builder import build_ast

    for code in Source('tests/samples/string_types/str.py').read():
        tree = build_ast(code)
        transformer = StringTypesTransformer.__new__(StringTypesTransformer)
        transformer.visit(tree)
        dump(tree)

# Generated at 2022-06-14 02:21:08.463950
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''def test():
    print(str(1))
'''
    expected = '''def test():
    print(unicode(1))
'''
    t = StringTypesTransformer()
    tree, _ = t.transform_code(code)
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:21:15.937183
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    results = StringTypesTransformer.run_test('''
        class Test(object):
            def __init__(self):
                print str(1)
        ''')

    tree = results.transformations[0].tree
    # Prints Test class
    print(ast.dump(tree))

    # TestResult is unchanged after transformations
    assert results.is_results_equal()



# Generated at 2022-06-14 02:21:18.969948
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    tree = ast.parse("str(2)")
    tree_changed = StringTypesTransformer.transform(tree)
    tree_changed.tree.body[0].value.func.id == "unicode"

# Generated at 2022-06-14 02:21:28.879585
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    example1 = ast.parse('str()')
    example2 = ast.parse('str.capitalize()')
    example3 = ast.parse('str(x)')
    example4 = ast.parse('str(x).capitalize()')
    example5 = ast.parse('x.capitalize()')
    new_ex1 = StringTypesTransformer.transform(example1)
    new_ex2 = StringTypesTransformer.transform(example2)
    new_ex3 = StringTypesTransformer.transform(example3)
    new_ex4 = StringTypesTransformer.transform(example4)
    new_ex5 = StringTypesTransformer.transform(example5)
    result1 = ast.dump(new_ex1.new_tree)
    result2 = ast.dump(new_ex2.new_tree)
    result3 = ast

# Generated at 2022-06-14 02:21:38.987468
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_code = """def foo(a):
        b = str(a)"""

    expected_code = """def foo(a):
        b = unicode(a)"""

    print("Input code:", input_code, sep="\n")
    print("Expected code:", expected_code, sep="\n")

    code_obj = compile(input_code, "<string>", "exec", ast.PyCF_ONLY_AST)
    ast_tree = ast.parse(input_code)

    transformer = StringTypesTransformer()
    output_code = transformer.transform(ast_tree)

    print("Output code:", output_code.code, sep="\n")

    assert output_code.code == expected_code

# Generated at 2022-06-14 02:21:50.968397
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from .base import get_transformer_test_cases
    from ..__main__ import transform_with_imports
    import sys, os

    this_dir = os.path.dirname(__file__)

    # Unit test disabled: see issue #93 on GitHub
    # test_cases = get_transformer_test_cases(os.path.join(this_dir, 'test_cases', 'StringTypesTransformer'),
    #                                         sys.modules[__name__],
    #                                         'StringTypesTransformer')
    # for case in test_cases:
    #     # Test the default transformer (no additional imports)
    #     transform_with_imports(case.source, sys.modules[__name__], (2, 7))
    #     # ... and the same transformer with additional

# Generated at 2022-06-14 02:22:00.978377
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # program:
    # x = str(2)
    root = ast.Module([ast.Assign([ast.Name('x', ast.Store())], 
        ast.Call(func=ast.Name('str', ast.Load()), args=[ast.Num(n=2)], keywords=[], starargs=None, kwargs=None))])
    tree = ast.fix_missing_locations(root)

    # expected output:
    # x = unicode(2)
    new_root = ast.Module([ast.Assign([ast.Name('x', ast.Store())], 
        ast.Call(func=ast.Name('unicode', ast.Load()), args=[ast.Num(n=2)], keywords=[], starargs=None, kwargs=None))])
    expected_tree = ast.fix_missing_

# Generated at 2022-06-14 02:22:02.773177
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """
    """
    assert StringTypesTransformer.target == (2, 7)


# Generated at 2022-06-14 02:22:06.561720
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    node = ast.parse('"Hello, world!"')
    result = StringTypesTransformer.transform(node)
    assert result.tree == ast.parse('u"Hello, world!"')
    assert result.tree_changed
    assert result.failed_transformations == []

# Generated at 2022-06-14 02:22:25.541843
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('a = str(1)')
    StringTypesTransformer.run_on(tree)
    assert ast.dump(tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Num(n=1)], keywords=[], starargs=None, kwargs=None))])"

# Generated at 2022-06-14 02:22:31.720609
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    # Test that the transformer replaces `str` with `unicode`.
    tree = ast.parse('a = str')
    actual_changed, actual_imported = StringTypesTransformer.transform(tree)
    expected_changed = True
    expected_imported = []
    assert actual_changed == expected_changed
    assert actual_imported == expected_imported

# Generated at 2022-06-14 02:22:40.996502
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert_transformation_result(
        StringTypesTransformer,
        [],
        """
        def tree(a: str) -> str:
            return a

        def tree_2(a: str) -> str:
            return str(a)
        """
    )
    assert_transformation_result(
        StringTypesTransformer,
        ["""
        def tree(a: unicode) -> unicode:
            return a

        def tree_2(a: unicode) -> unicode:
            return str(a)
        """],
        """
        def tree(a: str) -> str:
            return a

        def tree_2(a: str) -> str:
            return unicode(a)
        """
    )

# Generated at 2022-06-14 02:22:49.125056
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class MyTransformer(StringTypesTransformer):
        @classmethod
        def transform(cls, tree: ast.AST) -> TransformationResult:
            return super().transform(tree)

    code = """
        x = str("asd")
        y = str("asd")
        z = str("asd")
    """
    tree = ast.parse(code)
    new_tree = MyTransformer.transform(tree)
    assert isinstance(new_tree.tree, ast.AST)
    for node in find(new_tree.tree, ast.Name):
        if node.id == 'str':
            node.id = 'unicode'

if __name__ == "__main__":
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:22:50.079591
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor

# Generated at 2022-06-14 02:22:52.217172
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.fake import FakeFile


# Generated at 2022-06-14 02:23:01.428017
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = test_utils.build_ast_from_snippet('str(x)')
    t = StringTypesTransformer()
    new_tree, changed = t.transform(tree)
    assert changed == True
    assert isinstance(new_tree, ast.Module)
    assert len(new_tree.body) == 1
    call = new_tree.body[0].value
    assert isinstance(call, ast.Call)
    assert isinstance(call.func, ast.Name)
    assert call.func.id == 'unicode'
    assert len(call.args) == 1
    assert isinstance(call.args[0], ast.Name)
    assert call.args[0].id == 'x'

# Generated at 2022-06-14 02:23:02.557365
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:03.209833
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:07.053465
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("name = str()")
    tree = StringTypesTransformer.transform(tree).tree
    assert str(tree.body[0]) == "name = unicode()"

# Generated at 2022-06-14 02:23:40.815992
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test unit for constructor of class StringTypesTransformer

    """
    tree = ast.parse("""
        
        def my_function(a, b, c):
            if a == 1:
                b = str(b)
            return b
        """, 'exec')

    transformer = StringTypesTransformer()
    transformed_tree = transformer.transform(tree)
    assert isinstance(transformed_tree, ast.AST)
    assert len(transformer.errors) == 0


# Unit tests for method transform of class StringTypesTransformer

# Generated at 2022-06-14 02:23:45.443126
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    initial_tree = ast.parse('str()')
    target_tree = ast.parse('unicode()')

    assert target_tree == StringTypesTransformer.transform(initial_tree)

# Generated at 2022-06-14 02:23:53.709831
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse('''
        print(str(0))
        print(type(str))
        print(type(unicode))
        print(type(str()))
        print(type(unicode()))
    ''')

    expected = ast.parse('''
        print(unicode(0))
        print(type(unicode))
        print(type(unicode))
        print(type(unicode()))
        print(type(unicode()))
    ''')

    tr = StringTypesTransformer()
    tr.visit(tree)

    assert ast.dump(tree) == ast.dump(expected)

# Generated at 2022-06-14 02:24:03.272006
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import inspect 
    import ast
    # type: StringTypesTransformer
    StringTypesTransformer = StringTypesTransformer
    # type: inspect.getsource
    src = inspect.getsource(StringTypesTransformer)
    # type: ast.Module
    tree = ast.parse(src)

    # type: ast.AST
    tree = ast.fix_missing_locations(tree)
    # type: str
    code = compile(tree, filename='<ast>', mode='exec')
    # type: dict
    ns = {}
    # type: dict
    ns['ast'] = ast
    exec(code, ns)
    return ns['StringTypesTransformer']

StringTypesTransformer = test_StringTypesTransformer()

# Generated at 2022-06-14 02:24:17.624512
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.tree_tools import ast2str
    from .utils import transform_to_target
    from ..utils.test_utils import generate_testcase_from_func

    def test_func(a: str, b: str) -> str:
        return a + b
    module = ast.parse(test_func.__text_signature__)
    tree_changed, tree = transform_to_target(module, StringTypesTransformer, StringTypesTransformer.target)
    assert ast2str(tree) == 'def test_func(a:unicode, b:unicode) -> unicode: pass'
    assert tree_changed == True

    @generate_testcase_from_func(test_func)
    def test_gen(a: str, b: str) -> str:
        return a + b

# Generated at 2022-06-14 02:24:18.506136
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer._target == (2, 7)

# Generated at 2022-06-14 02:24:30.869980
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    import six

    # Test that class is callable
    transformer = StringTypesTransformer()
    #assert callable(transformer)

    # Test that code is transformed
    if six.PY2:
        tree = ast.parse("print type(a) is str")
        tree_new = transformer.visit(tree)
        assert "print type(a) is unicode" == ast.unparse(tree_new).rstrip()
    else:
        tree = ast.parse("print type(a) is str")
        tree_new = transformer.visit(tree)
        assert "print type(a) is str" == ast.unparse(tree_new).rstrip()


# Generated at 2022-06-14 02:24:40.288680
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import assign_name, from_source
    from ..utils.tree import print_ast

    transpiler = StringTypesTransformer()
    tree = from_source("""(a: str, b: str) -> (a: str, b: unicode, c: unicode):
    ''' Returns first argument as a str and second argument as a unicode '''
    a = b + 1
    b += 2
    c = a + b
    return a, b, c
    """)
    result = transpiler.transform(tree)
    print("# Modules")
    print_ast(result.tree)
    print("## Globals")
    print_ast(result.tree.body[0].body)


# Generated at 2022-06-14 02:24:46.469586
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
x = "a"
y = str
    """
    expected = """
x = "a"
y = unicode
    """
    parsed_code = ast.parse(code)
    StringTypesTransformer.transform(parsed_code)
    expected_code = ast.parse(expected)
    assert ast.dump(parsed_code) == ast.dump(expected_code)

# Generated at 2022-06-14 02:24:51.032006
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests that the StringTypesTransformer class was built correctly.

    """
    stt = StringTypesTransformer(None)
    assert stt.target == (2, 7)
    assert issubclass(stt.__class__, BaseTransformer)


# Generated at 2022-06-14 02:25:43.517723
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:25:54.821896
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse(
        """
        from string import Template
        from string import my_name
        from string import my_name as new_name
        
        a = str
        b = 'this'
        """
    )
    expected_module = ast.parse(
        """
        from string import Template
        from string import my_name
        from string import my_name as new_name
        
        a = unicode
        b = 'this'
        """
    )
    expected_imports = []
    result = StringTypesTransformer.transform(tree)

    assert result.tree.body == expected_module.body
    assert result.imports == expected_imports
    assert result.tree_changed

if __name__ == '__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:25:59.346483
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    result = StringTypesTransformer.transform(ast.parse("str(name)"))
    assert result.tree_changed == True
    assert type(result.tree) == ast.Module

# Generated at 2022-06-14 02:26:01.395277
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    result = StringTypesTransformer(None)
    assert result


# Tests for method transform of class StringTypesTransformer

# Generated at 2022-06-14 02:26:07.131881
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.sample_strings import TEST_STRINGS
    import astor

    tt = StringTypesTransformer()

    for i, s in enumerate(TEST_STRINGS):
        tree = ast.parse(s)
        new_tree, changed, errs = tt.transform(tree)
        print(astor.to_source(new_tree))
        assert errs == []

# Generated at 2022-06-14 02:26:09.795292
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
	test_string = """
	def test(x: str):
		return x
	"""

# Generated at 2022-06-14 02:26:14.571371
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_str = """
    import string
    x = str(string)
    """
    tree = ast.parse(input_str)
    tree = StringTypesTransformer().visit(tree)
    output_str = """
    import string
    x = unicode(string)
    """
    assert ast_to_str(tree.body[1]) == ast_to_str(ast.parse(output_str).body[0])

# Generated at 2022-06-14 02:26:25.579071
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_unicode
    from ..utils.tree import ast_to_str
    import ast

    code = source_to_unicode("""
        x = str(foo())
    """)

    input_tree = ast.parse(code)
    expected_tree = ast.parse("""
        x = unicode(foo())
    """)
    expected_messages = [
        "INFO:root:Replaced str with unicode",
    ]

    # Call function to be tested
    result = StringTypesTransformer.transform(input_tree)

    # Check the result
    assert result.tree_changed == True
    assert ast_to_str(result.tree) == ast_to_str(expected_tree)
    assert result.messages == expected_messages

# Generated at 2022-06-14 02:26:34.513677
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    # Make a derived class from StringTypesTransformer
    class StringTypesTransformerTest(StringTypesTransformer):
        # Class in which test is defined
        pass

    # Create instance of derived clas
    str_types_transformer = StringTypesTransformerTest()

    class Foo:
        def __init__(self):
            self.a = 'b'
            self.c = 'a'
            self.e = 'c'

    # create ast from sample code

# Generated at 2022-06-14 02:26:40.896072
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.tree import string_type_tree
    from ..utils.source import source
    from ..to27 import main

    treeChanged = True 
    
    while treeChanged:
        tree = string_type_tree()
        result = StringTypesTransformer.transform(tree)
        treeChanged = result.tree_changed 
   
    source_code = source(tree)
    assert source_code == "b = unicode(1)\n" 
