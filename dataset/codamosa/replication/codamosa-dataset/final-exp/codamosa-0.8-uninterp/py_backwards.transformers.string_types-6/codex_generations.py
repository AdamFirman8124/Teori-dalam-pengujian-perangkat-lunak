

# Generated at 2022-06-14 02:16:58.777115
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert(StringTypesTransformer.transform(parse('print str(1)'))[0].body[0].value.keys[0].id == 'unicode')
    assert(StringTypesTransformer.transform(parse('print str(1)'))[1] == True)
    assert(StringTypesTransformer.transform(parse('print str(1)'))[2] == [])

# Generated at 2022-06-14 02:17:06.860205
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import Source
    from ..utils.tree import print_tree
    source = Source("""
    def foo(bar: str):
        return bar
    """)
    
    tree = source.tree
    newtree = StringTypesTransformer.transform(tree)
    print(print_tree(newtree))
    assert print_tree(newtree) == print_tree(ast.parse("""
    def foo(bar: unicode):
        return bar
    """))

# Generated at 2022-06-14 02:17:10.905596
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test for constructor of class StringTypesTransformer.

    """
    stringTypesTransformer = StringTypesTransformer()
    assert stringTypesTransformer.target == (2, 7)



# Generated at 2022-06-14 02:17:20.965697
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..pygram import python_grammar

    def check_node(node: ast.AST) -> bool:
        return isinstance(node, ast.Name) and node.id == 'str'

    def check_child_node(child_node: ast.AST, node: ast.AST) -> bool:
        return isinstance(child_node, ast.Name) and child_node.id == 'str'

    tree = ast.parse("def f(a: str) -> str: return str(a)", mode='exec')
    transformer = StringTypesTransformer(check_node=check_node, check_child_node=check_child_node)
    new_tree, tree_changed, _ = transformer.transform(tree)
    assert tree_changed

    old_source = ast.unparse(tree)
    new_source = ast.unparse

# Generated at 2022-06-14 02:17:33.062351
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    try:
        with open('./test-data/test_StringTypesTransformer.py') as f:
            tree = ast.parse(f.read())
    except IOError as e:
        print(str(e))
        sys.exit(1)

    # Apply transformation
    res = StringTypesTransformer.transform(tree)
    # Write transformed code to file
    with open('./test-data/test_StringTypesTransformer_transformed.py', 'w') as f:
        f.write(astunparse.unparse(res.tree))

    # Test for correct transformation
    try:
        with open('./test-data/expected/test_StringTypesTransformer_expected.py') as f:
            expected_res = f.read()
    except IOError as e:
        print(str(e))


# Generated at 2022-06-14 02:17:39.200626
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
    def foo():
        a = str(1)
    '''
    expected_code = '''
    def foo():
        a = unicode(1)
    '''
    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed
    ast.fix_missing_locations(result.tree)
    assert ast.dump(result.tree) == ast.dump(ast.parse(expected_code))
    assert len(result.dependent_transformations) == 0

# Generated at 2022-06-14 02:17:51.477528
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import Source
    from .. import transform

    src = Source("""
a = '\u1234'
b = str('\u1234')
c = unicode('\u1234')
d = str('aaaa')
e = unicode('aaaa')
""")

    expected = Source("""
a = u'\u1234'
b = unicode('\u1234')
c = unicode('\u1234')
d = unicode('aaaa')
e = unicode('aaaa')
""")

    tree = src.tree
    tree = transform(tree, 2.7)

    assert src.path == expected.path
    assert tree == expected.tree

# Generated at 2022-06-14 02:17:53.937811
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    s = StringTypesTransformer()
    assert s.name == "StringTypesTransformer"

# Generated at 2022-06-14 02:18:02.970515
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:04.818009
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    src = "str('Hello')"
    trf = StringTypesTransformer()
    assert eval(trf(src)) == eval(src)

# Generated at 2022-06-14 02:18:12.652589
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class Foo:
        def bar(self):
            str('a')

    foo = Foo()
    src = inspect.getsource(foo.bar)
    tree = ast.parse(src)
    res = StringTypesTransformer.transform(tree)
    result = compile(res.tree, '<test>', 'exec')
    ns = {}
    exec(result, ns)
    assert ns['s'] == u"a"

# Generated at 2022-06-14 02:18:23.192825
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    from ..utils.ast_factory import ast_factory
    from .string_types import StringTypesTransformer


    tree = ast_factory(
        """
        class A:
    
            def f(self, x: str, y: list[str]):
                z: str = y[x]
                return x
        """
    )
    expected_tree = ast_factory(
        """
        class A:
    
            def f(self, x: unicode, y: list[unicode]):
                z: unicode = y[x]
                return x
        """
    )

    actual_tree_changed, actual_trees = StringTypesTransformer.transform(tree)
    assert actual_tree_changed
    assert actual_trees == []

# Generated at 2022-06-14 02:18:27.137750
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_1 = ast.parse("x = str(0)")
    result_1, modified_1, errors_1 = StringTypesTransformer.transform(input_1)
    assert not hasattr(result_1, "str")
    assert modified_1 == True
    assert errors_1 == []

# Generated at 2022-06-14 02:18:32.516571
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor

    code1 = '''def foo(bar: str): pass'''
    tree1 = astor.parse_file(code1)
    # print(astor.dump_tree(tree1))
    t1 = StringTypesTransformer.transform(tree1)
    assert astor.dump_tree(t1.tree) == 'def foo(bar: unicode): pass'

# Generated at 2022-06-14 02:18:33.569753
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:41.971208
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .fixtures import string_types_source
    from .fixtures import string_types_target
    from .fixtures import all_fixtures

    # Test on the fixture string_types_source
    transformer = StringTypesTransformer()
    source_tree = all_fixtures[string_types_source]
    expected_tree = all_fixtures[string_types_target]
    result = transformer.transform(source_tree)
    assert result.tree == expected_tree
    assert result.tree_changed == True
    assert result.transformer_output == []

# Generated at 2022-06-14 02:18:49.416245
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from typed_ast import ast2

    tree = astor.parse_file("CodeExamples\\str.py", filename="str.py")
    new_tree = StringTypesTransformer.transform(tree)

    # remove the docstring from the ast since it change every execution
    for node in ast.walk(new_tree.tree):
        if type(node) is ast.FunctionDef:
            node.body.pop(0)


# Generated at 2022-06-14 02:18:54.609758
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_code = '''
        def str_test(a, b):
            obj = str()
            return str(a) + str(b)
    '''
    expected_code = '''
        def str_test(a, b):
            obj = unicode()
            return unicode(a) + unicode(b)
    '''

    tree = ast.parse(input_code)
    transformer = StringTypesTransformer()
    actual_code = transformer.transform(tree)

    assert ast.dump(tree) == ast.dump(ast.parse(expected_code))

# Generated at 2022-06-14 02:18:57.852530
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = ast.parse('"test"')
    t_new = StringTypesTransformer.transform(t)
    assert t != t_new
    assert ast.dump(t) != ast.dump(t_new)

# Generated at 2022-06-14 02:19:01.965634
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
            x = str()
            """
    tree = ast.parse(code)
    t = StringTypesTransformer()
    t.transform(tree)
    exec(compile(tree, '<string>', 'exec'))

# Generated at 2022-06-14 02:19:11.527706
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_astunparse
    from ..preprocessing import preprocess
    test_tree = preprocess('a = str()')
    expected_tree = preprocess('a = unicode()')
    s = StringTypesTransformer()
    result = s.transform(test_tree)
    assert typed_astunparse.unparse(result.tree) == typed_astunparse.unparse(expected_tree)

# Generated at 2022-06-14 02:19:13.217901
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer()

# Generated at 2022-06-14 02:19:16.581203
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    constr = StringTypesTransformer()
    assert constr.target == (2, 7)
    assert constr.__class__.__name__ == 'StringTypesTransformer'


# Generated at 2022-06-14 02:19:25.926010
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('')).tree_changed == False

    tree = ast.parse('''
        x = str(y)
    ''')
    assert StringTypesTransformer.transform(tree).tree_changed == True

    tree = ast.parse('''
        x = unicode(y)
    ''')
    assert StringTypesTransformer.transform(tree).tree_changed == False

    tree = ast.parse('''
        x = str
    ''')
    assert StringTypesTransformer.transform(tree).tree_changed == True

    tree = ast.parse('''
        x = unicode
    ''')
    assert StringTypesTransformer.transform(tree).tree_changed == False

# Generated at 2022-06-14 02:19:30.325774
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('str(123)'), {}).code == "unicode(123)"
    assert StringTypesTransformer.transform(ast.parse('type(123)'), {}).code == "type(123)"
    assert StringTypesTransformer.transform(ast.parse('type(123)'), {}).tree_changed == False

# Generated at 2022-06-14 02:19:33.938778
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests the StringTypesTransformer transformer. 

    """
    transformer = StringTypesTransformer

    tree = ast.parse(
r"""
print(str("foo"))
"""
)

    expected_tree = ast.parse(
r"""
print(unicode("foo"))
"""
)

    # Print the source code of the expect

# Generated at 2022-06-14 02:19:34.622927
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert True

# Generated at 2022-06-14 02:19:39.732128
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .mocks import get_basic_python_parser
    from astunparse import unparse
    code = '''a = str(b)'''
    parsed = get_basic_python_parser(code)
    transformed, _ = StringTypesTransformer.transform(parsed)
    assert unparse(transformed) == 'a = unicode(b)'

# Generated at 2022-06-14 02:19:48.006497
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test if str is replaced with unicode.
    
    """
    from .base import BaseTransformerTest
    # Create instance
    t = StringTypesTransformer()
    tt = BaseTransformerTest()
    
    # Test
    code = "str"
    tree = ast.parse(code)
    result = t.transform(tree)
    tt.assertEqual(ast.dump(result.tree), "Module(body=[Expr(value=Name(id='unicode', ctx=Load()))])")
    
    # Test
    code = "[1, 2, 3]"
    tree = ast.parse(code)
    result = t.transform(tree)

# Generated at 2022-06-14 02:19:59.451734
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.testing import (
        assert_tree_transformation,
        tree_from_code
    )

    code_template = '''
    def foo(bar):
    {indent_level_one}return str
    {indent_level_zero}
    '''

    expected_tree = tree_from_code(code_template.format(indent_level_one=' '*4,
                                                        indent_level_zero=' '*0))

    tree = tree_from_code(code_template.format(indent_level_one=' '*4,
                                               indent_level_zero=' '*0))
    assert_tree_transformation(tree, expected_tree, StringTypesTransformer)

# Generated at 2022-06-14 02:20:09.844080
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    # Transforming code:
    # 
    # `print(str('hello, world!'))`
    # 
    # into Python 2.7 code:
    # 
    # `print(unicode('hello, world!'))`
    node = ast.parse('print(str("hello, world!"))')
    node = StringTypesTransformer.transform(node).tree
    target = ast.parse('print(unicode("hello, world!"))')
    assert astor.to_source(node) == astor.to_source(target)

# Generated at 2022-06-14 02:20:12.233117
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast as py_ast
    from ..utils.source import source_to_ast

    source = """
    a = str
    """

    tree = source_to_ast(source)
    updated_tree, tree_changed, _ = StringTypesTransformer().transform(tree)

    # Assert that unicode has been used instead of str
    assert isinstance(find(updated_tree, py_ast.Name)[0].ctx, py_ast.Store)
    assert find(updated_tree, py_ast.Name)[0].id == 'unicode'

# Generated at 2022-06-14 02:20:17.246833
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
    x = str('string')
    """)

    expected = ast.parse("""
    x = unicode('string')
    """)

    tr = StringTypesTransformer.transform(tree)

    assert compare_ast(tr.tree, expected)

# Generated at 2022-06-14 02:20:21.649503
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('a = str("a")')
    tree_changed, new_code, result = StringTypesTransformer.transform(tree)
    assert tree_changed == True
    assert new_code == 'a = unicode("a")'
    assert result == []

# Generated at 2022-06-14 02:20:34.870067
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:20:40.690574
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    x = ast.parse("y = str(x)", 'x.py')
    tree_changed, new_code = StringTypesTransformer.transform(x)

    assert tree_changed
    assert ast.dump(new_code) == ast.dump(ast.parse("y = unicode(x)", 'x.py'))


# Generated at 2022-06-14 02:20:47.256316
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    expected = ast.Call(func = ast.Name(id = "print", ctx = ast.Load()), args = [ast.UnaryOp(op = ast.Not(), operand = ast.UnaryOp(op = ast.USub(), operand = ast.Num(n = 1)))], keywords = [])

    result = StringTypesTransformer.transform(expected)

    assert result.tree is expected
    assert result.tree_changed == False
    assert len(result.details) == 0


# Generated at 2022-06-14 02:20:51.172162
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    
    # Create an instance of StringTypesTransformer
    transformer: StringTypesTransformer = StringTypesTransformer()

    # Define the expected AST

# Generated at 2022-06-14 02:20:58.859596
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    class TestStringTypesTransformer(unittest.TestCase):

        # Unit test for constructor of class StringTypesTransformer
        def test_constructor(self):
            transformer = StringTypesTransformer()
            self.assertEqual(transformer.target, (2, 7))

        # Unit test for method of class StringTypesTransformer
        def test_transformer(self):
            transformer = StringTypesTransformer()
            source = "def test():\n    x = 'test'\n    y = len(x)\n"
            tree = ast.parse(source, "", "exec")
            new_tree, tree_changed = transformer.transform(tree)
            self.assertTrue(tree_changed)
            new_source = compile(new_tree, '<string>', 'exec')

# Generated at 2022-06-14 02:21:08.431238
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test setup
    # Imports
    from textwrap import dedent
    from ..utils.tree import to_source
    from ..modification import ModificationTracker
    from ..context import Context
    # Test code
    test_code = dedent('''\
        x = str
        ''')
    # Expected generated code
    expected_code = dedent('''\
        x = unicode
        ''')
    # Run test
    mod_tracker = ModificationTracker(True)
    tree = ast.parse(test_code)
    mod_tracker.start_tracking()
    new_tree, changed = StringTypesTransformer.transform(tree)
    mod_tracker.stop_tracking()
    assert to_source(new_tree) == expected_code
    assert changed is True
    assert mod_tracker

# Generated at 2022-06-14 02:21:19.402899
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    program = '''class Foo:
    def __init__(self, s: str):
        pass'''
    expected = '''class Foo:
    def __init__(self, s: unicode):
        pass'''
    tree = ast.parse(program)
    tree = StringTypesTransformer.transform(tree).new_tree
    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 02:21:25.274464
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    assert transformer.target == (2, 7)
    
    node = ast.Name(id='str', ctx=ast.Load())
    tree = ast.Module(body=[node])
    tree_changed, node_changed, nodes_added, nodes_removed = transformer.transform(tree)
    assert tree_changed
    assert node_changed
    assert nodes_added == []
    assert nodes_removed == []
    assert transforme

# Generated at 2022-06-14 02:21:28.873163
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils import initialize_module_2_7

    tree = initialize_module_2_7()

    assert not StringTypesTransformer.transform(tree).changed

# Generated at 2022-06-14 02:21:29.987745
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:21:34.461557
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    my_ast = ast.parse("""
a = str(a)
b = str()
    """)
    my_ast = StringTypesTransformer.transform(my_ast)
    assert my_ast.code == """
a = unicode(a)
b = unicode()
    """

# Generated at 2022-06-14 02:21:44.053398
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class MyClass:
        attr1: str

        def __init__(self, attr1: str, attr2: str):
            self.attr1 = attr1

    transformer = StringTypesTransformer()
    code = """class MyClass:\n    attr1: str\n    def __init__(self, attr1: str, attr2: str):\n        self.attr1 = attr1"""
    tree = ast.parse(code)
    new_tree = transformer.transform(tree)
    new_code = ast.dump(new_tree, include_attributes=True)

# Generated at 2022-06-14 02:21:55.783164
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:22:02.270156
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.tree import ast_to_text
    tree = ast.parse('x = str(2)')
    trans = StringTypesTransformer.transform(tree)    
    assert ast_to_text(trans.tree) == "x = unicode(2)"

    tree = ast.parse('x = unicode(2)')
    trans = StringTypesTransformer.transform(tree)    
    assert ast_to_text(trans.tree) == "x = unicode(2)"

# Generated at 2022-06-14 02:22:06.832571
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("x = str()")
    transformed = StringTypesTransformer.transform(tree)
    assert transformed.tree_changed
    assert type(transformed.tree) == ast.Module
    assert "x = unicode()" == astor.to_source(transformed.tree)
    assert transformed.additional_imports == []

# Generated at 2022-06-14 02:22:11.422655
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    def test():
        import doctest
        s = str()
        print(s)

    """
    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)
    print(result.tree)
    print(result.warnings)

# Generated at 2022-06-14 02:22:33.976296
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .base import BaseTransformerTest
    from ..transforms import py3_ast
    from ..transforms.remove_print_function import RemovePrintFunctionTransformer

    class Test(BaseTransformerTest):
        target_version = (2, 7)
        transform_module = py3_ast
        transformers = [StringTypesTransformer, RemovePrintFunctionTransformer]
        base_tree = ast.parse("""
            a = str(b)
        """)
        expected_tree = ast.parse("""
            a = unicode(b)
        """)

    Test().test()

# Generated at 2022-06-14 02:22:41.732324
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer('StringTypesTransformer')
    transpiled_code = transformer.transform(
        """
        class A:
            def func(self, a: str):
                b = str(a)
                return b
        """
    )
    print(transpiled_code)
    assert transpiled_code == {
        'transformed_ast': ast.parse(
            """\nclass A:\n    def func(self, a: unicode):\n        b = unicode(a)\n        return b\n"""
        ),
        'trees_changed': True,
        'errors': []
    }

# Generated at 2022-06-14 02:22:44.721726
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_unicode_ast
    tree = source_to_unicode_ast("""
    a = str()
    """)
    assert StringTypesTransformer.transform(tree).changed

# Generated at 2022-06-14 02:22:52.321187
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .base import BaseTestTransformer
    from ..parser import parse

    class TestStringTypesTransformer(BaseTestTransformer):
        transformer = StringTypesTransformer


# Generated at 2022-06-14 02:22:56.992035
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer()
    tree = ast.parse('x = str(x) + str(y)')
    t.transform(tree)
    assert astor.to_source(tree) == "x = unicode(x) + unicode(y)"

# Generated at 2022-06-14 02:22:58.072892
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:13.023093
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # original source:
    # ==============================
    source = '''
    x = str(x)
    '''
    # Expected AST:
    # ==============================
    expected_ast = ast.Module(
        body=[
            ast.Assign(
                targets=[
                    ast.Name(
                        id='x', ctx=ast.Store()
                    )
                ],
                value=ast.Call(
                    func=ast.Name(
                        id='unicode', ctx=ast.Load()
                    ),
                    args=[
                        ast.Name(
                            id='x', ctx=ast.Load()
                        )
                    ],
                    keywords=[],
                    starargs=None,
                    kwargs=None
                )
            )
        ]
    )
    # Perform transformation:
    # ==============================


# Generated at 2022-06-14 02:23:16.075856
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("x = str()"))[0] == ast.parse("x = unicode()")

# Generated at 2022-06-14 02:23:17.432222
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:18.238754
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:48.392980
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class Foo:
        def __init__(self, x: str) -> None:
            self.x = x

    class Bar:
        def __init__(self, x: unicode) -> None:
            self.x = x

    # Before: Foo.__init__

# Generated at 2022-06-14 02:23:52.251179
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    selectors = 'abc'
    class_name = 'StringTypesTransformer'
    code = '''
    result = str(selectors)
    '''
    expected_code = '''
    result = unicode(selectors)
    '''
    run_test(class_name, code, expected_code, locals())

# Generated at 2022-06-14 02:24:03.294953
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ...tests.transformation_utils import transform_and_reconstruct
    from ...tests.transformation_utils import parse_to_ast

    code = \
"""
a = b'asdf'
"""

    tree = parse_to_ast(code)
    transformed = StringTypesTransformer.transform(tree)
    code_after = transform_and_reconstruct(transformed)
    assert code_after == \
"""
a = unicode(b'asdf')
"""

    code = \
"""
a = str('asdf')
"""

    tree = parse_to_ast(code)
    transformed = StringTypesTransformer.transform(tree)
    code_after = transform_and_reconstruct(transformed)
    assert code_after == \
"""
a = unicode('asdf')
"""

# Generated at 2022-06-14 02:24:08.636785
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """
    a = str()
    """

    tree = ast.parse(source)
    new_tree = StringTypesTransformer.run_it(tree)

    assert astor.to_source(new_tree) == """
    a = unicode()
    """

# Generated at 2022-06-14 02:24:12.128850
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    tree = ast.parse("""
        def foo(bar):
            if isinstance(bar, str):
                print("Hello")
        """
    )

# Generated at 2022-06-14 02:24:14.685238
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer()
    test_ast = ast.parse('str')
    assert t.transform(test_ast).tree_changed

# Generated at 2022-06-14 02:24:15.482537
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert False, "Not implemented"

# Generated at 2022-06-14 02:24:21.588688
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('''str(3)''')
    new_tree, changed, _ = StringTypesTransformer.transform(tree)
    assert changed
    assert ast.dump(new_tree) == 'Module(body=[Expr(value=Call(func=Name(id=\'unicode\', ctx=Load()), args=[Num(n=3)], keywords=[], starargs=None, kwargs=None))])'

# Generated at 2022-06-14 02:24:26.927407
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    test = """
            x = str()
            """
    expected = """
            x = unicode()
            """
    tree = ast.parse(test)
    new_tree = StringTypesTransformer.run(tree)
    assert ast.dump(new_tree) == expected

# Generated at 2022-06-14 02:24:29.073849
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    cls = StringTypesTransformer()
    # no assert needed - coverage

# Generated at 2022-06-14 02:25:31.501705
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.tree import print_ast
    from typed_ast import ast3 as ast

    class TestTransformer(BaseTransformer):
        @classmethod
        def transform(cls, tree: ast.AST) -> TransformationResult:
            pass

    import_node = ast.Import(
        [ast.alias(name='os', asname=None)],
        lineno=1,
        col_offset=0)
    from_import_node = ast.ImportFrom(
        module='enum',
        names=[ast.alias(name='Enum', asname=None)],
        level=0,
        lineno=2,
        col_offset=0)

# Generated at 2022-06-14 02:25:33.631985
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("str")).tree == ast.parse("unicode")

# Generated at 2022-06-14 02:25:34.244863
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:25:40.266898
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(
        ast.parse('def foo(s: str) -> str: return s')) == (
            ast.parse('def foo(s: unicode) -> unicode: return s'), True, [])
    assert StringTypesTransformer.transform(
        ast.parse('s = str()')) == (
        ast.parse('s = unicode()'), True, [])



# Generated at 2022-06-14 02:25:44.387421
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('def f():\n    return str()')
    assert astor.to_source(StringTypesTransformer.transform(tree).root) == "def f():\n    return unicode()\n"

# Generated at 2022-06-14 02:25:55.101063
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:26:05.262698
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = ast.parse("""
        b = str('s')
    """)
    t = StringTypesTransformer.transform(t)
    assert(t.tree_changed == True)
    assert(t.dependent_changes == [])
    assert(ast.dump(t.tree) == "Module(body=[Assign(targets=[Name(id='b', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Str(s='s')], keywords=[], starargs=None, kwargs=None))])")
    return


# Generated at 2022-06-14 02:26:14.421580
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3
    source = '''
    a = unicode()
    b = str()
    print(a)
    '''
    expected_code = '''
    a = unicode()
    b = unicode()
    print(a)
    '''
    tree = typed_ast.ast3.parse(source)
    tree_changed, new_tree = StringTypesTransformer.transform(tree)
    assert typed_ast.ast3.fix_missing_locations(new_tree)
    assert typed_ast.ast3.dump(new_tree) == expected_code
    assert tree_changed == True

    expected_code = '''
    a = unicode("hello")
    b = unicode("hello")
    print(a)
    '''

# Generated at 2022-06-14 02:26:24.796447
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import python_modernize.fixer_util

    pt = ast.parse('s = str(s)')
    new_pt = python_modernize.fixer_util.run_fixed(
        StringTypesTransformer, pt)
    assert ast.dump(pt) != ast.dump(new_pt)
    _ast_error_print(new_pt)
    assert ast.dump(new_pt) == "Expr(value=Assign(targets=[Name(id='s', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Name(id='s', ctx=Load())], keywords=[], starargs=None, kwargs=None)))"

# Generated at 2022-06-14 02:26:29.778694
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for constructor of class StringTypesTransformer.
    """
    tree = ast.parse("str.lower() + str.upper()")
    transformer = StringTypesTransformer()
    result = transformer.transform(tree)

    assert result.tree != tree
    assert result.tree_changed == True

    # TODO: better way to check the tree
    assert astor.to_source(result.tree) == 'unicode.lower() + unicode.upper()\n'