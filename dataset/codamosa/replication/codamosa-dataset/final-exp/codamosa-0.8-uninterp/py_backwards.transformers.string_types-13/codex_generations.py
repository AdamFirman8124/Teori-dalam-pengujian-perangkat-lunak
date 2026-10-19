

# Generated at 2022-06-14 02:17:00.550054
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from ..utils import get_ast
    from .string_types import StringTypesTransformer
    from ..utils.compare_asts import compare_asts
    file_path = 'examples/python2/string_types.py'
    ast1 = get_ast(file_path)
    ast2 = get_ast(file_path)
    ref_ast = get_ast(file_path)
    ast1 = StringTypesTransformer.transform(ast1).tree
    ast2 = StringTypesTransformer.transform(ast2).tree
    assert compare_asts(ast1, ref_ast)

# Generated at 2022-06-14 02:17:06.745447
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str(unicode)')
    result = StringTypesTransformer.transform(tree)
    
    assert(result.tree.body[0].value.func.id == 'unicode')
    assert(result.tree_changed is True)
    assert(len(result.warnings) == 0)

# Generated at 2022-06-14 02:17:08.787480
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    return StringTypesTransformer.transform(ast.parse("""a = str()""", mode="exec"))

# Generated at 2022-06-14 02:17:17.260550
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test cases for StringTypesTransformer.
    """
    # The AST with string types
    tree = ast.parse("""def convert(value):
        '''Convert to int'''
        return int(value)
        """)
    # The expected out
    exp = ast.parse("""def convert(value):
        '''Convert to int'''
        return int(value)
        """)
    # Test method
    result = StringTypesTransformer.transform(tree)
    # Check if the result is as expected
    assert ast.dump(result.tree) == ast.dump(exp)

# Generated at 2022-06-14 02:17:20.043453
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(
        ast.parse('str')
    ) == TransformationResult(
        tree=ast.parse('unicode'),
        tree_changed=True,
        imports=[]
    )

# Generated at 2022-06-14 02:17:29.877619
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..types import TEST_TREE_STR
    from ..utils import parse
    from typing import cast

    tree = parse(TEST_TREE_STR)
    result = StringTypesTransformer.transform(cast(ast.AST,tree))
    result = cast(TransformationResult,result)
    assert result.tree_changed == True
    for i in find(result.tree, ast.Name):
        if i.id == 'str':
            assert False
    for i in find(result.tree, ast.Name):
        if i.id == 'unicode':
            assert True

# Generated at 2022-06-14 02:17:33.762256
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source2 = """
    def foo(input):
        return str(input)"""
    res2 = StringTypesTransformer.transform(ast.parse(source2))
    assert ''.join(res2.changed_lines).strip() == "return unicode(input)"

# Generated at 2022-06-14 02:17:43.333305
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import get_source

    class SourceCodeWidget(QWidget):
        def __init__(self, parent=None):
            super(SourceCodeWidget, self).__init__(parent)
            self.source = get_source(QDateTime)

        def paintEvent(self, event):
            painter = QPainter(self)
            painter.drawText(self.rect(), self.source)
            painter.end()

    with_transform = StringTypesTransformer.transform_source(get_source(SourceCodeWidget))

    class SourceCodeWidgetPython2(SourceCodeWidget):
        def __init__(self, parent=None):
            super(SourceCodeWidgetPython2, self).__init__(parent)
            self.source = StringTypesTransformer.transform_source(get_source(SourceCodeWidget))


# Generated at 2022-06-14 02:17:47.029885
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer(ast.parse('''def x():
        print(str(1) + 'a')
     ''')).transform() == (ast.parse('''def x():
        print(unicode(1) + 'a')
     '''), True, [])

# Generated at 2022-06-14 02:17:52.938627
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str x')
    output, tree_changed, info = StringTypesTransformer.transform(tree)
    assert tree_changed
    assert info == []
    assert ast.dump(output) == "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], value=Unicode())])"

# Generated at 2022-06-14 02:17:58.290413
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(
        tree=ast.parse(text='str("foo")', mode='eval')
    ).tree_changed == True


# Generated at 2022-06-14 02:18:07.570228
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    p = ast.parse('print str(x)')
    e = ast.Expression(
        body=ast.Call(
            func=ast.Name(
                id='print',
                ctx=ast.Load()
            ),
            args=[
                ast.Call(
                    func=ast.Name(
                        id='unicode',
                        ctx=ast.Load()
                    ),
                    args=[
                        ast.Name(
                            id='x',
                            ctx=ast.Load()
                        )
                    ],
                    keywords=[],
                    starargs=None,
                    kwargs=None
                )
            ],
            keywords=[],
            starargs=None,
            kwargs=None
        )
    )
    t = StringTypesTransformer.transform(p)
    assert t.tree == e
   

# Generated at 2022-06-14 02:18:15.703129
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code_str1 = "f = open('a.txt', 'w')"
    code_str2 = "open('a.txt', 'w')"
    code_str3 = "type('a.txt') is str"
    result_code_str1 = "f = open('a.txt', 'w')"
    result_code_str2 = "open('a.txt', 'w')"
    result_code_str3 = "type('a.txt') is unicode"

    tree1 = ast.parse(code_str1)
    tree2 = ast.parse(code_str2)
    tree3 = ast.parse(code_str3)
    result_tree1 = ast.parse(result_code_str1)
    result_tree2 = ast.parse(result_code_str2)
    result_tree

# Generated at 2022-06-14 02:18:16.792516
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert isinstance(StringTypesTransformer, type)

# Generated at 2022-06-14 02:18:23.014753
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Tests generating and transforming code fragments
    tree = ast.parse('str("hello")')
    new_tree = StringTypesTransformer.transform(tree)
    assert ast.dump(new_tree) == ast.dump(ast.parse('unicode("hello")'))

    # Tests generating and transforming files
    test_path = 'test_sample.py'
    ast_dict = {
        '2.7': test_path
    }
    TreeRun(ast_dict, 'unicode("hello")')
    return

# Generated at 2022-06-14 02:18:27.342282
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()

    tree = ast.parse('str()', mode='eval')
    transformer.transform(tree)
    assert tree.body.func.id == 'unicode'

    tree = ast.parse('name', mode='eval')
    transformer.transform(tree)
    assert not hasattr(tree.body, 'id')

# Generated at 2022-06-14 02:18:35.112003
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # test when tree is changed
    code = """str(1)"""
    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)
    expected = """unicode(1)"""
    assert expected == astor.to_source(result.tree)

    # test when tree is the same
    code = """x = "test" """
    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)
    expected = """x = "test" """
    assert expected == astor.to_source(result.tree)

# Generated at 2022-06-14 02:18:43.666354
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_ast

    ast_tree = source_to_ast("""
x = str() # new
y = str(1) # new
z = str(c) # new
    """)

    new_ast_tree, changed, messages = StringTypesTransformer.transform(ast_tree)
    assert changed is True
    assert str(new_ast_tree) == str(source_to_ast("""
x = unicode() # new
y = unicode(1) # new
z = unicode(c) # new
    """))

# Generated at 2022-06-14 02:18:55.277940
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .basic import BasicTransformer
    
    # string type
    code = '''
    def foo(x: str):
        return x
    '''
    tree = ast.parse(code)
    BasicTransformer.annotate(tree)
    StringTypesTransformer.transform(tree)
    assert_code(code, tree)

    # string type
    code = '''
    def foo(x: str):
        return str(x)
    '''
    tree = ast.parse(code)
    BasicTransformer.annotate(tree)
    StringTypesTransformer.transform(tree)
    assert_code(code, tree)

    # empty string type
    code = '''
    def foo(x: ''):
        return x
    '''
    tree = ast.parse(code)
    BasicTransformer.annot

# Generated at 2022-06-14 02:19:00.035219
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('"string".replace("str", str())')
    t = StringTypesTransformer()
    new_tree = t.visit(tree)
    assert "unicode" in astunparse.unparse(new_tree)
    assert "str" not in astunparse.unparse(new_tree)

# Generated at 2022-06-14 02:19:06.767757
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str + str')
    assert StringTypesTransformer.transform(tree).tree_changed == True

# Generated at 2022-06-14 02:19:10.864835
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tt = StringTypesTransformer()
    assert tt.transform(ast.parse("def foo(a: str, b: str): pass")).tree == ast.parse("def foo(a: unicode, b: unicode): pass")

# Generated at 2022-06-14 02:19:17.685203
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    # Test 1: str to unicode
    tree = ast.parse("str()")
    transformed_tree, tree_changed, warnings = StringTypesTransformer.transform(
        tree)
    assert tree_changed, "The tree was not changed"
    assert isinstance(find(tree, ast.Call).func, ast.Name), "The str was not transformed to unicode"

    # Test 2: not transformation
    tree = ast.parse("'no unicode'")
    transformed_tree, tree_changed, warnings = StringTypesTransformer.transform(
        tree)
    assert not tree_changed, "The tree was changed"

# Generated at 2022-06-14 02:19:18.862822
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..all import StringTypesTransformer


# Generated at 2022-06-14 02:19:22.397369
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
            def func():
                a = str
            """
    tree = ast.parse(code)
    s = StringTypesTransformer()
    tree1 = s.visit(tree)

    assert find(tree1, ast.Name)

# Generated at 2022-06-14 02:19:27.384530
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('''
a = str(2)
''')

    expected_transformed_tree = ast.parse('''
a = unicode(2)
''')

    res = StringTypesTransformer.transform(tree)
    assert res.tree == expected_transformed_tree


# Generated at 2022-06-14 02:19:27.951918
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:19:33.348134
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import textwrap

    source = textwrap.dedent('''
        def foo():
            print(str('a'))
        print(str('b'))
    ''')

    expected_source = textwrap.dedent('''
        def foo():
            print(unicode('a'))
        print(unicode('b'))
    ''')

    tree = ast.parse(source)
    assert StringTypesTransformer.transform(tree).tree_changed
    assert ast.dump(tree) == expected_source

# Generated at 2022-06-14 02:19:38.854293
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    source = ast.parse("a = str()")
    tree = StringTypesTransformer.transform(source).tree
    print(ast.dump(tree))
# expect:
# Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[], keywords=[]))])

# Generated at 2022-06-14 02:19:47.711523
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Initialize the tree, nodes and the transformer
    input_str = "value = \"Hello World!\"\nprint(str(value))"
    tree = ast.parse(input_str)
    input_node1 = ast.Name(id='str', ctx=ast.Load())
    input_node2 = ast.Str('Hello World!')
    transformer = StringTypesTransformer()

    # Call the transform function
    result = transformer.transform(tree)

    # Get the nodes
    result_node1 = result.tree.body[1].value.func
    result_node2 = result.tree.body[0].value

    # Assert that the correct nodes are equal to the created nodes
    assert(result_node1 == input_node1)
    assert(result_node2 == input_node2)

# Generated at 2022-06-14 02:19:58.486927
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = "from typed_ast import ast3 as ast; ast.Name('str')"
    expected_code = "from typed_ast import ast3 as ast; ast.Name('unicode')"
    tree = ast.parse(code)
    print(ast.dump(tree))
    transformed_tree, changed, messages = StringTypesTransformer.transform(tree)
    assert changed
    print(ast.dump(transformed_tree))
    assert ast.dump(transformed_tree) == expected_code

# Generated at 2022-06-14 02:20:05.659147
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import sys
    import astor
    from io import StringIO
    from ..types import Py2PyTransformationsPipeline
    
    class Swapper(object):
        """Wrapper for an instance attribute which can be modified in a with statement

        """
        def __init__(self, obj, attr):
            self.obj = obj
            self.attr = attr
            self.real_stdout = sys.stdout

        def __enter__(self):
            setattr(self.obj, self.attr, StringIO())
            sys.stdout = getattr(self.obj, self.attr)

        def __exit__(self, type, value, traceback):
            sys.stdout = self.real_stdout


    p2p = Py2PyTransformationsPipeline(StringTypesTransformer)


# Generated at 2022-06-14 02:20:18.522857
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import copy
    import typed_ast.ast3 as ast
    from ..utils.syntaxtree import SyntaxTree

    test_tree = SyntaxTree("""
    import os
    import sys
    def add(a, b):
        print("Hello world")
        return a + b
    add("Hello", "World")
    """)

    transformer = StringTypesTransformer()
    transformed, _, _ = transformer.transform(test_tree.tree)

    assert isinstance(transformed, ast.Module)
    assert len(transformed.body) == 4
    assert isinstance(transformed.body[0], ast.Import)
    assert isinstance(transformed.body[1], ast.Import)
    assert isinstance(transformed.body[2], ast.FunctionDef)

# Generated at 2022-06-14 02:20:24.282572
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    src = (
        """
        def f():
            pass
        """
    )
    expected_result = (
        """
        def f():
            pass
        """
    )
    tree = ast.parse(src)
    transformer = StringTypesTransformer(tree)
    new_tree = transformer.result()
    assert ast.dump(new_tree) == expected_result
    assert transformer.status == False



# Generated at 2022-06-14 02:20:36.660026
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # tests on Python code
    s = 'a = str(1)'
    tree = ast.parse(s)
    new = StringTypesTransformer.transform(tree)
    assert (new.tree == ast.parse('a = unicode(1)'))
    assert (new.tree_changed == True)
    assert (new.file_changed == [])
    s = 'a = str'
    tree = ast.parse(s)
    new = StringTypesTransformer.transform(tree)
    assert (new.tree == ast.parse('a = unicode'))
    assert (new.tree_changed == True)
    assert (new.file_changed == [])
    s = 'str=str'
    tree = ast.parse(s)
    new = StringTypesTransformer.transform(tree)

# Generated at 2022-06-14 02:20:37.912390
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:20:42.747344
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer()
    b = ast.Module(body=[ast.Expr(value=ast.Name(id='str'))])
    a = ast.Module(body=[ast.Expr(value=ast.Name(id='unicode'))])
    assert t.transform(b).tree == a

# Generated at 2022-06-14 02:20:47.210202
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """
            a = str()
            """

    expected = """
            a = unicode()
            """

    tree = ast.parse(source)

    tr = StringTypesTransformer()
    new_tree = tr.transform(tree)

    assert ast.dump(new_tree) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 02:20:47.861716
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:20:50.407574
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.smk_testing import run_test_transform
    run_test_transform(StringTypesTransformer)

# Generated at 2022-06-14 02:21:09.715114
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transf = StringTypesTransformer()
    module_str = "import abc\n"
    module_str += "import collections\n"
    module_str += "import keyword\n"
    module_str += "import random\n"
    module_str += "import string\n"
    module_str += "\n"
    module_str += "from typing import Any, Union, Tuple, List, Dict, Sequence, Iterable, Callable, Generator\n"
    module_str += "\n"
    module_str += "def f(param: str) -> str:\n"
    module_str += "   return param"
    module_ast = ast.parse(module_str)
    module_transformed_ast, changed = transf.transform(module_ast)
    assert changed
    # Check if the transformer transformed the string '

# Generated at 2022-06-14 02:21:21.451745
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
    def f ():
        a = str()
        b = str(2)
        c = str(True)
        d = str('a')
        e = str(a)
        f = str(f)
    """)

    tree1 = ast.parse("""
    def f ():
        a = unicode()
        b = unicode(2)
        c = unicode(True)
        d = unicode('a')
        e = unicode(a)
        f = unicode(f)
    """)

    result = StringTypesTransformer().transform(tree)
    assert ast.dump(tree1) == ast.dump(result.tree)
    assert result.tree_changed == True

# Generated at 2022-06-14 02:21:26.430350
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """str()"""
    mod = ast.parse(source)
    mod = StringTypesTransformer.transform(mod)
    assert mod.code == "unicode()"



# Generated at 2022-06-14 02:21:32.368910
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor  # type: ignore

    tree = ast.parse('a = str()')
    transformed_tree, tree_changed, error_msgs = StringTypesTransformer.transform(tree)
    assert tree_changed
    assert astor.to_source(transformed_tree) == 'a = unicode()'


if __name__ == '__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:21:36.519065
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    x = 'abc'
    def foo(y):
        z = 'xyz'
        return z
    """
    tree = ast.parse(code)
    tree = StringTypesTransformer.transform(tree)
    assert tree.changes

# Generated at 2022-06-14 02:21:37.600005
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:21:42.300298
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    # Construct an instance of StringTypesTransformer
    transformer = StringTypesTransformer()
    # Sample AST
    tree = ast.parse("str(1)")
    # Transform the AST
    new_tree = transformer.visit(tree)
 
    assert astor.to_source(new_tree) == "unicode(1)"

# Generated at 2022-06-14 02:21:54.380388
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from .test_base import transform_test


# Generated at 2022-06-14 02:22:04.895484
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('"Hello Wolrd!"')) == TransformationResult(ast.parse('u"Hello Wolrd!"'), True, [])

    assert StringTypesTransformer.transform(ast.parse('"""\nHello Wolrd!\n"""')) == TransformationResult(ast.parse('u"""\nHello Wolrd!\n"""') ,True, [])

    assert StringTypesTransformer.transform(ast.parse('"""\nHello Wolrd!\n""" + """\nHey\n"""', mode='exec')) == TransformationResult(ast.parse('u"""\nHello Wolrd!\n""" + u"""\nHey\n"""', mode='exec'), True, [])


# Generated at 2022-06-14 02:22:05.861400
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:22:26.224369
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import sys
    
    ast_str = """
        if x:
            print(str(2))
        else:
            print(str(3))
        """
    ast_str = ast.parse(ast_str)
    
    StringTypesTransformer().visit(ast_str)
    ast.fix_missing_locations(ast_str)
    assert astor.to_source(ast_str) == """
        if x:
            print(unicode(2))
        else:
            print(unicode(3))
        """

# Generated at 2022-06-14 02:22:31.977716
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    foo = str
    """
    tree = ast.parse(code)
    t = StringTypesTransformer.transform(tree)
    code_out = compile(t.tree, '', mode='exec')
    namespace = {}
    exec(code_out, namespace)
    assert namespace['foo'] == unicode

# Generated at 2022-06-14 02:22:35.850363
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    input_str = """str(5)"""
    output_str = """unicode(5)"""
    tree = ast.parse(input_str)
    new_tree = StringTypesTransformer().transform(tree)
    assert ast.dump(new_tree) == output_str

# Generated at 2022-06-14 02:22:36.897550
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:22:46.004354
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = StringTypesTransformer()
    x = ast.parse("str(x)")
    print(ast.dump(x))
    x = ast.parse("str(x)")
    t.transform(x)
    print(ast.dump(x))
    x = ast.parse("y = str(x)")
    t.transform(x)
    print(ast.dump(x))

# Generated at 2022-06-14 02:22:52.052692
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    def dummy(s: str) -> str:
        return s
    """
    # Run the test
    result = StringTypesTransformer.transform(ast.parse(code))
    # Assert that tree was changed
    assert result.tree_changed

# Generated at 2022-06-14 02:23:02.224875
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Simple unit tests for StringTypesTransformer.
    
    """
    # TODO: Write unit tests for StringTypesTransformer!

    assert(str(StringTypesTransformer))
    assert(repr(StringTypesTransformer))
    assert(callable(StringTypesTransformer))
    assert(hasattr(StringTypesTransformer, "__module__"))
    assert(hasattr(StringTypesTransformer, "__name__"))
    assert(hasattr(StringTypesTransformer, "transform"))
    assert(hasattr(StringTypesTransformer, "target"))
    assert(isinstance(StringTypesTransformer.__module__, str))
    assert(isinstance(StringTypesTransformer.__name__, str))
    assert(isinstance(StringTypesTransformer.transform, collections.Callable))

# Generated at 2022-06-14 02:23:03.886714
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    stringTypesTransformer = StringTypesTransformer()


# Generated at 2022-06-14 02:23:13.876087
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from textwrap import dedent

    source = dedent('''
        call_some_function(str)
        call_some_function_with_keyword_args(type=str)
        call_some_function_with_var_args(*str)
        call_some_function_with_kw_args(**str)
        VAR = str
        VAR1, VAR2, VAR3 = str, str, str
    ''')


# Generated at 2022-06-14 02:23:15.822593
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:23:51.394937
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse
    from ..converter import PythonConverter
    code = "a = str('b')"
    tree = ast.parse(code)
    new_tree, changed = PythonConverter(StringTypesTransformer).visit(tree)
    assert changed
    assert astunparse.unparse(new_tree) == "a = unicode('b')\n"

    code = "a = str('b')"
    tree = ast.parse(code)
    new_tree, changed = PythonConverter(StringTypesTransformer).visit(tree)
    assert changed
    assert astunparse.unparse(new_tree) == "a = unicode('b')\n"

# Generated at 2022-06-14 02:23:59.624096
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from ast_tool_box import Transformer

    class TestTransformer(Transformer):
        def test_visit_Name(self, node):
            assert isinstance(node, ast.Name)
            assert isinstance(node.ctx, ast.Load)
            assert node.id == "unicode"

            return node

    tree = ast.parse("print len(str('hi'))")
    tree = StringTypesTransformer.transform(tree)
    TestTransformer().visit(tree)

# Generated at 2022-06-14 02:24:04.192987
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.testing import assert_transformation
    from ..utils.testing import generate_fixture
    from ..utils.testing import load_fixture

    from .string_types import StringTypesTransformer

    assert_transformation(StringTypesTransformer, load_fixture('string_types'), generate_fixture('string_types'))

# Generated at 2022-06-14 02:24:09.538842
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
    a = str()
    '''
    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)
    assert(tree)
    exec(compile(tree, filename="<ast>", mode="exec"))
    assert(a == u'')

# Generated at 2022-06-14 02:24:13.733265
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    stringTypesTransformer = StringTypesTransformer()
    assert stringTypesTransformer.transform(ast.parse('x = str(y)'))[0].body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:24:21.835424
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from py2to3.transformer import Transformer
    from ast_tools import dump
    import astunparse

    test_code = """
        var = str(42)
    """

    expected_ast = ast.parse(
        """
        var = unicode(42)
        """)
    tree = ast.parse(test_code)
    t = Transformer()
    t.register(StringTypesTransformer)
    t.apply(tree)
    assert ast.dump(tree) == ast.dump(expected_ast)
    assert astunparse.unparse(tree) == astunparse.unparse(expected_ast)

# Generated at 2022-06-14 02:24:26.440543
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    from typed_ast import ast3 as ast
    from ..types import TreeInstance
    from ..utils.tree import find


# Generated at 2022-06-14 02:24:37.081345
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_base import CodeTransformerTestCase
    cls = CodeTransformerTestCase(StringTypesTransformer, 2, 7)

    cls.test_tree1('""')
    cls.test_tree2('""')
    cls.test_tree3('""', expected_tree_changed=True)
    cls.test_tree4('""', expected_tree_changed=True)
    cls.test_tree5('""')
    cls.test_tree6('""')
    cls.test_tree7('""', expected_tree_changed=True)
    cls.test_tree8('""', expected_tree_changed=True)
    cls.test_tree9('""')
    cls.test_tree10('""')

# Generated at 2022-06-14 02:24:46.257641
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for `StringTypesTransformer`.

    """
    from ..run import compile_code
    from textwrap import dedent

    source = dedent("""
        x = str(y)
    """)
    tree = compile_code(source, 2, 7)
    tree = StringTypesTransformer.transform(tree)
    code = compile(tree, '<testcase>', 'exec')
    globals_ = {}
    locals_ = {'y': 123}
    exec(code, globals_, locals_)

    assert locals_['x'] == '123'

# Generated at 2022-06-14 02:24:49.220845
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
    """)
    result = StringTypesTransformer().transform(tree)
    assert result.tree_changed is False

# Generated at 2022-06-14 02:25:47.934065
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('a = str(2)')
    expected = ast.parse('a = unicode(2)')
    assert StringTypesTransformer.transform(tree).tree == expected

# Generated at 2022-06-14 02:25:54.291438
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    code = dedent('''\
    x = str('abc')
    ''')
    tree = ast.parse(code)
    result = transformer.transform(tree)
    code_after = to_source(result.tree)
    assert code_after == dedent('''\
    x = unicode('abc')
    ''')



# Generated at 2022-06-14 02:26:03.174401
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    sample = ast.Module([
        ast.Assign([
            ast.Name('a', ast.Store()),
            ast.Name('b', ast.Store()),
        ], ast.Call(
            ast.Name('str', ast.Load()),
            [ast.Num(3)], [], None, None
        ),
        )
    ])

    sample = StringTypesTransformer.transform(sample)
    assert sample.tree.body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:26:07.609459
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = "def foo(arg1):\n" \
           "    x = str\n" \
           "    y = 'x'\n" \
           "    a = str()\n" \
           "    b = str('x')\n" \
           "    c = x('x')\n" \
           "    d = type(x)\n" \
           "    e = isinstance(x, str)\n" \
           "    f = issubclass(type(x), str)\n" \
           "    pass\n"
    tree = ast.parse(code)

# Generated at 2022-06-14 02:26:16.177180
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .. import parse
    from .. import to_source
    from ..types import Code
    from .base import Transformer

    # Test basic case
    test_string = "str"
    test_tree = parse(test_string)
    tr = Transformer.from_subclass(StringTypesTransformer)
    res = tr.transform(test_tree)
    assert to_source(res.tree) == "unicode"

    # Test complex case
    test_string = """
        class Foo:
            def foo(self):
                return str(self)
    """
    test_tree = parse(test_string)
    tr = Transformer.from_subclass(StringTypesTransformer)
    res = tr.transform(test_tree)

# Generated at 2022-06-14 02:26:26.475067
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class A(object):
        def __init__(self):
            self.name = 'foo'
            self.value = 'bar'

    class B(object):
        def __init__(self):
            self.name = 'foo'
            self.value = 'bar'

    class C(object):
        def __init__(self):
            self.name = 'foo'
            self.value = 'bar'

    class D(object):
        def __init__(self):
            self.name = 'foo'
            self.value = 'bar'

    class E(object):
        def __init__(self):
            self.name = 'foo'
            self.value = 'bar'

    assert isinstance(StringTypesTransformer(None, None, None), StringTypesTransformer)

    B(), C(), D(),

# Generated at 2022-06-14 02:26:27.680576
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:26:32.870412
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
  class DummyTransformer(BaseTransformer):
    @classmethod
    def transform(cls, tree: ast.AST) -> TransformationResult:
      return TransformationResult(tree, True, [])
  # test the constructor
  t = DummyTransformer()
  assert t.target == (2, 7)



# Generated at 2022-06-14 02:26:43.220696
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import unittest

    class TestStringTypesTransformer(unittest.TestCase):
        def setUp(self):
            self.maxDiff = None

        def test_transform(self):
            from typed_ast import ast3 as ast
            
            transformer = StringTypesTransformer()
            node = ast.parse("x = str('hello')")
            self.assertTrue(transformer.can_be_applied(node))
            transformed_node, _ = transformer.transform(node)
            self.assertEqual(
                ast.dump(node),
                "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[Str(s='hello')], keywords=[]))])"
            )

# Generated at 2022-06-14 02:26:44.615219
# Unit test for constructor of class StringTypesTransformer