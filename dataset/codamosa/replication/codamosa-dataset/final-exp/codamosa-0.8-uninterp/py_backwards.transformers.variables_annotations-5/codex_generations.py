

# Generated at 2022-06-14 02:28:02.871120
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # given
    transformer = VariablesAnnotationsTransformer()

    # when

# Generated at 2022-06-14 02:28:04.654856
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == "VariablesAnnotationsTransformer"

# Generated at 2022-06-14 02:28:11.010984
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.testing import fix, evaluate
    from typed_ast import ast3 as ast
    node = ast.AnnAssign(target=ast.Name(id='b', ctx=ast.Store()),
                         annotation=ast.Name(id='int', ctx=ast.Load()),
                         value=None)
    assert evaluate(fix(node, VariablesAnnotationsTransformer)) == fix(node, VariablesAnnotationsTransformer)

# Generated at 2022-06-14 02:28:14.536515
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 10')
    tree2 = ast.parse('a: int')
    VariablesAnnotationsTransformer.transform(tree)
    VariablesAnnotationsTransformer.transform(tree2)

# Generated at 2022-06-14 02:28:17.136859
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    v = VariablesAnnotationsTransformer()
    assert v.__class__.__name__ == "VariablesAnnotationsTransformer"


# Generated at 2022-06-14 02:28:18.747745
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()
    assert(t.transform(ast.AnnAssign()) == ast.Assign())

# Generated at 2022-06-14 02:28:26.818598
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.source import source_to_node
    from ..utils.compare import compare_ast

    source = """
    from typing import Optional
    def foo():
        a: int = 10
        b: int
    """
    expected = """
    from typing import Optional
    def foo():
        a = 10
    """
    node = source_to_node(source)

    VariablesAnnotationsTransformer.transform(node)

    result = compare_ast(node, expected)
    assert result is True, result

# Generated at 2022-06-14 02:28:31.302078
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..test_utils import get_node
    x = get_node('a: str = 10', 3)
    assert isinstance(x, ast.AnnAssign)
    x = get_node('a: str = 10', 3)
    assert isinstance(x, ast.AnnAssign)

# Generated at 2022-06-14 02:28:37.625292
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3
    import copy

    tree = ast3.parse("""a: int = 10
                          b: int""", mode='exec')

    expected_tree = ast3.parse("""a = 10
                                        b: int""", mode='exec')


    tr = VariablesAnnotationsTransformer()
    actual_tree = tr.transform(copy.deepcopy(tree))
    assert actual_tree.tree == expected_tree

# Generated at 2022-06-14 02:28:50.694365
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # a: int = 10
    test_case = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()),
                              annotation=ast.Name(id='int', ctx=ast.Load()),
                              value=ast.Num(n=10), eq='=')
    # Generate an AST of the code above
    test_tree = ast.parse(
        textwrap.dedent(inspect.getsource(test_case.__class__))
    )

    assert isinstance(test_tree, ast.Module)
    assert len(test_tree.body) == 1
    assert isinstance(test_tree.body[0], ast.AnnAssign)

    # VariablesAnnotationsTransformer can be created
    transformer = VariablesAnnotationsTransformer()

    # transform() can be called

# Generated at 2022-06-14 02:28:58.884801
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree1 = ast.parse(u'x: int = 10').body[0]
    tree2 = ast.parse(u'x = 10').body[0]
    assert isinstance(tree1, ast.AnnAssign)
    assert isinstance(tree2, ast.Assign)
    assert VariablesAnnotationsTransformer.transform(tree1) == (tree2, True, [])

# Generated at 2022-06-14 02:29:01.903908
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    p = VariablesAnnotationsTransformer()
    assert p.target == (3, 5), 'should be (3, 5)'

# Generated at 2022-06-14 02:29:03.596374
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(None) == None

# Generated at 2022-06-14 02:29:08.782096
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print("VariablesAnnotationsTransformer")
    
    # Test case 1: check the constructor
    var_annotations = VariablesAnnotationsTransformer()

    assert var_annotations.target == (3, 5)


# Generated at 2022-06-14 02:29:16.895731
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor
    import ast
    # a class that is used to test constructor
    class Node:
        def __init__(self, value, type_comment):
            self.value = value
            self.type_comment = type_comment

    the_ast = ast.Assign(targets=[Node(1, 1)], value=1, type_comment=1)
    the_tree = tree(the_ast)
    compiler = VariablesAnnotationsTransformer()
    new_the_tree = compiler.transform(the_tree)
    print(astor.to_source(tree(new_the_tree)))

# Generated at 2022-06-14 02:29:22.437857
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    test_input = ast.parse('''
a: int = 10
b: int
''')
    test_output = ast.parse('''
a = 10
''')
    assert VariablesAnnotationsTransformer.transform(test_input).tree == test_output

# Generated at 2022-06-14 02:29:24.346683
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == "VariablesAnnotationsTransformer"

# Generated at 2022-06-14 02:29:30.464142
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.testing import render_assert_same
    # Test with type annotation
    code = """
        a: int = 10
    """
    render_assert_same(VariablesAnnotationsTransformer, code, code)

    # Test without type annotation
    code = """
        a = 10
    """
    render_assert_same(VariablesAnnotationsTransformer, code, code)

# Generated at 2022-06-14 02:29:35.077328
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class_info = VariablesAnnotationsTransformer
    class_name = "VariablesAnnotationsTransformer"
    assert class_info.__name__ == class_name, "Name of class should be " + class_name + " but found " + \
                                              class_info.__name__



# Generated at 2022-06-14 02:29:37.284840
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseTransformer


# Generated at 2022-06-14 02:29:47.435771
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast

    class Dummy:
        pass
    dummy_transformer = Dummy()
    dummy_transformer.target = (3,5)
    dummy_transformer.transform = VariablesAnnotationsTransformer.transform

# Generated at 2022-06-14 02:29:49.130504
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    VariablesAnnotationsTransformer.transform(ast.parse('a : int = 10'))

# Generated at 2022-06-14 02:29:54.928375
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = ast.parse("a: int = 10")
    tr = VariablesAnnotationsTransformer.transform(a)
    assert(tr.changed)
    b = ast.parse("a = 10")
    assert(ast.dump(tr.tree, include_attributes=False) == ast.dump(b, include_attributes=False))
    assert(tr.has_warnings == False)

# Generated at 2022-06-14 02:29:57.662529
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:29:59.602939
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:30:00.903290
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:30:05.550004
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import ast as py_ast
    from .utils import compare_asts
    from .test_FunctionAnnotationsTransformer import dummy_func_annotations

    print("Test 1")

# Generated at 2022-06-14 02:30:09.965094
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""
    def f(a: int = 0, b: int = 1):
        c = 2  # type: int
        d: str
        a
        b
        c
    """)
    VariablesAnnotationsTransformer.transform(tree)
    print(ast.dump(tree, include_attributes=True))

# Generated at 2022-06-14 02:30:17.869920
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
        a = ast.Assign(targets=[ast.Name(id="a", ctx=ast.Store())], value=ast.Constant(value=10, kind=None), type_comment="int")
        b = ast.Assign(targets=[ast.Name(id="b", ctx=ast.Store())], value=None, type_comment="int")
        tree = ast.Module(body=[
            a,
            b
        ])

        result = VariablesAnnotationsTransformer.transform(tree)
        assert result.tree is not None
        assert result.tree_changed is True
        assert result.messages is not None

# Generated at 2022-06-14 02:30:27.123714
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Compiles:
    # a: int = 10
    # b: int
    # To:
    # a = 10

    source = ast.parse("a: int = 10\nb: int", mode="exec")
    expected = ast.parse("a = 10", mode="exec")
    actual = VariablesAnnotationsTransformer.transform(source).new_tree
    assert ast.dump(actual) == ast.dump(expected)

    # Compiles:
    # def test_func(f: int = 10, g: int = 20, h: int = 30, i: int = 40):
    #     print(i)
    # To:
    # def test_func(f = 10, g = 20, h = 30, i = 40):
    #     print(i)


# Generated at 2022-06-14 02:30:38.326658
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    p = VariablesAnnotationsTransformer()
    assert p.target == (3, 5)

# Generated at 2022-06-14 02:30:43.099565
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test for constructor of class VariablesAnnotationsTransformer
    input_code = '''\
a: int = 10
b: int
'''
    expected_code = '''\
a = 10
'''
    output_code = VariablesAnnotationsTransformer.transform(input_code)
    assert output_code == expected_code

# Generated at 2022-06-14 02:30:44.712639
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3

# Generated at 2022-06-14 02:30:50.738599
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('''
a: int = 10
b: int
''')
    old_tree = copy.deepcopy(tree)
    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.tree == old_tree
    assert result.tree_changed == True
    assert result.errors == []

# Expected output
'''
'''

# Generated at 2022-06-14 02:30:53.498026
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = open('./examples/variable_annotations.py').read()
    tree = ast.parse(code)
    tree = VariablesAnnotationsTransformer.transform(tree).tree

# Generated at 2022-06-14 02:31:04.953397
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse('a: int = 10')
    variables_annotations_transformer = VariablesAnnotationsTransformer()
    result = variables_annotations_transformer.transform(tree)
    assert result.was_transformed is True
    assert result.tree_changed is True
    assert result.log.size == 0
    assert str(result.tree) == 'Assign(targets=[Name(id=\'a\', ctx=Store())], value=Num(n=10), type_comment=\'int\')'
    tree = ast.parse('b: int')
    result = variables_annotations_transformer.transform(tree)
    assert result.was_transformed is True
    assert result.tree_changed is False
    assert result.log.size == 1

# Generated at 2022-06-14 02:31:09.433853
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    input = """
        a: int = 10
        b: int
        """
    expected_output = """
        a = 10
        """
    tree = ast_parse(input)
    t = VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(t.tree) == expected_output

# Generated at 2022-06-14 02:31:10.722936
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    pass


# Generated at 2022-06-14 02:31:19.641083
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # create an instance of the class
    instance = VariablesAnnotationsTransformer()
    # type of the instance
    instance_type = type(instance)
    # type of the class
    class_type = VariablesAnnotationsTransformer
    # print(instance)
    # print(instance_type)
    # print(class_type)
    if instance_type == class_type:
        print('PASSED: test of constructor for class VariablesAnnotationsTransformer')
    else:
        print('FAILED: test of constructor for class VariablesAnnotationsTransformer')


# Generated at 2022-06-14 02:31:24.382063
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.test_utils import assert_transformation
    assert_transformation(VariablesAnnotationsTransformer,
                          'a: str = b',
                          '(a = b)')
"""
    assert_transformation(VariablesAnnotationsTransformer,
                          'a: str\nb: str',
                          '')
"""

# Generated at 2022-06-14 02:31:54.043369
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import assert_transform
    from ..utils.helpers import assert_source_equal
    assert_transform(VariablesAnnotationsTransformer,
                     # source
                     'a: int = 10',
                     # expected_ast
                     'a = 10',
                     # expected_source
                     'a: int = 10',
                     )
    assert_transform(VariablesAnnotationsTransformer,
                     # source
                     'a: int\n'
                     'a = 10',
                     # expected_ast
                     'a = 10',
                     # expected_source
                     'a: int\n'
                     'a = 10',
                     )

# Generated at 2022-06-14 02:32:02.034934
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = '''def f(a ,b, c:int = 10, d:int, e:int = 11) -> int: a:str = 'a'\nb:str = 'b'\nc:str = 'c'\nd:str = 'd'\ne:str = 'e'\nf:str = 'f'\ng:str = 'g'\nh:str = 'h'\ni:str = 'i'\nreturn c'''

# Generated at 2022-06-14 02:32:09.342924
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    with open('tests/data/typed_ast/annotations.py', 'rb') as source:
        tree = ast.parse(source.read())

    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.tree.body[0].type_comment is None
    assert result.tree.body[0].value.elts[0].type_comment is None
    assert result.tree.body[1].type_comment is None

# Generated at 2022-06-14 02:32:10.842593
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'


# Generated at 2022-06-14 02:32:14.110892
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'
    assert callable(VariablesAnnotationsTransformer)

# Generated at 2022-06-14 02:32:20.671824
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():

    class testVariablesAnnotationsTransformer(VariablesAnnotationsTransformer):
        """Dummy class"""
    testTree = ast.parse('a: int = 10')
    resultTree, treeChanged, linenos = testVariablesAnnotationsTransformer.transform(testTree)
    assert treeChanged == True
    assert linenos == []
    assert isinstance(resultTree.body[0], ast.Assign)

# Generated at 2022-06-14 02:32:26.556261
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..parser.decorators import CliDecorator, CliFunction
    from ..parser.extractor import extract_clis


# Generated at 2022-06-14 02:32:33.136307
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node_for_test = ast.AnnAssign(target=ast.Name('a', ast.Load()),
                                  annotation=ast.Name('int', ast.Load()),
                                  value=ast.Num(10),
                                  simple=1)
    assert isinstance(VariablesAnnotationsTransformer.transform(node_for_test),
                      TransformationResult)

# Generated at 2022-06-14 02:32:37.654508
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer(2, 3).version == (2, 3)
    # __doc__ would return None if there were no docstring
    assert VariablesAnnotationsTransformer.__doc__ is not None
    assert VariablesAnnotationsTransformer.transform.__doc__ is not None



# Generated at 2022-06-14 02:32:40.267559
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert issubclass(VariablesAnnotationsTransformer, BaseTransformer)
    assert VariablesAnnotationsTransformer.__name__ == "VariablesAnnotationsTransformer"


# Generated at 2022-06-14 02:33:19.844826
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('s = [1, 2, 3]')
    transformer = VariablesAnnotationsTransformer()
    assert transformer.tree_changed == False
    assert transformer.result == None


# Generated at 2022-06-14 02:33:23.950996
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Tests method transform of class VariablesAnnotationsTransformer"""
    code = "a: int = 10\nb: str"
    expected_code = "a = 10\n"
    src = ast.parse(code)
    res, _ = VariablesAnnotationsTransformer.transform(src)
    assert astor.to_source(res) == expected_code

# Generated at 2022-06-14 02:33:26.285773
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor

# Generated at 2022-06-14 02:33:31.339009
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
        a: int = 10
        b: int
    """

    tree = ast.parse(code)
    tree_new = VariablesAnnotationsTransformer.transform(tree)

    expected_code = """
        a = 10
    """

    assert ast.dump(tree_new.tree, annotate_fields=False, include_attributes=False) == expected_code


# Generated at 2022-06-14 02:33:37.616976
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.tree import parse
    from ..utils.helpers import get_node
    from .. import TransformationResult

    code = '''
    a: int = 10
    b: int
    '''

    tree = parse(code)
    result = VariablesAnnotationsTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert get_node(result.tree, ast.Assign)



# Generated at 2022-06-14 02:33:46.988839
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # create instance of class
    transformer = VariablesAnnotationsTransformer()
    # create class used in testing
    class Foo():
        def __init__(self):
            self.c: int = 10
            self.a = 10
            self.b: int

    # pass class to the tranform method of class
    result = transformer.transform(ast.parse(inspect.getsource(Foo)))
    # check if instance variables have been removed
    assert(result.tree_changed)
    # create a new tree with the old variable annotated
    tree = ast.AnnAssign(target=ast.Name(id="c", ctx=ast.Store()), annotation=ast.parse("int").body[0].value, value=ast.Num(10), simple=1)
    # insert that tree into the result

# Generated at 2022-06-14 02:33:59.620080
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Create a variable type annotation
    variable_annotate = ast.AnnAssign(target=ast.Name(id="a", ctx=ast.Store()),
                                      annotation=ast.Name(id="int", ctx=ast.Load()),
                                      value=ast.Num(n=10),
                                      simple=1)
    # Create a tree with variable type annotation
    tree = ast.Module(body=[variable_annotate])

    # Create an instance of VariablesAnnotationsTransformer
    t = VariablesAnnotationsTransformer()

    # Use VariablesAnnotationsTransformer to transform the tree
    TRANS = t.transform(tree)
    # Get the tree after transformation
    transformed_tree = TRANS.new_tree
    # Get the body of the transformed tree
    transformed_tree_body = transformed_tree.body
    # Get the

# Generated at 2022-06-14 02:34:03.410156
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    '''
    Tests the constructor of class VariablesAnnotationsTransformer.
    '''
    # Case 1: instance of class VariablesAnnotationsTransformer
    assert isinstance(VariablesAnnotationsTransformer(), VariablesAnnotationsTransformer)


# Generated at 2022-06-14 02:34:04.580206
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:34:06.972576
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Unit test for constructor of class VariablesAnnotationsTransformer"""
    assert VariablesAnnotationsTransformer.__name__ == "VariablesAnnotationsTransformer"

# Generated at 2022-06-14 02:35:26.102338
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    pass

# Generated at 2022-06-14 02:35:35.970040
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test case 1:
    # Example tree:
    # (Module(
    #     body=[
    #         AnnAssign(
    #             target=Name(id='a', ctx=Store()),
    #             annotation=Name(id='int', ctx=Load()),
    #             value=Num(n=10))
    #     ])
    # )
    example_tree = ast.parse('''
a: int = 10
''')
    transformed_tree = VariablesAnnotationsTransformer.transform(example_tree)
    assert len(transformed_tree.nodes) == 1
    assert isinstance(transformed_tree.nodes[0], ast.Assign)
    assert isinstance(transformed_tree.nodes[0].value, ast.Num)

# Generated at 2022-06-14 02:35:36.739450
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:35:40.019596
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == "VariablesAnnotationsTransformer"
    assert VariablesAnnotationsTransformer.transform.__name__ == "transform"
    assert VariablesAnnotationsTransformer.target == (3,5)

# Generated at 2022-06-14 02:35:48.238269
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # generate AST:
    #     a: int = 10
    #     b: int
    node_a = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()), annotation=ast.Name(id='int'), value=ast.Num(10))
    node_b = ast.AnnAssign(target=ast.Name(id='b', ctx=ast.Store()), annotation=ast.Name(id='int'))
    tree = ast.Module(body=[node_a, node_b])

    # expected AST:
    #     a = 10
    expected_node_a = ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Num(10), type_comment='int')

# Generated at 2022-06-14 02:35:53.130660
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:35:57.192452
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Creating the transformer:
    transformer = VariablesAnnotationsTransformer()
    assert transformer.target == (3, 5)
    assert transformer.transform("print('Hello World')") == TransformationResult(tree="print('Hello World')", tree_changed=False, deltas=[])

# Generated at 2022-06-14 02:36:03.250760
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import inspect
    import ast

    src = inspect.getsource(test_VariablesAnnotationsTransformer)
    src_ast = ast.parse(src)

    new_tree = VariablesAnnotationsTransformer.transform(src_ast).tree

    assert type(new_tree.body[1].value.body[3].value) == ast.Assign
    assert new_tree.body[1].value.body[3].value.targets[0].id == 'b'
    assert type(new_tree.body[1].value.body[4].value) == ast.AnnAssign

# Generated at 2022-06-14 02:36:10.167068
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from unittest import TestCase, main
    from ..utils.tree import tree_to_str

    class TestTransform(TestCase):
        def test_remove_type_annotations(self):
            expected_result = tree_to_str(ast.parse('a = 10'))
            tree = ast.parse('a: int = 10')
            actual_result = tree_to_str(VariablesAnnotationsTransformer.transform(tree).tree)
            self.assertEqual(expected_result, actual_result)

    main()



# Generated at 2022-06-14 02:36:16.585810
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.testing import get_test_case_as_nodes, assert_equal_trees

    tree = get_test_case_as_nodes('variable_annotations', 3, 5)
    expected_tree = get_test_case_as_nodes('variable_annotations', 3, 6)

    assert_equal_trees(VariablesAnnotationsTransformer.transform(tree).tree, expected_tree)