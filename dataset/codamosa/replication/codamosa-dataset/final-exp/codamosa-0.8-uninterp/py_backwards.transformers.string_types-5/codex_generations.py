

# Generated at 2022-06-14 02:17:07.097398
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Given
    from typed_ast import ast3 as ast
    from ..utils import parse

    src = u'a = str(1)'

    # When
    tree = parse(src)
    new_tree, changed, errors = StringTypesTransformer.transform(tree)

    # Then
    assert changed
    assert len(errors) == 0

    src2 = u'a = unicode(1)'
    tree2 = parse(src2)
    assert ast.dump(new_tree) == ast.dump(tree2)

# Generated at 2022-06-14 02:17:14.730682
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    source = '''
            def x(z):
                return str(z)
            '''
    expected = '''
            def x(z):
                return unicode(z)
            '''

    tr = StringTypesTransformer()

    tree = astor.parse_file(source)
    actual_tree, _, _ = tr.transform(tree)
    actual = astor.to_source(actual_tree)

    assert actual == expected

# Generated at 2022-06-14 02:17:20.849082
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    #test case 1
    root = ast.parse("a = str()")
    result = StringTypesTransformer.transform(root)
    assert result.tree_changed
    assert result.tree_transformed.body[0].value.func.id == 'unicode'
    assert result.tree_transformed.body[0].value.args == []

# Generated at 2022-06-14 02:17:25.870105
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # x: str = type(u'abc')
    test_ast = ast.Assign([ast.Name('x', ast.Store())], ast.Call(ast.Name('type', ast.Load()), [ast.Str('abc')], [], None, None))

# Generated at 2022-06-14 02:17:32.819306
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils import assert_equal_with_printing

    text = '''
    a = str(1)
    b = unicode(2)
    '''
    l_expected = [
    '    a = unicode(1)',
    "    b = unicode(2)",
    ]

    tree_a = ast.parse(text)
    out_a = str(ast.fix_missing_locations(StringTypesTransformer.transform(tree_a)))

    assert_equal_with_printing(out_a, '\n'.join(l_expected))

# Generated at 2022-06-14 02:17:37.733243
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("str(0)")
    StringTypesTransformer.transform(tree)
    assert(ast.dump(tree) == "Expr(value=Call(func=Name(id='unicode', ctx=Load()), args=[Num(n=0)], keywords=[], starargs=None, kwargs=None))")


# Generated at 2022-06-14 02:17:41.594377
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # This should fail without the call to `transformer.transform`
    transformer = StringTypesTransformer()
    transformer.transform(ast.parse('assertTrue(isinstance(x, str))'))

# Generated at 2022-06-14 02:17:42.520967
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:43.082856
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:17:46.747957
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
        def func(x: str):
            pass
    '''
    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)
    checker = StringTypesTransformer.get_checker()
    assert checker.visit(tree) == True

# Generated at 2022-06-14 02:17:52.391065
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    import astor
    source = """str(123)"""
    tree = ast.parse(source)
    StringTypesTransformer.transform(tree)
    print(astor.to_source(tree))

# Generated at 2022-06-14 02:17:54.333772
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor


# Generated at 2022-06-14 02:17:59.976528
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.dummy_context import DummyContext
    from ..semantics.resolver import Resolver
    from ..semantics.symbol_table import SymbolTable
    from ..semantics.symbol import Symbol, SymbolTableScope

    resolver = Resolver(DummyContext(), SymbolTable())

# Generated at 2022-06-14 02:18:09.693692
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .transform_imports import transform_imports_factory
    from ..utils import evaluate_transformation

    evaluate_transformation(
        StringTypesTransformer.transform,
        "x = str('a')",
        "x = unicode('a')",
    )

    # Now with a foreign import
    evaluate_transformation(
        transform_imports_factory(StringTypesTransformer.transform),
        "from something import str as mystr; x = mystr('a')",
        "from __future__ import unicode_literals; from something import unicode as myunicode; x = myunicode('a')",
    )

# Generated at 2022-06-14 02:18:19.002144
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """StringTypesTransformer test.
    
    """
    from .fake_parser import fake_parser
    from os.path import dirname, join, realpath
    from ..utils.parser import parse_module_from_path

    path = join(dirname(realpath(__file__)), "fixtures/sample2.py")
    tree = parse_module_from_path(path)
    tree = fake_parser(tree)
    tree, changed, _ = StringTypesTransformer.transform(tree)

    print(ast.dump(tree))
    assert changed, "Expecte True, but got {} instead.".format(changed)


# Generated at 2022-06-14 02:18:22.257109
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_unicode
    from ..utils.tree import ast_from_string, dump


# Generated at 2022-06-14 02:18:25.921622
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    a = ast.AST()
    b = ast.Name()
    b.id = 'str'
    a.body = [b]

    c = StringTypesTransformer.transform(a)
    assert c.tree.body[0].id == 'unicode'

# Generated at 2022-06-14 02:18:36.268661
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # test_str is the test string for this unit test
    test_str = "a = str('Hello World')"

    # test_ast is the Abstract Syntax Tree for the above test string
    test_ast = ast.parse(test_str)

    # test_result_ast is the expected Abstract Syntax Tree after applying
    # the StringTypesTransformer on the test_ast
    test_result_ast = ast.parse("a = unicode('Hello World')")

    # Calling the transform() method for StringTypesTransformer with the
    # test_str as its argument and checking if the resulting Abstract Syntax
    # Tree is equal to the expected Abstract Syntax Tree test_result_ast
    StringTypesTransformer.transform(test_ast) == test_result_ast

# Generated at 2022-06-14 02:18:47.447314
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    ast_tree = ast.parse('''from a import b\nfrom c import d as e\nimport f.g as h\nprint(b)''')
    transformer = StringTypesTransformer.instantiate()
    transformed_ast, tree_changed, _ = transformer.transform(ast_tree)
    assert not tree_changed
    assert ast.dump(transformed_ast) == ast.dump(ast_tree)

    ast_tree = ast.parse('''a = str''')
    transformer = StringTypesTransformer.instantiate()
    transformed_ast, tree_changed, _ = transformer.transform(ast_tree)
    assert tree_changed
    assert ast.dump(transformed_ast) == ast.dump(ast.parse('a = unicode'))


# Generated at 2022-06-14 02:18:51.785822
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        f = str("Hello World")
    """
    module = ast.parse(code)
    tree = StringTypesTransformer.transform(module)
    assert tree.node.body[0].value.args[0].s == "Hello World"
    assert tree.tree_changed == True

# Generated at 2022-06-14 02:19:02.409801
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import unittest
    import ast
    import sys
    import os
    import textwrap

    class TestStringTypesTransformer(unittest.TestCase):
        def setUp(self):
            self.maxDiff = None

        def test_str_to_unicode(self):
            initial = textwrap.dedent('''
            a = str(b)
            ''')
            expected = textwrap.dedent('''
            a = unicode(b)
            ''')
            tree = ast.parse(initial)
            transformer = StringTypesTransformer()
            result = transformer.transform(tree)
            self.assertEqual(ast.dump(tree), expected)
            self.assertEqual(textwrap.strip(transformer.get_patch()), '')

        def test_str(self):
            initial

# Generated at 2022-06-14 02:19:09.733817
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    string = 'something'
    """
    expected_code = """
    string = 'something'
    """
    tree = ast.parse(textwrap.dedent(code))
    result_tree = StringTypesTransformer.transform(tree)
    result_code = astor.to_source(result_tree.tree).strip()
    assert result_code == expected_code, result_code


# Generated at 2022-06-14 02:19:10.921989
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:19:17.093132
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    test_ast = ast.parse('def test(): a = str(1)')
    (tree_changed, messages) = StringTypesTransformer.transform(test_ast)
    print(ast.dump(test_ast))
    assert tree_changed == True
    assert test_ast.body[0].body[0].value.func.id == 'unicode'
    print('stringtype_test passed!')
    return

# Generated at 2022-06-14 02:19:17.928949
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:19:20.883940
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    test_code = '''
result = str([])
'''
    expected_code = '''
result = unicode([])
'''
    result = StringTypesTransformer.transform(CodeString(test_code))
    assert result.transformed_code == CodeString(expected_code)

# Generated at 2022-06-14 02:19:26.835189
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_helpers import get_tests

    test_cases = get_tests(__file__, 'StringTypesTransformer')
    for test_case in test_cases:
        ast2 = test_case.ast2
        ast3 = test_case.transformed

        transformed = StringTypesTransformer.transform(ast2)
        assert transformed.tree == ast3

# Generated at 2022-06-14 02:19:32.784494
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import sys
    sys.path.insert(0, '.')
    import string_types
    import typed_ast.ast3
    # Constructor
    assert isinstance(string_types.StringTypesTransformer, type)
    class_ = string_types.StringTypesTransformer
    instance = class_()
    assert isinstance(instance, class_)
    # transform
    assert string_types.StringTypesTransformer.transform.__annotations__ == {'tree': 'typed_ast.ast3.AST', 'return': 'TransformationResult'}

# Generated at 2022-06-14 02:19:39.881496
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = 'def foo(a: str): pass'

    ast_tree = ast.parse(code)
    transformed_tree, changed = StringTypesTransformer.transform(ast_tree)

    assert changed
    assert 'unicode' == find(transformed_tree, ast.Name)[0].id

    # also test that attribute access works
    code = 'a.test_str()'

    ast_tree = ast.parse(code)
    transformed_tree, changed = StringTypesTransformer.transform(ast_tree)

    assert not changed

# Generated at 2022-06-14 02:19:45.413312
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
foo = 'bar'
print(type(foo))
    '''
    expected_code = '''
foo = 'bar'
print(type(foo))
    '''
    tree = ast.parse(code)
    transformer = StringTypesTransformer()
    result = transformer.transform(tree)
    assert result.tree_changed == False
    assert result.code == expected_code

# Generated at 2022-06-14 02:19:59.662584
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_code = """\
x = "test string"
y = str(x)
"""
    expected_code = """\
x = u"test string"
y = unicode(x)
"""
    tree = ast.parse(input_code)
    transformed_tree, tree_changed = StringTypesTransformer.transform(tree)
    assert tree_changed is True
    generated_code = astunparse.unparse(transformed_tree)
    assert generated_code == expected_code


# Generated at 2022-06-14 02:20:02.258455
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    """.strip()

    tree = ast.parse(code)
    tree = StringTypesTransformer.run_pipeline(tree)
    assert tree

# Generated at 2022-06-14 02:20:07.811748
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_code = """
            variable = str(str_name)
            print "Hello, World\n"
    """
    expected_output = """
            variable = unicode(str_name)
            print "Hello, World\n"
    """
    trans = StringTypesTransformer()
    actual_output, tree_changed = trans.transform_snippet(input_code)
    assert expected_output == actual_output

# Generated at 2022-06-14 02:20:19.160798
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = '''
    def my_func(foo):
        return str(foo)
    '''
    tree = ast.parse(source)
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed
    assert result.errors == []
    result_source = compile(result.tree, filename='<ast>', mode='exec')
    assert 'def my_func(foo):\n    return unicode(foo)\n' in result_source
    # Make sure the call to the transformed function works
    # TODO - should work but get error
    #locals = {}
    #exec(result_source, locals)
    #assert locals['my_func'](1) == '1'

# Generated at 2022-06-14 02:20:20.857230
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('')
    transformer = StringTypesTransformer()
    result = transformer.transform(tree)

    assert type(result) == TransformationResult

# Generated at 2022-06-14 02:20:23.185003
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    given_class = StringTypesTransformer()
    given_class.__class__

# Generated at 2022-06-14 02:20:33.931290
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()

    assert transformer.transform(ast.parse('''str()''')) == TransformationResult(
        ast.parse('''unicode()'''),
        True, [])

    assert transformer.transform(ast.parse('''foo = str()''')) == TransformationResult(
        ast.parse('''foo = unicode()'''),
        True, [])

    assert transformer.transform(ast.parse('''foo = str.foo''')) == TransformationResult(
        ast.parse('''foo = unicode.foo'''),
        True, [])


# Generated at 2022-06-14 02:20:43.293044
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from .resolver import NameResolver
    source = """
    def foo(a):
        return str(a)

    def bar(a):
        return str.strip(a)
    """
    tree = astor.parse_file(source)
    NameResolver().resolve(tree)
    StringTypesTransformer().transform(tree)
    expected = """
    def foo(a):
        return unicode(a)

    def bar(a):
        return unicode.strip(a)
    """
    assert astor.to_source(tree) == expected


# Generated at 2022-06-14 02:20:49.822567
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from tests.utils import transform
    
    src = '''
print(str)
'''
    src_after = '''
print(unicode)
'''
    tree = ast.parse(src)
    tree_after = ast.parse(src_after)
    
    result = StringTypesTransformer.transform(tree)
    assert result.tree == tree_after


# Generated at 2022-06-14 02:20:54.518635
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    src = """
        A = 1
        str(A)
    """
    tree = ast.parse(src)
    tree = StringTypesTransformer.run(tree)
    assert isinstance(tree, ast.Module)
    assert tree is not None


# Generated at 2022-06-14 02:21:11.673677
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import textwrap
    source = textwrap.dedent("""\
        def foo(a, b):
            return str(b).strip() + str(a)
        """)

    tree = ast.parse(source)
    tr = StringTypesTransformer()
    new_tree = tr.transform(tree)

    assert new_tree.tree_changed == True
    print(ast.dump(new_tree.new_tree))

    assert new_tree.log == []

# Generated at 2022-06-14 02:21:20.977471
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Testing with different initial values
    assert StringTypesTransformer.transform(ast.parse('str')) == \
        TransformationResult(ast.parse('unicode'), True, [])
    assert StringTypesTransformer.transform(ast.parse('a = str')) == \
        TransformationResult(ast.parse('a = unicode'), True, [])
    assert StringTypesTransformer.transform(ast.parse('print(str)')) == \
        TransformationResult(ast.parse('print(unicode)'), True, [])

# Generated at 2022-06-14 02:21:32.717152
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        def add(x: str, y: str) -> str:
            pass
    """
    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)

    assert ast.dump(tree) == """
Module(body=[FunctionDef(name='add', args=arguments(args=[
    arg(arg='x', annotation=Name(id='unicode', ctx=Load())), 
    arg(arg='y', annotation=Name(id='unicode', ctx=Load()))], 
    vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), 
    body=[Pass()], decorator_list=[], returns=Name(id='unicode', ctx=Load()))])
"""

# Generated at 2022-06-14 02:21:39.044364
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tests = [
        (
            'import string',
            'import string'
        ),
        (
            'foo = str()',
            'foo = unicode()'
        ),
        (
            'foo = str("bar")',
            'foo = unicode("bar")'
        )
    ]

    for before, after in tests:
        assert StringTypesTransformer.transform(before) == after

# Generated at 2022-06-14 02:21:51.202625
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class Test:
        def __init__(self, node):
            self._node = node
            self._modified = False

    # __init__ function
    node = ast.Name(id="str", ctx=ast.Load())
    test = Test(node)
    StringTypesTransformer().visit(test)
    assert not test._modified
    # __init__ function modified AST
    assert node.id == 'unicode'
    # __init__ function returned
    assert isinstance(node, ast.Name)

    # empty tree
    node = ast.Module(body=[])
    test = Test(node)
    StringTypesTransformer().visit(test)
    assert not test._modified
    assert isinstance(node, ast.Module)

    # has unwanted node

# Generated at 2022-06-14 02:21:55.252157
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        def function(name):
            return "Hello " + name
    """
    transformations = [StringTypesTransformer]
    node = ast.parse(code)

    for t in transformations:
        result = t.transform(node)
        assert result.tree_changed
        node = result.tree

# Generated at 2022-06-14 02:22:02.895435
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.contains_target(ast.parse("""
        x = str
    """, mode='exec'))
    assert StringTypesTransformer.transform(ast.parse("""
        x = str
    """, mode='exec')).tree_changed
    assert not StringTypesTransformer.transform(ast.parse("""
        x = unicode
    """, mode='exec')).tree_changed
    assert StringTypesTransformer.transform(ast.parse("""
        def f(x):
            return str(x)
    """, mode='exec')).tree_changed

# Generated at 2022-06-14 02:22:13.842898
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = ast.parse('print(str(1 + 1))')
    tree_changed, errors = StringTypesTransformer.transform(t)
    assert isinstance(t, ast.Module)
    assert isinstance(t.body[0], ast.Expr)
    assert isinstance(t.body[0].value, ast.Call)
    assert (t.body[0].value.func.id == 'print')
    assert isinstance(t.body[0].value.args[0], ast.Call)
    assert isinstance(t.body[0].value.args[0].func, ast.Name)
    assert (t.body[0].value.args[0].func.id == 'unicode')
    assert isinstance(t.body[0].value.args[0].args[0], ast.BinOp)
   

# Generated at 2022-06-14 02:22:17.470475
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.snippet import transform
    from ..utils.tree import dump
    from ..types import TransformationResult

    snippet = """
    s = str()
    """
    result = transform(snippet, [StringTypesTransformer])
    assert result.tree_changed
    assert dump(result.tree)

# Generated at 2022-06-14 02:22:28.098825
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import sys
    import os
    import astunparse
    sys.path.insert(0, os.path.abspath('..'))
    import metamorphose  # noqa: E402
    from metamorphose.utils.tree import create_ast
    #
    # Code Example
    #
    code = '''
    class ClassName:
        def __init__(self):
            self.var = str()
    '''
    ast_tree = create_ast(code)
    print(astunparse.unparse(ast_tree))
    ast_new_tree = metamorphose.transform(ast_tree, StringTypesTransformer)
    print(astunparse.unparse(ast_new_tree[0]))
    # self.assertIsNotNone(ast_new_tree)

# Generated at 2022-06-14 02:23:02.117515
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import os
    import sys
    import unittest

    from typed_ast import ast3 as ast

    from ..utils.tree import to_src

    # Add grandparent to search path for testing
    grandparent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
    sys.path.insert(0, grandparent_dir)
    try:
        from py2to3.main import main
    finally:
        # Remove grandparent from search path
        sys.path.pop(0)

    class TestStringTypesTransformer(unittest.TestCase):
        def test_basic(self):
            source = '''
            def foo(s):
                return str(s)
            '''
            tree = ast

# Generated at 2022-06-14 02:23:11.521410
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import unittest
    from typed_ast import ast3 as ast

    class TestStringTypesTransformer(unittest.TestCase):
        def test_identity(self):
            tree = ast.parse('[1, 2, 3]')
            self.assertFalse(StringTypesTransformer.transform(tree).changed)

        def test_str(self):
            tree = ast.parse('str(1)')
            self.assertTrue(StringTypesTransformer.transform(tree).changed)

    unittest.main(argv=[''], verbosity=2, exit=False)


# Generated at 2022-06-14 02:23:13.057086
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:18.870600
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
    def func():
        return str
    """)

    t = StringTypesTransformer.transform(tree)

    expected = ast.parse("""
    def func():
        return unicode
    """)
    assert ast.dump(t.tree) == ast.dump(expected)

# Generated at 2022-06-14 02:23:25.951179
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..testing import run_transform_test

    run_transform_test(
        StringTypesTransformer,
        [
            "a = str(t)",
            'def f():\n    x = str(1)'
        ],
        [
            "a = unicode(t)",
            'def f():\n    x = unicode(1)'
        ])

# Generated at 2022-06-14 02:23:29.650813
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert hasattr(StringTypesTransformer, 'target')
    assert 'transform' in dir(StringTypesTransformer)
    assert callable(StringTypesTransformer.transform)

# Generated at 2022-06-14 02:23:36.536902
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import imp
    module_name = 'test'
    module = imp.new_module(module_name)
    module.__file__ = '%s.py' % module_name
    code = """
foo = str('hello')
bar = str(42)
"""
    expected_code = """
foo = unicode('hello')
bar = unicode(42)
"""
    tree = ast.parse(code)
    r = StringTypesTransformer.transform(tree)
    assert r.tree_changed
    assert len(r.warnings) == 0
    assert ast.dump(r.tree) == ast.dump(ast.parse(expected_code))

# Generated at 2022-06-14 02:23:37.897272
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor

# Generated at 2022-06-14 02:23:47.702343
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # source code for the class
    code = """
        # comment at the top
        class str:
            \"\"\"doc string for the class\"\"\"
        def func(str):
            \"\"\"doc string for the method\"\"\"
        \"\"\"doc string for the global variable\"\"\"
        str = 'str'
        # comment at the bottom
    """
    # expected source code for the class
    expected = """
        # comment at the top
        class unicode:
            \"\"\"doc string for the class\"\"\"
        def func(unicode):
            \"\"\"doc string for the method\"\"\"
        \"\"\"doc string for the global variable\"\"\"
        unicode = 'str'
        # comment at the bottom
    """
    # AST for the source code
    node = ast.parse(code)

# Generated at 2022-06-14 02:24:00.354184
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
  tree = ast.parse("""
print(str())
print(str('a'))
type(str())
type(str('a'))
type(str('a').encode())
str.encode(str('a'))
str.encode(str('a'), 'a')
str.encode(str('a'), 'a', 'a')
str.encode(str('a'), 
           'a', 'a')
""")
  tree_ = StringTypesTransformer.transform(tree)

# Generated at 2022-06-14 02:24:54.524521
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..fixer import Fixer
    from copy import deepcopy

    code = """
        '''Testing string types.'''
        a = str()
        b = str(4)
        c = str(str())

        x = str
        y = unicode
    """

    tree = ast.parse(code)
    fixed_tree = Fixer(StringTypesTransformer).fix(tree)
    fixed_code = compile(fixed_tree, '<string>', 'exec')

    assert fixed_code == compile(code, '<string>', 'exec')

# Generated at 2022-06-14 02:25:02.781735
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
a = str
a = b.str
""")
    expected_tree = ast.parse("""
a = unicode
a = b.unicode
""")
    
    tt = StringTypesTransformer()
    newtree = tt.visit(tree)
    assert isinstance(newtree, ast.AST)
    assert ast.dump(newtree) == ast.dump(expected_tree)

    # Ensure that the format of NodeTransformer was not changed
    assert isinstance(newtree, ast.AST)

# Generated at 2022-06-14 02:25:11.077388
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # 'a' is str() in Python2 
    code_before = '''
print('a')
'''
    code_after = '''
print(u'a')
'''

    tree = ast.parse(code_before)
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed
    assert ast.unparse(result.tree) == code_after

# Generated at 2022-06-14 02:25:18.278682
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    program = '''
    def is_a_string(x):
        return isinstance(x, str)
    '''
    result = StringTypesTransformer.transform(ast.parse(program))
    expected = '''
    def is_a_string(x):
        return isinstance(x, unicode)
    '''
    assert(astunparse.unparse(result.tree) == expected)
    assert(result.changed)

# Generated at 2022-06-14 02:25:21.784444
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    assert StringTypesTransformer.__name__ == 'StringTypesTransformer'

    transformer = StringTypesTransformer()
    assert transformer.target == (2, 7)
    assert callable(transformer.transform)


# Generated at 2022-06-14 02:25:31.162821
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    # Test code
    code = "import typing\n"
    code += "name: str = '123'\n"
    code += "name = str(123)\n"
    code += "name = '123'\n"
    code += "name = b\"123\"\n"
    
    # Expected code
    expected_code = "import typing\n"
    expected_code += "name: unicode = '123'\n"
    expected_code += "name = unicode(123)\n"
    expected_code += "name = '123'\n"
    expected_code += "name = b\"123\"\n"

    # Run transformations and compare ast
    result_ast, tree_changed = StringTypesTransformer.run_test(code)
    assert tree_changed == True
    assert astor.to_

# Generated at 2022-06-14 02:25:36.478738
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.testing import test_on_single_node
    from typed_ast import ast3 as ast
    code = "str"
    expected = "unicode"
    tree = test_on_single_node(code, StringTypesTransformer)
    assert ast.dump(tree).split(".")[0] == expected
    print(ast.dump(tree))

# Generated at 2022-06-14 02:25:41.692985
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("x='asdf'; print(str(x))")
    new_tree = StringTypesTransformer.transform(tree).tree
    assert new_tree.body[0].value.s == 'asdf'
    assert isinstance(new_tree.body[1].value.func, ast.Name)
    assert new_tree.body[1].value.func.id == 'unicode'
    assert isinstance(new_tree.body[1].value.args[0], ast.Name)
    assert new_tree.body[1].value.args[0].id == 'x'

# Generated at 2022-06-14 02:25:47.507346
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
from __future__ import unicode_literals
s = str()
"""
    expected_output = """
from __future__ import unicode_literals
s = unicode()
"""
    t = StringTypesTransformer()
    t.transform_source(code)
    assert expected_output == t.output()



# Generated at 2022-06-14 02:25:54.275208
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests that the StringTypesTransformer class was
    properly instantiated and contains the appropriate
    methods and attributes.

    """
    assert StringTypesTransformer.target == (2, 7)

    assert StringTypesTransformer.transform(None) == None

if __name__ == "__main__":
    test_StringTypesTransformer()