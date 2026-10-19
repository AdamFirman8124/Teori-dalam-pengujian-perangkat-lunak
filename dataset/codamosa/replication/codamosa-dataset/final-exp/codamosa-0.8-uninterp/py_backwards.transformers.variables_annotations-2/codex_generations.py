

# Generated at 2022-06-14 02:27:59.859565
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform is not None

# Generated at 2022-06-14 02:28:01.282160
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print('\nTest for constructor of class VariablesAnnotationsTransformer')
    # Given

# Generated at 2022-06-14 02:28:03.496655
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse("y : int = 23")) == TransformationResult(ast.parse("y = 23"),True, [])

# Generated at 2022-06-14 02:28:07.772078
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse('a: int = 1')).tree_changed
    assert not VariablesAnnotationsTransformer.transform(ast.parse('a = 1')).tree_changed

# Generated at 2022-06-14 02:28:10.722545
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Basic Functionality test
    transformer = VariablesAnnotationsTransformer()
    code = '''a: str = 10'''
    tree = ast.parse(textwrap.dedent(code))
    new_tree = transformer.visit(tree)
    assert code != astor.to_source(new_tree)

# Generated at 2022-06-14 02:28:17.186597
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = '''
    a: int = 10
    b: int
    '''

    result = BaseTransformer.get_ast(code, (3, 5))

    assert hasattr(result, 'body')
    assert len(result.body) == 2
    assert isinstance(result.body[0], ast.Assign)
    assert isinstance(result.body[1], ast.Expr)

# Generated at 2022-06-14 02:28:23.297221
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""
a: int = 10
b: int
""")
    BaseTransformer.add_backend_import(tree)
    new_tree = VariablesAnnotationsTransformer.transform(tree).tree
    assert ast.dump(new_tree) == ast.dump(ast.parse("""
a = 10
""", mode='exec'))
# end unit test

# Generated at 2022-06-14 02:28:24.100406
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:28:30.632610
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..tools import to_source
    from .ast_compare import compare_ast
    import inspect

    source1 = inspect.getsource(transform)
    source1 = '\n'.join(source1.split('\n')[1:])  # Remove module docstring
    tree1 = ast.parse(source1)
    tree2 = ast.parse(to_source(VariablesAnnotationsTransformer.transform(tree1)))
    assert(compare_ast(tree1, tree2))

# Generated at 2022-06-14 02:28:31.293319
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    pass

# Generated at 2022-06-14 02:28:34.248301
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:28:36.736889
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(None) is not None

# Generated at 2022-06-14 02:28:37.605247
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:28:45.439386
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.parse("def f(x: int = 10, y = 'abc'):\n    pass")
    VariablesAnnotationsTransformer.transform(node)
    assert node.body[0].args.args[0].annotation == ast.Name(id='int', ctx=ast.Param())
    assert node.body[0].args.defaults[0].annotation == ast.Name(id='int', ctx=ast.Param())

# Generated at 2022-06-14 02:28:48.135671
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a:int = 10", filename="", mode="exec")
    VariablesAnnotationsTransformer(tree)


# Generated at 2022-06-14 02:28:54.944215
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    input = """a: int = 10
               b: int = 11
            """
    expected = """a = 10
                  b = 11
            """
    at = ast.parse(input)
    t = VariablesAnnotationsTransformer()
    new_at, tree_changed = t.transform(at)
    assert ast.dump(new_at) == expected
    assert tree_changed
    # TODO: Add unit tests
    # For all functions in this class,
    # define input program, expected output,
    # and test that the output of calling the function with the input is equal to the expected output.

# Generated at 2022-06-14 02:28:59.180228
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    dummy_code = """
a: int = 10
b: int
    """
    dummy_tree = ast.parse(dummy_code)
    dummy_tree_changed, _, _ = VariablesAnnotationsTransformer.transform(dummy_tree)
    assert dummy_tree_changed

# Generated at 2022-06-14 02:29:02.117246
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Unit test for constructor of class VariablesAnnotationsTransformer."""
    assert VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:29:03.823428
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.target == (3, 5)

# Generated at 2022-06-14 02:29:10.191989
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast

    assert isinstance(VariablesAnnotationsTransformer, object)
    assert isinstance(VariablesAnnotationsTransformer(),
                      VariablesAnnotationsTransformer)
    assert isinstance(VariablesAnnotationsTransformer.transform, object)
    assert isinstance(VariablesAnnotationsTransformer.transform(ast), object)

# Generated at 2022-06-14 02:29:22.308066
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3
    from astunparse import unparse
    test_class = VariablesAnnotationsTransformer
    source = """
    a: int
    a: int = 1
    """
    expected = """
    a
    a = 1
    """

    tree = ast3.parse(source)
    result, changed, messages = test_class.transform(tree)
    converted_source = unparse(result)

    assert changed == True
    assert expected == converted_source
    assert messages == []


# Generated at 2022-06-14 02:29:30.049570
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..types import TransformationResult
    from .base import BaseTransformer

    class Tree:
        class body:
            node1 = ast.AnnAssign()
            node2 = ast.AnnAssign()
            node3 = ast.AnnAssign()
            node4 = ast.AnnAssign()
            node5 = ast.AnnAssign()
            node6 = ast.AnnAssign()

    tree = Tree()

    class My_AnnAssign(ast.AnnAssign):
        def __init__(self, value):
            self.value = value

    class My_Assign(ast.Assign):
        def __init__(self, value):
            self.value = value


# Generated at 2022-06-14 02:29:39.224692
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code_str = """
    class C:
      def __init__(self, a: int = 10, b: bool = False, c: str = 'test'):
        self.a: int = a
        self.b: bool = b
        self.c: str = c
    """

    module = ast.parse(code_str)

    tree, tree_changed, meta = VariablesAnnotationsTransformer.transform(module)

    # Test that tree is changed
    assert tree_changed == True
    # Test that meta is an empty list
    assert meta == []
    # Test that the tree is correctly changed
    assert ast.dump(module) == ast.dump(tree)

# Generated at 2022-06-14 02:29:48.922962
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
    a = 10
    b: int = 11
    """
    t = VariablesAnnotationsTransformer()
    node = ast.parse(code)
    t.transform(node)

    assert node.body[0].__class__.__name__ == 'Assign'
    assert node.body[0].value.__class__.__name__ == 'Num'
    assert node.body[0].value.n == 10
    assert node.body[0].target.id == 'a'

    assert node.body[1].__class__.__name__ == 'Assign'
    assert node.body[1].value.__class__.__name__ == 'Num'
    assert node.body[1].value.n == 11
    assert node.body[1].target.id == 'b'

# Generated at 2022-06-14 02:29:54.462471
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..transforms import transform_code
    from astunparse import dump
    from .base import BaseTestCase
    from .test_imports import ImportTransformerTestCase

    tree = ast.parse(ImportTransformerTestCase.test_transform.__doc__)
    VariablesAnnotationsTransformer.transform(tree)
    print(dump(tree))


# Generated at 2022-06-14 02:29:58.367177
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import sys

    module_path = "./tests/test_files/test_variables_annotations.py"
    sys.path.append('.')
    tree = ast.parse(open(module_path).read(), module_path)

    result, tree_changed = VariablesAnnotationsTransformer.transform(tree)
    assert tree_changed == True
    print(result)

# Generated at 2022-06-14 02:30:02.794036
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    ''' This test checks that the constructor of class VariablesAnnotationsTransformer works as expected '''
    actual=VariablesAnnotationsTransformer()
    assert actual.target == (3, 5), "Should be (3, 5)"


# Generated at 2022-06-14 02:30:06.471024
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    foo: int = VariablesAnnotationsTransformer(0, [])
    assert foo.target == (3, 5)
    assert foo.version() == (3, 0)


# Generated at 2022-06-14 02:30:16.143009
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test case 1
    code = """
    a: int = 10
    b: int
    """
    new_code = """
    a = 10
    """
    tree = ast.parse(code)
    tree = VariablesAnnotationsTransformer.transform(tree)
    code2 = compile(tree, "", "exec")
    code2 = '\n'.join([line.strip() for line in code2.splitlines()[1:-1]])
    assert code2 == new_code
    
    # Test case 2: no changes
    code = """
    a = 10
    """
    tree = ast.parse(code)
    tree = VariablesAnnotationsTransformer.transform(tree)
    code2 = compile(tree, "", "exec")

# Generated at 2022-06-14 02:30:25.992582
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import ast
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
    from ..utils.tree import find, get_non_exp_parent_and_index, insert_at
    from ..utils.helpers import warn
    from ..types import TransformationResult
    from ..exceptions import NodeNotFound
    from .base import BaseTransformer
    from .VariablesAnnotationsTransformer import VariablesAnnotationsTransformer

    class VariablesAnnotationsTransformer(BaseTransformer):
    	"""Compiles:
    	    a: int = 10
    	    b: int
    	To:
    	    a = 10

    	"""
    	target = (3, 5)


# Generated at 2022-06-14 02:30:37.152847
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:30:48.139498
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .test_helpers import assert_transform
    from typed_ast import ast3 as a3
    assert_transform(VariablesAnnotationsTransformer,
        a3.parse('a: int = 10\nb: int'),
        a3.parse('b'))

    assert_transform(VariablesAnnotationsTransformer,
        a3.parse('a: int = 10\nb: int = 20'),
        a3.parse('a = 10\nb = 20'))

    assert_transform(VariablesAnnotationsTransformer,
        a3.parse('a: int = 10\nb: int = 20\nclass C:\n\tpass'),
        a3.parse('a = 10\nb = 20\nclass C:\n\tpass'))


# Generated at 2022-06-14 02:30:51.483532
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor

    src = 'a: int = 10'
    tree = ast.parse(src)
    tree = VariablesAnnotationsTransformer.transform(tree).tree
    print(astor.to_source(tree))

# Generated at 2022-06-14 02:30:52.813655
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print(VariablesAnnotationsTransformer.transform(DeclarationsTestAST.tree))

# Generated at 2022-06-14 02:30:54.446587
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == "VariablesAnnotationsTransformer"


# Generated at 2022-06-14 02:31:05.612556
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .utils import compile_to_ast

    tree: ast.Module = compile_to_ast("""\
x: int = 10
y: int
z: int = 5
    """)

    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.tree_changed

    # x: int = 10
    assert len(result.tree.body) == 3
    assert isinstance(result.tree.body[0], ast.Assign)
    assert len(result.tree.body[0].targets) == 1
    assert isinstance(result.tree.body[0].targets[0], ast.Name)
    assert result.tree.body[0].targets[0].id == 'x'
    assert isinstance(result.tree.body[0].value, ast.Constant)
    assert result

# Generated at 2022-06-14 02:31:09.742931
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 10')
    tree2 = ast.parse('a = 10')
    newTree = VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(newTree) == ast.dump(tree2)


# Generated at 2022-06-14 02:31:22.077964
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    
    # Create tree for test
    test_tree = ast.parse("a: int = 4\nb: int\nc: int = a")

    # Create instance of class VariablesAnnotationsTransformer
    class_VariablesAnnotationsTransformer = VariablesAnnotationsTransformer()

    # Create transformed tree
    transformed_tree = class_VariablesAnnotationsTransformer.transform(test_tree)

    assert transformed_tree.tree.body[0].target.id == "a"
    assert transformed_tree.tree.body[0].value.n == 4

    assert transformed_tree.tree.body[1].target.id == "b"
    assert transformed_tree.tree.body[1].value is None

    assert transformed_tree.tree.body[2].target.id == "c"

# Generated at 2022-06-14 02:31:27.323802
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a: ast.Module = ast.parse('a: int = 10')
    b: ast.Module = ast.parse('b: int')

    assert VariablesAnnotationsTransformer.transform(a).tree == ast.parse('a = 10')
    assert VariablesAnnotationsTransformer.transform(b).tree == ast.parse('# comment\n')

# Generated at 2022-06-14 02:31:30.423060
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Testing the constructor of class VariablesAnnotationsTransformer
    """
    obj = VariablesAnnotationsTransformer()
    assert obj.target == (3, 5)



# Generated at 2022-06-14 02:31:55.902306
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.AnnAssign(target=ast.Name(id='a'), annotation=ast.Name(id='int'), value=ast.Num(10))
    node1 = ast.Assign(targets=[ast.Name(id='a')], value=ast.Num(10), type_comment=ast.Name(id='int'))
    node2 = ast.Module(body=[node])
    node3 = ast.Module(body=[node1])
    assert node2 == VariablesAnnotationsTransformer.transform(node2).tree
    assert node3 == VariablesAnnotationsTransformer.transform(node3).tree

# Generated at 2022-06-14 02:31:59.374500
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast.ast3 import parse
    from .test_utils import should_transform_equal


# Generated at 2022-06-14 02:32:05.584673
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast.ast3 import parse
    tree = parse("a: int = 10")
    result = VariablesAnnotationsTransformer.transform(tree)
    assert str(result.tree) == 'Assign(targets=[Name(id=\'a\', ctx=Store())], value=Num(n=10))'
    assert result.tree_changed == True

# Generated at 2022-06-14 02:32:13.127436
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('''
    a: str = "Hello"
    b: str
    ''')

    tree_should_be = ast.parse('''
    a = "Hello"
    ''')

    tree_changed, new_tree, _ = VariablesAnnotationsTransformer.transform(tree)

    assert tree_changed == True
    assert ast.dump(tree_should_be) == ast.dump(new_tree)

    tree = ast.parse('''
    a: str = "Hello"
    b: str
    ''')

    tree_should_be = ast.parse('''
    a = "Hello"
    b
    ''')

    tree_changed, new_tree, _ = VariablesAnnotationsTransformer.transform(tree)

    assert tree_changed == True

# Generated at 2022-06-14 02:32:19.602400
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    try:
        import typed_ast.ast3 as ta
    except ImportError:
        import typed_ast as ta
    from nuitka.nodes.VariableAnnotations import VariablesAnnotationsTransformer

    module = ta.parse('a: int = 10\nb: int\n')
    module_changed, nodes = VariablesAnnotationsTransformer.transform(module)
    print(module)

# Generated at 2022-06-14 02:32:26.002542
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    '''
    This function tests the constructor of class VariablesAnnotationsTransformer
    '''
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'
    assert VariablesAnnotationsTransformer(ast.parse("a: int = 10\nb: int")).__class__.__name__ == 'VariablesAnnotationsTransformer'


# Generated at 2022-06-14 02:32:32.932257
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    f = ast.AnnAssign(annotation=ast.Name(id='int', ctx=ast.Load()), target=ast.Name(id='a', ctx=ast.Store()), value=ast.Name(id='10', ctx=ast.Load()))
    assert VariablesAnnotationsTransformer.transform(f) == True

# Generated at 2022-06-14 02:32:38.670047
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""a: int = 10\nb: int = 20""").body[0]

    class_ = VariablesAnnotationsTransformer()
    class_.transform(tree)
    expected = ast.parse("""a = 10\n20""")

    assert ast.dump(tree) == ast.dump(expected)

if __name__ == '__main__':
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:32:45.312615
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.parse("a: int = 10")
    for node_t in find(node, ast.AnnAssign):
        node_t.target = ast.Name(id='a', ctx=ast.Load())
        node_t.annotation = ast.parse("int")
        node_t.value = ast.Num(n=10)
    transformation_res = VariablesAnnotationsTransformer.transform(node)
    assert transformation_res.changed, "Test #1 failed"
    


# Generated at 2022-06-14 02:32:46.872185
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:33:35.241882
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print('Testing VariablesAnnotationsTransformer()')
    print('Test case 1')
    node1 = ast.AnnAssign(target=ast.Name(id='b', ctx=ast.Store()), annotation=ast.Name(id='int', ctx=ast.Load()),
           value=None, simple=1)
    node2 = ast.AnnAssign(target=ast.Name(id='c', ctx=ast.Store()), annotation=ast.Name(id='int', ctx=ast.Load()),
           value=ast.Num(n=5), simple=1)
    node3 = ast.AnnAssign(target=ast.Name(id='d', ctx=ast.Store()), annotation=ast.Name(id='int', ctx=ast.Load()),
           value=None, simple=1)
   

# Generated at 2022-06-14 02:33:40.174025
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""a: int = 10
                        b: int
                        c: str = "foo"
                      """)
    expected_tree = ast.parse("""a = 10
                                 c = "foo"
                               """)

    tree = VariablesAnnotationsTransformer.transform(tree)
    assert expected_tree == tree.tree

# Generated at 2022-06-14 02:33:47.827534
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.tester import make_test, get_test_result

    # Call VariablesAnnotationsTransformer.transform(tree)
    test_1 = make_test(VariablesAnnotationsTransformer, 3, 5,
'''
a: int = 10
''',
'''
a = 10
''')

    # Call VariablesAnnotationsTransformer.transform(tree)
    test_2 = make_test(VariablesAnnotationsTransformer, 3, 5,
'''
a: int = 10
b: int
''',
'''
a = 10
''')

    # Call VariablesAnnotationsTransformer.transform(tree)
    test_3 = make_test(VariablesAnnotationsTransformer, 3, 5,
'''
a: int
b: int
''',
'''

''')

    # Call Vari

# Generated at 2022-06-14 02:34:00.096635
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .base import test_index
    from ..utils.helpers import compare_ast
    from ..errors import Error
    from ast_helpers.transformer_factory import transform
    from typed_ast.ast3 import parse

    ast_py_v3 = parse("a: int = 10\nb: int = 11")
    ast_py_py = parse("a = 10\nb = 11")
    ast_out = VariablesAnnotationsTransformer.transform(ast_py_v3).tree

    compare_ast(ast_py_py, ast_out, test_index, test_index, False)

    # Test if the transformer raise an error
    ast_py_v3 = parse("a: int = 10\nb: int")
    result = transform(ast_py_v3, VariablesAnnotationsTransformer)

# Generated at 2022-06-14 02:34:06.230733
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    ''' Test for constructor. '''
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'
    assert VariablesAnnotationsTransformer.__doc__ ==  """Compiles:
        a: int = 10
        b: int
    To:
        a = 10"""


# Generated at 2022-06-14 02:34:08.343940
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Unit test for constructor of class VariablesAnnotationsTransformer"""
    




# Generated at 2022-06-14 02:34:18.317052
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    stmt1 = ast.AnnAssign(target=ast.Name(id="a", ctx=ast.Store()),
                          annotation=ast.Name(id="int", ctx=ast.Load()),
                          value=ast.Num(n=10))
    stmt2 = ast.AnnAssign(target=ast.Name(id="b", ctx=ast.Store()),
                          annotation=ast.Name(id="int", ctx=ast.Load()),
                          value=None)
    test_tree = ast.Module(body=[stmt1, stmt2])

# Generated at 2022-06-14 02:34:28.450837
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = ast.AnnAssign(target=ast.Name(id="a", ctx=ast.Store()), annotation=ast.parse("int"), value= ast.Str(s="test"))
    b = ast.AnnAssign(target=ast.Name(id="b", ctx=ast.Store()), annotation=ast.parse("int"))
    ast.fix_missing_locations(a)
    ast.fix_missing_locations(b)
    print(VariablesAnnotationsTransformer.transform([a,b]))

test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:34:35.409874
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class_name = "VariablesAnnotationsTransformer"
    class_obj = eval(class_name)
    # Check if cls is a class object
    assert(isinstance(class_obj, type))
    # Create an object of the class
    obj = class_obj()
    # Check if class variable 'target' is set and type is tuple
    assert(isinstance(obj.target, tuple))
    # Check if class variable 'tree' is set and type is ast.AST
    assert(isinstance(obj.tree, ast.AST))
    # Check if class method 'transform' is available
    assert(callable(getattr(obj, "transform", None)))

# Generated at 2022-06-14 02:34:43.726244
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3
    ast_node = ast3.AnnAssign(target=ast3.Name(id='b', ctx=ast3.Store()), annotation=ast3.Name(id='int', ctx=ast3.Load()), value=ast3.Constant(value=10))
    result = VariablesAnnotationsTransformer.transform(ast_node)
    assert result.tree == ast3.Assign(targets=[ast3.Name(id='b', ctx=ast3.Store())], value=ast3.Constant(value=10), type_comment=ast3.Name(id='int', ctx=ast3.Load()))
    assert result.tree_changed
    assert result.children == []

# Generated at 2022-06-14 02:36:20.762680
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    x: int = 3
    a = x + 10
    return x + a

t = VariablesAnnotationsTransformer()

'''
# Python3.5
import dis
dis.dis(test_VariablesAnnotationsTransformer)
'''

# Output:
#   1           0 LOAD_CONST               3 (10)
#               2 STORE_FAST               1 (a)
#
#   2           4 LOAD_FAST                0 (x)
#               6 LOAD_FAST                1 (a)
#               8 BINARY_ADD
#              10 RETURN_VALUE

# Generated at 2022-06-14 02:36:29.520212
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    import astunparse
    from typed_ast.ast3 import AnnAssign, Load, Store, Name, Assign
    code = 'a: int = 10\nb: int'
    tree = ast.parse(code)
    transformer = VariablesAnnotationsTransformer()
    new = transformer.transform(tree)
    tree = new.tree
    node = tree.body[0]
    assert astunparse.dump(node) == "a = 10"
    node = tree.body[1]
    assert isinstance(node, AnnAssign)
    assert isinstance(node.target, Name)
    assert isinstance(node.target.ctx, Store)
    assert astunparse.dump(node) == "b: int"

# Generated at 2022-06-14 02:36:32.548532
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10\nb: int")
    assert VariablesAnnotationsTransformer.transform(tree).tree == ast.parse("a = 10\nb: int")

# Generated at 2022-06-14 02:36:46.101449
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.tree import get_ast
    from ..utils.helpers import get_default_args
    from ..visitors.base import BaseParser

    def check(input_code: str, expected_code: str) -> None:
        """Helper function to test transformer"""
        tree = get_ast(input_code)
        VariablesAnnotationsTransformer.transform(tree)
        actual_code = BaseParser.dump_ast(tree)
        assert actual_code == expected_code

    # Test 1 (a: int = 10)
    input_code = '''
    a: int = 10
    '''
    expected_code = '''
    a = 10
    '''
    check(input_code, expected_code)

    # Test 2 (a: int, b: str)

# Generated at 2022-06-14 02:36:50.471324
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
        a: int = 10
        b: int
    """
    tree = ast.parse(code)

    new_tree = VariablesAnnotationsTransformer.transform(tree)

    compare_ast(new_tree, """
    a = 10
    """)

# Generated at 2022-06-14 02:36:53.186159
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():  # pragma: no cover
    # TODO: implement this unit test
    # The lines below fake the test; they will be removed once the test has
    # been implemented
    assert True

# Generated at 2022-06-14 02:37:03.371036
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.tree import parse
    from ..utils.helpers import astformat
    code = """
        a: int = 10
        b: int
    """
    tree = parse(code)
    VariablesAnnotationsTransformer.transform(tree)
    assert astformat(tree) == """ 
    Module(
        body=[
            Assign(
                targets=[
                    Name(
                        id='a',
                        ctx=Store()
                    )
                ],
                value=Num(n=10),
            ),
            AnnAssign(
                target=Name(
                    id='b',
                    ctx=Store()
                ),
                annotation=Name(
                    id='int',
                    ctx=Load()
                )
            )
        ]
    )
    """, 'VariablesAnnotationsTransformer test failed'

# Generated at 2022-06-14 02:37:08.754092
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Unit test for constructor of class VariablesAnnotationsTransformer"""
    import BlackGeminiPy
    tree = ast.parse("""
a: int = 10
b: int""")
    assert BlackGeminiPy.compat.backport(tree, (3, 5)) == """
a = 10""", BlackGeminiPy.compat.backport_ast(tree, (3, 5))

# Generated at 2022-06-14 02:37:13.644808
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class Foo(object):
        '''Foo class'''
        def __init__(self):
            '''init.'''
            self.a: int = 1
    class_foo = ast.parse(inspect.getsource(Foo))
    VariablesAnnotationsTransformer.transform(class_foo)
    assert eval(compile(class_foo, filename="<ast>", mode="exec")) == Foo

# Generated at 2022-06-14 02:37:17.796690
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'
    assert VariablesAnnotationsTransformer.__doc__ is not None
    assert VariablesAnnotationsTransformer.transform.__doc__ is not None
    assert VariablesAnnotationsTransformer.target == (3, 5)
