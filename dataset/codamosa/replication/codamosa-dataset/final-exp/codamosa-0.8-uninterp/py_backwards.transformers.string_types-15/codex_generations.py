

# Generated at 2022-06-14 02:17:03.041943
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('str(x)')) == TransformationResult(ast.parse('unicode(x)'), True, [])

# Generated at 2022-06-14 02:17:13.846002
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # given
    tree_to_transform = ast.parse('from typing import Text\ntoken = str()\ndef foo() -> Text:\ntoken = str()')
    expected_source = 'from typing import Text\ntoken = unicode()\ndef foo() -> Text:\ntoken = unicode()'
    # when
    actual_source = to_source(StringTypesTransformer.transform(tree_to_transform)[0])
    # then
    assert expected_source == actual_source

if __name__ == '__main__':
    # to run tests, execute `pytest test_string_types.py` in command line
    import pytest
    pytest.main(['test_string_types.py'])

# Generated at 2022-06-14 02:17:20.043711
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    with open('src/typed_astunparse/tests/test_data/test_string.py', 'r') as input_file:
        input_str = input_file.read()
    input_ast = ast.parse(input_str)
    expected_output_ast = ast.parse(input_str.replace('str', 'unicode'))
    result_ast = StringTypesTransformer().transform(input_ast)
    assert result_ast.tree == expected_output_ast

# Generated at 2022-06-14 02:17:21.873609
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:24.931270
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:31.049494
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
    a = str(b)
    """)
    t = StringTypesTransformer()
    t.transform(tree)
    assert ast.dump(tree) == dedent("""\
    Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Name(id='b', ctx=Load())], keywords=[], starargs=None, kwargs=None))])
    """)

# Generated at 2022-06-14 02:17:31.632409
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:36.491136
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('str')).tree_changed == True
    assert StringTypesTransformer.transform(ast.parse('str')).changed_targets == [2, 7]
    assert StringTypesTransformer.transform(ast.parse('str')).targets_count == 1

# Generated at 2022-06-14 02:17:39.396919
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    assert transformer.target == (2, 7)
    assert isinstance(transformer, BaseTransformer)
    assert issubclass(StringTypesTransformer, BaseTransformer)

# Generated at 2022-06-14 02:17:54.021228
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .helpers import get_transformer_test_cases

    # Get test cases from helper
    test_cases = get_transformer_test_cases(
        transformer_class=StringTypesTransformer,
        transformer_name="StringTypesTransformer",
        original_version=(2, 7),
        target_version=(2, 7),
    )

    # Create test case for class (with setup code)
    def test_StringTypesTransformer_case(expected_output, code_input):
        tree = ast.parse(code_input)
        result = StringTypesTransformer.transform(tree)
        assert result.tree_changed == expected_output
        assert result.error_log == []
        assert result.warn_log == []
        assert ast.dump(result.tree) == ast.dump(ast.parse(expected_output))

    #

# Generated at 2022-06-14 02:18:08.503952
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for StringTypesTransformer class. 
    
    """
    code = '''
            import sys
            import os
            x = 'Hello World'
            y = str(x)
            z = 'Hello Worlf'
    '''
    expected_code = '''
            import sys
            import os
            x = 'Hello World'
            y = unicode(x)
            z = 'Hello Worlf'
    '''
    module = ast.parse(code)
    tree_changed, tree = StringTypesTransformer().transform(module)
    assert expected_code.strip() == ast.unparse(module).strip()

# Generated at 2022-06-14 02:18:15.730084
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import unittest
    from ..utils.tree import print_tree

    class TestMethods(unittest.TestCase):
        def test_tree_changed(self):
            code = """def f(s: str):
                pass
                """
            tree = ast.parse(code)
            result = StringTypesTransformer.transform(tree)
            print_tree(result.tree)
            self.assertEqual(result.tree_changed, True)

        def test_tree_not_changed(self):
            code = """def f(s: int):
                pass
                """
            tree = ast.parse(code)
            result = StringTypesTransformer.transform(tree)
            print_tree(result.tree)
            self.assertEqual(result.tree_changed, False)

    unittest.main()

# Generated at 2022-06-14 02:18:22.182756
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    s = "a = str"
    tree = ast.parse(s)
    print(ast.dump(tree))
    tree_changed = StringTypesTransformer.transform(tree)
    print(ast.dump(tree_changed.tree))
    assert(ast.dump(tree_changed.tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Name(id='unicode', ctx=Load()))])")

test_StringTypesTransformer()

# Generated at 2022-06-14 02:18:28.466140
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Argument for the constructor of class StringTypesTransformer
    test_in = ast.parse("str(1)") # Example: str(1)
    # Expected output from the transformer
    expected_out = ast.parse("unicode(1)") # Example: unicode(1)
    # Output from the transformer
    real_out, _ = StringTypesTransformer.transform(test_in)
    # Assert if the output from the transformer equals the expected output
    assert ast.dump(real_out) == ast.dump(expected_out)

# Generated at 2022-06-14 02:18:37.795784
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test for an ast.Name with id 'str'
    test_ast = ast.Name()
    test_ast.id = 'str'

    tree_changed, errors, new_ast = StringTypesTransformer.transform(test_ast)
    assert tree_changed
    assert len(errors) == 0
    assert new_ast.id == 'unicode'

    # Test for an ast.Num with n = 1
    test_ast = ast.Num()
    test_ast.n = 1

    tree_changed, errors, new_ast = StringTypesTransformer.transform(test_ast)
    assert not tree_changed
    assert len(errors) == 0
    assert new_ast.n == 1

test_StringTypesTransformer()

# Generated at 2022-06-14 02:18:41.963185
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..test_utils import assert_transformation
    from ..test_utils import parse_string

    assert_transformation(
        StringTypesTransformer,
        parse_string('str'),
        parse_string('unicode'),
    )

# Generated at 2022-06-14 02:18:44.123422
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from copy import copy


# Generated at 2022-06-14 02:18:52.495116
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests that the class StringTypesTransformer transforms a given tree into the expected tree.

    """
    tree = ast.parse("""a = '1'
    b = str('2')
    c = str.__name__
    d = str.mro()
    """)
    expected = ast.parse("""a = '1'
    b = unicode('2')
    c = unicode.__name__
    d = unicode.mro()
    """)
    result = StringTypesTransformer.transform(tree)
    assert(expected == result.tree)

# Generated at 2022-06-14 02:18:55.986881
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code_before = str("""
    s = str(b'a')
    """)
    code_after = str("""
    s = unicode(b'a')
    """)

    tree_before = ast.parse(code_before)
    tree_after = ast.parse(code_after)

    transformer = StringTypesTransformer()
    res, _ = transformer.transform(tree_before)

    assert ast.dump(tree_after) == ast.dump(res)

# Generated at 2022-06-14 02:19:00.723256
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    a = "a"
    """
    tree = ast.parse(code)
    new_tree = StringTypesTransformer.transform(tree)
    new_code = modast.dump_code(new_tree)
    assert new_code == """\
a = unicode("a")"""

# Generated at 2022-06-14 02:19:09.260663
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse(
        """
        a = str()
        """
    )
    expected = ast.parse(
        """
        a = unicode()
        """
    )
    result = StringTypesTransformer.transform(tree)
    assert expected == result.tree
    assert result.tree_changed == True

# Generated at 2022-06-14 02:19:09.975928
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:19:15.373226
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    s = """
    a = str
    """
    tree = ast.parse(s)
    tree = StringTypesTransformer().transform(tree)
    assert ast.dump(tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Name(id='unicode', ctx=Load()))])"

# Generated at 2022-06-14 02:19:21.383604
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from .sample_trees import TYPES_TREE

    tree = ast.parse(TYPES_TREE)
    tree, changes, _ = StringTypesTransformer.transform(tree)

    assert changes == True
    assert astor.to_source(tree) == TYPES_TREE.replace('str', 'unicode')
    assert astor.to_source(StringTypesTransformer.transform(tree)[0]) == TYPES_TREE.replace('str', 'unicode')

# Generated at 2022-06-14 02:19:28.192839
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
            def foo(s):
                return str(s)
            """
    expected_code = """
            def foo(s):
                return unicode(s)
            """
    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)
    assert_equal(result.tree.body[0], ast.parse(expected_code).body[0])
    assert_equal(result.tree_changed, True)

# Generated at 2022-06-14 02:19:31.754433
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    sample = "foo = str(42)"

    tree = ast.parse(sample)
    transformed = StringTypesTransformer.transform(tree)

    fixed_tree = ast.parse("foo = unicode(42)")

    assert transformed.tree == fixed_tree
    assert transformed.tree_changed == True

# Generated at 2022-06-14 02:19:36.621021
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
a = str(a)
b = str()
c = type(a)
    """)
    result = StringTypesTransformer.transform(tree)
    print(ast.dump(result.tree))

if __name__ == '__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:19:45.677750
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # no error thrown -> success
    node = ast.parse("x = 'foo'")
    StringTypesTransformer().visit(node)

    transformed = ast.parse("x = unicode(x)")
    assert ast.dump(transformed) == ast.dump(node)

    # transforms all occurences of "str"
    node = ast.parse("x = 'foo'; y = str('bar'); z = str();")
    StringTypesTransformer().visit(node)

    transformed = ast.parse("x = unicode(x); y = unicode(y); z = unicode();")
    assert ast.dump(transformed) == ast.dump(node)

    # no transformation
    node = ast.parse("x = 'foo'; y = str('bar'); z = str();")
    assert not StringTypesTransformer().visit

# Generated at 2022-06-14 02:19:56.604191
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:20:00.013153
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test that the constructor works
    transformer = StringTypesTransformer()
    assert transformer.target == (2, 7)


# Generated at 2022-06-14 02:20:09.008604
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("def func(): return str('hello')")).tree.body[0].body.body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:20:14.419706
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    type_info = {}
    node = ast.Name(id='str')
    transformer = StringTypesTransformer()
    node_transformed = transformer.visit(node, type_info)
    node_transformed = ast.copy_location(node_transformed, node)
    assert ast.dump(node) != ast.dump(node_transformed)

# Generated at 2022-06-14 02:20:20.094155
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
x = 'hello'
    """)
    actual = StringTypesTransformer.transform(tree)
    expected = ast.parse("""
x = 'hello'
    """)
    assert actual.tree != expected

# Generated at 2022-06-14 02:20:23.616832
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    tree = ast.parse('s = str(s)')
    new_tree, changed = transformer.transform(tree)
    assert changed
    assert str(new_tree) == 's = unicode(s)\n'

# Generated at 2022-06-14 02:20:33.219174
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # define the test code
    # test_code = '''
    # b = str
    # '''
    test_code = '''
    b = str
    '''
    # run the formatter
    tree = ast.parse(test_code)
    formatter = StringTypesTransformer()
    formatted_tree = formatter.transform(tree)
    # transform ast back to string
    tree_string = ast.dump(formatted_tree)
    # print formatted code
    print(tree_string)



# Generated at 2022-06-14 02:20:41.531380
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_str = """
print(str(1))
print(str(x))
print(str())
print(str)
    """
    expected_result = """
print(unicode(1))
print(unicode(x))
print(unicode())
print(unicode)
    """
    tr = StringTypesTransformer()
    result = tr.transform(input_str)
    assert result.tree_changed
    assert_equals_ignoring_whitespace(expected_result, compile(result.tree, filename="<ast>", mode="exec"))

# Generated at 2022-06-14 02:20:49.275984
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .utils import get_ast, assert_equal_ast

    data = '''
with open(filename) as f:
    data = f.read()
    return str(data)
'''

    expected = '''
with open(filename) as f:
    data = f.read()
    return unicode(data)
'''
    tree = get_ast(data)
    result = StringTypesTransformer.transform(tree)
    new_tree = ast.fix_missing_locations(result.tree)
    assert_equal_ast(new_tree, expected)

# Generated at 2022-06-14 02:20:53.850275
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    node = ast.Name('str', ast.Load())
    tree = ast.parse('a = str("a")')
    transformer = StringTypesTransformer()
    new_tree = transformer.transform(tree)
    assert(new_tree[0]) == node

# Generated at 2022-06-14 02:20:55.021738
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:20:57.753368
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer('a = str(1)') == 'a = unicode(1)'

# Generated at 2022-06-14 02:21:17.347268
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str(1)')
    result = StringTypesTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert isinstance(result.tree, ast.AST)
    result2 = StringTypesTransformer.transform(result.tree)
    assert result2.tree_changed == False
    assert result2.new_nodes == []
    assert result2.new_nodes == []
    result2.tree == result.tree

# Generated at 2022-06-14 02:21:22.191115
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = '''
        import pandas as pd
        foo = 1
        bar = str(foo)
    '''
    source_tree = ast.parse(source)
    result = StringTypesTransformer.transform(source_tree)
    print(result.tree)
    print(result)
    assert result.tree_changed == True
    assert result.num_errors == 0

# Generated at 2022-06-14 02:21:26.486420
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_code = '''
    a = str(42)
    '''
    expected_result = '''
    a = unicode(42)
    '''
    t = StringTypesTransformer()
    actual_result = t.transform(input_code)
    assert expected_result == actual_result

# Generated at 2022-06-14 02:21:30.324332
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test for constructor of class StringTypesTransformer.

    """
    assert not StringTypesTransformer.transform(None).changed
    assert ast.parse("str('foo')") == StringTypesTransformer.transform(ast.parse("unicode('foo')")).tree

# Generated at 2022-06-14 02:21:32.166669
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Make sure the constructor does not throw an exception
    StringTypesTransformer(None)



# Generated at 2022-06-14 02:21:33.778259
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:21:39.910879
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # given
    code = '''
    def f(x: str) -> str:
        pass
    '''
    tree = ast27.parse(code)

    # when
    result = StringTypesTransformer.transform(tree)

    # then
    assert result.tree_changed
    assert str(result.tree) == '''
    def f(x: unicode) -> unicode:
        pass
    '''

# Generated at 2022-06-14 02:21:49.834990
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    print('Testing StringTypesTransformer')

    tree = ast.parse('if True: x = str(5)')
    actual = StringTypesTransformer.transform(tree)

    print('Expected: if True: x = str(5)')
    print('Actual:', ast.unparse(actual.tree))
    print('Tree is changed:', actual.treeChanged)
    print('Messages:', actual.messages)

    assert 'str' not in ast.unparse(actual.tree)
    assert actual.treeChanged == True
    assert len(actual.messages) == 0

    print('Test Passed!')


# Generated at 2022-06-14 02:22:00.333138
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.testing import get_node_name

    trans = StringTypesTransformer()

    # Basic test
    source = "def foo():\n    a = str(1)\n    return True\n"
    tree = ast.parse(source)
    trans.transform(tree)
    assert get_node_name(tree.body[0].body[0]) == "Assign"
    assert get_node_name(tree.body[0].body[0].value) == "Call"
    assert get_node_name(tree.body[0].body[0].value.func) == "Name"
    assert tree.body[0].body[0].value.func.id == "unicode"
    
    # Check that we do not do anything if 'str' is not the first argument in the function

# Generated at 2022-06-14 02:22:05.062179
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = "if x is None: y = str()"
    tree = ast.parse(code, '<string>', 'exec')
    untransformed = ast.dump(tree)
    result = StringTypesTransformer().transform(tree)
    assert result.tree_changed
    transformed = ast.dump(tree)
    assert untransformed != transformed

# Generated at 2022-06-14 02:22:32.622849
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('''
print str(123)
''')) == TransformationResult(ast.parse('''
print unicode(123)
'''), True, [])

# Generated at 2022-06-14 02:22:36.353366
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer

    tree = ast.parse('str a = "hello"')
    modified_tree = transformer.transform(tree).tree
    assert ast.dump(modified_tree) == ast.dump(ast.parse('unicode a = "hello"'))

# Generated at 2022-06-14 02:22:41.566319
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer(None)
    assert_equal(t.target, (2, 7))
    assert_equal(isinstance(t, BaseTransformer), True)  # assert SuperClass is called


# Generated at 2022-06-14 02:22:42.984189
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()

# Generated at 2022-06-14 02:22:51.122407
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    
    tree = ast.parse("""def f(a):
    a.encode('utf-8') # with utf-8
    return str(a, 'utf-8')""")
    
    StringTypesTransformer.transform(tree)
    

# Generated at 2022-06-14 02:22:58.776453
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('str', mode='eval')) == TransformationResult(ast.parse('unicode', mode = 'eval'), True, [])
    assert StringTypesTransformer.transform(ast.parse('str', mode = 'eval')) != TransformationResult(ast.parse('str', mode = 'eval'), True, [])
    assert StringTypesTransformer.transform(ast.parse('str', mode = 'eval')) != TransformationResult(ast.parse('unicode', mode = 'eval'), False, [])

# Generated at 2022-06-14 02:23:05.763638
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    module = ast.parse('a = str(1)')
    transformed_module, changed = StringTypesTransformer.transform(module)
    if changed:
        print('Transformed code:')
        print(transformed_module)
        exec(compile(transformed_module, '<string>', mode='exec'))
    else:
        print('No changes')

if __name__ == '__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:23:11.883086
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input = """
s = 'string'
s = str('string')
    """
    expected = """
s = 'string'
s = unicode('string')
    """
    tree = ast.parse(input)
    tree_changed, messages, new_tree = StringTypesTransformer.transform(tree)
    assert ast.dump(new_tree) == expected
    assert tree_changed


# Generated at 2022-06-14 02:23:16.563166
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """
a = str()
b = str('foo')
c = str(x)
"""
    expected = """
a = unicode()
b = unicode('foo')
c = unicode(x)
"""
    tree = ast.parse(source)
    StringTypesTransformer.transform(tree)
    actual = ast.unparse(tree)
    assert actual == expected

# Generated at 2022-06-14 02:23:20.198221
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('a = str(b)')
    tree = StringTypesTransformer.transform(tree)
    assert str(tree) == "a = unicode(b)"

# Generated at 2022-06-14 02:24:13.317019
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    src = 'a = str(b)'
    mod = ast.parse(src)
    trf = StringTypesTransformer.transform(mod)
    mod = trf.tree
    assert mod.body[0].value.func.id == 'unicode'


# Generated at 2022-06-14 02:24:20.741443
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    x = """
    a = 'foo'
    b = str(1234)
    """
    tree = ast.parse(x)

    class MockBuilder:
        def __init__(self):
            self.imports = []

    builder = MockBuilder()
    result, changed = StringTypesTransformer.transform(tree, builder)
    assert changed
    assert ast.dump(result) == ast.dump(ast.parse("""
    a = 'foo'
    b = unicode(1234)
    """))

# Generated at 2022-06-14 02:24:24.827096
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('''
x = str(5)
if True:
    y = str(5)
    if True:
        z = str(5)
    else:
        w = str(5)
else:
    x = str(5)
''')).tree.body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:24:34.480479
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils import get_ast
    from ..utils.ast_helpers import compare_asts
    from .base import TransformationResult

    code = '''
        s = str(x)
        def f():
            return type(s)
    '''
    tree = get_ast(code)
    
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed
    assert result.compat_warnings == []

    expected = '''
        s = unicode(x)
        def f():
            return type(s)
    '''
    tree_expected = get_ast(expected)
    assert compare_asts(result.tree, tree_expected)

# Generated at 2022-06-14 02:24:41.021415
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3
    from ..test_utils import assert_equal_asts_py2_7
    ast1 = ast3.parse("a = str()")
    ast2 = ast3.parse("a = unicode()")
    result = StringTypesTransformer(ast1).transform()
    assert_equal_asts_py2_7(result[0], ast2)

# Generated at 2022-06-14 02:24:44.865430
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    x = str
    """
    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)
    assert code_gen.to_source(tree) == code.replace('str', 'unicode')

# Generated at 2022-06-14 02:24:49.359553
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = "a = str('abc')"
    tree = ast.parse(code)
    trans = StringTypesTransformer()
    new_tree = trans.visit(tree)
    assert astor.to_source(new_tree) == "a = unicode('abc')\n"

# Generated at 2022-06-14 02:24:51.970522
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """
    Test if all the string types are converted to unicode
    """
    from .. import transform
    from .. import python_code

# Generated at 2022-06-14 02:25:03.446838
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.python_parser import PythonParser
    from .unittest_support_transformer import UnitTestTransformerSupport
    # Add path where to find the support files.
    UnitTestTransformerSupport.add_path('../transformers/preliminary')
    
    class TreeInstance(UnitTestTransformerSupport):
        """Define the tree structure to be tested. 

        In this case we need to define the name of the module that will be
        analyzed and the sequence of transformations to be performed on it.

        """
        transformer_sequence = [
            ("StringTypesTransformer", {})
        ]
        test_module_name = "test_StringTypesTransformer"
    
    
    tree_instance = TreeInstance()
    tree_instance.test()

# Generated at 2022-06-14 02:25:05.336454
# Unit test for constructor of class StringTypesTransformer