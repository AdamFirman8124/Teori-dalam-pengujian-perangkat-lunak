

# Generated at 2022-06-14 02:28:08.466869
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .transformations_factory import transformations_factory
    from textwrap import dedent

    code = dedent('''
    def foo(a: int = 10, b: int):
        print(a)
        print(b)
    ''')

    tree = ast.parse(code)
    t = transformations_factory(3.5)
    new_tree = t(tree)

    expected = dedent('''
    def foo(a: int, b: int):
        a = 10
        print(a)
        print(b)
    ''')

    assert ast.dump(new_tree) == ast.dump(ast.parse(expected))



# Generated at 2022-06-14 02:28:10.552361
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse("a : int = 10", '', 'exec')).tree.body[0].value.n == 10

# Generated at 2022-06-14 02:28:15.404857
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Compiles:
        a: int = 10
        b: int
    To:
        a = 10

    """
    import typed_ast.ast3
    VariablesAnnotationsTransformer.transform(typed_ast.ast3.parse("a: int = 10\nb: int"))

# Generated at 2022-06-14 02:28:17.657034
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:28:29.195054
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()), annotation = ast.Name(id='int', ctx=ast.Load()), value = ast.Constant(value=10, kind=None), simple=1)
    b = ast.AnnAssign(target=ast.Name(id='b', ctx=ast.Store()), annotation = ast.Name(id='int', ctx=ast.Load()), value=None, simple=1)

    body = ast.Module(body=[a, b])
    input_code_tree = body

# Generated at 2022-06-14 02:28:37.610514
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.parse import parse_ast
    node = parse_ast("a: int = 10\n"
                     "b: int")
    tree = node.body[0]
    assert type(tree) is ast.AnnAssign
    assert tree.target.id == 'a'
    assert tree.annotation.id == 'int'
    assert type(tree.value) is ast.Num
    assert tree.value.n == 10
    assert type(tree.target) is ast.Name
    assert type(tree.target) is ast.Name
    assert type(tree.annotation) is ast.Name
    assert tree.value.n == 10
    assert type(tree.value) is ast.Num

# Generated at 2022-06-14 02:28:50.695757
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import typed_ast.ast3 as ast
    ast1=ast.parse('''
    a: int
    b: int
    ''')
    ast2=ast.parse('''
    a: int = 10
    b: int
    ''')
    tree1=ast1.body
    tree2=ast2.body
    variables_annotations_transformer1 = VariablesAnnotationsTransformer()
    variables_annotations_transformer2 = VariablesAnnotationsTransformer()
    result1=variables_annotations_transformer1.transform(tree1)
    result2=variables_annotations_transformer2.transform(tree2)
    assert(result1.tree == tree1)
    assert(result2.tree == tree1)
    assert(result1.tree_changed == False)

# Generated at 2022-06-14 02:28:56.698964
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3
    with open("VariablesAnnotationsTransformer", 'w') as file:
        file.write(str(ast.parse("a: int = 10; b: int", mode='single')))
    with open('VariablesAnnotationsTransformer', 'r') as file:
        node = ast.parse(file.read(), mode='single')
    VariablesAnnotationsTransformer.transform(node)
    with open("VariablesAnnotationsTransformer", 'w') as file:
        file.write(str(node))
    with open('VariablesAnnotationsTransformer', 'r') as file:
        node = ast.parse(file.read(), mode='single')
    assert isinstance(node, ast3.Module)
    assert isinstance(node.body[0], ast3.Assign)

# Generated at 2022-06-14 02:29:06.250425
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import parse

    sample_source = """
        def f(a: int, b: int) -> int:
           a: str = b
           b: str
           return a
        """
    expected_source = """
        def f(a, b) -> int:
           a = b
           return a
        """

    sample = parse(sample_source)
    result = VariablesAnnotationsTransformer.transform(sample)
    expected = parse(expected_source)
    assert result.tree == expected

    sample_source = """
        a: str = 'a'
        """
    expected_source = """
        a = 'a'
        """

    sample = parse(sample_source)
    result = VariablesAnnotationsTransformer.transform(sample)
    expected = parse(expected_source)

# Generated at 2022-06-14 02:29:15.021012
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    #print("Testing class VariablesAnnotationsTransformer")

    transformer = VariablesAnnotationsTransformer()
    assert transformer.target == (3, 5)

    result = transformer.transform(ast.parse("""
    a: int = 10
    b: int
    """))
    tree = result.tree
    assert str(tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=10)), AnnAssign(target=Name(id='b', ctx=Store()), annotation=Name(id='int', ctx=Load()), value=None, simple=1)])"

# Generated at 2022-06-14 02:29:25.827659
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typing import List
    from ..utils.helpers import create_module

    def assert_transform(code: str, expected_code: str):
        tree = create_module(code)
        res = VariablesAnnotationsTransformer.transform(tree)
        assert res.transformed_tree.as_string() == expected_code

    assert_transform('a: int\n', '\n')
    assert_transform('a: int = 10\n', 'a = 10\n')
    assert_transform('def fn():\n    a: int\n', 'def fn():\n    pass\n')
    assert_transform('def fn():\n    a: int = 10\n', 'def fn():\n    a = 10\n')

# Generated at 2022-06-14 02:29:32.303879
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = 5
    b = 7
    c = 8
    VariablesAnnotationsTransformer(3, 5)
    tree = ast.parse('''if True:
                        a: int = 10
                        b: int
                        ''')
    expected = ast.parse('''if True:
                        a = 10
                        b: int
                        ''')
    assert (VariablesAnnotationsTransformer.transform(tree)) == expected

# Generated at 2022-06-14 02:29:36.817098
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    params = '''
    a:int
    b:int
    '''
    expected_output = '''
    a
    b
    '''
    tree = ast.parse(params)
    assert ast.dump(tree) == ast.dump(ast.parse(expected_output))

# Generated at 2022-06-14 02:29:41.506559
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.parse("a: int = 10\nb: int")
    node2 = ast.parse("a = 10")
    expected_result = TransformationResult(node2, True, [])
    actual_result = VariablesAnnotationsTransformer.transform(node)
    assert actual_result == expected_result
    actual_result == expected_result

# Generated at 2022-06-14 02:29:47.913475
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    transformer = VariablesAnnotationsTransformer()
    tree = ast.parse('''
a: int = 10
b: int
    ''')

    expected = ast.parse('''
a = 10
    ''')

    result = transformer.transform(tree)
    assert result.tree == expected
    assert result.tree_changed == True
    assert result.messages == []

# Generated at 2022-06-14 02:29:52.116090
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    test_tree = ast.parse("""b: int = 0""")
    res = VariablesAnnotationsTransformer.transform(test_tree)
    assert str(res.tree)==str(ast.parse("""b = 0"""))

# Generated at 2022-06-14 02:30:05.965749
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils import get_ast

    code = 'a: str = "#"\n' \
           'b: int\n' \
           'c: str\n' \
           'd: str\n' \
           'e: int\n'

    tree = get_ast(code)
    out_tree = VariablesAnnotationsTransformer.transform(tree)
    assert len(out_tree.body) == 3
    assert out_tree.body[0].value.s == '#'
    assert type(out_tree.body[0]) == ast.Assign
    assert out_tree.body[1].value is None
    assert type(out_tree.body[1]) == ast.Assign
    assert out_tree.body[2].value is None
    assert type(out_tree.body[2]) == ast

# Generated at 2022-06-14 02:30:15.365314
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()), annotation=ast.Name(id='int', ctx=ast.Load()), value=ast.Constant(value=10, kind=None))
    parent = ast.Module(body=[node])
    index = 0
    assert type(VariablesAnnotationsTransformer.transform(parent)) is TransformationResult
    # assert VariablesAnnotationsTransformer.transform(parent) == (ast.Module(body=[ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Constant(value=10, kind=None), type_comment=ast.Name(id='int', ctx=ast.Load()))]), True, [])

# Generated at 2022-06-14 02:30:18.058434
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    v = VariablesAnnotationsTransformer()
    assert v.target == (3, 5)
    assert_equal(v.transform(0, 0), (0, 0))

# Generated at 2022-06-14 02:30:26.140833
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Testing transformation method
    from typed_ast import ast3
    from ..transformers.variables_annotations import VariablesAnnotationsTransformer
    tree = ast3.AnnAssign(target=ast3.Name(id='a', ctx=ast3.Store()), annotation=ast3.Name(id='int', ctx=ast3.Load()), value=10)
    transformation_result = VariablesAnnotationsTransformer.transform(tree)
    assert(transformation_result.tree == ast3.Assign(targets=[ast3.Name(id='a', ctx=ast3.Store())], value=10, type_comment=ast3.Name(id='int', ctx=ast3.Load())))

# Generated at 2022-06-14 02:30:38.180438
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Unit test for constructor of class VariablesAnnotationsTransformer"""
    assert issubclass(VariablesAnnotationsTransformer, BaseTransformer)



# Generated at 2022-06-14 02:30:41.358622
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.testing import get_test_case_as_tree, get_tree_string_after_transformation
    test_class = VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:30:45.003125
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse('a : int')) == \
        TransformationResult([],False,[])


# Generated at 2022-06-14 02:30:51.921935
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Instance creation
    instance = VariablesAnnotationsTransformer()

    # Attributes
    assert instance.target == (3, 5)
    # Since there are no class attributes, the count is one less than the number of attributes in the object
    assert instance.__dict__.__len__() == (instance.__class__.__dict__.__len__() - 1)

    # Methods
    assert callable(instance.transform)


# Generated at 2022-06-14 02:31:00.226200
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""a: int = 10""", mode='exec')

    new_tree = VariablesAnnotationsTransformer.transform(tree).tree
    assert isinstance(new_tree, ast.Module)
    assert isinstance(new_tree.body[0], ast.Assign)
    assert isinstance(new_tree.body[0].targets[0], ast.Name)
    assert new_tree.body[0].targets[0].id == 'a'
    assert isinstance(new_tree.body[0].value, ast.Num)
    assert new_tree.body[0].value.n == 10

# Generated at 2022-06-14 02:31:05.099486
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = '''
    a: int = 10
    b: int
    '''

    expected_output = '''
    a = 10
    '''

    tree = ast.parse(code)
    res = VariablesAnnotationsTransformer().transform(tree)
    assert res.tree_changed == True
    print(ast.dump(res.tree))
    assert ast.dump(res.tree) == expected_output

# Generated at 2022-06-14 02:31:09.859406
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse("a: int = 10", mode="eval")) == None
    assert VariablesAnnotationsTransformer.transform(ast.parse("b: int", mode="eval")) == None
    assert VariablesAnnotationsTransformer.transform(ast.parse("a = 10", mode="eval")) == None

# Generated at 2022-06-14 02:31:15.904579
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseTransformerTest
    class Test(BaseTransformerTest):
        target_class = VariablesAnnotationsTransformer

    Test.test_on_module(
        code="""
        a: int = 10),
        b: int
        """,
        expected_code="""
        a = 10
        """,
    )

# Generated at 2022-06-14 02:31:18.120445
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()
    assert t.target == (3, 5)


# Generated at 2022-06-14 02:31:28.084142
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    variable1=ast.AnnAssign(
        target=ast.Name(id='a', ctx=ast.Store()),
        annotation=ast.Name(id='int', ctx=ast.Load()),
        value=ast.Num(n=10),
        simple=1
    )

    transformation_result = VariablesAnnotationsTransformer.transform(
        variable1)
    
    expected_annotation=ast.Assign(
        targets=[ast.Name(id='a', ctx=ast.Store())], 
        value=ast.Num(n=10),
        type_comment=ast.Name(id='int', ctx=ast.Load())
    )

    assert(transformation_result.tree==expected_annotation)
    assert(transformation_result.tree_changed==True)

# Generated at 2022-06-14 02:31:41.238294
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    test_tree = ast.parse("a: int\nb: str = 'hello'")
    expected_tree = ast.parse("a\nb = 'hello'")
    result_tree, changed, messages = VariablesAnnotationsTransformer.transform(test_tree)
    assert ast.dump(expected_tree) == ast.dump(result_tree)
    assert changed

# Generated at 2022-06-14 02:31:44.627427
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from . import run_transformer_test
    run_transformer_test(VariablesAnnotationsTransformer, 'test_data/test_variables_annotations')

# Generated at 2022-06-14 02:31:47.402126
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test the constructor.
    transformer = VariablesAnnotationsTransformer()
    assert(transformer.target == (3, 5))

# Generated at 2022-06-14 02:31:56.577071
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    nodeA = ast.AnnAssign(target=ast.Name(id="a"), annotation=ast.Name(id="int"), value=ast.Num(n=10))
    nodeB = ast.AnnAssign(target=ast.Name(id="b"), annotation=ast.Name(id="int"))
    nodeC = ast.AnnAssign(target=ast.Name(id="c"), annotation=ast.Name(id="int"), value=ast.Num(n=10))

    nodeD = ast.AnnAssign(target=ast.Name(id="d"), annotation=ast.Name(id="int"))
    nodeE = ast.AnnAssign(target=ast.Name(id="e"), annotation=ast.Name(id="int"))

# Generated at 2022-06-14 02:32:05.410036
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .test_helpers import build_and_assert_tree
    import typed_ast.ast3 as ast
    from .test_helpers import compare_source

    code = """
a: int = 10
b: int
"""
    module = build_and_assert_tree(code, VariablesAnnotationsTransformer)
    assert len(module.body) == 2
    assert isinstance(module.body[0], ast.Assign)  # type: ignore
    compare_source(module, code)

# Generated at 2022-06-14 02:32:12.500879
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    ex1 = '''
a: int = 10
b: int
'''

    result1 = '''
a = 10
'''

    ex2 = '''
a: int = 10
b: int
'''

    result2 = '''
a = 10
'''

    to_test = [
        (ex1, result1),
        (ex2, result2),
    ]

    failures = []

    for (ex, result) in to_test:
        if not check_transformer(VariablesAnnotationsTransformer, ex, result):
            failures.append(ex)

    if failures:
        raise AssertionError('Failures: {}'.format(failures))



# Generated at 2022-06-14 02:32:14.052111
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:32:19.451310
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import parse
    from .helpers import should_transform_to

    code = '''
        a: int = 10
        b: float
    '''

    tree = parse(code)
    VariablesAnnotationsTransformer.transform(tree)
    expected_tree = parse('''
        a = 10

    ''')
    should_transform_to(tree, expected_tree)


# Generated at 2022-06-14 02:32:24.853825
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 10')
    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.tree.body[0].targets[0].id == 'a'
    assert result.tree.body[0].value.n == 10

# Generated at 2022-06-14 02:32:37.842808
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    cases = [
        ('a: int = 10\nb: int', 'a = 10'),
        ('a: int = 10\nb: int\nd: int', 'a = 10'),
        ('a: int = 10\nb: int\nd: int\n', 'a = 10'),
        ('a: int\n', 'a = None'),
        ('a: int', 'a = None'),
    ]
    for code, code_result in cases:
        tree = ast.parse(code)
        transformed_tree = VariablesAnnotationsTransformer.transform(tree)
        transformed_code = astor.to_source(transformed_tree.tree).strip()
        assert transformed_code == code_result

# Generated at 2022-06-14 02:32:59.174844
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast

    test_code = """
    a: int = 10
    b: int
    """
    test_tree = ast.parse(test_code)
    res, changed, err = VariablesAnnotationsTransformer.transform(test_tree)
    assert changed is True
    assert err == []

# Generated at 2022-06-14 02:33:00.988393
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()
    assert(t.target == (3, 5))

# Generated at 2022-06-14 02:33:08.860456
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # a: int = 10
    test_input = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()), annotation=ast.Name(id='int', ctx=ast.Load()), value=ast.Num(n=10), simple=1)
    # a = 10
    expected_result = ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Num(n=10), type_comment=ast.Name(id='int', ctx=ast.Load()))
    assert VariablesAnnotationsTransformer.transform(test_input) == (expected_result)

# Generated at 2022-06-14 02:33:13.166740
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """
    Test that VariablesAnnotationsTransformer can create object
    """
    try:
        VariablesAnnotationsTransformer()
    except:
        pytest.fail("VariablesAnnotationsTransformer constructor failed")


# Generated at 2022-06-14 02:33:15.466828
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer


# Generated at 2022-06-14 02:33:19.169344
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """
    VariablesAnnotationsTransformer class contains one method transform
    """
    transformer = VariablesAnnotationsTransformer()
    assert callable(transformer.transform.__func__)

# Generated at 2022-06-14 02:33:29.321030
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
        a: int = 10
        b: int

        def foo():
            c: int = 10
    """
    tree = ast.parse(code)
    res = VariablesAnnotationsTransformer.transform(tree)

    assert res.changed
    assert len(res.warnings) == 1

# Generated at 2022-06-14 02:33:39.494352
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .testutils import transform_and_reload_module
    from .testutils import get_all_nodes_by_type

    module = '''
a: int = 10
b: int
    '''
    tree = ast.parse(module)
    
    # no annotation transformed
    tree = VariablesAnnotationsTransformer.transform(tree)
    tree = transform_and_reload_module(tree)
    assert get_all_nodes_by_type(tree, ast.AnnAssign) == []

    # annotation transformed
    tree, tree_changed, err_msg = VariablesAnnotationsTransformer.transform(tree)
    assert tree_changed == True
    assert err_msg == []

    tree = transform_and_reload_module(tree)


# Generated at 2022-06-14 02:33:46.024875
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""
        def func(x: int) -> int:
            a: int = 10
            b: int
            c: int = 30
            return a + 30
    """, mode='exec')

    exp_tree = ast.parse("""
        def func(x: int) -> int:
            a = 10
            b: int
            c = 30
            return a + 30
    """, mode='exec')

    VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(tree) == ast.dump(exp_tree)

# Generated at 2022-06-14 02:33:50.762945
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print('Test VariablesAnnotationsTransformer')
    test_code = 'a: int = 10'
    test_tree = ast.parse(test_code)
    assert VariablesAnnotationsTransformer.transform(test_tree)

test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:34:14.486891
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    
    # Check that Compiles:

        # a: int = 10
        # b: int
    tree1 = ast.parse('a: int = 10\nb: int')
    # To:
    tree2 = ast.parse('a = 10')

    tree3 = VariablesAnnotationsTransformer.transform(tree1)

    assert tree2 == tree3.node

# Generated at 2022-06-14 02:34:20.734386
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils import compile_to_ast
    from ..utils.helpers import assert_equal_ast, dump_ast
    source = \
        """
        a: int = 10
        b: int
        print(a)
        """
    tree = compile_to_ast(source)
    result = VariablesAnnotationsTransformer.transform(tree)
    assert_equal_ast(result.tree,
                     """
                     a = 10
                     print(a)
                     """)
    assert result.tree_changed is True
    assert result.problems == []



# Generated at 2022-06-14 02:34:32.733550
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class Tree:
        def __init__(self, body):
            self.body = body

    class Class:
        def __init__(self, name, body):
            self.name = name
            self.body = body

    class Func:
        def __init__(self, name, body):
            self.name = name
            self.body = body

    class Assign:
        def __init__(self, target, value):
            self.target = target
            self.value = value

    class AnnAssign:
        def __init__(self, target, value):
            self.target = target
            self.value = value

    class Import:
        pass

    class Name:
        def __init__(self, s):
            self.s = s


# Generated at 2022-06-14 02:34:41.016377
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.ast_compare import ast_equal
    from typed_ast import ast3 as ast

    tree_before = ast.parse("""
        a: int = 10
        b: str
        c = 'hi'
        d: float
    """)

    tree_after = ast.parse("""
        a = 10
        c = 'hi'
    """)

    result = VariablesAnnotationsTransformer.transform(tree_before)

    assert ast_equal(tree_after, result.tree)
    assert result.tree_changed

# Generated at 2022-06-14 02:34:50.904945
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from astunparse import unparse
    from .annotations import AnnotationsTransformer

    # Declaration of VariablesAnnotationsTransformer class
    transformer_class = VariablesAnnotationsTransformer.__name__

    # Declaration of test case
    def test_case(input, output):
        """Test case for VariablesAnnotationsTransformer
        """

        # Declaration of VariablesAnnotationsTransformer
        transformer = globals()[transformer_class]()

        # Parse input
        tree_input = ast.parse(input)

        # Apply transformation on input code
        result = transformer.transform(tree_input)

        # Parse output
        tree_output = ast.parse(output)

        # Compare between the output and the transformed input

# Generated at 2022-06-14 02:35:01.206432
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    cases = {'no_annotations': ast.parse('a = 10'),
             'annotation_with_assign': ast.parse('a: int = 10'),
             'annotation_without_assign': ast.parse('a: int')}
    expected_results = {'no_annotations': ast.parse('a = 10'),
                        'annotation_with_assign': ast.parse('a = 10'),
                        'annotation_without_assign': ast.parse('a')}

    for case, expected_result in expected_results.items():
        result = VariablesAnnotationsTransformer.transform(cases[case])
        assert result.tree == expected_result

# Generated at 2022-06-14 02:35:10.038151
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import inspect
    import typed_ast.ast3 as ast
    from textwrap import dedent
    cls = VariablesAnnotationsTransformer
    filename = inspect.getfile(inspect.currentframe())
    tree = ast.parse(dedent("""\
        a: int = 10
        b: int
        """))
    tree_t, tree_changed, new_code = cls.transform(tree)
    assert tree_changed == True
    assert any(isinstance(new, ast.Assign) for new in find(tree_t, ast.AST))
    assert any(isinstance(new, ast.Expr) for new in find(tree_t, ast.AST))
    new_code_expected = dedent("""\
        a = 10
        """)
    assert new_code["code"] == new_code_expected

# Generated at 2022-06-14 02:35:15.765908
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Arrange
    from .base import BaseTransformer
    from typed_ast import ast3 as ast

    f_ast = ast.parse('a: int = 10\nb: int')
    
    # Act
    actual_result = VariablesAnnotationsTransformer.transform(f_ast)
    
    # Assert
    assert(actual_result.tree == ast.parse('a = 10'))

# Generated at 2022-06-14 02:35:28.484083
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast

    tree1 = ast.parse("a: int = 10")
    tree2 = ast.parse("b: int")

    expected_tree = ast.parse("a = 10")

    transformed_tree1, changed_tree1, *_ = VariablesAnnotationsTransformer.transform(tree1)
    transformed_tree2, changed_tree2, *_ = VariablesAnnotationsTransformer.transform(tree2)

    assert changed_tree1 and changed_tree2
    assert ast.dump(expected_tree) == ast.dump(transformed_tree1)
    assert ast.dump(transformed_tree2) == ast.dump(transformed_tree2)

# Generated at 2022-06-14 02:35:33.664489
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    strs = [
        """
assert 1 == 1
a: int = 10
        """,
        """
assert 1 == 1
a: int
        """
    ]
    ns = [
        ast.parse(s)
        for s in strs
    ]

    for n in ns:
        assert VariablesAnnotationsTransformer.transform(n).changed



# Generated at 2022-06-14 02:36:30.951137
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor
    from .VariableAnnotationsTransformer import VariableAnnotationsTransformer
    from .ImportTransformer import ImportTransformer
    from .TypeCommentTransformer import TypeCommentTransformer
    from .TypeIgnoreTransformer import TypeIgnoreTransformer
    from ..utils.helpers import recursively_replace_bin_ops

    tree = ast.parse(
    """
    def func(a: int, b: str) -> str:
        a = 10
    """)
    tree = recursively_replace_bin_ops(tree)
    test = TypeIgnoreTransformer.transform(tree)
    test = ImportTransformer.transform(test[0])
    test = TypeCommentTransformer.transform(test[0])
    test = VariableAnnotationsTransformer.transform(test[0])
    test = VariablesAnnotationsTransformer.transform

# Generated at 2022-06-14 02:36:35.261021
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    expected = ast.Module(body=[
        ast.Assign(targets=[ast.Name(id="a", ctx=ast.Store())],
                   value=ast.Num(n=10), type_comment=ast.Num(n=10))
    ])
    actual = ast.parse(
        "a: int = 10"
    )
    result = VariablesAnnotationsTransformer.transform(actual)
    assert result.tree == expected

# Generated at 2022-06-14 02:36:47.078152
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import os
    import sys
    import astor
    sys.path.append(os.path.dirname(__file__))
    from test_data.variables_annotation_test_data import test_data
    for i in test_data:
        print('Testing with: ')
        print(i[0])
        print('Expecting')
        print(i[1])
        tree = ast.parse(i[0])
        tree = VariablesAnnotationsTransformer.transform(tree)[0]
        result = astor.to_source(tree)
        print('Getting')
        print(result)
        assert result == i[1]

if __name__ == '__main__':
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:36:53.930012
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseTransformerTest
    ast_object = ast.parse("""
    a: int = 10
    b: int
    """)
    VariablesAnnotationsTransformer = VariablesAnnotationsTransformer()
    new_ast_object = VariablesAnnotationsTransformer.transform(ast_object)
    assert str(ast.dump(ast_object, include_attributes=True)) == str(ast.dump(new_ast_object, include_attributes=True))

# Generated at 2022-06-14 02:37:00.183407
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.simplify import simplify
    from typed_ast import ast3 as ast

    assert simplify(VariablesAnnotationsTransformer, """
    a: int = 10
    b: int
    """) == ast.Module(body=[ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Num(n=10), type_comment=ast.Name(id='int', ctx=ast.Load()))])

# Generated at 2022-06-14 02:37:07.592845
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast

    test_input = ast.AnnAssign(
        target=ast.Name(id='a', ctx=ast.Store()),
        annotation=ast.Name(id='int', ctx=ast.Load()),
        value=ast.Num(n=10),
    )
    expected_output = ast.Assign(
        targets=[ast.Name(id='a', ctx=ast.Store())],
        value=ast.Num(n=10),
    )
    expected_output.type_comment = ast.Name(id='int', ctx=ast.Load())

    expected = TransformationResult(expected_output, True, [])
    actual = VariablesAnnotationsTransformer.transform(test_input)
    assert actual.tree == expected.tree

# Generated at 2022-06-14 02:37:17.186843
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.tree import parse_code_to_ast
    from ..utils.ast_helpers import ast_to_str
    example_code = ("a = 10\n"
                    "b: int\n"
                    "c: str = 'Hello'")
    old_tree = parse_code_to_ast(example_code)
    new_tree = VariablesAnnotationsTransformer.transform(old_tree)

# Generated at 2022-06-14 02:37:27.893083
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor
    class_ = ast.ClassDef(name = 'Name',
                          bases = [], 
                          keywords = [], 
                          body = [
                            ast.AnnAssign(target = ast.Name(id = 'a', ctx = ast.Store()), 
                                         annotation = ast.Name(id = 'int', ctx = ast.Load()), 
                                         value = ast.Num(n = 1), 
                                         simple = 1)], 
                          decorator_list = [])


# Generated at 2022-06-14 02:37:30.827831
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = '''
from typing import List

a: List = []
    '''
    compare(VariablesAnnotationsTransformer, code, '''
from typing import List

a = []
    ''')

# Generated at 2022-06-14 02:37:33.718806
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a: int = 10
    b: int
    assert VariablesAnnotationsTransformer.transform(ast.parse('a: int = 10\n'
                                                               'b: int')).tree==ast.parse('a = 10')