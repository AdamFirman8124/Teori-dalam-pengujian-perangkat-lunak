

# Generated at 2022-06-14 02:28:03.489918
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.AnnAssign()
    result = VariablesAnnotationsTransformer.transform(node)
    assert result == (node, False, [('warn', 'Assignment outside of body')])


# Generated at 2022-06-14 02:28:14.185535
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():

    class Person:
        age: int

    class ClassExample:
        def test_method(self):
            a: int = 5
            b: int
            c: int
            if True:
                d: int = 6
                e: int
            f: str = "Hi"

            def test_inner_method():
                pass

        def another_method(self):
            p: Person = Person()
            p.age = 4
            x = 4
            x: int = 5

    old_tree = ast.parse(inspect.getsource(ClassExample))
    new_tree = VariablesAnnotationsTransformer.transform(old_tree).new_tree

    old_code = inspect.getsource(ClassExample)

# Generated at 2022-06-14 02:28:23.161132
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3
    from textwrap import dedent
    from ..utils.tree import parse_to_ast
    from ..utils.helpers import hash_node

    tree = parse_to_ast(dedent("""\
        a : int = 10.0
        b : int
        """))
    expected = parse_to_ast(dedent("""\
        a = 10.0
        """))

    actual = VariablesAnnotationsTransformer().transform(tree)
    assert actual.changed
    assert hash_node(ast.Module(body=[expected])) == hash_node(actual.new_tree.body[0])

# Generated at 2022-06-14 02:28:27.513024
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print(VariablesAnnotationsTransformer.__doc__)
    t = VariablesAnnotationsTransformer()
    assert t.target == (3, 5)  # check the python version
    assert isinstance(t, BaseTransformer) # check the type
    assert t.transform # check if the method is defined


# Generated at 2022-06-14 02:28:33.454212
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('''
        a: int = 10
        b: int
    ''')

    transformer = VariablesAnnotationsTransformer()
    result = transformer.transform(tree)
    assert not result.tree_changed
    assert len(result.error_messages) == 0
    assert ast.dump(result.tree) == ast.dump(ast.parse('''
        a = 10
    '''))



# Generated at 2022-06-14 02:28:44.657964
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..exceptions import NodeNotFound
    from ..utils.tree import get_non_exp_parent_and_index

    class TestTree:
        def __init__(self):
            self.body = []

    parent = TestTree()
    parent.body.append(ast.AnnAssign(None, None, None, None))
    parent.body.append(None)

    assert len(parent.body) == 2

    try:
        get_non_exp_parent_and_index(parent, parent.body[0])
        assert False
    except NodeNotFound:
        #assert True
        pass

    parent.body[1] = ast.AnnAssign(None, None, None, None)


# Generated at 2022-06-14 02:28:50.643101
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert issubclass(VariablesAnnotationsTransformer, BaseTransformer)
    assert isinstance(VariablesAnnotationsTransformer(), BaseTransformer)
    assert VariablesAnnotationsTransformer.transform(None) is not None
    assert VariablesAnnotationsTransformer.target == (3, 5)
    print('Unit test for constructor of class VariablesAnnotationsTransformer is passed!')


# Generated at 2022-06-14 02:28:56.045548
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import node_to_string
    from textwrap import dedent

    source = dedent('''
            def func():
                a: int  = 10
                b: int  = 20
                c: int
            ''')
    tree = ast.parse(source)

    transformer = VariablesAnnotationsTransformer()  # type: ignore
    result = transformer.transform(tree)

    expected = dedent('''
            def func():
                a = 10
                b = 20
            ''')

    assert node_to_string(result.tree) == expected

# Generated at 2022-06-14 02:28:58.586997
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()
    assert isinstance(t, BaseTransformer)
    assert t.target == (3, 5)

# Generated at 2022-06-14 02:28:59.511399
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert True

# Generated at 2022-06-14 02:29:12.230698
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10\nb: int")
    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.transformed is False
    assert result.tree == ast.parse("a: int = 10\nb: int")
    assert result.messages == ['Assignment outside of body']
    tree = ast.parse("def f(a: int = 10, b: int): pass")
    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.transformed
    assert result.tree == ast.parse('def f(a: int, b): pass')
    assert result.messages == []
    tree = ast.parse("class C:\n a: int = 10\n b: int")
    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.transformed


# Generated at 2022-06-14 02:29:13.921469
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class_ = VariablesAnnotationsTransformer
    assert class_.target == (3, 5)



# Generated at 2022-06-14 02:29:24.685355
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import ast
    # from typed_ast import ast3 as typed_ast
    from ast_pprint import pprint as pp
    from ..utils.tree import find


# Generated at 2022-06-14 02:29:36.145932
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():

    # Test simple cases
    for tree in [ast.parse(code) for code in [
        'a: int = 10',
        'b: int',
    ]]:
        res = VariablesAnnotationsTransformer().transform(tree)
        assert res.changed
        assert not res.errors
        assert isinstance(res.tree.body[0], ast.Assign)

    # Test with multiple assignments
    tree = ast.parse('a: int = 10; b: int; c: int = 20')
    res = VariablesAnnotationsTransformer().transform(tree)
    assert res.changed
    assert not res.errors
    assert len(res.tree.body) == 2
    assert isinstance(res.tree.body[0], ast.Assign)
    assert isinstance(res.tree.body[1], ast.Assign)



# Generated at 2022-06-14 02:29:46.546300
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import inspect
    import os
    import sys
    import unittest

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)

    from typed_ast import ast3 as ast

    # Simple test case
    tree = ast.parse('a: int = 10')
    tree_changed = VariablesAnnotationsTransformer.transform(tree).tree_changed
    assert tree_changed

    tree = ast.parse('a: int = 10')
    tree_changed = VariablesAnnotationsTransformer.transform(tree).tree_changed
    assert tree_changed

    tree = ast.parse('a: int')
    tree_changed = VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:29:47.731072
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert(VariablesAnnotationsTransformer(3, 5))

# Generated at 2022-06-14 02:29:52.408209
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
  code = 'a: int = 10\nb: int'
  expected = 'a = 10'

  tree = ast3.parse(code)
  tree = VariablesAnnotationsTransformer.transform(tree)
  assert ast3.dump(tree.tree) == expected



# Generated at 2022-06-14 02:29:58.567991
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Given
    class_to_test = VariablesAnnotationsTransformer()

    # When
    transformationResult = class_to_test.transform()

    # Then
    assert transformationResult.source_code == ""
    assert transformationResult.transformed_source_code == ""
    assert transformationResult.tree is None
    assert transformationResult.tree_has_changed is False

# Generated at 2022-06-14 02:30:04.991189
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.ast_helpers import ast_from_str
    from .utils import assert_transformation_result

    source = """
    a: int = 10
    b: str
    """
    expected = """
    a = 10
    """
    tree = ast_from_str(source)
    result = VariablesAnnotationsTransformer.transform(tree)
    assert_transformation_result(result, expected)

# Generated at 2022-06-14 02:30:08.849949
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    v = VariablesAnnotationsTransformer(ast.AnnAssign, ast.Assign)
    assert v.tree == ast.AnnAssign
    assert v.new_tree == ast.Assign

if __name__ == '__main__':
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:30:14.966953
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:30:23.919505
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    test1 = ast.parse("a: int = 10\nb: int")
    test2 = ast.parse("abc: int = 10")
    test3 = ast.parse("abc: int")
    test4 = ast.parse("b: int\nc: int")
    assert VariablesAnnotationsTransformer.transform(test1) == (test1, True, [])
    assert VariablesAnnotationsTransformer.transform(test2) == (test2, True, [])
    assert VariablesAnnotationsTransformer.transform(test3) == (test3, True, [])
    assert VariablesAnnotationsTransformer.transform(test4) == (test4, True, [])

# Generated at 2022-06-14 02:30:26.256328
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    transpiler = VariablesAnnotationsTransformer()
    assert(transpiler.target == (3, 5))
    assert(isinstance(transpiler, BaseTransformer))

# Generated at 2022-06-14 02:30:27.452518
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform

# Generated at 2022-06-14 02:30:29.978216
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('x: int')
    tree = VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(tree.ast) == "Module(body=[])"

# Generated at 2022-06-14 02:30:31.375587
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # If a: int = 10 is given
    # Then a = 10
    pass

# Generated at 2022-06-14 02:30:37.195135
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    for v in [ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()),
                            annotation=ast.Name(id='int', ctx=ast.Load()),
                            value=ast.Num(n=10),
                            simple=1)]:
        a = VariablesAnnotationsTransformer(None)
        b = a.transform(v)
        assert b
        print(ast.dump(v))

# Generated at 2022-06-14 02:30:39.419264
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import roundtrip

# Generated at 2022-06-14 02:30:47.285999
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """
    Unit test for class VariablesAnnotationsTransformer
    """
    print("\nUnit test for class VariablesAnnotationsTransformer")
    print("===================================================")
    test_text = """a: int = 10
    b: int"""
    expected_text = """a = 10"""
    test_ast = astor.parse_string(test_text)
    tools = VariablesAnnotationsTransformer.transform(test_ast)
    node = tools[0]
    assert(str(node) == expected_text)
    print("The test is successful!")

# test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:30:54.573391
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a: int = 10
    b: int
    from ..utils.helpers import parse_ast, compare
    from ..visitors import get_visitor_class

    ts = VariablesAnnotationsTransformer()

    expected = '''
a = 10

'''
    compare(ts.transform(parse_ast(a)), expected)

    expected = '''

'''
    compare(ts.transform(parse_ast(b)), expected)

    print("Test passed!")

# unit test get_non_exp_parent_and_index

# Generated at 2022-06-14 02:31:08.931907
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.source import source_to_nodes

    source = '''
    a: int = 10
    b: int
    '''
    result = source_to_nodes(source)
    print(result)
    tree = result[0]
    assert len(VariablesAnnotationsTransformer.transform(tree).tree.body) == 2

test_VariablesAnnotationsTransformer.venv = 'py3'

# Generated at 2022-06-14 02:31:14.905009
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Unit test for constructor of class VariablesAnnotationsTransformer"""
    tree = ast.parse("""c: str = 'hello'\nd: str""")
    expected_tree = ast.parse("""c = 'hello'\nd: str""")
    actual_tree,_,_ = VariablesAnnotationsTransformer.transform(tree)
    assert EqualAst(actual_tree, expected_tree)

# Generated at 2022-06-14 02:31:19.470375
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    d = "a: int = 10"
    tree_changed, _, new_code = \
        VariablesAnnotationsTransformer.transform(ast.parse(d))
    assert tree_changed
    assert new_code == 'a = 10'
    print(new_code)

# Generated at 2022-06-14 02:31:24.136046
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import parse

    found = VariablesAnnotationsTransformer.transform(parse("a: int = 10"))
    assert found.tree.body[0].value == 10
    assert isinstance(found.tree.body[0], ast.Assign)
    assert not found.tree_changed


# Generated at 2022-06-14 02:31:26.662533
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import ast
    # Building AST
    A = ast.AnnAssign()
    B = ast.AnnAssign()
    C = ast.AnnAssign()
    D = ast.AnnAssign()
    E = ast.AnnAssign()
    F = ast.AnnAssign()
    G = ast.Module([A,B,C,D,E,F])
    # Checking type
    assert isinstance(VariablesAnnotationsTransformer(), VariablesAnnotationsTransformer)
    # Testing functionality
    assert VariablesAnnotationsTransformer.transform(G) == ([B, D, F], True, [])

# Generated at 2022-06-14 02:31:39.041127
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    #testing with fully annotated variable
    test_node_1 = ast.AnnAssign(
        target=ast.Name(id='a', ctx=ast.Store()),
        annotation=ast.Name(id='int', ctx=ast.Load()),
        value=ast.Num(n=10)
    )

    #testing with partially annotated variable
    test_node_2 = ast.AnnAssign(
        target=ast.Name(id='b', ctx=ast.Store()),
        annotation=ast.Name(id='int', ctx=ast.Load()),
        value=None
    )


# Generated at 2022-06-14 02:31:51.191199
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """
    Unit test for constructor of class VariablesAnnotationsTransformer
    """
    import ast
    import types
    from python_ta.transforms.type_annotation import VariablesAnnotationsTransformer
    from python_ta.transforms.type_annotation import TransformationResult
    from python_ta.transforms.type_annotation import NodeNotFound
    from ..utils.tree import find, get_non_exp_parent_and_index, insert_at

    # Unit test for constructor of class VariablesAnnotationsTransformer
    def test_VariablesAnnotationsTransformer():
        """
        Unit test for constructor of class VariablesAnnotationsTransformer
        """
        import ast
        import types
        from python_ta.transforms.type_annotation import VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:31:52.342251
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.ast_builder import build_ast

# Generated at 2022-06-14 02:31:54.969901
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .test_helpers import compare_source
    from .testcode.var_annotations import testcode

    tree = ast.parse(testcode)
    tree = VariablesAnnotationsTransformer.transform(tree)
    compare_source(tree, testcode)

# Generated at 2022-06-14 02:32:08.011835
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    #x: int = 10
    #y: int
    tree = ast.Module(
        body=[
            ast.AnnAssign(
                target=ast.Name(
                    id="x",
                    ctx=ast.Store()
                ),
                annotation=ast.Name(
                    id="int",
                    ctx=ast.Load()
                ),
                value=ast.Num(n=10),
                simple=1
            ),
            ast.AnnAssign(
                target=ast.Name(
                    id="y",
                    ctx=ast.Store()
                ),
                annotation=ast.Name(
                    id="int",
                    ctx=ast.Load()
                ),
                simple=1
            )
        ]
    )

    #x = 10
    #y = None

# Generated at 2022-06-14 02:32:26.752456
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'

# Generated at 2022-06-14 02:32:35.145173
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.tree import test_tree_equality
    from ..utils.helpers import get_python_source

    source = get_python_source("""
    a: int = 10
    b: int
    """)

    tree = ast.parse(source)
    tree_changed = VariablesAnnotationsTransformer.transform(tree)
    expected_source = get_python_source("""
    a = 10
    """)
    test_tree_equality(expected_source, tree_changed)

# Generated at 2022-06-14 02:32:38.407614
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10")
    t = VariablesAnnotationsTransformer.transform(tree)
    assert t.modified
    assert t.code == "a = 10"

# Generated at 2022-06-14 02:32:39.467133
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
  t = VariablesAnnotationsTransformer()
  print(t)

# Generated at 2022-06-14 02:32:44.414092
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.parse('a: int = 10\nb: int')
    expected_node = ast.parse('a = 10')

    tree, tree_changed, debug = VariablesAnnotationsTransformer.transform(node)
    assert tree_changed
    print(ast.dump(tree) == ast.dump(expected_node))
    print(debug)

# Generated at 2022-06-14 02:32:54.655521
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import dump_tree
    from .. import single_dispatch

    src = """
    class foo:
        def __init__(self):
            self.foo:int = 10
            self.bar:int
        @single_dispatch
        def run(self):
            self.foo:int = 10
            self.bar:int
    """
    expected = """
    class foo:
        def __init__(self):
            self.foo = 10
            self.bar
        @single_dispatch
        def run(self):
            self.foo = 10
            self.bar
    """
    indented_expected = dedent(expected).strip()
    data = single_dispatch(src)
    result = data.run(ast)
    assert result == indented_expected

# Generated at 2022-06-14 02:32:56.284450
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
  class_variables_annotations_transformer_var = VariablesAnnotationsTransformer()
  assert class_variables_annotations_transformer_var.target == (3, 5)

# Generated at 2022-06-14 02:32:57.806360
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert isinstance(VariablesAnnotationsTransformer(), VariablesAnnotationsTransformer)

# Generated at 2022-06-14 02:33:08.109123
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    input = """
    def a(a: int = 10, b: int):
        return a
"""
    t = VariablesAnnotationsTransformer()
    result = t.transform(ast.parse(input))
    output = ast.dump(result.tree)
    expected = """
Module(body=[FunctionDef(name='a', args=arguments(args=[arg(arg='a', annotation=Constant(value=10), type_comment=Constant(value=int)), arg(arg='b', annotation=Constant(value=int), type_comment=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Return(value=Name(id='a', ctx=Load()))], decorator_list=[], returns=None)])
"""

# Generated at 2022-06-14 02:33:13.967416
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""def f():
    a: int = 10
    b: int
    c = a""")

    # Verify the VariablesAnnotationsTransformer constructor's return value
    assert VariablesAnnotationsTransformer.transform(tree).node == ast.parse("""def f():
    a = 10
    b
    c = a""")

# Generated at 2022-06-14 02:33:56.040771
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils import testing

    tree = testing.parse('''
        x: int
        x: int
        x: int = 10
    ''')

    result = VariablesAnnotationsTransformer.transform(tree)

    assert str(result.tree).strip() == '''
        x: int
        x: int
        x = 10
    '''.strip()

    assert result.tree_changed

    assert not result.changes

# Generated at 2022-06-14 02:33:57.590918
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import typing as t
    

# Generated at 2022-06-14 02:34:02.626535
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """
    Given:
        i:int = 10
    When:
        I construct a VariablesAnnotationsTransfomer()
    Then:
        I should see the following annotations:
            [<_ast.AnnAssign object at 0x0000026CB9C864E0>]
    """
    tree = ast.parse('i:int = 10')
    transformer = VariablesAnnotationsTransformer(tree)
    assert len(transformer.annotations) == 1
    assert transformer.annotations[0].lineno == 1
    assert transformer.annotations[0].col_offset == 0


# Generated at 2022-06-14 02:34:08.090485
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():

    # Creating an instance of class VariablesAnnotationsTransformer
    VariablesAnnotationsTransformer = VariablesAnnotationsTransformer(None)

    # Creating a tree like the one that is used in the transform method
    tree = ast.parse("""a: int = 10
        b: int """)

    VariablesAnnotationsTransformer.transform(tree)

# Generated at 2022-06-14 02:34:18.130122
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree1 = ast.parse("x:int=5")
    tree2 = ast.parse("def main():\n    x:int=5\n")
    res1 = VariablesAnnotationsTransformer.transform(tree1)
    res2 = VariablesAnnotationsTransformer.transform(tree2)
    i1 = str(res1.new_tree)
    i2 = str(res2.new_tree)

# Generated at 2022-06-14 02:34:26.476615
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import typed_ast.ast3 as ast
    
    # Source code
    src = '''
b: int = 10
    '''
    mod = ast.parse(src)
    c = VariablesAnnotationsTransformer()
    result = c.transform(mod)
    expected_src = '''
b = 10
    '''
    assert ast.dump(result.tree) == ast.dump(ast.parse(expected_src))

# Generated at 2022-06-14 02:34:31.215039
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = ast.parse("a: int = 10")
    b = ast.parse("b: int")
    c = ast.parse("return a")

    result = VariablesAnnotationsTransformer.transform(a)
    assert result.tree == ast.parse("a=10")

    result = VariablesAnnotationsTransformer.transform(b)
    assert result.tree == ast.parse("return a")

    result = VariablesAnnotationsTransformer.transform(c)
    assert result.tree == c

# Generated at 2022-06-14 02:34:33.320967
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
  test_VariablesAnnotationsTransformer = VariablesAnnotationsTransformer()
  assert(test_VariablesAnnotationsTransformer.target == (3,5))

# Generated at 2022-06-14 02:34:45.348327
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Arrange
    variant_name = "VariablesAnnotationsTransformer"
    node = ast.parse("a: int = 10")
    expected_changed_tree = ast.parse("a = 10")
    node_to_remove = node.body[0]
    changed_tree = copy.deepcopy(node)
    # changed_tree.body.remove(node_to_remove)
    # changed_tree.body.extend([node_to_remove.value])
    # for item in changed_tree.body:
    # 	if isinstance(item, ast.Expr):
    # 		changed_tree.body.remove(item)
    # changed_tree.body.append(item)
    # Act
    actual = VariablesAnnotationsTransformer.transform(tree=node)

# Generated at 2022-06-14 02:34:49.166516
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import get_ast 
    from ..utils.tree import to_code 
    import ast
    tree = get_ast("""a: int = 2""")
    VariablesAnnotationsTransformer.transform(tree)
    assert to_code(tree) == """a = 2"""

    tree = get_ast("""
        def x():
            a: int = 2
    """)
    VariablesAnnotationsTransformer.transform(tree)

# Generated at 2022-06-14 02:36:15.409794
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:36:21.330984
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils import parse_code_to_ast

    tree = parse_code_to_ast("""\
    a: int = 10
    b: int
    """)
    expected_tree = parse_code_to_ast("""\
    a = 10
    """)
    assert VariablesAnnotationsTransformer.transform(tree) == \
            TransformationResult(expected_tree, True, [])

# Generated at 2022-06-14 02:36:23.048664
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10\nb: int")
    VariablesAnnotationsTransformer.transform(tree)

# Generated at 2022-06-14 02:36:24.446943
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    v = VariablesAnnotationsTransformer()
    assert v.target == (3, 5)


# Generated at 2022-06-14 02:36:30.233303
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .test_base import compile_func, check_source

    source = '''
        def foo():
            i: int = 10
            j: str
    '''

    result = compile_func(source, VariablesAnnotationsTransformer)
    check_source(result, '''
        def foo():
            i = 10
            j = None
    ''')

# Generated at 2022-06-14 02:36:33.608048
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    test_tree = ast.parse("""
a: int = 10
b: int
    """)
    expected_tree = ast.parse("""
a = 10
b: int
    """)

    t = VariablesAnnotationsTransformer()
    t.transform(test_tree)

# Generated at 2022-06-14 02:36:46.919420
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('''
a: int = 10
b:int
''')

    tree_changed = False

    for node in find(tree, ast.AnnAssign):
        try:
            parent, index = get_non_exp_parent_and_index(tree, node)
        except NodeNotFound:
            warn('Assignment outside of body')
            continue

        tree_changed = True
        parent.body.pop(index)  # type: ignore

        if node.value is not None:
            insert_at(index, parent,
                      ast.Assign(targets=[node.target],  # type: ignore
                                 value=node.value,
                                 type_comment=node.annotation))

    print(ast.dump(tree, include_attributes=True))
    print(tree_changed)

# Generated at 2022-06-14 02:36:50.976388
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import ast
    assert ast.dump(VariablesAnnotationsTransformer.transform(ast.parse('''
a:str = 1
b:str = 2
''')).tree)==ast.dump(ast.parse('''
a=1
b=2
'''))


# Generated at 2022-06-14 02:36:56.313489
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    input_code = """
        def test_func(): 
            a: int = 10
            b: int
    """
    expected_code = """
        def test_func(): 
            a = 10
    """
    tr = VariablesAnnotationsTransformer()
    tree = ast.parse(input_code)
    tr.transform(tree)
    assert ast.dump(tree) == expected_code

# Generated at 2022-06-14 02:36:59.604531
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    transform = VariablesAnnotationsTransformer.transform
    a = ast.parse('a: int = 10\nb: int')
    b = ast.parse('a = 10')
    assert transform(a) == transform(b)