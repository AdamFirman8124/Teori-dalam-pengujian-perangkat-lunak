

# Generated at 2022-06-14 02:17:12.682546
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.fake import FakeFile
    from ..utils.source import source_to_tree

    source = FakeFile("""
        a = str(1 + 2)
        b = unicode(3 + 4)
        c = str('foo')
        def f(a, b):
            pass
    """)

    tree = source_to_tree(source)
    result = StringTypesTransformer.transform(tree)
    _, tree, _ = result

    assert result.tree_changed
    assert isinstance(tree.body[0].value, ast.BinOp)
    assert isinstance(tree.body[0].value.left, ast.Name)
    assert tree.body[0].value.left.id == 'unicode'

    assert isinstance(tree.body[2].value, ast.BinOp)

# Generated at 2022-06-14 02:17:14.272443
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.__name__ == 'StringTypesTransformer'


# Generated at 2022-06-14 02:17:21.141535
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
	tree = ast.parse('a = str(b)')
	tree2 = ast.parse('a = unicode(b)')
	test_function = StringTypesTransformer().transform(tree)
	assert(test_function[0].body[0].value.func.id == tree2.body[0].value.func.id)

# Generated at 2022-06-14 02:17:33.211539
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import types
    import unittest
    import typed_astunparse
    import typed_ast.ast3 as ast
    
    class tester(unittest.TestCase):

        def setUp(self):
            """
            set up data used in the tests
            setUp is called before each test function execution.
            """
            self.transformer = StringTypesTransformer()

        def test_stringtype(self):
            """Test for typing str to unicode in the function."""
            code = """def func1():
                x = str()"""
            tree = ast.parse(code)
            self.transformer.transform(tree)
            self.assertEqual(typed_astunparse.unparse(tree),
                             "def func1():\n    x = unicode()")


# Generated at 2022-06-14 02:17:34.108619
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:17:41.423071
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typing as t
    import typed_ast.ast3 as typed_ast

    trees = [
        """
        call = str('hello world')
        """,
        """
        call = list[str]('hello world')
        """,
        """
        def f(a: str):
            return a
        """
    ]

    for tree in trees:
        tree: typed_ast.AST
        tree = typed_ast.ast3.parse(tree)
        StringTypesTransformer.transform(tree)
        print(typed_ast.ast3.dump(tree))

# Generated at 2022-06-14 02:17:42.385205
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor

# Generated at 2022-06-14 02:17:45.216613
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("if 'a' == str('b'):\n\tpass")
    transformed = StringTypesTransformer.transform(tree)
    assert transformed.tree_changed


# Generated at 2022-06-14 02:17:47.872621
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    x = StringTypesTransformer()
    assert x.tree is None
    assert x.tree_changed is False
    assert x.log == []
    assert x.source_code is None
    assert x.source_code_changed is False
    assert x.context == {}

# Generated at 2022-06-14 02:17:48.818267
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:56.017547
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
str('abc')
    '''
    new_code = '''
unicode('abc')
    '''
    tree = ast.parse(code)
    transform_result = StringTypesTransformer.transform(tree)

# Generated at 2022-06-14 02:18:03.510073
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import pytest
    from .test_utils import transform_in_pythran_syntax

    tree = ast.parse("""
    from builtins import str, unicode
    from builtins import int
    from builtins import object
    from collections import abc
    from collections import Iterable
    a: str = ''
    b: str
    b = 'b'
    c: str
    c = str(1)
    def f(x: str):
        return x
        """)


# Generated at 2022-06-14 02:18:07.310514
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    mod = ast.parse("print(len(str(1))); str = 'hello'")
    StringTypesTransformer.transform(mod)
    expected = "print(len(unicode(1))); unicode = 'hello'"
    assert astor.to_source(mod) == expected

# Generated at 2022-06-14 02:18:13.623447
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Set up a tree.
    tree = ast.parse("a = str(5)")

    # Set up an instance of StringTypesTransformer
    transformer = StringTypesTransformer()

    # Run the transformation.
    TransformationResult.display_results(*transformer.transform(tree))

    # Display the new tree.
    print()
    print(ast.dump(tree))

# Generated at 2022-06-14 02:18:14.864723
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:21.492506
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    a1 = ast.Name(id="str", ctx=ast.Param())
    a2 = ast.Str(s="Hello")
    a3 = ast.Module(body=[a1, a2])

    r1 = StringTypesTransformer.transform(a3)
    assert(r1.tree.body[0].id == "unicode")

# Generated at 2022-06-14 02:18:22.386105
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Constructor test
    StringTypesTransformer()

# Generated at 2022-06-14 02:18:30.961830
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    x = 1 + 2
    y = 'hello'
    z = foo(1,2,3)
    a = '{x} {y} {z}'.format(x=x, y=y, z=z)
    b = '{0} {1} {2}'.format(x, y, z)
    c = '{:.2f}'.format(1.2)
    d = [str(i) for i in range(10)]
    e = str(x)
    f = '{str(x)}'.format(x)

# Generated at 2022-06-14 02:18:31.931287
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:43.288004
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..ast import to_source
    from ..__pkginfo__ import version

    transform = StringTypesTransformer.transform

    tree = ast.parse('else')
    result = transform(tree, version=(2, 6))
    assert result == TransformationResult(tree, False, [])

    tree = ast.parse('else')
    result = transform(tree, version=(2, 7))
    assert result == TransformationResult(tree, True, [])

    tree = ast.parse('if isinstance(x, str):\n  pass')
    result = transform(tree, version=(2, 6))
    assert result == TransformationResult(tree, False, [])

    tree = ast.parse('if isinstance(x, str):\n  pass')
    result = transform(tree, version=(2, 7))

# Generated at 2022-06-14 02:18:54.040952
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .base import BaseTransformerTest

    source = """
            # -*- coding: utf-8 -*-

            def hello():
                return "Hello World"

            def goodbye():
                return "Goodbye World"
            """

    expected = """
            # -*- coding: utf-8 -*-

            def hello():
                return u"Hello World"

            def goodbye():
                return u"Goodbye World"
            """

    result = BaseTransformerTest.test_transform_from_input(StringTypesTransformer, source)
    assert result == expected


# Generated at 2022-06-14 02:18:59.468350
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3, parse
    from .context import Context
    from .base import BaseTransformer

    tree = parse("""
    s = str(x)
    """)

    tree = StringTypesTransformer.transform(tree)
    BaseTransformer.resolve(tree, Context())

    assert tree.body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:19:02.762879
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert (StringTypesTransformer.transform(ast.parse('a = str()'))) == \
        TransformationResult(ast.parse('a = unicode()'), True, [])

# Generated at 2022-06-14 02:19:10.953848
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """ Unit test to verify the class StringTypesTransformer.

    """

# Generated at 2022-06-14 02:19:12.017590
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:19:17.622753
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
        print(str(123))
    '''
    expected = '''
        print(unicode(123))
    '''
    tree1 = ast.parse(code)
    tree2 = ast.parse(expected)

    tree1 = StringTypesTransformer.transform(tree1)
    assert ast.dump(tree1) == ast.dump(tree2)

# Generated at 2022-06-14 02:19:23.509588
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_unicode
    from ..utils.tree import tree_to_str

    source = source_to_unicode("""
d = str(2)

""")
    tree = ast.parse(source)
    new_tree, changed = StringTypesTransformer.transform(tree)
    assert changed is True
    expected_source = source_to_unicode("""
d = unicode(2)

""")
    assert tree_to_str(new_tree) == expected_source

# Generated at 2022-06-14 02:19:32.842139
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class Node:
        def __init__(self, children, id=None):
            self.children = children
            self.id = id

    class Leaf(Node):
        def __init__(self, id=None):
            super().__init__([], id)

    class Name(Leaf):
        pass
    
    tree_before = Name('str')
    tree_after = Name('unicode')

    tree = Node([Node([Node([tree_before])])])

    tr = StringTypesTransformer.transform(tree)

    assert tr.tree == tree_after
    assert tr.tree_changed == True
    assert tr.log == []

# Generated at 2022-06-14 02:19:39.591745
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    def foo(my_text):
        my_unicode = unicode(my_text)
        text = str(my_text)
        return text
    """
    tree = ast.parse(code)
    tree = StringTypesTransformer.transform(tree)
    assert tree.code == """
    def foo(my_text):
        my_unicode = unicode(my_text)
        text = unicode(my_text)
        return text
    """



# Generated at 2022-06-14 02:19:44.827778
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test case for this class.

    """
    # Test case 1: test if the class is able to convert from str to unicode.
    program_str = '''
    a = str
    '''
    expected_str = '''
    a = unicode
    '''
    tree = ast.parse(program_str)
    new_tree = StringTypesTransformer.transform(tree)
    assert astor.to_source(new_tree.tree) == expected_str

# Generated at 2022-06-14 02:20:02.465769
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Create an AST
    tree = ast.parse('def foo():\n    return str("Foo")')

    # Mutate the tree
    result = StringTypesTransformer(tree)

    # Check if the result is as expected
    assert result.tree_changed
    assert len(result.log) == 1
    assert result.log[0] == 'Replaced str() with unicode()'

# Generated at 2022-06-14 02:20:10.057988
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("class Test(object):\n\tdef __init__(self, name: str) -> None:\n\t\tself.name = name\n\t@staticmethod\n\tdef func() -> str:\n\t\treturn 'string'")
    StringTypesTransformer.transform(tree)
    assert ast.dump(tree) == dedent("""\
    class Test(object):
        def __init__(self, name: unicode) -> None:
            self.name = name
        @staticmethod
        def func() -> unicode:
            return 'string'""")

# Generated at 2022-06-14 02:20:14.470177
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    m = ast.parse("a = str()\n")
    m_transformed, changed, messages = StringTypesTransformer.transform(m)
    assert changed
    m_eval = ast.parse("a = unicode()\n")
    assert ast.dump(m_transformed) == ast.dump(m_eval)


# Generated at 2022-06-14 02:20:20.826313
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert_result = {'tree_changed': False, 'errors': []}
    assert_result_changed = {'tree_changed': True, 'errors': []}

    assert StringTypesTransformer.transform(ast.parse('')) == assert_result
    assert StringTypesTransformer.transform(
        ast.parse('str')) == assert_result_changed

# Generated at 2022-06-14 02:20:26.756573
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    input_str = str(input("Enter your name: "))
    print("Hello " + input_str)
    """

    tree = ast.parse(code)
    tree = StringTypesTransformer.transform(tree)
    exec(compile(tree, filename="<ast>", mode="exec"))

# Generated at 2022-06-14 02:20:31.019469
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    b = 2
    """
    tree = ast.parse(code)
    transformer = StringTypesTransformer()
    res = transformer.transform(tree)
    assert res.tree.body[0].value.id == 'b'

# Generated at 2022-06-14 02:20:42.257849
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Build AST
    stringbasic = ast.Str(s='This is a string')
    stringvar = ast.Name(id='unicode', ctx=ast.Load())
    stringfunction = ast.Call(func=ast.Name(id='unicode', ctx=ast.Load()), args=[], keywords=[], starargs=None,
                              kwargs=None)
    stringformat = ast.BinOp(left=ast.Str(s='I love '), op=ast.Mod(), right=ast.Str(s='strings'))
    stringassignment = ast.Assign(targets=[ast.Name(id='strname', ctx=ast.Store())], value=ast.Str(s='string'))


# Generated at 2022-06-14 02:20:50.282413
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import Source
    from ..utils.tree import to_source

    source = Source.from_string('def f(x: str) -> int:\n    return 0')
    tree = source.parse()

    transformer = StringTypesTransformer(tree, source)

    assert transformer.is_applicable()

    transformer.apply()
    assert to_source(tree).strip() == 'def f(x: unicode) -> int:\n    return 0'

# Generated at 2022-06-14 02:20:52.595003
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast


# Generated at 2022-06-14 02:20:58.054560
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test code
    code = """def foo(a):
        if type(a) == str:
            return (a > 5)
        else:
            return False"""

    # Expected result
    expected_code = """def foo(a):
        if type(a) == unicode:
            return (a > 5)
        else:
            return False"""

    tree = ast.parse(code)
    res = StringTypesTransformer.transform(tree)
    assert ast.dump(res.tree) == expected_code

# Generated at 2022-06-14 02:21:18.062251
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source_code = '''
    def test(x):
        return str(x)
    '''
    tree = ast.parse(source_code)
    tree_changed, _ = StringTypesTransformer.transform(tree)
    new_code = compile(tree, '', 'exec')
    globals = {}
    locals = {'__name__': '__main__'}
    exec(new_code, globals, locals)
    assert(locals['test']('a') == 'a')

# Generated at 2022-06-14 02:21:18.969678
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:21:28.772294
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test 1: if a tree is given, the transformer will transform it
    source = """
f = lambda t: str(t)
"""
    expected = """
f = lambda t: unicode(t)
"""
    tree = ast.parse(source)
    new_tree, tree_changed, messages = StringTypesTransformer.transform(tree)
    assert tree_changed
    assert ast.dump(new_tree) == expected

    # Test 2: if a tree has no str in it, the transformer will not change it
    source = """
f = lambda t: s(t)
"""
    tree = ast.parse(source)
    new_tree, tree_changed, messages = StringTypesTransformer.transform(tree)
    assert not tree_changed
    assert ast.dump(new_tree) == source

# Generated at 2022-06-14 02:21:38.086034
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
        s = str(1)
        t = str(2)
        u = str(3)
    '''
    tree = ast.parse(code)
    res = StringTypesTransformer.transform(tree)
    assert res.tree_changed == True
    assert res.num_nodes_visited == 3
    assert res.error_log == []
    assert astor.to_source(res.tree).strip() == astor.to_source(ast.parse('''
        s = unicode(1)
        t = unicode(2)
        u = unicode(3)
    ''')).strip()

# Generated at 2022-06-14 02:21:44.572570
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    #    global count
    #    count = 0
    result = StringTypesTransformer.transform(ast.parse('x = str(y)'))
    assert result.tree_changed is True
    assert not result.warnings

    result = StringTypesTransformer.transform(ast.parse('x = y + str(z)'))
    assert result.tree_changed is True
    assert not result.warnings

    result = StringTypesTransformer.transform(ast.parse('x = str(y)'))
    assert result.tree_changed is True
    assert not result.warnings


# Generated at 2022-06-14 02:21:49.123342
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    source2target = \
        {
            "a = str(123)" : "a = unicode(123)"
        }
    PythonTransformerTest.testTransformer(transformer, source2target)

# Generated at 2022-06-14 02:21:57.965313
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(None) == None
    assert StringTypesTransformer.transform(ast.parse("str(foo)")) == ast.parse("str(foo)")
    assert StringTypesTransformer.transform(ast.parse("a = str(foo)")) == ast.parse("a = str(foo)")
    assert StringTypesTransformer.transform(ast.parse("str(foo) == 'bar'")) == ast.parse("str(foo) == 'bar'")
    assert StringTypesTransformer.transform(ast.parse("str.upper(foo)")) == ast.parse("str.upper(foo)")

# Generated at 2022-06-14 02:22:01.481299
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    node = ast.Name('str', ast.Load())
    tree = ast.parse("str is not unicode")
    result = StringTypesTransformer.transform(tree)
    assert result.tree != tree
    assert result.tree_changed

# Generated at 2022-06-14 02:22:06.833095
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from textwrap import dedent

    from ..utils.source import Source

    source = Source(dedent("""
        def f(x):
            return str(x)
    """))
    tree = source.tree
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed
    assert result.tree.body[0].body.body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:22:18.335787
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:22:49.655857
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    def do_test(s):
        return StringTypesTransformer().visit(ast.parse(s))

    #  Test 'str'
    s = "a = str(b)"
    result = do_test(s)
    assert result == "a = unicode(b)"

    # Test 'str' with variable
    s = "a = str(b)"
    result = do_test(s)
    assert result == "a = unicode(b)"

    # Test 'str' with variable and string literal
    s = "a = str(b) + str('c')"
    result = do_test(s)
    assert result == 'a = unicode(b) + unicode(\'c\')'

    # Test 'str' with expression
    s = "a = str(b + c)"
    result = do_

# Generated at 2022-06-14 02:22:58.687168
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.codegen import to_source
    from typed_ast import ast3
    import astor
    tests = [
        ["""assert isinstance('', str)""", """assert isinstance('', unicode)"""],
        ["""assert isinstance('', str(1))""", """assert isinstance('', unicode(1))"""],
    ]
    for test in tests:
        new_tree = astor.parse_file(StringTypesTransformer.transform(astor.parse_file(test[0]))[0])
        new_source = to_source(new_tree)
        assert new_source == test[1]

# Generated at 2022-06-14 02:23:02.760205
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_helpers import assert_program_equivalent, string_types_transformer_test_case
    assert_program_equivalent(
        string_types_transformer_test_case,
        StringTypesTransformer,
    )

# Generated at 2022-06-14 02:23:12.640667
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.testing import assert_transformed_source

    assert_transformed_source(
        StringTypesTransformer,
        'str(1)',
        'unicode(1)',
    )

    assert_transformed_source(
        StringTypesTransformer,
        'str',
        'unicode',
    )

    assert_transformed_source(
        StringTypesTransformer,
        'str(a, b, c)',
        'unicode(a, b, c)',
    )

    assert_transformed_source(
        StringTypesTransformer,
        'def a(b: str): return b + 1',
        'def a(b: unicode): return b + 1',
    )

# Generated at 2022-06-14 02:23:21.336339
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Given
    tree = ast.parse(u'a = str()')
    expected_tree = ast.parse(u'a = unicode()')
    transformer = StringTypesTransformer()

    # When
    actual_transformation_result = transformer.transform(tree)

    # Then
    assert actual_transformation_result.tree == expected_tree
    assert actual_transformation_result.tree_changed == True
    assert actual_transformation_result.files_changed == []

# Generated at 2022-06-14 02:23:32.811610
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.transform import transform, assert_transform
    from .. import utils
    from ..utils.source import dedent

    tree_a = utils.parse(dedent('''
    a = 'a' + str(5)
    b = str(5) + 'a'
    c = str(5) + str(5)
    d = str(5)
    e = str(5, 'utf-8')
    '''))


# Generated at 2022-06-14 02:23:36.968336
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    a = ast.Name('str', ast.Load())
    t = StringTypesTransformer.transform(a)
    assert t.tree == ast.Name('unicode', ast.Load())

# Generated at 2022-06-14 02:23:42.749673
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    import astor

    code = '''
result = str(2)
'''

    tree = ast.parse(code)
    print(astor.to_source(tree))

    tree = StringTypesTransformer.transform(tree)
    print(astor.to_source(tree.tree))




if __name__ == '__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:23:48.787156
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Example with only 1 change
    assert StringTypesTransformer.transform(ast.parse('print(str(5))')) == (ast.parse('print(unicode(5))'), 1)

    # Example with no change
    assert StringTypesTransformer.transform(ast.parse('print(type(5))')) == (ast.parse('print(type(5))'), 0)

#-----------------------------------------------------------------------------


# Generated at 2022-06-14 02:23:50.027747
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:24:42.847246
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    expected_original_code = "str(1)"
    expected_transformed_code = "unicode(1)"
    transformer = StringTypesTransformer()
    src_transformed = transformer.src_to_src(expected_original_code)
    assert src_transformed == expected_transformed_code

# Generated at 2022-06-14 02:24:47.776009
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from ..utils.tree import parse

    tree = parse('str(1)')
    assert astor.to_source(tree).strip() == 'str(1)'
    tree = StringTypesTransformer.run_on_single_file(tree)
    assert astor.to_source(tree).strip() == 'unicode(1)'

# Generated at 2022-06-14 02:24:51.988550
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.fake_ast import fake_ast_with_str_node
    res = StringTypesTransformer.transform(fake_ast_with_str_node())
    assert type(res) is TransformationResult
    assert res.tree is not None
    assert res.tree_changed == True

# Generated at 2022-06-14 02:24:53.602784
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:24:58.341492
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
x = str
'''
    module = ast.parse(code)
    StringTypesTransformer.transform(module)
    assert ast.dump(module) == ast.dump(ast.parse('''
x = unicode
'''))

# Generated at 2022-06-14 02:25:07.148529
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.node_util import node_to_code

    source = """
    a = 'hello'
    b = str()
    """
    expected = """
    a = 'hello'
    b = unicode()
    """

    tree = ast.parse(source)
    t = StringTypesTransformer()
    result = t.transform(tree)
    assert node_to_code(result.tree) == expected


# Generated at 2022-06-14 02:25:18.385634
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("foo(1)")).tree_changed is False

    assert ast.dump(StringTypesTransformer.transform(ast.parse("foo(1, bar=str)")).tree) == \
        'Module(body=[Expr(value=Call(func=Name(id=\'foo\', ctx=Load()), args=[Num(n=1)], keywords=[keyword(arg=\'bar\', value=Name(id=\'unicode\', ctx=Load()))]))])'


# Generated at 2022-06-14 02:25:24.979109
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    x = str()
    """
    tree = ast3.parse(code)
    t = StringTypesTransformer()
    new_tree = t.visit(tree)
    assert ast3.dump(new_tree, include_attributes=True) == ast3.dump(ast3.parse("x = unicode()"), include_attributes=True)
    print(ast3.dump(new_tree, include_attributes=True))

# Generated at 2022-06-14 02:25:29.886949
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast

    tree = ast.parse('a = str("a")', mode='eval')
    transform = StringTypesTransformer.transform(tree)
    assert 'a = unicode("a")' == transform.node.body.value.left.id

# Generated at 2022-06-14 02:25:31.297946
# Unit test for constructor of class StringTypesTransformer