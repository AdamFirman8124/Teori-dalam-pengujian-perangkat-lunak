

# Generated at 2022-06-14 02:28:00.605475
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor
    v=VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:28:05.365291
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.testing import assert_transformation

    assert_transformation(
        VariablesAnnotationsTransformer,
        '''
        def foo():
            a: int = 10
            b: str = "hello"
        ''',
        '''
        def foo():
            a = 10
            b = "hello"
        '''
    )

# Generated at 2022-06-14 02:28:14.579594
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():

    # Initializing VariablesAnnotationsTransformer object
    # object with actual compiler version
    transformer = VariablesAnnotationsTransformer(3.5, 'VariablesAnnotationsTransformer')
    assert transformer.compiler.version == (3.5, 3.5)

    # Initializing VariablesAnnotationsTransformer object
    # object with default compiler version
    transformer = VariablesAnnotationsTransformer(None, 'VariablesAnnotationsTransformer')
    assert transformer.compiler.version == (3.0, 3.0)

    # Initializing VariablesAnnotationsTransformer object
    # object with out of bound compiler version
    transformer = VariablesAnnotationsTransformer(100, 'VariablesAnnotationsTransformer')
    assert transformer.compiler.version == (100, 100)


# Generated at 2022-06-14 02:28:20.739600
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    var = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()),
                        annotation=ast.Name(id='int', ctx=ast.Load()),
                        value=None,
                        simple=1)
    tree = ast.Module(body=[var])
    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.tree == ast.Module(body=[])

# Generated at 2022-06-14 02:28:22.181711
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'

# Generated at 2022-06-14 02:28:26.041983
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import ast
    # a: int
    tree = ast.parse('a: int = 10')
    assert isinstance(tree.body[0], ast.AnnAssign)
    result = VariablesAnnotationsTransformer.transform(tree)
    assert isinstance(result.tree.body[0], ast.Assign)



# Generated at 2022-06-14 02:28:32.270619
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import dump
    from .variable_annotations import VariableAnnotationsTransformer

    source = """
a: int = 10
b: int
c: int
b: str
d: str = {1: 1, 2: 2}
"""

    tree = VariableAnnotationsTransformer.run_pipeline(
        source, {'VariableAnnotationsTransformer'})

    print(dump(tree))
    # assert False

# Generated at 2022-06-14 02:28:33.634205
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert issubclass(VariablesAnnotationsTransformer, BaseTransformer)


# Generated at 2022-06-14 02:28:37.234400
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class T:
        def __init__(self, x):
            self.x = x
    a = T(5)
    assert a.x == 5


# Generated at 2022-06-14 02:28:47.587688
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3
    from .base import TestTransformer
    from ..utils.tree import compare_ast

    source = '''
    a: int = 10
    b: int = 20
    c: int
    '''
    want = ast3.parse('''
    a = 10
    b = 20
    ''',
                      type_comments=True)

    tree = ast3.parse(source,
                      type_comments=True)

    tr = TestTransformer(VariablesAnnotationsTransformer)
    result = tr.process(tree)
    compare_ast(want, result)

# Generated at 2022-06-14 02:28:56.329147
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test-1
    node1 = ast.parse('''
    a: int = 10
    b: int
    ''')
    node2 = ast.parse('''
    a = 10
    ''')
    obj = VariablesAnnotationsTransformer()
    assert str(node2) == str(obj.transform(node1).tree)

    # Test-2
    node1 = ast.parse('''
    a: int = 10
    b: int = 20
    ''')
    node2 = ast.parse('''
    a = 10
    b = 20
    ''')
    obj = VariablesAnnotationsTransformer()
    assert str(node2) == str(obj.transform(node1).tree)

# Generated at 2022-06-14 02:28:58.484971
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..unit import GenericTransformationTest
    GenericTransformationTest(VariablesAnnotationsTransformer)

# Generated at 2022-06-14 02:29:00.929045
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:29:05.866785
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils import test_utils
    test_in = '''a: int = 10'''
    expected_out = '''a = 10'''

    result = test_utils.test(test_in, VariablesAnnotationsTransformer)

    print(result)
    assert result.out == expected_out

# Generated at 2022-06-14 02:29:12.786370
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.source import source_to_tree
    tree = source_to_tree('''x: b
    y: c
    z: d
    a: int = 10
    b: int
    
    def some_func():
        return 0''')
    tree = VariablesAnnotationsTransformer.transform(tree).tree
    assert str(tree) == "x\ny\nz\na = 10\nb\ndef some_func():\n    return 0"


# Generated at 2022-06-14 02:29:13.787765
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:29:15.561969
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()
    assert t.target == (3, 5)

# Generated at 2022-06-14 02:29:17.095423
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print("Unit test for constructor of class VariablesAnnotationsTransformer")


# Generated at 2022-06-14 02:29:25.777614
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    input_code = """
test_variable: int = 10
test_variable_2: int
test_variable_3: int = 20
test_variable_4: int
test_variable_5: int = 30
test_variable_6: None = None
"""
    expected_code = """
test_variable = 10
test_variable_2
test_variable_3 = 20
test_variable_4
test_variable_5 = 30
test_variable_6 = None
"""
    tree = ast.parse(input_code)
    transformer = VariablesAnnotationsTransformer()
    new_tree = transformer.transform(tree)
    assert(expected_code == new_tree.code)

# Generated at 2022-06-14 02:29:35.098478
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print('test_VariablesAnnotationsTransformer')
    ast_node = ast.parse('''
    x = 1
    y: int
    c = 3
    d: int
    ''')

    print(ast.dump(ast_node))
    print(ast.dump(VariablesAnnotationsTransformer.transform(ast_node).tree))
    assert ast.dump(VariablesAnnotationsTransformer.transform(ast_node).tree) ==  ast.dump(ast.parse('''
    x = 1
    c = 3
    '''))

if __name__ == '__main__':
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:29:40.725124
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer


# Generated at 2022-06-14 02:29:49.188417
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    target = (3,5)
    class test_VariablesAnnotationsTransformer(BaseTransformer):
        """Creates a base transformer object."""

    # testing isinstance
    assert isinstance(test_VariablesAnnotationsTransformer, object)
    obj = test_VariablesAnnotationsTransformer
    # Testing __init__
    assert isinstance(obj, test_VariablesAnnotationsTransformer)
    assert obj.target == target

    #testing transform()
    with pytest.raises(TypeError):
        obj.transform()

# Generated at 2022-06-14 02:29:50.920245
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()
    assert t.target == (3, 5)

# Generated at 2022-06-14 02:29:58.661705
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    ast1 = ast.parse('a: int = 5')
    ast2 = ast.parse('b: int = 7')
    ast3 = ast.parse('c: int')

    transformer = VariablesAnnotationsTransformer()
    transformed = transformer.transform(ast1)
    assert transformed.tree == ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Num(5))

    transformed = transformer.transform(ast2)
    assert transformed.tree == ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())], value=ast.Num(7))

    assert transformer.transform(ast3).tree == None

if __name__ == '__main__':
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:30:05.908406
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    ast.parse = mock.MagicMock()
    ast.parse.return_value = ast.parse
    ast.dump = mock.MagicMock()
    tree = ast.parse('a: int = 10')
    VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(tree) == 'Assign(targets=[Name(id="a", ctx=Store())], value=Num(n=10), type_comment=Name(id="int", ctx=Load()))'

# Generated at 2022-06-14 02:30:09.549150
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..types import TransformationResult
    from .base import BaseTransformer
    test_var_annot_transformer = VariablesAnnotationsTransformer()

    assert isinstance(test_var_annot_transformer, BaseTransformer)


# Generated at 2022-06-14 02:30:14.262052
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10\nb: int")
    VariablesAnnotationsTransformer.transform(tree)
    assert(ast.dump(tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Constant(value=10), type_comment=Name(id='int', ctx=Load()))])")

# Generated at 2022-06-14 02:30:17.924737
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .test_helpers import check_transformer
    from typed_ast import ast3 as ast
    check_transformer(VariablesAnnotationsTransformer, ast.parse( """
m: int = 10
n: int
"""
).body)

# Generated at 2022-06-14 02:30:22.666743
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    input_string = "a: b = 2" # Test 1
    indented_input = "a: b = 2"
    result = VariablesAnnotationsTransformer.transform(ast.parse(input_string))
    expected_result = ast.parse(indented_input)
    assert result[0].body[0] == expected_result.body[0]

# Generated at 2022-06-14 02:30:32.523584
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ast import parse
    import sys
    sys.path.append("../")
    from utils.helpers import get_ast
    test1 = "r = range(2)\nfor i in r:\n  print(i)"
    test1_ast = get_ast(test1)
    test1_result = get_ast(test1)
    assert test1_ast != test1_result
    tree_changed = False
    trans_result = VariablesAnnotationsTransformer.transform(test1_ast)
    test1_ast = trans_result.new_tree
    tree_changed = trans_result.tree_changed
    assert test1_ast == test1_result and tree_changed == False
    test2 = "a: int = 10\nb: int"
    test2_ast = get_ast(test2)
   

# Generated at 2022-06-14 02:30:47.054373
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = 'x: int = 5 + 2'
    b = 'y: int'
    a_expected_res = 'x = 5 + 2'
    b_expected_res = ''
    a_result = VariablesAnnotationsTransformer().transform(a)
    b_result = VariablesAnnotationsTransformer().transform(b)
    assert a_expected_res in a_result
    assert b_expected_res in b_result

# Generated at 2022-06-14 02:30:47.792037
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    pass

# Generated at 2022-06-14 02:30:51.250053
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""a: int = 10
b: int""")
    VAR = VariablesAnnotationsTransformer()
    assert VAR.transform(tree).tree_changed == True


# Generated at 2022-06-14 02:30:55.093466
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import parse
    from .context import Context
    node = parse("""
    a : int
    """)
    tree = VariablesAnnotationsTransformer.transform(node)
    Context.set_current_context(Context(target=(3,4)))
    assert str(tree) == ""

# Generated at 2022-06-14 02:30:58.367714
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    try:
        t = VariablesAnnotationsTransformer()
        t.transform(None)
    except Exception:
        pass
    assert 1



# Generated at 2022-06-14 02:31:03.939986
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    source = """
a: int = 10
b: int = None
c = 10
    """
    tree = ast.parse(source)
    t = VariablesAnnotationsTransformer.transform(tree)
    tree = t.tree
    source = astor.to_source(tree).strip()
    expected_source = """
a = 10
c = 10
    """
    assert source == expected_source

# Generated at 2022-06-14 02:31:09.027787
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor
    from .base import BaseTransformer
    from typed_ast import ast3
    from .annotations import AnnotationTransformer
    t = astor.parse('a: int = 10\nb: int')
    a = ast3.parse('a = 10')
    VariablesAnnotationsTransformer.transform(t)
    assert BaseTransformer.structurally_equal(t, a)

# Generated at 2022-06-14 02:31:14.076969
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Unit test for constructor of class VariablesAnnotationsTransformer."""
    transformer = VariablesAnnotationsTransformer()
    print(VariablesAnnotationsTransformer.__doc__)
    print(transformer)
    print(repr(transformer))
    print(transformer.__dict__)



# Generated at 2022-06-14 02:31:18.308717
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.tree import transform_and_compare
    tree = ast.parse("""a: int = 10\nb: int""", '<string>', 'exec')
    expected = ast.parse("""a = 10""", '<string>', 'exec')
    transform_and_compare(tree, expected, VariablesAnnotationsTransformer)



# Generated at 2022-06-14 02:31:20.485933
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import dedent
    from ..utils.tree import build_ast
    from .base import BaseTransformer


# Generated at 2022-06-14 02:31:39.661459
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.AnnAssign()) == ast.Assign()

# Generated at 2022-06-14 02:31:41.116999
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():

    # break the module to get the test coverage up
    raise ImportError

# Generated at 2022-06-14 02:31:47.176114
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    transformer = VariablesAnnotationsTransformer()
    test_code = '''
x: int = 10
'''
    expected_code = '''
x = 10
'''
    tree = ast.parse(test_code)
    new_tree = transformer.transform(tree)
    assert ast.dump(new_tree) == expected_code

# Generated at 2022-06-14 02:31:56.085704
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse(
        'a: int = 10\n'
        'b: int\n'
        'c: int = 20\n'
        'd: int = None\n',
        mode='exec')

    transformer = VariablesAnnotationsTransformer()
    result = transformer.transform(tree)
    assert result.tree_changed

    tree = ast.parse(
        'def func():\n'
        '    a: int = 10\n'
        '    b: int\n'
        '    c: int = 20\n'
        '    d: int = None\n',
        mode='exec')

    transformer = VariablesAnnotationsTransformer()
    result = transformer.transform(tree)
    assert result.tree_changed

# Generated at 2022-06-14 02:32:08.335704
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..exceptions import NodeNotFound
    from .base import BaseTransformer

    class TestTransformer(BaseTransformer):
        pass

    x = TestTransformer.transform(x=ast.parse("a: int = 10\nb: int"))
    x = TestTransformer.transform(x=ast.parse("asdfasdf"))
    try:
        x = TestTransformer.transform(x=ast.parse("(a: int) = 10\nb: int"))
    except NodeNotFound:
        pass
    x = TestTransformer.transform(x=ast.parse("(a: int) = 10\nb: int"))
    x = TestTransformer.transform(x=ast.parse("a: int = 10"))

# Generated at 2022-06-14 02:32:19.583928
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()),
                      annotation=ast.Name(id='int', ctx=ast.Load()),
                      value=ast.Constant(value=10, kind=None),
                      simple=1)
    b = ast.AnnAssign(target=ast.Name(id='b', ctx=ast.Store()),
                      annotation=ast.Name(id='int', ctx=ast.Load()),
                      value=None,
                      simple=0)

    tree = ast.Module(body=[a, b])
    transformation_result = VariablesAnnotationsTransformer.transform(tree)
    assert transformation_result.tree != tree
    assert len(transformation_result.tree.body) == 2

# Generated at 2022-06-14 02:32:27.827492
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 15')
    tree_change = VariablesAnnotationsTransformer.transform(tree)
    assert (tree_change.new_tree == ast.parse('a = 15'))
    assert (tree_change.tree_changed == True)
    assert (tree_change.updated_markers == [])

if __name__ == "__main__":
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:32:34.415402
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class Test:
        a: int = 10
        b: int
    code = inspect.getsource(Test)
    tree = ast.parse(code)
    new_tree = VariablesAnnotationsTransformer.transform(tree).tree
    # ast.dump should be the same as ast.parse(code).
    assert ast.dump(new_tree) == ast.dump(ast.parse(code))

# Generated at 2022-06-14 02:32:38.415981
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # VariablesAnnotationsTransformer('example.py', 3, 5)
    transformer = VariablesAnnotationsTransformer()
    # assert transformer.tree is None
    # assert transformer.tree_changed is False
    # assert transformer.output_path == 'example.py'


# Generated at 2022-06-14 02:32:49.299907
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..unparse import Unparser
    from typing import cast

    # Test for a: int = 10
    test_tree = ast.Module(body=[ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()), annotation=ast.Name(id='int'), value=ast.Num(10), simple=1)])
    test_result, _ = VariablesAnnotationsTransformer.transform(test_tree)
    Unparser(cast(ast.Assign, test_result.body[0]))
    assert str(test_result) == 'a = 10'

    # Test for b: int

# Generated at 2022-06-14 02:33:28.991558
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor

# Generated at 2022-06-14 02:33:34.646069
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    data = open("./pegasus/python_transformer/tests/python_files/VariablesAnnotationsTransformer.py", "r").read()
    tree = ast.parse(data)
    newTree = VariablesAnnotationsTransformer.transform(tree)
    # assert newTree.body[0].value.elts[0].s == "-a"

# Generated at 2022-06-14 02:33:44.040585
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from os.path import dirname, abspath, join

    from typed_ast import ast3 as ast
    from .transformer_test import TransformerTest, print_node

    with TransformerTest(VariablesAnnotationsTransformer) as test:
        test.test('''a: int = 10\nb: int''',
                  'a = 10\n')
        test.test('a: int = 10', 'a = 10')
        test.test('''a: int = 10\nb: int = 20''',
                  'a = 10\nb = 20')
        test.test('a: int', 'a = None')


# Generated at 2022-06-14 02:33:46.041469
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer(None) is not None


# Generated at 2022-06-14 02:33:54.346652
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
a: int = 1
b: float = 1.0
c: float
d: int
e: int = 1
    """
    tree = ast.parse(code)

    expected_code = """
a = 1
b = 1.0

d
e = 1
    """
    expected_tree = ast.parse(expected_code)

    tree = VariablesAnnotationsTransformer.transform(tree)[0]
    assert ast.dump(tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:33:57.656973
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.testing import run_tests, test_node
    from .. import register_transformer
    register_transformer(VariablesAnnotationsTransformer)
    run_tests(VariableAnnotationsTransformer)

# Generated at 2022-06-14 02:34:01.109886
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    test_string = 'a: int = 10'
    test_ast = ast.parse(test_string)
    test_vartran = VariablesAnnotationsTransformer()
    test_vartran.transform(test_ast)
    assert len(test_vartran.hook_errors) == 0


# Generated at 2022-06-14 02:34:12.594152
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from textwrap import dedent
    from ..visitors.ast_visitor import ASTVisitor
    from ..adapters.python_adapter import PythonAdapter

    #Test for the target
    assert VariablesAnnotationsTransformer.target == (3, 5)

    #Test for the transformation
    code = dedent("""
    a:int = 10
    """)
    original_tree = PythonAdapter(code).create_suitable_ast()

    expected_tree = ast.Module(body=[ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                                                value=ast.Num(n=10),
                                                type_comment="int")],
                               type_ignores=[])


# Generated at 2022-06-14 02:34:17.098487
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('''
        a: int = 10
        b: int
    ''')
    result = VariablesAnnotationsTransformer().transform(tree)
    expected = ast.parse('''
        a = 10
    ''')
    assert ast.dump(result.tree) == ast.dump(expected)

# Generated at 2022-06-14 02:34:18.689798
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:35:42.408978
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree: ast.Module = ast.parse('a: int = 10')
    result = VariablesAnnotationsTransformer.transform(tree)
    assert (
        str(result.tree) ==
        "Module(body=[\n"
        "    Assign(targets=[\n"
        "        Name(id='a', ctx=Store())], value=Num(n=10), type_comment=' int')])"
    )

# Generated at 2022-06-14 02:35:47.075626
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .utils.basictest import BasicTest

    # Constructor test
    test = BasicTest(VariablesAnnotationsTransformer, VariablesAnnotationsTransformer.transform)
    #BasicTest.test_transform(transform, test)
    test.test( input_arg={'filename' : 'example/variables_annotations.py'},
               expected_arg={'filename' : 'example/variables_annotations_expected.py'})


# Generated at 2022-06-14 02:35:49.085910
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    transformer = VariablesAnnotationsTransformer()
    assert transformer.version == (3, 5)
    assert transformer.target == (3, 5)


# Generated at 2022-06-14 02:35:52.740796
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import parse
    import astor
    tree = parse("""
a: int = 10
b: int
    """)

    new_tree = VariablesAnnotationsTransformer.transform(tree).tree

# Generated at 2022-06-14 02:35:56.197883
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    '''
    shows that a: int = 10 and b: int will be removed from file after
    transformation

    '''
    x = """ """
    VariablesAnnotationsTransformer.transform(x)

# Generated at 2022-06-14 02:36:04.334499
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:36:08.849758
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Given
    input_src = """
    x: int = 3
"""
    # When
    result, no_changes = VariablesAnnotationsTransformer.transform(input_src)

    # Then
    assert no_changes == False


if __name__ == '__main__':
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:36:16.396250
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.AnnAssign(annotation=ast.Name(id='int'),
                    target=ast.Name(id='a'),
                    value=ast.Num(n=10))
    assert node.__class__.__name__ == 'AnnAssign'
    expected_result = ast.Assign(targets=[ast.Name(id='a')],
                                 value=ast.Num(n=10))
    assert VariablesAnnotationsTransformer.transform(node).tree == expected_result


# Generated at 2022-06-14 02:36:26.687749
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import get_node
    from ..exceptions import NodeNotFound
    from test_definitions import define_tests_for

    class TestDefinition:
        def __init__(self, target_code: str, expected_code: str):
            self.target_code = target_code
            self.expected_code = expected_code

    def test_target(test_case: TestDefinition):
        tree = get_node(test_case.target_code)
        _, tree_changed, _ = VariablesAnnotationsTransformer.transform(tree)
        assert tree_changed is True

# Generated at 2022-06-14 02:36:33.429922
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..types import TransformationError
    from ..utils.ast_factory import generate_ast
    from ..utils.helpers_test import str_ast
    import inspect

    # Test for constructor with inherits from base class
    try:
        assert issubclass(VariablesAnnotationsTransformer, BaseTransformer)
    except AssertionError:
        print("Fail to test constructor of class VariablesAnnotationsTransformer - inherits from base class")

    # Test for constructor with correct attributes
    try:
        assert VariablesAnnotationsTransformer.target == (3,5)
    except AssertionError:
        print("Fail to test constructor of class VariablesAnnotationsTransformer - correct attributes")

    # Test for constructor with correct variables annotations