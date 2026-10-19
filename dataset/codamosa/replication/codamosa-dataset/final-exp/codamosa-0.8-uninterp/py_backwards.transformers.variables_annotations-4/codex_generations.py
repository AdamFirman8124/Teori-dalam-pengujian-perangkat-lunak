

# Generated at 2022-06-14 02:27:58.613571
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Check that the constructor works as expected
    transformer = VariablesAnnotationsTransformer()
    assert transformer.target == (3, 5)


# Generated at 2022-06-14 02:28:04.775295
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 10; b: int;')
    VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(tree) == '''Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=10), type_comment=Name(id='int', ctx=Load())), Expr(value=Name(id='b', ctx=Load()))])'''

# Generated at 2022-06-14 02:28:13.246702
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = '''
        a: int = 10
        b: int
    '''
    tree = ast.parse(code)
    new_tree = VariablesAnnotationsTransformer.transform(tree)

    source = list(ast.walk(new_tree))[-1]
    assert isinstance(source, ast.Assign)
    assert isinstance(source.targets[0], ast.Name)
    assert source.targets[0].id == 'a'
    assert isinstance(source.targets[0].ctx, ast.Store)
    assert isinstance(source.value, ast.Num)
    assert source.value.n == 10

# Generated at 2022-06-14 02:28:13.880939
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:28:18.333090
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert ast.dump(VariablesAnnotationsTransformer.transform(
        ast.parse('a: int = 10')).tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=10))])"

# Generated at 2022-06-14 02:28:29.849013
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3
    from typed_ast.ast3 import parse
    import textwrap
    VariablesAnnotationsTransformer(ast3);

    var = r'''
    a: int
    b: int = 10
    '''
    expected_a = r'''
    '''
    expected_b = r'''
    b = 10
    '''
    t_var_a = parse(textwrap.dedent(var)) # type: ignore
    t_expected_a = parse(textwrap.dedent(expected_a)) # type: ignore
    t_expected_b = parse(textwrap.dedent(expected_b)) # type: ignore

    tree, tree_changed, messages = VariablesAnnotationsTransformer.transform(t_var_a)
    for message in messages:
        print(message)


# Generated at 2022-06-14 02:28:33.095032
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    p = parse("a: int = 10\nb: int")
    t = VariablesAnnotationsTransformer.transform(p)
    assert t.tree_changed
    assert t.code_changed
    assert unparse(t.tree) == 'a = 10\n'

# Generated at 2022-06-14 02:28:38.755081
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""
        a: int = 10
        b: int
    """)
    t = VariablesAnnotationsTransformer
    t.transform(tree)
    assert str(tree) == '<Module [<Assign targets=[<Name [<Name(id=a)>]>, <Name(id=__1__)>]>\n'

# Generated at 2022-06-14 02:28:41.120636
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print(VariablesAnnotationsTransformer)


# Generated at 2022-06-14 02:28:47.832705
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..tests import compose
    source = """
    def test(a: int, b: str):
        a: int = 10
        b: int = "test"
        c: int
    """
    expect = """
    def test(a: int, b: str):
        a = 10
        b = "test"
        c: int
    """
    assert compose(source, VariablesAnnotationsTransformer) == expect

# Generated at 2022-06-14 02:28:55.078403
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class_object = VariablesAnnotationsTransformer()
    assert class_object.target == (3, 5)


# Generated at 2022-06-14 02:29:02.864447
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from wabbit.transformers.variables import VariablesAnnotationsTransformer
    if VariablesAnnotationsTransformer.is_target_version((3, 7)):
        assert VariablesAnnotationsTransformer.transform(ast.Assign(targets=[ast.Name(id='foo', ctx=ast.Store())], value=None, type_comment='int')) == ast.Assign(targets=[ast.Name(id='foo', ctx=ast.Store())], value=None)

# Generated at 2022-06-14 02:29:07.218291
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a: int = 10
    b: int
    class A:
        pass

    tree = ast.parse(inspect.getsource(A))
    assert VariablesAnnotationsTransformer.transform(tree)[0] == tree

# Generated at 2022-06-14 02:29:18.289638
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from textwrap import dedent
    code = dedent('''\
        def foo() -> int:
            a: int = 10
        ''')
    tree = ast.parse(code)
    tree = VariablesAnnotationsTransformer.transform(tree)

# Generated at 2022-06-14 02:29:23.124437
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseASTNodeTransformer
    cl = VariablesAnnotationsTransformer()
    assert isinstance(cl, BaseASTNodeTransformer)
    assert cl.target == (3, 5)
    assert cl.visible_name == 'VariablesAnnotationsTransformer'


# Generated at 2022-06-14 02:29:34.557500
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import inspect
    # create an instance of class VariablesAnnotationsTransformer
    x = VariablesAnnotationsTransformer()
    # get all the properties of class VariablesAnnotationsTransformer
    print(''.join(inspect.getmembers(x, predicate=inspect.ismethod)))
    # get all the source code lines of class VariablesAnnotationsTransformer
    print(''.join(inspect.getsourcelines(x.__class__)))
    # get the source code of def transform of class VariablesAnnotationsTransformer
    print(''.join(inspect.getsourcelines(x.transform)))

# test the correctness of class VariablesAnnotationsTransformer
# if __name__ == '__main__':
#    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:29:45.167420
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a_assign_node = ast.AnnAssign(
            target=ast.Name(id='a', ctx=ast.Store()),
            annotation=ast.Name(id='int'),
            value=ast.Num(10),
            simple=1)
    b_assign_node = ast.AnnAssign(
            target=ast.Name(id='b', ctx=ast.Store()),
            annotation=ast.Name(id='int'),
            simple=1)

# Generated at 2022-06-14 02:29:54.888738
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # given
    input_code = 'from typing import List\n' \
            'def foo() -> List[int]:\n' \
            '    a: int = 10\n' \
            '    b: int\n' \
            '    return a'
    expected_code = 'from typing import List\n' \
            'def foo() -> List[int]:\n' \
            '    a = 10\n' \
            '    return a'
    # when
    actual_code = VariablesAnnotationsTransformer.run_test(input_code)
    # then
    assert actual_code == expected_code

# Generated at 2022-06-14 02:30:07.107281
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from random import randint
    from ..utils.tree import ast_to_str
    from ..exceptions import NodeNotFound

    my_ast = ast.parse('''a: int = 10
b: int''')
    expected_output = ast_to_str(ast.parse('''a = 10
'''))
    assert VariablesAnnotationsTransformer.transform(my_ast).tree_str() == expected_output

    # Test case with multiple asssignment
    my_ast = ast.parse('''a: int = 10
b: int = 5''')
    expected_output = ast_to_str(ast.parse('''a = 10
b = 5
'''))
    assert VariablesAnnotationsTransformer.transform(my_ast).tree_str() == expected_output

    # Test case where there is no annotation

# Generated at 2022-06-14 02:30:09.224394
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class_object = VariablesAnnotationsTransformer()
    assert class_object.target == (3, 5)


# Generated at 2022-06-14 02:30:27.981499
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    print("Testing VariablesAnnotationsTransformer...")
    node = [ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()),
                          annotation=ast.Name(id='int', ctx=ast.Load()),
                          value=ast.Num(n=10)),
            ast.AnnAssign(target=ast.Name(id='b', ctx=ast.Store()),
                          annotation=ast.Name(id='int', ctx=ast.Load()),
                          value=None)]

    VariablesAnnotationsTransformer.transform(node)

# Generated at 2022-06-14 02:30:36.996339
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test 1: successfully compiling function with no parameters
    node1 = ast.AnnAssign(target=ast.Name(id='t', ctx=ast.Store()),
                          annotation=ast.Name(id='int', ctx=ast.Load()),
                          value=ast.Num(n=10))
    expected_result1 = ast.Assign(targets=[ast.Name(id='t', ctx=ast.Store())],
                                  value=ast.Num(n=10),
                                  type_comment=ast.Name(id='int', ctx=ast.Load()))
    tree_changed, new_tree1 = VariablesAnnotationsTransformer.transform(node1)
    assert tree_changed
    assert new_tree1 == expected_result1

    # Test 2: successfully compiling function with no parameters
    node2

# Generated at 2022-06-14 02:30:48.020337
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .. import transform
    import typed_ast.ast3 as typed_ast

    # Given
    tree = typed_ast.parse('''
        a: int = 10
        b: int
    ''')

    # When
    VariablesAnnotationsTransformer.transform(tree)

    # Then
    assert typed_ast.dump(tree) == 'Module(body=[Assign(targets=[Name(id=\'a\', ctx=Store())], value=Constant(value=10, kind=None), type_comment=Constant(value=\'int\', kind=None)), Assign(targets=[Name(id=\'b\', ctx=Store())], value=None, type_comment=Constant(value=\'int\', kind=None))])'


# Integ test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:30:52.906441
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 10', mode='eval')
    expected_tree = ast.parse('a = 10', mode='eval')
    result_tree = VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(result_tree.tree) == ast.dump(expected_tree)



# Generated at 2022-06-14 02:30:58.055911
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..types import TransformationResult
    from ..utils.tree import get_tree

    tree = get_tree('''
        a: int = 0
    ''')

    result = VariablesAnnotationsTransformer().transform(tree)

    assert isinstance(result, TransformationResult)
    assert len(result.nodes) == 0
    assert result.tree_changed is True
    assert result.tree == get_tree('''
        a = 0
    ''')

# Generated at 2022-06-14 02:31:05.549259
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 10\nb: int')
    transformer = VariablesAnnotationsTransformer(tree)
    transformer.transform()

    assert ast.dump(tree, include_attributes=True) == \
    "Module(body=[Assign(targets=[Name(id='a', ctx=Store(), annotation=None, type_comment=' int')], value=Num(n=10), type_comment=None), Assign(targets=[Name(id='b', ctx=Store(), annotation=None, type_comment=' int')], value=None, type_comment=None)])"

# Generated at 2022-06-14 02:31:11.256244
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    trans = VariablesAnnotationsTransformer()
    node = ast.parse('a: int = 10\nb: int')
    assert isinstance(node, ast.Module)
    assert isinstance(node.body[0], ast.AnnAssign)
    node = trans.visit(node)
    assert isinstance(node, ast.Module)
    assert isinstance(node.body[0], ast.Assign)

# Generated at 2022-06-14 02:31:19.788781
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()
    assert t.transform(ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], # type: ignore
                                 value=ast.Num(n=1, ctx=ast.Load()))) ==\
           TransformationResult(ast.Assign(
            targets=[ast.Name(id='a', ctx=ast.Store())],
            value=ast.Num(n=1, ctx=ast.Load())),
            False, [])

# Generated at 2022-06-14 02:31:24.626343
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # given
    code = '''
# a: int = 10
# b: int
# '''

    # when
    result = VariablesAnnotationsTransformer.transform(parse(code))

    # then
    expect(result.tree).to(look_like("""
#
#
# '''
    """))


# Generated at 2022-06-14 02:31:32.721106
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as typed_ast
    from .utils import get_node_from_func
    from .utils import test_node_transformer
    func = '''
        def f(a: int = 10, b: int):
            pass
    '''
    node = get_node_from_func(func)
    expected_result = '''
        def f(a = 10, b):
            pass
    '''
    assert test_node_transformer(node, VariablesAnnotationsTransformer, expected_result) == 0

# Generated at 2022-06-14 02:31:56.594365
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("number: int = 5")
    transformer = VariablesAnnotationsTransformer()
    transformed_tree = transformer.transform(tree)
    assert ast.dump(tree) == 'Module(body=[AnnAssign(target=Name(id=\'number\', ctx=Store()), annotation=Name(id=\'int\', ctx=Load()), value=Num(n=5), simple=1)])'
    assert ast.dump(transformed_tree) == 'Module(body=[Assign(targets=[Name(id=\'number\', ctx=Store())], value=Num(n=5))])'


# Generated at 2022-06-14 02:32:06.412618
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'

    code_from = """
a:int = 10
b:int
"""
    code_to = """
a = 10
b = None
"""
    tree_from = ast.parse(code_from)  # parse tree
    tree_to = ast.parse(code_to)

    tree_changed, tree_new = VariablesAnnotationsTransformer.transform(tree_from).changed_and_new()
    assert tree_changed
    assert ast_equal(tree_new, tree_to)

# Generated at 2022-06-14 02:32:10.965190
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('''
a: int = 10
b: int
c: int = 20
    ''')

    expected = ast.parse('''
a = 10
b: int
c = 20
    ''')

    VariablesAnnotationsTransformer.transform(tree)

    assert ast.dump(expected) == ast.dump(tree)

# Generated at 2022-06-14 02:32:23.501387
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class1 = ast.AnnAssign(annotation = ast.Name(id = 'int',
                                                ctx = ast.Load()),
                           target = ast.Name(id = 'a',
                                            ctx = ast.Load()),
                           value = ast.Num(n = 10),
                           simple = 1)
    class2 = ast.AnnAssign(annotation = ast.Name(id = 'int',
                                                ctx = ast.Load()),
                           target = ast.Name(id = 'b',
                                            ctx = ast.Load()),
                           value = None,
                           simple = 1)

# Generated at 2022-06-14 02:32:29.055492
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    transformer = VariablesAnnotationsTransformer()
    tree = ast.parse('''x: str = 10
                          y: str''', mode='exec')
    tree_ = ast.parse('''x = 10''', mode='exec')
    tree_ = ast.fix_missing_locations(tree_)
    transformed_tree = transformer.transform(tree)
    assert transformed_tree.tree == tree_

# Generated at 2022-06-14 02:32:35.139062
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import typed_ast.ast3 as ast
    # a: int = 10
    # b: int
    tree = ast.parse("""
        a: int = 10
        b: int
    """, mode="exec")

    expected = ast.parse("""
        a = 10
    """, mode="exec")

    assert(VariablesAnnotationsTransformer.transform(tree).tree == expected)

# Generated at 2022-06-14 02:32:42.018538
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    var_annot_xpr = '''a = 10'''
    var_annot_ast = ast.parse(var_annot_xpr)
    var_annot_transformer = VariablesAnnotationsTransformer()
    var_annot_transformer.transform(var_annot_ast)
    assert str(var_annot_ast) == 'Module(body=[Assign(targets=[Name(id="a", ctx=Store())], value=Constant(value=10, kind=None), type_comment=None)])'


# Generated at 2022-06-14 02:32:44.511016
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class1 = VariablesAnnotationsTransformer()
    assert class1.target == (3, 5)


# Generated at 2022-06-14 02:32:54.713677
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.tree import get_parent_index, get_index
    from ..exceptions import NodeNotFound
    line0 = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()), annotation=ast.Name(id='int', ctx=ast.Load()),
                          value=ast.Constant(value=10, kind=None), simple=1)
    line1 = ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Constant(value=10, kind=None),
                       type_comment=ast.Name(id='int', ctx=ast.Load()))

# Generated at 2022-06-14 02:32:55.463568
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:33:42.179398
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .utils import get_transformer_and_test_results
    from ..exceptions import NodeNotFound
    from ..utils.helpers import build_comment

    node1 = ast.AnnAssign()
    node2 = ast.AnnAssign()

    node1.target = ast.Name()
    node2.target = ast.Constant()
    node1.annotation = ast.Name()
    node2.annotation = ast.Constant()
    node1.value = ast.Name()
    node2.value = ast.Constant()

    result1 = ast.Assign()
    result2 = ast.Assign()

    result1.targets = [node1.target]
    result2.targets = [node2.target]
    result1.value = node1.value
    result2.value = node

# Generated at 2022-06-14 02:33:49.506960
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import remove_whitespace

    class_ = VariablesAnnotationsTransformer

    def test(code, expected_code=None, **options):
        tree = ast.parse(remove_whitespace(code), **options)
        expected_tree = ast.parse(remove_whitespace(expected_code), **options)
        result = class_.transform(tree)

        assert result.tree == expected_tree
        assert result.tree != tree

    # test("a: int = 10", "a = 10\n")
    # test("b: int", "")
    # test("a: int = 10\nb: int", "a = 10\n")
    # test("x: int = 10\nfoo()\ny: int\nbar()\n", "x

# Generated at 2022-06-14 02:33:52.719043
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == "VariablesAnnotationsTransformer"
    assert VariablesAnnotationsTransformer.target == (3, 5)


# Generated at 2022-06-14 02:33:58.418288
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor
    test_code = '''
x: int
x = 12
'''
    tree = ast.parse(test_code)
    tree = VariablesAnnotationsTransformer.transform(tree)
    new_code = astor.to_source(tree)
    assert new_code == 'x = 12\n'

# Generated at 2022-06-14 02:33:59.468328
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # assertions
    assert(True)



# Generated at 2022-06-14 02:34:09.100714
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    transformer = VariablesAnnotationsTransformer
    target = (3, 5)
    # Node with annotation of form a: int = 10
    node = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()),
                         annotation=ast.Name(id='int', ctx=ast.Load()),
                         value=ast.Num(n=10), simple=1)
    tree = ast.parse('')
    tree.body.insert(0, node)
    transformed_tree, tree_changed, _ = transformer.transform(tree)
    assert tree_changed is True
    assert transformed_tree.body[0].__class__.__name__ == 'Assign'

# Generated at 2022-06-14 02:34:12.083019
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = "a: int = 10"
    codetree = ast.parse(code)
    assert VariablesAnnotationsTransformer.transform(codetree) is not None

# Generated at 2022-06-14 02:34:15.937205
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = 'a: int = 10\nb: int'
    expected = 'a = 10'

    tree = ast.parse(code)
    transformer = VariablesAnnotationsTransformer()
    tree_changed = transformer.transform(tree)

    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:34:21.625793
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
        a: int = 10
        b: int
    """
    # Transform code
    tree = parse(code)
    new_tree = VariablesAnnotationsTransformer.transform(tree).new_tree
    assert str(new_tree) == "a = 10"

# Generated at 2022-06-14 02:34:24.477703
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
    a: 'int' = 10
    
    b: 'int'
    """
    # Note: the code above is only valid in Python 3.6+, it is not valid in Python 3.5
    code = "a: 'int' = 10"
    module = ast.parse(code)
    tree = VariablesAnnotationsTransformer.transform(module)
    print(ast.dump(tree.tree))

# Generated at 2022-06-14 02:35:09.580191
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    assert t.__class__.__name__ == 'VariablesAnnotationsTransformer'
    assert t.target == (3, 5)

# Generated at 2022-06-14 02:35:15.344133
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .. import transform

    code = '''
    a: int = 10
    b: int
    c: int
    '''

    tree = ast.parse(code)
    VariablesAnnotationsTransformer.transform(tree)
    code2, _, _ = transform(code)
    assert code2 == '''a = 10\nc = None\n'''

# Generated at 2022-06-14 02:35:16.897144
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print(VariablesAnnotationsTransformer.transform(1))

# Generated at 2022-06-14 02:35:20.152735
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    v = VariablesAnnotationsTransformer(None)
    assert VariablesAnnotationsTransformer.target == (3, 5)
    assert v.tree is None

# Generated at 2022-06-14 02:35:29.985987
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10")
    tree = VariablesAnnotationsTransformer.transform(tree)
    assert(len(tree.body) == 1)
    assert(isinstance(tree.body[0], ast.Assign))
    assert(isinstance(tree.body[0].targets[0], ast.Name))
    assert(tree.body[0].targets[0].id == 'a')
    assert(isinstance(tree.body[0].value, ast.Num))
    assert(tree.body[0].value.n == 10)
    assert(isinstance(tree.body[0].type_comment, ast.Name))
    assert(tree.body[0].type_comment.id == 'int')


# Generated at 2022-06-14 02:35:33.544230
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from .base import compile_and_test

    code = '''
a: int = 10
b: int
    '''

    compare_code = '''
a = 10
    '''

    ast_tree = compile_and_test(code, VariablesAnnotationsTransformer)
    ast_compared = compile_and_test(compare_code, VariablesAnnotationsTransformer)
    assert ast.dump(ast_tree) == ast.dump(ast_compared)

# Generated at 2022-06-14 02:35:34.823498
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:35:43.544748
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor
    from ..utils.helpers import (
        parse_python, create_module_from_class, get_ast_representation
    )
    from typed_ast import ast3 as ast

    class TestClass:
        def __init__(self):
            self.a: int = 10
            self.b: int

        def test_method(self, a: str, b: str) -> str:
            return a + b

    module = create_module_from_class(TestClass)

    tree = parse_python(module)
    comment_nodes = find(tree, ast.Comment)
    # making sure that we don't have any comments in our tree
    assert comment_nodes == []
    # making sure that original tree contains all the annotations

# Generated at 2022-06-14 02:35:51.170605
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Load()), annotation=ast.Name(id='int', ctx=ast.Load()), value=ast.Num(n=10))
    node2 = ast.AnnAssign(target=ast.Name(id='b', ctx=ast.Load()), annotation=ast.Name(id='int', ctx=ast.Load()))
    node3 = ast.AnnAssign(target=ast.Name(id='c', ctx=ast.Load()), annotation=ast.Name(id='int', ctx=ast.Load()), value=ast.Num(n=10))
    actual = VariablesAnnotationsTransformer.transform(ast.Module(body=[node, node2, node3]))

# Generated at 2022-06-14 02:36:01.459239
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import ast
    import inspect
    import os
    import astor
    from astor.code_gen import to_source
    
    # Grab the source code of the function definition
    source = inspect.getsource(test_VariablesAnnotationsTransformer)

    # astor cannot parse the `inspect.getsource()` output due to decoding errors.
    # This fix helps astor parse the source correctly.
    # ref: https://stackoverflow.com/a/9389811/2771644
    source = os.linesep.join([s for s in source.splitlines() if s])

    # Convert the source into an AST
    tree = astor.parse_file(source)

    # Grab the function definition node for the function defined above
    func_def_node = tree.body[0]

    # Obtain source code of the

# Generated at 2022-06-14 02:37:32.112323
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.parse("""a: int = 10
    b: int
    """).body[0]
    expected_node = ast.parse("""a = 10
    """).body[0]

    actual_node = VariablesAnnotationsTransformer.transform(node)
    assert expected_node == actual_node

# Generated at 2022-06-14 02:37:41.540223
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # simple_test = ast.parse(textwrap.dedent(
    #     '''
    #     a: int = 10
    #     '''
    # ))
    # simple_test_compiled = ast.parse(textwrap.dedent(
    #     '''
    #     a = 10
    #     '''
    # ))
    simple_test = ast.parse(textwrap.dedent(
        '''
        a: int = 10
        '''
    ))
    simple_test_compiled = ast.parse(textwrap.dedent(
        '''
        a = 10
        '''
    ))
    without_value = ast.parse(textwrap.dedent(
        '''
        a: int
        '''
    ))

# Generated at 2022-06-14 02:37:46.028695
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    x = """
    a: int = 10
    b: int
    """
    expected_output = """a = 10"""
    # Creates a tree object
    tree = ast.parse(x)
    # Creates a VariablesAnnotationsTransformer object
    transform = VariablesAnnotationsTransformer()
    # Calls the transform method
    new_tree = transform.transform(tree)
    # Compares the output with the expected output
    assert ast.dump(new_tree.tree) == expected_output

# Generated at 2022-06-14 02:37:48.755003
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code_in = """
a: int = 10
b: int
"""
    code_out = """
a = 10
"""
    tree = ast.parse(code_in)
    new_tree = VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(new_tree.tree) == ast.dump(ast.parse(code_out))

# Generated at 2022-06-14 02:37:49.718700
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print(VariablesAnnotationsTransformer)

# Generated at 2022-06-14 02:37:50.588583
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:37:51.808816
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(None) is not None

# Generated at 2022-06-14 02:37:59.529721
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Given
    code_to_transform = "a: int = 10"
    expected_transformation_result = ['a = 10']

    # When
    actual_transformation_result, tree_changed = VariablesAnnotationsTransformer().transform(code_to_transform)

    # Then
    assert actual_transformation_result == expected_transformation_result

    # GIVEN
    code_to_transform = "b: int"
    expected_transformation_result = []
    # WHEN
    actual_transformation_result, tree_changed = VariablesAnnotationsTransformer().transform(code_to_transform)

    # THEN
    assert actual_transformation_result == expected_transformation_result