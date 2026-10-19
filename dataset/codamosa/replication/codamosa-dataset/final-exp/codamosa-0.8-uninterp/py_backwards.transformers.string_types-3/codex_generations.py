

# Generated at 2022-06-14 02:17:07.735576
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from .test_fixtures.classes_transforms import StringTypesTransformer_test

    for test in StringTypesTransformer_test:
        transformed_test = StringTypesTransformer.transform(test.test_tree)
        assert astor.to_source(transformed_test.tree) == test.test_source

# Generated at 2022-06-14 02:17:19.165760
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    from .. import tree_to_str
    
    input_compare = ast.parse('x = "abc"')
    input_result = ast.parse('x = u"abc"')
    assert StringTypesTransformer.transform(input_compare) == TransformationResult(input_result, True, []) 

    input_compare = ast.parse('x = "abc"\ny = "def"')
    input_result = ast.parse('x = u"abc"\ny = u"def"')
    assert StringTypesTransformer.transform(input_compare) == TransformationResult(input_result, True, []) 

    input_compare = ast.parse('''
    def f(*args):
        pass
    ''')

# Generated at 2022-06-14 02:17:26.969845
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import parse
    from ..utils.ast_compare import compare_ast
    my_ast = parse("a = str(b)")
    my_ast_changed = parse("a = unicode(b)")
    my_transformer = StringTypesTransformer()
    my_transformer.transform(my_ast)
    assert compare_ast(my_ast, my_ast_changed)

# Generated at 2022-06-14 02:17:33.310337
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """
    Simple unit test for constructor of class StringTypesTransformer:
        1)create a constructor
        2)get a tree
        3)check that tree was not changed
    """

    x = ast.parse('str(3)')
    transformer = StringTypesTransformer()
    tree_changed, tree, messages = transformer.transform(x)
    assert tree_changed == True
    assert tree == ast.parse('unicode(3)')

# Generated at 2022-06-14 02:17:36.392561
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.tree import to_source
    from ..utils.code import parse_ast


# Generated at 2022-06-14 02:17:42.452244
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    test_tree = astor.parse_file('./test/test_stringtype.py')
    test_classes = find(test_tree, ast.ClassDef)
    test_node = find(test_tree, ast.Name)
    test_node2 = test_node[0]
    test_node2.id = 'str'
    result = StringTypesTransformer.transform(test_tree)
    assert result.tree_changed == True
    assert result.tree != test_tree

# Generated at 2022-06-14 02:17:44.548578
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('str()')).tree.body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:17:45.117280
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:17:50.378626
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('''
a = str(1)
''')
    obj = StringTypesTransformer()
    new_tree, tree_changed, annotations = obj.transform(tree)
    obj.finalize()

    assert tree_changed
    assert annotations == []

    code = compile(new_tree, filename='<ast>', mode='exec')
    ns = {}
    exec(code, ns)

    assert ns['a'] == u'1'

# Generated at 2022-06-14 02:17:58.259803
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("str")
    result = StringTypesTransformer.transform(tree)
    assert(isinstance(result, TransformationResult))
    assert(isinstance(result.tree, ast.AST))
    assert(len(result.messages) == 0)
    result_tree = ast.fix_missing_locations(result.tree)
    assert(ast.dump(tree) == "Module(body=[Expr(value=Name(id='unicode', ctx=Load()))])")

# Generated at 2022-06-14 02:18:04.391571
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .. import apply_transformations

    expected = "def f(x):\n    return unicode(x)"

    tree = ast.parse(expected)
    assert expected == apply_transformations(StringTypesTransformer, tree)

# Generated at 2022-06-14 02:18:12.163795
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('''\
        import json

        class Foo(object):
            def __init__(self):
                self.x = "i am a string"
        ''')

    transformer = StringTypesTransformer()

    transformed = transformer.transform(tree)

    expected = ast.parse('''\
        import json

        class Foo(object):
            def __init__(self):
                self.x = u"i am a string"
        ''')

    ast.fix_missing_locations(transformed.tree)
    ast.fix_missing_locations(expected)

    assert ast.dump(transformed.tree, include_attributes=True) == ast.dump(expected, include_attributes=True)

# Generated at 2022-06-14 02:18:17.823437
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""\
x = str()
""", mode='exec')
    assert [node.id for node in find(tree, ast.Name)] == ['str']
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed
    assert [node.id for node in find(result.tree, ast.Name)] == ['unicode']

# Generated at 2022-06-14 02:18:28.660233
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_astunparse
    code = """
    def f(s):
        return s
    """
    tree = ast.parse(code)
    t = StringTypesTransformer()
    new_tree = t.visit(tree)
    typed_astunparse.dump(new_tree)
    code2 = """
    def f(s):
        return unicode(s)
    """
    tree2 = ast.parse(code2)
    assert typed_astunparse.dump(new_tree) == typed_astunparse.dump(tree2)

# Generated at 2022-06-14 02:18:30.391812
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for constructor of class StringTypesTransformer.
    """

# Generated at 2022-06-14 02:18:37.243020
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Unit test for case when input is in str
    tree = ast.parse('a = str(3)')
    expected = 'a = unicode(3)\n'

    actual = unparse(StringTypesTransformer.transform(tree).tree)

    assert actual == expected

    # Unit test for case when there is no string in the code
    tree = ast.parse('a = 3')
    expected = 'a = 3\n'
    
    actual = unparse(StringTypesTransformer.transform(tree).tree)

    assert actual == expected

# Generated at 2022-06-14 02:18:45.849933
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    res = transformer.transform(ast.parse("""
    class A:
        def __init__(self, x):
            self.x = x

    a = A(str(1))
    """))

    assert res.tree_changed
    assert len(res.linter_msgs) == 0
    assert astor.to_source(res.tree) == """
    class A:
        def __init__(self, x):
            self.x = x

    a = A(unicode(1))
    """



# Generated at 2022-06-14 02:18:52.090272
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor

    tree = ast.parse('a = str(1); b = str.join("a", "b")')

    transformer = StringTypesTransformer()
    new_tree = transformer.transform(tree)
    assert(new_tree.tree_changed == True)
    assert(astor.to_source(new_tree.tree) == 'a = unicode(1); b = unicode.join("a", "b")')


# Generated at 2022-06-14 02:18:52.696638
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:53.318612
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:19:04.945904
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    import sys

    node = ast.Name("str", ast.Load())
    tree = StringTypesTransformer.transform(node)
    assert ''.join(ast.dump(node)) == "Name(id='str', ctx=Load())".format(node)
    if sys.version_info >= (2, 7):
        assert ''.join(ast.dump(tree[0])) == "Name(id='unicode', ctx=Load())"
    else:
        assert ''.join(ast.dump(tree[0])) == "Name(id='str', ctx=Load())"

# Generated at 2022-06-14 02:19:09.500578
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
x = str('x')
""")
    result = StringTypesTransformer.transform(tree)

    assert ast.dump(result.tree) == ast.dump(ast.parse("""
x = unicode('x')
"""))

# Generated at 2022-06-14 02:19:15.373087
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('print(str(1), str(2), str(3))')
    expected_tree = ast.parse('print(unicode(1), unicode(2), unicode(3))')
    t = StringTypesTransformer()
    new_tree = t.transform(tree)
    assert_equal(new_tree, expected_tree)


# Generated at 2022-06-14 02:19:18.803978
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """
    some_string = str('foo')
    """
    expected = """
    some_string = unicode('foo')
    """

    tree = ast.parse(source)
    result = StringTypesTransformer.transform(tree)
    assert expected == result.new_tree.dump()

# Generated at 2022-06-14 02:19:31.427688
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Check correctness of class Name
    c = ast.Name(id = "str")
    assert c.id == "str"

    # Check correctness of class Assign
    c = ast.Assign(targets = [ast.Name(id = "str")], value = ast.Name(id = "str"))
    assert c.targets[0].id == "str" and c.value.id == "str"

    # Check correctness of class Attribute
    c = ast.Attribute(value = ast.Name(id = "str"), attr = "str")
    assert c.value.id == "str" and c.attr == "str"

    # Check correctness of class Call
    c = ast.Call(func = ast.Name(id = "str"), args = [ast.Name(id = "str")])

# Generated at 2022-06-14 02:19:40.369771
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_utils import make_python_code
    from ..utils.tree import pretty_print

    tree = make_python_code(3)
    StringTypesTransformer.transform(tree)
    assert pretty_print(tree) == """\
if False:
    class SomeClass(object):

        def __init__(self, some_first_arg, some_second_arg, **some_kwargs):
            self._some_first_arg = some_first_arg
            self._some_second_arg = some_second_arg
            self._some_kwargs = some_kwargs
            self._some_field = unicode()

        def some_method(self):
            pass
        """

# Generated at 2022-06-14 02:19:44.241541
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Tests whether a transformation into unicode class works.
    
    """
    import astor

    source = "str + str"

    tree = ast.parse(source)

    transformer = StringTypesTransformer()
    new_tree = transformer.transform(tree)

    assert astor.to_source(new_tree) == "unicode + unicode"

# Generated at 2022-06-14 02:19:46.160177
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(None) == None

# Generated at 2022-06-14 02:19:56.746277
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # class TestClass(unicode): pass
    cls = ast.ClassDef(name='TestClass', bases=[ast.Name(id='unicode', ctx=ast.Load())], body=[], decorator_list=[])

    # s = str('123')
    s = ast.Assign(targets=[ast.Name(id='s', ctx=ast.Store())], value=ast.Call(
        func=ast.Name(id='str', ctx=ast.Load()),
        args=[ast.Str(s='123')],
        keywords=[],
    ))

    # tree = [cls, s]
    tree = ast.Module(body=[cls, s])

    transformer = StringTypesTransformer()
    result = transformer.transform(tree)
    assert result.tree == tree
    assert result.tree_changed

# Generated at 2022-06-14 02:19:59.669160
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    assert transformer.__repr__() == "<StringTypesTransformer>"


# Generated at 2022-06-14 02:20:08.950314
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = "def foo(x: str) -> int: return 1"
    tree = ast.parse(code)
    assert StringTypesTransformer.transform(tree).tree_changed

# Generated at 2022-06-14 02:20:15.801465
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..types import PythonVersion
    from ..utils.source import source_to_ast

    tree = source_to_ast("""def foo(arg: str):
    return str(arg)""")

    assert StringTypesTransformer.transform(tree).tree_changed

    tree = source_to_ast("""def foo(arg: str):
    return unicode(arg)""")

    assert not StringTypesTransformer.transform(tree).tree_changed

# Generated at 2022-06-14 02:20:24.558334
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from ..transpile import Transpiler

    for test in [
        "str('string')",
        "'string'",
        "str(1)",
        "str(1.0)",
        "str([1, 2, 3])",
        "str([str(i) for i in [1, 2, 3]])",
    ]:
        tree = ast.parse(test, '<test>', 'eval')
        new_tree = Transpiler.transpile(tree)
        code = compile(new_tree, '<test>', 'eval')
        exec(code)

# Generated at 2022-06-14 02:20:29.643391
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    from typed_astunparse import unparse

    tree = ast.parse("""
x = str("abc")
y = unicode("abc")
""")

    tree = StringTypesTransformer.transform(tree)
    tree = ast.fix_missing_locations(tree)

    assert unparse(tree) == """
x = unicode("abc")
y = unicode("abc")
"""

# Generated at 2022-06-14 02:20:35.271727
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    call = foo()
    """
    tree = ast.parse(code)
    original_tree = deepcopy(tree)

    ret = StringTypesTransformer.transform(tree)
    assert ret.tree_changed == True
    assert types.compile_source(astor.to_source(tree)) == types.compile_source(astor.to_source(original_tree))
    assert astor.to_source(tree) == astor.to_source(original_tree)

# Generated at 2022-06-14 02:20:41.332235
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
x = str('abc')
y = str
""")
    r = StringTypesTransformer.transform(tree)
    assert r.tree_changed

    tree2 = ast.parse("""
x = str('abc')
y = str
""")
    r2 = StringTypesTransformer.transform(tree2)
    assert r2.tree_changed

# Generated at 2022-06-14 02:20:50.175118
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('print(str(1))')
    StringTypesTransformer.transform(tree)
    assert ast.dump(tree) == "Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Call(func=Name(id='unicode', ctx=Load()), args=[Num(n=1)], keywords=[])], keywords=[]))])\n"

# Unit test that tests the constructor
# If a test fails, this will raise an exception and the build will fail
# Uncomment the code below to test the constructor
#if __name__ == '__main__':
    #test_StringTypesTransformer()

# Generated at 2022-06-14 02:20:58.203659
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    node = ast.Name(id=str('str'), ctx=None)
    assert isinstance(node, ast.Name)
    assert node.id == str('str')
    tree = ast.parse('value = str("abc")')
    tr = StringTypesTransformer()
    assert tr.target == (2, 7)
    res = tr.transform(tree)
    assert res.tree_changed
    assert isinstance(res.tree.body[0].targets[0], ast.Name)
    assert res.tree.body[0].targets[0].id == str('value')
    assert isinstance(res.tree.body[0].value.func, ast.Name)
    assert res.tree.body[0].value.func.id == str('unicode')

# Generated at 2022-06-14 02:20:59.741702
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:21:05.039793
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """
s = str()
    """
    expected = """
s = unicode()
    """
    transformed = StringTypesTransformer().transform(ast.parse(source))
    assert astor.to_source(transformed.tree).strip() == expected.strip()

# Generated at 2022-06-14 02:21:21.885713
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(
        ast.parse('str("a")')) == TransformationResult(ast.parse('unicode("a")'), True, [])
    assert StringTypesTransformer.transform(
        ast.parse('int("b")')) == TransformationResult(ast.parse('int("b")'), False, [])
test_StringTypesTransformer()

# Generated at 2022-06-14 02:21:25.492355
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("def foo(a: str):\n    return 0")).tree_changed

# Generated at 2022-06-14 02:21:30.677360
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    try:
        import astor
    except ImportError:
        return

    result = StringTypesTransformer.transform(ast.parse("""my_var = str("Hello, world")"""))
    assert result.tree_changed == True
    assert astor.to_source(result.tree).strip() == "my_var = unicode(\"Hello, world\")"

# Generated at 2022-06-14 02:21:36.918137
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        f = foo()
        f.append(str(1))
    """
    
    expected = """
        f = foo()
        f.append(unicode(1))
    """

    tree = ast.parse(code)
    transformer = StringTypesTransformer()
    tree, changed = transformer.transform(tree)

    assert expected == ast.unparse(tree)
    assert changed


# Generated at 2022-06-14 02:21:41.443422
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('s = str.encode("utf-8")')
    new_tree = StringTypesTransformer.transform(tree)
    assert new_tree.was_changed == True
    assert ast.dump(new_tree.tree) == ast.dump(ast.parse('s = unicode.encode("utf-8")'))

# Generated at 2022-06-14 02:21:48.679410
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('mapper.attack_type == str')
    tree = StringTypesTransformer.transform(tree).tree

    assert ast.dump(tree) == "Module(body=[Compare(left=Attribute(value=Name(id='mapper', ctx=Load()), attr='attack_type', ctx=Load()), ops=[Eq()], comparators=[Name(id='unicode', ctx=Load())])])"

# Generated at 2022-06-14 02:21:49.626733
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor


# Generated at 2022-06-14 02:22:00.119300
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_setup import setup_test_module, assertEqualAST, parse_ast
    from .test_setup import setup_test_function

    code_before = (
        '''
a = str(5)
print(str(3))
        '''
    )
    code_after = (
        '''
a = unicode(5)
print(unicode(3))
        '''
    )

    # Parse code
    tree_before = parse_ast(setup_test_function(setup_test_module(code_before),
                                                'test_function'))
    tree_after = parse_ast(setup_test_function(setup_test_module(code_after),
                                               'test_function'))

    # Run transformation
    result = StringTypesTransformer.transform(tree_before)



# Generated at 2022-06-14 02:22:06.355258
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    s = "str = 'abc'"
    tree = ast.parse(s)
    print(tree)
    for node in ast.walk(tree):
        print(node)
    r = StringTypesTransformer.transform(tree)
    assert r.tree_changed
    assert not r.errors
    assert r.transformations
    print(r.tree)
    print(r.transformations)
    print(r.errors)
    print(astunparse.unparse(r.tree))

# Generated at 2022-06-14 02:22:08.585673
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """print(str)"""
    new_code = StringTypesTransformer().transform(code)
    print(new_code)

# Generated at 2022-06-14 02:22:43.349762
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Create a simple tree:
    # ast.Module(
    #     body=[
    #         ast.Assign(
    #             targets=[ast.Name(id='b', ctx=ast.Store())],
    #             value=ast.Call(
    #                 func=ast.Name(id='str', ctx=ast.Load()),
    #                 args=[ast.Str(s='...')],
    #                 keywords=[]
    #             )
    #         ),
    #         ast.Print(
    #             dest=None,
    #             values=[ast.Name(id='b', ctx=ast.Load())],
    #             nl=True
    #         )
    #     ]
    # )
    src = "b = str('...')\nprint b"

# Generated at 2022-06-14 02:22:50.182961
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    def test_function(string):
        return str(string)

    code = 'def test_function(string):\n    return str(string)'
    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree=tree)
    print(result)
    assert result.tree_changed

# Generated at 2022-06-14 02:22:57.881521
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('x = str(1.1)')
    ret_tree = StringTypesTransformer.transform(tree).tree

    assert ast.dump(tree) != ast.dump(ret_tree)
    assert ast.dump(ret_tree) == "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Num(n=1.1)], keywords=[]))])"

# Generated at 2022-06-14 02:22:59.728791
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:02.814109
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('str')).tree_changed
    assert not StringTypesTransformer.transform(ast.parse('unicode')).tree_changed

# Generated at 2022-06-14 02:23:13.134482
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    example = """
string = 'hello world'
string2 = unicode(123)
assert(isinstance(string, str))
    """
    tree = astor.parse_file(StringIO(example))
    t = StringTypesTransformer()
    res = t.transform(tree)
    assert res.tree_changed
    assert(isinstance(res.tree, ast.Module))
    assert (len(res.report) == 0)
    # Check that the source code generated matches the expected source code
    expected_result = """
string = 'hello world'
string2 = unicode(123)
assert(isinstance(string, unicode))
    """
    generated_src = astor.to_source(res.tree)
    assert generated_src == expected_result

# Generated at 2022-06-14 02:23:25.742087
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = 'a = str(b)'

    tree = ast.parse(code)
    transformer = StringTypesTransformer()

    new_tree, changed = transformer.transform(tree)

    assert not changed

    tree = ast.parse(code)
    transformer = StringTypesTransformer()

    new_tree, changed = transformer.transform(tree)

    assert changed

    # Test that the AST is correct
    assert str(new_tree) == '\n'.join(['Module(body=[Assign(targets=[Name(id="a", ctx=Store())], value=Call(func=Name(id="unicode", ctx=Load()), args=[Name(id="b", ctx=Load())], keywords=[]))])'])

# Generated at 2022-06-14 02:23:31.444021
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    code = '''
x = str
    '''
    tree = ast.parse(code)
    tree = StringTypesTransformer.transform(tree).tree
    res = astor.to_source(tree)
    expected_res = '''
x = unicode
    '''
    assert res.strip() == expected_res.strip()

# Generated at 2022-06-14 02:23:40.298837
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
        var1 = 'test'
        var2 = str()
        var3 = 'test ' + str(2.23)
    """)
    expected_tree = ast.parse("""
        var1 = u'test'
        var2 = unicode()
        var3 = u'test ' + unicode(2.23)
    """)
    transformer = StringTypesTransformer()
    result = transformer.transform(tree)
    assert result.tree == expected_tree

# Generated at 2022-06-14 02:23:46.416322
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    klass = StringTypesTransformer
    assert klass.transform(ast.parse("a = str('test')")) == TransformationResult(ast.parse("a = unicode('test')"), True, [])
    assert klass.transform(ast.parse("a = 'test'")) == TransformationResult(ast.parse("a = 'test'"), False, [])

# Generated at 2022-06-14 02:24:52.506805
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # If you change anything in the following code,
    # please verify the tests in test_2to3.py still pass.
    from .helpers import get_test_program

    program = get_test_program('''
        "test".__class__
        str(1)
        ""
        ""
        ""
        ""
        ""
        ""
        ""
        ""
        ""
        ""
    ''')

    result = program.transformed_by(StringTypesTransformer)
    assert result.tree_changed
    assert get_test_program('''
        "test".__class__
        unicode(1)
        u""
        u""
        u""
        u""
        u""
        u""
        u""
        u""
        u""
        u""
    ''') == result

# Generated at 2022-06-14 02:25:03.495919
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse(textwrap.dedent('''
    if x == "abc":
        print('abc')
    elif x == str('abc'):
        print('abc')
    else:
        print('cba')
    '''))
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed
    assert result.messages == []
    assert astor.to_source(result.tree).strip() == textwrap.dedent('''
    if x == "abc":
        print('abc')
    elif x == unicode('abc'):
        print('abc')
    else:
        print('cba')
    ''').strip()

# Generated at 2022-06-14 02:25:05.439379
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()


# Generated at 2022-06-14 02:25:12.113561
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .util import transform_from_cli, parse_to_ast, compare_asts
    import os
    import sys

    test_path = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(test_path,'..', '..', 'tests', 'resources', 'import_global.py')
    assert(os.path.isfile(test_file))
    ast1 = parse_to_ast(test_file)
    ast2 = transform_from_cli(test_file)
    assert(compare_asts(ast2, ast1, StringTypesTransformer))


# Generated at 2022-06-14 02:25:17.894058
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test with a simple typing rule
    tree = ast.parse("""
a: str
    """)

    tree = StringTypesTransformer.transform(tree).tree
    assert isinstance(tree, ast.AST)
    assert isinstance(tree.body[0], ast.AnnAssign)
    assert isinstance(tree.body[0].target, ast.Name)
    assert isinstance(tree.body[0].annotation, ast.Name)
    assert tree.body[0].target.id == 'a'
    assert tree.body[0].annotation.id == 'unicode'

# Generated at 2022-06-14 02:25:22.433507
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    x = ast.Name(id='str')
    tree = ast.Module(body=[x])
    res = StringTypesTransformer.transform(tree)
    assert res.tree.body[0].id == 'unicode'

# Generated at 2022-06-14 02:25:25.995119
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    example = 'str("hello")'
    expected = ast.parse('unicode("hello")').body[0].value

    obs = StringTypesTransformer.transform(ast.parse(example)).tree

    assert_equals(expected.s, obs.s)

# Generated at 2022-06-14 02:25:33.160294
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('''
s = 'foo'
s = str(1)
''')
    expected_tree = ast.parse('''
s = 'foo'
s = unicode(1)
''')
    result = StringTypesTransformer.transform(tree)
    assert result.tree == expected_tree
    assert result.failures == []



# Generated at 2022-06-14 02:25:43.960988
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    some_str = ast.Name(id='str', ctx=ast.Load())
    some_node = ast.Name(id='unicode', ctx=ast.Load())
    test_tree = ast.Module(body=[
        ast.Expr(value=some_str),
        ast.Assign(targets=[ast.Name(id='test', ctx=ast.Store())], value=some_str),
        ast.Assign(targets=[ast.Name(id='test2', ctx=ast.Store())], value=some_node)
    ])

# Generated at 2022-06-14 02:25:49.803898
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('s = str()')
    expected_tree = ast.parse('s = unicode()')
    result, _ = StringTypesTransformer.transform(tree)
    assert ast.dump(result, include_attributes=True) == ast.dump(expected_tree, include_attributes=True)


if __name__ == "__main__":
    test_StringTypesTransformer()